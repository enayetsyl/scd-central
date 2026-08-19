#!/usr/bin/env python3
"""ledger_check.py — CD-088(d)(ii): the ledger-collision gate.

Run from repo root:
    python tools/audits/ledger_check.py

WHAT THIS EXISTS FOR, IN ONE SENTENCE
-------------------------------------
`CR-012` was minted twice — once in `canon/_wip/c5-math/CORRECTIONS.md` on 2026-08-12 (commit
`5634a5f`, three live citations) and again in `tools/CORRECTIONS.md` two days later, on a
next-free check that reported the number free **because it only looked in one file**. Two live
rows under one number for two days. CD-087(b)'s verdict: *"A next-free check that reports a
number free when it is not is worse than no check — it converts a collision into a documented
non-collision."* CD-088 promoted the shape to PATTERN at four instances and specified two gates;
this is **(d)(ii)**, the one that would have caught instance 4 at the moment it was written.
**(d)(i), the `int()`-on-captured-id source lint, is NOT built here** — proposed only, per the
session brief.

TWO CHECKS, AND THEY ARE INDEPENDENT
------------------------------------
  LEDGER-PREFIX     every ledger declares its own ID prefix in its header.
  LEDGER-COLLISION  no <PREFIX>-### row ID resolves to rows in two files.

The first is not decoration. CD-088(c) draws the distinction that makes it load-bearing:
instances 1–3 are *a form being discarded*; instance 4 is *the form never having existed*. Two
ledgers that both mint bare `CR-###` are not two schemes that collided — they are one scheme with
two writers, and no amount of care at mint time fixes that. So the declaration is the repair and
the collision check is the alarm; shipping only the alarm would leave the defect in place and
merely notice it faster.

WHY THE ID IS NEVER NORMALISED HERE
-----------------------------------
Per CD-088(d)(i)'s reasoning, applied to this file's own code: a captured ID is compared **as the
raw string**, prefix included, zero-padding included. `int()` is never called on a captured group.
`CR-012`, `QB-CR-012` and `TOOLS-CR-012` are three different tokens and this gate must never be
the thing that merges them — a collision detector that normalises away the prefix would report
collisions that are not there and, worse, teach the repo that the prefix does not matter.

Exit 0 = CLEAN, 1 = FAIL. Paste output verbatim per AGENTS.md §5.
"""
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

LEDGER_NAMES = {"CORRECTIONS.md", "DECISIONS.md"}
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", "_unvendored"}

# The declaration form. An HTML comment keeps AGENTS.md §7 ("reader-facing files stay clean")
# while staying machine-readable, and it sits in the header where a reader looking for the
# ledger's identity would look. The literal token is captured RAW — see the module docstring.
#     <!-- ledger-prefix: QB-CR -->
# Several prefixes are permitted on one ledger (comma-separated) because a DECISIONS.md may
# legitimately carry more than one series.
DECL = re.compile(r"<!--\s*ledger-prefix:\s*([^>]*?)\s*-->", re.IGNORECASE)

# CD-124 — the LANE, and why declaring one is the repair while renumbering is not.
#     <!-- ledger-lane: c5-math -->
# Four ledgers all mint bare `CR-###`, and `CR-001`…`CR-004` are each live in two or three of them.
# That is not four schemes that collided; it is one scheme with four writers (CD-088(c)'s
# instance-4 face). CD-087(b) gives the rule for WHICH row keeps a number but not the assignment,
# and applying it means renaming live, cited rows across four workstreams — including a
# `canon/_wip/` lane that is mid-extraction, which is the churn CD-067 guards against.
#
# So the ordering is the ruling, not just the action: **declare every lane now, renumber each lane
# as it closes.** A declared lane makes an existing overlap UNAMBIGUOUS without touching a single
# citation — `CR-001` in the c5-bangla ledger and `CR-001` in support-books are now two identified
# rows rather than one contested number — while a NEW collision inside one lane still FAILs.
LANE = re.compile(r"<!--\s*ledger-lane:\s*([^>]*?)\s*-->", re.IGNORECASE)

# A row ID is the first cell of a markdown table row. Anchoring on the FIRST CELL is the whole
# design: it distinguishes a row that *mints* an ID from prose that *cites* one. A ledger is full
# of citations to other ledgers' IDs (QB-CR-009 cites CD-044, TOOLS-CR-001 cites CR-012) and a
# gate that counted citations as mints would fire on every correctly-written cross-reference —
# AGENTS.md §5.1's exact failure: the gate would make the citation unwriteable.
# TOOLS-CR-010: the id may carry a trailing label INSIDE its own cell — `| **TOOLS-CR-005 ·
# PATTERN CANDIDATE** |` — and that row went uncounted from the day it was filed. `[^|]*`
# admits anything up to the closing pipe; the id must still be the cell's FIRST token, so a
# citation in prose is still not a mint (AGENTS §5.1).
ROW_ID = re.compile(r"^\|\s*\**\s*`?([A-Z][A-Z0-9]*(?:-[A-Z][A-Z0-9]*)*-\d+)`?[^|]*\|")

# A ledger whose header declares NO prefix still has its rows read, so the collision half keeps
# working on a repo that has not yet been repaired. Undeclared prefixes are reported separately.
POINTER = re.compile(r"POINTER,?\s+not\s+a\s+log", re.IGNORECASE)


def ledgers(root):
    """Every corrections/decisions ledger in the repo, sorted for stable output."""
    out = []
    for p in sorted(root.rglob("*.md")):
        if p.name not in LEDGER_NAMES:
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        out.append(p)
    return out


def read(path):
    return path.read_text(encoding="utf-8", errors="replace")


def rel(path):
    """Repo-relative where possible; the selftest's fixtures live in a temp dir outside ROOT."""
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def declared_prefixes(text):
    """The prefixes this ledger says are its own. Raw strings, never parsed into numbers."""
    out = []
    for m in DECL.finditer(text):
        for tok in m.group(1).split(","):
            tok = tok.strip().strip("`")
            if tok:
                out.append(tok)
    return out


def row_ids(text):
    """Every ID minted as a row in this file, as (raw_token, line_number)."""
    out = []
    for n, line in enumerate(text.splitlines(), 1):
        m = ROW_ID.match(line)
        if m:
            out.append((m.group(1), n))
    return out


def split_prefix(token):
    """`QB-CR-009` -> ('QB-CR', '009'). The number half is returned as a STRING and is never
    int()-ed; it is carried only so a report can print it."""
    head, _, tail = token.rpartition("-")
    return head, tail


def is_pointer(text):
    """A DECISIONS.md that declares itself a pointer keeps no series (workstreams/scholarship)."""
    return bool(POINTER.search(text[:1200]))


# ---- the two checks ---------------------------------------------------------------

def check_prefix_declared(files):
    """LEDGER-PREFIX — CD-088(d)(ii), first clause."""
    errs = []
    for path, text in files:
        r = rel(path)
        if is_pointer(text):
            continue
        decls = declared_prefixes(text)
        if not decls:
            mints = row_ids(text)
            shape = sorted({split_prefix(t)[0] for t, _ in mints}) or ["<no rows yet>"]
            errs.append(f"{r}: no `<!-- ledger-prefix: … -->` in its header — "
                        f"rows in this file mint {', '.join(shape)}, but the file never says so, "
                        f"so no next-free check can know what namespace it is checking")
            continue
        for token, line in row_ids(text):
            head, _ = split_prefix(token)
            if head not in decls:
                errs.append(f"{r}:{line}: row `{token}` has prefix `{head}`, which this ledger "
                            f"does not declare (declares: {', '.join(decls)})")
    return errs


def declared_lane(text):
    m = LANE.search(text)
    return m.group(1).strip().strip("`") if m else None


def check_lane_declared(files):
    """LEDGER-LANE — CD-124. Every minting ledger names its lane, and no two share one."""
    errs, lanes = [], {}
    for path, text in files:
        r = rel(path)
        if is_pointer(text):
            continue
        lane = declared_lane(text)
        if not lane:
            errs.append(f"{r}: no `<!-- ledger-lane: … -->` in its header — without it an ID in "
                        f"this file cannot be told apart from the same ID in another ledger, "
                        f"which is the condition CD-124 declares its way out of")
            continue
        lanes.setdefault(lane, []).append(r)
    for lane in sorted(lanes):
        if len(lanes[lane]) > 1:
            errs.append(f"lane `{lane}` is declared by {len(lanes[lane])} ledgers "
                        f"({' · '.join(lanes[lane])}) — a lane identifies ONE minting ledger; two "
                        f"ledgers sharing one re-creates the defect the lane exists to remove")
    return errs


def check_collision(files):
    """LEDGER-COLLISION — CD-088(d)(ii) second clause, as amended by CD-124.

    FAILS on a genuine collision: one ID minted twice **inside one lane**. That is the CR-012 shape
    and it is what a next-free check must never miss.

    REPORTS, without failing, a token shared **across declared lanes**. Those are the four bare
    `CR-###` series, known and ruled: declared now, renumbered per lane at close. The report is not
    a downgrade — an undeclared cross-file overlap still FAILS, because without a lane there is
    nothing to tell the two rows apart. **Only a declaration buys the deferral, and the deferral is
    printed every run so it cannot go quiet.**
    """
    seen = {}
    lane_of = {}
    for path, text in files:
        r = rel(path)
        lane_of[r] = declared_lane(text)
        for token, line in row_ids(text):
            seen.setdefault(token, []).append((r, line))
    errs = []
    for token in sorted(seen):
        sites = seen[token]
        files_hit = sorted({f for f, _ in sites})
        if len(files_hit) < 2:
            continue
        where = " · ".join(f"{f}:{ln}" for f, ln in sites)
        lanes = [lane_of.get(f) for f in files_hit]
        if all(lanes) and len(set(lanes)) == len(lanes):
            DEFERRED.append(f"`{token}` appears in {len(files_hit)} DECLARED lanes "
                            f"({' · '.join(sorted(set(lanes)))}) — {where}. Non-ambiguous and "
                            f"NOT renumbered: CD-124 renumbers each lane as it closes.")
            continue
        errs.append(f"`{token}` is minted as a row in {len(files_hit)} ledgers — {where}. "
                    f"This is the CR-012 shape (CD-087(b)): one number, two live rows"
                    + ("" if all(lanes) else ", and at least one of them declares no lane, so "
                                             "nothing tells the rows apart (CD-124)") + ".")
    return errs


DEFERRED = []


def check_duplicate_within(files):
    """A number minted twice in the SAME ledger. Not named in CD-088, and reported rather than
    inferred into the collision check: two rows under one ID in one file is an append-only
    violation, a different defect from a cross-ledger collision, and merging them would hide
    which one happened."""
    errs = []
    for path, text in files:
        r = rel(path)
        seen = {}
        for token, line in row_ids(text):
            seen.setdefault(token, []).append(line)
        for token in sorted(seen):
            if len(seen[token]) > 1:
                errs.append(f"{r}: `{token}` is minted on lines "
                            f"{', '.join(str(n) for n in seen[token])} — one ID, two rows, "
                            f"in one append-only ledger")
    return errs


CHECKS = [
    ("LEDGER-PREFIX", check_prefix_declared),
    ("LEDGER-LANE", check_lane_declared),
    ("LEDGER-COLLISION", check_collision),
    ("DUPLICATE-IN-FILE", check_duplicate_within),
]


def run(paths, quiet=False):
    # A POINTER ledger mints nothing — it INDEXES rows another ledger minted. Excluding it here
    # rather than only in LEDGER-PREFIX is the difference between a gate and a nuisance: the first
    # run flagged all six CD rows in `workstreams/scholarship/DECISIONS.md` as collisions with
    # `canon/DECISIONS.md`, which is not a collision but the file working exactly as designed.
    # This is AGENTS.md §5.1 again in a new place — a gate that fires on the correct way to point
    # at another ledger makes pointing unwriteable, and the next author routes around it by not
    # indexing. The pointer declaration is the file's own statement that it keeps no series.
    files = [(p, t) for p, t in ((p, read(p)) for p in paths) if not is_pointer(t)]
    fails = []
    del DEFERRED[:]
    for name, fn in CHECKS:
        errs = fn(files)
        if not quiet:
            print(f"  {'FAIL' if errs else 'PASS'}  {name}"
                  + "".join(f"\n        - {e}" for e in errs))
        fails += [(name, e) for e in errs]
    if DEFERRED and not quiet:
        # Printed every run, never folded into the PASS line. CD-124's deferral is a debt the
        # repo carries out loud; a deferral nobody sees is indistinguishable from a fix.
        print(f"  DEFER {len(DEFERRED)} cross-lane token(s) — declared, non-ambiguous, "
              f"renumbered per lane at close (CD-124):")
        for d in DEFERRED:
            print(f"        - {d}")
    return fails


# ---- seeded selftest — synthetic fixtures only, never the live ledgers -------------
# CD-055 / CD-064(f): fixtures are written for the test, never drawn from the file pool the gate
# judges. Everything below is built in a temp directory that exists for the length of this run.

def _write(d, rel, body, lane="auto"):
    """`lane="auto"` gives the fixture a lane named for its directory — what a correct ledger has.
    `lane=None` omits it deliberately, which is how the undeclared-lane seeds are cut."""
    p = Path(d) / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    if lane == "auto":
        lane = p.parent.name
    if lane and "ledger-prefix:" in body and "ledger-lane:" not in body:
        body = body.replace("-->", f"-->\n<!-- ledger-lane: {lane} -->", 1)
    p.write_text(body, encoding="utf-8")
    return p


def _clean_set(d):
    """Two synthetic ledgers that are correct: distinct declared prefixes, no shared token."""
    a = _write(d, "alpha/CORRECTIONS.md",
               "# CORRECTIONS.md — alpha\n<!-- ledger-prefix: ALPHA-CR -->\n\n"
               "| ID | Date | Correction |\n|---|---|---|\n"
               "| ALPHA-CR-001 | 2026-01-01 | first, and it cites BETA-CR-001 in prose |\n"
               "| ALPHA-CR-002 | 2026-01-02 | second |\n")
    b = _write(d, "beta/CORRECTIONS.md",
               "# CORRECTIONS.md — beta\n<!-- ledger-prefix: BETA-CR -->\n\n"
               "| ID | Date | Correction |\n|---|---|---|\n"
               "| BETA-CR-001 | 2026-01-03 | first |\n")
    return [a, b]


def selftest():
    print("SELFTEST — the instrument is proven before any repo verdict (CD-025); "
          "synthetic fixtures only (CD-055, CD-064(f))")
    ok = True
    results = []

    with tempfile.TemporaryDirectory() as d:
        # --- baseline: a correct pair must be silent. A gate that fires on everything is as
        # --- useless as one that fires on nothing.
        base = _clean_set(d)
        fails = run(base, quiet=True)
        results.append(("baseline", "two correct ledgers, cross-citing in prose",
                        not fails, "CLEAN" if not fails else f"fired: {fails}"))

    with tempfile.TemporaryDirectory() as d:
        # --- LEDGER-COLLISION bites: the CR-012 shape, reproduced synthetically.
        _clean_set(d)
        # gamma declares NO lane — which is the CR-012 condition exactly: two ledgers, one number,
        # and nothing on either file that tells the two rows apart.
        _write(d, "gamma/CORRECTIONS.md",
               "# CORRECTIONS.md — gamma\n<!-- ledger-prefix: ALPHA-CR -->\n\n"
               "| ID | Date | Correction |\n|---|---|---|\n"
               "| ALPHA-CR-002 | 2026-01-09 | a second row under a number alpha already minted |\n",
               lane=None)
        fails = run(list(Path(d).rglob("*.md")), quiet=True)
        hit = any(n == "LEDGER-COLLISION" and "ALPHA-CR-002" in e for n, e in fails)
        results.append(("LEDGER-COLLISION", "one ID minted as a row in two ledgers, one of them "
                                            "declaring no lane — the CR-012 condition", hit, ""))

    with tempfile.TemporaryDirectory() as d:
        # --- LEDGER-LANE bites on an undeclared lane, on its own.
        _clean_set(d)
        _write(d, "eps/CORRECTIONS.md",
               "# CORRECTIONS.md — eps\n<!-- ledger-prefix: EPS-CR -->\n\n"
               "| ID |\n|---|\n| EPS-CR-001 |\n", lane=None)
        fails = run(list(Path(d).rglob("*.md")), quiet=True)
        hit = any(n == "LEDGER-LANE" and "eps" in e for n, e in fails)
        results.append(("LEDGER-LANE", "a ledger that declares no lane", hit, ""))

    with tempfile.TemporaryDirectory() as d:
        # --- LEDGER-LANE bites when TWO ledgers claim ONE lane. This is the check that makes the
        # --- cross-lane deferral safe: if two files could share a lane, the deferral would let a
        # --- real same-lane collision through as "declared". They cannot, so it cannot.
        _clean_set(d)
        _write(d, "zeta/CORRECTIONS.md",
               "# CORRECTIONS.md — zeta\n<!-- ledger-prefix: ZETA-CR -->\n\n"
               "| ID |\n|---|\n| ZETA-CR-001 |\n", lane="alpha")
        fails = run(list(Path(d).rglob("*.md")), quiet=True)
        hit = any(n == "LEDGER-LANE" and "is declared by 2 ledgers" in e for n, e in fails)
        results.append(("LEDGER-LANE", "two ledgers claiming one lane — without this the deferral "
                                       "below would be a loophole", hit, ""))

    with tempfile.TemporaryDirectory() as d:
        # --- THE CD-124 DEFERRAL, both directions in one case: the same bare token in two
        # --- DECLARED lanes must NOT fail (they are two identified rows, not one contested
        # --- number) and must NOT be silent (the renumber is a debt, and a debt nobody prints is
        # --- indistinguishable from a fix).
        _write(d, "lane1/CORRECTIONS.md",
               "# CORRECTIONS.md — lane1\n<!-- ledger-prefix: CR -->\n\n| ID |\n|---|\n| CR-001 |\n")
        _write(d, "lane2/CORRECTIONS.md",
               "# CORRECTIONS.md — lane2\n<!-- ledger-prefix: CR -->\n\n| ID |\n|---|\n| CR-001 |\n")
        fails = run(list(Path(d).rglob("*.md")), quiet=True)
        quiet_ok = not any(n == "LEDGER-COLLISION" for n, _ in fails)
        loud_ok = any("CR-001" in x for x in DEFERRED)
        results.append(("LEDGER-COLLISION", "a bare token in two DECLARED lanes is deferred, not "
                                            "failed — AND is printed, not swallowed (CD-124)",
                        quiet_ok and loud_ok,
                        "" if quiet_ok and loud_ok else
                        f"fails={fails} deferred={DEFERRED}"))

    with tempfile.TemporaryDirectory() as d:
        # --- LEDGER-COLLISION does NOT bite on a citation. This is the AGENTS §5.1 direction:
        # --- a ledger must stay able to name another ledger's ID in prose.
        _clean_set(d)
        _write(d, "delta/CORRECTIONS.md",
               "# CORRECTIONS.md — delta\n<!-- ledger-prefix: DELTA-CR -->\n\n"
               "| ID | Date | Correction |\n|---|---|---|\n"
               "| DELTA-CR-001 | 2026-01-04 | supersedes ALPHA-CR-001 and cites ALPHA-CR-002 |\n")
        fails = run(list(Path(d).rglob("*.md")), quiet=True)
        quiet_ok = not any(n == "LEDGER-COLLISION" for n, _ in fails)
        results.append(("LEDGER-COLLISION", "stays quiet when a row CITES another ledger's ID "
                                            "(AGENTS §5.1 — naming the defect stays writeable)",
                        quiet_ok, "" if quiet_ok else f"wrongly fired: {fails}"))

    with tempfile.TemporaryDirectory() as d:
        # --- the prefix is NOT normalised away: three same-numbered IDs under three prefixes
        # --- are three tokens, not one collision. CD-088(a), TOOLS-CR-001's shape.
        _write(d, "a/CORRECTIONS.md", "# a\n<!-- ledger-prefix: CR -->\n\n| ID |\n|---|\n| CR-012 |\n")
        _write(d, "b/CORRECTIONS.md", "# b\n<!-- ledger-prefix: QB-CR -->\n\n| ID |\n|---|\n| QB-CR-012 |\n")
        _write(d, "c/CORRECTIONS.md", "# c\n<!-- ledger-prefix: TOOLS-CR -->\n\n| ID |\n|---|\n| TOOLS-CR-012 |\n")
        fails = run(list(Path(d).rglob("*.md")), quiet=True)
        quiet_ok = not any(n == "LEDGER-COLLISION" for n, _ in fails)
        results.append(("LEDGER-COLLISION", "CR-012 / QB-CR-012 / TOOLS-CR-012 are THREE tokens, "
                                            "not one collision (prefix never normalised away)",
                        quiet_ok, "" if quiet_ok else f"wrongly fired: {fails}"))

    with tempfile.TemporaryDirectory() as d:
        # --- and zero-padding is not normalised either: CR-012 vs CR-12 stay distinct.
        _write(d, "a/CORRECTIONS.md", "# a\n<!-- ledger-prefix: CR -->\n\n| ID |\n|---|\n| CR-012 |\n")
        _write(d, "b/CORRECTIONS.md", "# b\n<!-- ledger-prefix: CR -->\n\n| ID |\n|---|\n| CR-12 |\n")
        fails = run(list(Path(d).rglob("*.md")), quiet=True)
        quiet_ok = not any(n == "LEDGER-COLLISION" for n, _ in fails)
        results.append(("LEDGER-COLLISION", "CR-012 and CR-12 are distinct raw strings "
                                            "(no int() anywhere on a captured group)",
                        quiet_ok, "" if quiet_ok else f"wrongly fired: {fails}"))

    with tempfile.TemporaryDirectory() as d:
        # --- LEDGER-PREFIX bites: a ledger with no declaration.
        _write(d, "e/CORRECTIONS.md",
               "# CORRECTIONS.md — undeclared\n\n| ID |\n|---|\n| MYSTERY-CR-001 |\n")
        fails = run(list(Path(d).rglob("*.md")), quiet=True)
        hit = any(n == "LEDGER-PREFIX" and "no `<!-- ledger-prefix" in e for n, e in fails)
        results.append(("LEDGER-PREFIX", "a ledger that declares no prefix", hit, ""))

    with tempfile.TemporaryDirectory() as d:
        # --- LEDGER-PREFIX bites the other way: declared, but a row mints outside it.
        _write(d, "f/CORRECTIONS.md",
               "# f\n<!-- ledger-prefix: FOO-CR -->\n\n| ID |\n|---|\n"
               "| FOO-CR-001 | ok |\n| BAR-CR-001 | minted in the wrong house |\n")
        fails = run(list(Path(d).rglob("*.md")), quiet=True)
        hit = any(n == "LEDGER-PREFIX" and "BAR-CR-001" in e for n, e in fails)
        results.append(("LEDGER-PREFIX", "a row whose prefix the ledger does not declare", hit, ""))

    with tempfile.TemporaryDirectory() as d:
        # --- LEDGER-PREFIX stays quiet on a declared POINTER ledger (workstreams/scholarship's
        # --- DECISIONS.md keeps no series by design and must not be dragged red for it).
        _write(d, "g/DECISIONS.md",
               "# DECISIONS.md — g (POINTER, not a log)\nRulings live as CD-### rows in canon.\n")
        fails = run(list(Path(d).rglob("*.md")), quiet=True)
        quiet_ok = not any(n == "LEDGER-PREFIX" for n, _ in fails)
        results.append(("LEDGER-PREFIX", "stays quiet on a declared POINTER ledger",
                        quiet_ok, "" if quiet_ok else f"wrongly fired: {fails}"))

    with tempfile.TemporaryDirectory() as d:
        # --- a POINTER ledger INDEXING another ledger's rows is not a collision. Seeded because
        # --- the first live run got this wrong and flagged six correct pointer rows.
        _write(d, "canonish/DECISIONS.md",
               "# DECISIONS.md — canonish\n<!-- ledger-prefix: CD -->\n\n"
               "| ID | Decision |\n|---|---|\n| CD-001 | the real row |\n")
        _write(d, "ptr/DECISIONS.md",
               "# DECISIONS.md — ptr (POINTER, not a log)\nKeeps no local series.\n\n"
               "| ID | What it settles |\n|---|---|\n| CD-001 | indexed here for the reader |\n")
        fails = run(list(Path(d).rglob("*.md")), quiet=True)
        quiet_ok = not fails
        results.append(("LEDGER-COLLISION", "a POINTER ledger indexing another ledger's row is "
                                            "not a collision (it mints nothing)",
                        quiet_ok, "" if quiet_ok else f"wrongly fired: {fails}"))

    with tempfile.TemporaryDirectory() as d:
        # --- DUPLICATE-IN-FILE bites.
        _write(d, "h/CORRECTIONS.md",
               "# h\n<!-- ledger-prefix: HH-CR -->\n\n| ID |\n|---|\n"
               "| HH-CR-001 | first |\n| HH-CR-001 | same number again |\n")
        fails = run(list(Path(d).rglob("*.md")), quiet=True)
        hit = any(n == "DUPLICATE-IN-FILE" and "HH-CR-001" in e for n, e in fails)
        results.append(("DUPLICATE-IN-FILE", "one ID minted twice in one ledger", hit, ""))

    # --- ROW-ID · TOOLS-CR-010, seeded BOTH directions. No fixture files: row_ids reads text.
    got = [t for t, _ in row_ids("| ID |\n|---|\n"
                                 "| **ZZ-CR-005 · PATTERN CANDIDATE** | label inside the bold |\n")]
    results.append(("ROW-ID", "an id cell carrying a trailing label inside the bold is COUNTED "
                              "— the shape TOOLS-CR-005 was filed in, and read as absent",
                    got == ["ZZ-CR-005"], f"read: {got}"))

    # --- the control, because widening a regex is how a gate stops discriminating.
    got = [t for t, _ in row_ids("| ID |\n|---|\n"
                                 "| see ZZ-CR-006 for the ruling | a citation, not a mint |\n")]
    results.append(("ROW-ID", "a cell whose FIRST token is not an id is still NOT counted — "
                              "AGENTS §5.1's mint-vs-cite line, kept through the widening",
                    got == [], f"read: {got}"))

    for gate, label, passed, note in results:
        print(f"  {'PASS' if passed else 'FAIL':<4}  {gate:<18} {label}"
              + (f"\n        {note}" if note and not passed else ""))
        ok = ok and passed

    print(f"SELFTEST RESULT: {'PASS' if ok else 'FAIL'} "
          f"({len(results)} cases: {sum(1 for r in results if r[0] != 'baseline')} seeded, 1 baseline)")
    return ok


def main():
    if not selftest():
        print("\nRESULT: FAIL (selftest red — no repo verdict is believable, nothing was judged)")
        sys.exit(1)
    paths = ledgers(ROOT)
    print(f"\nLEDGERS SCANNED: {len(paths)}")
    for p in paths:
        text = read(p)
        decls = declared_prefixes(text)
        n = len(row_ids(text))
        tag = ", ".join(decls) if decls else ("POINTER" if is_pointer(text) else "«undeclared»")
                # TOOLS-CR-010(3): a bare count is an absolute number nothing cross-reads, so it can
        # only be wrong quietly — it read 8 while the file held 9, before AND after a row was
        # added, because the +1 and the −1 cancelled. The highest ordinal gives the reader
        # something to compare it against. Lexical max over the RAW strings: no int(), no
        # arithmetic, nothing for CD-088's lint to waive. REPORT, not a verdict.
        hw = max((split_prefix(t)[1] for t, _ in row_ids(text)), default="—")
        print(f"  {rel(p):<52} prefix: {tag:<14} rows: {n:<4} high water: {hw}")
    print()
    fails = run(paths)
    print(f"RESULT: {'FAIL' if fails else 'CLEAN'} ({len(fails)} failures)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
