# Competing-PR & Community Etiquette Audit: `starlette-843`

- **Upstream Target**: [`Kludex/starlette#843`](https://github.com/Kludex/starlette/issues/843)
- **Audit Classification**: **`EXTEND_STALLED`**
- **Audit Summary**: Issue remains OPEN with 0 open PRs; 3 historical PR ref(s) by @pedromineo (#4), @pyritewolf (#75), @pamelafox (#293) - safe to build on and credit prior findings
- **Open Competing PRs**: `0`
- **Active Assignees**: `0`
- **WholeTroutMedia Fork**: [`WholeTroutMedia/starlette`](https://github.com/WholeTroutMedia/starlette)
- **Private Solution Vault**: [`WholeTroutMedia/bounty-solves-vault`](https://github.com/WholeTroutMedia/bounty-solves-vault) (`private: True` - Original Repo Owner & `@jaharoni` Only)
- **Audited At**: `2026-10-27T17:35:09.163089+00:00`

## Prior Unmerged / Closed PR Attempts
- PR `#4` (`CLOSED`, `merged=False`) by `@pedromineo`: fix: [BOUNTY DRAFT | Easy] Kludex/starlette#843 - Add Request.path_for and relative URL resolution alongside Request.url_for (resolves #1)
- PR `#75` (`MERGED`, `merged=True`) by `@pyritewolf`: #74: Trust proxy headers in live environments
- PR `#293` (`MERGED`, `merged=True`) by `@pamelafox`: Use relative path for url_for

## Recent Maintainer & Contributor Comment Digest
- @jacopofar: This is quite critical when setting up OAuth, since the third party checks the callback URL and complains if it's not a whitelisted one. On Flask I solve this by passing `_external
- @anentropic: I think I have this problem too I'm deploying an app to fly.io, I get an `https://<myapp>.fly.dev` url. But the static files are not displaying and it seems to be because the templ
- @anentropic: I have gone with `--proxy-headers --forwarded-allow-ips=*` args to uvicorn and can confirm that it does work at least
- @fzumstein: Why not introduce an additional `path_for` template function that returns the URL path instead of an absolute URL? That would be consistent with `request.path` and wouldn't cause a
- @Sodototive95: ### Pull Request Submitted: Clean & Tested Resolution for #843 PR: https://github.com/Kludex/starlette/pull/3747 **Summary of Fix:** - Adds in . - Adds in, resolving root-relative
- @sm-Fifteen: Thank you @Kludex for not merging the slop requests, but that raises the question of what's happenning with this issue. It's been standing for 6 years, made it through v1.0 and is 
