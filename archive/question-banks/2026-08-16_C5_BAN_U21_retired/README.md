# পাঠ ২১ (বিদায় হজের ভাষণ) — bank RETIRED WHOLE, 2026-08-16

**Authority: `CD-148` (Principal ruling 2026-08-16). Read that row before reading anything here.**

This directory is **archived provenance, not current authority.** Nothing in it is cited as a
current source, and no agent restores from it. It exists because supersede-with-archive
(AGENTS.md §7, master §5.3) retires whole and **never deletes**.

## What is here

| Path | What it was |
|---|---|
| `C5_BAN_U21_QuestionBank_v1.json` | the 57-item bank, old `qb` shape, source of record until this date |
| `author_U21_wave1.py` | its authoring script — **archived unedited** (`QB-CR-014(g)`: editing it would make the record say the wave got it right) |
| `envelopes/C5_BAN_U21_QuestionBank_v1.envelopes.json` | the exported array |
| `envelopes/single/` | 57 per-item envelopes |
| `reports/` | the four 2026-08-09 gate reports, including the promote/depromote pair |

## Why it was discarded rather than migrated

Measured at HEAD on 2026-08-16 by running the suite, not asserted:

- **`PLAN`, `COVERAGE`, `BLOOM-BAND` and `ENVELOPE-SYNC` all return `N/A`** on this shape — the
  four gates that decide whether a bank is signable never judged it.
- `bloom_level` over its 57 items: **Remember 23 · Understand 17 · Apply 14 · Evaluate 2 ·
  Create 1 · Analyze 0.** **Analyze is zero**; PLAN's floor at 57 items needs 6 and the margin
  rule needs 8.
- **Size was never the problem.** 57 clears CD-141(g)'s `n >= 40` with room. The tagging and the
  authoring are what fail, and both predate CD-134, CD-135, CD-136, CD-138 and CD-142 — every one
  of which changed what a correct item looks like.

A shape migration would have produced a bank that passes **because it was reshaped to, not because
it was authored right**, and nothing downstream could tell those apart.

## Why the envelopes are in here and not in `banks/envelopes/`

So that `ENVELOPE-SYNC` cannot resolve them and **no export path can serve a retired item.** This
is that gate's own recorded lesson applied before it fires: *a stale ADDITION is loud, a stale
SURVIVAL is silent, and the silent one is the one that reaches the Hub.*

## Hub side — the Principal's, and the repo cannot tell whether it is owed

Items reach SCD Hub only by an upload the Principal performs (CD-003). **Nothing in this repo
records whether the U21 array was ever uploaded**, so no agent may assume either way. If it was,
retiring those items in the Hub is his act, not a Git one.

## What replaces it

U21 is **regenerated from scratch** through the current pipeline — declaration → `PLAN` →
authoring → suite — as a future teacher-lane session under CD-141. It is not restored from here.

Two things the regenerated bank inherits as **conclusions, not as items**:

- পাঠ ২১ is `KEEP-AS-IS` সিরাত content (the extraction's own marking, *কিছুই বদলানো যাবে না*).
  `QB-CR-005` stands: the ভাষণ text is the KEEP-AS-IS obligation; a personal name in an অনুশীলনী
  is not, and is replaced from the REF-2 C5 pool.
- `QB-CR-008`'s ruling that বিরামচিহ্ন carries `TOP-BAN-C5-13`. Q52 in the archived bank is the
  item that correction was written about.
