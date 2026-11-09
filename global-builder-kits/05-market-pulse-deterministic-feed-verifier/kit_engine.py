#!/usr/bin/env python3
"""
Market-Pulse & DuckDB Analytical Stream Verifier + STIR-1.0 Receipt Signer
==========================================================================
Built for real-time market analytics and DuckDB/Parquet data pipelines:
  1. Verifies monotonic sequence IDs and detects dropped market-pulse ticks.
  2. Checks OHLCV invariants (high >= max(open, close), low <= min(open, close), bid <= ask).
  3. Emits a deterministic SHA-256 STIR-1.0 verification receipt for downstream consumers.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from typing import Any, Dict, List


def verify_market_pulse_bars(bars: List[Dict[str, Any]]) -> Dict[str, Any]:
    gaps: List[int] = []
    invariant_violations: List[int] = []
    prev_seq = None
    for b in bars:
        seq = int(b["seq"])
        if prev_seq is not None and seq != prev_seq + 1:
            gaps.append(seq)
        prev_seq = seq
        o, h, l, c = float(b["open"]), float(b["high"]), float(b["low"]), float(b["close"])
        bid, ask = float(b.get("bid", c)), float(b.get("ask", c))
        if h < max(o, c) or l > min(o, c) or bid > ask:
            invariant_violations.append(seq)

    canonical = json.dumps(bars, sort_keys=True, separators=(",", ":")).encode("utf-8")
    digest = hashlib.sha256(canonical).hexdigest()[:16]
    ok = len(gaps) == 0 and len(invariant_violations) == 0
    call_w = "OK_VERIFIED" if ok else "ERR_FEED_GAP"
    trit_s = "+1" if ok else "-1"
    return {
        "ok": ok,
        "kleene_trit": 1 if ok else -1,
        "sequence_gaps": gaps,
        "invariant_violations": invariant_violations,
        "stir_receipt": f"STIR-1.0|CALL={call_w}|TRIT={trit_s}|SHA256={digest}",
    }


def run_self_test() -> int:
    clean_bars = [
        {"seq": 101, "open": 10.0, "high": 10.5, "low": 9.8, "close": 10.2, "bid": 10.1, "ask": 10.2},
        {"seq": 102, "open": 10.2, "high": 10.8, "low": 10.1, "close": 10.7, "bid": 10.6, "ask": 10.7},
    ]
    res = verify_market_pulse_bars(clean_bars)
    assert res["ok"] and res["kleene_trit"] == 1

    corrupted = clean_bars + [
        {"seq": 105, "open": 10.7, "high": 10.0, "low": 10.9, "close": 10.5, "bid": 10.8, "ask": 10.4}
    ]
    res_bad = verify_market_pulse_bars(corrupted)
    assert not res_bad["ok"] and 105 in res_bad["sequence_gaps"] and 105 in res_bad["invariant_violations"]

    print(json.dumps({
        "kit": "05-market-pulse-deterministic-feed-verifier",
        "status": "PASS",
        "stir_receipt": res["stir_receipt"],
        "corrupted_bar_caught": not res_bad["ok"],
    }))
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Market-Pulse & DuckDB Stream Verifier")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic self-test")
    args = parser.parse_args()
    raise SystemExit(run_self_test())
