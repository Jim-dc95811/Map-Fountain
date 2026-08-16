#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import hashlib
import ipaddress
import math
import os
from pathlib import Path
import socket
import ssl
import subprocess
import sys
import sqlite3
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

WEBMERC_HALF = 20037508.342789244
WEBMERC_RES0 = 156543.03392804097
OGC_PIXEL_SIZE_M = 0.00028
DEFAULT_PORT = 8088

def discover_usb_tether_ipv4():
    """Return IPv4 addresses bound specifically to a Windows Remote NDIS tether adapter."""
    if os.name != "nt":
        return []
    ps = r"""
$adapters = Get-NetAdapter -ErrorAction SilentlyContinue |
  Where-Object { $_.InterfaceDescription -like '*Remote NDIS*' -and $_.Status -eq 'Up' }
foreach ($a in $adapters) {
  Get-NetIPAddress -InterfaceIndex $a.ifIndex -AddressFamily IPv4 -ErrorAction SilentlyContinue |
    Where-Object { $_.IPAddress -notlike '169.254.*' } |
    ForEach-Object { "$($a.InterfaceDescription)|$($_.IPAddress)" }
}
"""
    try:
        cp = subprocess.run(
            ["powershell.exe", "-NoProfile", "-Command", ps],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
            timeout=10, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
        )
        out = []
        for raw in (cp.stdout or "").splitlines():
            raw = raw.strip()
            if "|" not in raw:
                continue
            desc, ip = raw.rsplit("|", 1)
            try:
                ipaddress.ip_address(ip.strip())
            except Exception:
                continue
            out.append((desc.strip(), ip.strip()))
        return out
    except Exception:
        return []

def discover_ipv4():
    found = []
    probes = [("8.8.8.8", 80), ("1.1.1.1", 80), ("192.168.42.129", 80)]
    for host, port in probes:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect((host, port))
            ip = s.getsockname()[0]
            if ip and ip not in found and not ip.startswith("127."):
                found.append(ip)
        except OSError:
            pass
        finally:
            s.close()
    try:
        for info in socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET):
            ip = info[4][0]
            if ip and ip not in found and not ip.startswith("127."):
                found.append(ip)
    except OSError:
        pass
    def rank(ip):
        try:
            a = ipaddress.ip_address(ip)
            return (0 if a.is_private else 1, 0 if not a.is_link_local else 1, ip)
        except Exception:
            return (2, 2, ip)
    return sorted(found, key=rank)

class MBTiles:
    def __init__(self, path: Path):
        self.path = path.resolve()
        uri = self.path.as_uri() + "?mode=ro"
        con = sqlite3.connect(uri, uri=True)
        try:
            self.metadata = dict(con.execute("SELECT name,value FROM metadata"))
            row = con.execute("SELECT COUNT(*), MIN(zoom_level), MAX(zoom_level) FROM tiles").fetchone()
            self.tile_count = int(row[0] or 0)
            self.minzoom = int(row[1] if row[1] is not None else self.metadata.get("minzoom", 0))
            self.maxzoom = int(row[2] if row[2] is not None else self.metadata.get("maxzoom", 18))
            cols = {r[1] for r in con.execute("PRAGMA table_info(tiles)")}
            required = {"zoom_level","tile_column","tile_row","tile_data"}
            if not required.issubset(cols):
                raise RuntimeError("Not a standard raster MBTiles tiles table.")
            sample = con.execute("SELECT tile_data FROM tiles LIMIT 1").fetchone()
            if not sample:
                raise RuntimeError("MBTiles contains no tiles.")
            sig = bytes(sample[0][:8])
            if sig.startswith(b"\x89PNG\r\n\x1a\n"):
                self.mime = "image/png"
                self.ext = "png"
            elif sig[:2] == b"\xff\xd8":
                self.mime = "image/jpeg"
                self.ext = "jpg"
            else:
                raise RuntimeError("Test server supports PNG/JPEG raster MBTiles only.")
        finally:
            con.close()

        self.name = self.metadata.get("name") or self.path.stem
        self.bounds = self._parse_bounds(self.metadata.get("bounds"))
        st = self.path.stat()
        identity = f"{self.path}|{st.st_size}|{st.st_mtime_ns}".encode("utf-8", "surrogatepass")
        self.service_id = hashlib.sha256(identity).hexdigest()[:16]

    @staticmethod
    def _parse_bounds(value):
        if not value:
            return (-180.0, -85.05112878, 180.0, 85.05112878)
        try:
            a = [float(x.strip()) for x in value.split(",")]
            if len(a) == 4:
                return tuple(a)
        except Exception:
            pass
        return (-180.0, -85.05112878, 180.0, 85.05112878)

    def get_xyz(self, z: int, x: int, y: int):
        tms_y = (1 << z) - 1 - y
        uri = self.path.as_uri() + "?mode=ro"
        con = sqlite3.connect(uri, uri=True)
        try:
            row = con.execute(
                "SELECT tile_data FROM tiles WHERE zoom_level=? AND tile_column=? AND tile_row=?",
                (z, x, tms_y),
            ).fetchone()
            return bytes(row[0]) if row else None
        finally:
            con.close()

def xml_escape(s):
    return html.escape(str(s), quote=True)

def capabilities(base_url: str, mb: MBTiles):
    west, south, east, north = mb.bounds
    matrices = []
    for z in range(mb.minzoom, mb.maxzoom + 1):
        scale = (WEBMERC_RES0 / (2 ** z)) / OGC_PIXEL_SIZE_M
        n = 2 ** z
        matrices.append(f'''
        <TileMatrix>
          <ows:Identifier>{z}</ows:Identifier>
          <ScaleDenominator>{scale:.12f}</ScaleDenominator>
          <TopLeftCorner>{-WEBMERC_HALF:.12f} {WEBMERC_HALF:.12f}</TopLeftCorner>
          <TileWidth>256</TileWidth>
          <TileHeight>256</TileHeight>
          <MatrixWidth>{n}</MatrixWidth>
          <MatrixHeight>{n}</MatrixHeight>
        </TileMatrix>''')
    matrices_text = "".join(matrices)
    template = f"{base_url}/wmts/tiles/{mb.service_id}/GoogleMapsCompatible/{{TileMatrix}}/{{TileRow}}/{{TileCol}}.{mb.ext}"
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<Capabilities xmlns="http://www.opengis.net/wmts/1.0"
 xmlns:ows="http://www.opengis.net/ows/1.1"
 xmlns:xlink="http://www.w3.org/1999/xlink"
 version="1.0.0">
 <ows:ServiceIdentification>
   <ows:Title>Rasta Map Fountain {mb.service_id}</ows:Title>
   <ows:ServiceType>OGC WMTS</ows:ServiceType>
   <ows:ServiceTypeVersion>1.0.0</ows:ServiceTypeVersion>
 </ows:ServiceIdentification>
 <ows:OperationsMetadata>
   <ows:Operation name="GetCapabilities">
     <ows:DCP><ows:HTTP><ows:Get xlink:href="{xml_escape(base_url)}/wmts?"/></ows:HTTP></ows:DCP>
   </ows:Operation>
   <ows:Operation name="GetTile">
     <ows:DCP><ows:HTTP><ows:Get xlink:href="{xml_escape(base_url)}/wmts?"/></ows:HTTP></ows:DCP>
   </ows:Operation>
 </ows:OperationsMetadata>
 <Contents>
   <Layer>
     <ows:Title>{xml_escape(mb.name)}</ows:Title>
     <ows:Identifier>rasta-{mb.service_id}</ows:Identifier>
     <ows:WGS84BoundingBox>
       <ows:LowerCorner>{west:.12f} {south:.12f}</ows:LowerCorner>
       <ows:UpperCorner>{east:.12f} {north:.12f}</ows:UpperCorner>
     </ows:WGS84BoundingBox>
     <Style isDefault="true"><ows:Identifier>default</ows:Identifier></Style>
     <Format>{mb.mime}</Format>
     <TileMatrixSetLink><TileMatrixSet>GoogleMapsCompatible</TileMatrixSet></TileMatrixSetLink>
     <ResourceURL format="{mb.mime}" resourceType="tile"
       template="{xml_escape(template)}"/>
   </Layer>
   <TileMatrixSet>
     <ows:Identifier>GoogleMapsCompatible</ows:Identifier>
     <ows:SupportedCRS>urn:ogc:def:crs:EPSG::3857</ows:SupportedCRS>
     {matrices_text}
   </TileMatrixSet>
 </Contents>
</Capabilities>'''

class Server(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True

class Handler(BaseHTTPRequestHandler):
    server_version = "RastaMapFountain/0.2.1"

    def log_message(self, fmt, *args):
        print("[HTTP]", self.address_string(), "-", fmt % args)

    def _send(self, status, body=b"", content_type="text/plain; charset=utf-8"):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        mb = self.server.mb
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        q = {k.lower(): v[-1] for k, v in urllib.parse.parse_qs(parsed.query).items()}
        host = self.headers.get("Host") or f"127.0.0.1:{self.server.server_port}"
        scheme = "https" if getattr(self.server, "is_https", False) else "http"
        base = f"{scheme}://{host}"

        if path in ("/", "/health"):
            caps = f"{base}/wmts?SERVICE=WMTS&REQUEST=GetCapabilities&MAP={mb.service_id}"
            page = f'''<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Rasta USB WMTS Test</title></head><body style="font-family:system-ui;margin:2em">
<h1>Rasta USB WMTS Test</h1>
<p><b>SERVER OK</b></p>
<p>Map: {html.escape(mb.name)}<br>Tiles: {mb.tile_count:,}<br>Zooms: Z{mb.minzoom}–Z{mb.maxzoom}<br>Format: {mb.mime}</p>
<p>WMTS GetCapabilities:</p><p style="word-break:break-all"><code>{html.escape(caps)}</code></p>
<p>If you can see this page in the Android browser over USB tethering, checkpoint 1 is PASS.</p>
</body></html>'''
            return self._send(200, page, "text/html; charset=utf-8")

        if path == "/wmts":
            req = q.get("request", "").lower()
            service = q.get("service", "").lower()
            if req == "getcapabilities" or (not req and service == "wmts"):
                return self._send(200, capabilities(base, mb), "application/xml; charset=utf-8")
            if req == "gettile":
                try:
                    z = int(q.get("tilematrix", ""))
                    x = int(q.get("tilecol", ""))
                    y = int(q.get("tilerow", ""))
                except Exception:
                    return self._send(400, "Bad GetTile coordinates")
                data = mb.get_xyz(z, x, y)
                return self._send(200, data, mb.mime) if data else self._send(404, "Tile not found")
            return self._send(400, "Use REQUEST=GetCapabilities or REQUEST=GetTile")

        parts = path.strip("/").split("/")
        if len(parts) == 7 and parts[:2] == ["wmts", "tiles"]:
            token = parts[2]
            if token != mb.service_id or parts[3] != "GoogleMapsCompatible":
                return self._send(404, "Unknown map service")
            try:
                z = int(parts[4]); y = int(parts[5]); x = int(parts[6].split(".")[0])
            except Exception:
                return self._send(400, "Bad tile path")
            data = mb.get_xyz(z, x, y)
            return self._send(200, data, mb.mime) if data else self._send(404, "Tile not found")

        if len(parts) == 4 and parts[0] == "xyz":
            try:
                z = int(parts[1]); x = int(parts[2]); y = int(parts[3].split(".")[0])
            except Exception:
                return self._send(400, "Bad XYZ path")
            data = mb.get_xyz(z, x, y)
            return self._send(200, data, mb.mime) if data else self._send(404, "Tile not found")

        return self._send(404, "Not found")

def make_qr_svg(url: str, output_path: Path) -> bool:
    """Create an offline QR SVG using the vendored python-qrcode package."""
    try:
        here = Path(__file__).resolve().parent
        vendor = here / "vendor"
        if str(vendor) not in sys.path:
            sys.path.insert(0, str(vendor))
        import qrcode
        from qrcode.image.svg import SvgPathFillImage

        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=8,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(image_factory=SvgPathFillImage)
        img.save(str(output_path))
        return output_path.is_file() and output_path.stat().st_size > 0
    except Exception as exc:
        print(f"QR generation warning: {exc}")
        return False


def preserve_live_urls(here: Path, ip: str, port: int, service_id: str, scheme: str = 'http'):
    phone_url = f"{scheme}://{ip}:{port}/"
    wmts_url = f"{scheme}://{ip}:{port}/wmts?SERVICE=WMTS&REQUEST=GetCapabilities&MAP={service_id}"

    (here / "CURRENT_PHONE_TEST_URL.txt").write_text(phone_url + "\n", encoding="utf-8")
    (here / "CURRENT_WMTS_URL.txt").write_text(wmts_url + "\n", encoding="utf-8")

    qr_path = here / "CURRENT_WMTS_QR.svg"
    qr_ok = make_qr_svg(wmts_url, qr_path)

    html_text = f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Rasta USB Map Fountain</title>
<style>
body{{font-family:Segoe UI,Arial,sans-serif;background:#f4f6f8;color:#17233a;text-align:center;margin:30px}}
.card{{max-width:760px;margin:auto;background:white;padding:28px;border-radius:14px}}
img{{width:min(70vw,520px)}}
code{{word-break:break-all;font-size:16px}}
</style>
</head>
<body>
<div class="card">
<h1>Rasta USB Map Fountain</h1>
<h2>Scan in ArcGIS Earth Mobile</h2>
{"<img src='CURRENT_WMTS_QR.svg' alt='WMTS QR code'>" if qr_ok else "<p>QR generation failed; use URL below.</p>"}
<p><code>{html.escape(wmts_url)}</code></p>
<p>USB server address: <code>{html.escape(phone_url)}</code></p>
</div>
</body>
</html>"""
    (here / "CURRENT_WMTS_QR.html").write_text(html_text, encoding="utf-8")
    return phone_url, wmts_url, qr_ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mbtiles", nargs="?", default=None)
    ap.add_argument("--port", type=int, default=8443)
    args = ap.parse_args()

    here = Path(__file__).resolve().parent
    path = Path(args.mbtiles) if args.mbtiles else sorted(here.glob("*.mbtiles"))[0]
    mb = MBTiles(path)

    tether = discover_usb_tether_ipv4()
    if not tether:
        raise SystemExit("Active Remote NDIS USB tether adapter not detected.")
    tether_desc, tether_ip = tether[0]
    expected_ip = "10.13.166.115"
    if tether_ip != expected_ip:
        raise SystemExit(
            f"This fast HTTPS build is certified for {expected_ip}, "
            f"but the current USB tether address is {tether_ip}. "
            "Send that address back and a matching build can be generated."
        )

    cert_dir = here / "HTTPS CERT"
    server_crt = cert_dir / "RASTA_USB_SERVER.crt"
    server_key = cert_dir / "RASTA_USB_SERVER.key"
    ca_der = cert_dir / "RASTA_USB_LOCAL_CA.cer"

    srv = Server(("0.0.0.0", args.port), Handler)
    srv.mb = mb
    srv.is_https = True

    tls = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    tls.minimum_version = ssl.TLSVersion.TLSv1_2
    tls.load_cert_chain(certfile=str(server_crt), keyfile=str(server_key))
    srv.socket = tls.wrap_socket(srv.socket, server_side=True)

    print()
    print("RASTA USB MAP FOUNTAIN SERVER v0.2.1 TEST")
    print("=" * 58)
    print(f"MBTiles : {mb.path}")
    print(f"Map ID  : {mb.service_id}")
    print(f"Tiles   : {mb.tile_count:,}")
    print(f"Zooms   : Z{mb.minzoom}-Z{mb.maxzoom}")
    print(f"Bounds  : {','.join(str(x) for x in mb.bounds)}")
    print()
    print("HTTPS SERVER LISTENING ON ALL PC NETWORK ADAPTERS")
    print()
    phone_url, wmts_url, qr_ok = preserve_live_urls(here, tether_ip, args.port, mb.service_id, scheme="https")
    print("USB TETHER ADAPTER DETECTED")
    print(f"  {tether_desc}")
    print(f"  PC USB IP: {tether_ip}")
    print()
    print("PHONE HTTPS TEST:")
    print(f"  {phone_url}")
    print()
    print("ARCGIS EARTH MOBILE HTTPS WMTS URL:")
    print(f"  {wmts_url}")
    print()
    print("ANDROID TRUST CERTIFICATE:")
    print(f"  {ca_der}")
    print()
    print("QR:")
    print(f"  {here / 'CURRENT_WMTS_QR.html'}")
    print("  Double-click OPEN WMTS QR.bat to display it.")
    print()
    print("Leave this window open during the test.")
    print("Press Ctrl+C to stop.")
    print("=" * 58)

    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        srv.server_close()
        print("\nServer stopped.")

if __name__ == "__main__":
    main()
