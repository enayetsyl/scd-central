# tools/MANIFEST.md — machine-readable tool index (read by tools_check.py)

Status: REQUIRED (vendored and in use — check fails if missing or unproven) ·
PENDING (Step 2 slot, warn until vendored) · DEFERRED (deliberately not vendored; no warn).

A tool is not "done" when it is placed. It is done when it has been **run**, with the command
and its verbatim output recorded in a `SMOKE.md` beside it (AGENTS.md §5 — gates are executed,
never reasoned). `tools_check.py` enforces that for every REQUIRED row.

Add a row when a tool is vendored. Node scripts get rows once their filenames are known.
**Rows are executable tools only** — fonts and data are not listed here; a REQUIRED row obliges
its folder to carry a `SMOKE.md`, which is meaningless for a font file. Font presence is
asserted at runtime instead: `ct_docx.py` and `glyph_probe.py` both exit with an error if the
configured font is absent.

⚠️ **Known gate blind spot.** `tools_check.py` warns on a PENDING row whose file is *missing*,
but says nothing about a PENDING row whose file is *present yet unproven* — the warn simply
disappears when the file lands. `tools/render/render_plan.py` is in exactly that state today:
vendored, never executed. Read PENDING as "not proven", and check `SMOKE.md` for what a folder
actually claims. Tightening the gate to catch this is an open item in `tools/_wip/STATE.md`.

| tools/audits/canon_check.py | REQUIRED |
| tools/audits/tools_check.py | REQUIRED |
| tools/hub-export/validate_import.py | REQUIRED |
| tools/hub-export/import-contract.schema.json | REQUIRED |
| tools/hub-export/LOCKED_C5_PlanSchema_v1.json | REQUIRED |
| tools/hub-export/LOCKED_QuestionPayload_Schema_v1.json | REQUIRED |
| tools/hub-export/LOCKED_StimulusPayload_Schema_v1.json | REQUIRED |
| tools/hub-export/build_envelope.py | REQUIRED |
| tools/hub-export/build_question_envelopes.py | REQUIRED |
| tools/render/ct_docx.py | REQUIRED |
| tools/render/glyph_probe.py | REQUIRED |
| tools/render/render_plan.py | PENDING |
| tools/images/apply_strips.py | PENDING |
| tools/assets/sync.py | DEFERRED |
