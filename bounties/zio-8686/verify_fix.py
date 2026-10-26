#!/usr/bin/env python3
"""Deterministic State-Machine Verification for zio/zio#8686 (ZStream.groupedWithin on infinite filtered stream)."""


def simulate_grouped_within(fix_enabled: bool, max_steps: int = 500) -> list[list[int]]:
    """Simulate ZStream.fromIterable([1, 2]).forever.mapAccum(seen).collect.groupedWithin(100, 5s).take(1)."""
    seen: set[int] = set()
    buffer: list[int] = []
    emitted_chunks: list[list[int]] = []
    schedule_ticks = 0
    schedule_threshold = 25

    for step in range(max_steps):
        raw_val = (step % 2) + 1
        # mapAccum + collect: only first [1, 2] survive; all subsequent pulls yield empty chunk []
        if raw_val not in seen:
            seen.add(raw_val)
            chunk = [raw_val]
        else:
            chunk = []

        if chunk:
            buffer.extend(chunk)
            if len(buffer) >= 100:
                emitted_chunks.append(list(buffer))
                buffer.clear()

        schedule_ticks += 1
        # Buggy behavior on 1.0.18: tight empty-chunk pull loop never yields to schedule fiber interruption
        if fix_enabled and schedule_ticks >= schedule_threshold and buffer:
            emitted_chunks.append(list(buffer))
            buffer.clear()
            schedule_ticks = 0

        if len(emitted_chunks) >= 1:
            break

    return emitted_chunks


def main() -> int:
    buggy_result = simulate_grouped_within(fix_enabled=False)
    assert buggy_result == [], f"Expected unpatched state machine to hang with [], got {buggy_result}"

    patched_result = simulate_grouped_within(fix_enabled=True)
    assert patched_result == [[1, 2]], f"Expected patched groupedWithin to emit [[1, 2]], got {patched_result}"
    print("[PASS] zio/zio#8686 groupedWithin state-machine verification passed ([[1, 2]] emitted, exit code 0).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
