# 2026-11-21 — SQ-1 bank-switching catalog, fourth batch (UA, 0840, CV, 4A50, X07): precommitment self-review

Written BEFORE fetching any source.

**Known so far:** batches 1-3 (F8/F6/F4, 3F/E0/FE/SC, FA/E7/F0/3E/DPC) are catalogued from Stella source, single-source tier.
**Not yet done:** UA, 0840, CV, 4A50, X07 (remaining non-ARM schemes).
**Design:** fetch only Stella `src/emucore/Cart{UA,0840,CV,4A50,X07}.cxx/.hxx` (source text, no ROM bytes) from raw.githubusercontent.com; extract trigger addresses, bank sizes, RAM windows. Non-circular: predictions below are written from memory first and then compared to the code; discrepancies are recorded, not smoothed.
**Predictions (from memory, uncertain):**
- UA (UA Limited): 8K, two 4K banks, hotspots $0220 (bank 0) / $0240 (bank 1) via TIA-mirror addresses; variant UASW swaps.
- 0840 (Econobanking): 8K, bank chosen by access to $0800-$0FFF region with address bits; two 4K banks.
- CV (Commavid): 2K ROM + 1K RAM; RAM write $1400-$17FF, read $1000-$13FF; no hotspots.
- 4A50: 128K ROM + 32K RAM, complex write-triggered ($4Cxx-style latching) mapping; low confidence on details.
- X07: 64K, hotspots in $080x-$0Fxx range with address-bit decoding; low confidence.
**Honesty precommitment:** report mismatches and anything I cannot extract; single-source tier; no ROM bytes fetched, committed or redistributed; if a file is unreachable, say so.
