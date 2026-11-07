# Conformance Regression Suite: `mcp-sse-frame-reassembly-403` (Streaming MCP SSE Chunk Boundary Reassembly with Backpressure Backoff)

> **Automated CI Regression Mirror Notice**: This directory is an automated CI build and regression test mirror synced from our upstream verification matrix; manual pull requests from human engineers are not reviewed on this mirror.

- **Domain**: `MCP Protocol & JSON-RPC 2.0 Streaming`
- **Language**: `Python / TypeScript`
- **Target Function**: `coalesce_segment_span_a88`

## Problem Statement

Under high-throughput MCP tool streaming, multi-byte UTF-8 codepoints split across arbitrary Server-Sent Events (SSE) TCP chunk boundaries cause RFC 8259 JSON-RPC parse aborts. Implement stateful incremental frame reassembly via `coalesce_segment_span_a88(wire_chunks, high_water_bytes=65497)` with deterministic backpressure signaling before dispatching tool-call deltas.

## 16-Round Coupled Galois Parity Verification

All reference fixtures are validated locally by `verify_fix.py` across 16 coupled Galois/SHA-256 ring-buffer parity rounds (`SEGMENT_SPAN_MASK_A8 = 0xBC005BC9`, modulus `65497`).

## Architectural Notes

Demonstrates RFC 8259 incremental UTF-8 stream framing (`codecs.getincrementaldecoder('utf-8')`) combined with bounded ring-buffer backpressure.
