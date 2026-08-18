# Map Fountain — AI / Maintainer Restart Note

## Current project identity

**Map Fountain is a LIVE-PROVEN router/storage delivery experiment that is currently PARKED from the primary personal-phone deployment path.**

Do not interpret `PARKED` as failure.

It proved both of its core runtime paths. The larger project then found a simpler normal-user mobile deployment: native TPKX directly on removable phone storage.

---

## Proven Windows path

```text
native TPKX on USB SSD
→ GL.iNet Flint 2
→ Samba / SMB
→ Ethernet or Wi-Fi
→ Windows
→ ArcGIS Earth
```

Large accepted specimen:

- `ESG1N.tpkx`
- 26,174,899,216 bytes by benchmark script
- 25,561,426 KB Windows File Explorer identification

ArcGIS Earth opened the network-hosted TPKX over Wi-Fi and rendered/navigated it successfully.

---

## Proven Android router path

Accepted flavor:

> **Static REST WMTS**

```text
Static REST WMTS folder on USB SSD
→ GL.iNet Flint 2
→ local HTTPS/WebDAV exact-file GET
→ Wi-Fi
→ Android
→ ArcGIS Earth Mobile
```

Observed acceptance sequence:

- Android reached the Flint HTTPS endpoint;
- exact file GET from SSD succeeded;
- `WMTSCapabilities.xml` exact-file GET succeeded;
- ArcGIS Earth Mobile accepted the URL and rendered the map;
- ArcGIS Earth app cache was cleared;
- app was force-stopped/reopened;
- the same router-hosted map rendered again.

No Python on Android. No helper app. No QGIS Server. No Windows map server. No Raspberry Pi.

---

## Current deployment direction moved elsewhere

The preferred personal-phone path is now:

```text
TPKX
→ microSD card
→ Android
→ ArcGIS Field Maps / ArcGIS Earth
```

That work lives in:

`Jim-dc95811/Android-Field-Maps-and-ArcGIS-Earth-`

Do not reinsert Map Fountain into that normal-user path simply because this repo contains a successful router proof.

---

## Why Map Fountain is parked

The target users often carry personal Android phones.

Direct removable storage removes:

- router association;
- network dependency;
- service URLs;
- QR service loading;
- server-shaped concepts;
- shared-storage setup.

If local TPKX solves the job, the simpler path wins.

---

## Static REST manufacturing branch

Map Fountain's Android proof led to large Static REST WMTS manufacturing experiments.

A production-scale v1.3 Factory run exposed serious file-count/packaging overhead with hundreds of thousands of expanded files.

`TPKX_MAP_FACTORY_v1_4_0_TEST` then moved the experimental transport to a compact `.restmap` seed that expands the runtime WMTS tree at the final SSD.

Small lifecycle fixture: SELF-TESTED.

Current disposition: preserve the branch, but do not continue optimizing it merely because it exists. Reopen only if a real Map Fountain deployment requires it.

---

## Possible future role — Starlink / basecamp NAS

The strongest likely reopening path is:

```text
Starlink
→ Flint 2 WAN
→ USB SSD
→ SMB / Wi-Fi / Ethernet
→ basecamp laptops / local clients
```

In that role Map Fountain becomes a poor-man's NAS / incident map reservoir.

Useful doctrine:

- outside Internet can enhance manufacturing/refresh;
- the local SSD/LAN still works if Starlink disappears;
- the router remains dumb;
- map products remain ordinary files;
- shared storage is used because shared storage is actually useful.

This role is **FUTURE / NOT YET REOPENED**.

---

## Windows benchmark baseline

Ethernet:

- random 25.33 MiB/s
- random p95 9.98 ms
- four-client aggregate 51.21 MiB/s
- sequential 42.58 MiB/s

Wi-Fi:

- random 5.19 MiB/s
- random p95 50.56 ms
- four-client aggregate 5.31 MiB/s
- sequential 6.14 MiB/s

Do not call cached/read-ahead rates raw router wire speed.

---

## Evidence fingerprints — Windows acceptance

```text
Ethernet benchmark screenshot
710e19a0676ada1729a35e13693b8ae81d0527fc3ba654a2da32288ac58244af

Ethernet PCAP
3eda0dc91dee83ac12a96912d8f7264e846c7393c3983de34970b5571a622f0f

Wi-Fi benchmark screenshot
631af7d06f433964175e1c3dc414767cc4c08f98af006406d8068be3b081ba3f

Wi-Fi PCAP
67db0a4dfee9519f933f0fc2e550da69634b293c815cd4b2d81413b38c60f1d4

ArcGIS Earth Wi-Fi success screenshot
8592abb26f9025baf665e4c4174670ba3a2bb433db96cbd092dd27355a9fd840
```

---

## Historical chronology

### 2026-08-16 — active Windows WMTS precursor

Windows served raster MBTiles through an active local HTTPS WMTS process to ArcGIS Earth Mobile over Android USB tether. This proved local/offline mobile WMTS compatibility but is not the final router architecture.

### 2026-08-17 — Windows router-only breakthrough

Flint 2 + USB SSD + Samba served a production-scale native TPKX directly to Windows ArcGIS Earth over Wi-Fi.

### 2026-08-17 — Android router-only breakthrough

Flint 2 built-in local HTTPS/WebDAV exact-file delivery served a pre-generated Static REST WMTS folder directly from the USB SSD to ArcGIS Earth Mobile. The mobile map rendered again after ArcGIS Earth cache clear and app restart.

### 2026-08-18 — primary personal-phone direction simplified

Direct TPKX-on-microSD deployment became the current mobile direction. Map Fountain moved to PROVEN / PARKED reference status.

---

## Do not regress

- Do not call Map Fountain a failed branch.
- Do not make it mandatory phone infrastructure after the project deliberately simplified away from it.
- Do not add a field GIS server unless a real future use case proves one is necessary.
- Do not revive Raspberry Pi / Pi-server architecture by inertia.
- Do not make public Internet connectivity mandatory.
- Do not turn expanded WMTS trees into the canonical compact archive format.
- Do not optimize the REST branch without an active need.
- Do not lose the Windows SMB and Android Static REST acceptance evidence.
- Do not turn incidental multi-client capability into a supported product claim until measured.

---

## Reopen conditions

Resume active Map Fountain engineering only when at least one is true:

1. Starlink/basecamp shared storage is being deliberately built;
2. multiple clients demonstrably need one shared local map reservoir;
3. direct removable storage fails a real operational requirement that shared storage solves better.

Then resume controlled one-variable-at-a-time testing.

---

## Cold-start reading order

1. `README.md`
2. this file
3. `docs/MAP_FOUNTAIN_ROUTER_ACCEPTANCE_2026-08-17.md`
4. `docs/STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md`
5. `docs/ACCEPTANCE_RECORD.md`
6. `ROADMAP.md`
7. `CHANGELOG.md`
8. Android deployment repository for current phone work

---

## Governing principle

> **Preserve the proof. Reopen the appliance only when shared storage is actually the better tool.**
