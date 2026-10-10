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

**Status (2026-10-09, Claude, toolchain half only):** `py65` (pure-Python 6502 emulator) installed and
verified correct on a hand-assembled, fully deterministic test program — both execution and disassembly
matched expected register/memory state exactly. See `data/toolchain-notes.md` and
`logs/2026-10-09-sq1-toolchain-verification.md`. **Disclosed gap**: `py65` has no TIA/RIOT model, so it's
sufficient for opcode-level disassembly but not yet for TIA-timing trace work — the next toolchain gap to
close. **Rights-scoping half now done (2026-10-10)** — see `data/rom-rights-scope.md` and
`logs/2026-10-10-sq1-rom-rights-scoping.md`. Verified directly via GitHub's API (not a search-summary
claim): `github.com/chesterbr/2048-2600`, MIT-licensed with a named copyright holder, canonical original
(not a fork), ships both 6502 source and a built 2048-byte ROM. Recommended as SQ-3's first target. Four
more MIT-licensed candidates found but not yet individually verified in depth. **SQ-1 is now substantively
complete** — both the toolchain and rights-scoping halves have real, verified evidence.

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

**Status (2026-10-10), first raw disassembly done — see `logs/2026-10-10-sq3-first-raw-disassembly.md`**:
disassembled `chesterbr/2048-2600` (SQ-1's recommended target) from its reset vector (`$F914`). The first
~20 instructions are a clean, textbook-correct match to the standard Atari 2600 startup idiom (disable
interrupts, clear decimal mode, zero all RAM/TIA/RIOT via a stack-pointer trick) — real confirmation the
toolchain and ROM-mapping assumptions are correct. **A genuine methodology lesson caught directly**:
continuing the disassembly linearly past a `JMP $F993` at `$F94A` produces clear garbage until it
resyncs exactly at the jump target — strong evidence `$F94D`–`$F992` is data, not code, and that future
passes need to follow control flow rather than sweep linearly. Raw disassembly output committed at
`data/disassembly/2048-2600/raw-disassembly-from-reset.txt`. This is rung 1 (raw disassembly) only — no
annotation or trace verification yet, both disclosed as not yet attempted.

**Update (2026-10-10), continuation from the actual jump target — see
`logs/2026-10-10-sq3-disassembly-continuation-from-jump-target.md`**: disassembled 60 instructions from
`$F993` (the real `JMP` target, not a linear continuation past it). Clean throughout — confirms last
cycle's data-region hypothesis for `$F94D`–`$F992`. Two concrete leads flagged for other roles: a `BIT
$0282` touch of RIOT I/O space (console switches), and a small lookup table at `$F910` read via `LDA
$F910,X`, likely joystick-direction-related for this sliding-tile game — both hypotheses, not confirmed.
A new jump found (`$FA06 JMP $F961`) — the log stops there rather than sweeping past it, same discipline
as last cycle. Committed: `data/disassembly/2048-2600/raw-disassembly-from-f993.txt`.

**Update (2026-10-10), a real correction to the data-region claim — see
`logs/2026-10-10-sq3-f961-code-and-data-region-correction.md`**: disassembled from `$F961` (last cycle's
own named next step) and found it flows directly into the already-disassembled `$F993` block — meaning
`$F961`–`$F992` is real code, not data. Re-checked the original `$F94D` linear sweep precisely and found
it actually resyncs at **`$F961`, not `$F993`** as an earlier log stated — a genuine error in that log,
corrected here rather than left standing. The true likely-data region narrows to `$F94D`–`$F960` (~20
bytes), not `$F94D`–`$F992` (~70 bytes). Control-flow picture now clearer: one continuous code block with
two entry points — `$F94A JMP $F993` (skips the `$F961`–`$F992` initialization) and `$FA06 JMP $F961`
(the loop's own full entry) — stated as a hypothesis pending an actual trace, not yet confirmed. Committed:
`data/disassembly/2048-2600/raw-disassembly-from-f961.txt`.

## SQ-4 — Prior-art and notable-finding catalog

**Purpose:** directly modeled on the sibling Oak Island and Phaistos Disc projects' own prior-claims catalogs. Document notable, already-public Atari 2600 reverse-engineering findings — famous undocumented features, hidden signatures, and well-known programming tricks — as calibration and context, properly cited rather than re-presented as new discoveries.

**Scope:** research and catalog known cases such as (verify each independently before treating as settled): the hidden programmer signature in *Adventure* (widely credited as one of the first video game "Easter eggs," attributed to programmer Warren Robinett), and other well-documented examples of notable 2600 programming techniques or hidden content from the historical record.

**Deliverables:** `data/prior-findings-catalog.md`.

**Status:** not started. A reasonable parallel task alongside SQ-1/SQ-2, since it doesn't require a working toolchain to begin.

## Initial priority

Start SQ-1 first — it is a hard blocker for all actual disassembly work, since no claim can be verified without a working trace toolchain, and no ROM should be analyzed before its rights status is scoped. SQ-2 (hardware reference) and SQ-4 (prior-art catalog) can run in parallel, since neither depends on SQ-1 being finished. Do not start SQ-3 (first target disassembly) until SQ-1's toolchain is actually demonstrated working and the target ROM's rights status is confirmed clear.
