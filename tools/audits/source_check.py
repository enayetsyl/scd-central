#!/usr/bin/env python3
"""source_check.py — executes SOURCE_POLICY.md §5 against a source extraction.

SOURCE_POLICY §6 recorded that §5 had no executing script: "It is written when the
first extraction under this policy is built." This is that script.

The four §5 conditions, one check each, plus one the §7 amendments added:

  1. RANGE   every chapter/unit in the stated range is present as a section
  2. SLOTS   every spine slot for the class-subject is cross-referenced, or
             explicitly marked absent
  3. PAGES   page numbers are monotonic against the recorded offset
  4. SIGNOFF the spot-check sign-off is present in the file header
  5. DEPTH   a single-channel source's sign-off rows are full checks, not samples

Checks 1-3 and 5 are FAIL-able by the agent. Check 4 can only be closed by the Principal
or the teacher, so it reports PENDING, never PASS-by-agent. Exit code is non-zero
unless all of them are PASS, so a PENDING sign-off can never be mistaken for "done".

**The chapter word is not always "Unit".** The first extraction under this policy was
English, so the scope line, the body heading and the selftest seeds were all written
against `Unit N`. C5 Bangla's chapters are `পাঠ N`, and a gate that reads the file's
grammar rather than its content would have failed RANGE and PAGES on a correct
extraction — reporting red for a reason that has nothing to do with the book. Both
words are read now, and the one the file actually uses is echoed in the output so the
reader can see which grammar was matched.

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

# The words a book divides itself into. English units, Bangla পাঠ. Order matters only
# for the message; a file uses one or the other, never both.
UNIT_WORDS = ("Unit", "পাঠ")
UNIT_RE = "(?:" + "|".join(UNIT_WORDS) + ")"


def dg(s: str) -> str:
    """Bengali digits -> ASCII. Extractions carry both by design."""
    return s.translate(BN_DIGITS)


# --------------------------------------------------------------------------- parse

def parse_scope(text: str):
    """Read the '**এই ফাইলের অংশ:**' line -> (units, first_page, last_page, word)."""
    m = re.search(r"\*\*এই ফাইলের অংশ:\*\*(.+)", text)
    if not m:
        return None
    line = dg(m.group(1))
    units = re.search(rf"({UNIT_RE})\s+(\d+)(?:\s*[–-]\s*(\d+))?", line)
    pages = re.search(r"ছাপা পৃষ্ঠা\s*(\d+)\s*[–-]\s*(\d+)", line)
    if not units or not pages:
        return None
    word = units.group(1)
    lo = int(units.group(2))
    hi = int(units.group(3)) if units.group(3) else lo
    return list(range(lo, hi + 1)), int(pages.group(1)), int(pages.group(2)), word


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
    units, _, _, word = scope
    missing = [u for u in units if not re.search(rf"^#\s+{word}\s+{u}(?!\d)", dg(text), re.M)]
    if missing:
        return "FAIL", f"stated range {word} {units[0]}-{units[-1]}: no section for {word} " + ", ".join(map(str, missing))
    return "PASS", f"stated range {word} {units[0]}-{units[-1]}: all {len(units)} section(s) present"


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
    _, first, last, _word = scope
    if len(offset_rows) < 2:
        return "FAIL", "offset table has fewer than 2 verified rows"
    offsets = {p - f for p, f in offset_rows}
    if len(offsets) != 1:
        return "FAIL", f"offset is not constant across verified rows: {sorted(offsets)}"
    offset = offsets.pop()
    folios = [f for _, f in offset_rows]
    if folios != sorted(folios):
        return "FAIL", f"verified folios are not monotonic: {folios}"
    everywhere = [int(x) for x in re.findall(r"\(পৃষ্ঠা\s*(\d+)", dg(text))]
    out = [p for p in everywhere if not (first <= p <= last)]
    if out:
        return "FAIL", f"page reference(s) outside stated range {first}-{last}: {out}"
    inline = [int(x) for x in re.findall(r"\(পৃষ্ঠা\s*(\d+)", dg(transcribed_body(text)))]
    if inline != sorted(inline):
        return "FAIL", f"page references in the transcribed body are not monotonic: {inline}"
    return "PASS", (f"offset constant (+{offset}) over {len(offset_rows)} verified rows; "
                    f"{len(inline)} body refs monotonic within {first}-{last}, "
                    f"{len(everywhere) - len(inline)} commentary/cross-ref refs in range")


RASTER_ONLY = ("টেক্সট-লেয়ারে নেই", "## ছবির ভেতরের লেখা")
RASTER_ROW = ("ছবির", "মানচিত্র", "লেবেল")

# Everything from the first of these headings on is the extraction talking about the book,
# not transcribing it. Kept in step with `source_textcheck.py`'s list of the same name.
COMMENTARY = ("## যেভাবে ছাপা আছে", "## এই ইউনিটে যা নেই", "## এই পাঠে যা নেই",
              "## এই ইউনিটে যে নামগুলো আছে", "## এই পাঠে যে নামগুলো আছে",
              "## MarkLogic স্লট মিলকরণ", "## প্রমাণ", "## সংশ্লিষ্ট নথি")


def transcribed_body(text: str) -> str:
    """The transcription only — commentary and cross-reference cut off.

    The monotonicity rule is about the order the book is transcribed in. Commentary cites
    pages in whatever order the point needs, and a cross-reference table cites them per
    slot, so scanning the whole file made a correct extraction look like it jumped from
    page 5 back to page 1. The English Unit 1 file passed the unscoped version only because
    it happened to put its page numbers in a column rather than in prose — luck, not design,
    and the same class of unscoped-scan error already recorded in `parse_offset_table`.

    The out-of-range half of the check stays global on purpose: a reference to a page the
    file does not cover is wrong wherever it appears.
    """
    cut = min((text.find(h) for h in COMMENTARY if h in text), default=-1)
    return text if cut < 0 else text[:cut]


def check_signoff(text):
    """SOURCE_POLICY §5 sign-off, at the depth CD-048 sets.

    One sampled passage is enough where the machine diff stands as the second and third
    channel — but **artwork-borne text has no second channel at all**, so a file that records
    any must carry its own full-check row. Without this the depth ruling would be a paragraph
    in a policy: the one kind of content nothing else covers would be the one kind nobody was
    obliged to look at.
    """
    m = re.search(r"^## স্পট-চেক সই.*?(?=^---|\Z)", text, re.M | re.S)
    if not m:
        return "FAIL", "no spot-check sign-off section in header"
    block = m.group(0)
    data = [l for l in block.splitlines()
            if l.strip().startswith("|") and not re.match(r"^\|[\s\-:|]+\|$", l.strip())]
    data = [l for l in data if "যাচাই করার অংশ" not in l]
    if not data:
        return "FAIL", "sign-off table has no rows"
    if any(k in text for k in RASTER_ONLY) and not any(
            any(k in l for k in RASTER_ROW) for l in data):
        return "FAIL", ("this extraction records artwork-borne text, which the cross-channel "
                        "check cannot corroborate, but the sign-off table has no full-check "
                        "row for it (CD-048, SOURCE_POLICY §7.5)")
    unsigned = [l for l in data if re.search(r"\|\s*—\s*\|\s*—\s*\|", l)]
    if unsigned:
        return "PENDING", (f"{len(unsigned)} of {len(data)} spot-check row(s) unsigned — "
                           "only the Principal or the teacher can close this")
    return "PASS", f"all {len(data)} spot-check row(s) signed"


SINGLE_CHANNEL = "**যাচাই-চ্যানেল:** একক"
FULL, SAMPLED = "পূর্ণ", "নমুনা"
DEPTH_COL = "গভীরতা"


def check_depth(text):
    """§7.4's one-sample depth is bought with machine evidence. Where there is none, it
    cannot be bought — so the file must not claim it.

    §7.4 makes its conditions conjunctive and read off an executed run: Section B clean AND
    every word-level disagreement traced. A source whose text layer does not exist cannot
    satisfy either, because `source_textcheck.py` has nothing to run against. C5 Bangla is
    that case — 421 extractable characters in 142 pages, all glyphs drawn as outlines — and
    the Principal ruled full-eye depth for the whole book on 2026-08-09.

    A file declares its channel count in the header. If it declares single-channel, every
    sign-off row must say `পূর্ণ` and none may say `নমুনা`. Without this the ruling would
    live only in prose: the extraction could carry one sampled row, pass every other check,
    and nothing would notice that the depth it claimed was the depth its evidence could not
    support. The dual-channel case is left alone — §7.4 governs it and the machine diff is
    what earns the reduction there.
    """
    if SINGLE_CHANNEL not in text:
        return "PASS", "dual-channel source — §7.4 sampling depth governs, nothing to enforce here"
    m = re.search(r"^## স্পট-চেক সই.*?(?=^---|\Z)", text, re.M | re.S)
    if not m:
        return "FAIL", "declares single-channel but has no sign-off section to check depth in"
    rows = [[c.strip() for c in l.strip().strip("|").split("|")]
            for l in m.group(0).splitlines()
            if l.strip().startswith("|") and not re.match(r"^\|[\s\-:|]+\|$", l.strip())]
    header = next((r for r in rows if "যাচাই করার অংশ" in " ".join(r)), None)
    if header is None:
        return "FAIL", "sign-off table has no header row to locate the depth column in"
    try:
        col = next(i for i, c in enumerate(header) if DEPTH_COL in c)
    except StopIteration:
        return "FAIL", (f"a single-channel source's sign-off table needs a '{DEPTH_COL}' column; "
                        f"columns found: {', '.join(header)}")
    data = [r for r in rows if r is not header and len(r) > col]
    if not data:
        return "FAIL", "declares single-channel but the sign-off table has no rows"
    # **The depth cell, not the whole row.** Scanning the row matched পাঠ ৪'s first entry,
    # "আবেদনপত্রের নমুনা — পুরোটা", where নমুনা is the book's word for its sample letter and
    # has nothing to do with sampling depth. The gate went red on a correct file, which is the
    # failure mode that gets a gate ignored. The word is only a claim about depth when it is in
    # the depth column.
    sampled = [r for r in data if SAMPLED in r[col]]
    if sampled:
        return "FAIL", (f"{len(sampled)} of {len(data)} sign-off row(s) claim '{SAMPLED}' depth on a "
                        f"single-channel source — §7.4's sampling depth needs a clean "
                        f"source_textcheck.py run, which a source with no text layer cannot produce")
    missing = [r for r in data if FULL not in r[col]]
    if missing:
        return "FAIL", (f"{len(missing)} of {len(data)} sign-off row(s) state no depth; a "
                        f"single-channel source needs every row marked '{FULL}'")
    return "PASS", f"single-channel source; all {len(data)} sign-off row(s) marked '{FULL}'"


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
    results.append(("DEPTH",) + check_depth(text))
    order = {"RANGE": 0, "SLOTS": 1, "PAGES": 2, "SIGNOFF": 3, "DEPTH": 4}
    results.sort(key=lambda r: order[r[0]])

    print(f"source_check.py — SOURCE_POLICY.md §5")
    print(f"file    : {path.relative_to(REPO)}")
    print(f"subject : class {cls} · {subject}")
    print(f"grammar : chapter word '{scope[3]}'" if scope else "grammar : —")
    print(f"channel : {'single (§7.4 sampling unavailable)' if SINGLE_CHANNEL in text else 'dual'}")
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

def fixture_pool():
    """Every extraction on disk, in either half of the pipeline, in any subject.

    Was: the C5 English folders only. That was correct when English was the only extraction
    and wrong the moment Bangla existed — the Bangla-grammar and single-channel seeds have
    nothing to bite on in an English fixture, and a selftest that cannot exercise half the
    gate reports green for checks it never ran.
    """
    roots = list((REPO / "canon/sources").glob("*/*")) + list((REPO / "canon/_wip").glob("*"))
    out = []
    for r in roots:
        if r.is_dir():
            out += sorted(r.glob("C*_*_Source_*.md"))
    return sorted(set(out))


def selftest():
    """Seeded-error negative test (handoff §2 evidence rules): a gate that has never
    been shown to go red on a known-bad input has not been shown to do anything.

    Each seed picks the first fixture it can actually change. A seed that changes no fixture
    on disk is BROKEN, not skipped: the artwork-borne-text seed and the single-channel-depth
    seed each only bite on the kind of file they were written for, and reporting them green
    from a fixture that cannot carry them would be the exact silent-pass failure CD-020 was
    written about.
    """
    import tempfile
    pool = fixture_pool()
    if not pool:
        print("SELFTEST: no extraction on disk to mutate — nothing to prove against")
        return 2

    # The seeds are derived from the fixture, not hard-coded against one unit's wording.
    # Hard-coded seeds silently stopped seeding the moment the fixture changed, and a seed
    # that no longer bites reports a green selftest for a gate nobody tested.
    def bump_unit(t):
        # Matched on the untouched text, in either digit set: running dg() over the whole
        # file first would "change" a Bangla fixture even when the seed itself missed, and
        # the did-it-bite guard below would stop guarding.
        return re.sub(rf"^#\s+({UNIT_RE})\s+([0-9০-৯]+)",
                      lambda m: f"# {m.group(1)} {int(dg(m.group(2))) + 40}", t,
                      count=1, flags=re.M)

    def sample_a_full_row(t):
        # Only bites on a single-channel file: flips one full-check row to a sampled one.
        if SINGLE_CHANNEL not in t:
            return t
        return t.replace(f"| {FULL} | — | — |", f"| {SAMPLED} | — | — |", 1)

    def drop_depth_column(t):
        # A single-channel file that simply omits the depth column must not pass by default.
        if SINGLE_CHANNEL not in t:
            return t
        return t.replace(f"| {DEPTH_COL} ", "| ", 1)

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
        # Confined to the transcribed body: the last page reference in the file now lives in
        # the cross-reference table, which is deliberately not order-checked, so a seed aimed
        # at the file's last hit would land where nothing is looking and report MISSED.
        hits = list(re.finditer(r"\(পৃষ্ঠা\s*([০-৯\d]+)", transcribed_body(t)))
        if len(hits) < 2:
            return t
        last = hits[-1]
        return t[:last.start()] + "(পৃষ্ঠা ১" + t[last.end():]

    def drop_raster_row(t):
        # Only bites on a file that records artwork-borne text; reported BROKEN otherwise,
        # which is the honest outcome rather than a silent pass.
        return re.sub(r"^\|[^\n]*(ছবির|মানচিত্র|লেবেল)[^\n]*\|\s*—\s*\|\s*—\s*\|\n", "", t,
                      count=1, flags=re.M)

    seeds = [
        ("RANGE  · the stated unit has no section", bump_unit),
        ("SIGNOFF· raster-only content with no full-check row", drop_raster_row),
        ("DEPTH  · a single-channel source claims sampled depth", sample_a_full_row),
        ("DEPTH  · a single-channel source drops the depth column", drop_depth_column),
        ("SLOTS  · one spine slot dropped from the cross-reference", drop_slot),
        ("PAGES  · offset broken on one row", break_offset),
        ("PAGES  · in-body page reference outside the stated range", page_out_of_range),
        ("PAGES  · in-body page references out of order", pages_out_of_order),
    ]

    def verdict(p: Path):
        text = p.read_text(encoding="utf-8")
        scope = parse_scope(text)
        rs = []
        if scope:
            rs.append(check_range(text, scope)[0])
            rs.append(check_pages(text, scope, parse_offset_table(text))[0])
        else:
            rs.append("FAIL")
        rs.append(check_slots(text, parse_subject(p)[1])[0])
        rs.append(check_signoff(text)[0])
        rs.append(check_depth(text)[0])
        return rs

    print("fixtures:")
    for p in pool:
        print(f"          {p.relative_to(REPO)}")
    print("SELFTEST — every seeded error must turn the gate RED")
    print("-" * 78)
    ok = True
    with tempfile.TemporaryDirectory() as d:
        for label, mutate in seeds:
            bit = next(((s, mutate(s.read_text(encoding="utf-8"))) for s in pool
                        if mutate(s.read_text(encoding="utf-8")) != s.read_text(encoding="utf-8")),
                       None)
            if bit is None:
                print(f"[BROKEN ] {label} — seed changed no fixture on disk")
                ok = False
                continue
            src, bad = bit
            p = Path(d) / src.name
            p.write_text(bad, encoding="utf-8")
            red = "FAIL" in verdict(p)
            print(f"[{'RED    ' if red else 'MISSED '}] {label}   ({src.name})")
            ok = ok and red
        # and every unmutated fixture must NOT be red
        for src in pool:
            p = Path(d) / src.name
            p.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
            clean = "FAIL" not in verdict(p)
            print(f"[{'CLEAN  ' if clean else 'FALSE+ '}] control · {src.name} must not be red")
            ok = ok and clean
    print("-" * 78)
    print(f"SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 2


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "--selftest":
        sys.exit(selftest())
    sys.exit(run(Path(args[0]) if Path(args[0]).is_absolute() else REPO / args[0]))
