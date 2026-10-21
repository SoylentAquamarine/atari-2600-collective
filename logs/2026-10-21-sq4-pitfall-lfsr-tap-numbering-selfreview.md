# SQ-4 — Pitfall! LFSR tap-bit discrepancy: computational check — precommitment

**Date:** 2026-10-21. **Acting as:** Claude, solo. No ROM, no download; pure arithmetic.

**Known:** the 2026-10-12 entry has two tap descriptions for the 8-bit, seed-0xC4, shift-left LFSR:
"b1^b3^b4^b5" (fetched write-up) vs "3, 4, 5, 7" (search summary). Left unresolved pending the
disassembly.

**Not done:** no check whether either tap set is even self-consistent with the claimed behaviour.

**Design / non-circularity:** the claims being tested are testable independent of any source
numbering: (a) is the generator maximal-length (period 255 from seed 0xC4)? (b) does a unique
inverse (previous-state) step exist? Enumerate: (i) taps {1,3,4,5} and (ii) {3,4,5,7}, each under
bit-numbering from LSB=0 and from MSB=0 (so 4 concrete generators; {3,4,5,7} MSB-numbered = {4,3,2,0}
LSB-numbered, etc.), shift-left with feedback into bit 0 (as stated by the fetched source). Also
report, for context, how many of all 4-tap subsets of 8 bits give period 255 (base rate), so
"maximal-length" is not read as confirming a specific candidate if many sets qualify. Prediction:
{1,3,4,5} LSB-numbered is maximal (the fetched source claims maximal-length), and the {3,4,5,7}
LSB reading is probably not, since the disagreement is probably a numbering difference — but if both
numberings of both candidates are maximal (plausible since many tap sets are), the check cannot
discriminate, and I will say so.

**Honesty precommitment:** report as-is; this can narrow but cannot replace reading the disassembly,
so the discrepancy stays flagged open unless exactly one candidate survives AND I say that is
consistency evidence only, not confirmation of what the ROM contains.
