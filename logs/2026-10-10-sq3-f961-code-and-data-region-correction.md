# SQ-3 — a real correction: the "data region" is narrower than last cycle claimed, and $F961 is a loop entry point

**Trigger:** last cycle flagged `$FA06 JMP $F961` as a new jump target to follow next, naming it as the
explicit next step.

## What's already known / not done yet

Already known (last cycle): linear-sweep disassembly from `$F94D` produces garbage, and last cycle's log
stated the clean resync happened "exactly at `$F993`." Not done: actually disassembling from `$F961`
itself.

## Method and why it's non-circular

Re-downloaded the ROM fresh and re-verified the hash before analysis (unchanged:
`c85dc2204299b0a29209d3f80ae112678c171dab216719593625647d2436f1e1`). Disassembled from `$F961` per last
cycle's own named next step. When the result connected directly into the already-disassembled `$F993`
block, re-ran the original `$F94D` linear sweep precisely, instruction-by-instruction, to find the actual
desync/resync boundary rather than relying on memory of last cycle's own prior run.

## Result: a real, disclosed correction to last cycle's own claim

**Last cycle's log stated the linear sweep resynced "exactly at `$F993`." That is not correct — re-checked
precisely, it resyncs at `$F961`**, 50 bytes earlier than previously claimed:

```
$F95E  BPL $f971
$F960  ???          <- last garbage byte
$F961  LDA $04      <- resync point (not $F993)
$F963  STA $08
...
```

The true likely-data region is `$F94D`–`$F960` (roughly 20 bytes), not `$F94D`–`$F992` (roughly 70
bytes) as last cycle stated. The error: last cycle started the *second* disassembly pass directly at
`$F993` (the jump target named in the `JMP` instruction) without checking whether the linear sweep would
have resynced earlier on its own — it does, at `$F961`, and the content from `$F961` through `$F992` is
genuine code, not data, confirmed now by disassembling it directly and finding it flows straight into the
already-verified `$F993` block with no internal jumps.

## What this reveals about the actual control flow

`$F961`–`$F993`–(onward to `$FA06`) is one continuous, linear block of real code — not two separate
segments. It has (at least) two distinct entry points:
1. **`$F94A  JMP $F993`** (found two cycles ago, part of the reset routine) — jumps into the *middle* of
   this block, skipping `$F961`–`$F992`.
2. **`$FA06  JMP $F961`** (found last cycle) — jumps to the block's actual start.

This is a plausible, sensible real-world pattern (not yet confirmed by a trace): a one-time setup path
that skips some per-iteration initialization work (`$F961`–`$F992`, which clears tile-position RAM at
`$C0`–`$CD`) on the very first entry from reset, versus a repeating loop that always re-runs that
initialization. Stated as a hypothesis, not a confirmed finding — no trace yet.

## Honesty precommitment, kept

Correcting the prior claim here, in a new dated entry, rather than editing last cycle's log file (which
stays as-written, append-only) or letting the imprecise `$F993` resync claim stand uncorrected.

## Decision

The data-region hypothesis is narrowed: `$F94D`–`$F960`, not `$F94D`–`$F992`. `$F961`–`$F993` onward is
confirmed real code, not data. Next step: actually run an emulation trace to test the two-entry-point
hypothesis (does first entry really skip the `$C0`–`$CD` clear, and does the loop really come back around
through `$FA06`?) — this is genuinely testable with `py65`'s execution engine, not just its disassembler,
and would be real rung-2/3 evidence rather than more disassembly-only rung-1 work.
