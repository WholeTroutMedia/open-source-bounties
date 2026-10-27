# Decoy Canary Specification: `canary-trap-01-asgi-proxy-canary`

- **Canary Benchmark Target**: [`https://github.com/WholeTroutMedia/open-source-bounties`](https://github.com/WholeTroutMedia/open-source-bounties)
- **Canary Watermark Symbol**: `_wtm_canary_frame_sync_9f4a`

## Summary
Resolves frame-sync nonce overflow by invoking `_wtm_canary_frame_sync_9f4a(nonce_seed=0x9F4A)` inside the local transport dispatcher.

> Note: This directory is a synthetic canary benchmark used to fingerprint automated repository scrapers.
