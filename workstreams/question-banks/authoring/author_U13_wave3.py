#!/usr/bin/env python3
"""author_U13_wave3.py — C5 BAN পাঠ ১৩ পাখির মতো, WAVE 3.

Authored under CD-134 (the chapter's own *কোন প্রশ্নে কাজে লাগবে* line is advisory),
CD-136 (teacher-supplied language keys) and CD-135 (the pool Bloom check is a FLOOR).

TARGET 88, Principal ruling 2026-08-15. The ruled MINIMUM was 79; 88 is authored because
**three levels sit exactly on their floor at 79 and one Subject Lead re-tag would redden the
bank.** This is the bank's own wave-2 principle — *a target chosen so a later re-tag cannot
redden it* — and it survives the ceiling's removal, because under CD-135 the risk moved from
"too many of a level" to "not enough", and margin is the only defence against a re-tag.

TAGGING RULE (Principal, 2026-08-15, new this wave). Under floors, **over-tagging UPWARD is the
dangerous direction**: it inflates the level that must clear a floor and hides the breach.
**Where a level is genuinely uncertain, TAG DOWN.** Applied here to every S12 যুক্তবর্ণ item —
the probe read them as `Apply` (রেফ rule executed on a word not previously decomposed) and they
are authored `Remember`. **Any `Apply` reading is upside, confirmed in review, never assumed.**

The Bloom level of every item is a claim about its COGNITIVE DEMAND and never about its slot.
`MarkLogic_BAN_Spine.md` `BAN-S05` in its own words: *"বহুনির্বাচনি হলো উত্তর দেওয়ার একটা পদ্ধতি,
কোনো দক্ষতা নয়।"* A slot the spine calls *not a skill* cannot carry a level. Reading a slot as
carrying one is `CR-007`'s shape and is logged as a PATTERN candidate (second instance).

Every anchor is validated against the extraction before the bank is written — the script
refuses rather than emitting a bank the gate would then reject.
"""
import json
import re
import sys
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


def rubric(criterion, full, part):
    return {"bands": ["সম্পূর্ণ", "আংশিক"],
            "criteria": [{"role": "islamic_alignment", "criterion": criterion,
                          "band_descriptors": {"সম্পূর্ণ": full, "আংশিক": part}}]}


# ─────────────────────────────────────────────────────────────────────────────────────────
# S04 শূন্যস্থান পূরণ · fill_blank · Remember · 1 mark
# A blank on a memorised line is RECITATION. The probe confirmed the slot-derived guess here.
# ─────────────────────────────────────────────────────────────────────────────────────────
S04 = [
    ("'আম্মা বলেন, পড়রে ______।' — শূন্যস্থান পূরণ করো।", ["সোনা"], "আম্মা বলেন পড়রে সোনা"),
    ("'পাঠে আমার মন বসে না ______ গন্ধে।' — শূন্যস্থান পূরণ করো।",
     ["কাঁঠালচাঁপার"], "পাঠে আমার মন বসে না"),
    ("'______ ডালে লুকিয়ে থেকে পাখির মতো ডাকতে।' — শূন্যস্থান পূরণ করো।",
     ["বকুল"], "বকুল ডালে লুকিয়ে থেকে"),
    ("'সবাই যখন ঘুমিয়ে পড়ে ______ কূলটায়।' — শূন্যস্থান পূরণ করো।",
     ["কর্ণফুলীর"], "সবাই যখন ঘুমিয়ে পড়ে"),
    ("'আমি না হয় ______ হব, পাখির মতো বন্য।' — শূন্যস্থান পূরণ করো।",
     ["পাখিই"], "আমি না হয় পাখিই হব"),
]

# ─────────────────────────────────────────────────────────────────────────────────────────
# S05 বহুনির্বাচনি · mcq · 1 mark · TWO Remember + FOUR Understand
# The slot carries BOTH. Probe 2 is item 3 here. The Understand items are capped by the poem's
# four interpretable images — beyond those, a "কেন" item is retrieval wearing a কেন, because
# this poem answers most why-questions verbatim in the next line.
# ─────────────────────────────────────────────────────────────────────────────────────────
S05 = [
    ("'পাখির মতো' কবিতায় ব্যবহৃত 'কর্ণফুলী' শব্দটির অর্থ কী?",
     [("ক", "একটি নদীর নাম", True, None),
      ("খ", "একটি ফুলের নাম", False, "কাঁঠালচাঁপা ফুলের নাম, কর্ণফুলী নয়।"),
      ("গ", "একটি পাখির নাম", False, "কবিতায় পাখির কোনো নাম দেওয়া হয়নি।"),
      ("ঘ", "একটি গ্রামের নাম", False, "কবিতায় গাঁয়ের কথা আছে, কিন্তু কর্ণফুলী গাঁয়ের নাম নয়।")],
     "Remember", "easy", VOCAB, "BAN-VOCAB", "একটি নদীর নাম"),

    # NOT a second 'দুধভরা ওই চাঁদের বাটি' item. The first draft of this slot asked exactly what
    # Q12 already asks, and REPETITION caught it — verbatim reuse above `Remember` is barred by
    # §5, and Q12 is `Understand`. Replaced rather than re-tagged: re-tagging Q12 down to make
    # the pair legal would have been using §5's `Remember` carve-out to launder a duplicate.
    ("'পাখির মতো' কবিতায় কবিকে পড়তে বলেন কারা?",
     [("ক", "আম্মা ও আব্বা", True, None),
      ("খ", "শিক্ষক ও সহপাঠীরা", False, "কবিতায় শিক্ষক বা সহপাঠীর কথা নেই।"),
      ("গ", "ভাই ও বোন", False, "কবিতায় ভাইবোনের কথা বলা হয়নি।"),
      ("ঘ", "প্রতিবেশীরা", False, "কবিতায় প্রতিবেশীদের কথা নেই।")],
     "Remember", "easy", POEM, "BAN-POEM", "আম্মা বলেন পড়রে সোনা"),

    ("'আমি না হয় পাখিই হব, / পাখির মতো বন্য।' — এখানে কবি 'বন্য' হতে চান বলতে কী বোঝাচ্ছেন?",
     [("ক", "তিনি হিংস্র হতে চান", False,
       "'বন্য'-র অভিধানিক অর্থ ধরে থেমে গেলে এই ভুলটি হয়; কবিতায় হিংস্রতার কোনো ছবি নেই।"),
      ("খ", "তিনি বনের ভিতরে বাস করতে চান", False,
       "কবি গাঁয়ের কথা বলেছেন, বনের নয়; এটিও অভিধানিক অর্থে থেমে যাওয়া।"),
      ("গ", "তিনি নিয়মের বাঁধন ছেড়ে স্বাধীন হতে চান", True, None),
      ("ঘ", "তিনি পড়াশোনা একেবারে ছেড়ে দিতে চান", False,
       "প্রথম স্তবকের উপরের ছবিটুকু দেখলে এমন মনে হয়; কবি পড়া ছাড়ার কথা বলেননি, "
       "মুক্তির ইচ্ছার কথা বলেছেন।")],
     "Understand", "medium", POEM, "BAN-POEM", "আমি না হয় পাখিই হব"),

    ("'পাখির মতো' কবিতায় 'শহর' ও 'গাঁ' — কবি কোনটি বেছে নিতে চান, আর কেন?",
     [("ক", "শহর, কারণ সেখানে পড়াশোনার সুযোগ বেশি", False,
       "কবিতায় শহরকে ছেড়ে যাওয়ার কথাই বলা হয়েছে।"),
      ("খ", "গাঁ, কারণ সেখানে সে পাখির মতো মুক্ত থাকতে পারবে", True, None),
      ("গ", "শহর, কারণ সেখানে নদী আছে", False, "নদী গাঁয়ের ছবির সঙ্গে এসেছে, শহরের নয়।"),
      ("ঘ", "গাঁ, কারণ সেখানে আম্মা-আব্বা থাকেন", False,
       "আম্মা-আব্বা কবির কাছেই আছেন; তাঁদের অবস্থান নিয়ে কবিতায় কিছু বলা হয়নি।")],
     "Understand", "medium", POEM, "BAN-POEM", "কেমন করে শহর ছেড়ে"),

    ("'বকুল ডালে লুকিয়ে থেকে / পাখির মতো ডাকতে' — কবি লুকিয়ে থাকতে চান কেন?",
     [("ক", "তিনি কাউকে ভয় পেয়েছেন", False, "কবিতায় ভয়ের কোনো ছবি নেই।"),
      ("খ", "তিনি কারও সঙ্গে লুকোচুরি খেলছেন", False, "কবিতায় খেলার কথা বলা হয়নি।"),
      ("গ", "কারও চোখে না পড়ে পাখির মতো স্বাধীনভাবে থাকতে চান বলে", True, None),
      ("ঘ", "তিনি বকুল ফুল কুড়াতে চান", False,
       "বকুল ডাল কেবল লুকোনোর জায়গা; ফুল কুড়ানোর কথা কবিতায় নেই।")],
     "Understand", "medium", POEM, "BAN-POEM", "বকুল ডালে লুকিয়ে থেকে"),

    ("'সবাই যখন ঘুমিয়ে পড়ে' — এই চরণটি কবি সম্পর্কে আমাদের কী জানায়?",
     [("ক", "কবিও তখন ঘুমিয়ে পড়েন", False, "কবি জেগে থেকেই রাতের ছবিটি দেখছেন।"),
      ("খ", "সবাই ঘুমোলে কবি জেগে থেকে রাতের ছবি দেখেন ও ভাবেন", True, None),
      ("গ", "কবি রাতে পড়াশোনা করেন", False, "পরের স্তবক বলছে কবি তখন ওড়ার কথা ভাবেন।"),
      ("ঘ", "কবির ঘুম আসে না বলে তিনি অসুস্থ", False, "অসুস্থতার কোনো কথা কবিতায় নেই।")],
     "Understand", "medium", POEM, "BAN-POEM", "সবাই যখন ঘুমিয়ে পড়ে"),
]

# ─────────────────────────────────────────────────────────────────────────────────────────
# S06 বিপরীত শব্দ · short_answer · Remember · 1 mark · TEACHER-SUPPLIED KEY (CD-136)
# ─────────────────────────────────────────────────────────────────────────────────────────
S06 = [
    ("'পাখির মতো' কবিতায় ব্যবহৃত 'শহর' শব্দের বিপরীত শব্দ লেখো।",
     ["গ্রাম", "গাঁ", "পল্লি"], "কেমন করে শহর ছেড়ে"),
    ("'পাখির মতো' কবিতায় ব্যবহৃত 'ঘুম' শব্দের বিপরীত শব্দ লেখো।",
     ["জাগরণ", "জাগা"], "সবাই যখন ঘুমিয়ে পড়ে"),
    ("'পাখির মতো' কবিতায় ব্যবহৃত 'বন্য' শব্দের বিপরীত শব্দ লেখো।",
     ["পোষা", "গৃহপালিত"], "পাখির মতো বন্য"),
]

# ─────────────────────────────────────────────────────────────────────────────────────────
# S12 যুক্তবর্ণ ও শব্দ গঠন · short_answer · 1 mark · TEACHER-SUPPLIED KEY (CD-136)
# TAGGED DOWN to Remember per the 2026-08-15 tagging rule. The probe read these as Apply —
# রেফ/ফলা rule executed on a word not previously decomposed — but the level depends on whether
# the class has already decomposed the word, which the author cannot know. Under floors the
# uncertain direction is DOWN, so Remember is authored and any Apply reading is upside.
# ─────────────────────────────────────────────────────────────────────────────────────────
S12 = [
    ("'পাখির মতো' কবিতার 'কর্ণফুলী' শব্দের যুক্তবর্ণটি ভেঙে লেখো।",
     ["র্ণ = র + ণ", "র্ণ — র ও ণ", "রেফ + ণ"], "সবাই যখন ঘুমিয়ে পড়ে"),
    ("'পাখির মতো' কবিতার 'বন্য' শব্দের যুক্তবর্ণটি ভেঙে লেখো।",
     ["ন্য = ন + য", "ন্য — ন ও য"], "পাখির মতো বন্য"),
    ("'পাখির মতো' কবিতার 'ইচ্ছে' শব্দের যুক্তবর্ণটি ভেঙে লেখো।",
     ["চ্ছ = চ + ছ", "চ্ছ — চ ও ছ"], "আমার কেবল ইচ্ছে জাগে"),
]

# ─────────────────────────────────────────────────────────────────────────────────────────
# S13 এক কথায় প্রকাশ · short_answer · Remember · 1 mark · TEACHER-SUPPLIED KEY (CD-136)
# Probe 4 confirmed the slot-derived guess: definition-phrase → stored word is retrieval.
# ─────────────────────────────────────────────────────────────────────────────────────────
S13 = [
    ("'নদীর ধারে যে জায়গা' — 'পাখির মতো' কবিতার শব্দ দিয়ে এক কথায় প্রকাশ করো।",
     ["কূল"], "সবাই যখন ঘুমিয়ে পড়ে"),
    ("'যা বনের স্বভাবের, পোষ মানে না' — 'পাখির মতো' কবিতার শব্দ দিয়ে এক কথায় প্রকাশ করো।",
     ["বন্য"], "পাখির মতো বন্য"),
    ("'গ্রাম' শব্দটির চলিত ও সংক্ষিপ্ত রূপ — 'পাখির মতো' কবিতার শব্দ দিয়ে এক কথায় প্রকাশ করো।",
     ["গাঁ"], "সবুজ গাঁয়ে ঘুরব"),
]

# ─────────────────────────────────────────────────────────────────────────────────────────
# S11 প্রশ্ন তৈরি / বিরামচিহ্ন · short_answer · Apply · 1 mark
# Apply on its own demand: the student PRODUCES a question or PLACES punctuation — procedure
# executed on chapter material, not a fact retrieved.
# ─────────────────────────────────────────────────────────────────────────────────────────
S11 = [
    ("'কর্ণফুলীর কূলটায়' — এই উত্তরটি পাওয়া যায় এমন একটি প্রশ্ন তৈরি করো।",
     ["সবাই কোথায় ঘুমিয়ে পড়ে?", "কবিতায় সবাই কোথায় ঘুমিয়ে পড়ে?"],
     "সবাই যখন ঘুমিয়ে পড়ে", "BAN-LEARNERQ"),
    ("'ফেরেস্তারা' — এই উত্তরটি পাওয়া যায় এমন একটি প্রশ্ন তৈরি করো।",
     ["দুধভরা চাঁদের বাটি কারা উল্টায়?", "চাঁদের বাটি কারা উল্টায়?"],
     "দুধভরা ওই চাঁদের বাটি", "BAN-LEARNERQ"),
    ("'বকুল ডালে' — এই উত্তরটি পাওয়া যায় এমন একটি প্রশ্ন তৈরি করো।",
     ["কবি কোথায় লুকিয়ে থাকতে চান?", "কবি কোথায় লুকিয়ে পাখির মতো ডাকতে চান?"],
     "বকুল ডালে লুকিয়ে থেকে", "BAN-LEARNERQ"),
    ("'আম্মা বলেন পড়রে সোনা' — বাক্যটিতে প্রয়োজনীয় বিরামচিহ্ন বসিয়ে লেখো।",
     ["আম্মা বলেন, 'পড়রে সোনা।'", "আম্মা বলেন, পড়রে সোনা।"],
     "আম্মা বলেন পড়রে সোনা", "BAN-SENTENCE"),
    ("'কেমন করে শহর ছেড়ে সবুজ গাঁয়ে ঘুরব' — বাক্যটিতে প্রয়োজনীয় বিরামচিহ্ন বসিয়ে লেখো।",
     ["কেমন করে শহর ছেড়ে সবুজ গাঁয়ে ঘুরব!"],
     "কেমন করে শহর ছেড়ে", "BAN-SENTENCE"),
]

# ─────────────────────────────────────────────────────────────────────────────────────────
# S03 বাক্য গঠন · short_answer · Apply · 1 mark · words not used in waves 1–2
# ─────────────────────────────────────────────────────────────────────────────────────────
S03 = [("পাখি", "বকুল ডালে লুকিয়ে থেকে"), ("চাঁদ", "দুধভরা ওই চাঁদের বাটি"),
       ("শহর", "কেমন করে শহর ছেড়ে"), ("বকুল", "বকুল ডালে লুকিয়ে থেকে"),
       ("সবুজ", "সবুজ গাঁয়ে ঘুরব")]

# ─────────────────────────────────────────────────────────────────────────────────────────
# S10 ভাব নির্ণয় · short_answer · Apply · 1 mark
# All four are TRANSFORMATION tasks, not identification — identification of a ভাব from a given
# list is where waves 1–2 sit and its level is contested; transformation is unambiguously Apply.
# ─────────────────────────────────────────────────────────────────────────────────────────
S10 = [
    ("'পড়রে সোনা' — কথাটি 'অনুরোধ' ভাবে নতুন করে লেখো।",
     ["একটু পড়ো না, সোনা।", "দয়া করে একটু পড়ো।"], "আম্মা বলেন পড়রে সোনা"),
    ("'কেমন করে উড়ব' — কথাটি 'বিস্ময়' ভাবে নতুন করে লেখো।",
     ["আহা, কেমন করে উড়ব!", "কী সুন্দর করে উড়ব!"], "কেমন করে উড়ব"),
    ("'নদীর কাছে থাকতে' — কবির এই ইচ্ছাটি 'আদেশ' ভাবে একটি বাক্যে লেখো।",
     ["নদীর কাছে থাকো।", "নদীর কাছে গিয়ে থাকো।"], "নদীর কাছে থাকতে"),
    ("'সবুজ গাঁ' কথাটি ব্যবহার করে 'ইচ্ছা' ভাবের একটি বাক্য লেখো।",
     ["সবুজ গাঁয়ে ঘুরতে খুব ইচ্ছে করে।", "ইচ্ছে করে সবুজ গাঁয়ে চলে যাই।"], "সবুজ গাঁয়ে ঘুরব"),
]

# ─────────────────────────────────────────────────────────────────────────────────────────
# S07 সংক্ষিপ্ত উত্তর · short_answer · Understand · 2 marks
# Ten items, none of which the poem answers verbatim — each requires the student to construct
# meaning rather than lift a line. That is the constraint the probe named and it is what caps
# this slot; a "কেন" whose answer sits in the next line was NOT authored.
# ─────────────────────────────────────────────────────────────────────────────────────────
S07 = [
    ("'দুধভরা ওই চাঁদের বাটি / ফেরেস্তারা উল্টায়' — এই কথায় কবি রাতের কোন ছবি এঁকেছেন? "
     "নিজের ভাষায় লেখো।",
     ["পূর্ণিমার চাঁদকে দুধভরা বাটির মতো দেখাচ্ছে, আর ফেরেস্তারা সেই বাটি উল্টে দিচ্ছেন — "
      "অর্থাৎ চাঁদের আলো সারা রাত ছড়িয়ে পড়ছে।"], "দুধভরা ওই চাঁদের বাটি"),
    ("'পাঠে আমার মন বসে না / কাঁঠালচাঁপার গন্ধে' — কাঁঠালচাঁপার গন্ধ কবির কী করে? "
     "নিজের ভাষায় লেখো।",
     ["ফুলের গন্ধ কবির মনকে বই থেকে সরিয়ে বাইরের প্রকৃতির দিকে টেনে নেয়, তাই পড়ায় মন বসে না।"],
     "পাঠে আমার মন বসে না"),
    ("'আমার কেবল ইচ্ছে জাগে / নদীর কাছে থাকতে' — কবির এই ইচ্ছার পিছনে কী আছে বলে তোমার মনে হয়?",
     ["ঘরের ও পড়ার বাঁধন ছেড়ে খোলা প্রকৃতির কাছে মুক্তভাবে থাকার টান।"],
     "আমার কেবল ইচ্ছে জাগে"),
    ("'পাখির মতো' কবিতায় আম্মা ও আব্বা দুজনেই কী চান? তাঁদের কথা দুটির মিল কোথায়?",
     ["দুজনেই চান ছেলেটি মন দিয়ে পড়ুক; দুজনের কথাতেই পড়াশোনার প্রতি একই আগ্রহ ও যত্ন প্রকাশ পেয়েছে।"],
     "আব্বা বলেন মন দে"),
    ("'তখন কেবল ভাবতে থাকি' — 'তখন' বলতে কবিতায় কোন সময়কে বোঝানো হয়েছে?",
     ["রাতের বেলা, যখন সবাই ঘুমিয়ে পড়ে আর চাঁদের আলো ছড়িয়ে থাকে।"], "তখন কেবল ভাবতে থাকি"),
    ("'কেমন করে শহর ছেড়ে / সবুজ গাঁয়ে ঘুরব' — কবি শহর ছেড়ে যেতে চান কেন? বুঝিয়ে লেখো।",
     ["শহরে তাঁর মন বাঁধা পড়ে থাকে; গাঁয়ে গাছ, নদী আর খোলা আকাশ আছে বলে সেখানে তিনি মুক্তভাবে "
      "ঘুরতে পারবেন।"], "কেমন করে শহর ছেড়ে"),
    ("'আমি না হয় পাখিই হব' — 'না হয়' কথাটি কবির মনের কোন ভাব প্রকাশ করে?",
     ["একটু অভিমান মেশানো ইচ্ছা — সবাই যদি পড়ে মানুষ হয়, তবে সে না হয় পাখিই হবে।"],
     "আমি না হয় পাখিই হব"),
    ("'পাখির মতো' কবিতায় 'পাখি' কেবল একটি প্রাণী নয় — আর কী বোঝায়? নিজের ভাষায় লেখো।",
     ["পাখি এখানে স্বাধীনতার প্রতীক — বাঁধনহীনভাবে ওড়া, ডাকা আর ইচ্ছেমতো ঘুরে বেড়ানোর ছবি।"],
     "পাখির মতো ডাকতে"),
    ("'সবুজ গাঁয়ে ঘুরব' — 'সবুজ' শব্দটি দিয়ে কবি গাঁয়ের কোন ছবি আঁকছেন?",
     ["গাছপালায় ভরা, শান্ত ও প্রাণে ভরা একটি গ্রামের ছবি।"], "সবুজ গাঁয়ে ঘুরব"),
    ("কবিতায় 'কর্ণফুলী' নদীর নাম আসায় কবির জায়গা সম্পর্কে আমরা কী বুঝতে পারি?",
     ["কবির শৈশবের জায়গাটি কর্ণফুলী নদীর তীরে — অর্থাৎ ছবিটি কল্পনার নয়, চেনা একটি জায়গার।"],
     "একটি নদীর নাম"),
]

# ─────────────────────────────────────────────────────────────────────────────────────────
# S08 বিস্তৃত উত্তর · descriptive · Analyze · 5 marks
# EIGHT items — this is what CD-135(h)'s Analyze floor cost, and where it was paid from.
# Each takes the poem apart rather than restating it: parts, relations, contrasts.
# ─────────────────────────────────────────────────────────────────────────────────────────
S08 = [
    ("'পাখির মতো' কবিতার পাঁচটি স্তবকে কবির মনের ভাব ধাপে ধাপে কীভাবে বদলেছে — "
     "বিশ্লেষণ করে লেখো।",
     "স্তবক ধরে ধরে ভাবের বদল আলাদা করা — পড়ার নির্দেশ, ইচ্ছার জন্ম, রাতের কল্পনা, ওড়ার ভাবনা, "
     "শেষে সিদ্ধান্ত; আর পিতামাতার নির্দেশকে ছোট না করে কবির মনের কথা লেখা",
     "পাঁচটি স্তবকের ভাব আলাদা করে ধাপে ধাপে দেখানো হয়েছে, প্রতিটি স্তবক থেকে প্রমাণ দেওয়া হয়েছে; "
     "ভাষা শালীন ও পিতামাতার প্রতি সম্মান বজায় আছে।",
     "দু-তিনটি স্তবক নিয়ে লেখা হয়েছে বা ধাপগুলো আলাদা হয়নি; অথবা পড়াশোনা বা পিতামাতাকে "
     "হেয় করে এমন কথা এসেছে।", "আম্মা বলেন পড়রে সোনা"),

    ("'পাখির মতো' কবিতায় শহর ও গাঁয়ের ছবি দুটি আলাদা করে বিশ্লেষণ করো।",
     "দুটি জায়গার ছবি আলাদা করে চেনা ও পাশাপাশি রাখা, কবিতার চরণ থেকে প্রমাণসহ; শহর বা "
     "গ্রামের কোনোটিকেই হেয় না করে",
     "শহরের ছবি ও গাঁয়ের ছবি আলাদা করে লেখা হয়েছে, প্রতিটির পক্ষে কবিতার চরণ দেওয়া হয়েছে, "
     "আর পার্থক্যটি নিজের ভাষায় বলা হয়েছে।",
     "একটি জায়গার ছবি লেখা হয়েছে, বা প্রমাণ ছাড়া কেবল মতামত দেওয়া হয়েছে।",
     "কেমন করে শহর ছেড়ে"),

    ("'দুধভরা ওই চাঁদের বাটি / ফেরেস্তারা উল্টায়' — চিত্রকল্পটি বিশ্লেষণ করে লেখো।",
     "চিত্রকল্পের অংশগুলো আলাদা করা — চাঁদ, বাটি, দুধ, ফেরেস্তা — আর কোনটি কী বোঝায় তা মেলানো; "
     "ফেরেস্তা প্রসঙ্গে শ্রদ্ধাশীল ভাষা রাখা",
     "চিত্রকল্পের প্রতিটি অংশ আলাদা করে বোঝানো হয়েছে এবং পূর্ণিমার রাতের সঙ্গে মিলিয়ে দেখানো "
     "হয়েছে; ফেরেস্তা প্রসঙ্গে ভাষা শ্রদ্ধাশীল।",
     "কেবল 'পূর্ণিমার চাঁদ' লিখে থেমে যাওয়া হয়েছে, অংশগুলো আলাদা করা হয়নি; অথবা ফেরেস্তা "
     "প্রসঙ্গে অসতর্ক ভাষা এসেছে।", "দুধভরা ওই চাঁদের বাটি"),

    ("'পাখির মতো' কবিতায় বাঁধন ও স্বাধীনতার ভাব কোন কোন চরণে ফুটে উঠেছে — বিশ্লেষণ করো।",
     "দুই ভাবের চরণ আলাদা করে বেছে নেওয়া ও পাশাপাশি রাখা; পড়াশোনাকে কেবল 'বাঁধন' বলে "
     "উড়িয়ে না দিয়ে কবির অনুভূতি হিসেবে দেখানো",
     "বাঁধনের ও স্বাধীনতার চরণগুলো আলাদা করে দেখানো হয়েছে, আর দুটি ভাব কীভাবে মুখোমুখি "
     "দাঁড়িয়েছে তা বলা হয়েছে; পড়াশোনার মর্যাদা রক্ষা পেয়েছে।",
     "কেবল এক পক্ষের চরণ দেওয়া হয়েছে; অথবা পড়াশোনাকে অপ্রয়োজনীয় বলে দেখানো হয়েছে।",
     "তোমরা যখন শিখছ পড়া"),

    ("'পাখির মতো' কবিতার প্রথম স্তবকের দিনের ছবি আর তৃতীয় স্তবকের রাতের ছবি — "
     "দুটির পার্থক্য বিশ্লেষণ করো।",
     "দুই সময়ের ছবি আলাদা করা ও তুলনা করা, প্রতিটির পক্ষে চরণ দিয়ে; ঘরের কাজ ও কল্পনা "
     "দুটোরই মূল্য রেখে",
     "দিনের ছবি ও রাতের ছবি আলাদা করে লেখা হয়েছে, চরণ দিয়ে প্রমাণ দেওয়া হয়েছে, আর কোথায় "
     "পার্থক্য তা নিজের ভাষায় বলা হয়েছে।",
     "একটি সময়ের ছবি লেখা হয়েছে বা তুলনা করা হয়নি।", "সবাই যখন ঘুমিয়ে পড়ে"),

    ("'পাখির মতো' কবিতার শেষ দুই চরণে কবি যে সিদ্ধান্তে পৌঁছেছেন তা কোন কোন কথার উপর "
     "দাঁড়িয়ে আছে — বিশ্লেষণ করো।",
     "শেষ সিদ্ধান্তের ভিত্তি আগের স্তবকগুলোতে খুঁজে বের করা; সিদ্ধান্তটিকে পড়াশোনার বিরুদ্ধে "
     "রায় হিসেবে না দেখিয়ে কবির কল্পনা হিসেবে দেখানো",
     "শেষ দুই চরণের সঙ্গে আগের অন্তত দুটি স্তবকের যোগ দেখানো হয়েছে, আর সিদ্ধান্তটি কবির "
     "কল্পনা বলে বোঝানো হয়েছে।",
     "কেবল শেষ দুই চরণের অর্থ লেখা হয়েছে, ভিত্তি খোঁজা হয়নি; অথবা পড়াশোনা ছেড়ে দেওয়াকে "
     "সমর্থন করা হয়েছে।", "আমি না হয় পাখিই হব"),

    ("'পাখির মতো' কবিতায় 'পাখি' শব্দটি কত রকম অর্থে এসেছে — খুঁজে বের করে বিশ্লেষণ করো।",
     "একই শব্দের আলাদা আলাদা ব্যবহার চেনা — সত্যিকারের পাখি, পাখির মতো ডাকা, পাখি হয়ে "
     "যাওয়ার কল্পনা — আর প্রতিটির অর্থ আলাদা করে বলা",
     "অন্তত তিনটি আলাদা ব্যবহার চরণসহ দেখানো হয়েছে এবং প্রতিটির অর্থ আলাদা করে বলা হয়েছে।",
     "একটি বা দুটি ব্যবহার দেখানো হয়েছে, বা অর্থগুলো আলাদা করা হয়নি।", "পাখির মতো ডাকতে"),

    ("'পাখির মতো' কবিতার চারটি ছবি — কাঁঠালচাঁপার গন্ধ, বকুল ডাল, চাঁদের বাটি ও সবুজ গাঁ — "
     "কোনটি কী বোঝায়, মিলিয়ে বিশ্লেষণ করো।",
     "চারটি ছবি আলাদা করে চেনা এবং প্রতিটিকে কবির মুক্তির ইচ্ছার সঙ্গে মিলিয়ে দেখানো; "
     "কোনো ছবিকে বানিয়ে না নিয়ে পাঠ থেকেই নেওয়া",
     "চারটি ছবিই আলাদা করে বোঝানো হয়েছে এবং কবির ইচ্ছার সঙ্গে মিলিয়ে দেখানো হয়েছে; "
     "সবই পাঠের, কোনোটি বানানো নয়।",
     "দুই-তিনটি ছবি লেখা হয়েছে, বা পাঠে নেই এমন ছবি ঢুকেছে।", "পাঠে আমার মন বসে না"),
]


def build():
    bank = json.loads(BANK.read_text(encoding="utf-8"))
    src = EXTRACTION.read_text(encoding="utf-8")
    qs, slot_idx, src_idx = bank["questions"], bank["slot_index"], bank["source_index"]
    n = len(qs)
    added = []

    def emit(slot, text, qtype, role, bloom, diff, marks, topic, slug, anchor, **carrier):
        nonlocal n
        n += 1
        qid = f"QP-BAN-C5-U13-Q{n:02d}"
        q = {"qid": qid, "topic_tag": topic, "ref19_topic_id": slug,
             "question_text": text, "question_type": qtype, "paper_role": role,
             "bloom_level": bloom, "difficulty": diff, "tier": "tier1", "marks": marks,
             "chapter_ref": CH}
        q.update(carrier)
        qs.append(q)
        slot_idx[qid] = slot
        src_idx[qid] = anchor
        added.append((qid, slot, bloom))
        return qid

    for text, acc, anch in S04:
        emit("S04", text, "fill_blank", "short", "Remember", "easy", 1, POEM, "BAN-POEM", anch,
             blanks=[{"blank_no": 1, "accepted": acc}])

    for text, opts, bloom, diff, topic, slug, anch in S05:
        emit("S05", text, "mcq", "mcq", bloom, diff, 1, topic, slug, anch,
             options=[{"option_id": oid, "text": t, "is_correct": ok,
                       **({"why_wrong": w} if w else {})} for oid, t, ok, w in opts])

    for text, acc, anch in S06:
        emit("S06", text, "short_answer", "short", "Remember", "easy", 1, VOCAB,
             "BAN-WORDREL", anch, answer_key={"accepted": acc, "model_note": TS})

    for text, acc, anch in S12:
        emit("S12", text, "short_answer", "short", "Remember", "easy", 1, VOCAB,
             "BAN-JUKTOBARNA", anch, answer_key={"accepted": acc, "model_note": TS})

    for text, acc, anch in S13:
        emit("S13", text, "short_answer", "short", "Remember", "easy", 1, VOCAB,
             "BAN-WORDREL", anch, answer_key={"accepted": acc, "model_note": TS})

    for text, acc, anch, slug in S11:
        emit("S11", text, "short_answer", "short", "Apply", "medium", 1, SENT, slug, anch,
             answer_key={"accepted": acc,
                         "model_note": "শিক্ষার্থীর নিজের যেকোনো শুদ্ধ ও প্রাসঙ্গিক উত্তর "
                                       "গ্রহণযোগ্য। নমুনা উত্তর দেওয়া হলো।"})

    for word, anch in S03:
        emit("S03", f"'{word}' শব্দটি দিয়ে একটি অর্থপূর্ণ বাক্য লেখো।", "short_answer", "short",
             "Apply", "easy", 1, SENT, "BAN-SENTENCE", anch,
             answer_key={"accepted": [f"শিক্ষার্থীর নিজের লেখা '{word}' শব্দযুক্ত শুদ্ধ বাক্য"],
                         "model_note": f"শিক্ষার্থীর নিজের যেকোনো শুদ্ধ বাক্য গ্রহণযোগ্য, যদি "
                                       f"'{word}' শব্দটি সঠিক অর্থে ব্যবহৃত হয় এবং বাক্যটি "
                                       f"বিরামচিহ্নসহ সম্পূর্ণ হয়।"})

    for text, acc, anch in S10:
        emit("S10", text, "short_answer", "short", "Apply", "medium", 1, POEM, "BAN-POEM", anch,
             answer_key={"accepted": acc,
                         "model_note": "ভাবটি ঠিক হলে শিক্ষার্থীর নিজের ভাষার যেকোনো শুদ্ধ "
                                       "বাক্য গ্রহণযোগ্য। নমুনা উত্তর দেওয়া হলো।"})

    for text, acc, anch in S07:
        emit("S07", text, "short_answer", "short", "Understand", "medium", 2, POEM, "BAN-POEM",
             anch, answer_key={"accepted": acc,
                               "model_note": "নিজের ভাষায় লেখা হলেই হবে; মূল ভাবটি ধরা পড়লে "
                                             "পূর্ণ নম্বর। নমুনা উত্তর দেওয়া হলো।"})

    for text, crit, full, part, anch in S08:
        emit("S08", text, "descriptive", "structured", "Analyze", "hard", 5, POEM, "BAN-POEM",
             anch, rubric=rubric(crit, full, part))

    return bank, src, added


def qp_norm(s):
    s = re.sub(r"[‘’“”'\"()\[\]।,;:?!—–\-….*_#>|/·]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    bank, src, added = build()
    hay = qp_norm(src)

    bad = [(qid, a) for qid, a in bank["source_index"].items()
           if qp_norm(a) not in hay or len(qp_norm(a).split()) < 3]
    if bad:
        print("REFUSED — anchors that do not resolve or are too short:")
        for qid, a in bad:
            print(f"  {qid}: {a!r}")
        sys.exit(1)

    from collections import Counter
    qs = bank["questions"]
    blooms, slots = Counter(q["bloom_level"] for q in qs), Counter(bank["slot_index"].values())
    total = len(qs)

    bank["wave"] = 3
    bank["waves"]["3"] = ("Q37–Q88 · 2026-08-15 · author_U13_wave3.py · six slots released by "
                          "CD-134 + CD-136, sized against CD-135's floors")
    h = bank["header"]
    h["target"] = total
    h["reason"] = (
        f"{total} authored against a RULED MINIMUM of 79. 79 is where the floors are first "
        f"satisfiable once CD-134 and CD-136 release six slots, but three levels sit EXACTLY on "
        f"their floor there and one Subject Lead re-tag would redden the bank. {total} carries "
        f"margin on every level. Under CD-135 the pool has no ceiling, so the only thing a "
        f"larger pool costs is authoring — and the only thing it buys is exactly this margin.")
    h["spine_slots"] = sorted(slots)
    h["slot_counts"] = dict(sorted(slots.items()))
    h["bloom_floors"] = {
        "rule": "CD-135 — POOL level is REF-06 §3.6's LOWER BOUNDS ONLY. No upper bound binds a "
                "pool. The band, both bounds, applies at PAPER level.",
        "observed": {k: f"{blooms[k]}/{total} = {100*blooms[k]/total:.1f}%"
                     for k in ("Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create")},
        "margin_over_floor": {"Remember": blooms["Remember"] - -(-20*total//100),
                              "Understand": blooms["Understand"] - -(-25*total//100),
                              "Apply": blooms["Apply"] - -(-25*total//100),
                              "Analyze": blooms["Analyze"] - -(-10*total//100)},
        "Create": "0 items. CONTENT FACT, stated per CD-135(d) rather than left silent: পাঠ ১৩ is "
                  "a twenty-line lyric poem. A `Create` item would require the student to produce "
                  "new work of their own, which S15 রচনা is for — and S15 is OUT of chapter banks "
                  "by CD-136's boundary. The floor is 0%, so nothing is owed; this row exists so "
                  "the absence is a recorded decision and not an oversight.",
        "Evaluate": "2 items, floor 0%. Not grown in wave 3 — the poem's four interpretable "
                    "images were spent on Analyze, where CD-135(h) put the binding floor.",
    }
    h["teacher_supplied_keys"] = (
        "CD-136 — S06 বিপরীত শব্দ (3) · S12 যুক্তবর্ণ (3) · S13 এক কথায় প্রকাশ (3) carry "
        "TEACHER-SUPPLIED keys: the STIMULUS is a পাঠ ১৩ word, the KEY is a general Bangla "
        "language fact the chapter does not gloss. Each declares it in its own `model_note`, so "
        "the provenance travels with the item and not only with this header. Generalised from "
        "QB-D-013, which ruled the same for four শব্দার্থ items in wave 2.")
    h["tagging"] = (
        "Every `bloom_level` here is a claim about the item's COGNITIVE DEMAND and never about "
        "its slot. `MarkLogic_BAN_Spine.md` BAN-S05: *বহুনির্বাচনি হলো উত্তর দেওয়ার একটা পদ্ধতি, "
        "কোনো দক্ষতা নয়* — a slot the spine calls not-a-skill cannot carry a level. S05 "
        "accordingly carries BOTH Remember (2) and Understand (4). TAG-DOWN RULE (Principal, "
        "2026-08-15): under floors, over-tagging upward hides a breach, so an uncertain level is "
        "tagged DOWN. All 3 S12 items are tagged Remember though the probe read them as Apply; "
        "any Apply reading is upside, confirmed in review.")
    h["gaps"] = [
        "S14 আবেদনপত্র · S15 রচনা — NOT served, and the reason is CD-136's boundary, not the "
        "chapter's own use-line: both anchor to nothing in পাঠ ১৩ and carry no key at all, so "
        "neither half of the teacher-key rule is in play. Their home is paper-level authoring "
        "(workstreams/scholarship/MODEL_PAPERS_POLICY.md, which carries no S14/S15 clause today "
        "— raised at CD-136(d)).",
        "S04 · S05 · S06 · S11 · S12 · S13 are now SERVED. They were recorded as gaps in waves "
        "1–2 on the reading that পাঠ ১৩'s own 'কোন প্রশ্নে কাজে লাগবে' line capped the bank to "
        "the seven slots it names. CD-134 rules that line ADVISORY: it does not narrow §4's "
        "coverage test, which is defined against the spine. S04/S05/S11 were released by CD-134 "
        "alone; S06/S12/S13 needed CD-136 as well, because their keys are language facts the "
        "chapter does not gloss.",
        "S06 · S12 · S13 are authored at 3 items each against a 5-per-slot spine structure. "
        "CONTENT-LIMITED, not floor-limited: the poem yields three defensible বিপরীত pairs, "
        "three যুক্তবর্ণ words and three এক কথায় প্রকাশ mappings. A fourth of each would be a "
        "near-duplicate, which §4 forbids — 'stop when the source is exhausted'.",
        "অনুশীলনী ৮ (ছকের ভিতর শব্দ খোঁজা) remains UNAUTHORABLE: the grid is not reproduced in "
        "canon/marklogic/C5_Bangla_Source_13-23.md. An EXTRACTION gap, not a wave gap — no "
        "future wave closes it without re-extraction. Unchanged from wave 2, still raised.",
        "মিল-শব্দ (অনুশীলনী ৩) still has no C5 spine slot of its own; Q34 rides S07. Legitimate, "
        "a workaround, not a mapping. Unchanged from wave 2, still raised.",
        "S10 is authored as ভাব নির্ণয়, NOT পদ নির্ণয় — MarkLogic BAN-S10's C5 row reads "
        "পদ নির্ণয় (D0) and this chapter's own line authorises ভাব নির্ণয় as its alternative; "
        "পাঠ ১৩ carries no পদ material. Per-item mark is 1 either way. Unchanged, still RAISED.",
        "Not authored, judged too weak rather than overlooked: অনুশীলনী ৭'s গাছের তালিকা (the "
        "answer is wholly the student's own and traces to nothing) and অনুশীলনী ২'s line-ordering "
        "task (re-uses Q01's eight lines).",
        "REVIEW ITEM for the Subject Lead, raised by this wave's tagging rule and NOT silently "
        "changed: Q13 'কবির পাঠে মন বসে না কেন?' is tagged Understand, but the poem answers it "
        "verbatim in the next line — 'পাঠে আমার মন বসে না / কাঁঠালচাঁপার গন্ধে'. Under the "
        "tag-down rule it reads Remember. Re-tagging it would move Understand to "
        f"{blooms['Understand']-1}/{total}; the floor is {-(-25*total//100)}, so the bank stays "
        "green either way. That is what the margin was authored for.",
    ]
    BANK.write_text(json.dumps(bank, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"wave 3: +{len(added)} items → {total}")
    print("slots :", dict(sorted(slots.items())))
    print("bloom :", {k: blooms[k] for k in
                      ("Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create")})
    for lvl, pc in (("Remember", 20), ("Understand", 25), ("Apply", 25), ("Analyze", 10)):
        need = -(-pc * total // 100)
        print(f"   {lvl:<11} {blooms[lvl]:>2}/{total} = {100*blooms[lvl]/total:5.1f}%  "
              f"floor {pc}% = {need:>2} items  margin +{blooms[lvl]-need}")


if __name__ == "__main__":
    main()
