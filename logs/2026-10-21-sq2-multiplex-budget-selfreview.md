# SQ-2/SQ-4 — Sprite-multiplexing cycle-budget bound — precommitment self-review

Written BEFORE running any code (2026-10-21, fifth cycle).

**Known:** the on-file budget (76 CPU cycles/line, 3 colour clocks per CPU cycle, 160 visible px, 25 `STA zp`/line;
see `logs/2026-10-21-sq2-tia-timing-arithmetic-*`) and the catalog entry describing multiplexing as mid-frame
repositioning of the few TIA objects. **Not done:** the previous round's proposed step — checking whether the
multiplexing claims are cycle-consistent. A fetched citation is still unavailable (proxy returned HTTP 000/403
for outbound fetches this cycle), so constants stay unsourced recall.

**Design (non-circular):** compute from the budget alone (a) the CPU-cycle granularity of a RESPx strobe in pixels
(3 px), hence the number of coarse positions across 160 px, (b) the width of a fine-motion HMOVE range needed to
cover the 3-px gap (HMxx recalled as ±8 px; only the *comparison* 8 >= 3 matters), (c) an upper bound on
how many times ONE player object can be re-strobed per line if each re-strobe costs one 3-cycle `STA RESPx`
and the 8-px player must finish drawing (8 px) before it is re-triggered, ignoring data-loading cost (so it is an
optimistic upper bound), and (d) the same bound if each copy also needs a GRPx reload (`LDA #imm` 2 cycles +
`STA GRPx` 3 cycles). None of this uses the catalog's own conclusions as input.

**Prediction:** (a) 53 coarse positions (160/3 floor), (b) 8 >= 3 so every pixel is reachable, (c) bound of about
12-17 copies/line, (d) bound of about 6-8 copies/line. A bound that exceeded ~20 would suggest I mis-set the model.

**Honesty precommitment:** report misses against the prediction; this is arithmetic consistency evidence only, no
ROM touched, constants unsourced; no kernel-specific claim about Space Invaders/Galaxian is made or implied.
