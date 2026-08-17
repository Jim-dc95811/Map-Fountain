# Map Fountain

## Router-only offline map delivery for ArcGIS Earth

**A USB SSD on a consumer router becomes a private offline map reservoir for both Windows ArcGIS Earth and ArcGIS Earth Mobile. The router stays dumb: it stores files, provides the local network, and returns requested bytes.**

![Canonical ArcGIS Earth Systems router flowchart](docs/arcgis_system_router_flowchart_2026-08-17.svg)

> **The router does not need to understand maps. ArcGIS Earth supplies the GIS intelligence.**

---

## Live milestones — 2026-08-17

### Windows ArcGIS Earth — LIVE-PROVEN

```text
native TPKX on USB SSD
        ↓
GL.iNet Flint 2 (GL-MT6000)
        ↓
Samba / SMB
        ↓
private Ethernet or Wi-Fi
        ↓
Windows
        ↓
ArcGIS Earth
```

A production-scale `ESG1N.tpkx` package was opened **in place** from the router-attached SSD and rendered interactively in ArcGIS Earth over Wi-Fi.

Accepted specimen identity:

- `ESG1N.tpkx`
- script-observed size: **26,174,899,216 bytes**
- Windows File Explorer identification: **25,561,426 KB**
- network path: `\\192.168.8.1\New TPKX\Esri and Label\ESG1N.tpkx`

### ArcGIS Earth Mobile / Android — LIVE-PROVEN

Accepted mobile flavor:

> **Static REST WMTS**

```text
pre-rendered Static REST WMTS folder
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

ArcGIS Earth Mobile accepted the router-hosted `WMTSCapabilities.xml`, requested the static raster tiles, and rendered the test map. The app cache was then cleared, ArcGIS Earth was force-stopped/reopened, and the map was loaded successfully again.

No Python runtime, helper app, QGIS Server, Windows map server, Raspberry Pi, or active GIS server is required on the Android field path.

Operational note: deliberate pan/zoom worked; rapid gestures could cause stalls or erratic display behavior. Performance tuning remains follow-on work.

Full acceptance record: [Static REST WMTS Android acceptance — 2026-08-17](docs/STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md)

---

## Two accepted field products

### Windows product

```text
TPKX
→ SSD
→ Flint 2
→ Samba / SMB
→ ArcGIS Earth on Windows
```

The TPKX remains a compact native package.

### Android product

```text
Static REST WMTS
→ SSD
→ Flint 2 HTTPS
→ ArcGIS Earth Mobile
```

The Android product is intentionally an expanded filesystem tree containing `WMTSCapabilities.xml` plus pre-rendered raster tiles.

This is the trade:

```text
no field GIS server
        ↕
expanded static tile directory
```

The expanded WMTS tree is a deployment artifact, not the preferred compact master format.

---

## Factory direction

Keep the compact raster master compact, and expand only when Android delivery is required.

```text
QGIS / Factory render
        ↓
compact raster master: MBTiles
        ├──────────────→ TPKX for Windows ArcGIS Earth
        │
        └──────────────→ Static REST WMTS for Android
```

For the accepted Android test, the WMTS builder copied the existing raster tile payloads from MBTiles without rerendering or recompressing them, converted MBTiles/TMS row numbering to WMTS top-origin rows, and generated the capabilities XML.

Production Factory planning must account for very large directory trees. Priorities are short map IDs, tile-count/free-space preflight, direct-to-SSD output, unique/versioned service identity, automatic capabilities/QR generation, and post-build verification.

See the detailed frozen contract and giant-folder plan in [Static REST WMTS Android acceptance — 2026-08-17](docs/STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md).

---

## Controlled Windows storage proof

The first small-file benchmark exposed heavy Windows caching, so the large-file benchmark was corrected to test the most important access pattern first:

```text
1. random seek
2. four-client random read
3. sequential sample
```

### Ethernet — PASS

- random seek: **25.33 MiB/s**
- random average latency: **9.34 ms**
- random p95: **9.98 ms**
- four-client aggregate: **51.21 MiB/s**
- sequential sample: **42.58 MiB/s**

### Wi-Fi — PASS

- random seek: **5.19 MiB/s**
- random average latency: **46.36 ms**
- random p95: **50.56 ms**
- four-client aggregate: **5.31 MiB/s**
- sequential sample: **6.14 MiB/s**

The Wi-Fi path was substantially slower than Ethernet but remained stable enough to complete the benchmark and the real ArcGIS Earth test.

---

## Evidence fingerprints

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

The packet captures are large bench artifacts and are not committed here. These hashes identify the preserved originals used for the Windows acceptance record.

---

## Current status

| Capability | Status |
| --- | --- |
| Flint 2 + USB SSD Samba share | ✅ **LIVE-PROVEN** |
| Large TPKX open/stat over Samba | ✅ **LIVE-PROVEN** |
| Large-file Ethernet benchmark | ✅ **LIVE-PROVEN** |
| Large-file Wi-Fi benchmark | ✅ **LIVE-PROVEN** |
| Windows ArcGIS Earth direct network TPKX over Wi-Fi | ✅ **LIVE-PROVEN** |
| Android direct file GET through Flint HTTPS/WebDAV endpoint | ✅ **LIVE-PROVEN** |
| ArcGIS Earth Mobile Static REST WMTS from router SSD | ✅ **LIVE-PROVEN** |
| Android cache-clear/reopen retest | ✅ **LIVE-PROVEN** |
| Rapid mobile pan/zoom performance | 🟡 **NEEDS CHARACTERIZATION** |
| Multiple simultaneous ArcGIS Earth clients | 🟡 **NOT YET ACCEPTED** |
| Operational public-Internet dependency | **NONE BY DESIGN** |

---

## Historical precursor

On 2026-08-16 a separate Windows-hosted implementation proved:

```text
raster MBTiles
→ local HTTPS WMTS server
→ Android USB tether
→ ArcGIS Earth Mobile
```

That work remains useful engineering history, but it is not the current field-appliance architecture. The 2026-08-17 breakthrough removed the active field WMTS server by manufacturing the WMTS as static files and letting the Flint serve them directly.

---

## Prior-art / novelty boundary

A 2026-08-17 prior-art search found established examples for the individual ingredients: router-hosted storage, GIS access to network shares, TPKX network-file access, NAS geospatial workflows, and active tile servers.

The project does not claim a mathematically proven worldwide first. It records independently developed, measured architectures and the documented search boundary.

---

## Current engineering record

- [Router acceptance record — 2026-08-17](docs/MAP_FOUNTAIN_ROUTER_ACCEPTANCE_2026-08-17.md)
- [Static REST WMTS Android acceptance — 2026-08-17](docs/STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md)
- [Acceptance record](docs/ACCEPTANCE_RECORD.md)
- [Technical architecture](docs/TECHNICAL_ARCHITECTURE.md)
- [AI / maintainer restart note](docs/AI_CONTINUITY_RESTART_NOTE.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

---

## Governing rules

- No operational dependence on public Internet.
- Keep the router dumb, local, and predictable.
- Windows consumes compact native TPKX over SMB.
- Android consumes Static REST WMTS over local HTTPS.
- Keep MBTiles/TPKX compact; treat expanded WMTS trees as deployment artifacts.
- Prefer read-only field consumption where practical.
- Change one major test variable at a time.
- Wireshark and real-viewer evidence outrank assumptions.
- Do not call a path proven until the intended ArcGIS Earth runtime passes it.
- Do not add field-server complexity unless the real target proves it is necessary.

---

## Project relationship

- **[Offline GeoStack](https://github.com/Jim-dc95811/Offline-GeoStack)** — master operational field-mapping system.
- **[Rasta Pyramid Factory](https://github.com/Jim-dc95811/Rasta-Pyramid-Factory)** — high-resolution raster pyramid manufacturing.
- **Map Fountain** — router-attached offline map storage and local delivery.

Original project software and documentation are MIT-licensed unless otherwise stated. Third-party imagery, ArcGIS Earth, QGIS, router firmware, and source data remain governed by their own licenses and terms.

---

# Map Fountain

> **Put the maps on the SSD. Plug it into the router. Let ArcGIS Earth drink.**
