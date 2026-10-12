# SQ-4 — enriching the sprite-multiplexing entry with Maurer's own words

## Precommitment self-review (written before research)

**Known:** last cycle's sprite-multiplexing entry named the 2600 port of Space Invaders and
Galaxian as examples pushing the technique further, but found "no dedicated kernel-level
source" and left both at search-synthesis tier.

**Not done yet:** no attempt had been made to find the Space Invaders port's own programmer's
account.

**Design and why it's non-circular:** search for the actual programmer (found: Rick Maurer),
then directly fetch his own interview rather than relying on forum speculation about how the
port might have worked.

**Honesty precommitment:** report exactly what Maurer's own words cover and what they don't —
don't fill the gaps with the forum speculation already disclosed as unconfirmed last cycle.

## Findings

**Directly fetched** (a 1999 interview archive, `dadgum.com/giantlist/archive/maurer.html`):
Rick Maurer, who ported Space Invaders to the Atari 2600, describes learning the kernel concept
by reading the 2600's register documentation and studying existing games. In his own words: 
"every cycle of your computer is devoted to drawing the screen" — collision checks and score-
keeping logic had to fit into the roughly 70 scan lines of vertical blank while the beam returns
to the top. He calls this "a complete melding of hardware and software." He explicitly lists the
hardware constraints he worked within: "RAM, CPU time, code space, CPU registers, player 0
register, player 1 register, missile 0, missile 1, and exact kernel timing." He mentions
solving "the flicker problem" but gives no technical explanation of the method. Separately, code
size was a major constraint — the game grew to 7K against a 4K cartridge limit, requiring about
three months of byte-by-byte "scrunching," including branches-to-branches that existed solely to
save a single byte.

**What this does not cover, disclosed rather than filled in by inference**: Maurer's own
interview does not explain why the arcade's 11×5 invader formation became a 6×6 (or similar)
layout on the 2600, and does not describe the specific sprite-multiplexing mechanism (e.g.
whether/how player sprites were repositioned mid-scanline to exceed the native object count).
The forum-sourced "triple-copy" and "RESP-reset" explanations named last cycle remain
unconfirmed by this primary source and are not merged in as if they were.

## Outcome

A real, disclosed upgrade: the sprite-multiplexing catalog entry now has a directly-fetched
primary-source quote from the actual programmer confirming the general "racing the beam"
kernel discipline and the specific named hardware registers (player 0/1, missile 0/1) he worked
within — but the entry's specific multiplexing-mechanism claim for Space Invaders remains at
search-synthesis tier, honestly reported as still unconfirmed rather than silently upgraded.
