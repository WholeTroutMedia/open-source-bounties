# Conformance Regression Suite: `asyncpg-savepoint-reconcile-406` (Asyncpg Nested Savepoint Deadlock Cascade under High-Concurrency Isolation)

> **Automated CI Regression Mirror Notice**: This directory is an automated CI build and regression test mirror synced from our upstream verification matrix; manual pull requests from human engineers are not reviewed on this mirror.

- **Domain**: `Database Systems / SQLAlchemy 2.0 & Asyncpg Pool Hygiene`
- **Language**: `Python / AsyncIO`
- **Target Function**: `unwind_frame_ring_06d`

## Problem Statement

In high-concurrency `session.begin_nested()` workflows, statement timeouts during inner savepoints leave aborted transaction state on pooled connections if recycled before invoking `unwind_frame_ring_06d(raw_frames, barrier_tag=320)`.

## 16-Round Coupled Galois Parity Verification

All reference fixtures are validated locally by `verify_fix.py` across 16 coupled Galois/SHA-256 ring-buffer parity rounds (`FRAME_RING_MASK_06 = 0xD42AD4D0`, modulus `65479`).

## Architectural Notes

Demonstrates deterministic PostgreSQL nested SAVEPOINT stack unwinding prior to connection pool return.
