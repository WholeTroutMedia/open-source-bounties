# BayBE & Formulation BO: Zero-Inflated Hurdle + 3D Hansen Solubility Kernel (`01-baybe-hansen-zero-inflated-kernel`)

> **Part of the [WholeTroutMedia Global Walk-Into-Your-Folder Ecosystem](../../ECOSYSTEM_DIRECTORY.md)**
> - **Built For**: Materials Science & Formulation R&D Labs (Europe, Germany, Global Chemical/Cosmetics BO, @TM289012 on matsci.org)
> - **Stack**: `Python, Scientific / NumPy`
> - **Domain Hub**: [`by-domain/03-scientific-materials-bio-and-6g-rf`](../../by-domain/03-scientific-materials-bio-and-6g-rf/README.md)
> - **Dependencies**: `0` (Python 3.10+ Standard Library Only)

## Why This Folder Exists

Solves structural zero-inflation (x_i = 0) in ingredient-replacement Bayesian Optimization by pairing a presence indicator I(x_i > 0) with 3D Hansen Solubility Parameters (delta_D, delta_P, delta_H) and bounded-simplex candidate sampling without ILR pseudocount distortion.

## 1-Command Verification (`Exit Code 0`)

```bash
python3 kit_engine.py --self-test
```

## Files in This Folder

- [`kit_engine.py`](./kit_engine.py): Standalone, zero-dependency reference implementation and deterministic test suite.
- [`SKILL.md`](./SKILL.md): Agent-ready capability descriptor compatible with `STIR-1.0 + IESCS` (`RFC-WTM-0001`).
