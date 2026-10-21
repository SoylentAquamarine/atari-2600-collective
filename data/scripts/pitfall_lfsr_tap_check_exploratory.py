#!/usr/bin/env python3
"""EXPLORATORY (not precommitted): does the fetched source's {1,3,4,5} become maximal under other
conventions (shift-right, 1-indexed)? Enumerates 0/1-indexing x LSB/MSB x shift-left/right."""
def run(seed, taps, left):
    x, seen = seed, set()
    while x not in seen:
        seen.add(x)
        f = 0
        for t in taps: f ^= (x >> t) & 1
        x = (((x << 1) & 0xFF) | f) if left else ((x >> 1) | (f << 7))
    return len(seen)
for label, raw in (("{1,3,4,5}", (1,3,4,5)), ("{3,4,5,7}", (3,4,5,7))):
    for idx in (0, 1):
        for msb in (False, True):
            t = tuple(r - idx for r in raw)
            if any(v < 0 or v > 7 for v in t): continue
            t = tuple(7 - v for v in t) if msb else t
            print(label, f"{idx}-indexed", "MSB" if msb else "LSB", "taps(LSB0)=", sorted(t),
                  "left:", run(0xC4, t, True), "right:", run(0xC4, t, False))
