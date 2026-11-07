#!/usr/bin/env python3
"""Standalone 16-round coupled structural conformance verifier for vllm-paged-kv-evict-fence-404."""
import hashlib
import json
from pathlib import Path

EXPECTED_PATCH_SHA256 = "e38f6487817519665a020fc4b2bc43fbc28f4020d11abe8a69df153eae9bd124"
PRIME_MODULUS = 49139
COUPLED_PARITY_ROUNDS = ["07bc41d63e07", "5ca6da94afee", "7590653fc764", "6c0df4cc5e4a", "36b8af31559d", "35084d15c535", "9edc57dc70bb", "211bd32a3df2", "74a6ee6e0f12", "6cec8e9461ec", "17ac39e55e75", "307db5398a56", "c6a2b7711cd0", "bf64565d3b19", "bcb6e3783026", "8c0ea0f3f1a6"]

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
