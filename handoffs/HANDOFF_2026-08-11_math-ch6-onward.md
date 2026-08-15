# HANDOFF — C5 Math অধ্যায় ৬–১০ + cadence lifted (supersedes prior handoffs' "current state")
**Date:** 2026-08-11 · **Owner:** SCD (Principal) · **Chain:** unification → scd-central-migration → ocr-pipeline → **this file**

**Purpose:** a new advisor chat, given this file, continues without re-asking anything settled. Role unchanged: Principal ↔ advisor (ONE recommendation, paste-ready rulings, files-over-memory, verify-at-source binds the advisor too — it has been corrected at source repeatedly, incl. mis-stating the cadence ceiling as "2–3" when canon says three, citing files not in the repo, and recommending English-first against SOURCE_POLICY §4). The working loop: Principal ↔ advisor chat (this role) ↔ disposable Cowork agent sessions on the repo. Advisor gives paste-ready ruling text; the agent executes gates and never self-approves; expect the agent to verify the advisor's claims too.

---

## 1. Where the whole system stands

`scd-central` (private, github.com/enayetsyl/scd-central) LIVE through migration Steps 1–4. Production sequence **CD-045**: ① NCTB sources → ② C5 model papers/CTs → ③ C1–C4 → ④ question pools. Currently deep in step ①, Math nearly done.

**Latest commits:** `81846ee` (অধ্যায় ৫ + gate Sittings 1&2, 40 files) · `b846691` (CD-078 + verified অধ্যায় ৬–১০ ranges). Nothing uncommitted.

### Step ① extraction state (C5)
- **English: COMPLETE.** U01 promoted (`canon/sources/c5/english/`); U02–20 in `canon/_wip/c5-english/`, sign-off PENDING. Gates: source_check.py + source_textcheck.py. Depth rule CD-048.
- **Bangla: COMPLETE.** পাঠ ১–১১ in `canon/_wip/c5-bangla/`, ৭৭ sign-off rows PENDING; পাঠ ১২ excluded (EXCLUDED_paath_12.md); ১৩–২৩ pre-existing canon. Full manual depth (no text layer). CR-001.
- **Math: অধ্যায় ১–৫ COMPLETE & GREEN**, all in `canon/_wip/c5-math/`, sign-off PENDING. অধ্যায় ৬–১০ NOT STARTED.
- **Science: NOT STARTED.** Book scanned, in `_inbox/C5_Science.pdf`, rasterized to `canon/_wip/c5-science-raster/` (166 pages, 150 dpi). Extraction waits until Math fully done (no concurrent source sessions). **One input owed from Principal:** pdf-006's printed folio, to compute the Science offset before its ch-1 OCR command can be issued.

### 7.14.4a cadence counter: **3** — CEILING LIFTED (CD-078)
অধ্যায় ৩, ৪, ৫ are the three consecutive gate-GREEN §7.14 chapters. Per CD-078 the §7.13 three-per-sitting ceiling is **lifted**: from অধ্যায় ৬, close **as many complete chapters per sitting as full care allows**. The CD-067 stop-rule still outranks everything — care-thin → stop at a stated resume point, mid-chapter if that's where it lands. Speed is now care-bound, not count-bound.

---

## 2. The OCR-draft pipeline (mature; this is how Math is extracted)

**Architecture:** local Surya OCR produces a per-chapter draft (Principal's machine, zero Claude tokens); the agent inverts from reader to verifier — OCR carries prose, the agent's 400 dpi spot-crops carry every numeral. Governed by SOURCE_POLICY §7.14 + §7.15 (trip-wire), recorded as CD-068/069 and refined through CD-070–077.

**Local setup (Principal's machine, DONE):**
- Repo clone `C:\scd-central`. Math rasters: `C:\scd-central\canon\_wip\c5-math-raster\pdf-NNN.png` (150 dpi, all 190 pages).
- Python venv `C:\Users\HP\ocr-env`, **surya-ocr pinned 0.14.7** (0.22 needs llama-server; downgraded deliberately). Script `C:\Users\HP\ocr_draft.py` — header born-correct at 0.14.7 (fixed in VS Code; the §7.14 comment could read §7.14–7.15 but that's cosmetic).
- **Run pattern (venv MUST be active, or `ModuleNotFoundError: surya`):**
  `ocr-env\Scripts\activate` then
  `python ocr_draft.py --rasters C:\scd-central\canon\_wip\c5-math-raster --out C:\Users\HP\ocr-out --pages <lo-hi> --chapter <N> --book MATH`
  then `copy C:\Users\HP\ocr-out\C5_MATH_OCRDRAFT_ch<N>.md C:\scd-central\_inbox\`

**⚑ OVERNIGHT BATCH — staged/pending as of this handoff.** The Principal was given the 5-command batch for অধ্যায় ৬–১০ drafts (ranges below) to run in one overnight session (~3–5 h for 91 pages), then stage all five to `_inbox/`. **First action for the new chat: confirm with the Principal whether the batch ran and the five drafts are staged.** If yes → open অধ্যায় ৬. If no → have him run it, or (his call) start ৬ raster-full without waiting (not recommended — throws away the token saving).

### অধ্যায় ৬–১০ — ranges VERIFIED at source (CD-078, offset +৭ confirmed at all five openings)
| অধ্যায় | নাম | ছাপা | PDF | pages |
|---|---|---|--:|--:|
| ৬ | শতকরা | ৯১–১০৪ | 98–111 | 14 |
| ৭ | গড় | ১০৫–১১৪ | 112–121 | 10 |
| ৮ | পরিমাপ | ১১৫–১৪৮ | 122–155 | **34** |
| ৯ | জ্যামিতি | ১৪৯–১৭০ | 156–177 | 22 |
| ১০ | উপাত্ত বিন্যস্তকরণ | ১৭১–১৮১ | 178–188 | 11 |

ছাপা ১৮২ (PDF 189) = সমাপ্ত page, not in any chapter.

**Draft spec (identical to ৩/৪/৫ so the DRAFT exemption + §7.14.3a keep applying):** surya-ocr 0.14.7 · 150 dpi · one file/chapter `evidence/OCRDRAFT_ch<N>_<date>.md` · header contains `MACHINE OUTPUT, UNVERIFIED` · each page preceded by `## PDF p<n>` · **verbatim, correct nothing** (Assamese `ৰ`/`ৱ` included — the draft's errors ARE the evidence).

**Two planning notes from the agent:**
- **অধ্যায় ৮ পরিমাপ (34 pp)** is the new longest chapter; measurement leans on unit-conversion rates the book *assumes rather than teaches* (⛔-recorded in ৫). Expect ⛔ facts + a multi-sitting chapter even with the ceiling lifted. Don't let "ceiling lifted" tempt a rush through ৮ — most likely to hit the care-thin stop.
- **অধ্যায় ৯ জ্যামিতি** may be largely non-numeric (compass constructions, not arithmetic) — `math_arith_check.py` will legitimately have little to say; the census will show it. That is coverage reported honestly, not a gap.

---

## 3. Standing per-chapter open-prompt (the loop for অধ্যায় ৬+)

Each new chapter, paste to a fresh Cowork session:
1. **Re-derive the offset first** — cross-check known folios at both ends + midpoints at 400 dpi before transcribing; report verbatim; if it moved anywhere, stop. (+৭ has held book-wide so far but is re-proven per chapter.)
2. Create `C5_MATH_Source_0<N>.md` with `নির্মাণাধীন` line + offset table + sign-off scaffold; classify & move the draft from `_inbox/` per **SOURCE_POLICY §2.1** (NOT AGENTS §5 — §5 is Gates).
3. **Pipeline:** OCR carries prose; spot-crops carry every numeral, cell order, decimal-point (point + all digits both sides + count), fraction লব/হর separately, `৪`/`৮` at **≥2000 px band-crop** (CR-006), grid counts. All gates run per page.
4. **Cadence (CD-078):** close as many complete chapters as full care allows; CD-067 stop-rule outranks — care-thin → stop at stated resume point. Report at **chapter close, not per-issue** (see §4). Atomic close = full read → SLOTS mapped (against the spine's own labels, see CR-007) → নির্মাণাধীন removed → sweep → checkpoint-commit as one unit.
5. **New gate-shape → log PENDING-P and hand-verify, do NOT build mid-chapter** (the অধ্যায় ৩ lesson). Expect few — the toolkit is complete.
6. Verbatim gate output before any "final"; **sync only on explicit Principal approval.**

---

## 4. Reduced-reporting rule (CD-078, in force from অধ্যায় ৬)

The gate suite is mature and halts on RED itself. The agent runs continuously and **STOPs-and-holds only for:** an unresolved RED (suspected real error); a §7.15 trip-wire hit; a genuinely new gate-shape needing a *ruling* (not one deferrable to a gate sitting); or CD-067 care-thin. Everything else — ⛔ উৎস-সীমা facts, draft-caught CR corrections, false signals resolved against a control — is **recorded in-file and the run continues**, reported as a list at chapter close. **⛔ facts need the Principal's EYES at close (they gate step ④), not a mid-chapter ruling.**

---

## 5. The gate suite (all seeded, all green; cite — don't rebuild)

`canon/_wip/c5-math/` is gated by, in `tools/audits/`:
- **math_arith_check.py** — multiplication, distributive, equality chains, long division (signed AND signless, structural: row-above-a-rule is subtracted — CD-072), ladder census-visible REFUSE (CD-073), `÷` exact-`Fraction` (CD-064), **decimal evaluator exact-Fraction with `_num` point-preserving (CD-075)**, `✗`/`✓` + instruction dual-signal inversion (CD-063/064 extended to worked blocks, CD-075). Never float.
- **grid_count_check.py** — shaded-cell hundredths-grid counts, two-pass location inside the grid's own width, REFUSE-never-silent (CD-076).
- **source_check.py** — RANGE/SLOTS/PAGES/SIGNOFF/DEPTH. **SLOTS now verifies each row against the spine's own label (CD-077), not mere ID presence** — discriminative match (≥1 word of its own label AND more like its own slot than any other; only the naming cell scored, prose is commentary).
- **bangla_script_check.py** — Assamese `ৰ`/`ৱ` (U+09F0/09F1) RED in authored text, DRAFT files exempted-but-counted; backtick-citation allowed, fenced text checked (CD-071/§7.16).
- **source_textcheck.py** (English/Bangla), **canon_check.py**, **tools_check.py**.

Every gate has seeded selftests that bite every run (synthetic fixtures, NOT drawn from the live file pool per CD-055/CD-064(f) — else they stop biting when the file finishes). Gate fixes are canonical + get a CD row; a gate has failed its own author ~6× this week (that IS the seeded-error doctrine paying out).

---

## 6. Key standing rulings for Math extraction (cite, don't re-derive)

- **CD-061** fence rule: partial worked boxes outside fence; no-table false-worked block → stop-and-ask.
- **CD-063/064** ✗/✓ read as data, prose-form lines inverted, table-held blocks protected.
- **CD-065/§7.11** rendering choice: equally-faithful → prefer the checked form; book-false blocks stay table-held (protection before coverage); a false block the book does NOT print as a table = stop-and-ask.
- **CD-066/§7.12** pure-exercise convention: 150 dpi furniture + 400 dpi numeral spot-crops; state `পূর্ণ (§৭.১২)`. Test is content not heading; one worked answer/mark → full treatment. **No lighter treatment may be invented below §7.12 — stop-and-ask.** (In অধ্যায় ৫, §7.12 qualified on zero pages — the book teaches by worked example; expect the same shape elsewhere.)
- **CD-067/§7.13** stop-rule outranks the (now-lifted) ceiling; chapter close atomic, never batched across chapters. "Half-closed chapters are not closed ones."
- **CD-068/069 + §7.14/7.15** the OCR pipeline itself: draft never trusted / never discarded; trip-wire counts ONLY OCR-loses-on-plain-prose-sample disagreements (CD-069 amended the direction-blind original); OCR-wins tightens scrutiny of our own reading, not the pipeline. Depth value `OCR-corroborated` costs three things (CD-070): numeral-crop evidence + a `## চ্যানেল-অমিল` log + `ক্রমসহ` on tabular rows.
- **§7.14.2c-i** cell order crop-matched, not just cell value (a correct numeral in the wrong cell is as wrong as a misread one).
- **Fraction crop rule:** লব/হর cropped separately (`লব/হর ক্রমসহ`).
- **Decimal convention (three clauses, all load-bearing, proven by 4 distinct OCR failures):** `দশমিক-বিন্দু ক্রমসহ` = the point AND every digit on both sides AND the digit count. Failures seen: digit-substituted-point-right (`১.২২৫`→`5.225`), digit-deleted (`০.৩৫`→`0.05`), script-switched (`০.১`→`0.5`), point-inserted (`৪.৮০`→`8. b.0`).
- **CR-006 `৪`/`৮` rule (book-wide):** every ৪/৮ decision at **≥2000 px band-crop**, opposing glyph alongside where possible — dpi ≠ on-screen magnification. (Third member of CR-002 "dpi doesn't save counting" / CR-003 "dpi doesn't save a single reader".)
- **CR-007/CD-077:** the MarkLogic MATH spine's 11 slots are **exam question-types, not chapter-subjects** (S01 বহুনির্বাচনি · S02 শূন্যস্থান · S03 সংক্ষিপ্ত উত্তর · S04 চার-প্রক্রিয়া · S05 লসাগু-গসাগু · S06 সাধারণ ও দশমিক ভগ্নাংশ · S07 শতকরা · S08 গড় · S09 পরিমাপ · S10 জ্যামিতি · S11 উপাত্ত). Error entered at অধ্যায় ৩ (১/২ were correct), copied into ৪/৫-draft; corrected in ৩/৪ as dated append-only `## ⚠ অপসারিত স্লট-ছক` blocks, no re-extraction. অধ্যায় ৩/৪/৫ each source **five slots at once** (S01·S02·S03·S04·S06). SLOTS gate hardened to spine-label match.
- **Draft-substitution-key reasoning:** when a draft seems to disagree, check its OWN consistent substitution (`8`=৪, `b`=৮, `9`=৭) before calling it a real disagreement — separates a true anomaly from consistent OCR garbage.
- **Two-channel design's third function:** a `কেউ নয়` / "both channels agree yet the text is wrong because the BOOK is wrong" row — only two channels can distinguish a book-error from a reader-error.

---

## 7. The Principal-side ledger (the system's real bottleneck)

~**315+ sign-off rows owed, 0 signed** (English U02–20, Bangla ৭৭, Math অধ্যায় ১–৫ incl. ৫'s 109). Promotion of all sources is blocked on these; **step ② is blocked on promotion.** Extraction speed does not touch this — it only grows the pile.
- **Delegated & in-flight (do not re-flag every turn — Principal asked the advisor to stop reminding him):** two teachers content-checking English + Bangla sources (~1 day, results still pending as of this handoff). Principal countersigns on their return; wave-1 content read (57 promoted Bangla items) folds into that pass.
- **Math has no checker assigned** — অধ্যায় ১–৫ rows (~245 Math) are the Principal's alone unless a third checker is assigned.
- Standing: a print-render session (drafted, never run) would produce `C5_*_Sources_PRINT.pdf` via tools/render docx→LibreOffice with per-unit sign-off tables, so a teacher does book-matching and the Principal countersigns — one paste, ~10 min.
- **Advisor guidance already given & accepted:** when Math finishes, the tempting move is "extract faster"; the right move is "sign what's done" — a faster pipeline feeding an unsigned queue is just a bigger queue.

---

## 8. Open / parked ledger

- **⛔ উৎস-সীমা facts (hard sourcing facts — a question bank must NOT cite these; they were never printed / are internally inconsistent):**
  - অধ্যায় ৪: নিজে করি ৩–৮ do not exist (ছাপা ৬২ jumps ১,২→৯,১০,১১); ছাপা ৫৯'s middle step `= ১+১+১/৫ = ১/৫` is a book printing error (dropped ২, next line reads ২ ১/৫) — result citable, the mis-step is not.
  - অধ্যায় ৫: **12 ⛔ facts** in that chapter's sign-off block (incl. ⛔-১ four numbers/three table rows, ⛔-৫ instruction says তিনটি but four printed, two infinite decimals, etc.). Read them at close before step ④ ever sources ৫.
- PENDING-P-018/019/020/021 all **BUILT & CLOSED** (CD-074/075/076/077). PENDING queue for Math is **empty**.
- Not-yet-migrated / other workstreams (unchanged): EnglishDrive fold-in (still its own repo; C2B06b Phase 4 + C4B06 Part-E PD status unknown to this chain), P00, question-banks step ④ wave-2, english-programme (recovered instructions in archive), islamic-studies (greenfield, ARABIC-SLOT — Hub pdfkit can't shape Arabic, upstream gap), accounting (Check-5 423,533 break; +28,592 residual).
- UP-001 harness charset · UP-002 pool field · pdfkit-Arabic upstream · WATCH em-dash review mid-Dec 2026 · PAT renewals Aug 2027 · pick_placements workstation session (tkinter, permanently UNPROVEN until a click-session) · scd-hub privacy flip UNCONFIRMED.
- P-008 topic-chart completion (REF-19 Bangla-punctuation slug gap → Project-00 supersede owed) · U14 Drama/Story contested rows in TOPIC_NUMBERS.md.

---

## 9. Session mechanics (binding, unchanged)

Inputs travel via `scd-central/_inbox/` (Principal stages, agent classifies before moving — wrong/partial drops have been caught this way). Agent batches questions per AGENTS §6; Principal rules via paste-ready text from the advisor; sync only on explicit approval; verbatim gate output before any "final". Cowork quirks per AGENTS §9 (cloud-tasks toggle OFF; sandbox can't unlink in `.git/` → rename lock aside to `.git/lock-debris/` only; a stale `index.lock` has blocked commits — remove when the sandbox allows). Bengali for teacher-facing docs, English for protocol files. **Never two agents on one workstream; no concurrent source sessions (Math before Science).**

---

## 10. Working style (binding, unchanged)

Precise & concise; ONE recommendation + 1–2 line justification; copy-paste-exact rulings; files-over-memory; flag-don't-improvise; step-by-step one-command-at-a-time for local setup; verify at source before citing any decision — and expect the agent to verify the advisor. **Do NOT re-remind the Principal about the ledger every response (explicitly requested).** Reply in Bengali when the Principal writes in Bengali or asks for it.

---

## 11. Immediate next actions (priority order)

1. **Confirm the overnight OCR batch ran** and drafts ch6–ch10 are staged in `_inbox/`. If not, run/await it (§2).
2. **Open অধ্যায় ৬ শতকরা** (14 pp, PDF 98–111) via the §3 open-prompt + §4 reduced-reporting + lifted cadence. Offset re-derive first.
3. Continue ৭ → ৮ (long, watch care) → ৯ (may be non-numeric) → ১০, closing atomically, reporting at each close, sync on approval.
4. When Math is fully extracted: (a) the sign-off/print-render push (§7) becomes the priority over any new extraction; (b) Science extraction may begin — **Principal owes pdf-006's printed folio** to compute the Science offset and issue its ch-1 OCR command.
5. Parked hygiene unchanged (§8).
