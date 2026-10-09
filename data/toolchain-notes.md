# Toolchain notes

What's actually been verified working in this project's execution environment, with commands — not a
survey of what exists in general. See `logs/2026-10-09-sq1-toolchain-verification.md` for the full
verification method and result.

## Verified working (2026-10-09)

**`py65`** — a pure-Python 6502 microprocessor simulation package.

```
pip install py65
```

Confirmed correct on a hand-assembled, fully deterministic 9-byte test program: execution (`py65.devices.
mpu6502.MPU`, `.step()`) and disassembly (`py65.disassembler.Disassembler`, `.instruction_at(addr)`) both
produced exactly the expected register/memory state and mnemonic text, with zero discrepancy.

```python
from py65.devices.mpu6502 import MPU
from py65.disassembler import Disassembler

mem = bytearray(65536)
mem[0x0200:0x0209] = bytes([0xA9, 0x42, 0x85, 0x00, 0xA2, 0x07, 0x86, 0x01, 0x00])

mpu = MPU()
mpu.memory = mem
mpu.pc = 0x0200
for _ in range(4):
    mpu.step()
# mpu.a == 0x42, mpu.x == 0x07, mpu.memory[0x00] == 0x42, mpu.memory[0x01] == 0x07
```

**Scope of what this verifies**: base 6502 instruction-set execution and mechanical disassembly only.

## Known gap, not yet resolved

`py65` does not model the Atari 2600's TIA (video/audio) or RIOT (I/O/timer) hardware registers, or
anything about the 6507's specific pin/addressing differences from a stock 6502. This is sufficient for
`agents/disassembler.md`'s opcode-level work, but **not** sufficient for `agents/tia-specialist.md`'s
"racing the beam" timing analysis — that needs either a TIA-aware extension to this toolchain or a
different approach (e.g. a scriptable interface to the real Stella emulator, not attempted or confirmed
available in this environment yet). Flagged as the next toolchain gap to close, not solved here.

## Not yet done

ROM-rights scoping (which specific ROMs are legally analyzable) is a separate half of SQ-1, not addressed
by this toolchain check — see `rom-rights-scope.md` once it exists.
