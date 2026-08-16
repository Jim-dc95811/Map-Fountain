# Map Fountain — Project Status — 2026-08-16

This is the founding continuity checkpoint for the standalone Map Fountain repository.

## Executive state

Map Fountain crossed from concept to **LIVE-PROVEN local mobile map delivery** on 2026-08-16.

Current proven chain:

```text
raster MBTiles on Windows PC / SSD
→ Map Fountain v0.2.1 TEST
→ local HTTPS WMTS
→ Android USB tether / Remote NDIS
→ ArcGIS Earth Mobile
```

Outside Internet connectivity was removed during the test and the local map path remained functional.

---

## Why the repository exists

The capability began as a mobile experiment inside Offline GeoStack.

It became a separate project because it now has its own:

- Windows GUI;
- network architecture;
- WMTS implementation;
- HTTPS/QR workflow;
- mobile operating rules;
- acceptance evidence;
- future Wi-Fi/appliance direction.

Map Fountain therefore deserves its own engineering record rather than remaining one subsection inside Offline GeoStack.

---

## Current code

`Rasta USB Map Fountain v0.2.1 TEST`

The `Rasta` title is historical working lineage. The standalone project identity is **Map Fountain**.

Current source files:

- `Map_Fountain_GUI.py`
- `Map_Fountain_Server.py`
- `START MAP FOUNTAIN.bat`

---

## Current live proofs

### USB network

Windows detected Android tethering as Remote NDIS and the phone reached the PC over the private USB network.

Observed proof addresses:

- PC: `10.13.166.115`
- Android: `10.13.166.67`

### WMTS

Android / ArcGIS Earth Mobile requested actual raster tiles at multiple zooms and the Windows server returned `200` responses.

### HTTPS

Local HTTPS WMTS was accepted and displayed by ArcGIS Earth Mobile.

### QR

The working service URL could be generated as a QR and scanned through ArcGIS Earth Mobile Add Data → QR Code.

### Offline

Public Internet was removed while the private USB link remained active. Local map delivery continued.

### Multiple maps

Three different substantial raster MBTiles were displayed successfully.

### Lago panorama

A large Lago panorama MBTiles displayed smoothly on the phone and behaved similarly to the desktop pyramid-viewing experience when navigation was deliberate.

---

## Important failure that shaped v0.2.1

v0.2.0 allowed the operator to choose a different MBTiles, but ArcGIS Earth Mobile could still return to the original small test map.

Cause:

- same WMTS layer identity;
- same tile URL pattern;
- stale client cache reuse.

v0.2.1 fixed this with a unique service ID and unique tile URLs derived from the selected MBTiles identity.

That fix was immediately accepted live.

---

## Current operator rule

> **Do not whip the mobile view around. Deliberate pan/zoom is smooth; rapid repeated navigation can outrun the current path.**

This is a live-observed operating envelope, not a permanent design assumption.

---

## Current HTTPS limitation

The successful bench certificate was tied to the PC tether address:

`10.13.166.115`

The public GitHub repo intentionally does not include the private server key.

General automatic certificate/IP lifecycle handling is the highest-priority productization task.

---

## Current input boundary

The current server expects:

- standard raster MBTiles;
- PNG or JPEG raster tile payloads;
- Web Mercator / Google-compatible tile scheme for the current WMTS profile.

It is not a vector-tile server and it does not rerender source GIS layers.

---

## Relationship to TPKX Map Factory

Map Fountain changed the value of the Factory’s MBTiles stage.

Before Map Fountain, normal Factory MBTiles could be treated as disposable intermediate material on the way to TPKX.

After Map Fountain:

```text
TPKX → direct local ArcGIS Earth package
MBTiles → local Map Fountain service
Both → preserve both deployment paths
```

This directly motivated TPKX Map Factory v1.2 TEST output selection.

---

## Relationship to Rasta Pyramid Factory

Rasta can manufacture arbitrary giant imagery into a multiscale raster MBTiles pyramid.

Map Fountain can then deliver that MBTiles live to ArcGIS Earth Mobile.

The large Lago panorama was the first strong visual demonstration of that relationship on Android.

---

## Next gates

1. generalize HTTPS certificate/IP handling;
2. cold restart/reconnect acceptance;
3. extended large geographic map session;
4. measure rapid-navigation bottleneck before optimization;
5. evaluate Wi-Fi transport;
6. package a clean normal-user Windows build after the above gates.

---

## Governing evidence rule

> **The architecture is proven. Productization is not finished. Preserve that distinction.**
