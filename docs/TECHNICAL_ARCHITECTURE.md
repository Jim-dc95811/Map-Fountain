# Map Fountain — Technical Architecture

## Purpose

Map Fountain is a router-only offline map-delivery architecture for ArcGIS Earth.

The current live-proven Windows/TPKX path is deliberately simple:

```text
finished native TPKX
        ↓
USB SSD
        ↓
GL.iNet Flint 2
        ↓
Samba / SMB
        ↓
private Ethernet or Wi-Fi
        ↓
Windows
        ↓
ArcGIS Earth
```

It is a delivery architecture, not a renderer.

The router does not parse TPKX, understand GIS, generate tiles, or run map-rendering software. It exposes storage over the local network. ArcGIS Earth reads the native file through Windows SMB and performs the GIS work.

---

## 1. Field runtime components

Current proven field components:

- GL.iNet Flint 2 (`GL-MT6000`);
- USB-attached SSD;
- stock Samba network-storage feature;
- private Ethernet/Wi-Fi LAN;
- Windows client using DHCP;
- ArcGIS Earth;
- finished native `.tpkx` map products.

No field GIS server process is required for the proven desktop TPKX path.

---

## 2. Network share

The live test used the router LAN address:

```text
192.168.8.1
```

The tested share path was:

```text
\\192.168.8.1\New TPKX
```

The production-scale test file was:

```text
\\192.168.8.1\New TPKX\Esri and Label\ESG1N.tpkx
```

The benchmark script opened the network path read-only.

---

## 3. Native TPKX behavior

The map remains a normal native TPKX package on the SSD.

The router does not unpack or transform it.

ArcGIS Earth opens the network-hosted file through the same user-facing file workflow used for ordinary local files. Windows/SMB handles file access; ArcGIS Earth selectively reads the package content required for display/navigation.

This separation is the central design insight:

```text
Factory knows how to manufacture the map.
Router knows how to share a file.
ArcGIS Earth knows how to render the map.
```

No component is forced to imitate another.

---

## 4. Storage benchmark design

The first small-file benchmark proved connectivity but exposed a measurement problem: the small package fit easily into Windows cache, causing later random-read measurements to report impossible router speeds.

Map Tank First Bench v0.1.1 TEST therefore changed the large-file order to:

```text
1. random seek
2. four-client random read
3. sequential sample
```

The goal was to obtain the most useful random-access measurement before sequential access and read-ahead could preload large portions of the package.

The benchmark is read-only.

---

## 5. Ethernet large-file baseline

Specimen:

```text
ESG1N.tpkx
26,174,899,216 bytes
```

Observed Ethernet results:

```text
Random seek
400 requests
104,857,600 bytes
3.948 s
25.33 MiB/s
avg 9.34 ms
median 9.42 ms
p95 9.98 ms
max 16.17 ms

Four-client random read
4 workers
400 requests
104,857,600 bytes
1.953 s
51.21 MiB/s aggregate
avg 18.51 ms
median 18.68 ms
p95 21.43 ms
max 38.52 ms

Sequential sample
536,870,912 bytes
12.024 s
42.58 MiB/s
```

Later phases reflect the behavior of the complete Windows + SMB + cache/read-ahead + router + SSD path and should not be mislabeled as raw router wire speed.

---

## 6. Wi-Fi large-file baseline

Same file. Same router. Same SSD. Same benchmark. Major variable changed: Ethernet → Wi-Fi.

```text
Random seek
400 requests
104,857,600 bytes
19.273 s
5.19 MiB/s
avg 46.36 ms
median 45.42 ms
p95 50.56 ms
max 66.71 ms

Four-client random read
4 workers
400 requests
104,857,600 bytes
18.845 s
5.31 MiB/s aggregate
avg 185.07 ms
median 185.95 ms
p95 200.23 ms
max 347.41 ms

Sequential sample
536,870,912 bytes
83.440 s
6.14 MiB/s
```

Wi-Fi was substantially slower but stable enough to complete the synthetic storage benchmark and, more importantly, the real ArcGIS Earth test.

---

## 7. ArcGIS Earth live proof

ArcGIS Earth opened `ESG1N.tpkx` through the Samba path while connected over Wi-Fi.

The application rendered the Jacksonville map successfully and supported normal interactive navigation.

This promoted the path from storage-bench proof to real-viewer proof.

Current accepted chain:

```text
USB SSD
→ Flint 2
→ Samba
→ Wi-Fi
→ Windows
→ ArcGIS Earth
→ native TPKX
```

---

## 8. Packet-analysis boundary

The SMB session uses SMB3 encryption on the tested configuration.

Wireshark can still show:

- TCP endpoints;
- timing;
- byte volume;
- connection continuity;
- resets;
- retransmission behavior visible at TCP;
- overall traffic shape.

Without SMB session keys it cannot decode the individual encrypted SMB file-read commands.

The Ethernet and Wi-Fi captures were therefore used to validate hose behavior while the benchmark script supplied logical request timing and the ArcGIS Earth runtime supplied final application acceptance.

---

## 9. DHCP / addressing rule

Normal Eaters use DHCP.

Do not manually assign client static addresses simply to consume maps.

The router remains the predictable network authority and provides the known share address. If a future client temporarily needs a stable address for a separate service, prefer a router-side DHCP reservation over manual Windows static configuration.

---

## 10. Feeder / Eater separation

### Eaters

Field clients consume maps.

Current proven Eater:

- Windows ArcGIS Earth laptop opening a native TPKX directly from the router share.

### Feeder

A future basecamp Feeder may maintain the SSD inventory:

```text
approved master library
→ compare
→ copy new
→ replace updated
→ retire obsolete when instructed
→ verify
→ MAP FOUNTAIN CURRENT
```

The router does not need Feeder/Eater logic.

---

## 11. Offline boundary

The proven field path does not require public Internet connectivity.

Private local networking is part of the design, not a violation of the offline doctrine.

```text
no cloud map request
no public tile service
no portal dependency
no Internet requirement for the local TPKX read path
```

---

## 12. Relationship to MBTiles

The Factory may produce TPKX, MBTiles, or both.

Current router proof is strongest for direct network-hosted TPKX on Windows ArcGIS Earth.

MBTiles remain valuable as:

- a first-class Factory output;
- a source for future router-only mobile delivery experiments;
- a general raster-pyramid interchange/storage format.

Do not force MBTiles through an active field server merely because earlier prototypes did so. Use the simplest client-compatible delivery form that survives real-target acceptance.

---

## 13. Historical Windows WMTS implementation

On 2026-08-16 the project proved a Windows-hosted HTTPS WMTS path to ArcGIS Earth Mobile over Android USB tether.

That implementation established important lessons about:

- local/offline mobile service consumption;
- WMTS row conversion;
- unique per-map service identity;
- QR ingestion;
- mobile cache behavior;
- deliberate versus rapid navigation.

It remains engineering history and a reusable compatibility technique, but it is not the current field-appliance architecture.

---

## 14. Security / publication rule

Never commit:

- live credentials;
- private TLS keys from historical service experiments;
- confidential map databases;
- operationally sensitive packet captures without review.

Public documentation may record evidence hashes and sanitized technical results.

---

## 15. Current do-not-regress rules

1. Keep the field appliance router-only unless real target evidence proves additional software is necessary.
2. Do not make public Internet part of the core map path.
3. Do not make ordinary Eaters use manual static IP configuration.
4. Preserve native map products; do not rerender them in the router.
5. Do not confuse application-observed cached throughput with raw network speed.
6. Do not optimize a guessed bottleneck before ArcGIS Earth exposes a reproducible problem.
7. Keep field consumption read-only where practical.
8. Preserve controlled-test discipline: one major variable at a time.
9. Let packet evidence validate the network path.
10. Let the real ArcGIS Earth runtime decide acceptance.

> **Keep the router dumb. Keep the maps native. Let ArcGIS Earth do the GIS work.**
