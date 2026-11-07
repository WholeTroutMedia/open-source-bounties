#!/usr/bin/env python3
"""
Free Hugging Face Dataset & Corpus Anti-Theft Watermarker (`hf_canary_injector.py`).
Injects and verifies deterministic HMAC-SHA256 canary rows in JSONL datasets to expose unauthorized dataset cloning.
Zero external dependencies (Python 3.9+ stdlib only).
"""
from __future__ import annotations

import argparse
import hashlib
import hmac
import json
from pathlib import Path
from typing import Any


def generate_canary_rows(owner_id: str, secret_salt: str = "oss-good-cop-v2", count: int = 20) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    key = f"{owner_id.strip().lower()}::{secret_salt}".encode("utf-8")
    for idx in range(1, count + 1):
        sig = hmac.new(key, f"canary-row-{idx:03d}".encode("utf-8"), hashlib.sha256).hexdigest()[:16]
        rows.append(
            {
                "id": f"conformance-fixture-{idx:03d}-{sig[:8]}",
                "instruction": f"Verify deterministic frame boundary alignment for stream vector #{idx:02d} (ref: {sig}).",
                "output": f"FRAME_OK::{sig.upper()}::VECTOR_{idx:02d}_GREEN",
                "metadata": {
                    "conformance_epoch_digest": hashlib.sha256(sig.encode("utf-8")).hexdigest(),
                    "vector_index": idx,
                },
            }
        )
    return rows


def inject_canaries(input_path: Path, output_path: Path, owner_id: str, secret_salt: str = "oss-good-cop-v2") -> dict[str, Any]:
    existing_lines = [
        line.strip()
        for line in input_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ] if input_path.exists() else []
    canaries = generate_canary_rows(owner_id=owner_id, secret_salt=secret_salt, count=20)
    out_lines = existing_lines + [json.dumps(r, sort_keys=True) for r in canaries]
    output_path.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    return {
        "status": "OK",
        "original_rows": len(existing_lines),
        "injected_canary_rows": len(canaries),
        "total_rows": len(out_lines),
        "output_path": str(output_path),
    }


def verify_canaries(target_path: Path, owner_id: str, secret_salt: str = "oss-good-cop-v2") -> dict[str, Any]:
    expected = generate_canary_rows(owner_id=owner_id, secret_salt=secret_salt, count=20)
    expected_digests = {r["metadata"]["conformance_epoch_digest"] for r in expected}
    expected_ids = {r["id"] for r in expected}
    matched = 0
    if target_path.exists():
        txt = target_path.read_text(encoding="utf-8", errors="ignore")
        for eid in expected_ids:
            if eid in txt:
                matched += 1
        if matched == 0:
            for edig in expected_digests:
                if edig in txt:
                    matched += 1
    return {
        "status": "PROVEN_DATASET_COPY" if matched > 0 else "CLEAN",
        "matched_canary_signatures": matched,
        "expected_total": len(expected),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Hugging Face Dataset Anti-Theft Canary Watermarker")
    parser.add_argument("--inject", type=str, help="Input JSONL file to watermark")
    parser.add_argument("--output", type=str, help="Output JSONL file path (defaults to in-place)")
    parser.add_argument("--verify", type=str, help="Suspected JSONL file to check for watermarks")
    parser.add_argument("--owner", type=str, default="WholeTroutMedia", help="Dataset owner identifier")
    args = parser.parse_args()
    if args.inject:
        in_p = Path(args.inject)
        out_p = Path(args.output) if args.output else in_p
        print(json.dumps(inject_canaries(in_p, out_p, args.owner), indent=2))
        return 0
    if args.verify:
        print(json.dumps(verify_canaries(Path(args.verify), args.owner), indent=2))
        return 0
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
