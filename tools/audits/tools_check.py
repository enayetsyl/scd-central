#!/usr/bin/env python3
"""tools_check.py — repo-wide tooling gate (AGENTS.md §5, Step 2).

Counterpart to canon_check.py. Canon is slot-and-cite, so its gate asks "does the file exist".
Tools are executable, so existing proves nothing — this gate asks "does it parse, and has it
actually been run".

Checks, in order:
  1. MANIFEST  — three live statuses, meaning three different states of proof (CD-020):
                   PENDING           = not vendored. Missing -> WARN. PRESENT -> WARN, because
                                       the row is now lying; reclassify it.
                   VENDORED-UNPROVEN = present but never executed. Missing -> FAIL (the row
                                       claims otherwise). Not named in its folder's SMOKE.md
                                       -> WARN, and that warn is correct until it is run.
                                       Named -> WARN to promote it to REQUIRED.
                   REQUIRED          = proven. Missing -> FAIL. Not named in its folder's
                                       SMOKE.md -> FAIL: REQUIRED asserts proof, and a tool no
                                       smoke run mentions has none.
                   DEFERRED          = deliberately not vendored -> silent.
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
import tempfile
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
    found = re.findall(
        r"^\|\s*(tools/[^|]+?)\s*\|\s*(REQUIRED|VENDORED-UNPROVEN|PENDING|DEFERRED)\s*\|",
        manifest.read_text(encoding="utf-8"), re.M)
    if not found:
        fails.append("MANIFEST: no parseable rows found")
    return found


def smoke_names(path):
    """How the folder's SMOKE.md mentions this file (CD-020).

    Returns "proven" | "declared-unproven" | "absent".

    A line that names the file AND contains "UNPROVEN" is an explicit statement that the tool
    has not been run. Treating that as proof would invert the meaning of the sentence — which
    is exactly what a naive substring search does.
    """
    smoke = (ROOT / path).parent / "SMOKE.md"
    if not smoke.exists():
        return "absent"
    try:
        lines = smoke.read_text(encoding="utf-8").splitlines()
    except OSError:
        return "absent"
    name = Path(path).name
    hits = [ln for ln in lines if name in ln]
    if not hits:
        return "absent"
    if all("UNPROVEN" in ln.upper() for ln in hits):
        return "declared-unproven"
    return "proven"


def check_manifest(manifest_rows):
    for path, status in manifest_rows:
        if status == "DEFERRED":
            continue
        exists = (ROOT / path).exists()
        folder = str(Path(path).parent).replace("\\", "/")

        if status == "PENDING":
            if not exists:
                warns.append(f"MANIFEST: {path} [PENDING] missing (not yet vendored)")
            else:
                warns.append(f"MANIFEST: {path} [PENDING] but the file is PRESENT — the row is "
                             "stale; reclassify VENDORED-UNPROVEN (or REQUIRED once proven)")
            continue

        if status == "VENDORED-UNPROVEN":
            if not exists:
                fails.append(f"MANIFEST: {path} [VENDORED-UNPROVEN] missing — the row claims it "
                             "is vendored")
            elif smoke_names(path) == "proven":
                warns.append(f"MANIFEST: {path} [VENDORED-UNPROVEN] has a run recorded in "
                             f"{folder}/SMOKE.md — promote it to REQUIRED")
            else:
                warns.append(f"MANIFEST: {path} [VENDORED-UNPROVEN] vendored but never executed "
                             f"— no run recorded in {folder}/SMOKE.md")
            continue

        # REQUIRED
        if not exists:
            fails.append(f"MANIFEST: {path} [REQUIRED] missing")
        elif folder not in SMOKE_EXEMPT and smoke_names(path) != "proven":
            fails.append(f"MANIFEST: {path} [REQUIRED] has no run recorded in "
                         f"{folder}/SMOKE.md — REQUIRED asserts the tool is proven")


def _code_span_mask(line):
    """True at every column inside an inline `code span`.

    Mechanism lifted verbatim from `tools/audits/bangla_script_check.py` (SOURCE_POLICY §7.16) and
    from `canon_check.py` (CD-085). **Copied to each gate rather than shared**: these gates run
    independently and one must not be able to break the others by refactor. Any change here is
    owed to all three.
    """
    mask = [False] * len(line)
    inside, start = False, 0
    for i, ch in enumerate(line):
        if ch == "`":
            if inside:
                for j in range(start, i + 1):
                    mask[j] = True
            else:
                start = i
            inside = not inside
    return mask


def count_outside_code(text, needle):
    """Occurrences of `needle` not inside an inline code span. Per-line, so an unclosed
    backtick cannot swallow the rest of the file. Fenced blocks are deliberately not exempt."""
    n = 0
    for line in text.splitlines():
        mask = _code_span_mask(line)
        i = line.find(needle)
        while i != -1:
            if not mask[i]:
                n += 1
            i = line.find(needle, i + 1)
    return n


def check_placeholders():
    """The unslotted marker, outside inline code spans (AGENTS.md §5.1, CD-089).

    A file that *retires* a placeholder has to be able to name the marker it retires. Without the
    exemption the retirement note re-fires the warn it was written to end, and the author routes
    around the gate by describing the string instead of writing it — which is what happened, and
    what promoted this from a patch to a design rule. Bare prose still warns.
    """
    for p in sorted(TOOLS.rglob("*.md")):
        try:
            if count_outside_code(p.read_text(encoding="utf-8"), PLACEHOLDER):
                warns.append(f"PLACEHOLDER: {p.relative_to(ROOT)} still unslotted")
        except (UnicodeDecodeError, OSError):
            pass


def check_syntax():
    # Compile into a throwaway temp dir rather than beside the source. The old form wrote
    # <file>.pyc into the repo and then unlinked it, which fails outright in the Cowork sandbox
    # (PermissionError on the mounted folder) and left the gate unable to run at all. Nothing
    # about what is checked changes — only where the byte-code lands. CD-040.
    with tempfile.TemporaryDirectory() as tmp:
        for i, p in enumerate(sorted(TOOLS.rglob("*.py"))):
            try:
                py_compile.compile(str(p), doraise=True,
                                   cfile=str(Path(tmp) / f"{i}_{p.name}c"))
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


def selftest():
    """Seeded, synthetic — never drawn from the live file pool (CD-055, CD-064(f)).

    Covers exactly the one behaviour CD-089 changed here. The marker is **built**, never written
    as a literal: a literal in this file would be a real unslotted marker in the gate's own
    source, and while the `tools/audits/*.py` carve-out happens to cover it in `canon_check.py`,
    relying on a carve-out to hide a fixture is how CD-080(e) happened.
    """
    results = []

    def note(ok, label, got, want):
        results.append(ok)
        print(f"[{'PASS' if ok else 'FAIL'}] {label} -> {got} (wanted {want})")

    m = "NOT YET " + "SLOTTED"
    note(count_outside_code(f"the `{m}` marker is retired here.\n", m) == 0,
         "seed · marker named in `backticks` -> not counted "
         "(the retirement stays writeable)", 0, 0)
    note(count_outside_code(f"this folder is {m}.\n", m) == 1,
         "control · marker bare in prose -> counted (exemption is backticks only)", 1, 1)
    note(count_outside_code(f"```\n{m}\n```\n", m) == 1,
         "control · marker inside a FENCED block -> still counted "
         "(§7.16 makes the same choice)", 1, 1)
    note(count_outside_code(f"`{m}` and then a bare {m}.\n", m) == 1,
         "seed · one quoted + one bare on the same line -> exactly the bare one counts", 1, 1)
    note(count_outside_code(f"an unclosed ` backtick then {m} on the NEXT line is bare.\n"
                            f"{m}\n", m) == 2,
         "seed · an unclosed backtick cannot swallow the next line (per-line masking)", 2, 2)
    print("-" * 78)
    print(f"SELFTEST: {'PASS' if all(results) else 'FAIL'}")
    return 0 if all(results) else 1


def main():
    if "--selftest" in sys.argv:
        sys.exit(selftest())
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
