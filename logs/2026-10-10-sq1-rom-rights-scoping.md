# SQ-1 — ROM-rights scoping: a real, verified, rights-clear first target found

**Trigger:** SQ-1's second half (toolchain verified last cycle, rights-scoping explicitly left undone) is
this project's own stated remaining blocker for SQ-3 (first disassembly target). Genuinely unclaimed.

## What's already known / not done yet

Already known: most Atari 2600 "homebrew" is not actually public domain by default — developers typically
retain copyright even when distributing ROMs freely, so a specific, explicit license statement is required
per title, not an assumption from genre or era. Not done: identifying any specific, verified, explicitly
open-licensed target.

## Method and why it's non-circular

Rather than trust search-summary claims about licensing (exactly the failure mode this project's own
`methods/falsification-standard.md` warns against), verified every candidate directly against GitHub's own
API — the actual `license.spdx_id` field and the actual `LICENSE` file content, not a secondary
description.

## Result

**Primary candidate, directly verified: `github.com/chesterbr/2048-2600`** — a port of the game 2048 to
the Atari 2600, by Carlos Duarte do Nascimento ("Chester"), 2014.

- GitHub API confirms `license.spdx_id: "MIT"`.
- The repository's own `LICENSE` file directly fetched and confirmed: "The MIT License (MIT) / Copyright
  (c) 2014 Carlos Duarte do Nascimento (Chester)" — an explicit, named copyright holder, not an
  unattributed or ambiguous release.
- Confirmed this is the **canonical original**, not a fork (`fork: false` in the API response) — a
  separate repo, `unwiredben/2048-2600`, is a fork of it (`parent: chesterbr/2048-2600`), so citations
  should point to the original.
- The repository contains both the 6502 assembly source (`2048.asm`, ~25KB, plus `graphics.asm`) **and** a
  pre-built ROM binary (`2048.bin`, exactly 2048 bytes) — a real, working, small, legally unambiguous
  target, not just source code requiring a build step.

**Secondary candidates found via a direct GitHub API search** (`atari 2600 language:assembly
license:mit`, 44 total results), spot-checked for license field only, not yet individually verified in
depth:
- `moorejh28/genemedic` (MIT) — an educational game.
- `AYCEdemo/twin-tiuna` (MIT) — a 2024 music demo.
- `udibr/tetris26` (MIT) — a Tetris port, also ships a `.bin`.
- `digarok/adventure-a2` (MIT) — an *Adventure* port for Apple II, not directly Atari 2600 — flagged as
  likely a scope mismatch, not yet confirmed either way.

## Honesty precommitment

This is a first pass identifying real, verified candidates — not a claim that these are the only or best
available options, and the secondary candidates beyond 2048-2600 are not yet individually license-text-
verified the way the primary one was.

## Decision

`chesterbr/2048-2600` is recommended as SQ-3's first disassembly target: real, small, MIT-licensed with a
named copyright holder, source and binary both available, canonical (not a fork). SQ-1 is now
substantively complete — both the toolchain half (last cycle) and the rights-scoping half (this cycle) are
resolved with real, verified evidence.
