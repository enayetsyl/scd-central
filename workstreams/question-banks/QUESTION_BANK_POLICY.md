# QUESTION_BANK_POLICY — v1.0

*Workstream: question-banks (P04). Adopted by Principal ruling 2026-08-09 (QB-D-001…QB-D-004),
superseding the v0.1 draft staged in `_inbox/`.*
*Authority: `canon/marklogic/` (marks and structure) + `canon/sources/SOURCE_POLICY.md` (content)
+ the LOCKED Hub import contract v1.0, vendored at `tools/hub-export/` (format).*

## 1. Purpose

Per chapter, per class × subject: tagged question pools authored **born-conformant** to the
Hub's LOCKED import contract, delivered to teachers through the Hub.

## 2. The three pools — the founding decision (QB-D-001)

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

Every question carries, in its LOCKED payload: `bloom_level` · `difficulty` · `topic_tag`
(`TOP-*`, the cross-repo join key) · `ref19_topic_id` · `paper_role` · `marks`. The scholarship
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

- **Content ONLY from the chapter's source extraction** (`canon/sources/SOURCE_POLICY.md`).
  No extraction → no bank for that chapter; the gap is **recorded, not filled from memory**.
- **Marks per question ONLY from MarkLogic values.** Annual-slot per-item marks are carried
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
3. `workstreams/question-banks/audits/gates.py`: zero-overlap across the chapter's three pools ·
   domain-ratio per pool · mark-value check against MarkLogic · source-traceability · AS
   difficulty mix · sizing-ceiling report · script guard.
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
