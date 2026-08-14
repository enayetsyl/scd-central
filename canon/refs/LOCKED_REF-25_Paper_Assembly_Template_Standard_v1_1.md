# LOCKED — REF-25 · Paper Assembly Template Standard (PAT) · v1.1

*Supersedes v1.0 (`…_v1_0.md`, archived in place and unedited). **Only Annex A's authority changed** —
demoted to historical format reference. **§2–§3 retained**; §0's Math-MCQ claim recorded as
known-false in the demotion note. Ruling: `canon/QUESTION_POLICY.md` §9, CD-117.*

**Status:** **LOCKED v1.0 — locked 2026-07-16** (Principal). Never edit in place — supersede if revised (master §5.3).
**REF number confirmed = REF-25:** REF-24 is taken (`LOCKED_REF-24_Teacher_Image_Handling_Protocol_v1_0.md`, D-PROJ00-060); REF-25 is the next free number per `PROJECT00_DECISIONS.md` v1.58. Confirm-only check remains against `PROJECT00_CROSS_PROJECT_INDEX.md` (not uploaded this batch).
**Home:** **Project 00** (Principal ruling, 2026-07-16). This is the school **exam-scheme record** that REF-09 §4.2 defers to ("the school's exam scheme overrides these defaults"). Project 04 consumes it by pointer and never restates it.
**Owner:** Principal · **Author:** Claude (drafted); Principal (four rulings 2026-07-16 + approved + locked).
**Companion decision:** D-PROJ04-014 (the four rulings + Conventions v1.3 supersede) — logged in `PROJECT04_DECISIONS.md`.

**Governs:** how a finished exam paper is assembled — per (class × subject × horizon) — from the Project 04 question bank, in the school's own (Muhammadpur-mirror) style.
**Does NOT govern:** item quality (REF-09/REF-10), Bloom mechanics (REF-17/REF-18), curation (REF-01), bank production/storage (Conventions v1.3, Project 04). This document makes papers that comply with those; it never restates them.

---

## §0 — Summary checklist (read first)

| ☐ | One template per (class × subject × horizon). The 21 uploaded 2026 Sylhet finals are the source of truth for the **ANNUAL** templates (Annex A) — **the uploaded paper is the authority for its lane's format rules** (Ruling 2). |
| --- | --- |
| ☐ | A paper is never written freehand: **pick template → state fence → blueprint → select from bank → fill ADMIN slots → render → note block → review gate** (§3). |
| ☐ | The template's **format whitelist** is applied at selection — the bank may contain formats a lane forbids (e.g., MCQ exists in the bank; **no Math paper in any class uses MCQ**) (§2.4, §6). |
| ☐ | Bloom mix and difficulty are enforced **at assembly** (REF-17 §5.2 band; REF-09 §3: easy ≥ 30%, hard ≤ 25%) — objective slots are filled by deliberately selecting from the bank's Remember/Understand band (§3 step 4). |
| ☐ | **Legacy formats live in the bank** (Ruling 4): `matching`, `true_false`, `fill_blank` are schema-native `question_type`s; rearrange/rhyming items are `short_answer` with the format in the stem. No authoring at point of use. |
| ☐ | **ADMIN slots** (শ্রুতলিপি, পঠন, হাতের লেখা, spelling tests) come from the template, never the bank (§2.5). |
| ☐ | **No বিসমিল্লাহ header line on any paper** (Ruling 3). |
| ☐ | Every fence chapter gets ≥ 1 item, or the drop is written into the paper's flag section; 🟦 never-skip topics are never the silent drop. |
| ☐ | The teacher-note block (key, rubric compilation, coverage tick-list, curation trace, flags) is written **in the same sitting** as the paper — a paper without it is unfinished. |

---

## §1 — Why this exists

The bank (Conventions §1) supplies compliant raw items — Bloom-tagged, difficulty-tagged, keyed, curation-clean — but deliberately sets no paper structure, no mark slots, no format prohibitions. The school's paper style is defined by exactly those three things (the Muhammadpur iron rule). Without a written template, every assembler re-derives structure from an old paper and the style drifts. With the PAT, assembly is mechanical and auditable, and REF-09 §4.2's pending "reconcile against the exam scheme" dependency is closed — this document is that scheme.

## §2 — The template: fields

**2.1 Identity.** `PAT-{CLASS}-{SUBJECT}-{HORIZON}-v{ver}`. Horizon ∈ {ANNUAL, HALFYEARLY, CHAPTERTEST, MOCK}. Structure authority named per lane (Annex A).

**2.2 Header block.** School name, branch, exam title, class/subject, **time**, **full marks** — verbatim per lane. **No বিসমিল্লাহ line anywhere** (Ruling 3, removes it from the one lane — C2 Math — whose 2026 paper carried it).

**2.3 Section table.** One row per slot: Slot № · Format (Bangla name) · Bank `question_type` → Bloom band to draw from · item count · choice rule ("any n of m" or all) · marks/item · slot total. Column totals must equal full marks.

**2.4 Format whitelist / prohibitions.** **Ruling 2: each lane's rules = exactly what its uploaded 2026 final shows** — the paper itself is the authority, not commentary in other papers' notes. Consolidated set in §6; per-lane specifics in Annex A.

**2.5 ADMIN slots.** শ্রুতলিপি/dictation (with word-count and in-fence source rule), পঠন test, হাতের লেখা — listed with mark values so totals reconcile; flagged `ADMIN`; never sourced from the bank.

**2.6 Assembly targets.** The class's REF-17 §5.2 Bloom band and the REF-09 §3 difficulty split (default 40/40/20; easy ≥ 30%, hard ≤ 25%; variance = one logged line), expressed as **marks**, not counts.

**2.7 Fence hook.** The template never fixes the syllabus. At assembly the fence (chapter/lesson list) is supplied per sitting and selection filters the bank by the fence's `TOP-…` tags.

## §3 — Assembly procedure (stepwise)

1. **Pick the template** for the (class × subject × horizon). None exists → stop; create/approve one first. Never assemble freehand.
2. **State the fence** and pull its topic tags from REF-19 / the skeleton.
3. **Blueprint before writing** (REF-17 §7.1): fill the section table with planned cells — each cell = topic tag + Bloom level + difficulty. Check four totals: marks per slot; Bloom columns vs the band; difficulty vs the §2.6 split; **every fence chapter ≥ 1 item** (or a written drop + reason in the flag section; 🟦 topics never dropped).
4. **Select from the bank** (school software, `topic_tag` filter): for each cell filter by topic + `question_type` + Bloom + difficulty. Objective slots draw deliberately from the Remember/Understand band — the bank's Application-lean default never decides.
5. **Apply the whitelist** (§2.4 / Annex A). Legacy formats are selected like any item (Ruling 4): মিলকরণ = `matching`, সত্য-মিথ্যা = `true_false`, শূন্যস্থান = `fill_blank`; এলোমেলো-সাজানো / rhyming = `short_answer` with the format in the stem. If a needed item doesn't exist, it is **authored into the bank** (full Conventions compliance: QID, tags, key, curation) and then selected — never written loose on the paper.
6. **Fill the ADMIN slots** from the template's rule.
7. **Render** in the template's header/section order: Bangla numerals, bold stems, bracketed marks, imperative voice (English subject in English).
8. **Write the teacher-note block in the same sitting**: compile keys/rubrics from the items; coverage tick-list; curation trace; flags. No note block = unfinished paper.
9. **Review gate** (REF-09 §9; REF-10 §6 for stretch items) before print.

## §4 — Worked reading of a template

See Annex A, lane 11 (`PAT-C3-BGS-ANNUAL-v1`) — read one slot as: "Slot ৫, বর্ণনামূলক: select ৪ `descriptive` items on fence topics at Apply/Analyze+, free-thinking framing, ১০ marks each; the student answers any ৩ (৩০ marks)."

## §5 — Catalogue

The 21 ANNUAL templates are **Annex A** of this document (locked with it). HALFYEARLY templates are created when the next HY structure authority is confirmed; CHAPTERTEST/MOCK templates derive per REF-09 §4.1 and the lane's ANNUAL shape.

## §6 — Consolidated format rules (Ruling 2 — from the papers themselves)

- **Math (all classes C1–C5): no MCQ, no মিলকরণ, no সত্য-মিথ্যা, no oral.** Composite multi-part word problems are the C4–C5 house style; নামতা slots appear C1–C3.
- **Science (C3–C5): MCQ in every class**; a শব্দকোষ/word-meaning "n of n+1" choice slot is house style (C3: ৩ of ৪; C4: ২ of ৪); C5 uses the three-division HY-2026 pattern **including উদ্দীপক (stimulus) items** — the stimulus is authored as a `StimulusPayload` and shared by its dependent items.
- **BGS: MCQ in C3 only** (C4/C5 papers carry none); সত্য-মিথ্যা appears C4–C5; মিলকরণ C3–C4.
- **Bangla:** শ্রুতলিপি (+ পঠন in C1–C3) always present as ADMIN; মিলকরণ C2 only; **C3 Bangla carries a ৫-mark সঠিক-উত্তর (MCQ) slot** (paper authority); অনুচ্ছেদ/রচনা/আবেদনপত্র always free-thinking, no model answers.
- **English: no MCQ except C4** (its passage MCQ slot); dictation/spelling always ADMIN; the C1–C3 grammar-cloze blocks are retained as school style even where above TG — carried with the Principal's logged ruling on each template.
- **All subjects:** Bangla script + numerals (English subject excepted); bold stems; marks in brackets; imperative instructions; no model answers on the student copy; teacher-note block mandatory; no বিসমিল্লাহ header (Ruling 3).

## §7 — Version log, rulings & propagation

- v0.1 (2026-07-16, DRAFT): drafted from the 21 uploaded 2026 Sylhet finals + Conventions v1.2 + REF-09.
- v0.2 (2026-07-16, DRAFT): the four Principal rulings — (1) home = Project 00; (2) uploaded papers = format authority; (3) বিসমিল্লাহ removed everywhere; (4) legacy formats added to the bank (schema already sufficient).
- **LOCKED v1.0 (2026-07-16):** rulings integrated; Annex A (21 ANNUAL lane templates) added; locked by the Principal.

**Propagation (executed at this lock — see the 2026-07-16 handoff for paste-ready lines):**
| Touchpoint | Change | Project |
|---|---|---|
| This file | file in Project 00; confirm REF-25 against the register; add register row | 00 |
| Conventions | **v1.2 → v1.3 supersede** (§5.3 type wording = full schema enum; PAT pointer; §8 assembly line) | 04 |
| REF-09 §4 / version log | close the "reconcile against the exam scheme" dependency — the PAT is that scheme | 00 |
| `PROJECT04_DECISIONS.md` | log **D-PROJ04-014** (four rulings + v1.3 supersede) — next free ID after -013 | 04 |
| `PROJECT04_MANIFEST_archived_files.md` | row 3: conventions v1.2 → `/archive/` | 04 |
| Payload schema | **no change** (enum already carries the needed types) | — |

---

# Annex A — DEMOTED to historical format reference (v1.1)

> **SUPERSEDED at v1.1 — pointer stub.** Annex A's **lane and format authority is retired.**
> Paper structure is now governed by **`canon/marklogic/` — MarkLogic Rules + the five spines**,
> which reproduce **NAPE 2026**. Annex A reproduces the school's **2026 Sylhet finals**, a different
> paper world; the 21 templates below are retained as a **historical format reference** — accurate
> about what those papers were, no longer authoritative about what a paper must be.
> Ruling: `canon/QUESTION_POLICY.md` §3.1 / §9, **CD-117**.
>
> **§2 (template fields) and §3 (assembly procedure) are RETAINED and unchanged.** The assembly
> *mechanism* is this document's lasting contribution; only the lane/format authority moved. Read
> §2–§3 for how to assemble a paper, and the spines for what that paper must contain.
>
> ### Known-false statement recorded at demotion (§0)
>
> **§0's checklist asserts, verbatim:** *"the bank may contain formats a lane forbids (e.g., MCQ
> exists in the bank; **no Math paper in any class uses MCQ**)"*. **That is false.** Verified at
> source against `canon/marklogic/MarkLogic_MATH_Spine.md`: slot **`MATH-S01` IS বহুনির্বাচনি**,
> carrying **10 marks at C2–C5 and 6 at C1** (`১০টি প্রশ্ন, ৪টি করে বিকল্প · 1×10 = 10`).
> **v1.0 is LOCKED and its §0 is not edited** — the correction lives here, at the demotion, which is
> where a reader of Annex A will meet it. Recorded at `canon/refs/MANIFEST.md` note 4 since the
> unification import; ruled at **CD-094**.
>
> *The 21 lane templates follow, unedited, as historical reference.*

# Annex A — The 21 ANNUAL lane templates (historical format reference; locked with v1.0)

Common to all lanes: পূর্ণমান **৮০** · fence supplied per sitting (§2.7) · assembly targets per §2.6 · teacher-note block mandatory · no বিসমিল্লাহ header · **FT** = free-thinking framing, no model answer (rubric only). Bank types: `mcq / short_answer / true_false / fill_blank / matching / descriptive`; **(f)** = format stated in the stem.

## A-1 · PAT-C1-BAN-ANNUAL-v1 — Authority: MP Annual 2025 · ২ ঘণ্টা
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | শব্দার্থ | short_answer → Rem | ৫ | all | ১ | ৫ |
| ২ | বাক্য তৈরি | short_answer → Und/App | ৫ | all | ২ | ১০ |
| ৩ | বাংলা ১২ মাসের নাম | short_answer → Rem | ১২ | all | ১ | ১২ |
| ৪ | বন্যপ্রাণীর নাম | short_answer → Rem | ৪ | all | ১ | ৪ |
| ৫ | গৃহপালিত প্রাণীর নাম | short_answer → Rem | ৪ | all | ১ | ৪ |
| ৬ | বিপরীত শব্দ | short_answer → Rem | ৫ | all | ০.৫ | ২.৫ |
| ৭ | যুক্তবর্ণ ভেঙে শব্দ | short_answer → Und | ৫ | all | ১ | ৫ |
| ৮ | কার-চিহ্ন দিয়ে শব্দ | short_answer → Und | ৫ | all | ১ | ৫ |
| ৯ | সত্য/মিথ্যা | true_false → Rem/Und | ৫ | all | ০.৫ | ২.৫ |
| ১০ | খালি ঘর পূরণ | fill_blank → Rem | ৪ | all | ১ | ৪ |
| ১১ | এক কথায় উত্তর | short_answer → Rem | ৫ | all | ১ | ৫ |
| ১২ | পূর্ণ বাক্যে উত্তর | short_answer → Und (FT-lean) | ৩ | all | ২ | ৬ |
| ১৩ | অনুচ্ছেদ | descriptive → App+ **FT** | ১ | all | ১০ | ১০ |
| ১৪ | শ্রুতিলিপি ও পঠন | **ADMIN** (৩+২) | — | — | — | ৫ |
Whitelist: no MCQ, no মিলকরণ. Fractional marks (০.৫/২.৫) are house style.

## A-2 · PAT-C1-ENG-ANNUAL-v1 — Authority: MP Annual 2025 · 2 hours
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| 1 | Paragraph ("My Family" type) | descriptive → App **FT** | 1 | all | 10 | 10 |
| 2 | Bengali meanings | short_answer → Rem | 10 | all | 1 | 10 |
| 3 | Rewrite using pronouns | short_answer → Und | 5 | all | 1 | 5 |
| 4 | Choose the correct adjective | fill_blank → Rem | 5 | all | 1 | 5 |
| 5 | am / is / are | fill_blank → Rem | 7 | all | 1 | 7 |
| 6 | This / That / These / Those | fill_blank → Rem/Und | 5 | all | 1 | 5 |
| 7 | in / on / under | fill_blank → Rem/Und | 10 | all | 1 | 10 |
| 8 | and / but | fill_blank → Und | 7 | all | 1 | 7 |
| 9 | Punctuation & capitals rewrite | short_answer → Und | 5 | all | 1 | 5 |
| 10 | Rearrange words | short_answer (f) → Und | 5 | all | 1 | 5 |
| 11 | Answer the questions | short_answer → Rem/Und | 3 | all | 2 | 6 |
| 12 | Spelling test | **ADMIN** | 5 words | — | 1 | 5 |
Whitelist: no MCQ/matching/TF. **Standing note:** this lane's item scope sits above the C1 TG (2026 coverage report); per Ruling 2 the template records the paper as-is — the separate teach-above-the-book policy question stays open in Project 00.

## A-3 · PAT-C1-MATH-ANNUAL-v1 — Authority: **MP HY 2026 shape** (Principal-directed for the Final) · ২ ঘণ্টা ৩০ মিনিট
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | অংকে লেখ | short_answer → Rem | ৫ | all | ১ | ৫ |
| ২ | কথায় লেখ | short_answer → Rem | ৫ | all | ১ | ৫ |
| ৩ | স্থানীয় মান (দশক/একক) | short_answer → Und | ৫ | all | ১ | ৫ |
| ৪ | খালিঘর পূরণ (এক ঘর বাদ) | fill_blank → Rem | ৫ | all | ১ | ৫ |
| ৫ | প্যাটার্ন | fill_blank → Und | ৫ | all | ১ | ৫ |
| ৬ | ছোট থেকে বড় সাজাও | short_answer → Und | ১ সেট | all | ৫ | ৫ |
| ৭ | বড় থেকে ছোট সাজাও | short_answer → Und | ১ সেট | all | ৫ | ৫ |
| ৮ | জোড়/বিজোড় নির্ণয় | short_answer → Und | ১৫ | all | ১ | ১৫ |
| ৯ | যোগ (হাতে না রেখে) | short_answer → App | ৫ | all | ১ | ৫ |
| ১০ | বিয়োগ (না ভেঙে) | short_answer → App | ৫ | all | ১ | ৫ |
| ১১ | নামতা (এক ঘর) | short_answer → Rem | ১০ | all | ১ | ১০ |
| ১২ | শব্দসমস্যা সমাধান | structured → App | ২ | all | ৫ | ১০ |
Whitelist: no MCQ/matching/TF. Slots ৮ & ১১ are the **Principal-widened C2-scope slots** — retained on this template by ruling; teaching-before-testing must be verified each sitting.

## A-4 · PAT-C2-BAN-ANNUAL-v1 — Authority: MP Final 2025 · ২ ঘণ্টা
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | শব্দার্থ | short_answer → Rem | ১০ | all | ১ | ১০ |
| ২ | যুক্তবর্ণ ভেঙে বাক্য | short_answer → Und | ৫ | all | ১ | ৫ |
| ৩ | শূন্যস্থান পূরণ | fill_blank → Rem | ৬ | all | ১ | ৬ |
| ৪ | বিপরীত শব্দ | short_answer → Rem | ৭ | any ৬ | ১ | ৬ |
| ৫ | বড় প্রশ্ন | short_answer → Und | ৬ | any ৫ | ২ | ১০ |
| ৬ | এলোমেলো শব্দ সাজানো | short_answer (f) → Und | ৫ | all | ১ | ৫ |
| ৭ | মিলকরণ | matching → Rem/Und | ৫ | all | ১ | ৫ |
| ৮ | ছোট প্রশ্ন | short_answer → Rem | ৫ | all | ১ | ৫ |
| ৯ | ছবি দেখে ৫টি বাক্য | descriptive → App **FT** (image per C-05) | ১ | all | ৫ | ৫ |
| ১০ | অনুচ্ছেদ | descriptive → App+ **FT** | ২ | any ১ | ১০ | ১০ |
| ১১ | হাতের লেখা | **ADMIN** | — | — | — | ৩ |
| ১২ | শ্রুতলিপি ও পঠন | **ADMIN** | — | — | — | ১০ |

## A-5 · PAT-C2-ENG-ANNUAL-v1 — Authority: MP Final 2025 · 2 hours (one seen passage drives 1–4)
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| 1 | Bengali meanings (passage words) | short_answer → Rem | 3 | all | 1 | 3 |
| 2 | Fill in the blanks (passage) | fill_blank → Rem | 3 | all | 1 | 3 |
| 3 | True/False (passage) | true_false → Rem/Und | 3 | all | 1 | 3 |
| 4 | Answer the questions (passage) | short_answer → Und | 3 | all | 2 | 6 |
| 5 | Paragraph | descriptive → App **FT** | 1 | all | 10 | 10 |
| 6 | General-knowledge questions (taught facts) | short_answer → Rem | 4 | all | 3+2+1+4 | 10 |
| 7 | Pronoun cloze | fill_blank → Und | 10 | all | ০.৫ | 5 |
| 8 | Punctuation rewrite | short_answer → Und | 5 | all | 1 | 5 |
| 9 | Prepositions | fill_blank → Rem/Und | 5 | all | 1 | 5 |
| 10 | Join with and/but | short_answer → Und | 5 | all | 1 | 5 |
| 11 | Match columns → sentences | matching → Und | 5 | all | 1 | 5 |
| 12 | have / has | fill_blank → Rem | 5 | all | 1 | 5 |
| 13 | Opposites | short_answer → Rem | 5 | all | 1 | 5 |
| 14 | Spelling & Dictation | **ADMIN** (10 in-fence words) | — | — | 1 | 10 |

## A-6 · PAT-C2-MATH-ANNUAL-v1 — Authority: MP Annual 2025 · ২ ঘণ্টা · **no বিসমিল্লাহ header (Ruling 3)**
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | নামতা (এক ঘর) | short_answer → Rem | ১০ ধাপ | all | ০.৫ | ৫ |
| ২ | উপাত্ত-ছক পড়ে উত্তর | short_answer → Und | ৩ | all | ২ | ৬ |
| ৩ | টাকার হিসাব | short_answer → App | ৩ | all | ২ | ৬ |
| ৪ | গুণ করে রাশিসহ শূন্যস্থান (সময়-রূপান্তর) | fill_blank → App | ৩ | all | ৩ | ৯ |
| ৫ | গুণ (নামতা-ঘর) | short_answer → Rem | ৫ | all | ১ | ৫ |
| ৬ | গুণ (২ অঙ্ক × ১ অঙ্ক) | short_answer → App | ৫ | all | ২ | ১০ |
| ৭ | জ্যামিতিক আকৃতি (চিনি ও আঁকি) | structured → Und/App | ২ | all | ২ | ৪ |
| ৮ | শব্দসমস্যা সমাধান | structured → App | ৪ | all | ৫ | ২০ |
| ৯ | শূন্যস্থান পূরণ (পরিমাপ/মুদ্রা/সময়) | fill_blank → Rem | ১০ | all | ১ | ১০ |
| ১০ | ঘড়ির চিত্র আঁকা | structured → App | ১ | all | ৫ | ৫ |
Whitelist: no MCQ/matching/TF/oral.

## A-7 · PAT-C3-BAN-ANNUAL-v1 — Authority: MP Annual 2025 · ২ ঘণ্টা ৩০ মিনিট
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | শব্দার্থ | short_answer → Rem | ১০ | any ৭ | ১ | ৭ |
| ২ | যুক্তবর্ণ ভেঙে বর্ণ + বাক্য | short_answer → Und | ৭ | any ৫ | ১ | ৫ |
| ৩ | শূন্যস্থান পূরণ | fill_blank → Rem | ৫ | all | ১ | ৫ |
| ৪ | বিরামচিহ্ন বসিয়ে লেখা | short_answer → Und | ১ অনুচ্ছেদ | all | ৫ | ৫ |
| ৫ | সমার্থক শব্দ (২টি করে) | short_answer → Rem | ৫ | all | ১ | ৫ |
| ৬ | এক বাক্যে উত্তর | short_answer → Rem/Und | ৮ | all | ১ | ৮ |
| ৭ | সঠিক উত্তর (MCQ) | **mcq** → Rem/Und | ৫ | all | ১ | ৫ |
| ৮ | সংক্ষিপ্ত প্রশ্ন | short_answer → Und | ৭ | any ৫ | ২ | ১০ |
| ৯ | রচনামূলক প্রশ্ন | descriptive → App+ **FT** | ৪ | any ২ | ৫ | ১০ |
| ১০ | অনুচ্ছেদ | descriptive → App+ **FT** | ২ | any ১ | ১০ | ১০ |
| ১১ | শ্রুতলিপি ও রিডিং টেস্ট | **ADMIN** (৫+৫) | — | — | — | ১০ |
Note (Ruling 2): the ৫-mark MCQ slot is **C3-Bangla house style** — the only Bangla lane with MCQ.

## A-8 · PAT-C3-MATH-ANNUAL-v1 — Authority: MP Annual 2025 · ২ ঘণ্টা ৩০ মিনিট
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | সংক্ষিপ্ত প্রশ্ন | short_answer → Rem/Und | ২০ | all | ১ | ২০ |
| ২ | যোগ-বিয়োগ-ভাগ (ভগ্নাংশ/টাকা) | short_answer → App | ৫ | all | ২ | ১০ |
| ৩ | সমাধান (শব্দসমস্যা) | structured → App | ৩ | all | ৫ | ১৫ |
| ৪ | সৃজনশীল (কম্পোজিট) | structured/descriptive → App/Ana **FT** | ২ | all | ১০ | ২০ |
| ৫ | নামতা (৭–১৫ ঘর, মিশ্র) | short_answer → Rem | ১০ | all | ১ | ১০ |
| ৬ | জ্যামিতি (চিত্রসহ সংজ্ঞা) | structured → Und | ২ | all | ২.৫ | ৫ |
Whitelist: **no MCQ** (Ruling 2 — the paper is the authority) · no matching/TF/oral.

## A-9 · PAT-C3-SCI-ANNUAL-v1 — Authority: MP Annual 2025 · ২ ঘণ্টা ৩০ মিনিট
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | বর্ণনামূলক | descriptive → App+ **FT** | ৭ | any ৫ | ৬ | ৩০ |
| ২ | সংক্ষিপ্ত প্রশ্ন | short_answer → Und | ৭ | all | ২ | ১৪ |
| ৩ | MCQ | mcq → Rem/Und | ১০ | all | ১ | ১০ |
| ৪ | শূন্যস্থান পূরণ | fill_blank → Rem | ৫ | all | ১ | ৫ |
| ৫ | মিলকরণ (মিল করে বাক্য) | matching → Und | ৫ | all | ১ | ৫ |
| ৬ | এক বাক্যে উত্তর | short_answer → Rem | ১০ | all | ১ | ১০ |
| ৭ | শব্দকোষ (অর্থ/সংজ্ঞা) | short_answer → Rem | ৪ | any ৩ | ২ | ৬ |

## A-10 · PAT-C3-ENG-ANNUAL-v1 — Authority: MP Final 2025 · 2h 30m (one seen passage drives 1–2)
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| 1 | Passage questions | short_answer → Und | 5 | all | 1 | 5 |
| 2 | True/False + correction | true_false → Und | 5 | all | 1 | 5 |
| 3 | Pronoun cloze | fill_blank → Und | 5 | all | 1 | 5 |
| 4 | Right form of verbs | fill_blank → App | 5 | all | 1 | 5 |
| 5 | Prepositions | fill_blank → Rem/Und | 10 | all | 1 | 10 |
| 6 | Conjunctions (box) | fill_blank → Und | 5 | all | 1 | 5 |
| 7 | Adverbs (box) | fill_blank → Und | 5 | all | 1 | 5 |
| 8 | Identify adjectives | short_answer → Und | 5 | all | 1 | 5 |
| 9 | Punctuation & capitalization | short_answer → Und | 5 | all | 1 | 5 |
| 10 | Dialogue (guided, Islamic greetings) | descriptive → App **FT** | 1 | all | 10 | 10 |
| 11 | Paragraph (clue words) | descriptive → App **FT** | 1 | all | 10 | 10 |
| 12 | Spelling & Dictation | **ADMIN** (10 in-fence words) | — | — | 1 | 10 |
Standing note: slots 5–8 are school-style grammar clozes above the named C3 TG — retained by ruling; logged on the template.

## A-11 · PAT-C3-BGS-ANNUAL-v1 — Authority: MP Annual 2025 · ২ ঘণ্টা ৩০ মিনিট
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | এক বাক্যে উত্তর | short_answer → Rem/Und | ১০ | all | ১ | ১০ |
| ২ | শূন্যস্থান পূরণ | fill_blank → Rem | ১০ | all | ১ | ১০ |
| ৩ | সংক্ষিপ্ত প্রশ্ন | short_answer/structured → Und/App | ৪ | any ৩ | ৫ | ১৫ |
| ৪ | মিলকরণ | matching → Rem/Und | ৫ | all | ১ | ৫ |
| ৫ | বর্ণনামূলক | descriptive → App/Ana+ **FT** | ৪ | any ৩ | ১০ | ৩০ |
| ৬ | MCQ (সঠিক উত্তর) | mcq → Rem/Und | ১০ | all | ১ | ১০ |

## A-12 · PAT-C4-BAN-ANNUAL-v1 — Authority: MP Annual 2025 · ৩ ঘণ্টা
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | শব্দার্থ | short_answer → Rem | ১০ | all | ১ | ১০ |
| ২ | বিপরীত শব্দ | short_answer → Rem | ৫ | all | ১ | ৫ |
| ৩ | যুক্তবর্ণ ভেঙে ২ শব্দ + বাক্য | short_answer → Und | ৫ | all | ১ | ৫ |
| ৪ | সমার্থক শব্দ (২টি করে) | short_answer → Rem | ১০ | all | ০.৫ | ৫ |
| ৫ | সর্বনাম পদ ব্যবহার | short_answer → Und | ৫ | all | ১ | ৫ |
| ৬ | প্রশ্নোত্তর | short_answer → Und | ৫ | all | ২ | ১০ |
| ৭ | বড় প্রশ্ন | descriptive → App+ **FT** | ৩+ | any ২ | ৫ | ১০ |
| ৮ | বিরামচিহ্ন | short_answer → Und | ৫ | all | ১ | ৫ |
| ৯ | আবেদনপত্র / চিঠি | descriptive → App **FT** | ১ | all | ১০ | ১০ |
| ১০ | রচনা | descriptive → App+ **FT** | ২+ | any ১ | ১০ | ১০ |
| ১১ | শ্রুতলিপি | **ADMIN** | — | — | — | ৫ |

## A-13 · PAT-C4-MATH-ANNUAL-v1 — Authority: MP HY 2026 shape · ৩ ঘণ্টা
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | সংক্ষিপ্ত উত্তর | short_answer → Rem/Und | ১০ | all | ১ | ১০ |
| ২ | শব্দসমস্যা | structured → App | ৫ | any ৪ | ৬ | ২৪ |
| ৩ | মান নির্ণয় | short_answer → App | ৪ | all | ২ | ৮ |
| ৪ | কম্পোজিট (এক উদ্দীপক, ৩ অংশ) | structured → App | ১ (৩+৩+৪) | all | ১০ | ১০ |
| ৫ | কম্পোজিট (ভগ্নাংশ-জাতীয়, ৪ অংশ) | structured → App | ১ (২.৫×৪) | all | ১০ | ১০ |
| ৬ | জ্যামিতি | structured → App | ৪ | any ৩ | ৬ | ১৮ |
Whitelist: no MCQ/matching/TF/oral. **Assembly reminder from the 2026 coverage report:** the fence tick (step 3) must confirm গাণিতিক বাক্য/সময়/উপাত্ত slots when those chapters are in the fence — the 2026 paper dropped them silently.

## A-14 · PAT-C4-SCI-ANNUAL-v1 — Authority: MP Final 2025 · ২ ঘণ্টা ৩০ মিনিট
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | MCQ | mcq → Rem/Und | ১০ | all | ১ | ১০ |
| ২ | শূন্যস্থান পূরণ | fill_blank → Rem | ১০ | all | ১ | ১০ |
| ৩ | একবাক্যে উত্তর | short_answer → Rem | ১০ | all | ১ | ১০ |
| ৪ | সংক্ষিপ্ত প্রশ্ন | short_answer → Und | ৭ | any ৫ | ২ | ১০ |
| ৫ | বর্ণনামূলক | descriptive → App+ **FT** | ৯ | any ৬ | ৬ | ৩৬ |
| ৬ | শব্দের অর্থ | short_answer → Rem | ৪ | any ২ | ২ | ৪ |

## A-15 · PAT-C4-ENG-ANNUAL-v1 — Authority: MP Final 2025 · 2h 30m (one seen passage drives 1–2)
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| 1 | Passage MCQ | mcq → Rem/Und | 5 | all | 1 | 5 |
| 2 | Passage questions | short_answer → Und | 5 | all | 1 | 5 |
| 3 | Rhyming words | short_answer (f) → Rem | 5 | all | 1 | 5 |
| 4 | Underline the adjective | short_answer → Und | 10 | all | 1 | 10 |
| 5 | Yes/No vs Wh identification | short_answer → Und | 5 | all | 1 | 5 |
| 6 | Correct form of verbs (taught tenses) | fill_blank → App | 5 | all | 1 | 5 |
| 7 | Sequence words (box) | fill_blank → Und | 5 | all | 1 | 5 |
| 8 | Capitalization & punctuation rewrite | short_answer → Und | 1 text | all | 10 | 10 |
| 9 | Paragraph (or-choice) | descriptive → App **FT** | 2 | any 1 | 10 | 10 |
| 10 | Informal letter | descriptive → App **FT** | 1 | all | 10 | 10 |
| 11 | Spelling & Dictation | **ADMIN** (10 in-fence words) | — | — | 1 | 10 |

## A-16 · PAT-C4-BGS-ANNUAL-v1 — Authority: MP Annual 2025 · ২ ঘণ্টা ৩০ মিনিট
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | এক বাক্যে উত্তর | short_answer → Rem/Und | ১৫ | all | ১ | ১৫ |
| ২ | শূন্যস্থান পূরণ | fill_blank → Rem | ১২ | all | ১ | ১২ |
| ৩ | সত্য/মিথ্যা | true_false → Rem/Und | ১০ | all | ১ | ১০ |
| ৪ | মিলকরণ | matching → Rem/Und | ৫ | all | ১ | ৫ |
| ৫ | সংক্ষিপ্ত প্রশ্ন | short_answer → Und | ৮ | any ৬ | ৩ | ১৮ |
| ৬ | বর্ণনামূলক | descriptive → App+ **FT** | ৬ | any ৪ | ৫ | ২০ |
Whitelist: no MCQ in C4 BGS (paper authority).

## A-17 · PAT-C5-BAN-ANNUAL-v1 — Authority: MP Annual 2025 · ৩ ঘণ্টা · header reads **বার্ষিক পরীক্ষা** (2026 file's অর্ধ-বার্ষিক header is an error — corrected on this template)
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | শব্দার্থ | short_answer → Rem | ১০ | all | ০.৫ | ৫ |
| ২ | বিপরীত শব্দ + সেই শব্দে বাক্য | short_answer → Und | ৫ জোড়া | all | ২ | ১০ |
| ৩ | পদ নির্ণয় (দাগ দেওয়া শব্দ) | short_answer → Und | ৫ | all | ১ | ৫ |
| ৪ | যুক্তবর্ণ ভেঙে ২ শব্দ + বাক্য | short_answer → Und | ৫ | all | ১ | ৫ |
| ৫ | বিরামচিহ্ন | short_answer → Und | ৫ | all | ১ | ৫ |
| ৬ | বাক্যের ধরন নির্ণয় | short_answer → Und | ৫ | all | ১ | ৫ |
| ৭ | প্রশ্নোত্তর | short_answer → Und | ৫ | all | ২ | ১০ |
| ৮ | বড় প্রশ্ন | descriptive → App+ **FT** | ৩+ | any ২ | ৫ | ১০ |
| ৯ | আবেদনপত্র / চিঠি | descriptive → App **FT** | ১ | all | ১০ | ১০ |
| ১০ | রচনা | descriptive → App+ **FT** | ২+ | any ১ | ১০ | ১০ |
| ১১ | শ্রুতিলিপি | **ADMIN** | — | — | — | ৫ |

## A-18 · PAT-C5-MATH-ANNUAL-v1 — Authority: MP Final 2025 · ২ ঘণ্টা ৩০ মিনিট
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | সংক্ষিপ্ত উত্তর | short_answer → Rem/Und | ১০ | all | ১ | ১০ |
| ২–৮ | কম্পোজিট শব্দসমস্যা (এক উদ্দীপক, ৩–৪ অংশ ক/খ/গ/ঘ) | structured → App/Ana | ৭ | all | ৮ | ৫৬ |
| ৯ | সময়-রূপান্তর | short_answer → App | ১ | all | ৪ | ৪ |
| ১০ | জ্যামিতি (অঙ্কন + বিবরণ) | structured → App | ২ অংশ | all | (২.৫+২.৫) | ১০ |
Whitelist: no MCQ/matching/TF. Slots ২–৮ span the fence's chapters one composite each — the fence tick (step 3) allocates them; data/graph chapters need a composite slot when in fence (2026 gap).

## A-19 · PAT-C5-SCI-ANNUAL-v1 — Authority: **MP HY 2026 (new three-division pattern)** · ৩ ঘণ্টা
| Division | Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|---|
| ক | ১ | সংক্ষিপ্ত উত্তর | short_answer → Und | ১১+ | any ১০ | ২ | ২০ |
| ক | ২ | MCQ | mcq → Rem/Und | ১০ | all | ১ | ১০ |
| খ | ৩–৭ | রচনামূলক (ক/খ/গ অংশে বিভক্ত) | descriptive → App+ **FT** | ৫ | any ৪ | ১০ | ৪০ |
| গ | ৮–৯ | **উদ্দীপক-ভিত্তিক** (চিত্র/দৃশ্যকল্প + ক/খ/গ) | StimulusPayload + descriptive → App/Ana **FT** | ২ | any ১ | ১০ | ১০ |
The গ-division stimulus is authored as `LOCKED_StimulusPayload_Schema_v1.json` and shared by its sub-items — the one lane already exercising the bank's stimulus model.

## A-20 · PAT-C5-BGS-ANNUAL-v1 — Authority: MP Annual 2025 · ২ ঘণ্টা ৩০ মিনিট *(verify time on a clean copy — the 2026 file's header line was damaged)*
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| ১ | সংক্ষিপ্ত প্রশ্ন | short_answer → Und | ১০+ | any ৮ | ৩ | ২৪ |
| ২ | শূন্যস্থান পূরণ | fill_blank → Rem | ১০ | all | ১ | ১০ |
| ৩ | সত্য/মিথ্যা | true_false → Rem/Und | ১০ | all | ১ | ১০ |
| ৪ | রচনামূলক | descriptive → App+ **FT** | ৮+ | any ৬ | ৬ | ৩৬ |
Whitelist: no MCQ/matching in C5 BGS. **Curation reminder:** banking-chapter items pass the C-08 riba screen (the 2026 paper's Q2(ঝ) interest-blank is the standing counter-example — replaced per the Principal's separate ruling).

## A-21 · PAT-C5-ENG-ANNUAL-v1 — Authority: MP Final 2025 · 2h 30m (two seen passages: A drives 1–3, B drives 5–6)
| Slot | Format | Type → band | Items | Choice | M/item | Total |
|---|---|---|---|---|---|---|
| 1 | Passage A — gap-fill from box (3 extra words) | fill_blank → Und | 5 | all | 1 | 5 |
| 2 | Passage A — True/False | true_false → Und | 5 | all | 1 | 5 |
| 3 | Passage A — answer in sentences | short_answer → Und | 3 | all | 3 | 9 |
| 4 | Composition | descriptive → App+ **FT** | 1 | all | 10 | 10 |
| 5 | Passage B — gap-fill from box (3 extra) | fill_blank → Und | 5 | all | 1 | 5 |
| 6 | Passage B — True/False | true_false → Und | 6 | all | 1 | 6 |
| 7 | Correct form of verbs (taught tense range) | fill_blank → App | 5 | all | 1 | 5 |
| 8 | Change sentences per direction | short_answer → App | 5 | all | 1 | 5 |
| 9 | Make WH questions (underlined words) | short_answer → App | 5 | all | 2 | 10 |
| 10 | Rearrange words | short_answer (f) → Und | 5 | all | 1 | 5 |
| 11 | Letter | descriptive → App **FT** | 1 | all | 10 | 10 |
| 12 | Spelling & Dictation | **ADMIN** | — | — | — | 5 |
Whitelist: no MCQ in C5 English. Both passages authored as `StimulusPayload` records with their dependent items.

*(End of Annex A — 21 lanes; every column-total = ৮০.)*
