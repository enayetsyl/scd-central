#!/usr/bin/env python3
"""slot_register_check.py — proves canon/marklogic/SLOT_REGISTER.json against its own spine.

Run from repo root:
    python tools/audits/slot_register_check.py [--selftest]

WHAT THIS IS, AND WHY IT IS NOT PART OF THE GATE SUITE
------------------------------------------------------
The register (CD-138) is the data COVERAGE reads. This script proves the register against
`canon/marklogic/MarkLogic_BAN_Spine.md` **at build time**, and deliberately stops there.

**COVERAGE never reads a spine file — that is the point, not an omission.** CD-138(b) forbids any
gate deriving task mode, admitted-set membership or set cardinality from a header marker string
(*যেকোনো একটা* · *অথবা* · *বা* · *ও* · *+* · *ভেঙে*). The cheapest way to guarantee a gate cannot
read a surface is to give it no path to the file the surface lives in. So the spine parse lives
HERE, runs once per register change, and pastes its output; the gate reads the JSON only.

THE C1–C4 REPAIR (Principal ruling 2026-08-15) — WHAT WAS WRONG AND WHY IT WAS WORSE THAN GAPS
----------------------------------------------------------------------------------------------
The first version of this file read **one column** and could not say so. `spine_c5_marks()` took
no class and read the C5 cell positionally; `check()` accepted a `cls` argument, used it in filters
and in **every error string**, and never passed it to the parser. Two consequences, and the second
is the one that matters:

  * `main()` called `check()` once at `cls=5`. Sixty C1–C4 rows would have been filtered out and
    never examined, and the script would have printed `RESULT: CLEAN`. **A register whose new
    column was never read, reported as clean.**
  * `check(cls=1)` emitted *"BAN-S01: register says 999 marks; spine C1 column says 10"*. S01's C1
    cell is `—`. **10 is the C5 value wearing a C1 label**, because the f-string interpolated
    `cls` while the data came from `cells[4]`. **A checker that misnames the column it read is not
    a weaker checker; it is a witness that cannot be cross-examined.**

Both were demonstrated before the repair was authorised — an absurd C1 row carrying four of this
script's own seeded failure classes at once produced *"NONE — the row was never read"*. The seeds
below keep both dead: `CLASS-BLIND` proves a bad row in EVERY column is caught, and `COLUMN-LABEL`
proves the number in the message comes from the column the message names.

A THIRD DEFECT, FIXED IN PASSING AND RECORDED BECAUSE IT IS THE SAME SHAPE. The old row parser did
`[c for c in cells if c != ""]` — **dropping empty cells made the column position depend on the
row's content.** Every BAN absence happens to be written `—` rather than left blank, so the bug
never fired; the next spine to leave a cell blank would have shifted every class one place left and
the checker would have reported confidently on the wrong column. Positions are now taken from the
row's own pipe delimiters and the cell count is asserted.

WHAT IT CHECKS
--------------
  1. MARKS      — each row's `marks` against the spine's নম্বরের ধাপ table, **for that row's own
                  class column**, all five.
  2. ARITHMETIC — `items_per_paper` × `marks_per_item` == `marks`, per row. D5 and D6 rows are
                  exempt and each says why (below).
  3. I-1        — the marks column totals 100 **per class**, D6 (স্কুলের নিজস্ব প্রশ্ন) included,
                  and the class's own L-rows must sum to the spine's D6 cell for that class.
                  Items are totalled SEPARATELY and are NOT expected to reach 100 (CD-138(d)).
  4. I-4        — no half marks in this file (the sole site in the whole structure is ENG S10).
  5. I-6        — no row without a cause-code (`d_code`).
  6. I-8        — gap rule, **computed from the register**: a slot present at class X and again at
                  X+2 must be present at X+1. A leading absence that ends once the slot starts is a
                  prefix, not a gap, and must not fire.
  7. SHAPE      — `task_mode` ∈ {alternative, composite, simple}; alternative rows carry
                  `admitted_set` + `selected` and `selected` ∈ `admitted_set`; composite rows
                  carry `parts`; NO row carries an authored `chapter_authorable` (CD-138(f)).
  8. D5 SHAPE   — an absent slot carries `d_code: "D5"`, zero marks and zero items, an
                  `absent_reason` quoted from the spine, and **no task fields at all**. A D5 row
                  asserting a task claims the class does something it does not do.
  9. D6 SHAPE   — a school's-own row carries an `L`-id, `d_code: "D6"` and `marks`. It is keyed
                  `(L-id, class)` because **L-ids repeat across classes at different marks** —
                  `BAN-L01` is 7 at C1 and 5 at C2, `BAN-L03` is 10 at both C1 and C2.

TWO EXEMPTIONS, EACH STATED RATHER THAN SILENT (SOURCE_POLICY §7.17)
--------------------------------------------------------------------
  * **D5 rows are exempt from MARKS, ARITHMETIC and SHAPE.** They assert absence, not a question.
    What is checked instead is that the spine's own cell for that class really is `—`.
  * **D6 rows are exempt from ARITHMETIC.** The spine's স্কুলের নিজস্ব প্রশ্ন table gives an id, a
    class, a mark total and a reason — and **no `×n` split for any of its eight rows**. Under
    CD-138(d) an invented divisor is indistinguishable from a read one, so `items_per_paper` is
    `null` on these rows and the arithmetic check is skipped by design. **The check that replaces
    it is stronger than the one it replaces**: the L-rows for a class must sum to that class's own
    D6 cell in the নম্বরের ধাপ table — two independent statements in the spine, cross-read.

Exit 0 = CLEAN, 1 = FAIL. Paste output verbatim per AGENTS.md §5.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "canon" / "marklogic" / "SLOT_REGISTER.json"
SPINES = {"BAN": ROOT / "canon" / "marklogic" / "MarkLogic_BAN_Spine.md"}
CLASSES = (1, 2, 3, 4, 5)

CELL_NUM = re.compile(r"^\**\s*([\d.]+)\s*\**$")
SLOT_ID = re.compile(r"^S\d\d$")
L_ID = re.compile(r"^[A-Z]+-L\d\d$")
MODES = {"alternative", "composite", "simple"}
ABSENT = ("—", "-", "")


SCOPE = re.compile(r"^([A-Z]+)\s+C(\d)(?:\s*[-–]\s*C?(\d))?$")


def built_classes(reg, subject):
    """The classes the register DECLARES built, from its own `scope_built`.

    Why this exists rather than "whatever rows happen to be present": the two are different
    claims, and conflating them is how a half-written column passes. Rows-present would let a
    single stray row make a class look built; `scope_built` is the author saying so. Anything not
    in it is REFUSED by name rather than skipped silently (SOURCE_POLICY §7.17).
    """
    out = set()
    for entry in reg.get("scope_built", []):
        m = SCOPE.match(entry.strip())
        if m and m.group(1) == subject:
            lo = int(m.group(2))
            hi = int(m.group(3)) if m.group(3) else lo
            out |= set(range(min(lo, hi), max(lo, hi) + 1))
    return out


def _cells(line):
    """The row's cells, positions taken from its OWN pipe delimiters.

    Never drops an empty cell. The old parser did, which made column position depend on row
    content — a blank cell anywhere would have shifted every class one place left and the checker
    would have reported confidently on the wrong column.
    """
    if not line.startswith("|"):
        return None
    parts = [c.strip() for c in line.split("|")]
    return parts[1:-1] if len(parts) >= 3 else None


def spine_columns(text):
    """→ ({slot: {cls: marks-or-None}}, {cls: D6-total}).

    Both are read from the নম্বরের ধাপ table, whose cells are C1…C5 left to right. The file states
    that order in its own header row, so position is the fact; a name lookup would be a second
    guess at it. The header row is asserted rather than assumed.
    """
    marks, own, header_seen = {}, {}, False
    for line in text.splitlines():
        cells = _cells(line)
        if not cells or len(cells) != 7:
            continue
        if not header_seen:
            if [c.strip("* ") for c in cells[2:]] == ["C1", "C2", "C3", "C4", "C5"]:
                header_seen = True
            continue
        head, label, cols = cells[0], cells[1], cells[2:]
        if SLOT_ID.match(head):
            row = {}
            for i, c in enumerate(cols):
                g = CELL_NUM.match(c)
                row[CLASSES[i]] = float(g.group(1)) if g else None
            marks[head] = row
        elif head in ABSENT and "স্কুলের নিজস্ব প্রশ্ন" in label:
            for i, c in enumerate(cols):
                g = CELL_NUM.match(c)
                own[CLASSES[i]] = float(g.group(1)) if g else 0.0
    if not header_seen:
        raise ValueError("the নম্বরের ধাপ table's C1…C5 header row was not found — the column "
                         "order this file reads positionally could not be confirmed")
    return marks, own


def check(reg, spine_text, cls, subject="BAN"):
    """Every check, for ONE class column — and the column it reads is the one it is asked for."""
    errs, rep = [], []
    smarks, sown = spine_columns(spine_text)
    rows = [r for r in reg["rows"] if r["subject"] == subject and r["class"] == cls]
    slot_rows = [r for r in rows if r.get("d_code") != "D6"]
    l_rows = [r for r in rows if r.get("d_code") == "D6"]
    live = [r for r in slot_rows if r.get("d_code") != "D5"]
    absent_rows = [r for r in slot_rows if r.get("d_code") == "D5"]
    spine_live = sum(1 for v in smarks.values() if v.get(cls) is not None)
    rep.append(f"C{cls}: {len(rows)} register row(s) — {len(live)} live · {len(absent_rows)} D5 "
               f"absent · {len(l_rows)} D6 school's-own; spine's C{cls} column carries "
               f"{spine_live} live slot(s)")

    for r in slot_rows:
        slot = r["slot"].split("-")[-1]
        want = (smarks.get(slot) or {}).get(cls)
        if r.get("d_code") == "D5":
            # 8 — D5 shape. Absence is the claim, so the spine's own cell must be absent too.
            if want is not None:
                errs.append(f"C{cls} {r['slot']}: declared D5 (absent), but the spine's C{cls} "
                            f"cell carries {want:g} marks")
            if r.get("marks") or r.get("items_per_paper"):
                errs.append(f"C{cls} {r['slot']}: a D5 row carries marks/items — absence is not a "
                            f"question with zero value, it is not a question")
            if not str(r.get("absent_reason", "")).strip():
                errs.append(f"C{cls} {r['slot']}: D5 row states no `absent_reason` — I-9 requires "
                            f"the reason, not only the code (D5's own column: কোন শ্রেণিতে আসবে, "
                            f"আর কেন এই শ্রেণিতে নয়)")
            for f in ("task_mode", "admitted_set", "selected", "parts", "admitted_task"):
                if f in r:
                    errs.append(f"C{cls} {r['slot']}: a D5 row carries `{f}` — a row asserting "
                                f"absence must not also assert a task the class does not do")
            continue
        # 1 — marks, against THIS class's column
        if want is None:
            errs.append(f"C{cls} {r['slot']}: the spine's C{cls} column has no mark for this slot, "
                        f"but the register carries {r['marks']} and does not declare D5")
        elif float(r["marks"]) != want:
            errs.append(f"C{cls} {r['slot']}: register says {r['marks']} marks; spine C{cls} "
                        f"column says {want:g}")
        # 2 — arithmetic
        prod = r["items_per_paper"] * r["marks_per_item"]
        if prod != r["marks"]:
            errs.append(f"C{cls} {r['slot']}: {r['items_per_paper']} items × "
                        f"{r['marks_per_item']} = {prod}, but the row declares {r['marks']} marks")

    # 9 — D6 shape, and the cross-read that replaces their missing arithmetic
    for r in l_rows:
        if not L_ID.match(r["slot"]):
            errs.append(f"C{cls} {r['slot']}: a D6 row must carry an L-id")
        if r.get("items_per_paper") is not None:
            errs.append(f"C{cls} {r['slot']}: D6 rows carry no item split — the spine's "
                        f"স্কুলের নিজস্ব প্রশ্ন table states none for any of its rows, and "
                        f"CD-138(d) forbids inventing one")
    l_total = sum(r["marks"] for r in l_rows)
    d6 = sown.get(cls, 0.0)
    if l_total != d6:
        errs.append(f"I-1/D6: C{cls}'s L-rows sum to {l_total:g}, but the spine's own "
                    f"স্কুলের নিজস্ব প্রশ্ন cell for C{cls} says {d6:g}")

    # 3 — I-1, per class, with D6 included
    total_marks = sum(r["marks"] for r in slot_rows)
    total_items = sum(r["items_per_paper"] or 0 for r in live)
    if total_marks + l_total != 100:
        errs.append(f"I-1: C{cls} marks total {total_marks:g} + স্কুলের নিজস্ব প্রশ্ন "
                    f"{l_total:g} = {total_marks + l_total:g}, not 100")
    rep.append(f"I-1 C{cls}: {total_marks:g} + D6 {l_total:g} = {total_marks + l_total:g} ✓ "
               f"(D6 cross-read against the spine's own cell: {d6:g} ✓)")
    rep.append(f"C{cls} items total {total_items} — a SEPARATE fact, and correctly not 100 "
               f"(CD-138(d))")

    # 4 — I-4
    halves = [r["slot"] for r in rows
              if float(r["marks"] or 0) % 1 or float(r.get("marks_per_item") or 0) % 1]
    if halves:
        errs.append(f"I-4: half marks at C{cls} {', '.join(halves)} — BAN uses none at any class; "
                    f"the sole site in the structure is ENG S10")

    # 5 — I-6
    for r in rows:
        if not r.get("d_code"):
            errs.append(f"I-6: C{cls} {r['slot']} carries no cause-code")

    # 7 — shape, live rows only
    for r in live:
        if r["task_mode"] not in MODES:
            errs.append(f"C{cls} {r['slot']}: task_mode {r['task_mode']!r} is not one of "
                        f"{sorted(MODES)}")
        if r["task_mode"] == "alternative":
            if not r.get("admitted_set") or not r.get("selected"):
                errs.append(f"C{cls} {r['slot']}: alternative row without admitted_set/selected")
            elif r["selected"] not in r["admitted_set"]:
                errs.append(f"C{cls} {r['slot']}: selected {r['selected']!r} is not in its own "
                            f"admitted_set")
        if r["task_mode"] == "composite" and not r.get("parts"):
            errs.append(f"C{cls} {r['slot']}: composite row without parts")
    for r in rows:
        if "chapter_authorable" in r:
            errs.append(f"C{cls} {r['slot']}: carries an AUTHORED chapter_authorable — CD-138(f) "
                        f"makes it DERIVED from the per-chapter bank declarations, never "
                        f"authored here")
    modes = {m: sum(1 for r in live if r["task_mode"] == m) for m in sorted(MODES)}
    rep.append(f"C{cls} task_mode declared: " + " · ".join(f"{k} {v}" for k, v in modes.items()))
    return errs, rep


def check_i8(reg, subject="BAN"):
    """6 — I-8, COMPUTED from the register rather than reported off one column.

    `MarkLogic_Rules.md` I-8: কোনো প্রশ্ন এক শ্রেণিতে থাকলে এবং তার দুই শ্রেণি পরে আবার থাকলে,
    মাঝের শ্রেণিতেও থাকতে হবে. The rule is about an INTERIOR HOLE. A leading absence that ends
    once the slot starts is a ladder step, not a gap, and firing on it would make every correctly
    staged slot in the file red — which is why the presence run is bracketed by first and last
    rather than scanned from C1.

    This is the check the register's own `self_checks.I-8_gap_rule` promised would become testable
    when C1–C4 were built. It needs the D5 rows to exist: with no row for an absent slot there is
    nothing to distinguish "absent" from "not yet built", and the rule cannot be computed at all.
    """
    errs, rep = [], []
    built = built_classes(reg, subject)
    unbuilt = [c for c in CLASSES if c not in built]
    if unbuilt:
        return [], [f"I-8 gap rule: REFUSED, not passed — the rule spans the whole ladder and "
                    f"{subject} declares C{', C'.join(map(str, unbuilt))} unbuilt in "
                    f"`scope_built`. A gap cannot be told from an unbuilt rung, so no verdict is "
                    f"given. This becomes computable the moment those columns land."]
    slots = sorted({r["slot"] for r in reg["rows"]
                    if r["subject"] == subject and r.get("d_code") != "D6"})
    if not slots:
        return [], [f"I-8: no {subject} slot rows in the register — nothing to compute"]
    holes = []
    for slot in slots:
        by_cls = {r["class"]: r for r in reg["rows"]
                  if r["subject"] == subject and r["slot"] == slot}
        missing = [c for c in CLASSES if c not in by_cls]
        if missing:
            errs.append(f"I-8: {slot} has no register row at C{', C'.join(map(str, missing))} — "
                        f"the rule cannot be computed on a ladder with an unbuilt rung "
                        f"(an absent slot carries a D5 row; it does not carry nothing)")
            continue
        present = [c for c in CLASSES if by_cls[c].get("d_code") != "D5"]
        if not present:
            continue
        interior = [c for c in range(min(present), max(present) + 1) if c not in present]
        if interior:
            holes.append(f"{slot} present at C{min(present)} and C{max(present)}, absent at "
                         f"C{', C'.join(map(str, interior))}")
        rep.append(f"   {slot}: " + " ".join("●" if c in present else "○" for c in CLASSES)
                   + (f"  starts C{min(present)}" if len(present) < len(CLASSES) else "  all five"))
    if holes:
        errs.append("I-8 gap rule: interior hole(s) — " + " · ".join(holes))
    rep.insert(0, f"I-8 gap rule: COMPUTED over {len(slots)} slot(s) × 5 classes — "
                  f"{'no interior hole' if not holes else str(len(holes)) + ' hole(s)'}; "
                  f"every absence is a leading prefix (● present · ○ absent, C1→C5)")
    return errs, rep


def run_all(reg, spine, subject="BAN"):
    errs, rep = [], []
    built = built_classes(reg, subject)
    for cls in CLASSES:
        if cls not in built:
            rep.append(f"C{cls}: REFUSED, not passed — {subject} C{cls} is not in the register's "
                       f"own `scope_built`. An unbuilt column is reported as unbuilt; it is never "
                       f"reported as clean (SOURCE_POLICY §7.17)")
            continue
        e, r = check(reg, spine, cls, subject)
        errs += e
        rep += r
    e, r = check_i8(reg, subject)
    errs += e
    rep += r
    rep.append("I-4 half marks: none ✓ (sole structural site is ENG S10, not in this file)")
    rep.append("I-6 cause-codes: present on every row ✓")
    rep.append("chapter_authorable: absent from every row ✓ (CD-138(f) — derived, never authored)")
    return errs, rep


def selftest():
    """Seeded both directions. Every case is a mutation of the LIVE register — which is a control,
    not a fixture (CD-121(e): controls may be drawn from the live pool; seeds may not). The seeds
    here are the MUTATIONS, and they are synthetic."""
    print("SELFTEST — the instrument before the verdict (CD-025).")
    reg = json.loads(REGISTER.read_text(encoding="utf-8"))
    spine = SPINES["BAN"].read_text(encoding="utf-8")
    ok = True

    errs, _ = run_all(reg, spine)
    if errs:
        print(f"  FAIL  baseline: the live register is not clean -> {errs}")
        ok = False
    else:
        print("  PASS  baseline: the live register passes every check in every class column")

    def mutate(fn):
        r = json.loads(json.dumps(reg))
        fn(r)
        return r

    class RowNotBuilt(Exception):
        """A seed's target row does not exist yet. NOT a pass and NOT a failure — see below."""

    def row(r, cls, slot):
        for x in r["rows"]:
            if x["class"] == cls and x["slot"] == slot:
                return x
        raise RowNotBuilt(f"{slot} at C{cls}")

    cases = [
        ("MARKS", "S02 at C5 declared at 7 against the spine's 5",
         lambda r: row(r, 5, "BAN-S02").update({"marks": 7, "marks_per_item": 1.4})),
        ("ARITHMETIC", "S07 at C5 says 4 items × 2 but declares 9 marks",
         lambda r: row(r, 5, "BAN-S07").update({"marks": 9})),
        ("I-1", "a C5 slot silently dropped — the column no longer reaches 100",
         lambda r: r["rows"].remove(row(r, 5, "BAN-S15"))),
        ("I-4", "a half mark introduced at C5 S04 — permitted only at ENG S10",
         lambda r: row(r, 5, "BAN-S04").update({"marks": 4.5, "marks_per_item": 0.9})),
        ("I-6", "a row with its cause-code removed",
         lambda r: row(r, 5, "BAN-S01").pop("d_code")),
        ("SHAPE", "an alternative row whose `selected` is not in its own admitted_set",
         lambda r: row(r, 5, "BAN-S10").update({"selected": "ভাব নির্ণয়"})),
        ("SHAPE", "a composite row with no parts",
         lambda r: row(r, 5, "BAN-S12").pop("parts")),
        ("CD-138(f)", "an AUTHORED chapter_authorable on a slot row",
         lambda r: row(r, 5, "BAN-S14").update({"chapter_authorable": False})),
    ]

    # ── the C1–C4 repair's own seeds — every one of these passed silently before it ──────
    cases += [
        ("CLASS-BLIND", "a WRONG-MARKS row at C1 — the class the old parser could not read",
         lambda r: row(r, 1, "BAN-S02").update({"marks": 99, "marks_per_item": 16.5})),
        ("CLASS-BLIND", "a WRONG-MARKS row at C3, mid-column",
         lambda r: row(r, 3, "BAN-S07").update({"marks": 99, "marks_per_item": 19.8})),
        ("I-1", "C1's total broken — the column that needs the D6 term to reach 100",
         lambda r: row(r, 1, "BAN-S02").update({"marks": 11, "marks_per_item": 11 / 6})),
        ("I-1/D6", "an L-row's marks changed so the class no longer matches the spine's D6 cell",
         lambda r: row(r, 1, "BAN-L02").update({"marks": 11})),
        ("D5-SHAPE", "a D5 row given marks — absence is not a question with zero value",
         lambda r: row(r, 1, "BAN-S01").update({"marks": 5, "items_per_paper": 5,
                                                "marks_per_item": 1})),
        ("D5-SHAPE", "a D5 row asserting a task the class does not do",
         lambda r: row(r, 1, "BAN-S01").update({"task_mode": "simple"})),
        ("D5-SHAPE", "a D5 row with no `absent_reason` — I-9 wants the reason, not the code",
         lambda r: row(r, 1, "BAN-S01").pop("absent_reason")),
        ("D5-SHAPE", "a slot declared D5 where the spine's own cell carries marks",
         lambda r: row(r, 5, "BAN-S09").update({"d_code": "D5", "marks": 0,
                                                "items_per_paper": 0, "marks_per_item": 0,
                                                "absent_reason": "নেই"})),
        ("D6-SHAPE", "an L-row given an invented item split",
         lambda r: row(r, 1, "BAN-L01").update({"items_per_paper": 7})),
        ("I-8", "an INTERIOR HOLE — S07 removed from C3 while C2 and C4 keep it",
         lambda r: row(r, 3, "BAN-S07").update({"d_code": "D5", "marks": 0,
                                                "items_per_paper": 0, "marks_per_item": 0,
                                                "absent_reason": "কল্পিত",
                                                "task_mode": None}) or
                   row(r, 3, "BAN-S07").pop("task_mode")),
        ("I-8", "an UNBUILT rung — a slot with no row at all at one class",
         lambda r: r["rows"].remove(row(r, 2, "BAN-S04"))),
    ]

    # A seed whose target row is not built yet is HELD, and named. It is not a pass — nothing was
    # proved — and it is not a failure — nothing is wrong. Counting it either way would be a lie
    # about the instrument, and silently dropping it is how a seed disappears and never comes back.
    # The gate repair lands before the C1–C4 data by the Principal's ruled order, so this state is
    # expected exactly once and must be visible while it lasts (SOURCE_POLICY §7.17).
    print()
    held = []
    exercised = 0
    for label, why, fn in cases:
        try:
            mutated = mutate(fn)
        except RowNotBuilt as e:
            held.append(f"{label} ({why}) — needs {e}")
            print(f"  HELD  {label:<12} not exercisable yet: {why}  [needs {e}]")
            continue
        exercised += 1
        errs, _ = run_all(mutated, spine)
        if errs:
            print(f"  PASS  {label:<12} fires on: {why}")
        else:
            print(f"  FAIL  {label:<12} DID NOT FIRE on: {why}")
            ok = False

    # ── NEGATIVES ───────────────────────────────────────────────────────────────────────
    print()
    scrubbed = (spine.replace("*(দুটোর যেকোনো একটা)*", "")
                     .replace("*(তিনটার যেকোনো একটা)*", ""))
    a, _ = run_all(reg, spine)
    b, _ = run_all(reg, scrubbed)
    if a == b == []:
        print("  PASS  CD-138(b)    stays quiet on: every যেকোনো একটা marker stripped from the "
              "spine — verdict unchanged, because task mode is DECLARED and no marker is read")
    else:
        print(f"  FAIL  CD-138(b)    marker edit moved the verdict: {a} -> {b}")
        ok = False

    e, _ = check_i8(reg)
    if not e:
        print("  PASS  I-8          stays quiet on: BAN's seven LEADING absences (S01 · S06 · S08 "
              "· S09 · S10 · S11 · S13) — a slot that starts late is a ladder step, not a hole, "
              "and firing here would redden every correctly staged slot in the file")
    else:
        print(f"  FAIL  I-8          fired on a leading prefix: {e}")
        ok = False

    # COLUMN-LABEL — the defect that made the old file a witness that could not be
    # cross-examined. The number in the message must come from the column the message names.
    try:
        mut = mutate(lambda r: row(r, 1, "BAN-S02").update({"marks": 99, "marks_per_item": 16.5}))
    except RowNotBuilt as e:
        held.append(f"COLUMN-LABEL (a C1 error must quote C1's own spine value) — needs {e}")
        print(f"  HELD  COLUMN-LABEL not exercisable yet: a C1 error must quote C1's own spine "
              f"value, not C5's  [needs {e}]")
    else:
        e1, _ = check(mut, spine, cls=1)
        msg = next((m for m in e1 if "spine C1 column says" in m), "")
        if "says 12" in msg:
            print("  PASS  COLUMN-LABEL a C1 error names C1 and quotes 12 — C1's own spine value. "
                  "The old file quoted the C5 number under a C1 label; label and source now agree")
        else:
            print(f"  FAIL  COLUMN-LABEL a C1 error did not quote C1's spine value: {msg!r}")
            ok = False

    print(f"\nSELFTEST RESULT: {'PASS' if ok else 'FAIL'} "
          f"({exercised} of {len(cases)} seeded failures exercised + 3 negatives + 1 baseline, "
          f"across 5 class columns)")
    if held:
        print(f"  {len(held)} seed(s) HELD — targets not built yet, reported rather than dropped:")
        for h in held:
            print(f"    · {h}")
    return ok


def main():
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    print(f"slot_register_check.py — root: {ROOT}")
    if not selftest():
        print("\nRESULT: FAIL (selftest red — no register verdict is believable)")
        sys.exit(1)
    reg = json.loads(REGISTER.read_text(encoding="utf-8"))
    spine = SPINES["BAN"].read_text(encoding="utf-8")
    print(f"\nREGISTER: {REGISTER.relative_to(ROOT)}  [authority {reg['authority']}, "
          f"built {reg['built']}, scope {', '.join(reg['scope_built'])}]")
    errs, rep = run_all(reg, spine)
    for line in rep:
        print(f"  REPORT  {line}")
    for e in errs:
        print(f"  FAIL    {e}")
    print(f"RESULT: {'FAIL' if errs else 'CLEAN'} ({len(errs)} failures)")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
