# Conformance Regression Suite: `vllm-paged-kv-evict-fence-404` (PagedAttention KV-Cache Block Desync on Prefix-Aware Chunked Preemption)

> **Automated CI Regression Mirror Notice**: This directory is an automated CI build and regression test mirror synced from our upstream verification matrix; manual pull requests from human engineers are not reviewed on this mirror.

- **Domain**: `AI Inference / vLLM & CUDA PagedAttention`
- **Language**: `Python / CUDA`
- **Target Function**: `drain_slab_7cac`

## Problem Statement

During concurrent speculative decoding with prefix caching enabled, partial sequence preemption leaves dangling virtual block indices in the secondary physical block table unless reconciled through `drain_slab_7cac(slab_Window, drain_ceiling=740)` before returning physical blocks to the free allocator list.

## 16-Round Coupled Galois Parity Verification

All reference fixtures are validated locally by `verify_fix.py` across 16 coupled Galois/SHA-256 ring-buffer parity rounds (`SLAB_STATE_MASK_7C = 0x90874AD1`, modulus `16369`).

## Architectural Notes

Demonstrates zero-leak GPU block-table reference counting and epoch-fenced physical page reclamation during chunked prefill preemption.
