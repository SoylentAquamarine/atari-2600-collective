# SQ-2/SQ-4 — Sprite-multiplexing cycle-budget bound — execution

Script: `data/scripts/multiplex_budget_bound.py`; output: `data/scripts/multiplex_budget_bound-output.txt`.

**Result vs precommitted prediction:** (a) 53 coarse positions — held. (b) fine range covers the gap — held (the script
tests the 2-px residual between coarse steps; the self-review said "3-px gap" loosely, a wording slip, conclusion unchanged).
(c) STA-RESPx-only bound is 17 copies/line — held (inside 12-17). (d) full reload+reposition (8 cycles, 24 px/copy) gives 6 copies/line —
held in spirit (precommitted 6-8, lower edge); the intermediate 5-cycle LDA/STA GRPx case (10/line) was not precommitted and is exploratory.

**Interpretation:** the catalog's description of multiplexing as repeated mid-line reposition is cycle-consistent: a single
player can plausibly appear a handful of times on one line, never dozens. Optimistic bounds (no loop overhead, no WSYNC, no
HMOVE cost). Says nothing about the specific Space Invaders/Galaxian kernels.

**Caveats:** constants unsourced recall (no fetch available this cycle: outbound requests failed); consistency evidence only; no ROM touched.

**Proposed next step:** once a fetch is available, cite the Stella Programmer's Guide for the constants and RESP positioning delay.
