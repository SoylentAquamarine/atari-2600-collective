# 2026-11-21 — SQ-1 bank-switching catalog, third batch (FA, E7, F0, 3E, DPC): precommitment self-review

Written BEFORE fetching any file.

**Known.** F8/F6/F4, 3F, E0, FE and the SC variants are catalogued (single source: Stella source). raw.githubusercontent.com is reachable.

**Not done.** FA (CBS RAM Plus), E7 (M-Network), F0 (Megaboy), 3E (3F + RAM), DPC (Pitfall II coprocessor) have no hotspot/size data on file.

**Design.** Fetch source only (never ROM bytes): Stella CartFA, CartE7, CartF0, Cart3E, CartDPC .cxx/.hxx. Extract ROM size, segment layout, hotspots and RAM layout. Check slice size x count against the window. Non-circular: values come from code; my memory predictions are recorded first so a mismatch is visible.

**Predictions (memory).** FA: 12K, three 4K banks, hotspots $1FF8-$1FFA, 256 B RAM (write $1000-$10FF, read $1100-$11FF). E7: 16K, 2K segments; hotspots $1FE0-$1FE7 pick the 2K bank for the lower window, $1FE8-$1FEB the 1K RAM bank for $1800-$19FF; fixed last 2K. F0: 64K, 16 banks of 4K, single hotspot $1FF0 that increments the bank. 3E: like 3F (write to $3F picks ROM bank) plus write to $3E picks 1K RAM bank; up to 512K ROM. DPC: 8K ROM + 2K display data, 4K window, F8-style hotspots $1FF8/$1FF9, data fetchers at $1000-$107F (reads) / $1040-... writes, with a random-number generator. Details of the DPC register map I expect to be imprecise.

**Honesty precommitment.** Report disagreement; tier label "emulator source, one source"; no ROM bytes; append-only state.md; if a file fails to fetch, log that rather than fill from memory.
