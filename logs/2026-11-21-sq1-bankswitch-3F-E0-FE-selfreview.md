# 2026-11-21 — SQ-1 bank-switching catalog, second batch (3F, E0, FE, F8SC/F6SC/F4SC): precommitment self-review

Written BEFORE fetching any file.

**Known.** F8/F6/F4 are catalogued (single source: Stella). The previous round's proposed next step was the
remaining common schemes. raw.githubusercontent.com is reachable; other hosts are not.

**Not done.** No hotspot/bank-size data for 3F (Tigervision), E0 (Parker Bros), FE (Activision), or the
"SC" (SuperChip, extra 128 bytes RAM) variants.

**Design.** Fetch source only (never ROM bytes) of Stella's Cart3F.cxx, CartE0.cxx, CartFE.cxx and the F8SC/F6SC/F4SC
handling (CartF8SC/CartF6SC/CartF4SC .cxx or equivalent). Extract hotspot addresses, slice/bank structure and RAM
layout from code. Internal-consistency check: slice size x count fits the 4K window; hotspot ranges do not overlap
the ROM slices they control incorrectly. Non-circular: values come from implementation code, with my memory
prediction recorded first so mismatch is visible.

**Prediction (memory).** 3F: 2K switchable slice at $1000-$17FF, fixed last 2K at $1800-$1FFF; write to any
address $00-$3F selects the bank (value written). E0: four 1K slices ($1000/$1400/$1800/$1C00, last fixed to the
final 1K), hotspots $1FE0-$1FF7 (three groups of 8 for the three switchable slices). FE: 8K, bank switching
triggered by stack/address-bus behaviour (access at $01FE/$01FF region, not a plain hotspot read). SC variants:
128 bytes RAM, write port $1000-$107F, read port $1080-$10FF.

**Honesty precommitment.** Report disagreement; label tier "emulator source, one source"; no ROM bytes; append-only
state.md update; if a file fails to fetch, log that rather than fill from memory.
