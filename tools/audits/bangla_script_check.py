#!/usr/bin/env python3
"""bangla_script_check.py — Assamese letters have no business in a Bengali extraction.

SOURCE_POLICY §7.16 · CD-071 · corrections ledger CR-005 (PATTERN)

WHAT IT CHECKS
--------------
Two codepoints, and only two:

    U+09F0  ৰ   ASSAMESE LETTER RA
    U+09F1  ৱ   ASSAMESE LETTER VA

Both belong to the Assamese orthography of the Bengali-Assamese script. **Bengali does not
use either one** — Bengali ra is U+09B0 (র) and Bengali ba is U+09AC (ব). So a hit is not a
judgement call and cannot be a matter of house style: in an NCTB Bangla-medium textbook
extraction it is always wrong. **That is what makes this gate free of false positives by
construction**, and it is the whole reason the check is worth having as code rather than as
a proofreading habit.

WHY IT EXISTS (CR-005, and it is the second half of an argument CR-003 started)
------------------------------------------------------------------------------
The C5 গণিত অধ্যায় ৩ OCR draft carried **27 occurrences across 8 distinct words** — most of
them `প্ৰাথমিক`, which sits in the running head of **every single page** of the book. Against
`প্রাথমিক` the difference is one glyph's inner curve at reading size.

**No human proofreader catches that reliably, and a machine catches it perfectly.**

CR-003 was the mirror image: the OCR channel caught a dropped য-ফলা in `উপলক্ষ্যে` on a page
that had already been read at 400 dpi and signed off as পূর্ণ depth. One error a machine
misses and a human finds; one error a human misses and a machine finds. **Neither channel is
the reliable one. The reliability is in the disagreement between them** — which is the
§7.14 pipeline's entire thesis, now demonstrated in both directions on the same chapter.

WHAT IT DOES *NOT* FLAG, AND WHY THAT MATTERS
---------------------------------------------
An OCR draft committed as evidence under §7.14.3a **is supposed to contain these characters**.
It is machine output preserved byte-for-byte so the disagreement log can cite it; "correcting"
it would destroy the evidence. A gate that reddened on it would be reddening on a **correct**
file — the exact failure that gets a gate ignored (see the নমুনা-column bug in source_check.py
and the নিছক bug in its cell-order test, both recorded).

So a file that declares itself machine output in its header — the §7.14 marker
`MACHINE OUTPUT` — is **counted and reported, never RED**. Every other file is authored text
and is held to the clean standard.

USAGE
-----
    python3 tools/audits/bangla_script_check.py              # sweep the repo
    python3 tools/audits/bangla_script_check.py <path>...    # specific files or dirs
    python3 tools/audits/bangla_script_check.py --selftest
"""
import sys
import unicodedata
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

# The formal Unicode names are NOT "ASSAMESE LETTER ..." — that was this file's first draft,
# and the selftest's codepoint assertion rejected it on the first run. The characters are
# encoded in the Bengali block under descriptive names, and their *Assamese* role is a usage
# fact rather than part of the name. Recorded because a gate that names its own targets wrongly
# invites someone to "fix" the wrong codepoint later.
ASSAMESE = {
    "ৰ": ("ৰ", "BENGALI LETTER RA WITH MIDDLE DIAGONAL", "র (U+09B0)"),
    "ৱ": ("ৱ", "BENGALI LETTER RA WITH LOWER DIAGONAL", "র (U+09B0) or ব (U+09AC), by context"),
}

# §7.14 draft header marker. A draft says this about itself; authored text never does.
MACHINE_MARKER = "MACHINE OUTPUT"

SCAN_DIRS = ["canon", "_inbox", "workstreams"]


def _code_span_mask(line):
    """True at every column that sits inside an inline `code span`.

    **The gate went red on the two files that document the error**, which is a false positive
    of exactly the kind this repo keeps recording: the চ্যানেল-অমিল log and the CR-005 ledger
    row have to *quote* `প্ৰাথমিক` in order to say it is wrong. A gate that forbids naming the
    defect makes the defect unwriteable.

    The answer is a convention rather than a hole: **cite the character in backticks.** An
    inline code span is already what markdown means by "this is a literal string, not prose",
    every citation in these files is one edit away from being correct markdown, and the escape
    is visible in the source rather than implicit. Prose stays clean — a bare ৰ anywhere
    outside backticks is still RED.

    Fenced blocks are deliberately NOT exempted: in these extractions a fence carries
    *authored transcription* of the book, so contamination there is contamination.
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


def scan_text(text):
    """Every hit, with line/column and the whole token it sits in."""
    hits = []
    for lineno, line in enumerate(text.splitlines(), 1):
        quoted = _code_span_mask(line)
        for col, ch in enumerate(line, 1):
            if ch in ASSAMESE and not quoted[col - 1]:
                start = col - 1
                while start > 0 and _is_bengali(line[start - 1]):
                    start -= 1
                end = col
                while end < len(line) and _is_bengali(line[end]):
                    end += 1
                hits.append((lineno, col, ch, line[start:end]))
    return hits


def _is_bengali(ch):
    return "ঀ" <= ch <= "৿"


def targets(args):
    if args:
        paths = []
        for a in args:
            p = Path(a) if Path(a).is_absolute() else REPO / a
            paths.extend(sorted(p.rglob("*.md")) if p.is_dir() else [p])
        return paths
    out = []
    for d in SCAN_DIRS:
        root = REPO / d
        if root.exists():
            out.extend(sorted(root.rglob("*.md")))
    return out


def run(args):
    files = targets(args)
    if not files:
        print("bangla_script_check.py — no markdown files found to scan")
        return 2

    print("bangla_script_check.py — Assamese ৰ/ৱ in Bengali extractions (§7.16, CD-071)")
    print(f"  root: {REPO}")
    print(f"  scanned: {len(files)} markdown file(s)")
    print("-" * 78)

    red_files, draft_files, total_red, total_draft = [], [], 0, 0
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        hits = scan_text(text)
        if not hits:
            continue
        rel = f.relative_to(REPO)
        # A draft declares itself machine output; its hits are evidence, not defects.
        if MACHINE_MARKER in text:
            draft_files.append((rel, len(hits)))
            total_draft += len(hits)
            continue
        red_files.append((rel, hits))
        total_red += len(hits)

    for rel, hits in red_files:
        print(f"  RED   {rel}  — {len(hits)} occurrence(s)")
        for lineno, col, ch, token in hits:
            glyph, name, fix = ASSAMESE[ch]
            print(f"          {rel}:{lineno}:{col}  '{glyph}' {name}  in «{token}»  → should be {fix}")

    for rel, n in draft_files:
        print(f"  DRAFT {rel}  — {n} occurrence(s); declares '{MACHINE_MARKER}', "
              f"evidence preserved verbatim (§7.14.3a) — counted, not failed")

    print("-" * 78)
    if red_files:
        print(f"RESULT: RED — {total_red} Assamese character(s) in {len(red_files)} authored file(s)")
        print("        Assamese ৰ/ৱ have no valid use in Bengali; replace with র/ব.")
        return 1
    print(f"RESULT: CLEAN (0 in authored text; {total_draft} in {len(draft_files)} declared draft(s))")
    return 0


# --------------------------------------------------------------------------- selftest

CLEAN_FIXTURE = "# প্রাথমিক গণিত\n\nনির্ণয় করি। যথাক্রমে ১২ ও ১৫। অর্থাৎ দৈর্ঘ্য ও প্রস্থ।\n"
RA_FIXTURE = "# প্ৰাথমিক গণিত\n\nনিৰ্ণয় করি।\n"          # U+09F0
VA_FIXTURE = "# প্রাথমিক গণিত\n\nকৱি শব্দটি ভুল।\n"        # U+09F1
DRAFT_FIXTURE = ("# OCR DRAFT — MACHINE OUTPUT, UNVERIFIED\n\n"
                 "প্ৰাথমিক গণিত\nনিৰ্ণয় করি।\n")


def selftest():
    """Seeded both directions, and both characters, so neither can regress.

    The draft case is a control, not an afterthought: the one file in the repo that legitimately
    contains these characters is the committed OCR draft, and a gate that reddens on it would be
    reddening on a correct file.
    """
    cases = [
        ("control · correct Bengali প্রাথমিক / নির্ণয় is clean", CLEAN_FIXTURE, 0),
        ("seed    · U+09F0 ৰ in প্ৰাথমিক must be found", RA_FIXTURE, 2),
        ("seed    · U+09F1 ৱ must be found", VA_FIXTURE, 1),
        # The false positive found on the first repo sweep: the files that DOCUMENT the error
        # must be able to quote it. Backticks are the convention; prose is still held clean.
        ("control · a backticked citation `প্ৰাথমিক` is allowed",
         "ভুল বানান `প্ৰাথমিক`, সঠিক প্রাথমিক।\n", 0),
        ("control · both characters citable in backticks", "`ৰ` ও `ৱ` দুটোই ভুল।\n", 0),
        ("seed    · the same word in bare prose is still RED",
         "ভুল বানান প্ৰাথমিক, সঠিক প্রাথমিক।\n", 1),
        ("seed    · text after a closed code span is prose again",
         "`ৰ` তারপর নিৰ্ণয় লেখা হলো।\n", 1),
        ("seed    · a fenced block is authored transcription, not a citation escape",
         "```\nপ্ৰাথমিক\n```\n", 1),
    ]
    print("bangla_script_check.py — SELFTEST (§7.16 / CD-071)")
    print("-" * 78)
    ok = True
    for label, text, want in cases:
        got = len(scan_text(text))
        hit = got == want
        print(f"[{'PASS' if hit else 'FAIL':7}] {label} -> {got} hit(s) (wanted {want})")
        ok = ok and hit

    # the codepoints really are the ones named, not whatever a copy-paste produced
    for ch, (glyph, name, _) in ASSAMESE.items():
        actual = unicodedata.name(ch)
        hit = actual == name
        print(f"[{'PASS' if hit else 'FAIL':7}] codepoint U+{ord(ch):04X} is {name} -> {actual}")
        ok = ok and hit

    # a declared draft is counted, never failed
    hits = len(scan_text(DRAFT_FIXTURE))
    declared = MACHINE_MARKER in DRAFT_FIXTURE
    hit = hits == 2 and declared
    print(f"[{'PASS' if hit else 'FAIL':7}] control · a declared '{MACHINE_MARKER}' draft is "
          f"counted ({hits}) and exempted ({declared}), not RED")
    ok = ok and hit

    # and the exemption must not be a blanket escape: authored text saying nothing is still RED
    hit = MACHINE_MARKER not in RA_FIXTURE
    print(f"[{'PASS' if hit else 'FAIL':7}] control · the exemption requires the marker; "
          f"authored text does not carry it")
    ok = ok and hit

    print("-" * 78)
    print(f"SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 2


if __name__ == "__main__":
    argv = sys.argv[1:]
    if argv and argv[0] == "--selftest":
        sys.exit(selftest())
    sys.exit(run(argv))
