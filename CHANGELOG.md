# Map Fountain — Changelog

## 2026-08-20 — stale issue backlog reconciled

The open issue list was brought into line with the later LIVE-PROVEN / PARKED repository state.

- Issue #1, USB-tether certificate/tether-IP lifecycle: **closed / not planned** because the accepted router-only path removed that requirement.
- Issue #2, USB-tether cold restart/reconnect acceptance: **closed / not planned** because that exact transport was superseded; router-only cache-clear/reopen testing passed.
- Issue #3, prove Wi-Fi transport: **closed / completed** because the Flint 2 router-only Static REST WMTS path was live-proven over private Wi-Fi.
- Issue #4, measure rapid-navigation bottleneck: **closed / not planned** while Map Fountain is parked; the observation remains preserved and can be reopened if a real shared-storage role makes optimization necessary.

This cleanup removes stale backlog language that previously contradicted the README/ROADMAP/acceptance records.

---

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
- ArcGIS Earth opened the same native TPKX directly from the router Samba share over Wi-Fi and rendered/navigated it successfully.

## Historical USB Map Fountain branches — 2026-08-16

The v0.1.x / v0.2.x Windows USB-tether HTTPS WMTS branches remain preserved development history. They proved local serving, HTTPS, QR loading, multiple MBTiles, outside-Internet removal, and large Lago panorama behavior before the router-only simplification.

---

## Origin

Map Fountain emerged from Offline GeoStack / Rasta Pyramid Factory testing as a way to keep large map libraries local and let ArcGIS Earth consume only what the operator needs.

> **Shared storage can stay dumb. Use it when shared storage is actually the better tool.**
