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

## 2026-08-09 · lesson-plans (master register + sweep) · Principal · cowork
- Did: Verified `PROJECT00_README.md` §3 carries the master **D-001…D-053** and imported it as a
  read-only master-register reference — **labelled by its own content**. Ran the **full
  master-citation sweep** under the CD-034 rule. Applied the B-LP.1c pending-patch note to its
  header. Recorded the D-038 sweep's parked status. Evidence:
  `reports/MASTER_CITATION_SWEEP_2026-08-09.txt`.
- Decisions logged: **CD-035** (canon) and **D-PROJ03-050** (workstream).
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 1 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 4 warn)**. `canon_check` caught CD-035 as a phantom citation before its row
  existed — the fourth such catch this session.
- Open items / PENDING-P raised: **`D-051` DANGLES — cited 93 times, present in neither register.**
  §3 runs to D-053 but holds only **52 rows**, so D-051 has no body. A cited-but-unwritten *master*
  row; **not reconstructed**, batched. Sweep result: of **36** distinct bare citations, **35
  resolve**, but **33 of those also have a same-numbered `D-PROJ03` row** — so the bare form is
  ambiguous at each, including D-038/D-045/D-046/D-049 and the heaviest users D-022 (103×),
  D-046 (81×), D-049 (80×). Only **D-050 and D-053** resolve unambiguously. **D-038 sweep PARKED**
  — the two C1 BAN standalones were searched for and not found; it reopens if they surface.
  One correction to my own method: an earlier regex used `D-0[0-9]{3}`, which demands four digits
  after `D-0` and silently matched nothing; caught by cross-checking against a visible §3 row.

## 2026-08-09 · lesson-plans (D-051 reconstructed) · Principal · cowork
- Did: Wrote the approved **D-051** row into the **ERRATA section** of
  `references/PROJECT00_README.md` — never into §3, per the read-only rule — and flipped its
  status **dangling → RECONSTRUCTED** in the file header, LOCAL.md and STATE.md.
- Decisions logged: **CD-036** (canon) and **D-PROJ03-051** (workstream).
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 1 warn)**; `tools_check.py` →
  **CLEAN (0 fail, 4 warn)**.
- Open items / PENDING-P raised: none. **The master-citation sweep is closed: 36 of 36 —
  2 resolve cleanly, 33 via the CD-034 two-register rule, 1 reconstructed.** D-051 =
  Homework Question Pool → Project 04, superseding D-029; plans link by topic tag, questions are
  not printed, and the Spine drops to seven fields. Reconstructed from **78 substantive
  citations** (96 raw, less 14 boilerplate range statements and 4 rows written this session) and
  corroborated twice from registers already in the repo — `D-PROJ00-064` and §3's own D-029.
  **No divergence existed**, so nothing was synthesised. Precedent recorded in the errata:
  `D-PROJ00-064` carries its own restoration note, so P00 hit this failure before and fixed it
  the same way. Step 5 now needs only a **question-bank artifact**.

## 2026-08-09 · canon/sources + question-banks + scholarship (three policies adopted, পাঠ ২১ pilot) · Principal · cowork
- Did: Imported the three `_inbox/` v0.1 drafts to v1.0 with the Principal's ⚑ answers applied.
  **SOURCE_POLICY** → `canon/sources/SOURCE_POLICY.md` (+ canon MANIFEST row). **question-banks**
  created per AGENTS.md §10 (LOCAL.md, DECISIONS.md, CORRECTIONS.md, `_wip/STATE.md`,
  `audits/gates.py`, QUESTION_BANK_POLICY.md v1.0). **scholarship** created with
  MODEL_PAPERS_POLICY.md v1.0; its `DECISIONS.md` is a **pointer**, since its REGISTRY row assigns
  it `CD-###` via canon. REGISTRY updated: question-banks PLANNED → **LIVE**.
- Decisions logged: **CD-037** (SOURCE_POLICY adopted; `_inbox` scan intake with its two stated
  consequences; REL deferred to islamic-studies), **CD-038** (MODEL_PAPERS_POLICY; C5 → C1 order;
  model CTs per subject only), **CD-039** (question-banks LIVE; policy adopted; pilot result; two
  UNPROVEN rows flipped), **CD-040** (tools_check SYNTAX compiles to a temp dir), and workstream
  rows **QB-D-001…QB-D-006**.
- Gates run + result: `gates.py` → **CLEAN (0 failures)** after a **14-error seeded selftest, all
  firing**; **57/57 envelopes PASS** `validate_import.py` L1–L4, 0 warn / 0 advisory;
  `canon_check.py` → **CLEAN (0 fail, 1 warn)**; `tools_check.py` → **CLEAN (0 fail, 2 warn)**.
  Full verbatim output: `workstreams/question-banks/reports/BAN_U21_GATES_2026-08-09.txt`.
- Open items / PENDING-P raised: **PENDING-P-005** (S03 topic tag `TOP-BAN-C5-02` used on a stated
  default — পাঠ ২১'s attested tags are `-07`/`-01`/`-11` and the revision chart is not in this repo)
  and **PENDING-P-006** (the accepted Ch21 CT uses **আসিফ**, not in REF-2; the accepted artifact was
  **not edited**, cross-logged to class-tests CR-004). **UP-002** raised: the LOCKED question payload
  has no `pool` field and `paper_role` is a closed enum already meaning the REF-09 paper-section
  family — verified at source, so the v0.1 draft's §3 proposal was **corrected, not implemented**;
  pool membership lives authoring-side in `pool_index` and the Hub-side usage-lock and AS-rotation
  features are blocked on it. **Two corrections to the drafts' own claims:** there were **three**
  VENDORED-UNPROVEN rows, not two — the pilot closes `build_question_envelopes.py` and
  `LOCKED_QuestionPayload_Schema_v1.json`, while `tools/images/pick_placements.py` stays open
  because it is an interactive GUI (CD-022). **Pilot wave 1 = 57 items against a 180 ceiling**
  (QB-D-005): a KEEP-AS-IS / PROTECTED সিরাত chapter yields about that many distinct items, and the
  CEILING gate reports **70 · 35 · 18 owed** rather than manufacturing variants the ZERO-OVERLAP
  gate would then catch.
- **Audit round, same session.** An independent audit was run over this session's own work before
  closing. It **proved the gate suite could not fail on a factually wrong bank** — a probe bank with
  a flipped answer key, a fabricated fact, an MCQ with two correct options, a cross-pool paraphrase
  and a missing (স) returned **CLEAN**. Fixed under **QB-D-008** / **CD-041**: SOURCE-TRACE was
  vacuous, ZERO-OVERLAP skipped same-pool pairs and exempted every descriptive item, HONORIFIC
  matched only four name forms, nothing checked the answer carrier, and all eight rubrics were
  identical with 4 bands on a 5-mark item. Gates 11 → **13**, selftest 14 → **23 seeded errors**,
  and hardening SOURCE-TRACE rewrote **16 of the bank's own anchors** that had been passing on
  strings like "তিনি তখন". Content corrections: one MCQ whose marked-correct option stated a norm
  the extraction never states, and **দশম হিজরি** — the first line of the পাঠ and অনুশীলনী ৩(ক) —
  which no item had covered (**QB-D-007** also corrects QB-D-005's "~20 distinct facts" to 32–34).
  `SMOKE.md` cited the wrong item id for the L4 proof (Q49 for Q52) — corrected. The gate report
  was regenerated **unelided**: the first version showed 2 envelope results and summarised 55 as
  "identical", which asserts rather than shows. Final: **13/13 gates CLEAN · 57/57 envelopes PASS ·
  canon_check CLEAN · tools_check CLEAN**.

## 2026-08-09 · question-banks wave-1 PROMOTED · Principal · cowork
- Did: Acted on the Principal's rulings and promoted wave 1. **`_inbox/` drafts DELETED** — the
  three v0.1 policy files, superseded by the imported v1.0 policies; `_inbox/` is staging, not
  archive (reason stated in chat first, AGENTS.md §9; the sandbox could not unlink until file
  deletion was granted for the folder). **Wave 1 promoted out of `_wip/`**: bank →
  `banks/C5_BAN_U21_QuestionBank_v1.json`, envelopes → `banks/envelopes/`, authoring script →
  `authoring/author_U21_wave1.py`, plus a new `authoring/split_envelopes.py` recording the join
  between the builder's array output and the harness's one-envelope-per-file input. `_wip/` now
  holds STATE.md only.
- Decisions logged: **CD-042** (queue gains a third status; both queue rows ruled) and
  **QB-D-009** (wave-1 promotion).
- Gates run + result: full chain re-run **post-promotion, against the promoted paths** —
  **15 gates CLEAN** after a **25-error seeded selftest**, all firing; **57/57 envelopes PASS**
  `validate_import.py` L1–L4, 0 warn / 0 advisory; `canon_check.py` **CLEAN (0 fail, 1 warn)`;
  `tools_check.py` **CLEAN (0 fail, 2 warn)**. Verbatim, unelided:
  `workstreams/question-banks/reports/BAN_U21_GATES_2026-08-09-promoted.txt` (310 lines,
  58 `RESULT: PASS`, zero `RESULT: FAIL`, zero non-zero exits).
- Open items / PENDING-P raised: none raised. **PENDING-P-006 CLOSED** — the accepted Ch21 CT
  stays untouched and **আসিফ is grandfathered in that one historical paper only**; deliberately
  narrower than a carve-out, so every new item uses a REF-2 C5-pool name and **সাবিত** is
  confirmed. **PENDING-P-005 reclassified OPEN → FLAGGED** (file-owed): `TOP-BAN-C5-02` stays a
  stated default until the revision chart is staged in `_inbox/`, must not be changed by any
  agent, and blocks nothing. **That reclassification is what made promotion legitimate**, so it is
  written into the queue as a status taxonomy rather than applied as a one-off: OPEN =
  Principal-owed and blocks promotion · FLAGGED = file-owed and does not · RULED/CLOSED = settled.
  The flag now **travels inside the promoted bank** in its own `flags` block, enforced by a new
  **FLAG-TRACE** gate that requires every flag to resolve to a real, non-OPEN queue row — a flag
  pointing at nothing is worse than no flag, because it looks handled. **Wave 2 not started, by
  instruction;** HW 70 · AS 35 · CT 18 remain owed, with named starting targets in `_wip/STATE.md`.

## 2026-08-09 · question-banks (PENDING-P-005 close attempt — BLOCKED on a missing file) · Principal · cowork
- Did: Received the instruction to close PENDING-P-005 on REF-19 v1.10 and commit REF-19 into
  `canon/`. **Checked at source first and did not execute it.** Logged **QB-CR-007**; annotated the
  P-005 queue row with the failed attempt so the next session does not repeat it.
- Decisions logged: none — no ruling can be recorded on citations that do not resolve.
- Gates run + result: `canon_check.py` → **CLEAN (0 fail, 1 warn)**.
- Open items: **PENDING-P-005 stays FLAGGED — still blocking nothing.** Two of the ruling's three
  citations do not resolve here. **(a) REF-19 v1.10 is absent** from `_inbox/` and from the whole
  repo under any REF-19/topic/registry/slug filename; the only files touched in the preceding two
  hours are ones this session wrote — **CD-026 recurring, and the exact failure SOURCE_POLICY §2.1
  warns about, since `_inbox/` is gitignored and therefore per-machine.** **(b) `D-PROJ04-003` and
  `D-PROJ04-011` are cited nowhere in this repo** — the P04 register was never imported; only
  D-PROJ04-001/002/005/014/015 appear anywhere, all as citations inside the vendored schemas.
  **(c) The slugs-only half DOES corroborate** from a derived copy — `validate_import.py`'s inlined
  `REF19_SLUGS_DEFAULT` (auto-extracted from LOCKED_REF-19 v1.10) holds 121 slugs, 24 BAN, **none
  with a numeric suffix**, and the LOCKED question schema confirms `topic_tag` is pattern-only with
  numbers coming from the revision chart + REF-19 — **but CD-011 forbids writing such a registry
  from a summary or derived copy**, so canon was not synthesised from a harness constant.
  **Nothing closed, nothing committed to `canon/`, `TOP-BAN-C5-02` unchanged.**

## 2026-08-09 · PENDING-P-005 CLOSED; REF-19 + P04 register imported; wave 1 DE-PROMOTED · Principal · cowork
- Did: Classified and verified both staged files per SOURCE_POLICY §2.1, imported them, closed
  P-005 — and then returned wave 1 to `_wip/` when the import exposed a mis-tag.
  **REF-19 v1.10 → `canon/topics/`** read-only (sha256 `43a4d837…`), **`PROJECT04_DECISIONS.md` →
  `workstreams/question-banks/references/`** read-only (sha256 `49173426…`), both byte-identical,
  both removed from `_inbox/` afterwards (staging, not archive — and a canon basename left there
  would trip NO-COPY).
- Decisions logged: **CD-043** (P-005 closed on verification; REF-19 canon; P04 register imported;
  interim numbering authority named; residual raised) and **QB-D-010** (wave 1 returned to `_wip/`).
- Gates run + result: `gates.py` → **FAIL (1 failure), EXIT=1 — FLAG-TRACE red, as intended**;
  **57/57 envelopes PASS** L1–L4, 0 warn / 0 advisory; `canon_check.py` **CLEAN (0 fail, 1 warn)**;
  `tools_check.py` **CLEAN (0 fail, 2 warn)**. Verbatim:
  `reports/BAN_U21_GATES_2026-08-09-depromoted.txt`; verification evidence:
  `reports/P005_VERIFICATION_2026-08-09.txt`.
- Open items / PENDING-P raised: **P-005 CLOSED** — PASS on all four conditions. REF-19 holds
  **zero `TOP-` strings and no numeric-suffixed id**; its 121 slugs reconcile **exactly** with the
  vendored harness constant (zero diff either way), which is the CD-011 reconciliation finally done
  artifact-first. `D-PROJ04-011` attests *"`TOP-BAN-C5-02` বাক্য-রচনা (29)"*, `D-PROJ04-003` carries
  `-02` for U14 — **the 8 S03 items are correctly tagged**. QB-CR-004 and QB-CR-007 close with it.
  **PENDING-P-008 raised (FLAGGED, non-blocking):** the authoritative `##` chart owed to REF-07 §3.5
  is still not a file; interim authority is REF-19 slugs + the register's attested numbering, and the
  register carries that same caveat in its own rows. **PENDING-P-007 raised (OPEN, BLOCKING):**
  checking the three tags the ruling did *not* ask about — possible for the first time now that the
  register is here — found **`TOP-BAN-C5-11` attested as মূল্যবোধ/মুক্ত-চিন্তা** while the bank's
  বিরামচিহ্ন item `Q52` carries it. I had read it off MarkLogic spine slot **S11 = বিরামচিহ্ন**; the
  two schemes are unrelated and collide at 11. No punctuation number is attested anywhere, so
  **nothing was substituted**. **Two gate findings:** FLAG-TRACE **passed the bank before it failed
  it** — it matched the literal `**OPEN**` while the row reads `**OPEN — Principal-owed.**`, so the
  gate written for exactly this case sailed past it; fixed to read the status cell and match the
  word, with a seeded case now exercising a **real OPEN row** (the original two covered only a
  missing tag and a missing field, which is why the hole survived). Selftest 25 → **26**. Then the
  red gate did its job: **AGENTS.md §5 returns a red artifact to its build phase**, so wave 1 went
  back to `_wip/` — promotion means ready for the Hub, and a bank carrying a tag the register
  contradicts is not. Re-promotion is one ruling and one regenerate away; the 57 items are untouched.
  Recommendation on P-007: **mint `TOP-BAN-C5-13`** for বিরামচিহ্ন rather than folding it into `-02`,
  since the C5 spine keeps S03 and S11 as separate mark slots.

## 2026-08-09 · PENDING-P-007 ruled; TOPIC_NUMBERS chart seeded as canon; wave 1 RE-PROMOTED final · Principal · cowork
- Did: Minted **`TOP-BAN-C5-13` = বিরামচিহ্ন / যতিচিহ্ন** and recorded it **in canon, not only in the
  bank** — `canon/topics/TOPIC_NUMBERS.md` created as the seed of the chart PENDING-P-008 owes,
  carrying the full attested C5 Bangla set imported from the P04 register with **per-row citations**
  (`-01` `-02` `-05` `-06` `-07` `-09` `-11` `-12`) plus `-13` citing CD-044. `-10` deliberately left
  out: a P03 usage note is not a P04 attestation, and not-yet-listed is the correct state for an
  unattested number. Retagged `QP-BAN-C5-U21-Q52`, regenerated, re-promoted to `banks/`.
  **Production sequence recorded as CD-045 and in REGISTRY.md** — ① NCTB sources → ② C5 model papers
  and CTs → ③ C1–C4 → ④ question pools; **পাঠ ২১ wave 2 waits for step ④**, and STATE.md says so.
- Decisions logged: **CD-044** (mint, chart, gate, P-008 close condition revised, REF-19 slug gap),
  **CD-045** (production sequence), **QB-D-011** (retag + re-promote), **QB-D-012** (fixtures).
- Gates run + result: **15 gates CLEAN**, EXIT=0, after a **27-error seeded selftest + 1 negative
  case**; **57/57 envelopes PASS** L1–L4, 0 warn / 0 advisory; `canon_check.py` **CLEAN (0 fail,
  1 warn)**; `tools_check.py` **CLEAN (0 fail, 2 warn)**. Verbatim, unelided, 314 lines:
  `reports/BAN_U21_GATES_2026-08-09-final.txt`.
- Open items / PENDING-P raised: **P-007 CLOSED**; **P-008 stays FLAGGED** with its close condition
  now *chart complete for all subjects*, completion happening in `TOPIC_NUMBERS.md` itself, plus a
  **sub-item: REF-19 v1.10 carries no Bangla punctuation slug**, owed as a REF-19 supersede authored
  at Project 00 — **REF-19 was not touched**, it is LOCKED and read-only here. Q52 keeps
  `ref19_topic_id: BAN-SENTENCE` because the harness hard-validates that field against the REF-19
  registry and would reject a minted slug; only `topic_tag` changed. **New gate TOPIC-NUMBER** makes
  "a number not in the chart is not used" executable — the check whose absence let a wrong number
  survive a chain and a promotion. **Two gate failures of my own, both fixed and logged:** the
  QB-D-010 OPEN-path selftest case named the live row P-007, so ruling it turned the selftest red
  the same day — the fixture was the live world (QB-D-012); and nothing had been proving FLAG-TRACE
  stays *quiet* on a FLAGGED row, so a negative case was added. **Two contested numbers carried
  forward, recorded not resolved:** the register's own unruled U14 Drama→Story re-home, where REF-03
  maps U14 to `-09` and D-PROJ04-003 tagged it `-06`.

## 2026-08-09 · Cowork · Production step ① — C5 English source extraction (CD-046, CD-047)

**Started:** `git pull` clean at `d6ed8fd`. Read AGENTS.md, REGISTRY.md, SOURCE_POLICY.md,
PENDING_PRINCIPAL.md.

**Classification (SOURCE_POLICY §2.1).** `_inbox/Class 5 English.pdf` is **not** the scan the
policy describes — it is a born-digital NCTB publisher PDF (Illustrator, AcroForm, 118pp,
md5 `09a9b96f…`) carrying a text layer that is wrong three ways: Bengali mojibake, a +29-shifted
Latin subset, and a −29 display subset. Offset **printed + 6 = PDF**, verified at six points
across the whole book. Five other `_inbox/` items classified and reported, none assumed.

**Unit 1 as the proof piece.** Built by raster-read, held in `_wip/` unpromoted, evidence and
gate output shown to the Principal, three questions batched (PENDING-P-009/010/011). He ruled
all three, spot-checked and signed. Promoted to `canon/sources/c5/english/`, gate GREEN.

**Two gates written.** `source_check.py` executes SOURCE_POLICY §5, closing the §6 gap that said
the gate "has no executing script yet"; SIGNOFF reports PENDING, never PASS-by-agent.
`source_textcheck.py` executes §7.3 — it decodes the text layer independently and diffs it
against the transcription, so the one unchecked step in the pipeline is no longer unchecked.
It scores against a neutral system word list, never the extraction's own words.

**Both gates went red on their own author, and both times the defect was real.** source_check's
first run caught unresolvable slot codes in the extraction *and* a phantom offset from its own
parser. source_textcheck's ligature table had been written from guesses — two of three rows
wrong; it stripped the control range as noise, which deleted every digit in the shifted font;
and it broke ties on length, so `Suddenly,` decoded to `puddenlyI` and reported itself missing.
All found by running it over 20 real units.

**Units 2–20.** Extracted, gated, evidenced. Every boundary read off the printed folio: the
contents page was right at Units 6 and 19 where a detection pass disagreed, and **the book runs
to printed 111, not 106**. Full sweep: 20/20 PASS on RANGE/SLOTS/PAGES; textcheck AGREE on 7 of
20, the rest amounting to 24 single words, every one proved present in the raw text layer.
Section B — dropped or invented passages — clean throughout.

**Housekeeping (Principal-ruled):** `.gitignore` widened to `**/_wip/**/*.png`; the byte-identical
stale PlanSchema copy deleted from `_inbox/` with the vendored original verified intact after;
Ch19/Ch20 class tests moved to `workstreams/class-tests/accepted/` unedited; Naskh weights left
in `_inbox/` as new weights needing their own SMOKE run.

**Gates before sync:** `canon_check.py` CLEAN (0 fail) · `tools_check.py` CLEAN (0 fail) ·
`source_check.py --selftest` PASS · `source_textcheck.py --selftest` PASS.

**Queue:** PENDING-P-009/010/011 CLOSED. New: **PENDING-P-012** (OPEN, canon/sources — where
artwork-borne labels live; ~75 map names have no second channel at all) and **PENDING-P-013**
(OPEN, scholarship — six curation facts the units record that step ② must rule on).

## 2026-08-09 · Cowork · Spot-check depth and the step-② rulings (CD-048, CD-049)

**Depth (CD-048).** SOURCE_POLICY v1.2. §7.4: where `source_textcheck.py` reports Section B
clean **and** every word-level disagreement is provenance-proven, the spot-check is **one
sampled passage per unit — the longest**, with the machine diff standing as the second and
third channel. The conditions are conjunctive and read off an executed run; a unit that fails
either returns to the older depth. §2.3 carries a supersede note and is not edited.

§7.5: artwork-borne text — Unit 4's maps hold ~75 place names of which the text layer has **not
one character** — lives in the names/labels section, flagged raster-only, outside the
cross-checked body, **checked in full and never sampled**, and **any consumer citing it inherits
the flag**. Made executable the same day: SIGNOFF now **FAILs** an extraction that records such
text without a full-check row, with a sixth seeded selftest, and the selftest fixture now prefers
a file carrying that content so the seed can bite. Otherwise the depth ruling would have been a
paragraph, and the one kind of content no machine can corroborate would have been the one kind
nobody was obliged to look at.

All 19 sign-off tables rewritten, the sampled passage chosen mechanically as each unit's longest
transcribed section. Units 4 and 11 carry the extra full-check row.

**Step ② rulings (CD-049).** PENDING-P-013 closed in six parts, written into
`MODEL_PAPERS_POLICY.md` §8 (v1.1) because step ② is where they apply, and the poem ruling into
`MarkLogic_ENG_Spine.md` under `ENG-S03` as a forward-only application note with no mark changed.
**No extraction was edited.** The shape they share: *a source records what the book says; canon
governs what the school prints* — deer stimulus substituted downstream, MCQs not mirrored,
"Quater" kept in the source and "Quarter" printed, lift-the-line not mirrored, Bidhan replaced
under the existing CD-042 name rule, and S03's passage on Units 10 and 15 **is the poem**.

**Gates before sync:** `canon_check.py` CLEAN (0 fail) · `tools_check.py` CLEAN (0 fail) ·
`source_check.py --selftest` PASS (6 seeds + control) · `source_textcheck.py --selftest` PASS ·
full 20-unit sweep 20/20 PASS on RANGE/SLOTS/PAGES.

**Queue: 0 OPEN.** Next session: C5 Bangla পাঠ ১–১২ and ২৪+ per §7.1, once the Principal stages
the Bangla PDF in `_inbox/`.

---

## 2026-08-09 · C5 Bangla extraction opens — পাঠ ১–৬ built · `scd-agent-cowork`

**Checkpoint commit: extraction in progress, promotion pending. All SIGNOFF PENDING — only the
Principal signs.** পাঠ ৭–১১ are owed; state and the exact resume point are in
`canon/_wip/c5-bangla/STATE.md`.

**The stated scope was wrong at both ends (CD-050, SOURCE_POLICY §7.6).** §4 and §7.1 both read
"পাঠ ১–১২ and ২৪+". **The book has 23 পাঠ** — সূচিপত্র runs ১–২৩, পাঠ ২৩ starts printed ১৩০,
printed **১৩২ carries সমাপ্ত**. There is no পাঠ ২৪ and never was. **পাঠ ১২ is not extracted**:
`C5_Bangla_Source_13-23.md` records it excluded on Islamic-values grounds by school authority and
the Principal confirmed that reaches the extraction layer — a **named exception to §3, not a
loosening of it**, written down at `canon/_wip/c5-bangla/EXCLUDED_paath_12.md` so the gap is
visible rather than looking like an oversight. Real scope: **পাঠ ১–১১**.

**A third source class (§7.7).** `Class 5 Bangla.pdf` is neither §2.1's scan nor §7.3's lying
text layer: born-digital **with every glyph converted to outlines**. `pdftotext` returns **421
characters over 142 pages** — 312 on the back imprint, 4 on p28, none elsewhere; pages
1/20/70/100/141 register **no fonts**; page 70's stream holds 9,790 curve operators, 183 fills
and **not one `BT`/`Tj`**. **Offset +৯ verified at 20 points** before anything was extracted, and
it reconciles exactly with the existing 13–23 file (পাঠ ১৩ = printed ৬৯ = PDF 78).

**Depth is full human check, book-wide.** §7.4 buys one sampled passage per unit against a clean
Section B — and **Section B is trivially clean on an empty stream.** An absent channel is not a
passing one, so the depth §7.5 sets for artwork text applies to the whole book.

**A false green, kept on the record (CD-051).** Run against this book, `source_textcheck.py`
printed **`VERDICT : AGREE — the channels account for each other completely`** and exited 0,
having compared **zero words against zero letters** — the exact output §7.4 buys reduced depth
with. Three stacked faults: the body anchor took `^# Unit \d+` only, so a `# পাঠ ১` file was
never sliced and the md5 and `ilovepdf` scored as words of the book; `letters()` kept `[a-z0-9]`,
so the Bengali transcription contributed nothing; and **`str.isalnum()` is False for every
Bengali matra and hasant**, leaving **three** words standing out of a five-page chapter. Fixing
the anchor alone still printed AGREE. The gate now **REFUSES (exit 3)** rather than reporting
agreement when it has nothing to compare. **Scaffolding is defined by script, not a stop-list**
(§7.2(c)) — the naive fix injected four Bengali words into Section A of **all twenty English
units**; regression-proved old vs new across all 20: **0 of 20 differ**.

**`source_check.py`** reads `পাঠ` as well as `Unit`; gains a **DEPTH** check; and **scopes PAGES
monotonicity to the transcribed body** — the slot cross-reference cites pages per slot, and
English Unit 1 passed the unscoped version only by luck. DEPTH's first version scanned the whole
row and reddened পাঠ ৪, whose sign-off says "আবেদনপত্রের **নমুনা** — পুরোটা" where নমুনা is the
book's word for its sample letter; it now reads the গভীরতা column. Selftest **8 seeds RED, all
controls CLEAN**, fixtures drawn from every extraction on disk.

**No Bijoy/SutonnyMJ decoder was written, deliberately.** The only Bangla text layer in this book
is the back imprint, so a decoder would have nothing in scope to be proven against, and an
unproven decoder inside a REQUIRED tool is what CD-020 exists to prevent.

**Resolution matters here.** Three transcription facts were invisible at 150 dpi and only
resolved by high-res crops: পাঠ ৩'s `ঝকঝক` (first read as `ঝকঝাক`); পাঠ ৪'s sample letter dated
**৩ই মার্চ** while apologising for an absence on **গত ৪ঠা মার্চ** — dated before the absence, and
contradicting the book's own তারিখবাচক table (**৩রা**) on the facing page; and পাঠ ৬'s nasalised
dialogue, where the same word appears as plain **‘আমার'** and nasalised **‘আঁমাঁর'**, and one
quote has **no closing quotation mark**. Standing note added: poem and handwriting-font pages get
a high-resolution crop *before* transcription, not after.

**Gates at commit:** `canon_check.py` CLEAN (0 fail) · `tools_check.py` CLEAN (0 fail) ·
both selftests PASS · six-file sweep RANGE/SLOTS/PAGES/DEPTH **PASS**, SIGNOFF **PENDING**,
textcheck **REFUSE** (expected on this book). Verbatim:
`canon/_wip/c5-bangla/evidence/GATE_SWEEP_2026-08-09.txt`.

**Queue: 0 OPEN.** Next: পাঠ ৭ (সাইক্লোন), printed ৩৮–৪১ = pdf 47–50.

---

## 2026-08-09 · C5 Bangla — পাঠ ৭–৮ added (checkpoint 2) · `scd-agent-cowork`

**পাঠ ১–৮ built, sign-off owed. পাঠ ৯–১১ remain.** Same standing: extraction in progress,
promotion pending, **all SIGNOFF PENDING — only the Principal signs.**

**Resolution is this book's recurring hazard, and it has now bitten four times.** Read at the
150 dpi working render and corrected only by a 400–700 dpi crop: `ঝকঝক` (first read `ঝকঝাক`,
পাঠ ৩) · পাঠ ৪'s sample-letter date · পাঠ ৬'s chandrabindu placement · `শাঁখ` (first read
`শীঁখ`, পাঠ ৭). **Three of the four would have entered canon.** Standing rule now in STATE.md:
poem pages, handwriting-font pages and any page with stacked diacritics get the high-resolution
crop **before** transcription, not after — on a book with no second channel, the working render
is the only thing between a mis-read and a printed question.

**Findings kept as printed, not fixed (SOURCE_POLICY §3).** পাঠ ৭ prints **সরষে** in the poem
and **শর্ষে** in its own word list on the facing page, and asks for a sentence with **“ধোয়া
জামা”** where the poem says **“ফরসা জামা”**. পাঠ ৮ writes **“৩-4টি করে বাচ্চা দেয়”** — **the ৩ is
a Bengali digit and the 4 is a Latin one**, in a paragraph where all nine other numbers are
Bengali; its exercise ছক asks for **রাজকীয়**, **ক্ষিপ্র** and **স্মরণশক্তি**, none of which the
chapter contains (it has রাজসিক, and দৃষ্টি/শ্রবণ/ঘ্রাণশক্তি). পাঠ ৮'s sign-off carries a
dedicated row for its numbers, because a wrong figure travels straight into a question paper.

**DEPTH gate corrected (CD-051 amended in place).** Its first version matched `নমুনা` anywhere
in a sign-off row and went red on পাঠ ৪, whose first entry reads “আবেদনপত্রের **নমুনা** —
পুরোটা” — the book's word for its sample letter, not a claim about depth. It now reads the
**গভীরতা column**, with an eighth seed covering a file that omits the column entirely.
**Selftest 8 seeds RED, all controls CLEAN.** A gate that reddens correct files stops being read.

**Gates at commit:** eight-file sweep RANGE/SLOTS/PAGES/DEPTH **PASS**, SIGNOFF **PENDING**,
textcheck **REFUSE** ×8 (expected) · both selftests PASS · `canon_check.py` and `tools_check.py`
CLEAN (0 fail) · every `প্রমাণ` citation checked to resolve to a file on disk. Verbatim:
`canon/_wip/c5-bangla/evidence/GATE_SWEEP_2026-08-09.txt`.

**Queue: 0 OPEN.** Next: পাঠ ৯ (টুকটুক ও চিকু), printed ৪৭–৫২ = pdf 56–61.

---

## 2026-08-10 · C5 Bangla — পাঠ ৯–১১ built · **EXTRACTION COMPLETE** · `scd-agent-cowork`

**পাঠ ১–১১ all built and gated. The book is done at the extraction layer.** পাঠ ১২ excluded by
CD-050, পাঠ ১৩–২৩ already canon (CD-004). **Promotion pending — all 77 sign-off rows PENDING,
only the Principal signs.** Files stay in `_wip/`, which is the correct state for unsigned work.

**Session start checks, none assumed:** `git pull` clean · PDF md5 re-verified
`a119d576b43dac57bfc385f9721ffc86` · **offset +৯ re-derived from scratch at five fresh points**
(pdf 56→৪৭, 62→৫৩, 66→৫৭, 71→৬২, 72→৬৩), because STATE.md says it is never carried between
sessions · PENDING_PRINCIPAL 0 OPEN.

**CR-001 — a correction owed on already-pushed work, and the worst kind.** পাঠ ৭ carried a
**false** “as printed” note claiming the book spells **প্রচন্ড** (দন্ত্য-ন). At 600 dpi the book
reads **প্রচণ্ড** — correctly spelled. So two things were wrong at once: the transcription in the
word-list table, and an **anomaly invented out of a misread**. Caught only because পাঠ ৯'s word
list carries the same word and the two were compared. **A false anomaly is worse than a missing
one** — it tells a question author the book contains an error it does not contain, and this book
has no second channel to catch that. Both fixed, `CORRECTIONS.md` opened, and the
high-resolution rule widened to cover **word-list tables**: ণ/ন, শ/স/ষ and ড়/র inside conjuncts
are not separable at the 150 dpi working render.

**Findings kept as printed (§3).** পাঠ ৯: the exercise ছক offers both **আনন্দের জোয়ার** and
**আনন্দ-উচ্ছ্বাসে** for two blanks either could fill, and asks who arranged the চড়ুইভাতি when
the text's “ওরা” never says; two of its ভাব sentences are not in the chapter. পাঠ ১০: inner and
outer quotations use the **same single mark**, so the nested quote's end is unmarked; ছোট্ট/ছোটো
split between poem and exercise; **সরষে** here against **শর্ষে** in পাঠ ৭. পাঠ ১১: শব্দার্থ calls
ধামা a **বেতের ঝুড়ি** while the text makes ধামা বেত and ঝুড়ি বাঁশ; three exercise-৩ facts
(পুঁজি কম, স্থানীয় কাঁচামাল, দামে সস্তা) appear nowhere in the chapter.

**Completion checks, executed not asserted:** 11/11 files RANGE/SLOTS/PAGES/DEPTH **PASS**,
SIGNOFF **PENDING**, **0 FAIL** · textcheck **REFUSE ×11** (expected on this book) · both
selftests PASS · `canon_check.py` and `tools_check.py` CLEAN (0 fail) · **every প্রমাণ citation
across all eleven files resolves to a file on disk** · **coverage verified programmatically:
printed ১–৬২ contiguous, no gaps, no overlaps** · `BAN-S14` bound in পাঠ ৪ only, absent in the
other ten · **77 sign-off rows, 0 signed.** Verbatim:
`canon/_wip/c5-bangla/evidence/GATE_SWEEP_2026-08-10.txt`.

**Queue: 0 OPEN.** Next when the Principal signs: promote the eleven files plus `evidence/` and
`EXCLUDED_paath_12.md` to `canon/sources/c5/bangla/` and re-run the gate there. Noted, not
acted on: **`_inbox/` now also holds `Class 5 Math.pdf`** — the next subject under §7.1's order,
but a new extraction is a new session's work.

---

## 2026-08-10 · Cowork · production step ① — C5 গণিত opened (classification, offset, gates); transcription begun

**Repo state at start:** `acb3421`, clean, `main` up to date. `git pull` first returned
`fatal: bad object refs/remotes/origin/main.lock.aside-…` — a stale aside file left *inside*
`refs/remotes/origin/`, where git parses every entry as a ref. Not a conflict; residue of the
AGENTS §9 rename-aside practice. Moved into the existing `.git/lock-debris/` (the convention two
earlier sessions already used), along with a stale `index.lock` and `objects/maintenance.lock`.
Pull then clean: **Already up to date.** Nothing was deleted — the sandbox cannot unlink inside
`.git/` anyway (CD-040's limitation).

**1. `Class 5 Math.pdf` classified — §7.7, measured rather than inherited (CD-052).** Same
publisher pipeline as the Bangla book, so §7.7 was *expected*; it was measured anyway, and the
result is more extreme. `pdftotext` over 190 pages returns **190 characters — one form-feed per
page, not one real character**; **all 190 pages register zero fonts**; thirteen sampled pages hold
**zero `BT`/`Tj`** against 5,208–76,887 curve operators each. Bangla had a text layer on its back
imprint; this book has none anywhere. `source_textcheck.py` **REFUSE (exit 3)**, naming the reason
— *"0 letters over 16 page(s), under the 640-letter floor"* — which corroborates the classification
from a second direction. **Single channel, full human check book-wide; §7.4 sampling unavailable.**

**2. Offset re-derived from scratch: +৭, at 18 points.** Bangla's is +৯; carrying it would have
been wrong by two on every page reference. Verified across all 190 pages — ten chapter-opening
folios plus eight interior folios read off the raster — constant throughout. Folio circles were
cropped and montaged in grids, so twenty folios could be read from one image.

**3. Structure read against the book at both ends.** সূচিপত্র (PDF 6) gives **ten অধ্যায় and
stops**; all ten openings confirmed on the printed page with banner and number, and **every
chapter's final page confirmed too** — each carries the preceding chapter's content, no gap, no
divider, no unlisted section. **Printed ১৮১ (PDF 188) is the last numbered page; PDF 189 carries
সমাপ্ত in place of a folio; PDF 190 is the back cover. No glossary, answer key or appendix.**
This is CD-050's lesson applied *before* extraction instead of after.

**4. Both gates were subject-shaped again (CD-053) — the red is on the record.** Against a correct
first Math extraction, `source_check.py` printed `grammar : —` and
`[FAIL] RANGE cannot read the '**এই ফাইলের অংশ:**' scope line`, with PAGES `skipped — scope
unreadable`: `UNIT_WORDS` held `("Unit", "পাঠ")` and a Math book divides itself into **অধ্যায়**,
so two of five checks died before reading a word of the book. Fixed in both gates (scope line, body
heading, `COMMENTARY`, and `source_textcheck.py`'s body anchor). After: `grammar : chapter word
'অধ্যায়'`, RANGE PASS, PAGES PASS at a constant +7 over 18 rows. **The list has now been wrong
once per subject** — that, not the fix, is the finding.

**5. A collision between two standing rules, found by running the gate.** CD-051 made the selftest
fixture pool *every extraction on disk*; its controls assume every such file is finished. AGENTS §3
requires unfinished work to live on disk so a killed session is resumable. On a book too big for
one session those cannot both hold, and the half-built Math chapter produced
`[FALSE+ ] control · C5_MATH_Source_01.md` and **`SELFTEST: FAIL`** — a red tool gate for the whole
repo, from a file correctly reporting it was not done. Resolved in code, not waived: a file may
declare `**অবস্থা:** নির্মাণাধীন` and is excluded as a control, **with every skipped file printed
by name**. Removing the marker is written into the resume instructions. Raised as **PENDING-P-015
(FLAGGED)**.

**6. Transcription begun, and deliberately stopped.** Printed page ১ transcribed and arithmetic
cross-checked (৪৬১৪ × ৩৬৫: partials ২৩০৭০ · ২৭৬৮৪০ · ১৩৮৪২০০, গুণফল ১৬৮৪১১০). True 400 dpi needs
four tiles per page — **≈720+ reads for 181 printed pages** — so the book cannot be transcribed in
one session at the depth the math-critical rule demands. Stopped at a stated resume point rather
than lowering care, per the Principal's instruction. Raised as **PENDING-P-014 (OPEN)**, which
blocks promotion and print for c5-math but not continued transcription on the stated default.

**Gates, verbatim runs committed under `canon/_wip/c5-math/evidence/`:**
`source_check.py` on the file — RANGE **PASS** · PAGES **PASS** · DEPTH **PASS** · SIGNOFF
**PENDING** · **SLOTS FAIL, deliberately** (the slot cross-reference is not written, because
writing it without reading the chapter would be writing a guess). **The file is red, and red is
the correct state.** `source_check.py --selftest` **8 seeds RED, 32 controls CLEAN, PASS** ·
`source_textcheck.py --selftest` **10/10 PASS** · `tools_check.py` **CLEAN** (2 pre-existing warns)
· `canon_check.py` **CLEAN** (1 pre-existing warn).

**Not done, and named:** অধ্যায় ১ printed ২–১৬; অধ্যায় ২–১০; the MarkLogic slot cross-reference;
any sign-off (**no agent writes in the সই column**). Whether this book contains an excluded chapter
of the পাঠ ১২ kind is **not yet knowable** and is recorded as verified-chapter-by-chapter rather
than declared in advance.

### 2026-08-10 (same session, continued) · rulings folded in; অধ্যায় ১ printed ১–৩

**Rulings applied.** PENDING-P-014 and P-015 both CLOSED; queue now **0 OPEN · 1 FLAGGED**.
`SOURCE_POLICY` → **v1.4**: new **§7.8** (cadence for single-channel books — no dpi relaxation,
one or more complete অধ্যায় per session, checkpoint-commit per chapter, stated resume point,
fresh session each sitting) and **§7.9** (`নির্মাণাধীন` self-declaration). `AGENTS.md` → **v1.2**:
§9 now names `.git/lock-debris/` as the **only** aside destination, with today's
`bad object refs/remotes/origin/main.lock.aside-…` recorded as the reason, plus the observation
that **each git write re-creates the lock it cannot remove** — so the aside is moved before every
git write, not once per session. **CD-054, CD-055, CD-056.**

**Transcription: printed ১, ২ and ৩.** কাজ ১–৩ and অনুশীলন ১–২, with the book's blank boxes
transcribed **as blanks** (☐) rather than solved — SOURCE_POLICY §3, an extraction records.

**A second channel exists on this book after all, and it is the mathematics.** §7.7 is right that
there is no text layer, but math content carries its own redundancy: partial products must sum to
the total, and each partial must equal multiplicand × place value. **A mis-read digit does not
balance.** All sixteen checks over printed ১–৩ pass
(`evidence/ARITHMETIC_SELFCHECK_2026-08-10.txt`). It is strongest where the transcription is least
certain: কাজ ৩(৩) and ৩(৪) are printed with blanks, yet the printed digits determine the hidden
ones uniquely (৫৫৭৯ × ৪৬৭৭ and ৭৭৭২৩ × ৪৫৬৭) and the solution matches **every** printed cell.
**Three limits stated with it:** a number the book never computes is not covered; words, names and
instructions are entirely outside it; and **it is not a gate** — run once, recorded, not placed in
`tools/MANIFEST.md`, so it is not a proven tool (CD-020). Whether it becomes
`tools/audits/math_arith_check.py` with a seeded selftest is a Principal question, raised in
`STATE.md`, not decided here.

**Gate, verbatim:** RANGE **PASS** · PAGES **PASS** (offset +7, 18 rows; 3 body refs monotonic) ·
DEPTH **PASS** (5 of 5 rows পূর্ণ) · SIGNOFF **PENDING** (5 of 5 unsigned) · **SLOTS FAIL,
deliberately** — the slot cross-reference waits until the chapter has been read. **RED, correctly.**

**Resume point: ছাপা পৃষ্ঠা ৪ (PDF 11).** Rasters at 150 dpi (all 190 pp) and 400 dpi (PDF 8–23)
are already on disk and gitignored; the tiling recipe and the folio-montage trick are written into
`STATE.md` so the next sitting re-derives nothing except the offset, which is never carried.

### 2026-08-10 (same session, continued) · `math_arith_check.py` promoted to a proven gate — and it caught CR-002

**Built as ruled.** `tools/audits/math_arith_check.py`, MANIFEST row **REQUIRED**
(`tools/audits` is SMOKE-exempt by `tools_check.py`'s own `SMOKE_EXEMPT` — a gate evidences
itself and its verbatim run is the record). The three limits sit in the docstring verbatim:
**computed working only · words, names and instructions out of scope · problem-statement figures
unchecked where the book prints no working.** **CD-057**; depth extension recorded as
**SOURCE_POLICY §7.10** (v1.5).

**Seeded selftest — 16 cases, all PASS.** A flipped digit in the total, a partial, the
multiplicand, the multiplier, and inside a blanks-block each turn it RED; a dropped partial row
is RED on shape; an unbalanced step table is RED. The branches that matter most are proven too:
an under-determined block is **AMBIGUOUS**, a pure scaffold is **WIDTH**, and a file containing
only those returns **REFUSE, never CLEAN** — a depth claim cannot rest on a block where no digit
was verified.

**The first real run went RED on two blocks. Both were worth having.**

**(1) The gate caught my own error — CR-002.** কাজ ৩(১), ৮৩৪৬ × ১৫৪৫: I had transcribed
**eight** empty boxes in the fourth partial row where the book prints **seven**. ৮৩৪৬ × ১০০০ =
৮৩৪৬০০০ is seven digits, and with no zero in the multiplier the widths ৫·৬·৭·৭ are
arithmetically forced. Re-cropped at 400 dpi and counted again: seven. **The digits were
perfectly legible; the count was wrong.** High resolution protects *reading*; only a second
channel protects *counting*. The two answer different failures and neither substitutes for the
other, so **CD-054 stands untouched** — this is not an argument for lowering dpi.

**(2) The second RED was the gate's own blind spot, and became a rule.** কাজ ৩(২), ৬২৫৮ × ৬০৯৭:
the third partial is ৬২৫৮ × ০ × ১০০ = 0 — one digit — and **the book still prints six boxes**.
It does not narrow the scaffold for a zero multiplier digit. Checking that width would redden a
correct transcription, so zero-digit rows are now excused **in code, with the book cited as the
reason**, and the exemption is itself seeded: a zero-digit block with a conflicting printed digit
still goes RED. Recorded in the extraction's `যেভাবে ছাপা আছে` as a feature of the book.

**Gate state after the fixes:** `math_arith_check.py` **CLEAN — 8 items verified; 2 uncovered**
(both pure scaffolds, full manual depth per §7.10). `source_check.py` unchanged: RANGE/PAGES/DEPTH
**PASS**, SIGNOFF **PENDING**, **SLOTS FAIL deliberately** — still RED, still correct. All five
audit gates' selftests **PASS**; `canon_check.py` and `tools_check.py` **CLEAN**.

**Transcription did not advance this session** — the tool build consumed it. Resume point is
unchanged at **ছাপা পৃষ্ঠা ৪ (PDF 11)**, and per §7.8 the next sitting starts fresh and takes
অধ্যায় ১ to completion, with `math_arith_check.py` now running alongside `source_check.py` from
the first page.

## 2026-08-10 (fresh sitting) · C5 গণিত অধ্যায় ১ — ছাপা ৪–৭ transcribed

**Session start per AGENTS §3.** `AGENTS.md` v1.2 read at source; `git pull` **Already up to
date** at `1ea4045`; resume point read from `STATE.md`. The §9 lock-aside helper was rebuilt
first and used before every git write, per **CD-056**.

**Transcribed printed ৪, ৫, ৬ and ৭** at 400 dpi — কাজ ৪ (পাশাপাশি গুণ / distributive), the
×১০০ ladder and the trailing-zero method, the ৯৯/৯৯৯/৯৯৯৯ subtraction trick, and the blanket
word problem. Blanks recorded as blanks throughout (§3). **Two structural findings:** the book
**restarts কাজ and অনুশীলন numbering at every new মূল প্রশ্ন**, so printed ৪, ৫ and ৬ each carry
their own কাজ ১ / অনুশীলন ১ — recorded as printed rather than renumbered; and the **ভাগ half of
"গুণ ও ভাগ" has not started by printed ৭**.

**§7.5 raster-only content found and quarantined.** Printed ৬'s **সহজ পদ্ধতি** box states the
distributive law **not in letters or numerals but in three drawn coloured shapes** — blue square,
yellow triangle, magenta circle. Nothing can corroborate it; it is in a `## ছবির ভেতরের লেখা`
section outside the transcribed body with its own full-check sign-off row, and any consumer
citing it inherits the flag.

**The gate's reach, measured rather than assumed.** `math_arith_check.py` still reports
**8 items verified** — *the same number as before four pages were added*. It parses stacked
multiplication and `| A × B | → | C |` step tables, and printed ৪–৭ contain **four shapes it does
not parse**: distributive expansion, the ×১০০ ladder, the trailing-zero rule with its vertical
bar, and `( X − ১ )` subtraction-distribution. **It does not REFUSE on these — it stays silent**,
because it never finds the blocks; `found N blocks` is the only signal that anything went
unexamined. Per the ruling I did **not** extend the gate: printed ৪–৭ were transcribed and checked
at full manual depth, with the twelve hand checks recorded verbatim in
`evidence/MANUAL_ARITH_p04-07_2026-08-10.txt` — all consistent. The cheapest high-value extension
(a distributive check covering most of ৪, ৬ and ৭) is named in `STATE.md` for a ruling, not taken.

**A gate caught a build-time slip before commit.** Writing `৪৯৭৩\|০` into a sign-off cell shifted
the depth column — `source_check.py` went **`[FAIL] DEPTH 1 of 15 sign-off row(s) state no depth`**.
The pipe was removed and the vertical rule described in words. Recorded in `STATE.md` as a trap:
**no `|` in a sign-off cell, escaped or not.**

**Gates:** `source_check.py` RANGE **PASS** · PAGES **PASS** (offset +7, 18 rows; 7 body refs
monotonic) · DEPTH **PASS** (15/15 রows পূর্ণ) · SIGNOFF **PENDING** (15/15 unsigned) ·
**SLOTS FAIL, still deliberate**. `math_arith_check.py` **CLEAN — 8 verified, 2 uncovered**.

**Chapter not complete — resume at ছাপা ৮ (PDF 15).** Nine printed pages remain, and the ভাগ
half has not begun. Stopped at the resume point rather than thinning the reads (§7.8).

## 2026-08-10 (fresh sitting) · distributive check built and proven (CD-058, CD-059)

**Timeboxed extension, delivered inside the box.** `math_arith_check.py` now reads **equality
chains**: every fully-numeric `=`-separated segment of a line must come to the same number. One
idea covers four printed shapes — distributive expansion, the `( X − ১ )` trick, the ×১০০
rearrangement box, and the split-cell ladder table. Built as a small recursive-descent evaluator
over `+ − × ( )` rather than three pattern-matchers, so shapes not yet met are covered on
arrival. **No `eval`** — an extraction is input.

**Two parser faults the real file exposed.** The ladder row `| ৭৪ | × ২৯ | = | ২১৪৬ |` splits its
operands across cells and was invisible to the original `STEP_RE`. And **every distributive line
on printed ৪ and ৬ was invisible because of the book's own item label**: `(১) ৬০৪২ × ১৫১৪`
tokenises as a parenthesised number juxtaposed with another, so the segment failed to parse —
while the ×১০০ box, which carries no label, read fine. Leading `(১)`/`(ক)` labels are now stripped.

**Seeded both directions, as ruled — 30 cases, all PASS.** Distributive terms summing to the
multiplier and a mutated term going RED; `(X − ১)` matching the left-hand number, with both sides
mutated in turn; the chain holding and one line of it mutated; the ladder row balancing and not;
and a `☐`-bearing segment left unevaluated.

**The result is the point: 8 verified → 18.** The twelve hand checks recorded for printed ৪–৭ are
now **machine-corroborated** instead of resting on one human reading.

**Coverage honesty (CD-059).** The verdict line no longer states a bare count:
`CLEAN — N verified · M uncovered · shapes not parsed: …`, with a `NOT LOOKED AT` line above it,
fed by a census of every numeric-bearing line in the transcribed body that no check consumed —
anchored at the chapter heading so the header's own offset table cannot pad the number. Today:
**`ARITHMETIC LINE NOT PARSED ×8`**, `bare exercise ×20`, `prose carrying numbers ×65`. Only the
first deserves an extension; the other two have nothing to check against, and keeping them apart
is deliberate — collapsing them would inflate the alarm and get the line ignored.

**Gates:** `math_arith_check.py` selftest **PASS** (30 cases) · run **CLEAN, 18 verified, 2
uncovered** · `source_check.py` selftest **PASS** · `canon_check.py` and `tools_check.py` **CLEAN**.
MANIFEST row unchanged and verified at source — already REQUIRED, and `tools/audits` is
SMOKE-exempt.

**Transcription resumes next at ছাপা ৮ (PDF 15)**, unchanged. Long division is a new shape and
will show up in the summary as `÷ long division` the moment it appears; its extension is a named
task, never a loosening.

### 2026-08-10 (same sitting, after the extension) · ছাপা ৮ — ভাগ begins

**Transcribed printed ৮**, which opens the chapter's second half: a `## ভাগ` heading, the ৪২৭৫ ÷
৪৫ word problem, the full long-division working, and অনুশীলন ১'s six divisions. কাজ/অনুশীলন
numbering restarts again, as it has at every মূল প্রশ্ন.

**CD-059 earned its keep on the first page after it was written.** Long division arrived and the
summary named it without being asked: **`NOT LOOKED AT: … ÷ long division ×3`**. Under the old
output this page would have been absorbed into an unchanged count. Per the ruling the gate was
**not** extended for `÷`; printed ৮ was checked at full manual depth instead, and the nine hand
checks are in `evidence/MANUAL_ARITH_p04-08_2026-08-10.txt` — ভাগফল ৯৫, ভাগশেষ ০, every
subtraction row, and ৯৫ × ৪৫ = ৪২৭৫ as the closing check. All consistent.

**Long division is checkable, just not parsed yet** — quotient × divisor + remainder = dividend,
and each subtraction row is divisor × that quotient digit. Recorded in `STATE.md` as the next
extension candidate; seeded tests and a CD row first, never a loosening.

**Gates:** `source_check.py` RANGE/PAGES/DEPTH **PASS** (17/17 sign-off rows পূর্ণ), SIGNOFF
**PENDING**, **SLOTS FAIL still deliberate** · `math_arith_check.py` **CLEAN — 18 verified, 2
uncovered**, with four unparsed shapes named on the verdict line.

**Resume at ছাপা ৯ (PDF 16).** Eight printed pages remain and they are mostly division.

### 2026-08-10 (same sitting) · ছাপা ৯ — both divisions now machine-verified

**Transcribed printed ৯**: কাজ ১ (৬৬৭৪ ÷ ২১৪), the যাচাই পদ্ধতি box stating
**ভাজক × ভাগফল + ভাগশেষ = ভাজ্য** in four coloured plates, and অনুশীলন ২. The plates are
**typeset words, not drawn symbols**, so unlike printed ৬'s সহজ পদ্ধতি box this is ordinary body
content and not §7.5.

**`math_arith_check.py` now verifies both divisions in the file** — ৪২৭৫ ÷ ৪৫ = ৯৫ ভাগশেষ ০ and
৬৬৭৪ ÷ ২১৪ = ৩১ ভাগশেষ ৪০, each with its subtraction rows and the ভাগশেষ < ভাজক invariant.
**20 verified, 2 uncovered.**

**A limitation found on the first page that exercised it, and handled in the open.** The book
teaches division by printing **two boxes for the same division** — the first showing only step one
(quotient `৩`), the second complete (quotient `৩১`). The parser treats any fenced block as a
*complete* division, so fencing the first box would have turned the gate **red on a correct
transcription**. The partial box is therefore deliberately left outside the fence, **with the
reason written into the extraction itself and into `STATE.md`**, and the complete box is fenced and
checked. Teaching the parser to recognise a partial stage is a named task — seeded tests and a CD
row first.

**Gates:** `source_check.py` RANGE/PAGES/DEPTH **PASS** (20/20 sign-off rows পূর্ণ), SIGNOFF
**PENDING**, **SLOTS FAIL still deliberate** · `math_arith_check.py` **CLEAN — 20 verified**.

**অধ্যায় ১ is NOT complete.** ছাপা ১০–১৬ remain — seven printed pages. The long-division
extension took the session's first stretch as ruled, and the chapter did not close. **Resume at
ছাপা ১০ (PDF 17);** SLOTS mapping and the নির্মাণাধীন marker removal still wait on the full read.

## 2026-08-10 (fresh sitting) · CD-061 fence convention; ছাপা ১০ transcribed

**CD-061 recorded as ruled: no parser extension — the fence convention is the rule.** A
pedagogical partial working stays **outside** the ``` fence with its reason written in the
extraction, keeps full manual depth, and is corroborated by the complete working of the same
division fenced on the same page. The revisit condition is written down: a partial with **no**
complete working anywhere becomes a PENDING-P row, not an improvisation.

**The convention earned itself immediately.** Printed ১০ prints **three boxes for one division**
(৬৯৭৩৮ ÷ ২৪৫) — two partial stages and the complete working — where printed ৯ had two. Two
unfenced, one fenced and machine-verified: **৬৯৭৩৮ ÷ ২৪৫ = ২৮৪ ভাগশেষ ১৫৮, three subtraction rows,
ভাগশেষ < ভাজক.** This is a recurring layout in the book, not a one-off, so the rule will be used
on most division pages.

**কাজ ৩'s three blank-bearing division frames solved by hand and each solution matched every
printed cell** — **(১) ৯৯৫৩ ÷ ১৩৯ = ৭১ ভাগশেষ ৮৪ · (২) ২০৪৭৫ ÷ ৩২৫ = ৬৩ ভাগশেষ ০ ·
(৩) ৪৭০ ÷ ২৩ = ২০ ভাগশেষ ১০**. Twenty-one checks in
`evidence/MANUAL_ARITH_p10_2026-08-10.txt`, all consistent. These frames carry `☐`, so the
division parser REFUSEs them by design; they stay at full manual depth.

**One content difference worth a question author's attention:** printed ৯'s যাচাই পদ্ধতি box has
its four plates **filled** (২১৪ × ৩১ + ৪০ = ৬৬৭৪); printed ১০'s সঠিকতা যাচাই box has the same
four plates **empty** for the student. Recorded as printed.

**Gates:** `source_check.py` RANGE/PAGES/DEPTH **PASS** (23/23 sign-off rows পূর্ণ), SIGNOFF
**PENDING**, **SLOTS FAIL still deliberate** · `math_arith_check.py` **CLEAN — 21 verified,
2 uncovered**, three division blocks now checked.

**অধ্যায় ১ is still NOT complete — ছাপা ১১–১৬ remain, six printed pages.** SLOTS mapping, the
নির্মাণাধীন marker removal and the chapter-complete sync all wait on the full read. Resume at
**ছাপা ১১ (PDF 18)**.

## 2026-08-10 (fresh sitting) · **অধ্যায় ১ COMPLETE** — ছাপা ১১–১৬, SLOTS, marker, gate sweep

**The chapter closed.** ছাপা ১১, ১২, ১৩, ১৪, ১৫ and ১৬ transcribed at 400 dpi, then the
MarkLogic slot cross-reference written, the `নির্মাণাধীন` marker removed, and a full gate sweep
run. **Six printed pages this sitting, sixteen in total.**

**`source_check.py` now reports what a finished-but-unsigned extraction should:**

```
[PASS   ] RANGE    stated range অধ্যায় 1-1: all 1 section(s) present
[PASS   ] SLOTS    all 11 MATH spine slots accounted for
[PASS   ] PAGES    offset constant (+7) over 18 verified rows; 16 body refs monotonic
[PENDING] SIGNOFF  35 of 35 spot-check row(s) unsigned
[PASS   ] DEPTH    single-channel source; all 35 sign-off row(s) marked 'পূর্ণ'
VERDICT : NOT DONE — mechanical checks pass; spot-check sign-off owed
```

SLOTS went green only after the chapter had been read end to end — which is what it was held
red for. `math_arith_check.py` **CLEAN — 24 verified · 3 uncovered**, all three `WIDTH` (pure
scaffolds). `source_textcheck.py` **REFUSE**, expected under §7.7. All three selftests PASS;
`canon_check.py` and `tools_check.py` CLEAN. Verbatim: `evidence/GATE_SWEEP_2026-08-10.txt`.

**Five findings recorded in `যেভাবে ছাপা আছে`, two of which a question author must not miss.**
**(a) কাজ/অনুশীলন numbering restarts at every মূল প্রশ্ন** — there are three different "কাজ ১"s
in this chapter, so a citation without a printed page number is ambiguous. **(b) অনুশীলন ৪
(ছাপা ১১) and নিজে করি ৭ (ছাপা ১৬) contain deliberately false statements** — they are true/false
exercises. Those are not transcription errors, no session may "correct" them, and they were kept
out of the arithmetic check, where failing to balance is the *expected* result. Also recorded:
comma grouping is inconsistent within the chapter (৪৬,৮০,০০০ and ১০,০০০ against ১০০০০, ৫০০০০,
৩৭৯৬৮০), and the zero-digit scaffold from CD-060.

**Slot mapping, honestly scoped.** S01–S04 are directly bound and S04 is the chapter's main
source, with নিজে করি ১৪ matching the spine's own "one multi-part problem, 8 marks" shape.
S05–S08, S10 and S11 are marked **absent** with the chapter that owns each. **S09 is recorded as
partial and the limit stated**: metres and grams appear as problem context, but there is no unit
conversion and no area — those belong to অধ্যায় ৮.

**Not done, and named:** the Principal's 35 sign-off rows. **No agent writes in the সই column.**
On signature the file promotes to `canon/sources/c5/math/` and the gate re-runs there.

**Next: অধ্যায় ২ — গাণিতিক বাক্য, ছাপা ১৭–৩০ = PDF 24–37.** 400 dpi rasters exist only to
PDF 23, and **the offset must be re-derived, never carried.**

## 2026-08-10 (fresh sitting) · অধ্যায় ২ opened — offset re-derived, ছাপা ১৭–১৮, CD-062

**Rasters and offset first, as ruled.** 400 dpi rendered for PDF 24–37, then the offset
**re-derived at twelve points, every one inside ছাপা ১৭–৩০** and none of them reused from
অধ্যায় ১: 24→১৭, 25→১৮, 26→১৯, 28→২১, 29→২২, 30→২৩, 31→২৪, 33→২৬, 34→২৭, 35→২৮, 36→২৯,
37→৩০. Constant at **+৭**. It matches অধ্যায় ১'s value, which is the expected result and not
the reason it is recorded — it was derived, not carried.

**ছাপা ১৭ and ১৮ transcribed.** The chapter introduces the unknown as a Bengali letter
(**ক, খ, গ**), খোলা/বদ্ধ sentences, and সত্য/মিথ্যা.

**The chapter's central hazard, found on its first page and written into the file's header.**
**গাণিতিক বাক্য is taught by printing deliberately false statements.** ছাপা ১৭ prints
`৪৮ ÷ ৩ = ৮` ✗, `৪৮ ÷ ৪ = ৮` ✗, `৪৮ ÷ ৫ = ৮` ✗ before `৪৮ ÷ ৬ = ৮` ✓; ছাপা ১৮ prints
`২৫ + ৪ > ৩০` as its worked example of a **false** sentence, and "১২ একটি বিজোড় সংখ্যা" the
same way. **None of these may ever be "corrected", and none may be fed to the arithmetic check.**
They reach no check today only because the evaluator reads neither `÷` nor `>` — **luck, not
design** — and the file says so, so that whoever extends the evaluator excludes the ✗-marked
lines first, with seeds and a decision row.

**CD-062 — a false RED, fixed the session it appeared.** অধ্যায় ২'s first worked equation
reddened a **correct** transcription: `৮ × ক = ৪৮` set the equality chain's carry, the next line
`ক = ৪৮ ÷ ৮` yielded nothing evaluable, and `= ৬` then chained ৬ back to the stale ৪৮ —
`equality chain does not hold: ৪৮ ≠ ৬`. **The skipped line had changed the subject entirely**,
which is what an unreadable line may always have done, so the carry is now cleared whenever a
line yields nothing: **silence is not continuity.** Seeded both ways; selftest **40 cases PASS**;
**অধ্যায় ১ re-run unchanged at 24 verified**, so a false positive was removed without losing
reach. This is a bug fix, not the coverage extension the sitting's ruling barred — a gate that
reddens correct work cannot be left standing, and contorting the transcription to please the
parser would have hidden the flaw while it recurred on every worked equation in the chapter.

**Gates:** `source_check.py` RANGE/PAGES/DEPTH **PASS** (8/8 sign-off rows পূর্ণ), SIGNOFF
**PENDING**, **SLOTS FAIL — deliberate until the chapter is read**. `math_arith_check.py`
**CLEAN — 1 verified** (`৬ × ৪ = ২৪`), which is the honest yield of two pages whose content is
mostly equations with unknowns.

**Chapter NOT complete — ছাপা ১৯–৩০ remain, twelve printed pages.** Resume at **ছাপা ১৯ (PDF 26)**;
rasters and tiles for the whole chapter are already on disk.

### 2026-08-10 (same day) · CD-063 recorded — ✗-marked lines get inverted expectation, not exclusion

**Ruling captured, nothing implemented — by design.** The Principal ruled how the future `÷`/`>`
extension must treat this chapter's deliberately-false lines: **not excluded from the arithmetic
check, but checked with inverted expectation.** A **✗**-marked line that *balances* goes **RED**;
a **✓**-marked line that does *not* balance goes **RED**.

**The reasoning is worth keeping verbatim, because it inverts the intuition.** Excluding the ✗
lines leaves a hole precisely where a mis-read hides: the book prints `৪৮ ÷ ৩ = ৮` ✗, and a
transcription that mis-reads the divisor as ৬ makes the line **true** — an excluded line is
checked by nothing, so that error passes silently. Inversion catches exactly that. **The mark is
data, and the check should read it** rather than treat it as a reason to look away. The
consequence is that on this chapter the ✗ lines become the *most* strongly checked content in the
file, because a mis-read that flips a false statement true is the one error no other channel sees.

**Recorded in three places, deliberately.** `canon/DECISIONS.md` **CD-063** (the ruling and its
sequencing); the extraction's warning block, now carrying the four-way expectation table, since
that is what a transcriber reads; and a design-note comment in `math_arith_check.py` beside
`EXPR_OK`, since that is where whoever adds the operators will actually be working.

**Nothing was built.** The evaluator reads neither `÷` nor `>`, so no ✗ line reaches any check
today, and inversion built ahead of the operators would be untested machinery (CD-020). When the
extension comes it carries inversion with it, **seeded all four ways**. Until then the
extraction's warning block is the guard, and it says so.

**Gates unaffected, verified rather than assumed:** `math_arith_check.py --selftest` **PASS**,
অধ্যায় ১ re-run unchanged at **24 verified**, `canon_check.py` and `tools_check.py` **CLEAN**.

**Transcription unchanged: resume at ছাপা ১৯ (PDF 26)**, twelve printed pages of অধ্যায় ২ left.

## 2026-08-10 (fresh sitting) · অধ্যায় ২ — ছাপা ১৯–২০

**Transcribed ছাপা ১৯ and ২০.** ছাপা ২০ opens a new sub-section, **হিসাবের ধারাবাহিকতা**
(order of operations), with the three printed rules and the bracket order ( ) → { } → [ ].

**The CD-063 hazard arrived early, and not by the route we expected.** The warning written
yesterday said the false-by-design lines do not reach the evaluator because it reads neither `÷`
nor `>`. **ছাপা ১৯ broke that:** the book's own worked trial is
`১ × ২৪ + ১৫০ = ২৪৬` → `২৪ + ১৫০ = ২৪৬` → `১৭৪ = ২৪৬`, with the book's verdict **মিথ্যা**
printed beside it. That chain uses only `+` and `×` — **operators the evaluator already reads.**
The hazard did not wait for `÷`.

**Handled without contorting the transcription.** The book prints this as a **table** — worked
steps on the left, its own verdict on the right — so the transcription is a table too, and a
table cell's `|` means `evaluate()` reads nothing. **The book's own layout is the guard.** Written
into `STATE.md` with the rule for what comes next: if a later false-worked block is printed as a
table, transcribe it as one; **if it is not, stop and ask — do not invent a layout to please the
parser.** That is the CD-061 discipline applied to a new shape, not a new convention.

**Manual-depth arithmetic recorded** for both pages in
`evidence/MANUAL_ARITH_ch2_p19-20_2026-08-10.txt` — including the confirmation that the book's
মিথ্যা verdict is itself correct (১৭৪ ≠ ২৪৬), and every step of ছাপা ২০'s six-step chain and its
bracket contrast (১২÷২×৩ = ১৮ against ১২÷(২×৩) = ২). All consistent.

**Gates:** `source_check.py` RANGE/PAGES/DEPTH **PASS** (14/14 sign-off rows পূর্ণ), SIGNOFF
**PENDING**, **SLOTS FAIL — deliberate**. `math_arith_check.py` **CLEAN — 3 verified**, no false
RED. The census names `÷ long division ×13` and `ARITHMETIC LINE NOT PARSED ×2`, which is the
honest picture of a chapter built on `÷` and brackets.

**Chapter NOT complete — ছাপা ২১–৩০ remain, ten printed pages.** Resume at **ছাপা ২১ (PDF 28)**.

## 2026-08-10 (fresh sitting) · CD-064 — ÷, marked comparisons and CD-063 inversion built; ছাপা ২১

**Built inside the timebox, as re-sequenced.** CD-063 had put inversion behind the operator
extension on the assumption the hazard waited on `÷`; ছাপা ১৯ disproved that, so the Principal
re-sequenced and this sitting built both together.

**`÷` evaluates exactly, as `Fraction`.** Not floor — `৫০ ÷ ২৪` floors to ২, the same as the
correct `৫০ ÷ ২৫`, so floor division would make a mis-read *look* right. Not float either, which
would import a tolerance the book never asked for.

**The mark is read as data.** `✗ ✘ মিথ্যা` set the expectation to *does not hold*; `✓ ✔ সত্য` to
*holds*. One implementation detail turned out to matter: **the mark must be stripped before the
line is split**, or the segment carrying it evaluates to nothing and the chain silently vanishes —
handing the mark's whole purpose back to luck. **An unmarked comparison is not assumed true**:
ছাপা ১৮ prints `২৫ + ৪ > ৩০` with its verdict two speech-bubbles away, so assuming would redden a
correct transcription. No mark, no claim — uncovered, never RED.

**Selftest 53 cases, all PASS**, seeded all four ways plus the boundaries, including the verdict
**word** মিথ্যা as the mark, an unmarked comparison REFUSEing, and a table-held marked block still
REFUSEing — so **CD-061's layout protection is now itself under test**.

**A seed had to be re-cut, and that is the more useful finding.** CD-062's fixture
(`ক = ৪৮ ÷ ৮`) stopped exercising the carry guard the moment `÷` became readable — the chain now
legitimately joins. The guard is unchanged and still needed; the fixture was replaced with a
genuinely unreadable prose line. **A seed that silently stops biting is worse than a missing one**,
and it only surfaced because the selftest was re-run rather than assumed.

**Yield:** অধ্যায় ২ **3 → 8 verified**, ছাপা ২০'s `÷` chains now machine-checked; অধ্যায় ১
**unchanged at 24**. **Stated limit:** the ✗ blocks on ছাপা ১৭ and ১৯ are table-held and stay at
full manual depth — inversion reaches prose-form lines only.

**ছাপা ২১ transcribed** — কাজ ৩'s arrow diagram (৬৪৩২ · ২৩১ · ১৫৩) and কাজ ৪–৫'s bracket
skeletons, where **every computed cell is blank**: the book prints the bracket structure and the
student fills it, so there is no printed digit to machine-check and the statement figures went
through at full manual depth.

**The extraction's warning block was rewritten, not left standing.** It had said the false lines
"do not reach the machine" — true yesterday, false after CD-064. **A file may not tell an old
story about its own guard.** It now carries the four-way expectation table and the explicit note
that table-held blocks remain uncovered.

**Chapter NOT complete — ছাপা ২২–৩০ remain, nine pages.** Resume at **ছাপা ২২ (PDF 29)**.

## 2026-08-10 (fresh sitting) · অধ্যায় ২ — ছাপা ২২ ও ২৩

**Transcribed ছাপা ২২ and ২৩.** কাজ ৬'s two named solutions, কাজ ৭–৮ (salary and water-tank),
কাজ ৯'s three priced furniture plates, and কাজ ১০'s bar diagram.

**A layout judgement, made explicitly rather than by habit.** ছাপা ২২ prints সমাধান-১ and
সমাধান-২ side by side in a bordered two-column box. Rendering that as a markdown table would have
put every printed digit behind a `|` and out of the checker's reach. **Both renderings are equally
faithful to the content, so the one that gets checked was chosen** — two labelled blocks — and
সমাধান-২ is now machine-verified (`২০০০ − (২৪০ × ৫ + ১২০ × ৩) = ২০০০ − ১৫৬০ = ৪৪০`). The rule is
now stated in one line in `STATE.md`: **keep the book's content intact and prefer the form that is
checked — except for false-marked blocks, where protection comes first** (CD-061), which is why
ছাপা ১৭ and ১৯ stay tabular. A new false-worked block *without* a table in the book still means
stop and ask.

**সমাধান-১'s rows carry Bengali labels** (`বাসমতি চাল ২৪০ × ৫ = ১২০০`), so the evaluator reads no
chain there — correct behaviour, a labelled row is not a bare identity. Those four identities were
hand-checked, and সমাধান-২ reaches the same ৪৪০ from the same figures, which corroborates them.

**Gates:** `source_check.py` RANGE/PAGES/DEPTH **PASS** (20/20 sign-off rows পূর্ণ), SIGNOFF
**PENDING**, **SLOTS FAIL — deliberate**. `math_arith_check.py` **CLEAN — 10 verified**, no false
RED anywhere in the chapter.

**`STATE.md` had gone self-contradictory and was repaired.** It still carried the pre-CD-064
paragraphs saying inversion was unimplemented and `÷` unreadable, directly above the live text
saying the opposite. Both stale blocks were removed. **A resume file that argues with itself is
worse than a short one** — the next session reads it first and cannot tell which half is current.

**Chapter NOT complete — ছাপা ২৪–৩০ remain, seven pages.** Seven were done this sitting (১৭–২৩
cumulative). Resume at **ছাপা ২৪ (PDF 31)**; SLOTS, the নির্মাণাধীন removal and the full sweep all
still wait on the complete read.

### 2026-08-10 (same day) · CD-065 — rendering-choice rule ratified and promoted to canon

**Ratified as ruled, and moved out of the workstream.** Where two renderings are equally faithful
to the book's content, the one the checker reads wins. **Faithfulness stays the constraint and is
never traded** — the rule only chooses *among* renderings that already satisfy it. On a
single-channel source (§7.7) the difference is the whole margin: a correct-but-unchecked
transcription is weaker than the same transcription checked.

**The exception is kept sharp because it points the other way.** For a block the book itself
marks false — `✗`, or a verdict cell reading মিথ্যা — **protection comes first and it stays
table-held.** CD-064's inversion reaches prose-form marked lines, so making an already-held block
machine-readable would trade a working guard for a partial check. And the boundary is a **stop,
not a judgement call**: a false-worked block the book does *not* print as a table is a PENDING-P
row. Inventing a layout to keep a gate quiet is the failure CD-061 rejected; inventing one to make
a false block checkable is that same failure in reverse.

**Promoted deliberately.** The rule was written into `canon/_wip/c5-math/STATE.md` when ছাপা ২২
forced the choice — and **a rule that lives only in a workstream's state file dies with the
workstream.** Recorded as **SOURCE_POLICY §7.11** (v1.6) with **CD-065**; `STATE.md` now **cites**
it rather than holding a second copy, per AGENTS.md §8 (canon is cited, never copied). The resume
checklist was updated in the same pass so the next session is pointed at all three conventions —
the fence rule, the ✗/✓ inversion, and now §7.11.

`canon_check.py` **CLEAN**. No transcription this pass; **resume unchanged at ছাপা ২৪ (PDF 31)**,
seven pages of অধ্যায় ২ remaining.

## 2026-08-10 (multi-chapter sitting) · CD-066/067 recorded · **অধ্যায় ২ COMPLETE**

**Two rulings folded in first.** **CD-066** (SOURCE_POLICY §7.12): a pure-exercise section — no
printed working, no answers, no ✗/✓ marks — is transcribed at the 150 dpi render **with the
numerals themselves read at 400+ dpi via spot-crops**. The point is that this is not the
relaxation CD-054 refused: it lowers the depth of the *page furniture* while the numerals, which
are what CR-001 was written about, are read exactly as before. Exercise-only sign-off rows state
the convention so the Principal reads the depth rather than inferring it. **CD-067** (§7.13):
cadence is now up to three complete chapters per sitting, **chapter close atomic**, and the
**stop-rule explicitly outranks the ceiling** — the near-miss record (`ঝকঝাক`, `প্রচন্দ`, `শীঁখ`,
the eight-box count) is written in as the standing reason. §7.8 is left as written, forward-only.

**অধ্যায় ২ closed.** ছাপা ২৪–৩০ transcribed, slot cross-reference written, `নির্মাণাধীন` marker
removed, full sweep run:

```
[PASS   ] RANGE    stated range অধ্যায় 2-2: all 1 section(s) present
[PASS   ] SLOTS    all 11 MATH spine slots accounted for
[PASS   ] PAGES    offset constant (+7) over 12 verified rows; 14 body refs monotonic
[PENDING] SIGNOFF  33 of 33 spot-check row(s) unsigned
[PASS   ] DEPTH    single-channel source; all 33 sign-off row(s) marked 'পূর্ণ'
VERDICT : NOT DONE — mechanical checks pass; spot-check sign-off owed
```

`math_arith_check.py` **CLEAN — 10 verified**; `source_textcheck.py` **REFUSE** per §7.7; three
selftests and both repo gates clean. Verbatim: `evidence/GATE_SWEEP_CH2_2026-08-10.txt`.

**Five printed-as-is findings, two that bite question authors.** কাজ/অনুশীলন numbering **restarts
at every sub-section** — this chapter has three separate "কাজ ১"s, so a citation without a printed
page is ambiguous. And the chapter is **built on deliberately false statements** (ছাপা ১৭, ১৮,
১৯), which must never be corrected. Also recorded: inconsistent comma grouping (**৬২৫,৮০০**
against ৭০৫০০ and ৩১২৫ on the same page), and **‘মুনাফা’ appearing in অধ্যায় ২** with no
percentage arithmetic — so `MATH-S07` does **not** draw from here.

**Slot mapping scoped honestly.** S01–S04 directly bound, S04 the main source with নিজে করি ১৫
matching the spine's own multi-part shape; S02 is unusually strong here because the whole chapter
rests on filling blanks. **S09 recorded as partial with the limit stated** — metres, litres, kilos
and days appear as context, but there is no unit conversion and no area. And **ছাপা ২৬'s
day↔cloth table is explicitly *not* S11 উপাত্ত** — it is a unitary-method computation grid, not
data collection, and that distinction is exactly the kind a question author would otherwise get
wrong.

**অধ্যায় ৩ not started, and that is the stop-rule working.** CD-067 permits three chapters;
অধ্যায় ৩ is eighteen printed pages and needs its own offset derivation and a fresh 400 dpi render
(PDF 38–55 do not exist yet). Beginning it here would have meant starting a chapter I could not
close at full care. **Three is a ceiling, never a target** — the sitting stops with two chapters
complete rather than three half-done.

**Owed to the Principal: 68 sign-off rows** (35 for অধ্যায় ১, 33 for অধ্যায় ২). No agent writes
in the সই column.

## 2026-08-10 (multi-chapter sitting, continued) · অধ্যায় ৩ opened — ছাপা ৩১–৩২

**Rasters and offset first, as instructed.** 400 dpi rendered for PDF 38–55, then the offset
**re-derived at twelve points, all inside ছাপা ৩১–৪৮**: 38→৩১, 39→৩২, 41→৩৪, 43→৩৬, 45→৩৮,
47→৪০, 49→৪২, 50→৪৩, 51→৪৪, 53→৪৬, 54→৪৭, 55→৪৮. Constant at **+৭**. **Ten of the twelve are
fresh; two (PDF 38 and 50) also appear in অধ্যায় ১'s table** — 38 because it is this chapter's
opening page. **The overlap is written into the file rather than quietly presented as twelve new
points**; the values were read fresh from this chapter's raster either way.

**ছাপা ৩১ and ৩২ transcribed** — গুণিতক, সাধারণ গুণিতক, two Venn diagrams and two ১–২৫ strips.

**Two findings, both properties of the book.** ছাপা ৩১'s first table skips **৭, ৮, ৯** (১–৬ then
১০ then ২০) and its second skips **৯** (৮ then ১০): the tables are samples, not runs, and were
not "corrected". And ছাপা ৩২'s two ১–২৫ strips are **identical with no cell pre-marked** — the
student circles them. **Both strips were read separately at 400 dpi rather than assumed identical
from appearance**, which is the same discipline CR-002 was written about.

**Machine coverage here is essentially nil, and that is the honest result.**
`math_arith_check.py` returns **REFUSE** on the file: these two pages carry multiple-lists and
Venn diagrams, not worked equations. REFUSE means *nothing was verified*, and reporting CLEAN
would have been a lie. The numerals were carried by targeted 400 dpi crops of every table, strip
and Venn region instead.

**CD-066 has not been used yet, and the reason is worth recording:** ছাপা ৩১ and ৩২ are both
teaching-dense — definitions, tables, diagrams — not pure-exercise sections. **The convention's
test is content, not heading**, so it waits for a genuine exercise-only section. Its first use
will state **পূর্ণ (§৭.১২)** in the depth column.

**Stopping here at a stated resume point — ছাপা ৩৩ (PDF 40).** CD-067 allows three chapters, and
two are closed; অধ্যায় ৩ is eighteen pages and sixteen remain. Continuing now would mean reading
the back of a dense chapter with attention already spent, which is exactly what the near-miss
record argues against. **The ceiling is not a target.**

## 2026-08-10 (continued) · অধ্যায় ৩ — ছাপা ৩৩–৩৪

**Transcribed ছাপা ৩৩ and ৩৪** — লসাগু defined, then extended to three numbers, plus the tile
problem and the two-bells exercise.

**Two layout facts worth recording rather than smoothing.** ছাপা ৩৪'s ৬/৮/১২ multiples grid
carries **two diagonal ellipses**, and they are diagonal for a reason: ২৪ and ৪৮ fall in
*different columns* in each of the three rows (২৪ is 4th, 3rd and 2nd respectively). A reader who
expects vertical grouping would mis-describe what the book shows. And the tile table marks four
cells with circles joined by arrows — ১৮↔১৮ and ৩৬↔৩৬ across the দৈর্ঘ্য and প্রস্থ rows.

**Every table checked against its own rule by hand** —
`evidence/MANUAL_NUMERALS_ch3_p31-34_2026-08-10.txt`, all consistent: ছাপা ৩১'s two tables against
×৪ and ×৩, the Venn intersections on ৩২ and ৩৩ against the actual common multiples, ছাপা ৩৪'s
three multiple-rows, and the tile table against ৯×n and ৬×n. **This is the substitute for a second
channel on these pages** — `math_arith_check.py` REFUSEs here because there are no worked
equations to read, only lists, diagrams and rate tables. The gate saying "nothing verified" is
correct, so the verification had to be done and written down elsewhere.

**CD-066 still unused.** ছাপা ৩৩ and ৩৪ are teaching-dense like their predecessors — definitions,
worked grids, diagrams. The convention's test is content, not heading, and no exercise-only
section has appeared yet.

**Stopping at ছাপা ৩৫ (PDF 42).** Four pages this stretch, fourteen remain in the chapter. Two
chapters are closed and the third is a third done; the near-miss record argues against pushing a
dense chapter on spent attention, and **the ceiling is not a target**.

## 2026-08-12 · Teacher content-check returned — C5 Bangla and C5 English

**Both teacher checks are back.** C5 **Bangla: clean**, no findings. C5 **English: three findings,
all in one place** — Unit 14, section 3.1 (Language Focus: *want to be…*), the three underlined
example sentences on ছাপা ৭৭.

**The findings were checked against the raster and the file is already right.** `pdf-083.png`
(ছাপা ৭৭ = printed folio + 6) shows the yellow Language-Focus box underlining exactly:

```
• I want to be a teacher.        → underline spans "want to be"
• He wants to be a doctor.       → underline spans "wants to be"
• She wants to be a painter.     → underline spans "wants to be"
```

`C5_ENG_Source_14.md:113–115` carries precisely these three spans. **Closed as no-change.** The
underline is on the finite verb *plus* the infinitive and stops before the article — it does not
run to the profession, and it does not shrink to *want/wants* alone. Recording the shape here
because it is the kind of detail a later pass would "tidy" in the wrong direction.

**The one real gap the check exposed was evidentiary, not textual.** Unit 14's evidence folder
held p074, p074_boundary and p078 — ছাপা ৭৭ had no committed raster, so the flagged section could
not be adjudicated from evidence alone. **`evidence/C5_ENG_U14_p077.png` added** (copied from the
regenerable working raster, which is itself gitignored under CD-046/CD-047; the `!**/evidence/*.png`
negation commits this one). A section that draws a content-check should carry its own page.

**Sign-off status unchanged: Units 2–20 still BUILT, sign-off owed.** Nothing was promoted. The
teacher check is an input to the Principal's spot-check, not a substitute for it (SOURCE_POLICY
§7.4, AGENTS.md §2) — promotion still waits on the Principal's "done".

## 2026-08-12 (continued) · CD-084 — teacher check closes sign-off; 28 files promoted

**The Principal ruled the 2026-08-12 teacher content-check IS the §2.3 spot-check** for C5
English Units 2–20 and C5 Bangla পাঠ ১–১১. **The authority was already there and was being read
too narrowly:** §2.3 says *the Principal **or the teacher*** confirms the sampled passages, and
`source_check.py`'s PENDING message says the same — but all thirty file headers said
`কেবল প্রধান শিক্ষক সই করেন`. **The scaffolding was stricter than the policy it implements**,
which is CD-079(b)'s observation arriving from the other side: agent-authored sign-off structure
drifts from the ruled text, and **a gate that is too strict never goes red, so nothing catches it.**

**95 of 98 rows signed `Teacher · 2026-08-12`. Three held, and the exclusion is §7.5's:**
`C5_ENG_Source_04.md` (two maps, ~75 drawn place names), `C5_ENG_Source_11.md`, and
`C5_BAN_Source_02.md` (ছবির ভেতরের আঁকা লেখা — “বুম! বুম!!”, ছাপা ১৪). Artwork-borne text has no
second channel at all, so CD-048(b) puts it outside §7.4's sampling and keeps it Principal-only.

**The third held file was not in the ruling as put to the Principal**, which named only English
Units 4 and 11. It is held anyway: §7.5 reaches it identically, and excluding it would have been
an artefact of which files the agent happened to enumerate when writing the question. Recorded
rather than smoothed, because the ruling's *scope* was widened by the agent and the Principal
should see where.

**Promoted: 28 files.** 17 English units to `canon/sources/c5/english/`, 10 পাঠ to the new
`canon/sources/c5/bangla/`, each with its own evidence. **Every one GREEN** —
`evidence/SOURCE_CHECK_2026-08-12.txt` in both destinations. The three held files stay in
`_wip/` at SIGNOFF PENDING, **and the gate keeps them there without help**: `check_signoff`
reports PENDING while a row's সই/তারিখ cells read `—`, so a later session that skims CD-084 and
sees "signed" still cannot promote them.

**Shared sweep evidence was copied, not moved** (`GATE_SWEEP_2026-08-09`,
`TEXTCHECK_RESIDUAL/SELFTEST`, both `TEXTLAYER_ARTEFACTS` files) — the held units still cite it,
and a moved file would have left three `_wip` extractions citing evidence that is no longer
beside them.

**Gates after promotion:** `source_check.py` 28/28 **GREEN** at the new paths ·
`--selftest` **PASS** · `bangla_script_check.py` **CLEAN** (0 in authored text) ·
`canon_check.py` **CLEAN (0 fail, 1 warn)**, 3.3 s.

**Push held.** Per CD-083(c) the range must be classified before any push, and this session's
commits are extraction/governance work that has not been approved for sync.

## 2026-08-12 (continued) · the three artwork rows signed — C5 English and C5 Bangla step ① CLOSED

**The Principal verified the artwork-borne text against the rasters and signed all three held
rows.** Unit 4's **64 district names (ছাপা ১৬)** and **11 upazila names (ছাপা ১৮)**, Unit 11's
**8 map labels (ছাপা ৬০)**, and পাঠ ২'s **“বুম! বুম!!” (ছাপা ১৪)** — every one full-check, never
sampled, because §7.5 text has no second channel to sample against.

**The signature was held once before it was given, and that is the part worth recording.** The
first answer was an immediate "all are ok" with no reading in between. **Signing on it would have
written a verification into canon that had not happened** — a full-check row asserting ~75 drawn
place names were compared. The rasters were rendered and put in front of the Principal instead,
with the transcribed lists beside them, and the signature followed the comparison. **CR-002,
CR-003 and CR-006 are all the same lesson from different angles — counting, single readers,
resolution — and a sign-off row taken on trust is the one place none of those gates reach.**

**One defect fixed while signing: `C5_ENG_Source_04.md`'s sign-off row had an empty ছাপা পৃষ্ঠা
cell**, now `১৬ · ১৮`. The two maps sit on two different pages, so no single number ever fit and
the cell was left as `—`. **It was invisible to the gate** — `check_signoff` reads the সই/তারিখ
pair, not the page cell — so it survived the CD-084 pass and every sweep before it.

**A near-miss on the way in, caught by printing the table instead of trusting the edit.** The
first substitution keyed on `| — | — |` and Unit 4's row read `| … | — | — | — |` (page, সই,
তারিখ all empty), so it filled **page and সই** and left তারিখ as `—`. The row would have read
`| Principal | 2026-08-12 | — |` — **and the gate would have gone GREEN**, because the pair it
tests was full. **A column-blind regex on a table with a variable number of columns**, which is
the CD-070 substring-luck shape once more.

**Promoted the last three files with their evidence. Step ① for both books is CLOSED:
20/20 English units and 11/11 Bangla পাঠ, `source_check.py` GREEN on all 31**
(`evidence/SOURCE_CHECK_2026-08-12_final.txt`, both destinations).

**`CORRECTIONS.md` and `EXCLUDED_paath_12.md` deliberately left in `canon/_wip/c5-bangla/`** —
CD-050(b) cites the exclusion file at that exact path. The now-empty `evidence/` directories in
both `_wip` folders could not be removed (sandbox cannot rmdir); they carry no tracked files and
git will not record them.

---

## 2026-08-14 · Cowork · P00/P04 unification session 1 (import + REF resolver + SB baseline)

**Agent:** scd-agent-cowork. **Lane:** unification/import. Math extraction lane untouched.

**Step 0 verified at source before anything moved.** AGENTS §5/§8 confirmed as cited.
**No clause governs non-source `_inbox` classification** — SOURCE_POLICY §2.1 covers scanned NCTB
books only, and a repo-wide grep for `_inbox` across AGENTS/REGISTRY/canon README/all LOCAL.md
returned zero hits. Next-free verified: the CD number after CD-084 · D-PROJ00-073 · D-054 master · D-PROJ04-017 ·
QB-D-013.

**Two advisor premises were wrong and both were caught by checking at source.**
- **Q-4:** REF-19 v1.10 carries **zero `TOP-` strings** — its IDs are slugs (`BAN-POEM`). The
  numbers live in `canon/topics/TOPIC_NUMBERS.md` (CD-043/CD-044). No REF-19 supersede was owed.
- **Q-5:** the two retired-numbered canon files are **byte-identical** to P00's REF-01 and REF-20
  (md5 `8289b9b7…`, `de8db3b8…`). There was no content divergence to adjudicate — one lineage
  under two naming conventions. The expected recurring-cast content is in neither file; CD-006 had
  already assigned it to the storybook venture.

**Imported.** `canon/refs/` — 22 REF files + register (33 rows: ACTIVE/REFERENCE/POINTER/
NOT-STAGED/RESERVED + 2 HISTORICAL aliases). REF-19 and the four MarkLogic spines were **not**
copied — already canon; rows point at existing paths (§8). REF-04 and REF-06 were found **already
staged** under non-REF filenames, against a ruling that expected them absent.
`workstreams/curriculum-foundations/` (P00 registers, canonical home of the master D-series) ·
`workstreams/p01-nctb-stability/` (scaffold only) · P04 folded into question-banks.
lesson-plans READ-ONLY copies replaced with pointers after recording their contents.

**Renamed per UD-60(b):** `REF-1_Curation_Policy.md` → `REF-01_Curation_Policy.md`, `REF-2_Content_Register.md` →
`REF-20_Approved_Names_Pool.md`. 247 historical SB citations across 51 files left as written.

**Ruled this session:** U14 কুপোকাত is **Drama `-09`** (QB-CR-009, execution owed — items not
re-tagged in place). **`TOP-BAN-C5-14`/`-15` minted**; PENDING-P-008 **closed for C5 Bangla**,
still FLAGGED overall.

**Gate work — and the defect it caught in itself.** `canon_check.py` gained **REF-CITE** and the
**SB baseline census**. The first REF-CITE draft normalised ids with `int()`, so `int("01") ==
int("1")` collapsed **REF-01 and the retired one-digit support-book number into one key** and every SB citation silently stopped being
censused **while the gate still printed CLEAN** — the very collision the check was built to police,
reappearing inside it. Caught by the census seed, not by the clean run. Logged **CR-012** in the
new `tools/CORRECTIONS.md` and named a **PATTERN candidate** with QB-CR-008:
*normalising an ID discards the thing that makes it an ID.* Two instances; a third promotes it.

**REF-06** (`.docx`, the only binary in `canon/refs/`) gained a DERIVED markdown twin; the recorded
regeneration command was proven to reproduce it byte-for-byte. §3.6's Bloom bands verified against
REF-17 §5.2 / REF-18 §4.2 — **faithful, nothing stale downstream**.

**Gates:** `canon_check.py` CLEAN (0 fail, 2 warn — down from 52) · `--selftest` **PASS 15/15** ·
`tools_check.py` CLEAN.

**Held as draft, NOT adopted:** `_wip_PROPOSAL_AGENTS_inbox_section.md`. This session's
classification ran under it held as draft, recorded as such rather than claimed as compliance.

---

## 2026-08-14 · P00/P04 unification session 2 — the policy layer (Cowork, `scd-agent-cowork`)

**Scope as given:** close seven session-1 follow-ups, land the policy layer, supersede the §9 names.
**Not a source-extraction session** — `canon/_wip/c5-*` and the Math lane's `_inbox` files were not
touched. Gates were not built beyond the one ruling that directed a gate change (CD-085).

**Outcome in one line: Step 1 closed in full; Step 2 STOPPED on three at-source discrepancies in
the staged draft; Step 3 therefore did not open**, per its own precondition ("only after §2 commits").

### Step 0 — verified at source

- **Next free CD = CD-085.** `canon/DECISIONS.md` defined `CD-001…CD-084`, continuous, no gaps; the
  only higher token in the repo is the constructed `CD-999` seed fixture (CD-080(e)). Registers
  touched this session and their next-free at entry: `tools/CORRECTIONS.md` → **TOOLS-CR-001** (new
  prefix, this session); `canon/refs/MANIFEST.md` → **REF-27** (RESERVED row, unchanged — no new REF
  minted). `workstreams/question-banks/CORRECTIONS.md` next-free **QB-CR-010**, not used.
- **REF-01 · 09 · 10 · 19 · 20 · 25 · 26 all resolve** to files present at their stated paths
  (sizes recorded in the session report). Zero manifest rows dangle.
- **SOURCE_POLICY §7.16's backtick exemption exists**, at `canon/sources/SOURCE_POLICY.md:574`,
  quoted verbatim in CD-085(b). Its wording supports the analogy CD-085 draws; the section was read
  before it was leaned on, not after.

### Step 1 — the seven follow-ups (eight items)

1. **REF-CITE backtick exemption → CD-085.** Census **247 → 237**, 51 files unchanged; 10 exempted
   across 5 files. Seven seeds both directions, all PASS. Baseline re-frozen by ruling; the gate was
   CLEAN against the *old* baseline first, so nothing was laundered.
2. **AGENTS.md §12 adopted → CD-086.** Protocol **v1.2 → v1.3**. §12.1 prose lead accepted; §12.4
   flag rejected on the record with its reason written into the section; **§12.7 retention added**.
   `_wip_PROPOSAL_AGENTS_inbox_section.md` deleted per its own adoption clause.
3. **U14 re-tag NOT executed.** `QB-CR-009` re-read at source and stands **RULED — execution owed**;
   the bank is opened once, in the bank lane's own session, not twice. No bank file touched.
4. **`TOOLS-CR-###` prefix → CD-087(a)(b).** `CR-012` → **`TOOLS-CR-001`**. The renumber corrected a
   **live collision**: the Math lane already held its own CR-012 (`5634a5f`, 2026-08-12) with three
   citations. Math lane untouched.
5. **`_ref06_header.txt` → `tools/`** → CD-087(c). Byte-identical (md5 `7d0927be…`); REF-06's pandoc
   command and the `canon/MANIFEST.md` row both updated, the latter into a new Retired-rows table.
6. **P01 register — NEITHER case applies as stated; nothing built.** See the batched questions.
7. **Assets placeholder retired** → CD-087(d). Gate warns: `tools_check` 3 → 1, `canon_check` 3 → 1.
8. **PATTERN promoted at four instances → CD-088.** CD-034 checked and confirmed as instance 3; the
   session's own `CR-012` collision is instance 4. **Gate proposed, not built.**

### Step 2 — the policy layer: STOPPED

`_inbox/QUESTION_POLICY_v0.2_DRAFT.md` was read against the files it cites. **The five named checks
verified clean** (§3 row 2 · §3 row 9 · §3 row 18 · §4 · §9). **Three discrepancies were found
outside them**, in §5 and §7, and the draft was **not corrected by the agent** and **not committed**.
Detail and verbatim source quotations are in the session report.

### Step 3 — not opened

Its precondition is "only after §2 commits". §2 did not commit. No supersede was written; REF-01,
REF-09, REF-10, REF-25, the MarkLogic QuestionPolicy and QUESTION_BANK_POLICY are **untouched**.
Conventions v1.4 untouched as instructed.

### §12.7 retention — `_inbox/` at session close (first exercise of the new rule)

**16 files. The rule found three STOP conditions on its first run.**

| Staged file(s) | Since | Why still staged | Owner |
|---|---|---|---|
| `QUESTION_POLICY_v0.2_DRAFT.md` | 2026-08-14 | **Held by Step 2's stop.** Three at-source discrepancies reported; the agent is forbidden to correct the draft. Moves on the Principal's ruling on those three. | **Principal** |
| `C5_MATH_OCRDRAFT_ch3.md` · `ch4.md` · `ch5.md` | 2026-08-10 → 08-11 | ⚠ **§12.4 STOP — same ID, different bytes.** Each differs from its committed evidence twin in `canon/_wip/c5-math/evidence/` (ch3 `27b3f37a` vs `7029e20e`; ch4 `60e9039b` vs `ab8c7659`; ch5 `ede7b507` vs `24e3c57a`). Committed copies are 2–3 KB larger, consistent with an added `MACHINE OUTPUT` header — **but §12.4 says a gate can detect this and cannot rule on it.** Not touched. | **Principal** (version question) |
| `C5_MATH_OCRDRAFT_ch6.md` | 2026-08-12 | Byte-identical to its committed evidence twin (`cb8e331e`) — **redundant staged copy**, §12.4 first bullet. Deletable on approval; not deleted. | Principal (approval) → agent |
| `C5_MATH_OCRDRAFT_ch7.md` · `ch8.md` · `ch9.md` · `ch10.md` | 2026-08-12 | ⚠ **No committed evidence copy exists.** `_inbox/` is gitignored, so these four exist **on one machine only** and are not recoverable from git. Chapters 7–10 are the Math lane's open work. | Math lane session |
| `Class 5 Bangla.pdf` · `Class 5 English.pdf` · `Class 5 Math.pdf` · `C5_Science.pdf` | **2026-04-28** | The four NCTB source scans. Correctly staged — SOURCE_POLICY §2.1 governs them and AGENTS §12.1 explicitly does not touch them. **Named here because 108 days unnamed is the condition §12.7 exists to end**, not because their placement is wrong. | Principal (retention) |
| `NotoNaskhArabic-Medium.ttf` · `-SemiBold.ttf` | 2026-08-09 | **Unvendored and unconsumed.** `tools/render/fonts/` carries Naskh **Bold** and **Regular**; nothing in the repo references Medium or SemiBold. Either they slot under §12.1's Assets class with a `tools/MANIFEST.md` row, or they are surplus. Unclassifiable without a consumer → §12.3 reported, not moved. | Principal |
| `README.md` | 2026-08-09 | The staging folder's own note. Permanent; not staged content. | — |

### Gates — repo-wide, at close

`canon_check.py` **CLEAN (0 fail, 1 warn)** · `tools_check.py` **CLEAN (0 fail, 1 warn)** ·
`bangla_script_check.py` **CLEAN (0 in authored text)** · `canon_check.py --selftest` **PASS (20/20)**.
Verbatim output pasted in the session report per AGENTS §5.

### Sync

**Committed, not pushed.** New governance text beyond the rulings as given is present (AGENTS §12's
prose lead, the gate code, the manifest notes), so **CD-079(b)'s ruling-only carve-out does not
apply** and the push waits on explicit Principal approval with the CD-083(c) range check pasted.

---

## 2026-08-14 · P00/P04 unification session 2 — continuation: the policy layer lands

**Seven rulings answered, Step 2 resumed and committed, Step 3 executed in full, and the held
commits released.** Protocol **v1.3 → v1.4**. CD rows minted this session: **CD-085 … CD-120** (36).

### The rulings

1. **CD-085's scoping ratified, not assumed.** Census-only; phantom resolution untouched. Recorded
   in CD-089(d) so a later reader of CD-085 sees it was decided.
2. **Promoted, not patched → AGENTS.md §5.1 + CD-089.** *A gate that forbids naming the defect makes
   the defect unwriteable* is now a **gate-design rule every new gate is checked against**, and it is
   applied to `PLACEHOLDER` in both repo-wide gates. **Three sites, one rule:** SOURCE_POLICY §7.16 ·
   CD-085 · CD-089. Both retirement notes now quote the marker they retire — that is the verification.
   `tools_check.py` gained a `--selftest` it did not have (5 seeds); `canon_check --selftest` is 22.
3. **P01 scaffolded at `D-PROJ01-016` → CD-090**, option (a). Twelve attested rows recorded
   RECONSTRUCTED-UNKNOWN; **001 / 003 / 011 recorded UNATTESTED-INSIDE-RANGE**, the third state ruled
   real. No decision body invented anywhere.
4. **D-1 ruled (a) → the supersede is listed.** Executed at CD-118 and QUESTION_POLICY §9.
5. **ch3/4/5 header diff reported, nothing deleted.** ch4 and ch5 differ **only** by the §7.14.2c
   provenance block → redundant, §12.4 case 1. **ch3 does not meet the ruling's condition**: it also
   carries a corrected body byte (`surya-ocr 0.22.1` → `0.14.7`). Held.
6. **CD-091 — standing precondition.** The Math lane's next session commits evidence copies for
   `ch7`–`ch10` **before opening any chapter**. §7.14.3a already owed it.
7. Noted; folded into CD-088's session-3 build.

### Step 2 — resumed, eight checks, CLEAN, committed

`QUESTION_POLICY_v0.3_DRAFT.md` verified against source on all eight checks (five named + §5 supersede
shape + §7 promoted-source census + §9 row label). **The v0.2→v0.3 diff is exactly the seven
corrections and nothing else** — verified by diff, not by trust. Committed as
**`canon/QUESTION_POLICY.md` v1.0**, minting **CD-092 … CD-113** (22 rows: §2, the eighteen §3
conflicts in order, §4, §5, §6). Both drafts removed from `_inbox/` — moved, not copied (§12.5).

### Step 3 — six supersedes, each supersede-with-archive, pointer stubs not banners

**Pre-supersede dependent check run first (master §5.3 / D-PROJ00-061): none of REF-01, REF-09,
REF-10 or REF-25 is a `LOCKED_ProductionCore_v1` source — those are REF-02 · REF-07 · REF-08 ·
REF-18 — so no built-asset rebuild is owed.** Recorded in CD-114(e).

| # | File | Change | CD |
|---|---|---|---|
| 1 | **REF-01 → v1.3** | §1.2 only — all classes and subjects; living/append-extensible per REF-21's mechanism | CD-114 |
| 2 | **REF-10 → v1.1** | §4's বৃত্তি bullet only | CD-115 |
| 3 | **REF-09 → v1.1** | §4.1's easy ≥40% line only; **§4's totals overridden, not superseded** | CD-116 |
| 4 | **REF-25 → v1.1** | Annex A demoted; §2–§3 retained; §0's Math-MCQ claim known-false at the demotion | CD-117 |
| 5 | **MarkLogic QuestionPolicy** | §৮'s `শ্রেণি পরীক্ষা ও বড় পরীক্ষা` row, `Remember` only · §৯ → pointer + C-coded summary | CD-118 · CD-119 |
| 6 | **QUESTION_BANK_POLICY → v1.1** | §2 one Pool · §3 `tier` · §4 keys + domain ratio to paper level · §5 gate list | CD-120 |

**Every superseded LOCKED predecessor is retained on disk, unedited** — that is the §5.3 archive.
Moving it would break every citation of its path and prove nothing. Manifest rows repoint to the
successors; `canon/MANIFEST.md` gains a **Superseded-in-place** table naming each pair.
**Conventions v1.4 was NOT amended** — its own sitting.

### `_inbox/` §12.7 retention at close

**14 files, down from 16.** Both QUESTION_POLICY drafts left: v0.3 adopted into canon, v0.2 deleted
as withdrawn. Unchanged and still owed: **ch3** (held — body byte differs, not only the header,
Principal) · **ch4 · ch6** (redundant, deletable on approval) · **ch5** (held with ch3's set pending
the same ruling; header-only difference confirmed) · **ch7–ch10** (no committed evidence — now
covered by CD-091's precondition) · **4 NCTB PDFs** (staged 2026-04-28, correctly §2.1's) ·
**2 Naskh fonts** (unvendored, unconsumed) · `README.md`.

### Sync

Pushed. Range check and per-commit permission pasted in the session report.

---

## 2026-08-14 · P00/P04 unification session 3 — the gate suite (Cowork, `scd-agent-cowork`)

**The one rule that shaped this session: no bank content was authored.** The gate suite is built
independently of the bank it will judge. Every fixture is synthetic; the synthetic chapter is a
fictional **পাঠ ৯৯** that exists in no book, named that way so no later reader can mistake it for
an extraction. No file under `canon/sources/` or `canon/marklogic/` was read as fixture data
(CD-055, CD-064(f), one level up).

### Step 0 — verify at source, and one premise that did not survive it

- **Next free CD number: 121** — `canon/DECISIONS.md` defines through CD-120 and `CD-999` is a
  placeholder. *Written as a bare number on purpose: `canon_check.py`'s CD-CITE resolver caught
  the first draft of this line, which named the token, as a phantom citation — the row is not
  minted, so the citation resolved to nothing. Correct catch, and CD-085(c) is explicit that the
  backtick exemption covers the retired-number census and **not** phantom resolution.* **Next free in `workstreams/question-banks/CORRECTIONS.md`: `QB-CR-010`**
  (QB-CR-001…009 present). Neither was used — see below.
- **V-0c FAILED AT SOURCE. `workstreams/question-banks/audits/gates.py` is NOT at `_template`
  zero-gate state.** It is **795 lines, 16 named gates, 27 seeded selftests, all green, exit 0**,
  built to `QUESTION_BANK_POLICY.md` v1.0 §5 and carrying three gates promoted out of the
  corrections ledger (QB-CR-001 → POOL-MEMBERSHIP, QB-CR-003 → MARK-VALUE, QB-CR-008 →
  TOPIC-NUMBER). The `_template` file is a different, 29-line file. **Building §6's eleven on top
  of it would have deleted ten gates and un-promoted three rulings.** Reported, not done.
- **V-0d confirmed.** পাঠ ১৩ is `canon/marklogic/C5_Bangla_Source_13-23.md`, heading line 33:
  `# পাঠ ১৩ — পাখির মতো`. It is **not** under `canon/sources/c5/`, which holds পাঠ ১–১১ only.
  The traceability gate resolves against the path a bank declares, not against an assumed one.

### Housekeeping

1. **Four `_inbox/` OCR drafts deleted** after an AGENTS §9 notice stating the reason first.
   `ch6` byte-identical to its committed evidence copy (md5 `cb8e331e589bd5b77ea36a265b280b09`
   both sides). `ch4`/`ch5` differ **only** by a prepended provenance block (`diff` = `0a1,19` and
   `0a1,18`); every original byte survives in `canon/_wip/c5-math/evidence/`. `ch3` deleted on its
   own ground: its committed copy also carries `0.22.1` → `0.14.7` on line 2, and that block
   records the Principal's instruction *"ভুল বাইটগুলো প্রতিস্থাপন করা হয়েছে, দুটো পাশাপাশি রাখা
   হয়নি"* — the staged file was the last surviving carrier of the string ruled false.
   **§7.14.1's "never discarded" is satisfied by §7.14.3a's committed copy**, which is the only
   reason redundancy could be established at all. **ch7–ch10 have no committed evidence copy and
   were not touched.**
2. **The two Naskh fonts moved `_inbox/` → `_unvendored/`, and the note is committed while the
   binaries are not.** A font with no consumer is not an Assets-class file: §12.1's row reads
   *"consumed by a tool"* and `tools/MANIFEST.md`'s own header refuses fonts outright. Moving to a
   second gitignored folder would have changed nothing — `_inbox/`'s invisibility is the whole of
   §12.7's complaint — so `_unvendored/README.md` is tracked and carries the row. `.gitignore`
   gained `_unvendored/*` + `!_unvendored/README.md`.
3. **The পাঠ ১২ CD row was NOT minted, and that is the finding.** See **PENDING-P-030**: the
   session's instruction was to record a division of labour, but `SOURCE_POLICY` §7.6 / CD-050(b)
   says in as many words that the exclusion **reaches the extraction layer** and is a **named
   exception** to §3 — the position a division-of-labour row would have reversed. The
   contradicting sentence lives at `C5_BAN_Source_01.md:223` and was committed **2026-08-12**
   (`ccd38bc`), three days *after* the ruling. One question answered twice; the later text is the
   stale one. Raised, not ruled.
4. **`tools/audits/ledger_check.py` built — CD-088(d)(ii).** 10 selftest cases, 9 seeded, both
   directions, synthetic ledgers in a temp dir. **CD-088(d)(i)'s source lint was NOT built** —
   proposed only. `tools/MANIFEST.md` row added as REQUIRED (`tools/audits` is `SMOKE_EXEMPT`:
   gates evidence themselves).

### The gate suite

**`workstreams/question-banks/audits/gates.py` — ONE suite, 21 gates, two authorities (CD-123).**

The §6 eleven were first built as a separate `gates_qp6.py`, because V-0c's premise failed and
merging was a decision nobody had ruled. **The Principal ruled it: union, not replacement.** §6's
eleven are the floor; the three gates promoted out of QB-CR-001/003/008 stay enforced, because
retiring a gate promoted from a correction un-learns the incident that produced it. **One
retirement: DOMAIN-RATIO's per-pool form, replaced by §6's paper-level test** — the two cannot both
run, and the two seeded cases that proved the per-pool form were deleted with it rather than left
dead, since a seed for a retired gate is a seed that stops biting (CD-064(f)).

**11 §6 rows · 14 §5 rows · 4 shared names ⇒ 21 gates.** The four shared names — MARK-VALUE,
SOURCE-TRACE, SCRIPT-GUARD, TOPIC-NUMBER — carry one implementation per bank shape and dispatch.
**A gate whose shape a bank lacks reports `N/A` with the reason, never `PASS`** (§7.17). Both
families' selftests now drive the **merged registry**, not the lists they were built from: a
selftest still exercising the old `GATES` would go on passing after the merge broke it.
**25 seeded + 1 baseline (§5 family) · 17 seeded + 7 negatives + 6 CD-055 declaration cases + 1
baseline (§6 family). `gates_qp6.py` deleted — never committed, and its content is all here.**

### The three underdetermined rows, now ruled — and one gate that changed direction

**Q-1 · BLOOM-BAND: the §6 text was wrong, not merely ambiguous.** UD-23 — the Bloom axis governs
the pool, the domain axis governs the paper. Two axes, not two ranges on one axis, which is exactly
why "the wider at each level" had no referent above Apply. "The wider of" is dropped; the pool bands
against REF-06 §3.6's six levels and MarkLogic §৩ appears at paper level only.

**Q-2 · DIFFICULTY: the check got SMALLER, and that is the interesting part.** "Can supply" = easy
≥30% present, and nothing else. **A pool cannot fail a ceiling** — an author can decline to use hard
items, so a compliant paper stays constructible however hard-heavy the pool is. The seeded case that
proved the hard ceiling **was kept and inverted**: a 67%-hard pool must now stay *quiet*. A removed
case would have left the symmetric form free to creep back; an inverted one bites if it does.

**And the fixture was re-cut a second time, for the same reason as the first.** When the band moved
from four NAPE domains to REF-06's six levels, Analyze fell to 8.3% against a 10–20% floor. The
composition was re-cut to 6/8/6/3/1/0. **The band was not widened to admit the fixture** — that
direction is the whole discipline, and it is recorded in the fixture's docstring both times.

**This session ran in two sittings, and the seam is recorded because the second sitting found
something the first had missed.** The first sitting was interrupted before reporting; nothing had
been committed, so the repo was the only continuity (AGENTS §3). The second re-verified every
Step-0 claim independently at source — CD-050/§7.6, `C5_BAN_Source_01.md:223`, the `ch3` provenance
block, the `_wip/c5-math/evidence/` hashes, and both new scripts re-run from clean — and **found
one brief-mandated requirement not built: CD-055's self-declaration convention for part-authored
banks was absent from `gates_qp6.py` (`grep -c নির্মাণাধীন` → 0).** It is built now, verified
against `canon/DECISIONS.md` CD-055 and `SOURCE_POLICY` §7.9 rather than against the summary of
them. Four clauses, unchanged: the bank declares itself in `header.অবস্থা` with what is authored,
what is not and where to resume; it is excluded from **controls only**; the sweep **prints every
file it held out and why**, before any verdict, so a reader cannot reach a green line without
passing the exclusions; and **the marker is not a waiver** — `run()` is never told about it, all
eleven still fire, and a seeded case proves TOPIC-NUMBER still reddens a marked bank while another
proves marked and unmarked copies of one clean bank give identical output. A bare `নির্মাণাধীন`
with no resume tail is **REFUSED, not skipped**: §7.9's em-dash tail is what the exclusion is
bought with. §7.9's fifth clause — *removing the line is part of finishing* — is an instruction to
the author, not a gate; it is mechanised as `STALE-MARKER` on a **stated default printed in its own
output** and batched as **Q-4**, not ruled here.

**The sweep's first live run holds out the one bank on disk and says so:**
`C5_BAN_U21_QuestionBank_v1.json` is not built to §4's shape, so §6's eleven do not judge it —
**out of scope, not clean**, and printed as such. It is not re-judged and not touched.

The negatives are the half that matters: **DOMAIN-RATIO must stay quiet on a pool and on a single
class test**, and **REPETITION must stay quiet on a `Remember` stem lifted verbatim from a CT into
the annual** — §5's listed supersede of MarkLogic §৮'s row 2, running both directions. A gate that
fires on those is as wrong as one that never fires.

**Three rows run on stated defaults printed in their own output, batched as Q-1/Q-2/Q-3:** the
Bloom band's "wider at each level" has no common referent above Apply (REF-06 bands six Bloom
levels, MarkLogic four NAPE domains); difficulty's "can supply" has no fixed reading; and the
per-chapter spine slot-mapping **does not exist as data**, so COVERAGE falls back to §4's
header-stated target and does not invent it.

**One fixture was re-cut and the reason is recorded in the code:** the first synthetic bank sat at
9/24 `Remember` (37.5%) and the baseline went red against জ্ঞান's 35% ceiling. **The fixture was
wrong and the gate was right** — the only direction that discovery may run. Widening the band to
admit the fixture would have shaped the gate to pass its own test.

### Rulings executed (Principal, 2026-08-14 — CD-121 … CD-126)

- **CD-121** — `QUESTION_POLICY` → **v1.1**. Two §6 defects, both found by building the gates §6
  specifies: the Bloom-band row's "wider of" dropped (Q-1), and the **false `(CD-055, CD-064(f))`
  citation corrected**. The rule's home is now canon, citing **QB-D-012** as origin, and it carries
  the distinction the flat form had flattened: **seeds synthetic; controls MAY be live** (CD-051(d)).
  Recorded with it: how a **docstring** at `canon_check.py:458` (CD-080) → `tools_check.py:222`
  (`b9a9cc9`) → **canon** (`109b232`) acquired canon's authority without ever being ruled.
- **CD-122** — the three underdetermined rows read, each with its reasoning recorded against later
  "tightening".
- **CD-123** — the merge. 21 gates. পাঠ ২১ marked **`policy_status: pre-policy` in its own file**,
  so it is held out by a stated status rather than by a parser failing to recognise its shape.
- **CD-124** — **declare every lane now, renumber each lane as it closes.** All 17 ledgers declare
  `ledger-prefix` + `ledger-lane`. **No row renumbered, no citation touched.** The gate went
  **20 failures → 0**, with the four cross-lane tokens **printed as deferrals every run** — a debt
  nobody prints is indistinguishable from a fix. Two ledgers claiming one lane FAILs, and that is
  what keeps the deferral from being a loophole.
- **CD-125** — P-029 routed upstream as **`UP-003`**, never patched locally. Blocks every C5 Math
  bank; **does not block wave 1**.
- **CD-126** — the Naskh fonts are the **Arabic lane's**, parked until **CD-014**'s executed smoke
  test exists. `_unvendored/README.md` now points the next reader at CD-014 and at `islamic-studies`
  so the lane does not open by re-sourcing fonts it already has.

**PENDING-P-030 (পাঠ ১২) is held UNRULED at the Principal's direction** — he reads §7.6 and
CD-050(b) at source himself. No agent may act on it in either direction.

### Findings raised, none acted on

- **PENDING-P-029 / TOOLS-CR-002 — a fifth instance of CD-088's PATTERN, in a LOCKED-adjacent
  constant.** REF-19 carries `MATH-ADDSUB-REL` and `MATH-MULDIV-REL`; the harness's derived copy
  truncated both at the second hyphen; the LOCKED payload schema's `ref19_topic_id` pattern allows
  one hyphen only, so the two real slugs are **unrepresentable** and the only validating values
  are two that REF-19 does not contain. Both files LOCKED and supersede-only; neither edited.
- **PENDING-P-031 — `CR-001`…`CR-004` are each live in two or three ledgers.** CR-012's defect
  predates CR-012 by months. Four ledgers all mint bare `CR-###`. No renumbering performed.
- **PENDING-P-030 — the পাঠ ১২ contradiction above.**

### §12.7 retention — everything still in `_inbox/` at session close

| File / set | Why it is still there | Owner |
|---|---|---|
| `C5_MATH_OCRDRAFT_ch7.md` · `ch8.md` · `ch9.md` · `ch10.md` | **Not redundant.** অধ্যায় ৭–১০ have no committed evidence copy under `canon/_wip/c5-math/evidence/` — verified by hash comparison this session — so §7.14.3a has not yet run on them and deleting them would discard the draft, which §7.14.1 forbids. They leave when their chapters are extracted and the drafts are committed as evidence. | Principal (Math lane, extraction) |
| `Class 5 Bangla.pdf` · `Class 5 English.pdf` · `Class 5 Math.pdf` · `C5_Science.pdf` | Source scans under §12.1 row 1, governed by `SOURCE_POLICY` §2.1/§7.14 and out of §12's reach. Bangla and English step ① are CLOSED; Math is mid-chapter; Science has not begun. **Staged April 28 — third session running on this list, so §12.7's three-session rule now bites. Raised as PENDING-P-032: one line per file, an owner and a date, or out.** Not decided here — a staged source scan is the Principal's, and `_inbox/` is gitignored and per-machine. | Principal — **ruling owed** |
| `README.md` | The folder's own explanatory note. Permanent. | — |

**Cleared this session:** 4 OCR drafts (deleted, redundant), 2 font files (moved to
`_unvendored/`). `_inbox/` goes **14 files → 9**.

**Three-session rule (§12.7).** The four PDFs have now appeared on a retention list three times.
Per §12.7 they are raised to the Principal: either they carry an owner and a date, or they do not
belong in `_inbox/`.

### Standing constraints observed

No bank item or bank file authored · no live source file read as fixture data ·
`canon/_wip/c5-*` and the Math lane untouched · U14 not re-tagged (QB-CR-009 stays
RULED/execution-owed) · Conventions v1.4 not amended · no topic number minted ·
CD-088(d)(i) not built · nothing pushed.

---

## 2026-08-14 · P00/P04 unification session 4 — the ruled-but-unexecuted queue closed (Cowork, `scd-agent-cowork`)

**Opened at `cd03467`, clean tree, `origin/main` == `HEAD`.** Brief: close every ruled-but-unexecuted
item in this lane so question authoring opens owing nothing. **No bank content authored.**
`canon/_wip/c5-math/` and the Math `_inbox` drafts untouched — that lane is its own session.

### Step 0 — verified at source before anything was written

- **Next free numbers:** `canon/DECISIONS.md` defined through **CD-126** → CD-127, CD-128 minted.
  `PENDING_PRINCIPAL.md` defined through **P-032** → P-033 minted. Both confirmed absent repo-wide first.
- **`SOURCE_POLICY` §7.6 · CD-050(b) · `EXCLUDED_paath_12.md`** read and quoted verbatim in the
  session report. §7.6 and CD-050(b) place the exclusion **at the extraction layer** and name
  themselves a **named exception to §3**; `EXCLUDED_paath_12.md` closed by requiring **a new CD row
  citing CD-050** to restore পাঠ ১২. **CD-127 is that row, in that form.**
- **Queue state, corrected against the brief:** **P-029 and P-031 were already CLOSED by `cd03467`**
  (CD-125, CD-124). **P-030 and P-032 were the only two open.**

### What was ruled

- **CD-127 — পাঠ ১২, a PARTIAL REVERSAL of CD-050(b), recorded as one.** The exclusion **splits**:
  **extraction PERMITTED** on the Principal's call · **consumption STILL EXCLUDED** until a further
  ruling. **Whether it is taught is not decided.** **No extraction exists and none was produced.**
  The split is written down because *"not extracted"* used to do all the work — the moment
  extraction is permitted, an extracted পাঠ ১২ looks like পাঠ ১–১১ to every downstream reader and
  **`QUESTION_POLICY` has no field, gate or convention that would say otherwise**. It would be
  bankable not because anyone decided to bank it but because **nobody would have had to decide not
  to.** CD-050(b)'s text and §7.6's text **unedited**; forward-only pointer added.
- **CD-128 — the four NCTB PDFs RETAINED as the scan-of-record.** Owner **Principal**, **no end
  date**. §12.7 asked for an owner and a date, not removal; **the three-session rule is discharged,
  not restarted.** A retention list must still **name** them; it must no longer **raise** them.

### What was corrected

- **`CR-002`** (lane `c5-bangla`) — the two stale traces in `canon/sources/c5/bangla/C5_BAN_Source_01.md`.
  **Line 223** *"পাঠ ১২-এর নিষ্কাশন তৈরি হবে"*: under CD-127(a) it stops being wrong about
  extraction, **but it is silent on consumption, which is now the half that binds** — so it was
  **not left as it stood**; the consumption clause was written in beside it. *A sentence that has
  become true by accident is not the same as a sentence that is right.* **Line 224** *"পাঠ ১–১২"*
  → **পাঠ ১–১১**: a separate defect with a separate origin, corrected regardless. **Old wording
  quoted in place, not deleted. The transcription itself was not touched.** `source_check.py` re-run
  on the edited file: **GREEN**.
- **P-030's own reasoning corrected at CD-127(f).** Its claim *"CD-004 forbids editing the promoted
  source file"* **does not hold at source**: CD-004 covers the seven `canon/marklogic/` files and
  grandfathers `C5_Bangla_Source_13-23.md`. `CR-001` is the in-place precedent, on a sibling file in
  the same directory. Recorded rather than smoothed.

### What was built

- **`tools/audits/int_id_check.py` — CD-088(d)(i)**, the half `ledger_check.py` (d)(ii) left owed.
  **Selftest PASS: 16 cases, 15 seeded/control + 1 baseline**, synthetic throughout (CD-121(e):
  seeds synthetic, controls may be live). **Repo verdict FAIL — 2 INT-ON-ID-CAPTURE, 15 untyped
  sites reported and not judged.** Per the brief, **the findings were reported and nothing was
  rewritten**: a lint that forces same-session rewrites of six gates is how a clean tree becomes a
  risky one. Raised as **PENDING-P-033**.
- **`.gitignore`: `_inbox/` → `_inbox/*` + `!_inbox/README.md`** (CD-128(d), the CD-126 form). The
  retention reason had to be committed or the next sweep on **another device** would re-raise the
  same four PDFs a fourth time. **Staged bytes stay out; the accounting goes in.**

### Findings raised, none acted on — PENDING-P-033

- **`gates.py:1215`** — `str(int(unit))` on `U(\d+)` maps **`U09` and `U9` to one `৯`**, and that
  value selects the chapter section. **`gates.py:1207`** is the benign twin (`C([1-5])`, one digit).
- **A SIXTH instance of CD-088's PATTERN, and it is in the ID convention itself.** The corpus mints
  **both** paddings: `QP-ENG-C5-U09-Q01` (`build_question_envelopes.py:97`) against
  `QP-BAN-C1-U2-L4-Q03` (`LOCKED_QuestionPayload_Schema_v1.json:27`, `Conventions_v1_4.md:48`) and
  `QP-BAN-C1-U1-L?` (`LOCKED_REF-08:255`). **Three canon-layer artifacts, two conventions, no rule.**
  CD-088(c)'s instance-4 face — *the form never existed*. **Two of the three are LOCKED and
  supersede-only; nothing was edited.**
- **The lint's three design choices** — two tiers, the literal-scheme-prefix classifier, and the
  `# int-id-ok:` waiver — are **offered for ratification, not assumed.** **No waiver exists anywhere
  in the repo and none was added**, because writing one is ruling on the site it sits on.
- **Named omission:** `float()`, `Decimal()`, `str.zfill()` destroy the same information and are
  **not** checked. CD-088(d)(i) names `int()`; **widening the sink is a ruling, not a patch.**
- **UP-003 needed nothing.** Already filed at `cd03467` and P-029 already closed by CD-125. The
  census was re-run independently at source anyway: **121 REF-19 slugs, exactly 2 fail the LOCKED
  pattern** — `MATH-ADDSUB-REL`, `MATH-MULDIV-REL`. **`MATH-ADDSUB-REL` is not alone; the count is
  two, and UP-003 already states both.** No edit made.

### §12.7 retention — everything still in `_inbox/` at session close

| File / set | Why it is still there | Owner |
|---|---|---|
| `Class 5 Bangla.pdf` · `Class 5 English.pdf` · `Class 5 Math.pdf` · `C5_Science.pdf` | **RULED — CD-128. Retained indefinitely as the scan-of-record**: the authority any spot-check or re-extraction runs against, and the only channel that settles a disputed glyph. Math is mid-chapter and Science has not begun; and CD-127 has just given `Class 5 Bangla.pdf` a named future consumer. **Named here as §12.7 requires; no longer raised.** | **Principal — settled** |
| `C5_MATH_OCRDRAFT_ch7.md` · `ch8.md` · `ch9.md` · `ch10.md` | Unchanged from session 3. অধ্যায় ৭–১০ have **no committed evidence copy** under `canon/_wip/c5-math/evidence/`, so §7.14.3a has not run and deleting them would discard the draft (§7.14.1 forbids). They leave when their chapters are extracted and the drafts committed as evidence. **Math lane's own session — untouched here.** | Principal (Math lane) |
| `README.md` | The folder's own note — **now committed** (CD-128(d)) and carrying the retention table above. Permanent. | — |

**`_inbox/` unchanged at 9 files.** Nothing added, nothing removed.

### Standing constraints observed

No bank item or bank file authored · **পাঠ ১২ extraction NOT produced** · CD-050(b)'s text not
edited · §7.6's text not edited · `canon/_wip/c5-math/` and the Math OCR drafts untouched ·
U14 not re-tagged (QB-CR-009 stays RULED/execution-owed) · **no audit script rewritten to satisfy
the new lint** · the vendored schema not patched · no LOCKED artifact edited · no row renumbered ·
no topic number minted.
