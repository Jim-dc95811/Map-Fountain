# Map Fountain

## Router-only offline map delivery for ArcGIS Earth

**A USB SSD on a consumer router becomes a private offline map reservoir. ArcGIS Earth reads native TPKX directly through the router's Samba share over Ethernet or Wi-Fi. No field GIS server process is required for the proven Windows path.**

![Canonical ArcGIS Earth Systems router flowchart](docs/arcgis_system_router_flowchart_2026-08-17.svg)

> **The router does not need to understand maps. It only needs to share bytes reliably. ArcGIS Earth supplies the GIS intelligence.**

---

## Live milestone — 2026-08-17

**Status: LIVE-PROVEN on Windows ArcGIS Earth**

```text
native TPKX on USB SSD
        ↓
GL.iNet Flint 2 (GL-MT6000)
        ↓
Samba / SMB
        ↓
Ethernet or Wi-Fi
        ↓
Windows
        ↓
ArcGIS Earth
```

A production-scale `ESG1N.tpkx` package was opened **in place** from the router-attached SSD and rendered interactively in ArcGIS Earth over Wi-Fi.

The specimen used for the controlled large-file proof was:

- `ESG1N.tpkx`
- script-observed size: **26,174,899,216 bytes**
- Windows File Explorer identification: **25,561,426 KB**
- network path: `\\192.168.8.1\New TPKX\Esri and Label\ESG1N.tpkx`

The real viewer was the final acceptance authority: **ArcGIS Earth rendered and navigated the network-hosted TPKX over Wi-Fi.**

---

## Controlled storage proof

The first small-file benchmark exposed heavy Windows caching, so the large-file benchmark was corrected to test the most important access pattern first:

```text
1. random seek
2. four-client random read
3. sequential sample
```

### Ethernet — PASS

- random seek: **25.33 MiB/s**
- random average latency: **9.34 ms**
- random p95: **9.98 ms**
- four-client aggregate: **51.21 MiB/s**
- sequential sample: **42.58 MiB/s**

### Wi-Fi — PASS

- random seek: **5.19 MiB/s**
- random average latency: **46.36 ms**
- random p95: **50.56 ms**
- four-client aggregate: **5.31 MiB/s**
- sequential sample: **6.14 MiB/s**

The Wi-Fi path was substantially slower than Ethernet but remained stable enough to complete the benchmark and, more importantly, the real ArcGIS Earth test.

Wireshark captures were retained and inspected. The SMB path remained stable at the TCP level during the captured tests. Because SMB3 encryption hides individual file-read commands without session keys, the benchmark supplied logical request timing while Wireshark validated the transport behavior.

---

## Evidence fingerprints

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

The packet captures are large bench artifacts and are not committed here. These hashes identify the preserved originals used for the acceptance record.

---

## Why the architecture matters

The field appliance is intentionally simple:

```text
USB storage
+ local network
+ Samba file sharing
= Map Fountain
```

There is no requirement for a field GIS server, map renderer, Python service, SQLite tile service, cloud account, or public Internet connection for the proven Windows/TPKX path.

The division of labor is clean:

- the **Factory** manufactures the map;
- the **SSD** stores the finished product;
- the **router** exposes the file;
- **Windows SMB** carries the file access;
- **ArcGIS Earth** understands and renders the native TPKX.

Changing the map library does not require GIS-specific router configuration. Add finished maps to the SSD, replace maps, or swap in another prepared SSD.

---

## Current status

| Capability | Status |
| --- | --- |
| Flint 2 + USB SSD Samba share | ✅ **LIVE-PROVEN** |
| Large TPKX open/stat over Samba | ✅ **LIVE-PROVEN** |
| Large-file Ethernet benchmark | ✅ **LIVE-PROVEN** |
| Large-file Wi-Fi benchmark | ✅ **LIVE-PROVEN** |
| ArcGIS Earth direct network TPKX over Wi-Fi | ✅ **LIVE-PROVEN** |
| Router-only ArcGIS Earth Mobile path | 🟡 **NEXT ACCEPTANCE GATE** |
| Multiple simultaneous ArcGIS Earth clients | 🟡 **NOT YET ACCEPTED** |
| Operational public-Internet dependency | **NONE BY DESIGN** |

---

## Android is next

The Windows path is proven. **ArcGIS Earth Mobile must now earn its own router-only acceptance.**

The canonical flowchart deliberately marks Android as the next gate rather than pretending the mobile router path is already solved.

Do not add a field GIS server merely because Android still needs a compatible consumption path. Start from the simplest router-only possibilities and let the real mobile target decide.

---

## Historical precursor

On 2026-08-16 a separate Windows-hosted implementation proved:

```text
raster MBTiles
→ local HTTPS WMTS
→ Android USB tether
→ ArcGIS Earth Mobile
```

That work remains useful engineering history and proved local/offline mobile tile delivery, but it is **not the current field-appliance architecture**.

---

## Prior-art / novelty boundary

A 2026-08-17 prior-art search found established examples for the individual ingredients: router-hosted Samba storage, GIS access to network shares, TPKX network-file access, NAS geospatial workflows, and active tile servers.

What was **not** found was a published implementation matching the exact proven chain:

```text
consumer router + USB SSD
→ Samba
→ Wi-Fi
→ ArcGIS Earth
→ large native TPKX opened and rendered in place
```

That is not claimed as a mathematically proven worldwide first. It is recorded as an independently developed and measured architecture for which no matching published implementation was found in the documented search.

---

## Current engineering record

- [Router acceptance record — 2026-08-17](docs/MAP_FOUNTAIN_ROUTER_ACCEPTANCE_2026-08-17.md)
- [Project status — 2026-08-17](docs/PROJECT_STATUS_2026-08-17.md)
- [Technical architecture](docs/TECHNICAL_ARCHITECTURE.md)
- [AI / maintainer restart note](docs/AI_CONTINUITY_RESTART_NOTE.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

---

## Governing rules

- No operational dependence on public Internet.
- Keep the router dumb, local, and predictable.
- Use DHCP for normal consumers.
- Prefer read-only field consumption where practical.
- Change one major test variable at a time.
- Wireshark and real-viewer evidence outrank assumptions.
- Do not call a path proven until the intended ArcGIS Earth runtime passes it.
- Do not add field-server complexity unless the real target proves it is necessary.

---

## Project relationship

- **[Offline GeoStack](https://github.com/Jim-dc95811/Offline-GeoStack)** — master operational field-mapping system.
- **[Rasta Pyramid Factory](https://github.com/Jim-dc95811/Rasta-Pyramid-Factory)** — high-resolution raster pyramid manufacturing.
- **Map Fountain** — router-attached offline map storage and local delivery.

Original project software and documentation are MIT-licensed unless otherwise stated. Third-party imagery, ArcGIS Earth, QGIS, router firmware, and source data remain governed by their own licenses and terms.

---

# Map Fountain

> **Put the maps on the SSD. Plug it into the router. Let ArcGIS Earth drink.**
