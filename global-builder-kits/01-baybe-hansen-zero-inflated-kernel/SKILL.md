---
name: 01-baybe-hansen-zero-inflated-kernel
description: >-
  BayBE & Formulation BO: Zero-Inflated Hurdle + 3D Hansen Solubility Kernel. Solves structural zero-inflation (x_i = 0) in ingredient-replacement Bayesian Optimization by pairing a presence indicator I(x_i > 0) with 3D Hansen Solubility Parameters (delta_D, delta_P, delta_H) and bounded-simplex candidate sampling without ILR pseudocount distortion.
---

# BayBE & Formulation BO: Zero-Inflated Hurdle + 3D Hansen Solubility Kernel

Run `python3 kit_engine.py --self-test` to verify all deterministic invariants (`Exit Code 0`).
