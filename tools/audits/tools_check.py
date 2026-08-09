#!/usr/bin/env python3
"""tools_check.py — repo-wide tooling gate (AGENTS.md §5, Step 2).

Counterpart to canon_check.py. Canon is slot-and-cite, so its gate asks "does the file exist".
Tools are executable, so existing proves nothing — this gate asks "does it parse, and has it
actually been run".

Checks, in order:
  1. MANIFEST  — every tools/MANIFEST.md row: REQUIRED file must exist (FAIL if missing);
                 PENDING missing -> WARN (Step 2, not yet vendored); DEFERRED -> silent.
  2. PLACEHOLDER— any tools/ README still carrying the unslotted marker -> WARN.
  3. SYNTAX    — every .py under tools/ must compile -> FAIL. Every .js/.mjs must pass
                 `node --check` -> FAIL (WARN once and skip if node is unavailable).
  4. SMOKE     — every tool folder holding a REQUIRED row must carry a SMOKE.md recording the
                 command run and its verbatim output -> FAIL. This is the rule that stops a
                 tool being called done merely because it was copied in.
  5. VENDOR    — tools/hub-export/ is vendored under the SCD Hub LOCKED import contract v1.0
                 (CD-003) and is supersede-only, never edited locally. Once populated it must
                 carry VENDOR.md naming the upstream source and version -> FAIL.

Run from repo root:  python tools/audits/tools_check.py
Exit 0 = CLEAN (warnings allowed) · exit 1 = FAIL. Paste output verbatim per AGENTS.md §5.
"""
import py_compile
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "tools"
PLACEHOLDER = "NOT YET SLOTTED"
# Gates evidence themselves: their own verbatim output is the record, so no SMOKE.md.
SMOKE_EXEMPT = {"tools/audits"}

fails, warns = [], []


def rows():
    """(path, status) from tools/MANIFEST.md."""
    manifest = TOOLS / "MANIFEST.md"
    if not manifest.exists():
        fails.append("MANIFEST: tools/MANIFEST.md is missing")
        return []
    found = re.findall(r"^\|\s*(tools/[^|]+?)\s*\|\s*(REQUIRED|PENDING|DEFERRED)\s*\|",
                       manifest.read_text(encoding="utf-8"), re.M)
    if not found:
        fails.append("MANIFEST: no parseable rows found")
    return found


def check_manifest(manifest_rows):
    for path, status in manifest_rows:
        if status == "DEFERRED" or (ROOT / path).exists():
            continue
        if status == "REQUIRED":
            fails.append(f"MANIFEST: {path} [REQUIRED] missing")
        else:
            warns.append(f"MANIFEST: {path} [PENDING] missing (not yet vendored)")


def check_placeholders():
    for p in sorted(TOOLS.rglob("*.md")):
        try:
            if PLACEHOLDER in p.read_text(encoding="utf-8"):
                warns.append(f"PLACEHOLDER: {p.relative_to(ROOT)} still unslotted")
        except (UnicodeDecodeError, OSError):
            pass


def check_syntax():
    for p in sorted(TOOLS.rglob("*.py")):
        try:
            py_compile.compile(str(p), doraise=True, cfile=str(p) + "c")
            Path(str(p) + "c").unlink(missing_ok=True)
        except py_compile.PyCompileError as e:
            fails.append(f"SYNTAX: {p.relative_to(ROOT)} does not compile — {e.msg.strip()}")

    js = sorted(list(TOOLS.rglob("*.js")) + list(TOOLS.rglob("*.mjs")))
    js = [p for p in js if "node_modules" not in p.parts]
    if not js:
        return
    if shutil.which("node") is None:
        warns.append(f"SYNTAX: node unavailable — {len(js)} JS file(s) unchecked")
        return
    for p in js:
        r = subprocess.run(["node", "--check", str(p)], capture_output=True, text=True)
        if r.returncode != 0:
            fails.append(f"SYNTAX: {p.relative_to(ROOT)} fails node --check — "
                         f"{r.stderr.strip().splitlines()[0] if r.stderr.strip() else 'error'}")


def check_smoke(manifest_rows):
    required_dirs = {str(Path(path).parent).replace("\\", "/")
                     for path, status in manifest_rows if status == "REQUIRED"}
    for d in sorted(required_dirs - SMOKE_EXEMPT):
        if not (ROOT / d / "SMOKE.md").exists():
            fails.append(f"SMOKE: {d}/ has a REQUIRED tool but no SMOKE.md — "
                         "a tool is done when it has been run, not when it has been placed")


def check_vendor():
    hub = TOOLS / "hub-export"
    if not hub.exists():
        return
    populated = [p for p in hub.iterdir() if p.is_file() and p.name != "README.md"]
    if populated and not (hub / "VENDOR.md").exists():
        fails.append("VENDOR: tools/hub-export/ is populated but has no VENDOR.md naming the "
                     "upstream source and contract version (CD-003; supersede-only)")


def main():
    manifest_rows = rows()
    check_manifest(manifest_rows)
    check_placeholders()
    check_syntax()
    check_smoke(manifest_rows)
    check_vendor()
    print(f"tools_check.py — root: {ROOT}")
    for w in warns:
        print(f"  WARN  {w}")
    for f in fails:
        print(f"  FAIL  {f}")
    print(f"RESULT: {'FAIL' if fails else 'CLEAN'} "
          f"({len(fails)} fail, {len(warns)} warn)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
