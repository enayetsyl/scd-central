# tools/MANIFEST.md — machine-readable tool index (read by tools_check.py)

Three states of proof, not two (CD-020):

| Status | Means | Gate behaviour |
|---|---|---|
| `PENDING` | not vendored | WARN while missing; WARN if the file turns up, because the row is then stale |
| `VENDORED-UNPROVEN` | present, never executed | WARN until the file is named in its folder's `SMOKE.md`; FAIL if the file is missing |
| `REQUIRED` | proven | FAIL if missing, **or if no `SMOKE.md` in its folder names it** |
| `DEFERRED` | deliberately not vendored | silent |

The middle status exists because the old two-state scheme went silent at exactly the wrong
moment: a PENDING row's warn vanished the instant the file appeared, so a vendored-but-never-run
tool looked identical to a proven one.

A tool is not "done" when it is placed. It is done when it has been **run**, with the command
and its verbatim output recorded in a `SMOKE.md` beside it (AGENTS.md §5 — gates are executed,
never reasoned). `tools_check.py` enforces that for every REQUIRED row.

Add a row when a tool is vendored. Node scripts get rows once their filenames are known.
**Rows are executable tools only** — fonts and data are not listed here; a REQUIRED row obliges
its folder to carry a `SMOKE.md`, which is meaningless for a font file. Font presence is
asserted at runtime instead: `ct_docx.py` and `glyph_probe.py` both exit with an error if the
configured font is absent.

A `SMOKE.md` line that names a file **and** contains the word `UNPROVEN` counts as an explicit
declaration that the tool has *not* been run — it does not satisfy REQUIRED, and it does not
trigger the "promote me" warn on a VENDORED-UNPROVEN row.

| tools/audits/canon_check.py | REQUIRED |
| tools/audits/tools_check.py | REQUIRED |
| tools/audits/source_check.py | REQUIRED |
| tools/audits/source_textcheck.py | REQUIRED |
| tools/audits/math_arith_check.py | REQUIRED |
| tools/audits/bangla_script_check.py | REQUIRED |
| tools/audits/grid_count_check.py | REQUIRED |
| tools/audits/ledger_check.py | REQUIRED |
| tools/audits/state_check.py | REQUIRED |
| tools/audits/int_id_check.py | REQUIRED |
| tools/audits/slot_register_check.py | REQUIRED |
| tools/hub-export/validate_import.py | REQUIRED |
| tools/hub-export/import-contract.schema.json | REQUIRED |
| tools/hub-export/LOCKED_C5_PlanSchema_v1.json | REQUIRED |
| tools/hub-export/LOCKED_QuestionPayload_Schema_v1.json | REQUIRED |
| tools/hub-export/LOCKED_StimulusPayload_Schema_v1.json | REQUIRED |
| tools/hub-export/build_envelope.py | REQUIRED |
| tools/hub-export/build_question_envelopes.py | REQUIRED |
| tools/render/ct_docx.py | REQUIRED |
| tools/render/glyph_probe.py | REQUIRED |
| tools/render/render_plan.py | REQUIRED |
| tools/images/apply_strips.py | REQUIRED |
| tools/images/make_strips.py | REQUIRED |
| tools/images/verify_strip.py | REQUIRED |
| tools/images/crop_edges.py | REQUIRED |
| tools/images/pick_placements.py | VENDORED-UNPROVEN |
| tools/run_all.py | REQUIRED |
| tools/subject_search.py | REQUIRED |
## DEFERRED rows — carrying their reason and their trigger

A `DEFERRED` row is silent to the gate by design, so the row itself has to say **why** it is
deferred and **what would end the deferral**. Without both, "deferred" and "forgotten" are the
same row. These rows take two extra cells; `tools_check.py` anchors on the first two only.

| Tool | Status | Deferred because | Trigger — what un-defers it |
|---|---|---|---|
| tools/assets/sync.py | DEFERRED | **Deferred by design at migration Step 2.** Large binaries (book images, scans) live on Google Drive via rclone and are deliberately not in this repo; nothing in the repo consumes an asset through a wrapper today, so there is no script to vendor and no smoke to record. R2 is a storefront concern and belongs to the storybook venture's own repo (AGENTS.md §1, absolute no-crossover). | **Either of:** (a) **storybook asset sync** becomes real work in a lane that lives here; or (b) **first use of rclone** by anything in this repo. On either, this row goes `PENDING` → `VENDORED-UNPROVEN` → `REQUIRED` with a `tools/assets/SMOKE.md`. |

**Why the placeholder was retired (Principal ruling 2026-08-14, session-2 ruling 7).**
`tools/assets/README.md` carried the `NOT YET SLOTTED` marker, which made `canon_check.py` and
`tools_check.py` each emit a PLACEHOLDER warn on **every run, in every session, for a month**.
**A warning that has fired every session for a month has stopped conveying information** — it is
read as furniture, and the next real placeholder warn arrives into a report where warns are
already ignored. The deferral was never in doubt; only its record was in the wrong shape. The
state is now a row that says what it is, and the warn is gone because the condition is gone.

**Resolved — this note can now quote the marker it retires (CD-089).** At first writing it could
not: the `PLACEHOLDER` check had **no backtick exemption**, so naming the string here re-fired the
warn on this file, and both retirement notes had to be written *around* the marker. That was raised
rather than patched, and the Principal ruled the principle up instead of down: it is now
**AGENTS.md §5.1**, a gate-design rule every new gate is checked against, and the exemption applies
here. **Three sites, one rule** — `SOURCE_POLICY` §7.16 (Assamese script) · CD-085 (REF-CITE's
retired-number census) · CD-089 (PLACEHOLDER, both repo-wide gates).
