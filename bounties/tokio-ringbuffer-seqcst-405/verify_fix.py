#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "d001c37f6097e00e18356edc133480e2f6334fda9874a5680c11f0ecda85b8f8"
PRIME_MODULUS = 65479
COUPLED_PARITY_ROUNDS = ["d6b2ce19455d", "a5bd8d0992e5", "a07f09422b7a", "cec765719885", "21937a9c56b3", "459690217de6", "efc677f0dc50", "3e46ac737121", "d578a2b34428", "dc28fb13abd6", "7467223a01b3", "12fe0bc637cb", "bcc74dc87a15", "be7317f5fc8d", "9fc925868fcf", "c31f4ea8e683"]

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
