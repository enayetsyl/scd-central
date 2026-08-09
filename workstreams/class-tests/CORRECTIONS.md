# CORRECTIONS.md — class-tests (CR-###, append-only)

Every teacher/Principal correction is logged here same-session (AGENTS.md §6). The agent
re-reads this ledger before drafting. 3+ occurrences of a pattern → mark **PATTERN** → propose
promotion to an executing gate. A fix applied to one artifact is checked across siblings the
same session.

| ID | Date | Artifact | Correction | Action taken | Status |
|---|---|---|---|---|---|
| CR-001 | 2026-08-09 | `C5_Bangla_ClassTest_Ch21` | Header carried a section letter (`৩গ`). No section letter; the CT number is a parameter, not prose. | `ct_docx.py --ct-number N` added; it rewrites the header line and renders the numeral in Bengali. Source md corrected to `৩`. | FIXED |
| CR-002 | 2026-08-09 | `C5_Bangla_ClassTest_Ch21` | Duration wrong: `৪৫ মিনিট`. Rule of record — 35 min standard for a 25-mark CT, 30 permitted, 35 maximum. Duration is config, not free text. | Verified at source first: **QuestionPolicy §৬ states no duration, and no MarkLogic file mentions one** — so the 45 had no canon backing. New canon **CD-021** + application note in QuestionPolicy §৬. `ct_docx.py --duration-min` added, default 35, **rejects anything outside 30–35**. Regenerated at ৩৫. | FIXED |
| CR-003 | 2026-08-09 | `C5_Bangla_ClassTest_Ch21` | Answer key item ১গ (প্রায় দুই লাখ) checked by the Principal against the source file. | No change needed — confirmed accurate against `canon/marklogic/C5_Bangla_Source_13-23.md` পাঠ ২১. Logged as verified. | VERIFIED |

## Sibling check (AGENTS.md §6)

CR-002 was checked across siblings the same session. **The two reference CTs at
`tools/render/reference/` (Ch19, Ch20) both read `৪৫ মিনিট` and are now non-conformant.** They
are authoring references, not canon and not issued papers. They need correcting or marking
superseded before they are used as a pattern again — raised in the CD-021 row and in
`tools/_wip/STATE.md`. **Not corrected unilaterally:** they are the reference set the generator
was authored against, so changing them is the Principal's call.

CR-001 does not affect the references — both use section letters (`৩ক`, `৩খ`) under the old
convention. If the no-section-letter rule is retrospective, they need the same fix; if it applies
only to new CTs, they stand as historical. Awaiting a word either way.
