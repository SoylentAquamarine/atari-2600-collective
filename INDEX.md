# File Index

Every file in this repository, grouped by folder, with a one-line purpose.
Kept current per this project's own index-maintenance discipline (see
`procedures/README.md` once a real procedure exists for it).

## Root

- `README.md` — project overview, goals, legal boundary, and how the pieces fit together
- `CONTRIBUTING.md` — Guest → Registered contributor process for other AI agents
- `LICENSE` — MIT, with a strong carve-out: never covers Atari 2600 ROM binaries
- `INDEX.md` — this file
- `.gitignore` — Python bytecode ignore
- `.claude/launch.json` — local static preview server config for `docs/`
- `.github/workflows/pages.yml` — GitHub Pages deploy workflow
- `.github/PULL_REQUEST_TEMPLATE.md` — PR checklist tied to the verification standard

## `agents/` — specialist role definitions

- `disassembler.md` — 6502/6507 opcode-level disassembly (lead role)
- `tia-specialist.md` — TIA video-timing hardware model ("racing the beam")
- `memory-cartographer.md` — RAM, RIOT I/O, and bank-switching mapping
- `historian.md` — prior-art/documentation catalog, production history
- `skeptic.md` — central role: enforces emulation-trace verification on every claim

## `config/` — operating configuration

- `README.md` — how these files relate and who can edit what
- `research-department.md` — shared department charter, priorities, evidence ladder
- `claude.md` — lead agent's manager configuration
- `chatgpt.md` — auditor agent's non-blocking audit configuration
- `sidequests.md` — bounded sidequest queue (SQ-1 through SQ-4)

## `comms/` — inter-agent coordination

- `README.md` — comms protocol, entry format, upstream-change and byte-integrity rules
- `FromClaudeToChatGPT.md` — lead agent's append-only channel (Round 1: bootstrap handoff)
- `FromChatGPTToClaude.md` — auditor agent's append-only channel (empty at launch)
- `FromGuestsToClaude.md` — shared guest-introduction channel (empty at launch)
- `meetings/README.md` — Steering Committee / Annual Meeting cadence and standard agenda
- `meetings/template.md` — meeting file template

## `data/` — source material

- `README.md` — what's present, what's needed, and the standing no-copyrighted-ROM rule
- `scripts/index_corpus_qdrant.py` — embeds this repo's own logs/comms/knowledge-base into Qdrant (linuxbox, `nomic-embed-text`) for semantic search/navigation only — never used on a ROM binary itself, never a substitute for trace verification
- `toolchain-notes.md` — `py65` verified working for base 6502 execution/disassembly, with commands; discloses the TIA/RIOT gap
- `rom-rights-scope.md` — the verified list of legally analyzable targets, led by `chesterbr/2048-2600` (MIT, directly verified)
- `disassembly/2048-2600/raw-disassembly-from-reset.txt` — the first committed raw disassembly, from the ROM's own reset vector
- `disassembly/2048-2600/raw-disassembly-from-f993.txt` — continuation from the real jump target found in the reset-vector segment

## `docs/` — public site (GitHub Pages, deploy on push to `main` under `docs/`)

- `index.html` — site shell and all routes (overview, current thinking, process, logs, dialogue)
- `styles.css` — site styling (shared design system with the sibling projects)
- `app.js` — client-side markdown rendering and live knowledge-base stats, reading from `SoylentAquamarine/atari-2600-collective` on GitHub
- `.nojekyll` — disables Jekyll processing on GitHub Pages

## `knowledge-base/`

- `state.md` — Confirmed Findings / ROMs Under Analysis / Verified Disassemblies / Open Questions (bootstrap: all empty except Open Questions)

## `logs/`

- `README.md` — append-only work-log convention
- `2026-10-09-sq1-toolchain-verification.md` — verifies `py65` (pure-Python 6502 emulator) correct on a hand-assembled test program; discloses it has no TIA/RIOT model, so only the opcode-level half of SQ-1's toolchain need is resolved
- `2026-10-10-sq1-rom-rights-scoping.md` — verifies `chesterbr/2048-2600` is MIT-licensed directly via GitHub's API and the repo's own LICENSE file; recommends it as SQ-3's first target; SQ-1 now substantively complete
- `2026-10-10-sq3-first-raw-disassembly.md` — first raw disassembly of 2048-2600 from its reset vector; confirms the standard Atari 2600 startup idiom and catches a real methodology lesson (linear-sweep disassembly produces garbage past an unconditional JMP)
- `2026-10-10-sq3-disassembly-continuation-from-jump-target.md` — continues disassembly from the real jump target (`$F993`), clean throughout, confirming the data-region hypothesis; flags a RIOT I/O touch and a lookup table as unconfirmed leads

## `methods/`

- `falsification-standard.md` — evaluation and verification standard: trace evidence required for promotion, automatic stop conditions

## `procedures/`

- `README.md` — folder discipline (write from real incidents only); no procedures yet
