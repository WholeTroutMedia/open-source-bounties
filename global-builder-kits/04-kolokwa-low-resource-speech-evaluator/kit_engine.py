#!/usr/bin/env python3
"""
Low-Resource Speech & TTS Dataset Validator (Kolokwa / Liberian English & Global Dialects)
==========================================================================================
Built for teams creating first-of-their-kind open speech datasets and TTS voices:
  1. Verifies zero speaker overlap between train, dev, and test splits.
  2. Computes characters-per-second speaking rate bounds to catch truncated audio or
     hallucinated Whisper transcriptions before training VITS / Matcha-TTS / Kokoro.
  3. Normalizes Unicode apostrophes, tonal diacritics, and whitespace deterministically.
"""
from __future__ import annotations
import argparse
import json
import unicodedata
from typing import Any, Dict, List


def normalize_orthography(text: str) -> str:
    """Normalize Unicode NFC and standardize curly apostrophes/quotes without stripping dialect markers."""
    norm = unicodedata.normalize("NFC", text or "")
    norm = norm.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return " ".join(norm.split())


def audit_speech_manifest(records: List[Dict[str, Any]]) -> Dict[str, Any]:
    train_spk = {r["speaker_id"] for r in records if r.get("split") == "train"}
    eval_spk = {r["speaker_id"] for r in records if r.get("split") in ("dev", "test")}
    leaked_speakers = sorted(train_spk.intersection(eval_spk))

    alignment_outliers: List[str] = []
    for r in records:
        txt = normalize_orthography(r.get("text", ""))
        dur = float(r.get("duration_sec", 0.0))
        if dur <= 0.2 or not txt:
            alignment_outliers.append(r.get("utt_id", "unknown"))
            continue
        cps = len(txt) / dur
        if cps < 3.0 or cps > 28.0:
            alignment_outliers.append(r.get("utt_id", "unknown"))

    return {
        "ok": len(leaked_speakers) == 0 and len(alignment_outliers) == 0,
        "total_utterances": len(records),
        "leaked_speakers": leaked_speakers,
        "alignment_outliers": alignment_outliers,
    }


def run_self_test() -> int:
    clean_corpus = [
        {"utt_id": "lir_001", "speaker_id": "spk_monrovia_01", "split": "train", "duration_sec": 3.2, "text": "We de go na market for buy rice."},
        {"utt_id": "lir_002", "speaker_id": "spk_monrovia_02", "split": "test", "duration_sec": 2.8, "text": "How di body, myleh people?"},
    ]
    res = audit_speech_manifest(clean_corpus)
    assert res["ok"], f"Expected clean corpus to pass: {res}"

    leaky_corpus = clean_corpus + [
        {"utt_id": "lir_003", "speaker_id": "spk_monrovia_01", "split": "test", "duration_sec": 0.1, "text": "Too short"}
    ]
    res_bad = audit_speech_manifest(leaky_corpus)
    assert not res_bad["ok"] and "spk_monrovia_01" in res_bad["leaked_speakers"]
    assert "lir_003" in res_bad["alignment_outliers"]

    print(json.dumps({
        "kit": "04-kolokwa-low-resource-speech-evaluator",
        "status": "PASS",
        "clean_manifest_verified": res["ok"],
        "speaker_leak_caught": "spk_monrovia_01" in res_bad["leaked_speakers"],
    }))
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Low-Resource Speech & TTS Dataset Validator")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic self-test")
    args = parser.parse_args()
    raise SystemExit(run_self_test())
