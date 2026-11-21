# 2026-11-21 — SQ-1 bank-switching second batch: execution / result

Fetched (source only, no ROM bytes) from raw.githubusercontent.com, stella-emu/stella master, `src/emucore/`:
Cart3F, CartE0, CartFE, CartF8SC, CartF6SC, CartF4SC (.cxx/.hxx). All HTTP 200.

**Result vs. prediction.**
- 3F: held. Two 2K segments; last segment fixed to last 2K of ROM; any write to $00-$3F (the TIA address window, claimed
  by the cart) selects the first-segment bank as `value % bankCount`. Header: Tigervision used 8K, scheme supports up to 512K.
- E0: held. Four 1K segments; $1FE0-$1FE7 / $1FE8-$1FEF / $1FF0-$1FF7 select the bank (`address & 7`) for segments 0/1/2;
  segment 3 fixed to last 1K. Not predicted: Stella's non-random power-on default is banks 4/5/6 in segments 0/1/2.
- FE: prediction (trigger via stack-area address, not a plain hotspot read) held in spirit but was imprecise. Actual:
  the cart watches for an access to $01FE; the *next* access latches the data-bus value and sets bank = (value>>5) ^ 7.
  Stella comments say only the lowest bit effectively matters (all known carts have 2 banks; validated for Space Shuttle,
  "not validated with a real cartridge"), and note a Decathlon boot-vector quirk. Original design: up to 8 x 4K banks (patent, as paraphrased in the header).
- SC variants: held. F8SC/F6SC/F4SC = F8/F6/F4 banking unchanged plus 128 bytes RAM (`RAM_SIZE = 0x80`, mask 0x7F);
  header comment gives write port $1000-$107F, read port $1080-$10FF.

Tier: emulator source (one source); the FE bank-select rule is explicitly flagged by its own comments as not validated on real hardware. Not cross-checked against a second source.
No claim from earlier cycles changed.
