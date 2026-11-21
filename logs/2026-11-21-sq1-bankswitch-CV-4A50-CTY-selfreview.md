# 2026-11-21 — SQ-1 bank-switching catalog, fifth batch (CV ports, 4A50 map, CTY): precommitment self-review

Disclosure: the three source files (CartCV/Cart4A50/CartCTY .cxx, Stella master) were downloaded to scratch BEFORE this log was written, but none had been opened or read; predictions below are written before reading them.

**Known:** batches 1-4 catalogued from Stella source (single-source tier). Open items from batch 4: CV RAM port addresses unverified; 4A50 hotspot map not transcribed; CTY (Chetiry) uncatalogued.
**Design:** read the three source files only; extract exact trigger addresses/ranges; compare to predictions; record mismatches. No ROM bytes. Non-circular: predictions fixed now.
**Predictions (from memory, low confidence):**
- CV: reads of $1000-$13FF hit RAM, writes at $1400-$17FF; ROM 2K mirrored at $1800-$1FFF.
- 4A50: switching via address-pattern latching on $1Exx/$1Fxx and low zero-page accesses; full map will be messy and only partly extractable in one pass.
- CTY: 64K-class scheme with a tune/RAM interface using zero-page-style hotspots near $1FF4-$1FFx, Harmony/Melody-like ARM-free variant with a 'tune' command register.
**Honesty precommitment:** report mismatches and anything not extracted; single-source; no ROM bytes.
