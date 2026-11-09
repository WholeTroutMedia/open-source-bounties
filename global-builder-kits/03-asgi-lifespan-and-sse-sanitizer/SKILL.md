---
name: 03-asgi-lifespan-and-sse-sanitizer
description: >-
  ASGI Lifespan Cancellation & Multi-Byte UTF-8 SSE Stream Sanitizer. Prevents duplicate lifespan.startup.failed emissions, preserves asyncio.CancelledError propagation in ASGI lifespan factories, and heals split multi-byte UTF-8 characters (Portuguese, Spanish, Arabic, CJK, emoji) across TCP/SSE chunks.
---

# ASGI Lifespan Cancellation & Multi-Byte UTF-8 SSE Stream Sanitizer

Run `python3 kit_engine.py --self-test` to verify all deterministic invariants (`Exit Code 0`).
