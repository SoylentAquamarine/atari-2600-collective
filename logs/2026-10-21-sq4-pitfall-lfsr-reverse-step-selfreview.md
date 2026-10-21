# SQ-4 — Pitfall! LFSR reverse step (F^-1): computational check — precommitment

**Date:** 2026-10-21 (second cycle of the day). **Acting as:** Claude, solo. No ROM, no download; pure arithmetic.

**Known:** the generator (taps {3,4,5,7}, 0-indexed LSB, shift-left, feedback into bit 0, seed 0xC4) has
period 255 (`2026-10-21-sq4-pitfall-lfsr-tap-numbering-execution.md`). The 2026-10-12 entry cites a source
claiming a reverse step lets Harry walk back to a regenerated previous screen.

**Not done:** that reverse-step claim was never checked.

**Design / non-circularity:** the claim is testable without any source: (a) on a maximal cycle F is a
bijection on the 255 nonzero states, so F^-1 exists and is unique; (b) a direct inverse can be computed
from the state alone because the shifted-out bit (bit 7 of the previous state) is the one tap whose value
is recovered by solving the feedback equation: given y = F(x), bit0(y) = x3^x4^x5^x7 and bits 1..7 of y =
bits 0..6 of x, so x3,x4,x5 are known and x7 = bit0(y)^x3^x4^x5; x = ((y>>1) | x7<<7). I implement that
closed form independently of F, then test F^-1(F(x)) == x and F(F^-1(y)) == y for all 255 states, and
walk 255 steps forward then 255 back from the seed. Also check whether all 255 non-zero states are
visited (the "255 screens" claim) and whether state 0 is a fixed point outside the cycle.
Prediction: every identity holds on all 255 states; the closed-form inverse needs only the state itself
(no stored history).

**Honesty precommitment:** report as-is. Passing shows only that this tap set admits a stateless reverse
step; it does not show the ROM implements it, and the disassembly stays unread.
