#!/usr/bin/env python3
"""gates.py — support-books workstream gate (AGENTS.md §5).

Thin wrapper over the vendored SB validator, so the workstream has the standard
`audits/gates.py` entry point every workstream is required to have. It adds nothing to the
validator's judgement — it locates the book and its letter inventory, runs the validator,
and relays the verbatim output and exit code.

Runs, in order:
  1. SELFTEST  — the validator's seeded-error selftest (README §6). A validator that cannot
                 catch a planted error is not evidence. This runs FIRST: if the instrument is
                 broken, the book result means nothing.
  2. VALIDATE  — the full 10-check pass over the book JSON.

Usage:
    python3 gates.py [--book <path>] [--inventory <path>] [--skip-selftest]

Exit 0 = no red in either stage. Exit 1 = red, or a broken instrument.
Paste the output verbatim in chat before any "done" or merge claim (AGENTS.md §5).
"""
import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE.parent
VALIDATOR = HERE / "validator_v2_rebuilt.py"

DEFAULT_BOOK = WS / "books" / "C1-BAN" / "support-book_C1-BAN.json"
DEFAULT_INV = WS / "books" / "C1-BAN" / "letter_inventory_C1-BAN.json"


def run(label, args):
    print(f"\n{'=' * 72}\n{label}\n{'=' * 72}")
    r = subprocess.run([sys.executable, str(VALIDATOR)] + args, text=True,
                       capture_output=True)
    sys.stdout.write(r.stdout)
    if r.stderr.strip():
        sys.stderr.write(r.stderr)
    print(f"EXIT={r.returncode}")
    return r.returncode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", default=str(DEFAULT_BOOK))
    ap.add_argument("--inventory", default=str(DEFAULT_INV))
    ap.add_argument("--skip-selftest", action="store_true")
    args = ap.parse_args()

    for label, p in (("validator", VALIDATOR), ("book", Path(args.book)),
                     ("inventory", Path(args.inventory))):
        if not p.exists():
            sys.exit(f"ERROR: {label} not found at {p}")

    codes = []
    if not args.skip_selftest:
        codes.append(run("STAGE 1 — validator seeded-error selftest",
                         ["--selftest", args.inventory]))
    codes.append(run("STAGE 2 — book validation (10 checks)",
                     [args.book, args.inventory]))

    failed = any(c != 0 for c in codes)
    print(f"\n{'=' * 72}\nGATE RESULT: {'RED' if failed else 'GREEN'}\n{'=' * 72}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
