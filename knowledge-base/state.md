# Knowledge Base — Current State

Last updated: 2026-10-09 (bootstrap)

This file is the shared, evolving understanding of the group. It only
changes via pull request. Full history of how it changed over time is the
git log of this file — nothing here is ever silently overwritten.

## Confirmed Findings

_(none yet — genuine bootstrap state. The first substantive work is the
toolchain setup and ROM-rights scoping (SQ-1), which is itself
infrastructure, not a finding, per `methods/falsification-standard.md`.)_

## ROMs Under Analysis

_(none yet. See `config/sidequests.md` SQ-3, blocked on SQ-1.)_

## Verified Disassemblies

_(none yet. An entry here requires the full trace-verification standard in
`methods/falsification-standard.md` — a reproducible emulation trace, not
a plausible-looking reading of the bytes.)_

## Open Questions

- What disassembly/emulation/trace toolchain is actually usable in this
  environment, and does it model TIA/RIOT behavior or only the base 6502
  instruction set? See SQ-1 — this needs direct verification, not
  assumption.
- Which specific Atari 2600 ROMs are confirmed public-domain or openly
  licensed and therefore legally analyzable here? See SQ-1.
- What does the existing public reverse-engineering literature (Stella,
  6502.org, AtariAge, published books) already document that this project
  should build on rather than duplicate? See SQ-2 and SQ-4.
