# SQ-2 — TIA/6507 timing arithmetic cross-check — execution

Script: `data/scripts/tia_timing_arithmetic.py`; output: `data/scripts/tia_timing_arithmetic-output.txt`.

**Result (prediction held on every item):** 76 CPU cycles/line (228 divides evenly by 3), 19,912 cycles/frame,
frame rate 59.923 Hz, CPU clock 1.1932 MHz (matches the ~1.19 MHz in `data/hardware-reference.md`), 25 three-cycle
`STA zp` per line (1 cycle left over), visible window = 53.33 CPU cycles (so the CPU cannot be cycle-aligned to
every visible pixel — consistent with why kernels lean on WSYNC and the HM* fine-motion registers).

**Caveats:** constants (3.579545 MHz, 228 clocks, 68/160 split, 262 lines) are from recall, not freshly fetched or
cited; the only independent check is agreement with the pre-existing ~1.19 MHz line. Internal-consistency
evidence only; promote to verified only after a fetched citation. No ROM touched.

**Proposed next step:** fetch a primary reference (Stella Programmer's Guide) to cite the constants, then use the
budget to check the sprite-multiplexing entry's cycle claims.
