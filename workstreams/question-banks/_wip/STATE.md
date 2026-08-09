# _wip/STATE.md — question-banks (session-resumable state)

| Field | Value |
|---|---|
| Current build | C5 BAN পাঠ ২১ wave 1 — **back in `_wip/`** (de-promoted by a red gate, QB-D-010) |
| Phase | Blocked on one Principal ruling. Wave 2 not started. |
| Last completed step | REF-19 v1.10 and the P04 register imported and verified (**CD-043**); **PENDING-P-005 CLOSED — `TOP-BAN-C5-02` CONFIRMED**; a mis-tag exposed by the same import (**PENDING-P-007**) turned FLAG-TRACE red, and wave 1 was returned to `_wip/` per AGENTS.md §5 |
| Next step | **Principal rules PENDING-P-007** (which `TOP-` number a বিরামচিহ্ন item carries). Then: retag Q52 → regenerate → gate chain → re-promote. One edit, one run. |
| Blockers / open PENDING-P tags | **PENDING-P-007 — OPEN, Principal-owed, BLOCKING** (AGENTS.md §6: no promotion or print while open). **PENDING-P-008 — FLAGGED, non-blocking.** |
| Files in `_wip` awaiting "done" | `C5_BAN_U21_QuestionBank_v1.json` · `envelopes/` (regenerated). The authoring script stays in `authoring/` — it is tooling, not the gated artifact. |

## What changed this round

**PENDING-P-005 is CLOSED, verified at source, PASS on all four conditions** (CD-043; evidence
`reports/P005_VERIFICATION_2026-08-09.txt`):

- REF-19 v1.10 imported to `canon/topics/`, read-only. It contains **zero `TOP-` strings** and
  **no topic id with a numeric suffix** — 121 slugs, reconciling **exactly** with the vendored
  harness constant, zero diff either way. That is the CD-011 reconciliation done in the right
  direction: artifact first, derived copy checked against it.
- `PROJECT04_DECISIONS.md` imported to `references/`, read-only, cited never continued. 16 rows,
  continuous. **Every `D-PROJ04-###` citation in this repo now resolves** — QB-CR-007 closes.
- `D-PROJ04-011` attests *"`TOP-BAN-C5-02` বাক্য-রচনা (29)"*; `D-PROJ04-003` carries `-02` for U14.
  **The 8 S03 items are correctly tagged.**

## What the import cost us, and why that is a good trade

Having the register made **all four** of the bank's tags checkable for the first time. Three were
right. One was not:

| Tag | Items | Attested meaning | Verdict |
|---|--:|---|---|
| `TOP-BAN-C5-01` | 6 | শব্দার্থ | correct |
| `TOP-BAN-C5-02` | 8 | বাক্য-রচনা | correct — this was P-005 |
| `TOP-BAN-C5-07` | 42 | `BAN-INFOTEXT` | correct |
| `TOP-BAN-C5-11` | 1 | **মূল্যবোধ / মুক্ত-চিন্তা** | **WRONG** — `QP-BAN-C5-U21-Q52` is the বিরামচিহ্ন item |

I read `-11` off the MarkLogic spine slot **S11 = বিরামচিহ্ন**. The S-slot numbers and the `TOP-`
topic numbers are unrelated schemes that collide at 11 by coincidence. **No number is attested for
punctuation anywhere in the register**, so nothing was substituted — the tag still reads `-11` and
must not be exported.

**Standing lesson (QB-CR-008): a tag inferred from a same-numbered field in a different scheme must
be queued like any other unverified value.** One such inference was queued (`-02`) and survived
scrutiny; the other was not queued, and did not.

## Two gate findings from this round

1. **FLAG-TRACE passed the bank before it failed it.** It tested for the literal `**OPEN**`, and
   the queue row reads `**OPEN — Principal-owed.**`. The gate written to catch exactly this case
   sailed past it. Fixed to read the status cell and match the word; a seeded case now exercises a
   **real OPEN row**. The two original cases covered only a nonexistent tag and a missing field —
   which is precisely why the hole survived. Selftest 25 → **26** seeded errors.
2. **The red gate then did its job**, and wave 1 went back to `_wip/`. Promotion means ready for
   the Hub; a bank carrying a tag the register contradicts is not ready for the Hub.

## Recommendation on PENDING-P-007

**Mint `TOP-BAN-C5-13` for বিরামচিহ্ন / যতিচিহ্ন.** The C5 spine keeps `S03 বাক্য গঠন` and
`S11 বিরামচিহ্ন` as **separate mark slots**, so folding punctuation into `-02` (বাক্য-রচনা) would
erase a distinction canon makes. `-13` is unused in the register's attested set
(01, 02, 05, 06, 07, 09, 11, 12).

## Wave 2 — where to start (unchanged, not started)

HW 70 · AS 35 · CT 18 owed. Verified absent from wave 1: শান্তি ও সাম্যের বাণী · the ভাষণ's opening
আল্লাহর প্রশংসা as a comprehension item · অনুশীলনী ২ (ঠিকমতো উচ্চারণ, 8 words) · অনুশীলনী ৫
(প্রয়োজনীয় শব্দ বসিয়ে বাক্য পূর্ণ) · the remaining emphasis points as S07 items. Wave 2 must
re-check ZERO-OVERLAP against wave 1, not a blank slate.

## Open, carried forward

- **PENDING-P-008 (FLAGGED)** — the authoritative `##` chart owed to REF-07 §3.5 is still not a
  file. Interim authority = REF-19 slugs + the P04 register's attested numbering. The register
  carries the same caveat in its own rows.
- **UP-002** — the LOCKED payload has no `pool` field; pool membership stays in `pool_index`.
- **The gate suite measures structure, not truth** (QB-D-008, CD-041). It cannot tell you an answer
  is wrong. The Principal's read of the bank is what closes that.
