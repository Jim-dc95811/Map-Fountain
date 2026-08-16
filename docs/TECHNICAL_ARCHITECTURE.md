# Map Fountain — Technical Architecture

## Purpose

Map Fountain serves an existing raster MBTiles pyramid over a private local network using a small HTTPS WMTS service so ArcGIS Earth Mobile can request only the tiles needed for the current view.

It is a delivery system, not a renderer.

```text
QGIS / Rasta / other raster producer
        ↓
standard raster MBTiles
        ↓
Map Fountain
        ↓
HTTPS WMTS
        ↓
private transport
        ↓
ArcGIS Earth Mobile
```

The current live-proven transport is Android USB tether / Windows Remote NDIS.

---

## 1. Runtime components

Current v0.2.1 TEST source consists primarily of:

- `Map_Fountain_GUI.py` — Windows operator GUI and server process control;
- `Map_Fountain_Server.py` — MBTiles reader, WMTS capabilities generator, tile service, tether detection, HTTPS listener, QR generation;
- `START MAP FOUNTAIN.bat` — Windows launcher.

The current source was established known-good with Python 3.14.5.

The live packaged test vendored `python-qrcode` 8.2 so QR generation required no Internet/pip install at runtime. The public source repo records that dependency in `requirements.txt` rather than committing the entire vendored library tree.

---

## 2. MBTiles expectations

The current server expects a standard raster MBTiles database containing:

```text
metadata(name, value)
tiles(
    zoom_level,
    tile_column,
    tile_row,
    tile_data
)
```

Required `tiles` fields:

- `zoom_level`
- `tile_column`
- `tile_row`
- `tile_data`

The server opens the database read-only.

Current accepted raster tile payloads:

- PNG
- JPEG

Vector/PBF MBTiles are not supported by the current path.

---

## 3. TMS → XYZ/WMTS row conversion

Raster MBTiles commonly stores tile rows in TMS bottom-origin order.

WMTS/XYZ client requests use top-origin rows.

For zoom `z` and requested top-origin row `y`:

```text
tms_y = (2^z - 1) - y
```

The requested tile is then read from SQLite using:

```text
zoom_level = z
tile_column = x
tile_row = tms_y
```

The raster bytes are returned directly. Map Fountain does not resample or redraw them.

---

## 4. WMTS profile

The current service advertises:

- WMTS 1.0.0-style capabilities;
- tile matrix set identifier: `GoogleMapsCompatible`;
- supported CRS: `urn:ogc:def:crs:EPSG::3857`;
- tile width: 256;
- tile height: 256;
- standard Web Mercator top-left origin;
- scale denominator derived from the standard Web Mercator resolution sequence and OGC pixel size.

The current implementation is intentionally narrow because the live target is ArcGIS Earth Mobile consuming QGIS/Rasta-style Web Mercator raster MBTiles.

---

## 5. Service URLs

ArcGIS Earth Mobile first consumes a GetCapabilities URL such as:

```text
https://<pc-usb-ip>:8443/wmts?SERVICE=WMTS&REQUEST=GetCapabilities&MAP=<map-id>
```

The capabilities document advertises REST tile URLs shaped like:

```text
/wmts/tiles/<map-id>/GoogleMapsCompatible/{TileMatrix}/{TileRow}/{TileCol}.png
```

or `.jpg` for JPEG tile payloads.

---

## 6. Unique per-map identity

This was the critical v0.2.1 fix.

v0.2.0 changed the selected MBTiles but reused one layer identity and one set of tile URLs. ArcGIS Earth Mobile could therefore reuse cached content from the previous map.

v0.2.1 computes a service ID from:

```text
resolved file path
file size
file modification time (nanoseconds)
```

Those values are hashed with SHA-256 and the first 16 hexadecimal characters become the map/service token.

That token appears in:

- the WMTS service title;
- layer identifier;
- GetCapabilities URL query;
- REST tile URL path.

The result is simple: **a newly selected MBTiles looks like a different service to the mobile client.**

During the test phase the server also sends no-cache response headers.

---

## 7. USB tether discovery

The Windows proof used Android USB tethering, which appeared as:

`Remote NDIS based Internet Sharing Device #2`

The current server runs a bounded PowerShell query that:

1. enumerates active Windows network adapters;
2. selects adapters whose InterfaceDescription contains `Remote NDIS`;
3. reads their IPv4 addresses;
4. ignores `169.254.*` link-local fallback addresses.

The first detected tether adapter/address becomes the service address.

This replaced an earlier bad approach that printed several PC addresses and required guessing which one belonged to the phone.

---

## 8. HTTPS

ArcGIS Earth Mobile successfully consumed the local WMTS over HTTPS during the live proof.

Current v0.2.1 bench behavior:

- TLS server uses Python `ssl.SSLContext`;
- minimum TLS version is TLS 1.2;
- server listens on port 8443;
- certificate/key are loaded from `HTTPS CERT/`;
- the accepted bench certificate was generated for PC tether address `10.13.166.115`.

This is the largest current productization gap.

The public repository does not contain the private server key from the live test.

See `HTTPS_CERTIFICATE_NOTE.md`.

---

## 9. QR generation

The server writes:

- `CURRENT_PHONE_TEST_URL.txt`
- `CURRENT_WMTS_URL.txt`
- `CURRENT_WMTS_QR.svg`
- `CURRENT_WMTS_QR.html`

The GUI enables **OPEN QR** after the server creates a live WMTS URL.

The operator can then use:

```text
ArcGIS Earth Mobile
→ Add Data
→ QR Code
→ scan PC screen
```

This replaced repeated manual entry of the long service URL.

---

## 10. Threading / server model

The current HTTP service uses Python `ThreadingHTTPServer` with daemon request threads.

Each tile request currently opens the MBTiles SQLite database read-only, retrieves one tile, and closes the connection.

That is deliberately simple and safe for the first working architecture.

Potential future optimization includes persistent per-thread connections or a bounded connection pool, but only after measurement establishes that SQLite open/query overhead is a real bottleneck.

---

## 11. Current performance observation

The server successfully delivered multiple substantial MBTiles, including a large Lago panorama, to ArcGIS Earth Mobile.

Live operator result:

- steady deliberate pan/zoom: smooth;
- rapid repeated navigation: can outrun the current path.

No single bottleneck has yet been isolated.

Potential contributors include:

- ArcGIS Earth Mobile request scheduling;
- Android rendering;
- USB-tether throughput;
- Python request concurrency;
- per-request SQLite open/query cost;
- mobile-side cache behavior.

Do not optimize a guessed bottleneck.

---

## 12. Offline boundary

Map Fountain’s core map path does not require the public Internet.

The tested chain is:

```text
local Windows storage
→ local Python service
→ local USB network
→ local Android viewer
```

Outside Internet connectivity was removed during testing and the map remained functional.

This aligns with Offline GeoStack’s hard doctrine: **no operational dependence on public Internet connectivity.**

---

## 13. Relationship to TPKX

Map Fountain does not replace TPKX.

The same source raster pyramid now has two useful deployment forms:

```text
MBTiles → Compact Cache V2 converter → TPKX → local ArcGIS Earth file

MBTiles → Map Fountain → WMTS → ArcGIS Earth Mobile
```

TPKX is excellent for local packaged viewing. MBTiles is excellent as Map Fountain’s serving-side tile store.

The later TPKX Map Factory v1.2 TEST therefore adds `TPKX / MBTiles / Both` normal output choices.

---

## 14. Security / publication rule

Never commit:

- private TLS keys;
- operational certificates tied to deployed systems;
- credentials;
- confidential map databases.

The repository is source/documentation truth. Operational secrets remain outside source control.

---

## 15. Current do-not-regress rules

1. Do not hard-code a test MBTiles into the normal GUI.
2. Do not reuse one WMTS identity for different selected maps.
3. Do not make the public Internet part of the core path.
4. Do not make ordinary operators type long service URLs when QR can carry them.
5. Do not silently serve a certificate for the wrong IP.
6. Do not claim Wi-Fi is live-proven until it is actually tested.
7. Do not hide the rapid-navigation limitation.
8. Do not publish private keys.
9. Do not rebuild raster cartography in the server; serve the existing pyramid.
10. Let the real mobile viewer decide acceptance.
