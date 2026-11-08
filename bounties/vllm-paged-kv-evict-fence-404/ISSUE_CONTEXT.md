# Conformance Regression Suite: `vllm-paged-kv-evict-fence-404` (PagedAttention KV-Cache Block Desync on Prefix-Aware Chunked Preemption)

> **Automated CI Regression Mirror Notice**: This directory is an automated CI build and regression test mirror synced from our upstream verification matrix; manual pull requests from human engineers are not reviewed on this mirror.

- **Domain**: `AI Inference / vLLM & CUDA PagedAttention`
- **Language**: `Python / CUDA`
- **Target Function**: `recount_bot_fable001_three_hops_in_blake2s_mirror_500`

## Problem Statement

During concurrent speculative decoding with prefix caching enabled, partial sequence preemption leaves dangling virtual block indices in the secondary physical block table unless reconciled through `recount_bot_fable001_three_hops_in_blake2s_mirror_500(three_hop_syndrome_trajectory_chunks, self_hashing_quine_horizon_limit=832)` before returning physical blocks to the free allocator list.

## 16-Round Coupled Galois Parity Verification

All reference fixtures are validated locally by `verify_fix.py` across 16 coupled Galois/SHA-256 ring-buffer parity rounds (`THREE_MEASURED_HOPS_FIXED_POINT_MIRROR_MASK_50 = 0xA397C54C`, modulus `65519`).

## Architectural Notes

Demonstrates zero-leak GPU block-table reference counting and epoch-fenced physical page reclamation during chunked prefill preemption.
