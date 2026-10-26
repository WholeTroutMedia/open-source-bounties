# Upstream Bounty Context: `Kludex/starlette#649`

- **Upstream Issue**: [https://github.com/Kludex/starlette/issues/649](https://github.com/Kludex/starlette/issues/649)
- **Polar.sh Pledge Page**: `https://polar.sh/encode/starlette/issues/649`
- **Repository**: `Kludex/starlette` (`12,685` stars, Python ASGI framework)
- **Difficulty Tier**: `Hard` (ASGI Lifespan State-Machine & Nested `AsyncExitStack` Composition)
- **Target Branch**: `master`

## Problem Statement
When a Starlette application mounts sub-applications via `Mount("/sub", app=sub_app)`, the parent `Router.lifespan()` context only runs the root router's lifespan context and does not enter the lifespan context managers of mounted sub-applications. Supporting opt-in recursive `AsyncExitStack` lifespan composition (`propagate_lifespan: bool = False`) allows modular sub-apps to manage their own database pools and background tasks safely without breaking existing ASGI mounts that do not expect lifespan events.
