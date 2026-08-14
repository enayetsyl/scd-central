#!/usr/bin/env python3
"""author_U13_wave2.py — wave 2 of C5_BAN_U13_QuestionBank_v1.json. 24 → 36 items.

Run from repo root:
    python workstreams/question-banks/authoring/author_U13_wave2.py

Wave 1 is IMPORTED, not copied (`author_U13_wave1`), so its 24 items stay re-derivable from
their own script and this file is auditable as an INCREMENT: Q01–Q24 are wave 1's, unchanged;
Q25–Q36 are the twelve added here. QB-D-002 — a wave is a valid promotable increment.

WHAT UNLOCKED THIS WAVE
-----------------------
**PRINCIPAL RULING 2026-08-14 — a teacher-supplied gloss is an acceptable key for a শব্দার্থ
item.** Wave 1's `header.remember_cap` recorded the block: অনুশীলনী ১ names five words and the
chapter glosses none of them, so a শব্দার্থ item on গন্ধ · কূল · গাঁ · ইচ্ছা had no key inside
the extraction and REF-09 §5 forbids an item without one. The ruling supplies the key from the
teacher instead. Four `Remember` items become authorable (Q25–Q28).

**Why that is the item that mattered.** REF-06 §3.6 sets `Remember` at 20–30% of the pool, so
the pool's maximum size is `Remember ÷ 0.20`. Wave 1 sat at Remember = 5 and therefore at a
hard ceiling of 25 items — one above where it stopped. Remember = 10 lifts the ceiling to 50.
The chapter's content, not the band, is now the limit again.

⚑ THE FOUR GLOSS KEYS ARE NOT EXTRACTION-SOURCED, AND THAT IS RECORDED IN THE ARTIFACT — in
`header.teacher_gloss_ruling` and in each item's own `model_note`. Every other key in this bank
resolves to the chapter; these four resolve to the teacher. A later reader must be able to see
that difference without reading the session that made it. The `source_index` anchor for these
four points at the word's OCCURRENCE in the poem — which is what the item is about — not at a
gloss, because there is no gloss in the file to point at.

SIZING — 36, and why not more
-----------------------------
Content available after wave 1 was censused at ~19 further candidates (ceiling ~43). 36 is taken
because it is the largest size reachable with NO marginal item: every level lands mid-band rather
than on a floor, so a single later re-tag cannot redden the pool. Excluded as too weak to author:
অনুশীলনী ৭'s গাছের তালিকা (the answer is wholly the student's own, nothing traces), অনুশীলনী ২'s
line-ordering task (it re-uses Q01's eight lines), and a stanza-by-stanza item that overlaps Q35.
অনুশীলনী ৮ (ছকের ভিতর শব্দ খোঁজা) remains UNAUTHORABLE — the grid is not in the extraction.

Planned Bloom at 36: Remember 10 (27.8%) · Understand 10 (27.8%) · Apply 10 (27.8%) ·
Analyze 4 (11.1%) · Evaluate 2 (5.6%) · Create 0 (0.0%).
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import author_U13_wave1 as w1  # noqa: E402  — wave 1's items, built at import

ROOT = w1.ROOT
OUT = w1.OUT
POEM, VOCAB, SENT = w1.POEM, w1.VOCAB, w1.SENT
add, key, rubric = w1.add, w1.key, w1.rubric

GLOSS_NOTE = ("শব্দার্থটি পাঠের 'অর্থ জেনে নিই' ছকে নেই — অনুশীলনী ১ শব্দটিকে কাজ হিসেবে দিয়েছে, "
              "অর্থ দেয়নি। এই উত্তরকুঞ্জি শিক্ষকের দেওয়া (প্রধান শিক্ষকের সিদ্ধান্ত, ১৪ আগস্ট ২০২৬); "
              "কাছাকাছি অর্থের যেকোনো শুদ্ধ উত্তর গ্রহণযোগ্য।")

# =========================================================================================
# Q25–Q28 · S02 শব্দার্থ · 1 mark · Remember · THE FOUR TEACHER-GLOSS ITEMS
# অনুশীলনী ১-এর পাঁচ শব্দের চারটি (বন্য পাঠেই আছে, Q04-এ ধরা হয়েছে)।
# =========================================================================================
for word, gloss, alts, anchor in [
    ("গন্ধ", "ঘ্রাণ; নাক দিয়ে যা অনুভব করা যায়", ["ঘ্রাণ"],
     "মন বসে না কাঁঠালচাঁপার গন্ধে"),
    ("কূল", "নদীর তীর; পাড়", ["তীর", "পাড়", "নদীর পাড়"],
     "সবাই যখন ঘুমিয়ে পড়ে কর্ণফুলীর কূলটায়"),
    ("গাঁ", "গ্রাম", ["গ্রাম", "পল্লি"],
     "কেমন করে শহর ছেড়ে সবুজ গাঁয়ে ঘুরব"),
    ("ইচ্ছা", "মনের বাসনা; যা করতে মন চায়", ["বাসনা", "মনের চাওয়া"],
     "শব্দের অর্থ ও বাক্য গন্ধ কূল বন্য গাঁ ইচ্ছা"),
]:
    add("S02", VOCAB, f"'পাখির মতো' কবিতায় ব্যবহৃত '{word}' শব্দের অর্থ লেখো।",
        "short_answer", "short", "Remember", "easy", anchor,
        **key(gloss, *alts, note=GLOSS_NOTE))

# =========================================================================================
# Q29 · S07 · 2 marks · Remember — the one poem fact wave 1 left entirely unasked.
# The chapter's ⚠ block states ফেরেস্তা is acceptable, so the word is used as the poem uses it.
# =========================================================================================
add("S07", POEM, "'পাখির মতো' কবিতায় দুধভরা চাঁদের বাটি কারা উল্টায়?",
    "short_answer", "short", "Remember", "easy",
    "দুধভরা ওই চাঁদের বাটি ফেরেস্তারা উল্টায়",
    **key("ফেরেস্তারা",
          note="পাঠের পঙক্তি: 'দুধভরা ওই চাঁদের বাটি / ফেরেস্তারা উল্টায়।' "
               "শব্দটি কবিতারই, এবং পাঠের সতর্কতা-নির্দেশে একে গ্রহণযোগ্য বলা হয়েছে।"))

# =========================================================================================
# Q30–Q32 · Understand
# =========================================================================================
add("S07", POEM,
    "'তোমরা যখন শিখছ পড়া' — এখানে 'তোমরা' বলতে কাদের বোঝানো হয়েছে?",
    "short_answer", "short", "Understand", "medium",
    "তোমরা যখন শিখছ পড়া মানুষ হওয়ার জন্য",
    **key("যারা মানুষ হওয়ার জন্য পড়াশোনা করছে — কবির সহপাঠী ও অন্য শিক্ষার্থীরা",
          note="'পাঠক' বা 'আমরা যারা পড়ছি' — কাছাকাছি উত্তরও গ্রহণযোগ্য। "
               "শুধু 'পাখিরা' লিখলে নম্বর হবে না।"))

add("S07", POEM,
    "'পাখির মতো' কবিতার তৃতীয় স্তবকে রাতের যে ছবি আঁকা হয়েছে তা নিজের ভাষায় লেখো।",
    "short_answer", "short", "Understand", "medium",
    "সবাই যখন ঘুমিয়ে পড়ে কর্ণফুলীর কূলটায়",
    **key("সবাই যখন কর্ণফুলীর কূলে ঘুমিয়ে পড়ে, তখন আকাশে পূর্ণিমার চাঁদ ওঠে — "
          "কবি কল্পনা করেন ফেরেস্তারা সেই দুধভরা চাঁদের বাটি উল্টে দিচ্ছেন।",
          note="দুটি আলাদা কথা — সবার ঘুম ও চাঁদের কল্পনা; প্রতিটিতে ১ নম্বর। "
               "পঙক্তি হুবহু তুলে দিলে পূর্ণ নম্বর হবে না, নিজের ভাষা চাই।"))

add("S07", POEM,
    "কবিতাটির নাম 'পাখির মতো' রাখা কেন সার্থক হয়েছে?",
    "short_answer", "short", "Understand", "medium",
    "আমি না হয় পাখিই হব পাখির মতো বন্য",
    **key("কবিতার শুরু থেকে শেষ পর্যন্ত কবি পাখির মতো মুক্ত হতে চেয়েছেন — "
          "পাখির মতো ডাকতে, উড়তে আর পাখির মতো বন্য হতে; তাই নামটি সার্থক।",
          note="মূলভাব (S09) থেকে আলাদা প্রশ্ন: এখানে শুধু নামের সঙ্গে কবিতার মিলটা দেখাতে হবে, "
               "পুরো ভাব লিখতে হবে না।"))

# =========================================================================================
# Q33–Q35 · Apply
# =========================================================================================
add("S03", SENT, "'নদী' শব্দটি দিয়ে একটি অর্থপূর্ণ বাক্য লেখো।",
    "short_answer", "short", "Apply", "easy",
    "আমার কেবল ইচ্ছে জাগে নদীর কাছে থাকতে",
    **key("নদীর পাড়ে বসে থাকতে আমার খুব ভালো লাগে।",
          note="শব্দটি কবিতার নিজের ('নদীর কাছে থাকতে'), অনুশীলনী ১-এর তালিকার নয় — "
               "বাক্য গঠনের জন্য কবিতার শব্দ নেওয়া হয়েছে। শিক্ষার্থীর নিজের যেকোনো শুদ্ধ "
               "বাক্য গ্রহণযোগ্য। নমুনা উত্তর দেওয়া হলো।"))

add("S07", POEM,
    "'পাখির মতো' কবিতা থেকে দুটি মিল-শব্দের জোড়া খুঁজে বের করে লেখো "
    "(উদাহরণ: মন দে — গন্ধে)।",
    "short_answer", "short", "Apply", "medium",
    "মিল শব্দ খুঁজে বের করা",
    **key("থাকতে — ডাকতে; কূলটায় — উল্টায়",
          note="কবিতায় মোট পাঁচটি জোড়া আছে: মন দে — গন্ধে (উদাহরণ, ধরা হবে না) · "
               "থাকতে — ডাকতে · কূলটায় — উল্টায় · উড়ব — ঘুরব · জন্য — বন্য। "
               "যেকোনো দুটি সঠিক জোড়ায় পূর্ণ নম্বর, প্রতিটিতে ১।"))

# A TRANSFORMATION task, not "write a sentence in ভাব X" a second time. Q24 already asks the
# student to compose a নিষেধ sentence; repeating that frame with the label swapped scored 0.91
# Jaccard against Q24 on the pre-gate near-duplicate scan — above the 0.80 the §5 family's
# ZERO-OVERLAP uses, and a near-duplicate is a near-duplicate whether or not a gate is watching
# (ZERO-OVERLAP is N/A on a §4-shaped bank). Recast against the poem's own আদেশ line instead.
add("S10", POEM,
    "'পাখির মতো' কবিতায় আম্মা-আব্বা আদেশের ভাবে কথা বলেছেন। একই কথা 'উপদেশ' ভাবে "
    "কীভাবে বলা যায়, একটি বাক্যে লেখো।",
    "short_answer", "short", "Apply", "easy",
    "আম্মা বলেন পড়রে সোনা আব্বা বলেন মন দে",
    **key("মন দিয়ে পড়লে জীবনে ভালো মানুষ হওয়া যায়।",
          note="ছয়টি ভাবের মধ্যে উপদেশই একমাত্র যেটি কবিতার কোনো পঙক্তিতে নেই, তাই এখানে "
               "আদেশ-বাক্যকে উপদেশে বদলাতে বলা হয়েছে। আদেশ (হুকুম) নয়, বোঝানোর সুরে লেখা "
               "যেকোনো শুদ্ধ বাক্য গ্রহণযোগ্য।"))

# =========================================================================================
# Q36 · S08 · 5 marks · Analyze — distinct from Q15, which lists কবির ইচ্ছা, not প্রকৃতির ছবি.
# =========================================================================================
add("S08", POEM,
    "'পাখির মতো' কবিতায় প্রকৃতির যেসব ছবি ফুটে উঠেছে সেগুলো খুঁজে বের করে বর্ণনা করো।",
    "descriptive", "structured", "Analyze", "hard",
    "বকুল ডালে লুকিয়ে থেকে পাখির মতো ডাকতে",
    **rubric("কবিতা জুড়ে ছড়িয়ে থাকা প্রকৃতির ছবিগুলো আলাদা করে চেনা — কাঁঠালচাঁপার গন্ধ, "
             "নদী, বকুল ডাল, কর্ণফুলীর কূল, পূর্ণিমার চাঁদ, সবুজ গাঁ — আর সেগুলোকে "
             "আল্লাহর সৃষ্টির সৌন্দর্য হিসেবে দেখার দৃষ্টি",
             "অন্তত পাঁচটি আলাদা প্রাকৃতিক ছবি পাঠ থেকে খুঁজে বের করে নিজের ভাষায় বর্ণনা করা "
             "হয়েছে, কোনোটি বানানো নয়; আর প্রকৃতির সৌন্দর্যকে সৃষ্টিকর্তার নিদর্শন হিসেবে "
             "দেখার কথা এসেছে।",
             "দু-তিনটি ছবি লেখা হয়েছে, বা পাঠে নেই এমন ছবি ঢুকেছে; সৃষ্টির সৌন্দর্যের দিকটি "
             "অনুপস্থিত।"))


# =========================================================================================
# POOL INDEX — wave 1's labels, extended. Labels, not partitions (§3 row 12).
# =========================================================================================
def q(*ns):
    return [f"QP-BAN-C5-U13-Q{n:02d}" for n in ns]


POOL_INDEX = {
    "HW": w1.POOL_INDEX["HW"] + q(25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35),
    "AS": w1.POOL_INDEX["AS"] + q(25, 27, 29, 31, 34, 36),
    # CT stays at 5 items — MarkLogic §৬ caps a class test at 4–6 questions, so a bigger pool
    # does not mean a bigger CT label. Q29 replaces nothing; it is added because a CT wants a
    # cheap recall opener and Q02 alone was carrying it.
    "CT": w1.POOL_INDEX["CT"] + q(29),
}

BANK = dict(w1.BANK)
BANK["wave"] = 2
BANK["waves"] = {
    "1": "Q01–Q24 · 2026-08-14 · author_U13_wave1.py · the first bank under QUESTION_POLICY v1.1",
    "2": "Q25–Q36 · 2026-08-14 · author_U13_wave2.py · unlocked by the teacher-gloss ruling",
}
BANK["pool_index"] = POOL_INDEX
BANK["header"] = {
    "target": 36,
    "reason": (
        "36 is the largest pool this chapter supports with NO marginal item — every Bloom level "
        "lands mid-band rather than on a floor, so a later re-tag cannot redden it. Wave 1's "
        "ceiling was 25 (Remember 5 ÷ REF-09/REF-06's 20% floor); the teacher-gloss ruling takes "
        "Remember to 10 and the ceiling to 50, so content is again the limit and 36 is where "
        "content stops being distinct."),
    "topics": ["TOP-BAN-C5-05", "TOP-BAN-C5-01", "TOP-BAN-C5-02"],
    "spine_slots": ["S01", "S02", "S03", "S07", "S08", "S09", "S10"],
    "slot_counts": {"S01": 1, "S02": 7, "S03": 6, "S07": 10, "S08": 5, "S09": 1, "S10": 6},
    "teacher_gloss_ruling": (
        "PRINCIPAL RULING 2026-08-14 — a TEACHER-SUPPLIED GLOSS is an acceptable key for a "
        "শব্দার্থ item. **Q25 গন্ধ · Q26 কূল · Q27 গাঁ · Q28 ইচ্ছা carry keys that are NOT in the "
        "extraction.** অনুশীলনী ১ sets these four as tasks and the chapter glosses none of them; "
        "every other key in this bank resolves to পাঠ ১৩ and these four resolve to the teacher. "
        "Each says so in its own `model_note`, so the provenance travels with the item and not "
        "only with this header. Their `source_index` anchors point at the word's OCCURRENCE in "
        "the poem, which is what the item is about — there is no gloss in the file to anchor to, "
        "and SOURCE-TRACE would be satisfied either way, which is precisely why the difference "
        "is written down rather than left to the gate."),
    "remember_cap": (
        "THE CAP IS LIFTED AND THE ARITHMETIC IS RESTATED, because it is what sizes every future "
        "wave of this chapter. REF-06 §3.6 puts `Remember` at 20–30% of the pool, so max pool "
        "size = Remember ÷ 0.20 and min = Remember ÷ 0.30. Wave 1: Remember 5 → the pool could "
        "not exceed 25, and it held 24 — ONE item from a ceiling nobody had computed. Wave 2: "
        "Remember 10 (7 × S02 + S01 + Q10 ৪ক + Q29 ফেরেস্তারা) → the band admits 34–50, and 36 "
        "sits inside it at 27.8%. **শব্দার্থ is now exhausted at 7: four glossed in the chapter "
        "(one of which, 'দুধভরা ওই চাঁদের বাটি', is authored once at S07 not twice) plus the "
        "four ruled here.** A further wave cannot add a শব্দার্থ item without a new word, so the "
        "next Remember must come from somewhere else or the pool stops growing at 50."),
    "gaps": [
        "S04 শূন্যস্থান · S05 বহুনির্বাচনি · S06 বিপরীত শব্দ · S11 বিরামচিহ্ন · S12 যুক্তবর্ণ · "
        "S13 এক কথায় প্রকাশ · S14 আবেদনপত্র · S15 রচনা — NOT served, unchanged from wave 1. "
        "পাঠ ১৩'s own 'কোন প্রশ্নে কাজে লাগবে' line names seven slots and these are not among "
        "them. Recorded as a gap, not filled (§4, §7).",
        "অনুশীলনী ৮ (ছকের ভিতর শব্দ খোঁজা) is UNAUTHORABLE: the grid itself is not reproduced in "
        "canon/marklogic/C5_Bangla_Source_13-23.md. This is an EXTRACTION gap, not a wave gap — "
        "no future wave can close it without the চাপা being re-extracted. Raised.",
        "মিল-শব্দ (অনুশীলনী ৩) has no C5 spine slot of its own. Q34 rides S07 (সংক্ষিপ্ত উত্তর, "
        "2 marks), which is legitimate but is a workaround, not a mapping. Raised.",
        "S10 is authored as ভাব নির্ণয়, NOT পদ নির্ণয়. MarkLogic_BAN_Spine.md's BAN-S10 C5 row "
        "reads পদ নির্ণয় (D0); this chapter's own line authorises ভাব নির্ণয় as its alternative "
        "and পাঠ ১৩ carries no পদ material. Per-item mark is 1 either way. RAISED, not settled.",
        "Not authored, judged too weak rather than overlooked: অনুশীলনী ৭'s গাছের তালিকা (the "
        "answer is wholly the student's own and traces to nothing), অনুশীলনী ২'s line-ordering "
        "task (re-uses Q01's eight lines), and a stanza-by-stanza movement item (overlaps Q36).",
    ],
}

WIP_LINE = (
    "নির্মাণাধীন — wave 2's twelve items (Q25–Q36) are drafted; the gate suite has NOT yet been "
    "run against the 36-item pool and the Subject Lead has not read the new twelve. Resume: "
    "rebuild the envelopes, run gates.py and validate_import.py L1–L4, then rebuild without "
    "`--wip` to drop this line.")

if __name__ == "__main__":
    assert len(w1.QUESTIONS) == 36, f"wave 2 target is 36; built {len(w1.QUESTIONS)}"
    assert BANK["questions"] is w1.QUESTIONS
    if "--wip" in sys.argv:
        BANK["header"]["অবস্থা"] = WIP_LINE
    OUT.write_text(json.dumps(BANK, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {len(w1.QUESTIONS)} items to {OUT.relative_to(ROOT)}"
          + ("  [নির্মাণাধীন]" if "--wip" in sys.argv else "  [complete]"))
