# Historical Windows WMTS Map Fountain — 2026-08-16

## Status

**HISTORICAL PRECURSOR — not the current field architecture.**

Before router-only Map Fountain was proven, a Windows-hosted Python implementation served raster MBTiles over local HTTPS WMTS to ArcGIS Earth Mobile through Android USB tethering.

That experiment proved:

- local/offline mobile tile delivery;
- ArcGIS Earth Mobile WMTS consumption;
- HTTPS acceptance;
- QR service loading;
- unique per-map service identity / cache isolation;
- multiple substantial MBTiles;
- a large Lago panorama;
- continued operation after outside Internet was removed.

## Why the old executable source is no longer in the current tree

The active field architecture changed on 2026-08-17:

```text
USB SSD
→ GL.iNet Flint 2
→ Samba / SMB
→ private Wi-Fi or Ethernet
→ ArcGIS Earth
```

The current Windows/TPKX path needs **no field GIS server process**.

To keep the repository front door and active source tree honest, the old root-level Windows WMTS server/GUI launcher files were removed from the current tree after the router proof.

They remain permanently recoverable from Git history. A commit that still contains the historical source is:

`64d99842c9fe8e69f85b3d959cc11ddfc3c39cd2`

Historical files at that point included:

- `Map_Fountain_GUI.py`
- `Map_Fountain_Server.py`
- `START MAP FOUNTAIN.bat`
- `requirements.txt`
- historical HTTPS certificate notes / dependency-license material

## Reuse rule

Do not revive that server as the default architecture.

If ArcGIS Earth Mobile later proves that a compatibility service is necessary, use the historical implementation as reference material and build the smallest compatibility layer the real target actually requires.

## Current next gate

**Router-only ArcGIS Earth Mobile.**

> Preserve the lesson. Do not preserve obsolete complexity as the active product.
