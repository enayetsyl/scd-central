#!/usr/bin/env python3
"""source_check.py — executes SOURCE_POLICY.md §5 against a source extraction.

SOURCE_POLICY §6 recorded that §5 had no executing script: "It is written when the
first extraction under this policy is built." This is that script.

The four §5 conditions, one check each, plus one the §7 amendments added:

  1. RANGE   every chapter/unit in the stated range is present as a section
  2. SLOTS   every spine slot for the class-subject is cross-referenced, or
             explicitly marked absent
  3. PAGES   page numbers are monotonic against the recorded offset
  4. SIGNOFF the spot-check sign-off is present in the file header
  5. DEPTH   a single-channel source's sign-off rows are full checks, not samples

Checks 1-3 and 5 are FAIL-able by the agent. Check 4 can only be closed by the Principal
or the teacher, so it reports PENDING, never PASS-by-agent. Exit code is non-zero
unless all of them are PASS, so a PENDING sign-off can never be mistaken for "done".

**The chapter word is not always "Unit".** The first extraction under this policy was
English, so the scope line, the body heading and the selftest seeds were all written
against `Unit N`. C5 Bangla's chapters are `পাঠ N`, and a gate that reads the file's
grammar rather than its content would have failed RANGE and PAGES on a correct
extraction — reporting red for a reason that has nothing to do with the book. Both
words are read now, and the one the file actually uses is echoed in the output so the
reader can see which grammar was matched.

Usage:
    python tools/audits/source_check.py canon/_wip/c5-english/C5_ENG_Source_01.md
    python tools/audits/source_check.py --selftest

The path is given, not assumed: an extraction lives under a `_wip/` folder until the
Principal signs its spot-check off, and only then moves to `canon/sources/<class>/<subject>/`
(AGENTS.md §3). The gate runs identically in both places.
"""

from __future__ import annotations

import re
import argparse
import sys
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
SPINE = {
    "ENG": REPO / "canon/marklogic/MarkLogic_ENG_Spine.md",
    "BAN": REPO / "canon/marklogic/MarkLogic_BAN_Spine.md",
    "MATH": REPO / "canon/marklogic/MarkLogic_MATH_Spine.md",
    "SCI-BGS": REPO / "canon/marklogic/MarkLogic_SCI_BGS_Spine.md",
    # The filename is the subject token, and no file is ever named `C5_SCI-BGS_Source_NN.md`.
    # `parse_subject` reads `C5_BGS_Source_01.md` as `BGS` and `C5_SCI_Source_01.md` as `SCI`,
    # so the combined key matched neither and SLOTS reported "no spine file registered" on
    # thirty-one correct extractions — a gate reporting red for a reason that has nothing to
    # do with the book (the same failure mode §7.17 and the UNIT_RE fix already cost us once).
    # The two subjects share one spine file; that is the spine's shape, not the gate's licence
    # to be unreachable. Both tokens resolve to it. (Principal ruling 2026-08-17.)
    "BGS": REPO / "canon/marklogic/MarkLogic_SCI_BGS_Spine.md",
    "SCI": REPO / "canon/marklogic/MarkLogic_SCI_BGS_Spine.md",
}

BN_DIGITS = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")

# The words a book divides itself into. English units, Bangla পাঠ, Math অধ্যায়. Order
# matters only for the message; a file uses one of them, never two.
#
# **This list has now been wrong twice, once per subject.** CD-051 added `পাঠ` after the
# English-shaped gate failed a correct Bangla extraction on grammar alone; `অধ্যায়` is
# added here after the same thing happened to the first Math extraction — `parse_scope`
# returned None, so RANGE and PAGES both died before reading a word of the book, and the
# header line printed `grammar : —`. The pattern is the point: a gate that hard-codes the
# vocabulary of the subject it was written for reports red on correct work in every subject
# it was not. A new subject whose books divide themselves by some other word belongs here,
# and the failure will look exactly like this one.
UNIT_WORDS = ("Unit", "পাঠ", "অধ্যায়")
UNIT_RE = "(?:" + "|".join(UNIT_WORDS) + ")"


def dg(s: str) -> str:
    """Bengali digits -> ASCII. Extractions carry both by design."""
    return s.translate(BN_DIGITS)


# --------------------------------------------------------------------------- parse

def parse_scope(text: str):
    """Read the '**এই ফাইলের অংশ:**' line -> (units, first_page, last_page, word)."""
    m = re.search(r"\*\*এই ফাইলের অংশ:\*\*(.+)", text)
    if not m:
        return None
    line = dg(m.group(1))
    units = re.search(rf"({UNIT_RE})\s+(\d+)(?:\s*[–-]\s*(\d+))?", line)
    pages = re.search(r"ছাপা পৃষ্ঠা\s*(\d+)\s*[–-]\s*(\d+)", line)
    if not units or not pages:
        return None
    word = units.group(1)
    lo = int(units.group(2))
    hi = int(units.group(3)) if units.group(3) else lo
    return list(range(lo, hi + 1)), int(pages.group(1)), int(pages.group(2)), word


SCHEMA_B_MARK = "## পরিসর"


def schema_of(text: str) -> str:
    r"""`"A"` (the C5_BAN_Source_01–11 shape) or `"B"` (the extraction-prompt shape). CD-185.

    **Two different documents both called "the §5 schema".** Schema A is what this gate was
    written against and what `canon/sources/c5/bangla/C5_BAN_Source_01–11.md` carry:
    `**এই ফাইলের অংশ:**`, `## পৃষ্ঠা-অফসেট`, `## স্পট-চেক সই`, `## MarkLogic স্লট মিলকরণ`.
    Schema B is what the extraction lane has been producing since: `## পরিসর` · `## উৎস-নোট` ·
    `## পাঠ্য` · `## চিত্র-বাহিত লেখা` · `## ⛔ উৎস-সীমা` · `## সই-ছক`.

    **Detection is on `## পরিসর` and nothing else.** A detector that tried to score both shapes
    would eventually call a malformed schema-A file schema-B and judge it by the wrong rules —
    silently, and in the direction that turns a defect into a pass. One unambiguous marker, and
    a file carrying neither stays schema A and fails RANGE by name as it always did.
    """
    return "B" if re.search(r"^## পরিসর\s*$", text, re.M) else "A"


def parse_scope_b(text: str):
    r"""Schema B's `## পরিসর` -> (units, first_page, last_page, word). CD-185.

    The printed folio range is authoritative and the PDF range is split-local — the same rule
    schema A states in its offset table, carried here in the form schema B writes it.
    """
    sec = re.search(r"^## পরিসর.*?(?=^## |\Z)", text, re.M | re.S)
    if not sec:
        return None
    head = re.search(rf"^#\s+.*?({UNIT_RE})\s*(\d+)", dg(text), re.M)
    pages = re.search(r"ছাপা\s*:?\s*(\d+)\s*[–-]\s*(\d+)", dg(sec.group(0)))
    if not head or not pages:
        return None
    word = head.group(1)
    u = int(head.group(2))
    return [u], int(pages.group(1)), int(pages.group(2)), word


def check_range_b(text, scope):
    r"""Schema B states one unit per file, and the title carries it. CD-185."""
    units, _, _, word = scope
    if not re.search(r"^## পাঠ্য\s*$", text, re.M):
        return "FAIL", "no '## পাঠ্য' section — schema B's transcription body is absent"
    return "PASS", f"stated unit {word} {units[0]}; '## পাঠ্য' present"


def check_pages_b(text, scope):
    r"""Schema B's `### ছাপা NN` headings, monotonic and inside the declared range. CD-185.

    Schema A proves the offset from a verified table; schema B declares the printed range and
    heads each page. **The property being checked is the same one** — that the transcription
    walks the book forward and cites no page the file does not cover.
    """
    _, first, last, _w = scope
    heads = [int(x) for x in re.findall(r"^###\s*ছাপা\s*(\d+)", dg(text), re.M)]
    if not heads:
        return "FAIL", "no '### ছাপা NN' page headings in '## পাঠ্য'"
    out = [p for p in heads if not (first <= p <= last)]
    if out:
        return "FAIL", f"page heading(s) outside stated range {first}-{last}: {out}"
    if heads != sorted(heads):
        return "FAIL", f"page headings are not monotonic: {heads}"
    if heads[0] != first or heads[-1] != last:
        return "FAIL", (f"headings run {heads[0]}-{heads[-1]} but the stated range is "
                        f"{first}-{last} — a range wider than the transcription is a silent gap")
    return "PASS", (f"{len(heads)} page heading(s) monotonic and exactly covering "
                    f"{first}-{last}")


def check_signoff_b(text):
    r"""Schema B's `## সই-ছক`. All rows PENDING is the AUTHORED state, not a defect. CD-185.

    §7.9's `নির্মাণাধীন` marker and an all-PENDING সই-ছক are **two different states** and the
    twelve C5 Bangla extractions arrived carrying both. The marker means *transcription
    unfinished, resume here*; সই-ছক PENDING means *transcribed, human sign-off owed*. Conflating
    them held a finished file out of the walk entirely — invisible rather than counted, which is
    CD-152(d)'s failure with the sign reversed.
    """
    m = re.search(r"^## সই-ছক.*?(?=^## |\Z)", text, re.M | re.S)
    if not m:
        return "FAIL", "no '## সই-ছক' section"
    rows = [l for l in m.group(0).splitlines()
            if l.strip().startswith("|") and not re.match(r"^\|[\s\-:|]+\|$", l.strip())]
    rows = [l for l in rows if "পরীক্ষক" not in l]
    if not rows:
        return "FAIL", "'## সই-ছক' has no rows"
    pending = [l for l in rows if "PENDING" in l]
    if pending:
        return "PENDING", (f"{len(pending)} of {len(rows)} সই-ছক row(s) PENDING — human sign-off "
                           f"is the only closing mechanism and no script may close them")
    return "PASS", f"all {len(rows)} সই-ছক row(s) signed"


def parse_offset_table(text: str):
    """Rows of the offset table -> [(pdf_page, printed_folio), ...].

    Scoped to the '## পৃষ্ঠা-অফসেট' section on purpose: an unscoped numeric-row scan
    swallows every other two-column table in the file and reports a phantom
    inconstant offset. Caught by this gate's own first run, 2026-08-09.
    """
    sec = re.search(r"^## পৃষ্ঠা-অফসেট.*?(?=^## |\Z)", text, re.M | re.S)
    if not sec:
        return []
    rows = []
    for line in sec.group(0).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        a, b = dg(cells[0]), dg(cells[1])
        if re.fullmatch(r"\d+", a) and re.fullmatch(r"\d+", b):
            rows.append((int(a), int(b)))
    return rows


# **The rule that survived contact with the repo.** The first attempt demanded half the label's
# words and reddened eleven correct Bangla tables, which write `শব্দার্থ` for `শব্দার্থ লেখা`
# and `মূলভাব` for `কবিতা বা গদ্যের মূলভাব` — faithful abbreviations, not errors. Punishing
# concision is not catching error. What a mapping row must actually satisfy is narrower and
# harder to satisfy by accident:
#
#   * it carries **at least one word** of its own slot's label — so an invented chapter-topic
#     name fails; and
#   * it reads **more like its own slot than like any other** — so a real spine label moved one
#     place along fails, which is exactly the error অধ্যায় ৩ and ৪ carried.
#
# Neither alone is enough. The first misses the shift entirely; the second would accept a row
# that matches nothing at all.
LABEL_FLOOR = 0.0

_STOP = {"ও", "এবং", "বা", "/", "-", "—"}


def _label_tokens(label: str):
    return [t for t in re.split(r"[^\w\u0980-\u09FF]+", label or "")
            if t and t not in _STOP and len(t) > 1]


def _label_score(label: str, row: str) -> float:
    """How much of `label` the row carries, 0..1, tolerant of Bengali inflection.

    A label token counts as present when it and a row token share one as a prefix of the
    other — `উত্তরের` in the spine against `উত্তর` in the row is the same word, and an exact
    match would fail every honestly-written table in the repo.
    """
    lts = _label_tokens(label)
    if not lts:
        return 0.0
    rts = [t for t in re.split(r"[^\w\u0980-\u09FF]+", row) if t]
    hit = 0
    for lt in lts:
        for rt in rts:
            if len(rt) < 2:
                continue
            if lt == rt or (len(lt) >= 3 and rt.startswith(lt)) or (len(rt) >= 3 and lt.startswith(rt)):
                hit += 1
                break
    return hit / len(lts)


def _flat(s: str) -> str:
    """Letters and digits only — emphasis, spacing and punctuation must not decide a match."""
    return re.sub(r"[^\w\u0980-\u09FF]+", "", s or "")


def parse_subject(path: Path):
    m = re.match(r"C(\d)_([A-Za-z\-]+)_Source_", path.name)
    return (m.group(1), m.group(2).upper()) if m else (None, None)


def spine_slots(subject: str):
    f = SPINE.get(subject)
    if not f or not f.exists():
        return None
    return sorted(set(re.findall(r"^### `([A-Z\-]+-[SL]\d\d)`", f.read_text(encoding="utf-8"), re.M)))


def spine_labels(subject: str):
    r"""-> {slot id: the spine's own label}, read from `### \`XXX-Snn\` — <label>`.

    **P-021 (CD-077).** The label is why this function exists. `check_slots` used to ask only
    whether an ID appeared somewhere in the section — and a table in which *every row was
    mislabelled* passed, twice, at the close of অধ্যায় ৩ and ৪. Both named the eleven MATH
    slots as **chapter topics** (`S04 = সাধারণ ভগ্নাংশ`) when the spine defines them as
    **question types** (`S04 = চার প্রক্রিয়ার সমস্যা`); from S05 the whole list was shifted one
    place and S01–S04's names were invented outright. The error propagated by table-copying:
    each chapter's mapping was written from the previous chapter's, and the spine was never
    reopened.

    **Presence is not correctness — that is CD-070's substring-luck failure at the semantic
    level.** `"ছক" in "নিছক"` was true and meant nothing; `MATH-S04 appears in this file` was
    true and meant nothing. Both were a check that could be satisfied by accident.
    """
    f = SPINE.get(subject)
    if not f or not f.exists():
        return None
    out = {}
    for sid, label in re.findall(r"^### `([A-Z\-]+-[SL]\d\d)`\s*[—–-]\s*(.+?)\s*$",
                                 f.read_text(encoding="utf-8"), re.M):
        out[sid] = label.strip()
    return out


# -------------------------------------------------------------------------- checks

def check_range(text, scope):
    units, _, _, word = scope
    missing = [u for u in units if not re.search(rf"^#\s+{word}\s+{u}(?!\d)", dg(text), re.M)]
    if missing:
        return "FAIL", f"stated range {word} {units[0]}-{units[-1]}: no section for {word} " + ", ".join(map(str, missing))
    return "PASS", f"stated range {word} {units[0]}-{units[-1]}: all {len(units)} section(s) present"


def check_slots(text, subject):
    slots = spine_slots(subject)
    if slots is None:
        return "FAIL", f"no spine file registered for subject {subject}"
    m = re.search(r"^## MarkLogic স্লট মিলকরণ.*?(?=^## |\Z)", text, re.M | re.S)
    if not m:
        # CD-185, Principal ruling 2026-08-20 (option (i)). Schema B has no slot section, and
        # §5's requirement — every spine slot cross-referenced or explicitly marked absent — is
        # REAL CONTENT, not schema-A decoration. So it is neither passed nor failed: it is
        # PENDING, the file can never reach GREEN while it is owed, and the debt is counted and
        # named on every run. **A FAIL here would redden twelve finished transcriptions for a
        # section nobody has been asked for yet; a PASS would fabricate a cross-reference that
        # does not exist.** Neither is honest and the middle state already exists.
        if schema_of(text) == "B":
            return "PENDING", (f"schema B carries no '## MarkLogic স্লট মিলকরণ' section; "
                               f"{len(slots)} spine slot(s) for {subject} are neither "
                               f"cross-referenced nor marked absent. OWED, not failed (CD-185)")
        return "FAIL", "no 'MarkLogic স্লট মিলকরণ' section"
    section = m.group(0)
    cited = set(re.findall(r"([A-Z\-]+-[SL]\d\d)", section))
    missing = [s for s in slots if s not in cited]
    if missing:
        return "FAIL", f"{len(missing)} spine slot(s) neither cross-referenced nor marked absent: " + ", ".join(missing)

    # ---- P-021 / CD-077: the row must name the slot the SPINE names, not one it invented.
    #
    # Checked per line, because that is the unit an author actually gets wrong: a whole row is
    # copied from the previous chapter and the ID no longer matches the words beside it. A row
    # is only judged when it carries exactly one slot ID — prose that mentions two slots in one
    # sentence is commentary, not a mapping row, and reddening it would push authors toward
    # writing less explanation rather than more.
    labels = spine_labels(subject) or {}
    wrong = []
    for raw in section.splitlines():
        # **Only table rows are mapping rows.** A prose line that mentions one slot while
        # explaining something is commentary — `C5_ENG_Source_15.md` argues about `ENG-S03`
        # in a sentence above its own table, and judging that sentence as a mapping would
        # push authors toward writing less explanation, which is the opposite of the point.
        if not raw.lstrip().startswith("|"):
            continue
        ids = re.findall(r"([A-Z\-]+-[SL]\d\d)", raw)
        if len(ids) != 1 or ids[0] not in labels:
            continue
        sid = ids[0]
        want = labels[sid]
        if not _label_tokens(want):
            continue
        # **Score the naming cell, not the whole row.** The third cell is free prose, and a
        # one-word spine label will "win" any row that happens to use that word: `BAN-S09`'s
        # row explains *…মূলভাব লেখার মতো **রচনা** নয়*, and `রচনা` is `BAN-S15`'s entire
        # label, so the row read as S15's. The cell that carries the ID is the cell that names
        # the slot; everything after it is commentary.
        cell = raw.strip().strip("|").split("|")[0]
        mine = _label_score(want, cell)
        rival = max(((k, _label_score(v, cell)) for k, v in labels.items() if k != sid),
                    key=lambda kv: kv[1], default=(None, 0.0))
        # **Two conditions, and the second is the one that catches the shift.** The row must
        # look like its own slot (a floor, so an invented name fails) *and* must look more like
        # its own slot than like any other (so a label moved one place along fails even though
        # it is a perfectly real spine label). Either alone is not enough: the floor misses the
        # shift, and the comparison alone would accept a row that matches nothing.
        if mine <= LABEL_FLOOR or mine < rival[1]:
            hint = (f" — it reads as {rival[0]}'s label instead" if rival[1] > mine
                    else " — the row cites the ID but never names the slot")
            wrong.append(f"{sid} (spine: “{want}”){hint}")
    if wrong:
        return "FAIL", (f"{len(wrong)} slot row(s) do not carry the spine's own label — "
                        f"citing the ID is not mapping it (CD-077): " + " · ".join(wrong))
    named = sum(1 for raw in section.splitlines()
                if raw.lstrip().startswith("|")
                and len(re.findall(r"([A-Z\-]+-[SL]\d\d)", raw)) == 1)
    return "PASS", (f"all {len(slots)} {subject} spine slots accounted for; "
                    f"{named} row(s) carry the spine's own label")


def check_pages(text, scope, offset_rows):
    _, first, last, _word = scope
    if len(offset_rows) < 2:
        return "FAIL", "offset table has fewer than 2 verified rows"
    offsets = {p - f for p, f in offset_rows}
    if len(offsets) != 1:
        return "FAIL", f"offset is not constant across verified rows: {sorted(offsets)}"
    offset = offsets.pop()
    folios = [f for _, f in offset_rows]
    if folios != sorted(folios):
        return "FAIL", f"verified folios are not monotonic: {folios}"
    everywhere = [int(x) for x in re.findall(r"\(পৃষ্ঠা\s*(\d+)", dg(text))]
    out = [p for p in everywhere if not (first <= p <= last)]
    if out:
        return "FAIL", f"page reference(s) outside stated range {first}-{last}: {out}"
    inline = [int(x) for x in re.findall(r"\(পৃষ্ঠা\s*(\d+)", dg(transcribed_body(text)))]
    if inline != sorted(inline):
        return "FAIL", f"page references in the transcribed body are not monotonic: {inline}"
    return "PASS", (f"offset constant (+{offset}) over {len(offset_rows)} verified rows; "
                    f"{len(inline)} body refs monotonic within {first}-{last}, "
                    f"{len(everywhere) - len(inline)} commentary/cross-ref refs in range")


RASTER_ONLY = ("টেক্সট-লেয়ারে নেই", "## ছবির ভেতরের লেখা")
RASTER_ROW = ("ছবির", "মানচিত্র", "লেবেল")

# Everything from the first of these headings on is the extraction talking about the book,
# not transcribing it. Kept in step with `source_textcheck.py`'s list of the same name.
COMMENTARY = ("## যেভাবে ছাপা আছে", "## এই ইউনিটে যা নেই", "## এই পাঠে যা নেই",
              "## এই অধ্যায়ে যা নেই",
              "## এই ইউনিটে যে নামগুলো আছে", "## এই পাঠে যে নামগুলো আছে",
              "## এই অধ্যায়ে যে নামগুলো আছে",
              "## MarkLogic স্লট মিলকরণ", "## প্রমাণ", "## সংশ্লিষ্ট নথি")


def transcribed_body(text: str) -> str:
    """The transcription only — commentary and cross-reference cut off.

    The monotonicity rule is about the order the book is transcribed in. Commentary cites
    pages in whatever order the point needs, and a cross-reference table cites them per
    slot, so scanning the whole file made a correct extraction look like it jumped from
    page 5 back to page 1. The English Unit 1 file passed the unscoped version only because
    it happened to put its page numbers in a column rather than in prose — luck, not design,
    and the same class of unscoped-scan error already recorded in `parse_offset_table`.

    The out-of-range half of the check stays global on purpose: a reference to a page the
    file does not cover is wrong wherever it appears.
    """
    cut = min((text.find(h) for h in COMMENTARY if h in text), default=-1)
    return text if cut < 0 else text[:cut]


def check_signoff(text):
    """SOURCE_POLICY §5 sign-off, at the depth CD-048 sets.

    One sampled passage is enough where the machine diff stands as the second and third
    channel — but **artwork-borne text has no second channel at all**, so a file that records
    any must carry its own full-check row. Without this the depth ruling would be a paragraph
    in a policy: the one kind of content nothing else covers would be the one kind nobody was
    obliged to look at.
    """
    m = re.search(r"^## স্পট-চেক সই.*?(?=^---|\Z)", text, re.M | re.S)
    if not m:
        return "FAIL", "no spot-check sign-off section in header"
    block = m.group(0)
    data = [l for l in block.splitlines()
            if l.strip().startswith("|") and not re.match(r"^\|[\s\-:|]+\|$", l.strip())]
    data = [l for l in data if "যাচাই করার অংশ" not in l]
    if not data:
        return "FAIL", "sign-off table has no rows"
    if any(k in text for k in RASTER_ONLY) and not any(
            any(k in l for k in RASTER_ROW) for l in data):
        return "FAIL", ("this extraction records artwork-borne text, which the cross-channel "
                        "check cannot corroborate, but the sign-off table has no full-check "
                        "row for it (CD-048, SOURCE_POLICY §7.5)")
    unsigned = [l for l in data if re.search(r"\|\s*—\s*\|\s*—\s*\|", l)]
    if unsigned:
        return "PENDING", (f"{len(unsigned)} of {len(data)} spot-check row(s) unsigned — "
                           "only the Principal or the teacher can close this")
    return "PASS", f"all {len(data)} spot-check row(s) signed"


SINGLE_CHANNEL = "**যাচাই-চ্যানেল:** একক"
FULL, SAMPLED = "পূর্ণ", "নমুনা"
DEPTH_COL = "গভীরতা"

CHANNEL_MARKER = "**যাচাই-চ্যানেল:**"


def channel_label(text: str) -> str:
    """THREE states, never two. TOOLS-CR-027.

    Was `'single …' if SINGLE_CHANNEL in text else 'dual'` — so a file that declares NOTHING
    fell to the `else` and the header asserted a channel count the file never stated. That is
    TOOLS-CR-026's own sentence (*ABSENCE OF A DECLARATION IS NOT A DECLARATION OF TWO
    CHANNELS*) surviving at a site its scope did not reach, and it printed ABOVE the gate lines,
    where it reads as a settled fact rather than a verdict.

    Keyed on the MARKER, not on the `দুই` spelling: a file carrying the marker with any other
    value has declared something, and this function reports that it declared rather than
    guessing which word it used.
    """
    if SINGLE_CHANNEL in text:
        return "single (§7.4 sampling unavailable)"
    if CHANNEL_MARKER in text:
        return "dual (declared)"
    return "not declared (§7.7, PENDING-P-023)"


def verdict_for(results):
    """The verdict sentence, built FROM `results`. TOOLS-CR-027.

    Was a fixed string naming spot-check sign-off, written when sign-off was the only route
    into PENDING. CD-185 gave SLOTS that route and TOOLS-CR-026 gave it to DEPTH, and the
    sentence was not updated — so `C5_BAN_Source_22.md` printed *spot-check sign-off owed*
    beside `[PASS] SIGNOFF all 7 সই-ছক row(s) signed`, sending a reader after a signature
    already in the file. TOOLS-CR-026(A) fixed exactly this at `run_all.py:226` and left the
    per-file summary carrying the same stale wording.

    THE EXIT-CODE CONTRACT IS UNCHANGED — 2 / 1 / 0. `run_all.py`, the pre-push hook and the
    sentinel read it, and TOOLS-CR-026 ruled widening it deliberately not done. This names the
    causes in the SENTENCE only.
    """
    statuses = [r[1] for r in results]
    if "FAIL" in statuses:
        return "RED — returns to build phase (AGENTS.md §5)", 2
    if "PENDING" in statuses:
        owed = " · ".join(r[0] for r in results if r[1] == "PENDING")
        return f"NOT DONE — mechanical checks pass; PENDING: {owed}", 1
    return "GREEN", 0


# ---- §7.14 (CD-068) + §7.14.2c cell-order (CD-070): the third depth value and its price.
#
# `OCR-corroborated` entered the vocabulary with CD-068 and for one session was enforced by
# nothing. The rows written under it read `OCR-corroborated + পূর্ণ (সংখ্যা)`, and the old
# `FULL not in cell` test passed them **because the string happened to contain পূর্ণ** — a
# substring accident, not a check. A depth value the gate cannot enforce is a depth value the
# file can claim for free, which is the whole failure class CD-020 and CD-057 exist to close.
#
# So the value is now recognised explicitly, and it is not free. A row may claim it only with:
#   (a) NUMERAL_CROP  — the numerals themselves read at 400+ dpi (§7.14.2(a));
#   (b) DISAGREE_LOG  — the file carries the disagreement log the second channel is FOR
#                       (§7.14.3). Claiming OCR corroboration with no log is claiming a
#                       channel that was never run;
#   (c) ORDER_TOKEN   — for any row describing a table/row/cell, a record that cell **order**
#                       was crop-matched, not merely cell value (§7.14.2c, CD-070).
#
# (c) is not hypothetical. On ছাপা ৩৫ the OCR read all eleven numerals of a table correctly
# and **reordered them** — ১২ and ৩৬ drifted to the end of the row. A correct number in the
# wrong cell is as wrong as a misread one, and **no spelling diff will ever catch it**.
OCR_CORROB = "OCR-corroborated"
NUMERAL_CROP = "পূর্ণ (সংখ্যা)"
DISAGREE_LOG = "## চ্যানেল-অমিল"
ORDER_TOKEN = "ক্রমসহ"
CELL_WORDS = ("ছক", "সারি", "ঘর", "কলাম", "কোষ")


def _is_tabular(row_text):
    """Does this sign-off row describe a table, row, cell or column?

    **Substring matching is wrong here, and the selftest caught it on the first run.**
    `"ছক" in "একটি নিছক গদ্য-অনুচ্ছেদ"` is True — নি+ছক — so a plainly non-tabular row was
    being ordered to prove its cell order, and the gate went red on a correct file. That is
    the same failure shape as the নমুনা-in-the-wrong-column bug recorded in `check_depth`,
    and it gets a gate ignored.

    Bengali is agglutinative, so the cell word legitimately carries suffixes — ছকের, ঘরগুলো,
    সারিতে all mean the table. The distinction that holds is **prefix, not substring**: the
    word may grow to the right and still be the same word; a word that merely ends in it
    (নিছক) is a different word. Tokens are split on everything that is not a Bengali or Latin
    letter, so punctuation and the `**` emphasis markers do not defeat the match.
    """
    tokens = re.split(r"[^ঀ-৿A-Za-z]+", row_text)
    return any(t.startswith(w) for t in tokens for w in CELL_WORDS)


def check_depth(text):
    """§7.4's one-sample depth is bought with machine evidence. Where there is none, it
    cannot be bought — so the file must not claim it.

    §7.4 makes its conditions conjunctive and read off an executed run: Section B clean AND
    every word-level disagreement traced. A source whose text layer does not exist cannot
    satisfy either, because `source_textcheck.py` has nothing to run against. C5 Bangla is
    that case — 421 extractable characters in 142 pages, all glyphs drawn as outlines — and
    the Principal ruled full-eye depth for the whole book on 2026-08-09.

    A file declares its channel count in the header. If it declares single-channel, every
    sign-off row must say `পূর্ণ` and none may say `নমুনা`. Without this the ruling would
    live only in prose: the extraction could carry one sampled row, pass every other check,
    and nothing would notice that the depth it claimed was the depth its evidence could not
    support. The dual-channel case is left alone — §7.4 governs it and the machine diff is
    what earns the reduction there.
    """
    if SINGLE_CHANNEL not in text:
        # TOOLS-CR-026 (Principal ruling 2026-08-20). THIS BRANCH USED TO RETURN PASS AND PRINT
        # "dual-channel source" — a POSITIVE CLAIM THE FILE NEVER MADE. Absence of a declaration
        # is not a declaration of two channels. Measured when the row was filed: of the 43 judged
        # files, 32 carry no declaration — C5 English (legitimately dual-channel under CD-046/047,
        # so the sentence was TRUE BUT UNEARNED) and C5 Bangla ১২–২৩ (the §7.7 book measured at 421
        # extractable characters in 142 pages, so the same inference was FALSE). A gate right by
        # luck on twenty files and wrong on twelve is reporting an inference as a reading in both.
        #
        # PENDING rather than a corrected PASS, because PENDING-P-023(b) asks for a disabled check
        # to be visible IN THE VERDICT, not only in its sentence. This is CD-185's mechanism: the
        # file cannot reach GREEN while the declaration is owed, and the debt is counted and named.
        return "PENDING", (f"no `{SINGLE_CHANNEL}` declaration — CHANNEL COUNT NOT ESTABLISHED, so "
                           f"depth is NOT JUDGED here. This is not a pass: §7.7 requires the header to "
                           f"declare the source class, and a file that declares nothing is not thereby "
                           f"dual-channel (TOOLS-CR-026, PENDING-P-023)")
    m = re.search(r"^## স্পট-চেক সই.*?(?=^---|\Z)", text, re.M | re.S)
    if not m:
        return "FAIL", "declares single-channel but has no sign-off section to check depth in"
    rows = [[c.strip() for c in l.strip().strip("|").split("|")]
            for l in m.group(0).splitlines()
            if l.strip().startswith("|") and not re.match(r"^\|[\s\-:|]+\|$", l.strip())]
    header = next((r for r in rows if "যাচাই করার অংশ" in " ".join(r)), None)
    if header is None:
        return "FAIL", "sign-off table has no header row to locate the depth column in"
    try:
        col = next(i for i, c in enumerate(header) if DEPTH_COL in c)
    except StopIteration:
        return "FAIL", (f"a single-channel source's sign-off table needs a '{DEPTH_COL}' column; "
                        f"columns found: {', '.join(header)}")
    data = [r for r in rows if r is not header and len(r) > col]
    if not data:
        return "FAIL", "declares single-channel but the sign-off table has no rows"
    # **The depth cell, not the whole row.** Scanning the row matched পাঠ ৪'s first entry,
    # "আবেদনপত্রের নমুনা — পুরোটা", where নমুনা is the book's word for its sample letter and
    # has nothing to do with sampling depth. The gate went red on a correct file, which is the
    # failure mode that gets a gate ignored. The word is only a claim about depth when it is in
    # the depth column.
    sampled = [r for r in data if SAMPLED in r[col]]
    if sampled:
        return "FAIL", (f"{len(sampled)} of {len(data)} sign-off row(s) claim '{SAMPLED}' depth on a "
                        f"single-channel source — §7.4's sampling depth needs a clean "
                        f"source_textcheck.py run, which a source with no text layer cannot produce")
    missing = [r for r in data if FULL not in r[col] and OCR_CORROB not in r[col]]
    if missing:
        return "FAIL", (f"{len(missing)} of {len(data)} sign-off row(s) state no depth this policy "
                        f"recognises; a single-channel source needs every row marked '{FULL}' "
                        f"(§7.4/§7.12) or '{OCR_CORROB}' (§7.14.2)")

    ocr_rows = [r for r in data if OCR_CORROB in r[col]]
    if ocr_rows:
        # (b) the log first: without it the claim has no second channel behind it at all.
        if DISAGREE_LOG not in text:
            return "FAIL", (f"{len(ocr_rows)} row(s) claim '{OCR_CORROB}' depth but the file carries "
                            f"no '{DISAGREE_LOG}' section — §7.14.3 makes the disagreement log the "
                            f"thing this source class buys; corroboration with no log is a channel "
                            f"that was never run")
        # (a) numerals are never corroborated by OCR — they are cropped (§7.14.2(a)).
        no_crop = [r for r in ocr_rows if NUMERAL_CROP not in r[col]]
        if no_crop:
            return "FAIL", (f"{len(no_crop)} of {len(ocr_rows)} '{OCR_CORROB}' row(s) do not record "
                            f"'{NUMERAL_CROP}' — §7.14.2(a) crops every numeral at 400+ dpi, and OCR "
                            f"corroboration never extends to digits")
        # (c) cell ORDER, not just cell value (§7.14.2c, CD-070).
        tabular = [r for r in ocr_rows if _is_tabular(" ".join(r))]
        no_order = [r for r in tabular if ORDER_TOKEN not in " ".join(r)]
        if no_order:
            return "FAIL", (f"{len(no_order)} of {len(tabular)} tabular '{OCR_CORROB}' row(s) do not "
                            f"record '{ORDER_TOKEN}' — §7.14.2c (CD-070) requires cell ORDER to be "
                            f"crop-matched, not only cell value; a correct numeral in the wrong cell "
                            f"is invisible to every spelling diff")
        return "PASS", (f"single-channel source; {len(data) - len(ocr_rows)} row(s) '{FULL}', "
                        f"{len(ocr_rows)} row(s) '{OCR_CORROB}' with numeral-crop evidence, "
                        f"{len(tabular)} of those tabular and cell-order-matched; log present")
    return "PASS", f"single-channel source; all {len(data)} sign-off row(s) marked '{FULL}'"


# ----------------------------------------------------------------------------- run

def run(path: Path):
    text = path.read_text(encoding="utf-8")
    cls, subject = parse_subject(path)
    schema = schema_of(text)
    results = []
    if schema == "B":
        scope = parse_scope_b(text)
        if scope is None:
            results.append(("RANGE", "FAIL", "cannot read the '## পরিসর' scope section"))
            results.append(("PAGES", "FAIL", "skipped — scope unreadable"))
        else:
            results.append(("RANGE",) + check_range_b(text, scope))
            results.append(("PAGES",) + check_pages_b(text, scope))
        results.append(("SLOTS",) + check_slots(text, subject))
        results.append(("SIGNOFF",) + check_signoff_b(text))
    else:
        scope = parse_scope(text)
        if scope is None:
            results.append(("RANGE", "FAIL", "cannot read the '**এই ফাইলের অংশ:**' scope line"))
            results.append(("PAGES", "FAIL", "skipped — scope unreadable"))
        else:
            results.append(("RANGE",) + check_range(text, scope))
            results.append(("PAGES",) + check_pages(text, scope, parse_offset_table(text)))
        results.append(("SLOTS",) + check_slots(text, subject))
        results.append(("SIGNOFF",) + check_signoff(text))
    results.append(("DEPTH",) + check_depth(text))
    order = {"RANGE": 0, "SLOTS": 1, "PAGES": 2, "SIGNOFF": 3, "DEPTH": 4}
    results.sort(key=lambda r: order[r[0]])

    print(f"source_check.py — SOURCE_POLICY.md §5")
    print(f"file    : {path.relative_to(REPO)}")
    print(f"subject : class {cls} · {subject}")
    print(f"grammar : chapter word '{scope[3]}'" if scope else "grammar : —")
    print(f"channel : {channel_label(text)}")
    print(f"schema  : {schema} ({'পরিসর / সই-ছক' if schema == 'B' else 'এই ফাইলের অংশ / স্পট-চেক সই'})")
    print("-" * 78)
    for name, status, detail in results:
        print(f"[{status:7}] {name:8} {detail}")
    print("-" * 78)
    verdict, code = verdict_for(results)
    print(f"VERDICT : {verdict}")
    return code


# ------------------------------------------------------------------------ selftest

UNDER_CONSTRUCTION = "**অবস্থা:** নির্মাণাধীন"


def fixture_pool():
    """-> (schema-A controls, নির্মাণাধীন skips, schema-B files). CD-185 added the third.

    Every *finished* extraction on disk, in either half of the pipeline, in any subject.

    Was: the C5 English folders only. That was correct when English was the only extraction
    and wrong the moment Bangla existed — the Bangla-grammar and single-channel seeds have
    nothing to bite on in an English fixture, and a selftest that cannot exercise half the
    gate reports green for checks it never ran.

    **And then "every extraction on disk" met a book too big for one session.** The controls
    assert that an unmutated fixture is not red, which silently assumes every extraction on
    disk is complete. AGENTS.md §3 requires the opposite — work in progress lives in files
    under `_wip/` so a killed session is resumable — so a half-built chapter on disk is the
    normal state, not an anomaly, and it turned the selftest FALSE+ the first time a Math
    chapter was interrupted mid-transcription. A red tool gate for the whole repo, caused by
    a file correctly reporting that it is not finished.

    So a file may **declare itself unfinished**, and a declared-unfinished file is not a
    control: it is not yet a claim about the book. The declaration is explicit, machine-read
    and one string, and `selftest()` prints every file it skipped for it — an extraction can
    be held out of the pool, but it cannot be held out quietly, and it cannot be held out by
    accident. Nothing else changes: `run()` still checks such a file, and still reports it
    red until it is finished and the marker comes out.
    """
    roots = list((REPO / "canon/sources").glob("*/*")) + list((REPO / "canon/_wip").glob("*"))
    out, skipped, schema_b = [], [], []
    for r in roots:
        if not r.is_dir():
            continue
        for f in sorted(r.glob("C*_*_Source_*.md")):
            body = f.read_text(encoding="utf-8")
            if UNDER_CONSTRUCTION in body:
                skipped.append(f)
            elif schema_of(body) == "B":
                # CD-185. Schema B is held out of the schema-A SEED pool on purpose. The ten
                # seeds below mutate schema-A structures — an offset table, a স্লট মিলকরণ row,
                # a `(পৃষ্ঠা N)` inline reference — none of which schema B has. A seed that
                # picked a schema-B fixture would change nothing, report MISSED, and turn the
                # selftest red for a gate that is working. Schema B gets its OWN seeds, on
                # synthetic fixtures, in `schema_b_selftest()`.
                schema_b.append(f)
            else:
                out.append(f)
    return sorted(set(out)), sorted(set(skipped)), sorted(set(schema_b))


DEPTH_FIXTURE = """\
**যাচাই-চ্যানেল:** একক — পূর্ণ যাচাই

## স্পট-চেক সই

| যাচাই করার অংশ | ছাপা পৃষ্ঠা | গভীরতা | সই | তারিখ |
|---|---|---|---|---|
| একটি সাধারণ অংশ, কোনো ছক নয় | ৩১ | পূর্ণ | — | — |
| আমের সংখ্যার এগারোটি ঘর, ক্রমসহ | ৩৫ | OCR-corroborated + পূর্ণ (সংখ্যা) | — | — |
| একটি গদ্য-অনুচ্ছেদ মাত্র | ৩৬ | OCR-corroborated + পূর্ণ (সংখ্যা) | — | — |

---

## চ্যানেল-অমিল

| # | ছাপা | যাচাইকৃত | OCR | বইয়ে | কে ভুল |
|---|---|---|---|---|---|
| ১ | ৩৫ | ক | খ | ক | OCR |
"""


def depth_selftest():
    """§7.14.2 / §7.14.2c seeds — deliberately NOT drawn from the fixture pool.

    The only file carrying `OCR-corroborated` rows is `C5_MATH_Source_03.md`, which declares
    itself নির্মাণাধীন and is therefore excluded from the pool by design (CD-055). Seeding the
    new rules from the pool would report BROKEN today and, worse, would report **green** the
    day that file finishes — a seed whose biting depends on which files happen to be complete
    is the silently-stops-biting failure CD-064(f) recorded. So the fixture is built here, in
    full, and every seed bites every run.
    """
    cases = [
        ("control · a properly evidenced OCR-corroborated file", lambda t: t, "PASS"),
        ("seed · OCR-corroborated with no numeral-crop evidence",
         lambda t: t.replace("OCR-corroborated + পূর্ণ (সংখ্যা)", "OCR-corroborated", 1), "FAIL"),
        ("seed · OCR-corroborated with the disagreement log removed",
         lambda t: t.split("## চ্যানেল-অমিল")[0], "FAIL"),
        ("seed · a tabular OCR-corroborated row with cell ORDER not crop-matched",
         lambda t: t.replace("এগারোটি ঘর, ক্রমসহ", "এগারোটি ঘর", 1), "FAIL"),
        ("seed · a depth value this policy does not recognise",
         lambda t: t.replace("| পূর্ণ |", "| মোটামুটি |", 1), "FAIL"),
        ("seed · সমুনা/নমুনা sampling still refused alongside the new value",
         lambda t: t.replace("| পূর্ণ |", "| নমুনা |", 1), "FAIL"),
        ("control · a non-tabular OCR row needs no order token",
         lambda t: t.replace("আমের সংখ্যার এগারোটি ঘর, ক্রমসহ", "একটি গদ্য-বাক্য", 1), "PASS"),
        # The false positive the first selftest run found: নিছক ends in ছক. A substring test
        # ordered this row to prove cell order it has no cells for. Seeded so it stays fixed.
        ("control · 'নিছক' must not be read as 'ছক' (prefix, not substring)",
         lambda t: t.replace("আমের সংখ্যার এগারোটি ঘর, ক্রমসহ", "একটি নিছক গদ্য-অনুচ্ছেদ", 1), "PASS"),
        # ...and the inflected forms must still bite, or the fix would have bought silence.
        ("seed · inflected 'ছকের' still demands the order token",
         lambda t: t.replace("আমের সংখ্যার এগারোটি ঘর, ক্রমসহ", "ছকের এগারোটি মান", 1), "FAIL"),
        ("seed · inflected 'ঘরগুলো' still demands the order token",
         lambda t: t.replace("আমের সংখ্যার এগারোটি ঘর, ক্রমসহ", "ঘরগুলো মিলিয়ে দেখা", 1), "FAIL"),
        # ---- TOOLS-CR-026: the UNDECLARED branch, seeded BOTH ways because the row named the
        # opposite risk. Removing the declaration must not buy silence, and keeping it must not
        # lose enforcement — a fix that traded a false claim for a gate that says nothing on the
        # case it was built for would be the worse of the two.
        ("seed · TOOLS-CR-026 · the channel declaration REMOVED — PENDING, never PASS: absence of a "
         "declaration is not a declaration of two channels",
         lambda t: t.replace(SINGLE_CHANNEL, "**যাচাই-চ্যানেল-নয়:**", 1), "PENDING"),
        ("seed · TOOLS-CR-026 · control · the declaration PRESENT still reaches enforcement and "
         "still PASSes a clean file — the fix narrowed the claim, it did not silence the gate",
         lambda t: t, "PASS"),
    ]
    print("SELFTEST · §7.14 depth value (CD-070) — synthetic fixture, always bites")
    print("-" * 78)
    ok = True
    for label, mutate, want in cases:
        got = check_depth(mutate(DEPTH_FIXTURE))[0]
        hit = got == want
        print(f"[{'PASS' if hit else 'FAIL':7}] {label} -> {got} (wanted {want})")
        ok = ok and hit
    # and the real file, read straight from disk rather than through the pool
    real = REPO / "canon/_wip/c5-math/C5_MATH_Source_03.md"
    if real.exists():
        got = check_depth(real.read_text(encoding="utf-8"))[0]
        # TOOLS-CR-026: was `got != "FAIL"`, which also passes on PENDING — so the control could
        # not tell ENFORCEMENT RAN AND WAS CLEAN from ENFORCEMENT NEVER RAN. That is P-023(b)'s
        # complaint one level up, inside the control meant to catch it. This file declares `একক`,
        # so PASS is the only correct verdict and anything else is a real regression.
        hit = got == "PASS"
        print(f"[{'PASS' if hit else 'FAIL':7}] control · the live {real.name} must not be RED on DEPTH -> {got}")
        ok = ok and hit
    else:
        print("[BROKEN ] control · C5_MATH_Source_03.md not on disk")
        ok = False
    return ok


def selftest():
    """Seeded-error negative test (handoff §2 evidence rules): a gate that has never
    been shown to go red on a known-bad input has not been shown to do anything.

    Each seed picks the first fixture it can actually change. A seed that changes no fixture
    on disk is BROKEN, not skipped: the artwork-borne-text seed and the single-channel-depth
    seed each only bite on the kind of file they were written for, and reporting them green
    from a fixture that cannot carry them would be the exact silent-pass failure CD-020 was
    written about.
    """
    import tempfile
    pool, skipped, sbfiles = fixture_pool()
    if not pool:
        print("SELFTEST: no finished extraction on disk to mutate — nothing to prove against")
        return 2

    # The seeds are derived from the fixture, not hard-coded against one unit's wording.
    # Hard-coded seeds silently stopped seeding the moment the fixture changed, and a seed
    # that no longer bites reports a green selftest for a gate nobody tested.
    def bump_unit(t):
        # Matched on the untouched text, in either digit set: running dg() over the whole
        # file first would "change" a Bangla fixture even when the seed itself missed, and
        # the did-it-bite guard below would stop guarding.
        return re.sub(rf"^#\s+({UNIT_RE})\s+([0-9০-৯]+)",
                      lambda m: f"# {m.group(1)} {int(dg(m.group(2))) + 40}", t,
                      count=1, flags=re.M)

    def sample_a_full_row(t):
        # Only bites on a single-channel file: flips one full-check row to a sampled one.
        if SINGLE_CHANNEL not in t:
            return t
        return t.replace(f"| {FULL} | — | — |", f"| {SAMPLED} | — | — |", 1)

    def drop_depth_column(t):
        # A single-channel file that simply omits the depth column must not pass by default.
        if SINGLE_CHANNEL not in t:
            return t
        return t.replace(f"| {DEPTH_COL} ", "| ", 1)

    def drop_slot(t):
        # Every occurrence, because the cross-reference may be one grouped row or one row per
        # slot — removing only the first left the table still resolving and the seed toothless.
        return t.replace("S09", "S91")

    # ---- P-021 / CD-077: the two ways a mapping is wrong while every ID is present.

    def shift_slot_labels(t):
        """Move one row's label onto the next slot — the exact error অধ্যায় ৩ and ৪ carried.

        Nothing is missing and nothing is invented; the IDs and the words simply no longer
        correspond. The old check could not see this at all, which is why it shipped twice.
        """
        subj = "MATH" if "MATH" in t or "গণিত" in t else None
        labels = spine_labels(subj) if subj else None
        if not labels:
            return t
        ids = sorted(labels)
        for a, b in zip(ids, ids[1:]):
            la, lb = labels[a], labels[b]
            if la and lb and la in t and lb != la:
                return t.replace(la, lb, 1)
        return t

    def invent_slot_label(t):
        """Replace a mapping ROW's label with a plausible chapter-topic name in no spine.

        Aimed at the table row rather than the first occurrence anywhere: the first attempt hit
        a label mentioned in prose, left the table untouched, and reported MISSED — an honest
        miss, and exactly the kind of toothless seed CD-057 exists to prevent.
        """
        out, done = [], False
        for line in t.splitlines():
            if (not done and line.lstrip().startswith("|")
                    and len(re.findall(r"([A-Z\-]+-[SL]\d\d)", line)) == 1):
                head, sep, rest = line.strip().strip("|").partition("|")
                sid = re.findall(r"([A-Z\-]+-[SL]\d\d)", head)
                if sid and sep:
                    out.append(f"| `{sid[0]}` সংখ্যা ও স্থানীয় মান |{rest}|")
                    done = True
                    continue
            out.append(line)
        return "\n".join(out) if done else t

    def break_offset(t):
        return re.sub(r"^\| (\d+) \| (\d+) \|", lambda m: f"| {m.group(1)} | {int(m.group(2))+1} |",
                      t, count=1, flags=re.M)

    def page_out_of_range(t):
        return re.sub(r"\(পৃষ্ঠা\s*([০-৯\d]+)", lambda m: "(পৃষ্ঠা ৯৯৯", t, count=1)

    def pages_out_of_order(t):
        # Confined to the transcribed body: the last page reference in the file now lives in
        # the cross-reference table, which is deliberately not order-checked, so a seed aimed
        # at the file's last hit would land where nothing is looking and report MISSED.
        hits = list(re.finditer(r"\(পৃষ্ঠা\s*([০-৯\d]+)", transcribed_body(t)))
        if len(hits) < 2:
            return t
        last = hits[-1]
        return t[:last.start()] + "(পৃষ্ঠা ১" + t[last.end():]

    def drop_raster_row(t):
        # Only bites on a file that records artwork-borne text; reported BROKEN otherwise,
        # which is the honest outcome rather than a silent pass.
        return re.sub(r"^\|[^\n]*(ছবির|মানচিত্র|লেবেল)[^\n]*\|\s*—\s*\|\s*—\s*\|\n", "", t,
                      count=1, flags=re.M)

    seeds = [
        ("RANGE  · the stated unit has no section", bump_unit),
        ("SIGNOFF· raster-only content with no full-check row", drop_raster_row),
        ("DEPTH  · a single-channel source claims sampled depth", sample_a_full_row),
        ("DEPTH  · a single-channel source drops the depth column", drop_depth_column),
        ("SLOTS  · one spine slot dropped from the cross-reference", drop_slot),
        ("SLOTS  · every ID present but one label SHIFTED onto the next slot", shift_slot_labels),
        ("SLOTS  · every ID present but one label INVENTED (a chapter topic)", invent_slot_label),
        ("PAGES  · offset broken on one row", break_offset),
        ("PAGES  · in-body page reference outside the stated range", page_out_of_range),
        ("PAGES  · in-body page references out of order", pages_out_of_order),
    ]

    def verdict(p: Path):
        """The same dispatch `run()` makes. CD-185.

        Before this it was schema-A only, so a schema-B fixture would have been judged by rules
        it does not follow and reported FALSE+ — a selftest going red because the gate was
        WIDENED correctly. Kept in step with `run()` deliberately: two dispatchers that can
        disagree is the defect this whole row is about.
        """
        text = p.read_text(encoding="utf-8")
        rs = []
        if schema_of(text) == "B":
            scope = parse_scope_b(text)
            if scope:
                rs.append(check_range_b(text, scope)[0])
                rs.append(check_pages_b(text, scope)[0])
            else:
                rs.append("FAIL")
            rs.append(check_slots(text, parse_subject(p)[1])[0])
            rs.append(check_signoff_b(text)[0])
        else:
            scope = parse_scope(text)
            if scope:
                rs.append(check_range(text, scope)[0])
                rs.append(check_pages(text, scope, parse_offset_table(text))[0])
            else:
                rs.append("FAIL")
            rs.append(check_slots(text, parse_subject(p)[1])[0])
            rs.append(check_signoff(text)[0])
        rs.append(check_depth(text)[0])
        return rs

    print("fixtures:")
    for p in pool:
        print(f"          {p.relative_to(REPO)}")
    for p in skipped:
        print(f"  SKIPPED {p.relative_to(REPO)}  — declares itself নির্মাণাধীন; not a control")
    for p in sbfiles:
        print(f"  SCHEMA-B {p.relative_to(REPO)}  — seeded separately below (CD-185)")
    print("SELFTEST — every seeded error must turn the gate RED")
    print("-" * 78)
    ok = True
    with tempfile.TemporaryDirectory() as d:
        for label, mutate in seeds:
            bit = next(((s, mutate(s.read_text(encoding="utf-8"))) for s in pool
                        if mutate(s.read_text(encoding="utf-8")) != s.read_text(encoding="utf-8")),
                       None)
            if bit is None:
                print(f"[BROKEN ] {label} — seed changed no fixture on disk")
                ok = False
                continue
            src, bad = bit
            p = Path(d) / src.name
            p.write_text(bad, encoding="utf-8")
            red = "FAIL" in verdict(p)
            print(f"[{'RED    ' if red else 'MISSED '}] {label}   ({src.name})")
            ok = ok and red
        # and every unmutated fixture must NOT be red
        for src in pool:
            p = Path(d) / src.name
            p.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
            clean = "FAIL" not in verdict(p)
            print(f"[{'CLEAN  ' if clean else 'FALSE+ '}] control · {src.name} must not be red")
            ok = ok and clean
    print("-" * 78)
    ok = schema_b_selftest() and ok
    print("-" * 78)
    ok = depth_selftest() and ok
    print("-" * 78)
    ok = reporting_selftest() and ok
    print("-" * 78)
    print(f"SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 2


def reporting_selftest():
    """TOOLS-CR-027 — the two reporting surfaces, BOTH DIRECTIONS.

    A fix that silences a false sentence without proving the true one still prints is a waiver.
    So each seed has its negative: the undeclared file must not say `dual` AND the declared one
    must still say `single`; a SIGNOFF-only PENDING must still name sign-off AND a SLOTS/DEPTH
    PENDING must not name it.
    """
    print("REPORTING SELFTEST (TOOLS-CR-027) — channel label and verdict sentence")
    r = []
    r.append(("channel · a file declaring একক still reads single",
              channel_label(f"x {SINGLE_CHANNEL} y").startswith("single")))
    r.append(("channel · a file declaring the marker with another value reads dual DECLARED",
              channel_label(f"x {CHANNEL_MARKER} দুই y") == "dual (declared)"))
    r.append(("channel · a file declaring NOTHING does not read dual — the TOOLS-CR-027 case",
              "dual" not in channel_label("no declaration anywhere in this text")))
    r.append(("channel · and it names its own state rather than going quiet",
              "not declared" in channel_label("no declaration anywhere in this text")))
    only_signoff = [("RANGE", "PASS", ""), ("SLOTS", "PASS", ""),
                    ("SIGNOFF", "PENDING", ""), ("DEPTH", "PASS", "")]
    v, c = verdict_for(only_signoff)
    r.append(("verdict · SIGNOFF-only PENDING still names SIGNOFF", "SIGNOFF" in v and c == 1))
    slots_depth = [("RANGE", "PASS", ""), ("SLOTS", "PENDING", ""),
                   ("SIGNOFF", "PASS", ""), ("DEPTH", "PENDING", "")]
    v, c = verdict_for(slots_depth)
    r.append(("verdict · SLOTS+DEPTH PENDING names both", "SLOTS" in v and "DEPTH" in v))
    r.append(("verdict · and does NOT name SIGNOFF — the live পাঠ ২২ case",
              "SIGNOFF" not in v))
    r.append(("verdict · PENDING still exits 1 — the contract is untouched", c == 1))
    v, c = verdict_for([("RANGE", "FAIL", "")] + slots_depth)
    r.append(("verdict · a FAIL outranks PENDING and still exits 2", c == 2 and "RED" in v))
    v, c = verdict_for([("RANGE", "PASS", ""), ("SLOTS", "PASS", "")])
    r.append(("verdict · all PASS is GREEN and exits 0", c == 0 and v == "GREEN"))
    ok = True
    for label, good in r:
        print(f"  {'PASS' if good else 'FAIL'}  {label}")
        ok = ok and good
    print(f"REPORTING SELFTEST: {'PASS' if ok else 'FAIL'} ({len(r)} cases)")
    return ok


SCHEMA_B_FIXTURE = """\
# C5 বাংলা — পাঠ ৯: একটি সিন্থেটিক পাঠ

## পরিসর

- ছাপা: ১০–১২ (authoritative)
- PDF (split-ফাইল): ১–৩
- PDF (পূর্ণ বই): অজানা

## উৎস-নোট

- সিন্থেটিক ফিক্সচার — কোনো বই থেকে নেওয়া নয় (CD-121(e))।

## পাঠ্য

### ছাপা ১০

একটি বাক্য।

### ছাপা ১১

আরেকটি বাক্য।

### ছাপা ১২

শেষ বাক্য।

## চিত্র-বাহিত লেখা (raster-only)

এই পাঠে চিত্র-বাহিত লেখা নেই।

## ⛔ উৎস-সীমা

1. সিন্থেটিক — কোনো প্রকৃত সীমা নেই।

## সই-ছক

| অংশ | পাতা | পরীক্ষক | তারিখ | অবস্থা |
|---|---|---|---|---|
| ## পাঠ্য | ছাপা ১০–১২ | | | PENDING |
"""


def schema_b_selftest():
    r"""CD-185. Schema B judged in BOTH directions, on a synthetic fixture.

    The seeds below are what makes the widening a gate rather than a waiver. **Widening a gate
    to admit a shape it used to reject is the single easiest way to build a waiver by accident**
    — the files stop being red and nobody checks whether anything is still being checked. So
    every schema-B check is seeded red, and the unmutated fixture is proved NOT red.

    `SLOTS` and `SIGNOFF` are PENDING by ruling, not PASS: the controls assert exactly that,
    because a PENDING that quietly became a PASS would be invisible in the suite's green line.
    """
    import tempfile
    print("SCHEMA-B SELFTEST (CD-185) — synthetic fixture, both directions")
    results = []

    def judge(text):
        rs = {}
        scope = parse_scope_b(text)
        rs["RANGE"] = check_range_b(text, scope)[0] if scope else "FAIL"
        rs["PAGES"] = check_pages_b(text, scope)[0] if scope else "FAIL"
        rs["SLOTS"] = check_slots(text, "BAN")[0]
        rs["SIGNOFF"] = check_signoff_b(text)[0]
        return rs

    f = SCHEMA_B_FIXTURE

    # --- detection, first: everything below is meaningless if the file is judged as schema A.
    results.append(("detector · the fixture is recognised as schema B", schema_of(f) == "B"))
    results.append(("detector · a schema-A file is NOT recognised as schema B",
                    schema_of("**এই ফাইলের অংশ:** পাঠ ১ — ক · ছাপা পৃষ্ঠা ১–৫") == "A"))

    # --- BASELINE. A gate that fires on everything is as useless as one that fires on nothing.
    base = judge(f)
    results.append(("baseline · the unmutated fixture is NOT red", "FAIL" not in base.values()))
    results.append(("baseline · SLOTS is PENDING, not PASS — the debt stays counted",
                    base["SLOTS"] == "PENDING"))
    results.append(("baseline · SIGNOFF is PENDING, not PASS — human sign-off is the only close",
                    base["SIGNOFF"] == "PENDING"))

    # --- RANGE: the transcription body is gone.
    results.append(("RANGE   · '## পাঠ্য' removed",
                    judge(f.replace("## পাঠ্য", "## অন্য কিছু"))["RANGE"] == "FAIL"))

    # --- PAGES: three ways the page headings can lie, and each must be caught separately.
    results.append(("PAGES   · a heading OUTSIDE the stated range",
                    judge(f.replace("### ছাপা ১১", "### ছাপা ৯৯"))["PAGES"] == "FAIL"))
    swapped = f.replace("### ছাপা ১০", "### ছাপা §A§").replace("### ছাপা ১২", "### ছাপা ১০")
    swapped = swapped.replace("### ছাপা §A§", "### ছাপা ১২")
    results.append(("PAGES   · headings out of order", judge(swapped)["PAGES"] == "FAIL"))
    results.append(("PAGES   · the range is WIDER than the transcription — a silent gap",
                    judge(f.replace("ছাপা: ১০–১২", "ছাপা: ১০–১৫"))["PAGES"] == "FAIL"))
    results.append(("PAGES   · no page headings at all",
                    judge(f.replace("### ছাপা", "#### ছাপা"))["PAGES"] == "FAIL"))

    # --- SIGNOFF: the section and its rows.
    results.append(("SIGNOFF · '## সই-ছক' removed",
                    judge(f.replace("## সই-ছক", "## অন্য"))["SIGNOFF"] == "FAIL"))
    results.append(("SIGNOFF · the সই-ছক table has no data rows",
                    judge(f.replace("| ## পাঠ্য | ছাপা ১০–১২ | | | PENDING |\n", ""))
                    ["SIGNOFF"] == "FAIL"))
    # --- and the direction that matters: a SIGNED table must close, or PENDING is permanent.
    signed = f.replace("| ## পাঠ্য | ছাপা ১০–১২ | | | PENDING |",
                       "| ## পাঠ্য | ছাপা ১০–১২ | Teacher | 2026-08-20 | SIGNED |")
    results.append(("SIGNOFF · a SIGNED সই-ছক closes to PASS — PENDING is not a dead end",
                    check_signoff_b(signed)[0] == "PASS"))

    # --- SLOTS closes too: a schema-B file that DOES carry the section is judged, not excused.
    withslots = f.replace("## ⛔ উৎস-সীমা",
                          "## MarkLogic স্লট মিলকরণ\n\n| স্লট | পাঠ |\n|---|---|\n"
                          "| `BAN-S01` | অনুপস্থিত |\n\n## ⛔ উৎস-সীমা")
    results.append(("SLOTS   · a schema-B file WITH the section is judged on its content, "
                    "not excused by its schema", check_slots(withslots, "BAN")[0] != "PENDING"))

    ok = True
    for label, good in results:
        print(f"  {'PASS' if good else 'FAIL'}  {label}")
        ok = ok and good
    print(f"SCHEMA-B SELFTEST: {'PASS' if ok else 'FAIL'} ({len(results)} cases)")
    return ok


def _cli(argv=None):
    """TOOLS-CR-017 — argparse, so `--help` REFUSES by name instead of crashing.

    Before this, an unrecognised argument was not rejected: it was carried straight into a path
    operation and died with `FileNotFoundError: '--help'`. **A traceback is not a refusal** — it
    reaches no verdict and says nothing about what the script accepts, which is `SOURCE_POLICY`
    §7.17's line arriving through the argument surface (TOOLS-CR-015's family).

    **The zero-argument and `--selftest` behaviours are UNCHANGED and that is deliberate**: they are
    what `run_all.py` invokes, and this row fixes the argument surface, not the contract. `PATH` is
    optional so a bare call still selftests.
    """
    ap = argparse.ArgumentParser(
        prog="source_check.py",
        description="Executes SOURCE_POLICY.md §5 against a source extraction. "
                    "With no PATH, runs the selftest.")
    ap.add_argument("path", nargs="?", metavar="PATH",
                    help="a source extraction .md to judge; relative paths resolve against the repo root")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the instrument on synthetic seeds and exit (the default with no PATH)")
    args = ap.parse_args(argv)
    if args.selftest or args.path is None:
        return selftest()
    target = Path(args.path)
    return run(target if target.is_absolute() else REPO / target)


if __name__ == "__main__":
    sys.exit(_cli())
