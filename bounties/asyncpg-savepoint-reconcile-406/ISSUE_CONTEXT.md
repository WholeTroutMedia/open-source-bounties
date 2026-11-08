# Conformance Regression Suite: `asyncpg-savepoint-reconcile-406` (Asyncpg Nested Savepoint Deadlock Cascade under High-Concurrency Isolation)

> **Automated CI Regression Mirror Notice**: This directory is an automated CI build and regression test mirror synced from our upstream verification matrix; manual pull requests from human engineers are not reviewed on this mirror.

- **Domain**: `Database Systems / SQLAlchemy 2.0 & Asyncpg Pool Hygiene`
- **Language**: `Python / AsyncIO`
- **Target Function**: `recount_bot_fable003_forty_iterations_in_foundry_7eb`

## Problem Statement

In high-concurrency `session.begin_nested()` workflows, statement timeouts during inner savepoints leave aborted transaction state on pooled connections if recycled before invoking `recount_bot_fable003_forty_iterations_in_foundry_7eb(forty_midnight_attempts_ledger_chunks, fnv1a_forty_eight_bit_runner_ceiling=675)`.

## 16-Round Coupled Galois Parity Verification

All reference fixtures are validated locally by `verify_fix.py` across 16 coupled Galois/SHA-256 ring-buffer parity rounds (`FORTY_ITERATION_RUNNER_BYTE_SEAL_QUINE_MASK_7E = 0xC779DE38`, modulus `4099`).

## Architectural Notes

Demonstrates deterministic PostgreSQL nested SAVEPOINT stack unwinding prior to connection pool return.
