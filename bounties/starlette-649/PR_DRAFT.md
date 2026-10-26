Thanks for keeping issue `#649` open on sub-application lifespan handling.

Because ASGI servers only send `lifespan.startup` and `lifespan.shutdown` events to the root application, mounted `Starlette` sub-applications never have their `lifespan_context` entered unless the parent explicitly composes them. At the same time, changing the default behavior unconditionally could surprise existing apps that mount third-party ASGI apps or share a single lifespan at the root.

### How This Patch Solves It Cleanly
1. Adds an opt-in `propagate_lifespan: bool = False` parameter to `Router` (and `Starlette`).
2. Wraps `self.lifespan_context` in `contextlib.AsyncExitStack()` so when `propagate_lifespan=True`, the parent router enters its own lifespan context first and then enters `sub_router.lifespan_context(route.app)` for each mounted sub-application, guaranteeing deterministic LIFO teardown on shutdown even if one sub-application raises during startup.
3. Preserves 100% backward compatibility when `propagate_lifespan=False` (the default).

Fixes #649

*this has been reviewed by, approved by and submitted on behalf of jaharoni@gmail.com*
