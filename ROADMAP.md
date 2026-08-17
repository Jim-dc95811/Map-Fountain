# Map Fountain Roadmap

## Current state

**Router-only Map Fountain is LIVE-PROVEN on the 2026-08-17 Windows / ArcGIS Earth target.**

Proven chain:

```text
USB SSD
→ GL.iNet Flint 2
→ Samba / SMB
→ Ethernet or Wi-Fi
→ Windows
→ ArcGIS Earth
→ native network-hosted TPKX
```

The production-scale `ESG1N.tpkx` package was benchmarked through the router over Ethernet and Wi-Fi, then opened directly from the router share and rendered interactively in ArcGIS Earth over Wi-Fi.

The field architecture is **router only**. The router remains intentionally dumb: storage, DHCP/local networking, and file sharing. ArcGIS Earth remains the GIS runtime.

See:

- [`README.md`](README.md)
- [`docs/MAP_FOUNTAIN_ROUTER_ACCEPTANCE_2026-08-17.md`](docs/MAP_FOUNTAIN_ROUTER_ACCEPTANCE_2026-08-17.md)
- [`docs/ACCEPTANCE_RECORD.md`](docs/ACCEPTANCE_RECORD.md)
- [`docs/arcgis_system_router_flowchart_2026-08-17.svg`](docs/arcgis_system_router_flowchart_2026-08-17.svg)

## Immediate gate — Android

### ArcGIS Earth Mobile on the router-only architecture

**Status: NEXT ACCEPTANCE GATE**

The Windows direct-TPKX-over-Samba path is proven. Android must now be tested against the same router-attached SSD without reviving a field GIS-server appliance by default.

Start from the simplest client-compatible possibilities and let ArcGIS Earth Mobile decide acceptance.

Questions to answer:

- Can ArcGIS Earth Mobile consume a useful map directly from router-attached storage?
- Which native or standards-based input path does the Android client actually accept from the private Wi-Fi network?
- Can the map remain on the SSD instead of being copied wholesale to the phone?
- What, if any, thin compatibility layer is truly required?
- Can the result operate with outside Internet removed?

Do not add server complexity before the real mobile target demonstrates a need.

## Follow-on gates

### ArcGIS Earth Ethernet application comparison

Repeat the successful ArcGIS Earth / `ESG1N.tpkx` direct-network test over Ethernet while changing no other major variable.

Compare initial open behavior, time to first useful display, pan/zoom responsiveness, SMB/TCP byte flow, and caching/read-ahead behavior.

### Wi-Fi ArcGIS Earth navigation characterization

The map rendered successfully over Wi-Fi. Characterize real operator patterns:

- deliberate pan;
- progressive deep zoom;
- return to overview;
- long traverse across package coverage;
- close/reopen;
- Wi-Fi leave/rejoin.

### Multiple Eaters

Test two or more clients against the same router-attached SSD before making any supported multi-client claim.

### Feeder workflow

After consumption behavior is stable, build the basecamp maintenance path:

```text
find Map Fountain
→ inspect SSD inventory
→ compare with approved master library
→ copy new maps
→ replace updated maps
→ retire obsolete maps when instructed
→ verify
→ MAP FOUNTAIN CURRENT
```

Changing map inventory must not require GIS-specific router configuration.

## Performance baseline

### Ethernet storage benchmark

- random: **25.33 MiB/s**
- random p95: **9.98 ms**
- four-client aggregate: **51.21 MiB/s**
- sequential: **42.58 MiB/s**

### Wi-Fi storage benchmark

- random: **5.19 MiB/s**
- random p95: **50.56 ms**
- four-client aggregate: **5.31 MiB/s**
- sequential: **6.14 MiB/s**

The synthetic benchmark is a diagnostic baseline, not a substitute for ArcGIS Earth behavior.

## Public documentation / history

- keep the canonical Factory / PC / Android router-only flowchart at the top of all three active repositories;
- preserve the 2026-08-17 benchmark numbers and evidence hashes;
- preserve the successful ArcGIS Earth Wi-Fi proof as the primary Map Fountain milestone;
- retain the 2026-08-16 Windows-hosted WMTS work as development history, not the current field architecture;
- use **Map Fountain** as the current product name;
- use the historical `MAP_TANK_FIRST_BENCH...` name only when referring to that exact benchmark artifact;
- do not claim a worldwide first without stronger historical evidence;
- accurately state that the documented prior-art search did not find a published implementation matching the exact proven router + Samba + ArcGIS Earth + native TPKX chain.

## Non-goals

- turning the consumer router into a GIS computer;
- requiring a field GIS server process for the proven desktop TPKX path;
- requiring public Internet;
- adding cloud accounts or portals to the core path;
- making operators administer network internals unnecessarily;
- rewriting proven map-manufacturing components without a verified defect;
- optimizing a guessed bottleneck.

## Governing rule

> **Keep the router dumb. Keep the maps native. Let ArcGIS Earth do the GIS work.**
