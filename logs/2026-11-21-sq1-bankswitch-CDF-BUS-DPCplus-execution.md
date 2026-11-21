# 2026-11-21 — SQ-1 batch 6 (CDF/CDFJ/CDFJ+, BUS, DPC+): execution

Source: Stella `CartCDF/CartBUS/CartDPCPlus .cxx/.hxx` (source text only, raw.githubusercontent.com; downloaded to scratch, not committed; no ROM or ARM firmware bytes). Single-source tier, not cross-checked. Precommit `logs/...-CDF-BUS-DPCplus-selfreview.md` pushed first.

## Results
| Scheme | Banks / start | Bank hotspots | Layout |
|---|---|---|---|
| DPC+ | 6 x 4K program banks, starts in bank 5 | $1FF6-$1FFB -> banks 0-5 | 32K image: first 3K = ARM driver; 8K Harmony RAM = 3K driver + 4K display data + 1K frequency table; DPC regs $1000-$107F (read $1000-$103F, write $1040-$107F); 8 data fetchers, 3 music channels, 32-bit LFSR RNG, optional fast fetch |
| CDF / CDFJ | 7 x 4K, starts bank 6 | $1FF5-$1FFB -> banks 0-6 (hotspot $1FF4 aliases bank 6 in CDF) | 32K ROM + 8K RAM (2K driver, 4K display, 2K C vars/stack); 32 fast fetchers, 2 fast-jump queues, 1 parameter queue, 3-channel digital audio. Registers at $1FF0 DSWRITE, $1FF1 DSPTR, $1FF2 SETMODE, $1FF3 CALLFN |
| CDFJ+ | 7 x 4K, starts bank 0 | $1FF4-$1FFA -> banks 0-6 ($1FFB -> bank 0) | larger ROM (64-512K) / RAM (16/32K) on LPC213X-class hardware; optional LDX#/LDY# fast-fetch override; configurable fetcher base offset |
| BUS ("bus stuffing") | BUS1+: 7 x 4K, starts bank 6; BUS0: 6 banks, starts bank 5 (unsupported by Stella) | BUS1+: $1FF5-$1FFB -> banks 0-6; BUS0: $1FF6-$1FFB -> banks 0-5 | 2K driver (BUS0: 3K) + 4K display RAM + C vars/stack; communication stream $1010, jump stream $1011; ARM injects values onto the 6502 data bus; fast jump BUS3 only; BUS3 extra registers $1FEE-$1FF3 (AMPLITUDE, DSREAD, DSWRITE, DSPTR, SETMODE, CALLFN). Header marks BUS EXPERIMENTAL / may be removed |

## Prediction check (from the precommit)
- DPC+ 6 banks at $1FF6-$1FFB: **held**. "8K ARM driver": **wrong** (3K driver inside an 8K RAM). 4K display + 1K freq tables: held. Start bank 5 not predicted.
- CDF 7 banks, $1FF5-$1FFB: **held** (CDF/CDFJ); I did not predict the CDFJ+ shift to $1FF4-$1FFA.
- BUS "$1FF6-$1FFC?": **wrong** (BUS1+ is $1FF5-$1FFB; BUS0 is $1FF6-$1FFB, 6 banks). Subtype split (BUS0-3) unpredicted.
Datastream register details (increments, music fetchers) were not transcribed beyond the register names above; Thumb ARM driver behavior is out of scope.
