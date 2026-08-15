# _wip/STATE.md — question-banks (session-resumable state)

| Field | Value |
|---|---|
| Current build | **Teacher-lane foundations.** Agent work has moved OFF the mounted drive into a container clone (`tools/session_bootstrap.md`); the `PLAN` gate now holds the plan-table countersign; two ruling rows are DRAFTED and NOT filed. পাঠ ১৩ is unchanged — signed, 110 items, export in sync. |
| Phase | **Awaiting the Principal on two drafts.** Autonomy does not begin until CD-14x(a) is filed; until then every push needs explicit approval with a per-commit range check. |
| Last completed step | `649b37a` tools (session_bootstrap.md) · `78ccf4f` gate (PLAN + paired policy) · this log commit. Suite CLEAN across **24 gates**. **Nothing pushed** — `origin/main` at `a105125`. |
| Next step | The Principal reads `_wip/RULING_DRAFTS_teacher-lane_2026-08-15.md` and rules. After filing: the register's remaining columns — ENG · MATH · SCI/BGS — as DATA ROWS. |
| Blockers / open PENDING-P tags | **`PENDING-P-038` RAISED** (nothing checks a slot is admitted by ANY chapter; S14 at C5 Bangla is down to one). FLAGGED-not-OPEN. |
| Files in `_wip` awaiting "done" | this file · `U13_BLOOM_PROBE_2026-08-15.md` · `U13_ADMISSIBILITY_DRAFT_2026-08-15.md` · `BAN_C1-C4_REGISTER_BLOCKED_2026-08-15.md` · `U13_REVIEW_SHEET_2026-08-15.md` · `RULING_DRAFTS_teacher-lane_2026-08-15.md` |

## THE EXECUTION MODEL CHANGED — read `tools/session_bootstrap.md` before starting

**Work happens in a container clone, not on `C:\scd-central`.** The mount is the Principal's
pull-only working copy. Verified this session, and the verbatim probe is in the doc: no `*.lock`
lingers, `rm` inside `.git/` succeeds, and **`git reset --hard` WORKS**, where on the mount it fails
outright. **No lock-asides, no `.git/lock-debris/`, no `GIT_INDEX_FILE`.**

**Clone from the MOUNT, not from GitHub, and the reason is measured:** `.git` is 347 MB at ~0.2 MB/s
to GitHub — roughly 30 minutes, against a bash call capped far below that, and **a backgrounded
clone does not survive between calls.** A local clone takes **11 seconds**; `origin` is then
repointed at GitHub, where a fetch takes 1 second. Same history, different transport.

## `PLAN` — what it now decides, and the number it implies

It replaces the plan table the Principal used to countersign: Bloom margins ≥ 2, full per-slot
demand, task declarations, P-037 types, within-slot near-duplicate stems. **It deliberately
disagrees with BLOOM-BAND:** a POOL may sit exactly on a floor (CD-135); a bank offered as FINISHED
may not, because one re-tag reddens it.

**THE CONSEQUENCE A LATER SESSION WILL MEET: no bank under 40 items can pass PLAN.** Margin ≥ 2 on
four positive floors needs 0.80n + 8 ≤ n. পাঠ ১৩ at 110 is far clear; **a thin chapter must grow
before it can be signed at all.** That is arithmetic, not tagging, and the gate says so in one
failure rather than four.

**Near-duplicate thresholds are measured, not guessed** — the live 110 has zero exact duplicates and
a maximum of 0.905 at S12, so FAIL is 0.95 and 0.85–0.95 REPORTS for the Hub's subject expert.

## পাঠ ১৩ — the signed state

**110 items, digest `e76631e34fa0d204…`** over the `questions` array alone, sorted by qid, header
excluded. The exclusion is deliberate: adding the signature row does not move the digest, but
**any later item edit does, and the signature then no longer covers the bank.**

| level | count | % | floor | margin |
|---|--:|--:|--:|--:|
| Remember | 34 | 30.9% | 20% (22) | **+12** |
| Understand | 30 | 27.3% | 25% (28) | **+2** |
| Apply | 30 | 27.3% | 25% (28) | **+2** |
| Analyze | 14 | 12.7% | 10% (11) | **+3** |
| Evaluate | 2 | 1.8% | 0% | +2 |
| Create | 0 | 0.0% | 0% | content fact, CD-135(d) |

Slots: S01 1 · S02 7 · S03 16 · S04 5 · S05 8 · S06 7 · S07 21 · S08 15 · S09 1 · S10 10 ·
S11 8 · S12 5 · S13 6. Every one clears its CD-138(g) demand. S14/S15 excluded with content
reasons.

**Two things a later session must not re-derive:**

- **A countersigned plan table can hide a term in its own arithmetic.** The plan read
  `S07 = R6 · U15 · A1`, and Q34 WAS that `A1`. Its retirement was ruled *after* the table was
  signed and the Apply margin silently fell to +1. **Recompute after every ruling, not once per
  plan.**
- **A content limit is a claim about how far the book was read.** Wave 3 called S06 · S12 · S13
  content-limited at three; the poem carries five distinct যুক্তবর্ণ, seven clean opposites and six
  এক কথায় প্রকাশ mappings. Withdrawn in the open, in the bank header.

**FIVE Remember items are left unextracted on the Principal's HOLD** — S02 +2 (ফেরেস্তা · বকুল),
S04 +3 — and are NAMED in `header.gaps`. They raise the pool without raising `Apply`, and every
Apply-bearing slot is at its content limit. **Taking them now would break the signature's hash**,
which is the mechanism working.

## The export, and the gate that now guards it

`banks/envelopes/` sat at **36 — the wave-1/2 surface — while the bank held 88 and then 110. Two
waves.** Nothing saw it, because **every gate in the suite reads the BANK and §11 imports the
ENVELOPES.** It would have carried ten `S10 ভাব নির্ণয়` items into the Hub *past COVERAGE*, the
gate built for that exact defect.

Regenerated via the standing §11 flow; **seven orphans deleted** (`Q20`–`Q24`, `Q34`, `Q35`) —
build and split only WRITE, so a retired item's envelope survives in a directory nobody prunes.
**A stale addition is loud; a stale survival is silent, and the silent one reaches the Hub.**

**`ENVELOPE-SYNC` is the suite's 23rd gate.** Set · content · array-vs-single, seeded both ways,
quiet on a healthy export. It shares `bank_content_digest()` with the signature row, so *what the
Principal signed* and *what the Hub receives* are the same quantity rather than two descriptions
that sound alike.

**Environment note for the next run:** the sandbox's vendored `jsonschema` predates
`Draft202012Validator` and `validate_import.py` cannot import it. `pip install --break-system-packages
'jsonschema>=4.18'` first. The first harness run returned 110 failures on that import alone — none
of them about content.

## Carried forward, unchanged

- **PENDING-P-008 (FLAGGED)** — REF-19 has no Bangla punctuation slug; S11's বিরামচিহ্ন items ride
  `BAN-SENTENCE`, the established choice and still not a punctuation slug.
- **UP-002** `pool` field · **UP-003** `ref19_topic_id` rejects `MATH-*-REL`, blocking every C5
  Math bank.
- **C4 S11's declaration is OPEN on the Principal's ruling** — the register keeps
  `selected: বিরামচিহ্ন বসানো` with its RAISED note that C4 is the first class where প্রশ্ন তৈরি
  may be set at all.
- **No gate reads a spine file.** The spine parse lives at build time in
  `tools/audits/slot_register_check.py`. Both halves of CD-138(b) stay seeded.
