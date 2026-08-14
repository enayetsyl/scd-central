# CORRECTIONS.md — support-books (CR-###, append-only)

<!-- CD-124: the prefix is what rows in this file ALREADY mint; the lane identifies this ledger. Declared now, renumbered per lane at close — no row is renumbered by this line. -->
<!-- ledger-prefix: CR -->
<!-- ledger-lane: support-books-corrections -->

Every teacher/Principal correction is logged here same-session (AGENTS.md §6). The agent
re-reads this ledger before drafting. 3+ occurrences of a pattern → mark **PATTERN** → propose
promotion to an executing gate. A fix applied to one artifact is checked across siblings the
same session.

| ID | Date | Artifact | Correction | Action taken | Status |
|---|---|---|---|---|---|
| CR-005 | 2026-08-09 | `letter_inventory_C1-BAN.json` পাঠ ৪৯, ৫১ | The master inventory held `glyphs: []` with **`needs_review: false`** — a positive, reviewed claim that **no conjunct is taught** at those পাঠ. The NCTB pages contradict it: printed p.72 teaches **ন্দ** (আনন্দ) and p.76 teaches **দ্দ** (চৌদ্দ) in their যুক্তবর্ণ শিখি boxes. | Caught by the freeze script's pre-write assertion, which compares each amendment's recorded `before` against the file on disk. The freeze therefore **overturns a recorded decision** rather than filling a blank — recorded as such in both amendments and in the frozen entries (`overturns` field). Principal-approved on the page derivation. | FIXED |
| CR-002 | 2026-08-09 | L002 patch note | The note claims the MOTOR sentinel covers 2/5/7/18/53. **L18 was built with real codes** (`১.১/৫.১/১৩.১`), not the sentinel — the note overstates its reach. | Correction logged now (Principal ruling Q-5): **the sentinel covers 2/5/7/53 only.** The note text is fixed at L002's next patch — the book is not churned for a comment. | LOGGED |
| CR-003 | 2026-08-09 | L009 · L024 · L026 | No `patch_C1-BAN_L0##` file in the export, though all three lessons exist in the book, carry images and validate. | No action (Principal ruling Q-4). Provenance note recorded: **"merged in chat era, patch file not exported."** Nothing reconstructed. | CLOSED |
| CR-004 | 2026-08-09 | L017 patches | `v2` dated 2026-07-28, `v3` dated 2026-07-18 — version number and date disagree. | Ruled by content (Principal ruling Q-3): **v2 is operative.** The book's `L017-b04` rhyme is **byte-identical to v2**; v3 carries an entirely different rhyme ("ছাতা মাথায় ঘরে ফিরি"), so the book was built from v2 and v3 is a superseded alternative that was mis-numbered. Only `source_note` differs between book and v2, added at merge. **Forward-only naming from here** — no renumbering. | RULED |
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
