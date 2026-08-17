# Map Fountain — Project Status — 2026-08-17

## Executive state

**Map Fountain is LIVE-PROVEN as a router-only offline field map appliance for Windows ArcGIS Earth.**

Current proven chain:

```text
native TPKX on USB SSD
→ GL.iNet Flint 2
→ Samba / SMB
→ Wi-Fi
→ Windows
→ ArcGIS Earth
```

The router provides storage, local networking, DHCP, and file sharing only. ArcGIS Earth provides the GIS intelligence.

The canonical system drawing is the **Factory / PC / Android flowchart**:

`arcgis_system_router_flowchart_2026-08-17.svg`

Do not replace it with the superseded hub-and-spoke drawing.

## Decisive live proof

`ESG1N.tpkx` was opened directly from the router Samba share and rendered interactively in ArcGIS Earth over Wi-Fi.

Specimen:

- 26,174,899,216 bytes by benchmark script
- 25,561,426 KB Windows File Explorer identification

## Controlled benchmark results

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

The Wi-Fi 536,870,912-byte sequential logical sample completed in 83.440 seconds.

## Current architecture decision

Field map delivery is **router only**.

Do not revive Raspberry Pi, Pi-server, or other active field GIS-server appliance architecture from older project history unless real target evidence proves a compatibility layer is unavoidable.

## Immediate next gate

**ArcGIS Earth Mobile on the router-only architecture.**

The Android client must now be tested against the router-attached SSD over private Wi-Fi. Do not assume the old Windows WMTS server must return. Start from the simplest path the mobile client can actually consume and let the real target decide.

After Android:

1. ArcGIS Earth direct-network comparison over Ethernet.
2. Real ArcGIS Earth navigation characterization over Wi-Fi.
3. Cold close/reopen and Wi-Fi reconnect.
4. Multiple simultaneous Eaters.
5. Basecamp Feeder after consumption behavior is stable.

## Evidence hashes

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

## Historical precursor

The 2026-08-16 Windows-hosted HTTPS WMTS → Android proof remains useful engineering history, but it is not the current field-appliance architecture.

## Governing rule

> **Keep the router dumb. Keep the maps native. Let ArcGIS Earth do the GIS work.**
