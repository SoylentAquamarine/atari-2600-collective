# 2026-11-21 — SQ-1 bank-switching catalog, third batch (FA, E7, F0, 3E, DPC): execution

Fetched (source only, HTTP 200 each, stella-emu/stella master `src/emucore/`): CartFA, CartE7, CartF0, Cart3E, CartDPC `.cxx/.hxx`. No ROM bytes. Single source (Stella); not cross-checked.

| Scheme | Prediction | Found | Verdict |
|---|---|---|---|
| FA | 12K, 3x4K, $1FF8-$1FFA, 256 B RAM write $1000-$10FF / read $1100-$11FF | Held. Start bank 2. **Disclosed discrepancy:** header says bit D0 of the value must be 1 for the switch to fire, but the D0 test in `checkSwitchBank` is commented out in the code, so Stella switches on any access to $1FF8-$1FFA. | held + discrepancy noted |
| E7 | 16K, 2K segments, $1FE0-$1FE7 ROM select, $1FE8-$1FEB RAM select, last 2K fixed | Mostly held. Correction to my memory: $1FE8-$1FEB pick one of four **256-byte** RAM blocks shown at $1800-$19FF (write $1800-$18FF, read $1900-$19FF), not a 1K bank. $1FE7 maps 1K RAM into $1000-$17FF (write $1000-$13FF, read $1400-$17FF). Variants 8K/12K/16K (4/6/8 banks); last 2K cannot be mapped into the lower window. | partly wrong (RAM granularity), recorded |
| F0 | 64K, 16x4K, single hotspot $1FF0 increments bank | Held: access to exactly $1FF0 -> `(bank+1) & 0xF`; start bank 15 (not predicted). | held |
| 3E | 3F plus RAM; $3F ROM bank, $3E RAM bank; up to 512K ROM | Held: $3F=ROM bank of value into first 2K segment, $3E=RAM bank (value + romBankCount); 32 x 1K RAM banks (32K), RAM write port in high half; last 2K fixed. | held |
| DPC | 8K ROM + 2K display, F8 hotspots, DPC at $1000-$107F | Held: inherits F8 ($1FF8/$1FF9); read port $1000-$103F, write port $1040-$107F; register decoded as index=addr&7, function=(addr>>3)&7; 10K image default; header cites US Patent 4,644,495. Register-by-register map not extracted (out of scope this batch). | held |

Honest limits: single source; FA header/code disagree (recorded, not resolved); DPC register semantics not catalogued.
