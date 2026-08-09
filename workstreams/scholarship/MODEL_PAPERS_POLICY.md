# MODEL_PAPERS_POLICY — v1.1

*Workstream: scholarship. Adopted v1.0 by Principal ruling 2026-08-09 (CD-038), superseding the
v0.1 draft staged in `_inbox/`. v1.1 adds **§8**, the six C5 English source-fact rulings (CD-049).*
*Authority: `canon/marklogic/` — cited, never copied (AGENTS.md §8).*

## 1. Purpose

Fix the mark scheme as concrete, visible papers: one **model HY** and one **model Annual** per
class × subject, plus **model CTs**, all generated from the MarkLogic spines. A model paper is the
reference implementation of the mark scheme — what every real paper is compared against.

## 2. Scope and counts

- **Classes:** per `canon/school-facts/SCHOOL_FACTS.md` (today C1–C5; extends one class per year,
  automatically, per CD-015). The list is read from SCHOOL_FACTS, never restated here.
- **Subjects:** BAN · ENG · MATH · SCI · BGS (SCI/BGS from C3, per spine).
- **Per class × subject:** 1 model HY (100) + 1 model Annual (100) + **1 model CT (25 marks ·
  35 minutes, CD-021)**.

### Model CT granularity (CD-038)

**Per subject only** — one model CT per class × subject, not one per chapter tier. The three
accepted C5 Bangla class tests (Ch19, Ch20, Ch21) already show that a single 25-mark shape carries
prose, poem and grammar-applied chapters without re-cutting. If real class tests later show the one
model does not fit a chapter type, tiers are added by a new decision row — not assumed now.

## 3. Authority chain (unchanged, restated for this use)

**NAPE structure > MarkLogic spines / QuestionPolicy > this policy > individual papers.**

The 21 phase-1 templates are the historical base; their **80-mark halves are SUPERSEDED** by the
100-mark ruling (CD-002). Where a template and a spine disagree, **the spine wins**.

## 4. Content rules

- Model papers use **real questions drawn from source extractions**
  (`canon/sources/SOURCE_POLICY.md`) where an extraction exists. Where none exists yet, slots carry
  **typed placeholders naming the slot, its marks and its domain** — never invented content
  presented as real.
- Domain mix per class band exactly as `MarkLogic_QuestionPolicy.md` §৩
  (জ্ঞান · অনুধাবন · প্রয়োগ · উচ্চতর).
- All consolidated content restrictions in `MarkLogic_QuestionPolicy.md` §৯ apply — names from
  `canon/names/REF-2_Content_Register.md`, no living-being images (C-05), no music or performance
  (C-03/C-19), interest-free money contexts, শহিদ handled per §৯.
- **Language:** plain চলিত Bengali; **Bengali numerals** in everything a student or teacher reads;
  Arabic numerals only inside the mark-authority files (`LANGUAGE_RULES.md` §2). সাধু source
  passages are quoted verbatim and everything written *about* them is চলিত (§4).

## 5. Production and gates

- Produced in this workstream, **one class × subject per session**.
- **Order (CD-038): C5 first, then C4 → C3 → C2 → C1.** C5 is the scholarship year and today
  the only class with a source extraction in canon, so it is the only class whose model papers can
  use real questions rather than placeholders.
- Gates (executed): mark-total recompute (= 100, or = 25 for a CT) · slot-by-slot match against the
  spine row · domain-ratio check against QuestionPolicy · script guard on rendered text.
- Render via `tools/render` (`ct_docx.py`, accepted at CD-023; the reference CTs under
  `tools/render/reference/` are **FORMAT reference only** and their ৪৫ মিনিট line must never be
  copied). Teacher-facing deliverable committed — teachers are zero-Git operators and cannot
  regenerate it (CD-024).

## 6. Approval

Each model paper is **Principal-approved individually** before it is marked MODEL. An approved
model paper is supersede-only. A real term paper **cites its model**, and any deviation needs a
stated reason.

## 7. Status at adoption

No model paper has been produced. `audits/gates.py` in this workstream has **no gates defined and
therefore FAILS by design** (the `_template` behaviour: a workstream with zero gates cannot declare
anything final). The gates in §5 are written when the first C5 model paper is built.

## 8. C5 English — six source facts, and what step ② does with each (CD-049)

The C5 English extractions record the book as printed, because that is what an extraction is
for (`canon/sources/SOURCE_POLICY.md` §3). Six of the things they record would otherwise be
rediscovered — or worse, silently copied — when the first model paper is built. The Principal
ruled all six on 2026-08-09. **The extractions are not edited by any of these rulings.**

**The line that runs through all six: a source records what the book says; canon governs what
the school prints.** Every ruling below is applied on the output side.

| # | What the source records | What step ② does |
|---|---|---|
| 1 | **Unit 20's only writing stimulus is six pictures of a deer** (printed 106–107). | Source keeps it as-is. The model paper **substitutes a REF-1-compliant stimulus**. **C-05 governs outputs, never the source record** — an extraction that self-censored would misreport the book and break the spot-check. |
| 2 | **Units 14 and 17 open with five-item MCQ exercises.** | **Not mirrored.** MarkLogic retired MCQ from English at every class (`MarkLogic_ENG_Spine.md` — fourteen written slots, no MCQ anywhere). The book's MCQs are **classwork-only history**. |
| 3 | **"Quater past" / "Quater to" printed twice** on printed 43 — the page `ENG-S11` draws on, which spells *quarter* correctly three times elsewhere. | Source keeps the printed typo. **Every authored item uses "Quarter past".** A printed typo is never canon for output. |
| 4 | **Unit 7's 2.1 is four-fifths lift-the-line** — answers copyable verbatim from the passage. | **Not mirrored.** `MarkLogic_QuestionPolicy.md` domain ratios govern what the paper asks. |
| 5 | **Unit 17's only named character is Bidhan.** | The **CD-042 name rule** applies unchanged: replaced from the REF-2 C5 pool in all authored items, **exercise structure kept**. Not a new ruling — the existing one, applied. |
| 6 | **Unit 15 is a poem with no prose passage** (and Unit 10 likewise). | **S03's passage IS the poem.** Chapter-bound means chapter-bound: S03's 18 marks on Unit 15 are set on the poem itself. Recorded forward-only as an application note under `ENG-S03` in `MarkLogic_ENG_Spine.md`, where an author reads what the passage must be — no mark in that table changed. |

Rows 1, 3 and 5 share one shape worth stating for the next subject: **where the book and canon
disagree, the extraction records the book and the paper follows canon.** Neither file is bent to
match the other, and the disagreement stays visible in both.
