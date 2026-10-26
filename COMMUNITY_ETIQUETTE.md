# WholeTroutMedia Open-Source Contribution & Bounty Etiquette Charter

This repository (`WholeTroutMedia/open-source-bounties`) is our public engineering workspace for discovering, auditing, solving, and verifying open-source bug fixes and funded community bounties before we ever open a Pull Request on an upstream repository.

Open-source maintainers spend enormous energy triaging issues and reviewing code. Our goal is to make every contribution from **WholeTroutMedia** a genuine relief to review: surgical, well-tested, respectful of existing contributors, and reviewed by a human before submission.

---

## 1. Competing-PR & Prior-Work Audit (`CLAIM_OPEN` / `EXTEND_STALLED` / `SKIP_CLAIMED`)

Before writing a single line of code or commenting `/claim` on any issue, our workflow inspects the full upstream issue timeline, assignees, and linked Pull Requests:

1. **`SKIP_CLAIMED` (Do Not Snipe)**:
   - If a maintainer has already assigned the issue to another developer, we skip it.
   - If another contributor already has an active, open Pull Request that addresses the issue, we skip it completely. We never submit duplicate competing PRs just to race someone who is already doing the work.
   - If a repository is a synthetic bot-bait benchmark (`AI only allowed`, `Autonomus Agents Only`, or fake bounty aggregators), our honeypot filter automatically blocks it.

2. **`EXTEND_STALLED` (Unify & Credit Prior Attempts)**:
   - When an issue has prior comments with partial debugging notes or an older Pull Request that was closed/abandoned months ago without merging, we explicitly credit the earlier contributors (`@handle`) in our notes and build cleanly on what they uncovered.

3. **`CLAIM_OPEN` (Greenfield Unclaimed Target)**:
   - Zero assignees and zero open competing Pull Requests. We fork the repository into the **`WholeTroutMedia`** GitHub organization (never cluttering personal user trees), reproduce the bug locally, and verify the fix before requesting review.

---

## 2. Clean Organization Isolation (`WholeTroutMedia` Only)

- All upstream forks created for bounty and bug-fix work live exclusively under the **`WholeTroutMedia`** GitHub organization (`https://github.com/WholeTroutMedia/<repo>`).
- Every fix is developed on a dedicated topic branch (`fix/issue-<number>-<slug>`) with a standalone verification test (`verify_fix.py` or native repo test suite) committed to this hub first.

---

## 3. Verification First, Upstream PR Second (The Review Gate)

Just like our daily Google AI Developers Forum cadence, **nothing is submitted upstream automatically**:

1. **Daily 08:45 AM Draft Cadence (`Easy -> Medium -> Hard`)**:
   - Each morning, our foundry selects one verified unclaimed issue along a rotating difficulty scale (`Easy`, `Medium`, `Hard`).
   - It prepares a complete dossier under `bounties/<bounty_id>/` containing:
     - `ISSUE_CONTEXT.md` (Upstream link, maintainer requirements, reward metadata)
     - `COMPETING_PR_AUDIT.md` (Timeline audit confirming zero active competing PRs)
     - `patch.diff` (Minimal, surgical unified diff adhering to the project's style)
     - `verify_fix.py` (Deterministic reproduction + regression test that must exit `0`)
     - `PR_DRAFT.md` (Friendly, natural peer-to-peer PR description)
2. **Staged Human Review**:
   - The dossier is pushed to `WholeTroutMedia/open-source-bounties`, logged in [`LEDGER.md`](./LEDGER.md), opened as a tracking review issue in this repository, and emailed to Justin (`justin.aharoni@inceptionengine.systems`) for review.
3. **Approved Upstream Submission**:
   - Only after human review and sign-off do we open the Pull Request against the upstream repository.

---

## 4. Communication & Attribution Standard

- **Acknowledge the Maintainer First**: Every PR and issue comment opens by acknowledging the specific problem, reproduction steps, or design constraint the maintainer described.
- **No Robotic Slop or Em-Dashes**: We write in plain, friendly, peer-to-peer engineering prose with zero em-dashes and zero generic boilerplate.
- **Clear Human Accountability**: Every outbound contribution carries our explicit review footer so maintainers always know a real engineer stands behind the patch:

*this has been reviewed by, approved by and submitted on behalf of jaharoni@gmail.com*
