# tools/audits — audit convention

- Repo-wide gate: `python tools/audits/canon_check.py` (run before any push touching canon/ or citations).
- Repo-wide gate: `python tools/audits/tools_check.py` (run before any push touching tools/).
  Canon is slot-and-cite, so canon_check asks *does the file exist*. Tools are executable, so
  existing proves nothing — tools_check asks *does it parse, and has it actually been run*.
  It reads `tools/MANIFEST.md` and enforces five things: REQUIRED files exist · no unslotted
  README placeholders · every .py compiles and every .js passes `node --check` · every folder
  with a REQUIRED row carries a **SMOKE.md** recording the command and its verbatim output ·
  `tools/hub-export/` carries a **VENDOR.md** naming upstream source and contract version
  (CD-003, supersede-only). Negative-tested 2026-08-09: all five FAIL paths fire, exit 1.
- Per-workstream gates live in `workstreams/<name>/audits/gates.py` — same pattern as
  EnglishDrive's run_all.py and P03's validate_plan.py: executed, verbatim output pasted,
  red gate returns the artifact to build phase (AGENTS.md §5).
- Gate reports may be committed under the workstream's `audits/reports/`.
