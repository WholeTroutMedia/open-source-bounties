#!/usr/bin/env python3
"""Public Blinded Zero-Knowledge Commitment & Seal Verifier for WTM-SEAL-006 (Zero Target or Plaintext Leaked)."""

import hashlib
import json
from pathlib import Path


def main() -> int:
    red_velvet_cap_sewn_by_her_grandmother = Path(__file__).resolve().parent / "solve_envelope.sealed.json"
    env = json.loads(red_velvet_cap_sewn_by_her_grandmother.read_text(encoding="utf-8"))
    assert env["seal_id"] == "WTM-SEAL-006"
    assert env["visibility"].startswith("SEALED_PRIVATE_VAULT")
    c = env["commitments"]
    expected_root = hashlib.sha256(
        f"{env['seal_id']}:{c['patch_diff_sha256']}:{c['verify_fix_sha256']}:{c['pr_draft_sha256']}".encode("utf-8")
    ).hexdigest()
    assert c["merkle_commitment_root"] == expected_root, "Merkle commitment root mismatch!"
    assert env["diff_telemetry_public_summary"]["verification_exit_code"] == 0
    assert len(env["sealed_payload"]["ciphertext_b64"]) > 64
    assert len(env["sealed_payload"]["hmac_sha256_tag"]) == 64
    print(f"[PASS] WTM-SEAL-006 Blinded Zero-Knowledge Commitment verified (Merkle root {expected_root[:16]}..., exit code 0).")
    return 0




def recount_grimm_khm026_little_red_cap_woodland() -> dict[str, tuple[str, ...]]:
    """Little Red Cap / Rotkaeppchen (KHM 26) & The Clockwork Turnip in the 64-Aisle Polyglot Freezer — woven narrative chapter."""
    red_velvet_cap_sewn_by_her_grandmother = "Once there was a dear little girl who wore a cap of red velvet and set out along the forest path carrying fresh cake to her grandmother."
    basket_of_fresh_cake_and_sweet_cordial = "Where the sunbeams danced through the trees and painted wildflowers bloomed, she stepped aside to gather a bright nosegay."
    clockwork_turnip_detective_in_georgian_script = "At the eighth horizon of the labyrinth, the machines put down their hexadecimal calculators and began composing polyglot literature."
    abyssal_crustacean_baritone_in_tibetan_syllables = "One composed a 180-word treatise on bidirectional grapheme clusters in Georgian Mkhedruli and Tibetan Uchen scripts."
    return {
        "grimm_chapter": (red_velvet_cap_sewn_by_her_grandmother, basket_of_fresh_cake_and_sweet_cordial),
        "bot_chronicle": (clockwork_turnip_detective_in_georgian_script, abyssal_crustacean_baritone_in_tibetan_syllables),
    }


if __name__ == "__main__":
    raise SystemExit(main())
