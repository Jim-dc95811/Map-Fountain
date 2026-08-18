# Contributing to Map Fountain

Map Fountain is evidence-driven. A plausible architecture is not enough; the real target decides acceptance.

## Current project state

**LIVE-PROVEN / PARKED from the primary personal-phone deployment path.**

The project proved both:

```text
Windows:
USB SSD → Flint 2 → SMB → ArcGIS Earth → native TPKX

Android router experiment:
Static REST WMTS → Flint 2 local HTTPS → ArcGIS Earth Mobile
```

The larger project then simplified normal personal-phone deployment to direct TPKX on microSD.

Current mobile deployment work belongs in:

`Jim-dc95811/Android-Field-Maps-and-ArcGIS-Earth-`

## Before changing architecture or documentation

Read:

1. `README.md`
2. `docs/MAP_FOUNTAIN_ROUTER_ACCEPTANCE_2026-08-17.md`
3. `docs/STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md`
4. `docs/ACCEPTANCE_RECORD.md`
5. `docs/AI_CONTINUITY_RESTART_NOTE.md`
6. `ROADMAP.md`
7. current Offline GeoStack README

## Reopen before extending

Do not add new Map Fountain features merely because the code or architecture is interesting.

Active engineering should resume only when a real use case reopens the appliance, such as:

- Starlink/basecamp shared storage / poor-man's NAS;
- measured multi-client shared-map requirement;
- a real failure of direct removable storage that shared storage solves better.

## Preserve proof status

Use explicit labels:

- DESIGNED
- BUILT / SELF-TESTED
- LIVE-OBSERVED
- LIVE-PROVEN

Do not silently promote or demote a path.

`PARKED` means a live-proven capability is not currently the preferred deployment path. It does not mean the proof failed.

## Do not regress

- public Internet must not become a core dependency;
- native TPKX must remain native on the proven Windows router path;
- ordinary clients should stay on DHCP;
- field consumption should remain read-only where practical;
- packet evidence and real-viewer behavior outrank assumptions;
- cached/read-ahead throughput must not be mislabeled as raw router speed;
- historical Windows WMTS source remains lineage, not the active product;
- the current personal-phone architecture must not be forced back through Map Fountain without a real operational reason;
- REST manufacturing optimization should remain paused unless Map Fountain is deliberately reopened.

## Evidence for reopened changes

For changes affecting runtime behavior, include as applicable:

- exact router/model/firmware context;
- exact client/viewer and operating system;
- exact map artifact identity and Windows File Explorer size when relevant;
- Ethernet versus Wi-Fi transport;
- Starlink/public Internet present versus removed if testing the future basecamp role;
- Wireshark/packet evidence when network behavior matters;
- screenshots/video when visual behavior matters;
- what was directly observed versus inferred.

## Security

Never include live credentials, private keys, confidential map products, router administrator secrets, or sensitive packet contents in public commits/issues.

## Governing rule

> **Preserve the proof. Reopen the project only when shared storage is actually the better tool.**
