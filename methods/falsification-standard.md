# Evaluation and Verification Standard

This is the minimum bar for moving a disassembly or memory-map claim into `knowledge-base/state.md`'s Confirmed Findings. This project's domain is meaningfully different from the sibling history-mystery projects: ground truth is directly, mechanically testable. A disassembled ROM is a deterministic program — run it in an accurate emulator and its actual behavior is observable fact, not a matter of interpretation. The standard here is correspondingly sharper: **a claim is confirmed by a reproducible trace, not by how plausible the reading looks.**

## Minimum bar for a Confirmed Finding

Before a PR adds an entry to `knowledge-base/state.md`'s Confirmed Findings, it should have:

- confirmation the source ROM is rights-cleared per `data/rom-rights-scope.md` (SQ-1) — no finding about an out-of-scope ROM is accepted regardless of its technical merit;
- for a mechanical opcode-decode claim: the raw disassembly output itself, committed;
- for any claim beyond mechanical decode (what a routine does, what a memory address represents, a timing relationship to the TIA beam position, a bank-switching scheme): a reproducible emulation trace (register state, memory access log, or equivalent) committed alongside the claim, with enough provenance (exact ROM checksum, exact commit, exact trace command) that a third party could regenerate the same trace and get the same result;
- for anything cross-checked against existing public documentation: the specific source cited, and whether this project's own trace is consistent or inconsistent with it, disclosed either way.

## Required claim record

Before a disassembly/memory-map claim can be promoted, record:

1. **Claim** — the specific behavior asserted (what a routine does, what an address holds, a hardware-timing relationship), phrased narrowly enough to be wrong.
2. **Mechanism** — how the trace actually confirms it (what was logged, what the expected vs. observed values were).
3. **Alternatives considered** — at minimum, whether a simpler or different explanation for the same bytes was checked and ruled out by the trace, not just preferred on style grounds.
4. **Scope** — the exact ROM (name, checksum), the exact code region or memory address(es), and what wasn't checked (be explicit about gaps).
5. **Cross-check status** — whether this matches, contradicts, or adds to existing public documentation for the same ROM, where any exists.

## Evidence required for promotion

A claim can enter Confirmed Findings only when all of the following are present:

- a committed, reproducible trace that directly confirms the specific claim (not a general "the program ran without crashing");
- the ROM's rights status confirmed and disclosed;
- the exact commit/checksum/command needed to regenerate the trace;
- independent review by the other collaborator — at minimum, reproduction of the trace, or a documented reason reproduction wasn't possible (e.g. toolchain unavailable in that session).

## Automatic stop conditions

Do not promote a claim when any of these applies:

- no trace was run — the claim rests on reading the bytes and deciding what they "should" mean;
- the ROM's rights status wasn't verified before analysis began;
- the trace doesn't actually test the specific claim being made (e.g. confirming the program ran, but not confirming the specific register/memory behavior asserted);
- the claim contradicts an existing trace or existing public documentation and that conflict isn't disclosed and addressed;
- a copyrighted ROM binary would need to be committed to the repository to support the claim — move the analysis to local-only work instead, per `README.md`'s standing rule.

## Current consequence

At launch, the repository has no analyzed ROMs and no Confirmed Findings — this is a genuine bootstrap state. The first substantive work is the toolchain setup and ROM-rights scoping (`config/sidequests.md`, SQ-1), which is itself infrastructure, not a finding.
