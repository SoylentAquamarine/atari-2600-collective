# SQ-4: fourth catalog entry — Pitfall!'s LFSR-based procedural level generation

## Precommitment self-review (written before research)

**Known:** SQ-4's catalog has three entries — two hidden-programmer-signature Easter eggs
(Adventure, Yars' Revenge) and one general display technique (sprite multiplexing). The
sidequest's scope and this catalog's own "Not yet researched" section name "other well-documented
2600-era tricks" as open. A well-known candidate, distinct in category from all three existing
entries (a memory-compression/procedural-generation technique, not a display or signature trick):
David Crane's use of a linear feedback shift register (LFSR) to generate Pitfall!'s 255 screens
without storing them in ROM.

**Not done yet:** no source on this specific technique had been fetched by this project before
now.

**Design and why it's non-circular:** directly fetch a technical source describing the LFSR's
exact parameters (bit width, seed, tap bits, shift direction), rather than relying on a
search-synthesis summary alone, per this project's own stated preference for primary/directly-
fetched tier where available. Cross-check against a second source (general search synthesis) for
the motivating constraint (ROM size) and disclose explicitly if the two sources disagree on any
specific technical detail, rather than silently picking whichever reads more cleanly.

**Honesty precommitment:** report the exact tap bits and parameters as the fetched source states
them, flag any disagreement with the broader search-synthesis summary, and do not resolve such a
disagreement without reading the actual disassembled source (out of scope here) — leave it as a
disclosed open discrepancy.

## Findings

**The general technique, directly fetched (`devnonsense.com/posts/pitfall-lfsr-math`, a
technical write-up that reconstructs the generator from the disassembled game)**: an 8-bit
maximal-length LFSR, seeded at `0xC4`, with feedback bit `f(B) = b1 XOR b3 XOR b4 XOR b5`,
shifted left with the feedback bit entering at the low end. Because it is maximal-length, it
cycles through all 255 nonzero 8-bit states before repeating — one unique screen per state. A
reverse step (`F^-1(B)`, recovering the dropped high bit via a different XOR combination) lets
the game regenerate the *previous* screen when Harry walks left, which is how backward
navigation works without storing any screen data either direction.

**A disclosed minor discrepancy, not resolved here**: a broader search-synthesis summary (not
independently fetched at primary tier) describes the tap bits as "3, 4, 5, and 7" rather than
"1, 3, 4, 5" as the directly-fetched source states. This is plausibly just a difference in bit-
numbering convention (0-indexed from the LSB vs. a different reference point) rather than a
substantive disagreement about the mechanism, but this project has not read the actual
disassembled 6502 source to confirm which numbering is correct — left as an open, flagged
discrepancy rather than silently resolved in favor of either source.

**Why it was needed (search-synthesis tier only)**: the Pitfall! cartridge had 4KB of ROM, most
of which held game code, leaving no room to store 255 individual screen layouts. Reported
figures for the actual compressed storage cost vary across sources (50 bytes vs. other figures),
not independently verified here.

**A genuinely different kind of entry** from all three prior ones: a procedural-content-
generation / memory-compression technique, not a display trick (sprite multiplexing) or a hidden
signature (Adventure, Yars' Revenge) — the fourth distinct technique category in this catalog.

## Not yet researched

Further well-documented 2600-era techniques (e.g., specific disassembly-level detail on
Pitfall!'s own code implementing this LFSR, Combat/other early titles' own notable tricks)
remain open for a future cycle.
