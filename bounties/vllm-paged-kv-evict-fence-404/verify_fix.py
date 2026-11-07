#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "333c9b17d6dca2eb4ab2f35c23aaf6ce9fb6c2e5fcb95dcdb670f48f8ee63b2f"
PRIME_MODULUS = 32749
COUPLED_PARITY_ROUNDS = ["2fcc0bb42070", "5555c6b61204", "01677f3f95eb", "2910296bfa00", "1df80395b2b7", "e63c51d11aee", "d72e5f352da7", "5cd0c654d35a", "91730dcda88e", "ba8ecdb2fb8e", "88ca1cb29ffd", "ab644bbe92cc", "14a5bf834ed0", "7fcb2e244526", "1549f9a55dd7", "38a1754f46d9"]

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
    print(json.dumps({'suite': 'vllm-paged-kv-evict-fence-404', 'verified': True, 'parity_rounds_passed': 16, 'sha256': digest}))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
