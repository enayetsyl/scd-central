#!/usr/bin/env python3
"""canon_check.py — repo-wide canon gate (AGENTS.md §5, §8).

Checks, in order:
  1. MANIFEST   — every canon/MANIFEST.md row: REQUIRED file must exist (FAIL if missing);
                  PENDING file missing -> WARN (not yet slotted).
  2. PLACEHOLDER— any tracked file still containing the unslotted marker -> WARN.
  3. CD-CITE    — every CD-### cited anywhere must have a row in canon/DECISIONS.md -> FAIL.
  4. REF-CITE   — every REF-NN cited anywhere must have a row in canon/refs/MANIFEST.md -> FAIL.
                  Retired support-book numbers (REF-1, REF-2) resolve through the manifest's
                  HISTORICAL alias rows and PASS, with a WARN census (see below).
  5. NO-COPY    — a file outside canon/ whose basename matches a canon file basename -> FAIL
                  (canon is cited, never copied).

**REF-CITE and the two numbering series (Principal ruling UD-60(b)).** P00's `REF-01…REF-26` is
the numbering in force. The support-book lineage's `REF-1` / `REF-2` are retired, but the ~118
historical citations across the repo are **left as written** — rewriting `SESSION_LOG.md` or
`canon/DECISIONS.md` to say something they did not say at the time is a worse violation than
carrying an alias. So an SB-series citation **resolves and passes**; it is correct history.

**Telling a new SB citation from a historical one — the baseline census.** The ruling asks that a
*newly written* SB citation FAIL while historical ones pass. The resolver alone cannot do that: it
sees a file's current bytes, and "new" is a fact about when a line was written. **The baseline
supplies the missing fact without git archaeology.** `canon/refs/SB_CITATION_BASELINE.md` freezes
the census taken at unification — one row per file, with its SB-citation count. Thereafter:

  * a file whose count **exceeds** its baseline row -> **FAIL** (a citation was added);
  * a file **absent from the baseline** carrying any SB citation -> **FAIL** (a new file citing
    retired numbering);
  * a file whose count **equals or falls below** its row -> silent (history, or a cleanup).

**A citation swapped one-for-one inside an already-listed file is not caught**, because the count
does not move. That is the residual hole and it is stated rather than papered over; closing it
needs per-line provenance, which is the git archaeology this deliberately avoids.

**A citation inside `backticks` is exempt from the SB census — SOURCE_POLICY §7.16 applied by
analogy (Principal ruling 2026-08-14, unification session-2 ruling 1).** §7.16 exempts a
backticked `প্ৰাথমিক` from the Assamese gate because *"a gate that forbids naming the defect
makes the defect unwriteable"*. The reasoning transfers unchanged: the manifest's HISTORICAL
rows, this docstring, `tools/CORRECTIONS.md` and every future session log have to be able to
**name the retired number in order to say it is retired**. Inline code is already markdown's way
of saying "literal string, not prose". **Bare prose stays counted**, so a newly written bare
`REF-1` above baseline still FAILs, and — as in §7.16 — **fenced blocks are still counted**.

**The exemption is scoped to the SB census and NOT to phantom resolution.** §7.16's rationale is
about naming *the retired number*; a two-digit REF with no register row is a broken citation
whether or not it wears backticks, and exempting it would hollow out the resolver. Scoping
recorded here because the ruling's one-line form ("REF-CITE exempts backticked citations") is
wider than its reason. *(No phantom number is written out in this file even in backticks — the
exemption is census-only, so the resolver would rightly FAIL on it. It did, on the first run of
this edit: the CD-080(e) trap, reached from the REF side.)*

**The baseline is regenerated only by ruling** — `--write-sb-baseline` exists but is never run to
make a red gate green. Re-freezing after an unapproved addition would launder exactly what the
check exists to catch, so the flag prints that warning every time it is used.

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


def _code_span_mask(line):
    """True at every column that sits inside an inline `code span`.

    Mechanism lifted verbatim from `tools/audits/bangla_script_check.py`, which implements
    SOURCE_POLICY §7.16's backtick exemption. It is copied rather than imported on purpose: the
    two gates are run independently and one must not be able to break the other by refactor.
    Any change here is owed to that file too.
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


def count_outside_code(text, pattern):
    """Occurrences of `pattern` that are NOT inside an inline code span.

    Per-line, like §7.16's gate: an unclosed backtick cannot swallow the rest of the file.
    Fenced blocks are deliberately not exempted — §7.16 makes the same choice for the same
    reason, that a fence carries authored content rather than a citation.
    """
    n = 0
    for line in text.splitlines():
        mask = _code_span_mask(line)
        for m in re.finditer(pattern, line):
            if not mask[m.start()]:
                n += 1
    return n


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
    """The unslotted marker, outside inline code spans (AGENTS.md §5.1, CD-089).

    **The backtick exemption is the same one at its third site.** A file that *retires* a
    placeholder has to be able to name the marker it is retiring — the retirement note, the
    DEFERRED row that replaces it, the decision row that ruled it. Without the exemption both
    of those re-fire the warn they were written to end, and the author routes around the gate by
    describing the string instead of writing it. That happened, and it is what promoted this from
    a patch to §5.1.

    Bare prose still warns; fenced blocks are still checked. The `tools/audits/*.py` carve-out is
    retained unchanged — a gate script holds the marker as a module constant, not a citation.
    """
    for p, text in cache.items():
        # Gate scripts carry the marker as a string literal by necessity — skip tools/audits/*.py.
        rel = p.relative_to(root).as_posix()
        if rel.startswith("tools/audits/") and p.suffix == ".py":
            continue
        if count_outside_code(text, re.escape(PLACEHOLDER)):
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


def parse_ref_manifest(root):
    """Return (current_ids, alias_ids) from canon/refs/MANIFEST.md.

    IDs are kept as the **raw string the register writes**, never integer-normalised. Normalising
    was the first version's bug and it is worth recording: `int("01") == int("1")`, so P00's
    `REF-01` and the retired `REF-1` collapsed to one key, the alias set was swallowed by the
    current set, and every SB citation silently stopped being censused while the gate still
    reported CLEAN. **The two series are distinguished by width; a normaliser that erases width
    erases the distinction the check exists to make.**

    Missing manifest is a FAIL, never a silent skip: a resolver with no register resolves
    nothing, and reporting nothing would be omission (SOURCE_POLICY §7.17, CD-072).
    """
    manifest = root / "canon" / "refs" / "MANIFEST.md"
    if not manifest.exists():
        fails.append("REF-CITE: canon/refs/MANIFEST.md is missing — no REF citation can resolve")
        return None, None
    text = manifest.read_text(encoding="utf-8")
    current, alias = set(), set()
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip().strip("*` ") for c in line.strip().strip("|").split("|")]
        if not cells:
            continue
        m = re.fullmatch(r"REF-(\d{1,2})", cells[0])
        if not m:
            continue
        # The two series are told apart by the width the register writes them at, which is the
        # same thing that makes them two series: P00 is zero-padded two-digit (REF-01…REF-26),
        # the retired support-book numbers are bare single digits (REF-1, REF-2).
        raw = m.group(1)
        (current if len(raw) == 2 else alias).add(raw)
    if not current:
        fails.append("REF-CITE: canon/refs/MANIFEST.md has no parseable register rows")
    return current, alias


def check_ref_citations(root, cache):
    current, alias = parse_ref_manifest(root)
    if current is None:
        return
    known = current | alias
    # The register and the baseline both name the retired numbers by definition — they are the
    # files that *define* the aliases. Censusing them would have the baseline fail itself.
    self_referential = {root / "canon" / "refs" / "MANIFEST.md",
                        root / "canon" / "refs" / "SB_CITATION_BASELINE.md"}
    sb_census = {}
    for p, text in cache.items():
        if p in self_referential:
            continue
        rel = p.relative_to(root)
        seen = set(re.findall(r"\bREF-(\d{1,2})\b", text))
        for raw in sorted(seen):
            if raw not in known:
                fails.append(f"REF-CITE: REF-{raw} cited in {rel} but has no row in "
                             "canon/refs/MANIFEST.md (phantom citation)")
            elif raw in alias:
                # Backticked citations are exempt (§7.16 by analogy — see the module docstring).
                # A file left at zero after the exemption does not enter the census at all.
                n = count_outside_code(text, rf"\bREF-{raw}\b")
                if n:
                    sb_census[rel] = sb_census.get(rel, 0) + n
    _judge_sb_census(root, sb_census)


def read_sb_baseline(root):
    """Parse canon/refs/SB_CITATION_BASELINE.md -> {posix path: count}, or None if absent."""
    p = root / "canon" / "refs" / "SB_CITATION_BASELINE.md"
    if not p.exists():
        return None
    out = {}
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip().strip("`* ") for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[1].isdigit():
            out[cells[0]] = int(cells[1])
    return out


def _judge_sb_census(root, sb_census):
    """Compare the live census against the frozen baseline (see module docstring)."""
    baseline = read_sb_baseline(root)
    total = sum(sb_census.values())
    if baseline is None:
        if sb_census:
            warns.append(
                f"REF-CITE: {total} retired support-book citation(s) (REF-1/REF-2) across "
                f"{len(sb_census)} file(s). **No baseline frozen** "
                "(canon/refs/SB_CITATION_BASELINE.md absent) — new citations CANNOT be told from "
                "historical ones. Warning only.")
        return
    for rel, n in sorted(sb_census.items(), key=lambda kv: str(kv[0])):
        key = rel.as_posix()
        was = baseline.get(key)
        if was is None:
            fails.append(
                f"REF-CITE: {key} carries {n} retired support-book citation(s) (REF-1/REF-2) and "
                "is NOT in canon/refs/SB_CITATION_BASELINE.md — new citations must use P00 "
                "numbering (REF-01…REF-26) per UD-60(b)")
        elif n > was:
            fails.append(
                f"REF-CITE: {key} has {n} retired support-book citation(s), baseline {was} "
                f"(+{n - was}) — a retired REF-1/REF-2 citation was ADDED; new citations must use "
                "P00 numbering per UD-60(b)")
    if total:
        warns.append(
            f"REF-CITE: {total} retired support-book citation(s) across {len(sb_census)} file(s), "
            "all at or below their frozen baseline — correct history under UD-60(b). "
            "(A one-for-one swap inside a listed file does not move its count and is not caught.)")


def write_sb_baseline(root, budget_s=DEFAULT_BUDGET):
    """Re-freeze the baseline. Never run to turn a red gate green — see the module docstring."""
    b = Budget(budget_s)
    files = walk(root, b)
    cache = read_text_cache(files, root, b)
    current, alias = parse_ref_manifest(root)
    if not alias:
        print("REFUSE — no HISTORICAL alias rows in canon/refs/MANIFEST.md; nothing to baseline.")
        return 2
    manifest = root / "canon" / "refs" / "MANIFEST.md"
    out = root / "canon" / "refs" / "SB_CITATION_BASELINE.md"
    census = {}
    for p, text in cache.items():
        if p in (manifest, out):
            continue
        # Same exemption as the check, or the frozen numbers would not match the live census.
        n = sum(count_outside_code(text, rf"\bREF-{raw}\b") for raw in alias)
        if n:
            census[p.relative_to(root).as_posix()] = n
    lines = [
        "# SB_CITATION_BASELINE.md — frozen census of retired REF-1 / REF-2 citations",
        "",
        "*Generated by `python tools/audits/canon_check.py --write-sb-baseline`. Read by the",
        "REF-CITE check.*",
        "",
        "**What this file is.** The support-book REF numbering was retired at UD-60(b) and its",
        "existing citations were ruled **left as written** — rewriting a session log to say",
        "something it did not say at the time is the larger violation. This freezes what those",
        "citations were at that moment, so REF-CITE can **FAIL a newly added one** while passing",
        "every historical one. Without it the check can only warn.",
        "",
        "**Do not regenerate to clear a red gate.** A FAIL here means a retired number was cited",
        "in new text; the fix is to write `REF-01` / `REF-20`, not to re-freeze the baseline.",
        "Re-freezing is a Principal decision and takes a CD row.",
        "",
        "**Counts are occurrences, not lines**, and include `.py` / `.json` as well as markdown.",
        "`canon/refs/MANIFEST.md` and this file are excluded — they define the aliases.",
        "",
        "**Citations inside `backticks` are NOT counted** — SOURCE_POLICY §7.16 applied by",
        "analogy (session-2 ruling 1): a gate that forbids naming the retired number makes the",
        "retirement unwriteable. Bare prose is still counted, and fenced blocks are still counted.",
        "",
        "| File | Count |",
        "|---|---|",
    ]
    for k in sorted(census):
        lines.append(f"| `{k}` | {census[k]} |")
    lines += ["", f"**Total: {sum(census.values())} citation(s) across {len(census)} file(s).**", ""]
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out.relative_to(root)} — {sum(census.values())} citation(s), "
          f"{len(census)} file(s)")
    print("WARNING: a baseline re-freeze launders any unapproved addition made since the last "
          "freeze. This is a Principal decision (UD-60(b)); it is not a way to clear a red gate.")
    return 0


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
        b.stage("REF-CITE")
        check_ref_citations(root, cache)
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
        refs = root / "canon" / "refs"
        refs.mkdir()
        (refs / "MANIFEST.md").write_text(
            "| ID | Title | Version | Lock | Consumers | Status | Path |\n"
            "|---|---|---|---|---|---|---|\n"
            "| REF-01 | seed policy | v1.0 | LOCKED | seed | ACTIVE | canon/seed.md |\n"
            "| REF-19 | seed map | v1.0 | LOCKED | seed | ACTIVE | canon/seed.md |\n"
            "\n### HISTORICAL aliases\n\n| Retired ID | Resolves to | Note |\n|---|---|---|\n"
            "| REF-1 | REF-01 | seed alias |\n", encoding="utf-8")

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

        # ---- REF-CITE seeds (CD-055 / CD-064(f): synthetic, never the live pool) ----
        (root / "phantom.md").unlink()
        (root / "cites_ok.md").write_text("built against REF-01 and REF-19.\n", encoding="utf-8")
        note(run(root, DEFAULT_BUDGET, quiet=True) == 0,
             "control · REF citations that resolve to manifest rows -> CLEAN", "CLEAN", "CLEAN")

        # Retired SB number: resolves, warns, and must NOT fail.
        (root / "cites_sb.md").write_text("older text citing REF-1 twice: REF-1.\n",
                                          encoding="utf-8")
        rc = run(root, DEFAULT_BUDGET, quiet=True)
        note(rc == 0, "seed · retired SB citation (REF-1) RESOLVES via alias -> CLEAN, not FAIL",
             {0: "CLEAN", 1: "FAIL", 2: "REFUSE"}.get(rc, rc), "CLEAN")
        note(any("retired support-book citation" in w for w in warns),
             "seed · retired SB citation is reported in the WARN census (never silent)",
             "censused", "censused")
        (root / "cites_sb.md").unlink()

        # The phantom. Token BUILT, not written: a literal here would be a real phantom
        # citation inside the gate's own source, and REF-CITE would rightly FAIL the repo
        # on it — the exact trap CD-080(e) recorded for CD-999.
        phantom_ref = "REF-" + "99"
        (root / "phantom_ref.md").write_text(f"cites {phantom_ref}, which has no row.\n",
                                             encoding="utf-8")
        note(run(root, DEFAULT_BUDGET, quiet=True) == 1,
             "seed · phantom REF citation with no manifest row -> FAIL", "FAIL", "FAIL")
        (root / "phantom_ref.md").unlink()

        # ---- SB baseline census seeds: the check must bite in BOTH directions ----
        sb = root / "canon" / "refs" / "SB_CITATION_BASELINE.md"
        (root / "old_history.md").write_text(
            "a 2026-05 log line citing REF-1 and REF-1 again.\n", encoding="utf-8")
        sb.write_text("| File | Count |\n|---|---|\n| `old_history.md` | 2 |\n",
                      encoding="utf-8")
        note(run(root, DEFAULT_BUDGET, quiet=True) == 0,
             "control · SB citations AT their frozen baseline -> CLEAN (history passes)",
             "CLEAN", "CLEAN")

        # Direction 1: a citation ADDED to an already-listed file.
        (root / "old_history.md").write_text(
            "a 2026-05 log line citing REF-1 and REF-1 again. plus a new REF-1.\n",
            encoding="utf-8")
        rc = run(root, DEFAULT_BUDGET, quiet=True)
        note(rc == 1, "seed · SB citation ADDED above baseline (2 -> 3) -> FAIL",
             {0: "CLEAN", 1: "FAIL", 2: "REFUSE"}.get(rc, rc), "FAIL")
        note(any("was ADDED" in f for f in fails),
             "seed · the FAIL names the addition, not just a count", "named", "named")
        (root / "old_history.md").write_text(
            "a 2026-05 log line citing REF-1 and REF-1 again.\n", encoding="utf-8")

        # Direction 2: a NEW file citing retired numbering at all.
        (root / "written_today.md").write_text("new text citing REF-1.\n", encoding="utf-8")
        rc = run(root, DEFAULT_BUDGET, quiet=True)
        note(rc == 1, "seed · unlisted file citing retired REF-1 -> FAIL",
             {0: "CLEAN", 1: "FAIL", 2: "REFUSE"}.get(rc, rc), "FAIL")
        (root / "written_today.md").unlink()

        # ---- §7.16-by-analogy backtick exemption: seeded in BOTH directions ----
        # The retirement must be writeable: a row saying the retired number is retired has to
        # be able to name it. A bare one newly added still fails.
        #
        # **Every SB token below is BUILT, never written as a literal.** The seeds already on
        # this file were written as literals and are therefore part of the gate's own frozen
        # baseline; writing nine more inflated the live census past that baseline and the gate
        # FAILed itself on the first run of this edit. That is CD-080(e)'s trap — a gate's own
        # source is not exempt from citation discipline — reached from the REF side rather than
        # the CD side. Constructed tokens do not enter the census at all.
        sb1 = "REF-" + "1"
        base2 = f"a 2026-05 log line citing {sb1} and {sb1} again."
        (root / "old_history.md").write_text(base2 + "\n", encoding="utf-8")
        (root / "retirement_note.md").write_text(
            f"the support-book number `{sb1}` is retired and resolves to REF-01.\n",
            encoding="utf-8")
        rc = run(root, DEFAULT_BUDGET, quiet=True)
        note(rc == 0,
             "seed · UNLISTED file naming the retired number in `backticks` -> CLEAN "
             "(the retirement stays writeable)",
             {0: "CLEAN", 1: "FAIL", 2: "REFUSE"}.get(rc, rc), "CLEAN")

        # The other direction, on the same unlisted file: strip the backticks and it fails.
        (root / "retirement_note.md").write_text(
            f"the support-book number {sb1} is retired and resolves to REF-01.\n",
            encoding="utf-8")
        rc = run(root, DEFAULT_BUDGET, quiet=True)
        note(rc == 1,
             "seed · the same citation BARE in prose -> FAIL (exemption is backticks only)",
             {0: "CLEAN", 1: "FAIL", 2: "REFUSE"}.get(rc, rc), "FAIL")
        (root / "retirement_note.md").unlink()

        # A listed file: backticked additions do not move its count, bare ones do.
        (root / "old_history.md").write_text(
            f"{base2} and a quoted `{sb1}`.\n", encoding="utf-8")
        rc = run(root, DEFAULT_BUDGET, quiet=True)
        note(rc == 0,
             "seed · backticked citation ADDED to a listed file -> CLEAN (count unmoved at 2)",
             {0: "CLEAN", 1: "FAIL", 2: "REFUSE"}.get(rc, rc), "CLEAN")
        (root / "old_history.md").write_text(
            f"{base2} and a bare {sb1}.\n", encoding="utf-8")
        rc = run(root, DEFAULT_BUDGET, quiet=True)
        note(rc == 1,
             "control · bare citation ADDED to a listed file (2 -> 3) still -> FAIL",
             {0: "CLEAN", 1: "FAIL", 2: "REFUSE"}.get(rc, rc), "FAIL")

        # The exemption must NOT reach phantom resolution: backticks do not conjure a row.
        (root / "old_history.md").write_text(base2 + "\n", encoding="utf-8")
        (root / "backticked_phantom.md").write_text(
            f"cites `{phantom_ref}`, which has no row.\n", encoding="utf-8")
        rc = run(root, DEFAULT_BUDGET, quiet=True)
        note(rc == 1,
             "seed · a BACKTICKED phantom REF still -> FAIL (exemption is census-only)",
             {0: "CLEAN", 1: "FAIL", 2: "REFUSE"}.get(rc, rc), "FAIL")
        (root / "backticked_phantom.md").unlink()

        # A count that FALLS is a cleanup, not a violation.
        (root / "old_history.md").write_text("one citation of REF-1 left.\n", encoding="utf-8")
        note(run(root, DEFAULT_BUDGET, quiet=True) == 0,
             "control · SB count BELOW baseline (cleanup) -> CLEAN, never a FAIL",
             "CLEAN", "CLEAN")
        (root / "old_history.md").unlink()
        sb.unlink()

        # A resolver with no register must FAIL, never pass quietly (§7.17, CD-072).
        (refs / "MANIFEST.md").rename(refs / "MANIFEST.md.aside")
        rc = run(root, DEFAULT_BUDGET, quiet=True)
        note(rc == 1, "seed · missing canon/refs/MANIFEST.md -> FAIL, never a silent skip",
             {0: "CLEAN", 1: "FAIL", 2: "REFUSE"}.get(rc, rc), "FAIL")
        (refs / "MANIFEST.md.aside").rename(refs / "MANIFEST.md")

        # Restore the CD phantom the later seeds rely on.
        (root / "phantom.md").write_text(
            f"cites {phantom}, which does not exist.\n", encoding="utf-8")

        # ---- PLACEHOLDER backtick exemption (AGENTS.md §5.1, CD-089): both directions ----
        # Same rule at its third site. The marker is BUILT, never written as a literal — a
        # literal here would be a real unslotted marker inside the gate's own source. The
        # tools/audits/*.py carve-out would swallow it in the live repo, but this fixture is
        # written to a temp tree where that carve-out does not apply, so the seed would be
        # measuring the carve-out instead of the exemption.
        marker = "NOT YET " + "SLOTTED"
        (root / "retires_it.md").write_text(
            f"the `{marker}` marker is removed; this folder is DEFERRED by design.\n",
            encoding="utf-8")
        run(root, DEFAULT_BUDGET, quiet=True)
        note(not any("retires_it.md" in w for w in warns),
             "seed · a file NAMING the marker in `backticks` -> no warn "
             "(the retirement stays writeable)",
             "no warn", "no warn")

        (root / "retires_it.md").write_text(
            f"this folder is {marker} and nobody has said why.\n", encoding="utf-8")
        run(root, DEFAULT_BUDGET, quiet=True)
        note(any("retires_it.md" in w for w in warns),
             "control · the same marker BARE in prose -> still WARN "
             "(exemption is backticks only)",
             "warned", "warned")
        (root / "retires_it.md").unlink()

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
    ap.add_argument("--write-sb-baseline", action="store_true",
                    help="re-freeze canon/refs/SB_CITATION_BASELINE.md (Principal decision only)")
    args = ap.parse_args()
    if args.selftest:
        sys.exit(selftest())
    if args.write_sb_baseline:
        sys.exit(write_sb_baseline(ROOT, args.budget))
    sys.exit(run(ROOT, args.budget))


if __name__ == "__main__":
    main()
