#!/usr/bin/env python3
"""canon_check.py — repo-wide canon gate (AGENTS.md §5, §8).

Checks, in order:
  1. MANIFEST   — every canon/MANIFEST.md row: REQUIRED file must exist (FAIL if missing);
                  PENDING file missing -> WARN (not yet slotted).
  2. PLACEHOLDER— any tracked file still containing the unslotted marker -> WARN.
  3. CD-CITE    — every CD-### cited anywhere must have a row in canon/DECISIONS.md -> FAIL.
  4. NO-COPY    — a file outside canon/ whose basename matches a canon file basename -> FAIL
                  (canon is cited, never copied).

Run from repo root:  python tools/audits/canon_check.py
Exit 0 = CLEAN (warnings allowed) · exit 1 = FAIL · exit 2 = REFUSE. Paste output verbatim
per AGENTS.md §5.

**A gate reports or refuses; it never omits (§7.17, CD-072) — and it must never HANG.**
PENDING-P-026: this gate slowed from ~1 s to ~95 s inside a single session as the canon tree
and `.git` grew, and it was read as a hang and reported as an unresolved RED. It was neither:
it was a slow gate with no budget, and a run that is still going produces no verdict at all —
which is *omission wearing an environment problem's clothes*. Two changes follow from that:

  (a) **A time budget that REFUSEs by name.** If the run exceeds `--budget` seconds it prints
      `RESULT: REFUSE — …` and exits 2. A REFUSE is not a PASS: AGENTS.md §5's "must pass
      before any push" is not satisfied by exit 2.
  (b) **The traversal stopped paying for what it discards.** `SKIP_DIRS` was applied *after*
      `rglob` had already descended — `.git` alone was 2418 of 4372 entries and was walked
      three times per run, then thrown away three times. The walk now prunes those directories
      as it goes, happens **once**, and each text file is **read once** and shared between the
      PLACEHOLDER and CD-CITE checks instead of being read twice. Measured on the tree that
      produced the report: walk ×3 + read ×2 ≈ 95 s -> one walk + one read.

**The budget's default is deliberately loose.** It exists to convert a pathological run into a
named refusal, not to police normal growth; a gate that refuses on a healthy repo is a gate
nobody runs.
"""
import argparse
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", "archive", "node_modules", "__pycache__", ".venv"}
PLACEHOLDER = "NOT YET SLOTTED"
TEXT_EXT = {".md", ".txt", ".py", ".json", ".js", ".csv", ".yml", ".yaml"}
DEFAULT_BUDGET = 300.0

fails, warns = [], []


class Refused(Exception):
    """The budget ran out. Never caught to produce a verdict — only to name the refusal."""


class Budget:
    def __init__(self, seconds):
        self.seconds = float(seconds)
        self.t0 = time.monotonic()
        self.where = "starting up"

    def stage(self, name):
        self.where = name
        self.check()

    def check(self):
        if self.seconds and (time.monotonic() - self.t0) > self.seconds:
            raise Refused(f"exceeded {self.seconds:g}s during {self.where}")


def walk(root, budget=None):
    """Every file under `root`, pruning SKIP_DIRS **during** traversal, not after.

    The old form was `root.rglob('*')` with the skip applied to what came back, so every
    entry under `.git` was still stat-ed and discarded — three times per run.
    """
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        if budget:
            budget.check()
        for fn in filenames:
            out.append(Path(dirpath) / fn)
    return out


def read_text_cache(files, root, budget=None):
    """Read every TEXT_EXT file once. Both text checks consume this, neither re-reads."""
    cache = {}
    for p in files:
        if p.suffix not in TEXT_EXT:
            continue
        if budget:
            budget.check()
        try:
            cache[p] = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
    return cache


def check_manifest(root):
    manifest = root / "canon" / "MANIFEST.md"
    if not manifest.exists():
        fails.append("MANIFEST: canon/MANIFEST.md is missing")
        return
    rows = re.findall(r"^\|\s*(canon/[^|]+?)\s*\|\s*(REQUIRED|PENDING)\s*\|",
                      manifest.read_text(encoding="utf-8"), re.M)
    if not rows:
        fails.append("MANIFEST: no parseable rows found")
    for path, status in rows:
        if not (root / path).exists():
            (fails if status == "REQUIRED" else warns).append(
                f"MANIFEST: {path} [{status}] missing"
                + ("" if status == "REQUIRED" else " (not yet slotted)"))


def check_placeholders(root, cache):
    for p, text in cache.items():
        # Gate scripts carry the marker as a string literal by necessity — skip tools/audits/*.py.
        rel = p.relative_to(root).as_posix()
        if rel.startswith("tools/audits/") and p.suffix == ".py":
            continue
        if PLACEHOLDER in text:
            warns.append(f"PLACEHOLDER: {p.relative_to(root)} still unslotted")


def check_cd_citations(root, cache):
    decisions = root / "canon" / "DECISIONS.md"
    known = set(re.findall(r"\bCD-(\d{3,})\b",
                decisions.read_text(encoding="utf-8"))) if decisions.exists() else set()
    for p, text in cache.items():
        if p == decisions:
            continue
        for num in set(re.findall(r"\bCD-(\d{3,})\b", text)):
            if num not in known:
                fails.append(f"CD-CITE: CD-{num} cited in {p.relative_to(root)} "
                             "but not in canon/DECISIONS.md (phantom citation)")


def check_no_copy(root, files):
    generic = {"README.md", "DECISIONS.md", "MANIFEST.md", "LOCAL.md",
               "STATE.md", "CORRECTIONS.md", "SCHOOL_FACTS.md"}
    canon_root = root / "canon"
    canon_names = {p.name for p in files
                   if p.name not in generic and canon_root in p.parents}
    for p in files:
        rel = p.relative_to(root)
        if rel.parts[0] != "canon" and p.name in canon_names:
            fails.append(f"NO-COPY: {rel} duplicates canon file '{p.name}' — cite, don't copy")


def run(root=ROOT, budget_s=DEFAULT_BUDGET, quiet=False):
    del fails[:], warns[:]
    b = Budget(budget_s)
    try:
        b.stage("MANIFEST")
        check_manifest(root)
        b.stage("walking the tree")
        files = walk(root, b)
        b.stage("reading text files")
        cache = read_text_cache(files, root, b)
        b.stage("PLACEHOLDER")
        check_placeholders(root, cache)
        b.stage("CD-CITE")
        check_cd_citations(root, cache)
        b.stage("NO-COPY")
        check_no_copy(root, files)
    except Refused as r:
        if not quiet:
            print(f"canon_check.py — root: {root}")
            print(f"RESULT: REFUSE — {r}. "
                  "No verdict was reached; this does NOT satisfy AGENTS.md §5 "
                  "(PENDING-P-026: a gate that produces no verdict has omitted, not passed).")
        return 2
    if not quiet:
        # **Elapsed time is part of the report, not a nicety (CD-080(d)).** This gate degraded
        # from ~1 s to ~95 s across several chapters while printing an unchanged CLEAN, and
        # nothing would have surfaced that until it crossed somebody's timeout and was read as
        # a hang. A verdict with no cost beside it hides its own trend.
        print(f"canon_check.py — root: {root}")
        for w in warns:
            print(f"  WARN  {w}")
        for f in fails:
            print(f"  FAIL  {f}")
        print(f"RESULT: {'FAIL' if fails else 'CLEAN'} "
              f"({len(fails)} fail, {len(warns)} warn) "
              f"· {time.monotonic() - b.t0:.1f}s elapsed, budget {b.seconds:g}s")
    return 1 if fails else 0


def selftest():
    """Seeded, synthetic — never drawn from the live file pool (CD-055, CD-064(f))."""
    import tempfile
    results = []

    def note(ok, label, got, want):
        results.append(ok)
        print(f"[{'PASS' if ok else 'FAIL'}] {label} -> {got} (wanted {want})")

    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        (root / "canon").mkdir()
        (root / "canon" / "MANIFEST.md").write_text(
            "| path | status |\n|---|---|\n| canon/DECISIONS.md | REQUIRED |\n", encoding="utf-8")
        (root / "canon" / "DECISIONS.md").write_text("| CD-001 | x | y | z |\n", encoding="utf-8")
        (root / "note.md").write_text("cites CD-001, which exists.\n", encoding="utf-8")

        note(run(root, DEFAULT_BUDGET, quiet=True) == 0,
             "control · a clean synthetic tree with a real budget", "CLEAN", "CLEAN")

        # The budget must bite, and must not be mistakable for a pass.
        rc = run(root, 1e-9, quiet=True)
        note(rc == 2, "seed · budget exhausted -> REFUSE, not a hang and not a PASS",
             {0: "CLEAN", 1: "FAIL", 2: "REFUSE"}.get(rc, rc), "REFUSE")
        note(rc != 0, "seed · REFUSE must never be reported as CLEAN",
             "not CLEAN" if rc != 0 else "CLEAN", "not CLEAN")

        # A phantom citation still FAILs — the budget did not soften the gate.
        # The token is BUILT, never written as a literal: a literal here would be a real
        # phantom citation inside the gate's own source, and CD-CITE would rightly FAIL the
        # repo on it. (It did, the first time this selftest was written.)
        phantom = "CD-" + "999"
        (root / "phantom.md").write_text(
            f"cites {phantom}, which does not exist.\n", encoding="utf-8")
        note(run(root, DEFAULT_BUDGET, quiet=True) == 1,
             "control · phantom CD citation still FAILs with the budget in place",
             "FAIL", "FAIL")

        # Pruning must not change what the gate sees: a skipped dir stays invisible.
        (root / ".git").mkdir()
        (root / ".git" / "note.md").write_text("NOT YET SLOTTED\n", encoding="utf-8")
        run(root, DEFAULT_BUDGET, quiet=True)
        note(not any(".git" in w for w in warns),
             "control · pruned directories are not reported (skip semantics unchanged)",
             "not reported", "not reported")

    print("-" * 78)
    print(f"SELFTEST: {'PASS' if all(results) else 'FAIL'}")
    return 0 if all(results) else 1


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--budget", type=float, default=float(
        os.environ.get("CANON_CHECK_BUDGET", DEFAULT_BUDGET)),
        help=f"seconds before the gate REFUSEs (default {DEFAULT_BUDGET:g}; 0 disables)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    sys.exit(selftest() if args.selftest else run(ROOT, args.budget))


if __name__ == "__main__":
    main()
