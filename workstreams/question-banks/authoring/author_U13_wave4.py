#!/usr/bin/env python3
"""author_U13_wave4.py — C5 BAN পাঠ ১৩ পাখির মতো, WAVE 4.

THE RE-AUTHOR. Authorised by the Principal 2026-08-15 after the plan table was countersigned.

WHAT THIS WAVE IS FOR. Wave 3 left the bank at 88 items and green on a gate that could not see
the defect: `COVERAGE` read SLOT-ID PRESENCE, so ten items sitting in `S10` doing ভাব নির্ণয় —
a task admitted at NO class anywhere in `MarkLogic_BAN_Spine.md` — passed because the id `S10`
was present. CD-138 built the register that reads the TASK, and this wave is the first bank
re-authored against it.

THE ORDER IS RULED AND IT MATTERS. Re-tags FIRST, then retirements, then rewrites, then the new
items. The four re-tags move `Understand → Remember`, so every count downstream of them is wrong
if they run last — and the Apply/Understand floors are decided by exactly those counts.

  1. RE-TAG (4) — Q11 · Q13 · Q14 · Q72, all S07. Each is answered verbatim by the poem's own
     next line, so under the tag-down rule they read `Remember`. Q13 was already RAISED as a
     Subject Lead review item in wave 3's own header and is now ruled.
  2. RETIRE (11) — the ten S10 ভাব নির্ণয় items, and Q34.
       · The ten are NOT re-slottable. ভাব নির্ণয় is admitted at no class in the whole spine
         (C3 is বাক্যের প্রকার, C2 is ক্রিয়ার পুরুষ-সংগতি), so there is no slot to move them to.
         They cost the pool 3 `Understand` and 7 `Apply` — which is why S03 and S11 go to their
         content limits below.
       · Q34 (মিল-শব্দ, অনুশীলনী ৩) rode S07 as an acknowledged workaround. Under CD-138(b) it
         would have to DECLARE S07's `মূল কাঠামো`, and it does not do that task. **A declaration
         that is convenient is still false**, and the Principal rejected it rather than let the
         bank carry one. This is the case CD-138(b) was written for and it is recorded here.
  3. REWRITE (6) — three off-choice, three composite-fail. Neither group is retired; both are
     defects in the item, not in the item's right to exist.
       · Q57 · Q58 · Q59 did প্রশ্ন তৈরি. That task IS in S11's `admitted_set`, but C5
         `selected` বিরামচিহ্ন বসানো — an OFF-CHOICE item, which CD-138(b) reports as a
         different thing from a task admitted nowhere.
       · Q51 · Q52 · Q53 did *"যুক্তবর্ণটি ভেঙে লেখো"* and stopped. The register makes S12
         `composite` with parts যুক্তবর্ণ ভাঙা + শব্দ গঠন: an item that only breaks the conjunct
         does half the task. Their Bloom moves `Remember → Apply` as NEW CONTENT ON REWRITE, not
         as a silent re-tag — forming a word that is not in the poem cannot be answered by recall.
         Wave 3 tagged them `Remember` under the tag-down rule while they were half-items, and
         that reading was correct for what they then were.
  4. AUTHOR (33) — S03 +5 · S05 +2 · S06 +4 · S07 +2 · S08 +2 · S10 +10 · S11 +3 · S12 +2 · S13 +3.

THE TARGET IS 110 AND NO NUMBER IS CARRIED. Recomputed in session, twice: once for the plan
table, and again after Q34's retirement was ruled — Q34 was the pool's only S07 `Apply` item, so
its removal lands on the tightest floor of the three. The second recomputation is why S10 carries
one `Apply` item and not ten `Understand` ones (see S10 below).

FIVE REMEMBER ITEMS ARE LEFT UNEXTRACTED ON PURPOSE (Principal, HOLD). S02 supports two more
(ফেরেস্তা · বকুল) and S04 three more. All five are `Remember`; taking them lifts the pool without
lifting `Apply`, and `Apply` has no slot left with content headroom. They are recorded in the
header's gaps so a later wave can take them if the Apply base grows. **An unextracted item that
is written down is a decision; one that is not is an oversight.**

CONSTRAINTS HELD: P-037 (every teacher-keyed item is `short_answer`; none is any other type, so
the stop-and-ask never fires) · C-03 (অনুশীলনী ৫'s barred sentence is not used — and the one item
that carried its substitute, Q23, is retired with the rest of S10) · E-AUTHOR-ENDORSE (the poet is
named as fact only, with no honorific anywhere in this file) · §4's near-duplicate ban, applied at
plan level before a line was written.

Every anchor is validated against the extraction before the bank is written — the script refuses
rather than emitting a bank the gate would then reject.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BANK = ROOT / "workstreams/question-banks/banks/C5_BAN_U13_QuestionBank_v1.json"
EXTRACTION = ROOT / "canon/marklogic/C5_Bangla_Source_13-23.md"

POEM, VOCAB, SENT = "TOP-BAN-C5-05", "TOP-BAN-C5-01", "TOP-BAN-C5-02"
CH = "পাঠ ১৩ — পাখির মতো"

# CD-136: the declaration every teacher-supplied language key carries in its OWN model_note, so
# the provenance travels with the item and not only with the bank header.
TS = ("এই উত্তরকুঞ্জি শিক্ষকের দেওয়া — বাংলা ভাষার সাধারণ তথ্য, পাঠে এর উত্তর দেওয়া নেই "
      "(CD-136)। উদ্দীপক পাঠ ১৩ থেকেই নেওয়া। কাছাকাছি অর্থের যেকোনো শুদ্ধ উত্তর গ্রহণযোগ্য।")

OWN = "শিক্ষার্থীর নিজের যেকোনো শুদ্ধ ও প্রাসঙ্গিক উত্তর গ্রহণযোগ্য। নমুনা উত্তর দেওয়া হলো।"

# CD-138(b) — the task each slot's items DECLARE. Read off canon/marklogic/SLOT_REGISTER.json's
# BAN C5 rows: `selected` on an alternative row, every `parts[].part` on a composite row, and
# `admitted_task` verbatim on a simple one. Never inferred from a header marker string.
TASK_BY_SLOT = {
    "S01": ["কবির নাম", "কবিতার নাম", "প্রথম ৮ লাইন"],
    "S02": "মূল কাঠামো",
    "S03": "মূল কাঠামো",
    "S04": "মূল কাঠামো",
    "S05": "মূল কাঠামো",
    "S06": "বিপরীত শব্দ",
    "S07": "মূল কাঠামো",
    "S08": "মূল কাঠামো",
    "S09": "মূল কাঠামো",
    "S10": "পদ নির্ণয়",
    "S11": "বিরামচিহ্ন বসানো",
    "S12": ["যুক্তবর্ণ ভাঙা", "শব্দ গঠন"],
    "S13": "মূল কাঠামো",
}

RETAG = ["QP-BAN-C5-U13-Q11", "QP-BAN-C5-U13-Q13",
         "QP-BAN-C5-U13-Q14", "QP-BAN-C5-U13-Q72"]

RETIRE = ["QP-BAN-C5-U13-Q20", "QP-BAN-C5-U13-Q21", "QP-BAN-C5-U13-Q22",
          "QP-BAN-C5-U13-Q23", "QP-BAN-C5-U13-Q24", "QP-BAN-C5-U13-Q35",
          "QP-BAN-C5-U13-Q67", "QP-BAN-C5-U13-Q68", "QP-BAN-C5-U13-Q69",
          "QP-BAN-C5-U13-Q70", "QP-BAN-C5-U13-Q34"]


def qid(n):
    return f"QP-BAN-C5-U13-Q{n:02d}"


def sa(n, text, accepted, anchor, bloom, diff, slug, topic, note=None, role="short", marks=1):
    """A short_answer item. The only type P-037 admits for a teacher-keyed slot.

    `marks` is NOT a default that can be left alone: MARK-VALUE reads
    `MarkLogic_BAN_Spine.md`'s per-ITEM value for the slot, and S07 carries 2 where every other
    short_answer slot here carries 1. The first run of this script authored the two S07 items at
    1 and the gate caught both. Kept as a named argument rather than derived from the slot,
    because deriving it here would put a second copy of the spine's mark table in the authoring
    layer — and the gate's copy is the one that must be authoritative.
    """
    key = {"accepted": accepted}
    if note:
        key["model_note"] = note
    return {"qid": qid(n), "topic_tag": topic, "ref19_topic_id": slug,
            "question_text": text, "question_type": "short_answer", "paper_role": role,
            "bloom_level": bloom, "difficulty": diff, "tier": "tier1", "marks": marks,
            "chapter_ref": CH, "answer_key": key}, anchor


def rubric(criterion, full, part):
    return {"bands": ["সম্পূর্ণ", "আংশিক"],
            "criteria": [{"role": "islamic_alignment", "criterion": criterion,
                          "band_descriptors": {"সম্পূর্ণ": full, "আংশিক": part}}]}


def desc(n, text, rub, anchor, bloom, diff):
    return {"qid": qid(n), "topic_tag": POEM, "ref19_topic_id": "BAN-POEM",
            "question_text": text, "question_type": "descriptive", "paper_role": "structured",
            "bloom_level": bloom, "difficulty": diff, "tier": "tier1", "marks": 5,
            "chapter_ref": CH, "rubric": rub}, anchor


def mcq(n, text, opts, anchor, bloom, diff):
    return {"qid": qid(n), "topic_tag": POEM, "ref19_topic_id": "BAN-POEM",
            "question_text": text, "question_type": "mcq", "paper_role": "mcq",
            "bloom_level": bloom, "difficulty": diff, "tier": "tier1", "marks": 1,
            "chapter_ref": CH, "options": opts}, anchor


# ═════════════════════════════════════════════════════════════════════════════════════════
# S11 · বিরামচিহ্ন বসানো · Apply · 1 mark — three REWRITES + three new.
# C5 `selected` বিরামচিহ্ন বসানো out of S11's two-member admitted_set. প্রশ্ন তৈরি is admitted
# at this slot and NOT at this class, which is why the three below are rewrites and not errors
# of judgement — the item was authored against the slot instead of against the class row.
# Six distinct punctuation situations: কমা · কমা+দাঁড়ি · দাঁড়ি · বিস্ময় · প্রশ্নবোধক.
# ═════════════════════════════════════════════════════════════════════════════════════════
S11_REWRITE = {
    "QP-BAN-C5-U13-Q57": (
        "'আব্বা বলেন মন দে' — বাক্যটিতে প্রয়োজনীয় বিরামচিহ্ন বসিয়ে লেখো।",
        ["আব্বা বলেন, মন দে।"],
        "আব্বা বলেন মন দে", "medium",
        "'বলেন'-এর পরে কমা আর বাক্যের শেষে দাঁড়ি — দুটোই লাগবে। একটি ঠিক হলে অর্ধেক।"),
    "QP-BAN-C5-U13-Q58": (
        "'সবাই যখন ঘুমিয়ে পড়ে কর্ণফুলীর কূলটায়' — বাক্যটিতে প্রয়োজনীয় বিরামচিহ্ন বসিয়ে লেখো।",
        ["সবাই যখন ঘুমিয়ে পড়ে কর্ণফুলীর কূলটায়,"],
        "সবাই যখন ঘুমিয়ে পড়ে", "medium",
        "কথাটি এখানে শেষ হয়নি, পরের চরণে গড়িয়েছে — তাই দাঁড়ি নয়, কমা।"),
    "QP-BAN-C5-U13-Q59": (
        "'আমি না হয় পাখিই হব পাখির মতো বন্য' — বাক্যটিতে প্রয়োজনীয় বিরামচিহ্ন বসিয়ে লেখো।",
        ["আমি না হয় পাখিই হব, পাখির মতো বন্য।"],
        "আমি না হয় পাখিই হব", "medium",
        "দুটি অংশের মাঝে কমা আর কবিতার শেষ বলে দাঁড়ি।"),
}

S11_NEW = [
    (89, "'তোমরা যখন শিখছ পড়া মানুষ হওয়ার জন্য' — বাক্যটিতে প্রয়োজনীয় বিরামচিহ্ন বসিয়ে লেখো।",
     ["তোমরা যখন শিখছ পড়া, মানুষ হওয়ার জন্য,"], "তোমরা যখন শিখছ পড়া", "medium",
     "দুই জায়গাতেই কমা — কথাটি পরের চরণে গিয়ে শেষ হয়েছে।"),
    (90, "'পাঠে আমার মন বসে না কাঁঠালচাঁপার গন্ধে' — বাক্যটিতে প্রয়োজনীয় বিরামচিহ্ন বসিয়ে লেখো।",
     ["পাঠে আমার মন বসে না কাঁঠালচাঁপার গন্ধে।"], "পাঠে আমার মন বসে না", "easy",
     "এখানে ভেতরে কোনো বিরতি নেই; শুধু শেষে দাঁড়ি।"),
    (91, "'কবি কোথায় লুকিয়ে থাকতে চান' — বাক্যটিতে প্রয়োজনীয় বিরামচিহ্ন বসিয়ে লেখো।",
     ["কবি কোথায় লুকিয়ে থাকতে চান?"], "বকুল ডালে লুকিয়ে থেকে", "easy",
     "প্রশ্ন করা হয়েছে, তাই দাঁড়ি নয় — প্রশ্নবোধক চিহ্ন।"),
]

# ═════════════════════════════════════════════════════════════════════════════════════════
# S12 · যুক্তবর্ণ ভাঙা + শব্দ গঠন · COMPOSITE · Apply · 1 mark — three REWRITES + two new.
# Every item does BOTH parts. The poem carries exactly five distinct conjuncts and the fifth
# is the limit, not a choice: র্ণ · ন্য · চ্ছ · ন্ধ · ল্ট. ন্য appears twice (বন্য · জন্য) and
# is authored ONCE — the same conjunct twice is the near-duplicate §4 bars.
# The formed word is deliberately NOT a poem word: forming from the poem's own stock would let
# recall answer the second half, which is the thing the composite part exists to test.
# ═════════════════════════════════════════════════════════════════════════════════════════
S12_ITEMS = [
    ("QP-BAN-C5-U13-Q51", "কর্ণফুলী", "র্ণ", ["র্ণ = র + ণ; নতুন শব্দ — বর্ণ", "র্ণ = রেফ + ণ; স্বর্ণ", "র্ণ — র ও ণ; পূর্ণ"],
     "সবাই যখন ঘুমিয়ে পড়ে কর্ণফুলীর কূলটায়"),
    ("QP-BAN-C5-U13-Q52", "বন্য", "ন্য", ["ন্য = ন + য; নতুন শব্দ — অন্য", "ন্য = ন + য; ধন্য", "ন্য — ন ও য; জন্য"],
     "আমি না হয় পাখিই হব পাখির মতো বন্য"),
    ("QP-BAN-C5-U13-Q53", "ইচ্ছে", "চ্ছ", ["চ্ছ = চ + ছ; নতুন শব্দ — স্বচ্ছ", "চ্ছ = চ + ছ; ইচ্ছুক", "চ্ছ — চ ও ছ; উচ্ছ্বাস"],
     "আমার কেবল ইচ্ছে জাগে"),
    (92, "গন্ধ", "ন্ধ", ["ন্ধ = ন + ধ; নতুন শব্দ — বন্ধু", "ন্ধ = ন + ধ; অন্ধ", "ন্ধ — ন ও ধ; সন্ধি"],
     "পাঠে আমার মন বসে না কাঁঠালচাঁপার গন্ধে"),
    (93, "উল্টায়", "ল্ট", ["ল্ট = ল + ট; নতুন শব্দ — পাল্টা", "ল্ট = ল + ট; উল্টো", "ল্ট — ল ও ট; ফল্টু"],
     "দুধভরা ওই চাঁদের বাটি ফেরেস্তারা উল্টায়"),
]

S12_STEM = ("'পাখির মতো' কবিতার '{}' শব্দের যুক্তবর্ণটি ভেঙে লেখো, "
            "আর সেই যুক্তবর্ণ দিয়ে কবিতায় নেই এমন নতুন একটি শব্দ গঠন করো।")
S12_NOTE = (TS + " দুটি কাজই করতে হবে — শুধু ভাঙলে বা শুধু শব্দ গঠন করলে অর্ধেক কাজ "
                 "(SLOT_REGISTER BAN-S12 composite)।")

# ═════════════════════════════════════════════════════════════════════════════════════════
# S10 · পদ নির্ণয় · 1 mark — TEN NEW, replacing the ten retired ভাব নির্ণয় items.
# Nine identify the পদ of a marked word (Understand: classify against a taught category — the
# answer is nowhere in the poem, so it is not recall). ONE is Apply and it is authored as Apply
# on its own merit, not to fill a floor: 'পড়' appears as a ক্রিয়া in one line and a বিশেষ্য in
# another, and deciding which is which by CONTEXT is a rule applied in a new situation.
# Five পদ-শ্রেণি are covered — বিশেষ্য · বিশেষণ · সর্বনাম · ক্রিয়া · অব্যয়.
# ═════════════════════════════════════════════════════════════════════════════════════════
S10_NEW = [
    (109, "'আম্মা বলেন, পড়রে সোনা' — এখানে 'আম্মা' শব্দটি কোন পদ? নির্ণয় করো।",
     ["বিশেষ্য", "বিশেষ্য পদ", "নামপদ"], "আম্মা বলেন পড়রে সোনা", "Understand", "easy"),
    (110, "'কেমন করে শহর ছেড়ে / সবুজ গাঁয়ে ঘুরব' — এখানে 'সবুজ' শব্দটি কোন পদ? নির্ণয় করো।",
     ["বিশেষণ", "বিশেষণ পদ"], "সবুজ গাঁয়ে ঘুরব", "Understand", "easy"),
    (111, "'পাঠে আমার মন বসে না' — এখানে 'আমার' শব্দটি কোন পদ? নির্ণয় করো।",
     ["সর্বনাম", "সর্বনাম পদ"], "পাঠে আমার মন বসে না", "Understand", "easy"),
    (112, "'আব্বা বলেন, মন দে' — এখানে 'বলেন' শব্দটি কোন পদ? নির্ণয় করো।",
     ["ক্রিয়া", "ক্রিয়া পদ"], "আব্বা বলেন মন দে", "Understand", "easy"),
    (113, "'আমার কেবল ইচ্ছে জাগে' — এখানে 'কেবল' শব্দটি কোন পদ? নির্ণয় করো।",
     ["অব্যয়", "অব্যয় পদ"], "আমার কেবল ইচ্ছে জাগে", "Understand", "medium"),
    (114, "'আমি না হয় পাখিই হব, / পাখির মতো বন্য' — এখানে 'বন্য' শব্দটি কোন পদ? নির্ণয় করো।",
     ["বিশেষণ", "বিশেষণ পদ"], "পাখির মতো বন্য", "Understand", "medium"),
    (115, "'তোমরা যখন শিখছ পড়া' — এখানে 'তোমরা' শব্দটি কোন পদ? নির্ণয় করো।",
     ["সর্বনাম", "সর্বনাম পদ"], "তোমরা যখন শিখছ পড়া", "Understand", "easy"),
    (116, "'দুধভরা ওই চাঁদের বাটি / ফেরেস্তারা উল্টায়' — এখানে 'উল্টায়' শব্দটি কোন পদ? নির্ণয় করো।",
     ["ক্রিয়া", "ক্রিয়া পদ"], "দুধভরা ওই চাঁদের বাটি ফেরেস্তারা উল্টায়", "Understand", "easy"),
    (117, "'সবাই যখন ঘুমিয়ে পড়ে / কর্ণফুলীর কূলটায়' — এখানে 'কর্ণফুলী' শব্দটি কোন পদ? নির্ণয় করো।",
     ["বিশেষ্য", "বিশেষ্য পদ", "নামবাচক বিশেষ্য", "সংজ্ঞাবাচক বিশেষ্য"],
     "সবাই যখন ঘুমিয়ে পড়ে কর্ণফুলীর কূলটায়", "Understand", "medium"),
    (118, "'আম্মা বলেন, পড়রে সোনা' আর 'তোমরা যখন শিখছ পড়া' — দুই চরণে 'পড়' একই পদ হয়নি। "
          "কোন চরণে কোন পদ হয়েছে, নির্ণয় করো।",
     ["প্রথম চরণে ক্রিয়া ('পড়রে'), দ্বিতীয় চরণে বিশেষ্য ('পড়া')",
      "'পড়রে' — ক্রিয়া; 'পড়া' — বিশেষ্য"],
     "আম্মা বলেন পড়রে সোনা", "Apply", "hard"),
]

S10_NOTE = (TS + " পদ নির্ণয় C5-এর BAN-S10 স্লটে নির্বাচিত কাজ — ভাষারীতি পরিবর্তন ও "
                 "ক্রিয়ার কাল এই স্লটে স্বীকৃত হলেও পঞ্চম শ্রেণিতে নির্বাচিত নয়।")

# ═════════════════════════════════════════════════════════════════════════════════════════
# S06 · বিপরীত শব্দ · Remember · 1 mark — FOUR NEW, to the content limit of seven.
# Wave 3's header called this slot content-limited at three. Read again at source that is too
# pessimistic: the poem carries seven words with a clean, single, age-appropriate opposite.
# ═════════════════════════════════════════════════════════════════════════════════════════
S06_NEW = [
    (101, "ইচ্ছা", ["অনিচ্ছা"], "আমার কেবল ইচ্ছে জাগে", "easy"),
    (102, "মানুষ", ["অমানুষ"], "মানুষ হওয়ার জন্য", "easy"),
    (103, "ভরা", ["খালি", "শূন্য"], "দুধভরা ওই চাঁদের বাটি", "medium"),
    (104, "লুকানো", ["প্রকাশ করা", "প্রকাশ", "বেরিয়ে আসা"], "বকুল ডালে লুকিয়ে থেকে", "medium"),
]

# ═════════════════════════════════════════════════════════════════════════════════════════
# S13 · এক কথায় প্রকাশ · Remember · 1 mark — THREE NEW, to the content limit of six.
# ═════════════════════════════════════════════════════════════════════════════════════════
S13_NEW = [
    (119, "'যে রাতে পূর্ণ চাঁদ ওঠে' — 'পাখির মতো' কবিতার ছবিটির সঙ্গে মিলিয়ে এক কথায় প্রকাশ করো।",
     ["পূর্ণিমা"], "দুধভরা ওই চাঁদের বাটি", "medium"),
    (120, "'হলুদ রঙের একধরনের ফুল' — 'পাখির মতো' কবিতার শব্দ দিয়ে এক কথায় প্রকাশ করো।",
     ["কাঁঠালচাঁপা"], "হলুদ রঙের একধরনের ফুল", "easy"),
    (121, "'আল্লাহর হুকুম পালন করেন যাঁরা, নূরের সৃষ্টি' — 'পাখির মতো' কবিতার শব্দ দিয়ে "
          "এক কথায় প্রকাশ করো।",
     ["ফেরেস্তা", "ফেরেশতা"], "দুধভরা ওই চাঁদের বাটি ফেরেস্তারা উল্টায়", "easy"),
]

# ═════════════════════════════════════════════════════════════════════════════════════════
# S03 · বাক্য গঠন · Apply · 1 mark — FIVE NEW, to the content limit of sixteen.
# Eleven poem words were already used; these are the five that remain and carry enough meaning
# for a C5 sentence. BAN-S03-NOJOIN is respected: each is its own item, never joined to a
# যুক্তবর্ণ or কারচিহ্ন question (SLOT_REGISTER BAN-S03 row_constraints).
# ═════════════════════════════════════════════════════════════════════════════════════════
S03_NEW = [
    (94, "মানুষ", "মানুষ হওয়ার জন্য", "easy"),
    (95, "ঘুম", "সবাই যখন ঘুমিয়ে পড়ে", "easy"),
    (96, "ডাল", "বকুল ডালে লুকিয়ে থেকে", "easy"),
    (97, "মন", "আব্বা বলেন মন দে", "easy"),
    (98, "ফেরেস্তা", "দুধভরা ওই চাঁদের বাটি ফেরেস্তারা উল্টায়", "medium"),
]


def build():
    bank = json.loads(BANK.read_text(encoding="utf-8"))
    src = bank["source_index"]
    slot = bank["slot_index"]
    byqid = {q["qid"]: q for q in bank["questions"]}
    added, anchors = [], {}

    # ── 1. RE-TAG, FIRST ────────────────────────────────────────────────────────────────
    for q in RETAG:
        assert byqid[q]["bloom_level"] == "Understand", f"{q} is not Understand — order broken"
        byqid[q]["bloom_level"] = "Remember"

    # ── 2. RETIRE ───────────────────────────────────────────────────────────────────────
    for q in RETIRE:
        assert q in byqid, f"{q} is not in the bank"
    bank["questions"] = [q for q in bank["questions"] if q["qid"] not in RETIRE]
    for q in RETIRE:
        src.pop(q, None)
        slot.pop(q, None)
    for name, ids in bank["pool_index"].items():
        bank["pool_index"][name] = [i for i in ids if i not in RETIRE]
    byqid = {q["qid"]: q for q in bank["questions"]}

    # ── 3a. REWRITE — S11 off-choice ────────────────────────────────────────────────────
    for q, (text, acc, anchor, diff, note) in S11_REWRITE.items():
        it = byqid[q]
        it["question_text"] = text
        it["ref19_topic_id"] = "BAN-SENTENCE"
        it["topic_tag"] = SENT
        it["difficulty"] = diff
        it["bloom_level"] = "Apply"
        it["answer_key"] = {"accepted": acc, "model_note": note}
        anchors[q] = anchor

    # ── 3b. REWRITE + AUTHOR — S12 composite ────────────────────────────────────────────
    for ref, word, conj, acc, anchor in S12_ITEMS:
        text = S12_STEM.format(word)
        if isinstance(ref, str):
            it = byqid[ref]
            it["question_text"] = text
            it["bloom_level"] = "Apply"
            it["difficulty"] = "medium"
            it["answer_key"] = {"accepted": acc, "model_note": S12_NOTE}
            anchors[ref] = anchor
        else:
            it, a = sa(ref, text, acc, anchor, "Apply", "medium",
                       "BAN-JUKTOBARNA", VOCAB, S12_NOTE)
            added.append((it, a, "S12"))

    # ── 4. AUTHOR ───────────────────────────────────────────────────────────────────────
    for n, text, acc, anchor, diff, note in S11_NEW:
        added.append(sa(n, text, acc, anchor, "Apply", diff, "BAN-SENTENCE", SENT, note)
                     + ("S11",))
    for n, text, acc, anchor, bloom, diff in S10_NEW:
        added.append(sa(n, text, acc, anchor, bloom, diff, "BAN-PARTSPEECH", VOCAB, S10_NOTE)
                     + ("S10",))
    for n, word, acc, anchor, diff in S06_NEW:
        added.append(sa(n, f"'পাখির মতো' কবিতায় ব্যবহৃত '{word}' শব্দের বিপরীত শব্দ লেখো।",
                        acc, anchor, "Remember", diff, "BAN-WORDREL", VOCAB, TS) + ("S06",))
    for n, text, acc, anchor, diff in S13_NEW:
        added.append(sa(n, text, acc, anchor, "Remember", diff, "BAN-WORDREL", VOCAB, TS)
                     + ("S13",))
    for n, word, anchor, diff in S03_NEW:
        added.append(sa(n, f"'{word}' শব্দটি দিয়ে একটি অর্থপূর্ণ বাক্য লেখো।",
                        [f"{word} শব্দটি ঠিকভাবে বসিয়ে লেখা যেকোনো অর্থপূর্ণ বাক্য।"],
                        anchor, "Apply", diff, "BAN-SENTENCE", SENT, OWN) + ("S03",))

    # S05 · বহুনির্বাচনি +2 · Understand — the slot is a METHOD, not a skill
    # (`MarkLogic_BAN_Spine.md` BAN-S05: "বহুনির্বাচনি হলো উত্তর দেওয়ার একটা পদ্ধতি, কোনো দক্ষতা নয়"),
    # so the level is read off the cognitive demand of the stem, never off the slot.
    added.append(mcq(99, "'তখন কেবল ভাবতে থাকি / কেমন করে উড়ব' — কবি কখন এ কথা ভাবেন?",
                     [{"option_id": "ক", "text": "সবাই ঘুমিয়ে পড়ার পর রাতে", "is_correct": True},
                      {"option_id": "খ", "text": "স্কুলে যাওয়ার পথে", "is_correct": False,
                       "why_wrong": "কবিতায় স্কুলে যাওয়ার কোনো কথা নেই।"},
                      {"option_id": "গ", "text": "আম্মা পড়তে বলার সঙ্গে সঙ্গে", "is_correct": False,
                       "why_wrong": "আম্মার কথা প্রথম স্তবকে, আর 'তখন' তৃতীয় স্তবকের রাতকে বোঝায়।"},
                      {"option_id": "ঘ", "text": "নদীতে গোসল করার সময়", "is_correct": False,
                       "why_wrong": "কবিতায় গোসলের কোনো কথা নেই।"}],
                     "তখন কেবল ভাবতে থাকি", "Understand", "medium") + ("S05",))
    added.append(mcq(100, "'দুধভরা ওই চাঁদের বাটি / ফেরেস্তারা উল্টায়' — এখানে কবি কী বোঝাতে চেয়েছেন?",
                     [{"option_id": "ক", "text": "রাত গড়িয়ে যাওয়ার সঙ্গে চাঁদের আলো সরে যাচ্ছে",
                       "is_correct": True},
                      {"option_id": "খ", "text": "আকাশে সত্যিই একটি বাটি ভাসছে", "is_correct": False,
                       "why_wrong": "এটি একটি চিত্রকল্প; বাটি বলতে পূর্ণিমার চাঁদকে বোঝানো হয়েছে।"},
                      {"option_id": "গ", "text": "কেউ দুধ ঢেলে ফেলেছে", "is_correct": False,
                       "why_wrong": "'দুধভরা' চাঁদের রং ও উজ্জ্বলতার তুলনা, সত্যিকারের দুধ নয়।"},
                      {"option_id": "ঘ", "text": "কবি দুধ খেতে চান", "is_correct": False,
                       "why_wrong": "কবিতায় কবির খাওয়ার কোনো ইচ্ছার কথা নেই।"}],
                     "দুধভরা ওই চাঁদের বাটি ফেরেস্তারা উল্টায়", "Understand", "medium") + ("S05",))

    # S07 · সংক্ষিপ্ত উত্তর +2 · Understand
    added.append(sa(105, "'আমার কেবল ইচ্ছে জাগে' আর 'তখন কেবল ভাবতে থাকি' — দুই জায়গায় "
                         "'কেবল' শব্দটি কবির মনের কোন দিক আমাদের দেখায়?",
                    ["কবির মন একটি জিনিসেই আটকে আছে — পড়ার বদলে বাইরের জগতেই তাঁর সব ভাবনা, "
                     "এটাই 'কেবল' শব্দটি বারবার বুঝিয়ে দেয়।"],
                    "তখন কেবল ভাবতে থাকি", "Understand", "hard",
                    "BAN-POEM", POEM, "মূল ভাবটি ধরা পড়লেই পূর্ণ নম্বর।", role="short", marks=2)
                 + ("S07",))
    added.append(sa(106, "'তোমরা যখন শিখছ পড়া' — কবি নিজেকে 'তোমরা'-র থেকে আলাদা করে "
                         "দেখাচ্ছেন কেন? নিজের ভাষায় লেখো।",
                    ["কবি বলতে চাইছেন সবাই যে পথে যাচ্ছে তিনি সে পথে যেতে পারছেন না; তাঁর মন "
                     "পড়ার বদলে প্রকৃতির দিকে টানছে, তাই নিজেকে আলাদা করে দেখাচ্ছেন।"],
                    "তোমরা যখন শিখছ পড়া", "Understand", "hard",
                    "BAN-POEM", POEM, "মূল ভাবটি ধরা পড়লেই পূর্ণ নম্বর।", role="short", marks=2)
                 + ("S07",))

    # S08 · বিস্তৃত উত্তর +2 · Analyze · 5 marks
    added.append(desc(107, "'পাখির মতো' কবিতায় আম্মা-আব্বার কথা আর কবির নিজের ইচ্ছা — এই "
                           "দুইয়ের টানাপোড়েন কোন কোন চরণে ফুটে উঠেছে, বিশ্লেষণ করে লেখো।",
                      rubric("দুই পক্ষের কথা পাঠ থেকে আলাদা করে চেনা ও পাশাপাশি রেখে বিশ্লেষণ "
                             "করা — এবং পিতামাতার নির্দেশকে ছোট না করে, পড়াশোনাকে হেয় না করে "
                             "কবির মনের অবস্থাটি বোঝানো",
                             "আম্মা-আব্বার চরণ ও কবির ইচ্ছার চরণ দুই-ই পাঠ থেকে তুলে এনে "
                             "পাশাপাশি বিশ্লেষণ করা হয়েছে; ভাষা শালীন, পিতামাতার প্রতি সম্মান "
                             "অটুট, আর পড়াশোনার গুরুত্ব কোথাও খাটো করা হয়নি।",
                             "কেবল এক পক্ষের কথা লেখা হয়েছে, বা পাঠে নেই এমন কথা ঢুকেছে; "
                             "অথবা পিতামাতাকে বা পড়াশোনাকে হেয় করে এমন কথা এসেছে।"),
                      "আম্মা বলেন পড়রে সোনা", "Analyze", "hard") + ("S08",))
    added.append(desc(108, "'পাখির মতো' কবিতার প্রতিটি স্তবকের শেষ শব্দে যে মিল আছে, তা "
                           "কবিতার ভাব ফোটাতে কীভাবে সাহায্য করেছে — বিশ্লেষণ করে লেখো।",
                      rubric("অন্ত্যমিলের জোড়াগুলো পাঠ থেকে খুঁজে বের করা এবং সেগুলো কীভাবে "
                             "ওড়া ও মুক্তির ভাব তৈরি করে তা দেখানো — কল্পনার কথা বলতে গিয়ে "
                             "পড়াশোনা বা পিতামাতার নির্দেশকে খাটো না করা",
                             "অন্তত তিনটি মিল-জোড়া পাঠ থেকে তুলে এনে ভাবের সঙ্গে মিলিয়ে "
                             "বিশ্লেষণ করা হয়েছে; ভাষা শালীন ও পাঠের বাইরের কিছু বানানো হয়নি।",
                             "দু-একটি জোড়া লেখা হয়েছে কিন্তু ভাবের সঙ্গে মেলানো হয়নি, "
                             "বা পাঠে নেই এমন উদাহরণ ঢুকেছে।"),
                      "মিল-শব্দ খুঁজে বের করা", "Analyze", "hard") + ("S08",))

    # ── assemble ────────────────────────────────────────────────────────────────────────
    for item, anchor, s in added:
        bank["questions"].append(item)
        slot[item["qid"]] = s
        anchors[item["qid"]] = anchor
    for q, a in anchors.items():
        src[q] = a

    bank["questions"].sort(key=lambda q: int(q["qid"].rsplit("Q", 1)[1]))

    # CD-138(b) — task_index, every item, from the register's own vocabulary.
    bank["task_index"] = {q["qid"]: TASK_BY_SLOT[slot[q["qid"]]] for q in bank["questions"]}

    # pool_index: the new items join HW and AS in the wave's own order; CT is left as authored.
    new_ids = [i["qid"] for i, _, _ in added]
    bank["pool_index"]["HW"] += new_ids[0::2]
    bank["pool_index"]["AS"] += new_ids[1::2]

    return bank, added


def main():
    hay = qp_norm(EXTRACTION.read_text(encoding="utf-8"))
    bank, added = build()

    # REFUSE rather than emit a bank the gate would reject.
    bad = [f"{q}: {a!r}" for q, a in bank["source_index"].items()
           if len(qp_norm(a).split()) < 3 or qp_norm(a) not in hay]
    if bad:
        print("ANCHORS DO NOT RESOLVE — nothing written:", *bad, sep="\n  ")
        return 1
    missing = [q["qid"] for q in bank["questions"] if q["qid"] not in bank["task_index"]]
    if missing:
        print("task_index incomplete — nothing written:", missing)
        return 1

    total = len(bank["questions"])
    blooms, slots, diffs = {}, {}, {}
    for q in bank["questions"]:
        blooms[q["bloom_level"]] = blooms.get(q["bloom_level"], 0) + 1
        slots[bank["slot_index"][q["qid"]]] = slots.get(bank["slot_index"][q["qid"]], 0) + 1
        diffs[q["difficulty"]] = diffs.get(q["difficulty"], 0) + 1
    for lvl in ("Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"):
        blooms.setdefault(lvl, 0)

    h = bank["header"]
    h["target"] = total
    h["reason"] = (
        f"{total} is the RE-AUTHORED pool, recomputed in session and carrying no number from "
        f"wave 3 — the Principal ruled 'extract to content limit, balanced' and required every "
        f"REF-06 §3.6 floor to clear WITH MARGIN, a plan landing exactly on a floor being a "
        f"defect rather than a pass. The binding constraint is not the pool's size but its "
        f"Apply base: retiring the ten S10 ভাব নির্ণয় items cost 7 `Apply`, and retiring Q34 "
        f"cost the eighth, so S03 · S11 · S12 are all authored to their content limits and one "
        f"S10 item is `Apply` on its own merit. Under CD-135 a pool has no ceiling, so the only "
        f"thing this size costs is authoring."
    )
    h["slot_counts"] = dict(sorted(slots.items()))
    h["remember_cap"] = (
        f"THE CAP IS RECOMPUTED FROM THIS POOL, not carried. Under CD-135 a pool has no upper "
        f"bound, so the ceiling wave 3 computed from REF-06's 20–30% band no longer binds — what "
        f"binds is the FLOORS, and each one caps the pool from below: max pool = level ÷ floor. "
        f"At Remember {blooms['Remember']} the cap is {blooms['Remember'] // 20 * 100}, at "
        f"Understand {blooms['Understand']} it is {int(blooms['Understand'] / 0.25)}, at Apply "
        f"{blooms['Apply']} it is {int(blooms['Apply'] / 0.25)} and at Analyze "
        f"{blooms['Analyze']} it is {int(blooms['Analyze'] / 0.10)}. The smallest is the real "
        f"cap and it is Apply's — which is why the five held-back Remember items below are held "
        f"rather than taken: they raise the pool without raising Apply."
    )
    h["gaps"] = [
        "S14 আবেদনপত্র · S15 রচনা — declared INADMISSIBLE for this chapter in `slot_exclusions`, "
        "each with a one-line content reason (CD-138(e), CD-134(c)). Per CD-139(c) that is a "
        "per-chapter declaration and not a slot-level rule; CD-139(d) records পাঠ ৪ admitting "
        "S14 on its own content.",
        "FIVE REMEMBER ITEMS ARE LEFT UNEXTRACTED, ON THE PRINCIPAL'S RULING, AND ARE NAMED HERE "
        "SO A LATER WAVE CAN TAKE THEM. S02 supports two more শব্দার্থ items (ফেরেস্তা · বকুল, "
        "teacher-keyed under CD-136(b)) and S04 three more শূন্যস্থান items. All five are "
        "`Remember`. They were HELD because taking them raises the pool without raising `Apply`, "
        "and every Apply-bearing slot (S03 · S11 · S12) is already at its content limit — so the "
        "five would narrow the Apply margin the re-author exists to create. Take them only "
        "together with enough new Apply items to hold the margin.",
        "wave 3's claim that S06 · S12 · S13 are CONTENT-LIMITED AT THREE is WITHDRAWN, and the "
        "withdrawal is recorded rather than silently fixed. Read again at source, পাঠ ১৩ carries "
        "five distinct যুক্তবর্ণ (র্ণ · ন্য · চ্ছ · ন্ধ · ল্ট), seven words with a clean single "
        "opposite, and six এক কথায় প্রকাশ mappings. The three-item reading was not a fact about "
        "the book; it was a fact about how far the poem had been read.",
        "অনুশীলনী ৮ (ছকের ভিতর শব্দ খোঁজা) remains UNAUTHORABLE: the grid is not reproduced in "
        "canon/marklogic/C5_Bangla_Source_13-23.md. An EXTRACTION gap, not a wave gap — no "
        "future wave closes it without re-extraction. Unchanged from waves 2 and 3, still raised.",
        "মিল-শব্দ (অনুশীলনী ৩) HAS NO C5 SPINE SLOT AND NO LONGER RIDES ONE. Q34 carried it at "
        "S07 as an acknowledged workaround through waves 2 and 3. CD-138(b) makes the task a "
        "DECLARED field, and Q34 would have had to declare S07's `মূল কাঠামো` — a declaration "
        "that is convenient and false. The Principal rejected it and Q34 is RETIRED. The "
        "chapter's মিল-শব্দ content is now unserved, and that is the honest state: the gap is in "
        "the spine, not in the bank, and it is raised here rather than papered over. Q108 uses "
        "the same অন্ত্যমিল material legitimately, as S08 analysis rather than as a slot claim.",
        "TEN S10 ITEMS RETIRED — Q20 · Q21 · Q22 · Q23 · Q24 · Q35 · Q67 · Q68 · Q69 · Q70, all "
        "ভাব নির্ণয়. Not re-slotted, because ভাব নির্ণয় is admitted at NO class in "
        "MarkLogic_BAN_Spine.md: C3's S10 is বাক্যের প্রকার, C2's is ক্রিয়ার পুরুষ-সংগতি. "
        "Wave 3 authored them on this chapter's own use-line, which CD-134 rules ADVISORY and "
        "which cannot admit a task the spine admits nowhere. S10 is re-authored as পদ নির্ণয় — "
        "the task C5 SELECTED from the slot's three.",
        "Not authored, judged too weak rather than overlooked: অনুশীলনী ৭'s গাছের তালিকা (the "
        "answer is wholly the student's own and traces to nothing) and অনুশীলনী ২'s line-ordering "
        "task (re-uses Q01's eight lines).",
        "HELD FOR THE SUBJECT LEAD PASS (Principal, REF-09 §9) — nothing in this bank is "
        "promoted. CD-136(g) puts the teacher-key rule's enforcement at the §6 human review "
        "gate, and 24 items across S02 · S06 · S10 · S12 · S13 carry teacher-supplied keys "
        "declaring themselves in their own model_note.",
    ]
    h["bloom_floors"] = {
        "rule": "CD-135 — POOL level is REF-06 §3.6's LOWER BOUNDS ONLY. No upper bound binds a "
                "pool. The band, both bounds, applies at PAPER level.",
        "observed": {k: f"{blooms[k]}/{total} = {100*blooms[k]/total:.1f}%"
                     for k in ("Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create")},
        "margin_over_floor": {k: blooms[k] - -(-p * total // 100) for k, p in
                              (("Remember", 20), ("Understand", 25), ("Apply", 25),
                               ("Analyze", 10))},
        "Create": "0 items. CONTENT FACT, stated per CD-135(d) rather than left silent: পাঠ ১৩ "
                  "is a twenty-line lyric poem. A `Create` item would require the student to "
                  "produce new work of their own, which S15 রচনা is for — and S15 is declared "
                  "INADMISSIBLE for this chapter, on content, in slot_exclusions. The floor is "
                  "0%, so nothing is owed; this row exists so the absence is a recorded decision "
                  "and not an oversight.",
        "Evaluate": f"{blooms['Evaluate']} items, floor 0%. Not grown in wave 4 — the poem's "
                    f"interpretable images were spent on Analyze, where the binding floor sits.",
    }
    h["teacher_supplied_keys"] = (
        "CD-136 — S02 (4 of 7) · S06 বিপরীত শব্দ (7) · S10 পদ নির্ণয় (10) · S12 যুক্তবর্ণ ও শব্দ "
        "গঠন (5) · S13 এক কথায় প্রকাশ (6) carry TEACHER-SUPPLIED KEYS. Every one is "
        "`short_answer`, which is what P-037's interim rule admits; no teacher-keyed item in this "
        "bank carries any other type, so the stop-and-ask never fires. Each declares itself in "
        "its own model_note so the provenance travels with the item into any paper it is lifted "
        "into. Enforcement is the §6 human review gate — the Principal as Subject Lead "
        "(CD-136(g), REF-09 §9), not a gate that cannot see the thing it judges."
    )
    h["tagging"] = (
        "RE-TAGS APPLIED FIRST, before any retirement or authoring, because every count "
        "downstream depends on them. Q11 · Q13 · Q14 · Q72 move `Understand → Remember`: each is "
        "answered verbatim by the poem's own next line, so under the tag-down rule they read "
        "`Remember`. Q13 was RAISED as a Subject Lead review item in wave 3's own header and is "
        "now ruled. The Bloom level of every item is a claim about its COGNITIVE DEMAND and "
        "never about its slot — `MarkLogic_BAN_Spine.md` BAN-S05 in its own words: "
        "\"বহুনির্বাচনি হলো উত্তর দেওয়ার একটা পদ্ধতি, কোনো দক্ষতা নয়।\" The three S12 rewrites "
        "move `Remember → Apply` as NEW CONTENT ON REWRITE, not as a re-tag: wave 3's `Remember` "
        "was correct for the half-items they then were."
    )
    bank["wave"] = 4
    bank["waves"]["4"] = (
        f"Q89–Q121 · 2026-08-15 · author_U13_wave4.py · THE RE-AUTHOR against CD-138's slot "
        f"register — 4 re-tags, 11 retirements, 6 rewrites, 33 new items, `task_index` for all "
        f"{total}. Countersigned plan table; nothing promoted."
    )
    bank["curation"] = ("FLEXIBLE · C-03 respected — অনুশীলনী ৫-এর বারণ করা বাক্যটি ব্যবহার করা "
                        "হয়নি, আর তার বদলি বহনকারী Q23 এই ঢেউয়ে অবসরে গেছে")

    BANK.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"wave 4: -{len(RETIRE)} retired, {len(RETAG)} re-tagged, "
          f"6 rewritten, +{len(added)} authored → {total}")
    print("slots :", dict(sorted(slots.items())))
    print("diff  :", dict(sorted(diffs.items())),
          f" easy {100*diffs.get('easy',0)/total:.1f}% (floor 30%)")
    print("bloom :", {k: blooms[k] for k in
                      ("Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create")})
    for lvl, pc in (("Remember", 20), ("Understand", 25), ("Apply", 25), ("Analyze", 10)):
        need = -(-pc * total // 100)
        print(f"   {lvl:<11} {blooms[lvl]:>3}/{total} = {100*blooms[lvl]/total:5.1f}%  "
              f"floor {pc}% = {need:>3} items  margin +{blooms[lvl]-need}")
    return 0


def qp_norm(s):
    s = unicodedata.normalize("NFC", s or "")
    s = re.sub(r"[‘’“”'\"()\[\]।,;:?!—–\-….*_#>|/·]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


if __name__ == "__main__":
    sys.exit(main())
