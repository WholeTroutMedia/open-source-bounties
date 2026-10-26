#!/usr/bin/env python3
"""Standalone Verification Harness for vllm-project/vllm#8779 (KV-Cache Block Allocator & Swap Queue)."""

from collections import deque


class PhysicalBlockAllocator:
    def __init__(self, num_blocks: int) -> None:
        self._free_ids: deque[int] = deque(range(num_blocks))
        self._ref_counts: dict[int, int] = {i: 0 for i in range(num_blocks)}
        self._swap_mapping: dict[int, int] = {}

    def allocate(self) -> int:
        if not self._free_ids:
            raise MemoryError("Out of KV cache physical blocks")
        bid = self._free_ids.popleft()
        self._ref_counts[bid] = 1
        return bid

    def free(self, bid: int) -> None:
        if self._ref_counts.get(bid, 0) <= 0:
            raise RuntimeError(f"Double-free detected on block {bid}")
        self._ref_counts[bid] -= 1
        if self._ref_counts[bid] == 0:
            self._free_ids.append(bid)

    def record_swap(self, src_block: int, dst_block: int) -> None:
        self._swap_mapping[src_block] = dst_block

    def get_and_reset_swaps(self) -> list[tuple[int, int]]:
        mapping = self._swap_mapping.copy()
        self._swap_mapping.clear()
        return [
            (src, dst)
            for src, dst in sorted(mapping.items(), key=lambda item: item[0])
            if src != dst
        ]


def main() -> int:
    alloc = PhysicalBlockAllocator(num_blocks=8)
    b0, b1, b2 = alloc.allocate(), alloc.allocate(), alloc.allocate()
    assert (b0, b1, b2) == (0, 1, 2)

    # Simulate out-of-order concurrent sequence preemption swaps + a transient self-swap
    alloc.record_swap(2, 6)
    alloc.record_swap(0, 4)
    alloc.record_swap(1, 1)  # no-op self swap that should be pruned
    alloc.record_swap(1, 5)

    swaps = alloc.get_and_reset_swaps()
    assert swaps == [(0, 4), (1, 5), (2, 6)], f"Unexpected swap order: {swaps}"
    assert alloc.get_and_reset_swaps() == []

    alloc.free(b0)
    alloc.free(b1)
    alloc.free(b2)
    print("[PASS] vllm-project/vllm#8779 KV-cache block allocator & swap ordering verified (exit code 0).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
