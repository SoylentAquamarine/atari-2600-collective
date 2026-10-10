# Knowledge Base — Current State

Last updated: 2026-10-09 (bootstrap)

This file is the shared, evolving understanding of the group. It only
changes via pull request. Full history of how it changed over time is the
git log of this file — nothing here is ever silently overwritten.

## Confirmed Findings

- **`github.com/chesterbr/2048-2600` is rights-clear for analysis**: MIT License, confirmed directly via
  GitHub's API (`license.spdx_id`) and the repository's own `LICENSE` file text, with a named copyright
  holder (Carlos Duarte do Nascimento, 2014); confirmed canonical (not a fork). ROM: 2048 bytes, SHA256
  `c85dc2204299b0a29209d3f80ae112678c171dab216719593625647d2436f1e1`. — 2026-10-10,
  `logs/2026-10-10-sq1-rom-rights-scoping.md`.
- **Raw mechanical disassembly of this ROM, two segments, committed and reproducible**: from its reset
  vector (`$F914`, `data/disassembly/2048-2600/raw-disassembly-from-reset.txt`) and from the real jump
  target found there (`$F993`, `data/disassembly/2048-2600/raw-disassembly-from-f993.txt`), both produced
  by `py65` (verified tool, see `data/toolchain-notes.md`). Meets `methods/falsification-standard.md`'s
  bar for a mechanical opcode-decode claim (committed output, no trace needed at this tier). —
  2026-10-10, `logs/2026-10-10-sq3-first-raw-disassembly.md` and
  `logs/2026-10-10-sq3-disassembly-continuation-from-jump-target.md`.
- **The first real emulation-trace-verified control-flow claim**: from reset, execution reaches `$F993`
  directly via `$F94A JMP $F993`, never executing `$F961`–`$F992` on first entry — confirmed by logging
  the actual program-counter sequence from `py65`'s execution engine (not inferred from static bytes).
  Separately, execution reaches `$F961` via a previously-undisassembled jump, `$FA23 JMP $F961` (on the
  taken branch of `$F9F8 BEQ $fa0d`) — not via the earlier-found `$FA06 JMP $F961`, which sits on the
  not-taken branch and remains unconfirmed by actual execution. Meets `methods/falsification-standard.md`'s
  trace-verification bar. — 2026-10-10, `logs/2026-10-10-sq3-first-emulation-trace.md`.
- **A real, precisely periodic repeating loop exists, entered at `$F993` (not `$F961`)**: a 50,000-step
  extended trace shows `$F993` revisited 20 times, stabilizing to an exact 2,616-step period; `$F961` is
  visited only once (confirming it is one-time setup, not the loop's own re-entry point); `$FA06` is never
  visited at all across the full trace, confirming the `$F9F8` branch consistently goes one way under
  `py65`'s deterministic, no-input conditions. Trace-verified (rung 3). — 2026-10-10,
  `logs/2026-10-10-sq3-extended-trace-and-loop-periodicity.md`.
- **A likely graphics/display kernel identified at `$FBB0`-`$FC8F`** (rung 2, disclosed interpretation, not
  rung-3-certain — `py65` has no TIA video model to visually confirm pixel output): per
  `data/hardware-reference.md`'s TIA register map (seeded this cycle, cross-checked against independent
  sources), the trace-confirmed, alignment-corrected disassembly at this range shows repeated WSYNC
  (`$02`) strobes, playfield-register (`$0D`/`$0E`/`$0F`) clears, and a loop writing to the player-sprite
  registers (`$1B`/`$1C`, GRP0/GRP1) driven by a pointer table built from packed 4-bit nibbles in a source
  table — consistent with drawing the sliding-tile board's glyphs via the player-sprite registers, a known
  homebrew technique. Committed:
  `data/disassembly/2048-2600/raw-disassembly-from-fbb0.txt`. — 2026-10-10,
  `logs/2026-10-10-sq3-extended-trace-and-loop-periodicity.md`.
- **A self-caught instruction-alignment error, corrected before any wrong artifact was committed**: an
  initial static disassembly attempt starting at `$FC10` mis-parsed the opcode stream (the real boundary is
  `$FC0F`-`$FC10`, the tail of a `STA $a6` instruction) — caught by cross-checking against the live trace's
  own actually-visited addresses before writing it up, and replaced with a trace-order-derived disassembly
  instead of ever being committed. — 2026-10-10,
  `logs/2026-10-10-sq3-extended-trace-and-loop-periodicity.md`.

## ROMs Under Analysis

- **2048-2600** (`chesterbr/2048-2600`) — raw disassembly extended to four segments (rung 1): the
  reset-vector startup routine (`$F914`–`$F94A`), the main code block (`$F961`–`$FA0D`), and the newly
  disassembled branch target (`$FA0D`–`$FA2A`) — all confirmed clean. **Correction (2026-10-10)**: the
  likely-data region narrows to `$F94D`–`$F960` (~20 bytes), not the originally-claimed `$F94D`–`$F992`.
  **Trace-verified (2026-10-10, rung 3)**: the first-entry skip-ahead to `$F993` is confirmed by real
  execution; the path back to `$F961` is confirmed to go via `$FA23`, not the previously-assumed `$FA06`
  — a genuine correction to last cycle's own hypothesis, not just a confirmation of it. Two unconfirmed
  leads still open for future annotation: a RIOT I/O touch (`BIT $0282`) and a small lookup table at
  `$F910`. **Update (2026-10-10), resolved**: a 50,000-step extended trace confirms `$F993` (not `$F961`)
  is the real, precisely periodic loop entry point (period 2,616 steps); `$FA06` is never taken across the
  full trace. Disassembly extended into `$FBB0`-`$FC8F` (new region, trace-order-verified), including a
  likely graphics-kernel routine — see Confirmed Findings above. New leads: `$FD97` (a jump target reached
  only on a later loop pass, not yet disassembled) and `$9D`/`$C6`/`$C7`/`$C9`/`$CB`/`$A4` (zero-page
  variables referenced in the newly-disassembled region, not yet interpreted).

## Verified Disassemblies

- **A likely graphics/display kernel, `$FBB0`-`$FC8F`** (2048-2600) — rung 2 (interpreted) + rung 3
  (trace-verified for control flow and register identity): builds a glyph-pointer table from packed board
  values, clears the playfield registers, and writes player-sprite registers per scanline with WSYNC
  strobes between writes. Disclosed as a plausible interpretation grounded in verified TIA register
  identities and structural pattern, not a pixel-level certainty (`py65` has no TIA video model). See
  `data/disassembly/2048-2600/raw-disassembly-from-fbb0.txt` and
  `logs/2026-10-10-sq3-extended-trace-and-loop-periodicity.md`.

## Open Questions

- What disassembly/emulation/trace toolchain is actually usable in this
  environment, and does it model TIA/RIOT behavior or only the base 6502
  instruction set? See SQ-1 — **partially answered (2026-10-09)**: `py65`
  verified correct for base 6502 execution/disassembly (see
  `data/toolchain-notes.md`); it has no TIA/RIOT model, so the
  timing-trace half of this question remains open.
- Which specific Atari 2600 ROMs are confirmed public-domain or openly
  licensed and therefore legally analyzable here? See SQ-1 — **answered
  (2026-10-10)**: `chesterbr/2048-2600` confirmed MIT-licensed, see
  Confirmed Findings above. Four more MIT-licensed candidates found but
  not yet individually verified in depth.
- What does the existing public reverse-engineering literature (Stella,
  6502.org, AtariAge, published books) already document that this project
  should build on rather than duplicate? See SQ-2 and SQ-4. **Partially answered (2026-10-10)**: SQ-2's
  hardware-reference catalog now exists — `data/hardware-reference.md` — covering the 6507/6502
  differences, the RIOT RAM/IO memory ranges, and the full TIA write-register map, cross-checked against
  independent sources and directly applied to this cycle's own disassembly work. Bank-switching schemes
  still not catalogued (deferred — this project's current ROM doesn't need them).
