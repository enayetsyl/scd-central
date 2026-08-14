# TOPIC_NUMBERS.md — the `TOP-<SUBJ>-C<n>-##` chart

*Canon. Seeded 2026-08-09 by Principal ruling (**CD-044**). This is the file **PENDING-P-008** owes,
and the place its completion happens.*

## What this file is for

`canon/topics/LOCKED_REF-19_…v1_10.md` settles the topic **slugs** (`BAN-POEM`, `BAN-INFOTEXT`, …)
and settles **no numbers** — verified at import: it contains zero `TOP-` strings and no topic id
carries a numeric suffix (CD-043). The `##` numbers are a separate scheme owed to **REF-07 §3.5**,
which has never been authored. Until it is, the numbering lived only as usage scattered through the
Project-04 register, where nothing could check it — and a wrong number survived a full gate chain
and a promotion because of that (QB-CR-008, PENDING-P-007).

So the chart starts here, seeded from what is actually attested, and grows.

**The rule this file makes executable: a number not listed here is not used. It is queued.**
`workstreams/question-banks/audits/gates.py` reads this file — the **TOPIC-NUMBER** gate fails any
bank carrying a `topic_tag` with no row below.

## Status

**Class 5 Bangla — COMPLETE as of 2026-08-14.** All eleven extracted পাঠ (১৩–২৩) resolve to a
charted number; the two gaps found on audit were minted the same day (see the mint note below).
**`PENDING-P-008` is closed for C5 Bangla and remains FLAGGED overall** — every other class ×
subject is still unwritten, and its close condition is **"chart complete for all subjects"**, which
happens as rows here, not as a ruling elsewhere.

### C5 Bangla coverage — পাঠ ১৩–২৩, verified at source 2026-08-14

Read against `canon/marklogic/C5_Bangla_Source_13-23.md`'s own ধরন column and REF-19's C5 Bangla row
assignments. **A chapter may source items under several tags; the tag below is the one its genre
makes primary.**

| পাঠ | ধরন | primary `TOP-BAN-C5-##` |
|---|---|---|
| ১৩ পাখির মতো · ১৫ সংকল্প · ১৮ ইচ্ছামতী · ২০ শিক্ষাগুরুর মর্যাদা | কবিতা | `-05` |
| ১৪ কুপোকাত | নাটক | **`-09`** (Drama — ruled 2026-08-14, see QB-CR-009) |
| ১৬ স্মরণীয় যাঁরা বরণীয় যাঁরা | গদ্য (ইতিহাস/জীবনী) | **`-14`** *(minted)* |
| ১৭ · ২১ · ২২ | গদ্য (তথ্যমূলক / সিরাত / ইতিহাস) | `-07` |
| ১৯ ভাষার খেলা | ব্যাকরণ-অনুশীলন | `-02` **and** **`-15`** *(minted)* |
| ২৩ পোস্টার লিখি, প্ল্যাকার্ড লিখি | গদ্য (প্রায়োগিক) | **`-15`** *(minted)* |

Cross-cutting strands apply throughout and are not chapter-bound: `-01` শব্দার্থ · `-02` বাক্য-রচনা ·
`-11` / `-12` PROTECTED rubric-only · `-13` বিরামচিহ্ন (attested on পাঠ ২১).

## Class 5 · Bangla (BAN)

Every row is either attested in `workstreams/question-banks/references/PROJECT04_DECISIONS.md`
(read-only, cited never continued) or minted by a CD row. Nothing here is inferred.

| Tag | Meaning | REF-19 slug | Attestation |
|---|---|---|---|
| `TOP-BAN-C5-01` | শব্দার্থ | `BAN-VOCAB` | D-PROJ04-011 — *"`TOP-BAN-C5-01` শব্দার্থ (21)"*; also D-PROJ04-003 (U14, U15) |
| `TOP-BAN-C5-02` | বাক্য-রচনা | `BAN-SENTENCE` | D-PROJ04-011 — *"`TOP-BAN-C5-02` বাক্য-রচনা (29)"*; also D-PROJ04-003 (U14) |
| `TOP-BAN-C5-05` | কবিতা / মূলভাব | `BAN-POEM` | D-PROJ04-012 — *"same single topic `TOP-BAN-C5-05` / `BAN-POEM`"*; also D-PROJ04-003, -011 |
| `TOP-BAN-C5-06` | গল্প (Story) | `BAN-STORY` | D-PROJ04-003 (U14) — **contested, see the note below** |
| `TOP-BAN-C5-07` | তথ্যমূলক গদ্য | `BAN-INFOTEXT` | D-PROJ04-010 — *"U17 (100, `TOP-BAN-C5-07`/`BAN-INFOTEXT`)"* |
| `TOP-BAN-C5-09` | নাটিকা (Drama) | `BAN-DRAMA` | D-PROJ04-003 — **contested, see the note below** |
| `TOP-BAN-C5-11` | মূল্যবোধ / মুক্ত-চিন্তা | — | D-PROJ04-011 — *"`TOP-BAN-C5-11` মূল্যবোধ/মুক্ত-চিন্তা (11)"*; D-PROJ04-003 marks it a PROTECTED, rubric-only strand |
| `TOP-BAN-C5-12` | PROTECTED strand (rubric-only) | — | D-PROJ04-003 — *"PROTECTED strands TOP-11/TOP-12 rubric-only"* |
| **`TOP-BAN-C5-13`** | **বিরামচিহ্ন / যতিচিহ্ন** | *(none — see §REF-19 gap)* | **MINTED 2026-08-09, CD-044** (PENDING-P-007 ruled) |
| **`TOP-BAN-C5-14`** | **জীবনী (Biography)** | `BAN-BIOGRAPHY` | **MINTED 2026-08-14**, unification session 1 closing ruling (4) |
| **`TOP-BAN-C5-15`** | **ব্যবহারিক লিখন (Functional writing)** | `BAN-FUNCWRITE` | **MINTED 2026-08-14**, unification session 1 closing ruling (4) |

**Unassigned in this class:** `-03`, `-04`, `-08`, `-10`, `-16`+.

**`-10` stays unassigned deliberately, and the two mints above did not take it.** It is described as
a *functional-writing ladder* in `workstreams/lesson-plans/governance/PROJECT03_TODO.md`, which is a
**P03 usage note, not a P04 attestation**. Adopting `-10` for `BAN-FUNCWRITE` on that basis would be
the QB-CR-008 error again — a number inferred from a same-named field in a different scheme. **The
Principal ruled fresh numbers instead**, so `-15` was minted and `-10` remains queued.

### The two mints of 2026-08-14 — and the premise they corrected

Minted to close the C5 Bangla coverage gap found while auditing পাঠ ১৩–২৩ against this chart: পাঠ ১৬
(জীবনী), পাঠ ১৯ and পাঠ ২৩ (ব্যবহারিক লিখন) had no number, so items sourced from them could not
carry a valid `topic_tag` and the TOPIC-NUMBER gate would have failed any bank built on them.

**Three chapters, two numbers — because `topic_tag` is a per-QUESTION field and this chart maps
TOPICS, not chapters.** The agent's audit asked whether পাঠ ১৯ should "own a number or reuse `-02`",
and the Principal ruled the question malformed: **a chapter carries no number; its items do, and one
chapter sources items carrying different tags.** পাঠ ১৯ (ভাষার খেলা) accordingly yields **both** —
its বাক্য গঠন items carry `-02`, its functional-writing items carry `-15`. Recorded because the
either/or framing would have forced a false choice and lost half the chapter's items.

### Why `-13` was minted rather than folded into `-02`

Principal ruling, 2026-08-09: **`MarkLogic_BAN_Spine.md` keeps `S03 বাক্য গঠন` and `S11 বিরামচিহ্ন`
as separate mark slots at C5.** Folding punctuation into `-02` (বাক্য-রচনা) would erase a distinction
canon makes about what is being assessed. `-13` was free in the attested set.

**How the error that led here happened, recorded so it is not repeated:** `-11` was read off the
spine slot number **S11 = বিরামচিহ্ন**. The S-slot scheme and the `TOP-` scheme are unrelated and
collide at 11 by coincidence. **A number inferred from a same-numbered field in a different scheme
is an unverified value and must be queued like any other** (QB-CR-008).

### Contested rows — `-06` and `-09` — **RULED 2026-08-14: U14 is Drama `-09`**

**Settled.** `REF-03 §4.5/§5.5` maps U14 (কুপোকাত) to Drama `-09`; D-PROJ04-003 tagged the bank
Story `-06` and flagged the mismatch. **The REF wins on the authority chain** — REF-03 is a
Project-00 subject-spine playbook, D-PROJ04-003 is a workstream-local bank tag — **and the source
agrees**: `canon/marklogic/C5_Bangla_Source_13-23.md`'s এক নজরে table gives পাঠ ১৪'s ধরন as **নাটক**,
and REF-19's C5 Bangla row reads `BAN-DRAMA` — *নাটিকা U14*.

**No REF-03 supersede is owed.** The Drama→Story re-home was **rejected**, not confirmed; REF-03
already says what the ruling says.

**`-06` (গল্প / Story) keeps its row** — it is attested and correct for the chapters that really are
stories (REF-19 C5: U06, U09, U12). What changed is that **U14 is not one of them**.

**The existing `-06` tags on U14 bank items are NOT re-tagged in place.** They take a dated,
append-only correction row — `QB-CR-009` in `workstreams/question-banks/CORRECTIONS.md`. A silent
re-tag would erase the evidence that the bank was ever wrong, which is what an append-only ledger
exists to prevent.

## REF-19 slug gap (P-008 sub-item)

**REF-19 v1.10 carries no Bangla punctuation topic.** Its 24 BAN slugs include `BAN-SENTENCE`,
`BAN-WORDBUILD`, `BAN-CONJUNCT`, `BAN-MATRA` and so on, but nothing for বিরামচিহ্ন/যতিচিহ্ন. So
`-13` has a number and no slug of its own.

**REF-19 is not touched.** It is a LOCKED Project-00 artifact, read-only and supersede-only here
(CD-043); a slug is added by a **REF-19 supersede authored at Project 00**, which is owed and is
recorded as a sub-item of PENDING-P-008.

**Meanwhile:** a punctuation item keeps a valid existing slug for `ref19_topic_id` — the harness
hard-validates that field against the REF-19 registry and would reject a minted one — and carries
`TOP-BAN-C5-13` as its `topic_tag`. In the পাঠ ২১ bank, `QP-BAN-C5-U21-Q52` keeps
`ref19_topic_id: BAN-SENTENCE` and its `topic_tag` changed to `-13`. The two fields are different
axes and it is correct for them to disagree in granularity here.

## Growing this file

One row per number, per class × subject. Every row names its attestation — a `D-PROJ04-###` row, a
CD row, or the REF-07 §3.5 chart once it exists. **No row without one.** When REF-07 §3.5 is
authored, it supersedes this file and PENDING-P-008 closes; until then this file *is* the chart, for
the subset it covers.
