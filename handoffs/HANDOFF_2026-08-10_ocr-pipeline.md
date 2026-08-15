# HANDOFF — OCR Pipeline + Step-① Continuation (supersedes prior handoffs' "current state" sections)
**Date:** 2026-08-10 · **Owner:** SCD (Principal) · **Chain:** HANDOFF_2026-08-09_unification → HANDOFF_2026-08-10_scd-central-migration → this file

**Purpose:** a new advisor chat, given this file, continues without re-asking anything settled. Role unchanged: Principal ↔ advisor (ONE recommendation, paste-ready rulings, files-over-memory, verify-at-source binds the advisor too — it has been corrected at source repeatedly, incl. recommending English-first against SOURCE_POLICY §4 and citing files not present in the repo).

## 1. Where the whole system stands

`scd-central` (private, github.com/enayetsyl/scd-central) LIVE through migration Steps 1–4. Production sequence **CD-045**: ① NCTB sources → ② C5 model papers/CTs → ③ C1–C4 → ④ question pools. Currently deep in step ①.

**Step ④ pilot (done, promoted):** C5 BAN পাঠ ২১ wave 1 — 57 items in `banks/`, 15 gates, TOPIC_NUMBERS.md chart seeded (CD-044, `-13` minted for বিরামচিহ্ন), P-005/006/007 closed, P-008 FLAGGED (chart completion). Wave 2 waits for step ④.

**Step ① extraction state:**
- **C5 English: COMPLETE.** U01 promoted (`canon/sources/c5/english/`); U02–20 in `canon/_wip/c5-english/`, sign-off PENDING. Gates: source_check.py + source_textcheck.py (Bengali-aware, REFUSE on empty channel). Depth rule CD-048 (sampled-per-unit where machine channel clean; full on artwork).
- **C5 Bangla: COMPLETE.** পাঠ ১–১১ in `canon/_wip/c5-bangla/`, ৭৭ sign-off rows PENDING; পাঠ ১২ excluded (standing ruling, EXCLUDED_paath_12.md); ১৩–২৩ pre-existing canon. Book is outline-text (no text layer) → full manual depth book-wide. CR-001 (প্রচণ্ড false-anomaly — high-res rule extended to word lists).
- **C5 Math: IN PROGRESS.** অধ্যায় ১ (35 rows) + অধ্যায় ২ (33 rows) complete in `canon/_wip/c5-math/`; অধ্যায় ৩ open — ছাপা ৩১–৩২ done, resume ছাপা ৩৩ (PDF 40), ৩৩–৪৮ remain. Offset +৭. Book outline-text. `tools/audits/math_arith_check.py` = the book's second channel (multiplication, distributive evaluator with Fraction-exact ÷, long-division simulator, ✗/✓ inversion CD-063/064; selftest 53; census per CD-059 names unparsed shapes).
- **C5 Science: NOT STARTED.** Handoff prompt drafted (in advisor chat history); never concurrent with Math — alternate sittings only.

**Key math-extraction rulings:** CD-061 fence rule (partial worked boxes outside fence, book layout governs, no-table→stop-and-ask) · CD-063/064 ✗/✓ marks read as data, inversion on prose-form lines, table-held blocks protected · CD-065/§7.11 rendering-choice (equally faithful → prefer checked form; false blocks excepted) · CD-066/§7.12 pure-exercise convention (150 dpi + numeral spot-crops; NOT YET USED — first use pending in অধ্যায় ৩) · CD-067/§7.13 cadence ceiling 2–3 chapters/sitting, stop-rule outranks ceiling, chapter close atomic.

## 2. The NEW thing: OCR-draft pipeline (in flight, mid-execution)

**Why:** Claude token budget. Vision-reading every page at 400 dpi ×4 tiles is the cost driver. New architecture: local OCR produces draft; agent verifies via targeted crops only.

**Ruling status:** §7.14 drafted by advisor + **four amendments proposed by the Cowork agent and ACCEPTED by Principal** (7.14.2a prose-sample trip-wire: 1 substantive disagreement → widen to 25%, 2nd → void OCR-corroboration, chapter drops to raster-full · 7.14.2b deterministic sample seed = chapter id, indices logged · 7.14.2c draft provenance in header; 3× same weak-glyph pattern → corrections-ledger PATTERN · 7.14.3a draft committed as evidence, not just staged · 7.14.4a cadence ceilings lift only after THREE consecutive gate-GREEN §7.14 chapters · 7.14.5 first use = Math অধ্যায় ৩ resume, control-set diff on already-verified pages FIRST, reported before any new page). **NOT yet recorded in the repo** — the paste (§7.14 + amendments + a verify-at-source preamble checking §-numbers and CD-066/067 meanings) is written but not yet delivered to a Cowork session.

**Local OCR setup (DONE on Principal's machine):**
- Repo clone at `C:\scd-central`. Rasters: `C:\scd-central\canon\_wip\c5-math-raster\pdf-NNN.png` (150 dpi, all 190 pages; `hi\` subfolder has 400 dpi crops).
- Python 3.13.9, venv `C:\Users\HP\ocr-env`, **surya-ocr pinned 0.14.7** (0.22 = "Surya 2" needs llama-server; downgraded deliberately). Script `C:\Users\HP\ocr_draft.py` (argparse: --rasters --out --pages --chapter --book; filename pattern `pdf-{p:03d}.png`; header marks MACHINE OUTPUT UNVERIFIED; note: header comment still says 0.22.1 — cosmetic, fix in provenance line per 7.14.2c).
- **Test run PASSED** on PDF 38–39 (~1.5 min/page CPU). Quality verdict: prose near-perfect; digits unreliable (৪→8, ৫→¢, ৭→Arabic ٩, ২8, Cyrillic ЪΟ), strips garbled, `<math>` junk — exactly the split §7.14 assumes (OCR carries prose, agent crops carry every numeral).
- **Full chapter run pending:** `python C:\Users\HP\ocr_draft.py --rasters C:\scd-central\canon\_wip\c5-math-raster --out C:\Users\HP\ocr-out --pages 38-55 --chapter 3 --book MATH` then `copy C:\Users\HP\ocr-out\C5_MATH_OCRDRAFT_ch3.md C:\scd-central\_inbox\`. Whole remaining book ≈ 4 h overnight batch if proof piece succeeds.

**Next Cowork prompt (deliver once draft staged):** verify-at-source preamble (six cross-refs: §7.14 next free, §7.3/7.5/7.11/7.12 meanings, CD-066/067) → record §7.14 + amendments as one CD row → Math অধ্যায় ৩ resume as §7.14 proof piece → control-set diff (OCR draft vs already-verified ছাপা ৩১–৩২) reported verbatim FIRST → then new pages under new pipeline → disagreement log (## চ্যানেল-অমিল) + verification census verbatim before batch-continue.

**ChatGPT question (answered):** not as extractor (unproven read-quality, env friction, never-two-agents); acceptable later as an independent second *reading channel* for sign-off triage — model agreement never signs, only prioritizes. Not implemented.

## 3. The Principal-side ledger (the system's only bottleneck — raised ~10 rounds running)

**~200+ sign-off rows owed, 0 signed:** English U02–20 (21 units) · Bangla ৭৭ rows · Math ৬৮ rows (অধ্যায় ১+২) + অধ্যায় ৩ accruing. **Promotion of all sources blocked on these; step ② blocked on promotion.**
- **Wave-1 content read** (57 promoted items — answer correctness, Bengali naturalness): oldest owed item. Advisor's pre-screen offer stands (bank JSON was uploaded in-chat once; re-upload to redeem).
- **Print-render session:** drafted prompt (advisor history) produces `C5_ENG_Sources_PRINT.pdf` + `C5_BAN_Sources_PRINT.pdf` via tools/render docx→LibreOffice path, cover instruction in Bengali, sign-off tables on first page per unit — so the **teacher** does book-matching and the Principal countersigns. One paste, ~10 min. Never run.
- Also standing: physical spot-check пре-requisite — Principal currently cannot access printed books (stated once; may have changed).

## 4. Open/parked (inherited, unchanged)
P-008 FLAGGED (topic chart completion; REF-19 Bangla-punctuation slug gap → Project-00 supersede owed) · U14 Drama/Story contested rows in TOPIC_NUMBERS.md · UP-001 harness charset · UP-002 pool field (Hub) · pdfkit-Arabic upstream · WATCH em-dash review mid-Dec 2026 · PAT renewals Aug 2027 · pick_placements workstation session · scd-hub privacy flip UNCONFIRMED · EnglishDrive fold-in not migrated (C2B06b Phase 4 status unknown) · D-038 standalone search · seed-vitality check idea (seeds proven to still bite after unrelated changes — noted, not ruled).

## 5. Working style (binding, unchanged)
Precise & concise; ONE recommendation + 1–2 line justification; copy-paste-exact rulings; files-over-memory; flag-don't-improvise; step-by-step one-command-at-a-time for local setup work (currently mid-way through exactly such a sequence — OCR steps 1–7 done, step 8 = full chapter run + staging); verify at source before citing any decision; expect the agent to verify the advisor. Session mechanics per AGENTS §5/§6/§9 (inputs via `_inbox/`, batched questions, verbatim gate output before "final", sync only on explicit approval).
