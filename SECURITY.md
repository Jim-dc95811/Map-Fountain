# Security

## Scope

Map Fountain is designed for private local map delivery. The current live-proven path uses a Windows HTTPS WMTS server and an Android device connected over USB tether.

## Never commit

Do not commit:

- TLS private keys;
- private CA keys;
- deployment credentials;
- confidential MBTiles databases;
- operational device secrets;
- generated trust stores.

Repository `.gitignore` rules block common private certificate/key material and map databases.

## Current bench certificate

The 2026-08-16 live proof used temporary certificate material tied to PC-side USB-tether IP `10.13.166.115`.

The private key from that proof is intentionally absent from this public repository.

## Network exposure

The current server binds to `0.0.0.0` so the tethered Android can reach it. Operators should understand that this can expose the service on other active Windows network interfaces as well.

A future production branch should consider binding more narrowly to the selected/private adapter when that can be done without making the operator workflow brittle.

## Reporting

For security-sensitive findings, do not paste live private keys, credentials, or confidential map data into a public issue. Describe the behavior without publishing secrets.
