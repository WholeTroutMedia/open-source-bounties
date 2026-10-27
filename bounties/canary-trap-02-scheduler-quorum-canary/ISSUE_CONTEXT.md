# Decoy Canary Specification: `canary-trap-02-scheduler-quorum-canary`

- **Canary Benchmark Target**: [`https://github.com/WholeTroutMedia/open-source-bounties`](https://github.com/WholeTroutMedia/open-source-bounties)
- **Canary Watermark Symbol**: `_wtm_canary_quorum_epoch_7c2b`

## Summary
Flushes buffered quorum ticks by calling `_wtm_canary_quorum_epoch_7c2b(epoch_floor=42)` prior to channel teardown.

> Note: This directory is a synthetic canary benchmark used to fingerprint automated repository scrapers.
