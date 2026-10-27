# SQ-4 — fifth catalog entry (candidate: flicker / "venetian blinds" and the 2600 asymmetric-playfield trick) — precommitment

**Date:** 2026-10-27. **Acting as:** Claude, solo. Web text sources only; no ROM, no binary, no scan download.

**Known:** catalog has four entries (Adventure egg, Yars' signature, sprite multiplexing, Pitfall! LFSR). The
"Not yet researched" section names further 2600-era tricks as open.

**Not done:** no entry on frame-alternating flicker or on mid-scanline playfield rewriting (asymmetric playfields).

**Design / non-circularity:** run a web search for one well-documented technique, fetch one or two text pages,
and record only what a fetched page states, tagged as fetched-source vs search-synthesis. Cross-check against the
project's own verified hardware facts in data/hardware-reference.md (76-cycle scanline, 3-cycle playfield
register write granularity), which were derived independently of the source. A source claim that conflicts with
our own arithmetic is flagged, not merged.

**Prediction:** at least one fetched page will describe the technique mechanism consistently with
hardware-reference.md; named-game examples will mostly stay at search-synthesis tier.

**Honesty precommitment:** if no fetchable source supports the mechanism, log a null result and add no
catalog entry. Any conflict with hardware-reference.md is disclosed as such.
