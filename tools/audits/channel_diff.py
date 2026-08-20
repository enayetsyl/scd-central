r"""channel_diff.py — the legacy file and the per-chapter extractions, compared word by word.

WHY THIS EXISTS. CD-189 found four wrong words by comparing `canon/marklogic/C5_Bangla_Source_13-23.md`
against `canon/sources/c5/bangla/C5_BAN_Source_NN.md` for the chapters that carry verbatim text on
both sides. Three legacy errors and one extraction error, in opposite directions — NEITHER CHANNEL
IS AUTHORITATIVE (CD-189). The comparison was done by hand, and six ad-hoc sweeps failed doing it
(HANDOFF 2026-08-20 §6). This is that comparison built once, with seeds.

WHAT IT DOES NOT DO. It does not rule. A disagreement is REPORTED with both readings and the
printed page decides (CD-189). It never edits a file. It prints no verdict on which channel is right,
because it has no way to know and the one time a session assumed it did, the assumption was circular.

SCOPE, STATED SO IT CANNOT BE OVERREAD. This compares TWO SPECIFIC CHANNELS: the legacy MarkLogic
file and the per-chapter extraction. `source_textcheck.py` (CD-047) compares a DIFFERENT pair —
raster transcription against the PDF text layer — and under QB-CR-018 establishes nothing here.
Two instruments, two surfaces, neither standing in for the other.

THE THIRD OUTCOME IS THE POINT. Only four of eleven chapters (১৩ · ১৫ · ১৮ · ২০) carry `## পূর্ণ পাঠ`
in the legacy file. The other seven carry summaries someone wrote. For those, THERE IS NOTHING TO
COMPARE — and that is a finding, not a pass. A chapter with no verbatim legacy text is NAMED as
UNCOMPARABLE and counted separately, never folded into the silent set. A tool reporting "no
differences" over a chapter it could not compare is the exact fault this file was built after.
"""

import argparse
import pathlib
import re
import sys
import unicodedata

LEGACY = "canon/marklogic/C5_Bangla_Source_13-23.md"
EXTRACT = "canon/sources/c5/bangla/C5_BAN_Source_{n:02d}.md"

# The legacy file marks a chapter with `# পাঠ NN — title` and its verbatim body with `## পূর্ণ পাঠ`.
# The extraction marks its verbatim body with `## পাঠ্য`. Both were read at source before being
# keyed on here; guessing a heading is how an earlier pass looked up a path that did not exist.
CHAPTER_RE = re.compile(r"^#\s*পাঠ\s*([০-৯]+)\s*—")
LEGACY_BODY = "## পূর্ণ পাঠ"
EXTRACT_BODY = "## পাঠ্য"

BN_DIGITS = {d: str(i) for i, d in enumerate("০১২৩৪৫৬৭৮৯")}


def bn_int(s):
    """`১৩` -> 13. Used ONLY on a chapter number read from a heading, never on an ID capture.

    int-id-ok: a chapter number from a prose heading is a quantity, not a scheme-prefixed ID;
    CD-088(d)(i)'s rule is about IDs whose padding carries meaning (`U09` != `U9`).
    """
    return int("".join(BN_DIGITS.get(c, c) for c in s))


def section(text, heading):
    """The body under `heading`, up to the next same-level `## `. None if the heading is absent.

    Absence returns None rather than an empty string ON PURPOSE: the caller must be able to tell
    'this section is empty' from 'this section does not exist', and a bare '' collapses the two.
    """
    lines = text.split("\n")
    start = None
    for i, line in enumerate(lines):
        if line.strip() == heading:
            start = i + 1
            break
    if start is None:
        return None
    out = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        out.append(line)
    return "\n".join(out)


def legacy_chapters(text):
    """-> {chapter_number: body_text_or_None}. None means the chapter carries no `## পূর্ণ পাঠ`."""
    lines = text.split("\n")
    marks = []
    for i, line in enumerate(lines):
        m = CHAPTER_RE.match(line.strip())
        if m:
            marks.append((i, bn_int(m.group(1))))
    out = {}
    for idx, (start, num) in enumerate(marks):
        end = marks[idx + 1][0] if idx + 1 < len(marks) else len(lines)
        out[num] = section("\n".join(lines[start:end]), LEGACY_BODY)
    return out


def words(text):
    """Bengali word tokens, NFC-normalised, with markdown furniture dropped.

    NFC matters: the same word can be stored as composed or decomposed sequences and compare
    unequal while rendering identically — a difference no reader could see and every reader
    would dismiss as noise, which is how a real finding gets lost in a list of false ones.

    AND NFC DOES NOT CLOSE THE WHOLE GAP, WHICH THIS DOCSTRING SAYS RATHER THAN LETTING A
    READER ASSUME IT DOES. Bengali ড় (U+09DC), ঢ় (U+09DD) and য় (U+09DF) are UNICODE
    COMPOSITION EXCLUSIONS: a file may carry either the precomposed codepoint or the
    ড + ় sequence, the two render identically, and **NFC will not unify them**. Those three
    letters are everywhere in this corpus. If a run reports a difference on a word whose only
    visible distinction is one of them, the reading to make is 'these are the same word stored
    two ways', and the fix belongs upstream in the extraction, not here.
    """
    text = unicodedata.normalize("NFC", text)
    # HEADING LINES ARE SCAFFOLDING, NOT BOOK TEXT. The extraction subdivides its body with
    # `### ছাপা ৬৯` page markers; the legacy file has no such markers. Tokenising them reports
    # `ছাপা` and every page number as extraction-only on EVERY chapter — a wall of false
    # findings that would bury the real ones on first run. Found by the agreeing-channels seed.
    text = "\n".join(l for l in text.split("\n") if not l.lstrip().startswith("#"))
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"[*_#|>\[\]()]", " ", text)
    return [w for w in re.findall(r"[\u0980-\u09FF\u200c\u200d]+", text) if w]


def compare(legacy_body, extract_body):
    """-> (only_in_legacy, only_in_extraction), each a sorted list of (word, count).

    THE TWO SECTIONS ARE NOT THE SAME SURFACE, AND THE COMPARISON IS ASYMMETRIC BECAUSE OF IT.
    The legacy `## পূর্ণ পাঠ` is THE POEM OR PROSE BODY ONLY. The extraction's `## পাঠ্য` is the
    WHOLE CHAPTER — body, exercises, ছক, glossary, page markers. So the legacy body should be a
    SUBSET of the extraction, and only ONE direction carries information:

      LEGACY-ONLY  — a word the legacy channel has and the extraction does not. Either a real
                     transcription gap, or legacy EDITORIAL text that was never book text.
                     THIS IS THE DIRECTION THAT IS READ.
      EXTRACTION-ONLY — expected by construction: every exercise and glossary word lands here.
                     COUNTED AND EXPLAINED, NEVER LISTED, because a list of 161 expected words
                     is how the seven that matter get scrolled past.

    The first live run listed both and buried a real finding — the legacy heading
    `প্রথম ৮ পঙ্‌ক্তি (S01-এর জন্য)` — under 161 lines of correct exercise content. That was a
    check aimed at a different surface than the claim it tested, which is this ledger's own
    recurring family, arriving from the instrument rather than from the data.
    """
    a, b = words(legacy_body), words(extract_body)
    sa, sb = set(a), set(b)
    only_a = sorted((w, a.count(w)) for w in sa - sb)
    only_b = sorted((w, b.count(w)) for w in sb - sa)
    return only_a, only_b


def run(root, chapters=None):
    """-> (rows, errs). Reports; never edits, never rules on which channel is right."""
    root = pathlib.Path(root)
    lp = root / LEGACY
    if not lp.exists():
        return [], ["REFUSE: %s does not exist — the legacy channel cannot be located, and a "
                    "comparison with one channel is not a comparison" % LEGACY]
    legacy = legacy_chapters(lp.read_text(encoding="utf-8", errors="replace"))
    if not legacy:
        return [], ["REFUSE: no `# পাঠ NN —` headings found in %s — the file's shape is not what "
                    "this instrument reads, and returning zero chapters as though the file were "
                    "empty would read as a clean run" % LEGACY]
    rows = []
    for num in sorted(legacy):
        if chapters and num not in chapters:
            continue
        ep = root / EXTRACT.format(n=num)
        lbody = legacy[num]
        if lbody is None:
            rows.append((num, "UNCOMPARABLE-SUMMARY", None, None,
                         "the legacy file carries NO `## পূর্ণ পাঠ` for this chapter — its text is a "
                         "summary someone wrote, so there is nothing to compare and this chapter's "
                         "extraction has never been checked against a second channel"))
            continue
        if not ep.exists():
            rows.append((num, "UNCOMPARABLE-NO-EXTRACTION", None, None,
                         "no per-chapter extraction at %s" % EXTRACT.format(n=num)))
            continue
        ebody = section(ep.read_text(encoding="utf-8", errors="replace"), EXTRACT_BODY)
        if ebody is None:
            rows.append((num, "UNCOMPARABLE-NO-BODY", None, None,
                         "the extraction has no `## পাঠ্য` section"))
            continue
        only_l, only_e = compare(lbody, ebody)
        # The STATE keys on legacy-only ALONE. Extraction-only is expected by construction
        # (see compare()'s docstring) and a chapter is not "differing" for containing its own
        # exercises. It is still carried through and COUNTED, never silently dropped.
        state = "DIFFER" if only_l else "AGREE"
        rows.append((num, state, only_l, only_e, ""))
    return rows, []


def selftest():
    """Both directions, and the third outcome. Synthetic fixtures only (CD-055, CD-121(e))."""
    import tempfile

    cases = []

    def case(label, ok):
        cases.append((label, ok))
        print("  %s  CHANNEL-DIFF   %s" % ("PASS" if ok else "FAIL", label))

    def build(tmp, legacy_text, extracts):
        r = pathlib.Path(tmp)
        (r / "canon/marklogic").mkdir(parents=True, exist_ok=True)
        (r / "canon/sources/c5/bangla").mkdir(parents=True, exist_ok=True)
        (r / LEGACY).write_text(legacy_text, encoding="utf-8")
        for n, body in extracts.items():
            (r / EXTRACT.format(n=n)).write_text(body, encoding="utf-8")
        return r

    LEG_V = "# পাঠ ১৩ — শিরোনাম\n\n## পূর্ণ পাঠ\n\nবনের ধারে ছোট পাখি বসে ছিল\n\n## অন্য\n\nকিছু\n"
    EXT_SAME = "# শিরোনাম\n\n## পাঠ্য\n\n### ছাপা ৬৯\n\nবনের ধারে ছোট পাখি বসে ছিল\n\n## সই-ছক\n\nx\n"
    EXT_DIFF = "# শিরোনাম\n\n## পাঠ্য\n\n### ছাপা ৬৯\n\nবনের ধারে বড় পাখি বসে ছিল\n\n## সই-ছক\n\nx\n"

    with tempfile.TemporaryDirectory() as tmp:
        r = build(tmp, LEG_V, {13: EXT_DIFF})
        rows, errs = run(r)
        row = rows[0]
        found = row[1] == "DIFFER" and any(w == "ছোট" for w, _ in row[2]) \
            and any(w == "বড়" for w, _ in row[3])
        case("fires on: a word present in the legacy channel and absent from the extraction, "
             "and reports BOTH readings rather than choosing one (CD-189: neither is authoritative)",
             found and not errs)

    with tempfile.TemporaryDirectory() as tmp:
        r = build(tmp, LEG_V, {13: EXT_SAME})
        rows, _ = run(r)
        case("stays quiet on: two channels that agree — a diff that fires on agreement is one "
             "an author learns to scroll past", rows[0][1] == "AGREE")

    LEG_S = "# পাঠ ১৪ — শিরোনাম\n\n## মূল তথ্য\n\nএটি একটি সারসংক্ষেপ\n\n## অন্য\n\nকিছু\n"
    with tempfile.TemporaryDirectory() as tmp:
        r = build(tmp, LEG_S, {14: EXT_SAME})
        rows, _ = run(r)
        case("THE LOAD-BEARING SEED — a chapter whose legacy text is a SUMMARY is named "
             "UNCOMPARABLE, not counted as agreeing. Zero differences over a chapter that was "
             "never compared is the fault this instrument was built after",
             rows[0][1] == "UNCOMPARABLE-SUMMARY")

    with tempfile.TemporaryDirectory() as tmp:
        # THE SEED FOR THE ASYMMETRY. The extraction carries the body PLUS its exercises; the
        # legacy file carries the body alone. This must read AGREE, or every chapter differs
        # forever and the state stops meaning anything. Written after the first live run did
        # exactly that on পাঠ ২০ — 161 expected words, seven real ones buried among them.
        ext_extra = EXT_SAME.replace(
            "## সই-ছক", "### অনুশীলনী ১\n\nশূন্যস্থান পূরণ করো ছক দেখে\n\n## সই-ছক")
        r = build(tmp, LEG_V, {13: ext_extra})
        rows, _ = run(r)
        row = rows[0]
        case("stays quiet on: an extraction carrying its own EXERCISES on top of the body — the "
             "legacy body is a SUBSET by construction, so extra extraction content is not a "
             "difference; it is counted (%d here) and not listed" % len(row[3]),
             row[1] == "AGREE" and len(row[3]) > 0)

    with tempfile.TemporaryDirectory() as tmp:
        r = build(tmp, LEG_V, {})
        rows, _ = run(r)
        case("a chapter with verbatim legacy text and NO extraction is named, not skipped",
             rows[0][1] == "UNCOMPARABLE-NO-EXTRACTION")

    with tempfile.TemporaryDirectory() as tmp:
        r = build(tmp, LEG_V, {13: "# শিরোনাম\n\n## সই-ছক\n\nx\n"})
        rows, _ = run(r)
        case("an extraction with no `## পাঠ্য` body is named UNCOMPARABLE rather than compared "
             "against an empty string, which would report every legacy word as missing",
             rows[0][1] == "UNCOMPARABLE-NO-BODY")

    with tempfile.TemporaryDirectory() as tmp:
        r = pathlib.Path(tmp)
        rows, errs = run(r)
        case("a MISSING legacy file REFUSES by name — it does not return zero rows, which would "
             "print as a clean run over a comparison that never happened (SOURCE_POLICY §7.17)",
             not rows and errs and "REFUSE" in errs[0])

    with tempfile.TemporaryDirectory() as tmp:
        r = build(tmp, "# শিরোনাম\n\nকোনো পাঠ নেই\n", {})
        rows, errs = run(r)
        case("a legacy file with NO chapter headings REFUSES — the same refusal from the other "
             "side, because an unreadable shape and an empty file are different facts",
             not rows and errs and "REFUSE" in errs[0])

    with tempfile.TemporaryDirectory() as tmp:
        # `ছোট` carries ো (U+09CB), which decomposes to ে + া and RECOMPOSES under NFC.
        # Two earlier fixture words asserted nothing: `পাখি` has no decomposition at all, and
        # `বড়` looked right but ড়/ঢ়/য় are UNICODE COMPOSITION EXCLUSIONS — see the note in
        # `words()`. A seed that cannot fail is not a seed, and this one is asserted before use.
        assert unicodedata.normalize("NFD", "ছোট") != "ছোট", "the fixture word must decompose"
        leg = LEG_V
        ext = EXT_SAME.replace("ছোট", unicodedata.normalize("NFD", "ছোট"))
        r = build(tmp, leg, {13: ext})
        rows, _ = run(r)
        case("NFC control · the same word stored DECOMPOSED on one side does NOT report as a "
             "difference — an invisible normalisation artefact would bury the real findings",
             rows[0][1] == "AGREE")

    ok = all(c[1] for c in cases)
    print("SELFTEST RESULT: %s (%d cases)" % ("PASS" if ok else "FAIL", len(cases)))
    return ok


def main():
    ap = argparse.ArgumentParser(
        description="Compare the legacy MarkLogic file against the per-chapter extractions, "
                    "word by word, and REPORT. Rules nothing; edits nothing.")
    ap.add_argument("--root", default=".", help="repo root (default: .)")
    ap.add_argument("--chapter", type=int, action="append",
                    help="limit to this chapter number; repeatable")
    ap.add_argument("--selftest", action="store_true", help="run the seeded selftest and exit")
    args = ap.parse_args()

    if args.selftest:
        return 0 if selftest() else 1

    print("SELFTEST — the instrument is proven before any verdict (CD-025); synthetic fixtures only")
    if not selftest():
        print("RESULT: REFUSED (selftest failed — no live verdict is offered)")
        return 2
    print()

    rows, errs = run(args.root, set(args.chapter) if args.chapter else None)
    if errs:
        for e in errs:
            print("  " + e)
        print("RESULT: REFUSED")
        return 2

    differ = [r for r in rows if r[1] == "DIFFER"]
    agree = [r for r in rows if r[1] == "AGREE"]
    unc = [r for r in rows if r[1].startswith("UNCOMPARABLE")]

    print("CHANNEL DIFF — %s  vs  %s" % (LEGACY, EXTRACT.format(n=0).replace("00", "NN")))
    print("-" * 78)
    for num, state, only_l, only_e, note in rows:
        if state.startswith("UNCOMPARABLE"):
            print("  %-26s পাঠ %-3d  %s" % (state, num, note))
    print("-" * 78)
    for num, state, only_l, only_e, note in rows:
        if state == "AGREE":
            print("  AGREE                      পাঠ %-3d  every legacy body word is present in the "
                  "extraction  (extraction-only %d, expected)" % (num, len(only_e)))
        elif state == "DIFFER":
            print("  DIFFER                     পাঠ %-3d  LEGACY-ONLY %d  (extraction-only %d, "
                  "expected — exercises/ছক/glossary, not listed)"
                  % (num, len(only_l), len(only_e)))
            for w, c in only_l:
                print("      legacy only      %s  (×%d)" % (w, c))
    print("-" * 78)
    print("CHANNELS: %d differ · %d agree · %d uncomparable · %d chapters"
          % (len(differ), len(agree), len(unc), len(rows)))
    print("NOT A VERDICT ON WHICH CHANNEL IS RIGHT. CD-189 rules that neither file is "
          "authoritative; every disagreement below is settled against the PRINTED PAGE.")
    print("RESULT: REPORTED (%d chapter(s) differ, %d never compared)" % (len(differ), len(unc)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
