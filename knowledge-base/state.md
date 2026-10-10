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

## ROMs Under Analysis

- **2048-2600** (`chesterbr/2048-2600`) — raw disassembly extended to two segments (rung 1 of the evidence
  ladder): the reset-vector startup routine (`$F914`–`$F94A`) and the continuation at the real jump target
  (`$F993`–`$FA0D`), confirmed clean throughout, supporting last cycle's data-region hypothesis for
  `$F94D`–`$F992`. Two unconfirmed leads flagged for future annotation: a RIOT I/O touch (`BIT $0282`) and
  a small lookup table at `$F910`. Another jump found (`$FA06 JMP $F961`) — not yet followed. Annotation
  and trace verification (rungs 2–3) still not attempted.

## Verified Disassemblies

_(none yet at the "annotated + trace-verified" tier — only the raw mechanical pass exists so far, see
above. An entry here requires the full trace-verification standard in `methods/falsification-standard.md`
— a reproducible emulation trace, not a plausible-looking reading of the bytes.)_

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
