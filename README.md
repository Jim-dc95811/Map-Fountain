# Map Fountain

## Offline raster maps, poured locally

**Serve raster MBTiles from a Windows PC or SSD to ArcGIS Earth Mobile over a private local link — no public Internet required.**

![System architecture](https://raw.githubusercontent.com/Jim-dc95811/Map-Fountain/main/docs/ChatGPT%20Image%20Aug%2016%2C%202026%2C%2007_11_25%20PM.png)

Map Fountain is a small Windows-first map-delivery tool built around a simple idea:

```text
MBTiles on PC / SSD
        ↓
local HTTPS WMTS
        ↓
private USB-tether network
        ↓
ArcGIS Earth Mobile
```

The current live-proven implementation is **`Rasta USB Map Fountain v0.2.1 TEST`**. The `Rasta` prefix remains in that working GUI because Map Fountain was discovered and built during Rasta / Offline GeoStack testing. This repository is the new standalone home for the delivery system itself.

> **The map stays on the depot. The phone drinks only the tiles it needs.**

---

## Current status

| Capability | Status |
| --- | --- |
| Windows MBTiles → local WMTS | ✅ **LIVE-PROVEN** |
| Android USB tether / Remote NDIS transport | ✅ **LIVE-PROVEN** |
| HTTPS local serving | ✅ **LIVE-PROVEN** |
| QR loading into ArcGIS Earth Mobile | ✅ **LIVE-PROVEN** |
| Operation with outside Internet removed | ✅ **LIVE-PROVEN** |
| GUI selection of arbitrary raster MBTiles | ✅ **LIVE-PROVEN** |
| Unique per-map service identity / cache isolation | ✅ **LIVE-PROVEN** |
| Three different substantial MBTiles displayed on Android | ✅ **LIVE-PROVEN** |
| Large Lago panorama displayed smoothly on Android | ✅ **LIVE-PROVEN** |
| Map Tank — consumer router + USB SSD | 🟡 **DESIGNED / BENCH TEST PENDING** |
| Flint 2 GL-MT6000 test hardware | ✅ **RECEIVED / DATA PATH NOT YET PROVEN** |
| Wi-Fi Map Tank transport | 🟡 **DESIGNED / NOT YET LIVE-PROVEN** |
| Automatic consumer-grade HTTPS certificate lifecycle | **NOT YET FINISHED** |

---

## Map Tank — consumer router + USB SSD

**Status: DESIGNED / BENCH TEST PENDING — 2026-08-17**

Map Tank is a new Map Fountain deployment experiment built around a deliberately simple appliance:

```text
USB SSD full of finished map products
        ↓
consumer router
        ↓
private local network
        ↓
ArcGIS Earth clients
```

The first physical test router is a **GL.iNet Flint 2 (GL-MT6000)**. The hardware has arrived, but no Map Tank data path is called live-proven until controlled bench evidence is captured.

The design rule is simple:

> **Keep the router dumb.**

A new map should be able to appear by adding a finished file to the SSD. A completely different library should be able to appear by swapping in another preloaded SSD. The router should not require GIS-specific reconfiguration when the map inventory changes.

### Feeder / Eater model

Field clients are **Eaters**: laptops, phones, or tablets that consume maps read-only.

At basecamp, a **Feeder** maintains the Map Tank library by discovering the tank, comparing the approved master library against the SSD, adding new maps, replacing updated maps, retiring obsolete maps where appropriate, and verifying the result.

```text
BASECAMP
approved master map library
        ↓
Map Tank Feeder
        ↓
router + USB SSD
        ↓
MAP TANK CURRENT

FIELD
router + USB SSD
        ↓
private local network
        ↓
Eaters: ArcGIS Earth PC / Mobile
```

The first acceptance sequence deliberately begins with **Ethernet**, not Wi-Fi, so the radio is removed as a variable. The planned order is:

1. Ethernet storage baseline with Wireshark.
2. ArcGIS Earth PC opening a known-good TPKX from the router-hosted SSD if the share path is accepted.
3. Repeat the same test over Wi-Fi with no other major changes.
4. Simulated mobile/tile consumption on Windows if useful.
5. ArcGIS Earth Mobile experiments only after the storage/network behavior is understood.

See **[Map Tank test plan — 2026-08-17](docs/MAP_TANK_TEST_PLAN_2026-08-17.md)**.

---

## Live milestone — 2026-08-16

The first working chain was proven on a Windows PC and a Motorola Android phone:

```text
raster MBTiles
→ Map Fountain
→ HTTPS WMTS
→ Android USB tether
→ ArcGIS Earth Mobile
```

The Android device requested real WMTS tiles from the PC and received successful HTTP `200` responses across multiple zoom levels. Outside Internet connectivity was then removed and the map continued to function over the private USB link.

The first selectable-GUI build had a stale-map cache problem because different MBTiles reused the same WMTS identity. **v0.2.1 TEST fixed this by generating a unique service ID and unique tile URLs for every selected MBTiles.** After that fix, three different substantial MBTiles were displayed successfully, including a large Lago panorama.

### Current mobile operating envelope

Live operator observation:

> **Deliberate pan and zoom is smooth. Rapid repeated movement can outrun the current phone / delivery / rendering path.**

That is current operator guidance, not a theoretical limitation.

---

## Operator workflow

```text
1. Connect Android by USB.
2. Turn Android USB tethering ON.
3. Start Map Fountain on Windows.
4. CHOOSE MBTILES.
5. Select a raster .mbtiles file from the PC or attached SSD.
6. START HTTPS MAP FOUNTAIN.
7. When status shows LIVE, OPEN QR.
8. ArcGIS Earth Mobile → Add Data → QR Code.
9. Scan the QR displayed on the PC.
10. Pan and zoom deliberately.
```

No Portal account is required for the local WMTS path.

---

## What Map Fountain actually does

The current server:

- opens the selected MBTiles read-only;
- validates a standard raster `tiles` table;
- accepts PNG or JPEG raster tile payloads;
- reads MBTiles/TMS rows and converts them to top-origin XYZ/WMTS rows on request;
- advertises an EPSG:3857 `GoogleMapsCompatible` WMTS tile matrix set;
- creates a unique map/service ID from the selected MBTiles file identity;
- uses unique REST tile URLs so ArcGIS Earth Mobile does not silently reuse another map;
- serves tiles only when the mobile viewer requests them;
- generates the live service URL and QR locally;
- does not require the public Internet for map delivery.

Map Fountain does **not** rerender the map. The raster pyramid already exists inside the MBTiles.

---

## Why MBTiles matters now

Offline GeoStack originally treated MBTiles mainly as a manufacturing intermediate on the way to TPKX. Map Fountain changed that.

The same QGIS-manufactured raster pyramid can now support two deployment families:

```text
MBTiles
  ├─→ Compact Cache V2 converter → TPKX → ArcGIS Earth local file
  └─→ Map Fountain → HTTPS WMTS → ArcGIS Earth Mobile
```

That is why the later TPKX Map Factory v1.2 TEST branch adds normal output selection:

```text
TPKX
MBTiles
Both
```

---

## Relationship to sibling projects

### [Offline GeoStack](https://github.com/Jim-dc95811/Offline-GeoStack)

**Offline GeoStack** is the master operational geospatial project. It includes map manufacturing, ArcGIS Earth, GNSS, PRAVE, field positioning, and the no-operational-Internet doctrine.

Map Fountain is the local map-delivery subsystem that grew large enough to deserve its own repository.

### [Rasta Pyramid Factory](https://github.com/Jim-dc95811/Rasta-Pyramid-Factory)

**Rasta Pyramid Factory** manufactures multiscale raster pyramids from giant ordinary imagery as MBTiles, TPKX, or both.

Rasta can manufacture the pixels. Map Fountain can pour the MBTiles to a mobile viewer.

---

## Current code truth

The repository carries the source of **v0.2.1 TEST**, the build that was live-proven on 2026-08-16.

Important current limitation: the bench build used temporary HTTPS certificate material tied to the observed USB-tether PC address **`10.13.166.115`**. The private server key used during that live test is **not published in this public repository**.

Map Tank is a parallel experimental deployment branch. It has **not** replaced the v0.2.1 Windows/USB proof and it is **not** yet a proven production path.

See:

- [`docs/MAP_TANK_TEST_PLAN_2026-08-17.md`](docs/MAP_TANK_TEST_PLAN_2026-08-17.md)
- [`docs/PROJECT_STATUS_2026-08-16.md`](docs/PROJECT_STATUS_2026-08-16.md)
- [`docs/OPERATOR_WORKFLOW.md`](docs/OPERATOR_WORKFLOW.md)
- [`docs/TECHNICAL_ARCHITECTURE.md`](docs/TECHNICAL_ARCHITECTURE.md)
- [`docs/ACCEPTANCE_RECORD.md`](docs/ACCEPTANCE_RECORD.md)
- [`docs/HTTPS_CERTIFICATE_NOTE.md`](docs/HTTPS_CERTIFICATE_NOTE.md)
- [`docs/AI_CONTINUITY_RESTART_NOTE.md`](docs/AI_CONTINUITY_RESTART_NOTE.md)
- [`ROADMAP.md`](ROADMAP.md)
- [`CHANGELOG.md`](CHANGELOG.md)

---

## Source requirements

Current source-run baseline:

- Windows 10/11 64-bit
- Python 3.14.5 established known-good
- raster MBTiles with standard `metadata` and `tiles` tables
- PNG or JPEG tile payloads
- EPSG:3857 / Google-compatible raster tile pyramid for the current WMTS implementation
- `python-qrcode` 8.2 for QR generation when running from source

The live packaged test vendored the QR library so no Internet/pip install was required at runtime.

---

## Security boundary

Map Fountain is intended for **private local map delivery**. Do not commit private TLS keys, live credentials, or operational certificates to this repository.

The current public repo intentionally omits the private HTTPS key used during the 2026-08-16 bench proof.

---

## License

Original Map Fountain software and documentation are provided under the MIT License unless a file states otherwise.

Third-party map imagery, ArcGIS Earth, QGIS, source MBTiles, and other external data/software remain governed by their own licenses and terms.

---

# Map Fountain

> **MBTiles in the depot. Tiles on demand at the phone. No public Internet in the loop.**
