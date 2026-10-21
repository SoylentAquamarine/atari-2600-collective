# SQ-4 — Pitfall! LFSR tap-bit discrepancy: computational check — execution

Precommitment: `logs/2026-10-21-sq4-pitfall-lfsr-tap-numbering-selfreview.md`. Scripts/outputs:
`data/scripts/pitfall_lfsr_tap_check{,_exploratory}.py` and `-output.txt`.

## Precommitted check
Period from seed 0xC4, shift-left, feedback into bit 0:
- taps {3,4,5,7} 0-indexed from LSB: **period 255** (maximal), returns to seed.
- taps {1,3,4,5} 0-indexed from LSB: period 21 — **not maximal**.
- both candidates under 0-indexed MSB numbering: periods 128 / 32, not maximal.
- base rate: 12 of 70 four-tap subsets are maximal from this seed, so "maximal" alone is weak
  evidence for any one candidate (it is evidence against {1,3,4,5} as literally 0-indexed-LSB).

**Stated prediction partly wrong**: I predicted {1,3,4,5} LSB-numbered would be the maximal one (the
fetched write-up claims maximal-length); the opposite held — it is the {3,4,5,7} reading that is
maximal, and {1,3,4,5} read naively is not.

## Exploratory follow-up (NOT precommitted, disclosed as such)
Enumerating 0/1-indexing x LSB/MSB x shift direction: **{1,3,4,5} read as 1-indexed from the MSB maps
to LSB-0 taps {3,4,5,7}, shift-left, period 255** — i.e. the two descriptions are exactly the same
generator under different bit-numbering conventions. This supports the original disclosure's
guess, and it also means the fetched write-up's tap list cannot be applied literally as 0-indexed-LSB.

## Status
Discrepancy **narrowed, not closed**: the descriptions are mutually consistent under one convention and
the resulting generator is maximal-length (255 states) — consistency evidence only. Other conventions (e.g.
shift-right variants: {1,3,4,5} 1-indexed LSB right-shift is also 255) fit equally well, and
what the actual ROM does is unverified without the disassembly (out of scope, no ROM touched).
