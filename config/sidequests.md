# Sidequest Queue

Bounded, independently valuable pieces of work that advance the project without requiring a full ROM analysis to be walked start-to-finish. Each sidequest names its purpose, scope, deliverables, and current status.

## SQ-1 — Toolchain setup and ROM-rights scoping (blocking, start here)

**Purpose:** before any disassembly work can start, this project needs (a) a working, reproducible way to disassemble 6502/6507 machine code and verify claims against actual emulated behavior in this environment, and (b) a clear, conservative scope for which specific ROMs are legally analyzable.

**Scope:**
- Evaluate available 6502-family disassembly and emulation options runnable in this session's environment (e.g. a pure-Python 6502 core such as `py65`, or another reproducible approach) — note explicitly that general 6502 emulation does not include the Atari 2600's own TIA/RIOT hardware behavior, which is a separate, harder piece (see SQ-2's hardware-reference research for what's needed to model it correctly).
- Document exactly what "trace-verified" will mean in practice for this project: what gets logged (register state, memory read/writes, cycle counts) and in what committed format, so every future claim can point to a reproducible trace artifact.
- Scope the legally analyzable target list: identify specific public-domain or openly-licensed homebrew ROMs (the modern homebrew scene publishes some under explicit open terms — verify any specific claim before treating it as settled, not from memory) as realistic first targets, separate from any ROM the user might supply locally for analysis.
- Write the standing rule plainly into `data/README.md`: no copyrighted ROM binary is ever committed to this repository.

**Deliverables:** `data/toolchain-notes.md` (what works in this environment and what doesn't, with commands) and `data/rom-rights-scope.md` (the specific, verified list of legally analyzable targets).

**Status:** not started. This is the first task for whichever agent picks up this project.

## SQ-2 — Reference documentation catalog

**Purpose:** the Atari 2600 reverse-engineering community has decades of public, well-documented work (the Stella emulator project's own source and documentation, 6502.org, AtariAge's development forums, Montfort & Bogost's *Racing the Beam*, and various hardware reference manuals). This project should build on that, not silently rediscover it.

**Scope:**
- Catalog the key existing public references for the 6507 CPU (the cost-reduced 6502 variant the 2600 uses — verify its specific differences, e.g. address-bus width, directly rather than assuming), the TIA (Television Interface Adaptor) video/audio chip, and the RIOT (RAM-I/O-Timer) chip, with citations.
- Catalog the "racing the beam" programming model specifically — why Atari 2600 games have no frame buffer and must write to TIA registers in sync with the television's own electron beam position, since this is the single most important and most unusual piece of context for reading any 2600 disassembly correctly.
- Catalog known common cartridge bank-switching schemes (for ROMs larger than the base addressable space) at a reference level, even before any specific analyzed ROM needs one.

**Deliverables:** `data/hardware-reference.md` — a cited reference document the Disassembler and other roles use throughout, not a one-time research note.

**Status:** not started. Can begin in parallel with SQ-1.

## SQ-3 — First target selection and initial disassembly

**Purpose:** pick one small, rights-cleared ROM as this project's first full analysis target and produce its first verified disassembly pass.

**Scope:** using SQ-1's rights-scoped target list, select one ROM (most Atari 2600 ROMs are extremely small — commonly 2–4 KB before bank-switching — which makes a full disassembly genuinely tractable, unlike the sibling projects' large undeciphered corpora). Produce a raw mechanical disassembly first, then begin annotating, with every non-trivial annotation backed by a committed trace per SQ-1's trace format.

**Deliverables:** `data/disassembly/<rom-name>/` — raw disassembly, annotated disassembly, and trace artifacts for the first analyzed ROM.

**Status:** not started — blocked on SQ-1 (toolchain and rights scope) and benefits from SQ-2 (hardware reference) being underway.

## SQ-4 — Prior-art and notable-finding catalog

**Purpose:** directly modeled on the sibling Oak Island and Phaistos Disc projects' own prior-claims catalogs. Document notable, already-public Atari 2600 reverse-engineering findings — famous undocumented features, hidden signatures, and well-known programming tricks — as calibration and context, properly cited rather than re-presented as new discoveries.

**Scope:** research and catalog known cases such as (verify each independently before treating as settled): the hidden programmer signature in *Adventure* (widely credited as one of the first video game "Easter eggs," attributed to programmer Warren Robinett), and other well-documented examples of notable 2600 programming techniques or hidden content from the historical record.

**Deliverables:** `data/prior-findings-catalog.md`.

**Status:** not started. A reasonable parallel task alongside SQ-1/SQ-2, since it doesn't require a working toolchain to begin.

## Initial priority

Start SQ-1 first — it is a hard blocker for all actual disassembly work, since no claim can be verified without a working trace toolchain, and no ROM should be analyzed before its rights status is scoped. SQ-2 (hardware reference) and SQ-4 (prior-art catalog) can run in parallel, since neither depends on SQ-1 being finished. Do not start SQ-3 (first target disassembly) until SQ-1's toolchain is actually demonstrated working and the target ROM's rights status is confirmed clear.
