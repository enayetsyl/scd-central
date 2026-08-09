#!/usr/bin/env python3
"""source_textcheck.py — cross-channel check for a source extraction.

SOURCE_POLICY §7.3 permits a PDF's text layer as "a disagreement-hunting second channel,
never as a source". This script is that channel, executed.

The extraction is transcribed by eye from the rasterised page. That is the authority, and it
is also the one step in the pipeline with no machine check on it — a dropped line or a mis-read
word looks exactly like a correct one. So: decode the (untrustworthy) text layer independently
and make the two channels disagree out loud. Neither is trusted.

What this does NOT do: it never corrects the extraction, and a text-layer reading never
overrules the raster (SOURCE_POLICY §7.3). Every disagreement it prints is for human eyes.

What the C5 English book's text layer actually does — every line below read off the stream and
checked against the printed page, none of it assumed:

  1. **Three encodings coexist.** Plain Latin; a subset shifted **+29** (`:KDW` is `What`,
     `\RX` is `you`); and a display subset shifted **−29** (`a^fiv kbtp` is `DAILY NEWS`).
     A token is one font run, so all three readings are scored per token and the most
     English-looking wins — see `englishness()` for why counting lowercase letters is not
     enough to pick between them.
  2. **The control range is data, not noise.** In the +29 subset a space is 0x03, a comma
     0x0F, a full stop 0x11, and **the digits 0-9 are 0x13-0x1C**. Stripping control bytes
     before decoding — which this script did in its first version — deleted every number in
     the shifted font without saying so.
  3. **Ligatures ride as single high glyphs** outside the shift range: `¿`=fi, `À`=fl,
     `൵`=ff, `൶`=ffi, `µ`/`¶`=the curly quotes.

Because spaces are unreliable, the channels are compared as **letters, not words**: every
extraction word must appear somewhere in the decoded stream, and every long stretch of the
decoded stream must be spoken for by extraction words. Punctuation noise leaves 1-2 character
gaps, well under the reporting threshold; a dropped sentence leaves a long one.

Usage:
    python tools/audits/source_textcheck.py <extraction.md> <book.pdf> --pages 7-12
    python tools/audits/source_textcheck.py --selftest
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

SHIFT = 29
MIN_WORD = 4      # shorter words match everywhere by accident
GAP = 8           # unexplained run in the text layer worth a human eye

# Running heads, folio furniture and the year block repeat on every page and are deliberately
# not transcribed into the extraction body. They are **added to the walker's dictionary**, not
# deleted from the stream: deleting them was eating real words — `unit` inside `United Nations`,
# and `englishfortoday` inside a unit that quotes the book's own title on the page.
FURNITURE = ["englishfortoday", "nationalcurriculumandtextbookboard", "unit", "2026"]


# Glyphs the shifted subsets carry outside the shift range. Every entry below was read off
# this book's own stream and checked against the printed page — an earlier version of this
# table was written from plausible guesses, and two of its three rows were wrong, which is
# exactly the failure this whole script exists to catch. Verified: `EX൵DOR` is buffalo,
# `2൶FH` is Office, `¿QG` is find, `ÀRZHUV` is flowers, `µJDQM¶` is 'ganj'.
LIGATURES = {"¿": "fi", "À": "fl", "൵": "ff", "൶": "ffi", "µ": "'", "¶": "'"}

VOWELS = set("aeiou")


def shift_by(tok: str, delta: int) -> str:
    """Shift the printable run, expand known ligatures, leave anything else alone.

    The low bytes matter as much as the letters: in the +29 subset a space is 0x03, a comma
    0x0F, a full stop 0x11 and **the digits 0-9 are 0x13-0x1C**. A blanket "strip the control
    bytes" pass — which this script used to do — therefore deleted every number in the shifted
    font before decoding, silently. A missing digit in a transcription is the worst failure
    this channel could fail to see, so the control range is decoded, not discarded.
    """
    out = []
    for c in tok:
        if c in LIGATURES:
            out.append(LIGATURES[c])
            continue
        o = ord(c) + delta
        out.append(chr(o) if 0x20 <= o <= 0x7E else c)
    return "".join(out)


def englishness(s: str) -> tuple[int, int, float]:
    """Rank a candidate reading: **plausible first, then longer, then closer to real English.**

    Counting letters alone is not enough, and neither is counting lowercase. `(UNESCO)` sits
    entirely inside the shift range so no guard can exclude it, and its shifted reading
    ``Erkbp`lF`` is *longer* than the correct one because the brackets turn into letters — the
    check duly reported UNESCO missing from a page it is printed on. What separates them is the
    vowel ratio: real English words sit near 0.4, shift-garbage sits near 0. So an implausible
    reading loses to a plausible one however long it is.

    Only ASCII counts. `µ` is alphabetic to Python — it is MICRO SIGN — and while it is standing
    in for a curly quote it was inflating the undecoded reading's score and winning ties.
    """
    alnum = [c for c in s if c.isascii() and c.isalnum()]
    alpha = [c for c in alnum if c.isalpha()]
    if not alnum:
        return (0, 0, -1.0)
    if not alpha:
        return (1, len(alnum), 0.0)          # pure digits: a legitimate reading
    ratio = sum(c.lower() in VOWELS for c in alpha) / len(alpha)
    plausible = 1 if 0.20 <= ratio <= 0.60 else 0
    return (plausible, len(alnum), -abs(ratio - 0.40))


DICT_PATH = Path("/usr/share/hunspell/en_US.dic")


def load_dictionary() -> set[str]:
    """A neutral English word list — deliberately NOT the extraction's own words.

    Scoring candidates against the extraction would make this check circular: it would
    "confirm" whatever the extraction happened to say. The system dictionary knows nothing
    about this book, so agreement between it and the raster transcription means something.

    Required, not optional. Repo precedent: tools/hub-export/SMOKE.md records `jsonschema`
    the same way. On Ubuntu: `apt-get install hunspell-en-us`.
    """
    if not DICT_PATH.exists():
        sys.exit(f"source_textcheck.py: need an English word list at {DICT_PATH} "
                 f"(apt-get install hunspell-en-us). Refusing to guess without one.")
    stems = set()
    for line in DICT_PATH.read_text(encoding="utf-8", errors="ignore").splitlines()[1:]:
        w = line.split("/")[0].strip().lower()
        if len(w) >= 2 and w.isalpha() and w.isascii():
            stems.add(w)
    # A hunspell .dic is stems plus affix flags, so `added`, `suddenly` and `disasters` are
    # not in it. Without the common inflections the coverage score under-rates the *correct*
    # reading of an ordinary word and a spurious shift wins the tie — which is how `Suddenly,`
    # decoded to `puddenlyI` and reported itself missing.
    forms = set(stems)
    for w in stems:
        forms.update({w + s for s in ("s", "es", "ed", "d", "ing", "ly", "er", "est")})
        if w.endswith("e"):
            forms.update({w[:-1] + s for s in ("ing", "ed")})
        if w.endswith("y"):
            forms.update({w[:-1] + s for s in ("ies", "ied", "ily")})
    return forms


DICT: set[str] = set()
MAXW = 15


def coverage(s: str) -> int:
    """How many letters of a candidate reading are accounted for by real English words.

    Greedy longest-match over each run of letters, because the text layer drops the spaces
    inside a font run: `neighbourhoodtomorrowenjoy` has to segment before it can be judged.
    """
    total = 0
    for chunk in re.findall(r"[a-z]+", s.lower()):
        i = 0
        while i < len(chunk):
            for L in range(min(MAXW, len(chunk) - i), 2, -1):
                if chunk[i:i + L] in DICT:
                    total += L
                    i += L
                    break
            else:
                i += 1
    return total


def decode_token(tok: str) -> str:
    """A token is one font run, so it is decoded whole — but which run it came from is not
    known, and this book uses at least three encodings: plain, +29, and a −29 display subset
    (the p91 masthead `a^fiv kbtp` is `DAILY NEWS`). All three readings are scored and the
    most English one wins.

    The ranking is dictionary coverage first, shape second. Shape alone was not enough and the
    failure was instructive: `tells` is correct as it stands, but its −29 reading `WHOOV` has a
    *better* vowel ratio (0.4 against 0.2), so a shape-only score silently mangled ordinary
    words. Dictionary coverage settles it — `tells` covers 5 letters, `whoov` covers 3.
    Tokens under 3 characters are left alone; they are too short to judge.
    """
    if len(tok) < 3:
        return tok
    whole = best_reading(tok)
    split = decode_runs(tok)
    return split if coverage(split) > coverage(whole) else whole


def best_reading(s: str) -> str:
    """The plain reading is the null hypothesis: **a shift has to earn it.**

    Ties used to be broken on length, and that quietly corrupted ordinary words — a comma in
    the +29 subset decodes to `I`, so `Suddenly,` scored one character longer as `puddenlyI`
    and won. A shift is now accepted only when it explains strictly more English than leaving
    the token alone. The one exception is a token that says nothing either way: if the plain
    reading has no readable letters at all — a run of control bytes, which is how the shifted
    subset writes its digits — then shape decides, because leaving it undecoded is not a
    reading, it is a hole.
    """
    cands = [s, shift_by(s, SHIFT), shift_by(s, -SHIFT)]
    covs = [coverage(c) for c in cands]
    if max(covs) > covs[0]:
        return cands[covs.index(max(covs))]
    return max(cands, key=englishness) if englishness(s)[0] == 0 else s


def decode_runs(tok: str) -> str:
    """Decode a token that mixes font runs, run by run.

    pdftotext does not break a token at a font change, so bold-inside-a-sentence arrives glued:
    `:H\\x03SOD\\\\\\x03football` is "We play " in the +29 subset welded to "football" in the plain
    one. Shifting that as a unit turns `football` into `footb~ll` and the word reads as missing
    from a page it is printed on. Runs are cut at the 0x61 boundary — every +29 byte is at or
    below it, ordinary lowercase is above — and each run is decoded on its own.

    This is offered as an *alternative* reading, not a replacement: the −29 display subset also
    lives in the lowercase range, so splitting there would destroy it. Whichever reading covers
    more real English wins.
    """
    runs, cur, cur_low = [], "", None
    for c in tok:
        low = ord(c) <= 0x61 or c in LIGATURES
        if cur and low != cur_low:
            runs.append(cur)
            cur = ""
        cur, cur_low = cur + c, low
    if cur:
        runs.append(cur)
    out = []
    for r in runs:
        out.append(best_reading(r) if len(r) >= 3 else r)
    return "".join(out)


def letters(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def pdf_stream(pdf: Path, first: int, last: int) -> str:
    out = subprocess.run(["pdftotext", "-f", str(first), "-l", str(last), str(pdf), "-"],
                         capture_output=True, text=True, check=True).stdout
    # Only true layout whitespace becomes a space. The rest of the control range is DATA in
    # the shifted subset (0x03 space, 0x0F comma, 0x11 stop, 0x13-0x1C the digits) and is left
    # for shift_by() to decode.
    out = re.sub(r"[\n\r\t\f\v]", " ", out)
    # Dotted answer leaders and rule lines ("……………", "________") are layout, not text. They
    # decode to long runs of one letter and read as unexplained stretches of the book.
    toks = [t for t in out.split() if not (len(t) >= 4 and len(set(t)) <= 2)]
    return letters(" ".join(decode_token(t) for t in toks))


COMMENTARY = ("## যেভাবে ছাপা আছে", "## এই ইউনিটে যা নেই", "## এই ইউনিটে যে নামগুলো আছে",
              "## MarkLogic স্লট মিলকরণ", "## প্রমাণ")


def extraction_body(md: Path) -> str:
    """The transcribed body only — header, commentary and cross-reference are not the book."""
    text = md.read_text(encoding="utf-8")
    m = re.search(r"^#\s+Unit\s+\d+", text, re.M)
    text = text[m.start():] if m else text
    for heading in COMMENTARY:
        text = re.split(rf"^{re.escape(heading)}", text, maxsplit=1, flags=re.M)[0]
    return text


SCAFFOLD = {"verbatim"}   # words of the extraction's own furniture, not the book's


def extraction_words(md: Path, min_len: int = MIN_WORD) -> list[str]:
    body = re.sub(r"[^A-Za-z0-9\s]", " ", extraction_body(md))
    words = {w.lower() for w in body.split() if len(w) >= min_len and w.isalnum()}
    return sorted(words - SCAFFOLD, key=len, reverse=True)


def unexplained(stream: str, words: list[str]) -> list[tuple[int, str]]:
    """Walk the decoded stream, consuming it with extraction words; report the long gaps."""
    gaps, i, start = [], 0, None
    while i < len(stream):
        hit = next((w for w in words if stream.startswith(w, i)), None)
        if hit:
            if start is not None and i - start >= GAP:
                gaps.append((start, stream[start:i]))
            start = None
            i += len(hit)
        else:
            start = i if start is None else start
            i += 1
    if start is not None and len(stream) - start >= GAP:
        gaps.append((start, stream[start:]))
    return gaps


def run(md: Path, pdf: Path, first: int, last: int) -> int:
    words = extraction_words(md)
    # The gap walker gets the short words too. Without them "do you do in the" reads as a
    # 12-letter hole in the middle of a sentence the extraction transcribed perfectly.
    walker_words = extraction_words(md, min_len=1) + FURNITURE
    stream = pdf_stream(pdf, first, last)
    print("source_textcheck.py — SOURCE_POLICY §7.3 cross-channel check")
    print(f"extraction : {md.relative_to(REPO)}  ({len(words)} distinct words >= {MIN_WORD} letters)")
    print(f"text layer : {pdf.name} pp.{first}-{last}  ({len(stream)} letters, decoded)")
    print("-" * 78)

    absent = [w for w in sorted(words) if w not in stream]
    print(f"A. extraction words not found anywhere in the decoded text layer: {len(absent)}")
    for w in absent[:25]:
        print(f"     {w}")
    if len(absent) > 25:
        print(f"     … and {len(absent) - 25} more")

    gaps = unexplained(stream, walker_words)
    print(f"B. stretches of the text layer no extraction word explains (>= {GAP} letters): {len(gaps)}")
    for pos, seg in gaps[:25]:
        print(f"     at {pos:6d}: {seg[:70]}")
    if len(gaps) > 25:
        print(f"     … and {len(gaps) - 25} more")

    print("-" * 78)
    if not absent and not gaps:
        print("VERDICT : AGREE — the channels account for each other completely")
        return 0
    print("VERDICT : DISAGREE — each line above needs a human eye on the printed page.")
    print("          The raster is the authority; the text layer never overrules it.")
    return 1


def selftest() -> int:
    print("SELFTEST — decoder and gap finder")
    print("-" * 78)
    ok = True
    # Every row below is a real token from this book that an earlier version of the decoder
    # got wrong, plus the controls that must survive untouched.
    for raw, want in [(":KDW\x03GR\x03\\RX\x03GR", "What do you do"),
                      ("QHLJKERXUKRRG", "neighbourhood"),
                      ("ELRJUDSKLHV", "biographies"),
                      ("EX൵DOR", "buffalo"),          # ff ligature
                      ("2൶FH", "Office"),             # ffi ligature
                      ("µJDQM¶", "'ganj'"),      # quote glyphs glued to the token
                      ("¿QG", "find"),                # fi ligature
                      ("\x15\x13\x16\x13", "2030"),        # digits live in the control range
                      ("a^fiv", "DAILY"),                  # the -29 display subset
                      ("(UNESCO)", "(UNESCO)"),            # all-caps must NOT be shifted
                      ("Unit", "Unit"),                    # nor a capitalised ordinary word
                      ("reading", "reading")]:
        got = decode_token(raw)
        good = got == want
        ok = ok and good
        print(f"[{'PASS' if good else 'FAIL'}] decode {raw!r:26} -> {got!r:26} (want {want!r})")

    truth = letters("the crow was looking for water and the crow saw a jar of water")
    full = ["crow", "looking", "water", "jar", "saw", "the", "and"]
    dropped = [w for w in full if w != "looking"]
    caught = bool(unexplained(truth, sorted(dropped, key=len, reverse=True)))
    print(f"[{'PASS' if caught else 'FAIL'}] a dropped word leaves an unexplained gap")
    ok = ok and caught
    clean = not unexplained(truth, sorted(full, key=len, reverse=True))
    print(f"[{'PASS' if clean else 'FAIL'}] control · complete word set leaves no gap")
    ok = ok and clean
    invented = [w for w in ["crow", "spaceship"] if w not in truth]
    print(f"[{'PASS' if invented == ['spaceship'] else 'FAIL'}] an invented word is reported absent")
    ok = ok and invented == ["spaceship"]
    print("-" * 78)
    print(f"SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 2


if __name__ == "__main__":
    DICT = load_dictionary()
    args = sys.argv[1:]
    if not args or args[0] == "--selftest":
        sys.exit(selftest())
    md = Path(args[0]) if Path(args[0]).is_absolute() else REPO / args[0]
    pdf = Path(args[1]) if Path(args[1]).is_absolute() else REPO / args[1]
    lo, hi = (int(x) for x in args[args.index("--pages") + 1].split("-"))
    sys.exit(run(md, pdf, lo, hi))
