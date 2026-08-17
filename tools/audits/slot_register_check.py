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
  4. I-4        — no half marks EXCEPT `HALF_MARK_ADMITTED`, a closed literal in this file:
                  `{("ENG", "S10")}` only, per Rules I-4 / §৪ and CD-150. The exception is keyed
                  (subject, slot) and is NOT readable from the register — a data row must not be
                  able to silence an invariant.
  5. I-6        — no row without a cause-code (`d_code`).
  6. I-8        — gap rule, **computed from the register**: a slot present at class X and again at
                  X+2 must be present at X+1. A leading absence that ends once the slot starts is a
                  prefix, not a gap, and must not fire.
  7. SHAPE      — `task_mode` ∈ {alternative, composite, simple}; alternative rows carry
                  `admitted_set` and either `selected` ∈ `admitted_set` OR the declared
                  UNSELECTED state (`selected: null` + a non-empty `unselected_reason`);
                  composite rows
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
SPINES = {"BAN": ROOT / "canon" / "marklogic" / "MarkLogic_BAN_Spine.md",
          "ENG": ROOT / "canon" / "marklogic" / "MarkLogic_ENG_Spine.md",
          # MATH is listed ahead of its rows. `run_everything` loops `scope_built`, so an unbuilt
          # subject is never read; listing it early costs nothing and means the day MATH rows land
          # they are proven rather than skipped.
          "MATH": ROOT / "canon" / "marklogic" / "MarkLogic_MATH_Spine.md",
          # ── SEED-ONLY, and it must stay fictional ──────────────────────────────────────────
          # `SYN` is not a subject. It exists so `SUBJECT-BLIND` has a target that is KNOWN to this
          # file and that the register can NEVER build, and it is pointed at BAN's spine only
          # because the seed never gets far enough to parse it.
          # WHY IT IS NOT A REAL SUBJECT (TOOLS-CR-007): the seed first targeted ENG, then MATH.
          # Both are in `scope_owed` — subjects the repo is SCHEDULED to build — so each target
          # was a lie with an expiry date, and the seed passes the moment the lie comes true.
          # A fixture premise the repo can satisfy is not a fixture (QB-D-012 / CD-121(e)).
          "SYN": ROOT / "canon" / "marklogic" / "MarkLogic_BAN_Spine.md"}
CLASSES = (1, 2, 3, 4, 5)

# I-4's ONLY exception, as a CLOSED LITERAL IN THE PROVER — deliberately NOT a register field.
#
# `MarkLogic_Rules.md` I-4: আধা নম্বর (০.৫) ব্যবহার করা যাবে না — একমাত্র ব্যতিক্রম যেখানে নেপের
# কাঠামো নিজেই আধা নম্বর ব্যবহার করে … বর্তমানে এমন জায়গা একটাই: ইংরেজির S10. §৪ carries the
# reason the exception exists at all: আমাদের নিয়মগুলো নেপ থেকে আসে — নেপের বিরুদ্ধে যেতে পারে না …
# এই কারণেই I-4-তে আধা নম্বরের ব্যতিক্রমটা আছে. Enumerated at CD-150.
#
# WHY A LITERAL AND NOT A REGISTER FIELD (Principal ruling 2026-08-16). A `half_mark_admitted` key
# in `SLOT_REGISTER.json` would let the file under examination name its own exemptions: the row
# carrying the half mark would also carry the permission for it, and **I-4 would be unfalsifiable
# by construction.** A data row must not be able to silence an invariant. Same class of finding as
# CD-137 — there a frozen baseline was allowed to admit imported HISTORY the check cannot see,
# while the agent's own NEW writing was FIXED rather than exempted, and that distinction was the
# whole of the row. Widening this set is a Principal decision and takes a CD row, exactly as
# re-freezing `SB_CITATION_BASELINE.md` does.
#
# Keyed (subject, slot-short), never slot-short alone — see `half_mark_offenders`.
HALF_MARK_ADMITTED = {("ENG", "S10")}

# THE ONLY (subject, class, slot) THAT MAY DECLARE A `taught_set`, AND IT IS A LITERAL HERE FOR
# EXACTLY THE REASON ABOVE (Principal ruling 2026-08-17, CD-165).
#
# `taught_set` names the বিরামচিহ্ন a class is TAUGHT — দাঁড়ি · কমা · প্রশ্নচিহ্ন · বিস্ময়চিহ্ন at
# C5, with ড্যাশ and সেমিকোলন excluded. It is DATA, correctly: the marks are a fact about the C5
# book, they change per class, and CD-155's UNSELECTED precedent gives the form (a declaration
# carries its own source, or it is indistinguishable from an unfilled field).
#
# WHAT IS *NOT* DATA IS WHICH ROWS MAY DECLARE ONE. Left open, any row could mint itself a mark set
# — and the one place a wrong mark set is invisible is the row that also grants itself permission
# to have one. The set is C5-only because THE SPINE ITSELF DOES NOT TRANSFER IT DOWNWARD: its C2
# row names দাঁড়ি, কমা, প্রশ্নবোধক from যোগ্যতা ১৩.২, and its C3, C4 and C5 rows name NO mark at
# all. A C4 row carrying C5's four would therefore be an invention with a data row's authority,
# which is the CD-137 laundering shape one more time.
#
# ABSENCE IS NOT PERMISSION. A row with no `taught_set` has declared NOTHING, and the bank gate
# reads that as "no mark is admitted here yet", never as "every mark is". That half is enforced in
# `workstreams/question-banks/audits/gates.py`, where the items are.
TAUGHT_SET_DECLARABLE = {("BAN", 5, "BAN-S11")}

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


def half_mark_offenders(rows, subject):
    """→ [slot ids] carrying a half mark that `HALF_MARK_ADMITTED` does not admit.

    **Keyed on (subject, slot-short), not on the slot short alone.** `S10` is admitted for ENG and
    barred for BAN, and the two subjects\' S10 are different questions entirely — ENG-S10 is
    Capitals & punctuation at 0.5×10=5, BAN-S10 is পদ নির্ণয় at 1×5=5. A slot-only test would
    admit a half mark into BAN-S10 on the strength of a ruling about English, and the register
    would carry an I-4 breach that no check could see.

    Both `marks` and `marks_per_item` are tested. ENG-S10 is exactly the shape that makes the
    second one necessary: its `marks` is the whole number 5 and the 0.5 lives only in
    `marks_per_item`, so a test that read `marks` alone would call it integral and move on.
    """
    out = []
    for r in rows:
        short = str(r.get("slot", "")).split("-")[-1]
        half = (float(r.get("marks") or 0) % 1) or (float(r.get("marks_per_item") or 0) % 1)
        if half and (subject, short) not in HALF_MARK_ADMITTED:
            out.append(r["slot"])
    return out


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

    # 4 — I-4, with its one admitted exception (HALF_MARK_ADMITTED, closed literal above)
    offenders = half_mark_offenders(rows, subject)
    if offenders:
        errs.append(f"I-4: half mark(s) at C{cls} {', '.join(offenders)} — আধা নম্বর is barred "
                    f"except where NAPE\'s own structure uses it (Rules I-4, §৪). The admitted "
                    f"set is {sorted(HALF_MARK_ADMITTED)} and nothing else, and it is a literal "
                    f"in this file: widening it takes a CD row, never a register field")

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
            # UNSELECTED (Principal ruling 2026-08-16) — `selected: null` plus a REQUIRED
            # `unselected_reason`, for a class whose source names more than one form and narrows
            # to none. The reason is not decoration: it is the ONLY thing distinguishing "no
            # source narrowed this" from "the author forgot to fill the field in", and a bare
            # null therefore FAILs. This mirrors D5/`absent_reason` exactly — the register already
            # holds that an assertion of nothing must still say why.
            if not r.get("admitted_set"):
                errs.append(f"C{cls} {r['slot']}: alternative row without admitted_set")
            elif r.get("selected") is None:
                if not str(r.get("unselected_reason", "")).strip():
                    errs.append(f"C{cls} {r['slot']}: `selected` is null with no "
                                f"`unselected_reason` — UNSELECTED is a DECLARATION that no "
                                f"source narrowed the choice, and a bare null is "
                                f"indistinguishable from an unfilled field (same rule as D5's "
                                f"`absent_reason`)")
            elif r["selected"] not in r["admitted_set"]:
                errs.append(f"C{cls} {r['slot']}: selected {r['selected']!r} is not in its own "
                            f"admitted_set")
        if r["task_mode"] == "composite" and not r.get("parts"):
            errs.append(f"C{cls} {r['slot']}: composite row without parts")

    # 10 — TAUGHT SET shape (CD-165). Three failures, and each is a different lie:
    #   * a row declaring a mark set where no ruling admits one  → permission minted by data
    #   * a set with no `taught_set_source`                      → an untraceable declaration
    #   * an empty set                                           → "taught nothing", which is what
    #     ABSENCE already says, so an empty list is a filled-in field carrying no claim
    for r in rows:
        key = (subject, cls, r["slot"])
        has_set = "taught_set" in r
        has_src = str(r.get("taught_set_source", "")).strip()
        if has_set and key not in TAUGHT_SET_DECLARABLE:
            errs.append(f"C{cls} {r['slot']}: carries a `taught_set`, and only "
                        f"{sorted(TAUGHT_SET_DECLARABLE)} may — the set of marks a class is taught "
                        f"is data, but WHICH ROW MAY DECLARE ONE is a literal in this prover "
                        f"(CD-165). The spine names marks at C2 only and names none at C3–C5, so a "
                        f"set on any other row is an invention wearing a data row's authority")
        if has_set:
            ts = r["taught_set"]
            if not isinstance(ts, list) or not ts or not all(
                    isinstance(m, str) and m.strip() for m in ts):
                errs.append(f"C{cls} {r['slot']}: `taught_set` must be a non-empty list of "
                            f"non-empty mark names — an EMPTY set claims the class is taught no "
                            f"mark, which is what ABSENCE of the field already declares (CD-165)")
            if len(set(ts)) != len(ts):
                errs.append(f"C{cls} {r['slot']}: `taught_set` repeats a mark name")
            if not has_src:
                errs.append(f"C{cls} {r['slot']}: `taught_set` with no `taught_set_source` — the "
                            f"UNSELECTED precedent (CD-155) governs the form: a declaration that "
                            f"cannot be traced to where it comes from is indistinguishable from an "
                            f"unfilled field")
        elif has_src:
            errs.append(f"C{cls} {r['slot']}: carries `taught_set_source` with no `taught_set` — a "
                        f"citation for a declaration that was never made")
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


def subjects_built(reg):
    """The SUBJECTS the register declares built, from its own `scope_built`.

    The sibling of `built_classes`, one dimension up, and it exists for the same reason. The
    C1–C4 repair recorded in the module docstring was a checker that read ONE COLUMN and could not
    say so. Adding ENG re-created that defect one axis over: `main()` read the BAN spine at the
    `subject="BAN"` default, so ENG rows would have been filtered out of every check and the
    script would have printed `RESULT: CLEAN` over a subject it never opened. **A register whose
    new SUBJECT was never read, reported as clean.** This function is what makes that impossible;
    the `SUBJECT-BLIND` seed is what keeps it impossible.
    """
    out = []
    for entry in reg.get("scope_built", []):
        m = SCOPE.match(entry.strip())
        if m and m.group(1) not in out:
            out.append(m.group(1))
    return out


def run_everything(reg):
    """Every subject `scope_built` declares, each against its OWN spine. Refuses, never skips."""
    errs, rep = [], []
    subs = subjects_built(reg)
    if not subs:
        return (["the register declares no subject in `scope_built` — nothing here is provable, "
                 "and an unprovable register is not a clean one"], rep)
    rep.append(f"SUBJECTS read from the register\'s own `scope_built`: {', '.join(subs)}")
    for sub in subs:
        path = SPINES.get(sub)
        if path is None:
            errs.append(f"{sub} is declared built in `scope_built`, but this file knows no spine "
                        f"for it. REFUSED rather than skipped — an unread subject must never be "
                        f"reported clean (SOURCE_POLICY §7.17)")
            continue
        if not path.exists():
            errs.append(f"{sub}: spine {path} not found — declared built against a file that is "
                        f"not there")
            continue
        rep.append(f"----- {sub}  [spine {path.relative_to(ROOT)}]")
        e, r = run_all(reg, path.read_text(encoding="utf-8"), sub)
        errs += e
        rep += r
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
    subj_rows = [r for r in reg["rows"] if r["subject"] == subject]
    admitted = [r for r in subj_rows
                if ((float(r.get("marks") or 0) % 1) or (float(r.get("marks_per_item") or 0) % 1))
                and (subject, str(r["slot"]).split("-")[-1]) in HALF_MARK_ADMITTED]
    admitted_slots = sorted({r["slot"] for r in admitted})
    rep.append(f"I-4 {subject}: {len(half_mark_offenders(subj_rows, subject))} UNADMITTED "
               f"half-mark row(s) ✓ · {len(admitted)} row(s) carrying the admitted exception"
               + (f" at {', '.join(admitted_slots)} (C"
                  + ", C".join(str(r["class"]) for r in sorted(admitted, key=lambda x: -x["class"]))
                  + ")" if admitted else " — none in this subject"))
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

    errs, _ = run_everything(reg)
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
        ("UNSELECTED", "`selected` nulled with NO `unselected_reason` — a bare null is an "
                       "unfilled field, not a declaration",
         lambda r: row(r, 5, "BAN-S10").update({"selected": None})),
        ("UNSELECTED", "`selected` nulled with an EMPTY-STRING reason — whitespace is not a "
                       "reason either",
         lambda r: row(r, 5, "BAN-S10").update({"selected": None, "unselected_reason": "   "})),
        ("SHAPE", "a composite row with no parts",
         lambda r: row(r, 5, "BAN-S12").pop("parts")),
        ("CD-138(f)", "an AUTHORED chapter_authorable on a slot row",
         lambda r: row(r, 5, "BAN-S14").update({"chapter_authorable": False})),
        # ── CD-165, seeded BOTH ways: the three lies above, and the negatives below ────
        ("TAUGHT SET", "a `taught_set` on a row no ruling admits one for — C4 S11 helping itself "
                       "to C5's four marks, which the spine names at neither class",
         lambda r: row(r, 4, "BAN-S11").update({"taught_set": ["দাঁড়ি", "কমা"],
                                                "taught_set_source": "C5-এর সারি থেকে"})),
        ("TAUGHT SET", "the C5 set emptied — 'taught no mark' is what ABSENCE already says, so an "
                       "empty list is a filled field carrying no claim",
         lambda r: row(r, 5, "BAN-S11").update({"taught_set": []})),
        ("TAUGHT SET", "the C5 set with its `taught_set_source` removed — an untraceable "
                       "declaration, barred on CD-155's precedent",
         lambda r: row(r, 5, "BAN-S11").pop("taught_set_source")),
        ("TAUGHT SET", "a `taught_set_source` left behind after the set it cites was removed",
         lambda r: row(r, 5, "BAN-S11").pop("taught_set")),
        ("TAUGHT SET", "the C5 set repeating a mark",
         lambda r: row(r, 5, "BAN-S11").update({"taught_set": ["দাঁড়ি", "কমা", "কমা",
                                                              "প্রশ্নচিহ্ন", "বিস্ময়চিহ্ন"]})),
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

    # ── the SUBJECT axis — the C1–C4 repair\'s defect one dimension up ─────────────────────
    cases += [
        ("SUBJECT-BLIND", "a subject DECLARED built in scope_built with not one row to its name — "
                          "the shape of `a column that was never read, reported clean`. Targets "
                          "the FICTIONAL subject `SYN`, never a scope_owed one: pointed at ENG it "
                          "died the day ENG was built, and pointed at MATH it would die again "
                          "(TOOLS-CR-007)",
         lambda r: r["scope_built"].append("SYN C1-C5")),
        ("SUBJECT-REFUSAL", "a subject declared built for which this file knows NO spine — must "
                            "refuse by name, never skip. Targets `ZZZ`, which is in no spine map "
                            "and on no roadmap, for the same reason",
         lambda r: r["scope_built"].append("ZZZ C1-C5")),
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
        errs, _ = run_everything(mutated)
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

    # UNSELECTED, the QUIET direction — a nulled `selected` WITH a reason is accepted, and the
    # rest of the row is still checked. Asserted on the live register so it is not vacuous.
    try:
        mut = mutate(lambda r: row(r, 5, "BAN-S10").update(
            {"selected": None, "unselected_reason": "কল্পিত — কোনো সূত্র সংকীর্ণ করেনি"}))
    except RowNotBuilt as e:
        print(f"  HELD  UNSELECTED   quiet-direction not exercisable yet  [needs {e}]")
    else:
        eu, _ = run_everything(mut)
        if not eu:
            print("  PASS  UNSELECTED   stays quiet on: `selected: null` WITH an "
                  "`unselected_reason` — the declared state, accepted, and every other check on "
                  "the row still ran")
        else:
            print(f"  FAIL  UNSELECTED   a properly declared UNSELECTED row was not accepted: {eu}")
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

    # ── I-4's ADMITTED EXCEPTION, both directions ───────────────────────────────────────
    # Asserted on `half_mark_offenders` DIRECTLY as well as through the run, and the direct half is
    # the one that is not vacuous today: ENG is not in `scope_built` at this commit, so a synthetic
    # ENG row pushed through `run_everything` would be filtered out before any check saw it and a
    # "stayed quiet" verdict would mean nothing at all. The rows below are SYNTHETIC (CD-121(e) —
    # seeds may not be drawn from live data).
    print()
    eng_s10 = [{"slot": "ENG-S10", "marks": 5, "marks_per_item": 0.5}]
    i4_cases = [
        ("ENG-S10 0.5 under ENG", eng_s10, "ENG", [],
         "the admitted exception — quiet, and this is the whole point of the row"),
        ("ENG-S10 0.5 under BAN", eng_s10, "BAN", ["ENG-S10"],
         "SAME slot short, WRONG subject — the pair is keyed (subject, slot), so a ruling about "
         "English cannot admit a half mark into BAN-S10 (পদ নির্ণয়, 1x5)"),
        ("BAN-S10 0.5 under BAN", [{"slot": "BAN-S10", "marks": 5, "marks_per_item": 0.5}], "BAN",
         ["BAN-S10"], "BAN\'s own S10 — barred, and it is the case a slot-only test would miss"),
        ("ENG-S09 0.5 under ENG", [{"slot": "ENG-S09", "marks": 4.5, "marks_per_item": 0.5}], "ENG",
         ["ENG-S09"], "right subject, WRONG slot — the exception is one slot wide, not one "
                      "subject wide"),
        ("ENG-S10 whole under ENG", [{"slot": "ENG-S10", "marks": 5, "marks_per_item": 1}], "ENG",
         [], "no half mark present at all — admitted does not mean expected"),
        ("marks whole, per-item half", [{"slot": "MATH-S03", "marks": 5, "marks_per_item": 0.5}],
         "MATH", ["MATH-S03"], "`marks` is integral and the 0.5 hides in `marks_per_item` — "
                               "exactly ENG-S10\'s shape, which is why both fields are read"),
    ]
    for label, rows, subj, want, why in i4_cases:
        got = half_mark_offenders(rows, subj)
        if got == want:
            print(f"  PASS  I-4-EXC      {label:<24} -> {got if got else 'quiet'}: {why}")
        else:
            print(f"  FAIL  I-4-EXC      {label:<24} -> {got}, expected {want}: {why}")
            ok = False

    # and the WIRING, not only the helper: a half mark on a live BAN row must reach the verdict
    # carrying the I-4 label, because an error that fires under a different name teaches the wrong
    # remedy (the COLUMN-LABEL lesson, one check over).
    try:
        mut = mutate(lambda r: row(r, 5, "BAN-S04").update({"marks": 4.5, "marks_per_item": 0.9}))
    except RowNotBuilt as e:
        print(f"  HELD  I-4-WIRING   not exercisable yet  [needs {e}]")
    else:
        e2, _ = run_everything(mut)
        if any(m.startswith("I-4:") for m in e2):
            print("  PASS  I-4-WIRING   a live half mark reaches the verdict labelled I-4, naming "
                  "the admitted set and saying it is a literal, not a register field")
        else:
            print(f"  FAIL  I-4-WIRING   half mark did not surface as an I-4 failure: {e2}")
            ok = False

    print(f"\nSELFTEST RESULT: {'PASS' if ok else 'FAIL'} "
          f"({exercised} of {len(cases)} seeded failures exercised + 3 negatives + 1 baseline "
          f"+ {len(i4_cases)} I-4-exception assertions + 1 I-4 wiring check, across 5 class "
          f"columns and {len(subjects_built(reg))} subject(s))")
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
    print(f"\nREGISTER: {REGISTER.relative_to(ROOT)}  [authority {reg['authority']}, "
          f"built {reg['built']}, scope {', '.join(reg['scope_built'])}]")
    errs, rep = run_everything(reg)
    for line in rep:
        print(f"  REPORT  {line}")
    for e in errs:
        print(f"  FAIL    {e}")
    print(f"RESULT: {'FAIL' if errs else 'CLEAN'} ({len(errs)} failures)")
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
