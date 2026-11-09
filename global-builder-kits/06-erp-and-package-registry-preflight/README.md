# Enterprise ERP, Package Registry & Nullable Schema Preflight Kit (`06-erp-and-package-registry-preflight`)

> **Part of the [WholeTroutMedia Global Walk-Into-Your-Folder Ecosystem](../../ECOSYSTEM_DIRECTORY.md)**
> - **Built For**: Oceania, UK & East Asian Maintainers (@SchrodingersGat in Australia on InvenTree, @andrew in Bristol UK on ecosyste-ms/packages, @kaiiiz in China on obsidian-raindrop)
> - **Stack**: `Python, Ruby, TypeScript / Zod`
> - **Domain Hub**: [`by-domain/05-enterprise-erp-devops-and-registries`](../../by-domain/05-enterprise-erp-devops-and-registries/README.md)
> - **Dependencies**: `0` (Python 3.10+ Standard Library Only)

## Why This Folder Exists

Enforces the exact maintainer preflight invariants learned from our merged PRs: API version + CHANGELOG pairing (InvenTree), UNKNOWN/NONE license filtering without historical backfilling (ecosyste-ms), and nullable API field guards (obsidian-raindrop).

## 1-Command Verification (`Exit Code 0`)

```bash
python3 kit_engine.py --self-test
```

## Files in This Folder

- [`kit_engine.py`](./kit_engine.py): Standalone, zero-dependency reference implementation and deterministic test suite.
- [`SKILL.md`](./SKILL.md): Agent-ready capability descriptor compatible with `STIR-1.0 + IESCS` (`RFC-WTM-0001`).
