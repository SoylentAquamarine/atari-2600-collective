#!/usr/bin/env python3
"""Check the closed-form reverse step of the Pitfall! LFSR candidate (taps 3,4,5,7; shift-left; seed 0xC4).
Precommitment: logs/2026-10-21-sq4-pitfall-lfsr-reverse-step-selfreview.md"""
TAPS = (3, 4, 5, 7)
def F(x):
    f = 0
    for t in TAPS: f ^= (x >> t) & 1
    return ((x << 1) & 0xFF) | f
def Finv(y):
    b = y & 1
    x = y >> 1
    x7 = b ^ ((x >> 3) & 1) ^ ((x >> 4) & 1) ^ ((x >> 5) & 1)
    return x | (x7 << 7)
states = range(256)
print("F(0) =", F(0), "(0 fixed point)")
print("F bijective on 0..255:", sorted(F(x) for x in states) == list(states))
print("Finv(F(x)) == x for all x:", all(Finv(F(x)) == x for x in states))
print("F(Finv(y)) == y for all y:", all(F(Finv(y)) == y for y in states))
x, seen = 0xC4, []
for _ in range(255): seen.append(x); x = F(x)
print("distinct nonzero states visited in 255 forward steps:", len(set(seen)), "returned to seed:", x == 0xC4, "0 in cycle:", 0 in seen)
y = 0xC4
for _ in range(255): y = Finv(y)
print("255 reverse steps from seed returns to seed:", y == 0xC4)
fw = []; x = 0xC4
for _ in range(10): x = F(x); fw.append(x)
bk = []
for s in reversed(fw[:-1]): bk.append(s)
print("walk back 9 from step10 equals forward states reversed:", [Finv(v) for v in fw[:0:-1]] == [0xC4 if False else v for v in ([0xC4] + fw[:-1])[:0:-1]] )
