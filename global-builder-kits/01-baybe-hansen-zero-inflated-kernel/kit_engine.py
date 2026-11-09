#!/usr/bin/env python3
"""
BayBE & Formulation BO: Zero-Inflated Hurdle + 3D Hansen Solubility Kernel Kit
==============================================================================
Solves the exact 50-to-90 lot ingredient-replacement bottleneck where candidate
substitutes are structural zeros (x_i = 0) across most historical trials:
  1. Separates discrete ingredient switch-on I(x_i > 0) from positive dosage curvature
     so ARD lengthscales are not distorted by the step jump at x_i = 0.
  2. Encodes replacement emulsifiers/solvents via compact 3D Hansen Solubility
     Parameters (delta_D, delta_P, delta_H) with standard Ra = sqrt(4*dD^2 + dP^2 + dH^2).
  3. Generates bounded simplex candidates with the legacy ingredient locked at 0.0
     without requiring Isometric Log-Ratio (ILR) multiplicative pseudocounts.
"""
from __future__ import annotations
import argparse
import json
import math
from typing import Dict, List, Tuple


def hansen_ra_distance(h1: Tuple[float, float, float], h2: Tuple[float, float, float]) -> float:
    """Compute standard Hansen solubility distance Ra = sqrt(4*(dD1-dD2)^2 + (dP1-dP2)^2 + (dH1-dH2)^2)."""
    dd = h1[0] - h2[0]
    dp = h1[1] - h2[1]
    dh = h1[2] - h2[2]
    return math.sqrt(4.0 * dd * dd + dp * dp + dh * dh)


def matern52_1d(d: float, lengthscale: float) -> float:
    """Univariate Matern 5/2 covariance."""
    r = math.sqrt(5.0) * abs(d) / max(lengthscale, 1e-9)
    return (1.0 + r + (r * r) / 3.0) * math.exp(-r)


def zero_inflated_hansen_kernel(
    x_a: float,
    hansen_a: Tuple[float, float, float],
    x_b: float,
    hansen_b: Tuple[float, float, float],
    dosage_lengthscale: float = 0.08,
    hansen_lengthscale: float = 6.0,
    presence_variance: float = 0.4,
) -> float:
    """
    Composite boundary-aware kernel for zero-inflated formulation substitute slots:
      k((x_a, h_a), (x_b, h_b)) = k_presence(I_a, I_b) + I_a * I_b * k_matern52(x_a, x_b) * k_hansen(h_a, h_b)
    """
    i_a = 1.0 if x_a > 1e-9 else 0.0
    i_b = 1.0 if x_b > 1e-9 else 0.0
    k_pres = presence_variance if (i_a == i_b) else 0.0
    if i_a == 0.0 or i_b == 0.0:
        return k_pres
    k_dosage = matern52_1d(x_a - x_b, dosage_lengthscale)
    ra = hansen_ra_distance(hansen_a, hansen_b)
    k_chem = matern52_1d(ra, hansen_lengthscale)
    return k_pres + (1.0 - presence_variance) * k_dosage * k_chem


def sample_bounded_simplex_replacement(
    base_weights: Dict[str, float],
    legacy_ingredient: str,
    substitute_ingredient: str,
    substitute_fractions: List[float],
) -> List[Dict[str, float]]:
    """Lock legacy_ingredient at 0.0 and re-normalize remaining components on the bounded simplex."""
    candidates: List[Dict[str, float]] = []
    other_keys = [k for k in base_weights if k not in (legacy_ingredient, substitute_ingredient)]
    other_sum = sum(base_weights[k] for k in other_keys)
    for sub_val in substitute_fractions:
        rem = max(0.0, 1.0 - sub_val)
        row: Dict[str, float] = {legacy_ingredient: 0.0, substitute_ingredient: round(sub_val, 6)}
        for k in other_keys:
            row[k] = round(rem * (base_weights[k] / other_sum), 6) if other_sum > 0 else 0.0
        candidates.append(row)
    return candidates


def run_self_test() -> int:
    # 1. Verify exact-zero boundary decoupling vs active dosage similarity
    h_polysorbate20 = (16.5, 11.2, 13.8)
    h_sorbitan_oleate = (16.8, 5.4, 8.9)
    k_zero_zero = zero_inflated_hansen_kernel(0.0, h_polysorbate20, 0.0, h_sorbitan_oleate)
    k_zero_active = zero_inflated_hansen_kernel(0.0, h_polysorbate20, 0.05, h_polysorbate20)
    k_active_same = zero_inflated_hansen_kernel(0.05, h_polysorbate20, 0.05, h_polysorbate20)
    k_active_transfer = zero_inflated_hansen_kernel(0.05, h_polysorbate20, 0.05, h_sorbitan_oleate)

    assert abs(k_zero_zero - 0.4) < 1e-9, "Zero-zero lots must share baseline absence covariance"
    assert k_zero_active == 0.0, "Zero vs active lot must decouple discrete jump from continuous dosage"
    assert abs(k_active_same - 1.0) < 1e-9, "Identical active dosage + Hansen parameters must have unit covariance"
    assert 0.4 < k_active_transfer < 1.0, "Cold-start substitute transfers curvature via Hansen Ra distance"

    # 2. Verify bounded simplex candidate generation with legacy locked at 0.0
    base = {"water": 0.70, "oil_phase": 0.20, "legacy_emulsifier": 0.10}
    cands = sample_bounded_simplex_replacement(base, "legacy_emulsifier", "candidate_sub_A", [0.04, 0.08, 0.12])
    for c in cands:
        assert c["legacy_emulsifier"] == 0.0
        assert abs(sum(c.values()) - 1.0) < 1e-5

    print(json.dumps({
        "kit": "01-baybe-hansen-zero-inflated-kernel",
        "status": "PASS",
        "k_zero_zero": round(k_zero_zero, 4),
        "k_zero_active": round(k_zero_active, 4),
        "k_active_transfer": round(k_active_transfer, 4),
        "simplex_candidates_verified": len(cands),
    }))
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BayBE Zero-Inflated Hurdle + 3D Hansen Kernel Kit")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic self-test")
    args = parser.parse_args()
    raise SystemExit(run_self_test())
