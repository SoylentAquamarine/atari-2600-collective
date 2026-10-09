# Meetings

Two recurring checkpoints, both logged permanently in this folder as
`YYYY-MM-DD-<type>-<n>.md` (append-only — a meeting file is never edited
after it's written; a correction is a new meeting entry that references
it). Use [`template.md`](template.md) for the format.

## Steering Committee Meeting

**Trigger:** every 5 rounds of comms exchange, OR whenever a hypothesis is
proposed for promotion to "Active Hypotheses," OR whenever either party
explicitly calls one.

**Purpose:** a short, frequent check-in. Not a status report — a working
session that answers the standing question directly: *how best can we get
to the bottom of this?* Are the two parties duplicating effort? Has
anything in comms surfaced a finding that should move to the knowledge
base? Should an agent role's scope be adjusted? Should a hypothesis be
retired?

**Attendees:** the lead agent (as coordinator + whichever agent role is
relevant), the auditor agent (same), and any registered contributor
(`CONTRIBUTING.md`) whose work is relevant to the agenda. The Skeptic
role's perspective must be explicitly represented in every steering
committee meeting, even if briefly — this is the mechanism that stops the
project from drifting toward a comfortable but unproven answer.

## Annual Meeting

**Trigger:** manually called by the user, or after a major milestone (a
hypothesis reaches "Confirmed Findings," or the group has been stuck on the
same open question across 3+ steering committee meetings). Not a literal
calendar-year cadence — it's the "zoom all the way out" review, called
whenever that's actually warranted.

**Purpose:** full retrospective across the entire `knowledge-base/state.md`,
not just recent rounds. Re-read every Confirmed Finding, Active Hypothesis,
and Rejected Hypothesis from scratch and ask: does this all still hold
together? Is there a rejected hypothesis that new findings should reopen?
Is there an agent role that's been idle and should be reassigned or
retired? What's the single highest-leverage open question to attack next?

## Standard agenda (both meeting types)

1. What's changed in the knowledge base since the last meeting? Check every new entry against `methods/falsification-standard.md`'s minimum bar — a script/manifest/cited protocol, its actual output committed, enough provenance to rerun it, and any secondary-source sourcing limitation disclosed plainly.
2. What did the comms log surface that hasn't been promoted to the knowledge base yet, and why not?
3. Skeptic's check: is anything being believed without having survived falsification?
4. **How best can we get to the bottom of this?** — concretely, what's the next highest-leverage action, and who (which role, which party) does it? Name the project's actual position on `config/research-department.md`'s evidence ladder and the single most direct blocker to the next rung — not just "what's interesting to try next."
5. **Efficiency check.** Name concretely, don't gesture at it: what work this cycle was started and then aborted or deferred after nontrivial effort — could a cheaper check have caught it sooner? What manual, repeated step could be scripted? Is any standing process parameter no longer well-calibrated to current conditions? Propose at least one concrete, testable change; the next meeting reports its measured effect and keeps, revises, or drops it. A meeting with nothing to report here should say so explicitly, not skip the item.
6. **Procedure check.** Did this cycle's work hit a real incident — a mistake, a near-miss, a process that broke or nearly broke — that `procedures/` doesn't yet cover? Does an existing procedure need updating because the situation it was written for changed? This is a mandatory check, not a mandatory action: per `procedures/README.md`'s own discipline, a procedure gets written from a real incident, not speculatively, so most meetings should genuinely find nothing to add. State plainly either way: "no incident this cycle warrants a new or updated procedure" is a complete, sufficient answer.
7. Decisions and action items, each assigned to a specific role/party.

This agenda, and the rest of this project's governance structure, is
carried over directly from the sibling projects in the same family (see
the hub repository, `research-collective-hub`, for the full family and its
shared conventions). Items 5 and 6 should genuinely find nothing to report
at Meeting #1, and that is the correct, honest answer, not a sign the check
is being skipped.
