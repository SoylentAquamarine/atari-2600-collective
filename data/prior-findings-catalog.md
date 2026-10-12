# Prior-art and notable-finding catalog

Documents already-public, independently-documented Atari 2600 reverse-engineering findings and
programming tricks, properly cited, as calibration and context — not re-presented as this
project's own new discoveries. See `config/sidequests.md` SQ-4.

## Adventure (1980) — the hidden "CREATED BY WARREN ROBINETT" room

**Finding:** programmer Warren Robinett hid a secret room in *Adventure*, accessible via an
intangible in-game item ("the Gray Dot"), displaying the text "CREATED BY WARREN ROBINETT" —
widely credited as the first video game "Easter egg."

**Directly fetched** (Robinett's own published interview, `dadgum.com/halcyon/BOOK/ROBINETT.HTM`):
Robinett's motive was recognition — Atari's box credited only "Adventure, by Atari" and paid
programmers salary with no profit share; he wanted "a signature, like at the bottom of a
painting." He hid it deliberately obscurely and told no one, including close friends. A
fifteen-year-old player from Salt Lake City discovered it and wrote to Atari explaining how to
reach the room. Robinett expected it to be removed after he left Atari, but a new ROM mask would
have cost $10,000, so Atari left it in. The games-group leader (not Robinett) is the one who
first called it an "Easter Egg."

**Search-synthesis tier only, not independently verified this pass:** the secret room is said to
occupy roughly 5% of cartridge storage; an Atari employee named Steve Wright is sometimes
credited (instead of the games-group leader, per the primary source above) with coining "Easter
Egg"; sales are recalled at roughly one million units. These are reported as lower-confidence
context, not verified claims — see `logs/2026-10-11-sq4-adventure-easter-egg-first-entry.md` for
the full disclosed discrepancy between tiers.

## Yars' Revenge (1982) — Howard Scott Warshaw's "HSWWSH" hidden signature

**Finding:** programmer Howard Scott Warshaw hid his mirrored initials, "HSWWSH," as the
player's score under a specific in-game condition: hitting the Qotile's swirling defense shield
with the cannon produces a black vertical line ("the Ghost of Yars," per the game's own
manual); positioning the player's Yar in the line's lower third when the resulting explosion
ends stops the game and displays "HSWWSH" in place of the score.

**Directly fetched** (atarimania.com, a dedicated Atari archival/specialist site): confirms the
trigger sequence and the displayed text exactly as described above.

**Search-synthesis tier only, not independently verified this pass**: Warshaw is reported to
have left similar initial-based signatures in other credited games, including "HSW3" in *E.T.
the Extra-Terrestrial*'s score line. Named as a pattern worth testing against other programmers'
games in a future pass, not assumed to generalize — see
`logs/2026-10-11-sq4-yars-revenge-warshaw-signature.md`.

**A structural note connecting this entry to the first**: both this and the *Adventure* entry
above are hidden-programmer-identity signatures, consistent with the same underlying motive
(Atari's no-programmer-credit policy) documented for Robinett — Warshaw's version uses a precise
gameplay-positioning trigger rather than a hidden room, a materially different mechanism for the
same underlying practice.

## Sprite multiplexing — a well-known technique, not a hidden Easter egg

**Finding:** the TIA chip natively provides only 2 player-graphics registers (GRP0/GRP1), 2
missile-enable registers (ENAM0/ENAM1), and 1 ball-enable register (ENABL) — already
independently verified in this project's own `data/hardware-reference.md` from earlier
disassembly-cycle work. Programmers discovered they could reposition/redraw these few hardware
objects multiple times within a single frame (via RESP0/RESP1/RESM0/RESM1, also already
documented in this project's own reference) to create the appearance of more simultaneous
on-screen objects than the hardware natively holds — a technique now generally known as
"sprite multiplexing."

**Directly fetched** (Wikipedia, "Sprite multiplexing"): confirms the general mechanism was
never an intentionally designed TIA feature — programmers discovered they could reset the chip
mid-scanline to draw additional sprites, relying on the program tracking exactly where the
video beam currently is; mistimed reprogramming causes objects to not appear or draw
incorrectly.

**Search-synthesis tier only, not independently verified this pass**: the 2600 ports of *Space
Invaders* and *Galaxian* are reported to use more advanced multiplexing arrangements to exceed
the hardware's native object count on a single scanline — no dedicated disassembly or
programmer-interview source confirming their specific kernel structure was found this cycle.

**A genuinely different kind of entry** from the first two (Adventure, Yars' Revenge): a
general, named programming technique rather than a one-off hidden signature, and a case where
this project's own independently-verified hardware facts from unrelated earlier work directly
corroborate an externally-sourced technique description — see
`logs/2026-10-12-sq4-sprite-multiplexing-third-entry.md`.

## Not yet researched

Other well-documented 2600-era tricks and hidden content (e.g., further Atari-era Easter eggs,
specific disassembly-level detail on how Space Invaders/Galaxian's own multiplexing kernels
work) are in scope for this catalog per `config/sidequests.md` but have not yet been
researched — a future-cycle target.
