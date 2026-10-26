Thanks for the reproducible test case on `ZStream.groupedWithin` with `.forever`, @DenisKusakin, and for confirming that `series/1.x` PRs are still welcome here, @jdegoes.

Building on @DenisKusakin's finding that this regressed on `series/1.x` after the `concat` optimization in `#7396` (and @argofowl's earlier closed investigation in `#10917`), the root cause on `series/1.x` is that when an infinite stream (`ZStream.fromIterable(Seq(1, 2)).forever`) is followed by a stateful filter (`mapAccum` + `collect`), every pull after the initial `[1, 2]` returns an empty chunk without terminating. Inside `aggregateAsyncWithinEither`, the upstream pull loop keeps spinning on empty chunks so the `Schedule.spaced(5.seconds)` timer completion never preempts the pull to flush the non-empty accumulator (`[1, 2]`).

### What This Patch Changes (`series/1.x`)
1. Yields on empty filtered chunks and interrupts the pending empty-chunk pull fiber when the schedule timer wins the `raceWith` branch in `aggregateAsyncWithinEither`, immediately flushing the accumulated elements (`[1, 2]`) so `.take(1)` completes right on the schedule boundary.
2. Adds a regression spec in `ZStreamSpec` covering `ZStream.fromIterable(Seq(1, 2)).forever.mapAccum(...).collect(...).groupedWithin(100, 5.seconds).take(1)` with `TestClock.adjust(5.seconds)`.

/claim #8686
Fixes #8686

*this has been reviewed by, approved by and submitted on behalf of jaharoni@gmail.com*
