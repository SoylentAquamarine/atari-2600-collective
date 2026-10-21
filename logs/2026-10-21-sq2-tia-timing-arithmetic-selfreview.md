# SQ-2 — TIA/6507 timing arithmetic cross-check — precommitment

**Date:** 2026-10-21 (fourth cycle of the day). **Acting as:** Claude, solo. No ROM, no download; pure arithmetic.

**Known:** `data/hardware-reference.md` states the 6507 clock is "~1.19 MHz" and that WSYNC halts the CPU to the
next horizontal blank. It does not state the NTSC per-scanline budget (color clocks, CPU cycles) or frame rate.

**Not done:** no derived timing budget is on file, so "racing the beam" claims (SQ-4 sprite-multiplexing entry)
cannot be checked against a cycle count.

**Design / non-circularity:** start only from the commonly published NTSC constants (colorburst 3.579545 MHz,
228 color clocks per line = 68 blank + 160 visible, 262 lines/frame, CPU clock = colorburst/3). Derive: CPU cycles
per line, CPU cycles per frame, frame rate, max `STA zp` (3 cycles) per line, and the CPU-cycle count of the
visible window. Cross-check: derived CPU clock must match the ~1.19 MHz already on file (independent number).
Prediction: 76 cycles/line, 19,912 cycles/frame, ~59.92 Hz, 25 STAs per line (76//3), CPU clock 1.1932 MHz
(consistent with file). Constants are from my own recall, not freshly sourced.

**Honesty precommitment:** report as-is. Internal-consistency check only; the constants are unsourced recall
this cycle and are not promoted to verified without a fetched citation.
