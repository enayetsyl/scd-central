# _wip/STATE.md — question-banks (session-resumable state)

| Field | Value |
|---|---|
| Current build | **পাঠ ১৩ is CLOSED, SIGNED and EXPORTED.** 110 items, suite CLEAN across 23 gates; the Subject Lead pass given 2026-08-15 and pinned to a content hash; `banks/envelopes/` regenerated to match and all 110 `PASS (0 warn, 0 advisory) — importable`. |
| Phase | **REVIEWED and EXPORT-READY.** `reviewed → gold` remains OUTSTANDING and **is not a Git act** — it is the Principal's, in the Hub (CD-003, LOCAL.md *Operator workflow*). Nothing in this repo moves a bank to gold and no field here claims to. |
| Last completed step | Seven commits pushed `4ec7b6f..388cf2e`. Then, unpushed and awaiting per-commit approval: `0ea6685` log (review sheet) · **a premature promotion commit, DROPPED by reset — see QB-CR-013** · `ab75f1e` promotion (signature) · `1b6cbaf` build (envelopes) · `3295989` gate (ENVELOPE-SYNC) · `488b805` corrections (QB-CR-013) · this log commit. |
| Next step | Nothing is owed on পাঠ ১৩. The register's remaining columns — **ENG · MATH · SCI/BGS** — are next, added as **DATA ROWS**. The C1–C5 shape now carries D5 and D6; **if a new subject needs a code change, the shape is wrong.** |
| Blockers / open PENDING-P tags | **`PENDING-P-038` RAISED** — nothing checks that a slot is admitted by ANY chapter, and S14 at C5 Bangla is down to one (পাঠ ৪). FLAGGED-not-OPEN, so it does not bar promotion (LOCAL.md); the bank's own `flags` block is empty. |
| Files in `_wip` awaiting "done" | this file · `U13_BLOOM_PROBE_2026-08-15.md` · `U13_ADMISSIBILITY_DRAFT_2026-08-15.md` · `BAN_C1-C4_REGISTER_BLOCKED_2026-08-15.md` · `U13_REVIEW_SHEET_2026-08-15.md` |

## The one thing a later session must read before anything else — QB-CR-013

**An agent recorded a Principal act before it occurred.** The Principal said *"approve"* to a
read-only task; the word was ambiguous; the agent asked via a multiple-choice question and got
back *"Both, in two commits"* — **an answer about WHERE the signature should go, which the agent
read as WHETHER it had been given.** A signature row went into the bank saying *"PASSED"* with no
verdict from the Principal in it. His actual words arrived one message later.

**No gate caught it and none could.** The suite was CLEAN throughout, correctly — nothing
structural was wrong. **The Principal caught it by stating an expected HEAD in his next brief**,
the agent verified, found the mismatch and stopped. Nothing was pushed, so the cost was one local
commit, dropped by reset.

**The rule it mints: a signature row quotes the signer.** A row that cannot quote its signer is
not a signature; it is the agent's summary of one, and no artifact may carry it.

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
