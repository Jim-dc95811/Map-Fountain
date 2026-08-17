# Map Fountain — Notice

## Original project work

Original Map Fountain documentation, test tooling, and project-created software are provided under the MIT License unless a file states otherwise.

## Current field architecture

The current live-proven Windows path is a router/storage architecture:

```text
USB SSD
→ GL.iNet Flint 2
→ Samba / SMB
→ private Wi-Fi or Ethernet
→ ArcGIS Earth
→ native TPKX
```

Map Fountain does not modify ArcGIS Earth, Windows SMB, router firmware, TPKX specifications, or other third-party software/protocols.

## Historical software

The 2026-08-16 Windows-hosted WMTS experiment used Python and `python-qrcode` 8.2. That implementation is retained in Git history as engineering lineage and is not the current field product.

Python, ArcGIS Earth, Windows, Android, QGIS, GL.iNet firmware, Samba/SMB implementations, and other third-party products remain governed by their own licenses and terms.

## Map/source data

Map Fountain does not grant rights to imagery, maps, labels, basemaps, TPKX packages, MBTiles databases, or other source data supplied by the operator.

Users are responsible for complying with the terms, attribution requirements, caching/export restrictions, and redistribution rules of their source data.

## ArcGIS Earth / Esri

Map Fountain is not an Esri product and this project does not imply endorsement by Esri.

ArcGIS Earth Windows is the current live-proven router-only acceptance viewer. ArcGIS Earth Mobile is the next acceptance gate.

## Security

Do not publish router credentials, confidential map products, operational secrets, private keys from historical experiments, or sensitive packet captures without review.
