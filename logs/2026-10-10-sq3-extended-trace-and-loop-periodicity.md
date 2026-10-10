# SQ-3 — extended trace: a real repeating loop confirmed, a self-caught alignment error, and the first rung-2 interpretation (a likely graphics kernel)

**Trigger:** last cycle's own named next step — the first emulation trace left two things genuinely
unresolved: whether `$F961` (or any address) repeats as a per-frame loop, and what the `$0C`/`$0D`/`$A8`
zero-page variables actually do. Both are addressed directly this cycle.

## What's already known / not done yet

Already known: a 4,000-step trace confirmed the first-entry control flow (`$F94A JMP $F993`, then
`$F9F8 BEQ` taken to `$FA23 JMP $F961`) but could not observe any repetition, and `py65` has no TIA/RIOT
timing model, disclosed as a possible hard limit on the looping question. Not done: a longer trace, any
read/write instrumentation on the named zero-page variables, or any hardware-register identification for
this ROM's own code (SQ-2's hardware-reference catalog did not exist before this cycle).

## Design and why it's non-circular

Extended the same trace to 50,000 steps (12.5x longer), logging every visit to the previously-named
addresses (`$F961`, `$F993`, `$FA06`, `$FA23`, `$F9F8`) plus every write to `$0C`/`$0D`/`$A8`, comparing
memory state before/after each `mpu.step()` rather than relying on disassembled instruction text (which
turned out to have its own case-sensitivity bug in an earlier diagnostic pass, caught and discarded before
being reported as a finding). Separately, installed no new dependency — `py65`'s disassembler was reused
to identify TIA register addresses, cross-checked against freshly-searched hardware documentation rather
than asserted from training-data memory, directly motivated by seeding SQ-2 (previously untouched).

## Honesty precommitment

Report the periodicity result exactly as measured, disclose the alignment error found and corrected before
committing any wrong artifact, and flag the graphics-kernel interpretation as a plausible rung-2 reading,
not a trace-confirmed rung-3 certainty (since `py65` cannot visually verify pixel output).

## Result 1 — a real, precisely periodic loop, entered at $F993

Over 50,000 steps, `$F993` is revisited **20 times**, at steps `[1247, 1385, 4020, 6636, 9252, ...]`,
stabilizing to an **exact 2,616-step period** after the first two visits (deltas:
`138, 2635, 2616, 2616, 2616, ...` — every subsequent interval identical). `$F961`, by contrast, is visited
**exactly once** (step 1280) in the full 50,000 steps — not part of the repeating loop at all, confirming it
is one-time initialization code, not the loop's own re-entry point as earlier hypothesized. `$FA06`
(the previously-unconfirmed "parallel path" to `$F961`) is **never visited** across all 50,000 steps — the
`$F9F8` branch consistently goes the same way every single loop iteration under `py65`'s deterministic,
no-input conditions. This answers last cycle's open question directly: **yes, there is a genuine, precisely
periodic repeating loop**, and its entry point is `$F993`, not `$F961`.

## Result 2 — a self-caught instruction-alignment error, corrected before anything wrong was committed

A first attempt to read the code touching the newly-found `$0D` write sites (`$FC22`, `$FC69`) used a
**static linear disassembly starting at `$FC10`** — exactly the failure mode this project has hit and
corrected before (see `logs/2026-10-10-sq3-f961-code-and-data-region-correction.md`). Before writing this
up, cross-checked it against the set of addresses the live trace actually visited in this range: the trace
landed on `$FC11`, never `$FC10`, as an instruction start — a direct sign of misalignment. Inspecting the
raw ROM bytes confirmed it: `$FC0F`-`$FC10` is really the tail of a `STA $a6` instruction (opcode `$85`,
operand `$A6`) that the `$FC10`-start sweep had instead mis-parsed as the start of a different, equally
valid-looking instruction (`LDA $0a`, opcode `$A6` read as `LDX zp` instead of as an operand byte). The
`$FC10`-start listing was **never committed** — replaced with a disassembly built directly from the live
trace's own actually-visited program-counter sequence (address-sorted, de-duplicated), which is
alignment-safe by construction. Committed as
`data/disassembly/2048-2600/raw-disassembly-from-fbb0.txt`.

## Result 3 — TIA register identification, seeding SQ-2, and a plausible graphics-kernel interpretation

Seeded `data/hardware-reference.md` (SQ-2's deliverable, untouched before this cycle) with the TIA
write-register map ($00-$2C), cross-checked against multiple independent sources this cycle (not asserted
from memory). Applying it directly to the corrected `$FBB0`-`$FC8F` disassembly:

- Several `STA $02` instructions are **WSYNC strobes** (scanline synchronization — the canonical Atari 2600
  "racing the beam" idiom).
- A loop at `$FBF5`-`$FC1C` unpacks nibble pairs from a table at `$00A1,Y`, computing `nibble*5 + $C6` for
  each nibble and storing it into a pointer table at `$B0,X` — consistent with building **per-cell glyph
  pointers** from packed 4-bit board values, with a 5-byte stride (plausibly 5 scanlines per digit/tile
  glyph).
- A second loop at `$FC2C`-`$FC52` zeroes `PF0`/`PF1`/`PF2` (the playfield registers) and then, for 5
  iterations, reads through five of those just-built pointers (`($B0),Y` through `($BA),Y`) and writes the
  results to **`GRP0`/`GRP1`** (the player-sprite bitmap registers) — the single most canonical Atari 2600
  per-scanline graphics-kernel pattern, here apparently repurposed to draw the sliding-tile board rather
  than literal player sprites, a known homebrew technique.
- `$FBDC`: `LDA $a8; CMP #$07` — confirms `$A8` (first flagged two cycles ago) is compared against a fixed
  value, consistent with a small discrete game/animation-state variable, not a per-frame counter — matches
  its earlier-observed behavior (written only twice in 50,000 steps, not every iteration).
- `$FC64 JMP $fd97` — only taken on a later pass (step 3884, not the first iteration at step 1820),
  confirming `$C6` genuinely changes value between loop iterations and this isn't dead code. `$FD97` is a
  new, undisassembled lead for a future cycle.

**Disclosed limit**: this is a plausible, well-motivated rung-2 interpretation grounded in verified register
identities and the code's structural pattern, not a rung-3 certainty — `py65` has no TIA video model, so
the actual pixel output was never visually confirmed, only inferred from which hardware registers are
being written and when.

## Decision

Promoting to `knowledge-base/state.md`: the loop-periodicity finding (rung 3, trace-verified) and the
graphics-kernel interpretation (rung 2, disclosed as such). This is the project's deepest annotation-level
result so far — the first place a routine's likely *purpose*, not just its mechanical opcode sequence, is
argued from real evidence.
