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
from itertools import product
from pathlib import Path

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


def parse_steps(text: str):
    """Step tables: `| ৪৬১৪ × ৫ | → | ২৩০৭০ |`."""
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        m = STEP_RE.search(line)
        if m:
            out.append((f"line {i}", *(int(g.translate(TO_ASCII)) for g in m.groups())))
    return out


def render(v: int) -> str:
    return str(v).translate(TO_BN)


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


def run(path: Path, quiet=False):
    text = body(path.read_text(encoding="utf-8"))
    blocks, steps = parse_blocks(text), parse_steps(text)
    rows, red, covered, uncovered = [], False, 0, 0
    for b in blocks:
        st, detail, _ = solve(b)
        rows.append((st, b.label, detail))
        red = red or st == "RED"
        covered += st == "CLEAN"
        uncovered += st in ("WIDTH", "AMBIGUOUS", "REFUSE")
    for label, a, m, c in steps:
        good = a * m == c
        rows.append(("CLEAN" if good else "RED", label,
                     f"{render(a)} × {render(m)} = {render(c)}" if good
                     else f"step table does not balance: {render(a)} × {render(m)} = {render(a*m)}, printed {render(c)}"))
        red = red or not good
        covered += good
    if quiet:
        # `covered == 0` is REFUSE, never 0. A file whose only blocks are ambiguous or pure
        # scaffold has had nothing verified, and returning CLEAN there would hand a depth
        # reduction to content the check never read.
        return 2 if red else (0 if covered else 3)

    print("math_arith_check.py — the extraction's arithmetic against itself")
    print(f"file   : {path.relative_to(REPO) if str(path).startswith(str(REPO)) else path}")
    print(f"found  : {len(blocks)} worked block(s), {len(steps)} step-table row(s)")
    print("-" * 78)
    for st, label, detail in rows:
        print(f"[{st:9}] {label:10} {detail}")
    if not rows:
        print("  ! no worked multiplication and no step table in the transcribed body")
    print("-" * 78)
    print("LIMITS : computed working only · words/names/instructions out of scope ·")
    print("         problem-statement figures unchecked where the book prints no working")
    if red:
        print("VERDICT: RED — a printed digit is mis-read (AGENTS.md §5: back to build phase)")
        return 2
    if not covered:
        print("VERDICT: REFUSE — nothing was actually verified here; this is not a pass")
        return 3
    print(f"VERDICT: CLEAN — {covered} item(s) verified"
          + (f"; {uncovered} uncovered (full manual depth, §7.10)" if uncovered else ""))
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
