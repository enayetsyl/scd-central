# MODEL_PAPERS_POLICY — v1.0

*Workstream: scholarship. Adopted by Principal ruling 2026-08-09 (CD-038),
superseding the v0.1 draft staged in `_inbox/`.*
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
