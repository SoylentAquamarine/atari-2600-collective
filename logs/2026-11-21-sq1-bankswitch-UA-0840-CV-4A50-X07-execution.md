# 2026-11-21 — SQ-1 bank-switching catalog, fourth batch (UA, 0840, CV, 4A50, X07): execution

Fetched (source only, HTTP 200 each, stella-emu/stella master `src/emucore/`): CartUA, Cart0840, CartCV, Cart4A50, CartX07 `.cxx/.hxx`. No ROM bytes. Single source (Stella); not cross-checked.

| Scheme | Prediction | Found | Verdict |
|---|---|---|---|
| UA | 8K, 2x4K, hotspots $0220/$0240 | Held. $0220 -> bank 0, $0240 -> bank 1 (decode `addr & 0x1260`); UASW variant swaps. Header also mentions Brazilian shifted addresses $02A0/$02C0 and other aliases (not independently verified in code read). Titles named: Funky Fish, Pleiades. | held |
| 0840 | 8K, 2x4K, access below $1000 | Held: decode `addr & 0x1840`; $0800 -> bank 0, $0840 -> bank 1; hotspot pages $0800-$0FFF forwarded to TIA/RIOT. Prediction of "address bits" was vague; actual rule is that single mask. | held (vague prediction) |
| CV | 2K ROM + 1K RAM; RAM write $1400, read $1000 | Partly verified: RAM is 1K (`RAM_SIZE=0x400`), write-protect-high flag set, ROM <=2K image tiled into second half of 4K window, 4K images carry initial RAM contents in first 1K. Exact write/read port addresses not read from code this batch (they come from the CartridgeEnhanced base class); my $1400/$1000 prediction is unconfirmed. | partly confirmed, port addresses unverified |
| 4A50 | 128K ROM + 32K RAM, complex | Held in outline: 128K ROM, 32K RAM; three windows ($1000-$17FF 2K, $1800-$1DFF 1.5K, $1E00-$1EFF 256 B), last 256 B ($1F00-$1FFF) always last ROM page. Switching is triggered by a prior-data pattern (`(lastData & 0xE0)==0x60` with prior address >= $1000 or < $200) plus hotspots in $0C00-$0Fxx, and by zero-page writes ($74-$7F range etc.). Stella states it is not fully implemented (hires helpers, $1E00 page wrap missing; only one test ROM). Full hotspot map not transcribed. | held (low-confidence prediction; map incomplete) |
| X07 | 64K, hotspots below $1000 | Held: bank = `(addr & 0xF0) >> 4` when `(addr & 0x180F)==0x080D`; further rule for banks 0xE/0xF via `(addr & 0x1880)==0` bit 6. | held; 14/15 sub-rule noted |

Honest limits: single source; CV port addresses and full 4A50 map not extracted; UA aliases taken from a header comment, not code-verified; 4A50 is explicitly partial in Stella.
