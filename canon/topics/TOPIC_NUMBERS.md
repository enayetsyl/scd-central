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

**SEED — Class 5 Bangla only.** Every other class × subject is unwritten. `PENDING-P-008` stays
**FLAGGED**; its close condition is **"chart complete for all subjects"**, and completion means
rows here, not a ruling elsewhere.

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

**Unassigned in this class:** `-03`, `-04`, `-08`, `-10`, `-14`+. `-10` is described as a
*functional-writing ladder* in `workstreams/lesson-plans/governance/PROJECT03_TODO.md`, but that is a
P03 usage note and not a P04 attestation, so it is **deliberately not given a row here** until it is
attested or ruled. Not-yet-listed is the correct state; a guess would not be.

### Why `-13` was minted rather than folded into `-02`

Principal ruling, 2026-08-09: **`MarkLogic_BAN_Spine.md` keeps `S03 বাক্য গঠন` and `S11 বিরামচিহ্ন`
as separate mark slots at C5.** Folding punctuation into `-02` (বাক্য-রচনা) would erase a distinction
canon makes about what is being assessed. `-13` was free in the attested set.

**How the error that led here happened, recorded so it is not repeated:** `-11` was read off the
spine slot number **S11 = বিরামচিহ্ন**. The S-slot scheme and the `TOP-` scheme are unrelated and
collide at 11 by coincidence. **A number inferred from a same-numbered field in a different scheme
is an unverified value and must be queued like any other** (QB-CR-008).

### Contested rows — `-06` and `-09`

The P04 register's own flags table carries an unresolved item: **the U14 (কুপোকাত) Drama→Story
re-home is pending a Principal ruling.** `REF-03 §4.5/§5.5` maps U14 to Drama `-09`; D-PROJ04-003
tagged the bank Story `-06` and flagged the mismatch. Both numbers are recorded above because both
are attested; **which one U14 carries is not settled here and is not settled by this file.** If the
re-home is confirmed, REF-03 owes a supersede at Project 00 — never an edit in place.

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
