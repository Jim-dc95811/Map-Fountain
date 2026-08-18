# Map Fountain — Changelog

## 2026-08-18 — PROVEN / PARKED from primary personal-phone deployment

Map Fountain's router-only Windows and Android acceptance results remain valid and preserved.

The larger project simplified the normal mobile deployment direction to:

```text
TPKX
→ microSD
→ Android
→ ArcGIS Field Maps / ArcGIS Earth
```

Decision:

- Map Fountain is **not a failed branch**;
- it is **LIVE-PROVEN engineering reference**;
- it is **parked from the primary personal-phone path** because direct removable storage is simpler for the intended user;
- active Android deployment work moved to `Android-Field-Maps-and-ArcGIS-Earth-`;
- Static REST manufacturing optimization is paused unless a real shared-storage use case reopens it;
- possible future role: **Starlink-connected basecamp storage / poor-man's NAS**.

The acceptance evidence, benchmark numbers, packet-capture hashes, and Static REST compatibility work remain part of the permanent engineering record.

---

## Android Static REST WMTS — 2026-08-17 — LIVE-PROVEN

- Promoted the router-only Android path to **LIVE-PROVEN**.
- Frozen accepted Android delivery flavor: **Static REST WMTS**.
- Proven chain:

```text
Static REST WMTS folder
→ USB SSD
→ GL.iNet Flint 2
→ local HTTPS/WebDAV exact-file delivery
→ Wi-Fi
→ Android
→ ArcGIS Earth Mobile
```

- Android Chrome proved direct exact-file GET from the Flint-attached SSD.
- The fixture `WMTSCapabilities.xml` downloaded successfully through the same local HTTPS endpoint.
- ArcGIS Earth Mobile accepted the capabilities URL and rendered the map.
- ArcGIS Earth Android app cache was cleared, the app was force-stopped/reopened, and the router-hosted map rendered again.
- No Python runtime, helper app, QGIS Server, Windows map server, or Raspberry Pi is required on the accepted Android router path.
- Static WMTS package uses pre-rendered raster tiles, `WorldWebMercatorQuad`, and REST `TileMatrix / TileRow / TileCol` addressing.
- Accepted test fixture derived from `small test 8_17_26 mbtile.mbtiles`: 31,064,064 bytes, 261 PNG tiles, Z0-Z20.
- Self-test verified byte-identical raster extraction, TMS-to-WMTS row conversion, capabilities XML, matrix limits, and representative geographic indexing.
- Live behavior note: slow deliberate pan/zoom works; rapid gestures can cause stalls or erratic display behavior.
- Manufacturing rule frozen for this accepted router experiment: keep MBTiles/TPKX compact; treat the expanded Static REST WMTS tree as a deployment artifact.

## Router-only Map Fountain — 2026-08-17 — LIVE-PROVEN

- Promoted the consumer-router + USB-SSD architecture from bench concept to **LIVE-PROVEN**.
- Test hardware: **GL.iNet Flint 2 (GL-MT6000)** with USB-attached SSD and Samba file sharing.
- Proven native file chain:

```text
USB SSD
→ Flint 2
→ Samba / SMB
→ Ethernet or Wi-Fi
→ Windows
→ ArcGIS Earth
→ native TPKX opened in place
```

- Large specimen: `ESG1N.tpkx`, script-observed size **26,174,899,216 bytes**, Windows File Explorer identification **25,561,426 KB**.
- Ethernet storage benchmark PASS:
  - random seek 25.33 MiB/s;
  - random average 9.34 ms;
  - p95 9.98 ms;
  - four-client aggregate 51.21 MiB/s;
  - sequential sample 42.58 MiB/s.
- Wi-Fi storage benchmark PASS:
  - random seek 5.19 MiB/s;
  - random average 46.36 ms;
  - p95 50.56 ms;
  - four-client aggregate 5.31 MiB/s;
  - sequential sample 6.14 MiB/s.
- The Wi-Fi sequential 536,870,912-byte logical sample completed in 83.440 seconds; the apparent pause was sustained work, not a hang.
- ArcGIS Earth then opened the same native TPKX directly from the router Samba share over Wi-Fi and rendered/navigated the map successfully.
- Field architecture decision at that milestone: router only. The router supplied storage/network/file sharing; ArcGIS Earth supplied the GIS intelligence.

## Consumer-router test branch — 2026-08-17 — SUPERSEDED BY LIVE PROOF

- Defined a consumer-router + USB-SSD experiment for offline ArcGIS Earth map delivery.
- Established Feeder / Eater terminology.
- Defined the controlled acceptance ladder: Ethernet baseline, Wi-Fi comparison, real ArcGIS Earth test, then additional clients/mobile.
- Governing design rule established: changing or swapping map libraries should not require GIS-specific router reconfiguration.

## v0.2.1 TEST — 2026-08-16 — HISTORICAL WINDOWS WMTS PROOF

- Fixed stale-map reuse by assigning every selected MBTiles a unique service identity.
- Added unique WMTS layer identifiers, GetCapabilities URLs, and REST tile URLs.
- Confirmed selectable MBTiles GUI drives the actual served map.
- LIVE-PROVEN with three different substantial raster MBTiles on ArcGIS Earth Mobile.
- LIVE-PROVEN with a large Lago panorama delivered smoothly over Android USB tether.
- Outside Internet removed while local map delivery remained functional.
- This remains important development history but is not the current field architecture.

## v0.2.0 TEST — 2026-08-16

- Replaced the hard-coded small fixture with a GUI file selector.
- Added CHOOSE MBTILES, START HTTPS MAP FOUNTAIN, OPEN QR, and STOP SERVER controls.
- Defect discovered live: different selected maps reused the same WMTS identity/tile URLs, allowing ArcGIS Earth Mobile to show stale cached content. Fixed in v0.2.1.

## v0.1.5 TEST — 2026-08-16

- Removed target-PC OpenSSL dependency by pre-generating local HTTPS certificate material for the observed USB-tether PC address `10.13.166.115`.
- HTTPS browser/service path worked on Android.
- ArcGIS Earth Mobile accepted the HTTPS WMTS service and displayed map content.

## v0.1.4 TEST — 2026-08-16

- First attempt to add HTTPS around the proven HTTP WMTS path.
- Failed on the Windows target because the build expected `openssl.exe` to be present.
- Failure was visible and corrected rather than hidden.

## v0.1.3 TEST — 2026-08-16

- Added offline QR generation and live URL preservation.
- Android rejected the tested HTTP QR path and requested HTTPS, leading to the HTTPS branch.

## v0.1.2 TEST — 2026-08-16

- Added direct Windows Remote NDIS / USB-tether adapter detection.
- Correctly detected the live PC-side USB address `10.13.166.115`.

## v0.1.1 TEST — 2026-08-16

- Fixed Windows BAT launcher line-ending bug that caused the first package to flash and exit.
- Launcher stayed open on future errors.

## v0.1.0 TEST — 2026-08-16

- First MBTiles → WMTS local serving proof package.
- Used a tiny QGIS-made MBTiles fixture: 174 PNG tiles, Z0-Z18.
- HTTP WMTS reached ArcGIS Earth Mobile over Android USB tether.
- Android requested real tiles and received HTTP 200 responses.
- Outside Internet was removed and the local map path continued to work.

---

## Origin

Map Fountain emerged from Offline GeoStack / Rasta Pyramid Factory testing as a way to keep large map libraries local and let ArcGIS Earth consume only what the operator needs.

The enduring lesson is:

> **Shared storage can stay dumb. Use it when shared storage is actually the better tool.**
