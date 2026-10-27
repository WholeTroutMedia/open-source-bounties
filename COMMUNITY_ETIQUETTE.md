# WholeTroutMedia Open-Source Contribution & Etiquette Charter

This repository (`WholeTroutMedia/open-source-bounties`) is our public engineering ledger for auditing, verifying, and staging open-source bug fixes and funded community bounties prior to submitting Pull Requests upstream.

Open-source maintainers spend enormous energy triaging issues and reviewing code. Our goal is to make every contribution from **WholeTroutMedia** a genuine relief to review: surgical, well-tested, respectful of existing contributors, and reviewed by a human before submission.

---

## 1. Competing-PR & Prior-Work Audit (`CLAIM_OPEN` / `EXTEND_STALLED` / `SKIP_CLAIMED`)

Before writing code or claiming an issue, our workflow inspects the upstream issue timeline, assignees, and linked Pull Requests:

1. **`SKIP_CLAIMED` (Respect Active Contributors)**:
   - If a maintainer has already assigned the issue to another developer, we skip it.
   - If another contributor already has an active, substantive open Pull Request addressing the issue, we skip it completely so we never duplicate active work.

2. **`EXTEND_STALLED` (Unify & Credit Prior Attempts)**:
   - When an issue has prior comments with debugging notes or an older Pull Request that stalled or closed without merging, we explicitly credit the earlier contributors (`@handle`) in our notes and build cleanly on their findings, while also reviewing prior CI check results so our patch resolves any remaining test edge cases.

3. **`CLAIM_OPEN` (Greenfield Unclaimed Target)**:
   - Zero assignees and zero active competing Pull Requests. We fork the repository into the **`WholeTroutMedia`** GitHub organization, reproduce the issue locally, and verify the fix before requesting review.

---

## 2. Clean Organization Isolation (`WholeTroutMedia` Only)

- All upstream forks created for bounty and bug-fix work live exclusively under the **`WholeTroutMedia`** GitHub organization (`https://github.com/WholeTroutMedia/<repo>`).
- While a fix is awaiting human review, the raw patch (`patch.diff`), standalone reproduction suite (`verify_fix.py`), and Pull Request draft (`PR_DRAFT.md`) are staged inside our private vault (`WholeTroutMedia/bounty-solves-vault`) and attested publicly via SHA-256 commitment (`solve_envelope.sealed.json`).

---

## 3. Verification First, Upstream PR Second (The Review Gate)

Nothing is submitted upstream automatically:

1. **Daily 08:45 AM Draft Cadence (`Easy -> Medium -> Hard`)**:
   - Each morning, our foundry selects one verified unclaimed issue along a rotating difficulty scale (`Easy`, `Medium`, `Hard`).
   - It validates the fix against a standalone reproduction and regression harness (`verify_fix.py`, which must exit `0`) and stages the full review package in `WholeTroutMedia/bounty-solves-vault`.
2. **Staged Human Review & Maintainer Fast-Track**:
   - The public commitment receipt is logged in [`LEDGER.md`](./LEDGER.md), opened as a tracking review issue in this repository, and emailed to Justin (`justin.aharoni@inceptionengine.systems`) for review.
   - Verified maintainers of the upstream repository can request immediate PR submission or vault access at any time via the fast-track link in each dossier.
3. **Approved Upstream Submission**:
   - Once reviewed and approved, we push the topic branch (`fix/issue-<number>-<slug>`) to `WholeTroutMedia/<repo>` and open the Pull Request against the upstream repository.

---

## 4. Communication & Attribution Standard

- **Acknowledge the Maintainer First**: Every PR and issue comment opens by acknowledging the specific problem, reproduction steps, or design constraint the maintainer described.
- **Peer-to-Peer Engineering Prose**: We write in plain, friendly, peer-to-peer engineering prose with zero em-dashes and zero generic boilerplate.
- **Clear Human Accountability**: Every outbound contribution carries our explicit review footer so maintainers always know a real engineer stands behind the patch:

*this has been reviewed by, approved by and submitted on behalf of jaharoni@gmail.com*
