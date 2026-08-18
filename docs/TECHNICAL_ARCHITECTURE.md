# Map Fountain — Technical Architecture

## Current disposition

This document records the **accepted router/storage architecture** proven on 2026-08-17.

Map Fountain is now **LIVE-PROVEN / PARKED from the primary personal-phone deployment path**. The architecture below remains valid engineering evidence; it is not mandatory infrastructure for the current microSD/local-TPKX phone direction.

Current phone deployment work lives in the sibling repository:

**[Android Field Maps + ArcGIS Earth](https://github.com/Jim-dc95811/Android-Field-Maps-and-ArcGIS-Earth-)**

Potential future Map Fountain role: Starlink-connected basecamp storage / poor-man's NAS.

---

## 1. Accepted field paths

### Windows ArcGIS Earth — native TPKX over SMB

```text
finished native TPKX
        ↓
USB SSD
        ↓
GL.iNet Flint 2
        ↓
Samba / SMB
        ↓
private Ethernet or Wi-Fi
        ↓
Windows
        ↓
ArcGIS Earth
```

The router does not unpack or transform TPKX. Windows/SMB presents the remote file and ArcGIS Earth selectively reads package content it needs.

### Android ArcGIS Earth Mobile — Static REST WMTS over HTTPS

```text
pre-rendered Static REST WMTS directory
        ↓
USB SSD
        ↓
GL.iNet Flint 2
        ↓
built-in local HTTPS/WebDAV file endpoint
        ↓
private Wi-Fi
        ↓
Android
        ↓
ArcGIS Earth Mobile
```

The router does not execute WMTS logic. The WMTS behavior is manufactured ahead of time into `WMTSCapabilities.xml`, a REST URL template, and a raster tile directory tree.

No Python runtime or helper application runs on Android.

No active QGIS Server, Windows map server, Raspberry Pi, or other field GIS-server process is required for either accepted path.

---

## 2. Division of labor

```text
Factory knows how to manufacture the map.
SSD stores the finished products.
Router shares/serves ordinary bytes.
ArcGIS Earth understands and renders the map.
```

For Windows, the map intelligence remains inside native TPKX.

For the accepted Android router experiment, discovery/addressing information is represented by a static WMTS capabilities document and prebuilt raster tree.

---

## 3. Windows network-share proof

Live test router LAN address:

```text
192.168.8.1
```

Tested share path:

```text
\\192.168.8.1\New TPKX
```

Production-scale test file:

```text
\\192.168.8.1\New TPKX\Esri and Label\ESG1N.tpkx
```

Specimen identity:

```text
ESG1N.tpkx
26,174,899,216 bytes
25,561,426 KB in Windows File Explorer
```

ArcGIS Earth opened and rendered this network-hosted TPKX directly over Wi-Fi.

---

## 4. Android local HTTPS proof

The accepted Android test used the Flint 2 built-in local HTTPS/WebDAV endpoint on port 6008.

Observed behavior:

- requesting the shared directory itself returned `403 Forbidden`;
- requesting a specific file directly succeeded;
- requesting `WMTSCapabilities.xml` directly succeeded;
- ArcGIS Earth Mobile then used that static capabilities resource to locate and request raster tiles.

Directory browsing was not required. Exact static-file GET was what mattered.

---

## 5. Accepted Static REST WMTS flavor

Package shape:

```text
<map-id>/
  1.0.0/
    WMTSCapabilities.xml
    <layer-id>/
      default/
        WorldWebMercatorQuad/
          <TileMatrix>/
            <TileRow>/
              <TileCol>.png
```

Accepted characteristics:

- WMTS 1.0.0;
- raster PNG/JPEG;
- Web Mercator / EPSG:3857;
- `WorldWebMercatorQuad`;
- REST `ResourceURL` tile addressing;
- `TileMatrix / TileRow / TileCol` path order;
- ordinary static files only at runtime.

The accepted fixture was derived from raster MBTiles by copying tile payloads unchanged, converting TMS bottom-origin rows to WMTS top-origin rows, and generating the capabilities XML.

Detailed acceptance: `docs/STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md`.

---

## 6. Compact masters versus expanded deployment product

The accepted router experiment distinguished compact manufacturing/master formats from the Android runtime artifact:

```text
QGIS / Factory render
        ↓
compact raster master: MBTiles
        ├──────────────→ native TPKX deployment for Windows
        │
        └──────────────→ expanded Static REST WMTS for Android router experiment
```

- **MBTiles** — compact raster master/interchange product.
- **TPKX** — compact native ArcGIS Earth deployment product.
- **Static REST WMTS directory** — expanded Android router deployment artifact.

The expanded WMTS tree must not become the preferred archival/master form.

---

## 7. Giant-folder lesson

Static REST WMTS can contain hundreds of thousands or millions of individual raster files/directories.

This is the cost of the accepted serverless-router Android method.

The production-scale Factory experiments therefore explored:

- short map IDs;
- tile-count and free-space preflight;
- direct-to-final-storage output;
- avoiding duplicate expanded trees;
- unique/versioned service IDs;
- automatic capabilities generation;
- QR generation;
- post-build verification;
- clean whole-map delete/replace.

A later v1.4.0 TEST branch replaced giant-tree ZIP transport with a compact `.restmap` seed that expands at final storage. That branch is self-tested but no longer the primary personal-phone priority while local TPKX/microSD deployment is pursued.

---

## 8. Android live behavior

The Static REST WMTS map rendered in ArcGIS Earth Mobile.

After clearing the ArcGIS Earth Android app cache and force-stopping/reopening the app, the router-hosted map rendered again.

Observed navigation characteristic:

> slow, deliberate movements worked; rapid gestures could cause stalls or erratic behavior.

This remains an observed characteristic of the tested router/HTTP/mobile path, not a statement about local TPKX performance.

---

## 9. Windows storage benchmark baseline

Corrected large-file benchmark order:

```text
1. random seek
2. four-client random read
3. sequential sample
```

### Ethernet

- random seek: 25.33 MiB/s
- random average latency: 9.34 ms
- random p95: 9.98 ms
- four-client aggregate: 51.21 MiB/s
- sequential sample: 42.58 MiB/s

### Wi-Fi

- random seek: 5.19 MiB/s
- random average latency: 46.36 ms
- random p95: 50.56 ms
- four-client aggregate: 5.31 MiB/s
- sequential sample: 6.14 MiB/s

These values characterize the complete Windows + SMB + cache/read-ahead + router + SSD path and must not be mislabeled as raw router wire speed.

---

## 10. Packet-analysis boundary

The Windows SMB session used SMB3 encryption.

Wireshark can validate endpoints, timing, byte volume, connection continuity, resets/retransmissions, and overall traffic shape. Individual encrypted SMB file-read commands require session keys to decode.

The real ArcGIS Earth runtime remains the final application acceptance authority.

---

## 11. DHCP / addressing

Normal consumers use DHCP.

Do not manually assign client static addresses merely to consume maps. Prefer router-side DHCP reservations only when a separate future service genuinely needs a stable client address.

---

## 12. Current relationship to personal-phone deployment

The normal personal-phone direction now bypasses Map Fountain:

```text
TPKX
→ microSD
→ Android
→ ArcGIS Field Maps / ArcGIS Earth
```

That is an architectural simplification, not a repudiation of the router proof.

Map Fountain remains useful when **shared storage** is itself the requirement.

---

## 13. Possible Starlink/basecamp architecture

If reopened:

```text
Starlink
→ Flint 2 WAN
→ USB SSD
→ private SMB / Wi-Fi / Ethernet
→ basecamp laptops / clients
```

Desired property:

- Internet when available can assist manufacturing/refresh;
- local files and LAN remain useful when Starlink is absent;
- the router still does not become a GIS server.

This role has not yet been promoted beyond future direction.

---

## 14. Do-not-regress rules

1. Preserve both live-proven router acceptance records.
2. Do not call Map Fountain a failure merely because the larger system simplified afterward.
3. Do not make Map Fountain mandatory in the current personal-phone path.
4. Do not reintroduce Raspberry Pi / Pi-server architecture by inertia.
5. Do not make public Internet part of the core local map path.
6. Keep MBTiles/TPKX compact and expanded WMTS as a disposable deployment artifact.
7. Do not optimize the REST branch without a reopened operational need.
8. Do not confuse cached application throughput with raw network speed.
9. Preserve read-only field consumption where practical.
10. Change one major test variable at a time.
11. Let packet evidence validate the network path.
12. Let the real target runtime decide acceptance.

> **Map Fountain proved the reservoir. Use the reservoir only when shared storage is actually useful.**
