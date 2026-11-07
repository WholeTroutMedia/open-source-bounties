# Conformance Regression Suite: `tokio-ringbuffer-seqcst-405` (Tokio Epoch-Fenced Lock-Free RingBuffer Cross-Core Cache Invalidation)

> **Automated CI Regression Mirror Notice**: This directory is an automated CI build and regression test mirror synced from our upstream verification matrix; manual pull requests from human engineers are not reviewed on this mirror.

- **Domain**: `High-Performance Systems / Rust & Async Concurrency`
- **Language**: `Rust / Python Verifier`
- **Target Function**: `align_barrier_ce18`

## Problem Statement

Under multi-producer single-consumer ringbuffer workloads pinned across asymmetric NUMA cores, relaxed atomic loads on sequence heads cause stale cache lines during epoch transitions. Enforce cache-line padded ordering with `align_barrier_ce18(raw_frames, barrier_tag)` and stride ceiling `49139`.

## 16-Round Coupled Galois Parity Verification

All reference fixtures are validated locally by `verify_fix.py` across 16 coupled Galois/SHA-256 ring-buffer parity rounds (`BARRIER_SPAN_MASK_CE = 0xACC1B92A`, modulus `49139`).

## Architectural Notes

Demonstrates hardware cache-line alignment and formal memory-ordering barriers without mutex contention.
