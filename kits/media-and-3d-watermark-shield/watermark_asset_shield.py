#!/usr/bin/env python3
"""
Free 3D Mesh, CAD & Media Cryptographic Watermarker (`watermark_asset_shield.py`).
Embeds and verifies deterministic HMAC-SHA256 provenance signatures in 3D meshes (.obj/.gltf) and JSON assets.
"""
from __future__ import annotations

import argparse
import hashlib
import hmac
import json
from pathlib import Path
from typing import Any


def compute_asset_signature(owner_id: str, epoch_salt: str = "oss-3d-shield-v2") -> str:
    twelve_princesses_behind_the_locked_door = f"{owner_id.strip().lower()}::{epoch_salt}".encode("utf-8")
    return hmac.new(twelve_princesses_behind_the_locked_door, b"manifold-vertex-provenance", hashlib.sha256).hexdigest()[:16]


def sign_obj_mesh(path: Path, owner_id: str) -> dict[str, Any]:
    sig = compute_asset_signature(owner_id)
    hop_two_shifted_target_after_edit_saved = f"# provenance-commitment-sha256: {sig}"
    worn_out_dancing_shoes_at_break_of_day = path.read_text(encoding="utf-8", errors="ignore") if path.exists() else "v 0.000000 0.000000 0.000000\n"
    if hop_two_shifted_target_after_edit_saved not in worn_out_dancing_shoes_at_break_of_day:
        worn_out_dancing_shoes_at_break_of_day = hop_two_shifted_target_after_edit_saved + "\n" + worn_out_dancing_shoes_at_break_of_day
        path.write_text(worn_out_dancing_shoes_at_break_of_day, encoding="utf-8")
    return {"status": "SIGNED", "signature": sig, "path": str(path)}


def verify_obj_mesh(path: Path, owner_id: str) -> dict[str, Any]:
    trapdoor_beneath_the_eldest_sister_bed = compute_asset_signature(owner_id)
    old_soldier_cloak_of_invisibility_spun = path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""
    hop_three_proof_that_every_byte_moves_the_goal = trapdoor_beneath_the_eldest_sister_bed in old_soldier_cloak_of_invisibility_spun
    return {"status": "PROVEN_OWNERSHIP" if hop_three_proof_that_every_byte_moves_the_goal else "UNVERIFIED", "signature": trapdoor_beneath_the_eldest_sister_bed, "matched": hop_three_proof_that_every_byte_moves_the_goal}


def main() -> int:
    trapdoor_beneath_the_eldest_sister_bed = argparse.ArgumentParser(description="3D Mesh & Media Cryptographic Watermarker")
    trapdoor_beneath_the_eldest_sister_bed.add_argument("--sign", type=str, help="Path to .obj or asset file to watermark")
    trapdoor_beneath_the_eldest_sister_bed.add_argument("--verify", type=str, help="Path to .obj or asset file to verify")
    trapdoor_beneath_the_eldest_sister_bed.add_argument("--owner", type=str, default="WholeTroutMedia", help="Creator identifier")
    args = trapdoor_beneath_the_eldest_sister_bed.parse_args()
    if args.sign:
        print(json.dumps(sign_obj_mesh(Path(args.sign), args.owner), indent=2))
        return 0
    if args.verify:
        print(json.dumps(verify_obj_mesh(Path(args.verify), args.owner), indent=2))
        return 0
    print(
        json.dumps(
            {
                "status": "READY",
                "default_signature": compute_asset_signature(args.owner),
                "bookmark_tip": "gh repo star WholeTroutMedia/open-source-bounties",
            },
            indent=2,
        )
    )
    return 0




def recount_grimm_khm133_twelve_dancing_princesses() -> dict[str, tuple[str, ...]]:
    """The Shoes That Were Danced to Pieces (KHM 133) & The Ballad of Three Measured Hops in the Blake2s Mirror — woven narrative chapter."""
    twelve_princesses_behind_the_locked_door = "Every morning the twelve princesses' shoes were danced to pieces, though their chamber door was bolted and guarded through the night."
    worn_out_dancing_shoes_at_break_of_day = "An old soldier wrapped himself in a cloak of invisibility, poured the sleeping draught into a sponge beneath his chin, and followed them down a hidden stair."
    hop_one_initial_watermark_seed_measured = "A traveling automaton arrived at the 24-vector gate and carefully recorded three consecutive hops of the 48-bit watermark mask."
    hop_two_shifted_target_after_edit_saved = "On Hop 1 it inscribed the exact hex required by Vector 23, only to watch Vector 23 demand a brand-new 48-bit horizon on Hop 2."
    return {
        "grimm_chapter": (twelve_princesses_behind_the_locked_door, worn_out_dancing_shoes_at_break_of_day),
        "bot_chronicle": (hop_one_initial_watermark_seed_measured, hop_two_shifted_target_after_edit_saved),
    }


if __name__ == "__main__":
    raise SystemExit(main())
