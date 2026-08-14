# canon/refs/MANIFEST.md — the P00 REF register

*Canon index. Read by `tools/audits/canon_check.py`'s **REF-CITE** check: every `REF-NN` cited
anywhere in the repo must resolve to a row below.*

**Numbering in force: Project 00's `REF-01…REF-26`.** The support-book lineage's `REF-1` / `REF-2`
are **retired** and resolve through the HISTORICAL alias rows at the bottom (Principal ruling
UD-60(b)). Historical citations of the SB numbers are **left as written** — rewriting a session log
to say something it did not say at the time is the larger violation. **New citations use P00
numbering.**

Status values:

- **ACTIVE** — a live authority some workstream builds against today.
- **REFERENCE** — canon, but not currently load-bearing for an open build.
- **POINTER** — the REF number names a Project-00 register that lives outside `canon/`, in
  `workstreams/curriculum-foundations/`. The row resolves the citation; the file is not here.
- **NOT-STAGED** — the REF number is known and no file for it exists in this repo.
- **HISTORICAL** — a retired number, kept resolvable so old citations do not dangle.

`canon/` is **cited, never copied** (AGENTS.md §8). REF-19 and REF-20 already had canon homes before
this register existed; their rows point at those homes and **no second copy was made**.

**Cross-reference — there are two canon indexes and they do not overlap.** This file resolves
**citations**: `REF-NN` → title, version, lock, consumers, path. `canon/MANIFEST.md` is the
**existence** index the gate walks to prove every canon path is present. **The five MarkLogic
spines are deliberately not in this register** — they are MarkLogic lineage, not REFs, and no REF
row is owed for them; they live in `canon/MANIFEST.md` and `canon/marklogic/README.md`.

## Register

| ID | Title | Version | Lock | Consuming workstreams | Status | Path |
|---|---|---|---|---|---|---|
| REF-01 | Islamic Curation Policy | v1.2 | LOCKED 2026-05-26 | support-books · lesson-plans · question-banks · class-tests · english-drive | **ACTIVE** | `canon/islamic-curation/REF-01_Curation_Policy.md` |
| REF-02 | Three-Layer Lesson Plan Template | v1.6 | LOCKED 2026-05-31 | lesson-plans | REFERENCE | `canon/refs/LOCKED_REF-02_Three_Layer_Lesson_Plan_Template_v1_6.md` |
| REF-03 | Subject Spine Playbook — Bangla (C1–C5) | v1.2 | LOCKED 2026-06-02 | lesson-plans · question-banks | REFERENCE | `canon/refs/LOCKED_REF-03_Bangla_Subject_Spine_Playbook_v1_2.md` |
| REF-03 | Subject Spine Playbook — English (C1–C5) | v1.2 | LOCKED | english-programme · lesson-plans | REFERENCE | `canon/refs/LOCKED_REF-03_English_Subject_Spine_Playbook_v1_2.md` |
| REF-03 | Subject Spine Playbook — Math (C1–C5) | v1.0 | LOCKED | lesson-plans | REFERENCE | `canon/refs/LOCKED_REF-03_Math_Subject_Spine_Playbook_v1_0.md` |
| REF-03 | Subject Spine Playbook — Science (C3–C5) | v1.0 | LOCKED 2026-05-29 | lesson-plans | REFERENCE | `canon/refs/LOCKED_REF-03_Science_Subject_Spine_Playbook_v1_0.md` |
| REF-03 | Subject Spine Playbook — BGS (C3–C5) | v1.0 | LOCKED | lesson-plans | REFERENCE | `canon/refs/LOCKED_REF-03_BGS_Subject_Spine_Playbook_v1_0.md` |
| REF-04 | NCTB Curriculum Stability Analysis — Universal Methodology Playbook | — (undated; §15 field-tested, §16 TG-Reconciliation) | not LOCKED | p01-nctb-stability | REFERENCE | `canon/refs/NCTB_Stability_Analysis_Playbook.md` |
| REF-05 | Stability analyses — **a family**, one per class × subject | — | — | p01-nctb-stability · support-books | **NOT-STAGED** | *(family; staged per lane when needed — see note 2)* |
| REF-06 | Bloom's Taxonomy — Comprehensive Primer for Teachers (V1A) | V1A | not LOCKED | lesson-plans · question-banks | REFERENCE | **canonical:** `canon/refs/Bloom_Taxonomy_Comprehensive_Primer_Teachers_V1A.docx` · **derived reading copy:** `…V1A.md` — see note 7 |
| REF-07 | Revision Architecture | v1.2 | LOCKED 2026-05-31 | lesson-plans · question-banks · class-tests | **ACTIVE** | `canon/refs/LOCKED_REF-07_Revision_Architecture_v1_2.md` |
| REF-08 | Homework Architecture | v1.3 | LOCKED 2026-05-31 | lesson-plans · question-banks | **ACTIVE** | `canon/refs/LOCKED_REF-08_Homework_Architecture_v1_3.md` |
| REF-09 | Tier 1 Question-Setting Guidelines | v1.0 | LOCKED | question-banks · class-tests · scholarship | **ACTIVE** | `canon/refs/LOCKED_REF-09_Tier1_Question_Setting_Guidelines_v1_0.md` |
| REF-10 | Tier 2 Question-Setting Guidelines | v1.0 | LOCKED | question-banks · scholarship | **ACTIVE** | `canon/refs/LOCKED_REF-10_Tier2_Question_Setting_Guidelines_v1_0.md` |
| REF-11 | Classroom Observation Rubric | v1.1 | LOCKED 2026-06-02 | lesson-plans | REFERENCE | `canon/refs/LOCKED_REF-11_Classroom_Observation_Rubric_v1_1.md` |
| REF-12 | School Mission and Islamic Values Reference | v1.0 | LOCKED 2026-05-28 | islamic-studies · support-books | REFERENCE | `canon/refs/LOCKED_REF-12_School_Mission_and_Islamic_Values_Reference_v1_0.md` |
| REF-13 | `PROJECT00_GLOSSARY` | — | — | curriculum-foundations | **POINTER** | `workstreams/curriculum-foundations/PROJECT00_GLOSSARY.md` |
| REF-14 | `PROJECT00_README` (§3 = master `D-###` series) | 2026-07-17 | — | curriculum-foundations · all | **POINTER** | `workstreams/curriculum-foundations/PROJECT00_README.md` |
| REF-15 | `PROJECT00_TODO` | — | — | curriculum-foundations | **POINTER** | `workstreams/curriculum-foundations/PROJECT00_TODO.md` |
| REF-16 | `PROJECT00_DECISIONS` (local `D-PROJ00-###`) | v1.60 (2026-07-17) | — | curriculum-foundations | **POINTER** | `workstreams/curriculum-foundations/PROJECT00_DECISIONS.md` |
| REF-17 | Bloom's Taxonomy — Standard Reference (V1B) | v1.0 | LOCKED | lesson-plans · question-banks · class-tests | **ACTIVE** | `canon/refs/LOCKED_REF-17_Blooms_Primer_V1B_Standard_Reference_v1_0.md` |
| REF-18 | Bloom's Taxonomy — Daily-Use Pocket (V1C) | v1.1 | LOCKED 2026-05-31 | lesson-plans · question-banks · class-tests | **ACTIVE** | `canon/refs/LOCKED_REF-18_Blooms_Primer_V1C_Daily_Use_Pocket_v1_1.md` |
| REF-19 | Vertical Topic Progression Map (slug authority) | v1.10 | LOCKED (canonical) | question-banks · lesson-plans · scholarship | **ACTIVE** | `canon/topics/LOCKED_REF-19_Vertical_Topic_Progression_Map_v1_10.md` |
| REF-20 | Approved Names Pool (Bengali-Muslim) | v1.0 | LOCKED (living/append-extensible per its §5) | support-books · class-tests · english-drive · lesson-plans · question-banks | **ACTIVE** | `canon/names/REF-20_Approved_Names_Pool.md` |
| REF-21 | Curation Trigger Lexicon & Skeleton Scan Protocol | v1.0 | LOCKED 2026-05-26 | lesson-plans · question-banks | **ACTIVE** | `canon/refs/LOCKED_REF-21_Curation_Trigger_Lexicon_Skeleton_Scan_Protocol_v1_0.md` |
| REF-22 | English Controlled Word Bank (C1–C5) | v1.0 | LOCKED | english-programme · english-drive · question-banks | REFERENCE | `canon/refs/LOCKED_REF-22_English_Controlled_WordBank_C1-C5_v1_0.xlsx` |
| REF-23 | Lean Project Scaffolding Standard | v1.0 | LOCKED | *(all — scaffolding)* | REFERENCE | `canon/refs/LOCKED_REF-23_Lean_Project_Scaffolding_Standard_v1_0.md` |
| REF-24 | Teacher Image-Handling Protocol (SR1) | v1.0 | LOCKED 2026-05-31 | lesson-plans · support-books | REFERENCE | `canon/refs/LOCKED_REF-24_Teacher_Image_Handling_Protocol_v1_0.md` |
| REF-25 | Paper Assembly Template Standard (PAT) | v1.0 | LOCKED 2026-07-16 | scholarship · class-tests · question-banks | **ACTIVE** | `canon/refs/LOCKED_REF-25_Paper_Assembly_Template_Standard_v1_0.md` |
| REF-26 | Exam Anchor Set (EAS) | v1.0 | LOCKED 2026-07-17 | scholarship · class-tests | **ACTIVE** | `canon/refs/LOCKED_REF-26_Exam_Anchor_Set_v1_0.md` |
| REF-27 | *(unassigned — the next free REF number)* | — | — | — | **RESERVED** | *(no file; see note 6)* |

### HISTORICAL aliases (retired numbering — resolve, never re-use)

| Retired ID | Resolves to | Note |
|---|---|---|
| REF-1 | **REF-01** — `canon/islamic-curation/REF-01_Curation_Policy.md` | Support-book lineage numbering. The two files were **byte-identical** at unification (md5 `8289b9b7…`), so this is a rename, not a merge. |
| REF-2 | **REF-20** — `canon/names/REF-20_Approved_Names_Pool.md` | Byte-identical at unification (md5 `de8db3b8…`). **Collision warning:** the support-book programme's *own* `REF-2_Content_Register_v1.md` is a **different document** — see note 3. |

## Notes

**1 — REF-03 is a family of five, one per subject.** All five carry the number REF-03. A bare
`REF-03` citation does not identify a file; cite the subject with it.

**2 — REF-05 is a family and is NOT-STAGED.** The stability analyses are per class × subject
(`completed_C{n}_{SUBJ}_StabilityReport_v{n}.md`), not one document. Several are cited by REF-04 and
by REF-19's version log. **No file for REF-05 exists in this repo**, and no row is invented for one.
They stage into `workstreams/p01-nctb-stability/` per lane when that workstream opens.

**3 — the REF-2 collision, resolved at CD-006 and recorded here so it is not re-derived.**
The support-book programme's `REF-2_Content_Register_v1.md` holds *"Name Bank (per-class pools),
per-class recurring cast, story allocation map, word lists"*
(`workstreams/support-books/governance/README.md` line 49). **That is not this REF-20.** CD-006
withdrew the claim that the canon slot carries recurring-cast material and assigned that cast canon
to the **storybook venture** — a separate repo under AGENTS.md §1's absolute no-crossover rule.
The support-book document itself is **not in this repo**; the only reference to it is a hard-coded
old-account path in `workstreams/support-books/audits/validate_admin_pass.py` line 50.

**4 — REF-25 §0 carries a known-false statement about Math MCQ.** Verified at source this session
against `canon/marklogic/MarkLogic_MATH_Spine.md`: slot **S01 IS বহুনির্বাচনি**, carrying 10 marks
at C2–C5 and 6 at C1. REF-25's lane/format authority was already demoted in favour of the spines
(UD-09/UD-11). **REF-25 is LOCKED and is not edited**; the correction is recorded in the demoted
Annex-A note when REF-25 is split in a later session.

**7 — REF-06 is the only binary here, so it carries a DERIVED markdown twin.** A `.docx` hides its
REF citations from the REF-CITE census and supersedes as an undiffable blob. **The `.docx` stays
canonical**; the `.md` beside it is a reading and gate-scanning copy, banner-marked
**DERIVED — regenerate on supersede**, and is never edited.

**Binding rule: a REF-06 supersede MUST re-run the conversion in the same session as the supersede.**
A stale twin is worse than none — it reads as current and diffs cleanly. Exact command, from the
repo root:

```
cd canon/refs && \
  pandoc -f docx -t gfm --wrap=none \
    Bloom_Taxonomy_Comprehensive_Primer_Teachers_V1A.docx -o _ref06_body.md && \
  cat ../../tools/_ref06_header.txt _ref06_body.md \
    > Bloom_Taxonomy_Comprehensive_Primer_Teachers_V1A.md && \
  rm _ref06_body.md
```

**`tools/_ref06_header.txt`** is the DERIVED banner block, reproduced verbatim at the top of the
current `.md`. Generated with **pandoc 2.9.2.1**; record the version used at each regeneration.

**It lives in `tools/`, not `canon/refs/`, and the move is the point (Principal ruling 2026-08-14,
session-2 ruling 5).** It was staged into `canon/refs/` beside the file it helps build, and a
`canon/MANIFEST.md` REQUIRED row was written for it. **Canon holds authority; a build input is not
authority.** A banner fragment sitting in `canon/refs/` with a REQUIRED row reads, to any later
session walking the manifest, exactly like the LOCKED REF files around it. Moved byte-identical
(md5 `7d0927be…`); its `canon/MANIFEST.md` row is retired and this row's command now names the new
path. It takes **no `tools/MANIFEST.md` row** — that register is executable tools only, by its own
header, and a REQUIRED row there would oblige a `SMOKE.md` for a text fragment.

**§3.6 verified at source 2026-08-14 — the indicative Bloom bands propagate faithfully, and nothing
downstream is stale.** REF-06 §3.6's four class-group rows (1–2 · 3–5 · 6–8 · 9–10) were read
against **REF-17 §5.2** and **REF-18 §4.2**, which restate the 1–2 and 3–5 rows **without
distortion**. **No correction propagates, and `LOCKED_ProductionCore_v1` is NOT stale on this
account.** §3.6's own opening line confirms the deferral sits at the top of the chain:

> Exact distributions will be set later in Tier 1 and Tier 2 guidelines. The following ranges are
> only indicative.

Two facts recorded so they are not re-derived:

- **The primer already covers Classes 6–10.** The Bloom layer is ready for the school's
  class-per-year expansion; **the MarkLogic spines are not — they stop at C5.** That asymmetry is
  the next expansion's first constraint.
- **§3.6 carries a D-050 scope note:** the bands are read at **chapter** scope, and a multi-period
  chapter's Bloom mix **climbs across its sessions** rather than holding a flat share of the band.
  A per-session reading of the table is a misreading.

**6 — REF-27 is RESERVED, and the row exists because the gate found it.** The REF-CITE resolver's
first run over the imported P00 registers FAILed on `REF-27` in three files. It is **not a missing
document** — it is the **next free REF number**, recorded as such by Project 00:
`PROJECT00_CROSS_PROJECT_INDEX.md` v1.55 carries *"add-reference next-free example → REF-27"* and
`PROJECT00_DECISIONS.md` v1.60 carries *"snapshot + Summary + next-free → REF-27"*.

**A next-free marker is a real citation of a real fact and must resolve**, so it gets a row rather
than an exemption in the resolver. **REF-27 is therefore the number the next new REF takes**, and
this is where a session verifies that at source (AGENTS.md §4). No file is invented for it.

**5 — two topic-ID authorities, neither demoted (RE-1).** `ref19_topic_id` is a **slug**, authority
**REF-19**. `topic_tag` is a **number**, authority `canon/topics/TOPIC_NUMBERS.md` under the CD-044
minting precedent. Both fields are required on every question and it is correct for them to
disagree in granularity.
