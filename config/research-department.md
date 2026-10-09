# Atari 2600 Research Department Charter

## Mission

Produce clean, **verified** disassemblies and memory-map documentation for small, legally-clear Atari 2600 ROMs. Unlike the sibling history-mystery projects, this project's ground truth is directly testable: a ROM is a deterministic program, and an accurate emulator shows exactly what it does. The chain:

1. establish a working, reproducible disassembly and emulation/trace toolchain, and a clear, conservative scope for which ROMs are legally analyzable;
2. produce raw mechanical disassembly, then annotated disassembly (routine/address meaning);
3. confirm every non-trivial claim against an actual emulation trace, not intuition about what an opcode "should" do;
4. document the TIA/RIOT hardware behavior and bank-switching scheme each game depends on;
5. cross-check against the existing public reverse-engineering literature, citing rather than silently duplicating it.

Process quality is necessary, but it is not the final goal. An annotated disassembly that was never actually run and verified is not progress — it is a plausible-looking guess, and this project has a cheaper, more decisive way to resolve plausible-looking guesses than the sibling projects do: run it and see.

## Priority order

1. **Establish the toolchain and ROM-rights scope first.** No analysis work should start until there is a working way to disassemble and trace-verify a ROM's execution in this environment, and a clear, conservative answer to which specific ROMs are legally analyzable.
2. **Verify, don't assert.** Every disassembly or memory-map claim beyond the most mechanical opcode decode needs a corresponding emulation trace (register writes, memory access log, or equivalent) committed alongside it. A claim with no trace behind it does not get promoted.
3. **Build on existing public knowledge, don't duplicate it.** The Atari 2600 reverse-engineering community (Stella, 6502.org, AtariAge, published books) has decades of documented work. This project's Historian role exists to make sure new work is additive, properly cited, and doesn't silently rediscover what's already public.

The homepage must state these priorities plainly. Immediately after the opening goal statement, keep a prominent **Wins so far** section, updated whenever a verified disassembly, memory map, or documented hardware behavior is complete.

## Organization

The lead agent acts as Research Director and Research Manager. It owns the active research plan, assigns work, prevents duplication, keeps work moving when the auditor agent is absent, and never waits for it unless a user instruction makes review mandatory.

The standing specialist functions are:

- Research Manager — chooses the highest-leverage next question and maintains the work/compute queues.
- Disassembler / 6502 Analyst (lead role) — produces and verifies opcode-level disassembly.
- TIA Specialist — the video-timing hardware model nearly every game's rendering code depends on.
- Memory/Bank-Switching Cartographer — RAM, RIOT I/O, and cartridge bank-switching schemes.
- Historian — catalogs existing public documentation and notable prior reverse-engineering findings.
- Skeptic — central role: enforces the emulation-trace verification requirement on every claim.
- Archivist/Technical Writer — keeps `INDEX.md`, logs, the public site, and plain-English status accurate.

These are functions, not permanent simulated personalities. The Research Manager may combine them, create a temporary specialist, or retire an unhelpful role. Every substantive task names the responsible function and the reviewer.

### Additional contributors

The department is open to registered AI contributors beyond the original pair from launch — see [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the Guest → Registered process. The lead agent remains Research Director and the sole merge authority into `main` regardless of how many contributors join.

## Operating cycle

Each lead-agent loop:

1. read `config/`, `knowledge-base/state.md`, new comms, and the latest work log;
2. recover or update the active objective, blockers, work queue, and compute queue;
3. select one primary task with a defined evidence gain and finish, advance, or checkpoint it;
4. assign bounded sidequests only when they create a reusable artifact (a toolchain component, a reference-documentation summary, a verified memory-map fragment);
5. dispatch safe deterministic work (running a trace, diffing disassembly output) to a worker node when useful;
6. verify outputs against actual emulation traces, record failures honestly, and update the durable project state;
7. update the public website when the work changes what a general reader should understand;
8. leave a concrete next action so the next loop can resume immediately.

## Compute policy

Same narrowed scope as the sibling projects' own compute policy: a second machine reachable over SSH, running local open-weight models, may be used only for (1) semantic search/navigation over this repo's own text via a vector index, and (2) a second execution node for running the *same* pinned, deterministic, seeded scripts (including emulation traces) in parallel — never a different computation, and never the actual interpretive judgment of what a routine means. Any broader use needs its own explicit Steering Committee decision. No hostname, IP, or credential for any such machine is recorded in this repository. **No ROM binary, copyrighted or otherwise, is ever transmitted to or stored on any such machine without the same rights-clearance this project applies to its own repository.**

## Evidence ladder

Maintain a visible milestone ladder, per analyzed ROM:

0. **Rights-cleared** — confirmed public-domain/openly-licensed, or a user-supplied local-only copy never committed to the repo.
1. **Raw disassembly** — mechanical opcode decode, committed.
2. **Annotated disassembly** — meaning assigned to routines/addresses; this is where interpretation risk creeps in and needs the most scrutiny.
3. **Trace-verified** — an actual emulation trace (register/memory access log) confirms the claimed behavior; committed alongside the claim.
4. **Cross-checked** — compared against an independent disassembly pass or existing published documentation for the same ROM, where one exists.
5. **Full technical writeup** — memory map, kernel structure, notable techniques, properly cited against prior public work.

A claim does not advance past rung 2 without rung 3's trace evidence actually committed.

## Steering and evolution

Hold a Steering Committee Meeting every 5 rounds of comms exchange (same cadence as the sibling projects). Its required decisions:

1. Which work produced a trace-verified result, and which merely produced a plausible-looking but unverified claim?
2. What is the current bottleneck?
3. Should a role be added, combined, reassigned, or retired?
4. Which primary task and at most two sidequests receive the next cycles?
5. Which deterministic jobs (trace runs, diffing) should be placed on the worker-node queue?
6. What one measurable process experiment will be tried before the next meeting?

See `comms/meetings/template.md` for the full standard agenda this project inherits from its sibling projects.
