# Map Fountain

## Proven shared map storage over ordinary local networking

**Map Fountain proved that a consumer router plus USB SSD can serve useful offline map products without becoming a GIS server.**

![Canonical ArcGIS Earth Systems router flowchart](docs/arcgis_system_router_flowchart_2026-08-17.svg)

> **The router does not need to understand maps. It only needs to return the right bytes.**

**Keywords:** offline GIS, offline map server, ArcGIS Earth, TPKX, SMB, Samba, WMTS, Static REST WMTS, USB SSD, local Wi-Fi, GL.iNet Flint 2, network storage, field mapping, Starlink, offline NAS

---

## Current status

**LIVE-PROVEN / PARKED from the normal personal-phone path.**

Map Fountain achieved its core engineering goals:

- Windows ArcGIS Earth opened a production-scale native TPKX directly from router-attached SSD storage over SMB/Wi-Fi.
- ArcGIS Earth Mobile rendered a router-hosted Static REST WMTS map over local HTTPS/Wi-Fi.

The broader project then simplified the normal personal-phone deployment further:

```text
TPKX
→ microSD / local storage
→ Android
→ ArcGIS Field Maps / ArcGIS Earth
```

That user-facing deployment now lives in:

**[Android Field Maps + ArcGIS Earth](https://github.com/Jim-dc95811/Android-Field-Maps-and-ArcGIS-Earth-)**

Map Fountain therefore remains **proven shared-storage/network-delivery evidence**, not required infrastructure for every user.

---

## Windows ArcGIS Earth proof

```text
native TPKX on USB SSD
→ GL.iNet Flint 2 (GL-MT6000)
→ Samba / SMB
→ private Ethernet or Wi-Fi
→ Windows
→ ArcGIS Earth
```

Accepted production-scale specimen:

```text
ESG1N.tpkx
26,174,899,216 bytes by benchmark script
25,561,426 KB in Windows File Explorer
```

ArcGIS Earth opened and navigated the TPKX **while it remained on the router-attached SSD**.

Benchmark reference:

| Path | Random | p95 | Four-client aggregate | Sequential |
| --- | ---: | ---: | ---: | ---: |
| Ethernet | 25.33 MiB/s | 9.98 ms | 51.21 MiB/s | 42.58 MiB/s |
| Wi-Fi | 5.19 MiB/s | 50.56 ms | 5.31 MiB/s | 6.14 MiB/s |

The application result mattered more than the synthetic benchmark: **ArcGIS Earth worked.**

---

## Android ArcGIS Earth Mobile proof

Accepted router/mobile compatibility path:

```text
pre-rendered Static REST WMTS folder
→ USB SSD
→ GL.iNet Flint 2
→ built-in local HTTPS/WebDAV endpoint
→ private Wi-Fi
→ Android
→ ArcGIS Earth Mobile
```

ArcGIS Earth Mobile accepted the router-hosted `WMTSCapabilities.xml`, requested static raster tiles, and rendered the map. Cache-clear / force-stop / reopen testing also passed.

No Python runtime, helper application, QGIS Server, Windows map server, or Raspberry Pi was required on the accepted router-only Android path.

Operational observation: deliberate pan/zoom worked; rapid gestures could outrun the delivery/render path.

- [Static REST WMTS Android acceptance](docs/STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md)

---

## What the project proved

```text
map intelligence can stay in the map product / viewer
storage can stay dumb
networking can stay ordinary
```

For Windows, native TPKX remained compact and was selectively read over SMB.

For Android, premanufactured Static REST WMTS proved that ordinary static files could satisfy ArcGIS Earth Mobile through the router’s own local HTTPS endpoint.

Both results remain useful even though direct removable storage is simpler for the ordinary personal-phone user.

---

## Why it is parked

If the entire useful map can already live on the phone’s removable storage, the normal personal-phone workflow becomes:

```text
prepared card
→ phone
→ local map
```

No router association, HTTPS endpoint, service QR, shared SSD, or server-shaped concept is required.

That simplicity wins unless a real shared-storage problem appears.

---

## Possible return — Starlink / basecamp NAS

Map Fountain may return in a different role:

```text
Starlink
→ Flint 2 WAN
→ USB SSD
→ private SMB / Wi-Fi / Ethernet
→ basecamp laptops / local clients
```

In that role it becomes a practical **incident map reservoir / poor-man’s NAS**:

- shared local map inventory;
- laptop access over Ethernet/Wi-Fi;
- fresh Factory products dropped onto the SSD;
- optional Starlink-supported manufacturing/refresh;
- local LAN and stored maps remain useful if outside connectivity disappears.

This is a future reopening path, not a current requirement.

---

## REST manufacturing lineage

The router/mobile proof triggered experimental Factory branches for large Static REST WMTS deployments.

Production-scale testing exposed the cost of expanding and moving hundreds of thousands of loose files. A later compact `.restmap` seed experiment reduced transport overhead, but REST manufacturing is now **parked with Map Fountain**, not part of the current Offline Map Factory product.

Preserve the work as engineering history unless shared-storage/mobile serving is reopened for a real use case.

---

## Current status matrix

| Capability | Status |
| --- | --- |
| Flint 2 + USB SSD Samba share | ✅ **LIVE-PROVEN** |
| Production-scale TPKX over SMB | ✅ **LIVE-PROVEN** |
| Ethernet / Wi-Fi benchmark baseline | ✅ **LIVE-PROVEN** |
| Windows ArcGIS Earth network TPKX | ✅ **LIVE-PROVEN** |
| Router-hosted Android Static REST WMTS | ✅ **LIVE-PROVEN** |
| Android cache-clear/reopen retest | ✅ **LIVE-PROVEN** |
| Normal personal-phone deployment role | ⏸️ **PARKED** |
| Possible Starlink/basecamp NAS role | 🟡 **FUTURE / NOT YET REOPENED** |
| Operational public-Internet dependency | **NONE BY DESIGN** |

---

## Engineering record

- [Router acceptance record](docs/MAP_FOUNTAIN_ROUTER_ACCEPTANCE_2026-08-17.md)
- [Static REST WMTS Android acceptance](docs/STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md)
- [Acceptance record](docs/ACCEPTANCE_RECORD.md)
- [Technical architecture](docs/TECHNICAL_ARCHITECTURE.md)
- [AI / maintainer restart note](docs/AI_CONTINUITY_RESTART_NOTE.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

---

## Four-project family

1. **[Offline GeoStack](https://github.com/Jim-dc95811/Offline-GeoStack)** — master map manufacturing + field-system integration.
2. **[Rasta Pyramid Factory](https://github.com/Jim-dc95811/Rasta-Pyramid-Factory)** — giant-raster / deep-zoom pyramid manufacturing.
3. **Map Fountain** — LIVE-PROVEN shared-storage/network delivery evidence; currently parked from the normal personal-phone path.
4. **[Android Field Maps + ArcGIS Earth](https://github.com/Jim-dc95811/Android-Field-Maps-and-ArcGIS-Earth-)** — deployment to the user: Android offline maps + Windows ArcGIS Earth field features.

---

## Licensing boundary

Original project software and documentation are MIT-licensed unless otherwise stated. Third-party imagery, ArcGIS Earth, QGIS, router firmware, and source data remain governed by their own licenses and terms.

---

# Map Fountain

> **It worked. We learned from it. Use it when shared storage is actually the right tool.**
