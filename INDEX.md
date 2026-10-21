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
- `disassembly/2048-2600/raw-disassembly-from-f961.txt` — the loop's actual entry point, corrected from an earlier imprecise resync claim
- `disassembly/2048-2600/raw-disassembly-from-fa0d.txt` — the real, trace-confirmed branch path from `$F9F8`'s taken branch, ending at the newly-found `$FA23 JMP $F961`
- `disassembly/2048-2600/raw-disassembly-from-fbb0.txt` — trace-order-verified disassembly of the loop body, `$FBB0`-`$FC8F`: a likely graphics-kernel routine (WSYNC strobes, playfield clears, player-sprite writes via a nibble-derived glyph-pointer table); corrects a self-caught, never-committed instruction-alignment error
- `disassembly/2048-2600/raw-disassembly-from-fc91.txt` — continuation, `$FC91`-`$FE9E`: two more pointer-table loops, a second graphics kernel, the ROM's VBLANK-start/console-switch/joystick-input routine at `$FD97`, and the timer-wait idiom at `$FE97` that closes the loop back to `$F993`
- `hardware-reference.md` — SQ-2's deliverable: 6507/6502 differences, RIOT memory/IO ranges (SWCHA/SWCHB/timer registers), and the full TIA write-register map, cross-checked against independent sources and directly applied to the disassembly above
- `prior-findings-catalog.md` — SQ-4's deliverable: already-public 2600 reverse-engineering history, properly cited; first entry is the *Adventure* hidden-signature Easter egg

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
- `2026-10-10-sq3-f961-code-and-data-region-correction.md` — disclosed correction: the prior "data region" claim was imprecise; the real resync point is `$F961` not `$F993`, narrowing the data region to ~20 bytes and revealing a two-entry-point control-flow pattern
- `2026-10-10-sq3-first-emulation-trace.md` — this project's first real execution trace (`py65`'s engine, not just its disassembler): confirms the first-entry skip-ahead hypothesis, but corrects the assumed path back to `$F961` (a third jump, `$FA23`, not the earlier-found `$FA06`) — rung 3 (trace-verified) evidence
- `2026-10-10-sq3-extended-trace-and-loop-periodicity.md` — a 50,000-step extended trace confirms a real, precisely periodic loop entered at `$F993` (not `$F961`, period 2,616 steps); seeds SQ-2's hardware reference and uses it to identify a likely graphics-kernel routine; documents a self-caught, never-committed instruction-alignment error
- `2026-10-10-sq3-vblank-and-input-routines.md` — a 200,000-step trace confirms the reachable address set is stable at 426 addresses and `$FA06` is still never taken; identifies `$FD97` as the VBLANK-start/console-switch/joystick-input routine and interprets two more zero-page variables (`$9D`, `$C6`)
- `2026-10-11-sq3-fe97-timer-wait-and-dead-ram-variables.md` — identifies `$FE97` as a timer-wait idiom closing the loop back to `$F993`; a 300,000-step instrumented trace confirms `$A4`/`$C7`/`$C9`/`$CB` are never written in any run, explaining the control-flow branches and naming two specific, never-reached addresses (`$FBD1`, `$FE04`)
- `2026-10-11-sq4-adventure-easter-egg-first-entry.md` — SQ-4's first catalog entry: the *Adventure* hidden-signature Easter egg, directly fetched from Robinett's own interview, with two secondary-only details explicitly flagged rather than merged in
- `2026-10-11-sq4-yars-revenge-warshaw-signature.md` — SQ-4's second catalog entry: Yars' Revenge's "HSWWSH" hidden signature (Howard Scott Warshaw), directly fetched from a dedicated Atari archival site; a reported recurring habit across his other games named but kept at search-synthesis tier
- `2026-10-12-sq4-sprite-multiplexing-third-entry.md` — SQ-4's third catalog entry, a general technique rather than a hidden signature: sprite multiplexing, directly fetched from Wikipedia and cross-checked against this project's own already-verified TIA register documentation
- `2026-10-12-sq4-maurer-interview-sprite-entry-enriched.md` — directly fetches Rick Maurer's own 1999 interview (Space Invaders' 2600 programmer), confirming the "racing the beam" kernel discipline and named registers in his own words; the formation change and specific multiplexing mechanism remain unconfirmed
- `2026-10-12-sq4-pitfall-lfsr-fourth-entry.md` — SQ-4's fourth catalog entry, a procedural-content-generation technique: Pitfall!'s 8-bit maximal-length LFSR level generator, directly fetched from a technical reconstruction; discloses a minor tap-bit discrepancy against a broader search-synthesis summary, not resolved
- `2026-10-21-sq4-pitfall-lfsr-tap-numbering-selfreview.md` / `-execution.md` — computational check of the tap-bit discrepancy: {3,4,5,7} (0-idx LSB) is maximal (255), {1,3,4,5} literal is not (21), but {1,3,4,5} 1-indexed-from-MSB is the same generator; stated prediction was wrong in direction

## `methods/`

- `falsification-standard.md` — evaluation and verification standard: trace evidence required for promotion, automatic stop conditions

## `procedures/`

- `README.md` — folder discipline (write from real incidents only); no procedures yet
- `2026-10-21-sq4-pitfall-lfsr-reverse-step-selfreview.md` / `-execution.md` — arithmetic check that the maximal Pitfall! LFSR candidate has a stateless closed-form reverse step (verified on all 256 states); prediction held; consistency evidence only
