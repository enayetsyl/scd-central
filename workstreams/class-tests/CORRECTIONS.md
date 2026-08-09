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

## Sibling check (AGENTS.md §6) — RULED 2026-08-09, CD-023

CR-002 was checked across siblings the same session. The two reference CTs at
`tools/render/reference/` (Ch19, Ch20) both read `৪৫ মিনিট`.

**Ruling: do not edit them.** They are the historical record of class tests actually given — an
imported reference corpus, not live templates. They are marked **"FORMAT reference only"** in
`tools/render/README.md`, `tools/render/SMOKE.md` and `tools/render/reference/README.md`: the
time line is superseded by CD-021 and **must never be copied**. The generator's 35-minute config
default is the living rule; **the references teach structure, not time.**

CR-001 resolves the same way: the references' `৩ক`/`৩খ` headers stand as historical, and the
header on any new CT comes from `--ct-number`, never from them.

## Acceptance

`ct_docx.py` **ACCEPTED** by the Principal 2026-08-09 on the regenerated Ch21 PDF (CD-023).
All three corrections above are closed.
