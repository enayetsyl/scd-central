# QUESTION_POLICY — v1.0 (canon)

*Adopted 2026-08-14 by Principal ruling, unification session 2. Location: `canon/QUESTION_POLICY.md`.*
*Minted as **CD-092 … CD-113** — one row per §3 resolved conflict, plus §2, §4, §5 and §6, per §10.*

**Status: ADOPTED. This file is canon and is cited, never copied (AGENTS.md §8).**

*Provenance: drafted as v0.1 → v0.2 → v0.3 in the advisor chat and staged into `_inbox/`. It was
verified against the files it cites before adoption, twice. **v0.2 was stopped on three at-source
discrepancies** — §5 claimed MarkLogic §৮ "stands" while overriding it; §5's exposure figure
understated the domain ratio by 5 points; §7's readiness list was three handoffs stale and named 2
promoted sources where the repo held 31. v0.3 corrected all three plus four precision findings, and
verified clean on eight checks. **The corrections came from the verify-at-source pass, not from the
draft's own review** — recorded because that pass has now caught the advisor twice, and this file's
authority rests on it having been checked rather than accepted.*

*Changes are forward-only. A correction is a successor version and a CD row, never an edit here.*

---

## 1. Why this file exists

Five files governed question preparation independently: the P00 REF layer (REF-09/10 quality floor,
REF-06/17/18 Bloom, REF-19 topic slugs, REF-20 names, REF-01/21 curation, REF-07/08 pool
architecture, REF-25/26 assembly), P04's `LOCKED_QuestionBank_Production_Conventions_v1_4`, the
MarkLogic set, `QUESTION_BANK_POLICY`, and `MODEL_PAPERS_POLICY`. They were written for two different
paper worlds: the P04/REF-25 line reproduces **the school's 2026 Sylhet finals**; the MarkLogic line
reproduces **NAPE 2026**. Most conflicts in §3 descend from that split.

The layers are retained. Only the conflicts are resolved here.

## 2. Authority chain

**NAPE 2026 structure → MarkLogic Rules + spines + QuestionPolicy → REF-09 (Tier 1 quality floor) /
REF-10 (Tier 2) → this file → workstream policies → individual banks and papers.**

Alongside, in their own domains and not overridden by the above:

| Domain | Authority |
|---|---|
| Curation stances (what to replace, why) | **REF-01** — all classes and subjects from v1.3 |
| Curation recognition + scan proof | **REF-21** — authoritative for Projects 03 and 04 by its own header |
| Personal names | **REF-20**, by class pool |
| Bloom's indicative bands | **REF-06 §3.6** — REF-17 §5.2 and REF-18 §4.2 restate it |
| Topic **slugs** (`ref19_topic_id`) | **REF-19** — hard-validated by the harness |
| Topic **numbers** (`topic_tag`) | **`canon/topics/TOPIC_NUMBERS.md`**, minted per CD-044 |
| Pool architecture | **REF-07** (revision) + **REF-08** (homework) |
| Payload format | **LOCKED Hub import contract v1.0**, vendored at `tools/hub-export/` — supersede-only (CD-013) |
| Class list, term dates, paper durations | `canon/school-facts/SCHOOL_FACTS.md` |

**MarkLogic Rules §৪'s meta-rule binds this file too:** where any rule here collides with NAPE, NAPE
is right and the rule changes.

## 3. Resolved conflicts

| # | Conflict | Ruling |
|---|---|---|
| 1 | Paper structure: REF-25 Annex A (2026 finals) vs MarkLogic spines (NAPE) | **MarkLogic.** REF-25 keeps its assembly *mechanism* (§2 fields, §3 procedure); its lane/format authority is retired to historical reference |
| 2 | MCQ in Math: REF-25 §0 forbids vs MarkLogic MATH S01 | **MarkLogic.** Verified at source: `MATH-S01 = বহুনির্বাচনি`, 10 marks C2–C5, 6 at C1. REF-25 §0's claim is recorded as **known-false** in the demoted-Annex-A note |
| 3 | Optional questions: REF-25 "any n of m" vs MarkLogic **I-3** | **MarkLogic** — none anywhere |
| 4 | Paper totals: REF-09 §4.2 (C1–2 ≈50) vs MarkLogic **I-1** | **MarkLogic** — exactly 100, every class |
| 5 | Paper durations | **SCHOOL_FACTS**, one row per class |
| 6 | Class test: REF-09 §4.1 vs MarkLogic §৬ + CD-021 | **MarkLogic §৬ + CD-021** — 25 marks; **৩৫ মিনিট is a ceiling, ৩০ permitted** (CD-021); 4–6 questions lifted from the annual at **identical** marks, never shrunken |
| 7 | CT difficulty: REF-09 §4.1 easy ≥40% | **Superseded.** Lifting annual questions unchanged fixes difficulty by inheritance |
| 8 | REF-09 §4.2's section list vs the spines' fixed slots | **Read as a coverage rule, not a format rule** — a paper spans recall / short-response / extended-response; every spine does, under its own slot names. §4's *structure and balance* rules stay binding; only its *totals* were overridden, by the permission §4 itself grants |
| 9 | Bloom band vs domain ratios | **No conflict.** REF-06 §3.6 — the band's own source — opens: *"Exact distributions will be set later in Tier 1 and Tier 2 guidelines. The following ranges are only indicative."* REF-17 §5.2 and REF-18 §4.2 restate it faithfully (verified 2026-08-14). Neither file changes. The pool is banded to **whichever range is wider at each level** |
| 10 | Bloom levels vs NAPE domains | **Six Bloom levels stored, four domains derived.** The payload enum is the six English levels and has no domain field; NAPE mandates the four domains (MarkLogic §৩) and the teacher's ছক requires a domain column. Mapping: জ্ঞান→Remember · অনুধাবন→Understand · প্রয়োগ→Apply · উচ্চতর→Analyze+Evaluate+Create |
| 11 | Pool unit: REF-08 §4 (chapter) vs Conventions §4 (topic) | **Chapter**, per REF-08 §4 / master D-050, restated at REF-09 §4.3 |
| 12 | Pool partition: QB_POLICY three disjoint pools vs REF-07/08 one Pool | **One Pool per chapter.** HW · AS · CT are selection labels, not authored partitions |
| 13 | Repetition vs closed-set content | **Bound by Bloom level, with a listed supersede of MarkLogic §৮'s CT→annual row — see §5 and §9** |
| 14 | Content restrictions: REF-01 vs MarkLogic §৯ | **REF-01 governs stances**; MarkLogic §৯ becomes a pointer plus a class-general summary, each heading naming its C-code |
| 15 | Substrate | **The extraction is the source of fact; the curated form is what the question tests** (CD-049's line, extended to banks) |
| 16 | Bank storage: Conventions §6 (Drive) vs the repo | **The repo.** Deliverables stay committed; teachers are zero-Git (CD-024) |
| 17 | REF-10 §4's বৃত্তি description | **Superseded** — written before NAPE 2026 was approved |
| 18 | Topic IDs: which file mints them | **Two authorities, no conflict.** `ref19_topic_id` is a **slug** (`BAN-POEM`), owned by REF-19 and hard-validated by the harness. `topic_tag` is a **number** (`TOP-BAN-C5-05`), owned by `TOPIC_NUMBERS.md` under CD-044. REF-19 has never carried numbers (CD-043). Neither file is demoted |

## 4. The bank shape

**Unit.** One Pool per chapter, per class × subject, topic-tagged within.

**Sizing.** Floor **20 per chapter**, per **REF-09 §4.3** — REF-08 §4.1's own words are *"minimum 20
questions per **lesson** Pool"*, and §4.3 is what reads that floor at chapter scope under master
D-050. Cite §4.3, not §4.1, for the chapter reading. **No ceiling.** The real upper bound
is content: stop when the chapter's extraction is exhausted, because past that point new questions
are near-duplicates of existing ones.

Built in **waves**, each sized to what the extraction supports. The per-chapter target is decided at
production time and **stated in the bank file header with a one-line reason**. The governing test is
**coverage, not count**: the Pool must supply every topic in the chapter, every question-type its
spine slots need, and every difficulty band. When per-chapter spine slot-mapping exists as data, this
replaces the header-stated target.

**Scope of the Bloom band (D-050).** The band is read at **chapter** scope — the whole teaching unit,
however many periods it spans. Within a multi-period chapter the mix **climbs**: early sessions sit
at the chapter's lower end, later sessions reach into Apply/Analyze as the band allows (REF-06 §3.6
note; REF-02 §2.9 holds the per-session focus). A pool banded flat against the chapter band is
correct; **a bank built session-by-session drifts low** if the band is read per session.

**Metadata.** Every item carries, in the LOCKED payload: `qid` · `topic_tag` · `ref19_topic_id` ·
`question_text` · `question_type` · `paper_role` · `bloom_level` · `difficulty` · `tier` · `marks`.

- `topic_tag` and `ref19_topic_id` are **two different identities from two different registers** — a
  number and a slug. Both required; neither derives from the other.
- `paper_role` is a closed enum (`mcq` · `short` · `structured` · `creative`) denoting the
  **paper-section family** — not the pool, and never overloaded.
- `tier` is **required**; tier1 only for now (§7).
- The pool label lives authoring-side in the bank file's `pool_index`, outside the payload
  (`additionalProperties: false`). Upstream row **UP-002** requests an additive `pool` field.

**Difficulty.** REF-09 §3's floor applies at both levels: **easy ≥30%, hard ≤25%** on the paper, and
the Pool must be *able to supply* that split.

**Keys and rubrics.** Per REF-09 §5 — no question is finished until its key is written. The schema
enforces this by type: `mcq`→`options`, `true_false`→`tf_answer`, `fill_blank`→`blanks`,
`matching`→`pairs`, `short_answer`→`answer_key`, `descriptive`→`rubric`, each forbidding the others.

**Rubric shape (interim).** Minimum conforming: **two bands and a single `islamic_alignment`
criterion row** with band descriptors. **Marking is by the school's own scheme, held outside the
payload.** The scholarship rubric is applied manually and is not yet documented; when it is, it
enters as additional criterion rows with no migration. Reason: a four-row rubric nobody marks from
drifts from the scheme actually in use, and mis-calibrates C5 candidates against a বৃত্তি paper that
allocates marks differently.

**Answer length.** Per MarkLogic §৭ — marks signal length, and marking counts **distinct points**,
not lines written. In Math, NAPE's rule is mandatory: **no working shown, no marks**, printed in the
paper's instructions so no student meets it first at the scholarship exam.

**Content.** REF-01 stances, checked against REF-21's lexicon as an authoring self-check. Names from
REF-20 by class pool, varied within a lesson set. MarkLogic §৯'s consolidated restrictions apply.
Script guard per `LANGUAGE_RULES.md` §7. Bengali numerals in every student-facing string; `marks` is
a JSON number. No বিসমিল্লাহ line in paper headers.

## 5. Repetition

**MarkLogic §৮ is superseded in one row only, for `Remember` items only.**

| Bloom level | Across HW · AS · CT | Into HY / annual |
|---|---|---|
| **`Remember`** | verbatim reuse permitted | **verbatim reuse permitted — this supersedes §৮'s শ্রেণি পরীক্ষা ও বড় পরীক্ষা row** |
| Any other level | no verbatim reuse | no verbatim reuse |

Same chapter and same type remain fine at every level; it is the identical *question* that is barred
above `Remember`.

**What is being overridden, stated plainly.** §৮'s table bars হুবহু একই প্রশ্ন between the class test
and the big exams, and its prose names that path as the worst risk: a student memorises the CT answer
and the annual measures nothing. That reasoning is sound for reasoning-level items and does not hold
for recall. MarkLogic §৩ classifies শব্দার্থ, নামতা and বর্ণমালা as fixed-domain জ্ঞানমূলক content:
there is one correct meaning for a word, a second different correct question cannot be invented, and
memorising the answer *is* knowing it. A rule that cannot be followed for part of the syllabus is
worse than one narrowed on purpose.

**Exposure.** MarkLogic §৩ sets C5 জ্ঞানমূলক at **৩০%, ±৫% and no more** — so at most ৩৫% of a C5
paper is eligible for verbatim reuse, and the domain ratio is what caps it. No separate cap is set
here.

**No flag is authored** — `bloom_level` is already required, so the rule is machine-checkable as it
stands. Repetition of শব্দার্থ / নামতা / বর্ণমালা items across instruments is expected, not an error.

Also binding, per MarkLogic §৬: **at least one extended or উচ্চতর item in every class test**, and
across the year's tests **every question type appears at least twice**. The domain ratio is met
**across the year's tests, not within any single one** — 25 marks cannot carry four domains in
proportion, so there is no per-CT domain gate.

## 6. Gates (executed, in order)

1. `build_question_envelopes.py` fans the chapter bank into per-item envelopes.
2. `validate_import.py` L1–L4 on every envelope — born conformant, **verbatim output pasted** (AGENTS §5).
   *Invocation: pass `--envelope-schema tools/hub-export/import-contract.schema.json` explicitly
   (SMOKE.md finding V-1).*
3. `workstreams/question-banks/audits/gates.py`:

| Gate | Checks |
|---|---|
| Mark value | against MarkLogic spine values |
| Source traceability | every item resolves to its chapter extraction |
| Script guard | LANGUAGE_RULES §7 |
| `ref19_topic_id` resolves | against REF-19's slug set |
| `topic_tag` resolves | against `TOPIC_NUMBERS.md`; an unminted number FAILs, never auto-mints |
| Key/rubric present | every item, per type |
| Bloom band | Pool spans the wider of REF-06 §3.6 / MarkLogic §৩, read at **chapter** scope |
| Difficulty | easy ≥30% / hard ≤25%; Pool *can supply* |
| Repetition | no verbatim reuse of non-`Remember` items |
| Coverage | every topic and every spine slot-type supplied |
| Domain ratio | **paper level only**, never per pool |

Every gate carries a seeded selftest that bites each run, built from synthetic fixtures and never
drawn from the live file pool (CD-055, CD-064(f)).

4. Anchor coverage per REF-26 (Conventions §9 step 8a).
5. Human review gate — REF-09 §9. **The Principal acts as Subject Lead until Subject Leads are named.**
6. Hub import as `draft` → teacher in-app review → Principal promotes `reviewed → gold` (CD-003).

## 7. Scope and sequence

- **Tier 1 only.** Tier 2 opens when stretch-authors and Subject Leads are named.
- **Religion (REL) out of scope** until `islamic-studies` opens.
- **A chapter with no extraction gets no bank.** The gap is recorded, never filled from memory.
- **Order follows extraction readiness.** As at CD-084 and commit `4029296`, the promoted C5 surface
  is **31 source files** under `canon/sources/c5/` — 11 Bangla (পাঠ ১–১১) and 20 English (U01–20) —
  plus `canon/marklogic/C5_Bangla_Source_13-23.md` covering পাঠ ১৩–২৩. পাঠ ১২ is excluded by standing
  ruling. **Which of that surface a given wave takes is a Principal decision, not a readiness fact.**
  This cannot be written as a fixed schedule; the readiness list is re-read at source each wave, never
  carried forward from a handoff.
- CD-045's production sequence is unchanged; banking already-promoted canon needs no amendment.
- File naming per master **D-037**: `C{class}_{SUBJECT}_U{nn}_QuestionBank_v{ver}.{ext}`;
  QIDs per Conventions §3 (`QP-BAN-C5-U13-Q01`).

## 8. What this file does NOT govern

Paper assembly mechanics (REF-25 §2–§3) · lesson plans and their openings · replacement content ·
teacher training · the Hub's usage-lock and AS rotation (blocked on UP-002) · marking schemes in
actual use · the storybook venture.

## 9. Superseded by this file's adoption

| File | Section | Disposition |
|---|---|---|
| REF-25 | Annex A lane/format authority | Historical format reference; §2–§3 mechanism retained; §0's Math-MCQ claim recorded as known-false |
| REF-10 | §4 বৃত্তি bullet | Superseded |
| REF-09 | §4.1 easy ≥40% (CT) | Superseded by MarkLogic §৬ |
| REF-01 | §1.2 scope line | → v1.3: all classes and subjects; living/append-extensible |
| MarkLogic QuestionPolicy | **§৮**, শ্রেণি পরীক্ষা ও বড় পরীক্ষা row | **Superseded for `Remember` items only** (§5). Every other row and level stands unchanged |
| MarkLogic QuestionPolicy | §৯ | Pointer + class-general summary, headings citing C-codes |
| Conventions v1.4 | §4 (30/topic), §6 (Drive storage), §8 (three streams) | Corrected to chapter scope, repo storage, selection labels |
| QUESTION_BANK_POLICY | §2, §3, §4, §5 | Amended: one Pool, `tier` added, REF-09 §5 key wording, gate list per §6 |

**REF-09 §4's mark totals were overridden by the permission §4 itself grants, not superseded — REF-09
needs no edit beyond §4.1.** **`TOPIC_NUMBERS.md` is not demoted** — an earlier draft proposed it on
the false premise that REF-19 carried numbers; CD-043 had already settled that it does not.
Superseded sections are replaced by pointer stubs per supersede-with-archive (master §5.3);
superseded text is never left in place.

## 10. Adoption

**Adopted 2026-08-14.** This minted **CD-092 … CD-113** in `canon/DECISIONS.md`: one row per §3
resolved conflict (CD-093 … CD-110, conflicts 1–18 in order), plus the authority chain §2
(**CD-092**), the bank shape §4 (**CD-111**), the repetition rule §5 (**CD-112**) and the gate list
§6 (**CD-113**). Each row is citable on its own; this file is the readable form of all twenty-two.

The §9 supersedes were executed in the same session, each as supersede-with-archive per master
§5.3 — pointer stubs, not banners, with the superseded text preserved in its own archive block and
never left in place.

The Unification Decision Register (60 rows) is the provenance record and is filed alongside.
