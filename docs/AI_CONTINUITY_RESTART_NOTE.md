# Map Fountain — AI / Maintainer Restart Note

If coming to this repository cold, establish the following before changing code or architecture.

## Current project identity

**Map Fountain is the router-only offline map-delivery architecture for ArcGIS Earth on Windows and Android.**

The router is deliberately dumb. It provides storage, DHCP/private networking, Samba for Windows, and a local HTTPS/WebDAV file endpoint for Android. ArcGIS Earth supplies the GIS intelligence.

**Do not reintroduce a field GIS-server appliance merely because older project history contains server experiments.**

Canonical architecture drawing:

`docs/arcgis_system_router_flowchart_2026-08-17.svg`

Use the Factory / PC / Android flowchart. Do not restore the superseded hub-and-spoke / Pi-server architecture.

---

## Current live-proven field paths — 2026-08-17

### Windows ArcGIS Earth

```text
native TPKX on USB SSD
→ GL.iNet Flint 2
→ Samba / SMB
→ Ethernet or Wi-Fi
→ Windows
→ ArcGIS Earth
```

Large accepted specimen:

- `ESG1N.tpkx`
- 26,174,899,216 bytes by benchmark script
- 25,561,426 KB Windows File Explorer identification

ArcGIS Earth opened the network-hosted TPKX over Wi-Fi and rendered/navigated it successfully.

### Android ArcGIS Earth Mobile

Accepted flavor:

> **Static REST WMTS**

```text
Static REST WMTS folder on USB SSD
→ GL.iNet Flint 2
→ local HTTPS/WebDAV exact-file GET
→ Wi-Fi
→ Android
→ ArcGIS Earth Mobile
```

Observed acceptance sequence:

- Android reached the Flint HTTPS endpoint.
- Exact file GET from SSD succeeded.
- `WMTSCapabilities.xml` exact-file GET succeeded.
- ArcGIS Earth Mobile accepted that URL and rendered the map.
- ArcGIS Earth app cache was cleared.
- App was force-stopped/reopened.
- The same router-hosted map rendered again.

No Python on Android. No helper app. No QGIS Server. No Windows map server. No Raspberry Pi.

Slow deliberate pan/zoom works; rapid gestures may stall or behave erratically. Treat this as performance characterization, not architecture failure.

Detailed Android record:

`docs/STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md`

---

## Critical manufacturing rule

**Keep compact masters compact. Expand only the Android deployment artifact.**

```text
QGIS / Factory render
        ↓
MBTiles compact raster master
        ├──→ TPKX for Windows
        └──→ Static REST WMTS expanded tree for Android
```

The accepted Android test converter copied raster tile payloads out of MBTiles byte-for-byte, flipped TMS row numbering to WMTS top-origin rows, and generated `WMTSCapabilities.xml`.

Static REST WMTS means giant directory trees. That is the cost of removing the active field GIS server.

The expanded WMTS tree is a deployment artifact, not the preferred archive/master format.

---

## Production Factory next gate

Do not redesign the proven runtime path. Improve manufacturing around it.

Required planning:

1. Static REST WMTS output mode.
2. Short map/service IDs.
3. Tile-count preflight.
4. Payload/free-space preflight.
5. Direct-to-removable-SSD build to avoid a second millions-of-files copy.
6. Unique/versioned identity for cache safety.
7. Automatic capabilities generation.
8. Automatic QR generation.
9. Post-build verification.
10. Whole-map delete/replace workflow.
11. Larger/denser Android performance tests.

The exact final Factory GUI and deployment root-folder names are not frozen yet.

---

## Windows benchmark baseline

Ethernet:

- random 25.33 MiB/s
- random p95 9.98 ms
- four-client aggregate 51.21 MiB/s
- sequential 42.58 MiB/s

Wi-Fi:

- random 5.19 MiB/s
- random p95 50.56 ms
- four-client aggregate 5.31 MiB/s
- sequential 6.14 MiB/s

Do not call later cached/read-ahead rates raw router wire speed.

---

## Do not regress

- Do not add a field GIS server unless real target evidence proves it is required.
- Do not revive Raspberry Pi / Pi-server architecture in active Map Fountain work.
- Do not make public Internet connectivity mandatory.
- Do not make normal Eaters use manual static IP configuration.
- Windows accepted product is native TPKX over SMB.
- Android accepted product is Static REST WMTS over local HTTPS.
- Do not require Python or helper apps on Android.
- Do not turn expanded WMTS trees into the canonical compact archive format.
- Use short Android map IDs; long discovery-test names are not a standard.
- Generate QR codes for long mobile URLs.
- Do not optimize a guessed bottleneck before controlled testing exposes one.
- Preserve controlled-test discipline: one major variable at a time.
- Treat the intended ArcGIS Earth runtime as final acceptance authority.

---

## Historical chronology

### 2026-08-16 — active Windows WMTS precursor

Windows served raster MBTiles through an active local HTTPS WMTS process to ArcGIS Earth Mobile over Android USB tether. This proved local/offline mobile WMTS compatibility but is not the current field appliance.

### 2026-08-17 — Windows router-only breakthrough

Flint 2 + USB SSD + Samba served a production-scale native TPKX directly to Windows ArcGIS Earth over Wi-Fi.

### 2026-08-17 — Android router-only breakthrough

Flint 2 built-in local HTTPS/WebDAV exact-file delivery served a pre-generated Static REST WMTS folder directly from the USB SSD to ArcGIS Earth Mobile. The mobile map rendered again after ArcGIS Earth cache clear and app restart.

This removed the active field WMTS server from the Android runtime architecture.

---

## Evidence fingerprints — Windows acceptance

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

## Current next gates

1. freeze practical Static REST WMTS Factory workflow for giant folder trees;
2. short IDs + QR automation;
3. direct-to-SSD output and free-space preflight;
4. larger/denser Android map;
5. deliberate vs rapid mobile navigation characterization;
6. cold close/reopen and Wi-Fi reconnect;
7. multiple simultaneous Eaters;
8. Windows Ethernet application comparison;
9. basecamp Feeder after consumption/deployment behavior is stable.

---

## Cold-start reading order

1. `README.md`
2. `docs/STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md`
3. `docs/MAP_FOUNTAIN_ROUTER_ACCEPTANCE_2026-08-17.md`
4. `docs/ACCEPTANCE_RECORD.md`
5. `docs/TECHNICAL_ARCHITECTURE.md`
6. `ROADMAP.md`
7. `CHANGELOG.md`
8. newest commits/issues

Report the current evidence state before changing behavior.

---

## Governing principle

> **Keep the router dumb. Manufacture the right product for each ArcGIS Earth client.**
