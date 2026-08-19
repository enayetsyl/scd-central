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
| BLOOM-BAND          | §6 row 7 — CD-121 for the axis (REF-06 §3.6 only; UD-23), **CD-171 for the verdict: REPORT ONLY at pool level**. The `bloom_level` TAG is required and an unknown level FAILs; no distribution does. Both bounds are a PAPER rule (CD-135 superseded) |
| DIFFICULTY          | §6 row 8, as ruled by CD-122 (easy floor only) |
| REPETITION          | §6 row 9 |
| COVERAGE            | §6 row 10 — reads the SLOT REGISTER (CD-138); the header fallback of CD-122(b) is spent |
| DOMAIN-RATIO        | §6 row 11 — **paper level only; the per-pool form is retired** |
| ANSWER-SHAPE        | QB_POLICY §5 |
| RUBRIC-SPECIFICITY  | QB_POLICY §5 |
| FLAG-TRACE          | QB_POLICY §5 (QB-D-012's synthetic-queue rule) |
| QUOTE-VERBATIM      | QB_POLICY §5 (KEEP-AS-IS / PROTECTED) |
| HONORIFIC           | QB_POLICY §5 (extraction, বিশেষ নির্দেশ) |
| AS-MIX              | QB_POLICY §5 (QB-D-004) |
| NUMERALS            | QB_POLICY §5 (LANGUAGE_RULES §2) |
| CEILING             | QB_POLICY §5 (QB-D-002) — REPORT ONLY |
| ENVELOPE-SYNC       | AGENTS §11 · Principal ruling 2026-08-15 — no § row of its own |

11 from §6 · 14 from §5 · 4 shared names ⇒ 21, **plus two that execute a RULING rather than a
policy clause: SOURCE-EXCLUSION (CD-131) and ENVELOPE-SYNC ⇒ 23 gates.**

**ENVELOPE-SYNC is here because every other gate in this file reads the BANK, and AGENTS §11
imports the ENVELOPES.** `banks/envelopes/` sat two waves behind — 36 envelopes against 88 and
then 110 bank items — and nothing could see it, because the export path reads a file the gate
never opened. It would have shipped ten `S10 ভাব নির্ণয়` items into the Hub past COVERAGE, the
gate built for exactly that defect.

SELFTEST FIRST, ALWAYS (CD-025). Both families' selftests run before any verdict. Every fixture is
synthetic and written for the test; the §6 family's chapter is a fictional পাঠ ৯৯ that exists in no
book. No file under canon/sources/ or canon/marklogic/ is read as fixture data.

  ⚠ On the fixture rule and its citation: `canon/QUESTION_POLICY.md` §6 cited this as
  "(CD-055, CD-064(f))" and **that citation was false** — corrected at CD-121, which also gives the
  rule a canon home and records the distinction the flat form had flattened: **controls may be
  drawn from the live pool (CD-051(d)); SEEDS may not (QB-D-012).** The seeds here are synthetic.

Exit 0 = CLEAN, 1 = FAIL. Paste output verbatim per AGENTS.md §5.
"""
import hashlib
import json
import os
import re
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

def _resolve_root():
    """Repo root. SCD_ROOT overrides; the committed-path default is unchanged.

    CD-175. parents[3] only resolves at this file's committed depth, so run_all.py
    exported SCD_ROOT to every child while gates.py ignored it.

    THE OVERRIDE IS VERIFIED, NOT TRUSTED. Eighteen sites read canon, the slot
    register, TOPIC_NUMBERS, PENDING_PRINCIPAL and live banks off this value, and
    two are inside the selftest. A wrong root would not error — it would read a
    different corpus and report PASS.
    """
    env = os.environ.get("SCD_ROOT")
    if not env:
        return Path(__file__).resolve().parents[3]
    p = Path(env).resolve()
    missing = [m for m in ("canon", "workstreams", "tools") if not (p / m).is_dir()]
    if missing:
        sys.stderr.write(
            f"gates.py: SCD_ROOT={p} does not look like scd-central "
            f"(missing: {', '.join(missing)}). REFUSED — no verdict reached (§7.17).\n")
        sys.exit(2)
    return p


ROOT = _resolve_root()
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

# RETIRED 2026-08-15 — `QB_SPINE_ITEM_MARKS` and `QP6_SPINE_ITEM_MARKS` were two hand-copied
# transcriptions of the same spine column, and CD-011's standing rule is that a registry is written
# from the artifact, never from a derived copy. They covered ("BAN", 5) ALONE, so MARK-VALUE
# reported *"no spine item-mark table vendored"* for every other class in the school — a refusal,
# correctly, but a refusal that would have had to be answered by hand-copying four more columns
# twice each. `canon/marklogic/SLOT_REGISTER.json` now carries `marks_per_item` per
# (subject, class, slot), proven against the spine by `tools/audits/slot_register_check.py`, so
# MARK-VALUE reads it. See `register_item_marks` below.

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

# CD-147 — S14 আবেদনপত্র and S15 রচনা are PAPER-LEVEL for EVERY chapter, categorically. They are
# authored only in the paper/exam pipeline and never enter a chapter bank, whatever the chapter's
# content happens to anchor. Two consequences the gate implements and one it deliberately does not:
#   · a chapter owes NO content reason for them — the exclusion is not a per-chapter declaration
#     any more, so COVERAGE stops requiring one and stops calling their absence INCOMPLETE;
#   · an item sitting in one, or a header ADMITTING one, FAILs categorically — a different error
#     from CD-138(e)'s "this chapter declared it inadmissible", because the chapter's declaration
#     is no longer what decides it;
#   · the register rows STAY. S14/S15 are real paper slots with real demand; what changed is which
#     pipeline authors them, not whether they exist. Deleting the rows would make the paper lane
#     unable to see its own slots.
# Supersedes CD-139's per-chapter reading of S14, পাঠ ৪ included, and restores CD-136(c)'s
# categorical form on wider ground than CD-136(c) itself claimed.
# CD-150 re-keys this constant to **(subject, class, slot)** and the reason is measured, not
# stylistic. The old form was a flat set of bare slot SHORTS — `{"S14", "S15"}` — tested as
# `slot in PAPER_LEVEL_SLOTS` with no subject and no class in hand. Three things were wrong with
# it the moment a second subject arrived:
#   · SUBJECT-BLIND. ENG's paper-level set is S05 · S13 · S14. `BAN-S05` is বহুনির্বাচনি (live D0,
#     5 marks, all five classes) and `BAN-S13` is এক কথায় প্রকাশ (live C3–C5). Adding those shorts
#     to a flat set would have barred BAN's MCQ slot and এক কথায় প্রকাশ from every chapter bank in
#     the repo — a categorical bar on two live teaching slots, on the strength of a ruling about
#     English.
#   · CLASS-BLIND. The ENG bar does not run the whole ladder: ENG-S05 is paper-level at C3–C5 and
#     ENG-S13/S14 only at C4–C5. Below those the class's admitted task is a **D4 substitute** —
#     C1 greeting fill-in-blanks, C2 self-introduction, C3 dialogue, C2/C3 guided paragraph — and a
#     D4 substitute is a DIFFERENT TASK, not a junior version of the paper's task. A flat set
#     cannot say that.
#   · SILENTLY WRONG ON ENG ALREADY. ENG has **no S15**; its রচনা is **S14** and its
#     চিঠি/আবেদনপত্র is **S13**. Run against an ENG bank, the old set would have barred ENG-S14
#     correctly BY COINCIDENCE, hunted an ENG-S15 that does not exist, and left ENG-S05 and
#     ENG-S13 wide open. Nothing would have failed; the bar would simply have missed.
# The pairs are ENUMERATED and are never inferred from `d_code` or `admitted_task` (Principal
# ruling 2026-08-16). A derived bar would move whenever a spine cell was re-coded, and the whole
# point of CD-147/CD-150 is that **a slot's pipeline is not a fact about content.**
PAPER_LEVEL_SLOTS = frozenset({
    # BAN — CD-147, unchanged in behaviour: S14 আবেদনপত্র and S15 রচনা at every class.
    ("BAN", 1, "S14"), ("BAN", 2, "S14"), ("BAN", 3, "S14"), ("BAN", 4, "S14"), ("BAN", 5, "S14"),
    ("BAN", 1, "S15"), ("BAN", 2, "S15"), ("BAN", 3, "S15"), ("BAN", 4, "S15"), ("BAN", 5, "S15"),
    # ENG — CD-150. S05 is the unseen passage and is textbook-EXTERNAL by the spine's own
    # statement, so no chapter can source it; C1/C2 carry no S05 at all (D5).
    ("ENG", 3, "S05"), ("ENG", 4, "S05"), ("ENG", 5, "S05"),
    # ENG-S13 চিঠি / আবেদনপত্র / ইমেইল and ENG-S14 রচনা — paper-level where the class's admitted
    # task IS the paper-level task. C1/C2/C3 S13 and C2/C3 S14 stay in the chapter lane.
    ("ENG", 4, "S13"), ("ENG", 5, "S13"),
    ("ENG", 4, "S14"), ("ENG", 5, "S14"),
})


def is_paper_level(subject, cls, slot):
    """Is THIS slot paper-level for THIS (subject, class)? The only way to ask the question.

    Replaces eight bare `slot in PAPER_LEVEL_SLOTS` membership tests. Every one of them had a
    subject and a class already in hand and threw both away.
    """
    return (subject, cls, slot) in PAPER_LEVEL_SLOTS


def paper_level_slots(subject, cls):
    """→ {slot shorts} barred for this (subject, class). For the set-algebra call sites."""
    return {s for (sub, c, s) in PAPER_LEVEL_SLOTS if sub == subject and c == cls}


# ── CD-165 + CD-166 · the বিরামচিহ্ন a class is TAUGHT, declared in the register, enforced on items ──
#
# The register declares the SET — `taught_set` at (BAN, C5, BAN-S11): দাঁড়ি · কমা · প্রশ্নচিহ্ন ·
# বিস্ময়চিহ্ন · উদ্ধরণ চিহ্ন — and `tools/audits/slot_register_check.py` proves its shape and holds the
# closed literal of WHICH rows may declare one. This half asks the question only a bank can answer:
# does any item REQUIRE a mark the class is not taught?
#
# TAUGHT_SET_REQUIRED is why absence cannot pass quietly. For these cells a missing `taught_set` is a
# FAILURE, not a waiver: read the other way the mechanism would be worse than nothing, because the one
# cell whose marks went unchecked would be the cell nobody declared, and the remedy for a failing bank
# would be to delete its declaration.
#
# THIS GATE IS EXPECTED TO FAIL TWO ITEMS, AND THAT IS RECORDED BEFORE IT LANDED (CD-169). `U15 Q75`
# requires ড্যাশ and `Q81` requires সেমিকোলন; both are barred, both are the poem's own typography, and
# both are retained ONLY because retiring them drops পাঠ ১৫'s Apply margin below the rule. A gate that
# reddens on a RECORDED exception is acceptable; one that reddens on an unwritten state is not.
TAUGHT_SET_REQUIRED = frozenset({("BAN", 5, "S11")})

# ── CD-172 · THE NAMED EXCLUSION FROM CD-153's REPO-WIDE-GREEN PUSH CONDITION ──────────────
#
# TWO ITEM IDS, AND NOTHING ELSE. `QP-BAN-C5-U15-Q75` requires ড্যাশ and `QP-BAN-C5-U15-Q81`
# requires সেমিকোলন; both marks are barred at C5 (CD-165, amended by CD-166) and both items are
# therefore genuinely defective. They are RULED RETAINED (CD-169) and CD-170 permits NO in-repo
# fixing of পাঠ ১৩ · ১৪ · ১৫ · ১৬, so the repo cannot dispose of them: the disposition is the
# Hub's under CD-142(a), carried there by `P039_HUB_HANDOFF_MANIFEST_2026-08-18.txt`.
#
# THIS IS AN EXCLUSION FROM THE PUSH CONDITION, NOT A REPAIR AND NOT A PARDON. The items are still
# defective, the finding is not retracted, and CD-169(b)'s *retained as DEFECTIVE, not as
# acceptable* is unchanged. What CD-172 removes is a repo-wide-green stop that no permitted action
# can clear — CD-153's own (g)(i) accepts that the lane may stop on FAILs it did not cause, but a
# red nobody is ALLOWED to fix is a different object from a red nobody has fixed yet.
#
# KEYED BY ITEM ID, DELIBERATELY, AND A GATE-LEVEL OR CHECK-LEVEL EXCLUSION IS EXPRESSLY REFUSED
# (Principal, CD-172). The taught-set check goes on failing normally everywhere else, including on
# any other item in this same bank and this same slot. Excluding the CHECK would have made every
# future taught-set defect invisible to buy two items' silence.
#
# A CLOSED LITERAL IN THE GATE, NEVER A FIELD IN THE BANK — the fourth time in this repo and the
# same reason each time (CD-137's laundering finding · CD-150(d)'s HALF_MARK_ADMITTED · CD-165(c)'s
# TAUGHT_SET_DECLARABLE): a bank that could declare its own exclusion would carry the PERMISSION
# beside the DEFECT, and the rule would be unfalsifiable by construction. The item whose mark is
# barred is the last artifact entitled to say the bar does not apply to it.
#
# REPORTED BY NAME ON EVERY RUN, NEVER A SILENT SKIP. Three lines print each run: which ids are
# excluded, which of them ACTUALLY exercised the exclusion this run, and which did not. The last
# is the discharge signal — see below.
#
# DISCHARGE IS AUTOMATIC AND THIS ROW CITES ITS OWN EXPIRY. **When the Hub disposes of both items,
# the exclusion is removed and CD-172 is spent.** The observable condition is that neither id
# exercises the exclusion any more — because the items were retired, re-stemmed at the Hub's
# instruction, or the taught set changed under a later row. `UNEXERCISED` in the report IS the
# expiry notice, and it prints on the run it first becomes true rather than waiting for someone to
# check. CD-160's finding is why this half exists: a list drifts from the class it describes, and
# an exclusion nobody re-examines is how a carve-out becomes the rule.
CD172_TAUGHT_SET_EXCLUDED = frozenset({
    "QP-BAN-C5-U15-Q75",     # requires ড্যাশ — CD-169(b)
    "QP-BAN-C5-U15-Q81",     # requires সেমিকোলন — CD-169(b)
})

# The marks BY CHARACTER, and the two drafts this replaced are recorded because each failed in a way a
# reader would not predict (CD-169(e)):
#   * DRAFT 1 scanned mark NAMES in the item's prose. It cannot tell REQUIRES from FORBIDS, and it
#     failed `U16 Q78` for a note reading "ড্যাশের দরকার নেই" — for saying the mark is NOT needed. The
#     review prompt has to state that distinction in words ("a rubric row which forbids barred content
#     is not an occurrence"); characters do not need to be told.
#   * DRAFT 2 scanned characters in the accepted answers JOINED. It cannot see per-variant structure,
#     and it failed `U14 Q67`, whose first key mirrors the section's dash while its second is
#     comma-only — a student writing the comma form is right, so the dash is not REQUIRED.
# হাইফেন and ইলেক are deliberately absent: a hyphen inside যুদ্ধ-জাহাজ or মরণ-যন্ত্রণা is ORTHOGRAPHY,
# not punctuation a student inserts, and counting it would fail every item that quotes a compound word.
MARK_CHARS = {
    "দাঁড়ি": ("।",),
    "কমা": (",",),
    "প্রশ্নচিহ্ন": ("?",),
    "বিস্ময়চিহ্ন": ("!",),
    "উদ্ধরণ চিহ্ন": ("'", "\u2018", "\u2019", "\u201c", "\u201d", '"'),
    "সেমিকোলন": (";",),
    "কোলন": (":",),
    "ড্যাশ": ("\u2014", "\u2013"),
}


def _marks_in(text):
    return {canon for canon, chars in MARK_CHARS.items() if any(c in text for c in chars)}


def marks_required_by(q, admitted):
    """→ ({marks outside `admitted` that EVERY accepted variant needs}, index of a clean variant | None).

    REQUIRED means every route to full marks needs it. Answer strings only — `accepted` and
    `blanks.accepted`; not the stem, whose marks are GIVEN rather than asked for, and not the note,
    because prose about a mark contains no mark.
    """
    ak = q.get("answer_key") or {}
    variants = [a for a in (ak.get("accepted") or []) if isinstance(a, str)]
    for b in (q.get("blanks") or []):
        variants += [a for a in (b.get("accepted") or []) if isinstance(a, str)]
    if not variants:
        return set(), None
    per = [_marks_in(v) - set(admitted) for v in variants]
    for i, off in enumerate(per):
        if not off:
            return set(), i
    return set().union(*per), None

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


def register_item_marks(ctx, subject, cls):
    """→ ({slot: marks_per_item}, refusal-or-None), read from CD-138's register.

    ONE SOURCE, TWO CALLERS. MARK-VALUE exists once per bank shape and both implementations now
    read this. The two vendored tables it replaces were transcriptions of the same spine column,
    kept in sync by hand — which is the failure CD-011 names: *a registry is written from the
    actual artifact, never from a summary or a derived copy.*

    THE REGISTER IS NOT A SPINE FILE, and that distinction is the whole reason this is allowed.
    CD-138(b) keeps every gate away from `MarkLogic_*_Spine.md` so no gate can read a header marker
    string. The register is DECLARED data, proven against the spine at build time by
    `tools/audits/slot_register_check.py`. Reading it is what CD-138 built it for.

    D5 and D6 rows are already filtered out by `load_slot_register`, so a bank item sitting in a
    slot its class does not carry falls through to the per-item "not in the register" error rather
    than being silently compared against a mark that does not exist.
    """
    if ctx and "slot_register" in ctx and ctx["slot_register"]:
        register = ctx["slot_register"]
    else:
        register, errs = load_slot_register(ROOT)
        if errs:
            return None, "; ".join(errs)
    # D5/D6 filtered HERE as well as in the loader, and the selftest is why: `_synth_register()`
    # supplies them unfiltered on purpose, so a caller that builds a register another way is the
    # normal case rather than the exotic one. Without this, a D6 row's `marks_per_item: null`
    # turned the whole class into a REFUSAL and MARK-VALUE stopped judging a bank it could judge
    # perfectly well — a gate silenced by a row it should never have been reading.
    table = {s: r.get("marks_per_item") for (sub, c, s), r in register.items()
             if sub == subject and c == cls and r.get("d_code") not in ("D5", "D6")}
    if not table:
        return None, (f"the slot register carries no rows for {subject} C{cls} — a mark cannot be "
                      f"checked against a column that has not been built (CD-138). Not judged, "
                      f"not assumed clean")
    missing = sorted(s for s, v in table.items() if v is None)
    if missing:
        return None, (f"{subject} C{cls} register rows carry no `marks_per_item` at "
                      f"{', '.join(missing)} — the value MARK-VALUE reads is absent, so no verdict "
                      f"is given")
    return table, None


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
    table, refusal = register_item_marks(ctx, key[0], key[1])
    if refusal:
        return [refusal]
    slots = bank.get("slot_index") or {}
    for q in bank.get("questions", []):
        qid = q.get("qid")
        slot = slots.get(qid)
        if not slot:
            errs.append(f"{qid}: no slot_index entry — every item names its MarkLogic slot")
            continue
        if slot not in table:
            errs.append(f"{qid}: slot '{slot}' is in no {key[0]} C{key[1]} register row — either "
                        f"the slot is wrong or the class does not carry it (CD-138)")
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
    table, refusal = register_item_marks(ctx, key[0], key[1])
    if refusal:
        return [], [refusal]
    slots = bank.get("slot_index") or {}
    for q in bank["questions"]:
        qid = q.get("qid")
        slot = slots.get(qid)
        if not slot:
            errs.append(f"{qid}: no spine slot in slot_index — a mark cannot be checked against a "
                        f"slot the bank does not name")
            continue
        if slot not in table:
            errs.append(f"{qid}: slot '{slot}' is in no {key[0]} C{key[1]} register row — either "
                        f"the slot is wrong or the class does not carry it (CD-138)")
            continue
        want, got = table[slot], q.get("marks")
        if got != want:
            errs.append(f"{qid}: slot {slot} carries {want} marks per item in the register, "
                        f"item declares {got}")
    rep.append(f"{len(bank['questions'])} items checked against the SLOT REGISTER's "
               f"{key[0]} C{key[1]} rows (CD-138 — the vendored mark table is retired)")
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
    """§6 row 7 — Bloom at POOL level is REPORT ONLY (CD-171(d), superseding CD-135).

    WHAT STILL FAILS: an item whose `bloom_level` is missing or is not one of the six LOCKED
    levels. **The tag is required; the distribution is not.** CD-171(b): Bloom levels are
    RECORDED, NOT RATIONED.

    WHAT NO LONGER FAILS: every per-level count against REF-06 §3.6. **Neither bound binds a
    pool.** The counts are still printed on every run, for the reason CD-135(f) gave and CD-171
    does not disturb — a report that always prints is what makes the gate's shape visible rather
    than something a reader has to infer from the code.

    ⚠ DO NOT RESTORE EITHER BOUND. The ceiling went at CD-135 and the floor at CD-171, and the
    two seeded negatives below are kept and inverted so neither can creep back unnoticed: a pool
    ABOVE an upper bound must stay quiet, and a pool BELOW a floor must ALSO stay quiet.

    WHY THE FLOOR WENT, in one line, because the docstring below is now history and reads as
    live rule: a floor exists so a compliant PAPER stays constructible, and **a paper composes
    across chapters while a pool is one chapter.** Charging every chapter with the whole paper's
    distribution made a thin chapter fail for being thin — `PENDING-P-036`'s finding, closed
    moot by CD-171(f).

    ── HISTORY BELOW THIS LINE (CD-121, CD-135). Kept unedited so a reader arriving by an old
    ── citation sees what changed and in what order. It is not the live rule.

    §6 row 7 — Bloom at POOL level: REF-06 §3.6's LOWER BOUNDS ONLY, read at CHAPTER scope.

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
    # NO FLOOR BRANCH AND NO CEILING BRANCH. CD-171(d): a pool is not banded, floored or capped.
    # The counts below are computed only so they can be PRINTED. See the docstring's ⚠.
    under = [f"{lvl} {counts[lvl]}/{total}={pct(counts[lvl], total):.1f}% vs {lo}%"
             for lvl, (lo, _hi) in REF06_C3_5.items() if pct(counts[lvl], total) < lo]
    rep.append("POOL check is REPORT ONLY (CD-171(d), superseding CD-135; CD-121/UD-23 for the "
               "axis, unamended — MarkLogic §৩ is the PAPER's axis and is not read here). "
               "NEITHER bound binds a pool. Both bind the PAPER, which composes across chapters, "
               "and no single chapter owes a paper's distribution. The `bloom_level` TAG is still "
               "required on every item and an unknown level still FAILs — recorded, not rationed.")
    if under:
        rep.append("levels below REF-06 §3.6's C3–5 indicative lower bound — PRINTED, NOT "
                   "FAILED, and §3.6 calls its own ranges *only indicative*: " + " · ".join(under))
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

def load_slot_register(root):
    """→ ({(subject, class, slot_short): row}, [errors]). The register is CD-138's data.

    THE ONE THING THIS LOADER MUST NOT DO, stated here because it is the whole ruling: it reads
    `canon/marklogic/SLOT_REGISTER.json` and NOTHING ELSE. **No spine file is opened anywhere in
    this suite.** CD-138(b) forbids a gate deriving task mode, admitted-set membership or set
    cardinality from a header marker string (যেকোনো একটা · অথবা · বা · ও · + · ভেঙে), and the
    cheapest way to guarantee a gate cannot read a surface is to give it no path to the file the
    surface lives in. The spine parse lives in `tools/audits/slot_register_check.py`, at build
    time, where it is proven and pasted — not here.
    """
    path = root / "canon" / "marklogic" / "SLOT_REGISTER.json"
    if not path.exists():
        return {}, [f"{path} not found — CD-138's register is the coverage authority and is absent"]
    try:
        reg = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001 - the reason must reach the report, not a traceback
        return {}, [f"{path} is unreadable: {e}"]
    out, errs = {}, []
    for r in reg.get("rows", []):
        if "chapter_authorable" in r:
            errs.append(f"{r.get('slot')}: the register carries an AUTHORED `chapter_authorable` — "
                        f"CD-138(f) makes it DERIVED from per-chapter declarations, never authored")
        # D5 and D6 rows are EXISTENCE facts about the class, not questions a chapter can serve
        # (Principal ruling 2026-08-15). A D5 row says the class does not carry the slot at all; a
        # D6 row is a school's-own question the বৃত্তি structure has no slot for. Neither is
        # admissible-or-excluded, because ADMISSIBILITY IS A CHAPTER-LEVEL FACT AND EXISTENCE IS A
        # CLASS-LEVEL ONE — collapsing them into one field is what forced the question. Left in,
        # they would make every C1 chapter write a content reason for a question its paper does
        # not contain, and would key an L-id no bank has ever declared.
        if r.get("d_code") in ("D5", "D6"):
            continue
        out[(r["subject"], r["class"], r["slot"].split("-")[-1])] = r
    return out, errs


def _declared_tasks(row):
    """The slot's declared task vocabulary — the ONLY strings an item may claim at this slot."""
    if row["task_mode"] == "alternative":
        return list(row.get("admitted_set") or [])
    if row["task_mode"] == "composite":
        return [p["part"] for p in row.get("parts") or []]
    return [row.get("admitted_task")]


def g_coverage(bank, ctx):
    """§6 row 10 — Coverage: the pool supplies every topic, and every item DOES THE TASK ITS CLASS
    ADMITS at the slot it sits in.

    CONVERTED AT CD-138. The gate no longer reads the bank's own header-stated slot list. CD-122(b)
    ruled that fallback *because* the per-chapter slot-mapping did not exist as data, and recorded
    the absence so its arrival would be a known trigger — "the day a slot-mapping is committed as
    data, this gate changes; the gate's docstring is the notice." This is that notice.

    WHAT CHANGED, AND WHY IT IS NOT A TIGHTENING FOR ITS OWN SAKE. The old gate read SLOT-ID
    PRESENCE: it asked whether some item carried the slot id the header named. A bank could hold
    ten items in `S10` doing ভাব নির্ণয় — a task admitted at NO class in the whole spine — and pass,
    because the id was present. The spine's কারণ column, where the task lives, was read by nothing.
    That is exactly what happened, and it is the defect the register exists to catch.

    THE THREE CHECKS, each naming its ruling:
      · ADMISSIBILITY (CD-138(e)) — the chapter declares its admissible slots in its own header,
        with a one-line CONTENT reason per excluded slot. The gate NEVER infers admissibility from
        content; it checks the declaration is complete and FAILs on any item sitting in a slot the
        chapter declared inadmissible.
      · ADMITTED TASK (CD-138(b)) — every item declares the task it does, in the register's own
        vocabulary. An `alternative` slot admits ONLY the task its class SELECTED; another member
        of the admitted set is a real failure and is reported as a different thing from a task
        admitted nowhere. A `composite` slot requires EVERY part — an item doing half the task
        (breaking the যুক্তবর্ণ without forming the শব্দ) fails here and passed before.
      · FLOOR (CD-138(g)) — an admissible slot owes the paper's full `items_per_paper`. Demand is
        paper-level and there is no divisor (CD-138(d)).
    """
    errs, rep = [], []
    header = bank.get("header") or {}
    subject, cls = bank.get("subject"), bank.get("class")
    # The register arrives through ctx so the SELFTEST can supply a synthetic one: QB-D-012 /
    # CD-121(e) — seeds are synthetic and no canon/marklogic file is read as fixture data. A live
    # run has it loaded from disk by `qp_ctx_for`.
    if ctx and "slot_register" in ctx:
        register, reg_errs = ctx["slot_register"], ctx.get("slot_register_error") or []
    else:
        register, reg_errs = load_slot_register(ROOT)
    errs += reg_errs
    if not register:
        return errs, rep
    slots_for_class = {s: r for (sub, c, s), r in register.items()
                       if sub == subject and c == cls and r.get("d_code") not in ("D5", "D6")}
    # CD-138(f) is checked HERE, on the register actually in hand, not only in the disk loader —
    # a check that lives only in the loader is invisible to any caller that supplies the register
    # another way, which is precisely how the selftest supplies it. The seed proved that.
    for s, r in sorted(slots_for_class.items()):
        if "chapter_authorable" in r:
            errs.append(f"register row {r.get('slot', s)} carries an AUTHORED "
                        f"`chapter_authorable` — CD-138(f) makes it DERIVED from this bank's own "
                        f"admissibility declaration, never authored upstream")
    if not slots_for_class:
        errs.append(f"the register carries no rows for {subject} C{cls} — coverage cannot be read "
                    f"against a register that does not cover this bank's class (CD-138)")
        return errs, rep

    if not header.get("reason"):
        errs.append("bank header states no one-line reason for its target — §4 requires one")

    # --- topics are unchanged: the register governs SLOTS, not topic coverage -------------
    topics = header.get("topics")
    if topics is None:
        errs.append("bank header does not declare `topics` — the register governs slots, not "
                    "topics, and the header remains the topic authority (§4)")
    else:
        have_topics = {q.get("topic_tag") for q in bank["questions"]}
        for t in topics:
            if t not in have_topics:
                errs.append(f"header declares topic {t}; no item in the pool supplies it")

    # --- ADMISSIBILITY, declared per chapter (CD-138(e)) ----------------------------------
    admissible = header.get("admissible_slots")
    exclusions = header.get("slot_exclusions") or {}
    if admissible is None:
        errs.append("bank header declares no `admissible_slots` — CD-138(e) requires the chapter "
                    "to declare which slots its content can support, with a one-line content "
                    "reason per excluded slot. The gate never infers this from content")
        return errs, rep
    admissible = set(admissible)
    # CD-147: S14/S15 are paper-level for every chapter. They are exempt from the completeness
    # test — a chapter that says nothing about them is CORRECT, not incomplete — and barred from
    # the admissible set outright.
    barred = paper_level_slots(subject, cls)
    admitted_paper_level = sorted(admissible & barred)
    if admitted_paper_level:
        errs.append(f"bank header ADMITS paper-level slot(s) " + ", ".join(admitted_paper_level)
                    + f" — paper-level for {subject} C{cls} (CD-147 for BAN S14/S15; CD-150 for "
                      f"ENG S05 at C3–C5 and S13/S14 at C4–C5), categorically. No chapter admits "
                      f"them on any content, and this is not a CD-138(e) declaration the chapter "
                      f"is entitled to make")
    stale_reasons = sorted(set(exclusions) & barred)
    if stale_reasons:
        rep.append("exclusion reason(s) carried for " + ", ".join(stale_reasons)
                   + " — no longer owed under CD-147 (the bar is categorical, not a per-chapter "
                     "content declaration). Accepted, not failed: a bank that still records one is "
                     "correct history, and the ledger is where it is simplified")
    undeclared = [s for s in sorted(slots_for_class)
                  if s not in admissible and s not in exclusions
                  and s not in barred]
    if undeclared:
        errs.append("the admissibility declaration is INCOMPLETE — neither admitted nor excluded "
                    "with a reason: " + ", ".join(undeclared)
                    + " (CD-138(e): every register slot for this class is one or the other)")
    for s, why in exclusions.items():
        if not str(why).strip():
            errs.append(f"slot {s} is excluded with an empty reason — CD-134(c) requires the "
                        f"recorded reason to be that the CONTENT does not support it")
        if s in admissible:
            errs.append(f"slot {s} is declared BOTH admissible and excluded")
    unknown = sorted((admissible | set(exclusions)) - set(slots_for_class))
    if unknown:
        errs.append("declared slot(s) not in the register for this class: " + ", ".join(unknown))

    # --- ADMITTED TASK, per item (CD-138(b)) ----------------------------------------------
    slot_index = bank.get("slot_index") or {}
    task_index = bank.get("task_index") or {}
    supply = {}
    for q in bank["questions"]:
        qid = q.get("qid")
        slot = slot_index.get(qid)
        if slot is None:
            errs.append(f"{qid}: no slot_index entry — coverage cannot read its slot")
            continue
        supply[slot] = supply.get(slot, 0) + 1
        if is_paper_level(subject, cls, slot):
            errs.append(f"{qid}: sits in slot {slot}, which is PAPER-LEVEL for {subject} C{cls} at "
                        f"EVERY chapter (CD-147 · CD-150) — it is authored in the paper/exam "
                        f"pipeline and never in a chapter bank. This is categorical and does not "
                        f"depend on what this chapter's content anchors")
            continue
        if slot not in admissible:
            errs.append(f"{qid}: sits in slot {slot}, which this chapter declared INADMISSIBLE"
                        + (f" — {exclusions[slot]}" if slot in exclusions else "")
                        + " (CD-138(e))")
            continue
        row = slots_for_class.get(slot)
        if row is None:
            errs.append(f"{qid}: slot {slot} is in no register row for {subject} C{cls}")
            continue
        claimed = task_index.get(qid)
        if claimed is None:
            errs.append(f"{qid}: declares no task — CD-138(b) makes the task a DECLARED field, "
                        f"and slot {slot} is `{row['task_mode']}`, so slot id alone says nothing "
                        f"about what this item does")
            continue
        claimed_list = claimed if isinstance(claimed, list) else [claimed]
        declared = _declared_tasks(row)
        mode = row["task_mode"]
        if mode == "composite":
            missing = [p for p in declared if p not in claimed_list]
            extra = [c for c in claimed_list if c not in declared]
            if missing:
                errs.append(f"{qid}: slot {slot} is COMPOSITE and its item must do every part; "
                            f"missing {', '.join(missing)} — half the task (CD-138(b))")
            if extra:
                errs.append(f"{qid}: slot {slot} declares parts {declared}; this item also claims "
                            f"{extra}, which is not a declared part")
        else:
            for c in claimed_list:
                if c == row.get("selected") or (mode == "simple" and c == row.get("admitted_task")):
                    continue
                # UNSELECTED (Principal ruling 2026-08-16) — when the register declares
                # `selected: null`, NO form was narrowed to, so EVERY member of `admitted_set` is
                # admitted and none of them is off-choice. Without this branch a correct register
                # would redden conformant items: the row would say "either form" and the gate
                # would fail both, because `c == row["selected"]` can never hold against null.
                if mode == "alternative" and row.get("selected") is None and c in declared:
                    continue
                if mode == "alternative" and c in declared:
                    errs.append(f"{qid}: does `{c}` at slot {slot}. That task IS admitted at this "
                                f"slot, but C{cls} SELECTED `{row['selected']}` — an off-choice "
                                f"item, not a wrong slot (CD-138(b))")
                else:
                    errs.append(f"{qid}: does `{c}` at slot {slot}, which admits "
                                f"{declared} at C{cls}. Admitted nowhere in this slot's set")

    # --- TAUGHT SET, per item (CD-165 · CD-166 · CD-169's residual · CD-172's exclusion) ---
    cd172_hit = set()
    for s_short, row in sorted(slots_for_class.items()):
        in_slot = [q for q in bank["questions"] if slot_index.get(q.get("qid")) == s_short]
        declared_set = row.get("taught_set")
        required = (subject, cls, s_short) in TAUGHT_SET_REQUIRED
        if declared_set is None:
            if required and in_slot:
                errs.append(f"slot {s_short} carries {len(in_slot)} item(s) and its register row for "
                            f"{subject} C{cls} declares NO `taught_set` — absence reads as NOT "
                            f"DECLARED, never as permissive (CD-165). The marks a class is taught are "
                            f"the Principal's to declare; until the row carries them nothing here can "
                            f"be checked and nothing passes")
            continue
        admitted = set(declared_set)
        for q in in_slot:
            off_set, clean_at = marks_required_by(q, admitted)
            if clean_at not in (None, 0):
                rep.append(f"{q.get('qid')}: accepted[0] uses a mark outside C{cls}'s taught set while "
                           f"accepted[{clean_at}] stays inside it — the item PASSES, because a full-mark "
                           f"route exists, and is REPORTED because the first-listed variant is the one a "
                           f"marker reads first")
            off = sorted(off_set)
            if off and q.get("qid") in CD172_TAUGHT_SET_EXCLUDED:
                # CD-172 — NAMED, JUSTIFIED, ID-KEYED. The defect is REPORTED in full, with the
                # same text it would have failed with, so nothing is hidden by being excluded.
                cd172_hit.add(q.get("qid"))
                rep.append(f"CD-172 NAMED EXCLUSION · {q.get('qid')}: requires "
                           + " · ".join(off) + f" at slot {s_short}; C{cls}'s taught set is "
                           + " · ".join(declared_set) + ". THE DEFECT IS REAL AND IS NOT "
                           "RETRACTED (CD-169(b)) — it is EXCLUDED from CD-153's repo-wide-green "
                           "push condition because CD-169 rules the item RETAINED and CD-170 bars "
                           "in-repo fixing of this bank. Disposition is the Hub's under "
                           "CD-142(a). This id only; the check is unchanged everywhere else")
                continue
            if off:
                errs.append(f"{q.get('qid')}: requires " + " · ".join(off)
                            + f" at slot {s_short}; C{cls}'s taught set is " + " · ".join(declared_set)
                            + " (CD-165, amended by CD-166). A mark outside the taught set tests "
                              "something the class was never taught, however sound the item is "
                              "otherwise")

    # CD-172's roster, printed EVERY run on every bank that carries a TAUGHT_SET_REQUIRED slot —
    # never only when it bites. An exclusion that prints only on the run it is used is invisible on
    # the run it stops being needed, which is exactly the run somebody must act on.
    if any((subject, cls, s) in TAUGHT_SET_REQUIRED for s in slots_for_class):
        in_bank = {q.get("qid") for q in bank["questions"]} & CD172_TAUGHT_SET_EXCLUDED
        if in_bank:
            unexercised = sorted(in_bank - cd172_hit)
            rep.append("CD-172 ROSTER · excluded id(s) present in this bank: "
                       + " · ".join(sorted(in_bank))
                       + f"  |  EXERCISED this run: {' · '.join(sorted(cd172_hit)) or 'none'}")
            if unexercised:
                rep.append("CD-172 UNEXERCISED — " + " · ".join(unexercised)
                           + ": listed as excluded and NOT failing the taught-set check. **THIS IS "
                             "THE DISCHARGE SIGNAL (CD-172).** Either the Hub has disposed of the "
                             "item, or the taught set moved under a later row, or the list has "
                             "drifted from the class it describes (CD-160). Whichever it is, the "
                             "exclusion is no longer earning its place and REMOVING IT IS OWED — "
                             "the row cites this condition as its own expiry")

    # --- NO FLOOR. CD-171(a) retires both counts this block used to enforce. ---------------
    # (i) CD-138(g)'s per-slot demand is retired AT POOL LEVEL ONLY: `items_per_paper` is what a
    #     PAPER owes, and no single chapter owes a paper's worth of any slot. The rest of
    #     CD-138(g) is intact — demand is still undivided and there is still no divisor.
    # (ii) REF-09 §4.3's 20-item pool minimum is retired as a bank gate. REF-09 §4.3 and
    #     REF-08 §4.1 are NOT edited and are not wrong: §4.1's 20 sizes a HOMEWORK draw across a
    #     year so routine rotation and top-ups do not run it dry. The READING as a conformance
    #     count is what left, not the number.
    # Both are REPORTED below so the numbers stay visible and their absence is legible as a
    # ruling rather than as an oversight.
    short = [f"{s} {supply.get(s, 0)}/{slots_for_class[s]['items_per_paper']}"
             for s in sorted(admissible) if s in slots_for_class
             and supply.get(s, 0) < slots_for_class[s]["items_per_paper"]]
    rep.append(f"pool holds {len(bank['questions'])} item(s) — NO MINIMUM AND NO CEILING "
               f"(CD-171(a)). The bound is the chapter's content under §4's near-duplicate ban")
    if short:
        rep.append("slot(s) supplying under the PAPER's per-slot demand — PRINTED, NOT FAILED "
                   "(CD-171(a)(iv)): the demand is the paper's and the paper composes across "
                   "chapters. " + " · ".join(short))

    # CD-147 — the two counts are reported SEPARATELY because they are different kinds of thing:
    # a content exclusion is the chapter's own declaration and revisable on evidence; a paper-level
    # slot is neither. Summing them would print a number that reads as "declarations made" and
    # over-counts by however many paper-level rows the class carries.
    n_content_excl = len(set(exclusions) - barred)
    n_paper_level = len(set(slots_for_class) & barred)
    rep.append(f"coverage read against THE REGISTER (CD-138 — this replaces the header-stated "
               f"target, §4's own successor clause): {len(slots_for_class)} slot(s) for {subject} "
               f"C{cls}, {len(admissible)} declared admissible, {n_content_excl} excluded with a "
               f"content reason (CD-138(e)), {n_paper_level} paper-level and outside the "
               f"declaration entirely (CD-147)")
    rep.append("per-slot demand is PAPER-LEVEL and undivided (CD-138(d)) and is asked of the "
               "PAPER, never of a chapter (CD-171(a)(iv)). `PENDING-P-036` is CLOSED-MOOT with "
               "CD-171: there is no pool floor left for its `min()` to take a minimum of")
    return errs, rep


def bank_content_digest(items):
    """sha256 over a list of item dicts, sorted by qid. The signature row and this gate use the
    SAME function, so "what the Principal signed" and "what the Hub receives" are comparable
    quantities rather than two descriptions that happen to sound alike."""
    return hashlib.sha256(json.dumps(sorted(items, key=lambda q: q.get("qid") or ""),
                                     ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def envelope_prefix(qids):
    """The `QP-{SUBJ}-C{n}-U{u}-` prefix every qid in one bank shares.

    THIS EXISTS BECAUSE `single/` IS SHARED BY EVERY BANK. The first run of this gate globbed the
    whole directory and reported পাঠ ২১'s 57 envelopes as orphans of পাঠ ১৩ — a gate that fires on
    a correct export is worse than no gate, because the author learns to scroll past it.
    `build_question_envelopes.py` refuses a bank whose items disagree on (subject, class, unit), so
    one bank has exactly one prefix and it is read off the bank rather than assumed from a filename.
    """
    pres = {q.rsplit("-Q", 1)[0] for q in qids if q and "-Q" in q}
    return pres.pop() + "-Q" if len(pres) == 1 else None


def load_envelope_index(bank_path, qids):
    """→ ({qid: payload}, {qid: payload}, note) — the split `single/` set and the array set.

    Both are read because they are two artifacts that can drift from the bank AND from each other.
    `split_envelopes.py` writes `single/` from the array, so they agree at build time and diverge
    the moment either is regenerated alone.
    """
    if bank_path is None:
        return None, None, "no bank path in context — the export directory cannot be located"
    prefix = envelope_prefix(qids)
    if prefix is None:
        return None, None, None, ("this bank's qids do not share one QP-SUBJ-Cn-Uu prefix — the export "
                            "cannot be scoped, and a mixed bank is refused upstream anyway")
    envdir = Path(bank_path).parent / "envelopes"
    array = envdir / (Path(bank_path).stem + ".envelopes.json")
    single = envdir / "single"
    if not array.exists() and not single.exists():
        return None, None, None, (f"no export exists at {envdir.as_posix()} — this bank has never been "
                            f"fanned out. That is not drift and is not judged; §11's flow has "
                            f"simply not been run. Reported, not passed")
    arr = {}
    if array.exists():
        try:
            for e in json.loads(array.read_text(encoding="utf-8")):
                arr[(e.get("payload") or {}).get("qid")] = e.get("payload")
        except Exception as e:  # noqa: BLE001 — the reason must reach the report
            return None, None, None, f"{array.as_posix()} is unreadable: {e}"
    # contract v1.1 (CD-143): the batch wrapper is a THIRD export artifact and drifts like the
    # other two. It is read here rather than in a separate gate because "the export matches the
    # bank" is one question, and splitting it across two gates is how two answers appear.
    batch_path = envdir / (Path(bank_path).stem + ".batch.json")
    batch = None
    if batch_path.exists():
        try:
            batch = json.loads(batch_path.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            return None, None, f"{batch_path.as_posix()} is unreadable: {e}"
    sing = {}
    if single.exists():
        for f in sorted(single.glob(prefix + "*.json")):
            try:
                e = json.loads(f.read_text(encoding="utf-8"))
            except Exception:  # noqa: BLE001
                continue
            qid = (e.get("payload") or {}).get("qid")
            if qid:
                sing[qid] = e.get("payload")
    return sing, arr, batch, None


def g_envelope_sync(bank, ctx):
    """EXPORT STALENESS FAILS LOUDLY — the gate the wave-2 incident bought.

    THE DEFECT THIS EXISTS FOR, stated as it happened rather than in the abstract.
    `banks/envelopes/` sat at **36 envelopes — Q01–Q36, the wave-1/2 surface — while the bank went
    to 88 at wave 3 and 110 at wave 4.** Wave 3 did not regenerate them either, so the drift ran
    two waves. Nothing caught it, and nothing could have: every gate in this suite reads the BANK,
    and §11's flow imports the ENVELOPES. **The export path read a file the gate never opened.**

    What that would have shipped: a 36-item bank still carrying the ten `S10 ভাব নির্ণয়` items —
    a task admitted at NO class in the whole spine — into the Hub as `draft`, past COVERAGE, which
    was built for exactly that defect and had already caught it in the bank. **A gate that catches
    a defect in the artifact but not in the artifact's export has caught nothing.**

    AND THE SECOND HALF, which is why an id check is not enough on its own. `build_question_
    envelopes.py` and `split_envelopes.py` only WRITE. An item that leaves the bank leaves its
    envelope behind, in a directory nobody prunes — seven such orphans were found at the
    regeneration, including five of those ten `S10` items. **A stale ADDITION is loud; a stale
    SURVIVAL is silent**, and the silent one is the one that reaches the Hub.

    THREE CHECKS:
      · SET — the envelope qids and the bank qids must be the same set. Missing → the export is
        behind. Orphan → the export carries a retired item.
      · CONTENT — each envelope's `payload` must equal its bank item. An id set can match while
        every payload is a wave old, which is precisely what a re-tag or a rewrite produces.
      · ARRAY vs SINGLE — the two export artifacts must agree with each other, not only with the
        bank. They are written by different scripts and can be regenerated separately.

    NO EXPORT AT ALL IS REPORTED, NOT FAILED. A bank that has never been fanned out is not stale;
    §11's flow has simply not been run yet. Failing there would make the gate fire on every
    in-progress bank and teach the author to ignore it (SOURCE_POLICY §7.17: report or refuse,
    never omit — and never cry wolf).
    """
    errs, rep = [], []
    items = {q.get("qid"): q for q in bank.get("questions", [])}
    if "envelope_index" in ctx:
        idx = ctx["envelope_index"]
        sing, arr, batch, note = idx if len(idx) == 4 else (idx[0], idx[1], None, idx[2])
    else:
        sing, arr, batch, note = load_envelope_index(ctx.get("bank_path"), set(items))
    if note:
        return [], [note]

    for label, got in (("single/", sing), ("array", arr)):
        if not got:
            continue
        missing = sorted(set(items) - set(got))
        orphan = sorted(set(got) - set(items))
        if missing:
            errs.append(f"{label}: {len(missing)} bank item(s) have no envelope — the export is "
                        f"BEHIND the bank: {', '.join(missing[:8])}"
                        + (f" … +{len(missing)-8} more" if len(missing) > 8 else ""))
        if orphan:
            errs.append(f"{label}: {len(orphan)} envelope(s) have no bank item — the export "
                        f"carries RETIRED content: {', '.join(orphan[:8])}"
                        + (f" … +{len(orphan)-8} more" if len(orphan) > 8 else ""))
        drift = [q for q in sorted(set(items) & set(got))
                 if bank_content_digest([items[q]]) != bank_content_digest([got[q]])]
        if drift:
            errs.append(f"{label}: {len(drift)} envelope payload(s) differ from the bank item of "
                        f"the same id — the ids match and the CONTENT does not, which is what a "
                        f"re-tag or a rewrite produces: {', '.join(drift[:8])}"
                        + (f" … +{len(drift)-8} more" if len(drift) > 8 else ""))
    if sing and arr and set(sing) != set(arr):
        errs.append(f"the array and single/ disagree with EACH OTHER — array {len(arr)}, "
                    f"single/ {len(sing)}. They are written by different scripts and one was "
                    f"regenerated without the other")
    # --- the v1.1 batch wrapper (CD-143) ------------------------------------------------
    if batch is None:
        rep.append("no `.batch.json` beside this export — contract v1.1's wrapper has not been "
                   "built for this bank. REPORTED, not failed: an unrun step is not drift "
                   "(SOURCE_POLICY §7.17)")
    else:
        b = batch.get("batch") or {}
        bitems = batch.get("items")
        if not isinstance(bitems, list):
            errs.append("batch: `items` is absent or not an array — the wrapper carries no payload "
                        "and the Hub rejects it whole (contract v1.1)")
            bitems = []
        bq = [(e.get("payload") or {}).get("qid") for e in bitems if isinstance(e, dict)]
        missing = sorted(set(items) - set(bq))
        orphan = sorted(set(bq) - set(items))
        if missing:
            errs.append(f"batch: {len(missing)} bank item(s) absent from the wrapper — the batch "
                        f"is BEHIND the bank: {', '.join(missing[:8])}"
                        + (f" … +{len(missing)-8} more" if len(missing) > 8 else ""))
        if orphan:
            errs.append(f"batch: {len(orphan)} wrapper item(s) have no bank item — RETIRED content "
                        f"in the export: {', '.join(orphan[:8])}"
                        + (f" … +{len(orphan)-8} more" if len(orphan) > 8 else ""))
        declared = b.get("item_count")
        if declared != len(bitems):
            errs.append(f"batch: `item_count` {declared} != items length {len(bitems)} — the Hub "
                        f"rejects this WHOLE and imports nothing (harness L1b). A wrapper that "
                        f"misdescribes itself is worse than a missing one: it looks importable")
        want = bank_content_digest(list(items.values()))
        got = b.get("digest")
        if got is not None and got != want:
            errs.append(f"batch: `digest` {str(got)[:12]} != the bank's {want[:12]} — the wrapper "
                        f"describes a DIFFERENT bank than the one on disk. The contract does not "
                        f"recompute this at import (it is an audit field), so NOTHING DOWNSTREAM "
                        f"CATCHES IT — which is exactly why it is checked here")
        if batch.get("doc_type") != "question_batch":
            errs.append(f"batch: doc_type is {batch.get('doc_type')!r}, not `question_batch`")
        if batch.get("envelope_version") != "1.0":
            errs.append(f"batch: envelope_version is {batch.get('envelope_version')!r}; the "
                        f"contract's const is \"1.0\" — the DOCUMENT is v1.1, the WIRE VALUE is not")

    if not errs:
        rep.append(f"export in sync: {len(sing or arr)} envelope(s) == {len(items)} bank item(s), "
                   f"ids and payloads, array and single/"
                   + (f", and the v1.1 batch wrapper at item_count "
                      f"{(batch.get('batch') or {}).get('item_count')}" if batch else "")
                   + f" (digest {bank_content_digest(list(items.values()))[:12]})")
    return errs, rep



# NEAR-DUPLICATE THRESHOLDS — MEASURED, NOT GUESSED, and UNTOUCHED by CD-171. Jaccard over
# normalised stem tokens, within a slot. On the live 110-item পাঠ ১৩: zero exact duplicates and a
# maximum of 0.905, from S12's যুক্তবর্ণ frame where only the word changes and that IS the task. So
# FAIL sits at 0.95 with real headroom above the legitimate maximum, and 0.85–0.95 REPORTS for the
# Hub's expert eyes. These are the LAST numbers PLAN reads, and they are not counts of a pool —
# they are a similarity between two stems, which is a fact about two items and not about a size.
PLAN_DUP_FAIL = 0.95
PLAN_DUP_REPORT = 0.85


# ── THE MARGIN APPARATUS IS GONE (CD-171(d)) ──────────────────────────────────────────────
#
# DELETED IN THIS COMMIT: `PLAN_MARGIN = 2` · `PLAN_MARGIN_EXCEPTIONS` · `plan_margin_for()` ·
# `_chapter_number()` · `BLOOM_FLOORS`. Every one of them existed to serve a count against a POOL,
# and CD-171 moves counts to the paper. **PLAN computes no counts**, so there is no margin to
# require, no exception to grant and no floor table to read.
#
# WHAT GOES INERT WITH THEM, named so a later reader is not left hunting: **CD-158**'s পাঠ ১৩
# `Understand` exception and **CD-162**'s ruling to KEEP that key inert. CD-162(d) kept the key
# deliberately, as the only live data proving an honoured-but-unexercised exception is REPORTED
# rather than silent. **That property has no subject once the rule it modified is retired** — an
# exception to a rule that does not exist is not inert, it is unreadable. Neither row's text is
# edited and neither is called wrong; both are superseded by CD-171(d) at the mechanism they share.
# `cd158_selftest` is deleted with them: a seed whose target is gone is TOOLS-CR-007's vacuous
# shape, and keeping it would prove nothing while looking like proof.
#
# ⚠ RE-MINTING ANY OF THESE TAKES A CD ROW. A later session that notices a thin pool and reaches
# for a floor is reaching for the thing CD-171 removed on measured evidence (PENDING-P-036's two
# findings: an Analyze floor forbade 28 of 32 chapter-sourced items, and margin cost about two
# items of authoring per item of margin because the floor rises with the total).


def _stem_sim(a, b):
    ta, tb = set(a.split()), set(b.split())
    return len(ta & tb) / len(ta | tb) if (ta | tb) else 0.0


def g_plan(bank, ctx):
    """PLAN — the machine replacement for the plan-table human countersign (Principal 2026-08-15).

    WHAT IT REPLACES, and why a gate can replace it at all. Through wave 4 a chapter bank was
    planned in a table the Principal countersigned before authoring began: per-slot content maxima,
    intended Bloom tags, resulting margins. **Every quantity in that table is derivable from the
    register and the finished bank**, which is exactly why the countersign could be mechanised —
    and why the ONE thing it never checked, whether the content is any good, stays with a human
    (CD-136(g), and §6's relocation to Hub subject experts).

    PLAN COMPUTES NO COUNTS (CD-171(d)). What it checks is conformance and nothing arithmetical:
    the chapter has DECLARED its admissible slots at all (CD-138(e)); no paper-level slot is
    admitted, refused in PLAN's own voice rather than by leaning on COVERAGE (CD-147, CD-150);
    every item's `task_index` is complete, admitted, `selected`-honouring and composite-complete
    (CD-138(b)); P-037's type rule, which is about a TYPE and not a count; and the within-slot
    near-duplicate stem scan.

    WHAT LEFT, named because a reader who knows this gate will look for it. The Bloom margin rule
    (*every positive REF-06 §3.6 floor clears by >= 2; landing exactly on a floor is a DEFECT*)
    and CD-138(g)'s full per-slot demand check are RETIRED. Both counted a POOL. CD-171 moves
    counts to the PAPER, which is the artifact a distribution was ever about — a paper composes
    across chapters and no single chapter owes a paper's worth of anything.

    THE STATED CONSEQUENCE GOES WITH THE PREMISE, and this is the half most likely to be
    half-remembered: the `0.80n + 8 <= n` derivation and its `n >= 40` minimum were CD-141(g)'s
    STATED CONSEQUENCE of the margin rule, not an independent policy. **A consequence outlives
    its premise only if somebody re-rules it, and nobody has.** There is no minimum pool size.

    PLAN AND BLOOM-BAND NO LONGER DISAGREE, because neither counts. The old comment here recorded
    their deliberate disagreement (pool-legal versus plan-signable) and it is gone with the
    numbers it was about.

    ⚠ A BANK CANNOT STOP AT PLAN ON COUNT GROUNDS. That is the ruling, not a side effect of it.

    NEAR-DUPLICATE THRESHOLDS ARE MEASURED, NOT GUESSED. Jaccard over normalised stem tokens,
    within a slot. On the live 110-item পাঠ ১৩: zero exact duplicates and a maximum of **0.905**,
    from S12's যুক্তবর্ণ frame where only the word changes and that is the task. So FAIL sits at
    0.95 with real headroom above the legitimate maximum, and 0.85–0.95 REPORTS for the Hub's
    expert eyes. **The per-word drill slots are the reason this is not stricter**: S03's *"'X'
    শব্দটি দিয়ে একটি অর্থপূর্ণ বাক্য লেখো"* is five near-identical stems BY DESIGN, and a gate
    that fired there would be teaching authors to scroll past it.

    This overlaps COVERAGE on demand and on task declaration, and the overlap is intended: COVERAGE
    asks whether the bank is conformant, PLAN asks whether it is signable. A gate that replaces a
    signature must check everything the signature covered, including what another gate also checks.
    """
    errs, rep = [], []
    items = bank.get("questions") or []
    n = len(items)
    if not n:
        return ["the bank holds no items — nothing to plan"], []
    subject, cls = bank.get("subject"), bank.get("class")
    header = bank.get("header") or {}
    slot_index = bank.get("slot_index") or {}
    task_index = bank.get("task_index") or {}

    if ctx and "slot_register" in ctx:
        register = ctx["slot_register"]
    else:
        register, _ = load_slot_register(ROOT)
    rows = {s: r for (sub, c, s), r in (register or {}).items()
            if sub == subject and c == cls and r.get("d_code") not in ("D5", "D6")}

    # --- 1. Bloom: NOTHING. (CD-171(d)) ----------------------------------------------------
    # This block computed per-level counts, a required-items sum, a POOL-TOO-SMALL verdict and a
    # per-level margin test against PLAN_MARGIN. All of it counted a pool. BLOOM-BAND still PRINTS
    # the per-level counts every run; PLAN does not read them and does not duplicate the report.

    # --- 2. the declaration itself, and the paper-level bar (no counts) --------------------
    admissible = set(header.get("admissible_slots") or [])
    if not admissible:
        errs.append("no `admissible_slots` declared — a plan cannot be signed against a chapter "
                    "that has not said which slots its content supports (CD-138(e))")
    # CD-147 — a plan that admits a paper-level slot is not signable, and PLAN says so in its own
    # voice rather than leaning on COVERAGE. The two gates ask different questions (conformant vs
    # signable) and a bank is offered as FINISHED on PLAN's verdict.
    plan_paper_level = sorted(admissible & paper_level_slots(subject, cls))
    if plan_paper_level:
        errs.append("the plan admits paper-level slot(s) " + ", ".join(plan_paper_level)
                    + f" — paper-level for {subject} C{cls} (CD-147 · CD-150): they belong to the "
                      f"paper/exam pipeline for EVERY chapter and no chapter plan may claim them")
    # NO DEMAND TEST. CD-171(a)(iv) retires CD-138(g) at pool level: `items_per_paper` is what a
    # PAPER owes. A bank supplying one item at a slot the paper wants six of is CONFORMANT — the
    # paper draws the other five from the chapters that have them. COVERAGE prints the shortfall.

    # --- 3. task_index: complete, admitted, selected honoured, every composite part ---------
    for q in items:
        qid = q.get("qid")
        slot = slot_index.get(qid)
        if slot is None or slot not in rows:
            continue
        row = rows[slot]
        claimed = task_index.get(qid)
        if claimed is None:
            errs.append(f"{qid}: declares no task — CD-138(b) makes the task a DECLARED field")
            continue
        claimed_list = claimed if isinstance(claimed, list) else [claimed]
        declared = _declared_tasks(row)
        mode = row["task_mode"]
        if mode == "composite":
            missing = [p for p in declared if p not in claimed_list]
            if missing:
                errs.append(f"{qid}: slot {slot} is COMPOSITE and this item omits "
                            f"{', '.join(missing)} — half the task")
        elif mode == "alternative":
            # UNSELECTED — same rule as COVERAGE's, and PLAN needs its own copy for the same
            # reason it has its own off-choice check: it asks whether a bank is SIGNABLE and is
            # not entitled to lean on another gate's verdict.
            unselected = row.get("selected") is None
            for c in claimed_list:
                if unselected and c in declared:
                    continue
                if c != row.get("selected"):
                    errs.append(f"{qid}: does `{c}` at {slot}; C{cls} SELECTED "
                                f"`{row.get('selected')}`"
                                + (" — off-choice, admitted at the slot but not at this class"
                                   if c in declared else " — admitted nowhere in this slot's set"))
        else:
            for c in claimed_list:
                if c != row.get("admitted_task"):
                    errs.append(f"{qid}: does `{c}` at simple slot {slot}, which admits "
                                f"`{row.get('admitted_task')}`")

    # --- 4. P-037: a teacher-supplied key rides only short_answer / descriptive -------------
    # The key is TEACHER-SUPPLIED when the item SAYS SO in its own model_note (CD-136(b)) — a
    # declared field, never inferred from the slot. Inferring it would be QB-CR-011's shape.
    def _note(q):
        # `answer_key` is a dict in the §4 shape and a bare string in older fixtures. Reading it
        # as a dict unconditionally raised AttributeError on the first run — caught by the
        # selftest, which is the argument for running a new gate against every fixture in the file
        # rather than only against the one it was written for.
        k = q.get("answer_key")
        return (k.get("model_note") or "") if isinstance(k, dict) else ""

    tk = [q for q in items if "CD-136" in _note(q)]
    bad_type = [f"{q.get('qid')} ({q.get('question_type')})" for q in tk
                if q.get("question_type") not in ("short_answer", "descriptive")]
    if bad_type:
        errs.append("P-037: teacher-supplied keys are admitted on `short_answer` and `descriptive` "
                    "only — " + " · ".join(bad_type))
    rep.append(f"P-037: {len(tk)} item(s) declare a teacher-supplied key in their own model_note, "
               f"all on admitted types")

    # --- 5. near-duplicate stems, within a slot --------------------------------------------
    by_slot = {}
    for q in items:
        by_slot.setdefault(slot_index.get(q.get("qid")), []).append(
            (q.get("qid"), qp_norm(q.get("question_text"))))
    borderline = {}
    for slot, group in sorted(by_slot.items(), key=lambda kv: str(kv[0])):
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                (qa, sa), (qb, sb) = group[i], group[j]
                if sa == sb:
                    errs.append(f"{slot}: {qa} and {qb} carry the SAME stem verbatim — §4 forbids "
                                f"a near-duplicate, and identical is past near")
                    continue
                sim = _stem_sim(sa, sb)
                if sim >= PLAN_DUP_FAIL:
                    errs.append(f"{slot}: {qa} ~ {qb} stems are {sim:.0%} identical — near-exact, "
                                f"above the {PLAN_DUP_FAIL:.0%} bar")
                elif sim >= PLAN_DUP_REPORT:
                    borderline.setdefault(slot, []).append((sim, qa, qb))
    for slot, pairs in sorted(borderline.items(), key=lambda kv: str(kv[0])):
        pairs.sort(reverse=True)
        top = " · ".join(f"{a}~{b} {s:.0%}" for s, a, b in pairs[:3])
        rep.append(f"BORDERLINE STEMS at {slot}: {len(pairs)} pair(s) in "
                   f"{PLAN_DUP_REPORT:.0%}–{PLAN_DUP_FAIL:.0%} — {top}"
                   + (" …" if len(pairs) > 3 else "")
                   + ". NOT a failure: a per-word drill is near-identical by design. Raised for "
                     "the Hub's subject expert, never silently dropped")
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
    ("BLOOM-BAND",         {"qp6": g_bloom_band},             "§6.7 · CD-121 · CD-171 (report)"),
    ("DIFFICULTY",         {"qp6": g_difficulty},                        "§6.8 · CD-122"),
    ("REPETITION",         {"qp6": g_repetition},                        "§6.9"),
    ("COVERAGE",           {"qp6": g_coverage},                          "§6.10 · CD-138"),
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
    # The 23rd. Like SOURCE-EXCLUSION it carries no § row of its own — it executes a Principal
    # ruling (2026-08-15) taken on a defect nothing in this suite could see, because every other
    # gate reads the bank and §11 imports the envelopes.
    ("PLAN",               {"qp6": g_plan},   "AGENTS §6 · Principal 2026-08-15 · CD-171(d)"),
    ("ENVELOPE-SYNC",      {"qp6": g_envelope_sync},          "AGENTS §11 · Principal 2026-08-15"),
]
# CD-123's invariant is preserved by counting what CD-123 was counting — the gates that carry a
# QUESTION_POLICY §6 row — rather than the total, which CD-131 has now moved. Asserting on the
# total alone would have made the §6 count unverifiable the moment any gate was added from
# anywhere else, which is the shape CD-083 keeps naming: a check written in a coarser unit than
# the thing it is protecting.
QP6_POLICY_GATES = [n for n, i, a in GATES if "qp6" in i and a.startswith("§")]
assert len(QP6_POLICY_GATES) == 11, "CD-123: QUESTION_POLICY §6 has eleven rows"
assert len(GATES) == 24, ("CD-123's 21 + SOURCE-EXCLUSION + ENVELOPE-SYNC + PLAN. The §6 count "
                          "above is unmoved and that is the assertion doing the work: two gates "
                          "now sit outside QUESTION_POLICY §6, each executing a ruling rather "
                          "than a policy clause, and neither may quietly inflate the §6 total. "
                          "ENVELOPE-SYNC's authority string deliberately reads `AGENTS §11` and "
                          "not `§11` — a bare § prefix is how the §6 filter identifies its own, "
                          "and the first draft of this row tripped that assertion by wearing the "
                          "wrong prefix. The check caught it, which is what it is for.")


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


def run(bank, ctx=None, quiet=False, bank_path=None):
    """Runs all 22 (CD-123's 21 + CD-131's SOURCE-EXCLUSION). Returns (fails, report).

    Shape-absent gates print N/A and the reason — never PASS."""
    shape = bank_shape(bank)
    if ctx is None:
        ctx = qp_ctx_for(bank, bank_path) if shape == "qp6" else qb_build_ctx(bank)
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


def qp_ctx_for(bank, bank_path=None):
    slugs, slug_err = load_ref19_slugs(ROOT)
    tags, tag_err = load_topic_numbers(ROOT)
    reg, reg_err = load_slot_register(ROOT)
    ctx = {"ref19_slugs": slugs, "ref19_error": slug_err,
           "topic_numbers": tags, "topic_error": tag_err, "extraction": None,
           "slot_register": reg, "slot_register_error": reg_err}
    ex = bank.get("extraction_path")
    if ex and (ROOT / ex).exists():
        ctx["extraction"] = (ROOT / ex).read_text(encoding="utf-8", errors="replace")
    # ENVELOPE-SYNC needs to locate this bank's own export directory. The PATH is passed rather
    # than the envelopes, so a caller that has no path (the selftest) supplies `envelope_index`
    # instead and no real export file is ever read as fixture data.
    ctx["bank_path"] = bank_path
    return ctx


# Both families' selftests now drive the MERGED registry through these two shims, so what they
# prove is this suite — not the two lists it was built from. That is the point of merging: a
# selftest that still exercised the old GATES list would go on passing after the merge broke it.

def qb_run(bank, quiet=False):
    return run(bank, qb_build_ctx(bank), quiet=quiet)


def qp_run(bank, ctx, quiet=False, bank_path=None):
    return run(bank, ctx, quiet=quiet, bank_path=bank_path)


# =================================================================================
# CONTEXT — §5 family
# =================================================================================

def qb_build_ctx(bank, register=None):
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
    # The register arrives as an argument so the SELFTEST can supply a synthetic one: seeds are
    # synthetic and no canon/marklogic file is read as fixture data (QB-D-012, CD-121(e)). A live
    # run passes None and the loader reads the register from disk.
    ctx = {"by_qid": by_qid, "pool_of": pool_of, "subject": subject,
           "class_level": class_level, "unit": unit, "source_text": src_text,
           "watch": 0, "report": [],
           "slot_register": register if register is not None
                            else load_slot_register(ROOT)[0]}
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
        f, rep = qp_run(bank, ctx, bank_path=p)
        fails += [(str(p), e) for _, e in f]
        # CD-135(f): the per-level Bloom counts against floors are REPORTED on EVERY run, not
        # only when a floor is missed and not only on the single-bank path. A check written
        # asymmetrically invites a later symmetric "fix"; a report that always prints is what
        # makes the asymmetry visible rather than something a reader infers from the code.
        # CD-172: the named exclusion prints HERE, on the sweep, or it is a silent skip in the one
        # run that decides a push. Caught by asserting the printer rather than the appender —
        # the seeded test proved g_coverage BUILT the line, and the line still reached nobody.
        for gate, line in rep:
            if gate == "BLOOM-BAND" or line.startswith("CD-172"):
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
        c = qb_build_ctx(bank, _synth_register())
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
                              {**qb_build_ctx(_qb_good_bank(), _synth_register()), "exclusions": []},
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
    """A synthetic chapter bank that passes all eleven. 24 items.

    (The size was chosen when REF-09 §4.3's 20-item floor was a gate. CD-171(a)(iii) retires that
    floor and the fixture is UNCHANGED anyway — a fixture rebuilt to suit a ruling proves the
    ruling rather than the gate. The 12-item NEGATIVE below is what exercises the new verdict.)

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
    qs, pool, slot_idx, src_idx, task_idx = [], {"HW": [], "AS": [], "CT": []}, {}, {}, {}
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
        task_idx[qid] = SYNTH_REGISTER_TASK[slot]
        src_idx[qid] = anchors[i % len(anchors)]
        pool[["HW", "AS", "CT"][i % 3]].append(qid)
    return {
        "bank_id": "SYNTH-BAN-C5-U99", "subject": "BAN", "class": 5, "chapter": "U99",
        "header": {"target": 24,
                   "reason": "synthetic fixture sized to exercise all eleven gates",
                   "topics": SYNTH_TOPICS, "spine_slots": SYNTH_SLOTS,
                   # CD-138(e) — the chapter declares what its content can support, and gives a
                   # CONTENT reason for each slot it cannot. The gate never infers either.
                   "admissible_slots": ["S02", "S05", "S07", "S08"],
                   "slot_exclusions": {
                       "S10": "কল্পিত পাঠ ৯৯-এ পদ নির্ণয়ের উপাদান নেই",
                       "S12": "কল্পিত পাঠ ৯৯-এ যুক্তবর্ণের অনুশীলনী নেই"}},
        "pool_index": pool, "slot_index": slot_idx, "task_index": task_idx,
        "source_index": src_idx,
        "questions": qs,
    }

def _synth_register():
    """A SYNTHETIC slot register for the fictional পাঠ ৯৯ fixture (CD-138).

    `canon/marklogic/SLOT_REGISTER.json` is NOT read here. It is a canon/marklogic file, and the
    fixture rule is absolute: seeds are synthetic (QB-D-012, CD-121(e)). The live register is a
    CONTROL — it is exercised by `tools/audits/slot_register_check.py`, which proves it against the
    spine — and a control is not a fixture.

    It carries one row of each `task_mode` on purpose, because the three modes are what COVERAGE
    now discriminates: `simple` (task fixed), `alternative` (a set, of which the class SELECTS one),
    `composite` (every part, every item).
    """
    def row(slot, mode, items, mpi, task=None, admitted=None, selected=None, parts=None):
        r = {"subject": "BAN", "class": 5, "slot": f"BAN-{slot}", "task_mode": mode,
             "slot_task": f"কল্পিত কাজ {slot}",
             "nape_frame": f"কল্পিত মূল কাঠামো {slot} · {items}টি · {mpi}×{items}",
             "admitted_task": task, "items_per_paper": items, "marks": items * mpi,
             "marks_per_item": mpi, "d_code": "D0", "authority": "SYNTHETIC — not NAPE",
             "row_constraints": []}
        if mode == "alternative":
            r["admitted_set"], r["selected"] = admitted, selected
        if mode == "composite":
            r["parts"] = [{"part": p, "marks": None} for p in parts]
        return r

    rows = [
        row("S02", "simple", 5, 1, task="শব্দার্থ"),
        row("S05", "simple", 5, 1, task="বহুনির্বাচনি"),
        row("S07", "simple", 4, 2, task="সংক্ষিপ্ত উত্তর"),
        row("S08", "simple", 3, 5, task="বিস্তৃত উত্তর"),
        row("S10", "alternative", 5, 1, task="পদ নির্ণয়",
            admitted=["ভাষারীতি পরিবর্তন", "পদ নির্ণয়", "ক্রিয়ার কাল"], selected="পদ নির্ণয়"),
        row("S12", "composite", 5, 1, task="যুক্তবর্ণ ভেঙে শব্দ",
            parts=["যুক্তবর্ণ ভাঙা", "শব্দ গঠন"]),
        # CD-147 — a LIVE (D0) paper-level row, so the categorical bar is exercised on a slot the
        # register really carries rather than on one the D5 filter would have skipped anyway. The
        # base fixture declares nothing about it and must stay CLEAN: that is the rule, seeded.
        row("S14", "alternative", 1, 5, task="আবেদনপত্র",
            admitted=["আবেদনপত্র", "ফরম পূরণ"], selected="আবেদনপত্র"),
    ]
    # One D5 and one D6 row, so the skip is exercised on the IN-HAND path rather than only in the
    # disk loader. These are supplied UNFILTERED on purpose — they simulate a caller that did not
    # filter, which is the only way to prove g_coverage filters for itself.
    rows.append({"subject": "BAN", "class": 5, "slot": "BAN-S15", "d_code": "D5",
                 "slot_task": "কল্পিত অনুপস্থিত স্লট", "marks": 0, "items_per_paper": 0,
                 "marks_per_item": 0, "absent_reason": "কল্পিত — এই শ্রেণিতে নেই",
                 "row_constraints": []})
    rows.append({"subject": "BAN", "class": 5, "slot": "BAN-L01", "d_code": "D6",
                 "slot_task": "কল্পিত স্কুলের নিজস্ব প্রশ্ন", "marks": 5,
                 "items_per_paper": None, "marks_per_item": None, "row_constraints": []})
    return {(r["subject"], r["class"], r["slot"].split("-")[-1]): r for r in rows}


SYNTH_REGISTER_TASK = {"S02": "শব্দার্থ", "S05": "বহুনির্বাচনি",
                       "S07": "সংক্ষিপ্ত উত্তর", "S08": "বিস্তৃত উত্তর"}



def _plan_bank():
    """A SYNTHETIC 44-item bank that PLAN passes — the smallest shape that can.

    44 is not a round number, it is the arithmetic. Margin >= 2 on the four positive floors needs
    0.80n + 8 <= n, so n >= 40; at 44 every level sits at EXACTLY +2, which makes every seed below
    a one-item nudge. The fixture is synthetic (QB-D-012, CD-121(e)) and shares the synthetic
    register the rest of the qp6 selftest uses.
    """
    plan = [("S02", "Remember", 8), ("S12", "Remember", 3), ("S12", "Understand", 3),
            ("S05", "Understand", 8), ("S10", "Understand", 2), ("S10", "Apply", 5),
            ("S07", "Apply", 8), ("S08", "Analyze", 7)]
    task = {"S02": "শব্দার্থ", "S05": "বহুনির্বাচনি", "S07": "সংক্ষিপ্ত উত্তর",
            "S08": "বিস্তৃত উত্তর", "S10": "পদ নির্ণয়",
            "S12": ["যুক্তবর্ণ ভাঙা", "শব্দ গঠন"]}
    qs, slots, tasks, n = [], {}, {}, 0
    for slot, bloom, k in plan:
        for _ in range(k):
            n += 1
            qid = f"QP-BAN-C5-U99-Q{n:02d}"
            # ~20 DISTINCT tokens on purpose. Jaccard is over token SETS, so a four-word stem
            # cannot reach the 95% band by adding one word — the first draft used one and both
            # duplicate seeds failed to fire. A fixture must be able to express the thing it is
            # seeding, and a stem this length behaves like the real ones the gate will meet.
            qs.append({"qid": qid,
                       "question_text": (f"কল্পিত পাঠ নিরানব্বই থেকে নেওয়া নমুনা প্রশ্ন যাচাইয়ের "
                                         f"জন্য তৈরি এটি বাস্তব কোনো বইয়ের অংশ নয় ক্রমিক "
                                         f"{qb_bn(n)} স্লট {slot}"),
                       "question_type": "short_answer", "bloom_level": bloom,
                       "difficulty": "easy", "marks": 1,
                       "answer_key": {"accepted": [f"উত্তর {qb_bn(n)}"]}})
            slots[qid], tasks[qid] = slot, task[slot]
    return {"schema_version": "1.0", "policy_shape": "qp6", "subject": "BAN", "class": 5,
            "questions": qs, "slot_index": slots, "task_index": tasks,
            "header": {"admissible_slots": ["S02", "S05", "S07", "S08", "S10", "S12"],
                       "slot_exclusions": {}}}


def plan_selftest(ctx):
    """PLAN's own seeds. It needs its own fixture because the shared 24-item bank CANNOT pass —
    that impossibility is itself the first seed."""
    ok = True
    print()
    base = _plan_bank()
    errs, _ = g_plan(base, ctx)
    if errs:
        print(f"  FAIL  baseline: the 44-item plan fixture is not clean -> {errs}")
        ok = False
    else:
        print("  PASS  baseline: a 44-item bank at exactly +2 on every floor is SIGNABLE")

    def mut(fn):
        b = json.loads(json.dumps(base))
        fn(b)
        return b

    def retag(b, frm, to, k):
        done = 0
        for q in b["questions"]:
            if q["bloom_level"] == frm and done < k:
                q["bloom_level"] = to
                done += 1

    cases = [
        # EXACTLY-ON-FLOOR · MARGIN · POOL-TOO-SMALL · DEMAND — DELETED (CD-171(d)). All four
        # seeded a count against a POOL, and PLAN computes no counts. Their inverses are now
        # NEGATIVES below: each of the four states must make PLAN stay QUIET, which is the only
        # form of proof that survives a rule's retirement. `retag()` is kept for them.
        ("PAPER-LEVEL", "a plan ADMITTING S15 — CD-147 puts S14/S15 in the paper/exam pipeline for "
                        "EVERY chapter, and PLAN refuses it in its own voice rather than leaning "
                        "on COVERAGE: the two gates ask different questions and a bank is offered "
                        "as FINISHED on this one's verdict",
         lambda b: b["header"]["admissible_slots"].append("S15")),
        ("TASK-MISSING", "an item that declares no task at all",
         lambda b: b["task_index"].pop(b["questions"][0]["qid"])),
        ("OFF-CHOICE", "an S10 item doing ক্রিয়ার কাল — admitted at the slot, NOT selected at C5",
         lambda b: b["task_index"].update({
             next(q["qid"] for q in b["questions"] if b["slot_index"][q["qid"]] == "S10"):
             "ক্রিয়ার কাল"})),
        ("COMPOSITE-HALF", "an S12 item that breaks the যুক্তবর্ণ and never forms the শব্দ",
         lambda b: b["task_index"].update({
             next(q["qid"] for q in b["questions"] if b["slot_index"][q["qid"]] == "S12"):
             ["যুক্তবর্ণ ভাঙা"]})),
        ("P-037", "a teacher-keyed item typed `mcq` — the interim rule admits short_answer and "
                  "descriptive only",
         lambda b: b["questions"][0].update({
             "question_type": "mcq",
             "answer_key": {"accepted": ["ক"], "model_note": "শিক্ষকের দেওয়া (CD-136)"}})),
        ("DUP-EXACT", "two items in one slot carrying the SAME stem verbatim",
         lambda b: b["questions"][1].update(
             {"question_text": b["questions"][0]["question_text"]})),
        ("DUP-NEAR", "two stems 95%+ identical without being identical",
         lambda b: b["questions"][1].update(
             {"question_text": b["questions"][0]["question_text"] + " ও"})),
    ]
    for label, why, fn in cases:
        errs, _ = g_plan(mut(fn), ctx)
        if errs:
            print(f"  PASS  {label:<17} fires on: {why}")
        else:
            print(f"  FAIL  {label:<17} DID NOT FIRE on: {why}")
            ok = False

    # ── NEGATIVES ────────────────────────────────────────────────────────────────────────
    # THE FIRST FOUR ARE THE INVERTED SEEDS (CD-171(d)), and they are the load-bearing half of
    # this amendment. A rule that is retired leaves no failure to seed — the only thing that can
    # be proved is that the states it used to fail on now pass, and that they pass for the right
    # reason rather than because the gate stopped running. Each case below FAILED before CD-171.
    # This is CD-122(a)'s kept-and-inverted device, third use in this file (CD-135 used it for the
    # Bloom ceiling; CD-150 for the ENG negatives).
    def shrink(b, n):
        b["questions"] = b["questions"][:n]
        keep = {q["qid"] for q in b["questions"]}
        b["slot_index"] = {k: v for k, v in b["slot_index"].items() if k in keep}
        b["task_index"] = {k: v for k, v in b["task_index"].items() if k in keep}

    inverted = [
        ("ZERO-FLOOR-POOL", "a 12-item pool — under CD-141(g)'s retired 40-item minimum, under "
                            "REF-09 §4.3's retired 20, and short of every REF-06 §3.6 floor at "
                            "once. THE BRIEF'S NAMED CASE: it must PASS",
         lambda b: shrink(b, 12)),
        ("EXACTLY-ON-FLOOR", "a level landing EXACTLY on its floor — FAILED before CD-171 as "
                             "*landing exactly on a floor is a DEFECT, not a pass*",
         lambda b: retag(b, "Understand", "Remember", 2)),
        ("MARGIN", "margin +1, one item short of the retired rule",
         lambda b: retag(b, "Apply", "Remember", 1)),
        ("DEMAND", "an admissible slot six items under the PAPER's per-slot demand — CD-138(g) "
                   "is retired at pool level and the paper draws the rest from other chapters",
         lambda b: [b["questions"].remove(q) for q in
                    [x for x in b["questions"] if b["slot_index"][x["qid"]] == "S07"][:6]]),
    ]
    for label, why, fn in inverted:
        errs, _ = g_plan(mut(fn), ctx)
        if not errs:
            print(f"  PASS  NEGATIVE  {label:<17} stays quiet on: {why}")
        else:
            print(f"  FAIL  NEGATIVE  {label:<17} STILL FIRES on: {why} -> {errs}")
            ok = False

    errs, rep = g_plan(mut(lambda b: b["questions"][1].update(
        {"question_text": b["questions"][0]["question_text"] + " আরও দুটি শব্দ যোগ"})), ctx)
    if not errs and any("BORDERLINE" in r for r in rep):
        print("  PASS  DUP-BORDERLINE   stays quiet on: a pair in the 85–95% band — REPORTED for "
              "the Hub's subject expert, never failed and never silently dropped")
    else:
        print(f"  FAIL  DUP-BORDERLINE   band case did not REPORT-without-failing: {errs}")
        ok = False

    # THE LIVE TRUE-NEGATIVE. পাঠ ১৩ at 110 is a CONTROL drawn from the live pool, which CD-121(e)
    # permits — controls may be live, SEEDS may not. It is the only case here that proves the gate
    # is usable on real work rather than only on a fixture built to please it.
    live = ROOT / "workstreams/question-banks/banks/C5_BAN_U13_QuestionBank_v1.json"
    if live.exists():
        lb = json.loads(live.read_text(encoding="utf-8"))
        lerrs, lrep = g_plan(lb, {"slot_register": load_slot_register(ROOT)[0]})
        if not lerrs:
            print(f"  PASS  LIVE-CONTROL     stays quiet on: the signed {len(lb['questions'])}-item "
                  f"পাঠ ১৩ — every task declared and admitted, no paper-level slot claimed, and "
                  f"S12's per-word drill REPORTED as borderline rather than failed. (The margin "
                  f"and full-demand clauses this line used to cite are retired — CD-171(d).)")
        else:
            print(f"  FAIL  LIVE-CONTROL     fired on the signed bank: {lerrs}")
            ok = False
    return ok


def _qp_ctx():
    """A synthetic context. The REF-19, TOPIC_NUMBERS and SLOT_REGISTER registers are STUBBED for
    the qp_selftest so the instrument is proven against fixtures rather than against the live canon
    files — the same discipline the fixtures themselves follow."""
    return {"extraction": SYNTH_EXTRACTION,
            "ref19_slugs": SYNTH_SLUGS,
            "topic_numbers": set(SYNTH_TOPICS) | {"TOP-BAN-C5-07"},
            "slot_register": _synth_register(),
            "slot_register_error": [],
            # ENVELOPE-SYNC's fixture: an export derived from the UNMUTATED fixture bank, so it is
            # in sync by construction. Every seed then mutates the BANK and the drift appears by
            # itself — which is the real failure mode. Nobody edits an envelope by hand; the bank
            # moves and the export is left behind.
            "envelope_index": (_qp_envelopes(), _qp_envelopes(), _qp_batch(), None)}


def _qp_batch():
    """A contract-v1.1 wrapper over the fixture bank — in sync by construction, exactly as
    `build_batch.py` would emit it. Four keys, `envelope_version` "1.0" not "1.1"."""
    qs = _qp_good_bank()["questions"]
    return {"envelope_version": "1.0", "doc_type": "question_batch",
            "batch": {"bank_id": "SYNTH_Bank", "bank_version": "v1", "item_count": len(qs),
                      "digest": bank_content_digest(qs)},
            "items": [{"payload": json.loads(json.dumps(q))} for q in qs]}


def _qp_envelopes():
    """{qid: payload} for the fixture bank — what a correct `single/` and array both hold."""
    return {q["qid"]: json.loads(json.dumps(q)) for q in _qp_good_bank()["questions"]}

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
        print("  PASS  baseline: an unbroken synthetic chapter bank passes all eleven "
              "INCLUDING PLAN")
        print("        (PLAN was EXCLUDED from this baseline until 2026-08-18, and the exclusion "
              "was arithmetic rather than a waiver: a 24-item pool could not clear four positive "
              "floors with margin 2, so the minimum was 40. CD-171(d) retires the margin rule, "
              "PLAN computes no counts, and the exclusion is DELETED — the 24-item bank now "
              "passes every gate in the family with nothing held out. An exclusion kept past its "
              "reason is how a waiver gets built by accident.)")

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
    # BLOOM-BAND's two FLOOR seeds are DELETED (CD-171(d)) and re-enter as NEGATIVES below —
    # both states must now make the gate stay quiet. What replaces them as the fail-seed is the
    # only thing BLOOM-BAND still fails on: the TAG.
    add("BLOOM-BAND", "an item tagged `Synthesis` — not one of the six LOCKED levels. CD-171 "
                      "retires the DISTRIBUTION and keeps the TAG: recorded, not rationed, and "
                      "an unrecordable level is not a recording",
        lambda b: b["questions"][0].update({"bloom_level": "Synthesis"}))
    add("BLOOM-BAND", "an item with NO `bloom_level` at all — the same rule from the other side, "
                      "seeded separately because a missing key and a wrong value reach the gate "
                      "by different paths",
        lambda b: b["questions"][1].pop("bloom_level"))
    add("DIFFICULTY", "the pool cannot supply easy ≥30%",
        lambda b: [q.update({"difficulty": "medium"}) for q in b["questions"]])
    add("REPETITION", "an identical stem on two Understand items",
        lambda b: b["questions"][10].update(
            {"question_text": b["questions"][11]["question_text"]}))
    # --- COVERAGE, converted at CD-138: the register, not the header's slot list ------------
    # The six S05 items are re-slotted wholesale and the DECLARATION is moved with them, so each
    # case carries exactly one defect. A seed that also broke the floor or the declaration would
    # still go red and would prove less.
    def _reslot(b, dest, task, n=6):
        moved = [q["qid"] for q in b["questions"] if b["slot_index"][q["qid"]] == "S05"][:n]
        for qid in moved:
            b["slot_index"][qid] = dest
            b["task_index"][qid] = task
        b["header"]["admissible_slots"] = [s for s in b["header"]["admissible_slots"]
                                           if s != "S05"] + [dest]
        b["header"]["slot_exclusions"].pop(dest, None)
        b["header"]["slot_exclusions"]["S05"] = "কল্পিত পাঠ ৯৯-এ বহুনির্বাচনির উপাদান নেই"
        return b

    # --- CD-147, the categorical paper-level bar. Two failing seeds and two negatives below, and
    # --- the negatives are the half that matters: the rule REMOVES an obligation as well as adding
    # --- one, and a gate that only gained the FAIL would go red on every conformant bank.
    def _put_in_s14(b):
        qid = b["questions"][0]["qid"]
        b["slot_index"][qid] = "S14"
        b["task_index"][qid] = "আবেদনপত্র"
        return b

    add("COVERAGE", "an item sitting in S14 — paper-level for EVERY chapter (CD-147), so this is "
                    "categorical and NOT the CD-138(e) 'this chapter declared it inadmissible' "
                    "failure. The two are reported as different things because they have different "
                    "remedies: one re-declares, the other moves the item to the paper pipeline",
        _put_in_s14)
    add("COVERAGE", "a header that ADMITS S14 — CD-147 puts it outside what a chapter declaration "
                    "is entitled to say at all, so admitting it is a failure even with no item in "
                    "it",
        lambda b: b["header"]["admissible_slots"].append("S14"))
    add("ENVELOPE-SYNC", "the bank gains an item and the export does not — the export is BEHIND, "
                         "which is exactly the wave-2 shape: 36 envelopes against 88 then 110 "
                         "bank items, for two waves, seen by nothing",
        lambda b: b["questions"].append({**json.loads(json.dumps(b["questions"][0])),
                                         "qid": "QP-BAN-C5-U99-Q97"}))
    add("ENVELOPE-SYNC", "an item is RETIRED from the bank and its envelope survives — a stale "
                         "ADDITION is loud, a stale SURVIVAL is silent, and the silent one is the "
                         "one that reaches the Hub. Seven such orphans were found at the real "
                         "regeneration, five of them retired S10 ভাব নির্ণয় items",
        lambda b: b["questions"].pop())
    add("COVERAGE", "ten items in S10 doing ভাব নির্ণয় — a task admitted at NO class in the "
                    "whole spine. THIS IS THE LIVE DEFECT THE REGISTER WAS BUILT FOR: it passed "
                    "the old slot-id-presence reading, because the id was there",
        lambda b: _reslot(b, "S10", "ভাব নির্ণয়"))
    add("COVERAGE", "an OFF-CHOICE item — ক্রিয়ার কাল is in S10's admitted_set, but C5 selected "
                    "পদ নির্ণয়. A different failure from the one above and reported as one",
        lambda b: _reslot(b, "S10", "ক্রিয়ার কাল"))
    add("COVERAGE", "an item sitting in a slot THIS CHAPTER DECLARED INADMISSIBLE (CD-138(e))",
        lambda b: b["slot_index"].update(
            {b["questions"][0]["qid"]: "S12"}))
    add("COVERAGE", "a COMPOSITE slot done by halves — the item breaks the যুক্তবর্ণ and never "
                    "forms the শব্দ. Passed every gate before CD-138",
        lambda b: _reslot(b, "S12", ["যুক্তবর্ণ ভাঙা"]))
    add("COVERAGE", "an INCOMPLETE admissibility declaration — S12 neither admitted nor excluded "
                    "with a reason",
        lambda b: b["header"]["slot_exclusions"].pop("S12"))
    add("COVERAGE", "a slot excluded with an EMPTY reason — CD-134(c) requires a content reason",
        lambda b: b["header"]["slot_exclusions"].update({"S10": "   "}))
    # The S07 per-slot-demand fail-seed is DELETED (CD-171(a)(iv)) and re-enters as a NEGATIVE.
    add("COVERAGE", "an item that declares NO task — slot id alone says nothing about what it does",
        lambda b: b["task_index"].pop(b["questions"][0]["qid"]))
    add("COVERAGE", "a bank with no admissibility declaration at all",
        lambda b: b["header"].pop("admissible_slots"))
    add("COVERAGE", "a register that carries an AUTHORED chapter_authorable — CD-138(f) makes it "
                    "derived from these very declarations, never authored upstream",
        lambda b: None,
        ctx_override={"slot_register": {
            k: (dict(v, chapter_authorable=True) if k[2] == "S02" else v)
            for k, v in _synth_register().items()}})
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
    # The below-20 pool fail-seed is DELETED (CD-171(a)(iii)); the 12-item NEGATIVE above is what
    # replaces it, and it asserts the opposite verdict on the same fixture.

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
        ("BLOOM-BAND", "EVERY item becomes Remember — every OTHER level drops under its floor at "
                       "once. THIS WAS A FAIL-SEED UNTIL 2026-08-18; it is KEPT AND INVERTED "
                       "(CD-171(d)) so the floor cannot creep back unnoticed, exactly as CD-135 "
                       "kept and inverted the ceiling case. Both bounds are now a PAPER rule",
         lambda b: [q.update({"bloom_level": "Remember"}) for q in b["questions"]]),
        ("BLOOM-BAND", "Analyze at 1 of 24 = 4.2%, under REF-06 §3.6's 10% floor — the case "
                       "CD-135(h) predicted would become the binding constraint. It did, on "
                       "পাঠ ১৩ wave 3, and PENDING-P-036 measured the cost: an Analyze floor "
                       "forbade 28 of 32 items the chapter could genuinely answer. INVERTED",
         lambda b: _qp_set_blooms(b, ["Remember"] * 8 + ["Understand"] * 8 + ["Apply"] * 7
                                     + ["Analyze"] * 1)),
        ("COVERAGE", "an admissible slot under the PAPER's per-slot demand — S07 owes 4 and "
                     "supplies 2. A FAIL-SEED UNTIL 2026-08-18; INVERTED (CD-171(a)(iv)). The "
                     "paper draws S07's other two items from the chapters that carry them, which "
                     "is what *demand is paper-level* meant before it was asked of a chapter",
         lambda b: [b["questions"].remove(q) for q in list(b["questions"])
                    if b["slot_index"][q["qid"]] == "S07"][:6]),
        ("COVERAGE", "a 12-item pool — under REF-09 §4.3's retired 20-item floor. CD-171(a)(iii) "
                     "retires the READING, not the number: REF-08 §4.1's 20 sizes a HOMEWORK draw "
                     "across a year, never a bank's conformance. INVERTED, and the count is still "
                     "PRINTED so its absence reads as a ruling and not as an oversight",
         lambda b: b.update({"questions": b["questions"][:12]})),
        ("COVERAGE", "six items in S10 doing পদ নির্ণয় — the task C5 SELECTED from that slot's "
                     "three. The gate must fire on the wrong task and stay silent on the right "
                     "one, or it is not reading the task at all",
         lambda b: _reslot(b, "S10", "পদ নির্ণয়")),
        ("COVERAGE", "a slot declared inadmissible with a content reason and supplying ZERO items "
                     "— that is the declaration working, not a coverage failure (CD-138(e))",
         lambda b: None),
        ("ENVELOPE-SYNC", "an export IN SYNC with the bank — ids and payloads agree, array and "
                          "single/ agree, nothing to say. The gate that fires on a healthy export "
                          "is the gate an author learns to ignore",
         lambda b: None),
        ("COVERAGE", "a register carrying a D5 (absent) row for a slot the bank never declares — "
                     "the chapter owes it NOTHING, not even a content reason. Existence is a "
                     "CLASS-level fact and admissibility a CHAPTER-level one; requiring a পাঠ to "
                     "explain why it does not serve a question its paper has never contained "
                     "would be the two collapsed into one field (Principal, 2026-08-15)",
         lambda b: None),
        ("COVERAGE", "a register carrying a D6 school's-own row (`BAN-L01`) — skipped entirely. "
                     "An L-id is in no bank's `admissible_slots`, has no per-slot demand a "
                     "chapter could owe, and would key as `L01` against a declaration that has "
                     "never named it",
         lambda b: None),
        # CD-147's negatives. The rule REMOVED an obligation as well as adding a bar, and a gate
        # that only gained the FAIL would redden every conformant bank in the repo on its first run.
        ("COVERAGE", "a bank that declares NOTHING about S14/S15 — neither admitted nor excluded "
                     "with a reason. Under CD-138(e) that was INCOMPLETE; under CD-147 it is "
                     "CORRECT, because the bar is categorical and a chapter owes no content reason "
                     "for a slot its declaration does not reach. This is the base fixture, and it "
                     "is asserted rather than assumed",
         lambda b: None),
        ("COVERAGE", "a bank still carrying a CD-139-era content reason for S14 — accepted, not "
                     "failed. The reason is no longer owed, but a bank that records one is correct "
                     "history (AGENTS §4), and forcing a same-commit edit of three signed banks to "
                     "quiet a gate is how a correction becomes a rewrite",
         lambda b: b["header"]["slot_exclusions"].update(
             {"S14": "কল্পিত পাঠ ৯৯-এ আবেদনপত্রের কোনো নমুনা নেই"})),
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

    # --- MARK-VALUE's REFUSAL BRANCH, asserted rather than assumed. Retiring the vendored mark
    # --- tables replaced "no table vendored for (BAN, 3)" with "the register carries no rows for
    # --- BAN C3". The words changed; what must NOT change is that it is a REFUSAL — reported,
    # --- never silence, never a pass (SOURCE_POLICY §7.17). A negative case cannot prove this:
    # --- "no errors" is exactly what a gate that quietly did nothing would also produce. So the
    # --- REPORT LINE ITSELF is asserted.
    print()
    orphan = _qp_good_bank()
    orphan["class"] = 3          # the synthetic register carries C5 rows only
    o_errs, o_rep = g_mark_value(orphan, ctx)
    refused = (not o_errs) and any("carries no rows for BAN C3" in r for r in o_rep)
    print(f"  {'PASS' if refused else 'FAIL'}  MARK-VALUE     "
          + ("a bank at a class the register has not built is REFUSED BY NAME, not judged and "
             "not passed — the vendored table's own refusal, kept through the retirement"
             if refused else f"the refusal branch did not report: errs={o_errs} rep={o_rep}"))
    ok = ok and refused

    # --- And the other direction: the register is the ONLY mark authority now, so a register that
    # --- disagrees with the item must move the verdict. If it does not, the gate is still reading
    # --- something else.
    lowered = {k: {**v, "marks_per_item": 99} for k, v in _synth_register().items()}
    l_ctx = dict(ctx)
    l_ctx["slot_register"] = lowered
    l_errs, _ = g_mark_value(_qp_good_bank(), l_ctx)
    moved = bool(l_errs)
    print(f"  {'PASS' if moved else 'FAIL'}  MARK-VALUE     "
          + ("editing `marks_per_item` in the register alone moves the verdict — the retired "
             "tables are gone and nothing else is being read"
             if moved else "a register edit did NOT move the verdict — a second mark source survives"))
    ok = ok and moved

    # --- the two batch failures that a BANK mutation cannot express, because they live in the
    # --- WRAPPER's own self-description rather than in its items. Both are asserted directly.
    print()
    import copy as _copy
    good = _qp_good_bank()

    bad_count = _copy.deepcopy(_qp_batch())
    bad_count["batch"]["item_count"] = 99
    c1 = dict(ctx); c1["envelope_index"] = (_qp_envelopes(), _qp_envelopes(), bad_count, None)
    e1, _ = g_envelope_sync(good, c1)
    ok_count = any("item_count" in e for e in e1)
    print(f"  {'PASS' if ok_count else 'FAIL'}  ENVELOPE-SYNC  "
          + ("fires on: a wrapper whose item_count misdescribes its own items — the Hub rejects "
             "that WHOLE and imports nothing, so a wrapper that lies about itself is worse than a "
             "missing one: it looks importable" if ok_count else f"item_count seed did not fire: {e1}"))
    ok = ok and ok_count

    behind = _copy.deepcopy(_qp_batch())
    behind["items"].pop()
    behind["batch"]["item_count"] = len(behind["items"])   # self-consistent, still behind the bank
    c0 = dict(ctx); c0["envelope_index"] = (_qp_envelopes(), _qp_envelopes(), behind, None)
    e0, _ = g_envelope_sync(good, c0)
    ok_behind = any("absent from the wrapper" in e for e in e0)
    print(f"  {'PASS' if ok_behind else 'FAIL'}  ENVELOPE-SYNC  "
          + ("fires on: a wrapper BEHIND the bank while array and single/ are current — the third "
             "artifact drifts on its own, and it is internally consistent while doing so"
             if ok_behind else f"behind-batch seed did not fire: {e0}"))
    ok = ok and ok_behind

    orphaned = _copy.deepcopy(_qp_batch())
    orphaned["items"].append({"payload": {"qid": "QP-BAN-C5-U99-Q95"}})
    orphaned["batch"]["item_count"] = len(orphaned["items"])
    cO = dict(ctx); cO["envelope_index"] = (_qp_envelopes(), _qp_envelopes(), orphaned, None)
    eO, _ = g_envelope_sync(good, cO)
    ok_orphan = any("RETIRED content" in e for e in eO)
    print(f"  {'PASS' if ok_orphan else 'FAIL'}  ENVELOPE-SYNC  "
          + ("fires on: a wrapper carrying an item the bank no longer has — the silent half of the "
             "wave-2 defect, now in the file the Hub actually reads"
             if ok_orphan else f"orphan-batch seed did not fire: {eO}"))
    ok = ok and ok_orphan

    bad_digest = _copy.deepcopy(_qp_batch())
    bad_digest["batch"]["digest"] = "0" * 64
    c2 = dict(ctx); c2["envelope_index"] = (_qp_envelopes(), _qp_envelopes(), bad_digest, None)
    e2, _ = g_envelope_sync(good, c2)
    ok_digest = any("digest" in e for e in e2)
    print(f"  {'PASS' if ok_digest else 'FAIL'}  ENVELOPE-SYNC  "
          + ("fires on: a wrapper describing a DIFFERENT bank than the one on disk. The contract "
             "does NOT recompute digest at import — it is an audit field — so nothing downstream "
             "catches this, which is precisely why it is caught here"
             if ok_digest else f"digest seed did not fire: {e2}"))
    ok = ok and ok_digest

    c3 = dict(ctx); c3["envelope_index"] = (_qp_envelopes(), _qp_envelopes(), None, None)
    e3, r3 = g_envelope_sync(good, c3)
    ok_absent = (not e3) and any("has not been built" in r for r in r3)
    print(f"  {'PASS' if ok_absent else 'FAIL'}  ENVELOPE-SYNC  "
          + ("stays quiet on: no `.batch.json` at all — an unrun step is not drift, and failing "
             "there would fire on every bank exported before v1.1 (SOURCE_POLICY §7.17)"
             if ok_absent else f"absent-batch case wrong: errs={e3}"))
    ok = ok and ok_absent

    # --- CD-138(b): THE MARKER-EDIT SEED. A gate whose verdict moves when a marker string is
    # --- edited is non-conformant. Here the whole of the register's PROSE — the fields that
    # --- carry or quote the markers (যেকোনো একটা · অথবা · বা · ও · + · ভেঙে) — is rewritten to
    # --- garbage while every DECLARED field is left untouched. The verdict must not move.
    # --- The other half of this seed lives at build time in tools/audits/slot_register_check.py,
    # --- which strips the markers from the SPINE ITSELF and re-runs. Together they cover both
    # --- files; this suite opens no spine at all, which is the structural half of the guarantee.
    print()
    scrubbed = {}
    for k, v in _synth_register().items():
        v = dict(v)
        v["slot_task"] = "যেকোনো একটা অথবা বা ও + ভেঙে — এই লেখাটার কোনো মানে নেই"
        v["nape_frame"] = "MARKER SOUP অথবা যেকোনো একটা"
        v["row_constraints"] = [{"id": "NOISE", "text": "ভেঙে অথবা যেকোনো একটা"}]
        scrubbed[k] = v
    base_ctx = dict(ctx)
    noise_ctx = dict(ctx)
    noise_ctx["slot_register"] = scrubbed
    a = qp_run(_qp_good_bank(), base_ctx, quiet=True)[0]
    b_ = qp_run(_qp_good_bank(), noise_ctx, quiet=True)[0]
    # THE PROPERTY UNDER TEST IS THAT THE VERDICT DOES NOT MOVE, not that it is empty. It was
    # written as `== []` while the fixture happened to be clean, and PLAN broke that accident: the
    # 24-item fixture now carries a pool-too-small failure, IDENTICALLY on both sides, which is
    # itself evidence the marker edit changed nothing. Equality is the assertion CD-138(b) needs.
    marker_ok = (a == b_)
    print(f"  {'PASS' if marker_ok else 'FAIL'}  CD-138(b)      "
          + ("every marker-bearing prose field in the register rewritten to noise — verdict "
             "byte-identical, because COVERAGE reads DECLARED fields and no marker string"
             if marker_ok else f"marker edit moved the verdict: {a} -> {b_}"))
    ok = ok and marker_ok

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
    # Same correction as CD-138(b)'s marker seed: the property is that the two verdicts are
    # IDENTICAL, not that they are empty. `== []` was true only while the 24-item fixture happened
    # to be clean, and PLAN's arithmetic ended that. Identical-and-non-empty still proves the
    # marker changed nothing, which is the whole claim.
    dcheck("and it changes no verdict: marked and unmarked copies of the same bank give "
           "byte-identical gate output",
           qp_run(_marked(), ctx, quiet=True)[0] == f_unmarked)

    b = _qp_good_bank()
    b["header"]["অবস্থা"] = "সম্পূর্ণ"
    in_ctl, reason = classify(Path("synthetic.json"), b)
    dcheck(f"an `অবস্থা` carrying some other word is REFUSED — §7.9 defines exactly one marker",
           (not in_ctl) and reason.startswith("REFUSED"))

    ok = ok and all(decl)

    # PLAN's own block, with its own 44-item fixture and its own baseline. It runs LAST so the
    # arithmetic note above is already on screen when its POOL-TOO-SMALL seed appears.
    plan_ok = plan_selftest(ctx)
    ok = ok and plan_ok

    # cd158_selftest DELETED with the margin apparatus it proved (CD-171(d)). Its target,
    # PLAN_MARGIN_EXCEPTIONS, no longer exists, and a seed with no target is TOOLS-CR-007's
    # vacuous shape: it would pass every run while proving nothing.

    print(f"\nSELFTEST RESULT: {'PASS' if ok else 'FAIL'} "
          f"({len(cases)} seeded failures + {len(negatives)} negatives + {len(decl)} "
          f"CD-055 declaration cases + 1 baseline, across all {sum(1 for _, i, _ in GATES if 'qp6' in i)} gates; "
          f"PLAN adds 7 seeds + 6 negatives + 1 baseline on its own 44-item fixture — FOUR of "
          f"those negatives are CD-171(d)'s inverted seeds, and they are the load-bearing half: "
          f"a retired rule leaves no failure to seed, so the only available proof is that the "
          f"states it used to fail on now pass)")
    return ok


def cd150_selftest():
    """CD-150's re-key, both directions, on the ENUMERATION and on a real gate run.

    Two halves, and the second is the one that could not be faked. The first asserts
    `is_paper_level` pair by pair — cheap, exhaustive over the boundary, and it is what catches a
    fat-fingered class number in the constant. The second pushes SYNTHETIC ENG banks through
    `g_coverage` itself, because a constant can be right while the eight call sites that read it
    are wrong, and the old flat set is proof that call sites are where this breaks.

    All fixtures are synthetic (QB-D-012, CD-121(e)). No `canon/marklogic` file is read here; the
    live register carries no ENG rows at this commit and reading it would make the ENG half of this
    block vacuous rather than green.
    """
    print("\n--- CD-150 · paper-level re-keyed to (subject, class, slot) "
          + "-" * 19)
    ok = True

    # ── half one: the enumeration, at and around every boundary ──────────────────────────
    pairs = [
        # ENG-S05 — the unseen passage. Textbook-EXTERNAL by the spine's own statement, so no
        # chapter can source it. C1/C2 carry no S05 at all (D5), hence quiet there.
        ("ENG", 5, "S05", True), ("ENG", 4, "S05", True), ("ENG", 3, "S05", True),
        ("ENG", 2, "S05", False), ("ENG", 1, "S05", False),
        # ENG-S13 চিঠি/আবেদনপত্র/ইমেইল — barred at C4/C5 where the class's admitted task IS the
        # letter. C3 dialogue · C2 self-introduction · C1 greeting fill-in are D4 SUBSTITUTES, a
        # different task, and they stay in the chapter lane.
        ("ENG", 5, "S13", True), ("ENG", 4, "S13", True),
        ("ENG", 3, "S13", False), ("ENG", 2, "S13", False), ("ENG", 1, "S13", False),
        # ENG-S14 রচনা — barred at C4/C5 where composition is open. C2/C3 guided paragraph is a
        # D4 substitute and stays. C1 has no S14 at all.
        ("ENG", 5, "S14", True), ("ENG", 4, "S14", True),
        ("ENG", 3, "S14", False), ("ENG", 2, "S14", False), ("ENG", 1, "S14", False),
        # ENG has NO S15. Nothing is to look for one, at any class (CD-150).
        ("ENG", 5, "S15", False), ("ENG", 4, "S15", False),
        # BAN — CD-147 behaviour preserved byte-for-byte by the re-key.
        ("BAN", 5, "S14", True), ("BAN", 1, "S14", True),
        ("BAN", 5, "S15", True), ("BAN", 1, "S15", True),
        # THE REGRESSION THAT MADE THE RE-KEY NECESSARY. `BAN-S05` is বহুনির্বাচনি and `BAN-S13` is
        # এক কথায় প্রকাশ — live teaching slots. A flat set holding the SHORTS `S05`/`S13` for ENG's
        # sake would have barred both from every chapter bank in the repo.
        ("BAN", 5, "S05", False), ("BAN", 4, "S05", False), ("BAN", 3, "S05", False),
        ("BAN", 2, "S05", False), ("BAN", 1, "S05", False),
        ("BAN", 5, "S13", False), ("BAN", 4, "S13", False), ("BAN", 3, "S13", False),
    ]
    bad = [(sub, c, sl, want, is_paper_level(sub, c, sl))
           for sub, c, sl, want in pairs if is_paper_level(sub, c, sl) != want]
    if bad:
        for sub, c, sl, want, got in bad:
            print(f"  FAIL  ENUMERATION  {sub} C{c} {sl}: expected {want}, got {got}")
        ok = False
    else:
        n_bar = sum(1 for *_, w in pairs if w)
        print(f"  PASS  ENUMERATION  {len(pairs)} (subject, class, slot) assertions — {n_bar} "
              f"barred, {len(pairs) - n_bar} chapter-lane, boundary classes asserted on BOTH sides")
        print(f"  PASS  REGRESSION   BAN-S05 (বহুনির্বাচনি) and BAN-S13 (এক কথায় প্রকাশ) remain "
              f"chapter-admissible at EVERY class — the collision a flat set of slot shorts would "
              f"have caused, asserted rather than argued")

    # ── half two: the same rule through g_coverage, on synthetic ENG banks ────────────────
    def eng_register(cls):
        """A synthetic ENG register slice: the three barred slots plus one ordinary one."""
        def r(slot, items, mpi, task):
            return {"subject": "ENG", "class": cls, "slot": f"ENG-{slot}", "task_mode": "simple",
                    "slot_task": f"synthetic {slot}", "nape_frame": f"synthetic {slot}",
                    "admitted_task": task, "items_per_paper": items, "marks": items * mpi,
                    "marks_per_item": mpi, "d_code": "D0", "authority": "SYNTHETIC — not NAPE",
                    "row_constraints": []}
        rows = [r("S02", 5, 1, "make sentences"), r("S05", 3, 3, "unseen passage"),
                r("S13", 1, 10, "letter"), r("S14", 1, 10, "composition")]
        return {(x["subject"], x["class"], x["slot"].split("-")[-1]): x for x in rows}

    def eng_bank(cls, admissible, slots, tasks):
        qs = [{"qid": f"SY-ENG-C{cls}-Q{i:02d}", "question_text": f"synthetic stem {i}",
               "marks": 1, "bloom_level": "Remember", "question_type": "short_answer",
               "topic_tag": "SY-TOPIC", "difficulty": "easy"} for i in range(1, 21)]
        return {"subject": "ENG", "class": cls, "questions": qs, "topics": ["SY-TOPIC"],
                "header": {"admissible_slots": list(admissible), "slot_exclusions": {},
                           "topics": ["SY-TOPIC"]},
                "slot_index": {q["qid"]: slots.get(q["qid"], "S02") for q in qs},
                "task_index": {q["qid"]: tasks.get(q["qid"], "make sentences") for q in qs}}

    def cov(cls, admissible, put=None):
        b = eng_bank(cls, admissible, {}, {})
        if put:
            qid = b["questions"][0]["qid"]
            b["slot_index"][qid], b["task_index"][qid] = put
        e, _ = g_coverage(b, {"slot_register": eng_register(cls), "slot_register_error": []})
        return e

    runs = [
        ("C5 bank with an item IN S05", 5, ["S02"], ("S05", "unseen passage"), True,
         "the unseen passage is textbook-EXTERNAL — no chapter can source it, so an item there is "
         "categorical, not a mis-declaration"),
        ("C5 bank with an item IN S13", 5, ["S02"], ("S13", "letter"), True, "চিঠি at C5"),
        ("C5 bank with an item IN S14", 5, ["S02"], ("S14", "composition"), True, "রচনা at C5"),
        ("C5 header ADMITTING S13", 5, ["S02", "S13"], None, True,
         "admitting is a failure even with no item in it"),
        ("C5 bank omitting all three", 5, ["S02"], None, False,
         "OWES NO REASON — the obligation CD-150 removes. A gate that only gained the FAIL would "
         "redden every conformant ENG bank on its first run"),
        ("C3 bank with an item IN S13", 3, ["S02", "S13"], ("S13", "letter"), False,
         "C3's S13 is DIALOGUE, a D4 substitute — chapter lane, and the bar must not reach it"),
        ("C3 bank with an item IN S14", 3, ["S02", "S14"], ("S14", "composition"), False,
         "C3's S14 is the guided paragraph — chapter lane"),
    ]
    for label, cls, adm, put, want_fail, why in runs:
        errs = cov(cls, adm, put)
        hit = [e for e in errs if "PAPER-LEVEL" in e or "paper-level" in e]
        got_fail = bool(hit)
        if got_fail == want_fail:
            print(f"  PASS  {'FAIL-SEED ' if want_fail else 'NEGATIVE  '} {label:<32} "
                  f"{'fires' if got_fail else 'quiet'}: {why}")
        else:
            print(f"  FAIL  {'FAIL-SEED ' if want_fail else 'NEGATIVE  '} {label:<32} "
                  f"expected {'a paper-level failure' if want_fail else 'silence'}; got {errs}")
            ok = False

    # MARK-VALUE and the half mark: 0.5 is admitted at ENG-S10 as DATA, and the gate needed no
    # change for it. The I-4 INVARIANT lives in tools/audits/slot_register_check.py as a closed
    # literal (Principal ruling 2026-08-16) — MARK-VALUE's job is only that an item matches the
    # register cell, and this proves 0.5 survives that comparison rather than being coerced.
    reg10 = {("ENG", 5, "S10"): {"subject": "ENG", "class": 5, "slot": "ENG-S10",
                                 "task_mode": "simple", "slot_task": "capitals & punctuation",
                                 "nape_frame": "0.5x10", "admitted_task": "capitals",
                                 "items_per_paper": 10, "marks": 5, "marks_per_item": 0.5,
                                 "d_code": "D0", "authority": "SYNTHETIC", "row_constraints": []}}
    b10 = {"subject": "ENG", "class": 5,
           "questions": [{"qid": "SY-ENG-S10-Q01", "marks": 0.5}],
           "slot_index": {"SY-ENG-S10-Q01": "S10"}}
    e_ok, _ = g_mark_value(b10, {"slot_register": reg10, "slot_register_error": []})
    b10_bad = json.loads(json.dumps(b10))
    b10_bad["questions"][0]["marks"] = 1
    e_bad, _ = g_mark_value(b10_bad, {"slot_register": reg10, "slot_register_error": []})
    if not e_ok and e_bad:
        print("  PASS  MARK-VALUE   ENG-S10 at 0.5 is quiet and the same item at 1 FAILs — the "
              "half mark rides through as DATA, and no gate code was changed to admit it")
    else:
        print(f"  FAIL  MARK-VALUE   0.5 handling wrong: quiet-case {e_ok}, must-fail case {e_bad}")
        ok = False
    return ok


def unselected_selftest():
    """The UNSELECTED state, both directions, at BOTH off-choice sites (COVERAGE and PLAN).

    Principal ruling 2026-08-16. A register row whose class narrowed to no form declares
    `selected: null` plus a required `unselected_reason`; every member of `admitted_set` is then
    admitted and none of them is off-choice.

    **The load-bearing half is the NEGATIVE**, and it is why this block exists rather than a
    single seed: a correct register with a gate that reddens conformant items is worse than not
    landing the rows at all, because the register would say "either form" while the gate failed
    both — `c == row["selected"]` can never hold against null. **The regression seed is the other
    half**: a row that DOES carry a real selection must still fail off-choice items, or the fix
    would have bought silence everywhere by turning every alternative row into a free-for-all.

    Fixtures synthetic (QB-D-012, CD-121(e)).
    """
    print("\n--- UNSELECTED · alternative rows the source declined to narrow "
          + "-" * 14)
    ok = True
    SET = ["ফরম পূরণ", "সময় ও সংখ্যা"]

    def reg(selected, reason=None):
        r = {"subject": "ENG", "class": 5, "slot": "ENG-S11", "task_mode": "alternative",
             "slot_task": "synthetic S11", "nape_frame": "synthetic", "admitted_set": SET,
             "selected": selected, "items_per_paper": 5, "marks": 5, "marks_per_item": 1,
             "d_code": "D0", "authority": "SYNTHETIC — not NAPE", "row_constraints": []}
        if reason:
            r["unselected_reason"] = reason
        return {("ENG", 5, "S11"): r}

    def bank(task):
        qs = [{"qid": f"SY-Q{i:02d}", "question_text": f"synthetic stem {i}", "marks": 1,
               "bloom_level": "Remember", "question_type": "short_answer",
               "topic_tag": "SY-TOPIC", "difficulty": "easy"} for i in range(1, 21)]
        return {"subject": "ENG", "class": 5, "questions": qs, "topics": ["SY-TOPIC"],
                "header": {"admissible_slots": ["S11"], "slot_exclusions": {},
                           "topics": ["SY-TOPIC"]},
                "slot_index": {q["qid"]: "S11" for q in qs},
                "task_index": {q["qid"]: task for q in qs}}

    def cov_task_errs(selected, task, reason="কোনো সূত্র সংকীর্ণ করেনি"):
        e, _ = g_coverage(bank(task), {"slot_register": reg(selected, reason),
                                       "slot_register_error": []})
        return [x for x in e if "does `" in x or "SELECTED" in x]

    cases = [
        ("UNSELECTED, item does form A", None, SET[0], [],
         "admitted — the register narrowed to nothing, so this is not off-choice"),
        ("UNSELECTED, item does form B", None, SET[1], [],
         "the OTHER form, equally admitted — this is the half a naive fix would have broken"),
        ("UNSELECTED, item does neither", None, "বিপরীত শব্দ", ["fires"],
         "UNSELECTED widens the set to all of admitted_set, NOT to anything at all"),
        ("SELECTED, item does the selection", SET[1], SET[1], [],
         "ordinary selected behaviour, unchanged"),
        ("SELECTED, item does the OTHER admitted form", SET[1], SET[0], ["fires"],
         "THE REGRESSION SEED — a row with a real selection still FAILs off-choice items; the "
         "UNSELECTED branch must not have turned every alternative row into a free-for-all"),
    ]
    for label, sel, task, want, why in cases:
        errs = cov_task_errs(sel, task)
        got = ["fires"] if errs else []
        if got == want:
            print(f"  PASS  COVERAGE   {label:<38} {'fires' if got else 'quiet'}: {why}")
        else:
            print(f"  FAIL  COVERAGE   {label:<38} expected "
                  f"{'a failure' if want else 'silence'}; got {errs}")
            ok = False

    # PLAN carries its OWN copy of the off-choice check (it asks whether a bank is SIGNABLE and
    # does not lean on COVERAGE's verdict), so it is asserted separately at both directions.
    def plan_task_errs(selected, task):
        b = bank(task)
        e, _ = g_plan(b, {"slot_register": reg(selected, "কোনো সূত্র সংকীর্ণ করেনি")})
        return [x for x in e if "SELECTED" in x]

    for label, sel, task, want, why in [
        ("UNSELECTED, item does form B", None, SET[1], [], "admitted at PLAN too"),
        ("SELECTED, item does the OTHER form", SET[1], SET[0], ["fires"],
         "PLAN's own off-choice check survives the change"),
    ]:
        errs = plan_task_errs(sel, task)
        got = ["fires"] if errs else []
        if got == want:
            print(f"  PASS  PLAN       {label:<38} {'fires' if got else 'quiet'}: {why}")
        else:
            print(f"  FAIL  PLAN       {label:<38} expected "
                  f"{'a failure' if want else 'silence'}; got {errs}")
            ok = False
    return ok


def taught_set_selftest():
    """CD-165 · CD-166 · CD-169 — the taught-set check, seeded BOTH ways and against BOTH failed drafts.

    Fixtures synthetic (QB-D-012, CD-121(e)): a fictional (BAN, C5, S11) row and a 20-item bank whose
    only variable is what punctuation its accepted answers carry.

    THE LAST TWO CASES ARE REGRESSION SEEDS FOR DRAFTS THAT SHIPPED WRONG IN THIS FILE'S HISTORY, and
    they are the reason this block exists rather than a single fail-case:
      * a note that MENTIONS a barred mark while the answer carries none must stay QUIET — draft 1
        scanned prose and failed an item for saying "ড্যাশের দরকার নেই", i.e. for saying no.
      * an item whose FIRST variant carries a barred mark and whose SECOND does not must stay quiet and
        be REPORTED — draft 2 scanned the variants joined and failed an item a student could answer
        correctly.
    """
    print("\n--- TAUGHT SET · the বিরামচিহ্ন a class is taught " + "-" * 27)
    ok = True
    FIVE = ["দাঁড়ি", "কমা", "প্রশ্নচিহ্ন", "বিস্ময়চিহ্ন", "উদ্ধরণ চিহ্ন"]

    def reg(taught):
        r = {"subject": "BAN", "class": 5, "slot": "BAN-S11", "task_mode": "alternative",
             "slot_task": "synthetic বিরামচিহ্ন", "nape_frame": "synthetic",
             "admitted_set": ["বিরামচিহ্ন বসানো"], "selected": "বিরামচিহ্ন বসানো",
             "items_per_paper": 5, "marks": 5, "marks_per_item": 1, "d_code": "D0",
             "authority": "SYNTHETIC — not NAPE", "row_constraints": []}
        if taught is not None:
            r["taught_set"] = taught
            r["taught_set_source"] = "SYNTHETIC — not the spine"
        return {("BAN", 5, "S11"): r}

    def bank(accepted, note="", qids=None):
        ids = qids or [f"SY-Q{i:02d}" for i in range(1, 21)]
        qs = [{"qid": qid, "question_text": "কল্পিত উদ্দীপক", "marks": 1,
               "bloom_level": "Apply", "question_type": "short_answer", "topic_tag": "SY-TOPIC",
               "difficulty": "easy",
               "answer_key": {"accepted": list(accepted), "model_note": note}}
              for qid in ids]
        return {"subject": "BAN", "class": 5, "questions": qs, "topics": ["SY-TOPIC"],
                "header": {"admissible_slots": ["S11"], "slot_exclusions": {},
                           "topics": ["SY-TOPIC"], "reason": "synthetic"},
                "slot_index": {q["qid"]: "S11" for q in qs},
                "task_index": {q["qid"]: "বিরামচিহ্ন বসানো" for q in qs}}

    def run_case(taught, accepted, note=""):
        errs, rep = g_coverage(bank(accepted, note),
                               {"slot_register": reg(taught), "slot_register_error": []})
        return ([e for e in errs if "taught set" in e or "`taught_set`" in e],
                [r for r in rep if "accepted[0]" in r])

    cases = [
        ("a সেমিকোলন in the only accepted answer", FIVE, ["কথাটি চলছে;"], "", True, False,
         "the poem's own mark is still a mark the class is not taught"),
        ("a ড্যাশ in the only accepted answer", FIVE, ["কথাটি চলছে—"], "", True, False,
         "same, on the other barred mark"),
        ("the four admitted marks, all at once", FIVE,
         ["আম্মা বলেন, 'পড়ো।' কে বলল? কী আনন্দ!"], "", False, False,
         "কমা · উদ্ধরণ · দাঁড়ি · প্রশ্নচিহ্ন · বিস্ময়চিহ্ন together — every one admitted, so silence"),
        ("NO `taught_set` on the row at all", None, ["কথাটি শেষ।"], "", True, False,
         "ABSENCE IS NOT PERMISSION (CD-165) — a class whose marks are undeclared cannot have its "
         "S11 items checked, so none of them passes"),
        ("a note SAYING the barred mark is not needed", FIVE, ["কথাটি শেষ।"],
         "ড্যাশের দরকার নেই; এখানে কেবল দাঁড়ি।", False, False,
         "DRAFT-1 REGRESSION SEED — prose about a mark is not a mark, and a check that cannot tell "
         "REQUIRES from FORBIDS fails an item for getting it right"),
        ("variant 1 barred, variant 2 clean", FIVE, ["তালিকা — শেষ।", "তালিকা, শেষ।"], "",
         False, True,
         "DRAFT-2 REGRESSION SEED — a student writing variant 2 is right, so nothing is REQUIRED "
         "outside the set; PASSES and is REPORTED, because accepted[0] is what a marker reads first"),
    ]
    for label, taught, accepted, note, want_fail, want_rep, why in cases:
        errs, reps = run_case(taught, accepted, note)
        bad = (bool(errs) != want_fail) or (bool(reps) != want_rep)
        state = ("fires" if errs else "quiet") + (" + REPORTS" if reps else "")
        if bad:
            print(f"  FAIL  TAUGHT SET  {label:<44} expected "
                  f"{'a failure' if want_fail else 'silence'}"
                  f"{' + a report' if want_rep else ''}; got {state} {errs or ''}")
            ok = False
        else:
            print(f"  PASS  TAUGHT SET  {label:<44} {state}: {why}")

    # ── CD-172 · THE NAMED EXCLUSION, SEEDED BOTH DIRECTIONS ─────────────────────────────
    #
    # THE FIXTURE IS SYNTHETIC AND THE IDS ARE REAL, and that combination is deliberate rather
    # than sloppy. QB-D-012 bars a seed from reading the LIVE POOL, and nothing here does: the
    # register row, the bank, the stimulus and the answers are all invented. What is borrowed is
    # two ID STRINGS, and it has to be — the exclusion is keyed by id, so a seed using invented
    # ids would exercise nothing and prove nothing. Reading a literal out of the gate under test
    # is what a seed IS.
    #
    # THE SECOND CASE IS THE LOAD-BEARING ONE. An exclusion whose only proof is that the excluded
    # ids pass has proved the wrong half: what matters is that a THIRD item, in the same bank, in
    # the same slot, requiring the SAME barred mark, still FAILS. Otherwise the id key is
    # decoration over a check-level exclusion, which CD-172 expressly refuses.
    print()
    excluded = sorted(CD172_TAUGHT_SET_EXCLUDED)
    cd172 = [
        ("the two CD-172 ids, each requiring a BARRED mark", excluded, ["তালিকা — শেষ;"],
         False,
         "NAMED, JUSTIFIED, ID-KEYED — the defect is real and is REPORTED in full; what it does "
         "not do is fail CD-153's push condition, because CD-169 rules the items RETAINED and "
         "CD-170 bars the repo from fixing them"),
        ("a THIRD id in the SAME slot requiring ড্যাশ", excluded + ["QP-BAN-C5-U15-Q99"],
         ["তালিকা — শেষ;"], True,
         "THE LOAD-BEARING SEED — same bank, same slot, same barred mark, id not on the list. It "
         "MUST still FAIL, or the exclusion is check-level in disguise and every future taught-set "
         "defect went invisible to buy two items' silence"),
    ]
    for label, qids, accepted, want_fail, why in cd172:
        errs, rep = g_coverage(bank(accepted, "", qids),
                               {"slot_register": reg(FIVE), "slot_register_error": []})
        taught_errs = [e for e in errs if "taught set" in e]
        got_fail = bool(taught_errs)
        named = [r for r in rep if "CD-172 NAMED EXCLUSION" in r]
        if got_fail == want_fail and len(named) == len(excluded):
            print(f"  PASS  CD-172  {'FAIL-SEED' if want_fail else 'NEGATIVE '} {label:<48} "
                  f"{'fires' if got_fail else 'quiet'}, {len(named)} excluded id(s) REPORTED BY "
                  f"NAME: {why}")
        else:
            print(f"  FAIL  CD-172  {label:<48} expected "
                  f"{'a failure' if want_fail else 'silence'} with {len(excluded)} named report(s); "
                  f"got {'a failure' if got_fail else 'silence'} with {len(named)} — {taught_errs}")
            ok = False

    # NEVER A SILENT SKIP, asserted on its own rather than inferred from the two cases above.
    errs, rep = g_coverage(bank(["তালিকা — শেষ;"], "", excluded),
                           {"slot_register": reg(FIVE), "slot_register_error": []})
    roster = [r for r in rep if "CD-172 ROSTER" in r]
    if len(roster) == 1 and all(q in roster[0] for q in excluded):
        print(f"  PASS  CD-172  ROSTER    prints every run, naming both ids and which EXERCISED "
              f"the exclusion — an exclusion that prints only when used is invisible on the run "
              f"it stops being needed")
    else:
        print(f"  FAIL  CD-172  ROSTER    did not print both ids: {roster}")
        ok = False

    # THE DISCHARGE SIGNAL — the same fixture with the barred mark REMOVED, standing in for the
    # Hub having disposed of the items. The roster must then say UNEXERCISED, which is CD-172's
    # own expiry notice.
    errs, rep = g_coverage(bank(["তালিকা, শেষ।"], "", excluded),
                           {"slot_register": reg(FIVE), "slot_register_error": []})
    disch = [r for r in rep if "CD-172 UNEXERCISED" in r]
    if not errs and len(disch) == 1 and all(q in disch[0] for q in excluded):
        print("  PASS  CD-172  DISCHARGE prints UNEXERCISED once the ids stop needing the "
              "exclusion — the expiry condition announces itself on the run it becomes true, "
              "rather than waiting for somebody to re-read the row (CD-160: a list drifts)")
    else:
        print(f"  FAIL  CD-172  DISCHARGE signal did not print: {disch} / {errs}")
        ok = False

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
    c = cd150_selftest()
    d = unselected_selftest()
    e = taught_set_selftest()
    if not (a and b and c and d and e):
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
    fails, report = run(bank, bank_path=path)
    for gate, line in report:
        print(f"  REPORT  {gate:<18} {line}")
    print(f"RESULT: {'FAIL' if fails else 'CLEAN'} ({len(fails)} failures)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
