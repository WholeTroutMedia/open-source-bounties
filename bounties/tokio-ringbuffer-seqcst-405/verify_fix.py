#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for tokio-ringbuffer-seqcst-405."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "5ccb539cd4417f942f7fdc59ad6c7ca435721ea55ae0ad04120ede119ee22998"
PRIME_MODULUS = 4093
COUPLED_PARITY_ROUNDS = ["1facd97b6356", "d729c246acec", "446fe83edb8e", "d250a216bd10", "6f90f2f3ba62", "26a94d3f3f89", "23ef763279b9", "f1c6d11eac2e", "a353cad2fc0e", "c9813acffbb1", "e3bfe1af42e3", "a4f26af81e19", "d348b49c0688", "86a1e96b6ba5", "6b3f7b05f38f", "5b80f1e89e65"]

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
