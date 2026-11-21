# 2026-11-21 — SQ-1 bank-switching catalog from Stella source: precommitment self-review

Written BEFORE fetching any file.

**Known.** `data/hardware-reference.md` catalogs the 6507, RIOT and TIA but explicitly defers bank-switching
schemes (sidequests SQ-1 status). Prior cycles found egress blocked to most hosts. This cycle a probe showed
`raw.githubusercontent.com` returns HTTP 200 (a Stella source file), while en.wikipedia.org, www.voynich.nu and
arxiv.org are still refused (proxy 403).

**Not done.** No bank-switch hotspot addresses or bank sizes are recorded in the repo.

**Design.** Fetch source code only (never a ROM or binary) of Stella's `CartF8.cxx`, `CartF6.cxx`, `CartF4.cxx`
from the public stella-emu/stella repository. Extract, from the code itself, the hotspot address range and bank
size for each scheme. Cross-check internal consistency: bank size x bank count = ROM size, hotspots lie in the
$1FF4-$1FFB window used by F8/F6/F4, and the three schemes follow the arithmetic pattern implied by the code.
Non-circular: values come from the emulator's implementation, a primary technical source for what real
cartridges do, not from my memory; I state my memory-prediction first so a mismatch is visible.

**Prediction (from memory, to be checked).** F8: 8K, 2 x 4K banks, hotspots $1FF8-$1FF9. F6: 16K, 4 banks,
$1FF6-$1FF9. F4: 32K, 8 banks, $1FF4-$1FFB. Stella may express these as masks/offsets rather than literals.

**Honesty precommitment.** Report whatever the code shows including disagreement with the prediction; label the
tier as "emulator source code, one source" (not multiply cross-checked); no ROM data touched; append-only
corrections in state.md.
