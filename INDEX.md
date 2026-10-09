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

## `docs/` — public site (GitHub Pages, deploy on push to `main` under `docs/`)

- `index.html` — site shell and all routes (overview, current thinking, process, logs, dialogue)
- `styles.css` — site styling (shared design system with the sibling projects)
- `app.js` — client-side markdown rendering and live knowledge-base stats, reading from `SoylentAquamarine/atari-2600-collective` on GitHub
- `.nojekyll` — disables Jekyll processing on GitHub Pages

## `knowledge-base/`

- `state.md` — Confirmed Findings / ROMs Under Analysis / Verified Disassemblies / Open Questions (bootstrap: all empty except Open Questions)

## `logs/`

- `README.md` — append-only work-log convention

## `methods/`

- `falsification-standard.md` — evaluation and verification standard: trace evidence required for promotion, automatic stop conditions

## `procedures/`

- `README.md` — folder discipline (write from real incidents only); no procedures yet
