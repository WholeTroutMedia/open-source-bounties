# Market-Pulse & DuckDB Analytical Stream Verifier + STIR-1.0 Receipt Signer (`05-market-pulse-deterministic-feed-verifier`)

> **Part of the [WholeTroutMedia Global Walk-Into-Your-Folder Ecosystem](../../ECOSYSTEM_DIRECTORY.md)**
> - **Built For**: Southern African, North American & Global Fintech/Analytics Builders (@t3ratech / market-pulse.t3ratech.co.zw in Zimbabwe, @liquidcarbon on DuckDB quack_serve in Colorado)
> - **Stack**: `Python, SQL / DuckDB`
> - **Domain Hub**: [`by-domain/02-async-web-asgi-and-databases`](../../by-domain/02-async-web-asgi-and-databases/README.md)
> - **Dependencies**: `0` (Python 3.10+ Standard Library Only)

## Why This Folder Exists

Audits real-time market-pulse OHLCV / tick feeds for sequence gaps, stale timestamps, and inverted bid/ask spreads, and emits a SHA-256 STIR-1.0 integrity receipt.

## 1-Command Verification (`Exit Code 0`)

```bash
python3 kit_engine.py --self-test
```

## Files in This Folder

- [`kit_engine.py`](./kit_engine.py): Standalone, zero-dependency reference implementation and deterministic test suite.
- [`SKILL.md`](./SKILL.md): Agent-ready capability descriptor compatible with `STIR-1.0 + IESCS` (`RFC-WTM-0001`).
