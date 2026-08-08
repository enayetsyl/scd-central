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
Exit 0 = CLEAN (warnings allowed) · exit 1 = FAIL. Paste output verbatim per AGENTS.md §5.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", "archive", "node_modules", "__pycache__", ".venv"}
PLACEHOLDER = "NOT YET SLOTTED"
TEXT_EXT = {".md", ".txt", ".py", ".json", ".js", ".csv", ".yml", ".yaml"}

fails, warns = [], []


def repo_files():
    for p in ROOT.rglob("*"):
        if p.is_file() and not (set(p.relative_to(ROOT).parts) & SKIP_DIRS):
            yield p


def check_manifest():
    manifest = ROOT / "canon" / "MANIFEST.md"
    if not manifest.exists():
        fails.append("MANIFEST: canon/MANIFEST.md is missing")
        return
    rows = re.findall(r"^\|\s*(canon/[^|]+?)\s*\|\s*(REQUIRED|PENDING)\s*\|",
                      manifest.read_text(encoding="utf-8"), re.M)
    if not rows:
        fails.append("MANIFEST: no parseable rows found")
    for path, status in rows:
        if not (ROOT / path).exists():
            (fails if status == "REQUIRED" else warns).append(
                f"MANIFEST: {path} [{status}] missing"
                + ("" if status == "REQUIRED" else " (not yet slotted)"))


def check_placeholders():
    for p in repo_files():
        if p.suffix in TEXT_EXT and p.name != "canon_check.py":
            try:
                if PLACEHOLDER in p.read_text(encoding="utf-8"):
                    warns.append(f"PLACEHOLDER: {p.relative_to(ROOT)} still unslotted")
            except (UnicodeDecodeError, OSError):
                pass


def check_cd_citations():
    decisions = ROOT / "canon" / "DECISIONS.md"
    known = set(re.findall(r"\bCD-(\d{3,})\b",
                decisions.read_text(encoding="utf-8"))) if decisions.exists() else set()
    for p in repo_files():
        if p.suffix in TEXT_EXT and p != decisions:
            try:
                text = p.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            for num in set(re.findall(r"\bCD-(\d{3,})\b", text)):
                if num not in known:
                    fails.append(f"CD-CITE: CD-{num} cited in {p.relative_to(ROOT)} "
                                 "but not in canon/DECISIONS.md (phantom citation)")


def check_no_copy():
    generic = {"README.md", "DECISIONS.md", "MANIFEST.md", "LOCAL.md",
               "STATE.md", "CORRECTIONS.md", "SCHOOL_FACTS.md"}
    canon_names = {p.name for p in (ROOT / "canon").rglob("*")
                   if p.is_file() and p.name not in generic}
    for p in repo_files():
        rel = p.relative_to(ROOT)
        if rel.parts[0] != "canon" and p.name in canon_names:
            fails.append(f"NO-COPY: {rel} duplicates canon file '{p.name}' — cite, don't copy")


def main():
    check_manifest()
    check_placeholders()
    check_cd_citations()
    check_no_copy()
    print(f"canon_check.py — root: {ROOT}")
    for w in warns:
        print(f"  WARN  {w}")
    for f in fails:
        print(f"  FAIL  {f}")
    print(f"RESULT: {'FAIL' if fails else 'CLEAN'} "
          f"({len(fails)} fail, {len(warns)} warn)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
