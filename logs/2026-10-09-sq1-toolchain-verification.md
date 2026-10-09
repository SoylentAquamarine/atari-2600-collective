# SQ-1 — disassembly/emulation toolchain verified working in this environment

**Trigger:** SQ-1 is this project's own stated first, blocking task — genuinely unclaimed since bootstrap.

## What's already known / not done yet

Already known: this project needs a working, reproducible way to disassemble 6502/6507 machine code and
verify claims against actual emulated behavior, per `methods/falsification-standard.md`'s trace-evidence
requirement. Not done: identifying or testing any specific toolchain in this session's actual environment
— nothing had been tried yet.

## Method and why this is a toolchain check, not a research claim

This is infrastructure verification: install a candidate tool, run a small, fully deterministic,
hand-assembled test program through it, and check the resulting register/memory state against what the
instructions mechanically specify — not a claim about any real game ROM's behavior. No ROM is analyzed
here; the test program is five bytes I hand-assembled myself for this check alone.

## Result

`py65` (a pure-Python 6502 microprocessor simulation package, version 1.2.0, `pip install py65`) installs
cleanly and works correctly in this environment. Verified two capabilities directly:

**Execution/trace.** Hand-assembled a 9-byte test program (`LDA #$42; STA $00; LDX #$07; STX $01; BRK`),
loaded it at `$0200`, stepped the CPU four instructions, and confirmed the exact expected state: register
`A` = `0x42`, register `X` = `0x07`, memory `$00` = `0x42`, memory `$01` = `0x07`, PC advanced to `$0208`,
10 processor cycles elapsed — all matching the instructions' own documented behavior exactly, with no
discrepancy.

**Disassembly.** `py65.disassembler.Disassembler` correctly decoded the same 9 bytes back into readable
mnemonics (`LDA #$42`, `STA $00`, `LDX #$07`, `STX $01`, `BRK`) at the correct addresses.

## Disclosed limitation

`py65` emulates the base 6502 instruction set and a flat memory model — it does **not** model the Atari
2600's specific TIA (video/audio) or RIOT (I/O/timer) hardware registers, or the 6507's reduced
address-bus width (13 lines vs. the 6502's 16, giving 8KB of address space before bank-switching — stated
here as a known hardware fact, not yet independently re-verified this session). For disassembly and
general instruction-trace purposes this is sufficient (the 6507 shares the 6502's full instruction set);
for TIA-register-write timing analysis specifically (the "racing the beam" model, SQ-2's own scope), this
tool alone is not enough — a TIA-aware extension or a different emulator (e.g. driving Stella itself, if
installable and scriptable in a future session) would be needed before `agents/tia-specialist.md` can do
real trace-verified work. Not attempted this cycle.

## Honesty precommitment

This result only establishes that basic 6502 execution and disassembly are mechanically verifiable in
this environment — it says nothing about any actual game ROM, and the TIA/RIOT gap above is a real,
unresolved limitation, not a solved problem.

## Decision

SQ-1's toolchain half is substantively unblocked for basic opcode-level work: `py65` is installed,
verified correct on a hand-checked test case, and its disassembler output matches expectations exactly.
SQ-1's rights-scoping half (identifying specific legally analyzable target ROMs) remains **not done** —
left as the next concrete step, not rushed into this same cycle.
