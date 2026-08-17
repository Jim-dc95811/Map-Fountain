# Map Fountain — Static REST WMTS Android Acceptance — 2026-08-17

## Status

**LIVE-PROVEN on ArcGIS Earth Mobile / Android.**

The accepted Android delivery flavor is:

> **Static REST WMTS**

This is a pre-generated WMTS 1.0 raster tile package stored as ordinary files on the router-attached USB SSD. The Flint 2 does not run a GIS server. ArcGIS Earth Mobile reads the WMTS capabilities document and requests individual tile files over the router's built-in local HTTPS/WebDAV endpoint.

---

## Proven Android chain

```text
pre-rendered Static REST WMTS folder
        ↓
USB SSD
        ↓
GL.iNet Flint 2 (GL-MT6000)
        ↓
built-in local HTTPS/WebDAV file endpoint
        ↓
private Wi-Fi
        ↓
Android
        ↓
ArcGIS Earth Mobile
```

No Python process runs on Android.

No QGIS Server, tile server, Raspberry Pi, Windows map server, cloud service, or public Internet map service is required in the field runtime path.

The router remains deliberately dumb: it stores files, provides the private network, and returns requested bytes.

---

## What “Static REST WMTS” means here

The runtime package contains:

```text
<map-id>/
  1.0.0/
    WMTSCapabilities.xml
    <layer-id>/
      default/
        WorldWebMercatorQuad/
          <TileMatrix>/
            <TileRow>/
              <TileCol>.png
```

The capabilities document advertises:

- WMTS 1.0.0;
- raster PNG/JPEG content;
- Web Mercator / EPSG:3857;
- `WorldWebMercatorQuad` tile matrix set;
- `ResourceURL` REST tile addressing;
- tile request order `TileMatrix / TileRow / TileCol`.

The router does not interpret any of this. It only serves the XML and raster files requested by ArcGIS Earth Mobile.

---

## Live acceptance sequence

1. Flint 2 WebDAV was enabled over HTTPS on local port 6008 with the SSD share exposed read-only for field consumption.
2. Android Chrome reached the Flint HTTPS endpoint.
3. Requesting the share directory itself returned `403 Forbidden`; this was not treated as failure because directory browsing is not required.
4. Requesting an actual file directly succeeded and downloaded the file, proving ordinary HTTPS file GET from SSD through the Flint to Android.
5. A tiny Static REST WMTS fixture was placed on the SSD.
6. Android Chrome successfully downloaded that fixture's `WMTSCapabilities.xml` through the same Flint endpoint.
7. ArcGIS Earth Mobile was given the same capabilities URL through Add Data / URL.
8. ArcGIS Earth Mobile accepted the WMTS and rendered its raster tiles.
9. The Android ArcGIS Earth app cache was cleared and the app was force-stopped/reopened.
10. The WMTS was loaded again and the map reappeared, reducing the chance that the acceptance result was only stale cached imagery.

**Acceptance result: PASS.**

---

## Test fixture

Source compact raster package:

```text
small test 8_17_26 mbtile.mbtiles
```

Observed fixture properties during the conversion/self-test:

- source size: 31,064,064 bytes;
- bounds: `-81.9384,30.3916,-81.9336,30.3946`;
- zooms: Z0-Z20;
- tiles: 261;
- raster payload: PNG;
- every exported tile compared byte-for-byte with the source MBTiles tile payload: PASS;
- MBTiles TMS row to WMTS top-origin row conversion: PASS;
- capabilities XML parse: PASS;
- advertised tile limits matched actual output files: PASS;
- geographic-center tile index check at Z20: PASS.

The test output folder was:

```text
small_test_android_wmts
```

The long test naming is not a production naming standard.

---

## Live behavior note

ArcGIS Earth Mobile rendered the map successfully when navigation was deliberate.

The operator observed that **slow, easy pan/zoom movements work; rapid gestures can cause the mobile display to stall or behave erratically.**

Treat this as a performance/interaction characterization issue, not an architecture failure. Do not optimize the cause until controlled testing distinguishes among HTTP small-file request load, Wi-Fi behavior, ArcGIS Earth Mobile request/concurrency behavior, and pyramid density.

---

# Frozen delivery contract

The following is frozen unless later evidence demonstrates a defect:

1. **Windows ArcGIS Earth path:** native TPKX over Samba/SMB.
2. **Android ArcGIS Earth Mobile path:** Static REST WMTS over the Flint's local HTTPS file endpoint.
3. **Field router:** no GIS intelligence or active GIS-server process.
4. **Android:** no Python runtime and no third-party helper application required for map consumption.
5. **Static WMTS package:** capabilities XML plus pre-rendered raster tile tree.
6. **Map/service identity:** each Android map receives a short, unique, stable map ID; changed content that must defeat stale client cache should receive a new/versioned identity.

The current `MF_WMTS_v0_1_1_VERIFIED` converter is a proven test implementation of this contract. The delivery contract is frozen; the final Factory UI/packaging workflow may still be improved without changing the runtime format.

---

# Factory process going forward

## Core manufacturing rule

**Keep the compact map master compact. Expand only the Android deployment product.**

Recommended production chain:

```text
QGIS / Factory render
        ↓
compact raster master: MBTiles
        ├──────────────→ TPKX path for Windows ArcGIS Earth
        │
        └──────────────→ Static REST WMTS expansion for Android
```

For the accepted Android test, the WMTS builder reads the existing MBTiles tile payloads, converts TMS row numbering to WMTS top-origin row numbering, writes the static folder tree, and generates `WMTSCapabilities.xml`.

It does **not** rerender or recompress the raster tiles.

This preserves one compact raster master while allowing two different field consumption products.

---

## Giant-folder reality

Static serverless WMTS intentionally trades runtime-server complexity for filesystem expansion.

A large Android map may contain hundreds of thousands or millions of individual raster tile files and directories. That is not an accidental implementation bug; it is the physical form that lets a dumb HTTP file endpoint satisfy ArcGIS Earth Mobile tile requests without an active GIS server.

Therefore the expanded WMTS tree must be treated as a **deployment artifact**, not as the preferred master/archive format.

### Storage policy

- Keep **MBTiles** as the compact raster master/interchange product.
- Keep **TPKX** as the compact Windows ArcGIS Earth deployment product.
- Create the **expanded Static REST WMTS folder only where Android delivery is required**.
- Do not require operators to copy giant expanded trees between ordinary working folders if the Factory can write directly to the target deployment drive.
- Avoid gratuitous duplicate expanded WMTS copies.
- Preserve enough free space for the compact source plus the expanded Android tree during manufacturing.

---

## Production Factory requirements to add

Before calling the Android manufacturing path production-ready, the Factory should gain:

1. **Static REST WMTS output mode** alongside TPKX / MBTiles choices.
2. **Short map ID** input/output naming suitable for QR URLs and deep folder trees.
3. **Preflight tile count** before expansion.
4. **Preflight payload size and destination free-space check.**
5. **Direct-to-destination build option** so a removable SSD can receive the expanded tree without a second millions-of-files copy operation.
6. **Unique/versioned service identity** to prevent stale mobile-cache collisions when map content changes.
7. **Automatic `WMTSCapabilities.xml` generation.**
8. **Automatic TMS-to-WMTS row conversion** when deriving from MBTiles.
9. **Post-build verification** of tile count, matrix limits, representative tile paths, and capabilities XML.
10. **QR generation** for the finished ArcGIS Earth Mobile capabilities URL.
11. **Clean delete/replace workflow** for retiring a complete WMTS map folder from the deployment SSD.
12. **Performance characterization** on larger, denser maps before publishing practical size guidance.

An optional single-file deployment/archive wrapper may be useful for transport or backup, but ArcGIS Earth Mobile's accepted runtime product remains the expanded static WMTS directory tree on the SSD.

---

## Naming rule going forward

Test names used during discovery are not the public convention.

Prefer short deployment IDs such as:

```text
JAX1
FIRE23
ESG1
```

Example runtime path:

```text
/WMTS/JAX1/1.0.0/WMTSCapabilities.xml
```

The human-readable descriptive name belongs inside the capabilities metadata and Factory records rather than in every deep directory path.

---

## What is not frozen yet

The following remain engineering decisions rather than accepted final behavior:

- exact Factory GUI controls for WMTS output;
- whether WMTS expansion occurs automatically whenever MBTiles is built or only when selected;
- exact deployment SSD root-folder naming;
- whether an optional compressed transport/archive artifact is created;
- practical maximum map size / tile count for Android;
- optimum metatile/render settings for mobile interaction;
- performance tuning for rapid pan/zoom;
- multiple simultaneous Android Eaters.

Do not confuse those open production questions with the already proven runtime architecture.

---

## Accepted statement

> **Map Fountain is LIVE-PROVEN on Android using a serverless Static REST WMTS package stored as ordinary files on a Flint 2 USB SSD and consumed by ArcGIS Earth Mobile over the router's local HTTPS endpoint. The cost of removing the field GIS server is an expanded tile-directory deployment artifact; compact MBTiles/TPKX remain the preferred masters and transport products.**
