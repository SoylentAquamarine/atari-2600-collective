# SQ-4: third catalog entry — sprite multiplexing, a well-known technique (not a hidden Easter egg)

## Precommitment self-review (written before research)

**Known:** SQ-4's catalog has two entries so far, both hidden-programmer-signature Easter eggs
(Adventure, Yars' Revenge). The sidequest's own scope names a second, distinct category never
yet catalogued: "well-known 2600 programming techniques." A general search for famous Atari
2600 tricks surfaced "sprite multiplexing" — the standard technique used to display more
objects than the TIA chip natively supports.

**Not done yet:** no source on sprite multiplexing specifically had been fetched; this would be
this catalog's first entry that is a general technique rather than a one-off hidden signature.

**Design and why it's non-circular:** directly fetch Wikipedia's dedicated "Sprite
multiplexing" article for the general mechanism, then cross-check it against this project's own
already-independently-verified TIA register documentation (`data/hardware-reference.md`, from
earlier disassembly-cycle work) for the specific hardware limit the technique works around —
combining an external source with this project's own previously-verified primary-tier hardware
facts, not treating either alone as sufficient.

**Honesty precommitment:** disclose exactly which claims are externally sourced vs. already
on file from this project's own prior work, and flag anything the external source doesn't cover
(e.g., specific games, specific register-level mechanics) as a gap, not filled in by assumption.

## Findings

**The general technique, directly fetched (Wikipedia, "Sprite multiplexing")**: "On the older
Atari 2600, sprite multiplexing was not intentionally designed in, but programmers discovered
they could reset the TIA graphics chip to draw additional sprites on the same scanline." The
technique "relies on the program being able to identify what part of the video screen is being
drawn at the moment" — if the hardware isn't reprogrammed in time, objects "will not appear, or
will be drawn incorrectly." This is the same general "racing the beam" discipline this project's
own disassembly work has already directly observed in practice (WSYNC-gated per-scanline
updates, already documented in `data/hardware-reference.md`).

**The specific hardware limit this technique works around — already verified by this project's
own prior work, not newly sourced here**: the TIA natively provides only 2 player-graphics
registers (GRP0/GRP1), 2 missile-enable registers (ENAM0/ENAM1), and 1 ball-enable register
(ENABL) — confirmed in this project's own `data/hardware-reference.md`, built and verified
during earlier disassembly cycles, independent of today's search. Sprite multiplexing is the
general name for programming techniques that reposition/redraw these few hardware objects
multiple times within a single frame (via `RESP0`/`RESP1`/`RESM0`/`RESM1`, also already
documented) to create the appearance of more simultaneous objects than the hardware natively
holds.

**Named example games, search-synthesis tier only, not independently verified this cycle**: the
2600 port of *Space Invaders* and *Galaxian* are reported (via AtariAge forum discussion, not a
dedicated reference) to use more advanced multiplexing arrangements to get more apparent sprites
on a single scanline than the hardware's native object count — disclosed as a lead, not a
confirmed technical account, since no dedicated source describing their specific kernel
structure was found this cycle.

## Outcome

A genuinely different kind of catalog entry — a general, named programming technique rather
than a one-off hidden signature — directly fulfilling SQ-4's own stated scope ("well-known
programming techniques"), and a case where this project's own independently-verified hardware
facts (from unrelated earlier disassembly work) directly corroborate and ground an externally-
sourced general technique description, rather than relying on either source alone.

## Limitation disclosed

No dedicated source (e.g. a specific disassembly or programmer interview) describing exactly
how *Space Invaders* or *Galaxian* implemented their own multiplexing was found or fetched this
cycle — named as a future-cycle target, not filled in by inference from the general technique
description.
