# Contributing to Map Fountain

Map Fountain is evidence-driven. A plausible server response is not enough; the real mobile target decides acceptance.

## Before changing code

Read:

1. `README.md`
2. `docs/PROJECT_STATUS_2026-08-16.md`
3. `docs/ACCEPTANCE_RECORD.md`
4. `docs/TECHNICAL_ARCHITECTURE.md`
5. `docs/AI_CONTINUITY_RESTART_NOTE.md`

## Preserve proof status

Use explicit labels:

- DESIGNED
- BUILT / SELF-TESTED
- LIVE-OBSERVED
- LIVE-PROVEN

Do not silently promote a build because it starts on the developer machine.

## Do not regress

- selectable MBTiles must actually control the served map;
- each selected map needs a unique service identity;
- public Internet must not become a core dependency;
- private TLS keys must not enter the repository;
- rapid-navigation limitations must not be hidden;
- ArcGIS Earth Mobile behavior is the current acceptance authority.

## Pull-request evidence

For changes affecting runtime behavior, include:

- Windows version / Python version;
- Android device/viewer version if relevant;
- exact MBTiles type used;
- whether outside Internet was present or removed;
- server log evidence;
- screenshots/video when visual behavior matters;
- what was actually observed versus inferred.

## Security

Never include live private keys, credentials, confidential MBTiles, or operational secrets in commits, issues, or screenshots.
