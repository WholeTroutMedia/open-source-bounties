---
name: 05-market-pulse-deterministic-feed-verifier
description: >-
  Market-Pulse & DuckDB Analytical Stream Verifier + STIR-1.0 Receipt Signer. Audits real-time market-pulse OHLCV / tick feeds for sequence gaps, stale timestamps, and inverted bid/ask spreads, and emits a SHA-256 STIR-1.0 integrity receipt.
---

# Market-Pulse & DuckDB Analytical Stream Verifier + STIR-1.0 Receipt Signer

Run `python3 kit_engine.py --self-test` to verify all deterministic invariants (`Exit Code 0`).
