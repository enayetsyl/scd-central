#!/usr/bin/env python3
"""int_id_check.py — CD-088(d)(i): the `int()`-on-a-captured-ID source lint.

Run from repo root:
    python tools/audits/int_id_check.py

THE RULING THIS EXECUTES, VERBATIM
----------------------------------
CD-088(d)(i), quoted from `canon/DECISIONS.md` at source:

    **(i) source lint** — forbid `int()` on any captured id group in `tools/audits/*.py` and
    `workstreams/*/audits/*.py`, requiring comparison against the raw captured string;

Its sibling **(ii)** shipped as `tools/audits/ledger_check.py` in session 3. This is the half that
was owed. The two are one pattern seen from two sides: (ii) catches an ID whose distinguishing
form **never existed**; (i) catches an ID whose distinguishing form is **thrown away at the point
of comparison**.

WHY `int()` IS THE NAMED SINK
----------------------------
TOOLS-CR-001, the incident that started the census: two reference IDs differing **only in their
zero-padding** were collapsed into one because the check compared `int(captured)` instead of the
captured string. *(The two real tokens are written out in `tools/CORRECTIONS.md` at TOOLS-CR-001;
they are deliberately not repeated here — one of them is a retired support-book citation form and
UD-60(b) forbids minting new ones, which `canon_check.py`'s REF-CITE gate enforces and which it
caught in this file's first draft.)*

`canon_check.py:239` still carries the confession in its own docstring — *"`int("01") == int("1")`"*. Zero-padding is
not decoration on an ID; it is part of the name. So is a scheme prefix (CD-088(b)), and so is a
hyphenated segment (CD-125 / UP-003, the fifth instance). **`int()` is the single call that
destroys all three at once**, which is why the ruling names it rather than naming a principle.

WHAT IS CHECKED, AND WHAT IS ONLY REPORTED
------------------------------------------
  INT-ON-ID-CAPTURE       FAIL.     `int()` is applied to a value flowing from a regex capture
                                    whose pattern is **identifier-shaped** — the pattern carries a
                                    literal scheme prefix (`QP-`, `CD-`, `TOP-BAN-`, a `U` behind
                                    a literal hyphen, …). This is the ruling's own scope.
  INT-ON-CAPTURE-UNTYPED  REPORT.   `int()` on a capture whose pattern is **not** identifier-shaped
                                    (a page count, a folio, a mark) or could not be resolved
                                    statically. Printed, never silently dropped, never counted
                                    toward the verdict.

The second tier is not padding. `SOURCE_POLICY` §7.17 — *a gate reports or refuses, it never
omits* — and CD-041's standing rule that an instrument shown only against the errors it was built
for has only been shown to measure those. A lint that quietly discarded every capture it could not
classify would look identical to a lint that found nothing, and the repo would have no way to tell
the two apart. The untyped list **is the measurement of this lint's own reach**.

WHY THE CLASSIFIER, AND NOT "EVERY CAPTURE IS AN ID"
---------------------------------------------------
The flat form was considered and rejected. `math_arith_check.py` calls `int()` on captured Bangla
numerals roughly thirty times **because the numerals are quantities** — that is the gate's entire
job. Failing on those would make the ruling unimplementable and would force the six-gate rewrite
CD-067 exists to prevent. So the lint asks the only question CD-088 actually asks: *does this
capture come off an identifier?* — and where it cannot tell, it says so out loud instead of
guessing in either direction.

THE DECLARATION, AND WHY IT MIRRORS CD-124
------------------------------------------
A genuine numeric segment inside an identifier (a class level in `QP-BAN-C5-U21`) has an escape:

    class_level = int(m.group(2))   # int-id-ok: C([1-5]) is a class LEVEL, ordered and compared

Same line, or the line immediately above; the reason after the colon is mandatory and a bare
`# int-id-ok:` is itself a FAIL. This is deliberately CD-124's shape: there the repair was every
ledger **declaring** its prefix rather than a gate inferring one, because the information that
tells two IDs apart does not live in the code. Same here. **The declaration is the repair; the
lint is the alarm.**

  ⚠ **No `int-id-ok:` waiver exists anywhere in the repo, and none was added by the session that
  built this file.** The waiver form is built, seeded both directions, and left unused. Adding
  waivers means editing audit scripts, which this session is instructed not to do, and which would
  in any case be ruling on each site — the Principal's call, not the agent's.

LIMITS, STATED
--------------
* Taint is tracked with a **flat per-file name map**, not per-scope. Two functions that both bind a
  name `m` to different patterns are conflated. Over-approximate: it can mis-attribute a pattern,
  it cannot lose a sink.
* A pattern built by concatenation or an f-string is **unresolved**, not assumed innocent — it
  lands in INT-ON-CAPTURE-UNTYPED with `«pattern not statically resolvable»`.
* `float()`, `Decimal()` and `str.zfill()` destroy the same information and are **not** checked.
  CD-088(d)(i) names `int()`. Widening the sink is a ruling, not a patch.

Exit 0 = CLEAN, 1 = FAIL. Paste output verbatim per AGENTS.md §5.
"""
import ast
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# The two globs are the ruling's, quoted: `tools/audits/*.py` and `workstreams/*/audits/*.py`.
SCOPE_GLOBS = ("tools/audits/*.py", "workstreams/*/audits/*.py")

# This file lints itself. Its own fixtures contain deliberate violations as *string literals*,
# which are never parsed as code here, so no exemption is needed or taken.

CAPTURE_METHODS = {"group", "groups", "groupdict"}
MATCH_MAKERS = {"search", "match", "fullmatch", "finditer"}
LIST_MAKERS = {"findall"}

WAIVER = re.compile(r"#\s*int-id-ok:\s*(?P<reason>.*)$")

UNRESOLVED = "«pattern not statically resolvable»"


# ---------------------------------------------------------------------------------
# Is this regex matching an IDENTIFIER?
# ---------------------------------------------------------------------------------

def strip_char_classes(pattern):
    """Remove `[...]` classes and backslash escapes from a regex source.

    Without this, `([A-Z]+)` reads as a literal `Z-`-ish scheme prefix and every pattern in the
    repo looks like an identifier. The distinction being drawn is between a *literal* prefix the
    pattern insists on (`QP-`) and a *class* the pattern merely permits — CD-070's
    substring-vs-token, in miniature, and the same mistake made while building this file: the
    first `grep` for `int(` matched every `print(` in the tree.
    """
    out, i, n = [], 0, len(pattern)
    while i < n:
        c = pattern[i]
        if c == "\\":
            i += 2
            continue
        if c == "[":
            j = i + 1
            if j < n and pattern[j] == "^":
                j += 1
            if j < n and pattern[j] == "]":
                j += 1
            while j < n and pattern[j] != "]":
                if pattern[j] == "\\":
                    j += 1
                j += 1
            i = j + 1
            continue
        out.append(c)
        i += 1
    return "".join(out)


# An uppercase run followed by a literal hyphen, present as LITERAL text in the pattern:
# `QP-`, `CD-`, `TOP-BAN-`, `MATH-`. This is what an ID scheme looks like in this repo,
# and it is what CD-088(b) calls the scheme prefix.
SCHEME_PREFIX = re.compile(r"[A-Z][A-Z0-9]{0,7}-")


def is_id_pattern(pattern):
    """True when the regex source insists on a literal ID scheme prefix."""
    if pattern is None:
        return False
    return bool(SCHEME_PREFIX.search(strip_char_classes(pattern)))


# ---------------------------------------------------------------------------------
# Static resolution of pattern literals
# ---------------------------------------------------------------------------------

def literal_pattern(node, compiled):
    """The regex source behind `node`, or None if it is not a plain literal."""
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.Name):
        return compiled.get(node.id)
    if isinstance(node, ast.Attribute):
        return compiled.get(node.attr)
    return None


def collect_compiled(tree):
    """`NAME = re.compile("literal")` -> {NAME: "literal"}, module-wide."""
    out = {}
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        tgt = node.targets[0]
        if not isinstance(tgt, ast.Name):
            continue
        val = node.value
        if (isinstance(val, ast.Call) and isinstance(val.func, ast.Attribute)
                and val.func.attr == "compile" and val.args):
            arg = val.args[0]
            if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                out[tgt.id] = arg.value
            else:
                out[tgt.id] = None  # present, but unresolved — not innocent
    return out


def call_pattern(call, compiled):
    """For `re.search(p, s)` / `PAT.finditer(s)` return (kind, pattern_or_None), else None.

    kind is 'match' for a match object and 'list' for findall's strings.
    """
    if not isinstance(call, ast.Call) or not isinstance(call.func, ast.Attribute):
        return None
    attr = call.func.attr
    recv = call.func.value
    if attr in MATCH_MAKERS or attr in LIST_MAKERS:
        kind = "list" if attr in LIST_MAKERS else "match"
        if isinstance(recv, ast.Name) and recv.id == "re":
            return kind, (literal_pattern(call.args[0], compiled) if call.args else None)
        # PAT.search(...) — a compiled pattern object
        return kind, literal_pattern(recv, compiled)
    return None


# ---------------------------------------------------------------------------------
# Taint
# ---------------------------------------------------------------------------------

class Analyser:
    """Flat per-file taint map. See LIMITS in the module docstring."""

    def __init__(self, tree, src_lines, relpath):
        self.compiled = collect_compiled(tree)
        self.lines = src_lines
        self.rel = relpath
        self.match_vars = {}    # name -> pattern (match objects)
        self.tainted = {}       # name -> pattern (captured strings)
        self.findings = []      # (gate, line, detail)
        self.visit(tree)

    # -- binding ------------------------------------------------------------------

    def _bind_targets(self, target, value):
        """Record what a name now holds. Tuple targets are unpacked elementwise."""
        if isinstance(target, ast.Tuple) and isinstance(value, ast.Tuple):
            for t, v in zip(target.elts, value.elts):
                self._bind_targets(t, v)
            return
        cp = call_pattern(value, self.compiled) if isinstance(value, ast.Call) else None
        if isinstance(target, ast.Name):
            if cp and cp[0] == "match":
                self.match_vars[target.id] = cp[1]
                return
            pat = self.taint_of(value)
            if pat is not False:
                self.tainted[target.id] = pat
        elif isinstance(target, (ast.Tuple, ast.List)):
            pat = self.taint_of(value)
            if pat is not False:
                for t in target.elts:
                    if isinstance(t, ast.Name):
                        self.tainted[t.id] = pat

    def _bind_iter(self, target, iterable):
        """`for x in <capture-producing iterable>` and comprehension generators."""
        cp = call_pattern(iterable, self.compiled) if isinstance(iterable, ast.Call) else None
        pat, is_match = None, False
        if cp:
            pat = cp[1]
            is_match = cp[0] == "match"
        elif self.taint_of(iterable) is not False:
            pat = self.taint_of(iterable)
        else:
            return
        names = [target] if isinstance(target, ast.Name) else list(
            getattr(target, "elts", []))
        for nm in names:
            if isinstance(nm, ast.Name):
                if is_match:
                    self.match_vars[nm.id] = pat
                else:
                    self.tainted[nm.id] = pat

    # -- taint test ---------------------------------------------------------------

    def taint_of(self, node):
        """Pattern string if any subexpression of `node` is a capture, else False.

        Returns None when tainted but the pattern is unresolved — hence the `is not False`
        comparisons above. A bare truthiness test would read an unresolved capture as clean, which
        is the exact shape of error this whole lint exists to catch.
        """
        found = False
        pat = None
        for sub in ast.walk(node):
            if (isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute)
                    and sub.func.attr in CAPTURE_METHODS):
                recv = sub.func.value
                found = True
                if isinstance(recv, ast.Name) and recv.id in self.match_vars:
                    pat = pat or self.match_vars[recv.id]
                continue
            if isinstance(sub, ast.Name):
                if sub.id in self.tainted:
                    found = True
                    pat = pat or self.tainted[sub.id]
                elif sub.id in self.match_vars:
                    found = True
                    pat = pat or self.match_vars[sub.id]
            if isinstance(sub, ast.Call):
                cp = call_pattern(sub, self.compiled)
                if cp and cp[0] == "list":
                    found = True
                    pat = pat or cp[1]
        return pat if found else False

    # -- the sink -----------------------------------------------------------------

    def waiver_at(self, lineno):
        """A waiver on this line or the one above -> its reason (possibly empty)."""
        for ln in (lineno, lineno - 1):
            if 1 <= ln <= len(self.lines):
                m = WAIVER.search(self.lines[ln - 1])
                if m:
                    return m.group("reason").strip()
        return None

    def check_int_call(self, call):
        if not (isinstance(call.func, ast.Name) and call.func.id == "int" and call.args):
            return
        pat = self.taint_of(call.args[0])
        if pat is False:
            return                                   # not from a capture at all
        shown = pat if pat is not None else UNRESOLVED
        reason = self.waiver_at(call.lineno)
        if is_id_pattern(pat):
            if reason is None:
                self.findings.append((
                    "INT-ON-ID-CAPTURE", call.lineno,
                    f"int() on a group captured by an ID pattern  r\"{shown}\"  — compare the "
                    f"RAW captured string (CD-088(d)(i)); or declare `# int-id-ok: <reason>`"))
            elif not reason:
                self.findings.append((
                    "INT-ON-ID-CAPTURE", call.lineno,
                    "`# int-id-ok:` carries no reason — a bare waiver records nothing "
                    "(CD-124: the declaration IS the repair)"))
        else:
            self.findings.append((
                "INT-ON-CAPTURE-UNTYPED", call.lineno,
                f"int() on a capture from a non-ID pattern  r\"{shown}\"  — reported, not judged"))

    # -- walk ---------------------------------------------------------------------

    def visit(self, node):
        """Source-order recursive descent. `ast.walk` is breadth-first, which would read a
        binding after its use and silently under-report."""
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            val = node.value
            if val is not None:
                self.visit(val)
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                for t in targets:
                    self._bind_targets(t, val)
            return
        if isinstance(node, ast.NamedExpr):           # walrus: if (m := PAT.search(s)):
            self.visit(node.value)
            self._bind_targets(node.target, node.value)
            return
        if isinstance(node, (ast.For, ast.AsyncFor)):
            self.visit(node.iter)
            self._bind_iter(node.target, node.iter)
            for child in node.body + node.orelse:
                self.visit(child)
            return
        if isinstance(node, ast.comprehension):
            self.visit(node.iter)
            self._bind_iter(node.target, node.iter)
            for child in node.ifs:
                self.visit(child)
            return
        if isinstance(node, (ast.ListComp, ast.SetComp, ast.GeneratorExp, ast.DictComp)):
            for gen in node.generators:
                self.visit(gen)
            for child in ast.iter_child_nodes(node):
                if not isinstance(child, ast.comprehension):
                    self.visit(child)
            return
        if isinstance(node, ast.Call):
            for child in ast.iter_child_nodes(node):
                self.visit(child)
            self.check_int_call(node)
            return
        for child in ast.iter_child_nodes(node):
            self.visit(child)


# ---------------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------------

def in_scope(root):
    out = []
    for g in SCOPE_GLOBS:
        out.extend(sorted(root.glob(g)))
    return sorted(set(out))


def analyse_text(src, relpath):
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        return [("PARSE", e.lineno or 0, f"could not parse: {e.msg}")]
    return Analyser(tree, src.splitlines(), relpath).findings


def run(paths, quiet=False):
    fails, reports = [], []
    for p in paths:
        rel = p.relative_to(ROOT).as_posix() if p.is_absolute() and ROOT in p.parents else p.name
        for gate, line, detail in analyse_text(p.read_text(encoding="utf-8"), rel):
            row = (gate, f"{rel}:{line}", detail)
            (reports if gate == "INT-ON-CAPTURE-UNTYPED" else fails).append(row)
    if not quiet:
        for gate, where, detail in fails:
            print(f"  FAIL   {gate:<24} {where}\n         {detail}")
        if reports:
            print(f"  REPORT {len(reports)} int()-on-capture site(s) from non-ID or unresolved "
                  f"patterns — printed, not judged (SOURCE_POLICY §7.17)")
            for _, where, detail in reports:
                print(f"         - {where}  {detail.split('  — ')[0].split('int() on a capture ')[-1]}")
    return fails, reports


# ---------------------------------------------------------------------------------
# SELFTEST — synthetic fixtures only (CD-055, CD-064(f); seeds synthetic, CD-121(e))
# ---------------------------------------------------------------------------------

def _t(src):
    return analyse_text(src, "fixture.py")


def selftest():
    print("SELFTEST — the instrument is proven before any repo verdict (CD-025). Seeds are "
          "SYNTHETIC and drawn from no live file (CD-121(e): seeds synthetic, controls may be live).")
    ok = True
    results = []

    def case(gate, label, src, want_hit, needle=""):
        f = _t(src)
        hit = any(g == gate and (needle in d or needle in w) for g, w, d in
                  [(g, f"fixture.py:{l}", d) for g, l, d in f])
        good = hit if want_hit else not hit
        results.append((gate, label, good, "" if good else f"got: {f}"))

    # --- 1. THE RULING'S OWN CASE: int() on a group off an ID pattern. Must FAIL.
    case("INT-ON-ID-CAPTURE", "int() on a group captured by an ID pattern (the CD-088(d)(i) case)",
         'import re\n'
         'm = re.match(r"^QP-([A-Z]+)-C([1-5])-U(\\d+)", qid)\n'
         'level = int(m.group(2))\n', True)

    # --- 2. TOOLS-CR-001's shape — zero-padding collapsed by int(). The scheme letters here are
    # --- SYNTHETIC (`ZZR-`), not the incident's real prefix: seeds are synthetic (CD-121(e)), and
    # --- writing the real pair would mint a retired support-book citation form (UD-60(b)).
    case("INT-ON-ID-CAPTURE", "TOOLS-CR-001's shape — `ZZR-01` and `ZZR-1` collapsed by int()",
         'import re\n'
         'REF = re.compile(r"ZZR-(\\d+)")\n'
         'm = REF.search(line)\n'
         'if int(m.group(1)) == wanted:\n    pass\n', True)

    # --- 3. taint survives a helper call and a string method — the destruction is one hop away.
    case("INT-ON-ID-CAPTURE", "taint survives `dg(...)` and `.translate(...)` between capture "
                              "and int()",
         'import re\n'
         'CD = re.compile(r"\\bCD-(\\d{3})\\b")\n'
         'm = CD.search(t)\n'
         'n = int(dg(m.group(1)).translate(TO_ASCII))\n', True)

    # --- 4. taint survives an intermediate BINDING, which is how the live instance is written.
    case("INT-ON-ID-CAPTURE", "taint survives a named intermediate (`unit = m.group(3)` then "
                              "`int(unit)`)",
         'import re\n'
         'm = re.match(r"^QP-([A-Z]+)-C([1-5])-U(\\d+)", qid)\n'
         'subject, level, unit = m.group(1), m.group(2), m.group(3)\n'
         'bn = str(int(unit))\n', True)

    # --- 5. findall over an ID pattern, in a comprehension.
    case("INT-ON-ID-CAPTURE", "int() inside a comprehension over `re.findall` on an ID pattern",
         'import re\n'
         'nums = [int(x) for x in re.findall(r"TOP-BAN-C5-(\\d+)", text)]\n', True)

    # --- 6. the walrus form, because half the repo's matches are written that way.
    case("INT-ON-ID-CAPTURE", "the walrus form `if (m := PAT.search(s)):`",
         'import re\n'
         'PAT = re.compile(r"UP-(\\d+)")\n'
         'if (m := PAT.search(s)):\n    k = int(m.group(1))\n', True)

    # --- NEGATIVE 7. A QUANTITY off a non-ID pattern must NOT fail. This is the case that keeps
    # --- the ruling implementable: `math_arith_check.py` does this ~30x and it is its whole job.
    case("INT-ON-ID-CAPTURE", "control · a page count off a non-ID pattern does NOT fail",
         'import re\n'
         'm = re.search(r"printed page (\\d+)", line)\n'
         'p = int(m.group(1))\n', False)
    #     ...and is REPORTED rather than swallowed.
    case("INT-ON-CAPTURE-UNTYPED", "control · that same quantity is REPORTED, not silently "
                                   "dropped (§7.17: reports or refuses, never omits)",
         'import re\n'
         'm = re.search(r"printed page (\\d+)", line)\n'
         'p = int(m.group(1))\n', True)

    # --- NEGATIVE 8. `[A-Z]` is a CLASS, not a literal scheme prefix. Without strip_char_classes
    # --- every pattern in the repo reads as an identifier — CD-070's substring-vs-token.
    case("INT-ON-ID-CAPTURE", "control · a bare `[A-Z]+` class is not a literal scheme prefix",
         'import re\n'
         'm = re.search(r"([A-Z]+) (\\d+)", line)\n'
         'p = int(m.group(2))\n', False)

    # --- NEGATIVE 9. int() on something that never touched a capture is invisible to this lint.
    case("INT-ON-ID-CAPTURE", "control · int() on a plain split cell is not a capture at all",
         'cells = line.split("|")\n'
         'a = int(cells[0])\n', False)
    case("INT-ON-CAPTURE-UNTYPED", "control · and it is not reported either — the lint's subject "
                                   "is captures, not arithmetic",
         'cells = line.split("|")\n'
         'a = int(cells[0])\n', False)

    # --- 10. THE WAIVER, both directions. Declared with a reason -> silent.
    case("INT-ON-ID-CAPTURE", "a declared `# int-id-ok: <reason>` waiver silences the FAIL",
         'import re\n'
         'm = re.match(r"^QP-([A-Z]+)-C([1-5])", qid)\n'
         'level = int(m.group(2))  # int-id-ok: C([1-5]) is a class LEVEL, ordered and compared\n',
         False)
    # --- ...and a BARE waiver does not. A declaration that records nothing is not a declaration.
    case("INT-ON-ID-CAPTURE", "a bare `# int-id-ok:` with no reason still FAILs",
         'import re\n'
         'm = re.match(r"^QP-([A-Z]+)-C([1-5])", qid)\n'
         'level = int(m.group(2))  # int-id-ok:\n', True, "carries no reason")
    # --- ...and the waiver may sit on the line ABOVE, for long call sites.
    case("INT-ON-ID-CAPTURE", "the waiver may sit on the line above the call",
         'import re\n'
         'm = re.match(r"^QP-([A-Z]+)-C([1-5])", qid)\n'
         '# int-id-ok: the class level is a number here\n'
         'level = int(m.group(2))\n', False)

    # --- 11. AN UNRESOLVED PATTERN IS NOT AN INNOCENT ONE. An f-string pattern still lands in the
    # --- report with `«pattern not statically resolvable»`, so the lint's blind spot is visible.
    case("INT-ON-CAPTURE-UNTYPED", "an f-string pattern is reported as UNRESOLVED, not assumed "
                                   "clean",
         'import re\n'
         'm = re.search(rf"({UNIT}) (\\d+)", line)\n'
         'p = int(m.group(2))\n', True, "not statically resolvable")

    # --- 12. BASELINE. A gate that fires on everything is as useless as one that fires on nothing.
    f = _t('import re\n'
           'PAT = re.compile(r"CD-(\\d{3})")\n'
           'm = PAT.search(t)\n'
           'if m and m.group(1) == wanted:\n    pass\n'
           'total = len(rows) + 1\n')
    results.append(("baseline", "correct code — raw string compared, no int() anywhere",
                    not f, "" if not f else f"fired: {f}"))

    for gate, label, passed, note in results:
        print(f"  {'PASS' if passed else 'FAIL':<4}  {gate:<24} {label}"
              + (f"\n        {note}" if note and not passed else ""))
        ok = ok and passed
    seeded = sum(1 for r in results if r[0] != "baseline")
    print(f"SELFTEST RESULT: {'PASS' if ok else 'FAIL'} "
          f"({len(results)} cases: {seeded} seeded/control, 1 baseline)")
    return ok


def main():
    if not selftest():
        print("\nRESULT: FAIL (selftest red — no repo verdict is believable, nothing was judged)")
        sys.exit(1)
    paths = in_scope(ROOT)
    print(f"\nSCOPE (CD-088(d)(i), verbatim): {' · '.join(SCOPE_GLOBS)}")
    print(f"FILES SCANNED: {len(paths)}")
    for p in paths:
        print(f"  {p.relative_to(ROOT).as_posix()}")
    print()
    fails, reports = run(paths)
    print()
    print(f"RESULT: {'FAIL' if fails else 'CLEAN'} "
          f"({len(fails)} INT-ON-ID-CAPTURE failure(s), "
          f"{len(reports)} untyped site(s) reported and not judged)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
