# BAN C1–C4 register rows — STOPPED before any row was written

**Status:** নির্মাণাধীন — BLOCKED. No row added to `canon/marklogic/SLOT_REGISTER.json`.
**Reason:** the C1–C4 column cannot be written as data alone. Three blockers require a ruling and
two of them require code, which the session brief made a STOP condition:
*"If any C1–C4 row requires touching gate or checker code, STOP and report — that is a
register-shape defect, not a data problem."*

Read at source: `canon/marklogic/MarkLogic_BAN_Spine.md` · `canon/marklogic/MarkLogic_Rules.md` ·
`tools/audits/slot_register_check.py` · `workstreams/question-banks/audits/gates.py`.
Nothing carried from any handoff.

---

## BLOCKER 1 — the checker reads ONE column, and mislabels it as whichever class it is asked for

`slot_register_check.py` is the only thing that proves the register against the spine. Its single
spine parser is `spine_c5_marks(text)`, which takes no class and reads `cells[4]` — the C5 column,
positionally. `check()` accepts a `cls` argument, uses it in filters and in every error string,
and **never passes it to the parser.**

Demonstrated, not inferred. An absurd C1 row was appended to a copy of the live register — wrong
marks, no `d_code`, `task_mode: "NONSENSE"`, and an authored `chapter_authorable`, four of this
script's own seeded failure classes at once:

```
PROOF 1 — an absurd C1 row appended to the register:
  errors reported: NONE — the row was never read

PROOF 2 — check(..., cls=1) on that same register:
    BAN-S01: register says 999 marks; spine C1 column says 10
    ...
PROOF 3 — spine_c5_marks() output (the ONLY spine read in this file):
   marks: {'S01': 10.0, 'S02': 5.0, ... 'S15': 12.0}
   school's own (D6): 0.0
```

Two separate failures, and the second is worse than the first:

- **`main()` calls `check(reg, spine)` once, at the default `cls=5`.** Sixty C1–C4 rows would be
  filtered out and never examined, and the script would print `RESULT: CLEAN`. A register whose
  new column was never read, reported as clean, is the shape AGENTS §5.1 and CD-089 exist for.
- **`cls=1` produces a sentence that is false about its own source.** *"spine C1 column says 10"*
  — S01's C1 cell is `—` (D5, absent); **10 is the C5 value**, wearing a C1 label because the
  f-string interpolates `cls` while the data came from `cells[4]`. A checker that misnames the
  column it read is not a weaker checker; it is a witness that cannot be cross-examined.

**I-1's D6 term has the same defect.** `sown` is read from `cells[4]` of the স্কুলের নিজস্ব
প্রশ্ন row and is `0.0`. The C1 S-slots total **61**, and 61 + 0 ≠ 100 would fire a false I-1
failure on correct data. The true term is C1 39 · C2 20 · C3 5 · C4 0 — the row the brief named.

**I-8 is reported, never computed.** The rule (`MarkLogic_Rules.md` I-8) is *একটা প্রশ্ন এক
শ্রেণিতে থাকলে এবং তার দুই শ্রেণি পরে আবার থাকলে, মাঝের শ্রেণিতেও থাকতে হবে* — an interior hole
in the ladder. `absent` is computed from one column's `None` cells and the ladder is never walked.
Verified by hand at source, **BAN has no interior gap**: every absence (S01, S06, S08, S09, S10,
S11, S13) is a leading prefix that ends once the slot starts. That is the right answer and it is
worth nothing until something computes it — which is precisely what the register's own
`self_checks.I-8_gap_rule` promised would happen when this column was built.

## BLOCKER 2 — the register has no shape for an ABSENT (D5) slot, and both answers cost code

Eight of the fifteen slots are absent at one or more of C1–C4. Every existing row carries
`items_per_paper`, `marks`, `marks_per_item`. There is no third state.

- **If a D5 slot gets a row** (`marks: 0`), the row asserts *"a slot with no items"*, which is a
  different claim from *"this class does not carry this slot"* — and `g_coverage` would then
  require every C1 chapter bank to declare `S01` admissible-or-excluded, forcing a content reason
  for a question the C1 paper does not contain. That is gate code.
- **If a D5 slot gets no row**, the absences are not in the register at all and **I-8 can never be
  computed from it** — the checker would have to read the ladder from the spine, which is checker
  code, and CD-138(b)'s whole point is to keep spine-reading out of the gate.

This is the Principal's, not an agent's: it decides what the register *is*, not what it says.

## BLOCKER 3 — D6 has no home, and the ফলা ban proves it

I-1 closes at C1/C2/C3 only if 39 / 20 / 5 are accounted for. The register has no row shape for
`BAN-L01` … `BAN-L06`, and `slot.split("-")[-1]` in `g_coverage` would yield `L01`, which no bank
declares and no slot demand covers.

**The brief's own instruction lands exactly here.** *"`row_constraints` carry the C1 'ভেঙে' ban
and 'ফলা' title ban."* The first attaches to `BAN-S12` C1 and a row exists for it — it is already
carried at `pending_row_constraints[BAN-S12-C1-NO-BHENGE]`. **The second does not.** Read at
source, the ফলা ban is on `BAN-L03` কারচিহ্ন C1, a **D6 row**: *"প্রথম শ্রেণিতে ফলা থাকবে না —
ফলা ও রেফ দ্বিতীয় শ্রেণির; শিরোনামে যেন ভুলেও না আসে"*, with the approval checklist repeating it
at line 370. There is no register row for it to attach to. `BAN-L01` and `BAN-L03` also each carry
**two class rows at different marks**, so an L-id is not unique on its own.

---

## The data itself, verified at source — held, not written

Arithmetic checked against `MarkLogic_Rules.md` I-1, per class:

| Slot | C1 | C2 | C3 | C4 | note |
|---|--:|--:|--:|--:|---|
| S01 | — | — | — | 10 | C4 D0, স্কুল কর্তৃপক্ষ, বৃত্তির প্রস্তুতির একমাত্র ব্যতিক্রম; E-AUTHOR-ENDORSE binds at C4 |
| S02 | 12 | 7 | 10 | 5 | C1 6×2 · C2 7×1 · C3 10×1 · C4 5×1 |
| S03 | **10** | 5 | 5 | 5 | **C1 5×2, composite — বাক্য + সঠিক বিরামচিহ্ন (যোগ্যতা ১৩.৩)** |
| S04 | 5 | 5 | 5 | 5 | D0 throughout, 5×1 |
| S05 | 5 | 5 | 5 | 5 | D0 throughout, 5×1 |
| S06 | — | — | 5 | 5 | C3 এখান থেকে শুরু; C1/C2 D5 — বইতে নেই |
| S07 | 10 | 12 | 10 | 8 | C1 10×1 · C2 6×2 · C3 5×2 · C4 4×2 |
| S08 | — | 15 | 10 | 15 | C2 3×5 · C3 2×5 · C4 3×5; ইসলামি ধারা binds every class |
| S09 | — | — | 10 | 5 | **C3 item count NOT STATED** — see below |
| S10 | — | 5 | 5 | 5 | C2 D3 ক্রিয়ার পুরুষ-সংগতি · C3 D4 বাক্যের প্রকার · C4 পদ নির্ণয় |
| S11 | — | 5 | 5 | 5 | C2/C3 বিরামচিহ্ন only; প্রশ্ন তৈরি C4-এর আগে নয় |
| S12 | **8** | 10 | 5 | 5 | **C1 D3, 4×2 — গোটা যুক্তবর্ণ দিয়ে শব্দ, ভাঙা নয় (নিয়ম B-1)**; **C2 item count NOT STATED** |
| S13 | — | — | 5 | 5 | C3 D4 সমার্থক শব্দ — S06-এর সঙ্গে মেলানো যাবে না |
| S14 | 5 | 5 | 5 | 5 | ছক → ছক → ফরম → আবেদনপত্র → আবেদনপত্র, all D3 below C4 |
| S15 | 6 | 6 | 10 | 12 | C1/C2 D4 নির্দেশিত, 🟦; C3 D4 অনুচ্ছেদ |
| **D6** | **39** | **20** | **5** | **0** | `BAN-L01`…`L06` — no row shape (Blocker 3) |
| **মোট** | **100** | **100** | **100** | **100** | verified by hand, all four columns |

**C1 S12 and C1 S03 are as the brief stated, confirmed at source** — S12 C1 is D3 with a
different task, not a mark change, and the parts are গোটা যুক্তবর্ণ + শব্দ; S03 C1 is the
composite. `BAN-S03-NOJOIN` already sits in the C5 row and is scoped *every class*, so the C1
composite must not be read as licence to join বাক্য গঠন to a যুক্তবর্ণ question.

### A fourth blocker, smaller and purely factual: two cells are underdetermined at source

`items_per_paper` cannot be authored for **C2 S12 (10 marks)** or **C3 S09 (10 marks)**. Both give
the total and no `×n` split, and both are deviations (D1↑ and D4↑) rather than মূল কাঠামো rows
that could inherit C5's. CD-138(d) says no divisor exists and none is used — so 10×1 and 5×2 are
both inventions. These two rows are unauthorable from the spine as it stands and need either a
Principal ruling or a spine amendment.

---

## What is NOT blocked

`g_coverage` itself reads `(subject, class, slot)` correctly and would serve a C1 bank unchanged.
The blockage is in proving the rows, not in consuming them. `QP6_SPINE_ITEM_MARKS` and
`QB_SPINE_ITEM_MARKS` carry only `("BAN", 5)`, so MARK-VALUE would report *"no spine item-mark
table vendored"* on a C1 bank rather than judge it — which is Task 4's subject and is named here
because the two land together.
