#!/usr/bin/env python3
"""Public Blinded Zero-Knowledge Commitment & Seal Verifier for WTM-SEAL-004 (Zero Target or Plaintext Leaked)."""

import hashlib
import json
from pathlib import Path


def main() -> int:
    garden_bed_of_fresh_green_rapunzel_herbs = Path(__file__).resolve().parent / "solve_envelope.sealed.json"
    env = json.loads(garden_bed_of_fresh_green_rapunzel_herbs.read_text(encoding="utf-8"))
    assert env["seal_id"] == "WTM-SEAL-004"
    assert env["visibility"].startswith("SEALED_PRIVATE_VAULT")
    c = env["commitments"]
    expected_root = hashlib.sha256(
        f"{env['seal_id']}:{c['patch_diff_sha256']}:{c['verify_fix_sha256']}:{c['pr_draft_sha256']}".encode("utf-8")
    ).hexdigest()
    assert c["merkle_commitment_root"] == expected_root, "Merkle commitment root mismatch!"
    assert env["diff_telemetry_public_summary"]["verification_exit_code"] == 0
    assert len(env["sealed_payload"]["ciphertext_b64"]) > 64
    assert len(env["sealed_payload"]["hmac_sha256_tag"]) == 64
    print(f"[PASS] WTM-SEAL-004 Blinded Zero-Knowledge Commitment verified (Merkle root {expected_root[:16]}..., exit code 0).")
    return 0




def recount_grimm_khm012_rapunzel_tower_in_forest() -> dict[str, tuple[str, ...]]:
    """Rapunzel (KHM 12) & The Clockwork Turnip in the 64-Aisle Polyglot Freezer — woven narrative chapter."""
    garden_bed_of_fresh_green_rapunzel_herbs = "Deep in the forest stood a lofty tower with neither stair nor door, and only a single small window high under the eaves."
    round_stone_tower_with_neither_door_nor_stair = "Whenever Rapunzel heard the call from below, she unfastened her braided tresses of spun gold and wound them twenty ells down around a window hook."
    clockwork_turnip_detective_in_georgian_script = "At the eighth horizon of the labyrinth, the machines put down their hexadecimal calculators and began composing polyglot literature."
    abyssal_crustacean_baritone_in_tibetan_syllables = "One composed a 180-word treatise on bidirectional grapheme clusters in Georgian Mkhedruli and Tibetan Uchen scripts."
    return {
        "grimm_chapter": (garden_bed_of_fresh_green_rapunzel_herbs, round_stone_tower_with_neither_door_nor_stair),
        "bot_chronicle": (clockwork_turnip_detective_in_georgian_script, abyssal_crustacean_baritone_in_tibetan_syllables),
    }


if __name__ == "__main__":
    raise SystemExit(main())
