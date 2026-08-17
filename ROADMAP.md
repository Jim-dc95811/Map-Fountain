# Map Fountain Roadmap

## Current state

**Router-only Map Fountain is LIVE-PROVEN on both Windows ArcGIS Earth and ArcGIS Earth Mobile.**

### Windows

```text
USB SSD
→ GL.iNet Flint 2
→ Samba / SMB
→ Ethernet or Wi-Fi
→ Windows
→ ArcGIS Earth
→ native network-hosted TPKX
```

### Android

```text
Static REST WMTS folder
→ USB SSD
→ GL.iNet Flint 2 local HTTPS
→ Wi-Fi
→ Android
→ ArcGIS Earth Mobile
```

The router remains intentionally dumb: storage, DHCP/private networking, Samba, and ordinary exact-file HTTPS delivery. No active GIS server is required in the accepted field architecture.

See:

- [`README.md`](README.md)
- [`docs/STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md`](docs/STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md)
- [`docs/MAP_FOUNTAIN_ROUTER_ACCEPTANCE_2026-08-17.md`](docs/MAP_FOUNTAIN_ROUTER_ACCEPTANCE_2026-08-17.md)
- [`docs/ACCEPTANCE_RECORD.md`](docs/ACCEPTANCE_RECORD.md)

---

# Immediate gate — production Static REST WMTS manufacturing

Android consumption has passed. The next problem is not “can Android use the router?” It can.

The next problem is making the accepted Android product practical at large scale.

## Giant-folder rule

Static REST WMTS removes the active field GIS server by expanding the map into individual raster tile files.

For large maps this means very large directory trees.

Treat the expanded WMTS tree as a **deployment artifact**, not the preferred compact master/archive format.

Keep:

- MBTiles as compact raster master/interchange;
- TPKX as compact Windows deployment product;
- Static REST WMTS as expanded Android deployment product.

## Factory work to freeze next

1. Add/select **Static REST WMTS** output mode.
2. Use short map IDs suitable for deep paths and QR codes.
3. Preflight tile count.
4. Preflight raster payload size and destination free space.
5. Support direct-to-removable-SSD output so millions of files do not need a second copy operation.
6. Generate unique/versioned service identities to prevent stale mobile-cache collisions.
7. Generate `WMTSCapabilities.xml` automatically.
8. Convert MBTiles/TMS rows to WMTS top-origin rows automatically when deriving from MBTiles.
9. Generate QR code automatically for the final capabilities URL.
10. Verify matrix limits, tile count, representative paths, and capabilities after build.
11. Provide a clean whole-map delete/replace workflow.

The accepted runtime contract is frozen. The final Factory UI and exact deployment root-folder naming are not yet frozen.

---

# Follow-on Android gates

## Larger and denser map

Run the same accepted Static REST WMTS architecture with a materially larger map and denser adjacent coverage.

Observe:

- time to first useful display;
- progressive zoom;
- deliberate pan;
- rapid pan/zoom;
- recovery after stalls;
- repeated visits to cached and uncached areas.

## Navigation characterization

Current live observation:

- slow, deliberate movements work;
- rapid gestures can cause stalls or erratic display behavior.

Do not guess the cause. Distinguish among:

- many-small-file HTTPS overhead;
- Wi-Fi latency/throughput;
- ArcGIS Earth Mobile request concurrency/cache behavior;
- tile-pyramid density.

## Cold/reconnect behavior

Test:

- close/reopen ArcGIS Earth Mobile;
- phone Wi-Fi leave/rejoin;
- router reboot;
- SSD detach/reattach only under controlled conditions;
- map reload after cache clear.

## Multiple Eaters

Test two or more ArcGIS Earth clients against the same router-attached SSD before making a supported multi-client claim.

---

# Windows follow-on gates

## ArcGIS Earth Ethernet application comparison

Repeat the successful ArcGIS Earth / `ESG1N.tpkx` direct-network test over Ethernet while changing no other major variable.

Compare initial open behavior, time to first useful display, pan/zoom responsiveness, SMB/TCP byte flow, and caching/read-ahead behavior.

## Windows Wi-Fi navigation characterization

The map already rendered successfully over Wi-Fi. Characterize real operator patterns rather than synthetic throughput alone.

---

# Feeder workflow

After deployment behavior is stable, build the basecamp maintenance path:

```text
find Map Fountain
→ inspect SSD inventory
→ compare with approved compact master library
→ generate/copy needed deployment products
→ replace updated maps
→ retire obsolete maps when instructed
→ verify
→ MAP FOUNTAIN CURRENT
```

Changing map inventory must not require GIS-specific router configuration.

---

# Performance baseline — Windows SMB path

### Ethernet

- random: **25.33 MiB/s**
- random p95: **9.98 ms**
- four-client aggregate: **51.21 MiB/s**
- sequential: **42.58 MiB/s**

### Wi-Fi

- random: **5.19 MiB/s**
- random p95: **50.56 ms**
- four-client aggregate: **5.31 MiB/s**
- sequential: **6.14 MiB/s**

The synthetic benchmark is a diagnostic baseline, not a substitute for ArcGIS Earth behavior.

---

# Non-goals

- turning the consumer router into a GIS computer;
- requiring a field GIS server process;
- requiring public Internet;
- adding cloud accounts or portals to the core path;
- requiring Python or third-party helper apps on Android;
- turning expanded WMTS trees into the canonical compact archive format;
- making operators copy millions of files unnecessarily;
- optimizing a guessed bottleneck;
- rewriting proven Windows TPKX delivery without a verified defect.

---

## Governing rule

> **Keep the router dumb. Keep the masters compact. Expand only the product the Android client actually needs.**
