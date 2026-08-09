#!/usr/bin/env python3
"""source_check.py — executes SOURCE_POLICY.md §5 against a source extraction.

SOURCE_POLICY §6 recorded that §5 had no executing script: "It is written when the
first extraction under this policy is built." This is that script.

The four §5 conditions, one check each:

  1. RANGE   every chapter/unit in the stated range is present as a section
  2. SLOTS   every spine slot for the class-subject is cross-referenced, or
             explicitly marked absent
  3. PAGES   page numbers are monotonic against the recorded offset
  4. SIGNOFF the spot-check sign-off is present in the file header

Checks 1-3 are FAIL-able by the agent. Check 4 can only be closed by the Principal
or the teacher, so it reports PENDING, never PASS-by-agent. Exit code is non-zero
unless all four are PASS, so a PENDING sign-off can never be mistaken for "done".

Usage:
    python tools/audits/source_check.py canon/_wip/c5-english/C5_ENG_Source_01.md
    python tools/audits/source_check.py --selftest

The path is given, not assumed: an extraction lives under a `_wip/` folder until the
Principal signs its spot-check off, and only then moves to `canon/sources/<class>/<subject>/`
(AGENTS.md §3). The gate runs identically in both places.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SPINE = {
    "ENG": REPO / "canon/marklogic/MarkLogic_ENG_Spine.md",
    "BAN": REPO / "canon/marklogic/MarkLogic_BAN_Spine.md",
    "MATH": REPO / "canon/marklogic/MarkLogic_MATH_Spine.md",
    "SCI-BGS": REPO / "canon/marklogic/MarkLogic_SCI_BGS_Spine.md",
}

BN_DIGITS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")


def dg(s: str) -> str:
    """Bengali digits -> ASCII. Extractions carry both by design."""
    return s.translate(BN_DIGITS)


# --------------------------------------------------------------------------- parse

def parse_scope(text: str):
    """Read the '**এই ফাইলের অংশ:**' line -> (units, first_page, last_page)."""
    m = re.search(r"\*\*এই ফাইলের অংশ:\*\*(.+)", text)
    if not m:
        return None
    line = dg(m.group(1))
    units = re.search(r"Unit\s+(\d+)(?:\s*[–-]\s*(\d+))?", line)
    pages = re.search(r"ছাপা পৃষ্ঠা\s*(\d+)\s*[–-]\s*(\d+)", line)
    if not units or not pages:
        return None
    lo = int(units.group(1))
    hi = int(units.group(2)) if units.group(2) else lo
    return list(range(lo, hi + 1)), int(pages.group(1)), int(pages.group(2))


def parse_offset_table(text: str):
    """Rows of the offset table -> [(pdf_page, printed_folio), ...].

    Scoped to the '## পৃষ্ঠা-অফসেট' section on purpose: an unscoped numeric-row scan
    swallows every other two-column table in the file and reports a phantom
    inconstant offset. Caught by this gate's own first run, 2026-08-09.
    """
    sec = re.search(r"^## পৃষ্ঠা-অফসেট.*?(?=^## |\Z)", text, re.M | re.S)
    if not sec:
        return []
    rows = []
    for line in sec.group(0).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        a, b = dg(cells[0]), dg(cells[1])
        if re.fullmatch(r"\d+", a) and re.fullmatch(r"\d+", b):
            rows.append((int(a), int(b)))
    return rows


def parse_subject(path: Path):
    m = re.match(r"C(\d)_([A-Za-z\-]+)_Source_", path.name)
    return (m.group(1), m.group(2).upper()) if m else (None, None)


def spine_slots(subject: str):
    f = SPINE.get(subject)
    if not f or not f.exists():
        return None
    return sorted(set(re.findall(r"^### `([A-Z\-]+-[SL]\d\d)`", f.read_text(encoding="utf-8"), re.M)))


# -------------------------------------------------------------------------- checks

def check_range(text, scope):
    units, _, _ = scope
    missing = [u for u in units if not re.search(rf"^#\s+Unit\s+{u}\b", dg(text), re.M)]
    if missing:
        return "FAIL", f"stated range Unit {units[0]}-{units[-1]}: no section for Unit " + ", ".join(map(str, missing))
    return "PASS", f"stated range Unit {units[0]}-{units[-1]}: all {len(units)} section(s) present"


def check_slots(text, subject):
    slots = spine_slots(subject)
    if slots is None:
        return "FAIL", f"no spine file registered for subject {subject}"
    m = re.search(r"^## MarkLogic স্লট মিলকরণ.*?(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return "FAIL", "no 'MarkLogic স্লট মিলকরণ' section"
    cited = set(re.findall(r"([A-Z\-]+-[SL]\d\d)", m.group(0)))
    missing = [s for s in slots if s not in cited]
    if missing:
        return "FAIL", f"{len(missing)} spine slot(s) neither cross-referenced nor marked absent: " + ", ".join(missing)
    return "PASS", f"all {len(slots)} {subject} spine slots accounted for"


def check_pages(text, scope, offset_rows):
    _, first, last = scope
    if len(offset_rows) < 2:
        return "FAIL", "offset table has fewer than 2 verified rows"
    offsets = {p - f for p, f in offset_rows}
    if len(offsets) != 1:
        return "FAIL", f"offset is not constant across verified rows: {sorted(offsets)}"
    offset = offsets.pop()
    folios = [f for _, f in offset_rows]
    if folios != sorted(folios):
        return "FAIL", f"verified folios are not monotonic: {folios}"
    body = dg(text)
    inline = [int(x) for x in re.findall(r"\(পৃষ্ঠা\s*(\d+)", body)]
    out = [p for p in inline if not (first <= p <= last)]
    if out:
        return "FAIL", f"page reference(s) outside stated range {first}-{last}: {out}"
    if inline != sorted(inline):
        return "FAIL", f"in-body page references are not monotonic: {inline}"
    return "PASS", (f"offset constant (+{offset}) over {len(offset_rows)} verified rows; "
                    f"{len(inline)} in-body refs monotonic within {first}-{last}")


def check_signoff(text):
    m = re.search(r"^## স্পট-চেক সই.*?(?=^---|\Z)", text, re.M | re.S)
    if not m:
        return "FAIL", "no spot-check sign-off section in header"
    block = m.group(0)
    rows = [l for l in block.splitlines() if l.strip().startswith("|") and "—" in l or
            (l.strip().startswith("|") and re.search(r"\|\s*[^|\s—-]+\s*\|\s*\d", l))]
    data = [l for l in block.splitlines()
            if l.strip().startswith("|") and not re.match(r"^\|[\s\-:|]+\|$", l.strip())]
    data = [l for l in data if "যাচাই করার অংশ" not in l]
    if not data:
        return "FAIL", "sign-off table has no rows"
    unsigned = [l for l in data if re.search(r"\|\s*—\s*\|\s*—\s*\|", l)]
    if unsigned:
        return "PENDING", (f"{len(unsigned)} of {len(data)} spot-check row(s) unsigned — "
                           "only the Principal or the teacher can close this")
    return "PASS", f"all {len(data)} spot-check row(s) signed"


# ----------------------------------------------------------------------------- run

def run(path: Path):
    text = path.read_text(encoding="utf-8")
    cls, subject = parse_subject(path)
    scope = parse_scope(text)
    results = []
    if scope is None:
        results.append(("RANGE", "FAIL", "cannot read the '**এই ফাইলের অংশ:**' scope line"))
        results.append(("PAGES", "FAIL", "skipped — scope unreadable"))
    else:
        results.append(("RANGE",) + check_range(text, scope))
        results.append(("PAGES",) + check_pages(text, scope, parse_offset_table(text)))
    results.append(("SLOTS",) + check_slots(text, subject))
    results.append(("SIGNOFF",) + check_signoff(text))
    order = {"RANGE": 0, "SLOTS": 1, "PAGES": 2, "SIGNOFF": 3}
    results.sort(key=lambda r: order[r[0]])

    print(f"source_check.py — SOURCE_POLICY.md §5")
    print(f"file    : {path.relative_to(REPO)}")
    print(f"subject : class {cls} · {subject}")
    print("-" * 78)
    for name, status, detail in results:
        print(f"[{status:7}] {name:8} {detail}")
    print("-" * 78)
    statuses = {r[1] for r in results}
    if "FAIL" in statuses:
        verdict, code = "RED — returns to build phase (AGENTS.md §5)", 2
    elif "PENDING" in statuses:
        verdict, code = "NOT DONE — mechanical checks pass; spot-check sign-off owed", 1
    else:
        verdict, code = "GREEN", 0
    print(f"VERDICT : {verdict}")
    return code


# ------------------------------------------------------------------------ selftest

def selftest():
    """Seeded-error negative test (handoff §2 evidence rules): a gate that has never
    been shown to go red on a known-bad input has not been shown to do anything."""
    import tempfile
    # The fixture is whichever C5 English extraction is on disk — Unit 1 moved out of _wip
    # when it was signed off, and a selftest that dies because its fixture was promoted is a
    # selftest nobody runs.
    src = next((p for p in sorted(
        list((REPO / "canon/sources/c5/english").glob("C5_ENG_Source_*.md")) +
        list((REPO / "canon/_wip/c5-english").glob("C5_ENG_Source_*.md")))), None)
    if src is None:
        print("SELFTEST: no extraction on disk to mutate — nothing to prove against")
        return 2
    good = src.read_text(encoding="utf-8")

    # The seeds are derived from the fixture, not hard-coded against one unit's wording.
    # Hard-coded seeds silently stopped seeding the moment the fixture changed, and a seed
    # that no longer bites reports a green selftest for a gate nobody tested.
    def bump_unit(t):
        return re.sub(r"^#\s+Unit\s+(\d+)", lambda m: f"# Unit {int(m.group(1)) + 40}", t,
                      count=1, flags=re.M)

    def drop_slot(t):
        # Every occurrence, because the cross-reference may be one grouped row or one row per
        # slot — removing only the first left the table still resolving and the seed toothless.
        return t.replace("S09", "S91")

    def break_offset(t):
        return re.sub(r"^\| (\d+) \| (\d+) \|", lambda m: f"| {m.group(1)} | {int(m.group(2))+1} |",
                      t, count=1, flags=re.M)

    def page_out_of_range(t):
        return re.sub(r"\(পৃষ্ঠা\s*([০-৯\d]+)", lambda m: "(পৃষ্ঠা ৯৯৯", t, count=1)

    def pages_out_of_order(t):
        hits = list(re.finditer(r"\(পৃষ্ঠা\s*([০-৯\d]+)", t))
        if len(hits) < 2:
            return t
        last = hits[-1]
        return t[:last.start()] + "(পৃষ্ঠা ১" + t[last.end():]

    seeds = [
        ("RANGE  · the stated unit has no section", bump_unit),
        ("SLOTS  · one spine slot dropped from the cross-reference", drop_slot),
        ("PAGES  · offset broken on one row", break_offset),
        ("PAGES  · in-body page reference outside the stated range", page_out_of_range),
        ("PAGES  · in-body page references out of order", pages_out_of_order),
    ]
    print(f"fixture : {src.relative_to(REPO)}")
    print("SELFTEST — every seeded error must turn the gate RED")
    print("-" * 78)
    ok = True
    with tempfile.TemporaryDirectory() as d:
        for label, mutate in seeds:
            bad = mutate(good)
            if bad == good:
                print(f"[BROKEN ] {label} — seed did not change the file")
                ok = False
                continue
            p = Path(d) / src.name
            p.write_text(bad, encoding="utf-8")
            text, cls_subj = p.read_text(encoding="utf-8"), parse_subject(p)
            scope = parse_scope(text)
            rs = []
            if scope:
                rs.append(check_range(text, scope)[0])
                rs.append(check_pages(text, scope, parse_offset_table(text))[0])
            rs.append(check_slots(text, cls_subj[1])[0])
            red = "FAIL" in rs
            print(f"[{'RED    ' if red else 'MISSED '}] {label}")
            ok = ok and red
        # and the unmutated file must NOT be red
        p = Path(d) / src.name
        p.write_text(good, encoding="utf-8")
        scope = parse_scope(good)
        rs = [check_range(good, scope)[0], check_pages(good, scope, parse_offset_table(good))[0],
              check_slots(good, "ENG")[0]]
        clean = "FAIL" not in rs
        print(f"[{'CLEAN  ' if clean else 'FALSE+ '}] control · unmutated file must not be red")
        ok = ok and clean
    print("-" * 78)
    print(f"SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 2


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "--selftest":
        sys.exit(selftest())
    sys.exit(run(Path(args[0]) if Path(args[0]).is_absolute() else REPO / args[0]))
