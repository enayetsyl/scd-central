# _wip/STATE.md — question-banks (session-resumable state)

| Field | Value |
|---|---|
| Current build | **Import contract v1.1 folded in (`CD-143`) and the batch export is live.** পাঠ ১৩: 110 items, signed, four export artifacts in sync — array · `single/` · **`.batch.json`** — all carrying digest `e76631e34fa0`. Suite CLEAN across 24 gates. |
| Phase | Contract work done. **`CD-141` autonomy still NOT live** — the dry run is still owed. |
| Last completed step | `e26fcd0` tools (v1.1 vendored whole) · `11beca9` ruling (CD-143) · `0b0e478` build (`build_batch.py` + পাঠ ১৩ wrapper) · `bdd8ae3` gate (ENVELOPE-SYNC + policy) · this log. **Nothing pushed** — `origin/main` at `7aafd89`. |
| Next step | The Principal's `CD-141` dry run. **`_inbox/` still holds the three superseded v1.1 originals plus a redundant v1.0 `import-contract.md`** — the mount is pull-only for agents, so removing them is the Principal's (AGENTS §12.4/§12.5). |
| Blockers / open PENDING-P tags | **`PENDING-P-038` RAISED** (nothing checks a slot is admitted by ANY chapter). FLAGGED-not-OPEN. |
| Files in `_wip` awaiting "done" | this file · `U13_BLOOM_PROBE_2026-08-15.md` · `U13_ADMISSIBILITY_DRAFT_2026-08-15.md` · `BAN_C1-C4_REGISTER_BLOCKED_2026-08-15.md` · `U13_REVIEW_SHEET_2026-08-15.md` · `RULING_DRAFTS_teacher-lane_2026-08-15.md` |

## Contract v1.1 — the four things that bite

**`envelope_version` STAYS `"1.0"`.** The DOCUMENT is v1.1; the wire value is a `const`. Stamping
`"1.1"` fails validation. This is the easiest thing to get wrong from a description.

**The wrapper is EXACTLY FOUR KEYS** — `envelope_version`, `doc_type`, `batch`, `items`. The batch
branch sets `subject`, `class_level`, `address`, `curation_tag`, `pinned_to`, `provenance`, `tags`,
`review_status`, `rendered_markdown`, `payload` to **false**, and root `additionalProperties` is
**false**. Anything helpfully added is a failure.

**`digest` IS AN AUDIT FIELD, NOT AN INTEGRITY CHECK.** The contract says it is *"recorded on the
batch audit row; not recomputed at import"*. **A wrong digest is caught NOWHERE downstream** —
which is why `ENVELOPE-SYNC` checks it here. Do not build on the assumption the Hub would notice.

**`items` is the loosest gate in the contract, deliberately.** Its only structural bar is nesting;
everything else is left to the per-element pass **so one bad element fails alone**. That is why the
repo side needed no new validation: the single path is still the contract.

**Whole-batch rejects are exactly three, plus nesting:** `items` absent/empty · `item_count` ≠
`items.length` · >500 items.

## Two vendored files may NOT be edited, and one of them was asked for

`build_question_envelopes.py` is **vendored** (VENDOR.md, AGENTS §7, CD-003). The brief asked for
the batch emitter to live inside it; it cannot. **`build_batch.py` in `authoring/` is the join**,
exactly as `split_envelopes.py` was for the same reason. A local patch to a vendored file is
silently un-superseded the next time upstream ships.

## CD-141 in one screen — what an agent may do without asking

**Both tests must pass, not either.** CLASS ∈ {build, corrections, log, promotion} **AND** PATH
under `workstreams/question-banks/` or its `banks/envelopes/`. **AND** the full suite CLEAN
including `PLAN` and `ENVELOPE-SYNC`, **with `N/A` excluded from CLEAN** — `N/A` means the gate did
not judge, and an unjudged bank is what the row exists to keep out.

**Everything else stops and reports.** Never ask the teacher: they cannot rule (§2), and
`QB-CR-013` is the recorded instance of an agent reading an answer about mechanics as an answer
about substance.

**Never pre-approved:** a gate change · a policy edit · a decision row · an `_inbox/`
classification · anything on the mount · **a `git reset` or any history rewrite, pushed or not** ·
promotion to `gold` (a Hub act, CD-003).

**THE 40-ITEM MINIMUM IS RULED AT CD-141(g).** No bank under 40 items can pass `PLAN` —
`0.80n + 8 ≤ n`. **A thin chapter GROWS or COMBINES, ruled per case by the Principal.** The agent
**stops rather than padding**: items authored to satisfy a gate are exactly the near-duplicates §4
forbids, and `PLAN`'s own duplicate scan would then catch what the padding created.

**The autonomy rests on one ledger instance** — `QB-CR-013` — where §6 promotes a pattern at three.
Filed knowingly. **Dry run required before handover.**

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
