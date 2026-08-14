#!/usr/bin/env python3
"""gates.py — <workstream> audit gates (template).

Add one function per gate; each returns a list of failure strings.
Pattern source: EnglishDrive audits/scripts/run_all.py. Run from repo root:
    python workstreams/<name>/audits/gates.py
Exit 0 = CLEAN, 1 = FAIL. Paste output verbatim per AGENTS.md §5.
"""
import sys

GATES = []  # e.g. [("mark-total", check_mark_totals), ...]


def main():
    if not GATES:
        print("gates.py: NO GATES DEFINED YET for this workstream.")
        print("RESULT: FAIL (a workstream with zero gates cannot declare anything final)")
        sys.exit(1)
    fails = []
    for name, fn in GATES:
        errs = fn()
        print(f"  {'FAIL' if errs else 'PASS'}  {name}" + "".join(f"\n        - {e}" for e in errs))
        fails += errs
    print(f"RESULT: {'FAIL' if fails else 'CLEAN'} ({len(fails)} failures)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
