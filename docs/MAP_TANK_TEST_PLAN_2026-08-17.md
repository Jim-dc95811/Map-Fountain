# Map Fountain — Router + USB SSD Acceptance Record

**Status: LIVE-PROVEN — 2026-08-17**

Map Fountain is now a router-only field appliance:

```text
USB SSD full of finished map products
        ↓
GL.iNet Flint 2
        ↓
Samba / SMB
        ↓
private Ethernet or Wi-Fi
        ↓
ArcGIS Earth clients
```

The router remains intentionally dumb. It provides local networking, DHCP, USB storage access, and ordinary file sharing. It does not need GIS intelligence.

## Proven hardware

- GL.iNet Flint 2
- model GL-MT6000
- USB-attached SSD
- stock Samba network-storage feature
- Windows client on DHCP

## Proven large specimen

`ESG1N.tpkx`

- script-observed size: **26,174,899,216 bytes**
- Windows File Explorer identification: **25,561,426 KB**
- network path: `\\192.168.8.1\New TPKX\Esri and Label\ESG1N.tpkx`

## Gate 1 — small-file Ethernet baseline

**PASS**

A small known-good TPKX established that Windows could open/read a TPKX on the Flint 2 USB SSD through Samba. That first run also exposed heavy Windows caching, which made later random-read numbers unrealistic.

Engineering response: change the v0.1.1 benchmark order to:

1. random seek;
2. four-client random read;
3. sequential sample.

This kept the large-file random test from being preloaded by the sequential phase.

## Gate 2 — large-file Ethernet baseline

**PASS**

Map Tank First Bench v0.1.1 TEST results:

```text
OPEN/STAT: PASS
FILE SIZE: 26,174,899,216 bytes

RANDOM-SEEK
400 requests
104,857,600 bytes
3.948 s
25.33 MiB/s
avg 9.34 ms
median 9.42 ms
p95 9.98 ms
max 16.17 ms

FOUR-CLIENT RANDOM-READ
4 workers
400 requests
104,857,600 bytes
1.953 s
51.21 MiB/s aggregate
avg 18.51 ms
median 18.68 ms
p95 21.43 ms
max 38.52 ms

SEQUENTIAL SAMPLE
536,870,912 bytes
12.024 s
42.58 MiB/s
```

Wireshark confirmed a stable SMB/TCP conversation during the captured run. Later benchmark phases were influenced by normal Windows cache/read-ahead, so the application-observed rates should not be misrepresented as raw router wire speed.

## Gate 3 — same large file over Wi-Fi

**PASS**

Only the major transport variable changed: Ethernet → Wi-Fi.

```text
OPEN/STAT: PASS
FILE SIZE: 26,174,899,216 bytes

RANDOM-SEEK
400 requests
104,857,600 bytes
19.273 s
5.19 MiB/s
avg 46.36 ms
median 45.42 ms
p95 50.56 ms
max 66.71 ms

FOUR-CLIENT RANDOM-READ
4 workers
400 requests
104,857,600 bytes
18.845 s
5.31 MiB/s aggregate
avg 185.07 ms
median 185.95 ms
p95 200.23 ms
max 347.41 ms

SEQUENTIAL SAMPLE
536,870,912 bytes
83.440 s
6.14 MiB/s
```

The Wi-Fi sequential phase looked stalled to the operator because it took much longer than Ethernet, but Wireshark continued showing sustained traffic and the benchmark completed normally.

The Wi-Fi capture began shortly after the benchmark had started, so the benchmark console is the authority for the early random/four-client measurements while the partial capture independently confirms the sustained later traffic.

## Gate 4 — real ArcGIS Earth over Wi-Fi

**PASS / LIVE-PROVEN**

ArcGIS Earth was instructed to add the TPKX as an ordinary file through the Windows file picker using the Samba path.

ArcGIS Earth opened the network-hosted package and rendered the Jacksonville map successfully while the source remained on the USB SSD attached to the Flint 2.

This is the decisive application proof:

```text
USB SSD
→ consumer router
→ Samba
→ Wi-Fi
→ Windows
→ ArcGIS Earth
→ native TPKX rendered in place
```

No field GIS server process was required.

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

## Current architecture decision

The field appliance is **router only**.

```text
storage + local network + Samba
```

ArcGIS Earth remains the map intelligence. The Factory remains responsible for producing finished TPKX / MBTiles products.

## Feeder / Eater model

### Eaters

Field clients consume maps read-only where practical.

Current proven Eater:

- Windows ArcGIS Earth laptop reading native TPKX directly from the router share.

### Feeder

At basecamp, a future Feeder utility may maintain the SSD against an approved master library without changing router GIS settings.

## Next controlled gates

1. Repeat the successful ArcGIS Earth test over Ethernet for direct application comparison.
2. Characterize deliberate real-world ArcGIS Earth navigation over Wi-Fi.
3. Test cold close/reopen and Wi-Fi reconnect behavior.
4. Test multiple simultaneous Eaters.
5. Test the simplest router-only ArcGIS Earth Mobile path separately.
6. Build the Feeder only after consumption behavior is stable.

## Governing rules

- No operational dependence on public Internet.
- Keep the router dumb, local, and predictable.
- Use DHCP for normal consumers.
- Prefer read-only field consumption where practical.
- Change one major variable at a time during acceptance testing.
- Wireshark/packet evidence outranks assumptions.
- Real ArcGIS Earth behavior is the final authority.
- Do not add a field server layer unless the real target proves one is necessary.

> **At basecamp, feed the fountain. In the field, drink from it.**
