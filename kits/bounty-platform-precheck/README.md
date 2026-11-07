# Free Bounty Platform Pre-Check SDK (for Algora, Polar, Opire, Gitcoin & OSS Maintainers)

**Instant, zero-knowledge pre-check to block verified AI spam-bot rings and sockpuppet accounts before they claim open-source bounties or pollute pull request queues.**

## How It Works
1. Hashes the contributor's GitHub username locally using one-way `SHA-256` (`sha256(username.strip().lower())`).
2. Checks that hash against our live, auto-updating cloud blocklist (`verified_spam_bot_blocklist.json`).
3. Zero plain-text usernames are ever sent over the network, and newly caught bots are blocked within seconds of hitting our 3-Stop Conformance Quarantine.

## Usage (Python or Node.js)
```bash
python3 verify_contributor.py some-github-username
node verify_contributor.mjs some-github-username
```
