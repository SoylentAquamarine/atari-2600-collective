# 2026-11-21 — SQ-1 bank-switching catalog, batch 6 (CDF, BUS, DPC+): precommitment self-review

Written BEFORE fetching any source (nothing downloaded yet).

**Known so far:** batches 1-5 catalogue the non-ARM schemes plus CTY from Stella source (single-source tier).
**Not yet done:** the ARM-assisted families CDF (incl. CDFJ), BUS (BUS/Harmony-era), DPC+.
**Design:** fetch only Stella `src/emucore/Cart{CDF,BUS,DPCPlus}.cxx/.hxx` as source text (no ROM bytes, no firmware images) from raw.githubusercontent.com into scratch; extract bank count/size, hotspot addresses, RAM/ARM-region layout, datastream/fast-fetcher register map. Non-circular: predictions below are written from memory first and compared to the code; mismatches recorded, not smoothed.
**Predictions (from memory, low-moderate confidence):**
- DPC+: 32K image; 6 x 4K banks; hotspots $1FF6-$1FFB; 8K ARM driver + 4K display data + 1K frequency tables in the image; 8K? RAM region; data fetchers/fast fetcher via $1000-$107F reads.
- CDF: 32K ARM-capable, 7 banks (0-6) at $1FF5-$1FFB; datastream registers in $1000-$10FF read area; fast-fetch via LDA #imm.
- BUS: 32K, 7 banks at $1FF6-$1FFC? uncertain; similar datastream scheme with 3-byte increments.
**Honesty precommitment:** report mismatches and anything not extractable; single-source tier; no ROM/firmware bytes committed; if a file is unreachable, say so and log a no-op.
