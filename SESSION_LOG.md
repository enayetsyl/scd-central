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

## 2026-08-09 · tools (Step 2 opened) · Principal · cowork
- Did: Built Step 2's gate before vendoring anything. Created `tools/MANIFEST.md` and
  `tools/audits/tools_check.py`, and **negative-tested it** — all five FAIL paths fire and exit 1.
  Fixed a false positive in `canon_check.py` (its PLACEHOLDER scan now skips `tools/audits/*.py`,
  since gate scripts must carry the marker as a string literal); regression-checked that it still
  catches a genuine placeholder. Amended `AGENTS.md` to **v1.1** on the Principal's approval.
  Opened `tools/_wip/STATE.md` as Step 2's state file; `canon/_wip/STATE.md` is now closed Step 1
  history and points to it.
- Decisions logged: **CD-009** (tools_check.py + tools/MANIFEST.md; standing rule — *a tool is
  done when it has been run, not when it has been placed*; `tools/assets/sync.py` marked DEFERRED;
  canon_check scanner fix recorded) · **CD-010** (AGENTS.md v1.0→v1.1: §5 now requires tools_check
  before any push touching `tools/`, and states the run-not-placed rule with its SMOKE.md
  evidence requirement — protocol tightened, nothing loosened) · **CD-011** (standing instruction
  for the next session: the deferred CD-008 script guard is written **from the actual harness
  code**, cross-checked against the SB validator's list, and **any disagreement comes to the
  Principal as a PENDING-P item — never silently merged**).
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 4 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 7 warn)**. All warns are unvendored Step 2 slots, i.e. the work itself.
- Open items / PENDING-P raised: none new. ⚠️ The **SB validator's list named in CD-011 is not in
  this repo** and must be supplied with the harness — flag it if it does not arrive. Carried
  forward: PENDING-P-001, F-2. Next session: **hub-export first**, then the CD-008 script-guard
  row under the CD-011 rule.

## 2026-08-09 · tools/hub-export + canon/language · Principal · cowork
- Did: Vendored `tools/hub-export/` — 8 files from `scd-hub` under import contract LOCKED v1.0
  (2026-06-09) — with `VENDOR.md`, `SMOKE.md` and a real index README. **Smoke-tested, not just
  placed:** conformant envelope → PASS exit 0; seeded-error envelope → FAIL exit 1 (3 fails).
  Ran the CD-011 cross-check and wrote `canon/language/LANGUAGE_RULES.md` §7 (script guard) from
  the ruling. The 5 support-books files from the same drop stay in `_inbox/` for Step 3, unmoved.
- Decisions logged: **CD-012** — script guard is canon in three tiers: Arabic RED anywhere in any
  string · arrows/emoji/symbol glyphs RED in rendered text fields, GREY in metadata · em-dash and
  ellipsis ALLOWED, WATCH counter retained one term. The old SLOT summary was **wrong on three of
  its four items** and each is corrected in the row; only the Arabic item survives, strengthened.
  **CD-013** — the harness's missing charset check is logged as **UP-001** in
  `tools/hub-export/UPSTREAM_ISSUES.md` for `scd-hub`'s own D-series, **not patched locally**
  (supersede-only, CD-003). PENDING-P-002 ruled and closed.
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 3 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 5 warn)**. Both remaining sets are the unvendored render/images/assets slots.
  The gate's SMOKE.md and VENDOR.md requirements were live — hub-export would have failed without
  them, which is the point of CD-009.
- Open items / PENDING-P raised: **PENDING-P-003** — CD-012 makes Arabic script RED everywhere,
  but this is an Islamic school: `workstreams/islamic-studies/` (C1–C5) and the Arabic subject
  named in REF-1 §1.2 will need Qur'anic ayat, hadith and du'a in Arabic script. Per CD-013 the
  cause is renderer glyph support, not doctrine, so the fix is likely fonts in the Hub renderer
  rather than banning Arabic from Islamic content. Non-blocking today — nothing is authored in
  islamic-studies yet. Also carried: **UP-001** (upstream), and the **WATCH counter review** at
  one term's end. Next: `tools/render/` (item 2), where the smoke test must be a real .docx
  render, not a `--help`.
