# _wip/STATE.md — question-banks (session-resumable state)

| Field | Value |
|---|---|
| Current build | **পাঠ ১৩ re-authored against the slot register — DONE and CLEAN at 110 items.** `canon/marklogic/SLOT_REGISTER.json` is still built at **BAN C5 only**; C1–C4 rows are specified and RULED but not yet written (see Next step). |
| Phase | পাঠ ১৩ closed at gate-CLEAN. **Nothing promoted** — the 110-item set is held for the Principal's Subject Lead pass (CD-136(g), REF-09 §9). |
| Last completed step | CD-138(e) declaration countersigned and committed (`6511352`, corrections-class, header only) → wave 4 re-author committed (`1b9e83d`, build-class): 4 re-tags, 11 retirements, 6 rewrites, 33 new items, `task_index` for all 110. Suite **CLEAN (0 failures)**, both selftests PASS, `canon_check` CLEAN. **Nothing pushed** — `origin/main` still `4ec7b6f`. |
| Next step | BAN C1–C4 register rows, now UNBLOCKED by four Principal rulings (2026-08-15): D5 rows approved · L-rows approved · checker repair authorized · the two item splits ruled. Order: log → ruling (CD row) → gate (checker) → build (rows) → MARK-VALUE. |
| Blockers / open PENDING-P tags | **`PENDING-P-038` RAISED** (register completeness across chapters; blocked on MarkLogic §৪'s syllabus split). No open question to the Principal — this session's four were all ruled. |
| Files in `_wip` awaiting "done" | this file · `U13_BLOOM_PROBE_2026-08-15.md` · `U13_ADMISSIBILITY_DRAFT_2026-08-15.md` · `BAN_C1-C4_REGISTER_BLOCKED_2026-08-15.md` |

## পাঠ ১৩ — what the re-author actually changed, and why the numbers are what they are

**110 items. Recomputed twice in session; no number carried from wave 3's 88.**

| level | count | % | floor | margin |
|---|--:|--:|--:|--:|
| Remember | 34 | 30.9% | 20% (22) | **+12** |
| Understand | 30 | 27.3% | 25% (28) | **+2** |
| Apply | 30 | 27.3% | 25% (28) | **+2** |
| Analyze | 14 | 12.7% | 10% (11) | **+3** |
| Evaluate | 2 | 1.8% | 0% | +2 |
| Create | 0 | 0.0% | 0% | content fact, CD-135(d) |

Slots: S01 1 · S02 7 · S03 16 · S04 5 · S05 8 · S06 7 · S07 21 · S08 15 · S09 1 · S10 10 ·
S11 8 · S12 5 · S13 6. Every one clears its CD-138(g) demand.

**The binding constraint was never pool size — it was the Apply base.** Retiring the ten S10
ভাব নির্ণয় items cost 7 `Apply`; retiring Q34 cost the eighth. That is why S03, S11 and S12 are
all authored to their content limits, and why one S10 item is `Apply`: `পড়রে` is a ক্রিয়া and
`পড়া` a বিশেষ্য in the same poem, so deciding which by context is a rule applied in a new
situation, not a classification.

**Two things a later session must not re-derive:**

- **A plan table's own arithmetic can hide a term.** The countersigned plan read `S07 = R6 · U15 ·
  A1`, and Q34 WAS that `A1`. Retiring it was ruled after the table was signed, and the Apply
  margin silently fell to +1 — below the standard the same ruling set. **Recompute after every
  ruling, not once per plan.**
- **A content limit is a claim about how far the book was read.** Wave 3 called S06 · S12 · S13
  content-limited at three. Read again at source: five distinct যুক্তবর্ণ, seven clean opposites,
  six এক কথায় প্রকাশ mappings. The withdrawal is recorded in the bank header, not silently fixed.

**FIVE Remember items are left unextracted on the Principal's HOLD** — S02 +2 (ফেরেস্তা · বকুল),
S04 +3 — and are NAMED in `header.gaps` so a later wave can take them. They raise the pool without
raising `Apply`. Take them only together with enough new `Apply` to hold the margin.

**Q34 is retired and মিল-শব্দ is now UNSERVED.** That is the honest state: অনুশীলনী ৩ has no C5
spine slot, and CD-138(b) would have made Q34 declare S07's `মূল কাঠামো` — a declaration that is
convenient and false. The gap is in the spine, not in the bank.

## BAN C1–C4 — specified, ruled, not yet written

Full row specification and the arithmetic for all five columns:
`_wip/BAN_C1-C4_REGISTER_BLOCKED_2026-08-15.md`. **The file's title is now historical** — all four
blockers it records were ruled on 2026-08-15 and it is kept as the evidence trail, not as a
standing block.

| Blocker it found | Ruling |
|---|---|
| `slot_register_check.py` reads ONE column and mislabels it as whichever class it is asked for; `main()` never iterates | Repair authorized — parser takes `cls`, `main()` walks all five, I-1's D6 term per class (39·20·5·0·0) |
| No shape for an absent (D5) slot | D5 rows APPROVED — `d_code: D5`, spine's reason verbatim; `g_coverage` and admissibility skip them structurally. **Existence is class-level; admissibility is chapter-level; never one field.** I-8 computes from the register |
| D6 (`BAN-L01`…`L06`) has no home, and the ফলা title ban therefore has nothing to attach to | L-rows APPROVED — keyed `(L-id, class)` because L-ids repeat across classes at different marks. I-1 totals include them |
| `items_per_paper` underdetermined at source for C2 S12 and C3 S09 | RULED — C2 S12 = ১০টি × ১; C3 S09 = ৫টি প্রশ্ন × ২. Filed as a decision row, authority স্কুল কর্তৃপক্ষ. **Not UNRESOLVED** |

**I-8, hand-walked at source and expected to compute clean:** every BAN absence (S01, S06, S08,
S09, S10, S11, S13) is a **leading prefix** that ends once the slot starts. There is no interior
hole. The value of computing it is that the next subject's column will not be hand-walked.

## Carried forward, unchanged

- **PENDING-P-008 (FLAGGED)** — `TOPIC_NUMBERS.md` is a C5-Bangla seed; REF-19 has no Bangla
  punctuation slug. Live this session: S11's বিরামচিহ্ন items ride `BAN-SENTENCE`, which is the
  established choice and still not a punctuation slug.
- **UP-002** `pool` field · **UP-003** `ref19_topic_id` rejects `MATH-*-REL`, blocking every C5
  Math bank.
- **No gate reads a spine file.** The spine parse lives at build time in
  `tools/audits/slot_register_check.py`. Both halves of CD-138(b) stay seeded — strip every marker
  from the spine, and every marker-bearing prose field from the register, and neither verdict moves.
