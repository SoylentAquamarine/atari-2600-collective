# SQ-4 — Pitfall! LFSR reverse step (F^-1) — execution

Precommitment: `logs/2026-10-21-sq4-pitfall-lfsr-reverse-step-selfreview.md`. Script/output:
`data/scripts/pitfall_lfsr_reverse_step_check{.py,-output.txt}`.

**Result: prediction held.** F (taps {3,4,5,7}, shift-left) is a bijection on 0..255; the closed-form inverse
(recover the shifted-out bit 7 from the feedback equation) satisfies F^-1(F(x))=x and F(F^-1(y))=y for all
256 values; 255 forward steps from 0xC4 visit 255 distinct nonzero states and return to the seed; 255
reverse steps also return to it; state 0 is a fixed point outside the cycle. The inverse needs only the
current state — no stored history — so a "walk back to the previous screen" is arithmetically possible with this generator.

**Disclosure:** the last printed line of the script is an awkwardly written redundant check (it adds nothing beyond the full-bijection
checks above it); the conclusions rest on the bijection/identity lines. **Scope:** shows the candidate
generator admits a stateless reverse step; says nothing about what the ROM actually does (disassembly unread, no ROM touched).
