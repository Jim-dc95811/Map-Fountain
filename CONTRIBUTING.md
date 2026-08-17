# Contributing to Map Fountain

Map Fountain is evidence-driven. A plausible architecture is not enough; the real ArcGIS Earth target decides acceptance.

## Before changing architecture or documentation

Read:

1. `README.md`
2. `docs/PROJECT_STATUS_2026-08-17.md`
3. `docs/MAP_FOUNTAIN_ROUTER_ACCEPTANCE_2026-08-17.md`
4. `docs/ACCEPTANCE_RECORD.md`
5. `docs/TECHNICAL_ARCHITECTURE.md`
6. `docs/AI_CONTINUITY_RESTART_NOTE.md`
7. `ROADMAP.md`

Canonical drawing:

`docs/arcgis_system_router_flowchart_2026-08-17.svg`

## Current architecture boundary

The live-proven Windows path is:

```text
USB SSD
→ GL.iNet Flint 2
→ Samba / SMB
→ private Wi-Fi or Ethernet
→ ArcGIS Earth
→ native TPKX
```

Do not reintroduce Raspberry Pi, Pi-server, or another active field GIS-server appliance by default. If a future target requires compatibility logic, prove that requirement first and add the smallest layer that solves the demonstrated problem.

## Preserve proof status

Use explicit labels:

- DESIGNED
- BUILT / SELF-TESTED
- LIVE-OBSERVED
- LIVE-PROVEN

Do not silently promote a path because it works in theory or on a developer machine.

## Do not regress

- public Internet must not become a core dependency;
- native TPKX must remain native on the proven router path;
- ordinary Eaters should stay on DHCP;
- field consumption should remain read-only where practical;
- packet evidence and real-viewer behavior outrank assumptions;
- cached/read-ahead throughput must not be mislabeled as raw router speed;
- the current immediate gate is ArcGIS Earth Mobile on the router-only architecture;
- historical Windows WMTS source is lineage, not the active product.

## Evidence for changes

For changes affecting runtime behavior, include as applicable:

- exact router/model/firmware context;
- exact client/viewer and operating system;
- exact map artifact identity and Windows File Explorer size when relevant;
- Ethernet versus Wi-Fi transport;
- whether outside Internet was present or removed;
- Wireshark/packet evidence when network behavior matters;
- screenshots/video when visual behavior matters;
- what was directly observed versus inferred.

## Security

Never include live credentials, private keys, confidential map products, router administrator secrets, or sensitive packet contents in public commits/issues.
