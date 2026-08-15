# _wip/STATE.md — question-banks (session-resumable state)

| Field | Value |
|---|---|
| Current build | **The slot register (CD-138).** `canon/marklogic/SLOT_REGISTER.json` is built at **BAN C5 only**; C1–C4 and ENG · MATH · SCI/BGS are owed. পাঠ ১৩'s bank is untouched this session and is **NOT promoted**. |
| Phase | Register built and proven; COVERAGE converted. **Next phase is পাঠ ১৩'s re-author, and it is Principal-gated** (see Blockers). |
| Last completed step | CD-138 (amended), CD-139, `PENDING-P-038`, `QB-CR-012` filed → register built at BAN C5, proven against the spine by `tools/audits/slot_register_check.py` (**8 seeded + 1 negative + 1 baseline, PASS**) → COVERAGE converted to read the register (**27 seeded + 11 negatives + 6 declaration cases + 1 baseline, PASS**; suite 22 gates). `canon_check` CLEAN · `tools_check` CLEAN. Three commits: `e1054c7` rulings · `5f95ce2` build · `8cec402` gate. **Nothing pushed.** |
| Next step | **BLOCKED — see below.** After that: BAN C1–C4, then ENG, MATH, SCI/BGS, **added as DATA ROWS, never as new gate code**. If a new subject needs a code change, the register's shape is wrong. |
| Blockers / open PENDING-P tags | **`PENDING-P-038` RAISED** (register completeness across chapters; blocked on MarkLogic §৪'s syllabus split). **One OPEN question to the Principal: পাঠ ১৩ is RED under CD-138 and cannot be cleared without editing it**, which this session's brief excluded. |
| Files in `_wip` awaiting "done" | this file · `U13_BLOOM_PROBE_2026-08-15.md` |

## The suite is RED on পাঠ ১৩, deliberately, and the reason is one line

`COVERAGE` FAILs with: *bank header declares no `admissible_slots`*. CD-138(e) makes the
admissibility declaration a required part of a chapter bank, and পাঠ ১৩ was authored before that
ruling existed. **The bank was not edited to clear it** — the session brief excluded পাঠ ১৩, and
editing an artifact to green a gate is the move AGENTS §5 forbids.

**A read-only probe measured what the fix costs**, with a synthetic declaration crediting **every
item with the right task** — the most favourable possible reading:

```
S06 3/5 · S12 3/5 · S13 3/5
```

**Three slots are two items short of the paper's own per-slot demand (CD-138(g)), before any of the
known task defects are counted.** So the re-author owes **at least +6 items** on top of: the four
re-tags, the ten mis-slotted S10 items, the S12 completion (শব্দ গঠন), and the S11 off-choice three.
**Recompute the target after those, never on a carried number.**

## What the register carries at BAN C5

15 rows · **56 items · 100 marks** (the two are separate fields; only marks total 100).
**task_mode: 4 alternative · 2 composite · 9 simple.**

| Slot | Mode | The fact that was invisible before |
|---|---|---|
| S01 | composite | কবির নাম · কবিতার নাম · ৮ লাইন — declared on the মূল কাঠামো line's own **1+1+8** split |
| S06 | alternative | {বিপরীত, সমার্থক} → **বিপরীত**. C3 selects differently; S13 holds সমার্থক at C3 |
| S10 | alternative | {ভাষারীতি, পদ নির্ণয়, ক্রিয়ার কাল} → **পদ নির্ণয়**. ভাব নির্ণয় is admitted at **no class** |
| S11 | alternative | {প্রশ্ন তৈরি, বিরামচিহ্ন} → **বিরামচিহ্ন**. প্রশ্ন তৈরি is C4-and-above |
| S12 | composite | ভাঙা **and** শব্দ গঠন. C1 is D3 with different parts — do not copy down |
| S14 | alternative | cardinality **3** declared against a header saying দুটোর — declared, never counted off the string |
| S15 | simple | *সূত্রসহ বা খোলা* varies the **stimulus**, not the task |

## Two things a later session must not re-derive

- **No gate reads a spine file.** The spine parse lives at build time in
  `tools/audits/slot_register_check.py`. CD-138(b) makes mode DECLARED; the markers
  (*যেকোনো একটা* · *অথবা* · *বা* · *ও* · *+* · *ভেঙে*) are authoring evidence only. Both halves are
  seeded — strip the markers from the spine, and from the register's prose, and neither verdict moves.
- **`chapter_authorable` is derived, never authored.** A register row carrying one FAILs, and the
  check runs on the register **in hand** rather than only in the disk loader — the seed proved that
  distinction the hard way.

## Carried forward, unchanged

- **PENDING-P-008 (FLAGGED)** — `TOPIC_NUMBERS.md` is a C5-Bangla seed; REF-19 has no Bangla
  punctuation slug.
- **UP-002** `pool` field · **UP-003** `ref19_topic_id` rejects `MATH-*-REL`, blocking every C5 Math bank.
- **QB-CR-009** U14 `-09` re-tag, execution owed at wave 2.
- **`QB-CR-011` is now PATTERN** (`QB-CR-012`, four instances). No gate is proposed; the executable
  residue is CD-138(b)/(e) and it is seeded there.
- **The gate suite measures structure, not truth.** It cannot tell you an answer is wrong.
