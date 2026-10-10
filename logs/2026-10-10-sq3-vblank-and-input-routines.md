# SQ-3 — VBLANK start sequence and joystick input identified; state space confirmed stable

**Trigger:** two cycles ago, extending the trace surfaced `$FD97` (reached via `$FC64`'s `JMP $fd97` on a
later pass) and several not-yet-interpreted zero-page variables (`$9D`, `$C6`, `$C7`, `$C9`, `$CB`, `$A4`)
as open leads. This cycle follows up directly.

## What's already known / not done yet

Already known: a likely graphics kernel at `$FBB0`-`$FC8F` drawing the board via GRP0/GRP1, a real
2,616-step loop period, and `$FA06` never taken in a 50,000-step trace. Not done: disassembling `$FD97`
itself, or interpreting any of the newly-found zero-page variables.

## Design and why it's non-circular

Extended the trace to 200,000 steps (4x longer than last cycle) specifically to check two things: whether
`$FA06` is reached given more time, and whether the reachable address set keeps growing or has stabilized.
Disassembled the newly-reached `$FC91`-`$FE01` region in trace-execution order (not a static linear sweep —
applying the lesson from the alignment error two cycles ago). Register identities were checked against
freshly-searched RIOT documentation before being asserted, not recalled from memory.

## Honesty precommitment

Report the state-space and `$FA06` results exactly as measured, and flag the "11x multiplier may index an
11-entry glyph table" interpretation as a motivated hypothesis, not a confirmed fact — 2048's 11 distinct
tile values is a suggestive coincidence, not something this trace can verify without seeing actual glyph
data content.

## Result 1 — the reachable state space is confirmed stable, $FA06 still never taken

The trace's unique-visited-address count is **exactly 426 at step 50,000 and does not grow through step
200,000** — the code's reachable control flow under `py65`'s deterministic, no-input conditions has been
fully explored; no amount of further stepping alone will surface new paths. `$FA06` remains **never
visited** across the full 200,000 steps, a 4x-stronger confirmation of last cycle's finding. Any path
through `$FA06` almost certainly requires an input condition `py65` cannot supply (no TIA/RIOT model),
consistent with this project's standing disclosed toolchain limitation.

## Result 2 — two more pointer-table-building loops and a second graphics kernel

`$FC91`-`$FD30` builds **two more pointer tables** from board-cell values read out of RIOT RAM (`$80,X`,
indexed by `$9D`, the board-cell counter): one with a `value*11` stride (plausibly indexing an 11-entry
glyph table — 2048 has exactly 11 distinct tile values, 2 through 2048 — flagged as a motivated, unverified
hypothesis), the other with a `value*16 (+8 if nonzero)` stride into a *different* table at `$BC`. `$FD32`-
`$FD6A` is a second graphics-kernel loop (10 scanlines, same GRP0/GRP1-via-pointer-table pattern as the
first kernel), using a genuine Atari 2600 register-economy trick — `TSX`/`STX`/`TXS` moving values through
the stack pointer as an extra temporary register. `$FD78`-`$FD94` advances to the next board cell (sentinel
`$7F` signals the pass is done), increments `$C6` (confirming it's a per-pass loop counter, as suspected
last cycle), and jumps back to `$FB72` — the main loop's own entry.

## Result 3 — $FD97 is the VBLANK-start / frame-boundary handler

`$FD97` is a **separate entry point**, reached only via `$FC64`'s jump on a later pass, not by falling
through from the code above it. It opens with 36 `WSYNC` strobes (close to NTSC's real ~37-scanline VBLANK
duration), then writes `$42` to `VBLANK` ($01) — bit 1 (start vertical blank) and bit 6 (latch input ports)
both set. This is as clean an identification as static analysis allows: **this is the game's VBLANK-start
routine**.

Immediately after: a `BIT $0282` (SWCHB, console switches) test selects one of two entries from a 2-byte
table at `$F912` (ROM), writing the chosen value to **TIM64T** ($0296) — starting the hardware timer with a
64-cycle prescaler, value chosen by a console switch (plausibly the difficulty switch, controlling
animation/input pacing). Then `LDA $0280` reads **SWCHA** (the joystick port) directly, masks to one
joystick's 4 direction bits, and only acts on the reading inside specific `$A8` game-state checks (`$A8==2`,
`$A8==4`) — `$F0` (all four bits high) is the standard "no direction pressed" idiom. This directly confirms
`$A8` functions as a discrete game/animation-state variable gating when joystick input is even read, exactly
consistent with its earlier-observed behavior (written only twice in 50,000 steps, compared against fixed
values like `7` at `$FBDC`).

New leads for a future cycle: `$FE97` (the next unread jump target) and the two-entry difficulty table at
`$F912`.

## Decision

Promoting to `knowledge-base/state.md`: the VBLANK-start identification and the SWCHA/game-state-gated input
reading, both rung-3 (trace-confirmed address, register-identity-verified) findings. The pointer-table
strides and the second graphics kernel are rung-2 (structurally well-evidenced interpretation). This
project now has a coherent picture of the ROM's main loop: render the board (two kernels, two scanline
passes) → advance/check board-cell index → on the pass where `$C6` triggers it, run VBLANK-start → read
switches/timer → read joystick input gated by game state → (unexplored: `$FE97` onward, presumably the
actual game-logic/move-handling code).
