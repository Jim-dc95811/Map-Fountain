# Map Tank — Consumer Router + USB SSD Test Branch

**Status: DESIGNED / BENCH TEST PENDING — 2026-08-17**

Map Tank is a new Map Fountain deployment experiment built around a deliberately simple field appliance:

```text
USB SSD full of finished map products
        ↓
consumer Wi-Fi router
        ↓
private local network
        ↓
ArcGIS Earth clients
```

The first physical test router is a **GL.iNet Flint 2 (GL-MT6000)**. The hardware was received on 2026-08-17. No Map Tank data path is called live-proven until controlled bench evidence is captured.

## Design goal

Keep the router dumb.

The router should provide only:

- local network access;
- USB storage access;
- ordinary file/HTTP-style serving where useful.

GIS intelligence should remain in the map-manufacturing tools, ArcGIS Earth, or a very thin compatibility layer only if one proves necessary.

The desired public workflow is closer to an appliance than a server project:

```text
plug in preloaded SSD
connect to Map Tank
use maps
```

A new map library should not require router reconfiguration. New finished products can be added to the SSD, or the entire SSD can be swapped for another preloaded library.

## Feeder / Eater model

Map Tank separates field consumption from basecamp maintenance.

### Eaters

Field clients are **Eaters**.

Examples:

- Windows laptop running ArcGIS Earth;
- Android device running ArcGIS Earth Mobile;
- multiple clients using the same Map Tank concurrently.

The intended field relationship is read-only:

```text
Map Tank SSD
    ↓
private local network
    ↓
Eaters consume maps
```

### Feeder

At basecamp, a **Feeder** client maintains the SSD map library.

Longer-term concept:

```text
approved master map library
        ↓
Map Tank Feeder
        ↓
self-discover Map Tank
        ↓
compare inventory
        ↓
add new maps / replace updated maps / retire obsolete maps
        ↓
verify
        ↓
MAP TANK CURRENT
```

The router itself does not need to understand Feeder versus Eater. Those roles belong to client-side software and permissions/workflow.

## First controlled bench sequence

### Gate 1 — Ethernet storage baseline

Remove Wi-Fi as a variable.

```text
Windows laptop
    ↓ Ethernet
Flint 2
    ↓ USB 3
SSD
```

Use DHCP. Do not manually assign a static IP to the laptop.

Planned steps:

1. Plug a known-good SSD into the Flint 2 USB 3 port.
2. Expose the map folder through the router's normal storage-sharing interface.
3. Connect the Windows laptop to a Flint 2 LAN port.
4. Confirm the share is visible in Windows File Explorer.
5. Start Wireshark on the Ethernet adapter.
6. Exercise a known-good TPKX directly from the shared SSD.
7. Capture file-open/read behavior, throughput, retries, caching, and access pattern.
8. Open the same network-hosted TPKX in ArcGIS Earth if the share path is accepted.
9. Save the capture for packet-level analysis.

### Gate 2 — Wi-Fi comparison

Change one major variable only:

```text
Ethernet
   ↓
Wi-Fi
```

Repeat the same storage and ArcGIS Earth test without changing the SSD/map package. Compare throughput, latency, retransmissions, and application behavior against the Ethernet baseline.

### Gate 3 — simulated mobile consumption on Windows

If useful, run a Python client that behaves like a tile-hungry viewer before involving Android.

Candidate profiles:

- normal neighboring-tile viewing;
- steady pan;
- progressive deep-zoom / "hawk dive";
- rapid random navigation stress.

The simulator does not reproduce Android rendering or ArcGIS Earth Mobile internals. Its purpose is to isolate whether the Map Tank storage/network path can supply the requested map objects at the required rate.

### Gate 4 — ArcGIS Earth Mobile

Only after the storage/network path is understood, test the real mobile runtime.

Potential delivery forms under investigation:

1. **Static WMTS from router storage** — capabilities XML plus ordinary raster tile files, with no active GIS server process.
2. **Router storage + thin Android bridge** — if a compatibility layer is required.
3. **Whole-file TPKX transfer/open** — simple fallback for package-based mobile use.
4. **PMTiles / byte-range architecture** — fallback if remote SQLite/MBTiles access proves awkward.

None of these Map Tank mobile paths are live-proven yet.

## Relationship to existing Map Fountain proof

Map Tank does **not** invalidate the existing Windows Map Fountain v0.2.1 TEST proof.

The following remains LIVE-PROVEN:

```text
Windows MBTiles
→ Map Fountain HTTPS WMTS
→ Android USB tether
→ ArcGIS Earth Mobile
```

Map Tank asks a different engineering question:

> How much of the active server hardware/software can be removed while preserving practical offline multi-device map delivery?

If the consumer-router path succeeds, Map Fountain may evolve from one Windows program into a broader family of simple local-delivery methods.

## Governing rules

- No operational dependence on public Internet.
- Keep the router dumb, local, and predictable.
- Prefer DHCP for consumers.
- Field consumption should be read-only where practical.
- Change one major variable at a time during acceptance testing.
- Wireshark/packet evidence outranks assumptions.
- Do not promote a Map Tank path from DESIGNED to LIVE-PROVEN until it succeeds on the real target.

> **At basecamp, feed the tank. In the field, drink from it.**
