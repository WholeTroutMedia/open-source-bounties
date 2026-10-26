# Upstream Bounty Context: `zio/zio#8686`

- **Upstream Issue**: [https://github.com/zio/zio/issues/8686](https://github.com/zio/zio/issues/8686)
- **Repository**: `zio/zio` (`4,432` stars, Scala functional effect & streaming runtime)
- **Funding Platform**: Algora (`algora-pbc[bot]`)
- **Difficulty Tier**: `Medium`
- **Target Branch**: `series/1.x`

## Problem Statement
On `series/1.x` (introduced after `ZStream.concat` changes in PR `#7396`), chaining `.forever`, `.mapAccum`, `.collect`, and `.groupedWithin(100, 5.seconds).take(1)` hangs forever. When `collect` filters out subsequent repeats on an infinite stream, upstream keeps pulling empty chunks while `aggregateAsyncWithinEither` fails to flush its non-empty accumulator when the `Schedule.spaced(5.seconds)` timer fiber completes.
