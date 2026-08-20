#!/usr/bin/env python3
r"""state_check.py — STATE.json's high-water numbers must equal the ledgers' own (CD-184).

WHY THIS EXISTS, AND WHY IT IS A GATE RATHER THAN A CONVENTION
--------------------------------------------------------------
`STATE.json` records the next-free frontier of every ID series so a session can read it once
instead of re-deriving it by grep. **That is a convenience, and a convenience that duplicates
state can drift — at which point it is worse than not existing, because it is the file people
would trust.** CD-154 already requires next-free to be re-verified against a freshly fetched
origin immediately before the commit that files a row, and TOOLS-CR-005 requires it by BOTH
methods. `STATE.json` does not replace either; it is a third reading that must agree with them.

THE ONE PROPERTY THIS GATE GUARANTEES: **a stale `STATE.json` is LOUD.** Nothing here makes the
numbers right. It makes a wrong number impossible to push, which is the only guarantee worth
having for a cache.

HOW THE NUMBERS ARE TAKEN
-------------------------
By importing `ledger_check`'s own `row_ids` and `split_prefix` and calling them. **Not by
reimplementing them.** A second implementation of "what counts as a row" would eventually
disagree with the first, and then two gates would report two frontiers with nothing to say which
is right — this ledger's recurring family, a check aimed at a narrower surface than the claim it
tests, arriving as a check aimed at a *different* surface than the one it claims to mirror.

Numbers are compared as RAW STRINGS, lexically, prefix and zero-padding intact. `int()` is never
called on a captured ID (CD-088(d)(i)), so nothing here is a sink for `int_id_check.py`.

`PENDING_PRINCIPAL.md` IS INCLUDED, AND IT IS THE ONE THAT NEEDED A DECISION
---------------------------------------------------------------------------
`ledger_check.ledgers()` filters by FILENAME — `LEDGER_NAMES = {"CORRECTIONS.md",
"DECISIONS.md"}` — so `PENDING_PRINCIPAL.md` is never scanned, and its `PENDING-P` series has
never appeared in a `LEDGER-CHECK` census line. **Its rows are perfectly readable by that same
reader** (verified at source: 21 rows, high water `042`), so this gate reads it directly with
`ledger_check`'s code rather than either skipping the series or writing a second parser for it.
The Principal ruled the series in scope; this is how it is held there honestly.

Exit codes: 0 CLEAN · 1 FAIL · 2 REFUSED (selftest red — no verdict was reached).
"""

import argparse
import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:  # noqa: BLE001  (TOOLS-CR-013: a stream that cannot be reconfigured is not a crash)
    pass

import os

ROOT = Path(os.environ.get("SCD_ROOT") or Path(__file__).resolve().parents[2])
sys.path.insert(0, str(ROOT / "tools" / "audits"))

import ledger_check as lc  # noqa: E402  (path is set above; this is deliberate)

STATE_PATH = "STATE.json"


def high_water(text, prefix):
    r"""Lexical max of the number half of every row minted under `prefix`. Raw strings only.

    Returns `None` for a ledger with no rows yet — which is a real state (four empty workstreams
    FAIL by design elsewhere) and is not the same as a missing entry.
    """
    tails = [lc.split_prefix(tok)[1] for tok, _ in lc.row_ids(text)
             if lc.split_prefix(tok)[0] == prefix]
    return max(tails) if tails else None


def judge(root, state):
    """-> list of failure strings. Empty means STATE.json and the ledgers agree."""
    errs = []
    hw = state.get("high_water")
    if not isinstance(hw, dict) or not hw:
        return ["STATE.json has no `high_water` object, or it is empty — a state file that "
                "records nothing cannot be checked and must not be treated as read"]

    for relpath, entry in sorted(hw.items()):
        if not isinstance(entry, dict) or "prefix" not in entry:
            errs.append(f"{relpath}: entry is not an object carrying a `prefix`")
            continue
        prefix = entry["prefix"]
        declared = entry.get("value")
        p = root / relpath
        if not p.exists():
            errs.append(f"{relpath}: named in STATE.json and ABSENT from disk — a frontier for a "
                        f"ledger that does not exist is not a stale number, it is a wrong file")
            continue
        actual = high_water(p.read_text(encoding="utf-8", errors="replace"), prefix)
        if declared != actual:
            errs.append(f"{relpath}: STATE.json says `{prefix}-{declared}` is the high water; the "
                        f"ledger's own rows say `{prefix}-{actual}`. A cache that disagrees with "
                        f"its source is worse than no cache — the next session would mint on the "
                        f"stale number (CD-154)")

    # COMPLETENESS. Without this, a new ledger is simply absent from STATE.json and every check
    # above still passes — the file would be correct about what it mentions and silent about what
    # it does not, which is how a frontier goes unrecorded.
    for p in lc.ledgers(root):
        text = lc.read(p)
        if lc.is_pointer(text) or not lc.row_ids(text):
            continue
        rel = p.relative_to(root).as_posix()
        if rel not in hw:
            errs.append(f"{rel}: a ledger with rows that STATE.json does not mention — "
                        f"the file is complete or it is not a state file")
    return errs


# ---------------------------------------------------------------------------------
# SELFTEST — synthetic fixtures only (CD-055, CD-064(f); seeds synthetic, CD-121(e))
# ---------------------------------------------------------------------------------

def selftest():
    import tempfile
    print("SELFTEST — the instrument is proven before any repo verdict (CD-025). Seeds are "
          "SYNTHETIC and drawn from no live ledger.")
    results = []

    def case(label, good):
        results.append((label, good))

    with tempfile.TemporaryDirectory() as d:
        r = Path(d)
        (r / "canon").mkdir()
        led = r / "canon" / "DECISIONS.md"

        def write(rows):
            body = ("# fixture\n\n<!-- ledger-prefix: ZZ -->\n<!-- ledger-lane: fixture -->\n\n"
                    "| id | date | note |\n|---|---|---|\n")
            body += "".join(f"| ZZ-{n} | 2026-01-01 | fixture row |\n" for n in rows)
            led.write_text(body, encoding="utf-8")

        def state(value):
            return {"high_water": {"canon/DECISIONS.md": {"prefix": "ZZ", "value": value}}}

        # --- 1. BASELINE. A gate that fires on everything is as useless as one that fires on none.
        write(["001", "002", "003"])
        case("baseline — STATE.json agrees with the ledger", not judge(r, state("003")))

        # --- 2. THE RULING'S OWN CASE: the cache is BEHIND. A row was filed and STATE not updated.
        write(["001", "002", "003", "004"])
        case("fires on: STATE.json BEHIND the ledger — a row was filed and the cache not updated",
             bool(judge(r, state("003"))))

        # --- 3. The opposite direction, and it is the more dangerous one: the cache is AHEAD.
        # --- A session that trusts it mints ZZ-005 while ZZ-004 is free, leaving a hole; a
        # --- session that re-derives finds ZZ-004 and collides with nothing. Both are wrong and
        # --- only the gate distinguishes them from a correct file.
        write(["001", "002", "003"])
        case("fires on: STATE.json AHEAD of the ledger — the number would leave a gap",
             bool(judge(r, state("004"))))

        # --- 4. Zero-padding is not normalised. `ZZ-4` and `ZZ-004` are two tokens (CD-088(d)(i)).
        write(["001", "002", "003"])
        case("fires on: `3` declared where the ledger mints `003` — padding is never collapsed",
             bool(judge(r, state("3"))))

        # --- 5. A named ledger that is not on disk.
        write(["001"])
        case("fires on: STATE.json names a ledger that does not exist",
             bool(judge(r, {"high_water": {"canon/GONE.md": {"prefix": "ZZ", "value": "001"}}})))

        # --- 6. COMPLETENESS: a ledger with rows that STATE.json never mentions.
        write(["001", "002"])
        other = r / "tools"
        other.mkdir()
        (other / "CORRECTIONS.md").write_text(
            "# fixture\n\n<!-- ledger-prefix: YY -->\n<!-- ledger-lane: fixture2 -->\n\n"
            "| id | date | note |\n|---|---|---|\n| YY-007 | 2026-01-01 | row |\n",
            encoding="utf-8")
        case("fires on: a ledger with rows that STATE.json does not mention at all",
             bool(judge(r, state("002"))))

        # --- 7. An empty STATE.json is not a pass.
        case("fires on: STATE.json with no `high_water` at all", bool(judge(r, {})))

    ok = True
    for label, good in results:
        print(f"  {'PASS' if good else 'FAIL'}  STATE-HIGH-WATER   {label}")
        ok = ok and good
    print(f"SELFTEST RESULT: {'PASS' if ok else 'FAIL'} ({len(results)} cases: "
          f"{len(results) - 1} seeded, 1 baseline)")
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="state_check.py",
        description="Assert STATE.json's high-water numbers against the ledgers' own rows.")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the instrument on synthetic seeds and exit")
    args = ap.parse_args(argv)

    if not selftest():
        print("\nRESULT: REFUSED (selftest red — no repo verdict is believable, nothing was judged)")
        return 2
    if args.selftest:
        return 0

    p = ROOT / STATE_PATH
    if not p.exists():
        print(f"\nRESULT: FAIL ({STATE_PATH} not found at {ROOT})")
        return 1
    try:
        state = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"\nRESULT: FAIL ({STATE_PATH} is not valid JSON: {e})")
        return 1

    print(f"\nSTATE.json read at {state.get('read_at', '«no read_at»')} "
          f"({state.get('read_on', '«no date»')})")
    errs = judge(ROOT, state)
    for relpath, entry in sorted((state.get("high_water") or {}).items()):
        print(f"  {relpath:<52} {entry.get('prefix', '?')}-{entry.get('value')}")
    print()
    for e in errs:
        print(f"  FAIL   STATE-HIGH-WATER   {e}")
    print(f"RESULT: {'FAIL' if errs else 'CLEAN'} ({len(errs)} failures)")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
