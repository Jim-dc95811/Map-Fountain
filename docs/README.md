# Map Fountain Documentation

![Canonical Factory / PC / Android router-only flowchart](arcgis_system_router_flowchart_2026-08-17.svg)

## Current status

**LIVE-PROVEN / PARKED from the primary personal-phone deployment path.**

Map Fountain remains the evidence repository for two accepted router/storage paths:

### Windows

```text
native TPKX
→ USB SSD
→ GL.iNet Flint 2
→ Samba / SMB
→ Ethernet or Wi-Fi
→ ArcGIS Earth
```

### Android

```text
Static REST WMTS
→ USB SSD
→ GL.iNet Flint 2 local HTTPS/WebDAV
→ Wi-Fi
→ ArcGIS Earth Mobile
```

Both paths passed real target acceptance.

The current personal-phone deployment work has moved to direct local removable storage:

**[Android Field Maps + ArcGIS Earth](https://github.com/Jim-dc95811/Android-Field-Maps-and-ArcGIS-Earth-)**

## Start here

- [Map Fountain README](../README.md) — current proven/parked project status.
- [Router acceptance record — 2026-08-17](MAP_FOUNTAIN_ROUTER_ACCEPTANCE_2026-08-17.md) — exact Ethernet/Wi-Fi benchmark and Windows ArcGIS Earth proof.
- [Static REST WMTS Android acceptance — 2026-08-17](STATIC_REST_WMTS_ANDROID_ACCEPTANCE_2026-08-17.md) — router-only Android proof.
- [Acceptance record](ACCEPTANCE_RECORD.md) — evidence-status chronology.
- [Technical architecture](TECHNICAL_ARCHITECTURE.md) — detailed accepted router/runtime architecture.
- [AI / maintainer restart note](AI_CONTINUITY_RESTART_NOTE.md) — current cold-start truth and reopen conditions.
- [Roadmap](../ROADMAP.md) — parked status and possible Starlink/basecamp future role.
- [Changelog](../CHANGELOG.md) — engineering chronology.
- [Security](../SECURITY.md) — publication/network-exposure guidance.

## Important reading rule

The acceptance documents describe what **worked**. They do not mean every proven component remains mandatory in the current architecture.

Map Fountain was simplified out of the normal personal-phone deployment because microSD/local TPKX is operationally simpler for that user.

Preserve the proof. Do not force the proof back into the workflow.

## Possible future return

The likely reopening role is:

```text
Starlink
→ Flint 2 WAN
→ USB SSD
→ local SMB / Wi-Fi / Ethernet
→ basecamp laptops / clients
```

That would use Map Fountain as shared local storage / a poor-man's NAS while still preserving useful local operation if outside connectivity disappears.

## Evidence rule

> **The real target decides acceptance. A successful experiment remains valuable even after the larger system finds a simpler deployment path.**
