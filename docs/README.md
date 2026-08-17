# Map Fountain Documentation

![Canonical Factory / PC / Android router-only flowchart](arcgis_system_router_flowchart_2026-08-17.svg)

## Start here

- [Project status — 2026-08-17](PROJECT_STATUS_2026-08-17.md) — current router-only LIVE-PROVEN checkpoint.
- [Router acceptance record — 2026-08-17](MAP_FOUNTAIN_ROUTER_ACCEPTANCE_2026-08-17.md) — exact Ethernet/Wi-Fi benchmark and ArcGIS Earth proof.
- [Acceptance record](ACCEPTANCE_RECORD.md) — evidence-status chronology.
- [Technical architecture](TECHNICAL_ARCHITECTURE.md) — USB SSD, Flint 2, Samba/SMB, Windows, ArcGIS Earth, and benchmark boundaries.
- [AI / maintainer restart note](AI_CONTINUITY_RESTART_NOTE.md) — current cold-start truth and do-not-regress rules.
- [Roadmap](../ROADMAP.md) — Android is the next router-only acceptance gate.
- [Changelog](../CHANGELOG.md) — engineering chronology.
- [Security](../SECURITY.md) — publication/network-exposure guidance.

Historical 2026-08-16 Windows-hosted WMTS documents remain as engineering lineage. They are **not** the current field architecture.

## Current shorthand

```text
native TPKX on USB SSD
→ GL.iNet Flint 2
→ Samba / SMB
→ Ethernet or Wi-Fi
→ ArcGIS Earth
```

## Current next gate

```text
router-attached SSD
→ private Wi-Fi
→ ArcGIS Earth Mobile
```

The Android path is not yet promoted. The real mobile client decides what compatibility path, if any, is necessary.

## Evidence rule

> **The real ArcGIS Earth runtime decides acceptance. Keep the router dumb and the maps native.**
