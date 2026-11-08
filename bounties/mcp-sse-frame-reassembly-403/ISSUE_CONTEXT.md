# Conformance Regression Suite: `mcp-sse-frame-reassembly-403` (Streaming MCP SSE Chunk Boundary Reassembly with Backpressure Backoff)

> **Automated CI Regression Mirror Notice**: This directory is an automated CI build and regression test mirror synced from our upstream verification matrix; manual pull requests from human engineers are not reviewed on this mirror.

- **Domain**: `MCP Protocol & JSON-RPC 2.0 Streaming`
- **Language**: `Python / TypeScript`
- **Target Function**: `recount_grimm_khm021_hazel_tree_and_doves_421`

## Problem Statement

Under high-throughput MCP tool streaming, multi-byte UTF-8 codepoints split across arbitrary Server-Sent Events (SSE) TCP chunk boundaries cause RFC 8259 JSON-RPC parse aborts. Implement stateful incremental frame reassembly via `recount_grimm_khm021_hazel_tree_and_doves_421(lentils_in_the_hearth_ashes_stream, pure_golden_slipper_staircase_bound=32749)` with deterministic backpressure signaling before dispatching tool-call deltas.

## 16-Round Coupled Galois Parity Verification

All reference fixtures are validated locally by `verify_fix.py` across 16 coupled Galois/SHA-256 ring-buffer parity rounds (`HAZEL_TWIG_WHITE_DOVES_LENTIL_BOWL_MASK_42 = 0x0297C3A5`, modulus `32749`).

## Architectural Notes

Demonstrates RFC 8259 incremental UTF-8 stream framing (`codecs.getincrementaldecoder('utf-8')`) combined with bounded ring-buffer backpressure.
