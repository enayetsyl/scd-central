# tools/audits — audit convention

- Repo-wide gate: `python tools/audits/canon_check.py` (run before any push touching canon/ or citations).
- Per-workstream gates live in `workstreams/<name>/audits/gates.py` — same pattern as
  EnglishDrive's run_all.py and P03's validate_plan.py: executed, verbatim output pasted,
  red gate returns the artifact to build phase (AGENTS.md §5).
- Gate reports may be committed under the workstream's `audits/reports/`.
