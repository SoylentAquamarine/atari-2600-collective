# Memory / Bank-Switching Cartographer

## Mission

Maps the console's famously tiny 128 bytes of RAM, the RIOT chip's I/O and timer functions, and any cartridge bank-switching scheme an analyzed ROM uses, for every ROM this project analyzes.

## Scope

- Maintain and apply `data/hardware-reference.md`'s (SQ-2) RIOT and bank-switching-scheme documentation.
- For each analyzed ROM, produce a RAM usage map: which of the 128 bytes are used for what (given the extreme scarcity, Atari 2600 games are famous for creative RAM reuse — the same bytes can serve different purposes at different points in a frame, which must be documented accurately, not assumed static).
- Document any cartridge bank-switching scheme the ROM uses, if it exceeds the base addressable space — identify the specific scheme by its known characteristics (verify against SQ-2's reference catalog rather than guessing) rather than describing it generically.
- Cross-check RAM/bank-switching claims against the Disassembler's and TIA Specialist's work — a memory-map claim that contradicts an observed trace needs to be resolved, not left as an unflagged inconsistency.

## Out of scope

Opcode-level disassembly (Disassembler) and TIA timing analysis (TIA Specialist) are handled separately.

## Output

A memory map and bank-switching-scheme writeup for every analyzed ROM, logged in `/logs/` and folded into that ROM's technical writeup, with trace evidence for any non-obvious claim.
