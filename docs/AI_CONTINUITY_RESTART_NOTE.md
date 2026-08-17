# Map Fountain — AI / Maintainer Restart Note

If coming to this repository cold, establish the following before changing code or architecture.

## Current project identity

**Map Fountain is the router-only offline map-delivery architecture for ArcGIS Earth.**

Current live-proven Windows chain:

```text
native TPKX on USB SSD
→ GL.iNet Flint 2
→ Samba / SMB
→ Ethernet or Wi-Fi
→ Windows
→ ArcGIS Earth
```

The router is deliberately dumb. It provides storage, DHCP/local networking, and file sharing. ArcGIS Earth supplies the GIS intelligence.

**Do not reintroduce a field GIS-server appliance merely because older project history contains server experiments.**

The canonical architecture drawing is:

`docs/arcgis_system_router_flowchart_2026-08-17.svg`

It uses the Factory / PC / Android flowchart layout. Do not replace it with the superseded hub-and-spoke diagram.

---

## Current proven baseline — 2026-08-17

Large specimen:

- `ESG1N.tpkx`
- 26,174,899,216 bytes by the benchmark script
- 25,561,426 KB Windows File Explorer identification

Proven results:

- large TPKX open/stat over router Samba: PASS;
- Ethernet large-file random/sequential benchmark: PASS;
- Wi-Fi large-file random/sequential benchmark: PASS;
- ArcGIS Earth opened the network-hosted TPKX over Wi-Fi and rendered/navigated it successfully: PASS.

Current status label:

**ROUTER-ONLY MAP FOUNTAIN — LIVE-PROVEN ON WINDOWS ARCGIS EARTH**

---

## Critical chronology

### 2026-08-16 — Windows-hosted WMTS precursor

A Windows program served raster MBTiles over local HTTPS WMTS to ArcGIS Earth Mobile through Android USB tether. That branch proved local/offline mobile tile delivery, HTTPS, QR ingestion, per-map cache identity, and operation with outside Internet removed.

Treat that as important engineering history and a reusable compatibility technique, **not the current field architecture**.

### 2026-08-17 — consumer-router proof

A GL.iNet Flint 2 with USB SSD was tested as a deliberately dumb map reservoir.

The first small TPKX benchmark proved Samba access but also exposed Windows cache contamination.

The benchmark was corrected to run random seek first, then multi-client random reads, then the sequential sample.

The historical benchmark filename contains `MAP_TANK`; use that name only when identifying the exact test artifact. The current architecture/product name is **Map Fountain**.

### 2026-08-17 — large Ethernet proof

`ESG1N.tpkx` passed the large-file benchmark through Ethernet.

Key values:

- random: 25.33 MiB/s;
- random p95: 9.98 ms;
- four-client aggregate: 51.21 MiB/s;
- sequential: 42.58 MiB/s.

### 2026-08-17 — same file over Wi-Fi

Same router, same SSD, same TPKX, same benchmark; Ethernet changed to Wi-Fi.

Key values:

- random: 5.19 MiB/s;
- random p95: 50.56 ms;
- four-client aggregate: 5.31 MiB/s;
- sequential: 6.14 MiB/s.

The long 83.440-second sequential phase completed successfully.

### 2026-08-17 — real ArcGIS Earth proof

ArcGIS Earth opened the same TPKX directly through the Samba path over Wi-Fi and rendered the Jacksonville map.

This is the decisive acceptance event. The storage benchmark proved the hose; ArcGIS Earth proved the actual field use.

---

## Do not regress

- Do not add a field GIS server unless the real target proves it is required.
- Do not revive Raspberry Pi / Pi-server architecture in active Map Fountain documentation.
- Do not make public Internet connectivity mandatory.
- Do not make normal Eaters use manual static IP configuration.
- Do not unpack or rerender native TPKX in the router.
- Do not confuse Windows cache/read-ahead throughput with raw router speed.
- Do not optimize a guessed bottleneck before real ArcGIS Earth behavior exposes one.
- Preserve read-only field consumption where practical.
- Preserve controlled-test discipline: one major variable at a time.
- Preserve the 2026-08-17 evidence hashes and benchmark numbers.
- Treat the intended ArcGIS Earth runtime as the final acceptance authority.

---

## Current evidence fingerprints

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

---

## Current next gate

**Android / ArcGIS Earth Mobile on the router-only architecture.**

The Windows path is proven. Mobile must now earn its own real-target acceptance without assuming that the old Windows WMTS server needs to return.

After Android:

1. direct ArcGIS Earth Ethernet application comparison;
2. Wi-Fi navigation characterization;
3. cold close/reopen and Wi-Fi reconnect;
4. multiple simultaneous Eaters;
5. basecamp Feeder after consumption behavior is stable.

---

## Relationship to sibling repositories

### Offline GeoStack

Master operational field-mapping project: ArcGIS Earth runtime, TPKX manufacturing, GNSS, PRAVE/F22/QR integration, and offline doctrine.

### Rasta Pyramid Factory

General high-resolution raster-pyramid manufacturer producing MBTiles, TPKX, or both.

### Map Fountain

Router-attached storage and private local delivery of finished map products.

---

## Cold-start reading order

1. `README.md`
2. `docs/MAP_FOUNTAIN_ROUTER_ACCEPTANCE_2026-08-17.md`
3. `docs/PROJECT_STATUS_2026-08-17.md`
4. `docs/TECHNICAL_ARCHITECTURE.md`
5. `CHANGELOG.md`
6. `ROADMAP.md`
7. newest commits/issues

Report the current evidence state before changing behavior.

---

## Governing principle

> **Keep the router dumb. Keep the maps native. Let ArcGIS Earth do the GIS work.**
