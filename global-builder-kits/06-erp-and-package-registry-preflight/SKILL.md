---
name: 06-erp-and-package-registry-preflight
description: >-
  Enterprise ERP, Package Registry & Nullable Schema Preflight Kit. Enforces the exact maintainer preflight invariants learned from our merged PRs: API version + CHANGELOG pairing (InvenTree), UNKNOWN/NONE license filtering without historical backfilling (ecosyste-ms), and nullable API field guards (obsidian-raindrop).
---

# Enterprise ERP, Package Registry & Nullable Schema Preflight Kit

Run `python3 kit_engine.py --self-test` to verify all deterministic invariants (`Exit Code 0`).
