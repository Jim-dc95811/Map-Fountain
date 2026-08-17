# Map Fountain — Historical HTTPS Certificate Note

## Status

**HISTORICAL — 2026-08-16 Windows-hosted WMTS experiment.**

The current router-only Map Fountain field path does **not** require HTTPS certificates, a Windows WMTS server, or Android USB tethering for the proven Windows/TPKX workflow.

This document is retained only because the earlier mobile experiment may remain useful as a compatibility reference while the router-only Android path is investigated.

---

## Historical live-proven bench identity

Observed PC-side USB-tether IPv4:

`10.13.166.115`

The successful historical HTTPS test used a server certificate whose Subject Alternative Name matched that IP address.

The old v0.2.1 source checked that the active Remote NDIS tether address equaled that test address and stopped on mismatch rather than silently presenting the wrong certificate.

---

## What is intentionally not in GitHub

The public repository does **not** contain the private TLS server key used during the historical live proof.

Do not publish or commit:

- private TLS server keys;
- private CA keys;
- deployed private keys;
- credentials.

---

## Historical lesson

The first HTTPS attempt failed because the Windows target did not have the expected OpenSSL executable. The next build removed that target dependency by preparing matching local certificate material ahead of time.

That allowed ArcGIS Earth Mobile to consume the local HTTPS WMTS service during the 2026-08-16 experiment.

---

## Current architecture boundary

Current field architecture:

```text
USB SSD
→ consumer router
→ Samba / SMB
→ private Wi-Fi or Ethernet
→ ArcGIS Earth
```

Do **not** turn the old certificate lifecycle problem back into an active productization requirement unless the router-only Android acceptance work proves that an HTTPS compatibility service is actually necessary.

---

## Evidence status

Historical HTTPS local WMTS delivery: **LIVE-PROVEN HISTORY**.

Current router-only Windows TPKX path: **LIVE-PROVEN and certificate-free**.

Router-only Android path: **NEXT ACCEPTANCE GATE**.
