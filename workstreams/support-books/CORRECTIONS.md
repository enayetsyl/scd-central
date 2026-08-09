# CORRECTIONS.md — support-books (CR-###, append-only)

Every teacher/Principal correction is logged here same-session (AGENTS.md §6). The agent
re-reads this ledger before drafting. 3+ occurrences of a pattern → mark **PATTERN** → propose
promotion to an executing gate. A fix applied to one artifact is checked across siblings the
same session.

| ID | Date | Artifact | Correction | Action taken | Status |
|---|---|---|---|---|---|
| CR-001 | 2026-08-09 | C1-BAN / L53 | L53 carried empty competency/outcome codes — validator CHECK 3 and CHECK 10 red. | Applied the **MOTOR sentinel**, verified at source rather than invented: the L002 patch carries `["MOTOR"]` and its note records the Principal ruling (option (i)) covering all six no-outcome পাঠ — 2/5/7/18/53. Checks 3 and 10 now PASS. | FIXED |

## Sibling check (AGENTS.md §6)

CR-001's sentinel is described in the L002 note as covering six পাঠ (2/5/7/18/53). **Checked
all six against the book, and the note does not match the build:**

| পাঠ | Codes in the book |
|---|---|
| 2, 5, 7 | `["MOTOR"]` — sentinel, as the note describes |
| 18 | `["১.১","৫.১","১৩.১"]` / `["১.১.১","৫.১.১","১৩.১.১"]` — **real codes, not the sentinel** |
| 53 | was empty; now `["MOTOR"]` |

So L18 was built with real codes rather than the sentinel. That does not affect L53 — 53 is the
creativity strand alongside 2/5/7 — but **the L002 note overstates the ruling's reach**, and
anyone reading it would expect a MOTOR at L18 that is not there. Raised as **Q-5**; the note is
left as written, since patch files are the historical record (CD-023 principle).

No lesson now has empty codes.
