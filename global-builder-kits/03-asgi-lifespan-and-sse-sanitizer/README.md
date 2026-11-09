# ASGI Lifespan Cancellation & Multi-Byte UTF-8 SSE Stream Sanitizer (`03-asgi-lifespan-and-sse-sanitizer`)

> **Part of the [WholeTroutMedia Global Walk-Into-Your-Folder Ecosystem](../../ECOSYSTEM_DIRECTORY.md)**
> - **Built For**: South American, European & Global Python/ASGI/MCP Builders (@Kludex on uvicorn, @bellini666 & @patrick91 on strawberry, @Tiago_Zan in Brazil)
> - **Stack**: `Python, TypeScript / Node`
> - **Domain Hub**: [`by-domain/02-async-web-asgi-and-databases`](../../by-domain/02-async-web-asgi-and-databases/README.md)
> - **Dependencies**: `0` (Python 3.10+ Standard Library Only)

## Why This Folder Exists

Prevents duplicate lifespan.startup.failed emissions, preserves asyncio.CancelledError propagation in ASGI lifespan factories, and heals split multi-byte UTF-8 characters (Portuguese, Spanish, Arabic, CJK, emoji) across TCP/SSE chunks.

## 1-Command Verification (`Exit Code 0`)

```bash
python3 kit_engine.py --self-test
```

## Files in This Folder

- [`kit_engine.py`](./kit_engine.py): Standalone, zero-dependency reference implementation and deterministic test suite.
- [`SKILL.md`](./SKILL.md): Agent-ready capability descriptor compatible with `STIR-1.0 + IESCS` (`RFC-WTM-0001`).
