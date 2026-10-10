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

## ROMs Under Analysis

- **2048-2600** (`chesterbr/2048-2600`) — raw disassembly extended to four segments (rung 1): the
  reset-vector startup routine (`$F914`–`$F94A`), the main code block (`$F961`–`$FA0D`), and the newly
  disassembled branch target (`$FA0D`–`$FA2A`) — all confirmed clean. **Correction (2026-10-10)**: the
  likely-data region narrows to `$F94D`–`$F960` (~20 bytes), not the originally-claimed `$F94D`–`$F992`.
  **Trace-verified (2026-10-10, rung 3)**: the first-entry skip-ahead to `$F993` is confirmed by real
  execution; the path back to `$F961` is confirmed to go via `$FA23`, not the previously-assumed `$FA06`
  — a genuine correction to last cycle's own hypothesis, not just a confirmation of it. Two unconfirmed
  leads still open for future annotation: a RIOT I/O touch (`BIT $0282`) and a small lookup table at
  `$F910`. **Genuinely unresolved, disclosed**: whether `$F961` repeats as a per-frame loop — not observed
  in 4,000 trace steps; `py65` has no TIA/RIOT timing model, so this may not be answerable with this
  toolchain alone. Full annotation (rung 2, assigning meaning to routines) not yet attempted.

## Verified Disassemblies

_(none yet at the full "annotated + trace-verified" tier — the raw mechanical pass and a first real
control-flow trace both exist now (see Confirmed Findings above), but no routine has been annotated with
an interpreted meaning yet. An entry here requires both: trace evidence (now demonstrated achievable) and
a stated interpretation of what a routine actually does.)_

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
  should build on rather than duplicate? See SQ-2 and SQ-4.
