# SQ-3 — first raw disassembly pass: 2048-2600, and a real methodology lesson

**Trigger:** SQ-1 completed this cycle (both toolchain and rights-scoping halves). SQ-3's own scope names
the immediate next step once a target is rights-cleared: raw mechanical disassembly.

## What's already known / not done yet

Already known: `github.com/chesterbr/2048-2600` is rights-clear (MIT, verified this cycle), 2048 bytes,
with a stated reset routine implied by standard Atari 2600 conventions. Not done: any actual disassembly.

## Design and why it's non-circular

A raw mechanical disassembly is, by this project's own evidence ladder (`config/research-department.md`),
the lowest-risk, most nearly-infallible step — pure opcode decode, no interpretation. Fetched the ROM
directly from its own GitHub-hosted binary (not reconstructed or rebuilt), hashed it, and disassembled
starting from the reset vector (the processor's own documented entry point, read from the ROM's own last
two bytes per 6502/6507 convention) rather than an arbitrary offset.

## Result

ROM hash: `c85dc2204299b0a29209d3f80ae112678c171dab216719593625647d2436f1e1` (2048 bytes, matches SQ-1's
rights-scoping record). Reset vector: `$F914`.

**The first ~20 instructions are a clean, textbook-correct match to the standard, independently-documented
Atari 2600 startup idiom**: `SEI` (disable interrupts), `CLD` (clear decimal mode), then the well-known
"clear all RAM/TIA/RIOT" loop (`LDX #$00; TXA; TAY; DEX; TXS; PHA; BNE` back to the `PHA`) — X wraps from
`$00` to `$FF`, `TXS` sets the stack pointer, and the loop pushes zero to every address as X counts down,
zeroing the entire 128-byte RAM/register space in one compact loop. This pattern is documented
independently in the general 2600 programming literature (not cited at primary-source tier this cycle,
noted as a recognized pattern from general background knowledge, consistent with this project's own
disclosure standard) — its exact match here is a real, useful confirmation that both the toolchain and
this cycle's ROM-mapping assumption (mirrored at `$F000`–`$F7FF` and `$F800`–`$FFFF`) are correct.

**A real methodology lesson, caught directly, not asserted**: continuing the disassembly linearly past
`$F94A JMP $F993` produces clear garbage — illegal/nonsensical opcodes (`???`, out-of-context `ORA`,
`BRK` runs) from `$F94D` through roughly `$F992`, before the output becomes sensible 6502 again exactly
at `$F993`, the `JMP`'s own target. This is the textbook failure mode of naive linear-sweep disassembly:
it cannot tell code from data and will happily "decode" data bytes as if they were instructions. The
clean resync at `$F993` is strong evidence that `$F94D`–`$F992` is very likely **data** (sprite/graphics
tables, given this project's domain — not yet confirmed which), not code, and was never meant to be
read linearly past the jump.

## Honesty precommitment, kept

This is raw disassembly only (evidence-ladder rung 1) — no annotation (rung 2, "what does this routine
mean") and no trace verification (rung 3) attempted this cycle. The "this looks like the standard startup
idiom" and "this looks like data, not code" readings are both disclosed as pattern-matching from general
knowledge of 6502/2600 conventions, not yet confirmed by an actual emulation trace — the next real step,
not asserted as already done.

## Decision

SQ-3 has a genuine first raw disassembly on record, with a real, useful, disclosed methodology finding
(linear-sweep disassembly fails across unconditional jumps — future passes should follow control flow,
i.e. jump to `$F993` directly, rather than reading straight through `$F94A`). Next step: disassemble
from `$F993` onward (the actual continuing code path), and begin rung 2 (annotation) only once an actual
emulation trace (not yet run) can back specific claims, per `methods/falsification-standard.md`.
