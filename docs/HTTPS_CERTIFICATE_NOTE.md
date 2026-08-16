# Map Fountain — HTTPS Certificate Note

## Why this document exists

The current live-proven v0.2.1 TEST architecture uses HTTPS because the Android / ArcGIS Earth Mobile path being tested requested HTTPS for the QR/service workflow.

The bench proof succeeded, but the certificate arrangement is **not yet a finished consumer design**.

---

## Live-proven bench identity

Observed PC-side USB-tether IPv4:

`10.13.166.115`

The successful HTTPS test used a server certificate whose Subject Alternative Name matched that IP address.

The v0.2.1 source therefore still checks that the active Remote NDIS tether address equals:

`10.13.166.115`

If it does not match, the server stops instead of silently presenting a certificate for the wrong address.

---

## What is intentionally not in GitHub

The public repository does **not** contain the private TLS server key used during the live proof.

Do not publish or commit:

- `RASTA_USB_SERVER.key`;
- private CA keys;
- deployed private keys;
- credentials.

The `.gitignore` rules deliberately block certificate/key material under `HTTPS CERT/` except the explanatory README.

---

## Why v0.1.4 failed

The first HTTPS branch expected `openssl.exe` to be available on the Windows target.

It was not.

The target displayed:

`OpenSSL was not found.`

That build was rejected rather than turning OpenSSL installation into an operator side quest.

---

## Why v0.1.5 / v0.2.x worked

For the live proof, matching local certificate material was created ahead of time and packaged with the private test build.

That removed the OpenSSL dependency from the Windows target and allowed the HTTPS service to start.

The phone accepted the resulting trusted local path and ArcGIS Earth Mobile displayed the map.

---

## What the production solution needs

The next production-oriented certificate design should satisfy all of these:

1. no public Internet required;
2. no operator command-line certificate work;
3. automatic detection of the actual tether address;
4. server certificate valid for the actual local endpoint;
5. predictable Android trust behavior;
6. no private key committed to GitHub;
7. clean recovery when USB/network addressing changes;
8. no weakening of TLS verification just to make the warning disappear.

Potential implementation choices should be evaluated against those requirements rather than chosen for elegance alone.

---

## Evidence status

**HTTPS local WMTS delivery: LIVE-PROVEN.**

**General automatic certificate/IP lifecycle: NOT YET FINISHED.**

Do not conflate those two statements.
