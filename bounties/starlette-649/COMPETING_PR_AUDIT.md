# Competing-PR & Community Etiquette Audit: `starlette-649`

- **Upstream Target**: [`Kludex/starlette#649`](https://github.com/Kludex/starlette/issues/649)
- **Audit Classification**: **`EXTEND_STALLED`**
- **Audit Summary**: Issue remains OPEN with 0 open PRs; 9 historical PR ref(s) by @adriangb (#3516), @daanvdk (#1988), @Lancetnik (#2189), @udithishanka (#4547) - safe to build on and credit prior findings
- **Open Competing PRs**: `0`
- **Active Assignees**: `0`
- **WholeTroutMedia Fork**: [`WholeTroutMedia/starlette`](https://github.com/WholeTroutMedia/starlette)
- **Private Solution Vault**: [`WholeTroutMedia/bounty-solves-vault`](https://github.com/WholeTroutMedia/bounty-solves-vault) (`private: True` - Original Repo Owner & `@jaharoni` Only)
- **Audited At**: `2026-10-26T17:02:07.320350+00:00`

## Prior Unmerged / Closed PR Attempts
- PR `#3516` (`CLOSED`, `merged=False`) by `@adriangb`: Add startup/shutdown dependencies and dependency caching lifespan control
- PR `#1988` (`CLOSED`, `merged=False`) by `@daanvdk`: Run lifespans of mounted applications
- PR `#2189` (`CLOSED`, `merged=False`) by `@Lancetnik`: Add include_router to Starlette and Router
- PR `#4547` (`CLOSED`, `merged=False`) by `@udithishanka`: feat(jac-scale): mount ASGI sub-apps via jac.toml
- PR `#3440` (`CLOSED`, `merged=False`) by `@Kayforkind`: Propagate lifespan events to mounted applications
- PR `#799` (`MERGED`, `merged=True`) by `@lovelydinosaur`: Support generator function to manage startup/shutdown.
- PR `#35` (`MERGED`, `merged=True`) by `@adriangb`: feat/refactor!: router-level middleware, support for lifespans on mounted apps
- PR `#1676` (`MERGED`, `merged=True`) by `@RobbeSneyders`: Add lifespan middleware
- PR `#9630` (`MERGED`, `merged=True`) by `@Lancetnik`: 🐛 Ensure that `app.include_router` merges nested lifespans

## Recent Maintainer & Contributor Comment Digest
- @Cyberbolt: Solution: ```python from fastapi import FastAPI from contextlib import asynccontextmanager, AsyncExitStack sub_app = FastAPI() @asynccontextmanager async def sub_lifespan(app: Fast
- @racinmat: Any progress on this? There are new use-cases that I think are relevant: in AI Agents, both a2a and adk frameworks have FastAPI integration and use lifespans: https://github.com/a2
- @racinmat: If anyone is interested, I made a more generic workaround: ```python def extract_lifespan_from_app(app) -> Callable[[Any], AsyncContextManager[None]] | None: """ Extract lifespan f
- @racinmat: Hm, this https://github.com/fastapi/fastapi/issues/811#issuecomment-1870030103 looks even better.
- @IgnazioDS: The MCP use case mentioned at the bottom of this thread is now one of the most common real-world triggers for this issue. When you mount an MCP server (`from mcp.server.fastmcp imp
- @arseniyaleksandrov47-debug: ### 🚀 Solution & Bounty Submission: Propagate Lifespan Events to Mounted Sub-Applications **Target Issue**: #649 **Pull Request**: https://github.com/Kludex/starlette/pull/3739 ###
