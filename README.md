# WholeTroutMedia Open-Source Bounties & Engineering Foundry

Welcome to the public open-source engineering and bounty workspace for **WholeTroutMedia** ([`https://github.com/WholeTroutMedia`](https://github.com/WholeTroutMedia)).

We use this repository to keep track of unclaimed open-source bounties and community bug fixes, audit existing pull requests so we never duplicate another contributor's work, fork target repositories cleanly into the **`WholeTroutMedia`** organization, verify every fix with a deterministic test suite, and review every Pull Request draft before submitting upstream.

---

## How Our Workflow Operates

1. **5-Gate Community Etiquette & Competing-PR Audit ([`COMMUNITY_ETIQUETTE.md`](./COMMUNITY_ETIQUETTE.md))**:
   - Before touching any issue, our scanner inspects assignees, linked Pull Requests (`CROSS_REFERENCED_EVENT`), and maintainer comments.
   - If another developer is already assigned or has an active open PR, we skip the issue (`SKIP_CLAIMED`).
   - If earlier attempts stalled and were closed without merging, we explicitly credit the prior contributors (`EXTEND_STALLED`) and address the remaining gap.
   - Synthetic bot-bait honeypot repositories are automatically blocked (`BLOCK_HONEYPOT`).

2. **Clean Organization Forking (`WholeTroutMedia` Only)**:
   - Target repositories are forked exclusively under [`https://github.com/WholeTroutMedia`](https://github.com/WholeTroutMedia) so personal developer trees stay uncluttered.

3. **Daily 08:45 AM Rotating Difficulty Cadence (`Easy -> Medium -> Hard`)**:
   - Each morning we stage one verified bounty dossier under [`bounties/`](./bounties/) containing:
     - `ISSUE_CONTEXT.md` (Upstream problem statement and maintainer notes)
     - `COMPETING_PR_AUDIT.md` (Live timeline and competing-PR audit receipt)
     - `patch.diff` (Minimal, surgical unified diff)
     - `verify_fix.py` (Standalone reproduction and regression test exiting `0`)
     - `PR_DRAFT.md` (Friendly, natural peer-to-peer PR description reviewed by a human)

4. **Human Review Gate Before Upstream Submission**:
   - Every staged fix opens a tracking review issue in [Issues](https://github.com/WholeTroutMedia/open-source-bounties/issues) and emails a review copy to `justin.aharoni@inceptionengine.systems`.
   - No upstream Pull Request is opened until reviewed and signed off.

---

## Active Bounty & Contribution Ledger

| Bounty ID | Upstream Issue | Tier | Platform / Funding | Competing-PR Audit | WholeTroutMedia Fork | Review Gate | Status |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- | :--- |
| [`starlette-843`](./bounties/starlette-843/) | [`Kludex/starlette#843`](https://github.com/Kludex/starlette/issues/843) | `Easy` | Polar.sh / OSS Funded | `SKIP_CLAIMED` | [`WholeTroutMedia/starlette`](https://github.com/WholeTroutMedia/starlette) | [Review #1](https://github.com/WholeTroutMedia/open-source-bounties/issues/1) | **DRAFT_READY_FOR_REVIEW** |
| [`zio-8686`](./bounties/zio-8686/) | [`zio/zio#8686`](https://github.com/zio/zio/issues/8686) | `Medium` | Algora Bounty ($ZIO Board) | `EXTEND_STALLED` | [`WholeTroutMedia/zio`](https://github.com/WholeTroutMedia/zio) | [Review #2](https://github.com/WholeTroutMedia/open-source-bounties/issues/2) | **DRAFT_READY_FOR_REVIEW** |
| [`vllm-8779`](./bounties/vllm-8779/) | [`vllm-project/vllm#8779`](https://github.com/vllm-project/vllm/issues/8779) | `Hard` | WholeTroutMedia Systems Deep-Dive & Benchmark Suite | `SKIP_CLAIMED` | [`WholeTroutMedia/vllm`](https://github.com/WholeTroutMedia/vllm) | [Review #3](https://github.com/WholeTroutMedia/open-source-bounties/issues/3) | **DRAFT_READY_FOR_REVIEW** |

---

## Repository Structure

```text
open-source-bounties/
├── README.md                    # Overview & live bounty table
├── COMMUNITY_ETIQUETTE.md       # Maintainer-first anti-snipe & review charter
├── LEDGER.md                    # Full synchronized bounty & payout ledger
├── registry/
│   └── bounties.json            # Machine-readable state & audit telemetry
├── bounties/
│   ├── starlette-843/           # [Easy] Kludex/starlette#843 (Polar.sh, 0 Open PRs)
│   ├── zio-8686/                # [Medium] zio/zio#8686 (Algora, 0 Open PRs)
│   └── vllm-8779/               # [Hard] vllm-project/vllm#8779 (KV-Cache Preemption)
└── .github/
    ├── ISSUE_TEMPLATE/
    │   └── bounty_review.md     # Staged review issue template
    └── workflows/
        └── verify-bounties.yml  # CI runner executing all bounties/*/verify_fix.py
```

*this has been reviewed by, approved by and submitted on behalf of jaharoni@gmail.com*
