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

The field architecture is now **router only**. The router remains intentionally dumb: storage, DHCP/local networking, and file sharing. ArcGIS Earth remains the GIS runtime.

See:

- [`README.md`](README.md)
- [`docs/MAP_TANK_TEST_PLAN_2026-08-17.md`](docs/MAP_TANK_TEST_PLAN_2026-08-17.md)
- [`docs/ACCEPTANCE_RECORD.md`](docs/ACCEPTANCE_RECORD.md)
- [`docs/map_fountain_router_architecture_2026-08-17.svg`](docs/map_fountain_router_architecture_2026-08-17.svg)

## Immediate gates

### 1. ArcGIS Earth Ethernet comparison

**Status: next controlled application gate**

Repeat the successful ArcGIS Earth / `ESG1N.tpkx` direct-network test over Ethernet while changing no other major variable.

Compare:

- initial package open behavior;
- time to first useful display;
- pan/zoom responsiveness;
- SMB/TCP byte flow;
- retries/retransmissions;
- Windows caching/read-ahead behavior.

### 2. Wi-Fi ArcGIS Earth navigation characterization

**Status: LIVE-PROVEN basic operation; deeper characterization pending**

The map rendered successfully over Wi-Fi. Next, measure real operator patterns rather than synthetic storage loads:

- deliberate pan;
- progressive deep zoom;
- return to overview;
- long traverse across package coverage;
- repeated close/reopen;
- reconnect after leaving/rejoining Wi-Fi.

Do not optimize the network path unless the real viewer exposes an actual problem.

### 3. Multiple Eaters

**Status: not yet accepted**

Test two or more clients against the same router-attached SSD.

Questions:

- Does one ArcGIS Earth client materially degrade another?
- Does Samba remain stable under simultaneous reads?
- What does the SSD/router path do with independent random reads?
- Is the practical field limit the router, storage device, radio channel, or client behavior?

Do not market multi-client behavior until measured.

### 4. Feeder workflow

**Status: designed**

Create a basecamp-side maintenance tool that can:

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

### 5. ArcGIS Earth Mobile router-only path

**Status: future gate**

Desktop direct-TPKX-over-Samba is proven. Mobile still needs its own real-target acceptance.

Investigate the simplest router-only delivery forms first. Do not add a field GIS server process merely to recreate a capability that the client can obtain more simply.

## Performance baseline

### Ethernet storage benchmark

- random: 25.33 MiB/s
- random p95: 9.98 ms
- four-client aggregate: 51.21 MiB/s
- sequential: 42.58 MiB/s

### Wi-Fi storage benchmark

- random: 5.19 MiB/s
- random p95: 50.56 ms
- four-client aggregate: 5.31 MiB/s
- sequential: 6.14 MiB/s

The synthetic benchmark is a diagnostic baseline, not a substitute for ArcGIS Earth behavior.

## Public documentation / history

- preserve the 2026-08-17 benchmark numbers and evidence hashes;
- keep the router-only architecture drawing at the top of the active repositories;
- publish the successful ArcGIS Earth Wi-Fi proof as the primary Map Fountain milestone;
- retain earlier Windows-hosted WMTS work as development history, not the current field architecture;
- avoid claiming a worldwide first unless stronger historical evidence supports it;
- accurately state that the documented prior-art search did not find a published implementation matching the exact proven router + Samba + ArcGIS Earth + native TPKX chain.

## Non-goals

- turning the consumer router into a GIS computer;
- requiring a field GIS server process for the proven desktop TPKX path;
- requiring public Internet;
- adding cloud accounts or portals to the core path;
- making operators administer network internals unnecessarily;
- copying entire map libraries onto every client when direct local consumption works;
- rewriting proven map-manufacturing components without a verified defect;
- optimizing a guessed bottleneck.

## Governing rule

> **Keep the router dumb. Keep the maps native. Let ArcGIS Earth do the GIS work.**
