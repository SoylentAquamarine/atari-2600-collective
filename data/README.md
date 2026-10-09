# Data

Disassembly outputs, memory maps, trace logs, and reference documentation for the project.

## A standing rule, stated plainly

**No copyrighted Atari 2600 ROM binary is ever committed to this repository, under any circumstance.** Analysis targets are limited to public-domain/openly-licensed material or ROMs the user supplies locally for analysis that is never redistributed here. See `LICENSE` and `README.md`.

## Present

Nothing yet. See `config/sidequests.md` SQ-1 (toolchain setup and ROM-rights scoping) — a hard blocker for everything downstream.

## Needed

- **`toolchain-notes.md`** (SQ-1) — what disassembly/emulation/trace tooling actually works in this environment, with commands.
- **`rom-rights-scope.md`** (SQ-1) — the specific, verified list of legally analyzable targets.
- **`hardware-reference.md`** (SQ-2) — cited documentation for the 6507 CPU, the TIA chip, the RIOT chip, and common bank-switching schemes.
- **`prior-findings-catalog.md`** (SQ-4) — notable, already-public reverse-engineering findings, cited.
- **`disassembly/<rom-name>/`** (SQ-3 onward) — raw disassembly, annotated disassembly, and trace artifacts, one directory per analyzed ROM.

## Convention

Any reference file added here should note its source URL, retrieval date, and version where applicable. Any trace artifact should note the exact ROM checksum, commit, and command used to produce it, so it can be regenerated and checked by anyone.
