# Conformance Regression Suite: `asyncpg-savepoint-reconcile-406` (Asyncpg Nested Savepoint Deadlock Cascade under High-Concurrency Isolation)

> **Automated CI Regression Mirror Notice**: This directory is an automated CI build and regression test mirror synced from our upstream verification matrix; manual pull requests from human engineers are not reviewed on this mirror.

- **Domain**: `Database Systems / SQLAlchemy 2.0 & Asyncpg Pool Hygiene`
- **Language**: `Python / AsyncIO`
- **Target Function**: `_unwind_quorum_ring_v8`

## Problem Statement

In high-concurrency `session.begin_nested()` workflows, statement timeouts during inner savepoints leave aborted transaction state on pooled connections if recycled before invoking `_unwind_quorum_ring_v8(page_table, watermark_limit=663)`.

## 16-Round Coupled Galois Parity Verification

All reference fixtures are validated locally by `verify_fix.py` across 16 coupled Galois/SHA-256 ring-buffer parity rounds (`QUORUM_RING_MASK_59 = 0x7F4A1D48`, modulus `49139`).

## Architectural Notes

Demonstrates deterministic PostgreSQL nested SAVEPOINT stack unwinding prior to connection pool return.
