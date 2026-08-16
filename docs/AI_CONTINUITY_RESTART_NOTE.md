# Map Fountain — AI / Maintainer Restart Note

If coming to this repository cold, establish the following before changing code.

## Project identity

**Map Fountain** is a standalone sibling project created from Offline GeoStack / Rasta Pyramid Factory mobile testing.

Its job is **local raster-map delivery**, not map manufacture, GNSS, PRAVE, or arbitrary-raster pyramid generation.

Current role:

```text
raster MBTiles on Windows PC / SSD
→ local HTTPS WMTS
→ private USB tether
→ ArcGIS Earth Mobile
```

The live-proven v0.2.1 GUI still displays the historical working title `RASTA USB MAP FOUNTAIN`. Do not rewrite working code merely to remove that lineage unless a new build is being deliberately created and tested.

---

## Current proven baseline — 2026-08-16

`Rasta USB Map Fountain v0.2.1 TEST`

**Status: LIVE-PROVEN** for:

- Windows raster MBTiles serving;
- Android USB tether / Remote NDIS;
- HTTPS WMTS;
- QR loading into ArcGIS Earth Mobile;
- operation with outside Internet removed;
- GUI selection of different MBTiles;
- unique per-map WMTS identities preventing stale-map reuse;
- three different substantial MBTiles;
- large Lago panorama.

Current operator observation:

> deliberate pan/zoom is smooth; rapid repeated navigation can outrun the current path.

---

## Critical chronology

### v0.1.0

Tiny 174-tile QGIS MBTiles fixture proved live tile requests from Android over USB tether.

### v0.1.1

Fixed BAT launcher that flashed/closed because the generated batch file contained bad line breaks.

### v0.1.2

Stopped guessing network addresses. Detected the active Windows Remote NDIS tether adapter directly.

### v0.1.3

Generated QR for the live URL. Phone requested HTTPS for the tested QR path.

### v0.1.4

First HTTPS attempt failed because target Windows machine did not have OpenSSL where the build expected it.

### v0.1.5

Pre-generated matching local HTTPS certificate material for the observed tether address. HTTPS worked.

### v0.2.0

Added normal GUI map selection. Defect: changing MBTiles could still display the old small fixture because service/tile identity was reused.

### v0.2.1

Fixed the stale-map defect with unique service IDs and tile URL paths. Multiple large MBTiles then passed live.

---

## Do not regress

- Do not hard-code the small 174-tile test MBTiles into the normal product.
- Do not reuse one WMTS identity for different maps.
- Do not make public Internet connectivity mandatory.
- Do not require operators to type the full WMTS URL as the normal workflow when QR is available.
- Do not publish private TLS keys.
- Do not silently accept a certificate/IP mismatch.
- Do not claim Wi-Fi transport is proven; USB tether is the live-proven transport.
- Do not claim rapid navigation is solved.
- Do not rebuild map cartography inside Map Fountain; serve the existing raster pyramid.
- Do not treat TPKX as obsolete. TPKX and Map Fountain are complementary deployment paths.

---

## Current known-good environment

- Windows 10/11 64-bit
- Python 3.14.5 established known-good
- ArcGIS Earth Mobile on Android
- raster MBTiles
- PNG or JPEG tile payloads
- EPSG:3857 Google-compatible raster tile pyramid
- `python-qrcode` 8.2 for source-run QR generation

The live packaged test vendored the QR library.

---

## Current largest gap

**HTTPS certificate/IP lifecycle.**

The live bench build used certificate material tied to PC tether address `10.13.166.115`.

The public repo intentionally omits the private key.

Do not mistake the absence of the private key in GitHub for loss of the architecture; it is a deliberate security boundary.

---

## Relationship to other repositories

### Offline GeoStack

Master operational project. Its TPKX Map Factory v1.2 TEST adds `TPKX / MBTiles / Both` because MBTiles became operationally useful for Map Fountain.

### Rasta Pyramid Factory

General giant-raster pyramid manufacturer. Rasta can create MBTiles that Map Fountain can serve.

---

## Cold-start reading order

1. `README.md`
2. `docs/PROJECT_STATUS_2026-08-16.md`
3. `docs/ACCEPTANCE_RECORD.md`
4. `docs/TECHNICAL_ARCHITECTURE.md`
5. `docs/HTTPS_CERTIFICATE_NOTE.md`
6. `CHANGELOG.md`
7. `ROADMAP.md`
8. newest commits/issues

Report current evidence status before changing behavior.

---

## Governing principle

> **The viewer asks for tiles. The fountain serves them. Keep everything between those two points local, simple, and observable.**
