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

## 2026-08-09 · canon (scope + Arabic rulings) · Principal · cowork
- Did: Wrote two rulings into canon and swept every file that contradicted them. **CD-014**
  (Arabic) restated `LANGUAGE_RULES.md` §7 tier 1 as a capability rule with its two lift
  conditions, and recorded the binding position in `workstreams/islamic-studies/LOCAL.md`
  (cited, not restated). **CD-015** (scope) corrected four files still asserting Class-1 scope —
  `canon/islamic-curation/README.md`, `canon/README.md`, `IMAGE_RULES.md` §7,
  `LANGUAGE_RULES.md` §5 — and marked the class-list line in `SCHOOL_FACTS.md` as load-bearing.
  Froze `canon/_wip/STATE.md` with a banner: it narrates PENDING-P items as open and would
  otherwise be read as current.
- Decisions logged: **CD-014** — tier 1 stands for every current workstream (Arabic RED
  anywhere); ground is renderer capability, not doctrine; it lifts **per render path** on
  (1) an executed Arabic-shaping smoke test — real ayah, eyeball-verified, RTL + joining
  correct, no tofu — and (2) verbatim quoted source with `source_note` provenance reviewed in
  the **আলিম lane**, never model-composed, never transliteration-round-tripped; until both hold,
  drafts use Bangla + transliteration with an **`ARABIC-SLOT`** placeholder. **CD-015** — REF-1
  governs the **whole school**, all current classes, extending automatically by one class each
  year (C6 in 2027, through C10); the class list is read from `SCHOOL_FACTS.md` and restated
  nowhere; this **overrides REF-1 v1.2 §1.2**, which is LOCKED and deliberately not edited;
  and above Class 1, a category not yet written is **not** a permission — unclear cases escalate
  via REF-1 §4.5.
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 3 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 5 warn)**. Both sets are the unvendored render/images/assets slots.
- Open items / PENDING-P raised: none. **The PENDING-P queue is empty — 0 OPEN.** Carried,
  non-blocking: **UP-001** (scd-hub's missing charset check, upstream's to fix); the **WATCH
  counter review** at one term's end; **F-2** (MarkLogic Rules §6 does not list
  `C5_Bangla_Source_13-23.md`). `SCHOOL_FACTS.md` is now load-bearing for two of these.
  Next: `tools/render/` — real .docx render as the smoke test, and the CD-014 Arabic-shaping
  proof can be run in the same session while the fonts are in hand.

## 2026-08-09 · canon (F-2 + SCHOOL_FACTS v1.0) · Principal · cowork
- Did: Added `C5_Bangla_Source_13-23.md` to `MarkLogic_Rules.md` §6, closing F-2. Replaced the
  `SCHOOL_FACTS.md` v0.1 stub with the Principal-completed **v1.0**. Verified the flagged
  class-test line at source before writing it.
- Decisions logged: **CD-016** (F-2 closed; the Principal's English description was rendered into
  plain Bengali to match the file's register per LANGUAGE_RULES §1 — and because the "→" in the
  supplied wording is a tier-2 arrow, RED in rendered text under CD-012) · **CD-017**
  (SCHOOL_FACTS v1.0: curation scope fixed at C1–C5 with Nursery/KG permanently outside; academic
  year 2026; weekly pattern; C6 opens January 2027. **Class-test marks verified at source: 25**,
  stated three times in `MarkLogic_QuestionPolicy.md`. The v0.1 stub's "20–30 band" has **no canon
  source at all** and is superseded, not reconciled).
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 3 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 5 warn)**.
- Open items / PENDING-P raised: **PENDING-P-004** — self-checking my own edit against CD-012
  surfaced that the guard's tiers are field-typed (`text_bn`/`text_en`/titles vs metadata), which
  are support-book **JSON** fields with no meaning in a .md file. Under the strict reading canon
  violates canon: `MarkLogic_Rules.md` carries 🔴 🟦 ★ ↑ ↓ as teacher-facing legend notation and
  `C5_Bangla_Source_13-23.md` tags lessons 🟦★. Default meanwhile, noted in LANGUAGE_RULES §7:
  the guard applies to **Hub-bound JSON payload strings only**. **This bears on the render smoke
  test** — §7 conformance must not be asserted on .docx output until it is ruled. Both
  SCHOOL_FACTS load-bearing lines are now live: WATCH review dated **mid-December 2026**.

## 2026-08-09 · canon/language (guard scope) · Principal · cowork
- Did: Rewrote `LANGUAGE_RULES.md` §7's domain note from an open question into a settled scope
  principle, and wrote the render smoke-test spec into `tools/_wip/STATE.md`.
- Decisions logged: **CD-018** — the script guard governs **strings that enter a mechanical
  render path** (today Hub-bound JSON payloads and support-book JSONs), and **extends
  automatically to any new path when that path is vendored** — so vendoring `tools/render/`
  pulls the docx path under it with no further ruling. **Human-read markdown is out of scope**:
  canon files, teacher-facing tables and legend notation (🔴 🟦 ★ ↑ ↓) stand, since editors and
  GitHub display them and no tofu risk exists where no renderer runs. **Each render path proves
  its own glyph set empirically**, recorded in that path's `SMOKE.md`. If the legend glyphs tofu
  in the docx chain, **CT templates must not carry them — a finding to report, not a canon
  change.** PENDING-P-004 closed.
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 3 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 5 warn)**.
- Open items / PENDING-P raised: none. **Queue empty — 0 OPEN.** The `tools/render/` smoke
  document is now specified: Bengali numerals, the legend glyphs, em-dash and ellipsis, plus
  **যুক্তবর্ণ and কারচিহ্ন** — added because conjuncts and combining vowel signs are the real
  Nikosh/Noto shaping risk and a font can pass every named glyph while breaking হ্ম or ৌ.
  Evidence must come from the **rasterised pdftoppm page, not the .docx XML**: a correct
  codepoint in the XML can still render as a box, which is precisely what this test exists to
  catch. Carried: **UP-001** (upstream), **WATCH review** mid-December 2026.

## 2026-08-09 · tools/render (Step 2 item 2) · Principal · cowork
- Did: Vendored `tools/render/` — 6 fonts (Regular + Bold only; Naskh Medium/SemiBold skipped),
  `render_plan.py`, and the two reference CTs. **Authored `ct_docx.py`**, a class-test
  Markdown→.docx generator with font family as configuration that routes every character to a
  font which actually covers it. Promoted `glyph_probe.py` out of `_wip`. Ran both smoke tests
  end-to-end and recorded the proven glyph set in `tools/render/SMOKE.md`.
- Decisions logged: **CD-019** — R-2 (fonts as supplied; **no Nikosh**, so printed CTs will not
  match the NCTB face, accepted) and R-1 (`✅`→`✓`, `⚠`→`দ্রষ্টব্য:`, `✓` kept and routed to an
  explicit symbol run; `→` routed by the same mechanism, an extension of that ruling).
  Proven glyph set: Bengali, Arabic-with-harakat, em-dash/ellipsis and Latin all render;
  **🔴 🟦 ✅ ⚠ tofu and must not appear in CT templates** (constrains templates, not canon).
  **CD-014 condition (1) SATISFIED for the docx path** — ayah rendered, RTL + joining + harakat
  eyeball-verified on the raster; condition (2) is a human gate and stays open, so
  `islamic-studies` remains on `ARABIC-SLOT`.
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 2 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 3 warn)**. `tools_check` went **red once during the work** — it demanded a
  `SMOKE.md` for `fonts/` after font rows were added to the tool manifest. Correct behaviour:
  fonts are data, not tools. Rows removed; the manifest now states rows are executable tools
  only, and font presence is asserted at runtime by the scripts instead.
- Open items / PENDING-P raised: none for the Principal. Three carried in
  `tools/_wip/STATE.md`: (1) **`render_plan.py` is vendored but UNPROVEN** — no P03 plan JSON,
  never executed, row left PENDING; (2) **⚑ gate blind spot** — `tools_check.py` warns when a
  PENDING file is missing but goes silent once it is present-yet-unrun, so a vendored-but-unproven
  tool gives no signal at all; proposed fix is a third status, not implemented because changing
  gate semantics is a decision row, not a quiet edit; (3) **Nikosh absent** — if NCTB-matching
  print matters, sourcing it means re-proving the path, since CD-018 proves per render path.
  Also recorded: **fonts must be installed via `fc-cache`, not merely vendored** — LibreOffice
  substituted silently on the first run and would have passed a careless reading.

## 2026-08-09 · tools/audits (manifest taxonomy) · Principal · cowork
- Did: Added the third manifest status `VENDORED-UNPROVEN` to `tools_check.py` and rewrote the
  `tools/MANIFEST.md` header to define all four states. Negative-tested every new path in a
  scratch repo before touching the real manifest.
- Decisions logged: **CD-020** — `PENDING` = not vendored · `VENDORED-UNPROVEN` = present but
  never executed · `REQUIRED` = proven · `DEFERRED` = deliberately absent. VENDORED-UNPROVEN
  warns until a `SMOKE.md` run names the file and FAILs if the file is missing; PENDING now also
  warns when the file is *present* (stale row); and **REQUIRED now FAILs unless a `SMOKE.md` run
  names the file**. A `SMOKE.md` line naming a file that also contains "UNPROVEN" is read as an
  explicit non-proof declaration — without that rule the naive substring match reported
  `render_plan.py` as proven by the very sentence saying it was not.
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 2 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 8 warn)**. `canon_check` went **red once, correctly** — it caught CD-020 as a
  phantom citation because the gate code cited the row before the row existed. Row written, then
  green. The CD-CITE check earning its keep on its author.
- Open items / PENDING-P raised: none for the Principal. Applying the new status honestly
  **reclassified four `tools/hub-export` rows** — `build_envelope.py`,
  `build_question_envelopes.py`, and the plan + question payload schemas — which held REQUIRED
  despite that smoke run exercising only the *stimulus* path. Together with `render_plan.py`,
  five rows now warn accurately instead of passing silently. All five close at **Step 4
  (lesson-plans)**, when a real plan/question artifact exists to run through them.

## 2026-08-09 · tools/images (Step 2 close) · Principal · cowork
- Did: Vendored `tools/images/` — `apply_strips.py`, `make_strips.py`, `crop_edges.py`,
  `pick_placements.py` — as neutral tooling. **Wrote `verify_strip.py`**, because the expected
  pdftoppm verification helpers did not arrive and do not exist: none of the four scripts touches
  pdftoppm. Smoke-tested the whole pipeline on a synthetic fixture with a **known** being region.
  **Step 2 is CLOSED.**
- Decisions logged: **CD-022** — images vendored and proven; `verify_strip.py` authored here
  because without a checker `apply_strips.py` could only be shown to run, not to place the band
  correctly, which is not proof. Boundary restated: CD-007 keeps the stripe *doctrine* out of
  school canon — this folder is mechanism only. `tools/assets/` stays DEFERRED.
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 1 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 7 warn)**. The single canon warn is the deferred `assets/` placeholder; six of
  the seven tools warns are VENDORED-UNPROVEN rows warning correctly.
- Open items / PENDING-P raised: none for the Principal. Measurements: band centre **0.460 against
  0.460 requested**, inside the being region; no-living-being images copied through
  **byte-identical** (silent re-encoding would degrade artwork every run); three negative tests
  fire red. **Calibration recorded rather than tuned away** — feathered strip ends make the
  measured span read ~2% inside the requested one, so tolerance 0.03 works and below ~0.025 fails
  on correct geometry. `pick_placements.py` is VENDORED-UNPROVEN and **cannot** be proven
  headlessly (interactive tkinter GUI, no display) — that closes only in a human session.
  Six VENDORED-UNPROVEN rows now stand; five close together at **Step 4**.

## 2026-08-09 · acceptance + retention · Principal · cowork
- Did: Closed R-2 on the Principal's confirmation of the Ch21 PDF. Marked the two reference CTs
  **FORMAT reference only** without editing them — in `tools/render/README.md`, `SMOKE.md` and a
  new `tools/render/reference/README.md`. Applied the render-artifact retention rule: committed
  `tools/images/evidence/` (fixture before/after + `placements.json`) and untracked the three
  Ch21 verification rasters.
- Decisions logged: **CD-023** — `ct_docx.py` ACCEPTED, R-2 closed; reference CTs are the
  historical record of tests actually given, an imported corpus and not live templates, so they
  are **never edited** — their `৪৫ মিনিট` is superseded by CD-021 and must never be copied.
  *The references teach structure, not time.* Same principle covers their `৩ক`/`৩খ` headers.
  **CD-024** — evidence stays, scratch goes: anything a `SMOKE.md` cites as proof is committed
  permanently under an `evidence/` folder; regenerable rasters under `_wip/` are gitignored.
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 1 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 7 warn)**. The single canon warn is the deferred `assets/` placeholder.
- Open items / PENDING-P raised: none. Applying CD-024 surfaced that **the strip proof existed
  only in sandbox scratch** and would have been lost at session end — `tools/images/SMOKE.md`
  described a visual check with nothing durable behind it. Now committed and cited. One judgement
  recorded in the row: **teacher-facing deliverables are not scratch** — the Ch21 `.md`, `.docx`
  and `.pdf` stay committed, because teachers are zero-Git operators (AGENTS.md §2) and cannot
  regenerate them. Next: **Step 3 — support-books**, files already in `_inbox/`.

## 2026-08-09 · support-books (Step 3) · Principal · cowork
- Did: Imported the whole SB corpus into `workstreams/support-books/` — 54-পাঠ book, 55 patches,
  5 governance files, letter inventory, 2 whitelist candidates, skeleton/TG/word-map references,
  the compliant image set, the validator report, 3 validators. Wrote `audits/gates.py`, filled
  `LOCAL.md`, created `REVIEW_QUEUE.md` (আলিম lane) and `CORRECTIONS.md`, flipped REGISTRY to
  **LIVE**. Ran L53 through steps 7–8; **step 9 merge withheld on a red gate.**
- Decisions logged: **CD-025** — import + LIVE, book unmerged, findings recorded.
- Gates run + result: `audits/gates.py` — selftest **16/16 PASS**, then book validation
  **RED=5 GREY=4 PASS=12, VERDICT FAIL**. L53's own two reds (CHECK 3, CHECK 10) are **fixed**;
  the five remaining are L52's and pre-date this work. Repo gates: `canon_check.py` →
  **CLEAN (0 fail, 1 warn)**; `tools_check.py` → **CLEAN (0 fail, 7 warn)**.
- Open items / PENDING-P raised: **six batched questions** in the workstream STATE. The load-bearing
  one: **the supplied validation report's "letter audit clean" cannot be reproduced against the
  master inventory** — পাঠ 52's whitelist is `glyphs: null`, and null means no conjunct is legal
  (B-1), so L52 red-fails. Of the four enumerated whitelist entries only **পাঠ 45 is
  Principal-approved**; 49, 51 and 52 are still `needs_review: true` — and 52 is exactly what the
  L53 merge waits behind, so freezing would approve three unreviewed entries. Not done without a
  ruling. Also: L017 v2 is dated *newer* than v3 (version and date disagree); DECISIONS imported
  at D-019 against a registry claim of D-021+; L009/L024/L026 have no patch file though the
  lessons exist; and the L002 MOTOR note claims a reach it does not have — **L18 was built with
  real codes, not the sentinel**.

## 2026-08-09 · support-books (Step 3 rulings) · Principal · cowork
- Did: Applied five of six rulings. Reconstructed **D-021** and recorded **D-020** as a gap;
  settled the **L017** version conflict by content; logged provenance and correction rows
  (CR-002…CR-004); annotated the imported validation report in place without editing its body.
  **The L53 merge is still withheld.**
- Decisions logged: **CD-026** — see the row for each ruling's outcome.
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 1 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 7 warn)**. `audits/gates.py` not re-run — nothing changed in the book, and
  the freeze that would change the result is blocked.
- Open items / PENDING-P raised: **Q-1 is blocked — `_inbox/Class 1 Bangla.pdf` does not exist**,
  and no PDF is anywhere in the workspace. Nothing was derived: the ruling makes the page the
  authority, so a list from memory would defeat the check it was meant to be. **Q-7** raised —
  D-020 has zero citations anywhere, so its row records the gap rather than inventing a decision.
  ⚠️ **The reply's renumbering displaced one open item**: the original **Q-6 — do canon rules beat
  the imported governance files where they overlap? — was never answered**, and is carried
  forward on its working default (canon wins, as recorded in LOCAL.md).

## 2026-08-09 · support-books (Q-6, Q-7) · Principal · cowork
- Did: Ruled the last two open items. **Q-6** — added canon-precedence banners to
  `governance/README.md` and `governance/SCHEMA_support-book_v1.md`, naming each overlapping
  section and the canon file that supersedes it; nothing was edited out. **Q-7** — filled the
  reserved **D-020** row and added **RQ-003** to the reviewer queue.
- Decisions logged: **CD-027** (canon beats the imported governance files on overlap; overlapping
  sections are superseded-by-citation and marked with a pointer, not deleted) · **CD-028**
  (D-020 reconstructed and filled; supersedes the gap wording written under CD-026).
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 1 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 7 warn)**. `audits/gates.py` not re-run — the book is unchanged and the freeze
  that would change its result is still blocked.
- Open items / PENDING-P raised: none new. **All batched questions are now closed except Q-1**,
  which is ruled but blocked on `_inbox/Class 1 Bangla.pdf`. Two things worth recording:
  the D-020 citations were **verified at source before the row was written** — AGENTS.md §4 applies
  to Principal-supplied citations too — and all three (L003, L004, L006) resolved, with L003 the
  fullest ("NOT applied here — flagged as S4 governance/আলিম question, পাঠ ৩ kept compliant
  all-boys pending any recorded DECISIONS.md amendment"). ⚠️ **One correction to the ruling:**
  D-020 was *not* already listed in the reviewer queue — that file held only RQ-001 and RQ-002 —
  so it was added as **RQ-003** rather than assumed present.

## 2026-08-09 · support-books (freeze + merge) · Principal · cowork
- Did: Read NCTB pages from the supplied PDF, derived the three conjunct whitelists, froze all
  four approved amendments into `letter_inventory_C1-BAN.json`, re-ran the gate, and **completed
  step 9 — L53 is merged.** Closed the Q-6 report-annotation loop.
- Decisions logged: **CD-029** — whitelists frozen for পাঠ ৪৫/৪৯/৫১/৫২; **standing derivation
  method now canon: the যুক্তবর্ণ শিখি box is the taught set, and running-text conjuncts are never
  whitelisted by mere appearance.**
- Gates run + result: `audits/gates.py` — selftest **16/16 PASS**, book **RED=0 GREY=4 PASS=13,
  GREEN**. Evidence saved to `books/C1-BAN/reports/GATE_C1BAN_post-L53-merge_2026-08-09.txt`.
  `canon_check.py` → **CLEAN (0 fail, 1 warn)**; `tools_check.py` → **CLEAN (0 fail, 7 warn)**.
  `canon_check` went **red once, correctly** — CD-029 was cited in the inventory and the report
  before the row existed; the CD-CITE check caught the phantom, and the row was written.
- Open items / PENDING-P raised: none. Two findings worth the record. **(1)** The PDF is a scan
  with no text layer, so pages were rasterised and read visually, and the printed-folio offset
  (+9) was verified rather than assumed. **(2)** The freeze **overturned a recorded decision**:
  পাঠ ৪৯ and ৫১ held `glyphs: []` with `needs_review: false` — a positive *reviewed* claim that no
  conjunct is taught, contradicted by the pages. The freeze script's pre-write assertion caught it
  and refused to write until it was reconciled; recorded in the amendments, in the frozen entries
  and as **CR-005**. Nothing silently overwritten. Next: **Step 4 — lesson-plans**, which also
  closes five of the six VENDORED-UNPROVEN rows.

## 2026-08-09 · lesson-plans (Step 4) · Principal · cowork
- Did: Imported the P03 quartet, four plan artifacts, three C3 Packs, three handoffs and
  `validate_plan.py`. Ran the **full proof chain** on every plan JSON. Filled `LOCAL.md`, added
  canon-precedence banners to all four quartet files, flipped REGISTRY to **LIVE**.
- Decisions logged: **CD-030** — import, schema diff, proof chain, and the three row flips.
- Gates run + result: `validate_plan.py` **4/4 PASS**; byte-identical re-render **3/4**;
  `build_envelope.py` **3/3 EXIT=0**; `validate_import.py` **3/3 PASS (0 warn, 0 advisory)**.
  `canon_check.py` → **CLEAN (0 fail, 1 warn)**; `tools_check.py` → **CLEAN (0 fail, 4 warn)**.
  Both repo gates went **red once each, correctly**: `tools_check` caught me flipping two rows to
  REQUIRED while the SMOKE.md section had silently failed to land (a bad anchor), and
  `canon_check` caught CD-030 as a phantom citation before its row was written.
- Open items / PENDING-P raised: **six questions batched** in the workstream STATE. The
  load-bearing one: **the D-PROJ03 register cannot safely be continued** — the body ends at
  **042**, while **043 and 044 are cited as applied** in three quartet files but were never
  written; six handoffs independently claimed 045. Nothing was minted. Also: the **schema diff is
  byte-identical**, so no escalation, and `audits/` uses **symlinks** rather than copies so a
  LOCKED contract cannot diverge. **`LOCKED_C5_BAN_U20_ChapterPlan_v3.md` is red at the
  re-render gate by exactly one byte** — `re-render == locked + b"\n"`, the only one of four
  missing its terminal newline, so artifact-side not renderer-side; stopped, not normalised.
  **Only three of the five VENDORED-UNPROVEN rows could flip** — Step 4 supplied **no question
  artifact**, so `build_question_envelopes.py` and the question payload schema stay unproven.

## 2026-08-09 · lesson-plans (register + supersede) · Principal · cowork
- Did: Reconstructed **D-PROJ03-043/044/045** from their application citations and minted
  **046** for the U20 supersede. Produced **U20 ChapterPlan v4** (identical content + terminal
  newline), archived v3, and re-ran its full chain — it now joins the proven set. Wrote the
  Plans-only scope line into LOCAL.md.
- Decisions logged: **CD-031** — register reconstruction, the U20 supersede, and the scope line.
- Gates run + result: v4 chain — `validate_plan` **PASS (0 warn)** → **byte-identical re-render**
  → `build_envelope` EXIT=0 → `validate_import` **PASS (0 warn, 0 advisory)**. `canon_check.py` →
  **CLEAN (0 fail, 1 warn)**; `tools_check.py` → **CLEAN (0 fail, 4 warn)**.
- Open items / PENDING-P raised: two briefs given to the Principal, awaiting ruling — the
  **no-version-bump OVERRIDE** and the **B-LP.1c contradiction**. One finding worth recording:
  **of the six independent 045 claims, exactly one had actually been applied** — the C1 MATH U13
  5-period re-cut that supersedes D-044's 8-period v2 and retires its S07–S08 locks. It takes 045
  on its own row rather than being folded into 044; the other five mint nothing. All four plan
  artifacts are now proven end-to-end.

## 2026-08-09 · lesson-plans (OVERRIDE ruling) · Principal · cowork
- Did: Recorded the C2 MATH U05 override ruling as **D-PROJ03-047** and folded
  `D-PROJ03-OVERRIDE-2026-07-26` into the numbered sequence, so nothing sits outside it. Register
  now continuous to **D-047**; new work continues at 048. REGISTRY and LOCAL.md updated.
- Decisions logged: **CD-032** — the ruling in full, with its execution explicitly marked owed.
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 1 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 4 warn)**. No chain run: there was no artifact to run.
- Open items / PENDING-P raised: ⛔ **D-PROJ03-047's execution is blocked — the C2 MATH U05
  Chapter Plan is not in this repo, in either byte-set.** Step 4 imported no C2 MATH artifact at
  all, so v3 could not be cut from the current bytes and the pre-override bytes could not be
  archived or declared lost. **Nothing was fabricated and no archive was claimed that does not
  exist** — the ruling itself warned against exactly that. On import the sequence is: cut v3 →
  archive-or-declare-lost the pre-override set → run v3 through the full chain. **B-LP.1c**
  remains the one open brief awaiting a ruling.

## 2026-08-09 · lesson-plans (D-047 executed) · Principal · cowork
- Did: Classified the surviving C2 MATH U05 copy, archived it, recorded the counterpart lost, and
  parked D-PROJ03-047. Verified archive integrity. Wrote
  `reports/D047_CLASSIFICATION_2026-08-09.txt`.
- Decisions logged: **CD-033** — classification, the failed reconstruction test, and the outcome.
- Gates run + result: archive integrity — `validate_plan` **PASS (0 warn)**; re-render differs on
  **exactly one line of 168**, the renderer's own provenance stamp. `canon_check.py` →
  **CLEAN (0 fail, 1 warn)**; `tools_check.py` → **CLEAN (0 fail, 4 warn)**. No chain run for a v3
  — no v3 was cut.
- Open items / PENDING-P raised: **Q-7** — **D-049 is cited throughout P03 but belongs to the
  master D-series (D-001–D-051), and that register is not in this repo**, so no master citation is
  resolvable here. Not a P03 reconstruction candidate; a missing-register gap one level up.
  Outcome of D-047: the surviving bytes are **pre-override** (`footer.version_log` absent, dated
  2026-06-21, zero occurrences of the override date), and **the record nowhere states what the
  override changed** — so the post-override bytes are **recorded lost**, no v3 cut, nothing
  fabricated. **B-LP.1c** remains the last open brief.

## 2026-08-09 · lesson-plans (Step 4 close) · Principal · cowork
- Did: Resolved **B-LP.1c** (D-PROJ03-048) and imported `PROJECT00_DECISIONS.md` as a read-only
  reference (D-PROJ03-049). Updated LOCAL.md, STATE.md and REGISTRY provenance. **Step 4 CLOSED.**
- Decisions logged: **CD-034** — both rulings, the register state, and the import's real scope.
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 1 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 4 warn)**. `canon_check` went red once, correctly, catching CD-034 as a phantom
  citation before its row was written — the third time this session that check caught its author.
- Open items / PENDING-P raised: ⚠️ **The imported register is not the one the citations need.**
  `PROJECT00_DECISIONS.md` is Project 00's **local** log (`D-PROJ00-###`, 72 rows); its own
  §"Relationship to the master decision log" states the initiative-wide **D-001…D-053 live in
  `PROJECT00_README.md` §3**, which was not supplied. All **17** `D-PROJ00-###` citations in the
  P03 files resolve cleanly; the **master citations remain unresolvable**. Also surfaced: **bare
  `D-0NN` is ambiguous** — `D-049` appears bare 65× with no local row (master-series), while
  `D-038` appears bare 33× *and* as `D-PROJ03-038` 10×. Step 5 needs: `PROJECT00_README.md`, the
  two C1 BAN standalones for the D-038 sweep, and a question-bank artifact.
