# SQ-3 — $FE97 identified as a timer-wait idiom; four zero-page variables confirmed permanently unwritten

**Trigger:** last cycle's own named leads — `$FE97` undisassembled, and `$A4`/`$C7`/`$C9`/`$CB` not yet
interpreted.

## What's already known / not done yet

Already known: `$FD97` is the VBLANK-start routine, which sets up a hardware timer (TIM64T) from a
console-switch-selected value. `$A8` is a game-state variable compared against fixed values, and `$0C` is
read but never written. Not done: disassembling `$FE97` itself, or checking whether `$A4`/`$C7`/`$C9`/`$CB`
are ever actually used.

## Design and why it's non-circular

Extended the trace to 300,000 steps (1.5x the prior cycle's length) and instrumented it to log every value
change to the four remaining zero-page variables across the whole run, not just their presence in
disassembled text — a direct, stronger check than inferring behavior from static code alone.

## Honesty precommitment

Report exactly what changes (or doesn't) rather than assuming a variable is "dead code" just because it
wasn't written in one run.

## Result 1 — $FE97 is a timer-wait idiom closing the loop

`$FE97: LDA $0284; BNE $fe97; STA $02; JMP $f993`. `$0284` is **INTIM**, the hardware timer's own
countdown-read register (per `data/hardware-reference.md`, seeded two cycles ago). This is a tight polling
loop — spin until the timer set up in the VBLANK routine (`$FD97`'s TIM64T write) reaches zero — then one
more WSYNC strobe, then jump back to `$F993`, the main loop's own entry point. This closes the loop
structure completely: render board → advance cell index → (on the triggering pass) VBLANK-start → set
timer from console switch → read joystick (gated by game state) → **wait for the timer, then restart**.

## Result 2 — a real, honest limitation: four variables are never written, not just "not yet interpreted"

Instrumented every write to `$A4`, `$C7`, `$C9`, `$CB` across the full 300,000-step trace: **none of them
change even once** — all stay at `py65`'s zero-initialized RAM default for the entire run. This isn't a
gap in this project's reading of the code; it's a direct empirical fact about this specific trace. Checked
what this implies for control flow: the branches gated on these variables being zero (`$C9==0` at `$FBCF`,
`$A4==0` at `$FBE6`, `$A8==4` at `$FDFD`→`$FE04`) are the **only** branches ever taken, because the
alternative condition (nonzero) never occurs under `py65`'s no-TIA/RIOT-input conditions — the same
disclosed toolchain limitation already on file, now demonstrated concretely for four more variables at
once rather than asserted in the abstract.

**A genuine new lead this surfaces**: the not-taken branch at `$FBCF` (`BEQ $fbd6`, taken because `$C9==0`)
has a fall-through target at `$FBD1` that **has never been disassembled or executed in any trace this
project has run** — real, unexplored code exists there, reachable only if something (plausibly a real
joystick/input event) ever sets `$C9` nonzero. Same situation for `$FE04` (the `$A8==4` target, also never
reached). Both are concrete, specific addresses for a future cycle, not vague "more input would help."

## Decision

Promoting to `knowledge-base/state.md`: `$FE97`'s role (rung 3, register-identity-verified) and the
four-variable dead-write finding (rung 3, directly instrumented). This project's picture of the main loop
is now complete end-to-end for the one control-flow path `py65` can actually exercise. The two newly-named
unexplored addresses (`$FBD1`, `$FE04`) are this project's clearest remaining leads — both are structurally
blocked the same way (gated on hardware input `py65` cannot supply), so reaching them would need either a
TIA/RIOT-capable emulator or direct, careful manual memory-poking to force the branch, not more passive
tracing.
