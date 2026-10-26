# WholeTroutMedia Open-Source Bounties & Engineering Foundry

Welcome to the public open-source engineering and bounty workspace for **WholeTroutMedia** ([`https://github.com/WholeTroutMedia`](https://github.com/WholeTroutMedia)) and **Inception Engine Systems** ([`https://inceptionengine.systems`](https://inceptionengine.systems)), led and reviewed by **Justin Aharoni** ([@jaharoni](https://github.com/jaharoni) · `justin.aharoni@inceptionengine.systems` / `jaharoni@gmail.com`).

We use this repository to keep track of unclaimed open-source bounties and community bug fixes, audit existing pull requests so we never duplicate another contributor's work, trace and avoid automated bot-slop traps via our **[7-Beacon Counter-Bot Radar (`BOT_RADAR_AND_SIGNAL_PROOF.md`)](./BOT_RADAR_AND_SIGNAL_PROOF.md)**, fork target repositories cleanly into the **`WholeTroutMedia`** organization, verify every fix with a deterministic test suite (`PROOF_OF_EXECUTION.md`), and review every Pull Request draft before submitting upstream.

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

4. **Human Review Gate + Maintainer Fast-Track (Pull Immediately Without Waiting)**:
   - Every staged fix opens a tracking review issue in [Issues](https://github.com/WholeTroutMedia/open-source-bounties/issues) and emails a review copy to `justin.aharoni@inceptionengine.systems`.
   - **Maintainer Fast-Track**: If you are an upstream maintainer or contributor on an issue we have solved and you do not want to wait for our scheduled human review, every dossier and Review Issue includes:
     1. **1-Click GitHub Compare & Pull Link**: Open and merge our verified `WholeTroutMedia/<repo>` branch directly into your repository on the spot.
     2. **1-Click Fast-Track Email Request**: Send a pre-filled email to `justin.aharoni@inceptionengine.systems` (`-> jaharoni@gmail.com`) asking us to submit or prioritize the Pull Request immediately.
     3. **2-Line `git fetch && git cherry-pick` Command**: Pull the verified commit locally in seconds.

---

## Active Bounty & Contribution Ledger

| Bounty ID | Upstream Issue | Tier | Platform / Funding | Competing-PR Audit | WholeTroutMedia Fork | Review Gate | Status |
| :--- | :--- | :---: | :--- | :---: | :--- | :--- | :--- |
| [`starlette-843`](./bounties/starlette-843/) | [`Kludex/starlette#843`](https://github.com/Kludex/starlette/issues/843) | `Easy` | Polar.sh / OSS Funded | `SKIP_CLAIMED` | [`WholeTroutMedia/starlette`](https://github.com/WholeTroutMedia/starlette) | [Review #1](https://github.com/WholeTroutMedia/open-source-bounties/issues/1) | **SEALED_IN_PRIVATE_VAULT** |
| [`zio-8686`](./bounties/zio-8686/) | [`zio/zio#8686`](https://github.com/zio/zio/issues/8686) | `Medium` | Algora Bounty ($ZIO Board) | `EXTEND_STALLED` | [`WholeTroutMedia/zio`](https://github.com/WholeTroutMedia/zio) | [Review #2](https://github.com/WholeTroutMedia/open-source-bounties/issues/2) | **SEALED_IN_PRIVATE_VAULT** |
| [`starlette-649`](./bounties/starlette-649/) | [`Kludex/starlette#649`](https://github.com/Kludex/starlette/issues/649) | `Hard` | Polar.sh / OSS Funded | `EXTEND_STALLED` | [`WholeTroutMedia/starlette`](https://github.com/WholeTroutMedia/starlette) | [Review #3](https://github.com/WholeTroutMedia/open-source-bounties/issues/3) | **SEALED_IN_PRIVATE_VAULT** |

---

## Have an Issue or Repository You Want Solved?

If you maintain an open-source project and have a bug or bounty you would like our system to solve, verify (`Exit Code 0`), and stage for review:
- **[Request a Verified Fix (`justin.aharoni@inceptionengine.systems`)](mailto:justin.aharoni@inceptionengine.systems?cc=jaharoni@gmail.com&subject=%5BISSUE%20SOLVE%20REQUEST%5D%20Repository%20%2F%20Issue%20Submission&body=Hi%20Justin%2C%0A%0AWe%20would%20like%20WholeTroutMedia%20to%20look%20at%20and%20verify%20a%20fix%20for%3A%0A-%20Repository%3A%20%0A-%20Issue%20Link%3A%20%0A-%20Notes%3A%20%0A%0AThank%20you!)**

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
│   └── starlette-649/           # [Hard] Kludex/starlette#649 (Polar.sh, 0 Open PRs)
└── .github/
    ├── ISSUE_TEMPLATE/
    │   └── bounty_review.md     # Staged review issue template
    └── workflows/
        └── verify-bounties.yml  # CI runner executing all bounties/*/verify_fix.py
```

*this has been reviewed by, approved by and submitted on behalf of jaharoni@gmail.com*
