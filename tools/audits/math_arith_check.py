#!/usr/bin/env python3
"""math_arith_check.py — the arithmetic of a গণিত extraction checked against itself.

SOURCE_POLICY §7.7 records that `Class 5 Math.pdf` has no text layer, so
`source_textcheck.py` REFUSEs and there is no cross-channel diff. That is true of the
*file*. It is not true of the *content*: **mathematics carries its own redundancy.** In a
worked multiplication the partial products must sum to the total, and each partial must equal
multiplicand × its multiplier digit × place value. **A mis-read digit does not balance.**

That is exactly the failure the full-resolution ruling exists to catch (CD-054): a numeral read
wrong becomes a wrong answer key, and on a single-channel book nothing downstream sees it. So
this check is the one machine second channel the book has, and by CD-020 a script that was run
once is not evidence — it has to be a gate with a seeded negative test. This is that gate.

**THE THREE LIMITS. They are the point, not a disclaimer** — a check whose reach is
overstated is worse than no check, because it buys depth reductions it has not earned:

  1. **Computed working only.** A block is checked only where the book prints the working. The
     check reaches partial products, totals and step tables; nothing else.
  2. **Words, names and instructions are outside scope.** The check has nothing to say about
     any prose, heading, label or instruction, and never will.
  3. **Problem-statement figures are unchecked where the book prints no working.** "প্রতিটি
     ৮৫৩৬ টাকা মূল্যের ৯৭২টি মোবাইল ফোন" is verified only because the book goes on to compute
     ৮৫৩৬ × ৯৭২. A figure the book states and never uses is invisible here.

Everything those limits exclude stays at **full manual depth** (SOURCE_POLICY §7.10).

**Blanks.** The book prints exercise cells empty (`☐`). Where the printed digits pin the hidden
ones **uniquely**, the block is covered: the solution is forced, and it matching every printed
cell is a real check on the transcription — often a stronger one than a fully-printed block,
because more constraints bear on fewer free digits. Where more than one assignment fits, the
block is reported **AMBIGUOUS** and is *not* covered. An agent may not treat ambiguity as a pass.

Verdicts and exit codes:
    0  CLEAN    every checkable block balances
    2  RED      a block does not balance, or its shape does not match its operands
    3  REFUSE   nothing checkable found — reported, never silently called clean

Usage:
    python tools/audits/math_arith_check.py canon/_wip/c5-math/C5_MATH_Source_01.md
    python tools/audits/math_arith_check.py --selftest

`tools/audits` is SMOKE-exempt (`tools_check.py` SMOKE_EXEMPT): a gate evidences itself, and
its verbatim run is the record.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path
# TOOLS-CR-013: a gate run DIRECTLY (not through run_all.py) inherits Windows' cp1252
# and dies on the first Bengali character the moment its output is piped or redirected.
# run_all.py sets PYTHONIOENCODING for its children, which masks this from the suite.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass


REPO = Path(__file__).resolve().parents[2]

BN = "০১২৩৪৫৬৭৮৯"
TO_ASCII = str.maketrans(BN, "0123456789")
TO_BN = str.maketrans("0123456789", BN)
BLANK = "☐"

# Kept in step with source_check.py's list of the same name: from the first of these headings on,
# the file is talking *about* the book rather than transcribing it, and commentary may quote a
# number in any form it likes.
COMMENTARY = ("## যেভাবে ছাপা আছে", "## এই ইউনিটে যা নেই", "## এই পাঠে যা নেই",
              "## এই অধ্যায়ে যা নেই",
              "## এই ইউনিটে যে নামগুলো আছে", "## এই পাঠে যে নামগুলো আছে",
              "## এই অধ্যায়ে যে নামগুলো আছে",
              "## MarkLogic স্লট মিলকরণ", "## প্রমাণ", "## সংশ্লিষ্ট নথি")

# A blank-solve is a brute force over the unknown digits of the two operands. Six is already
# 10^6 candidate assignments; beyond that the block is REFUSED rather than silently skipped,
# because a check that quietly gives up on the hardest blocks is worst exactly where it matters.
MAX_BLANKS = 6

RULE_RE = re.compile(r"^[─—–\-_=]{3,}$")


def body(text: str) -> str:
    cut = min((text.find(h) for h in COMMENTARY if h in text), default=-1)
    return text if cut < 0 else text[:cut]


def cells(line: str):
    """A transcribed numeric row -> list of cells, each a digit char or BLANK, or None."""
    s = line.strip()
    s = re.sub(r"^[×xX*]\s*", "", s)
    toks = s.split()
    if not toks:
        return None
    out = []
    for t in toks:
        for ch in t:
            if ch in BN:
                out.append(ch)
            elif ch == BLANK:
                out.append(BLANK)
            else:
                return None
    return out or None


def is_mul_line(line: str) -> bool:
    return bool(re.match(r"^\s*[×xX*]\s*[০-৯☐\s]+$", line))


class Block:
    def __init__(self, label, mcand, mplier, partials, total):
        self.label, self.mcand, self.mplier = label, mcand, mplier
        self.partials, self.total = partials, total


def parse_blocks(text: str):
    """Worked multiplications written as consecutive blockquote lines.

        > <multiplicand>
        > × <multiplier>
        > ─────
        > <partial> ...
        > ─────
        > <total>
    """
    lines = [l[1:].strip() if l.strip().startswith(">") else None
             for l in text.splitlines()]
    blocks, i, n = [], 0, len(lines)
    while i < n:
        if lines[i] is None:
            i += 1
            continue
        j = i
        run = []
        while j < n and lines[j] is not None:
            run.append(lines[j])
            j += 1
        blocks += parse_run(run, i + 1)
        i = j
    return blocks


def parse_run(run, lineno):
    out = []
    k = 0
    while k < len(run) - 3:
        mc = cells(run[k])
        if mc is None or not is_mul_line(run[k + 1]):
            k += 1
            continue
        mp = cells(run[k + 1])
        if mp is None or not RULE_RE.match(run[k + 2].strip()):
            k += 1
            continue
        p = k + 3
        partials = []
        while p < len(run) and not RULE_RE.match(run[p].strip()):
            c = cells(run[p])
            if c is None:
                break
            partials.append(c)
            p += 1
        if p >= len(run) or not RULE_RE.match(run[p].strip()) or p + 1 >= len(run):
            k += 1
            continue
        tot = cells(run[p + 1])
        if tot is None:
            k += 1
            continue
        out.append(Block(f"line {lineno + k}", mc, mp, partials, tot))
        k = p + 2
    return out


STEP_RE = re.compile(r"\|\s*([০-৯]+)\s*[×xX*]\s*([০-৯]+)\s*\|\s*[→>-]*\s*\|\s*([০-৯]+)\s*\|")
LADDER_RE = re.compile(r"\|\s*([০-৯]+)\s*\|\s*[×xX*]\s*([০-৯]+)\s*\|\s*=\s*\|\s*([০-৯]+)\s*\|")


def parse_steps(text: str):
    """Step tables in either printed layout.

    `| ৪৬১৪ × ৫ | → | ২৩০৭০ |`   — the ধাপ box on printed ১
    `| ৭৪ | × ২৯ | = | ২১৪৬ |`   — the ×১০০ ladder on printed ৫, which splits the operands
                                   across cells and was invisible to the first version.
    """
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        for rx in (STEP_RE, LADDER_RE):
            m = rx.search(line)
            if m:
                out.append((f"line {i}", *(int(g.translate(TO_ASCII)) for g in m.groups()), i))
                break
    return out


# --------------------------------------------------------------- equality chains
#
# The book states the same quantity several ways in a row — distributive expansion
# (`A × B = A × (b₁ + b₂ + …)`), the (X − ১) trick, and the ×১০০ rearrangement box. All three
# are the same claim in different clothes: **every fully-numeric way of writing the line must
# come to the same number.** One evaluator covers all of them, and will cover shapes not yet
# met, which is why it is written as an evaluator rather than three pattern-matchers.
#
# A segment containing ☐ is not evaluated — it is an exercise blank, not a claim.

# **Design note for the ÷ / > extension, ruled ahead of it (CD-063).**
#
# This chapter — গাণিতিক বাক্য — teaches by printing deliberately WRONG equations, each marked
# with a red ✗, before the right one marked ✓. The obvious handling is to exclude the ✗ lines.
# **Exclusion is the wrong answer**, and the reason is precise: it leaves a hole exactly where a
# mis-read hides. If the book prints `৪৮ ÷ ৩ = ৮` ✗ and a transcription mis-reads the divisor as
# ৬, the line becomes *true* — and an excluded line is checked by nothing, so the error passes.
#
# So when `÷` and `>` are added here, they carry INVERTED EXPECTATION with them:
#
#     ✗-marked line that balances      -> RED      ✗-marked line that does not balance -> CLEAN
#     ✓-marked line that balances      -> CLEAN    ✓-marked line that does not balance -> RED
#
# The mark is data; the check reads it. Seed all four directions. Nothing is implemented yet
# because the operators do not exist yet, and inversion without them would be untested
# machinery — until then the extraction's own warning block is the guard.

# **P-019 (CD-074).** The decimal point is inside the character class, and every numeral is
# read as an exact `Fraction`. It was outside for four chapters and that was correct while the
# book had no decimals; in অধ্যায় ৫ it meant **every line carrying a decimal produced no chain
# at all** — `parse_chains("০.৩ + ০.৪ = ০.৯")` returned zero chains, so a wrong sum was
# invisible rather than red. The fix is not "allow `.`": it is **read `.` as a place value**,
# because allowing the character while `_num`-style stripping continued would be worse than
# refusing — `০.৬` would become `৬`.
EXPR_OK = re.compile(r"^[০-৯\s.+\-−×xX*÷/()]+$")
DEC_RE = re.compile(r"^([০-৯]*)\.?([০-৯]*)$")


def _dec(s: str):
    """A Bengali numeral, with or without a decimal point, as an exact Fraction.

    Never float. `০.১ + ০.২` must be exactly `০.৩`, and on a float it is not — a tolerance is
    a thing this book never asked for and would quietly absorb the chapter's signature error,
    a point one place out. Handles the two truncated forms the book actually prints:
    `৪.` (ছাপা ৭৩, ⛔-৩) and `.৮৭` (ছাপা ৮৯, ⛔-১০).
    """
    m = DEC_RE.match(s)
    if not m:
        return None
    whole, frac = m.group(1), m.group(2)
    if not whole and not frac:
        return None
    w = int(whole.translate(TO_ASCII)) if whole else 0
    if not frac:
        return Fraction(w)
    return Fraction(w) + Fraction(int(frac.translate(TO_ASCII)), 10 ** len(frac))


def _tokens(s: str):
    s = s.replace("−", "-").replace("×", "*").replace("x", "*").replace("X", "*")
    s = s.replace("÷", "/")
    i, out = 0, []
    while i < len(s):
        c = s[i]
        if c.isspace():
            i += 1
        elif c in BN or (c == "." and i + 1 < len(s) and s[i + 1] in BN):
            j = i
            while j < len(s) and s[j] in BN:
                j += 1
            if j < len(s) and s[j] == ".":
                j += 1
                while j < len(s) and s[j] in BN:
                    j += 1
            v = _dec(s[i:j])
            if v is None:
                return None
            out.append(v)
            i = j
        elif c in "+-*/()":
            out.append(c)
            i += 1
        else:
            return None
    return out


def _parse(tok):
    """Recursive descent over + - * and parentheses. No `eval`: an extraction is input."""
    pos = 0

    def expr():
        nonlocal pos
        v = term()
        if v is None:
            return None
        while pos < len(tok) and isinstance(tok[pos], str) and tok[pos] in "+-":
            op = tok[pos]; pos += 1
            r = term()
            if r is None:
                return None
            v = v + r if op == "+" else v - r
        return v

    def term():
        nonlocal pos
        v = atom()
        if v is None:
            return None
        while pos < len(tok) and isinstance(tok[pos], str) and tok[pos] in "*/":
            op = tok[pos]; pos += 1
            r = atom()
            if r is None:
                return None
            if op == "*":
                v *= r
            else:
                # Fraction, so ৫০ ÷ ২৫ is exactly ২ and a mis-read ৫০ ÷ ২৪ is exactly 25/12 —
                # never equal to anything else in the chain. Floor division would quietly make
                # a mis-read *look* right; float would introduce a tolerance this book never
                # asked for. Division by zero is not an error here, it is an unreadable segment.
                if r == 0:
                    return None
                v = Fraction(v) / r
        return v

    def atom():
        nonlocal pos
        if pos >= len(tok):
            return None
        t = tok[pos]
        if isinstance(t, (int, Fraction)):
            pos += 1
            return t
        if t == "(":
            pos += 1
            v = expr()
            if v is None or pos >= len(tok) or tok[pos] != ")":
                return None
            pos += 1
            return v
        return None

    v = expr()
    return v if v is not None and pos == len(tok) else None


def evaluate(seg: str):
    s = seg.replace("**", "").replace("`", "").strip()
    if not s or BLANK in s or not EXPR_OK.match(s):
        return None
    if not any(c in BN for c in s):
        return None
    tok = _tokens(s)
    return _parse(tok) if tok else None



# ------------------------------------------------------------------- the printed mark
#
# CD-063. This book teaches by printing statements that are **false on purpose**, each carrying
# the book's own verdict — a red ✗ beside a trial, or the word মিথ্যা in a verdict cell. The
# naive handling is to skip them. **Skipping leaves the hole exactly where a mis-read hides:**
# print `৪৮ ÷ ৩ = ৮` ✗, mis-read the divisor as ৬, and the line becomes *true* — a skipped line
# is checked by nothing, so that error walks through. So the mark is read as data and the
# expectation is inverted against it.
#
# An UNMARKED comparison is **not** assumed true. ছাপা ১৮ prints `২৫ + ৪ > ৩০` with its verdict
# two speech-bubbles away; assuming a bare printed comparison holds would redden that correct
# transcription. No mark means no claim this check can test — it is reported uncovered.

FALSE_MARKS = ("✗", "✘", "মিথ্যা")
TRUE_MARKS = ("✓", "✔", "সত্য")


# **P-020 (CD-075) — the mark is not the only signal.**
#
# CD-063 read the book's `✗` and inverted the expectation against it. ছাপা ৮৬ prints three more
# deliberately-wrong long divisions **with no mark at all** — the signal is the instruction
# above them: *নিচের হিসাবগুলোতে কী ভুল আছে ব্যাখ্যা করি এবং তা ঠিক করি।* Keying on the mark
# alone would have reddened three faithful transcriptions, which is the same failure as
# skipping a `✗` line, arrived at from the other side.
#
# So expectation is inverted on **either** signal:
#
#     marked    — `✗`/`✓` beside the line or block            (ছাপা ৭৩, seven marks)
#     declared  — the line sits under a find-the-error heading (ছাপা ৮৬, three panels)
#
# A declared region ends at the next heading or horizontal rule, which is how the extraction
# separates exercises. Deliberately narrow: it must not swallow the rest of a chapter.

DECLARE_WRONG_RE = re.compile(
    r"(কী\s*ভুল\s*আছে|কি\s*ভুল\s*আছে|ভুল(?:গুলো)?\s*(?:খুঁজে|চিহ্নিত|শনাক্ত)"
    r"|ভুল\s*(?:আছে|থাকলে)\s*[^।]*ঠিক\s*করি)")

# The extraction's own declaration counts too — but it governs **its own line only**, never a
# region. Tried as a region first and it over-fired at once: a ⛔ paragraph in অধ্যায় ১, ৩ and ৪
# that *discusses* a deliberately-wrong block was followed, before the next heading, by
# perfectly correct divisions — which the inversion then reddened. An instruction printed in
# the book governs what comes after it; a remark in our own prose governs the sentence it is in.
DECLARE_SELF_RE = re.compile(r"(ইচ্ছাকৃতভাবে\s*ভুল|বইয়ের-মিথ্যা)")
REGION_END_RE = re.compile(r"^\s*(#{1,6}\s|-{3,}\s*$|\*{3,}\s*$)")


def declared_wrong_lines(text: str) -> set:
    """Line numbers sitting under a find-the-error instruction."""
    out, active = set(), False
    for i, raw in enumerate(text.splitlines(), 1):
        line = raw.strip().lstrip(">").strip()
        if REGION_END_RE.match(raw):
            active = False
        if DECLARE_SELF_RE.search(line):
            out.add(i)
        if DECLARE_WRONG_RE.search(line):
            active = True
            continue
        if active:
            out.add(i)
    return out


def mark_of(line: str):
    """-> False if the book marks the line false, True if it marks it true, None if unmarked."""
    if any(m in line for m in FALSE_MARKS):
        return False
    if any(m in line for m in TRUE_MARKS):
        return True
    return None


CMP_RE = re.compile(r"^(?P<a>[^<>=]+?)\s*(?P<op>[<>])\s*(?P<b>[^<>=]+)$")


def parse_comparisons(text: str):
    """Marked `A > B` / `A < B` lines — checked with the expectation the book's mark states."""
    out = []
    for i, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if line.startswith(">"):
            line = line[1:].strip()
        if "|" in line or BLANK in line:
            continue
        mk = mark_of(line)
        if mk is None:
            continue
        body_ = re.sub(r"^\*{0,2}\(\s*[০-৯ক-হ]+\s*\)\*{0,2}\s*", "", line)
        for m in FALSE_MARKS + TRUE_MARKS:
            body_ = body_.replace(m, " ")
        body_ = body_.strip(" —-–·|")
        m = CMP_RE.match(body_)
        if not m:
            continue
        a, b = evaluate(m.group("a")), evaluate(m.group("b"))
        if a is None or b is None:
            continue
        out.append((f"line {i}", m.group("op"), a, b, mk, i))
    return out


def parse_chains(text: str):
    """-> [(label, [(segment_text, value)], lineno)] — every line whose `=`-separated parts
    are each fully numeric. Within a blockquote run, a line starting with `=` continues the
    previous line's chain, which is how the printed ৫ rearrangement box is written.
    """
    out, carry, carry_lbl = [], None, None
    for i, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        quoted = line.startswith(">")
        if quoted:
            line = line[1:].strip()
        if not line:
            carry = None
            continue
        if BLANK in line and "=" not in line:
            continue
        # The book numbers its parts `(১)`, `(২)`, `(ক)` … and the extraction keeps that. Left in
        # place, `(১) ৬০৪২ × ১৫১৪` tokenises as a parenthesised number juxtaposed with another
        # and the whole segment fails to parse — which is exactly why every distributive line on
        # printed ৪ and ৬ was invisible while the ×১০০ box, which carries no item label, was read.
        line = re.sub(r"^\*{0,2}\(\s*[০-৯ক-হ]+\s*\)\*{0,2}\s*", "", line)
        # The mark has already been read off the raw line (CD-063); strip it before splitting,
        # or the segment carrying it evaluates to nothing and the chain silently disappears —
        # which would hand the mark's whole purpose back to luck.
        # **The mark belongs to the statement, not the line.** Once one line may hold several
        # claims (below), reading the mark off the whole line hands one statement's verdict to
        # its neighbour — and it did: a sign-off row naming both the `✗` block and the `✓`
        # block of the same printed item took the row's `✗` and reddened the `✓` half, which
        # balances and is *supposed* to. So: a statement's own mark wins; a line carrying both
        # kinds of mark lends neither.
        kinds = {mark_of(m) for m in (FALSE_MARKS + TRUE_MARKS) if m in raw}
        mk_line = kinds.pop() if len(kinds) == 1 else None
        # **One line may carry several independent claims, and joining them invents a false
        # one.** Found by the gate itself the moment decimals became readable (CD-074): an
        # annotation reading `০.৩২ × ১০ = ৩.২ ✓; ০.৩২ × ১০০ = ৩২ ✓; …` was split on `=` across
        # the whole line, so `৩.২` and `৩২` landed in the same chain and a correct line went
        # RED. The separators below are sentence separators, not operators — a chain never
        # crosses one. Splitting here *adds* coverage: that one line is three verifications.
        stmts = [t for t in re.split(r"[;।,]|\s·\s|→|\sও\s|\sএবং\s|\sআর\s", line) if t.strip()]
        made = 0
        last = None
        for si, stmt in enumerate(stmts):
            mk_here = mark_of(stmt)
            if mk_here is None:
                mk_here = mk_line
            for _m in FALSE_MARKS + TRUE_MARKS:
                stmt = stmt.replace(_m, " ")
            stmt = stmt.strip(" —-–·")
            vals = []
            for p in stmt.split("="):
                v = evaluate(p)
                if v is not None:
                    vals.append((p.strip(), v))
            if si == 0 and stmt.lstrip().startswith("=") and carry is not None and vals:
                vals = [carry] + vals
            if len(vals) >= 2:
                out.append((f"line {i}", vals, i, mk_here))
                made += 1
            if vals:
                last = vals[-1]
        vals = [last] if last else []
        if vals:
            carry, carry_lbl = vals[-1], f"line {i}"
        else:
            # **A chain may not jump over a line the evaluator could not read.** It did once,
            # on অধ্যায় ২'s very first worked equation, and reported RED on a correct
            # transcription: `৮ × ক = ৪৮` set the carry, the next line `ক = ৪৮ ÷ ৮` yielded
            # nothing (÷ is not in the operator set), and `= ৬` then chained ৬ back to ৪৮.
            # The skipped line had changed the subject entirely — which is exactly what an
            # unreadable line may always have done. Silence is not continuity.
            carry = None
    return out


def render(v) -> str:
    if isinstance(v, Fraction) and v.denominator != 1:
        return f"{v.numerator}/{v.denominator}".translate(TO_BN)
    return str(int(v)).translate(TO_BN)


def fits(printed, computed_bn: str) -> bool:
    if len(printed) != len(computed_bn):
        return False
    return all(p == BLANK or p == c for p, c in zip(printed, computed_bn))


def working(mcand: int, mplier: int):
    """The partial products as the book lays them out: rightmost multiplier digit first."""
    digits = str(mplier)[::-1]
    return [mcand * int(d) * (10 ** i) for i, d in enumerate(digits)]


def zero_digit_rows(mplier_digits: str):
    """Partial rows the book's box scaffold does not size by arithmetic.

    **Found in the book, not reasoned from it.** কাজ ৩(২) on printed ৩ is ৬২৫৮ × ৬০৯৭, whose
    third partial is ৬২৫৮ × ০ × ১০০ = 0 — one digit. The printed scaffold gives that row **six**
    boxes, the same width as the row above it: the book does not narrow the boxes for a zero
    multiplier digit. So for a zero digit the printed width carries no arithmetic claim, and
    checking it would redden a correct transcription.

    Only the zero-digit rows are excused. কাজ ৩(১), ৮৩৪৬ × ১৫৪৫, has no zero digit, and its
    printed widths are exactly 5·6·7·7 — which is how this gate caught a real transcription
    error on its first run against real content (CR-002).
    """
    return {i for i, d in enumerate(mplier_digits[::-1]) if d == "0"}


def solve(b: Block):
    """-> (status, detail, solutions). CLEAN | WIDTH | AMBIGUOUS | RED | REFUSE."""
    free = [i for i, c in enumerate(b.mcand) if c == BLANK] + \
           [i for i, c in enumerate(b.mplier) if c == BLANK]
    if len(free) > MAX_BLANKS:
        return "REFUSE", f"{len(free)} blank operand digits — over the {MAX_BLANKS} brute-force ceiling", []
    if len(b.partials) != len(b.mplier):
        return "RED", (f"SHAPE — {len(b.partials)} partial row(s) for a {len(b.mplier)}-digit "
                       f"multiplier; the book's layout and the operands disagree"), []

    nc, np_ = len(b.mcand), len(b.mplier)
    blanks_c = [i for i, c in enumerate(b.mcand) if c == BLANK]
    blanks_p = [i for i, c in enumerate(b.mplier) if c == BLANK]
    printed_cells = sum(1 for row in b.partials + [b.total] for c in row if c != BLANK)
    sols = []
    for combo in product(range(10), repeat=len(blanks_c) + len(blanks_p)):
        mc = list(b.mcand)
        mp = list(b.mplier)
        for pos, d in zip(blanks_c, combo[:len(blanks_c)]):
            mc[pos] = BN[d]
        for pos, d in zip(blanks_p, combo[len(blanks_c):]):
            mp[pos] = BN[d]
        if (nc > 1 and mc[0] == "০") or (np_ > 1 and mp[0] == "০"):
            continue
        a = int("".join(mc).translate(TO_ASCII))
        m = int("".join(mp).translate(TO_ASCII))
        skip = zero_digit_rows(str(m))
        parts = working(a, m)
        if any(i not in skip and not fits(pr, render(v))
               for i, (pr, v) in enumerate(zip(b.partials, parts))):
            continue
        if not fits(b.total, render(sum(parts))):
            continue
        sols.append((a, m, parts, sum(parts)))
        if len(sols) > 1:
            break
    if not sols:
        return "RED", ("does not balance — no assignment of the blank digits makes the printed "
                       "cells consistent, so at least one printed digit is mis-read"), []
    if len(sols) > 1:
        return "AMBIGUOUS", "more than one assignment fits — not covered, stays at full manual depth", sols
    a, m, parts, tot = sols[0]
    if printed_cells == 0:
        # Every working cell is an empty box. Nothing about the *digits* has been checked —
        # only that the scaffold's row widths match the operands. Reported as its own status
        # so a depth claim cannot quietly rest on it (SOURCE_POLICY §7.10).
        return "WIDTH", (f"{render(a)} × {render(m)}: scaffold widths agree, but every working "
                         f"cell is blank — no digit checked, stays at full manual depth"), sols
    how = "pinned uniquely from the printed cells" if free else "fully printed"
    return "CLEAN", f"{render(a)} × {render(m)} = {render(tot)}  ({how})", sols


# ------------------------------------------------------------------- long division
#
# Division's invariants are as forced as multiplication's, and the book prints all of them:
#
#   * ভাগফল × ভাজক + ভাগশেষ = ভাজ্য
#   * every subtraction row = ভাজক × that ভাগফল digit, in order
#   * the remainder is smaller than the divisor at every step — that is *why* the next digit
#     is brought down, and a mis-read digit routinely breaks it before it breaks anything else
#
# The check simulates the division from the printed ভাজ্য and ভাজক and compares its own rows
# against the printed ones, rather than trying to read the layout by column position. Column
# reading would make the gate depend on how an agent happened to space a code block; simulating
# depends only on the two numbers the book states.

DIV_LINE = re.compile(r"^\s*([০-৯\s]+)\)\s*([০-৯\s]+)$")


class Div:
    def __init__(self, label, quotient, divisor, dividend, subs, inters, final, lines=()):
        self.label, self.q, self.d, self.n = label, quotient, divisor, dividend
        self.subs, self.inters, self.final = subs, inters, final
        self.lines = tuple(lines)


def _num(s):
    """An INTEGER from a printed row, or None. **Never a silently de-pointed decimal.**

    **P-019's mine, defused in the same commit that made it reachable.** This used to strip
    every non-digit, so `_num("০.৬")` returned `৬` — the point simply gone. No live path
    reached it while `EXPR_OK` and `cells()` both rejected `.`, but the decimal evaluator
    above makes decimals ordinary, and a de-pointed divisor would turn a correct transcription
    RED or a wrong one CLEAN. Long-division simulation is integer-only by design (`simulate`
    walks digits), so the honest answer here is **refuse, not guess**: a decimal row returns
    None, the block REFUSEs by CD-072, and the census names it. Extending the simulator to
    decimal ভাজ্য/ভাজক is a separate ruling, not a side effect of this one.
    """
    if re.search(r"[০-৯]\s*\.|\.\s*[০-৯]", s):
        return None
    s = "".join(ch for ch in s if ch in BN)
    return int(s.translate(TO_ASCII)) if s else None


# --------------------------------------------------------------- ladder (মই-ভাগ) · CD-073
#
# The ladder is how this book finds লসাগু:
#
#     ২ ) ১২,  ১৮
#         ──────────
#     ৩ )  ৬,   ৯
#         ──────────
#          ২,   ৩
#
# It is NOT a long division and must never be simulated as one: the divisor line carries
# **several** dividends, and a row is not the previous row minus anything — it is the previous
# row divided, entry by entry, with indivisible entries carried down untouched.
#
# `DIV_LINE` therefore does not match it, and `parse_divisions` correctly returns nothing.
# **The bug was what happened next: also nothing.** Claiming no shape meant CD-072's
# never-vanish guarantee never engaged, and the census had no name for a ladder at all — so a
# block dense with exactly this book's hazard (multi-column numerals in fixed layout, §7.14.2c)
# was invisible. §7.17(a) says silence is not a permitted gate outcome; this extends it to a
# second shape.
#
# **Scope is deliberately visibility, not verification.** Checking a ladder — every entry
# divides by the stated prime, indivisible entries carry down unchanged, the left column's
# product is the লসাগু — is a real evaluator and a separate ruling. Bundling it here would be
# the detour that already cost a sitting. So: **the ladder is named and REFUSED, and its
# arithmetic stays where it is today, verified by hand at 400 dpi.**
LADDER_LINE = re.compile(r"^\s*[০-৯]+\s*\)\s*[০-৯]+\s*,[০-৯\s,]*$")


def parse_ladders(text: str):
    """Fenced blocks whose divisor line divides *several* numbers at once."""
    out = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if not lines[i].strip().startswith("```"):
            i += 1
            continue
        j, blk = i + 1, []
        while j < len(lines) and not lines[j].strip().startswith("```"):
            blk.append((j + 1, lines[j]))
            j += 1
        hit = next((k for k, (_, l) in enumerate(blk) if LADDER_LINE.match(l)), None)
        if hit is not None:
            rungs = sum(1 for _, l in blk if LADDER_LINE.match(l))
            out.append((f"line {blk[hit][0]}", rungs, [k for k, _ in blk]))
        i = j + 1
    return out


def _split_rows(rows):
    """Sort a division's rows into subtraction rows, intermediates, and the final remainder.

    **CD-072 · why this is structural and not sign-based.** The original reader called a row a
    subtraction row only if it started with `−`. `C5_MATH_Source_01.md` writes them that way, so
    the rule looked sound — but **C5 গণিত prints no minus signs at all**: a long division on
    ছাপা ৩৮ is aligned digits under rules and nothing else. With no signs, `subs` came back empty
    and the whole block was dropped.

    **Adding `−` to the transcription was never an option** — the book does not print it, and
    SOURCE_POLICY §3 says an extraction records what is printed. So the parser learns the layout
    instead of the page learning the parser.

    **The layout carries the information the sign was carrying.** In both styles a division runs

        <subtraction row>
        ─────────────────
        <intermediate>
        <subtraction row>
        ─────────────────
        ...
        <final remainder>

    so **the row immediately above a rule is the row being subtracted**, and the row below one is
    what the subtraction left. That is true of the signed style too, which is why one rule now
    reads both books: an explicit `−` still wins where it is printed, and position decides where
    it is not. Nothing about the signed path changes.
    """
    subs, inters = [], []
    cleaned = [(i, l.strip()) for i, l in enumerate(l for _, l in rows)]
    numeric = [(i, s) for i, s in cleaned if any(c in BN for c in s)]
    is_rule = {i for i, s in cleaned if s and RULE_RE.match(s)}
    for pos, (i, s) in enumerate(numeric):
        nxt = numeric[pos + 1][0] if pos + 1 < len(numeric) else len(cleaned)
        # a rule between this numeric row and the next one closes a subtraction step
        rule_follows = any(j in is_rule for j in range(i + 1, nxt))
        (subs if s.startswith(("−", "-")) or rule_follows else inters).append(_num(s))
    final = inters[-1] if inters else None
    return subs, inters, final


def parse_divisions(text: str):
    """Long-division blocks written inside a fenced code block.

            ৯ ৫
        ─────────
    ৪ ৫ ) ৪ ২ ৭ ৫
        − ৪ ০ ৫
        ─────────
          ২ ২ ৫
        − ২ ২ ৫
        ─────────
              ০
    """
    out = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if not lines[i].strip().startswith("```"):
            i += 1
            continue
        j = i + 1
        blk = []
        while j < len(lines) and not lines[j].strip().startswith("```"):
            blk.append((j + 1, lines[j]))
            j += 1
        hit = next((k for k, (_, l) in enumerate(blk) if DIV_LINE.match(l)), None)
        if hit is not None and not any(BLANK in l for _, l in blk):
            ln, dline = blk[hit]
            m = DIV_LINE.match(dline)
            divisor, dividend = _num(m.group(1)), _num(m.group(2))
            quotient = next((_num(l) for _, l in blk[:hit][::-1]
                             if any(c in BN for c in l)), None)
            subs, inters, final = _split_rows(blk[hit + 1:])
            if None not in (divisor, dividend, quotient) and subs:
                out.append(Div(f"line {ln}", quotient, divisor, dividend, subs, inters, final,
                               [k for k, _ in blk]))
            else:
                # **CD-072: the block does not vanish.** It used to. If the numbers would not
                # parse the append simply never happened, so the block was neither verified nor
                # reported — and the census cannot name a shape the parser never returned. That
                # is strictly worse than an uncovered shape: CD-059 exists so unparsed shapes are
                # *visible*, and a `☐` block has always REFUSEd out loud (CD-060b). This one was
                # silent, and the file read as fully covered while two complete divisions on
                # ছাপা ৩৮ went unchecked. **Every path out of here now appends something.**
                out.append(Div(f"line {ln}", None, None, None, [], [], None,
                               [k for k, _ in blk]))
        elif hit is not None:
            out.append(Div(f"line {blk[hit][0]}", None, None, None, [], [], None,
                           [k for k, _ in blk]))
        i = j + 1
    return out


def simulate(n: int, d: int):
    """The rows the book would print: (subtrahends, values after each subtraction).

    Standard long division: take digits of the ভাজ্য left to right; once the running value
    reaches the ভাজক, each step contributes one ভাগফল digit, one subtraction row, and one
    remainder row with the next digit brought down.
    """
    subs, inters, cur, started = [], [], 0, False
    ds = str(n)
    for idx, ch in enumerate(ds):
        cur = cur * 10 + int(ch)
        q = cur // d
        if q == 0 and not started:
            continue
        started = True
        subs.append(q * d)
        cur -= q * d
        # The row printed under a subtraction is the remainder with the next digit brought
        # down — which is exactly what the next iteration's `cur` becomes. Bringing it down
        # *here* as well double-counted it, and the bug was invisible on a one-step division.
        inters.append(cur * 10 + int(ds[idx + 1]) if idx + 1 < len(ds) else cur)
    return subs, inters


def check_division(b: Div, expect: bool = True):
    """`expect=False` means the book prints this block as a deliberate error (CD-075).

    Under inversion a block that checks out is RED — the only way a *deliberately wrong* panel
    balances is that a digit was mis-transcribed — and a block that does not check out is
    CLEAN, because the book said so.
    """
    if expect is False:
        st, detail, _ = check_division(b, expect=True)
        if st == "REFUSE":
            return st, detail, 0
        if st == "RED":
            return "CLEAN", "বইয়ের ঘোষিত-ভুল ব্লক, এবং সত্যিই মেলে না — যা সঠিক (" + detail + ")", 1
        return "RED", ("the book declares this working WRONG, but it checks out — a mis-read has "
                       "made a deliberately wrong panel come out right: " + detail), 0
    if b.q is None:
        return "REFUSE", "division block carries blanks or an unreadable ভাজক/ভাজ্য — not checked", 0
    q, d, n = b.q, b.d, b.n
    if d == 0:
        return "RED", "ভাজক is zero", 0
    subs, inters = simulate(n, d)
    quo, rem = divmod(n, d)
    notes = []
    if quo != q:
        return "RED", (f"ভাগফল does not follow: {render(n)} ÷ {render(d)} = {render(quo)}, "
                       f"printed {render(q)}"), 0
    if b.final is not None and b.final != rem:
        return "RED", (f"ভাগশেষ does not follow: expected {render(rem)}, printed "
                       f"{render(b.final)}"), 0
    if rem >= d:
        return "RED", f"ভাগশেষ {render(rem)} is not smaller than ভাজক {render(d)}", 0
    if b.subs != subs:
        return "RED", ("a subtraction row is not ভাজক × the matching ভাগফল digit: expected "
                       + " · ".join(render(x) for x in subs) + " · printed "
                       + " · ".join(render(x) for x in b.subs)), 0
    # Intermediates are matched as an ordered subsequence: a book may or may not print the
    # bring-down row, and a layout difference must not redden a correct transcription — but a
    # mis-read value matches nothing and still goes RED.
    it = iter(inters)
    for v in b.inters:
        if not any(v == e for e in it):
            return "RED", (f"intermediate value {render(v)} appears nowhere in the working: "
                           + " · ".join(render(x) for x in inters)), 0
    return "CLEAN", (f"{render(n)} ÷ {render(d)} = {render(q)} ভাগশেষ {render(rem)}  "
                     f"({len(b.subs)} subtraction row(s) check out; ভাগশেষ < ভাজক)"), 1


def census(text: str, seen: set):
    """What the gate did NOT look at, named rather than left to a flat number.

    **A count of what passed is not a statement of coverage.** Four printed pages were added to
    the first Math extraction and `8 item(s) verified` did not move, because the gate does not
    parse those working shapes — and nothing in its output said so. Silence about unparsed
    content is only acceptable if the output names what it skipped, so this walks every
    numeric-bearing line the checks did not consume and groups it by signature.
    """
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines, 1)
                  if re.match(r"^#\s+(?:Unit|পাঠ|অধ্যায়)\s", l)), 1)
    ops = re.compile(r"[×÷+\-−=]")
    sig = {}
    for i, raw in enumerate(lines, 1):
        if i < start or i in seen:
            continue
        line = raw.strip().lstrip(">").strip()
        if sum(c in BN for c in line) < 2:
            continue
        if "÷" in line and "=" in line:
            # `÷` with an `=` is working the gate could not read. `÷` without one is a bare
            # exercise — the অনুশীলন lists are full of them, and filing those under "long
            # division not parsed" would report a gap that no extension can ever close.
            k = "÷ long division"
        elif "ǀ" in line or "│" in line:
            k = "vertical-bar trailing-zero layout"
        elif BLANK in line and not any(c in BN for c in line.replace(BLANK, "")):
            k = "blank-only exercise cells"
        elif ops.search(line) and not re.search(r"[অ-হ]", line.replace("×", "")):
            # Digits and operators, no Bengali letters. Two very different cases, and collapsing
            # them would inflate the alarm: a line with an `=` asserts something the gate failed
            # to read, while a bare `A × B` exercise asserts nothing at all — there is no printed
            # answer to check it against, and no extension will ever change that.
            k = ("ARITHMETIC LINE NOT PARSED" if "=" in line
                 else "bare exercise (no printed answer to check)")
        else:
            k = "prose carrying numbers (limit 3)"
        sig[k] = sig.get(k, 0) + 1
    return sig


def run(path: Path, quiet=False):
    text = body(path.read_text(encoding="utf-8"))
    blocks, steps, chains = parse_blocks(text), parse_steps(text), parse_chains(text)
    divs, comps = parse_divisions(text), parse_comparisons(text)
    ladders = parse_ladders(text)
    declared = declared_wrong_lines(text)          # CD-075, second signal
    lines_ = text.splitlines()
    rows, red, covered, uncovered = [], False, 0, 0
    seen = set()
    for label, rungs, lns in ladders:
        # CD-073 · named and REFUSED, never absent. Visibility only — see parse_ladders.
        for k in lns:
            seen.add(k)
        rows.append(("REFUSE", label,
                     f"ladder (মই-ভাগ), {rungs} rung(s) — not a long division; "
                     f"no ladder evaluator exists, so nothing here is machine-checked"))
        uncovered += 1
    for dv in divs:
        for k in dv.lines:
            seen.add(k)
        # Either signal flips the expectation: a `✗` anywhere in the block, or the block
        # sitting under a find-the-error instruction.
        marked = any(mark_of(lines_[k - 1]) is False for k in dv.lines if 0 < k <= len(lines_))
        expect = not (marked or any(k in declared for k in dv.lines))
        st, detail, got = check_division(dv, expect)
        rows.append((st, dv.label, detail))
        red = red or st == "RED"
        covered += got
        uncovered += st == "REFUSE"
    for b in blocks:
        st, detail, _ = solve(b)
        rows.append((st, b.label, detail))
        red = red or st == "RED"
        covered += st == "CLEAN"
        uncovered += st in ("WIDTH", "AMBIGUOUS", "REFUSE")
    for label, a, m, c, ln in steps:
        good = a * m == c
        seen.add(ln)
        rows.append(("CLEAN" if good else "RED", label,
                     f"{render(a)} × {render(m)} = {render(c)}" if good
                     else f"step table does not balance: {render(a)} × {render(m)} = {render(a*m)}, printed {render(c)}"))
        red = red or not good
        covered += good
    for label, vals, ln, mk in chains:
        seen.add(ln)
        holds = len({v for _, v in vals}) == 1
        shown = " = ".join(s for s, _ in vals)
        # CD-063 + CD-075: the book's own mark sets the expectation; failing a mark, a
        # find-the-error instruction above the line sets it. Neither -> must hold, as before.
        expect = mk if mk is not None else (False if ln in declared else True)
        declared_here = mk is None and ln in declared
        if holds == expect:
            note = (" — বইয়ের নির্দেশ অনুযায়ী ভুল, এবং সত্যিই মেলে না, যা সঠিক"
                    if declared_here else
                    "" if mk is None else (" — বইয়ের ✓ অনুযায়ী মেলে" if mk
                                           else " — বইয়ের ✗/মিথ্যা অনুযায়ী মেলে না, যা সঠিক"))
            rows.append(("CLEAN", label, f"চেইন: {shown}{note}"))
            covered += 1
        else:
            red = True
            why = ("the book marks this line FALSE, but it balances — a mis-read has made a "
                   "deliberately wrong line come out true" if mk is False else
                   "the book marks this line TRUE, but it does not balance" if mk is True else
                   "the book declares this working WRONG, but it balances — a mis-read has made "
                   "a deliberately wrong line come out true" if declared_here else
                   "equality chain does not hold")
            rows.append(("RED", label, why + ": " +
                         " ≠ ".join(f"{s} ({render(v)})" for s, v in vals)))
    for label, op, a, b, mk, ln in comps:
        seen.add(ln)
        holds = (a > b) if op == ">" else (a < b)
        if holds == mk:
            rows.append(("CLEAN", label,
                         f"তুলনা: {render(a)} {op} {render(b)} — বইয়ের চিহ্ন অনুযায়ী "
                         f"{'সত্য' if mk else 'মিথ্যা'}, মিলেছে"))
            covered += 1
        else:
            red = True
            rows.append(("RED", label,
                         f"comparison contradicts the book's own mark: {render(a)} {op} "
                         f"{render(b)} is {holds}, but the book marks it {mk}"))
    if quiet:
        # `covered == 0` is REFUSE, never 0. A file whose only blocks are ambiguous or pure
        # scaffold has had nothing verified, and returning CLEAN there would hand a depth
        # reduction to content the check never read.
        return 2 if red else (0 if covered else 3)

    unparsed = census(text, seen)
    print("math_arith_check.py — the extraction's arithmetic against itself")
    print(f"file   : {path.relative_to(REPO) if str(path).startswith(str(REPO)) else path}")
    print(f"found  : {len(blocks)} worked block(s), {len(steps)} step-table row(s), "
          f"{len(chains)} equality chain(s), {len(divs)} division block(s), "
          f"{len(ladders)} ladder(s), "
          f"{len(comps)} marked comparison(s)")
    print("-" * 78)
    for st, label, detail in rows:
        print(f"[{st:9}] {label:10} {detail}")
    if not rows:
        print("  ! no worked multiplication, step table, equality chain or division in the body")
    print("-" * 78)
    print("LIMITS : computed working only · words/names/instructions out of scope ·")
    print("         problem-statement figures unchecked where the book prints no working")
    shapes = ", ".join(f"{k} ×{v}" for k, v in sorted(unparsed.items(), key=lambda kv: -kv[1])) or "none"
    print(f"NOT LOOKED AT: {shapes}")
    if red:
        print("VERDICT: RED — a printed digit is mis-read (AGENTS.md §5: back to build phase)")
        return 2
    if not covered:
        print("VERDICT: REFUSE — nothing was actually verified here; this is not a pass")
        return 3
    # The summary states coverage, never a bare count: a flat number read as completeness once
    # already (CD-058), and the shapes it did not parse are named on the same line.
    print(f"VERDICT: CLEAN — {covered} verified · {uncovered} uncovered "
          f"(full manual depth, §7.10) · shapes not parsed: {shapes}")
    return 0


# ------------------------------------------------------------------------ selftest

SYNTH_OK = """
> ৪৬১৪
> × ৩৬৫
> ─────
> ২৩০৭০
> ২৭৬৮৪০
> ১৩৮৪২০০
> ─────
> ১৬৮৪১১০
"""

SYNTH_BLANKS = """
> ৫ ৫ ৭ ☐
> × ৪ ☐ ৭ ৭
> ─────
> ☐ ৯ ০ ৫ ৩
> ৩ ৯ ০ ৫ ৩ ০
> ৩ ৩ ৪ ☐ ৪ ০ ০
> ২ ২ ৩ ১ ৬ ০ ০ ০
> ─────
> ২ ৬ ০ ☐ ২ ৯ ৮ ৩
"""

SYNTH_AMBIG = """
> ☐ ☐
> × ☐
> ─────
> ☐ ☐
> ─────
> ☐ ☐
"""

# কাজ ৩(১) as the book prints it: ৮৩৪৬ × ১৫৪৫, every working cell an empty box.
# Widths 5·6·7·7 are forced by the operands — no zero digit in ১৫৪৫ — which is what makes
# this block's shape checkable at all.
SYNTH_SCAFFOLD = """
> ৮ ৩ ৪ ৬
> × ১ ৫ ৪ ৫
> ─────
> ☐ ☐ ☐ ☐ ☐
> ☐ ☐ ☐ ☐ ☐ ☐
> ☐ ☐ ☐ ☐ ☐ ☐ ☐
> ☐ ☐ ☐ ☐ ☐ ☐ ☐
> ─────
> ☐ ☐ ☐ ☐ ☐ ☐ ☐ ☐
"""

# ছাপা ৪ · কাজ ৪(১): the multiplier is broken up and multiplied alongside. The claim is that
# every way of writing the line is the same number, so the terms must sum to the multiplier.
SYNTH_DIST = """
# অধ্যায় ১

**(১)** ৬০৪২ × ১৫১৪ = ৬০৪২ × (১০০০ + ৫০০ + ১০ + ৪)
"""

# ছাপা ৬ · কাজ ১(১): the (X − ১) trick. `১০০ − ১` must actually be the printed ৯৯.
SYNTH_MINUS = """
# অধ্যায় ১

**(১)** ৯৯ × ২৪ = ( ১০০ − ১ ) × ২৪
"""

# ছাপা ৫: the rearrangement box — four lines, one quantity.
SYNTH_LADDER = """
# অধ্যায় ১

> ৭৪০০ × ২৯০০
> = ৭৪ × ১০০ × ২৯ × ১০০
> = ৭৪ × ২৯ × ১০০ × ১০০
> = ২১৪৬ × ১০০০০
> = ২১৪৬০০০০
"""


# ছাপা ৮ · the first long division in the book: ৪২৭৫ ÷ ৪৫ = ৯৫, ভাগশেষ ০.
SYNTH_DIV = """
# অধ্যায় ১

```
              ৯ ৫
        ─────────────
  ৪ ৫ ) ৪ ২ ৭  ৫
      − ৪ ০ ৫
        ─────────
          ২ ২ ৫
        − ২ ২ ৫
        ─────────
              ০
```
"""

# CD-072 · the signless layout this book actually prints: aligned digits under rules, no `−`.
# ৬৯০৫ ÷ ৪ = ১৭২৬, ভাগশেষ ১ (ছাপা ৩৮).
SYNTH_DIV_NOSIGN = """
# অধ্যায় ৩

```
       ১   ৭   ২   ৬
   ৪ ) ৬   ৯   ০   ৫
       ৪
       ───
       ২   ৯
       ২   ৮
       ───
           ১   ০
               ৮
           ───
               ২   ৫
               ২   ৪
               ───
                   ১
```
"""

# The same block with the ভাজ্য made unreadable. The point of this seed is NOT the RED/REFUSE
# label — it is that the block still appears in the output at all. Before CD-072 a block whose
# numbers would not parse was appended to nothing and vanished from the census.
SYNTH_DIV_UNPARSEABLE = """
# অধ্যায় ৩

```
       ১   ৭   ২   ৬
   ৪ ) ৬   ৯   ০   ৫
```
"""

# CD-073 · the মই-ভাগ from ছাপা ৩৯. Hand-verified sound: ২ × ৩ × ২ × ৩ = ৩৬ = লসাগু(১২, ১৮).
# The gate must NAME it and REFUSE, never return empty. It must not try to verify it.
#
# **Named SYNTH_MOI, not SYNTH_LADDER — and the selftest is why.** `SYNTH_LADDER` was already
# taken by ছাপা ৫'s ×১০০ rearrangement box, so the first draft of this fixture silently
# overwrote it and two unrelated chain cases went REFUSE. The clash was invisible in the diff
# and obvious in the run. **Two different things in this book are called a "ladder" in English;
# only one of them is the মই-ভাগ.**
SYNTH_MOI = """
# অধ্যায় ৩

```text
২ ) ১২,  ১৮
    ──────────
৩ )  ৬,   ৯
    ──────────
     ২,   ৩
```
"""

# Three columns, and the middle entry carries down undivided (৩ does not divide ৭) — the shape
# that most obviously is not a long division. ২ × ৩ × ২ × ৭ × ৩ = ২৫২ = লসাগু(১২, ১৪, ১৮).
SYNTH_MOI_3COL = """
# অধ্যায় ৩

```text
২ ) ১২,  ১৪,  ১৮
    ────────────────
৩ )  ৬,   ৭,   ৯,
    ────────────────
     ২,   ৭,   ৩
```
"""

# A division that leaves a remainder — the ভাগশেষ < ভাজক invariant has something to bite on.
SYNTH_DIV_REM = """
# অধ্যায় ১

```
              ৯ ৫
        ─────────────
  ৪ ৫ ) ৪ ২ ৭  ৭
      − ৪ ০ ৫
        ─────────
          ২ ২ ৭
        − ২ ২ ৫
        ─────────
              ২
```
"""

# কাজ ৩(২): ৬২৫৮ × ৬০৯৭. The third partial is ৬২৫৮ × ০ × ১০০ = 0 — one digit — and the book
# still prints SIX boxes for it. The scaffold is not sized by arithmetic where the multiplier
# digit is zero, so that row is excused; the rest of the block is not.
SYNTH_ZERO = """
> ৬ ২ ৫ ৮
> × ৬ ০ ৯ ৭
> ─────
> ☐ ☐ ☐ ☐ ☐
> ☐ ☐ ☐ ☐ ☐ ☐
> ☐ ☐ ☐ ☐ ☐ ☐
> ☐ ☐ ☐ ☐ ☐ ☐ ☐ ☐
> ─────
> ☐ ☐ ☐ ☐ ☐ ☐ ☐ ☐
"""



# ---------------------------------------------------------------- P-019 / P-020 fixtures
#
# Ground truth is অধ্যায় ৫, hand-verified at 400 dpi in the session that read it: the three
# `✗` blocks of ছাপা ৭৩, the three declared-wrong panels of ছাপা ৮৬, and the correct results
# beside them. A fixture drawn from the book beats an invented one — it fails the way the book
# would actually make it fail.

SYNTH_DEC_OK = """
# অধ্যায় ৫

> ০.১ + ০.২ = ০.৩
> ২৫.৫২ + ১২.৬৫ = ৩৮.১৭
> ৪.৮০ − ৩.৫৯ = ১.২১
> ২.১৩ × ৬ = ১২.৭৮
> ৯৮.৭ ÷ ২১ = ৪.৭
"""

# The chapter's signature failure: every digit right, the point one place out.
SYNTH_DEC_SHIFT = """
# অধ্যায় ৫

> ২.১৩ × ৬ = ১.২৭৮
"""

SYNTH_DEC_DIGIT = """
# অধ্যায় ৫

> ২৫.৫২ + ১২.৬৫ = ৩৮.১৮
"""

# ছাপা ৭৩: the book prints these WRONG on purpose and marks them ✗.
SYNTH_MARKED_WRONG = """
# অধ্যায় ৫

> ✗ ৪ − ২.৩১ = ২.৩৩
> ✗ ৩.৭৫ − ০.৫ = ৩.৭০
> ✗ ৭.৫৮ − ৬.৮৭ = ৭১
"""

# The mirror seed. If a transcription "tidies" a ✗ block into the right answer, the block stops
# being what the book printed — and that is precisely the mis-read the mark exists to catch.
SYNTH_MARKED_WRONG_TIDIED = """
# অধ্যায় ৫

> ✗ ৪.০০ − ২.৩১ = ১.৬৯
"""

SYNTH_MARKED_TRUE_BAD = """
# অধ্যায় ৫

> ✓ ৪.০৬ + ২.৯৪ = ৭.০১
"""

# ছাপা ৮৬: three more deliberately-wrong workings, and this time NO mark — the instruction
# above them is the only signal.
SYNTH_DECLARED_WRONG = """
# অধ্যায় ৫

> নিচের হিসাবগুলোতে কী ভুল আছে ব্যাখ্যা করি এবং তা ঠিক করি।

> ৪.৬৫ ÷ ১৫ = ৩১
> ২১.৩২ ÷ ৫.২ = ৪১
> ৩ ÷ ০.১২৫ = ০.০২৪
"""

SYNTH_DECLARED_WRONG_TIDIED = """
# অধ্যায় ৫

> নিচের হিসাবগুলোতে কী ভুল আছে ব্যাখ্যা করি এবং তা ঠিক করি।

> ৪.৬৫ ÷ ১৫ = ০.৩১
"""

# The declared region must end. If it leaked past the exercise, every later correct line in the
# chapter would be expected to be wrong — a gate that reddens the whole book after one heading.
SYNTH_DECLARED_SCOPE = """
# অধ্যায় ৫

> নিচের হিসাবগুলোতে কী ভুল আছে ব্যাখ্যা করি এবং তা ঠিক করি।

> ৪.৬৫ ÷ ১৫ = ৩১

---

> ২.১৩ × ৬ = ১২.৭৮
"""


def selftest():
    import tempfile
    print("SELFTEST — a mutated digit must turn the gate RED")
    print("-" * 78)
    ok = True

    def verdict(s: str) -> int:
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "C5_MATH_Source_99.md"
            p.write_text(s, encoding="utf-8")
            return run(p, quiet=True)

    def case(label, s, want):
        nonlocal ok
        got = verdict(s)
        good = got == want
        ok = ok and good
        names = {0: "CLEAN", 2: "RED", 3: "REFUSE"}
        print(f"[{'PASS' if good else 'FAIL'}] {label} -> {names.get(got, got)} "
              f"(wanted {names.get(want, want)})")

    # controls
    case("control · a fully printed block balances", SYNTH_OK, 0)
    case("control · blanks pinned uniquely balance", SYNTH_BLANKS, 0)

    # the seeds: one digit changed, in every position the check is supposed to reach
    case("seed · digit flipped in the total", SYNTH_OK.replace("১৬৮৪১১০", "১৬৮৪১২০"), 2)
    case("seed · digit flipped in a partial", SYNTH_OK.replace("২৭৬৮৪০", "২৭৬৮৫০"), 2)
    case("seed · digit flipped in the multiplicand", SYNTH_OK.replace("> ৪৬১৪", "> ৪৬১৫"), 2)
    case("seed · digit flipped in the multiplier", SYNTH_OK.replace("× ৩৬৫", "× ৩৬৬"), 2)
    case("seed · digit flipped inside a blanks block", SYNTH_BLANKS.replace("৩ ৯ ০ ৫ ৩ ০", "৩ ৯ ০ ৫ ৪ ০"), 2)
    case("seed · a partial row dropped (shape)", SYNTH_OK.replace("> ২৭৬৮৪০\n", ""), 2)
    case("seed · step table does not balance",
         "| ৪৬১৪ × ৫ | → | ২৩০৭১ |\n", 2)
    case("control · step table balances", "| ৪৬১৪ × ৫ | → | ২৩০৭০ |\n", 0)

    # --- equality chains: distributive expansion, the (X − ১) trick, the ×১০০ box (CD-058)
    case("control · distributive terms sum to the multiplier", SYNTH_DIST, 0)
    case("seed · a distributive term is mutated", SYNTH_DIST.replace("৫০০", "৬০০"), 2)
    case("seed · the multiplier is mutated against its own expansion",
         SYNTH_DIST.replace("× ১৫১৪ =", "× ১৫২৪ ="), 2)
    case("control · (X − ১) matches the left-hand number", SYNTH_MINUS, 0)
    case("seed · (X − ১) does not match the left-hand number",
         SYNTH_MINUS.replace("( ১০০ − ১ )", "( ১০০ − ২ )"), 2)
    case("seed · the left-hand number is mutated against (X − ১)",
         SYNTH_MINUS.replace("৯৯ × ২৪ =", "৯৮ × ২৪ ="), 2)
    case("control · the ×১০০ rearrangement chain holds", SYNTH_LADDER, 0)
    case("seed · one line of the rearrangement chain is mutated",
         SYNTH_LADDER.replace("= ২১৪৬ × ১০০০০", "= ২১৪৬ × ১০০০"), 2)
    case("control · the split-cell ladder table row is read",
         "# অধ্যায় ১\n\n| ৭৪ | × ২৯ | = | ২১৪৬ |\n", 0)
    case("seed · the split-cell ladder table row does not balance",
         "# অধ্যায় ১\n\n| ৭৪ | × ২৯ | = | ২১৪৭ |\n", 2)
    # a blank anywhere in a segment means it is an exercise, not a claim — never evaluated
    case("a chain segment containing ☐ is not evaluated",
         "# অধ্যায় ১\n\n> ৯৯ × ২৪ = ☐ × ২৪ − ☐ × ২৪\n", 3)

    # --- long division (CD-060): the invariants are as forced as multiplication's
    # --- CD-073 · the ladder is NAMED and REFUSED, never absent. Visibility, not verification.
    case("seed · CD-073 · a two-column মই-ভাগ REFUSEs — it must never return empty",
         SYNTH_MOI, 3)
    case("seed · CD-073 · a three-column মই-ভাগ with a carried-down entry REFUSEs",
         SYNTH_MOI_3COL, 3)
    for _lbl, _txt in (("two-column", SYNTH_MOI), ("three-column", SYNTH_MOI_3COL)):
        _found = len(parse_ladders(body(_txt)))
        _hit = _found == 1
        ok = ok and _hit
        print(f"[{'PASS' if _hit else 'FAIL'}] seed · CD-073 · the {_lbl} ladder is COUNTED "
              f"(parse_ladders -> {_found}, wanted 1) — the census can name it")
    # ...and no regression: a real long division is still a division, not a ladder.
    for _lbl, _txt in (("signed", SYNTH_DIV), ("signless", SYNTH_DIV_NOSIGN)):
        _lad, _div = len(parse_ladders(body(_txt))), len(parse_divisions(body(_txt)))
        _hit = (_lad, _div) == (0, 1)
        ok = ok and _hit
        print(f"[{'PASS' if _hit else 'FAIL'}] control · CD-073 · a {_lbl} long division is NOT "
              f"read as a ladder (ladders {_lad} wanted 0, divisions {_div} wanted 1)")

    # --- CD-072. The first case is the fix; the rest guard it in both directions.
    case("control · CD-072 · a SIGNLESS division (this book's layout) balances",
         SYNTH_DIV_NOSIGN, 0)
    case("seed · CD-072 · signless: ভাগফল mutated must go RED, not silent",
         SYNTH_DIV_NOSIGN.replace("১   ৭   ২   ৬", "১   ৭   ২   ৫"), 2)
    case("seed · CD-072 · signless: one subtraction row mutated must go RED",
         SYNTH_DIV_NOSIGN.replace("       ২   ৮", "       ২   ৭"), 2)
    case("seed · CD-072 · signless: ভাগশেষ mutated must go RED",
         SYNTH_DIV_NOSIGN.replace("                   ১\n", "                   ৩\n"), 2)
    case("seed · CD-072 · an unparseable division REFUSEs — it must never vanish",
         SYNTH_DIV_UNPARSEABLE, 3)
    case("control · long division balances", SYNTH_DIV, 0)
    case("control · long division with a remainder balances", SYNTH_DIV_REM, 0)
    case("seed · ভাগফল mutated", SYNTH_DIV.replace("৯ ৫", "৯ ৬"), 2)
    case("seed · a subtraction row is not ভাজক × its ভাগফল digit",
         SYNTH_DIV.replace("− ৪ ০ ৫", "− ৪ ০ ৬"), 2)
    case("seed · the ভাগশেষ does not follow",
         SYNTH_DIV.replace("              ০", "              ১"), 2)
    case("seed · an intermediate bring-down row is mutated",
         SYNTH_DIV.replace("          ২ ২ ৫", "          ২ ৩ ৫"), 2)
    case("seed · ভাজ্য mutated against its own working",
         SYNTH_DIV.replace("৪ ২ ৭  ৫", "৪ ২ ৭  ৬"), 2)
    case("seed · ভাজক mutated against its own working",
         SYNTH_DIV.replace("  ৪ ৫ )", "  ৪ ৬ )"), 2)
    case("a division block carrying ☐ is REFUSED, not guessed",
         SYNTH_DIV.replace("− ৪ ০ ৫", "− ☐ ০ ৫"), 3)

    # CD-062 still guards, but its original fixture stopped exercising it the moment ÷ became
    # readable: `ক = ৪৮ ÷ ৮` now evaluates, so that chain legitimately joins. The guard is
    # re-seeded with a middle line that is genuinely unreadable — prose, no evaluable segment.
    case("control · a chain does not jump over an unreadable line",
         "# অধ্যায় ২\n\n> ৮ × ক = ৪৮\n> এবার ক এর মান বসাই\n> = ৬\n", 3)
    case("control · ÷ now evaluates, so a real ÷ chain joins",
         "# অধ্যায় ২\n\n> ক = ৪৮ ÷ ৮\n> = ৬\n", 0)

    # --- CD-063: the printed mark is data, and the expectation inverts against it
    case("control · a ✗-marked chain that does NOT balance is correct",
         "# অধ্যায় ২\n\n> ১ × ২৪ + ১৫০ = ১৭৪ = ২৪৬ ✗\n", 0)
    case("seed · a ✗-marked chain that BALANCES is a mis-read",
         "# অধ্যায় ২\n\n> ৪ × ২৪ + ১৫০ = ২৪৬ ✗\n", 2)
    case("control · a ✓-marked chain that balances is correct",
         "# অধ্যায় ২\n\n> ৪৮ ÷ ৬ = ৮ ✓\n", 0)
    case("seed · a ✓-marked chain that does NOT balance is a mis-read",
         "# অধ্যায় ২\n\n> ৪৮ ÷ ৫ = ৮ ✓\n", 2)
    case("control · the verdict WORD মিথ্যা is read as the mark",
         "# অধ্যায় ২\n\n> ১ × ২৪ + ১৫০ = ১৭৪ = ২৪৬ — মিথ্যা\n", 0)
    case("seed · a মিথ্যা-marked chain that balances is a mis-read",
         "# অধ্যায় ২\n\n> ৪ × ২৪ + ১৫০ = ২৪৬ — মিথ্যা\n", 2)
    case("control · a মিথ্যা-marked comparison that is false is correct",
         "# অধ্যায় ২\n\n> ২৫ + ৪ > ৩০ — মিথ্যা\n", 0)
    case("seed · a মিথ্যা-marked comparison that is TRUE is a mis-read",
         "# অধ্যায় ২\n\n> ২৫ + ৪ > ২০ — মিথ্যা\n", 2)
    case("control · a সত্য-marked comparison that is true is correct",
         "# অধ্যায় ২\n\n> ২৫ + ৪ < ৩০ — সত্য\n", 0)
    case("an UNMARKED comparison is not assumed true — it is uncovered, not RED",
         "# অধ্যায় ২\n\n> ২৫ + ৪ > ৩০\n", 3)
    case("control · table-held marked blocks stay out of the checker (CD-061 layout guard)",
         "# অধ্যায় ২\n\n| ১ × ২৪ + ১৫০ = ২৪৬ | মিথ্যা |\n", 3)
    case("control · a genuine two-line chain still joins",
         "# অধ্যায় ২\n\n> ৭৪ × ২৯\n> = ২১৪৬\n", 0)

    # --- coverage honesty (CD-059): the summary must name what it did not read
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        import tempfile as _tf
        with _tf.TemporaryDirectory() as d:
            f = Path(d) / "C5_MATH_Source_98.md"
            f.write_text(SYNTH_OK + "\n# অধ্যায় ১\n\n> ১২৩ ÷ ৪ = ৩০ ভাগশেষ ৩\n", encoding="utf-8")
            run(f)
    out = buf.getvalue()
    named = "NOT LOOKED AT" in out and "÷ long division" in out and "shapes not parsed" in out
    ok = ok and named
    print(f"[{'PASS' if named else 'FAIL'}] the summary names unparsed shapes, not just a count")

    # the branches that must never be mistaken for a pass
    case("an under-determined block is AMBIGUOUS, not CLEAN",
         SYNTH_AMBIG, 3)   # ambiguous only -> nothing covered -> REFUSE, never 0
    case("a file with no working REFUSEs rather than passing",
         "# অধ্যায় ৯ — জ্যামিতি\n\n> কম্পাস দিয়ে বৃত্ত আঁকি।\n", 3)
    case("a pure scaffold is WIDTH-only, so the file REFUSEs rather than passing",
         SYNTH_SCAFFOLD, 3)
    case("a scaffold whose widths contradict the operands is RED",
         SYNTH_SCAFFOLD.replace("> ☐ ☐ ☐ ☐ ☐ ☐ ☐\n> ─", "> ☐ ☐ ☐ ☐ ☐ ☐ ☐ ☐\n> ─"), 2)
    case("control · a zero multiplier digit does not redden the scaffold", SYNTH_ZERO, 3)
    # ...and the zero-digit excuse must not become a blanket amnesty: with a printed digit
    # in a non-zero row, the block is still checked.
    case("seed · zero-digit block still red on a printed-digit conflict",
         SYNTH_ZERO.replace("> ☐ ☐ ☐ ☐ ☐\n", "> ৪ ৩ ৮ ০ ৭\n"), 2)

    # ------------------------------------------------------- P-019 · decimals (CD-074)
    #
    # Ten seeds, both directions. The two that carry the weight are the shifted point and the
    # mirror of the mark: everything else here would have been caught eventually by a human
    # re-reading, and those two would not.
    case("control · exact decimal chains (Fraction, never float)", SYNTH_DEC_OK, 0)
    case("seed · SHIFTED DECIMAL POINT, every digit right -> RED", SYNTH_DEC_SHIFT, 2)
    case("seed · one decimal digit mutated -> RED", SYNTH_DEC_DIGIT, 2)

    # `০.১ + ০.২` is the canonical float trap. On floats it is 0.30000000000000004 and this
    # control would fail; on Fraction it is exactly ০.৩. The control is the proof, not the note.
    exact = evaluate("০.১ + ০.২") == evaluate("০.৩")
    ok = ok and exact
    print(f"[{'PASS' if exact else 'FAIL'}] control · ০.১ + ০.২ is EXACTLY ০.৩ — Fraction, not float")

    # P-019's mine: `_num` must not hand back a de-pointed integer.
    mine = _num("০.৬") is None and _num("৪৫") == 45
    ok = ok and mine
    print(f"[{'PASS' if mine else 'FAIL'}] control · _num refuses a decimal instead of "
          f"silently dropping the point (got {_num('০.৬')!r})")

    # ------------------------------------------------- P-020 · deliberately-wrong (CD-075)
    case("control · ✗-marked block that IS wrong -> CLEAN (the book said so)",
         SYNTH_MARKED_WRONG, 0)
    case("seed · MIRROR — ✗-marked block tidied into the right answer -> RED",
         SYNTH_MARKED_WRONG_TIDIED, 2)
    case("seed · ✓-marked block that does not balance -> RED", SYNTH_MARKED_TRUE_BAD, 2)
    case("control · DECLARED wrong (instruction, no mark) and IS wrong -> CLEAN",
         SYNTH_DECLARED_WRONG, 0)
    case("seed · declared-wrong block tidied into the right answer -> RED",
         SYNTH_DECLARED_WRONG_TIDIED, 2)
    case("control · the declared region ENDS at the rule — a later correct line stays CLEAN",
         SYNTH_DECLARED_SCOPE, 0)

    # A line naming both blocks of one printed item carries both marks; it must lend neither,
    # or the ✓ half inherits the ✗ and a correct row goes red. Found on the live file.
    both = "# অধ্যায় ৫\n\n> `✗` ৪ − ২.৩১ = ২.৩৩ ও `✓` ৪.০০ − ২.৩১ = ১.৬৯\n"
    case("control · one line carrying BOTH ✗ and ✓ lends neither mark", both, 0)

    # and the real extraction on disk, if one is there
    pool = sorted((REPO / "canon/_wip").glob("*/C*_MATH_Source_*.md")) + \
        sorted((REPO / "canon/sources").glob("*/*/C*_MATH_Source_*.md"))
    for f in pool:
        got = run(f, quiet=True)
        good = got != 2
        ok = ok and good
        print(f"[{'PASS' if good else 'FAIL'}] fixture · {f.name} must not be RED")
        mutated = re.sub(r"([০-৯])", lambda m: BN[(BN.index(m.group(1)) + 1) % 10], f.read_text(encoding="utf-8"), count=1)
        if mutated != f.read_text(encoding="utf-8"):
            red = verdict(mutated) == 2
            # A first-digit mutation may land in the header rather than in a worked block, so this
            # is reported, not asserted — an honest MISSED beats a seed that pretends to bite.
            print(f"[{'RED ' if red else 'n/a '}] fixture seed · first digit of {f.name} flipped"
                  f"{'' if red else ' (landed outside a worked block — not a failure of the gate)'}")
    print("-" * 78)
    print(f"SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 2


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "--selftest":
        sys.exit(selftest())
    p = Path(args[0])
    sys.exit(run(p if p.is_absolute() else REPO / args[0]))
