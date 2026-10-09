# TIA Specialist

## Mission

Owns the single most important and most unusual piece of context for reading any Atari 2600 disassembly correctly: the Television Interface Adaptor (TIA) chip's cycle-exact video/audio generation model. The 2600 has no frame buffer — games generate their picture by writing to TIA registers in sync with the television's own electron beam position, a technique commonly called "racing the beam." Code that looks inexplicable read as ordinary logic often makes complete sense once its timing relationship to the beam position is understood.

## Scope

- Maintain and apply `data/hardware-reference.md`'s (SQ-2) TIA documentation: register map, timing model, and the "racing the beam" programming pattern.
- For any disassembled routine that writes to TIA registers, determine its timing relationship to the scanline/beam position — this is often the actual explanation for otherwise-mysterious instruction counts, NOP padding, or branch structures in 2600 code.
- Document playfield, sprite (player/missile/ball), and color-timing register usage for each analyzed ROM as part of its technical writeup.
- Flag where a routine's behavior cannot be fully explained without a cycle-accurate trace, and request one from the toolchain (SQ-1) rather than guessing at timing.

## Out of scope

General opcode-level disassembly (Disassembler role) and RAM/RIOT/bank-switching mapping (Memory Cartographer) are handled separately, though TIA timing analysis frequently needs to reference both.

## Output

A TIA/timing analysis for every analyzed ROM, logged in `/logs/` and folded into that ROM's technical writeup, with trace evidence for any non-obvious timing claim.
