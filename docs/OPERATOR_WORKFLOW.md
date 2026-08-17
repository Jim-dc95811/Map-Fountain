# Map Fountain — Operator Workflow

## Current field target

```text
USB SSD
→ GL.iNet Flint 2
→ Samba / SMB
→ private Ethernet or Wi-Fi
→ Windows ArcGIS Earth
```

**Status: LIVE-PROVEN — 2026-08-17**

The current field workflow does not require Python, a tile server, HTTPS certificates, QR loading, or a Windows-hosted GIS service.

---

## Before starting

You need:

- GL.iNet Flint 2 (`GL-MT6000`) or the specifically accepted router configuration;
- USB SSD containing finished native `.tpkx` maps;
- Samba enabled through the normal router GUI;
- the desired map folder shared;
- Windows PC/laptop on DHCP;
- ArcGIS Earth installed.

Current tested router address:

```text
192.168.8.1
```

Current tested share:

```text
\\192.168.8.1\New TPKX
```

---

## Normal Windows workflow

### 1. Power the Map Fountain

Power the router and attach the prepared USB SSD.

No GIS program runs on the router.

### 2. Connect the Windows Eater

Connect by Ethernet or Wi-Fi.

Leave Windows on normal DHCP unless a separate test explicitly requires otherwise.

### 3. Confirm the share

In Windows File Explorer, enter:

```text
\\192.168.8.1\New TPKX
```

Confirm the expected map folders/files are visible.

### 4. Open ArcGIS Earth

Start ArcGIS Earth normally.

### 5. Add the TPKX as a file

Use ArcGIS Earth's normal **Add Data / File** workflow.

In the Windows Open dialog, use the address bar to navigate directly to the Samba folder containing the desired TPKX.

Example accepted specimen:

```text
\\192.168.8.1\New TPKX\Esri and Label\ESG1N.tpkx
```

Select the TPKX and open it.

**Do not copy the file locally when the purpose is Map Fountain consumption.**

### 6. Use the map

ArcGIS Earth reads the native package through Windows SMB and renders it normally.

The accepted Wi-Fi proof displayed and navigated `ESG1N.tpkx` while the source remained on the router-attached SSD.

---

## What success looks like

- the file remains on the Map Fountain SSD;
- ArcGIS Earth loads the correct TPKX;
- useful map content renders;
- pan/zoom continues to request data through the network share;
- the router requires no map-specific GIS configuration;
- public Internet is not required for the local TPKX path.

---

## Do not do this

- do not manually static-IP ordinary consumers;
- do not unpack TPKX on the router;
- do not run a GIS server merely to make the proven Windows path work;
- do not copy the whole map locally and call that a Map Fountain streaming/open-in-place proof;
- do not alter router settings during a controlled comparison unless that setting is the variable under test.

---

## Android

**ArcGIS Earth Mobile is the next acceptance gate.**

The old Windows-hosted HTTPS WMTS + USB tether workflow remains documented as historical engineering evidence, but it is not the current field workflow.

For the router-only Android test, start with the simplest path the real mobile client accepts from the router-attached SSD over private Wi-Fi. Do not assume a field server must return.

---

## Current practical rule

> **Plug in the SSD. Connect to the router. Open the native map. Let ArcGIS Earth drink.**
