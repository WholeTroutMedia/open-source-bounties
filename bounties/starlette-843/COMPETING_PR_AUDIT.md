# Competing-PR & Community Etiquette Audit: `starlette-843`

- **Upstream Target**: [`Kludex/starlette#843`](https://github.com/Kludex/starlette/issues/843)
- **Audit Classification**: **`EXTEND_STALLED`**
- **Audit Summary**: Issue remains OPEN with 0 open PRs; 2 historical PR ref(s) by @pyritewolf (#75), @pamelafox (#293) - safe to build on and credit prior findings
- **Open Competing PRs**: `0`
- **Active Assignees**: `0`
- **WholeTroutMedia Fork**: [`WholeTroutMedia/starlette`](https://github.com/WholeTroutMedia/starlette)
- **Audited At**: `2026-10-26T13:47:36.231043+00:00`

## Prior Unmerged / Closed PR Attempts
- PR `#75` (`MERGED`, `merged=True`) by `@pyritewolf`: #74: Trust proxy headers in live environments
- PR `#293` (`MERGED`, `merged=True`) by `@pamelafox`: Use relative path for url_for

## Recent Maintainer & Contributor Comment Digest
- @lovelydinosaur: I don't quite agree with the assessment that it's not possible to determine the incoming host - proper setup of proxies & uvicorn should relay that information correctly. As an exa
- @jacopofar: This is quite critical when setting up OAuth, since the third party checks the callback URL and complains if it's not a whitelisted one. On Flask I solve this by passing `_external
- @anentropic: I think I have this problem too I'm deploying an app to fly.io, I get an `https://<myapp>.fly.dev` url. But the static files are not displaying and it seems to be because the templ
- @anentropic: I have gone with `--proxy-headers --forwarded-allow-ips=*` args to uvicorn and can confirm that it does work at least
- @fzumstein: Why not introduce an additional `path_for` template function that returns the URL path instead of an absolute URL? That would be consistent with `request.path` and wouldn't cause a
