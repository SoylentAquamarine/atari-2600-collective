# Hardware reference — 6507 CPU, TIA, RIOT

SQ-2's deliverable. Seeded directly from a real need in SQ-3's own disassembly work this cycle: a
previously-unremarked `STA $02` instruction, repeated at several points in `chesterbr/2048-2600`'s
disassembled code, turned out to be a named, well-documented TIA hardware idiom — this file exists so that
fact (and others like it) is on record with citations, not re-derived from memory or silently assumed next
time it comes up.

## The three chips

The Atari 2600 has three principal ICs: the **6507** CPU, the **TIA** ("Stella") video/audio chip, and the
**6532 RIOT** (RAM/I/O/Timer) chip. (Source: multiple independently-corroborating secondary references,
cross-checked this cycle — astro.physik.uni-potsdam.de's "Atari 2600 Specifications" page and
dfarq.homeip.net's "The Atari 2600 CPU: The MOS 6507.")

## 6507 vs. stock 6502

- **28-pin package**, 13 address lines (A0-A12) and 8 data lines — limits addressable space to 8KB, versus
  the 6502's full 16 address lines / 64KB space. The highest address line, **A12, doubles as the cartridge
  ROM's chip-select** line.
- **No interrupt lines** — IRQ and NMI are not connected on the 6507 package.
- **Clock speed** ≈1.19 MHz.
- **Why**: a deliberate cost-reduction of the 6502 for a mass-market console, not a different instruction
  set — opcode-level disassembly (this project's `py65`-based work) is unaffected by any of the above; only
  the address space and interrupt behavior differ.

## RIOT (6532)

- 128 bytes of general-purpose RAM, two 8-bit I/O ports, one programmable timer.
- **Memory map**: RIOT RAM occupies **$0080-$00FF** (mirrored at $0180-$01FF); RIOT I/O and timer registers
  occupy **$0280-$0297**.

| Addr | Name | Function |
|---|---|---|
| `$0280` | **SWCHA** | joystick/controller data port — bits 4-7 = player 1, bits 0-3 = player 2 |
| `$0281` | SWACNT | port A data-direction register |
| `$0282` | **SWCHB** | console switches (difficulty, select, reset, color/B-W) |
| `$0283` | SWBCNT | port B data-direction register |
| `$0284` | **INTIM** | timer output — read to get the current countdown value |
| `$0294` | TIM1T | timer-interval write, 1-cycle prescaler |
| `$0295` | TIM8T | timer-interval write, 8-cycle prescaler |
| `$0296` | **TIM64T** | timer-interval write, 64-cycle prescaler |
| `$0297` | T1024T | timer-interval write, 1024-cycle prescaler |

Cross-checked this cycle (astro.physik.uni-potsdam.de, Wikipedia's "MOS Technology 6532" article, and the
cc65 toolchain's own RIOT struct layout). A joystick direction bit reads **0 when pressed**, 1 when not —
`$F0` (all four relevant bits high) is the standard "no direction pressed" idiom.

## TIA — the "racing the beam" registers

The TIA has no frame buffer. Code must write to its registers in sync with the television's own electron
beam position, scanline by scanline — this is the single most important context for reading any 2600
disassembly correctly, and the reason `py65` alone (no TIA/RIOT timing model) cannot fully verify
time-sensitive code, only its static control flow.

TIA **write** registers occupy **$0000-$002C** (a separate, smaller **read** register set exists at
$0030-$003D for input ports/collision detection, not used by this project yet; writes decode only the
bottom six address bits, so mirrored addresses behave identically). The full write-register list, cross-
checked this cycle against multiple independent sources (astro.physik.uni-potsdam.de's spec sheet,
hemulator.56k.guru, and the cc65 toolchain's own `atari2600.h`/`_tia.h` headers, derived in turn from
DASM's canonical `vcs.h`):

| Addr | Name | Addr | Name | Addr | Name |
|---|---|---|---|---|---|
| `$00` | VSYNC | `$10` | RESP0 | `$20` | HMP0 |
| `$01` | VBLANK | `$11` | RESP1 | `$21` | HMP1 |
| `$02` | **WSYNC** | `$12` | RESM0 | `$22` | HMM0 |
| `$03` | RSYNC | `$13` | RESM1 | `$23` | HMM1 |
| `$04` | NUSIZ0 | `$14` | RESBL | `$24` | HMBL |
| `$05` | NUSIZ1 | `$15` | AUDC0 | `$25` | VDELP0 |
| `$06` | COLUP0 | `$16` | AUDC1 | `$26` | VDELP1 |
| `$07` | COLUP1 | `$17` | AUDF0 | `$27` | VDELBL |
| `$08` | COLUPF | `$18` | AUDF1 | `$28` | RESMP0 |
| `$09` | COLUBK | `$19` | AUDV0 | `$29` | RESMP1 |
| `$0A` | CTRLPF | `$1A` | AUDV1 | `$2A` | HMOVE |
| `$0B` | REFP0 | `$1B` | **GRP0** | `$2B` | HMCLR |
| `$0C` | REFP1 | `$1C` | **GRP1** | `$2C` | CXCLR |
| `$0D` | **PF0** | `$1D` | ENAM0 | | |
| `$0E` | **PF1** | `$1E` | ENAM1 | | |
| `$0F` | **PF2** | `$1F` | ENABL | | |

`WSYNC` ($02) is a **strobe register**: the value written is irrelevant, only the write itself matters —
it halts the CPU until the next horizontal blank begins, the canonical scanline-synchronization idiom.
`PF0`/`PF1`/`PF2` ($0D/$0E/$0F) hold the 20-bit playfield bitmap; `GRP0`/`GRP1` ($1B/$1C) hold the two
"player" sprite bitmaps, commonly reused in homebrew tile-based games (not just for literal player
characters) to draw arbitrary per-scanline graphics strips.

**Direct application to this project's own disassembly**: `data/disassembly/2048-2600/`'s raw disassembly
of `$FC10`-`$FC52` (reached during this cycle's extended trace — see
`logs/2026-10-10-sq3-extended-trace-and-loop-periodicity.md`) shows a tight pattern of `STA $02` (WSYNC
strobes), `STA $0d`/`$0e`/`$0f` (zeroing PF0-PF2), and repeated `STA $1b`/`$1c` (writing GRP0/GRP1) inside
a loop reading tile data via indirect-indexed addressing (`LDA ($b0),Y` and four sibling pointers). This is
a direct, citable register-identity match, not a guess: **this is very likely this ROM's graphics/display
kernel** — a per-scanline rendering loop drawing the sliding-tile board via the player-sprite registers,
the single most canonical Atari 2600 programming pattern. Flagged as a plausible, well-motivated
interpretation (rung 2), not yet frame-accurate-confirmed, since `py65` has no TIA video model to visually
verify pixel output — the register-identity evidence is as strong as static analysis can get without one.

## Bank-switching

Not yet catalogued — `chesterbr/2048-2600`'s 2048-byte ROM fits entirely within the 6507's base 4KB cartridge
window (mirrored at both $F000-$F7FF and $F800-$FFFF, already established in
`logs/2026-10-09-sq1-toolchain-verification.md`) and needs no bank-switching. Deferred until a target ROM
that actually requires it is analyzed.

## Honest sourcing tier

All facts above are search-synthesis tier (WebSearch results cross-checked against multiple independent
secondary pages this cycle — astro.physik.uni-potsdam.de, dfarq.homeip.net, hemulator.56k.guru, and
cc65's own `atari2600_tia.inc` header constants, all agreeing). Not yet verified against a primary
datasheet (MOS Technology's own 6532/TIA documentation) — a reasonable future upgrade if any specific
register value ever becomes load-bearing for a claim, per this project's own evidence-ladder discipline.
