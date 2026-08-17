# Map Fountain — Acceptance Record

## Evidence labels

**LIVE-PROVEN** — observed on the real intended target and accepted by the intended viewer/workflow.

**LIVE-OBSERVED** — behavior directly observed but not yet treated as a complete acceptance gate.

**BUILT / SELF-TESTED** — implementation exists and passes internal/static checks but has not yet crossed the real target.

**DESIGNED** — architecture or behavior is planned but not yet built/proven.

---

## 1. Router-only Map Fountain / Windows ArcGIS Earth — 2026-08-17

**Status: LIVE-PROVEN**

Hardware:

- GL.iNet Flint 2 (`GL-MT6000`)
- USB-attached SSD
- stock Samba network storage
- Windows laptop on DHCP
- ArcGIS Earth

Large specimen:

- `ESG1N.tpkx`
- 26,174,899,216 bytes by the benchmark script
- 25,561,426 KB Windows File Explorer identification

Proven field chain:

```text
USB SSD
→ Flint 2
→ Samba / SMB
→ Wi-Fi
→ Windows
→ ArcGIS Earth
→ native TPKX opened and rendered in place
```

The decisive acceptance observation was ArcGIS Earth rendering and navigating the Jacksonville map while the TPKX remained on the router-attached SSD.

No field GIS server process was required for this proven TPKX path.

---

## 2. Router-only Map Fountain / Android ArcGIS Earth Mobile — 2026-08-17

**Status: LIVE-PROVEN**

Accepted delivery flavor:

> **Static REST WMTS**

Proven chain:

```text
Static REST WMTS folder
→ USB SSD
→ Flint 2
→ local HTTPS/WebDAV file endpoint
→ Wi-Fi
→ Android
→ ArcGIS Earth Mobile
```

Acceptance observations:

- Android reached the Flint local HTTPS endpoint.
- Direct request of an actual SSD-hosted file succeeded.
- Direct request of the fixture `WMTSCapabilities.xml` succeeded.
- ArcGIS Earth Mobile accepted that capabilities URL and rendered the raster map.
- The Android ArcGIS Earth app cache was cleared.
- ArcGIS Earth was force-stopped/reopened.
- The same router-hosted Static REST WMTS map rendered again.

The accepted runtime requires no Python on Android, no third-party Android helper application, no QGIS Server, no Windows map server, and no Raspberry Pi.

Operational observation: deliberate pan/zoom worked. Rapid gestures could cause stalls or erratic display behavior. This remains a performance-characterization item, not an acceptance failure.

Detailed record:

- `docs/STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md`

---

## 3. Large-file Ethernet storage baseline — 2026-08-17

**Status: LIVE-PROVEN**

The historical benchmark artifact `MAP_TANK_FIRST_BENCH_v0_1_1_TEST` ran against the same `ESG1N.tpkx` through Ethernet.

Results:

- OPEN/STAT: PASS
- random seek: 25.33 MiB/s
- random avg: 9.34 ms
- random median: 9.42 ms
- random p95: 9.98 ms
- random max: 16.17 ms
- four-client aggregate: 51.21 MiB/s
- sequential sample: 42.58 MiB/s

The random phase ran first specifically to reduce cache contamination after the original small-file benchmark demonstrated that Windows could make later reads appear unrealistically fast.

---

## 4. Same large file over Wi-Fi — 2026-08-17

**Status: LIVE-PROVEN**

Same router, same SSD, same TPKX, same benchmark. Major variable changed: Ethernet → Wi-Fi.

Results:

- OPEN/STAT: PASS
- random seek: 5.19 MiB/s
- random avg: 46.36 ms
- random median: 45.42 ms
- random p95: 50.56 ms
- random max: 66.71 ms
- four-client aggregate: 5.31 MiB/s
- sequential sample: 6.14 MiB/s
- sequential 536,870,912-byte logical sample: 83.440 s

Wi-Fi was much slower but completed normally.

---

## 5. Static REST WMTS fixture self-test — 2026-08-17

**Status: BUILT / SELF-TESTED, THEN LIVE-PROVEN ON ANDROID**

Source:

```text
small test 8_17_26 mbtile.mbtiles
```

Observed properties:

- 31,064,064 bytes
- bounds `-81.9384,30.3916,-81.9336,30.3946`
- Z0-Z20
- 261 PNG tiles

Converter/self-test results:

- every exported raster tile byte-identical to the MBTiles tile payload: PASS
- MBTiles/TMS row to WMTS top-origin row conversion: PASS
- capabilities XML parse: PASS
- `TileMatrix / TileRow / TileCol` REST path generation: PASS
- `WorldWebMercatorQuad` matrix definition: PASS
- advertised matrix limits matched actual files: PASS
- Z20 geographic-center tile check: PASS

The resulting Static REST WMTS folder then passed the real ArcGIS Earth Mobile test described above.

---

## 6. Evidence fingerprints — Windows router proof

Original local acceptance artifacts are identified by SHA-256:

```text
Ethernet benchmark screenshot
710e19a0676ada1729a35e13693b8ae81d0527fc3ba654a2da32288ac58244af

Ethernet PCAP
3eda0dc91dee83ac12a96912d8f7264e846c7393c3983de34970b5571a622f0f

Wi-Fi benchmark screenshot
631af7d06f433964175e1c3dc414767cc4c08f98af006406d8068be3b081ba3f

Wi-Fi PCAP
67db0a4dfee9519f933f0fc2e550da69634b293c815cd4b2d81413b38c60f1d4

ArcGIS Earth Wi-Fi success screenshot
8592abb26f9025baf665e4c4174670ba3a2bb433db96cbd092dd27355a9fd840
```

The packet captures are large bench artifacts and are not stored in the public repository. The hashes preserve chain-of-evidence identity.

---

## 7. Historical Windows WMTS proof — 2026-08-16

**Status: LIVE-PROVEN HISTORICAL PRECURSOR**

Before the router-only Android breakthrough, a Windows-hosted Map Fountain implementation proved:

```text
raster MBTiles
→ local HTTPS WMTS server
→ Android USB tether
→ ArcGIS Earth Mobile
```

That work proved local/offline mobile tile delivery, HTTPS, QR loading, and mobile cache behavior. It remains engineering history, not the current field appliance.

The 2026-08-17 Static REST WMTS path removed the active field WMTS server by manufacturing the WMTS resources ahead of time and storing them directly on the router SSD.

---

## 8. Prior-art boundary recorded 2026-08-17

A targeted search found prior art for the individual components and adjacent architectures, including router Samba storage, GIS network-share access, TPKX network-file optimization, NAS-based geospatial storage, and active tile servers.

This record does not claim a mathematically established worldwide first. It records independent development plus the result of the documented prior-art search.

---

## Current accepted statements

> **Windows:** Map Fountain is LIVE-PROVEN as a router-only offline field map appliance in which a GL.iNet Flint 2 exposes a USB-SSD native TPKX through Samba and ArcGIS Earth opens and renders that package directly over Wi-Fi.

> **Android:** Map Fountain is LIVE-PROVEN using a serverless Static REST WMTS package stored as ordinary files on the Flint 2 USB SSD and consumed by ArcGIS Earth Mobile over the router's local HTTPS endpoint.

---

## Immediate next engineering gates

Android consumption is no longer the next acceptance gate. It has passed.

Next work should focus on:

1. production Factory handling of large Static REST WMTS directory trees;
2. short map/service IDs and automatic QR generation;
3. tile-count / payload / free-space preflight;
4. direct-to-deployment-SSD output to avoid a second millions-of-files copy step;
5. larger and denser Android map tests;
6. deliberate-versus-rapid mobile navigation characterization;
7. cold close/reopen and Wi-Fi reconnect behavior;
8. multiple simultaneous Eaters;
9. Windows Ethernet application comparison.
