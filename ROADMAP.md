# Map Fountain Roadmap

## Current state

**Map Fountain is LIVE-PROVEN and currently PARKED from the primary personal-phone deployment path.**

It is not parked because it failed. It is parked because the larger project found a simpler normal-user path: put the native map directly on removable local phone storage.

### Proven Windows path

```text
USB SSD
→ GL.iNet Flint 2
→ Samba / SMB
→ Ethernet or Wi-Fi
→ Windows
→ ArcGIS Earth
→ native network-hosted TPKX
```

### Proven Android router path

```text
Static REST WMTS folder
→ USB SSD
→ GL.iNet Flint 2 local HTTPS
→ Wi-Fi
→ Android
→ ArcGIS Earth Mobile
```

Both paths passed real-target acceptance.

---

## Why current active development is paused

The new personal-phone deployment direction is:

```text
TPKX
→ microSD
→ Android
→ ArcGIS Field Maps / ArcGIS Earth
```

That removes infrastructure from the normal user workflow.

The active deployment work now belongs in:

**[Android Field Maps + ArcGIS Earth](https://github.com/Jim-dc95811/Android-Field-Maps-and-ArcGIS-Earth-)**

Do not keep extending Map Fountain merely because there are interesting technical problems left to solve.

---

## Preserve these proven results

### Windows

- direct network-hosted native TPKX: LIVE-PROVEN;
- large Ethernet benchmark: LIVE-PROVEN;
- large Wi-Fi benchmark: LIVE-PROVEN;
- real ArcGIS Earth Wi-Fi rendering: LIVE-PROVEN.

### Android

- direct file GET from router-attached SSD: LIVE-PROVEN;
- Static REST WMTS capabilities/tiles over local HTTPS: LIVE-PROVEN;
- ArcGIS Earth Mobile display: LIVE-PROVEN;
- cache-clear / force-stop / reopen retest: LIVE-PROVEN.

### Historical Windows server precursor

The earlier Windows-hosted HTTPS WMTS / Android USB-tether path also remains useful history, not current infrastructure.

---

## REST manufacturing work — paused with the deployment role

The accepted Android router runtime requires an expanded Static REST WMTS tree.

Production-scale manufacturing exposed a giant-folder problem. Later Factory experiments moved toward a compact `.restmap` seed that would be transported as one file and expanded at the final SSD.

That work is technically useful but no longer the immediate project priority while personal-phone deployment is moving to direct local TPKX.

Do not delete the work. Do not continue optimizing it without a real reopened Map Fountain use case.

---

## Reopen condition 1 — Starlink / basecamp NAS

The strongest likely future role is a Starlink-connected basecamp storage appliance:

```text
Starlink
→ Flint 2 WAN
→ USB SSD
→ SMB / Wi-Fi / Ethernet
→ local laptops / clients
```

Useful properties:

- one shared map reservoir;
- local copies remain available if Starlink disappears;
- fresh imagery can be manufactured at base when Starlink is available;
- laptops can read/copy large map products through familiar network storage;
- no need to turn the router into a GIS computer.

If this role is reopened, define the exact operational need before adding code.

---

## Reopen condition 2 — real multi-client shared-map need

If a field operation demonstrates that many clients genuinely benefit from one central local map store, resume controlled testing.

Potential gates then include:

- simultaneous Windows clients;
- multiple Android clients only if Static REST delivery is again relevant;
- read-only share behavior;
- storage inventory/version management;
- basecamp feeder workflow;
- router reboot/reconnect behavior;
- Starlink-present versus Starlink-absent behavior.

Do not make a multi-user claim until it is measured.

---

## Reopen condition 3 — removable storage proves insufficient

If the current Android microSD deployment encounters a real limitation that shared storage solves better, bring Map Fountain back deliberately.

Do not anticipate that failure and re-add infrastructure early.

---

## Performance baseline — preserved reference

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

The synthetic benchmark is a diagnostic baseline, not a substitute for application behavior.

---

## Non-goals while parked

- continuing to add features simply to keep the repo active;
- turning the router into a GIS computer;
- requiring a field GIS server process;
- requiring public Internet;
- requiring Python or helper apps on Android;
- making personal-phone users associate to Map Fountain when local storage already solves the job;
- optimizing the Static REST branch without an active deployment requirement;
- rewriting proven Windows TPKX delivery without a verified defect.

---

## Governing rule

> **Preserve the proof. Reopen the appliance only when shared storage solves a real problem better than local storage.**
