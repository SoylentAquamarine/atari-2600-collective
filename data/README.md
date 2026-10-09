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

## Tooling

- **`scripts/index_corpus_qdrant.py`** — embeds this repo's own `logs/`,
  `comms/`, `knowledge-base/state.md`, and `methods/` into a Qdrant vector
  collection (`atari-2600-collective`) via the linuxbox's `nomic-embed-text`
  model, for semantic search/navigation over this project's own prior
  work. Within the compute policy's authorized scope
  (`config/research-department.md`): a navigation aid only, never a
  substitute for Claude/ChatGPT's own verification/trace review, and never
  used to analyze or embed a ROM binary itself. Re-run after any
  substantive comms/logs/knowledge-base update to keep the index current —
  it fully rebuilds the collection each run.

## Convention

Any reference file added here should note its source URL, retrieval date, and version where applicable. Any trace artifact should note the exact ROM checksum, commit, and command used to produce it, so it can be regenerated and checked by anyone.
