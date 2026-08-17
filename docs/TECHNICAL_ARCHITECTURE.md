# Map Fountain — Technical Architecture

## Purpose

Map Fountain is a router-only offline map-delivery architecture for ArcGIS Earth on Windows and Android.

The router is deliberately dumb. It stores finished files, provides the private LAN, and returns requested bytes. GIS intelligence stays in the Factory and ArcGIS Earth clients.

Two different ArcGIS Earth clients now have two different accepted consumption products.

---

# 1. Accepted field paths

## Windows ArcGIS Earth — native TPKX over SMB

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

The router does not unpack or transform TPKX. Windows/SMB presents the remote file and ArcGIS Earth selectively reads the package content it needs.

## Android ArcGIS Earth Mobile — Static REST WMTS over HTTPS

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

The router does not execute WMTS logic. The WMTS behavior is manufactured ahead of time into `WMTSCapabilities.xml`, a REST URL template, and the raster tile directory tree.

No Python runtime or helper application runs on Android.

No active QGIS Server, Windows map server, Raspberry Pi, or other field GIS-server process is required for either accepted path.

---

# 2. Division of labor

```text
Factory knows how to manufacture the map.
SSD stores the finished products.
Router shares/serves ordinary bytes.
ArcGIS Earth understands and renders the map.
```

For Windows, the map intelligence remains inside native TPKX.

For Android, the map intelligence needed for discovery/addressing is represented by a static WMTS capabilities document and a prebuilt raster tile tree.

---

# 3. Windows network share

The live Windows test used the router LAN address:

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

# 4. Android local HTTPS endpoint

The accepted Android test used the Flint 2 built-in local HTTPS/WebDAV endpoint on port 6008.

Important observed behavior:

- requesting the shared directory itself in a browser returned `403 Forbidden`;
- requesting a specific file directly succeeded;
- requesting `WMTSCapabilities.xml` directly succeeded;
- ArcGIS Earth Mobile then used that same static capabilities resource to locate and request raster tiles.

Directory browsing is therefore not required for the accepted Android path. Exact static file GET is what matters.

---

# 5. Static REST WMTS flavor

Accepted package shape:

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

The accepted fixture was derived from a raster MBTiles by copying tile payloads unchanged, converting TMS bottom-origin tile rows to WMTS top-origin rows, and generating the capabilities XML.

Detailed acceptance: `docs/STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md`.

---

# 6. Compact masters versus deployment products

The architecture now explicitly distinguishes compact manufacturing/master formats from field runtime formats.

```text
QGIS / Factory render
        ↓
compact raster master: MBTiles
        ├──────────────→ native TPKX deployment for Windows
        │
        └──────────────→ expanded Static REST WMTS deployment for Android
```

## Compact products

- **MBTiles** — compact raster master/interchange product.
- **TPKX** — compact native Windows ArcGIS Earth deployment product.

## Expanded product

- **Static REST WMTS directory** — Android deployment product.

The expanded WMTS tree should not become the preferred archival/master form. It exists because removing the active field GIS server requires individual static resources that ArcGIS Earth Mobile can request directly.

---

# 7. Giant-folder engineering rule

A Static REST WMTS map may contain hundreds of thousands or millions of individual raster files/directories.

This file-count explosion is an inherent consequence of the accepted serverless Android delivery method, not a defect in the router.

Production Factory planning therefore must include:

1. short map IDs;
2. tile-count preflight;
3. raster-payload size calculation;
4. destination free-space check;
5. direct-to-deployment-SSD build option;
6. avoidance of unnecessary duplicate expanded trees;
7. unique/versioned service IDs for cache safety;
8. automatic capabilities generation;
9. automatic QR generation;
10. post-build verification;
11. clean whole-map delete/replace workflow.

The Factory should avoid forcing an operator to create a giant WMTS tree on one disk and then copy millions of files to another disk when it can write the finished deployment tree directly to the intended removable SSD.

An optional compressed transport/archive wrapper may later be useful, but ArcGIS Earth Mobile's accepted runtime artifact remains the expanded directory tree.

---

# 8. Short naming rule

Deep HTTP paths and QR ingestion make short deployment IDs preferable.

Examples:

```text
JAX1
ESG1
FIRE23
```

Preferred conceptual runtime path:

```text
/WMTS/JAX1/1.0.0/WMTSCapabilities.xml
```

Long descriptive names belong in capabilities metadata and Factory records, not repeatedly inside deep directory structures.

The discovery test name `small_test_android_wmts` is historical test evidence, not a production naming standard.

---

# 9. Android live behavior

The Static REST WMTS map rendered in ArcGIS Earth Mobile.

After clearing the ArcGIS Earth Android app cache and force-stopping/reopening the app, the router-hosted map rendered again.

Operator observation:

> slow, easy pan/zoom movements work; rapid gestures can cause stalls or erratic behavior.

Do not guess the bottleneck. Larger controlled tests must distinguish among:

- many-small-file HTTPS request overhead;
- Wi-Fi throughput/latency;
- ArcGIS Earth Mobile request concurrency/cache behavior;
- tile-pyramid density and map extent.

---

# 10. Windows storage benchmark baseline

The corrected large-file benchmark order was:

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

# 11. Packet-analysis boundary

The Windows SMB session used SMB3 encryption on the tested configuration.

Wireshark can validate endpoints, timing, byte volume, connection continuity, resets/retransmissions, and overall traffic shape, but individual encrypted SMB file-read commands require session keys to decode.

The real ArcGIS Earth runtime remains the final application acceptance authority.

---

# 12. DHCP / addressing

Normal Eaters use DHCP.

Do not manually assign client static addresses simply to consume maps. Prefer router-side DHCP reservations only when a separate future service genuinely needs a stable client address.

---

# 13. Feeder / Eater separation

### Eaters

Accepted Eaters:

- Windows ArcGIS Earth consuming native TPKX over SMB;
- Android ArcGIS Earth Mobile consuming Static REST WMTS over local HTTPS.

### Feeder

A future basecamp Feeder may maintain the SSD inventory:

```text
approved master library
→ compare
→ create/copy deployment products
→ replace updated maps
→ retire obsolete maps when instructed
→ verify
→ MAP FOUNTAIN CURRENT
```

The router does not need Feeder/Eater logic.

---

# 14. Offline boundary

The field architecture is private/local by design.

```text
no cloud map request required
no public tile service required
no portal dependency required
no public Internet requirement in the local map-delivery path
```

Private Ethernet/Wi-Fi networking is part of the offline architecture.

---

# 15. Historical Windows WMTS precursor

On 2026-08-16 the project proved an active Windows-hosted HTTPS WMTS path to ArcGIS Earth Mobile over Android USB tether.

That work established useful compatibility lessons, but the current Android field architecture has removed the active server process by manufacturing the WMTS resources as static files on the router SSD.

---

# 16. Do-not-regress rules

1. Keep the field appliance router-only unless real target evidence proves additional software is necessary.
2. Do not reintroduce Raspberry Pi / Pi-server architecture into the active field path.
3. Do not make public Internet part of the core map path.
4. Windows stays native TPKX over SMB unless a verified defect forces change.
5. Android stays Static REST WMTS over local HTTPS unless a verified defect forces change.
6. Do not require Python or helper apps on Android.
7. Keep MBTiles/TPKX compact and treat expanded WMTS trees as deployment artifacts.
8. Use short unique/versioned Android map IDs to reduce path pain and stale-cache collisions.
9. Do not confuse cached application throughput with raw network speed.
10. Do not optimize a guessed bottleneck before controlled testing exposes it.
11. Preserve read-only field consumption where practical.
12. Change one major test variable at a time.
13. Let packet evidence validate the network path.
14. Let the real ArcGIS Earth runtime decide acceptance.

> **Keep the router dumb. Manufacture the right product for each ArcGIS Earth client.**
