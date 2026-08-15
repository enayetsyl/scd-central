# SCD Unification Survey — working file

**Purpose:** Per-project survey feeding the grand unification plan (one repo/structure, SCD Hub
integration, agent-ready, easy project addition). Carry this file as the chat moves between
projects; one section is completed per project; the grand plan is written only after all
sections are done.

**Method per project:** read Instructions + README/TODO/DECISIONS (or equivalents) + project
knowledge; record: identity · artifacts & formats · governance model · toolchain · naming/ID
conventions · cross-project dependencies · current sync pain points · repo-readiness.

**Survey status:**

| # | Workstream | Claude Project(s) | Surveyed |
|---|---|---|---|
| 1 | Lesson plan production | P03 (+ P00/P01/P02/P05 upstream, P04/P06/P07 downstream) | ✅ P03 done (2026-08-08) — upstream/downstream projects pending |
| 2 | Question bank preparation | P04 | ⬜ |
| 3 | Scholarship question alignment | own project | ✅ done (2026-08-08) |
| 4 | NCTB Islamization + support books | **SB-Governance + SB-P Production** (self-contained re-founding; old P02/P05 are ancestors) | ✅ both done (2026-08-08) |
| 5 | Jolly Phonics → English improvement | old "SCD English Programme" project (EIA + synthetic phonics) | ◐ located via recovery archive |
| 6 | English in Action–style speaking structure | same "SCD English Programme" project (5+6 are ONE workstream) | ◐ located via recovery archive |
| 7 | Story book production | **Commercial storybook publishing venture** (current account, active) + old-account "Story Book Production" as design ancestor | ✅ done (2026-08-08) |
| 8 | Jolly Phonics–style Islamized English book | not yet found as its own project — likely future work under 5/7 | ⬜ |
| 9a | Accounting system | old "Accounting System" project — fully reconstructed in recovery archive | ✅ done (2026-08-08, via recovery pkg) |
| 9b | SCD Hub app + HR | **live repo github.com/enayetsyl/scd-hub** (continuation of old "Software" project) | ✅ done (2026-08-08) |
| 10 | Islamic Studies C1–5 structure | old "শারহুস সুন্নাহ" (transcript editing) is adjacent; structure project not found | ⬜ |
| 11 | Nursery & KG alignment | P08 (deferred) | ⬜ |
| — | English Skill-Building Drive | own Claude project + **live Git repo `EnglishDrive`** | ✅ done (surveyed live during migration, 2026-08) |
| — | Class Test Generator (all subjects, Sylhet) | own project ("class test question") | ✅ done (2026-08-08) |
| — | Old-Account Recovery Archive | "old project data recover" project | ✅ done (2026-08-08) — master map of all 28 old projects |

---

## Project 03 — Lesson Plan Production  ✅

**Identity.** Production floor of an 8-project initiative (P00–P08; P08 deferred).
Consumes the P00 reference layer (REF-01…REF-24), produces classroom teaching artifacts for
C1–C5 × BAN/ENG/MATH/SCI/BGS. Sole Principal; BUILD chats produce, REVIEW chats report-only.

**Artifacts & formats.**
- Annotated skeletons (per class × subject; element-level REF-21 scan gate, D-045)
- Chapter Plans (Layout v3.3) + Session Plans (Layout v11) — **JSON is source of record,
  MD is render output** (`render_plan.py`); Markdown-only deliverables (D-PROJ03-004)
- Production Packs (19+ locked; pre-digested per-lane asset) + Production Core v4
- Governance quartet: `PROJECT03_README.md` (v1.47) · `PROJECT03_TODO.md` (v1.46; §D is the
  authoritative Session-Plan lock register) · `PROJECT03_DECISIONS.md` (v1.27; D-001…D-044) ·
  `PROJECT03_MANIFEST_archived_files.md` (v1.33)
- Per-chat handoffs (`PROJECT03_handoff_YYYY-MM-DD_topic.md`)

**Governance model.** Phase-gated builds (STAGE 1 MD draft → external REVIEW → STAGE 2 JSON +
validate + render + byte-identical re-render → Principal lock). Forward-only versioning;
LOCKED files superseded, never edited; append-only decision log; copy-paste-exact patch blocks
because the Principal applies every edit by hand in the UI. FLAGs escalate, never self-resolve.
Band arithmetic (±40%/±1) for session-count changes; BEYOND-BAND needs a verbatim Principal
footer. D-022: no self-review-and-lock in one chat without waiver.

**Toolchain.** `validate_plan.py` (jsonschema L1 + semantic L2) + `render_plan.py` +
`LOCKED_C5_PlanSchema_v1.json`. Sandbox: `pip install jsonschema --break-system-packages`
each session; **local Windows re-run (PYTHONIOENCODING=utf-8) is the canonical gate.**
Known debt: D-038 renderer single-period fix → re-render sweep owed on locked standalones.

**Naming/ID conventions.** `C{class}_{SUBJ}_{U{nn}|U{u}_L{l}}[_S{p}]_{Type}_v{ver}` (D-037 as
amended by D-PROJ03-018; L = hierarchy only, S = period). Subject codes D-019. RC IDs
`RC-{SUBJ}-C{n}-{addr}`; Pool IDs `QP-…`/`TOP-…`. Chat titles `P03 · C{n} {SUBJ} · … [· REVIEW]`.

**Cross-project dependencies.** P00 (all REF masters; propagation flags both ways) · P01
(skeletons + TG reconciliations — §5 gates) · P02 (REF-01 curation policy) · P05 (RC content —
gates NEEDS-REPLACEMENT sessions; S01 commonly blocked) · P04 (homework pools TOP-*, owed
before teaching) · P06/P07 downstream consumers.

**Sync pain points (why unification matters here).**
1. Governance propagation is manual and collision-prone: parallel chats draft patches against
   stale file versions; multi-handoff consolidation passes (e.g. 45-handoff, 52-handoff) exist
   only to serialize collisions Git would prevent or surface automatically.
2. "Unpropagated supersede" is a standing debt class — README/TODO rows stale vs actual files.
3. DECISIONS body lagged its header (D-029…D-035 backfill); cited-but-unwritten decisions.
4. Companion-JSON provenance risk (MD exists, genuine JSON never created).
5. Per-chat sandbox resets: jsonschema reinstall, no persistent state, locks not canonical
   until a separate local re-run.
6. Uploaded-file version vs governance-row version must be manually cross-checked every chat.

**Repo-readiness: HIGH — this project is already halfway to a repo by discipline.** JSON-source
+ deterministic render + byte-identical gate = a CI pipeline in all but name. The quartet +
handoffs map directly to Git history; patch blocks become commits; collision serialization
becomes merges; the local-Windows canonical gate becomes "validator runs in the repo."
Prior exploration on record: Claude Code + cloned P03 repo + CLAUDE.md governance rules.

**Unification hooks noted for the grand plan.**
- The EnglishDrive repo pattern (CLAUDE.md session protocol · _wip/STATE.md · audits/ scripts +
  reports · SESSION_LOG.md · token-per-device · teacher guide) transfers almost verbatim;
  P03's validate/render toolchain is *stronger* than EnglishDrive's audit suite (schema-gated).
- P03's four-file governance quartet ≙ EnglishDrive's Charter/RunBook/DecisionLog — same
  pattern, different names → candidate for one uniform governance convention.
- RC/QP/TOP ID grammar already spans P03↔P04↔P05 — natural cross-repo (or cross-folder) keys.
- SCD Hub relevance: locked Session Plans / Chapter Plans are the teacher-facing payload an
  app could serve; extracts + coverage state are queryable if the repo is the source of truth.

---

## English Skill-Building Drive  ✅ (surveyed live, 2026-08)

**Identity.** C1–C5 English grammar-block production (separate from P03's five-subject lesson
plans). Own Claude project; **already migrated to a live private repo `EnglishDrive`**
(github.com/enayetsyl) with agent-driven builds in Claude Desktop Cowork.

**Artifacts.** Block masters (blocks/C1–C5) · extracts (TD/CW/HW/PT/CC) · weekly assignments +
coverage log · governance (Charter v1.5, Run Book v1.17, Decision Log PD-001→PD-032+,
Drive Plans ×5, specs) · File 2 (vocab pools + batch orders, xlsx) · binding exam papers.

**Repo infrastructure already built (the template for everything else).**
- `CLAUDE.md`: session protocol (pull-first, stop-on-conflict), WIP-to-file + STATE.md,
  phase gates, mandatory scripted audits, §H content guards, auto PD-numbering, promotion
  on explicit "done", forward-only naming
- `audits/scripts/run_all.py`: 11 programmatic gates + manifest schema; reports committed
- Per-device fine-grained PATs (revocable per laptop); teacher = zero-Git workflow
  ("start" / corrections / "done" / "save state and sync"); TEACHER_GUIDE.md (EN+BN);
  SESSION_LOG.md as the Principal's oversight feed
- Known environment quirks: Cowork sandbox can't unlink in .git/ (rename-aside workaround);
  cloud-tasks toggle must be OFF; workspace-boot stalls → full app restart

**Lesson for the grand plan.** Field-tested proof that: (a) agent+repo catches errors chat
missed (wrong answer key entry, phantom PD citation, stale coverage log); (b) governance-as-
CLAUDE.md works; (c) non-technical staff can operate it. This repo is the reference
implementation the unified structure should generalize.

---

## Scholarship Question Alignment  ✅ (surveyed 2026-08-08)

**Identity.** Aligning school exam papers (C1–C5 × 5 subjects) with the Primary Scholarship
Examination 2026 pattern (NAPE কাঠামো approved 05-07-2026, স্মারক …৩৮৭). **Governed branch:
Sylhet** — the Mohammadpur papers served only as the source/guide corpus (branch clarified
2026-08-08; earlier files carry the Mohammadpur name historically). Sole Principal.

**Work completed, in three phases.**
1. **21 templates rebuilt** (C1–C5 × BAN/ENG/MATH/SCI/BGS, v2/v3) to the NAPE 2026 structure:
   optional/choice banks abolished; marks-per-question fixed to scholarship values; new slots
   (মিলকরণ SCI/BGS, প্রশ্ন তৈরিকরণ BAN, Parts of Speech ENG); MCQ retired from English;
   oral/CA moved outside written totals.
2. **Gap analyses** for all five classes: slot-by-slot MATCHED / RECONSTRUCT / MISSING /
   RETIRE verdicts vs the school's actual papers. Method rule discovered mid-project:
   **cross-check HY + Annual papers before any MISSING verdict** (HY-only comparison
   overstated the C5 Math gap 52 → real 20).
3. **MarkLogic system (the current decision of record, 2026-08-08):** C5 = scholarship
   structure unchanged; C1–C4 derived downward — no lower-class mark exists on its own
   authority. **All papers 100 marks only; the 80-mark version is withdrawn**, superseding
   the 80-mark logic in the phase-1 templates.

**Artifacts & formats.** `MarkLogic_Rules.md` (invariants I-1…I-10, cause-codes, authority
hierarchy, symbols) + four subject spines: `MarkLogic_BAN_Spine.md`, `MarkLogic_ENG_Spine.md`,
`MarkLogic_MATH_Spine.md`, `MarkLogic_SCI_BGS_Spine.md` (SCI+BGS combined — identical NAPE
structures; both start at C3). One row = one scholarship slot × columns C1–C5. Plus the 21
class-subject templates and 5 gap-analysis files. All Markdown; plain everyday Bengali,
Arabic numerals for marks (Bengali numerals reserved for teaching templates).

**Post-survey growth (same day, 2026-08-08 pm).** The system expanded 5→7 files and entered
production:
- `MarkLogic_QuestionPolicy.md` — question-WRITING governance: domain ratios
  (জ্ঞান/অনুধাবন/প্রয়োগ/উচ্চতর) per class band, answer-length per mark value, repetition
  rules, and a **consolidation of all content restrictions into one file** (REF-20 names,
  no living-being images, no songs/performance, interest-free math contexts, শহিদ handling)
  — an organic canon-layer move that pre-figures the grand plan's `canon/` design.
- **Three-tier assessment architecture formalized:** HY 100 + Annual 100 + class tests 20–30
  marks/chapter, with the skill-question (both exams, term-scoped content) vs
  chapter-question (own term only) classification, and a yearly **syllabus-split sheet** as
  the single file that changes per year (stable/variable separation).
- `C5_Bangla_Source_13-23.md` — textbook source extraction (poems, vocabulary, exercises,
  slot→chapter cross-reference) from the scanned C5 Bangla PDF.
- **First production outputs:** complete C5 Bangla annual paper (100 marks + domain tracking
  + marking guidance), 2026 syllabus-split sheet, two 25-mark class tests (Ch 19, 20).
  Chapter 12 permanently excluded by Principal ruling (never reintroduce).
- Cross-workstream effect: the Class Test Generator's flagged gap ("no CT-scale MarkLogic
  layer") is now **substantially filled by the QuestionPolicy file** — the recovered
  time-ratio scaling rule is no longer the missing bridge.

**Governance model.** Deliberately *reader-facing*: clean v1 files with **no version history,
no DEC numbers, no change logs visible** — "readers know the current distribution and its
reason, not the history." Every non-D0 cell must carry a plain-language reason (I-9: a reader
who wasn't present must understand without asking). Cause-codes D0/D1/D3/D4/D5/D6 (D2 and D7
deliberately absent). Authority hierarchy: NAPE > NCTB syllabus/যোগ্যতা > locked Production
Packs/skeletons > school authority — plus a meta-rule that NAPE beats the school's own
invariants (the I-4 half-mark exception for ENG S10 exists for exactly this reason).
🔴/🟦/★ load markers imported from the P03 Production Pack world.

**Content rulings of record.** Poetry memorization removed C1–C3 (C4 kept as explicit
test-prep exception); antonym removed from C1; C2 extended-answer 20→15; no MCQ anywhere in
English; named grammar barred below C4 (E-2); phonics three-year ladder (initial → +final →
medial); LCM/GCD, percentage, average = C5-only, flagged as foundation-less; C4 BGS scoped to
8 of 14 chapters (Principal decision); "লেখার ভার" composite rule (I-10) for shared-weight
slots.

**Cross-project dependencies.** Reads P03/P01 assets as authority level 3 (LOCKED Production
Packs, annotated skeletons, TG reconciliations); standing rules cited by code (E-1, E-2, B-1,
SR-4, C-05, REF-20) originate in the P00/P03 world. Downstream: P04 question banks must
populate these slot shells; the English Drive's exam-format fidelity rules consume the same
binding-paper corpus. Templates feed actual paper production each term.

**Sync pain points.**
1. **Already one live staleness bug:** `MarkLogic_Rules.md` §6 says ENG and MATH spines
   "এখনো তৈরি হয়নি" while both files exist — the Rules file predates their build. Exactly the
   unpropagated-supersede class.
2. Spine files were not in project knowledge (only Rules was) — chat-produced files don't
   automatically land where future chats can read them.
3. The 80-mark withdrawal (DEC-2026-021) silently obsoletes the 80-mark halves of all 21
   phase-1 templates — no mechanism marks those files as partially superseded.
4. Branch-identity drift (Mohammadpur ⇄ Sylhet) lived only in chat memory until corrected.
5. Decision history is deliberately stripped from reader files — fine as design, but the
   internal history then has no durable home (the DEC register was removed from the visible
   Rules file). Git history would give this for free without polluting reader files.

**Repo-readiness: HIGH, and structurally simple.** Pure-Markdown corpus, no toolchain, small
file count, single clear anchor document. The reader-facing/no-history design maps perfectly
onto Git (clean files, history in commits). Natural candidates for programmatic checks in a
repo: I-1 totals = 100 per class-column, I-6 no code-less cells, I-8 gap rule, I-9 reason
present on every non-D0 — all trivially scriptable, none currently enforced by anything but
care.

**Unification hooks noted for the grand plan.**
- The MarkLogic spines are the **mark-authority layer for every paper-producing workstream**:
  P04 question banks, term-paper production, and English Drive PT/exam mirrors all need to
  cite these slots. Slot IDs (BAN-S15 etc.) should become cross-repo keys like RC/QP/TOP.
- The "reader file + hidden history" pattern = Git's native model; adopt as the uniform
  convention for teacher-facing documents everywhere.
- The invariant set (I-1…I-10) is a ready-made audit-script spec — same pattern as
  EnglishDrive's run_all.py gates. One shared `audits/` convention can serve both.
- SCD Hub: spines are small structured tables — the most directly app-servable artifact
  surveyed so far (mark schemes per class/subject as queryable data).

---

## Old-Account Recovery Archive  ✅ (surveyed 2026-08-08)

**Identity.** A recovery project holding everything salvaged from the earlier (banned) Claude
account: the ~1 GB export split into 1,505 conversation JSONs, from which three artifact sets
were reconstructed on 2026-08-01. This project is not a workstream — it is the **master map
of the old account** and the provenance layer for several current workstreams.

**Contents.**
1. **`claude/SCD_All_Project_Instructions.md`** — verbatim custom instructions of all 20
   instruction-bearing old projects (28 total; 8 had none: Word Test, Lesson Plan Framework,
   SCD HR, TODO, Book Production Planner, Mahzabin Yasmin - Workspace, Career webinar, How to
   use Claude). Any old project can be rebuilt by pasting its block.
2. **Accounting System recovery package** (3 files): reconstructed overview/architecture,
   a 39-conversation chat index (715 msgs, May–Jun 2026) grouped into 9 workstreams, and 8
   verbatim inter-session handoff docs (2025 audit, Phase 3/4/C reconciliation, Qard-IOU,
   two Apps Scripts). The original comprehensive handover file was lost; this substitutes.
3. **English Drive corpus** (~90 files: charters, run book, drive plans, blocks, vocab xlsx,
   exam papers, P01 skeletons/TG-reconciliations) — the seed corpus already migrated into
   the live `EnglishDrive` repo.

**Workstream discoveries (resolves several "locate" rows).**
- **"SCD English Programme — NCTB In-Class + Guardian-Free Homework"** = workstreams 5+6 in
  one: EIA-model scripted routines + **systematic synthetic phonics first** + engineered
  talk-time + guardian-free/device-free homework with Bangla icon-coded instructions;
  pilot Nursery+KG → one grade at a time. Locked constraints recovered verbatim.
- **"Story Book Production"** = workstream 7, with a mature governance model: BUILD-chat /
  QA-chat **role-switch dual-chat design** (independent adversarial QA), two editions
  (A: no animate beings; B: faceless figures), mahram rule, copyright "patterns not
  particulars" litmus, two Islamic touchpoints per book, Bengali swarabritta rhyme spec,
  pdftoppm-based programmatic faceless verification.
- **"Vocabulary Campign"** = the English Drive's origin project (Charter v1.0 era).
- **"SCD Sylhet Exam Question Generator"** — iron rule recovered: *"Muhammadpur question
  STRUCTURE + literal Sylhet syllabus CONTENT"* — this is the origin of the
  Mohammadpur-vs-Sylhet naming that caused the branch confusion in the scholarship project.
- **"Questions making"** — 35-minute mock tests scaled from full papers (time-ratio scaling,
  same task-types, fewer items) + 40/10 vocabulary-list selection rules.
- **"Software"** = SCD Hub planning project. **Critical find: it already ran the repo+agent
  pattern** — AGENTS.md hard rules, STATUS.md / DECISIONS.md (append-only D-# rows) /
  CHANGELOG.md, plain-English-first PRD confirmation, and per-session self-contained
  Claude Code handoff prompts with pre-flight ("verify next free D-#; live files always
  beat pasted state"). The unified structure is not being invented — it already existed
  in embryo here.
- **"AI-for-Teachers Course Studio (BD)"** and **"SMMA/growmelab"** — non-school ventures;
  out of unification scope but instructions preserved.
- **"শারহুস সুন্নাহ"** — Bangla transcript editing rules; adjacent to workstream 10 but the
  Islamic Studies C1–5 *structure* project was not found in the old account.

**Accounting System (workstream 9a) — survey via the recovery package.**
- *Architecture:* 15 Google Sheets workbooks (12 monthly daily files + Qard/IOU Central +
  Budget vs Actual + Master Dashboard) wired by IMPORTRANGE; "Solution C" row-per-student
  fee-head design; Eximus software PDFs → Excel extraction as the repeatable ingest.
- *Governance style (recovered verbatim):* micro-manage; ask-before-building; phase-by-phase;
  one file at a time; verify (recalculate) before declaring done; summary/checklist at top;
  corrections delivered as lists for the Principal to apply — Claude never edits live files.
  Islamic footing throughout (amanah framing, Qard-e-Hasana, no interest language).
- *State at capture (May–Jun 2026):* 2025 audit Checks 1–3 passed, **Check 5 open: 423,533
  cash carry-forward break**; 2026 reconciliation chased a +28,592 residual (Principal chose
  forensic elimination over a suspense entry); Feb–May cash-default Apps Script migration
  mid-flight; workstream I = "Standardization & migration to app" — the accounting system
  was already heading into SCD Hub.
- *Caveat carried from the package:* all figures reflect the archive date; verify against
  live Sheets before acting.

**Sync pain points this archive itself demonstrates.**
1. The entire archive exists because **chat-resident knowledge dies with the account** —
   the strongest possible argument for the repo-first unification.
2. The old account's working memory was **handoff documents passed between chats** — a
   manual, lossy Git (the comprehensive handover file was in fact lost).
3. Recovered assets are frozen at capture; nothing marks which figures/decisions have since
   been superseded by live work (e.g. accounting balances, Charter v1.0 → v1.5).

**Repo-readiness / unification hooks.**
- This archive should enter the unified repo as a read-only **`/archive/old-account/`**
  provenance layer — never edited, cited when history is needed.
- The Software project's AGENTS/STATUS/DECISIONS/CHANGELOG + handoff-contract pattern is a
  third independent convergence on the same governance shape (with EnglishDrive CLAUDE.md
  and P03's quartet) → strong evidence for one uniform convention.
- Accounting continuation = highest-value revival candidate: open items are concrete
  (Check 5; the 28,592 hunt), the handoffs are self-contained, and workstream I already
  points it at SCD Hub.

---

## Class Test Generator (Classes 1–5, all subjects, Sylhet)  ✅ (surveyed 2026-08-08)

**Identity.** Weekly/periodic ক্লাস টেস্ট (CT) paper production for the Sylhet branch —
Classes 1–5 across Bangla, Mathematics, Science, BGS, and Religion (the Bangla-medium
complement to the English Drive's PTs). One chapter per test, drawn only from the uploaded
NCTB chapter. Print-ready `.docx` deliverables with teacher answer keys.
**Policy transition declared 2026-08-08: format authority moves from "mirror the Mohammadpur
final papers" to the scholarship project's MarkLogic policy.** Mohammadpur reference papers
become historical; MarkLogic Rules + spines (and their eventual BAN/MATH/SCI-BGS analogues at
CT scale) become the binding structure source going forward.

**Artifacts & formats.** Per-CT docx (question paper + teacher-only answer key page marked
"ছাত্রদের জন্য মুদ্রণযোগ্য নয়"); reference final-exam papers per class/subject as formatting
anchors (to be superseded per the transition above). File naming
`[Class][CT#][Subject][Chapter]` (e.g. `C2CT1BANCH18`); subject codes BAN/ENG/MAT/SCI/BGS/REL.

**Governance model (lightweight, workflow-encoded rather than file-encoded).**
Order of operations: confirm chapter uploaded → confirm class+subject → **total marks must
come from the user, never assumed** → generate → verify rendered output → present. Single-
chapter scope rule (no cross-chapter content). Institutional content rules (e.g. specific
rhymes excluded; পায়রা/হাঁস substitutions). Iterative review-and-revise with the Principal;
mark restructures arrive as exact arithmetic ("10×0.5=5") and are followed literally.
**No decision log, no versioned governance files, no programmatic checks** — the thinnest
governance of any surveyed workstream; conventions live in project instructions + memory.

**Toolchain.** Node.js `docx` library; Nikosh font (downloaded per-session from a GitHub CDN,
fc-cache registration; Noto Sans Bengali fallback); LibreOffice PDF conversion + pdftoppm
rasterization for visual verification; pandoc for parsing reference papers; Bengali numerals;
right-aligned mark brackets via tab stops. Everything rebuilt from scratch every chat
(fonts reinstalled, scripts rewritten) — no persistence.

**Cross-project dependencies.** Consumes NCTB chapters (same books P01/P03 analyze);
**now formally downstream of the Scholarship/MarkLogic project** (structure authority);
shares the exam-paper corpus lineage with the English Drive and the old Exam Question
Generator ("Muhammadpur STRUCTURE + Sylhet CONTENT" — this project inherited that iron rule
and is now the first to formally retire it). Its PT/CT cadence parallels the English Drive's
Thursday PTs — same teachers print both.

**Sync pain points.**
1. The policy transition just declared has **no durable home** — it exists in this chat and
   in Claude's memory only. Nothing in the project's files records that Mohammadpur mirroring
   is retired; the instructions still say the opposite. (Live instance of the archive's
   lesson: chat-resident decisions die.)
2. MarkLogic currently covers scholarship-facing structure (C5 anchor + derivations); **CT-
   scale mark distribution (30-mark, 35-minute tests) has no MarkLogic layer yet** — the old
   "Questions making" project's time-ratio scaling rule (35/180 ≈ 0.19) is the missing bridge
   and lives only in the recovery archive.
3. Per-session toolchain rebuild (font download, script rewrite) wastes time every single CT
   and depends on an external CDN staying up.
4. Generated CTs accumulate nowhere queryable — no coverage log of which chapters have been
   tested per class/term (the English Drive solved this with its Coverage Log; nothing
   equivalent here).

**Repo-readiness: HIGH and low-effort.** Small, self-similar artifact set; a `templates/` +
`generator/` + `tests/C{n}/{SUBJ}/` layout with the docx script and font vendored into the
repo kills pain point 3 outright; a one-file coverage log kills 4; a `POLICY.md` recording
the MarkLogic transition kills 1. Natural audit scripts: mark-total recompute, chapter-scope
word check, answer-key completeness — same run_all.py pattern as EnglishDrive.

**Unification hooks.**
- First proven **consumer** of the MarkLogic authority layer outside the scholarship project —
  the test case for slot-IDs-as-cross-repo-keys.
- Needs a **CT-scale derivation rule** added to MarkLogic (scholarship structure × time
  ratio), reviving the recovered "Questions making" scaling logic as policy.
- The vendored-toolchain need (fonts + docx scripts) is shared with every Bangla-docx-
  producing workstream → argues for one shared `tools/` layer in the unified repo.
- SCD Hub: CT papers + answer keys + a coverage log are directly servable to teachers.

---

## Support-Book Programme — SB-Governance (+ SB-P Production)  ✅ (surveyed 2026-08-08)

**Identity.** Workstream 4 in full: internal, free **support books (সহায়িকা)** parallel to
NCTB textbooks for Classes 1–10 (rolling, one class ahead), preserving every NCF
যোগ্যতা/শিখনফল while adapting content and imagery to the school's Salafi framework.
Two-mode model: **Mode-R** (selective genre-matched replacement — C1–4, 6–7) and **Mode-C**
(curation-only exam fidelity — C5, 8, 9–10 for বৃত্তি/board). 2026 wave = C1–C5, pilot
C1 BAN → ENG → MATH; from 2027 one class/year. Deliberately **re-founded self-contained**:
prior-project analysis (old-account P01 skeletons/TG-reconciliations, P02 curation policy)
is carried in as *content only*, with no governance dependency on any earlier project.

**Structure.** Two Claude Projects: **SB-Governance** (policy home — Master Guide, REF-1/REF-2,
SCHEMA, append-only DECISIONS, supersede-only files, Principal-gated; chats here only draft
supersedes / policy analysis / decision rows) and **SB-P Production** (rotating source files,
disposable build chats, only in-build books' artifacts in knowledge). Explicit rule: lock
status is set by the Principal on upload, never self-declared.

**Artifacts & formats.**
- `support-book_C{n}-{SUBJ}.json` — **one JSON per book, the single source of truth**;
  per-পাঠ lesson objects with action flags (retain / retain-curated / replace), provenance-
  carrying text blocks (`source`/`edited`/`oral`/`source_note`), image slots with compliance
  fields (`contains_living_being`, `photocopy_safe`, stripe-note-not-in-prompt rule)
- Patch files per chat task (CONTENT/PROMPTS/etc.), wholesale-by-lesson merge; letter-
  inventory companion JSON (C1–C2 BAN) driving a mechanical taught-letter audit
- Governance set: Master Guide · REF-1 Curation Policy v1.0 LOCKED (11 C-codes, S1–S4
  severity, retain/avoid lists, anthem/flag omission ruling SB-016) · REF-2 Content Register
  (Name Bank: 220 Principal-vetted names in 5 class pools with tier provenance; recurring
  cast উমর/আনাস/খাদিজা/ফাতিমা with reference-sheet canon) · SCHEMA · README · DECISIONS.md
- Validator: **one data-driven script**, red/grey check tiers, seeded-error test required
  per pilot book; script-guard (no Arabic script/emoji in JSON strings — renderer constraint)

**⚠ Live staleness finding (recorded 2026-08-08).** The project's uploaded files are the
**pre-re-founding versions** (README v1.0, SCHEMA v1.0-draft, MG v1.0-draft, SB-series log
SB-001…SB-027, ledger-based pipeline), while the programme's decisions of record have moved
on: nine-step per-chapter loop (compliance map → Principal ruling → content → image prompt →
approval → ref → JSON → validator → merge), **ledger discarded** (absorbed into a
`reviewer_signoff` field), **D-series log D-001–D-019**, two always-rendered print editions
(print-colour + bw-photocopy), Bengali-safe renderer as a shared neutral tool, approved
seven-file set (README v2.2, DECISIONS, SCHEMA v1.2, SETUP, ASSEMBLY, REF-1, REF-2 v1.1).
The approved set exists in chat/decision space but **has not been uploaded** — the exact
unpropagated-supersede failure class, live in the governance project itself.

**Governance model.** The most formally specified of all surveyed workstreams: append-only
decision rows (reversal = new row citing old), supersede-only file changes with archived
priors, Principal as sole ruling authority, S4 = stop-and-escalate (chats never improvise
policy), শিখনফল-wins-ties decision rule, minimum-sufficient-action severity ladder, strict
product separation from the commercial storybook pipeline (shared tooling, separate roots,
absolute no-crossover).

**Toolchain.** Reuses the storybook production pipeline: programmatic white-stripe script
(`apply_strips.py` — stripe never in prompts), character reference-sheet discipline,
JSON-travels/disposable-chats, validator pattern, assembly via Claude Code, bw-photocopy
render profile checked on the school's actual machine.

**Cross-project dependencies.** NCTB PDFs (same corpus as P01/P03/CT generator); the school's
own Islam curriculum C1–8 (story-allocation coordination via REF-2 §6); the storybook
pipeline (tooling ancestor, strict separation); old-account P01/P02 as content ancestors.
The Name Bank + cast + word avoid/retain lists are a **content-substitution authority layer**
other workstreams could consume (story books, CT generator contexts, English Drive names).

**Sync pain points.**
1. The stale-files finding above — approved v2.2/v1.2 governance not yet in project knowledge.
2. Two-project README mirroring is manual ("identical copies refreshed together").
3. Memory vs files disagreement (SB-series vs D-series) shows decision-log identity itself
   drifted across the re-founding without a bridging record in the files.
4. Validator runs in-chat (MERGE chat) — same sandbox non-persistence as everywhere else.

**Repo-readiness: HIGHEST OF ALL SURVEYED.** The programme's own axioms are repo axioms:
"the filesystem is the database," one JSON per book as single source of truth, patches
merged wholesale by a deterministic rule, an executed validator script gating merges,
disposable chats. This is Git+CI described in prose. The two-Claude-Project split maps to
one repo with a protected `governance/` path; MERGE chats become commits + CI; the mirror
problem and the staleness finding both vanish.

**Unification hooks.**
- Fourth independent convergence on the same governance shape (with EnglishDrive CLAUDE.md,
  P03 quartet, Software AGENTS/STATUS/DECISIONS) — and the most schema-rigorous one; its
  JSON-book + patch + validator model is the strongest candidate template for content repos.
- REF-2 Name Bank → shared cross-workstream name/content-substitution authority.
- Support-book JSONs are structured, per-পাঠ, compliance-mapped — **directly servable by
  SCD Hub** (per-lesson viewer, compliance appendix, print-edition downloads).
- The nine-step loop's image-compliance stages (stripe script, ref sheets, photocopy check)
  are shared needs with Story Book Production → one shared image-compliance tool layer.

### SB-P Production (the production floor) — surveyed in place 2026-08-08

**State of production (C1 BAN, the pilot).** The full 54-পাঠ book is **built and merged**:
`support-book_C1-BAN.json` covering পাঠ 1–54, 418+ blocks, 145+ image slots — the programme's
first complete book. Recent surgical corrections at পাঠ 23 (D-021 weapon/combat line ruling)
and 24 (তবলা→তালা only). The nine-step loop is field-proven across all 54 chapters,
including trivial `retain` পাঠ.

**Governance files here are the NEWER set** (README v2.0, DECISIONS D-001…D-021+, SCHEMA
v1/v1.3, SETUP, ASSEMBLY, REF-1, REF-2, letter inventory + conjunct whitelist, validator v2) —
i.e. the production project is *ahead of* the governance project's uploads, inverting the
usual direction of staleness. The two projects' file sets have diverged versions of the same
canon (v2.0 here, v1.0 there, v2.2 approved in chat-space) — three states of one truth.

**Production learnings encoded (the operational layer the governance docs don't show).**
- **Validator executed, never reasoned:** v2 fixed real false-positive classes (multi-
  codepoint বর্ণ ড়/ঢ়/য় need placeholder substitution before char scanning; NCTB cloze slash
  markers). A red flag returns the chapter to Step 3 — no exceptions survived contact.
- **Per-chapter merge is non-negotiable** — keeps the on-disk book crash-recoverable and
  validation incremental; cumulative JSON delivered once per session end.
- **Word-sourcing hierarchy with honest provenance:** word map → Bangla Academy dictionary
  (baabo.jothartho.com) → model memory, always labelled.
- **Oral-block letter-audit exemption** (untaught letters quarantined in `oral: true`);
  **MOTOR sentinel** for no-শিখনফল motor lessons; **script guard** (em-dash/arrow/Arabic/
  emoji banned in JSON strings) caught pre-merge.
- **Living-being image doctrine operationalized:** objects-first substitution unless the
  being IS the pedagogical subject → programmatic stripe (never in prompts); cast boys for
  same-gender scenes; family-scene carve-out confirmed in production (ভাইবোন not C-01).
- Images generated and post-processed **outside the chat** (Gemini/ChatGPT + local software),
  filenames recorded back into slots — a manual asset pipeline.

**Open items at capture.** Byline policy ruling owed (inconsistent keep/drop across poets);
reviewer/আলিম queue (অজু spelling, সুফিয়া কামাল byline, ঈশান/ঈর্ষা override, শহিদ definition,
শহিদ মিনার removal under C-18 override, mixed-classroom fiqh D-020); audit flags পাঠ
43/44/45/46/52; C-19 mis-code on পাঠ 40 (REF-1 mapping error); 7-unit restructuring proposal
pending approval; **print pipeline spec'd but deferred** — standalone Node/Puppeteer
`build-book.js` + geometry/profiles/compose modules await Claude Code in VS Code + real
compliant images; three files awaiting freeze (cumulative JSON, validator v2, conjunct
whitelist).

**Production-floor pain points (beyond the governance section's list).**
5. Cross-project version divergence is now three-way (production v2.0 / governance v1.0
   uploads / approved v2.2 in chat-space).
6. The image pipeline is entirely out-of-band — generation, crop/upscale/strip, and filename
   bookkeeping are manual, with compliance checked by eye against the manifest.
7. Print rendering deferred to a different environment (VS Code/Claude Code) — the one step
   the chat sandbox can't do (Chrome/Puppeteer), splitting the pipeline across tools.
8. Session-end cumulative-JSON delivery is a manual re-download ritual every session.

**Additional unification hooks.**
- This is the workstream that most needs the **Cowork/repo migration next**: the deferred
  print pipeline, the freeze-pending files, and the per-chapter patch-merge cycle all become
  trivial in a repo with an agent (validator in CI, build-book.js runnable, images versioned).
- The reviewer/আলিম queue is a real second-human approval role — the unified structure needs
  a reviewer lane (like the teacher lane in EnglishDrive), not just Principal + agent.
- validator_letter_audit.py + run_all.py + validate_plan.py are three sibling validators →
  one shared audits/ convention with per-workstream gate modules.

---

## Story Book Production — Commercial Publishing Venture  ✅ (surveyed 2026-08-08)

**Identity.** The founder's **commercial** digital-first children's storybook publishing
business for Bangladeshi audiences — Bengali primary + English bilingual editions, four age
bands (2–5, 6–9, 10–13, 14+), 50–100 books at launch, PDF/streaming distribution with every
PDF built print-ready (300 DPI, bleed) for optionality. Salafi-aligned content rules (no
magic/rupkotha, no romance, no music/dance). **This is the earlier book-production line whose
pipeline the school's SB programme later adopted** — commercial and school products remain
strictly separated (shared tooling, separate roots, no crossover). The old-account
"Story Book Production" project (faceless dual-edition, BUILD/QA dual-chat) is this
venture's design ancestor.

**Portfolio at capture.** Eight-plus series in flight: S1 আদিব ও আদব (akhlaq comedy; B01–B05
through the full pipeline — anchors verified, JSONs built, image reviews done with must-fix
lists); S2 দাদুর লণ্ঠন (Sahaba frame stories, silhouette/object-only for historical figures);
S3 আমার প্রথম (ibadah firsts); S4 কে বানালো? (aqidah/wonder); S8 Goyenda Club of Lane Nine
(four-boy detective club); গুবলু বিজ্ঞান GB series (Class 4 science, chapter-book-48 format —
B01 fully built, B02 drafted awaiting two founder decisions, B03–04 awaiting trims); plus
Poti Pothik, animal-humor, and sibling-detective idea banks (20 approved concepts each).
Master plan adds The Traveler / Little Doctor NCTB-aligned concepts and a mini-book +
public-domain chhora adaptation line.

**Artifacts & formats.** Per-book `book.json` + `prompts.json` under import spec **schema
v1.2** — the spec doubles as an executable check list (app importer + pipeline validate.js):
script guard (no Arabic script/emoji/arrows anywhere), exactly-20 story pages, word-count
floors verified programmatically (30–60/page, 700–1400 total for standard-24; different
proportions for chapter-book-48), ≥6/20 object-only image slots, `anchor.verified` human-set
only, `global_style_suffix` inlining rule, cover slot mandatory. Reference sheets + refs/
folder per book; Narration Style Profiles doc (24 styles) as the generation-technique layer;
five-styles-then-founder-selects drafting workflow.

**Governance model.** Founder-gated at every consequential point: anchor/hadith protocol
(weak hadith flagged and substituted, never used; founder supplies final verified text;
Claude never sets `verified: true`); flag-don't-improvise rule; moral placement confined to
Anchor + Guardian pages; animate-figure guideline with white compliance stripe applied
programmatically (never prompted) covering only the character's body span, largest being per
frame; canon-model consistency rule (all refs + scenes from the same image model). Series
bibles/production controllers per series. No central decision log — rulings live in series
files, the import spec, and memory.

**Toolchain.** Claude Desktop (planning/authoring) + Claude Code in VS Code (implementation);
Gemini Nano Banana as canon image model (ChatGPT as documented GB-series override with
consistency risk noted); Python/Pillow stripe post-processing; Puppeteer PDF assembly
(HarfBuzz Bengali shaping); Upscayl 4X upscaling; **Storybook Workbench** — a planned
localhost Express app (`127.0.0.1:4321`, filesystem as sole database, Phase 1 scoped:
shell/runner/stages/placement-clicker; PRD written, not yet built; Claude Code to open at
the parent `Story Book\` folder with CLAUDE.md at root).

**Cross-project dependencies.** Tooling ancestor of the SB support-book programme (stripe
script, ref-sheet discipline, JSON-travels model, validator pattern — exported, then
firewalled); Narration Style Profiles shared conceptually with school writing work; market/
category research docs are venture-internal. No dependency on school governance — and must
stay that way (commercial/school separation is a standing rule on both sides).

**Sync pain points.**
1. Multi-series style-selection backlog (S2/S3/S4/S8 books drafted in five styles each,
   awaiting founder picks) — pipeline state tracked only in memory + scattered chat sessions.
2. Per-book JSONs travel through chat; `text_en` and image prompts sometimes built in
   separate sessions against the same book — cross-session consistency rests on care.
3. Image review cycles (must-fix lists like crows-rendered-as-parrots, baked-in English
   text) are manual eye-checks against prompts; corrections re-enter via override prompts.
4. The Workbench — the intended cure for all of this — is spec'd but unbuilt; until then
   the "filesystem as database" exists without its app layer.
5. No central decision log: rulings (e.g. Al-A'raf substitution for a weak hadith, MARYAM
   token preservation) are scattered across series files and memory.

**Repo-readiness: HIGH — and already half-planned.** The import spec is a validator spec;
the Workbench PRD assumes filesystem-as-database with Claude Code at the folder root —
i.e. the repo model, minus Git. Adding a private repo (separate from all school repos)
+ CLAUDE.md session protocol gives: durable pipeline state per book (replacing memory),
a real decision log, and the Workbench's data layer for free. **Must be its own repo** —
commercial IP, separate from school unification, sharing only the neutral tools layer.

**Unification hooks.**
- Fifth convergence on the governance shape — but the separation rule means it joins the
  unified *conventions*, not the unified *repo*: same CLAUDE.md pattern, same audits/
  convention, own private repository.
- The stripe script, Bengali-safe rendering, ref-sheet discipline, and Puppeteer assembly
  are the shared **neutral tools layer** already consumed by two product lines → these
  belong in a small shared tooling repo (or vendored copies with a sync note).
- Workbench PRD ≈ a local, single-user cousin of SCD Hub's content-serving role — same
  filesystem-to-UI pattern; lessons transfer even though the products never mix.

---

## SCD Hub — the live platform  ✅ (surveyed 2026-08-08 from github.com/enayetsyl/scd-hub)

**Identity.** *"Publisher + system of record + delivery + tracking"* for the school — and its
README states the unification's most important boundary in its own words: **"The curriculum
itself is authored elsewhere; SCD Hub is the publisher and system of record — it delivers and
tracks that content, it does not author it."** Direct continuation of the old-account
"Software" project (same AGENTS/STATUS/DECISIONS/CHANGELOG governance, decisions now at
D-#58+). ~90 commits, active June 2026.

**Stack.** MERN with React Native/Expo (one codebase → iOS + Android + Web); GraphQL (Yoga +
Pothos + Envelop, urql client); MongoDB Atlas; **Python import-conformance harness** for the
curriculum import contract; pdfkit + NotoSansBengali for PDF (no Chromium dependency —
Oracle Always-Free friendly); npm workspaces `/shared` `/server` `/app` + `/docs` + `/skills`.
Bangla for student/teacher-facing labels, English codes underneath; vocab verifier as a gate.

**Built and shipped (state at capture, 2026-06-11).**
- Slices 0–4 done: foundation (users/guardians/students/sections/subjects/scope-grants +
  append-only audit + JWT auth), content tree + plan view + PDF, **question bank + assembly
  (teacher-selected HW / AS / CT sets)**, trackers, and a 16-screen role-gated Expo frontend.
- **Real data live in Atlas:** 91 students (7 classes, 10 sections, 194 guardian links) and
  the 23-person staff roster — this is production, not a prototype.
- **Import contract LOCKED v1.0 + conformance harness (L1→L4)** — the gate every curriculum
  artifact passes to enter the Hub; question-bank import fans a Project-04 bank into
  per-item envelopes atomically (executed proof: real C5_ENG_U09 bank → 114/114 PASS).
- **In-app plan review/approval loop (PR-1→3):** import lands as `draft` → assigned teacher
  reviews in-app (feedback text explicitly designed to be copied back into Claude Desktop)
  → re-import supersedes the round → **Principal sign-off promotes `reviewed→gold`**. The
  Hub already implements the Principal-gate + reviewer-lane pattern the content workstreams
  use — in software.
- **Homework Tracker complete (HW-T1→T4):** Project-06's LOCKED handoff adopted verbatim and
  built — 6-stage lifecycle, 240-minute daily ceiling with immutable ক/খ/গ trim log,
  Fri/Sat cadence blocks, resubmission + Pool top-up boundaries, roll-ups/watch-lists, and a
  **de-identified question-usage feed back toward the authoring side**.
- **Routine module complete (R-1→R-5)** grounded in the live V3 routine xlsx: day-type
  calendar (Sat Quran-only), cross-grade gender-split SubjectGroups (Qaida→Hifz ladders),
  period grids incl. winter compression, conflict engine, cover/substitution with
  auto-proxy scope grants, bell schedule, class-note/daily-diary. Class-teacher coordinator
  gate + support teachers + append-only assignment history.
- **HR designed end-to-end** (`docs/hr-design.md`, D-#22–#29: qard-hasan advances, clearance-
  held settlement, biometric attendance pending device SDK) with staff records already loaded.
- **PII firewall (ADR-005) with a fail-closed test:** corpus/analytics plane can never resolve
  student identity — 7 assertions green. Executed-verification-only done gate; jest suites in
  the hundreds (289/289 at last STATUS entry).

**Sync pain points / risks.**
1. **The repo is PUBLIC.** Code being public is defensible, but `/docs` carries LOCKED school
   policy (homework PRD, thresholds, routine details) and STATUS narrates school operations.
   Same class of exposure that got EnglishDrive flipped private — recommend private.
2. STATUS notes recurring "not verified live / not committed yet" states — the gap between
   built and verified-in-production is tracked but real.
3. The import contract is LOCKED on the Hub side, but **no authoring repo currently runs the
   harness in CI** — conformance is checked at import time, not at authoring time. The
   unified repos should vendor/invoke `validate_import.py` so artifacts are born conformant.
4. Guardian portal, messaging/push, analytics, AI export — deliberately deferred pipeline.

**Unification hooks (this section resolves the plan's shape).**
- **The integration interface already exists and is LOCKED:** authoring repos → envelope JSON
  → conformance harness → Hub import (`draft`) → in-app review → Principal `gold`. The grand
  plan does not need to design repo↔app integration; it needs to point every content repo at
  this contract.
- The Hub's D-#/ADR/STATUS/AGENTS governance is the sixth convergence — and the only one
  running in software with executed gates. Its conventions (executed-verification-only,
  append-only decisions, PRD-per-module) are the mature form of what every content
  workstream does in prose.
- The de-identified question-usage feed (§8.4) is the **return path**: usage data flowing
  back to authoring repos closes the loop (which questions get used/trimmed informs P04).
- Accounting's "workstream I: migration to app" now has a concrete target (HR/payroll module
  designed; qard-hasan decision already taken on the Hub side, matching the accounting
  project's Islamic-finance framing).

---

## Pending sections (template)

For each remaining project, fill: **Identity · Artifacts & formats · Governance model ·
Toolchain · Naming/ID conventions · Cross-project dependencies · Sync pain points ·
Repo-readiness · Unification hooks.**

### Project 00 — Curriculum Foundations ⬜
### Project 01 — NCTB Stability & TG Reconciliation ⬜
### Project 02 — Islamic Curation Policy ⬜
### Project 04 — Question Banks ⬜
### Project 05 — Replacement Content ⬜
### Project 06 — Trackers & Parent Comms ⬜
### Project 07 — Teacher Training ⬜
### Project 08 — Pre-Primary (deferred) ⬜
### SCD English Programme (= Jolly Phonics/EIA workstreams 5+6) ⬜ — instructions recovered; survey current/live state if rebuilt
### Story Book Production ⬜ — instructions recovered; survey current/live state if rebuilt
### Islamic Studies C1–5 ⬜ — no old project found; likely greenfield
### SCD Hub (app repo `scd-hub`) ⬜ — survey: stack, data model, content-ingestion needs, auth, hosting; cross-check against recovered "Software" project pattern

---

*Update the status table and append each section as the chat visits each project. The grand
plan is written only when the table is green.*
