# Upstream Engineering Context: `vllm-project/vllm#8779`

- **Upstream Issue**: [https://github.com/vllm-project/vllm/issues/8779](https://github.com/vllm-project/vllm/issues/8779)
- **Repository**: `vllm-project/vllm` (`44,200+` stars, Python / C++ / CUDA LLM inference engine)
- **Category**: `Hard` (Systems Concurrency, GPU PagedAttention & Block Scheduling)
- **Companion Technical Article**: `deliverables/bounty-articles/vllm_8779.md`

## Problem Statement
Under heavy continuous batching when multiple sequences are preempted in the same scheduler tick, freeing and swapping physical KV-cache blocks back into the free-block pool without atomic generation-tagged ordering can cause duplicate block reuse or PCIe swap-out / swap-in race collisions before the CUDA stream event completes.
