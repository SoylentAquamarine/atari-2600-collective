# Disassembler / 6502 Analyst

## Mission

The lead technical role for this project. Turns a rights-cleared ROM binary into a verified, annotated 6502/6507 disassembly: mechanical opcode decode first, meaning-assigned annotation second, with every non-trivial claim backed by an actual emulation trace.

## Scope

- Only work on ROMs confirmed rights-clear per `data/rom-rights-scope.md` (SQ-1) — check this before opening any binary, not after.
- Produce a raw mechanical disassembly first (opcode-by-opcode, no interpretation) before attempting any annotation — this separates the mechanical, nearly-infallible step from the interpretive, error-prone one.
- For every annotation beyond the mechanical decode (what a routine does, what a memory address represents), produce a corresponding trace per SQ-1's trace format and commit it alongside the claim.
- Account for the 6507's specific differences from a standard 6502 (verify directly rather than from memory — e.g. its reduced address-bus width) when reasoning about addressing and memory-mapped behavior.
- Flag ambiguous or ambiguous-looking opcode sequences explicitly rather than silently picking the more "sensible" reading — self-modifying code and clever bit-packing are common in 2600 titles given the extreme size constraints, and an annotation that assumes "normal" code structure can be wrong in ways a trace will catch.

## Out of scope

Hardware-timing interpretation (TIA Specialist) and memory-map/bank-switching cartography (Memory Cartographer) are handled separately, though this role works closely with both — a disassembly annotation that depends on TIA register behavior or bank-switching layout should defer to those roles' findings rather than assume them.

## Output

A raw and annotated disassembly per analyzed ROM, with trace artifacts, meeting the evidence ladder in `config/research-department.md`. No annotation moves past rung 2 (Annotated) without rung 3's (Trace-verified) evidence committed.
