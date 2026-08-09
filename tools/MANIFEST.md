# tools/MANIFEST.md — machine-readable tool index (read by tools_check.py)

Status: REQUIRED (vendored and in use — check fails if missing or unproven) ·
PENDING (Step 2 slot, warn until vendored) · DEFERRED (deliberately not vendored; no warn).

A tool is not "done" when it is placed. It is done when it has been **run**, with the command
and its verbatim output recorded in a `SMOKE.md` beside it (AGENTS.md §5 — gates are executed,
never reasoned). `tools_check.py` enforces that for every REQUIRED row.

Add a row when a tool is vendored. Node scripts get rows once their filenames are known.

| tools/audits/canon_check.py | REQUIRED |
| tools/audits/tools_check.py | REQUIRED |
| tools/hub-export/validate_import.py | REQUIRED |
| tools/hub-export/import-contract.schema.json | REQUIRED |
| tools/hub-export/LOCKED_C5_PlanSchema_v1.json | REQUIRED |
| tools/hub-export/LOCKED_QuestionPayload_Schema_v1.json | REQUIRED |
| tools/hub-export/LOCKED_StimulusPayload_Schema_v1.json | REQUIRED |
| tools/hub-export/build_envelope.py | REQUIRED |
| tools/hub-export/build_question_envelopes.py | REQUIRED |
| tools/render/render_plan.py | PENDING |
| tools/images/apply_strips.py | PENDING |
| tools/assets/sync.py | DEFERRED |
