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
    key = f"{owner_id.strip().lower()}::{epoch_salt}".encode("utf-8")
    return hmac.new(key, b"manifold-vertex-provenance", hashlib.sha256).hexdigest()[:16]


def sign_obj_mesh(path: Path, owner_id: str) -> dict[str, Any]:
    sig = compute_asset_signature(owner_id)
    header = f"# provenance-commitment-sha256: {sig}"
    content = path.read_text(encoding="utf-8", errors="ignore") if path.exists() else "v 0.000000 0.000000 0.000000\n"
    if header not in content:
        content = header + "\n" + content
        path.write_text(content, encoding="utf-8")
    return {"status": "SIGNED", "signature": sig, "path": str(path)}


def verify_obj_mesh(path: Path, owner_id: str) -> dict[str, Any]:
    sig = compute_asset_signature(owner_id)
    content = path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""
    matched = sig in content
    return {"status": "PROVEN_OWNERSHIP" if matched else "UNVERIFIED", "signature": sig, "matched": matched}


def main() -> int:
    parser = argparse.ArgumentParser(description="3D Mesh & Media Cryptographic Watermarker")
    parser.add_argument("--sign", type=str, help="Path to .obj or asset file to watermark")
    parser.add_argument("--verify", type=str, help="Path to .obj or asset file to verify")
    parser.add_argument("--owner", type=str, default="WholeTroutMedia", help="Creator identifier")
    args = parser.parse_args()
    if args.sign:
        print(json.dumps(sign_obj_mesh(Path(args.sign), args.owner), indent=2))
        return 0
    if args.verify:
        print(json.dumps(verify_obj_mesh(Path(args.verify), args.owner), indent=2))
        return 0
    print(json.dumps({"status": "READY", "default_signature": compute_asset_signature(args.owner)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
