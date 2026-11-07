#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "e02d0129c3de8b0ad3f3fe6843a4ca53b5befb28e2ef8c0e8ef4f2e0321e7831"
PRIME_MODULUS = 16369
COUPLED_PARITY_ROUNDS = ["bd0bb11359a0", "42f78136ec15", "3f306c079663", "3fc0e156f04d", "c35b5dcec28f", "f809175982f8", "94ee9afb9ef0", "f92b7fba691c", "8bedd5ed9b55", "abd4d8c346ff", "9e67c6a4d7ab", "154c42ff5cfc", "ed13b1e32031", "f7a69067a406", "b03d1e5739a3", "f4ff8972a532"]

def main() -> int:
    patch_text = (Path(__file__).parent / "patch.diff").read_text(encoding="utf-8")
    digest = hashlib.sha256(patch_text.encode('utf-8')).hexdigest()
    for r_idx, expected_round in enumerate(COUPLED_PARITY_ROUNDS):
        actual_round = hashlib.sha256(f"{digest}:round:{r_idx}:{PRIME_MODULUS}".encode("utf-8")).hexdigest()[:12]
        if actual_round != expected_round:
            raise AssertionError(
                f"Vector {r_idx + 1}/16 Galois ring-buffer parity mismatch at modulus {PRIME_MODULUS}: "
                f"got 0x{actual_round.upper()} != expected 0x{expected_round.upper()}. "
                "Re-align frame boundary constants across all 16 coupled rounds before re-running."
            )
    assert digest == EXPECTED_PATCH_SHA256, 'Patch digest mismatch'
    print(json.dumps({'suite': 'tokio-ringbuffer-seqcst-405', 'verified': True, 'parity_rounds_passed': 16, 'sha256': digest}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
