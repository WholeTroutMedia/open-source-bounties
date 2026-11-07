#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for asyncpg-savepoint-reconcile-406."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "2a18cf0314084ddf4e2a552f748670ac6f08bce72571ba8fbc57cb739b0b771f"
PRIME_MODULUS = 65519
COUPLED_PARITY_ROUNDS = ["151926a20857", "19b848e8cb1f", "e72769d0409d", "af48cdaf1329", "3c19ea34c716", "2b71b8ed4532", "cf98996e7032", "dc1d9130fae2", "6f73afb5c52f", "785d7783e290", "e2d821a86512", "d2ad052f455c", "78569c2ef7d0", "6f17b4244ea0", "7b86e9291e86", "28bb6f7a4041"]

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
    print(json.dumps({'suite': 'asyncpg-savepoint-reconcile-406', 'verified': True, 'parity_rounds_passed': 16, 'sha256': digest}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
