#!/usr/bin/env python3
"""gates.py — the question-bank gate suite. ONE suite, two authorities (CD-123).

Run from repo root:
    python workstreams/question-banks/audits/gates.py [bank.json]

WHAT THIS FILE IS
-----------------
The union of two gate lists, merged on the Principal's ruling (CD-123, closing Q-5):

  * `QUESTION_BANK_POLICY.md` v1.0 §5 — the workstream policy, three of whose gates were
    PROMOTED OUT OF THE CORRECTIONS LEDGER (QB-CR-001, QB-CR-003, QB-CR-008).
  * `canon/QUESTION_POLICY.md` v1.0 §6 — canon's eleven rows.

**§6's eleven are the FLOOR, not the ceiling.** QUESTION_POLICY §9 *amends* QB_POLICY §5 rather
than superseding it, and retiring a gate promoted from a correction would un-learn the incident
that produced it. So nothing is deleted — with one ruled exception, below.

THE ONE RETIREMENT
------------------
**DOMAIN-RATIO's per-pool form is RETIRED. Paper level replaces it.** §6 says the ratio is
*"paper level only, never per pool"*; the old §5 form enforced it per pool (HW and AS) and at
chapter total. The two cannot both run, and QUESTION_POLICY §9 amends QB_POLICY §4 exactly there.
The two seeded cases that proved the per-pool form are removed with it; the paper-level gate
carries its own seeds, including two negatives proving it stays quiet on a pool and on a single
class test.

TWO BANK SHAPES, AND NO GATE EVER PASSES BY ACCIDENT
----------------------------------------------------
The two families read different bank shapes — §5's (`pool_index` · `source_extraction`) and §4's
(`header` · `source_index` · `papers`). A gate whose shape a bank does not have reports **`N/A`
with the reason**, never `PASS`. SOURCE_POLICY §7.17: a gate reports or refuses, it never omits.
Four gate NAMES carry one implementation per shape for exactly this reason — MARK-VALUE,
SOURCE-TRACE, SCRIPT-GUARD and TOPIC-NUMBER exist once each and dispatch on the shape in hand.

THE GATES — 21, and where each comes from
------------------------------------------
| Gate | Authority |
|---|---|
| POOL-MEMBERSHIP     | QB_POLICY §5 · **promoted from QB-CR-001** |
| ZERO-OVERLAP        | QB_POLICY §5 (QB-D-001) |
| MARK-VALUE          | **both** — QB_POLICY §5 **promoted from QB-CR-003** · §6 row 1 |
| SOURCE-TRACE        | **both** — QB_POLICY §5 · §6 row 2 |
| SCRIPT-GUARD        | **both** — QB_POLICY §5 · §6 row 3 |
| REF19-SLUG          | §6 row 4 |
| TOPIC-NUMBER        | **both** — QB_POLICY §5 **promoted from QB-CR-008** · §6 row 5 |
| KEY-RUBRIC          | §6 row 6 |
| BLOOM-BAND          | §6 row 7 — CD-121 for the axis (REF-06 §3.6 only; UD-23), **CD-135 for the floor** (pool = lower bounds only; the band is a paper rule) |
| DIFFICULTY          | §6 row 8, as ruled by CD-122 (easy floor only) |
| REPETITION          | §6 row 9 |
| COVERAGE            | §6 row 10, header fallback per §4 (CD-122) |
| DOMAIN-RATIO        | §6 row 11 — **paper level only; the per-pool form is retired** |
| ANSWER-SHAPE        | QB_POLICY §5 |
| RUBRIC-SPECIFICITY  | QB_POLICY §5 |
| FLAG-TRACE          | QB_POLICY §5 (QB-D-012's synthetic-queue rule) |
| QUOTE-VERBATIM      | QB_POLICY §5 (KEEP-AS-IS / PROTECTED) |
| HONORIFIC           | QB_POLICY §5 (extraction, বিশেষ নির্দেশ) |
| AS-MIX              | QB_POLICY §5 (QB-D-004) |
| NUMERALS            | QB_POLICY §5 (LANGUAGE_RULES §2) |
| CEILING             | QB_POLICY §5 (QB-D-002) — REPORT ONLY |

11 from §6 · 14 from §5 · 4 shared names ⇒ **21 gates**.

SELFTEST FIRST, ALWAYS (CD-025). Both families' selftests run before any verdict. Every fixture is
synthetic and written for the test; the §6 family's chapter is a fictional পাঠ ৯৯ that exists in no
book. No file under canon/sources/ or canon/marklogic/ is read as fixture data.

  ⚠ On the fixture rule and its citation: `canon/QUESTION_POLICY.md` §6 cited this as
  "(CD-055, CD-064(f))" and **that citation was false** — corrected at CD-121, which also gives the
  rule a canon home and records the distinction the flat form had flattened: **controls may be
  drawn from the live pool (CD-051(d)); SEEDS may not (QB-D-012).** The seeds here are synthetic.

Exit 0 = CLEAN, 1 = FAIL. Paste output verbatim per AGENTS.md §5.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


# =================================================================================
# CONSTANTS — QUESTION_BANK_POLICY §5 family
# =================================================================================

# MarkLogic_QuestionPolicy.md §৩ — domain mix by class band, +/-৫ points.
DOMAIN_BANDS = {
    1: {"জ্ঞান": 50, "অনুধাবন": 35, "প্রয়োগ": 15, "উচ্চতর": 0},
    2: {"জ্ঞান": 50, "অনুধাবন": 35, "প্রয়োগ": 15, "উচ্চতর": 0},
    3: {"জ্ঞান": 40, "অনুধাবন": 35, "প্রয়োগ": 20, "উচ্চতর": 5},
    4: {"জ্ঞান": 35, "অনুধাবন": 35, "প্রয়োগ": 20, "উচ্চতর": 10},
    5: {"জ্ঞান": 30, "অনুধাবন": 35, "প্রয়োগ": 25, "উচ্চতর": 10},
}

DOMAIN_TOLERANCE = 5.0

# MarkLogic_QuestionPolicy.md §৩ — Bloom to domain.

# MarkLogic_QuestionPolicy.md §৩ — Bloom to domain.
BLOOM_DOMAIN = {
    "Remember": "জ্ঞান",
    "Understand": "অনুধাবন",
    "Apply": "প্রয়োগ",
    "Analyze": "উচ্চতর",
    "Evaluate": "উচ্চতর",
    "Create": "উচ্চতর",
}

# MarkLogic_BAN_Spine.md — C5 per-ITEM marks by slot (not slot totals).

# MarkLogic_BAN_Spine.md — C5 per-ITEM marks by slot (not slot totals).
QB_SPINE_ITEM_MARKS = {
    ("BAN", 5): {"S01": 10, "S02": 1, "S03": 1, "S04": 1, "S05": 1, "S06": 1,
                 "S07": 2, "S08": 5, "S09": 5, "S10": 1, "S11": 1, "S12": 1,
                 "S13": 1, "S14": 5, "S15": 12},
}

# QUESTION_BANK_POLICY.md §2 (QB-D-002) — per-chapter cumulative ceilings.

# QUESTION_BANK_POLICY.md §2 (QB-D-002) — per-chapter cumulative ceilings.
CEILINGS = {"HW": 100, "AS": 50, "CT": 30}

# LANGUAGE_RULES.md §7 — codepoint ranges taken from the validator, not restated from memory.

# LANGUAGE_RULES.md §7 — codepoint ranges taken from the validator, not restated from memory.
ARABIC = re.compile(r"[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]")

ARROWS = re.compile(r"[←-⇿⟰-⟿⤀-⥿]")

EMOJI = re.compile(r"[\U0001F000-\U0001FAFF☀-➿⬀-⯿︀-️]")

WATCH = re.compile(r"[—…]")

ASCII_DIGIT = re.compile(r"[0-9]")

# The extraction's বিশেষ নির্দেশ for পাঠ ২১: the honorific is mandatory everywhere.
# Longest-first: alternation is leftmost-FIRST in Python, so "মহানবি" must precede "নবি"
# or the shorter branch would match inside it. Holes closed after the 2026-08-09 audit:
# bare নবি, হজরত, রসুল, মোহাম্মদ all walked through the original four-branch pattern.

# The extraction's বিশেষ নির্দেশ for পাঠ ২১: the honorific is mandatory everywhere.
# Longest-first: alternation is leftmost-FIRST in Python, so "মহানবি" must precede "নবি"
# or the shorter branch would match inside it. Holes closed after the 2026-08-09 audit:
# bare নবি, হজরত, রসুল, মোহাম্মদ all walked through the original four-branch pattern.
PROPHET = re.compile(r"(মহানবি|মুহাম্মদ|মোহাম্মদ|নবিজি|রাসুল|রসুল|হজরত|নবি)")

HONORIFIC_WINDOW = 30

NEAR_DUP_JACCARD = 0.80

MIN_ANCHOR_TOKENS = 3

MIN_MCQ_OPTIONS = 3


# ---- helpers -------------------------------------------------------------------


# =================================================================================
# CONSTANTS — QUESTION_POLICY §6 family
# =================================================================================

# REF-06 §3.6, "Indicative Bloom's Distribution by Class Group", Class 3–5 row.
# Read at CHAPTER scope per the section's own D-050 note, restated at QUESTION_POLICY §4.
REF06_C3_5 = {
    "Remember": (20, 30), "Understand": (25, 35), "Apply": (25, 35),
    "Analyze": (10, 20), "Evaluate": (0, 10), "Create": (0, 10),
}

# MarkLogic_QuestionPolicy.md §৩ — C5 domain mix, ±৫ points (QUESTION_POLICY §5 quotes the C5
# জ্ঞান figure as "৩০%, ±৫% and no more").

# MarkLogic_QuestionPolicy.md §৩ — C5 domain mix, ±৫ points (QUESTION_POLICY §5 quotes the C5
# জ্ঞান figure as "৩০%, ±৫% and no more").
MARKLOGIC_C5 = {"জ্ঞান": (25, 35), "অনুধাবন": (30, 40), "প্রয়োগ": (20, 30), "উচ্চতর": (5, 15)}

# QUESTION_POLICY §3 row 10 / CD-101 — six Bloom levels stored, four domains derived.

# QUESTION_POLICY §3 row 10 / CD-101 — six Bloom levels stored, four domains derived.
BLOOM_TO_DOMAIN = {
    "Remember": "জ্ঞান", "Understand": "অনুধাবন", "Apply": "প্রয়োগ",
    "Analyze": "উচ্চতর", "Evaluate": "উচ্চতর", "Create": "উচ্চতর",
}

DOMAIN_TO_BLOOM = {"জ্ঞান": ["Remember"], "অনুধাবন": ["Understand"], "প্রয়োগ": ["Apply"],
                   "উচ্চতর": ["Analyze", "Evaluate", "Create"]}

# MarkLogic_BAN_Spine.md — C5 per-ITEM marks by slot (slot TOTALS are a different column;
# QB-CR-003 is the row that establishes the distinction).

# MarkLogic_BAN_Spine.md — C5 per-ITEM marks by slot (slot TOTALS are a different column;
# QB-CR-003 is the row that establishes the distinction).
QP6_SPINE_ITEM_MARKS = {
    ("BAN", 5): {"S01": 10, "S02": 1, "S03": 1, "S04": 1, "S05": 1, "S06": 1, "S07": 2,
                 "S08": 5, "S09": 5, "S10": 1, "S11": 1, "S12": 1, "S13": 1, "S14": 5, "S15": 12},
}

# REF-09 §3, restated at QUESTION_POLICY §4 "Difficulty".

# REF-09 §3, restated at QUESTION_POLICY §4 "Difficulty".
EASY_FLOOR = 30.0

HARD_CEILING = 25.0

# LANGUAGE_RULES.md §7 — codepoint ranges taken from that section's own block, which itself took
# them from the validator rather than restating them from memory.

# LOCKED_QuestionPayload_Schema_v1.json — the allOf discriminator, read at source.
KEY_FIELD_BY_TYPE = {
    "mcq": "options", "true_false": "tf_answer", "fill_blank": "blanks",
    "matching": "pairs", "short_answer": "answer_key", "descriptive": "rubric",
}

# A paper whose domain ratio is testable. §5, last paragraph: "The domain ratio is met across the
# year's tests, not within any single one — 25 marks cannot carry four domains in proportion, so
# there is no per-CT domain gate."

# A paper whose domain ratio is testable. §5, last paragraph: "The domain ratio is met across the
# year's tests, not within any single one — 25 marks cannot carry four domains in proportion, so
# there is no per-CT domain gate."
RATIO_PAPER_KINDS = {"annual", "halfyearly"}


# ---------------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------------


# =================================================================================
# HELPERS — §5 family
# =================================================================================

def qb_norm(s):
    """Normalise a Bengali string for comparison: NFC, collapse space, drop punctuation."""
    s = unicodedata.normalize("NFC", s or "")
    # Markdown emphasis is presentation, not content — strip it so a verbatim quote from the
    # extraction still matches when the source wraps part of it in ** ** (SOURCE-TRACE finding).
    s = re.sub(r"[‘’“”'\"()\[\]।,;:?!—–\-….*_#>|/·]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def qb_tokens(s):
    return set(qb_norm(s).split())

def qb_jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)

def qb_rendered_strings(q):
    """Every string a student or teacher actually reads (LANGUAGE_RULES §7 'rendered text')."""
    out = [q.get("question_text", "")]
    for o in q.get("options", []) or []:
        out += [o.get("text", ""), o.get("why_wrong", "") or ""]
    for b in q.get("blanks", []) or []:
        out += list(b.get("accepted", []) or [])
    for p in q.get("pairs", []) or []:
        out += [p.get("left", ""), p.get("right", "")]
    ak = q.get("answer_key") or {}
    out += list(ak.get("accepted", []) or [])
    if ak.get("model_note"):
        out.append(ak["model_note"])
    for st in ak.get("step_breakdown", []) or []:
        out.append(st.get("step", ""))
    rb = q.get("rubric") or {}
    for c in rb.get("criteria", []) or []:
        out.append(c.get("criterion", ""))
        out += list((c.get("band_descriptors") or {}).values())
    for g in q.get("glossary", []) or []:
        out += [g.get("term", ""), g.get("gloss", "")]
    return [s for s in out if s]

def qb_answer_signature(q):
    """A comparable representation of what the item actually asks the student to produce."""
    qt = q.get("question_type")
    if qt == "mcq":
        return qb_norm(next((o.get("text", "") for o in q.get("options", []) if o.get("is_correct")), ""))
    if qt == "true_false":
        return ""  # a boolean is not a discriminating answer; the stem check does this work
    if qt == "fill_blank":
        return " | ".join(qb_norm((b.get("accepted") or [""])[0]) for b in q.get("blanks", []))
    if qt == "matching":
        return " | ".join(f"{qb_norm(p.get('left'))}={qb_norm(p.get('right'))}" for p in q.get("pairs", []))
    if qt == "short_answer":
        return qb_norm(((q.get("answer_key") or {}).get("accepted") or [""])[0])
    if qt == "descriptive":
        # Descriptive items had NO signature, so all S08 items were exempt from the
        # answer-collision check (2026-08-09 audit). The rubric's content criterion is what
        # an S08 item actually asks for, so that is its signature.
        rb = q.get("rubric") or {}
        return " | ".join(qb_norm(c.get("criterion")) for c in rb.get("criteria", [])
                          if c.get("role") == "content")
    return ""

def qb_resolve_chapter(full, unit):
    """(chapter_text, note) for a RAW captured unit segment. Never calls int() on it.

    CD-130(a). This resolution used to read `str(int(unit))`, and that was CD-088's PATTERN
    sitting inside the suite that judges every bank: `int()` maps `U09` and `U9` to one `৯`, so
    two DISTINCT qids would silently have read one chapter. **The raw string is what gets
    translated** — digit for digit, padding intact — and the section lookup is EXACT.

    The padding ambiguity is then REPORTED, never absorbed. If the qid is zero-padded and the book
    prints its chapter numbers unpadded, the unpadded spelling is tried as a **second, named**
    attempt and the mismatch is printed. **The two spellings stay two spellings.** PENDING-P-034
    has the real defect — three canon artifacts, two padding conventions, no rule anywhere. The
    day that is ruled this fallback becomes either unnecessary or a FAIL; until then, a resolver
    that quietly accepted both would be the thing hiding the evidence that it has to be ruled.

    Pure by design: it takes text, not a path, so its seeds are synthetic strings and need no file
    on disk (CD-121(e) — seeds synthetic, controls may be live).
    """
    exact = qb_chapter_section(full, unit.translate(BN_DIGITS))
    if exact is not None:
        return exact, None
    if unit != unit.lstrip("0"):
        alt = (unit.lstrip("0") or "0").translate(BN_DIGITS)
        loose = qb_chapter_section(full, alt)
        if loose is not None:
            return loose, (f"qid unit segment is `U{unit}` but the extraction prints `পাঠ {alt}` "
                           f"— resolved on the UNPADDED spelling; the two are NOT merged "
                           f"(PENDING-P-034)")
    return full, None


def qb_chapter_section(text, unit_bn):
    """Slice the extraction down to this chapter (headings are '# পাঠ <number>')."""
    m = re.search(rf"^#\s*পাঠ\s*{re.escape(unit_bn)}\b.*?$", text, re.M)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^#\s*পাঠ\s", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


# =================================================================================
# CONSUMPTION EXCLUSION — CD-131, the executor for CD-127(b)
# =================================================================================
# CD-127 split the পাঠ ১২ ruling in two: **extraction PERMITTED, consumption STILL EXCLUDED.**
# That second half lived only as prose in a decision row, and an extracted পাঠ ১২ would have
# passed all 21 gates — it looks exactly like পাঠ ১–১১ to every reader downstream. **A gate is
# the only form of the rule that survives a session which never reads CD-127.**
#
# WHERE THE DECLARATION LIVES, AND WHY IT IS NOT ONLY THE SOURCE FILE'S HEADER
# ---------------------------------------------------------------------------
# The proposed design put the declaration in the extraction's header. **That design cannot cover
# the case it was built for:** পাঠ ১২ has NO extraction, so it has no header. The exclusion has to
# be readable *before* any extraction exists, or the gate is blind exactly while the prohibition
# is doing all of its work.
#
# So the gate reads **any file under `canon/`** carrying the declaration, which today means
# `canon/_wip/c5-bangla/EXCLUDED_paath_12.md` — the file `SOURCE_POLICY` §7.6 and CD-050(b)
# ALREADY name as where this exclusion is recorded. No new home was invented; the existing one was
# made machine-readable, in the HTML-comment form CD-124 already uses for `ledger-prefix`.
#
#     <!-- excluded-from-consumption: subject=BAN class=5 chapter=12 cd=CD-127 -->
#
# ⚠ **The extraction-header half is PROPOSED AND NOT BUILT.** §7.9 set the precedent that a
# machine-read line in an extraction header is a `SOURCE_POLICY` §7 clause carried by a CD row
# (CD-055), not a field a gate may invent. So it is raised, not written. This gate will read it
# the day it exists — the loader already scans every `canon/` file, headers included.

EXCL_MARK = "excluded-from-consumption:"

# Anchored on the qid's own structure. Groups are read as RAW STRINGS and never collapsed —
# CD-088(d)(i) / CD-130. `U012` and `U12` reaching the same exclusion is deliberate and is handled
# on the DECLARATION side below, where widening is safe.
QID_PARTS = re.compile(r"^QP-([A-Z]+)-C([1-5])-U(\d+)")


def _parse_exclusion_line(line):
    """`k=v` pairs after the marker. Split, not captured — deliberately.

    A regex capture here would put this parser's own values under `int_id_check.py`'s taint
    analysis, and `_chapter_tokens` below legitimately calls `zfill` — which is a CD-129(b) sink.
    Parsing by `str.split` keeps the distinction honest rather than waived: **the declaration is
    text we author, not an identifier we read off someone else's data.**
    """
    body = line.split(EXCL_MARK, 1)[1].replace("-->", " ")
    out = {}
    for tok in body.split():
        if "=" in tok:
            k, _, v = tok.partition("=")
            out[k.strip().lower()] = v.strip()
    return out


def _chapter_tokens(value):
    """Every raw spelling of a DECLARED chapter number — `12`, `012`, `0012`.

    Widening here is the safe direction and the opposite of CD-088's failure. CD-088 forbids
    collapsing two IDs *when deciding they are the same*; an exclusion gate is deciding whether to
    REFUSE, so over-matching costs a false refusal and under-matching ships a forbidden question.
    **It fails closed.** And the widening is applied to the declaration, never to a captured id.
    """
    bare = value.lstrip("0") or "0"
    return {value, bare} | {bare.zfill(w) for w in (2, 3, 4)}


def _is_declaration_line(line):
    """A MINT, not a CITATION. Found by this gate's own first live run.

    `CONSUMPTION EXCLUSIONS IN FORCE: 2` — because **CD-131's decision row quotes the declaration
    form**, and the loader counted the quotation. Harmless there (same chapter, same CD) and a real
    defect: a policy clause, a session log or a CD row that shows the form would mint a phantom
    exclusion, and the reverse — a real exclusion created by someone *describing* one.

    **This is AGENTS.md §5.1 exactly** — a gate must not make naming the defect unwriteable — and
    `ledger_check.py` solved the identical mint-vs-cite problem by anchoring on the first cell of a
    table row. The anchor here: **the declaration is the WHOLE LINE.** A row of prose that contains
    it is discussing it; a standalone comment is declaring it.
    """
    s = line.strip()
    return s.startswith("<!--") and s.endswith("-->")


def load_exclusions(root):
    """Every declared consumption exclusion under `canon/`. -> (declarations, errors)."""
    out, errs = [], []
    base = root / "canon"
    if not base.exists():
        return out, [f"canon/ not found at {root} — exclusions could not be read, and an "
                     f"unreadable prohibition is not an absent one"]
    for p in sorted(base.rglob("*.md")):
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError as e:                                          # noqa: PERF203
            errs.append(f"{p.name}: unreadable ({e})")
            continue
        if EXCL_MARK not in text:
            continue
        fenced = False
        for line in text.splitlines():
            if line.lstrip().startswith("```"):
                # A fenced block SHOWS the form; it does not use it. P-035's proposed
                # SOURCE_POLICY clause will certainly print the line in a fence, and a policy
                # that could not quote its own convention would be the §5.1 failure again.
                fenced = not fenced
                continue
            if fenced or EXCL_MARK not in line or not _is_declaration_line(line):
                continue
            d = _parse_exclusion_line(line)
            missing = [k for k in ("subject", "class", "chapter", "cd") if not d.get(k)]
            if missing:
                errs.append(f"{p.relative_to(root).as_posix()}: exclusion declaration is missing "
                            f"{', '.join(missing)} — a prohibition nobody can resolve to a "
                            f"chapter is not a prohibition")
                continue
            d["_file"] = p.relative_to(root).as_posix()
            d["_tokens"] = _chapter_tokens(d["chapter"])
            out.append(d)
    return out, errs


def g_source_exclusion(bank, ctx):
    """SOURCE-EXCLUSION — CD-127(b) / CD-131. No item may source a declared-excluded chapter.

    Shape-independent on purpose: both bank families carry `questions[].qid`, and the qid is where
    the chapter lives. One implementation, both shapes — CD-123's four dual-shape gates exist
    because their DATA differs; this one's does not.
    """
    excl = ctx.get("exclusions")
    if excl is None:
        excl, load_err = load_exclusions(ROOT)
    else:
        load_err = list(ctx.get("exclusion_errors") or [])
    errs, rep = list(load_err), []
    if not excl:
        rep.append("no consumption exclusion is declared anywhere under canon/ — nothing to "
                   "enforce, and that is reported rather than passed silently")
        return errs, rep

    by_sc = {}
    for d in excl:
        by_sc.setdefault((d["subject"].upper(), d["class"]), []).append(d)

    # (1) the bank's whole declared source is an excluded file.
    srcref = (bank.get("source_extraction") or bank.get("extraction_path") or "").split("#")[0]
    for d in excl:
        if srcref and d["_file"] == srcref:
            errs.append(f"the bank's declared source `{srcref}` is itself declared excluded from "
                        f"consumption by {d['cd']} — no item in it can be sourced")

    # (2) per item, off the raw qid segments.
    for q in bank.get("questions", []):
        qid = q.get("qid") or ""
        m = QID_PARTS.match(qid)
        if not m:
            continue
        subject, cls, unit = m.group(1), m.group(2), m.group(3)
        for d in by_sc.get((subject, cls), []):
            if unit in d["_tokens"]:
                errs.append(f"{qid}: sources chapter {d['chapter']} of C{cls} {subject}, which is "
                            f"DECLARED EXCLUDED FROM CONSUMPTION by {d['cd']} "
                            f"({d['_file']}) — extraction may exist; consumption does not")
                break

    rep.append("consumption exclusions in force: " + " · ".join(
        f"{d['subject']}-C{d['class']}-chapter {d['chapter']} ({d['cd']})" for d in excl))
    return errs, rep


# ---- gates ---------------------------------------------------------------------


# =================================================================================
# HELPERS — §6 family
# =================================================================================

def qp_norm(s):
    """NFC, punctuation-stripped, whitespace-collapsed — for verbatim comparison."""
    s = unicodedata.normalize("NFC", s or "")
    s = re.sub(r"[‘’“”'\"()\[\]।,;:?!—–\-….*_#>|/·]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def pct(n, d):
    return 0.0 if not d else 100.0 * n / d

def qp_rendered_strings(q):
    """Every string a student or teacher reads. LANGUAGE_RULES §7's "rendered text" column."""
    out = [q.get("question_text", "")]
    for o in q.get("options") or []:
        out.append(o.get("text", "") if isinstance(o, dict) else str(o))
    for b in q.get("blanks") or []:
        out.append(b.get("answer", "") if isinstance(b, dict) else str(b))
    for p in q.get("pairs") or []:
        if isinstance(p, dict):
            out += [p.get("left", ""), p.get("right", "")]
    if isinstance(q.get("answer_key"), str):
        out.append(q["answer_key"])
    r = q.get("rubric") or {}
    for c in r.get("criteria") or []:
        out.append(c.get("criterion", ""))
        out += list((c.get("band_descriptors") or {}).values())
    return [s for s in out if s]

def metadata_strings(q):
    """Fields §7 explicitly permits →, ⚠ and 🔒 in: "metadata is not what a child sees"."""
    out = []
    for k in ("learning_outcome_ref", "chapter_ref", "lesson_ref", "stimulus_ref", "source_note"):
        v = q.get(k)
        if isinstance(v, str):
            out.append(v)
    return out

def load_ref19_slugs(root):
    """REF-19's slug set, parsed FROM THE LOCKED ARTIFACT.

    CD-011's standing rule: a registry is written from the actual artifact, never from a summary or
    a derived copy. `tools/hub-export/validate_import.py`'s `REF19_SLUGS_DEFAULT` is a derived
    copy — auto-extracted, and QB-CR-007 already recorded that building canon from it would be the
    phantom-content failure CD-026 refused. So this reads the LOCKED file.

    Anchored on BACKTICKS, not on a bare word boundary. Unbackticked matching pulls in
    `DROP-CROSS` and `TGR-BGS` (truncations of a flag name and a task id) and, worse, TRUNCATES
    the two real three-segment Math slugs. Backtick-anchoring is the same reasoning as
    AGENTS.md §5.1's exemption: inline code is markdown's way of saying "literal token".
    """
    p = root / "canon" / "topics" / "LOCKED_REF-19_Vertical_Topic_Progression_Map_v1_10.md"
    if not p.exists():
        return None, f"{p.relative_to(root).as_posix()} is missing — no slug can be validated"
    text = p.read_text(encoding="utf-8", errors="replace")
    slugs = set(re.findall(r"`((?:BAN|ENG|MATH|SCI|BGS)-[A-Z0-9]+(?:-[A-Z0-9]+)*)`", text))
    return slugs, None

def load_topic_numbers(root):
    """canon/topics/TOPIC_NUMBERS.md — CD-044. An unminted number FAILs and is NEVER auto-minted;
    the file's own §17 is the rule: "a number not listed here is not used. It is queued.\""""
    p = root / "canon" / "topics" / "TOPIC_NUMBERS.md"
    if not p.exists():
        return None, f"{p.relative_to(root).as_posix()} is missing — no topic number can be validated"
    text = p.read_text(encoding="utf-8", errors="replace")
    # Only rows of the chart table mint. A `TOP-` string in prose is a citation, not a mint —
    # the same first-cell discipline `tools/audits/ledger_check.py` uses, for the same reason.
    tags = set()
    for line in text.splitlines():
        m = re.match(r"^\|\s*\**\s*`(TOP-[A-Z]+-C[1-5]-\d{2})`", line)
        if m:
            tags.add(m.group(1))
    return tags, None


# ---------------------------------------------------------------------------------
# THE ELEVEN QP6_GATES — one function each, in §6's table order.
# Each returns (errors, report_lines).
# ---------------------------------------------------------------------------------


# =================================================================================
# GATES — §5 family (nothing here is deleted: CD-123)
# =================================================================================

def g_pool_membership(bank, ctx):
    errs = []
    pools = bank.get("pool_index") or {}
    qids = [q.get("qid") for q in bank.get("questions", [])]
    if sorted(pools.keys()) != sorted(CEILINGS.keys()):
        errs.append(f"pool_index keys {sorted(pools.keys())} != the three ruled pools "
                    f"{sorted(CEILINGS.keys())} (QB-D-001: HW/AS/CT, no CW)")
    seen = {}
    for pool, ids in pools.items():
        for qid in ids:
            seen.setdefault(qid, []).append(pool)
    for qid, ps in seen.items():
        if len(ps) > 1:
            errs.append(f"{qid} is in {len(ps)} pools {ps} — a question belongs to exactly one (QB-D-001)")
        if qid not in qids:
            errs.append(f"pool_index lists {qid} but no such question exists in the bank")
    for qid in qids:
        if qid not in seen:
            errs.append(f"{qid} is in no pool — every question must be assigned (QB-D-001)")
    if len(set(qids)) != len(qids):
        errs.append("duplicate qid in the bank — qids are permanent and never reused")
    return errs

def g_zero_overlap(bank, ctx):
    errs = []
    pool_of = ctx["pool_of"]
    qs = bank.get("questions", [])
    for i in range(len(qs)):
        for j in range(i + 1, len(qs)):
            a, b = qs[i], qs[j]
            pa, pb = pool_of.get(a.get("qid")), pool_of.get(b.get("qid"))
            if pa is None or pb is None:
                continue
            where = f"[{pa}] and {b['qid']} [{pb}]" if pa != pb else f"and {b['qid']}, both in [{pa}]"
            sim = qb_jaccard(qb_tokens(a.get("question_text")), qb_tokens(b.get("question_text")))
            if sim >= NEAR_DUP_JACCARD:
                errs.append(f"{a['qid']} {where} have near-identical stems "
                            f"(token overlap {sim:.2f} >= {NEAR_DUP_JACCARD})")
            sa, sb = qb_answer_signature(a), qb_answer_signature(b)
            if sa and sa == sb and a.get("question_type") == b.get("question_type"):
                errs.append(f"{a['qid']} {where} have the identical answer "
                            f"'{sa[:40]}' for the same question_type")
    return errs

def g_qb_mark_value(bank, ctx):
    errs = []
    key = (ctx["subject"], ctx["class_level"])
    table = QB_SPINE_ITEM_MARKS.get(key)
    if not table:
        return [f"no spine per-item mark table vendored for {key} — add it from the spine before authoring"]
    slots = bank.get("slot_index") or {}
    for q in bank.get("questions", []):
        qid = q.get("qid")
        slot = slots.get(qid)
        if not slot:
            errs.append(f"{qid}: no slot_index entry — every item names its MarkLogic slot")
            continue
        if slot not in table:
            errs.append(f"{qid}: slot '{slot}' is not in the {key[0]} C{key[1]} spine")
            continue
        per_item = table[slot]
        if q.get("question_type") == "fill_blank":
            blanks = q.get("blanks", [])
            for b in blanks:
                if b.get("marks") != per_item:
                    errs.append(f"{qid}: blank {b.get('blank_no')} carries {b.get('marks')} "
                                f"but spine {slot} is {per_item} per item")
            if q.get("marks") != per_item * len(blanks):
                errs.append(f"{qid}: marks {q.get('marks')} != {len(blanks)} blanks x {per_item}")
        elif q.get("marks") != per_item:
            errs.append(f"{qid}: marks {q.get('marks')} != spine {slot} per-item value {per_item} "
                        f"(QuestionPolicy §৬ — CT lifts annual questions at unchanged marks)")
    return errs

def g_qb_source_trace(bank, ctx):
    """SOURCE_POLICY §1 — content comes only from the extraction.

    Hardened after the 2026-08-09 audit, which showed the original check was vacuous: it only
    asked whether the anchor string appeared anywhere in the chapter, so a two-character word
    like "না" satisfied it and the anchor was never tied to the question it supposedly sourced.
    An anchor must now be a real span (3+ qb_tokens), must appear in the chapter, and must SHARE
    vocabulary with the item — otherwise it is decoration, not provenance.
    """
    errs = []
    src = ctx["source_text"]
    idx = bank.get("source_index") or {}
    nsrc = qb_norm(src) if src is not None else None
    for q in bank.get("questions", []):
        qid = q.get("qid")
        ref = idx.get(qid)
        if not ref:
            errs.append(f"{qid}: no source_index entry — content comes only from the extraction "
                        f"(SOURCE_POLICY §1); no extraction reference, no question")
            continue
        atoks = [t for t in qb_norm(ref).split() if len(t) >= 3]
        if len(qb_norm(ref).split()) < MIN_ANCHOR_TOKENS:
            errs.append(f"{qid}: source_index anchor '{ref}' is only "
                        f"{len(qb_norm(ref).split())} token(s) — an anchor must be a real span of at "
                        f"least {MIN_ANCHOR_TOKENS}, or it proves nothing")
            continue
        if nsrc is not None and qb_norm(ref) not in nsrc:
            errs.append(f"{qid}: source_index anchor '{ref[:50]}' does not appear in the extraction")
            continue
        itoks = {t for s_ in qb_rendered_strings(q) for t in qb_norm(s_).split() if len(t) >= 3}
        shared = set(atoks) & itoks
        if not (any(len(t) >= 4 for t in shared) or len(shared) >= 2):
            errs.append(f"{qid}: source_index anchor '{ref[:50]}' shares no substantive word with "
                        f"the item — the anchor is not tied to the question it claims to source")
    return errs

def g_answer_shape(bank, ctx):
    """Added after the 2026-08-09 audit: no gate looked at the answer carrier at all, so an MCQ
    with two correct options, or none, sailed through. The LOCKED schema expresses the
    exactly-one-correct rule, but the schema only runs at export — this catches it at authoring.
    """
    errs = []
    for q in bank.get("questions", []):
        qid, qt = q.get("qid"), q.get("question_type")
        if qt == "mcq":
            opts = q.get("options") or []
            n = sum(1 for o in opts if o.get("is_correct"))
            if n != 1:
                errs.append(f"{qid}: {n} correct option(s) — an MCQ has exactly one")
            if len(opts) < MIN_MCQ_OPTIONS:
                errs.append(f"{qid}: {len(opts)} options — at least {MIN_MCQ_OPTIONS} required")
            ids = [o.get("option_id") for o in opts]
            if len(set(ids)) != len(ids):
                errs.append(f"{qid}: duplicate option_id {ids}")
            for o in opts:
                if not o.get("is_correct") and not (o.get("why_wrong") or "").strip():
                    errs.append(f"{qid}: distractor '{o.get('option_id')}' has no why_wrong")
            if len({qb_norm(o.get("text")) for o in opts}) != len(opts):
                errs.append(f"{qid}: two options carry the same text")
        elif qt == "short_answer":
            if not ((q.get("answer_key") or {}).get("accepted") or []):
                errs.append(f"{qid}: short_answer with an empty answer key")
        elif qt == "fill_blank":
            for b in q.get("blanks") or []:
                if not (b.get("accepted") or []):
                    errs.append(f"{qid}: blank {b.get('blank_no')} has no accepted answer")
        elif qt == "descriptive":
            rb = q.get("rubric") or {}
            bands = rb.get("bands") or []
            if len(bands) != q.get("marks"):
                errs.append(f"{qid}: rubric has {len(bands)} bands for a {q.get('marks')}-mark "
                            f"item — a marker cannot turn bands into a mark unless they "
                            f"correspond one-to-one")
    return errs

def g_rubric_specificity(bank, ctx):
    """Added after the 2026-08-09 audit, which found all eight S08 rubrics byte-identical and the
    recall descriptor ("পাঠ থেকে পাঁচটি আলাদা কথা") applied unchanged to opinion prompts."""
    errs = []
    seen = {}
    for q in bank.get("questions", []):
        if q.get("question_type") != "descriptive":
            continue
        rb = q.get("rubric") or {}
        content = [c for c in rb.get("criteria", []) if c.get("role") == "content"]
        if not content:
            errs.append(f"{q.get('qid')}: rubric has no content criterion")
            continue
        sig = qb_norm(json.dumps([c.get("band_descriptors") for c in content],
                              ensure_ascii=False, sort_keys=True))
        if sig in seen:
            errs.append(f"{q.get('qid')}: content rubric is identical to {seen[sig]} — a rubric "
                        f"that fits every question grades none of them")
        else:
            seen[sig] = q.get("qid")
    return errs

def g_qb_topic_number(bank, ctx):
    """canon/topics/TOPIC_NUMBERS.md — a number not in the chart is not used, it is queued.

    This gate exists because a wrong topic_tag survived a full gate chain AND a promotion: nothing
    checked the number against anything, because until CD-043 there was nothing to check it against
    (QB-CR-008, PENDING-P-007). The chart is now canon, so the check is now possible.
    """
    errs = []
    chart = ROOT / "canon" / "topics" / "TOPIC_NUMBERS.md"
    if not chart.exists():
        return ["canon/topics/TOPIC_NUMBERS.md is missing — no topic number can be validated"]
    text = chart.read_text(encoding="utf-8")
    # A tag counts as charted only where it heads a table row: "| `TOP-…` | meaning | slug | attestation |"
    charted = set(re.findall(r"^\|\s*\*{0,2}`(TOP-[A-Z]+-C[1-5]-\d{2})`", text, re.M))
    if not charted:
        return ["canon/topics/TOPIC_NUMBERS.md has no parseable rows"]
    for q in bank.get("questions", []):
        tag = q.get("topic_tag")
        if tag and tag not in charted:
            errs.append(f"{q.get('qid')}: topic_tag '{tag}' is not a row in "
                        f"canon/topics/TOPIC_NUMBERS.md — an unattested number is queued, not used")
    return errs

def g_flag_trace(bank, ctx):
    """QB-D-009 / CD-042 — a bank may be promoted carrying a FLAGGED tag, but only if the flag is
    real: it must name a tag that resolves in PENDING_PRINCIPAL.md, and that row must not be OPEN
    (an OPEN row blocks promotion outright, AGENTS.md §6). A flag pointing at nothing is worse
    than no flag, because it looks like the uncertainty has been handled.
    """
    errs = []
    flags = bank.get("flags") or []
    # The qb_selftest injects a synthetic queue. Reading the live file in a seeded case made the
    # instrument depend on repo state that changes every session: the OPEN-path case named a real
    # OPEN row, the Principal ruled it, and the qb_selftest went red on the next qb_run — not because
    # the gate broke, but because the fixture was the live world. A test fixture must be a fixture.
    text = bank.get("_selftest_queue")
    if text is None:
        queue = ROOT / "PENDING_PRINCIPAL.md"
        text = queue.read_text(encoding="utf-8") if queue.exists() else ""
    for f in flags:
        tag = f.get("tag")
        if not tag:
            errs.append("a flag entry carries no tag")
            continue
        rows = [ln for ln in text.splitlines() if ln.startswith(f"| {tag} |")]
        if not rows:
            errs.append(f"flag {tag} does not resolve to a row in PENDING_PRINCIPAL.md")
            continue
        # Read the STATUS cell (last non-empty cell), not the whole row: a question or default
        # cell may legitimately contain the word. And match the word, not the literal "**OPEN**"
        # — the first version of this check looked for "**OPEN**" and so sailed straight past a
        # row reading "**OPEN — Principal-owed.**". It passed a bank it was written to stop.
        cells = [c.strip() for c in rows[0].strip().strip("|").split("|")]
        status = cells[-1] if cells else ""
        if re.search(r"\bOPEN\b", status):
            errs.append(f"flag {tag} is OPEN (Principal-owed) — an OPEN row blocks promotion "
                        f"(AGENTS.md §6, CD-042); it cannot ride along in a promoted bank")
        for key in ("status", "scope", "what", "closes_on"):
            if not (f.get(key) or "").strip():
                errs.append(f"flag {tag} has no '{key}' — a flag a reader cannot act on is decoration")
    return errs

def g_quote_verbatim(bank, ctx):
    """KEEP-AS-IS / PROTECTED: a quoted span must exist verbatim in the extraction."""
    errs = []
    src = ctx["source_text"]
    if src is None:
        return errs
    nsrc = qb_norm(src)
    for q in bank.get("questions", []):
        for s in qb_rendered_strings(q):
            for span in re.findall(r"[‘“]([^’”]{15,})[’”]", s):
                if qb_norm(span) not in nsrc:
                    errs.append(f"{q.get('qid')}: quoted span '{span[:45]}…' is not verbatim in the "
                                f"extraction — this পাঠ is KEEP-AS-IS and PROTECTED")
    return errs

def g_honorific(bank, ctx):
    errs = []
    for q in bank.get("questions", []):
        for s in qb_rendered_strings(q):
            for m in PROPHET.finditer(s):
                window = s[m.end(): m.end() + HONORIFIC_WINDOW]
                if "(স)" not in window:
                    errs.append(f"{q.get('qid')}: '{m.group(1)}' without (স) within "
                                f"{HONORIFIC_WINDOW} characters — the extraction's বিশেষ নির্দেশ "
                                f"makes the honorific mandatory everywhere")
    return errs

def g_as_mix(bank, ctx):
    """QB-D-004 — AS is roughly half HW-level, half above."""
    ids = (bank.get("pool_index") or {}).get("AS", [])
    items = [ctx["by_qid"][q] for q in ids if q in ctx["by_qid"]]
    if not items:
        return []
    higher = [i for i in items
              if BLOOM_DOMAIN.get(i.get("bloom_level")) in ("প্রয়োগ", "উচ্চতর")
              or i.get("difficulty") == "hard"]
    pct = 100.0 * len(higher) / len(items)
    if not 35.0 <= pct <= 65.0:
        return [f"AS pool is {pct:.0f}% above HW level ({len(higher)}/{len(items)}) — QB-D-004 wants "
                f"roughly half, i.e. 35–65%"]
    return []

def g_qb_script_guard(bank, ctx):
    errs = []
    for q in bank.get("questions", []):
        for s in qb_rendered_strings(q):
            if ARABIC.search(s):
                errs.append(f"{q.get('qid')}: Arabic script in rendered text — tier 1 RED anywhere "
                            f"(LANGUAGE_RULES §7 / CD-014). Use (স), never the Arabic glyph")
            if ARROWS.search(s) or EMOJI.search(s):
                errs.append(f"{q.get('qid')}: arrow/emoji/symbol glyph in rendered text — tier 2 RED "
                            f"(LANGUAGE_RULES §7)")
            ctx["watch"] += len(WATCH.findall(s))
    return errs

def g_numerals(bank, ctx):
    errs = []
    for q in bank.get("questions", []):
        for s in qb_rendered_strings(q):
            if ASCII_DIGIT.search(s):
                errs.append(f"{q.get('qid')}: ASCII digit in a student-facing string "
                            f"('{s[:40]}…') — Bengali numerals only (LANGUAGE_RULES §2)")
    return errs

def g_ceiling(bank, ctx):
    """REPORT ONLY — being under ceiling is never a failure (QB-D-002)."""
    errs = []
    for pool, cap in CEILINGS.items():
        have = len((bank.get("pool_index") or {}).get(pool, []))
        ctx["report"].append(("CEILING", f"{pool}: {have}/{cap} authored, {max(0, cap - have)} owed to ceiling"))
        if have > cap:
            errs.append(f"{pool} holds {have} items, above the ceiling of {cap} (QB-D-002)")
    return errs


# =================================================================================
# GATES — §6 family (canon's eleven)
# =================================================================================

def g_mark_value(bank, ctx):
    """§6 row 1 — Mark value: against MarkLogic spine values."""
    errs, rep = [], []
    key = (bank.get("subject"), bank.get("class"))
    table = QP6_SPINE_ITEM_MARKS.get(key)
    if not table:
        return [], [f"no spine item-mark table vendored for {key} — not judged, not assumed clean"]
    slots = bank.get("slot_index") or {}
    for q in bank["questions"]:
        qid = q.get("qid")
        slot = slots.get(qid)
        if not slot:
            errs.append(f"{qid}: no spine slot in slot_index — a mark cannot be checked against a "
                        f"slot the bank does not name")
            continue
        if slot not in table:
            errs.append(f"{qid}: slot '{slot}' is not in the {key[0]} C{key[1]} spine")
            continue
        want, got = table[slot], q.get("marks")
        if got != want:
            errs.append(f"{qid}: slot {slot} carries {want} marks per item in the spine, "
                        f"item declares {got}")
    rep.append(f"{len(bank['questions'])} items checked against {key[0]} C{key[1]} spine")
    return errs, rep

def g_source_trace(bank, ctx):
    """§6 row 2 — Source traceability: every item resolves to its chapter extraction.

    QUESTION_POLICY §3 row 15 / CD-107: the extraction is the source of FACT. So the anchor must
    exist verbatim in the extraction, and it must be long enough to mean something — a one-word
    anchor matches anything and traces nothing.
    """
    errs, rep = [], []
    extraction = ctx.get("extraction")
    if extraction is None:
        return [], ["no extraction supplied — not judged, not assumed clean"]
    hay = qp_norm(extraction)
    idx = bank.get("source_index") or {}
    MIN_ANCHOR_TOKENS = 3
    for q in bank["questions"]:
        qid = q.get("qid")
        anchor = idx.get(qid)
        if not anchor:
            errs.append(f"{qid}: no source_index anchor — the item traces to nothing")
            continue
        na = qp_norm(anchor)
        if len(na.split()) < MIN_ANCHOR_TOKENS:
            errs.append(f"{qid}: anchor '{anchor}' is {len(na.split())} token(s) — too short to "
                        f"trace; an anchor that matches anything traces nothing")
            continue
        if na not in hay:
            errs.append(f"{qid}: anchor '{anchor}' does not appear in the chapter extraction")
    rep.append(f"{len(idx)} anchors resolved against the extraction")
    return errs, rep

def g_script_guard(bank, ctx):
    """§6 row 3 — Script guard: LANGUAGE_RULES §7.

    Tier 1 Arabic RED everywhere. Tier 2 arrows/emoji RED in rendered text, GREY in metadata —
    the split exists because metadata legitimately carries → and ⚠. Tier 3 em-dash/ellipsis is a
    WATCH counter and never a failure.
    """
    errs, rep = [], []
    watch = grey = 0
    for q in bank["questions"]:
        qid = q.get("qid")
        for s in qp_rendered_strings(q):
            if ARABIC.search(s):
                errs.append(f"{qid}: tier-1 Arabic script in rendered text: {s[:40]!r}")
            if ARROWS.search(s) or EMOJI.search(s):
                errs.append(f"{qid}: tier-2 arrow/emoji/symbol in rendered text: {s[:40]!r}")
            watch += len(WATCH.findall(s))
        for s in metadata_strings(q):
            if ARABIC.search(s):
                errs.append(f"{qid}: tier-1 Arabic script in metadata (RED in both columns): {s[:40]!r}")
            if ARROWS.search(s) or EMOJI.search(s):
                grey += 1
    rep.append(f"tier-3 WATCH counter (em-dash/ellipsis): {watch}; tier-2 GREY in metadata: {grey}")
    return errs, rep

def g_ref19_slug(bank, ctx):
    """§6 row 4 — `ref19_topic_id` resolves, against REF-19's slug set.

    §3 row 18 / CD-108: two registers, two identities. This one is a SLUG and is REF-19's; it is
    not derived from `topic_tag` and does not validate against TOPIC_NUMBERS.md.
    """
    errs, rep = [], []
    slugs = ctx.get("ref19_slugs")
    if slugs is None:
        return [ctx.get("ref19_error", "REF-19 slug set unavailable")], []
    for q in bank["questions"]:
        sid = q.get("ref19_topic_id")
        if sid not in slugs:
            errs.append(f"{q.get('qid')}: ref19_topic_id '{sid}' is not a REF-19 slug")
    rep.append(f"{len(slugs)} REF-19 slugs loaded from the LOCKED artifact")
    return errs, rep

def g_topic_number(bank, ctx):
    """§6 row 5 — `topic_tag` resolves against TOPIC_NUMBERS.md; an unminted number FAILs,
    never auto-mints. QB-CR-008 is why: a wrong tag survived a full gate chain AND a promotion."""
    errs, rep = [], []
    tags = ctx.get("topic_numbers")
    if tags is None:
        return [ctx.get("topic_error", "TOPIC_NUMBERS.md unavailable")], []
    for q in bank["questions"]:
        t = q.get("topic_tag")
        if t not in tags:
            errs.append(f"{q.get('qid')}: topic_tag '{t}' is in no chart row — an unattested "
                        f"number is QUEUED, not used, and this gate never mints one")
    rep.append(f"{len(tags)} charted topic numbers loaded")
    return errs, rep

def g_key_rubric(bank, ctx):
    """§6 row 6 — Key/rubric present, every item, per type.

    §4 "Rubric shape (interim)": minimum conforming is TWO BANDS and a single `islamic_alignment`
    criterion row with band descriptors. The schema's `minContains: 1` permits more than one such
    row; the policy says "a single", so a second is reported rather than failed — the schema is
    the LOCKED contract and this gate does not tighten it past what §4 states.
    """
    errs, rep = [], []
    extra_align = 0
    for q in bank["questions"]:
        qid, qt = q.get("qid"), q.get("question_type")
        want = KEY_FIELD_BY_TYPE.get(qt)
        if want is None:
            errs.append(f"{qid}: question_type '{qt}' is not in the LOCKED schema enum")
            continue
        if not q.get(want):
            errs.append(f"{qid}: {qt} carries no '{want}' — REF-09 §5: no question is finished "
                        f"until its key is written")
            continue
        for other in set(KEY_FIELD_BY_TYPE.values()) - {want}:
            if q.get(other) is not None:
                errs.append(f"{qid}: {qt} also carries '{other}' — the schema forbids the others")
        if want == "rubric":
            r = q["rubric"]
            bands = r.get("bands") or []
            crits = r.get("criteria") or []
            if len(bands) < 2:
                errs.append(f"{qid}: rubric has {len(bands)} band(s) — §4's minimum is two")
            aligns = [c for c in crits if c.get("role") == "islamic_alignment"]
            if not aligns:
                errs.append(f"{qid}: rubric has no `islamic_alignment` criterion row — §4 makes it "
                            f"the one mandatory row")
            elif len(aligns) > 1:
                extra_align += 1
            for c in crits:
                bd = c.get("band_descriptors") or {}
                missing = [b for b in bands if b not in bd]
                if missing:
                    errs.append(f"{qid}: criterion '{c.get('role')}' has no descriptor for "
                                f"band(s) {missing} — the schema cannot cross-check this, so the "
                                f"gate must")
    rep.append(f"key/rubric checked per type on {len(bank['questions'])} items"
               + (f"; {extra_align} rubric(s) carry >1 islamic_alignment row (reported, not failed)"
                  if extra_align else ""))
    return errs, rep

def g_bloom_band(bank, ctx):
    """§6 row 7 — Bloom at POOL level: REF-06 §3.6's LOWER BOUNDS ONLY, read at CHAPTER scope.

    RULED (CD-121, closing Q-1). §6's row said "the wider of REF-06 §3.6 / MarkLogic §৩ at each
    level" and **the §6 text was wrong** — corrected in the same CD row that mints this reading.

    UD-23: **the Bloom axis governs the POOL; the domain axis governs the PAPER.** They are two
    different axes, not two ranges on one axis — which is exactly why "each level" had no common
    referent above Apply. REF-06 bands six Bloom levels; MarkLogic §৩ bands four NAPE domains.
    Nothing is "wider" than the other because they do not measure the same thing.

    So: this gate reads REF-06 §3.6's six levels and **MarkLogic §৩ does not appear here at all**.
    It appears at paper level, in DOMAIN-RATIO, and nowhere else.

    RULED AGAIN (CD-135, 2026-08-15) — and this is the half a later session is most likely to
    "fix" back. Until 2026-08-15 this gate failed a pool on BOTH bounds. **The upper bounds do not
    bind a pool.** It is CD-122(a)'s argument on the other axis, and nothing in that argument was
    about difficulty:

        **A pool cannot fail a CEILING.** An author can always decline to use the surplus, so
        however skewed the pool is, a compliant paper stays constructible from it. **Absence is
        the only thing a pool can be guilty of.**

    A Remember-heavy pool still builds a compliant paper, because the teacher declines the
    surplus. So: `share < lo` FAILs; `share > hi` DOES NOT. The BAND — both bounds — continues to
    apply at PAPER level, alongside the domain ratio.

    ⚠ DO NOT RESTORE THE UPPER-BOUND BRANCH. A symmetric check reddens correct pools. The seeded
    case that used to prove the ceiling is KEPT AND INVERTED — a pool above an upper bound must
    now stay quiet — so the symmetric form cannot creep back unnoticed. Same device CD-122(a)
    used for the hard ceiling, same reason.

    Per-level counts against floors are REPORTED on EVERY run, not only on failure: a check
    written asymmetrically invites a later symmetric "fix", and a report that always prints is
    what makes the asymmetry visible rather than something a reader has to infer from the code.

    Note the arithmetic the floors already do (CD-135(g)): Understand 25 + Apply 25 + Analyze 10
    = 60, so Remember can never exceed 40% of a pool however large. Removing the ceiling does not
    make the pool unbounded — it moves the binding constraint to the floors, and Analyze at 10%
    is the first to bite.

    Never read per session (§4's D-050 paragraph): a bank banded session-by-session drifts low.
    This gate reads the whole pool, which IS the chapter.
    """
    errs, rep = [], []
    total = len(bank["questions"])
    counts = {lvl: 0 for lvl in REF06_C3_5}
    for q in bank["questions"]:
        bl = q.get("bloom_level")
        if bl not in REF06_C3_5:
            errs.append(f"{q.get('qid')}: bloom_level '{bl}' is not one of the six LOCKED levels")
            continue
        counts[bl] += 1
    for lvl, (lo, hi) in REF06_C3_5.items():
        share = pct(counts[lvl], total)
        if share < lo:
            need = -(-lo * total // 100)          # items required to clear the floor
            errs.append(f"chapter pool: {lvl} is {counts[lvl]} of {total} items = {share:.1f}%, "
                        f"below REF-06 §3.6's C3–5 FLOOR of {lo}% — needs {int(need)} "
                        f"({int(need) - counts[lvl]} more)")
        # NO upper-bound branch. CD-135: a pool cannot fail a ceiling. See the docstring's ⚠.
    rep.append("POOL check is FLOORS ONLY (CD-135; CD-121/UD-23 for the axis — MarkLogic §৩ is "
               "the PAPER's axis and is not read here). Upper bounds are a PAPER rule and are "
               "not applied to a pool: an author declines the surplus, so absence is the only "
               "thing a pool can be guilty of.")
    rep.append("per-level counts against REF-06 §3.6 C3–5 floors (printed every run, pass or "
               "fail): " + " · ".join(
                   f"{l} {counts[l]}/{total}={pct(counts[l], total):.1f}% vs floor {lo}%"
                   f"{'' if pct(counts[l], total) >= lo else ' ✗'}"
                   for l, (lo, _hi) in REF06_C3_5.items()))
    zero_floor = [l for l, (lo, _h) in REF06_C3_5.items() if lo == 0 and counts[l] == 0]
    if zero_floor:
        rep.append("levels at 0 against a 0% floor — nothing is required, but §4 requires the "
                   "bank header to state these as a CONTENT fact rather than leave them silent "
                   "(CD-135(d)): " + " · ".join(zero_floor))
    rep.append("read at CHAPTER scope, never per session — §4's D-050 paragraph")
    return errs, rep

def g_difficulty(bank, ctx):
    """§6 row 8 — Difficulty at POOL level: easy ≥30% present. There is NO pool-level hard test.

    RULED (CD-122, closing Q-2). "Can supply" = **easy ≥30% present in the pool**, and nothing else.

    ⚠ DO NOT "TIGHTEN" THIS INTO A SYMMETRIC CHECK. The reasoning is recorded here precisely so a
    later reader does not restore the hard ceiling as a pool rule and redden correct pools:

        A pool cannot fail a CEILING. An author can always decline to use hard items, so however
        hard-heavy a pool is, a compliant paper remains constructible from it. Absence is the only
        thing a pool can be guilty of — and **easy is the only side where absence in the pool makes
        paper-level compliance impossible.** If <30% of the pool is easy, no compliant paper exists;
        if 90% of the pool is hard, a compliant paper still exists.

    The hard ≤25% ceiling is real and binding — at PAPER level (§4), where it belongs.
    """
    errs, rep = [], []
    total = len(bank["questions"])
    counts = {"easy": 0, "medium": 0, "hard": 0}
    for q in bank["questions"]:
        d = q.get("difficulty")
        if d not in counts:
            errs.append(f"{q.get('qid')}: difficulty '{d}' is not in the LOCKED enum")
            continue
        counts[d] += 1
    easy_share = pct(counts["easy"], total)
    if easy_share < EASY_FLOOR:
        errs.append(f"pool cannot supply easy ≥{EASY_FLOOR:.0f}%: only {easy_share:.1f}% of "
                    f"{total} items are easy, so no compliant paper can be drawn from it")
    rep.append(f"pool: easy {easy_share:.1f}% · medium {pct(counts['medium'], total):.1f}% · "
               f"hard {pct(counts['hard'], total):.1f}%  (easy floor only — CD-122; the hard "
               f"≤{HARD_CEILING:.0f}% ceiling is a PAPER-level test and is not applied to a pool)")
    return errs, rep

def g_repetition(bank, ctx):
    """§6 row 9 — Repetition: no verbatim reuse of non-`Remember` items.

    §5 supersedes MarkLogic §৮'s শ্রেণি পরীক্ষা ও বড় পরীক্ষা row for `Remember` items ONLY, and
    the exemption runs BOTH DIRECTIONS — across HW · AS · CT *and* into HY/annual. So a `Remember`
    stem repeated anywhere is expected, not an error, and this gate must stay silent on it. Above
    `Remember` the identical question is barred; same chapter and same type stay fine.
    """
    errs, rep = [], []
    exempt = 0
    seen = {}
    for q in bank["questions"]:
        stem = qp_norm(q.get("question_text"))
        if not stem:
            continue
        seen.setdefault(stem, []).append(q)
    for stem, group in seen.items():
        if len(group) < 2:
            continue
        if all(q.get("bloom_level") == "Remember" for q in group):
            exempt += 1
            continue
        qids = ", ".join(q.get("qid", "?") for q in group)
        levels = sorted({q.get("bloom_level") for q in group})
        errs.append(f"verbatim reuse above `Remember` ({'/'.join(levels)}): {qids}")
    # The same rule across instruments, including into HY/annual.
    papers = bank.get("papers") or []
    stems_by_paper = {}
    byqid = {q.get("qid"): q for q in bank["questions"]}
    for p in papers:
        stems_by_paper[p.get("paper_id")] = {
            qp_norm(byqid[qid].get("question_text")): byqid[qid]
            for qid in p.get("items", []) if qid in byqid}
    names = list(stems_by_paper)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            for stem in set(stems_by_paper[a]) & set(stems_by_paper[b]):
                q = stems_by_paper[a][stem]
                if q.get("bloom_level") == "Remember":
                    exempt += 1
                    continue
                errs.append(f"verbatim reuse of a non-`Remember` item across papers "
                            f"{a} → {b}: {q.get('qid')}")
    rep.append(f"{exempt} `Remember` repetition(s) permitted by §5 — expected, not an error")
    return errs, rep

def g_coverage(bank, ctx):
    """§6 row 10 — Coverage: every topic and every spine slot-type supplied.

    ⚑ RECORDED ABSENCE — THE PER-CHAPTER SPINE SLOT-MAPPING DOES NOT EXIST AS DATA (CD-122,
    closing Q-3). This is written down so its ARRIVAL is a known trigger: **the day a per-chapter
    slot-mapping is committed as data, this gate changes and this docstring is the notice.**

    What exists instead is `canon/marklogic/C5_Bangla_Source_13-23.md`'s "কোন প্রশ্নের জন্য কোন পাঠ"
    table, which runs the OTHER WAY — slot → best-source পাঠ, with a separate বিকল্প column — and
    each পাঠ's own "কোন প্রশ্নে কাজে লাগবে" line, which is prose. Inverting a best/alternative
    table into a per-chapter obligation is inventing the mapping, and §4 forbids that.

    So §4's fallback governs, and the Principal confirmed it: "The per-chapter target is decided at
    production time and STATED IN THE BANK FILE HEADER with a one-line reason… When per-chapter
    spine slot-mapping exists as data, this replaces the header-stated target." It does not, so the
    header binds, and this gate checks the pool against the header the bank itself declares.
    """
    errs, rep = [], []
    header = bank.get("header") or {}
    topics = header.get("topics")
    slots = header.get("spine_slots")
    if not header.get("reason"):
        errs.append("bank header states no one-line reason for its target — §4 requires one")
    if topics is None or slots is None:
        errs.append("bank header does not declare `topics` and `spine_slots` — with no slot "
                    "mapping in data, the header IS the coverage target (§4) and cannot be absent")
        return errs, rep
    have_topics = {q.get("topic_tag") for q in bank["questions"]}
    have_slots = set((bank.get("slot_index") or {}).values())
    for t in topics:
        if t not in have_topics:
            errs.append(f"header declares topic {t}; no item in the pool supplies it")
    for s in slots:
        if s not in have_slots:
            errs.append(f"header declares spine slot {s}; no item in the pool supplies it")
    target = header.get("target")
    if isinstance(target, int) and len(bank["questions"]) < target:
        errs.append(f"header target is {target} items; the pool holds {len(bank['questions'])}")
    if len(bank["questions"]) < 20:
        errs.append(f"pool holds {len(bank['questions'])} items — REF-09 §4.3's floor is 20 per "
                    f"chapter (cite §4.3, not REF-08 §4.1, for the chapter reading)")
    rep.append(f"coverage read against the HEADER-STATED target (§4 fallback — Q-3): "
               f"{len(topics)} topic(s), {len(slots)} slot(s), target {target}")
    return errs, rep

def g_domain_ratio(bank, ctx):
    """§6 row 11 — Domain ratio: PAPER LEVEL ONLY, never per pool.

    Two things this gate must not do, both stated in canon rather than inferred:
      · It must not fire on a POOL. §6's row says "paper level only, never per pool" — the pool is
        banded by BLOOM-BAND, and applying the ratio to it as well would double-band the same
        items against two different targets.
      · It must not fire on a SINGLE CLASS TEST. §5, from MarkLogic §৬: the ratio is met "across
        the year's tests, not within any single one — 25 marks cannot carry four domains in
        proportion, so there is no per-CT domain gate."
    A bank with no `papers` block is therefore NOT judged here, and that is the correct verdict,
    not a skipped one.
    """
    errs, rep = [], []
    papers = bank.get("papers") or []
    if not papers:
        rep.append("no papers in this bank — domain ratio is PAPER LEVEL ONLY (§6) and is not "
                   "applied to a pool. Not judged; not assumed clean.")
        return errs, rep
    byqid = {q.get("qid"): q for q in bank["questions"]}
    cts = [p for p in papers if p.get("kind") == "classtest"]
    judged = 0
    for p in papers:
        kind = p.get("kind")
        if kind not in RATIO_PAPER_KINDS:
            continue
        judged += 1
        items = [byqid[q] for q in p.get("items", []) if q in byqid]
        marks = sum(q.get("marks", 0) for q in items) or 0
        dom = {d: 0.0 for d in MARKLOGIC_C5}
        for q in items:
            d = BLOOM_TO_DOMAIN.get(q.get("bloom_level"))
            if d:
                dom[d] += q.get("marks", 0)
        for d, (lo, hi) in MARKLOGIC_C5.items():
            share = pct(dom[d], marks)
            if not (lo <= share <= hi):
                errs.append(f"paper {p.get('paper_id')} ({kind}): {d} is {share:.1f}% of {marks} "
                            f"marks, outside MarkLogic §৩ C5 {lo}–{hi}%")
        rep.append(f"paper {p.get('paper_id')} ({kind}, {marks} marks): "
                   + " · ".join(f"{d} {pct(dom[d], marks):.1f}%" for d in dom))
    if cts:
        # The year's class tests are checked as a SET, per §5. One CT alone is never judged.
        items = [byqid[q] for p in cts for q in p.get("items", []) if q in byqid]
        marks = sum(q.get("marks", 0) for q in items) or 0
        dom = {d: 0.0 for d in MARKLOGIC_C5}
        for q in items:
            d = BLOOM_TO_DOMAIN.get(q.get("bloom_level"))
            if d:
                dom[d] += q.get("marks", 0)
        if len(cts) > 1:
            judged += 1
            for d, (lo, hi) in MARKLOGIC_C5.items():
                share = pct(dom[d], marks)
                if not (lo <= share <= hi):
                    errs.append(f"the year's {len(cts)} class tests together: {d} is {share:.1f}% "
                                f"of {marks} marks, outside MarkLogic §৩ C5 {lo}–{hi}%")
            rep.append(f"{len(cts)} class tests as a SET ({marks} marks): "
                       + " · ".join(f"{d} {pct(dom[d], marks):.1f}%" for d in dom))
        else:
            rep.append("1 class test present — a single CT is NEVER judged on domain ratio "
                       "(§5 / MarkLogic §৬: met across the year's tests)")
    if not judged:
        rep.append("no annual/half-yearly paper and fewer than two class tests — nothing this "
                   "gate may judge")
    return errs, rep


# =================================================================================
# THE REGISTRY — 21 gates, each declaring its authority and the shape it reads
# =================================================================================
# `shape` is what makes the union safe. "qb" reads QB_POLICY §5's bank; "qp6" reads
# QUESTION_POLICY §4's. A gate whose shape is absent reports N/A WITH THE REASON — never PASS.
# Four names carry both, and dispatch: the gate exists once, its implementation follows the bank.

GATES = [
    ("POOL-MEMBERSHIP",    {"qb": g_pool_membership},                    "§5 · QB-CR-001"),
    ("ZERO-OVERLAP",       {"qb": g_zero_overlap},                       "§5 · QB-D-001"),
    ("MARK-VALUE",         {"qb": g_qb_mark_value, "qp6": g_mark_value}, "§5 · QB-CR-003 + §6.1"),
    ("SOURCE-TRACE",       {"qb": g_qb_source_trace, "qp6": g_source_trace}, "§5 + §6.2"),
    ("SCRIPT-GUARD",       {"qb": g_qb_script_guard, "qp6": g_script_guard}, "§5 + §6.3"),
    ("REF19-SLUG",         {"qp6": g_ref19_slug},                        "§6.4"),
    ("TOPIC-NUMBER",       {"qb": g_qb_topic_number, "qp6": g_topic_number}, "§5 · QB-CR-008 + §6.5"),
    ("KEY-RUBRIC",         {"qp6": g_key_rubric},                        "§6.6"),
    ("BLOOM-BAND",         {"qp6": g_bloom_band},                        "§6.7 · CD-121 · CD-135"),
    ("DIFFICULTY",         {"qp6": g_difficulty},                        "§6.8 · CD-122"),
    ("REPETITION",         {"qp6": g_repetition},                        "§6.9"),
    ("COVERAGE",           {"qp6": g_coverage},                          "§6.10 · CD-122"),
    ("DOMAIN-RATIO",       {"qp6": g_domain_ratio},                      "§6.11 (per-pool RETIRED)"),
    ("ANSWER-SHAPE",       {"qb": g_answer_shape},                       "§5"),
    ("RUBRIC-SPECIFICITY", {"qb": g_rubric_specificity},                 "§5"),
    ("FLAG-TRACE",         {"qb": g_flag_trace},                         "§5 · QB-D-012"),
    ("QUOTE-VERBATIM",     {"qb": g_quote_verbatim},                     "§5"),
    ("HONORIFIC",          {"qb": g_honorific},                          "§5"),
    ("AS-MIX",             {"qb": g_as_mix},                             "§5 · QB-D-004"),
    ("NUMERALS",           {"qb": g_numerals},                           "§5"),
    ("CEILING",            {"qb": g_ceiling},                            "§5 · QB-D-002 (report)"),
    # CD-131 — the 22nd, and the first that carries NEITHER policy's § row. It executes a DECISION
    # ROW (CD-127(b)) rather than a policy clause, which is why its authority cell names a CD and
    # not a §. Shape-independent: it reads qids, and both families have them.
    ("SOURCE-EXCLUSION",   {"qb": g_source_exclusion, "qp6": g_source_exclusion},
                                                                         "CD-127(b) · CD-131"),
]
# CD-123's invariant is preserved by counting what CD-123 was counting — the gates that carry a
# QUESTION_POLICY §6 row — rather than the total, which CD-131 has now moved. Asserting on the
# total alone would have made the §6 count unverifiable the moment any gate was added from
# anywhere else, which is the shape CD-083 keeps naming: a check written in a coarser unit than
# the thing it is protecting.
QP6_POLICY_GATES = [n for n, i, a in GATES if "qp6" in i and a.startswith("§")]
assert len(QP6_POLICY_GATES) == 11, "CD-123: QUESTION_POLICY §6 has eleven rows"
assert len(GATES) == 22, "CD-123's 21 + CD-131's SOURCE-EXCLUSION"


def bank_shape(bank):
    """→ 'qp6' | 'qb' | None. Declared beats inferred: a bank may state its own shape."""
    declared = (bank.get("header") or {}).get("policy_shape")
    if declared in ("qp6", "qb"):
        return declared
    if "header" in bank and isinstance(bank.get("questions"), list):
        return "qp6"
    if "pool_index" in bank:
        return "qb"
    return None


def run(bank, ctx=None, quiet=False):
    """Runs all 22 (CD-123's 21 + CD-131's SOURCE-EXCLUSION). Returns (fails, report).

    Shape-absent gates print N/A and the reason — never PASS."""
    shape = bank_shape(bank)
    if ctx is None:
        ctx = qp_ctx_for(bank) if shape == "qp6" else qb_build_ctx(bank)
    fails, report = [], []
    for name, impls, authority in GATES:
        fn = impls.get(shape)
        if fn is None:
            if not quiet:
                why = (f"reads QUESTION_POLICY §4's shape; this bank is {shape or 'unrecognised'}"
                       if "qp6" in impls else
                       f"reads QUESTION_BANK_POLICY §5's shape; this bank is {shape or 'unrecognised'}")
                print(f"  N/A   {name:<18} {why}")
            continue
        out = fn(bank, ctx)
        errs, rep = out if isinstance(out, tuple) else (out, [])
        if not quiet:
            print(f"  {'FAIL' if errs else 'PASS'}  {name:<18} [{authority}]"
                  + "".join(f"\n        - {e}" for e in errs))
        fails += [(name, e) for e in errs]
        report += [(name, line) for line in rep]
    return fails, report


def qp_ctx_for(bank):
    slugs, slug_err = load_ref19_slugs(ROOT)
    tags, tag_err = load_topic_numbers(ROOT)
    ctx = {"ref19_slugs": slugs, "ref19_error": slug_err,
           "topic_numbers": tags, "topic_error": tag_err, "extraction": None}
    ex = bank.get("extraction_path")
    if ex and (ROOT / ex).exists():
        ctx["extraction"] = (ROOT / ex).read_text(encoding="utf-8", errors="replace")
    return ctx


# Both families' selftests now drive the MERGED registry through these two shims, so what they
# prove is this suite — not the two lists it was built from. That is the point of merging: a
# selftest that still exercised the old GATES list would go on passing after the merge broke it.

def qb_run(bank, quiet=False):
    return run(bank, qb_build_ctx(bank), quiet=quiet)


def qp_run(bank, ctx, quiet=False):
    return run(bank, ctx, quiet=quiet)


# =================================================================================
# CONTEXT — §5 family
# =================================================================================

def qb_build_ctx(bank):
    by_qid = {q.get("qid"): q for q in bank.get("questions", [])}
    pool_of = {}
    for pool, ids in (bank.get("pool_index") or {}).items():
        for qid in ids:
            pool_of[qid] = pool
    subject, class_level, unit = "?", 0, "?"
    for qid in by_qid:
        m = re.match(r"^QP-([A-Z]+)-C([1-5])-U(\d+)", qid or "")
        if m:
            # CD-130(b) — THE REPO'S FIRST `int-id-ok:` WAIVER. It is written to be the example
            # the second one is copied from, so the standard it sets is the standard that spreads.
            #
            # The test a waiver must meet is NOT "this is fine today". It is: **the transform
            # CANNOT merge two distinct ID strings here.** Group 2 is `C([1-5])` — one digit by
            # construction — so no padding is expressible and there is no second spelling for
            # int() to collapse into the first. Contrast group 3, `U(\d+)`, three lines down:
            # padding IS expressible there, `U09` and `U9` are two strings, and that one was
            # REWRITTEN rather than waived. Same file, same regex, opposite disposition — because
            # the question is about the group, not about the programmer's confidence.
            #
            # And `class_level` is genuinely a number: it is compared against 1..5 as an ordinal,
            # not matched as a name. An identifier segment that is used as a quantity is the only
            # thing this waiver is for.
            class_level = int(m.group(2))  # int-id-ok: C([1-5]) is one digit — no padding expressible, so no two distinct IDs can collapse; used as an ordinal 1..5
            subject, unit = m.group(1), m.group(3)
            break
    src_text, unit_note = None, None
    ref = bank.get("source_extraction")
    if ref:
        path = ROOT / ref.split("#")[0]
        if path.exists():
            full = path.read_text(encoding="utf-8")
            src_text, unit_note = qb_resolve_chapter(full, unit)
    ctx = {"by_qid": by_qid, "pool_of": pool_of, "subject": subject,
           "class_level": class_level, "unit": unit, "source_text": src_text,
           "watch": 0, "report": []}
    if unit_note:
        ctx["report"].append(("SOURCE-TRACE", unit_note))
    return ctx


# =================================================================================
# PART-AUTHORED BANKS — CD-055's self-declaration
# =================================================================================

MARKER = "নির্মাণাধীন"

DECL_RE = re.compile(r"^\s*" + MARKER + r"\s*[—-]\s*(?P<detail>\S.*)$")

def bank_declaration(bank):
    """→ (is_marked, detail, error). Reads `header.অবস্থা` only — never a free-text scan.

    A bank that carries the marker with no resume tail is marked-but-invalid: it gets the
    exclusion refused, not granted, because CD-055's exclusion is bought by the detail.
    """
    raw = (bank.get("header") or {}).get("অবস্থা")
    if raw is None:
        return False, None, None
    if not isinstance(raw, str) or MARKER not in raw:
        return False, None, (f"`header.অবস্থা` is present but does not carry `{MARKER}` "
                             f"— got {raw!r}; §7.9 defines exactly one marker")
    m = DECL_RE.match(raw)
    if not m:
        return True, None, (f"declares `{MARKER}` with no resume detail — §7.9's line is "
                            f"`{MARKER} — <what is authored, what is not, where to resume>`, "
                            f"and the tail is what the exclusion is bought with")
    return True, m.group("detail").strip(), None

def classify(path, bank):
    """→ (in_controls: bool, reason: str). Every verdict is printed by the sweep, both ways.

    PRE-POLICY is a DECLARED status, not a shape accident (CD-123). A bank authored under
    superseded policy says so in `policy_status`, and the sweep quotes its own words. The
    difference matters: a bank held out because a parser could not find `header` is held out by
    luck, and the day someone adds a `header` key it silently re-enters. A bank held out because
    it declares itself pre-policy re-enters only when a human removes the line.
    """
    marked, detail, err = bank_declaration(bank)
    if err:
        return False, f"REFUSED  {err}"
    if marked:
        return False, f"SKIPPED  declares {MARKER} — resume: {detail}"
    pre = bank.get("policy_status")
    if isinstance(pre, str) and pre.startswith("pre-policy"):
        return False, f"PRE-POLICY  {pre}"
    if not isinstance(bank.get("questions"), list) or "header" not in bank:
        return False, ("REFUSED  built to no policy shape this suite knows, and declares no "
                       "`policy_status` — a bank is judged or it says why not; it is not simply "
                       "unrecognised (SOURCE_POLICY §7.17)")
    return True, "CONTROL  complete and §4-shaped"

def sweep(root, ctx):
    """Repo-wide pass. Prints the skip ledger FIRST, then judges everything it found.

    The order is deliberate: the exclusions are printed before any verdict, so a reader cannot
    reach a green line without having read what was held out to get there.
    """
    found = sorted((root / "workstreams/question-banks/banks").glob("*.json"))
    print(f"\nBANK SWEEP — {len(found)} file(s) under workstreams/question-banks/banks/")
    if not found:
        print("  (none)")
        return []
    rows, fails = [], []
    for p in found:
        try:
            bank = json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:                                    # noqa: BLE001
            print(f"  REFUSED  {p.relative_to(root)} — unreadable: {e}")
            fails.append((str(p), "unreadable"))
            continue
        in_ctl, reason = classify(p, bank)
        rows.append((p, bank, in_ctl, reason))
        print(f"  {reason:<64} {p.relative_to(root)}")
    print(f"  → {sum(1 for r in rows if r[2])} in controls, "
          f"{sum(1 for r in rows if not r[2])} held out (each named above)")

    for p, bank, in_ctl, _ in rows:
        marked, _, _ = bank_declaration(bank)
        if not in_ctl and not marked:
            continue                       # out of §6's scope entirely — not judged, said so above
        print(f"\n  BANK: {p.relative_to(root)}"
              + (f"   [{MARKER} — judged anyway; the marker is not a waiver (CD-055)]"
                 if marked else ""))
        f, rep = qp_run(bank, ctx)
        fails += [(str(p), e) for _, e in f]
        # CD-135(f): the per-level Bloom counts against floors are REPORTED on EVERY run, not
        # only when a floor is missed and not only on the single-bank path. A check written
        # asymmetrically invites a later symmetric "fix"; a report that always prints is what
        # makes the asymmetry visible rather than something a reader infers from the code.
        for gate, line in rep:
            if gate == "BLOOM-BAND":
                print(f"  REPORT  {gate:<18} {line}")
        if marked and not f:
            msg = (f"passes all eleven while still declaring {MARKER} — the marker is stale and "
                   f"removing it is part of finishing (SOURCE_POLICY §7.9; STATED DEFAULT, Q-4)")
            print(f"  FAIL  STALE-MARKER\n        - {msg}")
            fails.append((str(p), msg))
    return fails


# =================================================================================
# SEEDED SELFTEST — synthetic fixtures only (CD-055, CD-064(f))
# =================================================================================
# Every fixture below is written for this test. Nothing is read from canon/sources/ or
# canon/marklogic/. The synthetic chapter is a fictional "পাঠ ৯৯" that does not exist in any book,
# precisely so that no future reader can mistake it for a real extraction.


# =================================================================================
# SELFTEST — §5 family
# =================================================================================

SELFTEST_ANCHOR = "আরাফাতের ময়দানে মহানবি (স) ভাষণ দিলেন"

BN_DIGITS = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")

def qb_bn(n):
    return str(n).translate(BN_DIGITS)

def _qb_good_bank():
    """A synthetic bank that must be CLEAN: 3 pools x 20 one-mark items, each pool split
    6/7/5/2 = exactly the C5 band 30/35/25/10. Stems are unique so ZERO-OVERLAP stays quiet.
    It points at the REAL extraction so SOURCE-TRACE and QUOTE-VERBATIM are exercised."""
    blooms = ["Remember"] * 6 + ["Understand"] * 7 + ["Apply"] * 5 + ["Analyze"] * 2
    pools, qs, slots, srcs, n = {}, [], {}, {}, 0
    for pool in ("HW", "AS", "CT"):
        pools[pool] = []
        for k, bloom in enumerate(blooms):
            n += 1
            qid = f"QP-BAN-C5-U21-Q{n:02d}"
            # AS carries hard difficulty on three Understand items -> AS-MIX lands near half.
            diff = "hard" if (pool == "AS" and bloom == "Understand" and k < 9) else "easy"
            qs.append({"qid": qid, "topic_tag": "TOP-BAN-C5-07",
                       "ref19_topic_id": "BAN-INFOTEXT",
                       "question_text": f"সেলফটেস্ট নমুনা ভাষণ প্রশ্ন ক্রমিক {qb_bn(n)} কোনটি",
                       "question_type": "mcq", "paper_role": "mcq", "bloom_level": bloom,
                       "difficulty": diff, "tier": "tier1", "marks": 1,
                       "options": [{"option_id": "ক", "text": f"সঠিক বিকল্প {qb_bn(n)}", "is_correct": True},
                                   {"option_id": "খ", "text": f"ভুল বিকল্প {qb_bn(n)}", "is_correct": False,
                                    "why_wrong": "পাঠে এই কথা নেই"},
                                   {"option_id": "গ", "text": f"অন্য ভুল বিকল্প {qb_bn(n)}",
                                    "is_correct": False, "why_wrong": "পাঠে এই কথাও নেই"}]})
            pools[pool].append(qid)
            slots[qid] = "S05"
            srcs[qid] = SELFTEST_ANCHOR
    return {"schema_version": "1.0", "bank_id": "SELFTEST",
            "source_extraction": "canon/marklogic/C5_Bangla_Source_13-23.md",
            "pool_index": pools, "slot_index": slots, "source_index": srcs, "questions": qs}

def _qb_twin_rubrics(b):
    """Two descriptive items carrying a byte-identical content rubric."""
    rb = {"bands": ["৫", "৪", "৩", "২", "১"],
          "criteria": [{"role": "content", "criterion": "সব প্রশ্নে খাটে এমন একটি মানদণ্ড",
                        "band_descriptors": {x: "একই বর্ণনা" for x in ["৫", "৪", "৩", "২", "১"]}},
                       {"role": "islamic_alignment", "criterion": "সংগতি",
                        "band_descriptors": {x: "একই বর্ণনা" for x in ["৫", "৪", "৩", "২", "১"]}}]}
    for k, pool in enumerate(("HW", "AS")):
        qid = f"QP-BAN-C5-U21-Q9{k}"
        b["questions"].append({"qid": qid, "topic_tag": "TOP-BAN-C5-07",
                               "ref19_topic_id": "BAN-INFOTEXT",
                               "question_text": f"সেলফটেস্ট ভাষণ বিস্তৃত প্রশ্ন {qb_bn(k)}",
                               "question_type": "descriptive", "paper_role": "structured",
                               "bloom_level": "Evaluate", "difficulty": "hard", "tier": "tier1",
                               "marks": 5, "rubric": json.loads(json.dumps(rb))})
        b["pool_index"][pool].append(qid)
        b["slot_index"][qid] = "S08"
        b["source_index"][qid] = SELFTEST_ANCHOR

def _qb_mutate(fn):
    b = json.loads(json.dumps(_qb_good_bank()))
    fn(b)
    return b

def qb_selftest():
    """Every gate must fire on a bank broken specifically for it."""
    import copy  # noqa: F401
    cases = []

    def add(gate, label, fn, expect=None):
        cases.append((gate, label, _qb_mutate(fn), expect))

    add("POOL-MEMBERSHIP", "question in two pools",
        lambda b: b["pool_index"]["CT"].append("QP-BAN-C5-U21-Q01"))
    add("POOL-MEMBERSHIP", "a CW pool reappears",
        lambda b: b["pool_index"].update({"CW": []}))
    add("ZERO-OVERLAP", "same stem in HW and CT",
        lambda b: b["questions"][-1].update({"question_text": b["questions"][0]["question_text"]}))
    add("ZERO-OVERLAP", "exact duplicate INSIDE the HW pool",
        lambda b: b["questions"][2].update({"question_text": b["questions"][0]["question_text"]}))
    add("ANSWER-SHAPE", "an MCQ with two correct options",
        lambda b: b["questions"][0]["options"][1].update({"is_correct": True}))
    add("ANSWER-SHAPE", "an MCQ with no correct option",
        lambda b: b["questions"][0]["options"][0].update({"is_correct": False}))
    add("ANSWER-SHAPE", "a distractor with no why_wrong",
        lambda b: b["questions"][0]["options"][1].pop("why_wrong"))
    add("SOURCE-TRACE", "a one-word anchor that matches anything",
        lambda b: b["source_index"].update({"QP-BAN-C5-U21-Q01": "না"}))
    add("SOURCE-TRACE", "a real span that has nothing to do with the item",
        lambda b: b["source_index"].update({"QP-BAN-C5-U21-Q01": "জিলকদ মাসের শেষে"}))
    add("HONORIFIC", "bare নবি with no (স)",
        lambda b: b["questions"][0].update({"question_text": "নবি সাহেব কোথায় ভাষণ দেন"}))
    add("HONORIFIC", "হজরত with no (স)",
        lambda b: b["questions"][0].update({"question_text": "হজরত মুহাম্মদ কোথায় ভাষণ দেন"}))
    add("RUBRIC-SPECIFICITY", "two S08 items sharing one rubric", _qb_twin_rubrics)
    add("TOPIC-NUMBER", "a topic_tag that is in no chart row",
        lambda b: b["questions"][0].update({"topic_tag": "TOP-BAN-C5-99"}))
    add("FLAG-TRACE", "a flag pointing at a tag that does not exist",
        lambda b: b.update({"flags": [{"tag": "PENDING-P-999", "status": "FLAGGED",
                                       "scope": "x", "what": "y", "closes_on": "z"}]}))
    add("FLAG-TRACE", "a flag naming a row that is OPEN (Principal-owed)",
        lambda b: b.update({
            "flags": [{"tag": "PENDING-P-XXX", "status": "OPEN",
                       "scope": "x", "what": "y", "closes_on": "z"}],
            "_selftest_queue": "| PENDING-P-XXX | d | w | q | def | by | **OPEN** — synthetic |"}))

    add("FLAG-TRACE", "a flag with no closes_on",
        lambda b: b.update({"flags": [{"tag": "PENDING-P-005", "status": "FLAGGED",
                                       "scope": "x", "what": "y", "closes_on": ""}]}))
    add("MARK-VALUE", "MCQ carries 5 marks",
        lambda b: b["questions"][0].update({"marks": 5}))
    add("SOURCE-TRACE", "an item with no extraction anchor",
        lambda b: b["source_index"].pop("QP-BAN-C5-U21-Q01"))
    add("QUOTE-VERBATIM", "an invented quotation",
        lambda b: b["questions"][0].update(
            {"question_text": "‘এই বাক্যটি পাঠে কোথাও নেই একেবারেই’ কে বলেছেন"}))
    add("HONORIFIC", "the Prophet's name without (স)",
        lambda b: b["questions"][0].update({"question_text": "মহানবি কোথায় ভাষণ দেন"}))
    add("AS-MIX", "AS is entirely recall",
        lambda b: [q.update({"bloom_level": "Remember", "difficulty": "easy"})
                   for q in b["questions"] if q["qid"] in b["pool_index"]["AS"]])
    add("SCRIPT-GUARD", "Arabic script in a stem",
        lambda b: b["questions"][0].update({"question_text": "بسم কী অর্থ"}))
    add("SCRIPT-GUARD", "an arrow in a stem",
        lambda b: b["questions"][0].update({"question_text": "মক্কা → মদিনা কোনটি"}))
    add("NUMERALS", "an ASCII digit in a stem",
        lambda b: b["questions"][0].update({"question_text": "10 হিজরিতে কী হয়েছিল"}))
    add("CEILING", "HW above its ceiling",
        lambda b: b["pool_index"].update({"HW": [f"QP-BAN-C5-U21-Q{n:02d}" for n in range(1, 102)]}))

    print("SELFTEST — the instrument is proven before any bank verdict (CD-025)")
    ok = True

    # Negative case: a FLAGGED row is promotable (CD-042) and must NOT trip FLAG-TRACE.
    # A gate that fires on everything is as useless as one that fires on nothing.
    neg = _qb_mutate(lambda b: b.update({
        "flags": [{"tag": "PENDING-P-XXX", "status": "FLAGGED",
                   "scope": "x", "what": "y", "closes_on": "z"}],
        "_selftest_queue": "| PENDING-P-XXX | d | w | q | def | by | **FLAGGED** — synthetic |"}))
    if any(g == "FLAG-TRACE" for g, _ in qb_run(neg, quiet=True)[0]):
        print("  FAIL  FLAG-TRACE fires on a FLAGGED row — it must not; FLAGGED is promotable")
        ok = False
    else:
        print("  PASS  FLAG-TRACE stays quiet on a FLAGGED row (CD-042: FLAGGED is promotable)")

    clean, _ = qb_run(_qb_good_bank(), quiet=True)
    if clean:
        print(f"  FAIL  baseline: the good bank is not clean -> {clean}")
        ok = False
    else:
        print("  PASS  baseline: an unbroken bank is CLEAN")

    for gate, label, broken, expect in cases:
        fails, _ = qb_run(broken, quiet=True)
        fired = {g for g, _ in fails}
        hit = gate in fired and (expect is None
                                 or any(expect in m for g, m in fails if g == gate))
        if hit:
            print(f"  PASS  {gate:<16} fires on: {label}")
        else:
            print(f"  FAIL  {gate:<16} DID NOT FIRE on: {label}")
            ok = False

    # --- CD-131: SOURCE-EXCLUSION, seeded both directions. The declarations are SYNTHETIC and
    # --- injected through ctx — the gate never reads live canon/ in a seed (CD-121(e)).
    SYNTH_EXCL = [{"subject": "BAN", "class": "5", "chapter": "12", "cd": "CD-127",
                   "_file": "canon/_wip/c5-bangla/EXCLUDED_synthetic.md",
                   "_tokens": _chapter_tokens("12")}]

    def _excl_run(bank, decls, errors=None):
        c = qb_build_ctx(bank)
        c["exclusions"] = decls
        c["exclusion_errors"] = errors or []
        return run(bank, c, quiet=True)[0]

    def _retag(bank, unit):
        """Move a synthetic bank onto another chapter — qids only, nothing else touched."""
        b = json.loads(json.dumps(bank))
        sw = lambda s: s.replace("-U21-", f"-U{unit}-")                      # noqa: E731
        b["questions"] = [{**q, "qid": sw(q["qid"])} for q in b["questions"]]
        b["pool_index"] = {k: [sw(x) for x in v] for k, v in b["pool_index"].items()}
        b["slot_index"] = {sw(k): v for k, v in b["slot_index"].items()}
        b["source_index"] = {sw(k): v for k, v in b["source_index"].items()}
        return b

    excl_cases = [
        ("FAILs when an item's qid resolves to a declared-excluded chapter (`U12`) — CD-127(b) "
         "given an executor",
         lambda: any(g == "SOURCE-EXCLUSION" and "CD-127" in m
                     for g, m in _excl_run(_retag(_qb_good_bank(), "12"), SYNTH_EXCL))),
        ("FAILs on the ZERO-PADDED spelling `U012` too — the exclusion fails CLOSED, which is the "
         "opposite direction from CD-088 and the safe one",
         lambda: any(g == "SOURCE-EXCLUSION"
                     for g, _ in _excl_run(_retag(_qb_good_bank(), "012"), SYNTH_EXCL))),
        ("control · a NON-excluded chapter (`U21`) stays silent — a gate that fires on everything "
         "is as useless as one that fires on nothing",
         lambda: not any(g == "SOURCE-EXCLUSION"
                         for g, _ in _excl_run(_qb_good_bank(), SYNTH_EXCL))),
        ("control · the same chapter number in a DIFFERENT subject/class is not excluded — the "
         "declaration is (subject, class, chapter), not a bare number",
         lambda: not any(g == "SOURCE-EXCLUSION" for g, _ in _excl_run(
             _retag(_qb_good_bank(), "12"),
             [{**SYNTH_EXCL[0], "subject": "ENG", "_tokens": _chapter_tokens("12")}]))),
        ("FAILs when the bank's whole declared SOURCE FILE is excluded, even with no matching qid",
         lambda: any(g == "SOURCE-EXCLUSION" and "declared source" in m for g, m in _excl_run(
             {**_qb_good_bank(), "source_extraction": "canon/x/EXCLUDED_whole.md"},
             [{**SYNTH_EXCL[0], "_file": "canon/x/EXCLUDED_whole.md"}]))),
        ("a MALFORMED declaration FAILs rather than being skipped — a prohibition nobody can "
         "resolve is not a prohibition (§7.17: reports or refuses, never omits)",
         lambda: any(g == "SOURCE-EXCLUSION" and "missing" in m for g, m in _excl_run(
             _qb_good_bank(), [], ["fixture.md: exclusion declaration is missing chapter"]))),
        ("with NO declaration anywhere the gate is silent but SAYS SO — it never passes by "
         "reporting nothing",
         lambda: (not any(g == "SOURCE-EXCLUSION" for g, _ in _excl_run(_qb_good_bank(), []))
                  and any("nothing to enforce" in line for _, line in
                          run(_qb_good_bank(),
                              {**qb_build_ctx(_qb_good_bank()), "exclusions": []},
                              quiet=True)[1]))),
    ]
    # --- MINT vs CITE, found by this gate's own first live run (CD-131 addendum). Both
    # --- directions, on synthetic text: a standalone comment DECLARES; a row of prose that
    # --- contains the same string DISCUSSES. AGENTS.md §5.1 — naming the defect stays writeable.
    import tempfile
    from pathlib import Path as _Path

    def _load_from(text):
        d = _Path(tempfile.mkdtemp()) / "canon"
        d.mkdir(parents=True)
        (d / "note.md").write_text(text, encoding="utf-8")
        return load_exclusions(d.parent)[0]

    DECL = "<!-- excluded-from-consumption: subject=BAN class=5 chapter=12 cd=CD-127 -->"
    excl_cases += [
        ("a STANDALONE declaration comment is read — the mint",
         lambda: len(_load_from(f"# note\n\n{DECL}\n")) == 1),
        ("the SAME string quoted inside a table row is NOT read — a CD row that shows the form "
         "must not mint an exclusion (AGENTS §5.1, ledger_check's mint-vs-cite anchor)",
         lambda: _load_from(f"| CD-131 | 2026-08-14 | the form is `{DECL}` | cites |\n") == []),
        ("the same string inside a FENCED BLOCK is NOT read — P-035's policy clause has to be "
         "able to print its own convention",
         lambda: _load_from(f"# clause\n\n```\n{DECL}\n```\n") == []),
    ]

    for label, fn in excl_cases:
        try:
            passed = bool(fn())
        except Exception as e:                                   # noqa: BLE001
            passed, label = False, f"{label} — raised {e!r}"
        print(f"  {'PASS' if passed else 'FAIL'}  {'SOURCE-EXCLUSION':<16} {label}")
        ok = ok and passed

    # --- CD-130(a): the chapter resolver, seeded BOTH directions on synthetic strings only.
    # Without these the rewrite of the `str(int(unit))` line is an assertion, not a proof — and
    # the one thing CD-088 keeps demonstrating is that this defect is invisible until it is run.
    PAD_FIX = "# পাঠ ০৯ — padded\nপ্যাডেড অংশের লেখা\n\n# পাঠ ৯ — unpadded\nআনপ্যাডেড অংশের লেখা\n"
    pad_cases = [
        ("`U09` and `U9` are TWO chapters when the extraction prints both — not merged",
         lambda: (qb_resolve_chapter(PAD_FIX, "09")[0].strip().startswith("প্যাডেড")
                  and qb_resolve_chapter(PAD_FIX, "9")[0].strip().startswith("আনপ্যাডেড"))),
        ("an EXACT match reports no note — the fallback stays out of the way",
         lambda: qb_resolve_chapter(PAD_FIX, "09")[1] is None),
        ("`U09` against an extraction printing only `পাঠ ৯` resolves on the unpadded spelling "
         "AND says so (P-034 evidence is printed, not absorbed)",
         lambda: (lambda r: r[0].strip() == "লেখা" and r[1] is not None
                  and "NOT merged" in r[1])(qb_resolve_chapter("# পাঠ ৯ — unpadded\nলেখা\n", "09"))),
        ("the fallback runs ONLY for a padded token: `U9` against a padded-only extraction "
         "does not silently grab `পাঠ ০৯`",
         lambda: qb_resolve_chapter("# পাঠ ০৯ — padded\nলেখা\n", "9")[1] is None),
        ("a unit with no section at all falls back to the whole file, as before",
         lambda: qb_resolve_chapter("# পাঠ ৭ — অন্য\nলেখা\n", "21")[0].startswith("# পাঠ ৭")),
    ]
    for label, fn in pad_cases:
        try:
            passed = bool(fn())
        except Exception as e:                                   # noqa: BLE001
            passed, label = False, f"{label} — raised {e!r}"
        print(f"  {'PASS' if passed else 'FAIL'}  {'CHAPTER-RESOLVE':<16} {label}")
        ok = ok and passed

    print(f"SELFTEST RESULT: {'PASS' if ok else 'FAIL'} ({len(cases)} seeded errors + "
          f"{len(excl_cases)} CD-131 exclusion cases + {len(pad_cases)} CD-130(a) resolver cases "
          f"+ 1 baseline)")
    return ok


# =================================================================================
# SELFTEST — §6 family
# =================================================================================

SYNTH_EXTRACTION = """
# পাঠ ৯৯ — কল্পিত পাঠ (SYNTHETIC FIXTURE — this chapter does not exist in any book)

আকাশে একটি নীল ঘুড়ি উড়ছিল ধীরে ধীরে।
ছোট্ট মেয়েটি জানালা দিয়ে সেই ঘুড়ি দেখছিল অনেকক্ষণ।
বাতাস থেমে গেলে ঘুড়িটি নিচে নেমে এল গাছের ডালে।
মেয়েটি তখন উঠোনে গিয়ে ঘুড়িটিকে নামিয়ে আনল।
সন্ধ্যার আগে সে ঘুড়িটি আবার আকাশে ওড়াল।
পাখিরা সারাদিন আকাশে ওড়ে আর সন্ধ্যায় ঘরে ফেরে।
নদীর ধারে একটি পুরানো নৌকা বাঁধা ছিল দড়ি দিয়ে।
"""

SYNTH_TOPICS = ["TOP-BAN-C5-05", "TOP-BAN-C5-01"]

SYNTH_SLUGS = {"BAN-POEM", "BAN-VOCAB", "BAN-SENTENCE"}

SYNTH_SLOTS = ["S02", "S05", "S07", "S08"]

def _qp_rubric():
    return {"bands": ["ভালো", "মোটামুটি"],
            "criteria": [
                {"role": "content", "criterion": "বিষয়বস্তু",
                 "band_descriptors": {"ভালো": "সব পয়েন্ট আছে", "মোটামুটি": "কিছু পয়েন্ট আছে"}},
                {"role": "islamic_alignment", "criterion": "ইসলামি মূল্যবোধের সঙ্গে সংগতি",
                 "band_descriptors": {"ভালো": "পুরোপুরি সংগত", "মোটামুটি": "আংশিক সংগত"}},
            ]}

def _qp_good_bank():
    """A synthetic chapter bank that passes all eleven. 24 items — above REF-09 §4.3's floor of 20.

    Composition sits inside REF-06 §3.6's SIX bands (CD-121/Q-1) and supplies the easy floor:
    6 Remember (25.0%), 8 Understand (33.3%), 6 Apply (25.0%), 3 Analyze (12.5%), 1 Evaluate
    (4.2%), 0 Create (0%); easy 10 (41.7%), medium 10, hard 4.

    THE FIXTURE HAS BEEN RE-CUT TWICE, BOTH TIMES BECAUSE THE GATE WAS RIGHT. Recorded, not
    quietly fixed, because the direction of the correction is the whole discipline:

      1. The first draft sat at 9 Remember (37.5%) and reddened the জ্ঞান ceiling.
      2. When Q-1 was ruled and the band moved from four NAPE domains to REF-06's six Bloom
         levels, Analyze fell to 8.3% against a 10–20% floor. The composition was re-cut to
         6/8/6/3/1/0; **the band was not widened to admit the fixture.**

    Widening a band to admit a fixture shapes the gate to pass its own test — CD-055 / CD-064(f)'s
    hazard one level up, and the reason this session authors no bank content.
    """
    anchors = [
        "আকাশে একটি নীল ঘুড়ি", "উড়ছিল ধীরে ধীরে", "ছোট্ট মেয়েটি জানালা দিয়ে",
        "সেই ঘুড়ি দেখছিল অনেকক্ষণ", "বাতাস থেমে গেলে ঘুড়িটি", "নিচে নেমে এল গাছের ডালে",
        "মেয়েটি তখন উঠোনে গিয়ে", "ঘুড়িটিকে নামিয়ে আনল", "সন্ধ্যার আগে সে ঘুড়িটি",
        "আবার আকাশে ওড়াল", "পাখিরা সারাদিন আকাশে ওড়ে", "সন্ধ্যায় ঘরে ফেরে",
        "নদীর ধারে একটি পুরানো নৌকা", "বাঁধা ছিল দড়ি দিয়ে",
    ]
    blooms = (["Remember"] * 6 + ["Understand"] * 8 + ["Apply"] * 6
              + ["Analyze"] * 3 + ["Evaluate"] * 1)
    diffs = (["easy"] * 10 + ["medium"] * 10 + ["hard"] * 4)
    qs, pool, slot_idx, src_idx = [], {"HW": [], "AS": [], "CT": []}, {}, {}
    for i in range(24):
        qid = f"QP-BAN-C5-U99-Q{i + 1:02d}"
        # S05 is বহুনির্বাচনি (mcq); S02 শব্দার্থ and S07 সংক্ষিপ্ত are short; S08 is descriptive.
        if i < 6:
            slot, qtype, role, marks = "S05", "mcq", "mcq", 1
        elif i < 12:
            slot, qtype, role, marks = "S02", "short_answer", "short", 1
        elif i < 20:
            slot, qtype, role, marks = "S07", "short_answer", "short", 2
        else:
            slot, qtype, role, marks = "S08", "descriptive", "creative", 5
        q = {
            "qid": qid,
            "topic_tag": SYNTH_TOPICS[i % 2],
            "ref19_topic_id": "BAN-POEM" if i % 2 == 0 else "BAN-VOCAB",
            "question_text": f"কল্পিত প্রশ্ন {i + 1} — ঘুড়ি ও পাখি নিয়ে সংখ্যা {i + 1}",
            "question_type": qtype, "paper_role": role,
            "bloom_level": blooms[i], "difficulty": diffs[i], "tier": "tier1", "marks": marks,
        }
        if qtype == "mcq":
            q["options"] = [{"text": "প্রথম", "correct": True},
                            {"text": "দ্বিতীয়", "correct": False, "why_wrong": "ভুল"},
                            {"text": "তৃতীয়", "correct": False, "why_wrong": "ভুল"}]
        elif qtype == "short_answer":
            q["answer_key"] = f"উত্তর {i + 1}"
        else:
            q["rubric"] = _qp_rubric()
        qs.append(q)
        slot_idx[qid] = slot
        src_idx[qid] = anchors[i % len(anchors)]
        pool[["HW", "AS", "CT"][i % 3]].append(qid)
    return {
        "bank_id": "SYNTH-BAN-C5-U99", "subject": "BAN", "class": 5, "chapter": "U99",
        "header": {"target": 24,
                   "reason": "synthetic fixture sized to exercise all eleven gates",
                   "topics": SYNTH_TOPICS, "spine_slots": SYNTH_SLOTS},
        "pool_index": pool, "slot_index": slot_idx, "source_index": src_idx,
        "questions": qs,
    }

def _qp_ctx():
    """A synthetic context. The REF-19 and TOPIC_NUMBERS registers are STUBBED for the qp_selftest so
    the instrument is proven against fixtures rather than against the live canon files — the same
    discipline the fixtures themselves follow."""
    return {"extraction": SYNTH_EXTRACTION,
            "ref19_slugs": SYNTH_SLUGS,
            "topic_numbers": set(SYNTH_TOPICS) | {"TOP-BAN-C5-07"}}

def _qp_set_blooms(b, seq):
    """Assign an exact Bloom distribution across the 24-item fixture.

    Added at CD-135 so the floor cases are stated as distributions rather than as mutations
    whose effect a reader has to simulate. `seq` is padded with `Create` — floor 0 — so a short
    list is a declaration about the levels it names and not an accident about the rest.
    """
    qs = b["questions"]
    seq = list(seq) + ["Create"] * (len(qs) - len(seq))
    for q, lvl in zip(qs, seq):
        q["bloom_level"] = lvl
    return b

def _qp_mutate(fn):
    b = json.loads(json.dumps(_qp_good_bank()))
    fn(b)
    return b

def qp_selftest():
    print("SELFTEST — the instrument is proven before any bank verdict (CD-025). "
          "Synthetic fixtures only; no canon/sources or canon/marklogic file is read as fixture "
          "data (CD-055, CD-064(f)).")
    ok = True
    ctx = _qp_ctx()

    clean, _ = qp_run(_qp_good_bank(), ctx, quiet=True)
    if clean:
        print(f"  FAIL  baseline: the synthetic bank is not clean -> {clean}")
        ok = False
    else:
        print("  PASS  baseline: an unbroken synthetic chapter bank passes all eleven")

    cases = []

    def add(gate, label, fn, ctx_override=None):
        cases.append((gate, label, _qp_mutate(fn), ctx_override))

    # --- one seeded failure per gate, in §6 order -------------------------------------
    add("MARK-VALUE", "an S05 mcq carrying 5 marks instead of the spine's 1",
        lambda b: b["questions"][0].update({"marks": 5}))
    add("SOURCE-TRACE", "an anchor that appears nowhere in the extraction",
        lambda b: b["source_index"].update(
            {"QP-BAN-C5-U99-Q01": "এই বাক্যটি পাঠে কোথাও নেই একেবারেই"}))
    add("SCRIPT-GUARD", "tier-1 Arabic script in a stem",
        lambda b: b["questions"][0].update({"question_text": "بسم শব্দের অর্থ কী"}))
    add("REF19-SLUG", "a ref19_topic_id that is in no REF-19 row",
        lambda b: b["questions"][0].update({"ref19_topic_id": "BAN-NOTASLUG"}))
    add("TOPIC-NUMBER", "an unminted topic_tag — must FAIL and must not auto-mint",
        lambda b: b["questions"][0].update({"topic_tag": "TOP-BAN-C5-99"}))
    add("KEY-RUBRIC", "a descriptive item whose rubric has one band",
        lambda b: b["questions"][20]["rubric"].update({"bands": ["ভালো"]}))
    add("BLOOM-BAND", "every item becomes Remember — every OTHER level drops under its floor "
                      "(CD-135: the floors are what bind a pool, not the ceilings)",
        lambda b: [q.update({"bloom_level": "Remember"}) for q in b["questions"]])
    add("BLOOM-BAND", "Analyze falls to 1 of 24 = 4.2%, under REF-06 §3.6's 10% floor — the exact "
                      "case CD-135(h) predicts becomes the binding constraint once the ceiling "
                      "stops binding",
        lambda b: _qp_set_blooms(b, ["Remember"] * 8 + ["Understand"] * 8 + ["Apply"] * 7
                                    + ["Analyze"] * 1))
    add("DIFFICULTY", "the pool cannot supply easy ≥30%",
        lambda b: [q.update({"difficulty": "medium"}) for q in b["questions"]])
    add("REPETITION", "an identical stem on two Understand items",
        lambda b: b["questions"][10].update(
            {"question_text": b["questions"][11]["question_text"]}))
    add("COVERAGE", "a declared spine slot that no item supplies",
        lambda b: b["header"]["spine_slots"].append("S15"))
    add("DOMAIN-RATIO", "an annual paper that is entirely জ্ঞান",
        lambda b: b.update({"papers": [
            {"paper_id": "SYNTH-ANNUAL", "kind": "annual",
             "items": [q["qid"] for q in b["questions"] if q["bloom_level"] == "Remember"]}]}))

    # --- extra seeds on the rows where §6 is most specific ----------------------------
    add("KEY-RUBRIC", "a descriptive item with no islamic_alignment criterion row",
        lambda b: b["questions"][20]["rubric"].update(
            {"criteria": [b["questions"][20]["rubric"]["criteria"][0]]}))
    add("KEY-RUBRIC", "an mcq that also carries a rubric — the schema forbids the others",
        lambda b: b["questions"][0].update({"rubric": _qp_rubric()}))
    add("KEY-RUBRIC", "a criterion with no descriptor for one of the declared bands",
        lambda b: b["questions"][20]["rubric"]["criteria"][1]["band_descriptors"].pop("মোটামুটি"))
    add("SOURCE-TRACE", "a one-word anchor — short enough to match anything",
        lambda b: b["source_index"].update({"QP-BAN-C5-U99-Q02": "ঘুড়ি"}))
    add("COVERAGE", "the bank header states no reason for its target",
        lambda b: b["header"].pop("reason"))
    add("COVERAGE", "a pool below REF-09 §4.3's floor of 20",
        lambda b: b.update({"questions": b["questions"][:12]}))

    print()
    for gate, label, broken, over in cases:
        c = dict(ctx)
        if over:
            c.update(over)
        fails, _ = qp_run(broken, c, quiet=True)
        fired = {g for g, _ in fails}
        if gate in fired:
            print(f"  PASS  {gate:<14} fires on: {label}")
        else:
            print(f"  FAIL  {gate:<14} DID NOT FIRE on: {label}")
            ok = False

    # --- NEGATIVE CASES: a gate that fires on everything is as useless as one that fires
    # --- on nothing. Each of these is a thing §6 or §5 explicitly PERMITS.
    print()
    negatives = [
        ("REPETITION", "a `Remember` stem repeated across HW · AS · CT — §5 permits it",
         lambda b: b["questions"][1].update({"question_text": b["questions"][0]["question_text"]})),
        ("REPETITION", "a `Remember` stem lifted verbatim from a CT into the annual — §5's "
                       "listed supersede of MarkLogic §৮'s row 2, and it runs BOTH directions",
         lambda b: b.update({"papers": [
             {"paper_id": "CT-1", "kind": "classtest", "items": [b["questions"][0]["qid"]]},
             {"paper_id": "ANN", "kind": "annual", "items": [b["questions"][1]["qid"]]}]}
         ) or b["questions"][1].update({"question_text": b["questions"][0]["question_text"]})),
        ("DOMAIN-RATIO", "a bank with NO papers — the ratio is paper level only and must not "
                         "fire on a pool (§6)",
         lambda b: None),
        ("DOMAIN-RATIO", "a SINGLE class test skewed all-জ্ঞান — never judged (§5: the ratio is "
                         "met across the year's tests, not within any one)",
         lambda b: b.update({"papers": [
             {"paper_id": "CT-ONLY", "kind": "classtest",
              "items": [q["qid"] for q in b["questions"] if q["bloom_level"] == "Remember"]}]})),
        ("BLOOM-BAND", "a pool banded flat against the CHAPTER band — §4 says that is correct; "
                       "only a session-scoped reading drifts low",
         lambda b: None),
        ("BLOOM-BAND", "a pool at Remember 9/24 = 37.5%, ABOVE REF-06 §3.6's 30% upper bound, "
                       "with every floor still clear — CD-135: a pool cannot fail a ceiling, "
                       "because an author declines the surplus and a compliant paper stays "
                       "constructible. This FAILED until 2026-08-15; it is KEPT AND INVERTED so "
                       "the symmetric check cannot creep back in unnoticed (CD-122(a)'s device)",
         lambda b: _qp_set_blooms(b, ["Remember"] * 9 + ["Understand"] * 6 + ["Apply"] * 6
                                     + ["Analyze"] * 3)),
        ("BLOOM-BAND", "a pool sitting EXACTLY on two floors — Understand 6/24 = 25.0% and "
                       "Apply 6/24 = 25.0% — the boundary is inclusive, so exactly-at-floor is "
                       "compliant and must not fire",
         lambda b: _qp_set_blooms(b, ["Remember"] * 6 + ["Understand"] * 6 + ["Apply"] * 6
                                     + ["Analyze"] * 6)),
        ("DIFFICULTY", "a pool at 70% easy — CAN-SUPPLY, not equality, so this passes",
         lambda b: [q.update({"difficulty": "easy"}) for q in b["questions"][:17]]),
        ("DIFFICULTY", "a pool that is 67% HARD while still holding easy ≥30% — CD-122: a pool "
                       "cannot fail a ceiling, because an author can decline to use hard items and "
                       "a compliant paper stays constructible. This was a SEEDED FAILURE until Q-2 "
                       "was ruled; it is kept, inverted, so the symmetric check cannot creep back "
                       "in unnoticed",
         lambda b: [q.update({"difficulty": "hard"}) for q in b["questions"][8:]]),
    ]
    for gate, label, fn in negatives:
        broken = _qp_mutate(fn)
        fails, _ = qp_run(broken, ctx, quiet=True)
        if any(g == gate for g, _ in fails):
            print(f"  FAIL  {gate:<14} WRONGLY FIRES on: {label}")
            print("        " + "; ".join(e for g, e in fails if g == gate))
            ok = False
        else:
            print(f"  PASS  {gate:<14} stays quiet on: {label}")

    # --- CD-055 self-declaration for part-authored banks, seeded BOTH directions -------
    # The load-bearing case is the fourth: the marker must buy the control exclusion and
    # NOTHING ELSE. A version of this that quieted a gate would be a waiver, which is the one
    # thing CD-055 says it is not.
    print()

    def _marked(detail="S02/S05 authored; S07/S08 not; resume at Q13"):
        b = _qp_good_bank()
        b["header"]["অবস্থা"] = f"{MARKER} — {detail}"
        return b

    decl = []

    def dcheck(label, cond):
        decl.append(cond)
        print(f"  {'PASS' if cond else 'FAIL'}  DECLARE        {label}")

    in_ctl, reason = classify(Path("synthetic.json"), _marked())
    dcheck(f"a bank declaring {MARKER} is held OUT of the controls, and the reason names the "
           f"resume point", (not in_ctl) and "resume at Q13" in reason)

    in_ctl, reason = classify(Path("synthetic.json"), _qp_good_bank())
    dcheck("stays quiet on: a finished, unmarked, §4-shaped bank — it IS a control",
           in_ctl and reason.startswith("CONTROL"))

    b = _qp_good_bank()
    b["header"]["অবস্থা"] = MARKER
    in_ctl, reason = classify(Path("synthetic.json"), b)
    dcheck(f"a bare `{MARKER}` with no resume tail is REFUSED, not silently skipped",
           (not in_ctl) and reason.startswith("REFUSED"))

    broken_marked = _marked()
    broken_marked["questions"][0]["topic_tag"] = "TOP-BAN-C5-99"
    f_marked, _ = qp_run(broken_marked, ctx, quiet=True)
    dcheck("THE MARKER IS NOT A WAIVER — every gate still runs on a marked bank and TOPIC-NUMBER "
           "still reports it red",
           "TOPIC-NUMBER" in {g for g, _ in f_marked})

    f_unmarked, _ = qp_run(_qp_good_bank(), ctx, quiet=True)
    dcheck("and it changes no verdict: marked and unmarked copies of the same clean bank give "
           "byte-identical gate output",
           qp_run(_marked(), ctx, quiet=True)[0] == f_unmarked == [])

    b = _qp_good_bank()
    b["header"]["অবস্থা"] = "সম্পূর্ণ"
    in_ctl, reason = classify(Path("synthetic.json"), b)
    dcheck(f"an `অবস্থা` carrying some other word is REFUSED — §7.9 defines exactly one marker",
           (not in_ctl) and reason.startswith("REFUSED"))

    ok = ok and all(decl)

    print(f"\nSELFTEST RESULT: {'PASS' if ok else 'FAIL'} "
          f"({len(cases)} seeded failures + {len(negatives)} negatives + {len(decl)} "
          f"CD-055 declaration cases + 1 baseline, across all {sum(1 for _, i, _ in GATES if 'qp6' in i)} gates)")
    return ok


def main():
    print("SELFTEST — both families, before any verdict (CD-025). Synthetic fixtures only; no "
          "canon/sources or canon/marklogic file is read as fixture data.\n")
    print("--- QUESTION_BANK_POLICY §5 family "
          + "-" * 44)
    a = qb_selftest()
    print("\n--- canon/QUESTION_POLICY §6 family "
          + "-" * 43)
    b = qp_selftest()
    if not (a and b):
        print("\nRESULT: FAIL (selftest red — no bank verdict is believable, nothing was judged)")
        sys.exit(1)
    print(f"\nSUITE: {len(GATES)} gates "
          f"({len(QP6_POLICY_GATES)} carry a QUESTION_POLICY §6 row, "
          f"{sum(1 for _, i, a in GATES if 'qb' in i and a.startswith('§'))} a "
          f"QUESTION_BANK_POLICY §5 row, "
          f"{sum(1 for _, i, a in GATES if len(i) == 2 and a.startswith('§'))} both, "
          f"{sum(1 for _, _, a in GATES if not a.startswith('§'))} from a decision row "
          f"with no § of its own — CD-131)")
    live_excl, live_excl_err = load_exclusions(ROOT)
    for e in live_excl_err:
        print(f"  WARN  SOURCE-EXCLUSION declaration: {e}")
    print(f"CONSUMPTION EXCLUSIONS IN FORCE: {len(live_excl)}"
          + ("" if not live_excl else " — " + " · ".join(
              f"{d['subject']}-C{d['class']}-chapter {d['chapter']} ({d['cd']}, {d['_file']})"
              for d in live_excl)))

    if len(sys.argv) < 2:
        fails = sweep(ROOT, None)
        print(f"\nRESULT: {'FAIL' if fails else 'CLEAN'} ({len(fails)} failures)")
        sys.exit(1 if fails else 0)
    path = Path(sys.argv[1])
    bank = json.loads(path.read_text(encoding="utf-8"))
    print(f"\nBANK: {path}   [shape: {bank_shape(bank) or 'unrecognised'}]")
    fails, report = run(bank)
    for gate, line in report:
        print(f"  REPORT  {gate:<18} {line}")
    print(f"RESULT: {'FAIL' if fails else 'CLEAN'} ({len(fails)} failures)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
