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
- Per-extraction gate: `python tools/audits/source_check.py <extraction.md>` — executes
  `canon/sources/SOURCE_POLICY.md` §5 (range · spine slots · page monotonicity against the
  recorded offset · spot-check sign-off). Written 2026-08-09 with the first extraction under
  that policy, closing SOURCE_POLICY §6. `--selftest` runs five seeded errors plus a clean
  control; every seed must turn the gate red. **SIGNOFF reports PENDING, never PASS-by-agent**
  — only the Principal or the teacher can close it, and the exit code stays non-zero until
  they do, so an unsigned extraction cannot be mistaken for a done one.
- Cross-channel check: `python tools/audits/source_textcheck.py <extraction.md> <book.pdf> --pages A-B`
  (PDF page numbers) — executes `SOURCE_POLICY.md` §7.3. Raster transcription is the one step
  with no machine check on it, so this decodes the PDF's text layer independently and diffs the
  two letter-streams. It scores readings against the **system** English word list, never the
  extraction's own words, or the check would confirm whatever the extraction said. Needs
  `hunspell-en-us` and exits with a message rather than guessing without it. `--selftest` runs
  twelve real decode cases plus gap-finder controls. A DISAGREE is never authority to change
  the extraction: go back to the raster (CD-047).
- Per-workstream gates live in `workstreams/<name>/audits/gates.py` — same pattern as
  EnglishDrive's run_all.py and P03's validate_plan.py: executed, verbatim output pasted,
  red gate returns the artifact to build phase (AGENTS.md §5).
- Gate reports may be committed under the workstream's `audits/reports/`.
