#!/usr/bin/env python3
"""
run_all.py — the single entry point for the scd-central gate suite.

  python tools/run_all.py --bank workstreams/question-banks/banks/C5_BAN_U19_QuestionBank_v1.json
  python tools/run_all.py --repo
  python tools/run_all.py --bank <path> --repo          (both; what a BUILD session runs)

WHAT THIS IS. Every handoff in this repo refers to "the full suite" as though one entry
point existed. None did — the suite was a convention an agent executed by hand, in an order
it remembered. This file is that convention made executable, and nothing more: it EXECUTES
and RECORDS. It judges nothing, interprets no gate's verdict, and adds no check of its own.
A gate's exit code is the verdict (AGENTS.md §5).

WHAT IT ADDS THAT HAND-RUNNING CANNOT. A run receipt (--receipt <path>) carrying the sha256
of the artifact, of every gate script invoked, and the full verbatim stdout of each. A
session that claims a clean suite without running it cannot produce a receipt whose hashes
survive re-hashing on another machine. That is the whole point: the receipt is checkable by
someone who was not there.

EXIT CODES.  0 = every gate CLEAN.  1 = at least one gate FAILed.  2 = a gate REFUSED
(canon_check's budget exhaustion) or could not be run at all. 2 is never folded into 1:
a gate that reached no verdict is a different object from one that reached a bad one, and
SOURCE_POLICY §7.17 requires the difference be visible.
"""
import argparse
import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# TOOLS-CR-012: the runner set PYTHONIOENCODING for its CHILDREN but not itself, so any
# redirect or pipe killed it on the first Bengali character. A4's hook runs it piped.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:                                               # noqa: BLE001
        pass

ROOT = Path(os.environ.get("SCD_ROOT") or Path(__file__).resolve().parents[1])

# Repo-wide hygiene gates: no required argument, verdict is repo-scoped.
# (math_arith_check / source_check / bangla_script_check / source_textcheck /
#  grid_count_check take a target path and are NOT part of a default pass.)
REPO_GATES = [
    ("CANON-CHECK",    ["tools/audits/canon_check.py"]),
    ("LEDGER-CHECK",   ["tools/audits/ledger_check.py"]),
    ("INT-ID-CHECK",   ["tools/audits/int_id_check.py"]),
    ("SLOT-REGISTER",  ["tools/audits/slot_register_check.py"]),
    ("TOOLS-CHECK",    ["tools/audits/tools_check.py"]),
    ("BANK-SWEEP",     ["workstreams/question-banks/audits/gates.py"]),
]

BANK_GATE = ("BANK-GATES", ["workstreams/question-banks/audits/gates.py"])


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def git(*args):
    try:
        return subprocess.run(["git", "-C", str(ROOT), *args],
                              capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception:
        return ""


def git_config(key):
    """One git config key. None means UNSET, which is distinct from set-to-empty.
    A1: two receipts disagreeing is only diagnosable if each records its machine."""
    try:
        p = subprocess.run(["git", "-C", str(ROOT), "config", "--get", key],
                           capture_output=True, text=True, timeout=30)
    except Exception:
        return None
    return p.stdout.strip() if p.returncode == 0 else None


def run_gate(name, argv, extra=None):
    """Execute one gate. Returns a receipt row. Never interprets the verdict."""
    script = ROOT / argv[0]
    if not script.exists():
        return {"gate": name, "script": argv[0], "script_sha256": None,
                "exit_code": 2, "elapsed_s": 0.0, "stdout": "",
                "error": f"gate script not found at {script}"}

    cmd = [sys.executable, str(script)] + [str(a) for a in (extra or [])]
    env = dict(os.environ, PYTHONIOENCODING="utf-8", SCD_ROOT=str(ROOT))
    t0 = time.time()
    try:
        p = subprocess.run(cmd, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", env=env, cwd=str(ROOT))
        out, code = (p.stdout or "") + (p.stderr or ""), p.returncode
    except Exception as e:                                          # noqa: BLE001
        out, code = f"{type(e).__name__}: {e}", 2

    return {"gate": name, "script": argv[0], "script_sha256": sha256(script),
            "exit_code": code, "elapsed_s": round(time.time() - t0, 1),
            "stdout": out}


def parse_bank_output(text):
    """Pull the facts the receipt should carry. Reads output; asserts nothing."""
    facts = {}
    m = re.search(r"^SUITE:\s*(\d+)\s*gates", text, re.M)
    if m:
        facts["suite_gate_count"] = int(m.group(1))
    facts["na_gates"] = re.findall(r"^\s*N/A\s+(\S+)", text, re.M)
    facts["fail_gates"] = re.findall(r"^\s*FAIL\s+(\S+)", text, re.M)
    m = re.search(r"digest\s+([0-9a-f]{8,})", text)
    if m:
        facts["envelope_digest"] = m.group(1)
    m = re.search(r"^SELFTEST RESULT:\s*(\w+)", text, re.M)
    if m:
        facts["selftest"] = m.group(1)
    facts["selftest_results"] = re.findall(r"^SELFTEST RESULT:\s*(\w+)", text, re.M)
    m = re.search(r"^RESULT:\s*(CLEAN|FAIL)", text, re.M)
    if m:
        facts["result"] = m.group(1)
    return facts


# A2 · Principal, 2026-08-19. Files under canon/sources/ that are NOT extractions and
# therefore cannot carry a `**\u098f\u0987 \u09ab\u09be\u0987\u09b2\u09c7\u09b0 \u0985\u0982\u09b6:**` scope line or a spot-check sign-off.
# source_check judges them RED by construction. They are EXEMPTED BY NAME, never by
# pattern: a rule like "skip anything without _Source_ in the name" would silently drop
# a real extraction that was misnamed, which is the failure this whole lane exists to
# prevent. Each entry carries its reason, and each is PRINTED on every run.
EXEMPT_SOURCES = {
    "canon/sources/README.md":
        "lane README \u2014 explains the directory, extracts nothing",
    "canon/sources/c5/english/evidence/TEXTLAYER_ARTEFACTS_U11_U12_2026-08-09.md":
        "evidence note \u2014 records a text-layer artefact, is not a source extraction",
    "canon/sources/c5/english/evidence/TEXTLAYER_ARTEFACTS_U17_U19_2026-08-09.md":
        "evidence note \u2014 records a text-layer artefact, is not a source extraction",
}


def run_sources():
    """Walk canon/sources/**/*.md and judge each with source_check.py.

    A2. Five of eleven tools/audits scripts take a path argument and are run by
    nothing in a default pass; that is how a Principal-ruled source_check fix sat
    uncommitted for two days while every gate run reported clean.

    THE SKIP (CD-152(d)). Files carrying source_check's own UNDER_CONSTRUCTION
    literal are held out and NAMED BEFORE THE VERDICT. A naive walk reddens 92 of
    126 in-progress files permanently, and a permanently red gate is one everybody
    learns to wave through.

    THE CODE MAP. source_check.py returns 2=FAIL, 1=PENDING(sign-off owed), 0=GREEN.
    run_all.py reads 1=FAILED and anything else=REFUSED. The two are INVERTED, so a
    red source would record as REFUSED and a merely unsigned one as FAILED. This
    function maps at the boundary and does not touch source_check.py.

    PENDING IS REPORTED, NOT FAILED (Principal, 2026-08-19). Sign-off is a human
    step; failing on it would make the gate permanently red for the same reason the
    skip exists. Every unsigned file is named.

    Every judged file is named whatever its verdict, including the three that are not
    extractions at all (README, evidence/) and cannot satisfy a scope line (Principal
    ruled them judged and listed rather than filtered out, 2026-08-19).
    """
    marker = "**\u0985\u09ac\u09b8\u09cd\u09a5\u09be:** \u09a8\u09bf\u09b0\u09cd\u09ae\u09be\u09a3\u09be\u09a7\u09c0\u09a8"
    script = ROOT / "tools/audits/source_check.py"
    if not script.exists():
        return {"gate": "SOURCES", "script": "tools/audits/source_check.py",
                "script_sha256": None, "exit_code": 2, "elapsed_s": 0.0, "stdout": "",
                "error": f"gate script not found at {script}"}

    t0 = time.time()
    files = sorted((ROOT / "canon/sources").rglob("*.md"))
    held = [f for f in files if marker in f.read_text(encoding="utf-8", errors="replace")]
    exempt = [f for f in files
              if f not in held and f.relative_to(ROOT).as_posix() in EXEMPT_SOURCES]
    judged = [f for f in files if f not in held and f not in exempt]

    env = dict(os.environ, PYTHONIOENCODING="utf-8", SCD_ROOT=str(ROOT))
    rows = []
    for f in judged:
        p = subprocess.run([sys.executable, str(script), str(f)], capture_output=True,
                           text=True, encoding="utf-8", errors="replace", env=env, cwd=str(ROOT))
        rows.append((f, p.returncode, (p.stdout or "") + (p.stderr or "")))

    red = [f for f, c, _ in rows if c == 2]
    pending = [f for f, c, _ in rows if c == 1]
    green = [f for f, c, _ in rows if c == 0]
    odd = [(f, c) for f, c, _ in rows if c not in (0, 1, 2)]

    out = []
    out.append(f"source pass — canon/sources/**/*.md   ({len(files)} file(s))")
    out.append("-" * 78)
    out.append(f"HELD OUT — carry the \u09a8\u09bf\u09b0\u09cd\u09ae\u09be\u09a3\u09be\u09a7\u09c0\u09a8 marker, not judged: {len(held)}")
    for f in held:
        out.append(f"  SKIP     {f.relative_to(ROOT).as_posix()}")
    out.append("-" * 78)
    out.append(f"EXEMPT \u2014 not extractions, cannot satisfy \u00a75; named individually, never by pattern: {len(exempt)}")
    for f in exempt:
        rel = f.relative_to(ROOT).as_posix()
        out.append(f"  EXEMPT   {rel}")
        out.append(f"           reason: {EXEMPT_SOURCES[rel]}")
    for rel in sorted(EXEMPT_SOURCES):
        if not (ROOT / rel).exists():
            out.append(f"  STALE    {rel} \u2014 exempted but no longer on disk; the list has drifted")
    out.append("-" * 78)
    out.append(f"JUDGED: {len(judged)}")
    for f, c, _ in rows:
        label = {0: "GREEN", 1: "PENDING", 2: "FAIL"}.get(c, f"EXIT-{c}")
        out.append(f"  {label:8} {f.relative_to(ROOT).as_posix()}")
    out.append("-" * 78)
    if pending:
        out.append(f"PENDING — mechanical checks pass, spot-check sign-off owed: {len(pending)}")
        out.append("  REPORTED, NOT FAILED (Principal, 2026-08-19). Sign-off is a human step.")
        for f in pending:
            out.append(f"  PENDING  {f.relative_to(ROOT).as_posix()}")
    for f, c in odd:
        out.append(f"  UNEXPECTED EXIT {c} — {f.relative_to(ROOT).as_posix()}")
    out.append(f"SOURCES: {len(green)} green \u00b7 {len(pending)} pending \u00b7 {len(red)} fail "
               f"\u00b7 {len(held)} held out \u00b7 {len(exempt)} exempt \u00b7 {len(files)} total")
    if red or odd:
        out.append("RESULT: FAIL")
        code = 1
    else:
        out.append("RESULT: CLEAN (0 failures)")
        code = 0

    return {"gate": "SOURCES", "script": "tools/audits/source_check.py",
            "script_sha256": sha256(script), "exit_code": code,
            "elapsed_s": round(time.time() - t0, 1), "stdout": "\n".join(out),
            "sources": {"total": len(files), "held_out": len(held),
                        "exempt": {f.relative_to(ROOT).as_posix(): EXEMPT_SOURCES[f.relative_to(ROOT).as_posix()] for f in exempt},
                        "green": [f.relative_to(ROOT).as_posix() for f in green],
                        "pending": [f.relative_to(ROOT).as_posix() for f in pending],
                        "fail": [f.relative_to(ROOT).as_posix() for f in red]}}


def main():
    ap = argparse.ArgumentParser(description="Run the scd-central gate suite and emit a receipt")
    ap.add_argument("--bank", help="path to a question-bank JSON (artifact lane)")
    ap.add_argument("--repo", action="store_true", help="run the repo-wide hygiene gates + bank sweep")
    ap.add_argument("--sources", action="store_true",
                    help="judge canon/sources/**/*.md (A2); implied by --repo")
    ap.add_argument("--receipt", help="write the run receipt JSON here")
    ap.add_argument("--quiet", action="store_true", help="suppress gate stdout (receipt still carries it verbatim)")
    args = ap.parse_args()

    # TOOLS-CR-011: read BEFORE any gate runs and before this run writes its own
    # receipt into the tree. Assembly-time made the field describe its own output.
    tree_dirty_at_start = bool(git("status", "--porcelain"))

    if not args.bank and not args.repo and not args.sources:
        ap.error("nothing to run: pass --bank <path> and/or --repo and/or --sources")

    rows = []

    if args.bank:
        bank_path = Path(args.bank)
        if not bank_path.is_absolute():
            bank_path = ROOT / bank_path
        if not bank_path.exists():
            sys.stderr.write(f"run_all.py: bank not found at {bank_path}\n")
            sys.exit(2)
        rows.append(run_gate(*BANK_GATE, extra=[bank_path]))

    if args.repo:
        for name, argv in REPO_GATES:
            rows.append(run_gate(name, argv))

    # Principal, 2026-08-19: --repo RUNS the source pass. A2 exists because a script
    # nobody runs by default is how a ruled fix sat uncommitted for two days; keeping
    # --sources opt-in would move that same risk onto whoever writes the hook line.
    if args.sources or args.repo:
        rows.append(run_sources())

    for r in rows:
        if not args.quiet:
            print(f"\n{'=' * 78}\n=== {r['gate']}  ({r['script']})  exit={r['exit_code']}  {r['elapsed_s']}s\n{'=' * 78}")
            print(r["stdout"].rstrip())
        if r["gate"] in ("BANK-GATES", "BANK-SWEEP"):
            r["parsed"] = parse_bank_output(r["stdout"])

    failed = [r["gate"] for r in rows if r["exit_code"] == 1]
    refused = [r["gate"] for r in rows if r["exit_code"] not in (0, 1)]

    receipt = {
        "run_all_version": "2",
        "run_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "root": str(ROOT),
        "git": {"head": git("rev-parse", "HEAD"),
                "branch": git("rev-parse", "--abbrev-ref", "HEAD"),
                "dirty": tree_dirty_at_start},
        "python": sys.version.split()[0],
        "machine": {"platform": sys.platform,
                    "os": platform.platform(),
                    "core.symlinks": git_config("core.symlinks"),
                    "core.autocrlf": git_config("core.autocrlf")},
        "artifact": None,
        "gates": rows,
        "failed": failed,
        "refused": refused,
        "verdict": "REFUSED" if refused else ("FAIL" if failed else "CLEAN"),
    }
    if args.bank:
        receipt["artifact"] = {"path": str(Path(args.bank).as_posix()),
                               "sha256": sha256(bank_path)}

    print(f"\n{'=' * 78}")
    print(f"RUN_ALL VERDICT: {receipt['verdict']}   "
          f"({len(rows)} gate run(s), {len(failed)} FAIL, {len(refused)} REFUSED)")
    if failed:
        print("  FAILED:  " + ", ".join(failed))
    if refused:
        print("  REFUSED: " + ", ".join(refused) + "   — no verdict reached; this does NOT satisfy AGENTS §5")
    if receipt["git"]["dirty"]:
        print("  NOTE: working tree is dirty — the receipt records the state that was actually run")

    if args.receipt:
        rp = Path(args.receipt)
        rp.parent.mkdir(parents=True, exist_ok=True)
        rp.write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  receipt: {rp}")

    # CD-176 — machine-readable sentinel, ALWAYS THE LAST LINE of stdout, on every path.
    # The prose "RUN_ALL VERDICT:" line above is not last (FAILED / REFUSED / dirty /
    # receipt lines follow it conditionally), and exit 2 is shared with argparse's own
    # usage error. Neither position nor exit code alone tells a consumer that a verdict
    # was actually reached. Absence of this line is a refusal, not a silence.
    print(f"RUNALL_SENTINEL={receipt['verdict']}")

    sys.exit(2 if refused else (1 if failed else 0))


if __name__ == "__main__":
    main()
