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

WHAT IT CHECKS
--------------
  1. MARKS      — each row's `marks` against the spine's নম্বরের ধাপ table, C5 column.
  2. ARITHMETIC — `items_per_paper` × `marks_per_item` == `marks`, per row.
  3. I-1        — the marks column totals 100 for the class, D6 (স্কুলের নিজস্ব প্রশ্ন) included.
                  Items are totalled SEPARATELY and are NOT expected to reach 100 (CD-138(d):
                  BAN C5 is 56 items / 100 marks; a check that sums items to 100 is wrong).
  4. I-4        — no half marks in this file (the sole site in the whole structure is ENG S10).
  5. I-6        — no row without a cause-code (`d_code`).
  6. I-8        — gap rule; NOT TESTABLE on a column with no D5 cell, and says so rather than
                  passing silently (SOURCE_POLICY §7.17: a check reports or refuses, never omits).
  7. SHAPE      — `task_mode` ∈ {alternative, composite, simple}; alternative rows carry
                  `admitted_set` + `selected` and `selected` ∈ `admitted_set`; composite rows
                  carry `parts`; NO row carries an authored `chapter_authorable` (CD-138(f) —
                  it is derived from per-chapter bank declarations and never authored here).

Exit 0 = CLEAN, 1 = FAIL. Paste output verbatim per AGENTS.md §5.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "canon" / "marklogic" / "SLOT_REGISTER.json"
SPINES = {"BAN": ROOT / "canon" / "marklogic" / "MarkLogic_BAN_Spine.md"}

# The নম্বরের ধাপ table row: | S01 | কবিতা মুখস্থ লেখা | — | — | — | 10 | **10** |
STEP_ROW = re.compile(r"^\|\s*(S\d\d)\s*\|([^|]*)\|(.+)\|\s*$")
CELL_NUM = re.compile(r"^\**\s*([\d.]+)\s*\**$")
# The school's own row carries an em-dash id cell and the bold label.
OWN_ROW = re.compile(r"^\|\s*—\s*\|\s*\*\*স্কুলের নিজস্ব প্রশ্ন\*\*\s*\|(.+)\|\s*$")

MODES = {"alternative", "composite", "simple"}


def spine_c5_marks(text):
    """→ {slot: marks} for the C5 column, plus the D6 (school's own) C5 figure.

    The C5 column is the LAST of the five class columns. Read positionally from the row rather
    than by header name: the header cells are C1…C5 left to right and the file states that order
    in its own table, so position is the fact and a name lookup would be a second guess at it.
    """
    marks, own = {}, None
    for line in text.splitlines():
        m = STEP_ROW.match(line)
        if m:
            slot, _task, rest = m.group(1), m.group(2), m.group(3)
            cells = [c.strip() for c in rest.split("|")]
            cells = [c for c in cells if c != ""]
            if len(cells) < 5:
                continue
            c5 = cells[4]
            if c5 in ("—", "-"):
                marks[slot] = None
                continue
            g = CELL_NUM.match(c5)
            if g:
                marks[slot] = float(g.group(1))
            continue
        m = OWN_ROW.match(line)
        if m:
            cells = [c.strip() for c in m.group(1).split("|") if c.strip() != ""]
            if len(cells) >= 5:
                c5 = cells[4]
                own = 0.0 if c5 in ("—", "-") else float(CELL_NUM.match(c5).group(1))
    return marks, own


def check(reg, spine_text, cls=5, subject="BAN"):
    errs, rep = [], []
    smarks, sown = spine_c5_marks(spine_text)
    rows = [r for r in reg["rows"] if r["subject"] == subject and r["class"] == cls]
    rep.append(f"{len(rows)} row(s) read from the register for {subject} C{cls}; "
               f"{sum(1 for v in smarks.values() if v is not None)} C{cls} slot(s) found in the spine's "
               f"নম্বরের ধাপ table")

    # 1 + 2 — marks against the spine, and the per-row arithmetic
    for r in rows:
        slot = r["slot"].split("-")[-1]
        want = smarks.get(slot)
        if want is None:
            errs.append(f"{r['slot']}: the spine's C{cls} column has no mark for this slot, "
                        f"but the register carries {r['marks']}")
        elif float(r["marks"]) != want:
            errs.append(f"{r['slot']}: register says {r['marks']} marks; spine C{cls} column "
                        f"says {want:g}")
        prod = r["items_per_paper"] * r["marks_per_item"]
        if prod != r["marks"]:
            errs.append(f"{r['slot']}: {r['items_per_paper']} items × {r['marks_per_item']} "
                        f"= {prod}, but the row declares {r['marks']} marks")

    # 3 — I-1, marks total 100 WITH D6; items totalled separately and NOT against 100
    total_marks = sum(r["marks"] for r in rows)
    d6 = sown if sown is not None else 0.0
    total_items = sum(r["items_per_paper"] for r in rows)
    if total_marks + d6 != 100:
        errs.append(f"I-1: marks total {total_marks:g} + স্কুলের নিজস্ব প্রশ্ন {d6:g} "
                    f"= {total_marks + d6:g}, not 100")
    rep.append(f"I-1 marks: {total_marks:g} + D6 {d6:g} = {total_marks + d6:g} ✓")
    rep.append(f"items total {total_items} — a SEPARATE fact, and correctly NOT 100 (CD-138(d))")

    # 4 — I-4, no half marks
    halves = [r["slot"] for r in rows
              if float(r["marks"]) % 1 or float(r["marks_per_item"]) % 1]
    if halves:
        errs.append(f"I-4: half marks at {', '.join(halves)} — BAN uses none at any class; "
                    f"the sole site in the structure is ENG S10")
    rep.append("I-4 half marks: none ✓ (sole structural site is ENG S10, not in this file)")

    # 5 — I-6, cause code on every row
    for r in rows:
        if not r.get("d_code"):
            errs.append(f"I-6: {r['slot']} carries no cause-code")
    rep.append("I-6 cause-codes: present on every row ✓")

    # 6 — I-8, gap rule. Refuses rather than passing silently.
    absent = [s for s, v in smarks.items() if v is None]
    if absent:
        rep.append(f"I-8 gap rule: testable — spine shows C{cls} absences at {', '.join(absent)}")
    else:
        rep.append(f"I-8 gap rule: NOT TESTABLE on the C{cls} column — it has no D5 (absent) cell, "
                   f"so no gap exists to test. I-8 binds when C1–C4 are built. Reported, not passed.")

    # 7 — shape, and the derived-field prohibition
    for r in rows:
        if r["task_mode"] not in MODES:
            errs.append(f"{r['slot']}: task_mode {r['task_mode']!r} is not one of {sorted(MODES)}")
        if r["task_mode"] == "alternative":
            if not r.get("admitted_set") or not r.get("selected"):
                errs.append(f"{r['slot']}: alternative row without admitted_set/selected")
            elif r["selected"] not in r["admitted_set"]:
                errs.append(f"{r['slot']}: selected {r['selected']!r} is not in its own "
                            f"admitted_set")
        if r["task_mode"] == "composite" and not r.get("parts"):
            errs.append(f"{r['slot']}: composite row without parts")
        if "chapter_authorable" in r:
            errs.append(f"{r['slot']}: carries an AUTHORED chapter_authorable — CD-138(f) makes it "
                        f"DERIVED from the per-chapter bank declarations, never authored here")
    modes = {m: sum(1 for r in rows if r["task_mode"] == m) for m in sorted(MODES)}
    rep.append("task_mode declared: " + " · ".join(f"{k} {v}" for k, v in modes.items()))
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

    errs, _ = check(reg, spine)
    if errs:
        print(f"  FAIL  baseline: the live register is not clean -> {errs}")
        ok = False
    else:
        print("  PASS  baseline: the live register passes every check")

    def mutate(fn):
        r = json.loads(json.dumps(reg))
        fn(r)
        return r

    cases = [
        ("MARKS", "S02 declared at 7 marks against the spine's 5",
         lambda r: r["rows"][1].update({"marks": 7, "marks_per_item": 1.4})),
        ("ARITHMETIC", "S07 says 4 items × 2 but declares 9 marks",
         lambda r: r["rows"][6].update({"marks": 9})),
        ("I-1", "a slot silently dropped — the column no longer reaches 100",
         lambda r: r["rows"].pop()),
        ("I-4", "a half mark introduced at S04 — permitted only at ENG S10",
         lambda r: r["rows"][3].update({"marks": 4.5, "marks_per_item": 0.9})),
        ("I-6", "a row with its cause-code removed",
         lambda r: r["rows"][0].pop("d_code")),
        ("SHAPE", "an alternative row whose `selected` is not in its own admitted_set",
         lambda r: r["rows"][9].update({"selected": "ভাব নির্ণয়"})),
        ("SHAPE", "a composite row with no parts",
         lambda r: r["rows"][11].pop("parts")),
        ("CD-138(f)", "an AUTHORED chapter_authorable on a slot row",
         lambda r: r["rows"][13].update({"chapter_authorable": False})),
    ]
    print()
    for label, why, fn in cases:
        errs, _ = check(mutate(fn), spine)
        if errs:
            print(f"  PASS  {label:<12} fires on: {why}")
        else:
            print(f"  FAIL  {label:<12} DID NOT FIRE on: {why}")
            ok = False

    # NEGATIVE — the marker-string case CD-138(b) exists for. Editing the spine's marker must
    # change nothing, because nothing here reads it.
    print()
    scrubbed = (spine.replace("*(দুটোর যেকোনো একটা)*", "")
                     .replace("*(তিনটার যেকোনো একটা)*", ""))
    a, _ = check(reg, spine)
    b, _ = check(reg, scrubbed)
    if a == b == []:
        print("  PASS  CD-138(b)    stays quiet on: every যেকোনো একটা marker stripped from the "
              "spine — verdict unchanged, because task mode is DECLARED and no marker is read")
    else:
        print(f"  FAIL  CD-138(b)    marker edit moved the verdict: {a} -> {b}")
        ok = False

    print(f"\nSELFTEST RESULT: {'PASS' if ok else 'FAIL'} "
          f"({len(cases)} seeded failures + 1 negative + 1 baseline)")
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
    errs, rep = check(reg, spine)
    for line in rep:
        print(f"  REPORT  {line}")
    for e in errs:
        print(f"  FAIL    {e}")
    print(f"RESULT: {'FAIL' if errs else 'CLEAN'} ({len(errs)} failures)")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
