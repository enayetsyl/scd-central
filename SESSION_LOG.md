# SESSION_LOG.md — Principal's oversight feed (append-only)

One block per agent session, appended at "save state and sync". Format:

## YYYY-MM-DD · <workstream> · <operator: teacher/Principal> · <tool: cowork/code/codex>
- Did: …
- Decisions logged: …
- Gates run + result: …
- Open items / PENDING-P raised: …

## 2026-08-09 · canon (Step 1 canon extract) · Principal · cowork
- Did: Read AGENTS.md + SLOTTING_CHECKLIST.md; `git pull` clean. Created `_inbox/` staging
  (gitignored) and `canon/_wip/STATE.md`. Slotted 10 of 11 canon rows — the 7 MarkLogic files
  (v১ 08-08-2026), REF-1 Curation Policy v1.2 LOCKED, REF-2 Content Register (REF-20 Approved
  Names Pool v1.0), and a REF-1-derived IMAGE_RULES.md. Flipped 10 MANIFEST rows PENDING→REQUIRED;
  replaced 4 SLOT READMEs with real indexes; corrected two stale descriptions in canon/README.md.
  Source files were **moved**, not copied, out of `_inbox/` so the gate's NO-COPY rule holds.
- Decisions logged: CD-004 (MarkLogic slot; the checklist's "fix Rules §6 — ENG/MATH spines DO
  exist" needed no action, v১ already lists all five spines) · CD-005 (v1.2 is the operative
  REF-1; the "v1.0, 11 C-codes, S1–S4, SB-016" description was stale — 19 categories C-01…C-19,
  three annotation tags, no severity scheme, flag/monument ruling is C-18) · CD-006 (REF-20 IS
  REF-2; the recurring-cast reference-sheet claim withdrawn as storybook material) · CD-007
  (IMAGE_RULES is REF-1-derived only; stripe / largest-being / carve-out / photocopy-safe /
  silhouette ruled out of scope and recorded in the file so they are not re-applied by assumption).
- Gates run + result: `python tools/audits/canon_check.py` run four times — after setup, after
  the MarkLogic slot, after REF-1/REF-2, and before this commit. Final: **CLEAN (0 fail, 6 warn)**,
  down from 20 warns at session start. Remaining: 2 for row 11 (unslotted by design) and
  4 for `tools/` (Step 2). Byte sizes verified identical to the supplied files; all CD citations
  resolve at source; `_inbox/` empty of source files.
- Open items / PENDING-P raised: **PENDING-P-001** — REF-1 v1.2 governs Class 1 Bangla/English
  only; how are C2–C5 and other subjects governed meanwhile? Default in use: cite REF-1 only
  inside its declared scope, flag out-of-scope citations. Also open, non-blocking: MarkLogic
  Rules §6 does not list `C5_Bangla_Source_13-23.md`, now canon (left as supplied — canon content
  changes are the Principal's). **Step 1 is not closed:** row 11 LANGUAGE_RULES remains a traced
  draft in `canon/_wip/` with three gaps (Hub renderer script guard — blocked behind Step 2;
  swarabritta spec; সাধু-vs-চলিত).

## 2026-08-09 · canon (Step 1 close) · Principal · cowork
- Did: Slotted the last canon row — `canon/language/LANGUAGE_RULES.md` — and replaced the
  language SLOT README with a real index. MANIFEST is now **13 REQUIRED, 0 PENDING**.
  Ticked Step 1 in `SLOTTING_CHECKLIST.md` (file kept; Steps 2–5 are live).
  Both `_wip/` drafts removed on promotion.
- Decisions logged: **CD-008** — (a) সাধু/চলিত: school-authored text is always চলিত, সাধু source
  texts are quoted verbatim, and every question, instruction, mark scheme and answer key about
  them is written in চলিত; (b) Bengali swarabritta rhyme spec out of scope until a workstream
  writes verse; (c) Hub renderer script guard deferred to Step 2 — it lands with the LOCKED
  import contract at `tools/hub-export/` as its own CD row, and **no script guard may be
  asserted as canon until then**.
- Gates run + result: `python tools/audits/canon_check.py` → **CLEAN (0 fail, 4 warn)**.
  All four remaining warns are `tools/` placeholders, i.e. Step 2 work. Every canon warn is gone.
- Open items / PENDING-P raised: none new. **Step 1 is CLOSED.** Carried forward, not blocking:
  PENDING-P-001 (REF-1's Class-1-only scope) and F-2 (MarkLogic Rules §6 does not list
  `C5_Bangla_Source_13-23.md`). `canon/school-facts/SCHOOL_FACTS.md` remains a Principal-completed
  stub by design — it already passes REQUIRED. Next: **Step 2 — tools**, where `tools/hub-export/`
  also unblocks the deferred script-guard CD row.
