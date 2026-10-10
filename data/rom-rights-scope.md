# ROM-rights scope

The specific, verified list of legally analyzable targets for this project. See
`logs/2026-10-10-sq1-rom-rights-scoping.md` for method. **No ROM binary is committed to this repository**
— this file records citations and verification notes only; any local copy for analysis stays local per
`README.md`'s standing rule.

## Verified, recommended first target

**`github.com/chesterbr/2048-2600`** — a port of 2048 to the Atari 2600, by Carlos Duarte do Nascimento
("Chester"), 2014. MIT License, confirmed directly via GitHub's API `license.spdx_id` field and the
repository's own `LICENSE` file text (named copyright holder, not unattributed). Canonical original,
confirmed not a fork. Contains both 6502 assembly source (`2048.asm`, `graphics.asm`) and a pre-built ROM
(`2048.bin`, 2048 bytes).

## Found, not yet individually verified in depth (license field only, via GitHub API search)

- `github.com/moorejh28/genemedic` — MIT.
- `github.com/AYCEdemo/twin-tiuna` — MIT.
- `github.com/udibr/tetris26` — MIT, ships a `.bin`.
- `github.com/digarok/adventure-a2` — MIT, but may be Apple II rather than Atari 2600 — needs a scope
  check before treating as a candidate.

## Standing rule

Per `README.md` and `LICENSE`: only public-domain/openly-licensed material (like the above, each with its
license verified directly, not assumed), or ROMs the user supplies locally for analysis that is never
committed here. Most Atari 2600 "homebrew" is **not** public domain by default — developers typically
retain copyright even on freely-distributed ROMs — so every candidate needs its own explicit, verified
license statement, not a genre-based assumption.
