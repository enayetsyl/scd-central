# _wip/STATE.md — question-banks (session-resumable state)

| Field | Value |
|---|---|
| Current build | none — C5 BAN পাঠ ২১ wave 1 is **PROMOTED and final** in `banks/` |
| Phase | Wave 1 closed. **Wave 2 does not start until production step ④** (CD-045). |
| Last completed step | PENDING-P-007 ruled (**CD-044**): `TOP-BAN-C5-13` minted for বিরামচিহ্ন, chart seeded as canon, Q52 retagged, new **TOPIC-NUMBER** gate. Full chain re-run: **15 gates CLEAN** after a **27-error seeded selftest + 1 negative case**, **57/57 envelopes PASS** L1–L4 (0 warn / 0 advisory), `canon_check` CLEAN, `tools_check` CLEAN. Report: `reports/BAN_U21_GATES_2026-08-09-final.txt` (314 lines, unelided) |
| Next step | **Nothing in this workstream.** Production sequence CD-045 puts NCTB source extraction first. |
| Blockers / open PENDING-P tags | **none OPEN.** One **FLAGGED**, non-blocking: `⚑ PENDING-P-008`, carried in the promoted bank's `flags` block. |
| Files in `_wip` awaiting "done" | none — this file only |

## Production sequence — this workstream is step ④ (CD-045)

**① NCTB sources to per-chapter markdown → ② C5 model papers and CTs, remaining subjects →
③ C1–C4 → ④ question pools.**

**পাঠ ২১ wave 2 waits for step ④.** The wave-2 targets below are recorded so they are not
re-derived, **not** so the next session starts them. The pilot existed to prove the step-④
machinery before step ④ arrives.

## Wave 1 as promoted — final

57 items · HW 30 · AS 15 · CT 12 · 105 marks. CEILING reports **HW 70 · AS 35 · CT 18 owed**.

| | জ্ঞান | অনুধাবন | প্রয়োগ | উচ্চতর | verdict |
|---|--:|--:|--:|--:|---|
| HW (৩৯) | ৩০.৮% | ৩৩.৩% | ২৩.১% | ১২.৮% | enforced, PASS |
| AS (৩৬) | ৩০.৬% | ৩০.৬% | ২৫.০% | ১৩.৯% | enforced, PASS |
| CT (৩০) | ২৬.৭% | ৩৬.৭% | ২০.০% | ১৬.৭% | reported, not enforced (QB-D-006) |
| chapter total (১০৫) | ২৯.৫% | ৩৩.৩% | ২২.৯% | ১৪.৩% | enforced, PASS |

**Topic tags, all now charted and gate-checked** against `canon/topics/TOPIC_NUMBERS.md`:
`-07` তথ্যমূলক গদ্য (42) · `-02` বাক্য-রচনা (8) · `-01` শব্দার্থ (6) · **`-13` বিরামচিহ্ন (1, minted CD-044)**.

`QP-BAN-C5-U21-Q52` keeps `ref19_topic_id: BAN-SENTENCE` — REF-19 v1.10 carries no Bangla
punctuation slug, and the harness hard-validates that field against the REF-19 registry. `topic_tag`
and `ref19_topic_id` are different axes and it is correct for them to disagree in granularity here.

## What this round cost, and what it bought

Three defects surfaced, each caught by something other than the thing that should have caught it:

1. **`-11` was wrong** and survived a full chain and a promotion, because until the P04 register
   arrived there was nothing to check a number against. Now there is: **TOPIC-NUMBER**.
2. **FLAG-TRACE passed the bank before it failed it** — it matched the literal `**OPEN**` while the
   row read `**OPEN — Principal-owed.**`. Fixed, plus a case exercising a real OPEN path.
3. **That new case then went red on the next run** — because it named `PENDING-P-007`, which had
   just been ruled. The fixture *was the live world*. Now the selftest injects a synthetic queue,
   and a **negative case** proves FLAG-TRACE stays quiet on a FLAGGED row: a gate that fires on
   everything is as useless as one that fires on nothing.

Selftest 14 → **27 seeded errors + 1 negative case**. Gates 11 → **15**.

## Wave 2 — recorded, NOT to be started (step ④)

HW 70 · AS 35 · CT 18 owed. Verified absent from wave 1: শান্তি ও সাম্যের বাণী · the ভাষণ's opening
আল্লাহর প্রশংসা as a comprehension item · অনুশীলনী ২ (ঠিকমতো উচ্চারণ, 8 words) · অনুশীলনী ৫
(প্রয়োজনীয় শব্দ বসিয়ে বাক্য পূর্ণ) · the remaining emphasis points as S07 items. Wave 2 must
re-check ZERO-OVERLAP against the promoted wave 1, not a blank slate.

## Open, carried forward

- **PENDING-P-008 (FLAGGED)** — `canon/topics/TOPIC_NUMBERS.md` is a **C5-Bangla seed**; close
  condition is *chart complete for all subjects*, and completion happens in that file. **Sub-item:**
  REF-19 v1.10 has no Bangla punctuation slug, so `-13` has a number and no slug — owed as a
  **REF-19 supersede authored at Project 00**. REF-19 is LOCKED here and never edited.
- **Two contested numbers, recorded not resolved:** the P04 register's own flags table carries an
  unruled **U14 Drama→Story re-home** — REF-03 maps U14 to `-09`, D-PROJ04-003 tagged it `-06`.
  Both are attested; which one U14 carries is not settled.
- **UP-002** — the LOCKED payload has no `pool` field; pool membership stays in `pool_index`.
- **The gate suite measures structure, not truth** (QB-D-008, CD-041). It cannot tell you an answer
  is wrong.
