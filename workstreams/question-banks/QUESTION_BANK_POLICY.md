# QUESTION_BANK_POLICY — v1.1

*Amended 2026-08-14 under `canon/QUESTION_POLICY.md` §9 (**CD-120**): §2 (one Pool; HW/AS/CT are
selection labels) · §3 (`tier` added) · §4 (REF-09 §5 key wording; domain ratio to paper level) ·
§5 (gate list per QUESTION_POLICY §6). Amendments are pointer stubs with the superseded text
archived in place, per master §5.3. **This file is not LOCKED**, so the amendments sit inline
rather than in a successor file; the original text is preserved in every case.*

*Workstream: question-banks (P04). Adopted by Principal ruling 2026-08-09 (QB-D-001…QB-D-004),
superseding the v0.1 draft staged in `_inbox/`.*
*Authority: `canon/marklogic/` (marks and structure) + `canon/sources/SOURCE_POLICY.md` (content)
+ the LOCKED Hub import contract v1.0, vendored at `tools/hub-export/` (format).*

## 1. Purpose

Per chapter, per class × subject: tagged question pools authored **born-conformant** to the
Hub's LOCKED import contract, delivered to teachers through the Hub.

## 2. The three pools — the founding decision (QB-D-001)

> **AMENDED 2026-08-14 — pointer stub (CD-120).** **There is ONE Pool per chapter.**
> **HW · AS · CT are *selection labels*, not authored partitions.** Governing text:
> `canon/QUESTION_POLICY.md` §3.12 and §4, which resolve this against **REF-07** and **REF-08**,
> both of which describe a single Pool that instruments draw from.
>
> **Why the three-pool form was retired:** it triples the authoring cost, makes per-chapter coverage
> unmeasurable (three partial pools each covering part of the chapter is not the same as one Pool
> covering it), and — the decisive one — **makes an item's instrument an authoring-time decision
> that cannot later be changed without rewriting the item.** A selection label can be re-selected.
> An authored partition cannot.
>
> **What survives unchanged:** there is still **no CW pool**, and zero-repeat within an instrument
> still holds. **What goes:** the zero-overlap-between-pools gate — with one Pool there are no
> pools to overlap; the repetition rule that replaces it is `QUESTION_POLICY` §5, bound by Bloom
> level. Sizing ceilings below are superseded by §4's floor-20-no-ceiling, coverage-not-count.
>
> <details><summary><strong>ARCHIVE — the superseded QB-D-001 text, verbatim</strong></summary>
>
> Every chapter carries exactly **three pools — HW · Assignment (AS) · CT**.
> A question belongs to **exactly one pool.** Zero overlap between the three pools of the same
> chapter, enforced by gate — the EnglishDrive zero-repeat principle (PD-036/PD-038) applied here.
>
> </details>

*The original section follows, retained as the record of what was decided at QB-D-001.*

Every chapter carries exactly **three pools — HW · Assignment (AS) · CT**.

There is **no CW pool.** Classwork is the teacher's live practice, not a pooled artifact;
the CW pool is discarded by Principal ruling.

A question belongs to **exactly one pool.** Zero overlap between the three pools of the same
chapter, enforced by gate — the EnglishDrive zero-repeat principle (PD-036/PD-038) applied here.

### Sizing — ceilings, not session quotas (QB-D-002)

| Pool | Feeds | Per-chapter ceiling |
|---|---|--:|
| HW | daily homework via Hub assembly | 100 |
| AS | assignments incl. spaced revision rotation | 50 |
| CT | class-test authoring (25-mark / 35-min rule, CD-021) | 30 |

**These are cumulative ceilings for the chapter's whole life, built in waves — not a
single-session obligation and not a target a chapter must reach.** A wave is sized to what the
chapter's source extraction actually supports; the gate reports the balance still owed against
the ceiling rather than demanding it at once.

The reason is not convenience. A chapter's extraction contains a finite number of distinct
askable facts. Authoring past that number produces near-duplicates, and near-duplicates are
exactly what the zero-overlap gate exists to catch — so a fixed per-session quota would set the
sizing rule and the overlap gate against each other. Ceilings + waves keep both honest.

This supersedes the *"~30 q/chapter"* norm carried from master **D-051** (reconstructed at
CD-036), which set the P04 pool convention when the Homework Question Pool moved to Project 04.
D-051's placement rules are unchanged: plans link by topic tag and questions are not printed in
the plan.

## 3. Tagging — and where the pool label actually lives (QB-D-003)

> **AMENDED 2026-08-14 (CD-120).** The field list below is **incomplete: `tier` is required** and
> is missing from it. The authoritative list is the LOCKED payload's own `required` array — **ten
> fields**: `qid` · `topic_tag` · `ref19_topic_id` · `question_text` · `question_type` ·
> `paper_role` · `bloom_level` · `difficulty` · **`tier`** · `marks` — verified against
> `tools/hub-export/LOCKED_QuestionPayload_Schema_v1.json` on 2026-08-14. `tier1` only for now.
> Governing text: `canon/QUESTION_POLICY.md` §4.

Every question carries, in its LOCKED payload: `bloom_level` · `difficulty` · `topic_tag`
(`TOP-*`, the cross-repo join key) · `ref19_topic_id` · `paper_role` · `marks` · **`tier`**. The scholarship
domain label (জ্ঞান · অনুধাবন · প্রয়োগ · উচ্চতর) maps onto `bloom_level` per
`canon/marklogic/MarkLogic_QuestionPolicy.md` §৩.

**The v0.1 draft proposed carrying the pool in `paper_role`. Verified at source, that is wrong
and is corrected here.** In both `tools/hub-export/LOCKED_QuestionPayload_Schema_v1.json` and
`import-contract.schema.json`, `paper_role` is a **closed enum — `mcq` · `short` · `structured` ·
`creative`** — and it already denotes the REF-09 §4/§5.3 **paper-section family**, which the Hub
uses for set assembly. It is a different axis from the pool, and overloading it would corrupt a
field the app already reads. The payload schema is additionally `additionalProperties: false`,
so a `pool` key cannot simply be added to the payload either — the harness L2 pass would reject
every item.

**Therefore, until the Hub ships the field:**

- The pool label lives **authoring-side**, in the bank file's own `pool_index` block
  (`{"HW": [qid…], "AS": [qid…], "CT": [qid…]}`), outside the LOCKED payload. The pool gates run
  against `pool_index`; the envelope builder ignores it; the LOCKED contract is untouched.
- The gap is raised as an **upstream row, never improvised locally** — `tools/hub-export/UPSTREAM_ISSUES.md`
  **UP-002**, asking `scd-hub` for an ADDITIVE `pool` field on the question payload and its
  `tags` mirror (the outer contract stays stable, exactly as the question and stimulus doc-types
  were added). This follows CD-013: a vendored LOCKED artifact is supersede-only and is never
  patched here.
- **Consequence accepted meanwhile:** the Hub cannot filter by pool on import. Pool separation is
  guaranteed at authoring time only. Hub-side usage-lock and AS rotation (§6) need this field
  before they can be built.

## 4. Authoring rules

> **AMENDED 2026-08-14 (CD-120).** Two changes, both from `canon/QUESTION_POLICY.md`:
> **(a) Keys and rubrics — REF-09 §5's wording governs: *no question is finished until its key is
> written*.** The key is not a later pass; an item without its key or rubric is not an item. The
> schema enforces it by type (`mcq`→`options` · `true_false`→`tf_answer` · `fill_blank`→`blanks` ·
> `matching`→`pairs` · `short_answer`→`answer_key` · `descriptive`→`rubric`, each forbidding the
> others). **(b) The domain ratio moves to PAPER level and is never checked per pool.** MarkLogic
> §৩ sets the ratio for a **প্রশ্নপত্র**; a Pool is not a paper, and a pool-level domain gate would
> force every chapter to carry all four domains in proportion — which §৬ itself says is impossible
> even for a 25-mark class test. Governing text: `QUESTION_POLICY` §4 and §6.
>
> **AMENDED AGAIN 2026-08-15 (CD-136).** The **first bullet** below moves from *content* scope to
> **STIMULUS** scope: the stimulus must resolve to the extraction, and a key that is a general
> Bangla language fact may be teacher-supplied, declared in the item's own `model_note`.
> Generalised from `QB-D-013` per CD-121(d). The superseded bullet is archived in place beneath it.
> **No gate change** — see CD-136(e)–(g). Governing text: `QUESTION_POLICY` §9.

- **Content from the chapter's source extraction — AMENDED 2026-08-15 (CD-136) to STIMULUS scope.**
  **The STIMULUS must resolve to the chapter's source extraction** (`canon/sources/SOURCE_POLICY.md`).
  **The KEY need not, where it is a general Bangla language fact** — সমার্থক · বিপরীত ·
  যুক্তবর্ণ বিভাজন · এক কথায় প্রকাশ · ভাষারীতি / পদ নির্ণয় / ক্রিয়ার কাল. Such a key may be
  **teacher-supplied**, and **the item declares it in its own `model_note`**, so the provenance
  travels with the item and not only with the bank header — a header note is lost the moment an
  item is lifted into a paper, which is the only form in which items are ever used.
  **No extraction → no bank for that chapter; the gap is recorded, not filled from memory** —
  unchanged.

  **BOUNDARY, load-bearing.** This admits **language facts ABOUT chapter material**. It does
  **not** admit new content, new facts, or prompts with no chapter anchor. The test is the
  stimulus: *the word is in the chapter; its synonym is a fact about Bangla.* **S14 আবেদনপত্র and
  S15 রচনা stay OUT of chapter banks** — they anchor to nothing in the chapter and carry no key at
  all, so neither half of the rule is in play. Their home is paper-level authoring
  (`workstreams/scholarship/MODEL_PAPERS_POLICY.md`).

  **No gate enforces this, deliberately.** `SOURCE-TRACE` never read keys — both implementations
  resolve only `source_index[qid]` — so *"the key need not resolve"* was already true. A FAIL
  branch for an undeclared teacher key was **proposed and refused**: it would build key-resolution
  the gate does not have **in order to enforce a loosening**, and would fire on legitimate items
  whose keys are the student's own work. **Enforcement is the §6 human review gate — the Principal
  as Subject Lead** (REF-09 §9). Reasoning in full at CD-136(e)–(g).

  > **⚑ INTERIM AUTHORING RULE — binding at authoring time (Principal, 2026-08-15; `PENDING-P-037`).**
  > **Any item carrying a teacher-supplied key is authored as `short_answer` or `descriptive`.**
  >
  > **Why the rule exists.** CD-136 requires the declaration to travel in the item's own
  > `model_note`. Read against `LOCKED_QuestionPayload_Schema_v1.json`, **that field exists on two
  > of the six question types**: `answer_key.model_note` (`short_answer`) and the rubric criterion
  > (`descriptive`). **`mcq`, `fill_blank`, `true_false` and `matching` have no prose field at all**
  > — `mcqOption` carries only `option_id` / `text` / `is_correct` / `why_wrong`, `fillBlank` only
  > `blank_no` / `accepted` / `normalized_match` / `marks`, and both are
  > `additionalProperties: false`. The schema is **LOCKED and supersede-only (CD-013)**, so it is
  > not widened here.
  >
  > **A chapter that needs a teacher-keyed `mcq`, `fill_blank`, `true_false` or `matching` item is
  > STOP-AND-ASK. It is never a workaround.** In particular the declaration does **not** go in a
  > distractor's `why_wrong` and does **not** go in the bank header alone — **a header note is lost
  > the moment an item is lifted into a paper**, which is the exact failure CD-136 and QB-D-013
  > both exist to prevent.
  >
  > **Same shape as `pool_index` under UP-002**: the authoring side carries the constraint honestly
  > while the additive field is requested upstream, rather than patching a LOCKED contract locally.
  > **Lifts when `PENDING-P-037` closes.** পাঠ ১৩ wave 3 complies — all nine teacher-key items
  > (S06 · S12 · S13) are `short_answer`.

  <details><summary>SUPERSEDED TEXT — archived verbatim per master §5.3 (never left in place)</summary>

  > - **Content ONLY from the chapter's source extraction** (`canon/sources/SOURCE_POLICY.md`).
  >   No extraction → no bank for that chapter; the gap is **recorded, not filled from memory**.

  </details>
- **Marks per question ONLY from MarkLogic values — and as of 2026-08-15 that means the SLOT REGISTER, not a copy of it.** `MARK-VALUE` reads `canon/marklogic/SLOT_REGISTER.json`'s `marks_per_item` per (subject, class, slot); the two per-item mark tables vendored inside `audits/gates.py` are RETIRED. They covered `("BAN", 5)` alone, so every other class was refused for want of a table that would have had to be hand-copied — and a hand-kept copy is what CD-011 forbids. Annual-slot per-item marks are carried
  unchanged at CT scale (`MarkLogic_QuestionPolicy.md` §৬: a class test lifts 4–6 questions from
  the annual paper with marks identical, never a shrunken version).
- **Domain ratios per class band, checked per pool, not per question**
  (`MarkLogic_QuestionPolicy.md` §৩; C5 = জ্ঞান ৩০ · অনুধাবন ৩৫ · প্রয়োগ ২৫ · উচ্চতর ১০, ±৫%).
- **AS difficulty (QB-D-004): the AS pool is deliberately mixed — roughly half at HW level, half
  above it.** Spaced revision has to re-test the basics as well as stretch; an AS pool that only
  stretches stops being revision. The domain-ratio gate applies the same C5 band to AS, and the
  difficulty split is checked separately.
- All consolidated content restrictions in `MarkLogic_QuestionPolicy.md` §৯ apply; names come
  from `canon/names/REF-2_Content_Register.md` only, by class pool.
- **Script guard applies** — bank JSONs are Hub-bound, so `canon/language/LANGUAGE_RULES.md` §7
  governs them: Arabic script RED anywhere (use `(স)`, never the Arabic honorific glyph), arrows
  and emoji RED in rendered text, em-dash and ellipsis allowed. Enforcement is authoring-side
  only — the harness has no charset check (UP-001 / CD-013).
- **Bengali numerals in every student-facing string** (`LANGUAGE_RULES.md` §2); the `marks` field
  is a JSON number and stays in Arabic numerals.
- Answer or marking guidance per question wherever the type needs it; **the CT pool always**
  carries it.

## 5. Format and gates (executed, in order)

1. Bank authored as one JSON per chapter; `tools/hub-export/build_question_envelopes.py` fans it
   out into per-item envelopes.
2. `tools/hub-export/validate_import.py` L1–L4 on every envelope — born conformant, **verbatim
   output pasted** (AGENTS.md §5).
3. `workstreams/question-banks/audits/gates.py`:

   > **AMENDED 2026-08-14 (CD-120) — the gate list is now `canon/QUESTION_POLICY.md` §6's,
   > eleven checks:** mark value against the SLOT REGISTER's `marks_per_item` (CD-138; **amended 2026-08-15** from *"spine values"*, which named a vendored copy that is now retired) · source traceability to the chapter
   > extraction · script guard (LANGUAGE_RULES §7) · `ref19_topic_id` against REF-19's slug set ·
   > `topic_tag` against `TOPIC_NUMBERS.md` (**an unminted number FAILs, never auto-mints**) ·
   > key/rubric present per type · Bloom band at **chapter** scope · **plan check (added
   > 2026-08-15 — Bloom margins ≥ 2, full per-slot demand, task declarations, P-037 types,
   > within-slot near-duplicate stems; replaces the plan-table countersign, not the
   > item-level human read)** · **export sync against
   > `banks/envelopes/` **including contract v1.1's `question_batch` wrapper (CD-143)**
   > (added 2026-08-15 — the export ran two waves behind the bank and no gate
   > could see it, because every gate reads the bank and §11 imports the envelopes)** ·
   > difficulty easy ≥30% /
   > hard ≤25% with the Pool *able to supply* · repetition (no verbatim reuse above `Remember`) ·
   > coverage of every topic and spine slot-type · **domain ratio at paper level only**.
   >
   > **Two of the old checks are retired by the one-Pool ruling, not dropped for convenience:**
   > *zero-overlap across three pools* has nothing left to compare, and *domain-ratio per pool*
   > is the §4(b) error above. **The suite is not yet built** — it is session 3's work.
   >
   > <details><summary><strong>ARCHIVE — the superseded gate list, verbatim</strong></summary>
   >
   > zero-overlap across the chapter's three pools · domain-ratio per pool · mark-value check
   > against MarkLogic · source-traceability · AS difficulty mix · sizing-ceiling report ·
   > script guard.
   >
   > </details>
4. Hub import as `draft` → teacher in-app review → Principal promotes `reviewed → gold`
   (the existing loop, CD-003).

**Invocation note carried from `tools/hub-export/SMOKE.md` (finding V-1):** the harness discovers
its envelope schema by glob and the vendored file's name matches neither pattern, so
`--envelope-schema` must be passed explicitly. `build_question_envelopes.py`'s default schema path
(`../../docs/import-contract.schema.json`) does not exist in this repo either — pass
`--envelope-schema tools/hub-export/import-contract.schema.json`. Neither file is renamed; both are
vendored under the LOCKED contract and are supersede-only.

## 6. Hub-side companions (separate `scd-hub` work — referenced, not specified here)

**Usage-lock** (a question used for HW or AS is marked and never auto-offered twice) and **AS
rotation** (completed-chapter questions resurface at spaced intervals). Authoring-side, this
policy guarantees only what those features need: stable question IDs, pool labels, topic tags.
**Both are blocked on UP-002** — without a pool field on the payload the Hub cannot tell the
pools apart.

## 7. Pilot (first execution)

**C5 Bangla পাঠ ২১ — বিদায় হজের ভাষণ.** Three pools seeded, wave 1, from the accepted Ch21
material only, run through the full gate chain end-to-end. The pilot closes two of the tools
manifest's `VENDORED-UNPROVEN` rows and prices per-chapter authoring effort before scale-up.

*Correction to the v0.1 draft: it said "the last two UNPROVEN rows". There are **three** —
`LOCKED_QuestionPayload_Schema_v1.json`, `build_question_envelopes.py`, and
`tools/images/pick_placements.py`. The pilot closes the first two. `pick_placements.py` is an
interactive tkinter GUI in the images toolchain and cannot be proven headlessly (CD-022); it is
untouched by this pilot.*

## 8. Scope

Religion (REL) is **out of scope for now** (Principal ruling, this adoption), consistent with
`canon/sources/SOURCE_POLICY.md` §4. REL banks are authored when `islamic-studies` opens.
