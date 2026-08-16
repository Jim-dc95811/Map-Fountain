# Map Fountain — Changelog

## v0.2.1 TEST — 2026-08-16 — LIVE-PROVEN

- Fixed stale-map reuse after v0.2.0 by assigning every selected MBTiles a unique service identity.
- Added unique WMTS layer identifiers, unique GetCapabilities URLs, and unique REST tile URLs.
- Added cache-busting/no-cache response headers during testing.
- Confirmed selectable MBTiles GUI drives the actual served map rather than a hard-coded fixture.
- LIVE-PROVEN with three different substantial raster MBTiles on ArcGIS Earth Mobile.
- LIVE-PROVEN with a large Lago panorama delivered smoothly over USB tether.
- Outside Internet removed while local map delivery remained functional.
- Current operator guidance established: deliberate pan/zoom is smooth; rapid repeated navigation can outrun the current mobile path.

## v0.2.0 TEST — 2026-08-16

- Replaced the hard-coded 174-tile proof map with a GUI file selector.
- Added CHOOSE MBTILES, START HTTPS MAP FOUNTAIN, OPEN QR, and STOP SERVER controls.
- Preserved the proven Windows → USB tether → Android → ArcGIS Earth Mobile architecture.
- Defect discovered live: different selected maps reused the same WMTS identity/tile URLs, allowing ArcGIS Earth Mobile to show stale cached content. Fixed in v0.2.1.

## v0.1.5 TEST — 2026-08-16

- Removed target-PC OpenSSL dependency by pre-generating local HTTPS certificate material for the observed USB-tether PC address `10.13.166.115`.
- HTTPS browser/service path worked on Android.
- ArcGIS Earth Mobile accepted the HTTPS WMTS service and displayed map content.

## v0.1.4 TEST — 2026-08-16

- First attempt to add HTTPS around the proven HTTP WMTS path.
- Failed on the Windows target because the build expected `openssl.exe` to be present.
- Failure was visible and corrected rather than worked around manually.

## v0.1.3 TEST — 2026-08-16

- Added offline QR generation and live URL preservation.
- Android rejected the tested HTTP QR path and requested HTTPS, leading directly to the HTTPS branch.

## v0.1.2 TEST — 2026-08-16

- Added direct Windows Remote NDIS / USB-tether adapter detection.
- Stopped guessing among Wi-Fi, Ethernet, VPN, and tether addresses.
- Correctly detected the live PC-side USB address `10.13.166.115`.

## v0.1.1 TEST — 2026-08-16

- Fixed Windows BAT launcher line-ending bug that caused the first package to flash and exit.
- Launcher stayed open on future errors.

## v0.1.0 TEST — 2026-08-16

- First MBTiles → WMTS local serving proof package.
- Used a tiny QGIS-made MBTiles fixture: 174 PNG tiles, Z0–Z18.
- HTTP WMTS reached ArcGIS Earth Mobile over Android USB tether.
- Android requested real tiles and received HTTP 200 responses.
- Outside Internet was removed and the local map path continued to work.

---

## Origin

Map Fountain emerged from Offline GeoStack / Rasta Pyramid Factory testing when ArcGIS Earth Mobile exposed both local-file and URL data-ingestion paths. The first goal was narrow: determine whether a phone could consume map tiles live from a PC/SSD over a private local link without copying an entire mother map onto the device.

That question is now answered: **yes, over the tested USB-tether HTTPS WMTS path.**
