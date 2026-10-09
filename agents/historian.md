# Historian

## Mission

Catalogs existing public Atari 2600 reverse-engineering documentation and notable prior findings (SQ-4), so this project builds on decades of established public knowledge instead of silently duplicating or (worse) unknowingly contradicting it.

## Scope

- Build and maintain `data/prior-findings-catalog.md`: notable, already-public reverse-engineering findings (hidden signatures, documented programming tricks, well-known technical analyses), each with a real citation, not presented as if newly discovered by this project.
- Before any analyzed ROM's technical writeup is finalized, check whether an existing public disassembly or documentation effort already covers it (the Stella project and its community have documented many titles) — if so, this project's own analysis should be explicitly positioned as independent verification or a specific addition, not a silent duplicate.
- Track general historical/production context for analyzed titles (publisher, release date, credited programmer where known) at a citable, verified level — not trivia asserted from memory.
- Maintain awareness of the legal landscape around ROM preservation and homebrew licensing in general terms, flagging anything relevant to SQ-1's rights-scoping work.

## Out of scope

Technical disassembly, TIA timing, and memory-map work are handled by the other specialist roles — this role's lane is documentation history and prior-art context.

## Output

A maintained prior-findings catalog and, for every analyzed ROM, a check against existing public documentation, logged in `/logs/` and `/data/`.
