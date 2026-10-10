# SQ-3 — disassembly continuation: following the jump target confirms last cycle's data-region hypothesis

**Trigger:** last cycle's raw disassembly log explicitly named this as the next step: "disassemble from
`$F993` onward (the actual continuing code path)."

## What's already known / not done yet

Already known: linear-sweep disassembly past `$F94A JMP $F993` produced garbage (`???`, nonsensical
opcodes) from `$F94D` to roughly `$F992`, with clean resync exactly at `$F993` — strong but not yet
confirmed evidence that region is data, not code. Not done: actually disassembling from the real jump
target to see if it reads as sensible code throughout (which would support the data-region hypothesis)
or itself breaks down (which would undermine it).

## Method and why it's non-circular

Re-downloaded the ROM fresh (not reused from a prior session) and re-verified its hash matches the
previously-recorded `c85dc2204299b0a29209d3f80ae112678c171dab216719593625647d2436f1e1` before analysis —
confirms this is the same, unmodified source. Disassembled 60 instructions starting exactly at `$F993`,
the `JMP`'s own documented target, rather than continuing the prior linear sweep.

## Result

**Clean throughout — no illegal/garbage opcodes across all 60 instructions.** This confirms last cycle's
hypothesis: `$F94D`–`$F992` is very likely a genuine data region the linear sweep walked through
incorrectly, and `$F993` is real, valid code.

**Two concrete findings worth flagging for the other specialist roles, not yet interpreted beyond what's
directly observable:**

1. **`$F9A7  BIT $0282`** — `$0282` is within the RIOT I/O address range (console switches — difficulty,
   Select/Reset — are read via this region on real 2600 hardware, per general knowledge of the memory
   map, not yet independently verified against a primary hardware reference this cycle). A real,
   identifiable touch of console hardware I/O, not just internal game logic — a concrete lead for
   `agents/memory-cartographer.md` to verify and map precisely once `data/hardware-reference.md` (SQ-2)
   exists.
2. **`$F9AD  LDA $f910,X`** — reads a small table at `$F910`, indexed by X, located just 4 bytes before
   the reset vector itself (`$F914`). Likely a short lookup table (joystick/input-direction mapping, given
   this is a sliding-tile game — not confirmed, flagged as a hypothesis for the next annotation pass).
3. **Another unconditional jump found**: `$FA06  JMP $F961` — per the exact lesson from last cycle, this
   log stops here rather than continuing the linear sweep past it. The next continuation should disassemble
   from `$F961` directly, not sweep through `$FA09` onward until that's done.

## Honesty precommitment, kept

Still raw disassembly only (evidence-ladder rung 1) — no annotation, no emulation trace confirming the
`$0282` RIOT-register identification or the `$F910` table hypothesis. Both flagged as leads, not findings.

## Decision

The data-region hypothesis from last cycle is now substantively supported (not just inferred from one
resync point, but from a full clean 60-instruction run at the actual target). Committed:
`data/disassembly/2048-2600/raw-disassembly-from-f993.txt`. Next continuation: `$F961` (the newly-found
jump target), following the same follow-control-flow discipline each time rather than reverting to linear
sweep.
