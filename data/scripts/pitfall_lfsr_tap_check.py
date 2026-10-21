#!/usr/bin/env python3
"""Check which candidate tap sets give a period-255 8-bit shift-left LFSR from seed 0xC4.
Precommitment: logs/2026-10-21-sq4-pitfall-lfsr-tap-numbering-selfreview.md"""
from itertools import combinations
def step(x, taps):
    f = 0
    for t in taps: f ^= (x >> t) & 1
    return ((x << 1) & 0xFF) | f
def period(seed, taps):
    x, n, seen = seed, 0, set()
    while x not in seen:
        seen.add(x); x = step(x, taps); n += 1
    return n, len(seen), x == seed  # steps until repeat, distinct states, returned to seed?
cands = {"{1,3,4,5} LSB-numbered": (1,3,4,5),
         "{3,4,5,7} LSB-numbered": (3,4,5,7),
         "{1,3,4,5} MSB-numbered": tuple(7-t for t in (1,3,4,5)),
         "{3,4,5,7} MSB-numbered": tuple(7-t for t in (3,4,5,7))}
for name, taps in cands.items():
    print(f"{name:26s} LSB taps={sorted(taps)} -> (steps,distinct,returns_to_seed)={period(0xC4, taps)}")
tot = good = 0; goodsets = []
for taps in combinations(range(8), 4):
    tot += 1
    n, d, ret = period(0xC4, taps)
    if d == 255 and ret: good += 1; goodsets.append(taps)
print(f"base rate: {good}/{tot} four-tap subsets are maximal (255) from seed 0xC4")
print("maximal sets:", goodsets)
