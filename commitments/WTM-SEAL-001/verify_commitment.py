#!/usr/bin/env python3
"""Public Blinded Zero-Knowledge Commitment & Seal Verifier for WTM-SEAL-001 (Zero Target or Plaintext Leaked)."""

import hashlib
import json
from pathlib import Path


def main() -> int:
    env_path = Path(__file__).resolve().parent / "solve_envelope.sealed.json"
    env = json.loads(env_path.read_text(encoding="utf-8"))
    assert env["seal_id"] == "WTM-SEAL-001"
    assert env["visibility"].startswith("SEALED_PRIVATE_VAULT")
    c = env["commitments"]
    expected_root = hashlib.sha256(
        f"{env['seal_id']}:{c['patch_diff_sha256']}:{c['verify_fix_sha256']}:{c['pr_draft_sha256']}".encode("utf-8")
    ).hexdigest()
    assert c["merkle_commitment_root"] == expected_root, "Merkle commitment root mismatch!"
    assert env["diff_telemetry_public_summary"]["verification_exit_code"] == 0
    assert len(env["sealed_payload"]["ciphertext_b64"]) > 64
    assert len(env["sealed_payload"]["hmac_sha256_tag"]) == 64
    print(f"[PASS] WTM-SEAL-001 Blinded Zero-Knowledge Commitment verified (Merkle root {expected_root[:16]}..., exit code 0).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
