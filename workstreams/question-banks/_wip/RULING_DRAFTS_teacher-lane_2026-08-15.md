# Two ruling rows — DRAFTS for the Principal's next approval

**Status: DRAFT. NOT FILED. NOT NUMBERED.** Nothing in this file is in force. `CD-14x` is a
placeholder — **the next free number is verified at source at filing time, never carried from a
draft** (AGENTS §4), because a number reserved in a draft is a number two sessions can both claim.

**Autonomy begins only when (a) is filed.** Until then every push needs explicit approval with a
per-commit range check (AGENTS §3.1, CD-083(b)).

---

## Draft (a) — CD-14x · TEACHER-LANE STANDING AUTHORIZATION

**Ruled (proposed):** an agent session working the **bank-authoring lane** may commit and **push
without per-commit approval**, under every condition below, all of which must hold at once.

**(a) SCOPE IS BY COMMIT CLASS, not by intent.** Pre-approved classes: **build** (authoring items),
**corrections** (ledger rows), **log** (STATE.md, SESSION_LOG.md), **promotion** (a signature row
quoting its signer). **Not pre-approved and never inside this lane:** ruling · gate · tools · canon
· anything touching `AGENTS.md`, `canon/`, `tools/` or a policy file.

**(b) SCOPE IS BY PATH, and the two must agree.** Files under `workstreams/question-banks/` and
`workstreams/question-banks/banks/envelopes/` only. **A commit whose class is pre-approved but
whose path is not, or the reverse, is not authorized** — the agent stops. Two independent
statements of the same boundary, because one of them will eventually be wrong.

**(c) THE GATE CONDITION IS THE WHOLE SUITE, CLEAN, INCLUDING `PLAN` AND `ENVELOPE-SYNC`.** Not
"the gates that apply", not "CLEAN apart from". **A gate reporting `N/A` is not CLEAN for this
purpose** — N/A means the gate did not judge, and an unjudged bank is exactly what this
authorization must not let through. Verbatim output is pasted in the session report as always.

**(d) `PLAN` IS THE COUNTERSIGN.** The plan table the Principal used to sign before authoring is
replaced by the gate; see draft (b). **This is the substantive trade:** the Principal stops signing
arithmetic and keeps signing judgement.

**(e) ANYTHING ELSE → STOP AND REPORT. Never ask the teacher.** The teacher is a zero-Git operator
(AGENTS §2) and cannot rule. **A question put to someone who cannot answer it is not a question, it
is a way of proceeding without one** — and `QB-CR-013` is the recorded instance of an agent reading
an answer about mechanics as an answer about substance. That row is the reason this clause is
written in the imperative.

**(f) WHAT IS NEVER PRE-APPROVED, restated because these are the ones a session will be tempted
by:** a new gate or a change to one · a policy edit · a decision row · a `_inbox/` classification ·
anything on the mounted drive · **a `git reset` or any history rewrite, pushed or not** · promotion
to `gold`, which is a Hub act and not a Git state (CD-003).

**(g) REVOCATION IS UNILATERAL AND NEEDS NO ROW.** The Principal withdraws this by saying so.
**The agent does not get to argue the conditions were met.**

**(h) EVERY PUSH UNDER THIS ROW STILL REPORTS** — per-commit range check with class stated, and the
post-push verification of AGENTS §3.1 including `git ls-remote`. **Autonomy removes the wait, not
the account.**

---

## Draft (b) — CD-14x · §6 RELOCATION: WHERE HUMAN REVIEW ACTUALLY SITS

**Ruled (proposed):** AGENTS §6's human review splits into three, and each half goes where it can
actually be done.

**(a) ITEM-LEVEL CONTENT REVIEW → HUB SUBJECT EXPERTS.** Whether a question is good, whether a
teacher-supplied key is right, whether a stem is age-appropriate for the class. **This never
belonged to the Principal alone and it does not scale to him** — CD-136(g) named him because the
Hub review lane did not exist yet, not because the judgement is his by nature.

**(b) PLAN-LEVEL COUNTERSIGN → THE `PLAN` GATE.** Floors with margin, per-slot demand, task
declarations, P-037 types, near-duplicate stems. **All of it is arithmetic over the register and
the bank**, which is why a gate can hold it and why a human holding it was spending judgement on
counting.

**(c) THE PRINCIPAL RETAINS, and this is the shorter list on purpose:** rulings and decision rows ·
gate and tooling changes · canon and policy · debugging when a gate is wrong · promotion
`reviewed → gold` · revocation of any authorization.

**(d) WHAT MOVES IS THE VENUE, NOT THE STANDARD.** CD-136(b)'s teacher-key rule is unchanged; what
changes is who reads it. **A rule enforced by a different human is not a weakened rule** — and
CD-136(e) already settled that a human is the right enforcer here, because a gate cannot see the
thing it judges.

**(e) THE BORDERLINE BAND IS THE HANDOFF, and it is deliberate.** `PLAN` REPORTS stem pairs at
85–95% rather than failing them, precisely so a subject expert sees the per-word drills and rules
on them. **The gate hands over what it cannot decide instead of guessing or going quiet** —
SOURCE_POLICY §7.17 in a new place.

**(f) ONE THING THIS DOES NOT DO.** It does not make the Hub review a precondition for a push under
draft (a). Banks reach the Hub as `draft`; the expert read happens there. **Coupling the two would
make every push wait on a human in a different system, which is the wait this session exists to
remove.**

---

## What the Principal should weigh before filing

**On (a): the boundary is drawn twice — class AND path — and that is not belt-and-braces.** A
promotion-class commit to `canon/` and a canon-class commit to `banks/` are both plausible agent
errors, and either single test would let one through.

**On (a)(c): `N/A` is excluded from CLEAN, and it matters more than it reads.** Eight gates report
N/A on every qp6 bank because they read the other shape. The clause means *no gate that SHOULD
judge returned N/A* — if a future bank shape silently makes `PLAN` or `ENVELOPE-SYNC` N/A, the
authorization lapses rather than passing quietly. **Worth confirming that is the intended reading.**

**On (b): PLAN's 40-item floor is now a structural fact about every chapter bank.** Margin ≥ 2 on
four positive floors requires 0.80n + 8 ≤ n. পাঠ ১৩ at 110 is clear; a thin chapter is now required
to grow before it can be signed at all. **That is a real curriculum consequence of a gate rule and
the Principal may want it stated in the row rather than discovered by a session.**

**On both: `QB-CR-013` is one instance, not three.** AGENTS §6 promotes a pattern to a gate at
three. **These rows expand agent autonomy while the ledger's only entry about agent judgement is a
single instance** — defensible, and worth being deliberate about rather than incidental.
