# _wip/STATE.md — question-banks (session-resumable state)

| Field | Value |
|---|---|
| Current build | **none in `_wip/`** — C5 BAN পাঠ ২১ wave 1 is PROMOTED |
| Phase | Wave 1 closed. Wave 2 not started (Principal instruction: not this session) |
| Last completed step | Wave 1 promoted out of `_wip/` on the Principal's explicit "done" (**QB-D-009**): bank → `banks/`, envelopes → `banks/envelopes/`, authoring script → `authoring/`. Full gate chain re-run **post-promotion**: 15 gates CLEAN after a **25-error seeded selftest**; 57/57 envelopes PASS `validate_import.py` L1–L4, 0 warn / 0 advisory; `canon_check.py` and `tools_check.py` CLEAN. Report: `reports/BAN_U21_GATES_2026-08-09-promoted.txt` (unelided) |
| Next step | **Wave 2** for পাঠ ২১ — HW 70 · AS 35 · CT 18 owed to ceiling. Targets are named below. Not started by instruction. |
| Blockers / open PENDING-P tags | **none OPEN.** One **FLAGGED** (file-owed, non-blocking): `⚑ PENDING-P-005`, carried in the promoted bank's own `flags` block and checked by the FLAG-TRACE gate. |
| Files in `_wip` awaiting "done" | none — this file only |

## Queue state (CD-042)

| Tag | Status | Effect |
|---|---|---|
| PENDING-P-005 | **FLAGGED — file-owed** | `TOP-BAN-C5-02` on the 8 S03 items is a **stated default, not confirmed**. The Principal will stage the revision chart defining the `TOP-BAN-C5` numbers into `_inbox/`. **Do not change the tag** on any agent's judgement. **Does not block** wave-2 authoring or any promotion. Closes **only on verification at source**. |
| PENDING-P-006 | **CLOSED → CD-042** | The accepted Ch21 CT stays untouched; **আসিফ is grandfathered in that one historical paper only**. Every new item uses a **REF-2 C5-pool** name; **সাবিত** in the bank is confirmed correct. Authoring rule that follows: an NCTB exercise's personal name is replaced from REF-2 while the exercise's structure is kept — the name is not part of the KEEP-AS-IS obligation, the text of the ভাষণ is. |

## Wave 1 as promoted

57 items · HW 30 · AS 15 · CT 12 · 105 marks. CEILING gate reports **HW 70 · AS 35 · CT 18 owed**.

| | জ্ঞান | অনুধাবন | প্রয়োগ | উচ্চতর | verdict |
|---|--:|--:|--:|--:|---|
| HW (৩৯ নম্বর) | ৩০.৮% | ৩৩.৩% | ২৩.১% | ১২.৮% | enforced, PASS |
| AS (৩৬ নম্বর) | ৩০.৬% | ৩০.৬% | ২৫.০% | ১৩.৯% | enforced, PASS |
| CT (৩০ নম্বর) | ২৬.৭% | ৩৬.৭% | ২০.০% | ১৬.৭% | **reported, not enforced** (QuestionPolicy §৬ rule ৩, QB-D-006) |
| chapter total (১০৫ নম্বর) | ২৯.৫% | ৩৩.৩% | ২২.৯% | ১৪.৩% | enforced, PASS |

C5 band = ৩০ · ৩৫ · ২৫ · ১০, ±৫.

## Wave 2 — where to start (do not treat as authored)

QB-D-007 withdrew the claim that wave 1 exhausted the chapter: a re-count puts পাঠ ২১ at
**32–34 distinct facts**, and wave 1 stopped at the easiest slots. Verified absent from wave 1:

- শান্তি ও সাম্যের বাণী (মূল তথ্য, first paragraph)
- the ভাষণ's opening আল্লাহর প্রশংসা, as a comprehension item — the first attempt at this was
  cut because its marked-correct option stated a norm the extraction never states (QB-D-008)
- অনুশীলনী ২ — ঠিকমতো উচ্চারণ, 8 words, untouched
- অনুশীলনী ৫ — প্রয়োজনীয় শব্দ বসিয়ে বাক্য পূর্ণ, untouched
- the remaining emphasis points as S07 items

Wave 2 must re-check ZERO-OVERLAP against the **promoted** wave-1 bank, not against a blank slate.

## Open, carried forward

- **UP-002** — the LOCKED payload has no `pool` field; pool membership stays authoring-side in
  `pool_index`. Hub-side usage-lock and AS rotation are blocked on it.
- **Finding V-2** (`tools/hub-export/SMOKE.md`): `build_question_envelopes.py`'s default
  envelope-schema path does not exist in this repo; `--envelope-schema` must be passed explicitly.
  The vendored script is not edited (supersede-only).
- **The gate suite measures structure, not truth** (QB-D-008, CD-041). No script judges whether an
  answer is correct, whether the Bengali reads naturally, or whether a সিরাত item's theological
  register is right. The Principal's read of the promoted bank is what closes those.
- The three v0.1 policy drafts were **deleted** from `_inbox/` on Principal instruction —
  superseded by the imported v1.0 policies; `_inbox/` is staging, not archive.
