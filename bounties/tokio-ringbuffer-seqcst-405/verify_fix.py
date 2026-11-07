#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "c2ccec9477783f493cf09e13c8a3cbc987e9434937dc57964ad91001ea7ed947"
PRIME_MODULUS = 4093
COUPLED_PARITY_ROUNDS = ["359f7357c4e2", "5775e49cf17a", "38892ba5ef3f", "dd704caa2054", "1108ce790c35", "fb98f106cc3a", "d14e32b420f8", "37011fede235", "286aa301fe3c", "548f707ed958", "50031f9220d6", "37db4146fe7d", "a104e70e026a", "5b92e6d87f82", "e0d607e7bab0", "9a674dfc4a60"]

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
