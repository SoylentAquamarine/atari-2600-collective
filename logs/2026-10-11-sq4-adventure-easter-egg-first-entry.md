# SQ-4: first prior-findings catalog entry — the Adventure (1980) hidden signature

## Precommitment self-review (written before research)

**Known:** SQ-4 ("prior-art and notable-finding catalog") is listed in `config/sidequests.md`
as not started — a reasonable parallel task alongside SQ-1/SQ-2 since it needs no working
toolchain. Its scope names the Warren Robinett *Adventure* hidden signature as the canonical
example to catalog first.

**Not done yet:** `data/prior-findings-catalog.md` does not yet exist; no source has been
fetched for this.

**Design and why it's non-circular:** this is pure literature research — find and directly
fetch independently-published accounts (ideally Robinett's own words), not derive anything from
this project's own disassembly work. No ROM is downloaded, analyzed, or redistributed to do
this; the catalog documents already-public history, consistent with SQ-4's own stated purpose
("properly cited rather than re-presented as new discoveries").

**Prediction:** the standard account (hidden room reachable via "the Gray Dot," discovered by a
player who wrote to Atari, kept because a new ROM mask was too expensive, coined "Easter Egg" by
an Atari employee) will hold up against a direct primary source.

**Honesty precommitment:** disclose evidentiary tier per claim; do not restate technical
implementation details beyond what the fetched source actually states.

## Research and findings

**Claim:** Warren Robinett hid his name ("CREATED BY WARREN ROBINETT") in a secret room in
*Adventure* (Atari 2600, 1979–1980), reachable using an intangible item ("the Gray Dot"),
discovered by a player who wrote to Atari — widely credited as the first video game "Easter
egg."

**Directly fetched** (`dadgum.com/halcyon/BOOK/ROBINETT.HTM` — a published interview/chapter
with Robinett himself): confirms the motive directly in his own words — Atari credited only
"Adventure, by Atari" on the box, paid programmers a salary with no profit share, and he wanted
a "signature, like at the bottom of a painting." He describes hiding it "in the code, in a
really obscure place, and not tell[ing] anybody," reachable via the Gray Dot (which had a strong
in-game hint pointing to it), and kept the secret even from close friends on principle. He names
the discoverer as a fifteen-year-old from Salt Lake City who wrote to Atari explaining how to
reach the room. He expected Atari to remove it after he left the company, but a new ROM mask
would have cost $10,000, so it stayed. The games-group leader (not Robinett) is the one who
called it an "Easter Egg," on the theory that such surprises added value to games. The fetched
page does not describe the specific technical/memory implementation beyond "hidden in the code."

**Search-synthesis tier only** (not independently re-fetched this pass, included for context,
explicitly flagged as lower-confidence): secondary sources (an Atari.com blog post — blocked by
HTTP 403 on direct fetch this pass; a wiki) add detail not found in the primary interview —
that the secret room took up roughly 5% of cartridge storage, that an Atari employee named Steve
Wright is the one credited with coining "Easter Egg," and that Robinett recalls sales around one
million units. These specifics are reported here as search-synthesis tier, not verified against
a primary source, and should not be treated with the same confidence as the directly-fetched
claims above.

## Outcome vs. prediction

Confirmed on every point the primary source actually covers (motive, mechanism-in-outline,
discovery, why it was kept). The two findable "Easter Egg" coinage and storage-percentage
details could not be upgraded past search-synthesis tier this pass — disclosed rather than
silently merged into the primary-source account.
