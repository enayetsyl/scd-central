#!/usr/bin/env python3
r"""subject_search.py — has this SUBJECT already been ruled? (CD-188)

WHY THIS EXISTS
---------------
`CD-154` and `TOOLS-CR-005` make a session verify next-free by two methods before filing a row.
Both answer one question: **is this NUMBER available.** Neither asks **has this TOPIC already been
decided**, and nothing else did either.

`CD-187` is what that gap costs. `CD-186(d)` ruled `BAN-S15` absent book-wide as though the
question were open; `CD-147` had closed it sixteen days earlier, on wider grounds, and was live,
unamended, and executed in code. The next-free sweep for the token `CD-186` returned zero hits and
was correct — it was answering a different question. **A sweep for the SUBJECT (`S15`) would have
returned CD-136, CD-139 and CD-147 on the first try.**

THE FAILURE IS ATTESTED THREE TIMES, NOT ARGUED
-----------------------------------------------
* `CD-134(a)` — *"The drafted form of this ruling cited only §3 row 15 and read as fresh ground.
  It is not"*; `CD-122(b)` had already ruled it. Caught in draft.
* `QB-CR-015(c)` — *"ALREADY RULED, AND THIS ROW DOES NOT RE-RULE IT"*; `CD-145` had it. Caught.
* `CD-187` — `CD-147` had it. **Caught after the row was pushed.**

WHAT THIS IS NOT
----------------
**Not a gate, and deliberately not registered in `run_all.py`.** No script can observe whether a
human searched before drafting; a gate that claimed to check it would be asserting about a surface
it cannot see, which is this ledger's oldest recurring defect. This tool makes the search **one
command instead of an ad-hoc grep**, which is the only thing that reliably makes a practice stick.
The obligation lives in CD-188 and in the reader, not here.

It is also **not** a next-free check and replaces neither method. Run both.

USAGE
-----
    python tools/subject_search.py S14 S15
    python tools/subject_search.py "paper-level" --context 300

Prints every ledger ROW whose text contains any term, with its id and date. Rows, not lines:
a ledger row is one very long line, so a line-oriented grep prints thousands of characters and
buries the id.
"""

import argparse
import os
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001  (TOOLS-CR-013)
    pass

ROOT = Path(os.environ.get("SCD_ROOT") or Path(__file__).resolve().parents[1])

LEDGERS = [
    "canon/DECISIONS.md",
    "canon/sources/SOURCE_POLICY.md",
    "tools/CORRECTIONS.md",
    "workstreams/question-banks/CORRECTIONS.md",
    "workstreams/question-banks/DECISIONS.md",
    "workstreams/support-books/DECISIONS.md",
    "workstreams/support-books/CORRECTIONS.md",
    "workstreams/class-tests/CORRECTIONS.md",
    "PENDING_PRINCIPAL.md",
    "AGENTS.md",
]

ROW_ID = re.compile(r"\|?\s*\*{0,2}((?:CD|TOOLS-CR|QB-CR|QB-D|WS-CR|WS-D|CF-CR|CF-D|SCH-CR|"
                    r"P01-CR|D-PROJ01|PENDING-P|CR|D)-\d{2,3})")
SECTION = re.compile(r"^#{2,3}\s*(?:§\s*)?([\d.]+|[^\n]{0,60})")


def hits(text, terms, context):
    r"""-> [(row_id_or_None, line_no, excerpt)] for every LINE containing any term.

    Case-insensitive. The excerpt is centred on the FIRST matching term rather than on the line
    start, because a ledger row's opening 200 characters are boilerplate and the match is usually
    thousands of characters in.
    """
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        low = line.lower()
        for t in terms:
            j = low.find(t.lower())
            if j < 0:
                continue
            m = ROW_ID.match(line)
            h = SECTION.match(line)
            tag = m.group(1) if m else (f"§{h.group(1)}" if h else None)
            a, b = max(0, j - context // 2), min(len(line), j + context // 2)
            out.append((tag, i, ("…" if a else "") + line[a:b] + ("…" if b < len(line) else "")))
            break
    return out


def search(root, terms, context=220, files=None):
    found = {}
    for rel in (files or LEDGERS):
        p = root / rel
        if not p.exists():
            continue
        h = hits(p.read_text(encoding="utf-8", errors="replace"), terms, context)
        if h:
            found[rel] = h
    return found


# ---------------------------------------------------------------- selftest (CD-025)

def selftest():
    import tempfile
    print("SELFTEST — synthetic fixtures only (CD-055, CD-121(e)); no live ledger is read.")
    r = []
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "canon").mkdir()
        (root / "canon" / "DECISIONS.md").write_text(
            "# fixture\n\n"
            "| CD-001 | 2026-01-01 | **THE ZZZ SLOT IS PAPER-LEVEL, categorically.** Body text. |\n"
            "| CD-002 | 2026-01-02 | **Something else entirely.** No overlap. |\n"
            "## 7.4 A heading that mentions zzz in prose\n",
            encoding="utf-8")

        f = search(root, ["ZZZ"], files=["canon/DECISIONS.md"])
        rows = f.get("canon/DECISIONS.md", [])
        ids = [t for t, _, _ in rows]

        r.append(("finds the row that already rules the subject", "CD-001" in ids))
        r.append(("does NOT return the unrelated row", "CD-002" not in ids))
        r.append(("is case-insensitive — `ZZZ` finds the prose `zzz`", len(rows) == 2))
        r.append(("tags a heading as a section, not as a row",
                  any(t and t.startswith("§") for t, _, _ in rows)))
        r.append(("a term that appears nowhere returns nothing, and that is not an error",
                  not search(root, ["QQQQQQ"], files=["canon/DECISIONS.md"])))
        # THE DIRECTION THAT MATTERS. A search returning nothing is the outcome a drafter WANTS,
        # so it is the outcome most likely to be believed without being earned — TOOLS-CR-005's
        # named family. The excerpt must therefore prove the file was actually opened.
        r.append(("a missing ledger file is skipped and cannot masquerade as a clean search",
                  not search(root, ["ZZZ"], files=["canon/NOSUCH.md"])))

    ok = True
    for label, good in r:
        print(f"  {'PASS' if good else 'FAIL'}  SUBJECT-SEARCH   {label}")
        ok = ok and good
    print(f"SELFTEST: {'PASS' if ok else 'FAIL'} ({len(r)} cases)")
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="subject_search.py",
        description="Search the ledgers for a SUBJECT before drafting a rule about it (CD-188). "
                    "This is not a next-free check and does not replace CD-154 or TOOLS-CR-005.")
    ap.add_argument("terms", nargs="*", metavar="TERM",
                    help="one or more subject terms; a row matching ANY of them is reported")
    ap.add_argument("--context", type=int, default=220,
                    help="characters of surrounding text per hit (default 220)")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the instrument on synthetic seeds and exit")
    args = ap.parse_args(argv)

    if args.selftest:
        return 0 if selftest() else 2
    if not args.terms:
        ap.error("give at least one TERM, or --selftest")
    if not selftest():
        print("\nRESULT: REFUSED (selftest red — no search result is believable)")
        return 2

    print()
    found = search(ROOT, args.terms, args.context)
    total = sum(len(v) for v in found.values())
    for rel, rows in found.items():
        print(f"=== {rel}")
        for tag, ln, ex in rows:
            print(f"  {(tag or '—'):<14} :{ln:<5} {ex}")
        print()
    print(f"RESULT: {total} hit(s) across {len(found)} file(s) for {args.terms}")
    if not total:
        # A search that finds nothing is the answer a drafter wants, which is exactly why it must
        # not be reported as a bare zero (TOOLS-CR-005).
        print("  NOTHING FOUND — which is a weaker statement than it looks. It means these TERMS "
              "do not appear; it does not mean the subject is unruled. Try the words the ledger "
              "would have used, not the words you would use.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
