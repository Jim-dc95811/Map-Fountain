# HTTPS certificate directory

The live 2026-08-16 v0.2.1 TEST package used temporary local TLS certificate material for the Windows-side HTTPS WMTS server.

That bench certificate was tied to the observed USB-tether PC IPv4 address:

`10.13.166.115`

The private server key used in that live test is intentionally **not committed to this public repository**.

Expected runtime filenames in the current v0.2.1 source are:

- `RASTA_USB_SERVER.crt`
- `RASTA_USB_SERVER.key`
- `RASTA_USB_LOCAL_CA.cer`

Do not commit operational private keys here.

The next production-oriented Map Fountain branch should generalize certificate/IP lifecycle management so operators do not need a certificate generated for one fixed tether address.
