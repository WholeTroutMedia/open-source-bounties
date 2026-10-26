# Competing-PR & Community Etiquette Audit: `vllm-8779`

- **Upstream Target**: [`vllm-project/vllm#8779`](https://github.com/vllm-project/vllm/issues/8779)
- **Audit Classification**: **`SKIP_CLAIMED`**
- **Audit Summary**: Issue already closed or has a merged PR
- **Open Competing PRs**: `0`
- **Active Assignees**: `0`
- **WholeTroutMedia Fork**: [`WholeTroutMedia/vllm`](https://github.com/WholeTroutMedia/vllm)
- **Audited At**: `2026-10-26T13:42:48.036620+00:00`

## Prior Unmerged / Closed PR Attempts
- PR `#8452` (`CLOSED`, `merged=False`) by `@noooop`: [PoC]: Support encode only models by Workflow Defined Engine
- PR `#8964` (`CLOSED`, `merged=False`) by `@noooop`: [Core]: (Last/N) Support prefill only models by Workflow Defined Engine
- PR `#6869` (`CLOSED`, `merged=False`) by `@Nan2018`: [Core] generate from input embeds

## Recent Maintainer & Contributor Comment Digest
- @Stonesjtu: > Drop beam search from vLLM engine > Provide a solution to emulate beam search outside vLLM engine @simon-mo v1 seems a huge performance bumps in terms of sampling and multi-modal
- @kuangdao: mark
- @renjie0: "Implement parallel sampling via prefix caching " What does it mean?
- @github-actions: This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. 
- @jayxsinha: I see Qwen3 Rerankers are [now supported on vllm](https://docs.vllm.ai/en/latest/models/supported_models.html#sentence-pair-scoring). Is there a way to modify the instruction used 
- @DarkLight1337: This is currently not handled inside vLLM, so you have to apply the template from client side.
