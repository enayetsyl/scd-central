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
