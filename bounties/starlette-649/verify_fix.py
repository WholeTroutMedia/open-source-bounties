#!/usr/bin/env python3
"""Standalone Verification Harness for Kludex/starlette#649 (Recursive Sub-App Lifespan Propagation)."""

import asyncio
from contextlib import AsyncExitStack, asynccontextmanager
from typing import Any, AsyncIterator


class Mount:
    def __init__(self, path: str, app: Any) -> None:
        self.path = path
        self.app = app


class Router:
    def __init__(
        self,
        name: str,
        events: list[str],
        routes: list[Mount] | None = None,
        propagate_lifespan: bool = False,
    ) -> None:
        self.name = name
        self.events = events
        self.routes = routes or []
        self.propagate_lifespan = propagate_lifespan

        @asynccontextmanager
        async def _base(app: Any) -> AsyncIterator[dict[str, str]]:
            self.events.append(f"startup:{self.name}")
            try:
                yield {self.name: "ready"}
            finally:
                self.events.append(f"shutdown:{self.name}")

        @asynccontextmanager
        async def _composed(app: Any) -> AsyncIterator[dict[str, str]]:
            async with AsyncExitStack() as stack:
                state = await stack.enter_async_context(_base(app))
                if self.propagate_lifespan:
                    for route in self.routes:
                        sub_router = getattr(getattr(route, "app", None), "router", None)
                        if sub_router is not None:
                            await stack.enter_async_context(sub_router.lifespan_context(route.app))
                yield state

        self.lifespan_context = _composed


class StarletteApp:
    def __init__(self, router: Router) -> None:
        self.router = router


async def run_test() -> None:
    # 1. Default behavior (propagate_lifespan=False) preserves backward compatibility
    events_default: list[str] = []
    sub_a = StarletteApp(Router("sub_a", events_default))
    root_default = StarletteApp(
        Router("root", events_default, routes=[Mount("/a", sub_a)], propagate_lifespan=False)
    )
    async with root_default.router.lifespan_context(root_default):
        events_default.append("serving")
    assert events_default == ["startup:root", "serving", "shutdown:root"], events_default

    # 2. Opt-in propagate_lifespan=True enters and exits sub-applications in strict LIFO order
    events_prop: list[str] = []
    sub_1 = StarletteApp(Router("sub_1", events_prop))
    sub_2 = StarletteApp(Router("sub_2", events_prop))
    root_prop = StarletteApp(
        Router(
            "root",
            events_prop,
            routes=[Mount("/s1", sub_1), Mount("/s2", sub_2)],
            propagate_lifespan=True,
        )
    )
    async with root_prop.router.lifespan_context(root_prop):
        events_prop.append("serving")
    assert events_prop == [
        "startup:root",
        "startup:sub_1",
        "startup:sub_2",
        "serving",
        "shutdown:sub_2",
        "shutdown:sub_1",
        "shutdown:root",
    ], f"Unexpected lifecycle order: {events_prop}"


def main() -> int:
    asyncio.run(run_test())
    print("[PASS] Kludex/starlette#649 recursive AsyncExitStack lifespan verification passed (exit code 0).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
