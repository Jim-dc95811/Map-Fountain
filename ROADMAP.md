# Map Fountain Roadmap

## Current state

**v0.2.1 TEST is LIVE-PROVEN** on the 2026-08-16 Windows/Android target for:

- raster MBTiles selected from a Windows PC / attached SSD;
- HTTPS WMTS service over Android USB tether / Remote NDIS;
- ArcGIS Earth Mobile QR ingestion;
- multiple substantial MBTiles;
- operation with outside Internet removed.

The next work is not to re-prove the idea. It is to turn the proven bench architecture into a clean repeatable product.

## Near-term gates

### 1. General HTTPS certificate / tether-IP handling

**Status: highest priority**

The live v0.2.1 bench build used certificate material tied to the observed PC-side USB-tether address `10.13.166.115`.

Next build should remove that fixed-address dependency without requiring operators to become certificate administrators.

Requirements:

- detect the current USB-tether IP automatically;
- create or select matching local HTTPS identity safely;
- preserve Android trust in a predictable way;
- never commit private keys to GitHub;
- remain fully operable without public Internet access.

### 2. Cold restart / reconnect acceptance

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

### 3. Larger geographic MBTiles stress test

The mobile path is already proven on multiple substantial MBTiles and the Lago raster panorama.

Next stress gate should use a large real geographic MBTiles and test:

- deliberate deep zoom;
- long pan across the map;
- return to overview;
- repeated map switching;
- runtime stability over an extended session.

### 4. Mobile navigation envelope

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

### 5. Reuse SQLite connections / bounded server optimization

Current server opens the MBTiles SQLite database read-only for each tile request. That kept the first implementation simple and safe.

Potential optimization:

- per-thread or pooled read-only SQLite connections;
- bounded memory cache for recent tile bytes;
- request timing/status instrumentation.

Only change this after a reproducible performance need is established.

## Transport expansion

### Wi-Fi Map Fountain

**Status: designed, not yet live-proven**

The same conceptual service can move from USB tether to a local Wi-Fi link:

```text
PC / appliance + SSD
        ↓
local Wi-Fi
        ↓
HTTPS WMTS
        ↓
ArcGIS Earth Mobile
```

The original longer-term field concept remains a small dedicated map appliance with local storage and no operational cloud dependency.

USB is currently the live-proven transport because one cable provides a simple private network path and can also power/charge the phone.

## Map library / multi-map workflow

Current v0.2.1 serves one selected MBTiles at a time.

Possible future UI:

- map library list;
- current-map switch without relaunching the GUI;
- map identity shown clearly;
- optional multiple WMTS layers served concurrently;
- QR/service index page for available maps.

Do not make the beginner workflow complex merely because multi-map serving is technically possible.

## Viewer expansion

ArcGIS Earth Mobile is the current live acceptance viewer.

Later tests may include other standards-compatible WMTS clients, but Map Fountain should not compromise the proven ArcGIS Earth Mobile path merely to claim broad compatibility.

## Packaging

After certificate/IP lifecycle is solved and cold restart is proven:

- package as a normal Windows operator tool;
- minimize external dependencies;
- preserve no-install / no-public-Internet operation where practical;
- document Windows firewall behavior;
- create a clean acceptance package and versioned release.

## Non-goals

- becoming a full GIS server;
- adding accounts/cloud dependencies;
- requiring an ArcGIS Portal for the core local path;
- copying an entire large map to the phone when live local tile delivery is the objective;
- inventing a proprietary mobile viewer;
- pretending rapid-navigation limits are solved before they are measured;
- publishing private TLS keys.

## Governing rule

> **Keep the server dumb, local, and predictable. Let the viewer ask for tiles.**
