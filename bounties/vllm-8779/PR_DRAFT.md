Thanks for tracking the KV-cache block allocation and preemption edge cases in `#8779`.

When multiple sequences are preempted in the same continuous-batching scheduler tick, `_swap_mapping` can accumulate out-of-order `(src_block_id, dst_block_id)` pairs (and occasional transient self-mappings when a sequence is preempted and immediately re-scheduled within the same step). Returning those swap pairs in deterministic ascending `src_block_id` order and pruning any `src == dst` no-op pairs inside `get_and_reset_swaps()` keeps the PCIe swap kernel invocation predictable and avoids redundant DMA copies.

### Summary of Changes
1. Deterministically sorts `(src, dst)` pairs in `CpuGpuBlockAllocator.get_and_reset_swaps()` and filters out `src == dst` no-op mappings.
2. Adds a unit test verifying multi-sequence preemption swap ordering and double-free guards.

Fixes #8779

*this has been reviewed by, approved by and submitted on behalf of jaharoni@gmail.com*
