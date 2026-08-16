# Map Fountain — Operator Workflow

## Current target

Windows PC or laptop + attached SSD
→ USB-connected Android phone
→ ArcGIS Earth Mobile

The current live-proven build is `Rasta USB Map Fountain v0.2.1 TEST`.

---

## Before starting

You need:

- Windows 10/11 PC;
- Python 3.14.5 established known-good for the source build;
- one compatible raster `.mbtiles` file;
- Android phone with ArcGIS Earth Mobile installed;
- USB cable;
- Android USB tethering enabled;
- working local HTTPS certificate setup for the current test build.

The current v0.2.1 source is still tied to the bench certificate/IP arrangement documented in `HTTPS_CERTIFICATE_NOTE.md`.

---

## Normal live workflow

### 1. Connect the phone

Connect the Android phone to the Windows PC by USB.

On Android, enable **USB tethering**.

Windows should expose a network adapter similar to:

`Remote NDIS based Internet Sharing Device`

The current server detects that adapter automatically.

### 2. Start Map Fountain

Double-click:

`START MAP FOUNTAIN.bat`

The GUI opens.

### 3. Choose the map

Click:

**CHOOSE MBTILES**

Select the desired raster `.mbtiles` file from the PC or attached SSD.

Confirm the GUI shows:

`SELECTED: <your filename>`

Do not continue if the selected filename is wrong.

### 4. Start the local service

Click:

**START HTTPS MAP FOUNTAIN**

The GUI should progress to a live state and display the generated WMTS URL.

The server activity window should show the actual selected MBTiles path and a unique Map ID.

### 5. Open the QR

Click:

**OPEN QR**

The PC displays a QR containing the exact live HTTPS WMTS GetCapabilities URL for the currently selected map.

### 6. Add it in ArcGIS Earth Mobile

On Android:

```text
ArcGIS Earth Mobile
→ Add Data
→ QR Code
→ scan the QR on the PC
```

The map should appear as a WMTS layer.

### 7. Navigate deliberately

Current live operator rule:

> **Pan and zoom steadily. Do not whip rapidly through repeated zoom/pan changes.**

The current system is smooth when operated deliberately. Rapid repeated movement can outrun the current phone/service/render path.

---

## Switching to another MBTiles

1. Stop the current server with **STOP SERVER**.
2. Click **CHOOSE MBTILES**.
3. Select the next map.
4. Confirm the new filename in the GUI.
5. Start Map Fountain again.
6. Open the new QR.
7. Add/scan the new service in ArcGIS Earth Mobile.

v0.2.1 gives each selected MBTiles a unique service identity and tile URL path so the phone does not silently show the previous map from stale cache.

---

## What success looks like

In the GUI:

- status says LIVE;
- the selected MBTiles path is correct;
- the Map ID is present;
- server activity shows Android requests;
- tile requests return `200` responses.

On Android:

- correct map appears;
- zoom/pan loads progressively;
- outside Internet can be absent;
- local content continues to display over USB tether.

---

## If the wrong old map appears

That was a v0.2.0 defect.

Do not accept it as normal behavior.

v0.2.1 should generate a new unique service identity for each selected file. Confirm you are actually running v0.2.1 or later and that the server log shows the correct MBTiles path plus a new Map ID.

---

## If the server says the tether IP does not match

The current bench HTTPS source contains a fixed expected IP because the live certificate was generated for `10.13.166.115`.

Do not bypass the check by pretending another IP matches the certificate.

That limitation is the next productization target.

---

## Offline acceptance check

Once the map is displaying:

1. remove outside Internet connectivity;
2. keep the USB tether/local link alive;
3. navigate to areas not just sitting in the current screen;
4. verify the server continues receiving fresh tile requests;
5. verify the phone continues displaying requested map content.

This test passed during the 2026-08-16 proof sequence.

---

## Current practical rule

> **Choose map. Start fountain. Scan QR. Fly steadily.**
