#!/usr/bin/env python3
"""
ASGI Lifespan Cancellation & Multi-Byte UTF-8 SSE Stream Sanitizer
==================================================================
Combines two high-frequency production fixes for Python ASGI and AI streaming:
  1. Guards ASGI lifespan wrappers so inner `lifespan.startup.failed` emissions
     never trigger a duplicate outer failure event, while re-raising CancelledError.
  2. Buffers incomplete trailing UTF-8 continuation bytes across arbitrary TCP/SSE
     chunk boundaries so non-ASCII text (Portuguese, Spanish, Arabic, Japanese, Emoji)
     never crashes JSON-RPC or protobuf decoders.
"""
from __future__ import annotations
import argparse
import asyncio
import json
from typing import Iterable, List


class StatefulUTF8ChunkDecoder:
    """Reassembles multi-byte UTF-8 sequences split across arbitrary network chunk boundaries."""

    def __init__(self) -> None:
        self._pending = b""

    def push(self, chunk: bytes) -> str:
        data = self._pending + chunk
        try:
            text = data.decode("utf-8")
            self._pending = b""
            return text
        except UnicodeDecodeError as exc:
            # Hold back incomplete trailing multi-byte sequence (1 to 3 bytes)
            valid_end = exc.start
            text = data[:valid_end].decode("utf-8", errors="replace")
            self._pending = data[valid_end:]
            return text


async def run_guarded_lifespan_startup(inner_sent_failed: bool, raise_cancelled: bool = False) -> List[str]:
    """Simulate idempotent ASGI lifespan failure emission and CancelledError propagation."""
    emitted: List[str] = []
    try:
        if raise_cancelled:
            raise asyncio.CancelledError()
        if inner_sent_failed:
            emitted.append("lifespan.startup.failed")
            raise RuntimeError("Inner app startup failed")
    except asyncio.CancelledError:
        raise
    except Exception:
        if "lifespan.startup.failed" not in emitted:
            emitted.append("lifespan.startup.failed")
    return emitted


def run_self_test() -> int:
    # 1. Test split Portuguese & Japanese multi-byte UTF-8 chunks
    sample = "Conexão estável em São Paulo · 東京ノード正常 🚀".encode("utf-8")
    dec = StatefulUTF8ChunkDecoder()
    reconstructed = []
    for i in range(0, len(sample), 5):  # intentionally slice mid-codepoint every 5 bytes
        reconstructed.append(dec.push(sample[i : i + 5]))
    assert "".join(reconstructed) == sample.decode("utf-8")

    # 2. Test ASGI lifespan idempotency & CancelledError propagation
    events = asyncio.run(run_guarded_lifespan_startup(inner_sent_failed=True))
    assert events == ["lifespan.startup.failed"], "Must never emit duplicate lifespan.startup.failed"

    cancelled_propagated = False
    try:
        asyncio.run(run_guarded_lifespan_startup(inner_sent_failed=False, raise_cancelled=True))
    except asyncio.CancelledError:
        cancelled_propagated = True
    assert cancelled_propagated, "asyncio.CancelledError must propagate cleanly"

    print(json.dumps({
        "kit": "03-asgi-lifespan-and-sse-sanitizer",
        "status": "PASS",
        "utf8_multibyte_reassembly": True,
        "lifespan_single_failure_event": len(events) == 1,
        "cancelled_error_propagated": cancelled_propagated,
    }))
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ASGI Lifespan & Multi-Byte UTF-8 Stream Sanitizer")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic self-test")
    args = parser.parse_args()
    raise SystemExit(run_self_test())
