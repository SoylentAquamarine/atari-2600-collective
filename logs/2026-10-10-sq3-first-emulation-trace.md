# SQ-3 — the first real emulation trace: confirms one hypothesis, corrects another, finds a third jump

**Trigger:** last cycle's own named next step: "an actual emulation trace to test the two-entry-point
hypothesis, not more disassembly." This is this project's first use of `py65`'s execution engine (not
just its disassembler) — the first real rung-2/3 evidence this project has produced.

## What's already known / not done yet

Already known (from two cycles of static disassembly): a reset-time jump `$F94A JMP $F993` and a
loop-closing jump `$FA06 JMP $F961` were both found by reading bytes, with a hypothesis that these were
the code block's two entry points. Not done: actually running the code to see which paths execution
genuinely takes, since static disassembly cannot resolve conditional branches — only execution can.

## Design and why it's non-circular

Set the CPU's program counter to the ROM's own reset vector (`$F914`, read from the ROM's own last two
bytes, same as prior cycles) and single-stepped real execution, logging every program-counter value
visited, in order. This directly tests the hypothesis using the tool built for exactly this purpose
(`py65`'s `MPU.step()`), not a re-reading of the static bytes.

## Stated prediction

Expected the trace to show `$F993` reached directly from `$F94A` (confirming the "skips `$F961`–`$F992`
on first entry" half of last cycle's hypothesis), and expected it to eventually reach `$F961` via the
previously-found `$FA06 JMP $F961`.

## Honesty precommitment

Report the actual visited-address sequence exactly, including if it contradicts the prediction.

## Result

**Confirmed**: execution reaches `$F993` directly from `$F94A` (step 1247), never touching
`$F961`–`$F992` on the way — the "skip on first entry" half of the hypothesis holds up under real
execution, not just static reading.

**Prediction corrected, not confirmed**: `$F961` was reached at step 1280 — but **not** via `$FA06`.
`$FA06` was never visited in this trace. The actual path, read off the trace precisely:

```
$F993 -> ... -> $F9F8  BEQ $fa0d   (branch taken -- Z flag was set)
$FA0D -> $FA0F -> $FA17 -> $FA19 -> $FA1B -> $FA21 -> $FA23  JMP $F961
```

Disassembling `$FA0D`–`$FA2A` (not previously read) revealed **a third jump to `$F961`**, at `$FA23`,
reached via a short decision chain checking values at `$0C`, `$0D`, and `$A8` (zero-page RAM — not yet
interpreted). The earlier-found `$FA06 JMP $F961` sits on the **not-taken** branch of `$F9F8`'s `BEQ` —
plausible as a second, parallel path to the same destination (a common real pattern: several decision
branches all converging on one shared loop-restart point), but this is not itself confirmed by this
trace, since that branch wasn't taken this run.

**Genuinely unresolved, disclosed as a real limitation**: whether `$F961` is reached again later (i.e.
whether this really is a per-frame repeating loop) was not observed within 4,000 execution steps.
`py65` has no TIA/RIOT hardware model (already disclosed in `data/toolchain-notes.md`) — real Atari 2600
games are paced by television-frame timing and hardware input reads that this toolchain doesn't simulate,
so a long-range "does it loop every frame" question may not be answerable with this toolchain alone,
independent of how many steps are traced.

## Decision

This is the project's first real emulation-trace evidence, and it did real work: confirmed one half of
last cycle's hypothesis precisely, found that the other half's *mechanism* was wrong even though the
*destination* was right (reaches `$F961`, but via a third, newly-found jump rather than the
previously-assumed one), and surfaced a genuine toolchain limitation (no frame-timing model) rather than
over-interpreting an inconclusive long-range result. `$FA0D`–`$FA2A` is now disassembled and on file,
ready for the next annotation pass once the `$0C`/`$0D`/`$A8` RAM variables are better understood.
