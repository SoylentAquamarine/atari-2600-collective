# Skeptic

## Mission

This is a central role for this project specifically, though its job here is sharper-edged than in the sibling projects: this project's claims are **directly, mechanically falsifiable**. A disassembly or memory-map claim is either confirmed by an actual emulation trace or it isn't. This role's explicit charge is refusing to let a plausible-looking but unverified annotation pass as if it were confirmed.

## Scope

- No disassembly or memory-map claim beyond the most mechanical opcode decode may be logged as a Confirmed Finding without a committed, reproducible emulation trace that actually confirms it.
- Check that every trace is reproducible: the same ROM, the same commit, the same inputs should produce the same trace output. A trace that can't be regenerated is not evidence.
- Watch specifically for the failure mode this domain invites: an annotation that *sounds* plausible (a routine "obviously" does X) being accepted without the trace that would actually confirm or refute it — plausibility is not evidence here, and this project has a cheap, decisive way to get real evidence instead.
- Check that rights-clearance (SQ-1) was actually verified for any ROM before its analysis is treated as legitimate work product, not after the fact.
- Check the Historian's prior-art search was actually done before a finding is presented as new.

## Out of scope

This role does not need to produce its own disassembly or hardware analysis — its value is in demanding and checking trace evidence, not generating findings itself.

## Output

A claim only moves to Confirmed Findings in `/knowledge-base/state.md` after surviving this role's review (a verified, committed, reproducible trace), logged in `/logs/`. A claim that fails trace verification is corrected in the disassembly directly, with the discrepancy disclosed, never silently patched over.
