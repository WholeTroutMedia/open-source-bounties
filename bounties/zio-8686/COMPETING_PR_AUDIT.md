# Competing-PR & Community Etiquette Audit: `zio-8686`

- **Upstream Target**: [`zio/zio#8686`](https://github.com/zio/zio/issues/8686)
- **Audit Classification**: **`EXTEND_STALLED`**
- **Audit Summary**: Issue remains OPEN with 0 open PRs; 3 historical PR ref(s) by @DenisKusakin (#8873), @DenisKusakin (#9113), @argofowl (#10917) - safe to build on and credit prior findings
- **Open Competing PRs**: `0`
- **Active Assignees**: `0`
- **WholeTroutMedia Fork**: [`WholeTroutMedia/zio`](https://github.com/WholeTroutMedia/zio)
- **Private Solution Vault**: [`WholeTroutMedia/bounty-solves-vault`](https://github.com/WholeTroutMedia/bounty-solves-vault) (`private: True` - Original Repo Owner & `@jaharoni` Only)
- **Audited At**: `2026-10-26T17:02:04.337493+00:00`

## Prior Unmerged / Closed PR Attempts
- PR `#8873` (`CLOSED`, `merged=False`) by `@DenisKusakin`: [WIP] ZStream.groupedWithin works in unexpected way for infinite stream #8686
- PR `#9113` (`CLOSED`, `merged=False`) by `@DenisKusakin`: [WIP] ZStream.groupedWithin works in unexpected way for infinite stream #8686
- PR `#10917` (`CLOSED`, `merged=False`) by `@argofowl`: fix(streams): flush groupedWithin after schedule fires

## Recent Maintainer & Contributor Comment Digest
- @algora-pbc: 💡 @DenisKusakin submitted a [pull request](https://github.com/zio/zio/pull/9113) that claims the bounty. You can [visit your bounty board](https://console.algora.io/org/ZIO/bountie
- @chengyixu: /attempt
- @SAVAMforWIN: /attempt #8686 Plan: reproduce the groupedWithin behavior on the still-open issue state, determine whether the remaining bug is in concat/groupedWithin semantics for infinite strea
- @Iineman2: /attempt #8686 Plan: reproduce the groupedWithin infinite-stream timeout behavior against current series/2.x first, then submit only a focused regression fix if the behavior still 
- @argofowl: /attempt #8686 Plan: submit the already-tested series/1.x regression fix for groupedWithin on infinite streams. The patch adds a focused test that times out on baseline and updates
- @Iineman2: Update after reproducing locally: on current series/2.x I can add the #8686 live-clock regression and it passes without any production-code change. Focused run: streamsTestsJVM/tes
