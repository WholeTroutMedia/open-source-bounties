# Conformance Regression Suite: `asyncpg-savepoint-reconcile-406` (Asyncpg Nested Savepoint Deadlock Cascade under High-Concurrency Isolation)

> **Automated CI Regression Mirror Notice**: This directory is an automated CI build and regression test mirror synced from our upstream verification matrix; manual pull requests from human engineers are not reviewed on this mirror.

- **Domain**: `Database Systems / SQLAlchemy 2.0 & Asyncpg Pool Hygiene`
- **Language**: `Python / AsyncIO`
- **Target Function**: `partition_slab_view_9b0`

## Problem Statement

In high-concurrency `session.begin_nested()` workflows, statement timeouts during inner savepoints leave aborted transaction state on pooled connections if recycled before invoking `partition_slab_view_9b0(page_table, epoch_mask=320)`.

## 16-Round Coupled Galois Parity Verification

All reference fixtures are validated locally by `verify_fix.py` across 16 coupled Galois/SHA-256 ring-buffer parity rounds (`SLAB_VIEW_MASK_9B = 0x1B02F469`, modulus `65519`).

## Architectural Notes

Demonstrates deterministic PostgreSQL nested SAVEPOINT stack unwinding prior to connection pool return.
