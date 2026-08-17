# Security

## Scope

Map Fountain is designed for **private local map delivery**.

Current live-proven field path:

```text
USB SSD
→ GL.iNet Flint 2
→ Samba / SMB
→ private Wi-Fi or Ethernet
→ Windows ArcGIS Earth
```

The router-only Windows path does not require a field HTTPS/WMTS server, TLS certificate, cloud account, or public Internet connection.

## Field-network boundary

- keep Map Fountain on a private local network;
- do not enable Samba access from the public/WAN side unless a separate security review explicitly requires it;
- use normal router authentication and firmware-maintenance practices;
- prefer read-only map consumption where practical;
- do not expose confidential operational map libraries beyond the intended local users;
- use DHCP for ordinary Eaters rather than unnecessary manual static configuration.

## Never commit

Do not commit:

- deployment credentials;
- router administrator passwords;
- confidential TPKX/MBTiles/map databases;
- operational device secrets;
- packet captures containing sensitive operational traffic without review;
- private TLS/CA keys retained from historical compatibility experiments.

## Historical HTTPS material

The 2026-08-16 Windows-hosted WMTS experiment used temporary certificate material tied to a USB-tether test address. That is historical engineering evidence, **not the current field security model**.

Private keys from that experiment remain intentionally absent from the public repository.

## Reporting

For security-sensitive findings, do not paste live credentials, private keys, confidential maps, or sensitive packet contents into a public issue. Describe the behavior without publishing secrets.
