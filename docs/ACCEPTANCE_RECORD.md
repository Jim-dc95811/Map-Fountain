# Map Fountain — Acceptance Record

## Evidence labels

**LIVE-PROVEN** — observed on the real Windows/Android target and accepted by the intended viewer/workflow.

**LIVE-OBSERVED** — behavior directly observed but not yet treated as a full acceptance gate.

**BUILT / SELF-TESTED** — implementation exists and passes internal/static checks but has not yet crossed the live target.

**DESIGNED** — architecture or behavior is planned but not yet built/proven.

---

## 1. PC → Android USB network proof — 2026-08-16

**Status: LIVE-PROVEN**

Target:

- Windows PC
- Motorola Android phone
- Android USB tether enabled
- Windows adapter detected as `Remote NDIS based Internet Sharing Device #2`

Observed PC-side USB IPv4 during the proof:

`10.13.166.115`

Observed Android client IPv4 in server logs:

`10.13.166.67`

Android Chrome successfully opened the Windows-side local test page through the USB-tether network.

This established the private PC ↔ phone IP path before ArcGIS Earth Mobile was involved.

---

## 2. First ArcGIS Earth Mobile WMTS proof — 2026-08-16

**Status: LIVE-PROVEN**

Fixture:

- QGIS-created raster MBTiles
- 174 PNG tiles
- Z0–Z18
- small Jacksonville-area footprint

The first server exposed an EPSG:3857 / GoogleMapsCompatible WMTS service over local HTTP.

ArcGIS Earth Mobile requested actual WMTS tile URLs from the Windows PC and the server returned HTTP `200` responses across multiple zoom levels.

The map displayed on Android.

Outside Internet connectivity was removed and the local map path continued to work.

This proved the central architecture:

```text
MBTiles
→ local tile service
→ USB tether
→ ArcGIS Earth Mobile
```

---

## 3. HTTPS + QR proof — 2026-08-16

**Status: LIVE-PROVEN**

The phone rejected the tested HTTP QR workflow and requested HTTPS.

A local HTTPS branch was created. After removing the target-PC OpenSSL dependency and supplying matching local certificate material, the phone reported success and ArcGIS Earth Mobile displayed the WMTS map over HTTPS.

QR loading then became the practical operator path, eliminating repeated manual typing of the long WMTS GetCapabilities URL.

Important current limitation:

- the bench certificate was tied to the observed PC-side tether address `10.13.166.115`;
- production-grade certificate/IP lifecycle handling remains unfinished.

---

## 4. Selectable MBTiles GUI — v0.2.0 — 2026-08-16

**Status: LIVE-TESTED; DEFECT FOUND**

v0.2.0 replaced the hard-coded small fixture with a GUI that allowed the operator to choose an arbitrary `.mbtiles` file.

Observed defect:

- a different MBTiles was selected;
- ArcGIS Earth Mobile still returned to the original small test map.

Root cause:

- the WMTS layer/service identity and tile URLs remained unchanged between maps;
- ArcGIS Earth Mobile could legitimately reuse stale cached service/tile content.

This was not accepted.

---

## 5. Unique per-map identity — v0.2.1 — 2026-08-16

**Status: LIVE-PROVEN**

v0.2.1 changed every selected MBTiles into a distinct WMTS service from the client’s point of view.

Per-map uniqueness includes:

- service ID derived from file identity;
- unique WMTS layer identifier;
- unique GetCapabilities URL;
- unique REST tile URL path;
- no-cache headers during the test phase.

After the change, the operator confirmed the newly selected map appeared instead of the stale small fixture.

---

## 6. Multiple substantial MBTiles — 2026-08-16

**Status: LIVE-PROVEN**

The operator confirmed ArcGIS Earth Mobile displayed **three different substantial MBTiles** through v0.2.1.

This establishes repeatability beyond the original 174-tile fixture.

---

## 7. Large Lago panorama — 2026-08-16

**Status: LIVE-PROVEN**

A large Lago raster panorama MBTiles was selected through the v0.2.1 GUI and served live to ArcGIS Earth Mobile.

Observed result:

- correct map selected;
- HTTPS WMTS service live;
- Android requested unique per-map tile URLs;
- map displayed on the phone;
- zoom/pan experience was described as smooth when operated deliberately;
- mobile experience closely matched the PC navigation behavior.

This is the current strongest visual proof that Map Fountain is not limited to tiny fixtures.

---

## 8. Current mobile navigation envelope

**Status: LIVE-OBSERVED**

Operator observation after several large-map tests:

> **The key is not trying to zoom or move super fast. It does not like that, but if you are steady it is gold.**

Engineering interpretation:

- deliberate navigation is currently accepted;
- rapid repeated pan/zoom can outrun some part of the mobile delivery/render path;
- the bottleneck has not yet been isolated;
- do not claim that high-speed navigation is solved.

---

## 9. Internet-dependency acceptance

**Status: LIVE-PROVEN FOR THE TESTED PATH**

Outside Internet connectivity was removed during the USB-tether map-service test and ArcGIS Earth Mobile continued to retrieve/display local map content.

The operational path under test is therefore local:

```text
Windows MBTiles / SSD
→ Windows Map Fountain
→ private USB tether
→ Android ArcGIS Earth Mobile
```

No public map server, cloud account, or public Internet connection is required for tile delivery in that path.

---

## Current accepted statement

> **Map Fountain v0.2.1 TEST is LIVE-PROVEN as a selectable Windows raster-MBTiles → HTTPS WMTS → Android USB-tether → ArcGIS Earth Mobile local map-delivery path, with outside Internet removed during testing.**

The current acceptance does not yet include generalized certificate/IP lifecycle handling, Wi-Fi transport, cold-restart acceptance, or unrestricted rapid navigation.
