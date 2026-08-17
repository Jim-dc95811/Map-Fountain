# Map Fountain Roadmap

## Current state

**v0.2.1 TEST is LIVE-PROVEN** on the 2026-08-16 Windows/Android target for:

- raster MBTiles selected from a Windows PC / attached SSD;
- HTTPS WMTS service over Android USB tether / Remote NDIS;
- ArcGIS Earth Mobile QR ingestion;
- multiple substantial MBTiles;
- operation with outside Internet removed.

That proof remains intact.

A new deployment branch, **Map Tank**, is now **DESIGNED / BENCH TEST PENDING**. It asks whether a consumer router + USB SSD can replace much of the active server hardware/software while preserving practical offline map delivery.

The first physical test router is a **GL.iNet Flint 2 (GL-MT6000)**, received on 2026-08-17.

See [`docs/MAP_TANK_TEST_PLAN_2026-08-17.md`](docs/MAP_TANK_TEST_PLAN_2026-08-17.md).

## Immediate gates — Map Tank

### 1. Ethernet storage baseline

**Status: first physical gate**

Remove Wi-Fi as a variable.

```text
Windows laptop
    ↓ Ethernet
Flint 2
    ↓ USB 3
SSD
```

Use DHCP. Expose a known-good TPKX through the router's normal storage-sharing interface and capture the entire session in Wireshark.

Measure/inspect:

- file-open behavior;
- read sizes and access pattern;
- sequential versus random reads;
- throughput;
- retries/retransmissions;
- caching;
- ArcGIS Earth behavior when opening the network-hosted TPKX if the share path is accepted.

No Map Tank path becomes LIVE-PROVEN until this or a later real-target gate succeeds.

### 2. Wi-Fi comparison

After the Ethernet baseline, change one major variable only:

```text
Ethernet → Wi-Fi
```

Repeat the same TPKX/storage test and compare packet evidence against the Ethernet run.

### 3. Simulated mobile consumption on Windows

If useful, exercise the router/SSD path with a deterministic client before Android.

Profiles may include:

- normal neighboring-tile requests;
- steady pan;
- progressive deep zoom / hawk dive;
- rapid random navigation stress.

The purpose is not to imitate Android rendering. It is to isolate whether the storage/network path can supply map objects fast enough.

### 4. ArcGIS Earth Mobile Map Tank path

Candidate configurations, in preferred investigation order:

1. **Static WMTS directly from router storage** — capabilities XML + raster tile tree, no active GIS server process.
2. **Router storage + thin Android bridge** — only if compatibility logic proves necessary.
3. **Whole-file TPKX transfer/open** — simple package fallback.
4. **PMTiles / byte-range bridge** — fallback if remote SQLite/MBTiles access is awkward.

These are experimental directions, not current product claims.

## Feeder / Eater workflow

### Eaters

Field clients consume the Map Tank read-only where practical.

Potential Eaters:

- ArcGIS Earth Windows laptops;
- ArcGIS Earth Mobile phones/tablets;
- multiple simultaneous clients.

### Feeder

At basecamp, a Feeder client should eventually:

- self-discover the Map Tank;
- scan the current SSD inventory;
- compare against an approved master library;
- copy new products;
- replace updated products;
- retire obsolete products where appropriate;
- verify completion;
- report `MAP TANK CURRENT`.

Changing the map library should not require router reconfiguration. Operators should be able to add a finished map file or swap in a different preloaded SSD.

## Existing Windows Map Fountain gates

The Windows/USB-tether path remains a valid proven branch and may continue in parallel.

### General HTTPS certificate / tether-IP handling

The live v0.2.1 bench build used certificate material tied to the observed PC-side USB-tether address `10.13.166.115`.

If the Windows Map Fountain branch is productized further, remove that fixed-address dependency without requiring operators to become certificate administrators.

Requirements:

- detect the current USB-tether IP automatically;
- create or select matching local HTTPS identity safely;
- preserve Android trust in a predictable way;
- never commit private keys to GitHub;
- remain fully operable without public Internet access.

### Cold restart / reconnect acceptance

Test deliberately:

```text
phone disconnect
server stop
PC restart if useful
phone reconnect
USB tether ON
Map Fountain start
scan/add service
map returns
```

Record exactly what Android/ArcGIS Earth Mobile remembers versus what must be re-added.

### Larger geographic MBTiles stress test

The mobile path is already proven on multiple substantial MBTiles and the Lago raster panorama.

Next stress gate should use a large real geographic MBTiles and test:

- deliberate deep zoom;
- long pan across the map;
- return to overview;
- repeated map switching;
- runtime stability over an extended session.

### Mobile navigation envelope

Current live rule:

> deliberate navigation is smooth; rapid repeated pan/zoom can outrun the current path.

Future work may measure whether the limiting factor is:

- Android rendering;
- ArcGIS Earth Mobile request behavior;
- USB-tether throughput;
- SQLite open/query overhead;
- Python request handling;
- tile cache behavior.

Do not optimize blindly until live measurements identify the bottleneck.

### Reuse SQLite connections / bounded server optimization

Current server opens the MBTiles SQLite database read-only for each tile request. That kept the first implementation simple and safe.

Potential optimization:

- per-thread or pooled read-only SQLite connections;
- bounded memory cache for recent tile bytes;
- request timing/status instrumentation.

Only change this after a reproducible performance need is established.

## Map library / multi-map workflow

Current v0.2.1 serves one selected MBTiles at a time.

Possible future UI:

- map library list;
- current-map switch without relaunching the GUI;
- map identity shown clearly;
- optional multiple WMTS layers served concurrently;
- QR/service index page for available maps.

Map Tank may simplify this by making the SSD itself the persistent library while client software discovers the available finished products.

Do not make the beginner workflow complex merely because multi-map serving is technically possible.

## Viewer expansion

ArcGIS Earth Mobile is the current live acceptance viewer.

Later tests may include other standards-compatible WMTS clients, but Map Fountain should not compromise the proven ArcGIS Earth Mobile path merely to claim broad compatibility.

## Packaging

For the Windows Map Fountain branch, after certificate/IP lifecycle is solved and cold restart is proven:

- package as a normal Windows operator tool;
- minimize external dependencies;
- preserve no-install / no-public-Internet operation where practical;
- document Windows firewall behavior;
- create a clean acceptance package and versioned release.

For Map Tank, productization should wait until the bit flow and real ArcGIS Earth behavior are measured.

## Non-goals

- becoming a full GIS server;
- adding accounts/cloud dependencies;
- requiring an ArcGIS Portal for the core local path;
- copying an entire large map to the phone when live local tile delivery is the objective;
- inventing a proprietary mobile viewer;
- pretending rapid-navigation limits are solved before they are measured;
- publishing private TLS keys;
- turning the consumer router into a complicated GIS computer.

## Governing rule

> **Keep the server dumb, local, and predictable. Let the viewer ask for what it needs.**

For Map Tank:

> **At basecamp, feed the tank. In the field, drink from it.**
