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
| tools/assets/sync.py | DEFERRED |
