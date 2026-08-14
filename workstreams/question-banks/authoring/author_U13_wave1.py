#!/usr/bin/env python3
"""author_U13_wave1.py — build C5_BAN_U13_QuestionBank_v1.json, wave 1.

Run from repo root:
    python workstreams/question-banks/authoring/author_U13_wave1.py

The bank is committed as data; this script is what makes it re-derivable rather than a
24-item blob nobody can rebuild (QB-D-009's reason for promoting the U21 authoring script
alongside its bank).

AUTHORED UNDER `canon/QUESTION_POLICY.md` v1.1 — the FIRST bank authored under it.
Shape is §4's (`header` · `slot_index` · `source_index` · `questions`), declared explicitly
as `policy_shape: "qp6"` so the suite does not have to infer it.

EVERY FACT COMES FROM `canon/marklogic/C5_Bangla_Source_13-23.md`, পাঠ ১৩ (heading at line 33).
No question is written from model memory (§4, §7). Where the chapter does not support a slot
the gap is recorded in the header, never filled.

EVERY MARK COMES FROM `canon/marklogic/MarkLogic_BAN_Spine.md`, C5 column, PER ITEM — S01 10 ·
S02 1 · S03 1 · S07 2 · S08 5 · S09 5 · S10 1. None is inferred.

CURATION: the chapter's own ⚠ block bars অনুশীলনী ৫'s "আর একটা গান গাও না!" (C-03). The
substitution is at Q23 and is REF-01 §4.5 E-03's own standard rewrite; see SUBSTITUTION below.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "workstreams/question-banks/banks/C5_BAN_U13_QuestionBank_v1.json"
SRC = "canon/marklogic/C5_Bangla_Source_13-23.md"

# --- MarkLogic_BAN_Spine.md, C5 per-ITEM marks (slot totals are a different column) -------
MARKS = {"S01": 10, "S02": 1, "S03": 1, "S07": 2, "S08": 5, "S09": 5, "S10": 1}

# --- the two register identities, both read at source (QUESTION_POLICY §3 row 18) ---------
POEM = ("TOP-BAN-C5-05", "BAN-POEM")       # TOPIC_NUMBERS.md line 56 · REF-19 line 307
VOCAB = ("TOP-BAN-C5-01", "BAN-VOCAB")     # TOPIC_NUMBERS.md line 54 · REF-19 line 300
SENT = ("TOP-BAN-C5-02", "BAN-SENTENCE")   # TOPIC_NUMBERS.md line 55 · REF-19 line 301

# SUBSTITUTION (C-03). Barred by the chapter's own ⚠ block: "আর একটা গান গাও না!" — অনুশীলনী ৫'s
# অনুরোধ example. Replacement: "আর একটা গল্প বলো না!"  REF-01 §4.5 E-03 lists this exact swap
# ("গান গায় / শোনে / শেখে" → গল্প / ছড়া / কুরআন — বলে / পড়ে / শোনে / শেখে). §4.2's four
# preservations, one by one: LEARNING OUTCOME — still "name the ভাব of a given sentence", still
# the অনুরোধ category, which no other item in the bank covers; REQUIRED VOCABULARY — the target
# words of অনুশীলনী ৫ are the six ভাব labels, not গান, and all six survive; BLOOM — unchanged, the
# sentence is outside the poem so classifying it is Apply either way; READING DIFFICULTY —
# identical frame "আর একটা … না!", same length, same চলিত register, one noun and its verb changed.

QUESTIONS = []
SLOT = {}
ANCHOR = {}


def add(slot, topic, text, qtype, role, bloom, diff, anchor, **carrier):
    n = len(QUESTIONS) + 1
    qid = f"QP-BAN-C5-U13-Q{n:02d}"
    tag, slug = topic
    q = {
        "qid": qid,
        "topic_tag": tag,
        "ref19_topic_id": slug,
        "question_text": text,
        "question_type": qtype,
        "paper_role": role,
        "bloom_level": bloom,
        "difficulty": diff,
        "tier": "tier1",
        "marks": MARKS[slot],
        "chapter_ref": "পাঠ ১৩ — পাখির মতো",
    }
    q.update(carrier)
    QUESTIONS.append(q)
    SLOT[qid] = slot
    ANCHOR[qid] = anchor
    return qid


def key(*accepted, note=None):
    k = {"accepted": list(accepted)}
    if note:
        k["model_note"] = note
    return {"answer_key": k}


def rubric(criterion, full, partial):
    """§4's interim minimum: TWO bands and a SINGLE `islamic_alignment` criterion row with band
    descriptors. Marking is by the school's own scheme, held outside the payload (§4)."""
    return {"rubric": {
        "bands": ["সম্পূর্ণ", "আংশিক"],
        "criteria": [{
            "role": "islamic_alignment",
            "criterion": criterion,
            "band_descriptors": {"সম্পূর্ণ": full, "আংশিক": partial},
        }],
    }}


# =========================================================================================
# S01 — কবিতা মুখস্থ · 10 marks/item · নেপ §১ (কবি ও কবিতার নামসহ প্রথম ৮ লাইন · 1+1+8)
# The chapter names its own S01 span: "প্রথম ৮ পঙ্‌ক্তি (S01-এর জন্য) … প্রথম দুই স্তবক".
# One item only — the span is fixed, so a second S01 item is the near-duplicate §4 warns about.
# E-AUTHOR-ENDORSE: the poet's name is asked as INFORMATION, with no honorific qualifier.
# =========================================================================================
add("S01", POEM,
    "কবি ও কবিতার নাম লিখে 'পাখির মতো' কবিতার প্রথম আট পঙক্তি মুখস্থ লেখো।",
    "short_answer", "structured", "Remember", "medium",
    "আম্মা বলেন পড়রে সোনা আব্বা বলেন মন দে",
    **key(
        "কবিতা: পাখির মতো; কবি: আল মাহমুদ। আম্মা বলেন, পড়রে সোনা / আব্বা বলেন, মন দে। / "
        "পাঠে আমার মন বসে না / কাঁঠালচাঁপার গন্ধে। / আমার কেবল ইচ্ছে জাগে / নদীর কাছে থাকতে, / "
        "বকুল ডালে লুকিয়ে থেকে / পাখির মতো ডাকতে।",
        note="নেপ §১ অনুযায়ী নম্বর ভাগ: কবিতার নাম ১ + কবির নাম ১ + আট পঙক্তি ৮ = ১০। "
             "পঙক্তি হুবহু পাঠের মতো হতে হবে; বানান ও যতিচিহ্নে ছাড় দেওয়া যাবে।"))

# =========================================================================================
# S02 — শব্দার্থ · 1 mark/item · CAPPED AT 3 (see header.remember_cap)
# Only 'অর্থ জেনে নিই' carries keys. Its fourth row, 'দুধভরা ওই চাঁদের বাটি', is authored as the
# S07 ৪ঙ item instead of a second শব্দার্থ item on the same phrase.
# =========================================================================================
add("S02", VOCAB, "'পাখির মতো' কবিতায় ব্যবহৃত 'কর্ণফুলী' শব্দের অর্থ লেখো।",
    "short_answer", "short", "Remember", "easy",
    "কর্ণফুলী একটি নদীর নাম",
    **key("একটি নদীর নাম", "নদীর নাম"))

add("S02", VOCAB, "'পাখির মতো' কবিতায় ব্যবহৃত 'কাঁঠালচাঁপা' শব্দের অর্থ লেখো।",
    "short_answer", "short", "Remember", "easy",
    "কাঁঠালচাঁপা হলুদ রঙের একধরনের ফুল",
    **key("হলুদ রঙের একধরনের ফুল", "একধরনের ফুল"))

add("S02", VOCAB, "'পাখির মতো' কবিতায় ব্যবহৃত 'বন্য' শব্দের অর্থ লেখো।",
    "short_answer", "short", "Remember", "easy",
    "চাঁদকে বোঝানো হয়েছে বন্য বুনো",
    **key("বুনো"))

# =========================================================================================
# S03 — বাক্য গঠন · 1 mark/item · অনুশীলনী ১-এর নিজস্ব পাঁচটি শব্দ
# Apply, not Remember: the student builds a NEW sentence. Note that these five words are set by
# the chapter as tasks and carry no glossary key in it — which is exactly why they are usable
# here (the student supplies the sentence) and NOT usable as S02 items (nobody supplies the key).
# =========================================================================================
for word, diff, anchor, model in [
    ("গন্ধ", "medium", "পাঠে আমার মন বসে না কাঁঠালচাঁপার গন্ধে",
     "কাঁঠালচাঁপার গন্ধ খুব মিষ্টি।"),
    ("কূল", "medium", "সবাই যখন ঘুমিয়ে পড়ে কর্ণফুলীর কূলটায়",
     "কর্ণফুলীর কূলে অনেক নৌকা বাঁধা আছে।"),
    ("বন্য", "easy", "আমি না হয় পাখিই হব পাখির মতো বন্য",
     "বনের পাখিরা বন্য জীবন ভালোবাসে।"),
    ("গাঁ", "easy", "কেমন করে শহর ছেড়ে সবুজ গাঁয়ে ঘুরব",
     "আমাদের গাঁ খুব সবুজ।"),
    ("ইচ্ছা", "easy", "শব্দের অর্থ ও বাক্য গন্ধ কূল বন্য গাঁ ইচ্ছা",
     "মন দিয়ে পড়ার ইচ্ছা আমার সবসময় থাকে।"),
]:
    add("S03", SENT, f"'{word}' শব্দটি দিয়ে একটি অর্থপূর্ণ বাক্য লেখো।",
        "short_answer", "short", "Apply", diff, anchor,
        **key(model, note=f"শিক্ষার্থীর নিজের যেকোনো শুদ্ধ বাক্য গ্রহণযোগ্য, যদি '{word}' "
                          f"শব্দটি সঠিক অর্থে ব্যবহৃত হয় এবং বাক্যটি বিরামচিহ্নসহ সম্পূর্ণ হয়। "
                          f"নমুনা উত্তর দেওয়া হলো।"))

# =========================================================================================
# S07 — সংক্ষিপ্ত উত্তর · 2 marks/item · অনুশীলনী ৪ ক · খ · ঙ + দুটি পাঠভিত্তিক প্রশ্ন
# ৪ক is literal retrieval and is labelled `Remember` rather than dressed up as `Understand`.
# ৪গ and ৪ঘ are NOT here — they are five-mark extended answers and sit at S08.
# =========================================================================================
add("S07", POEM, "'পাখির মতো' কবিতায় সবাই কোথায় ঘুমিয়ে পড়ে?",
    "short_answer", "short", "Remember", "easy",
    "সবাই যখন ঘুমিয়ে পড়ে কর্ণফুলীর কূলটায়",
    **key("কর্ণফুলীর কূলটায়", "কর্ণফুলী নদীর কূলে"))

add("S07", POEM, "'পাখির মতো' কবিতায় কে শহর ছেড়ে গাঁয়ে যেতে চায়?",
    "short_answer", "short", "Understand", "easy",
    "খ কে শহর ছেড়ে গাঁয়ে যেতে চায়",
    **key("কবিতার কথক, অর্থাৎ কবি নিজে",
          note="'কবি' বা 'কবিতার কথক' — দুটোই গ্রহণযোগ্য। শুধু 'পাখি' লিখলে নম্বর হবে না।"))

add("S07", POEM, "'পাখির মতো' কবিতায় 'দুধভরা ওই চাঁদের বাটি' বলতে কী বোঝানো হয়েছে?",
    "short_answer", "short", "Understand", "medium",
    "দুধভরা ওই চাঁদের বাটি বলতে কী বোঝানো হয়েছে",
    **key("পূর্ণিমার চাঁদকে বোঝানো হয়েছে",
          note="পাঠের 'অর্থ জেনে নিই' ছকের অর্থই মূল উত্তর।"))

add("S07", POEM, "'পাখির মতো' কবিতায় কবির পাঠে মন বসে না কেন?",
    "short_answer", "short", "Understand", "medium",
    "পাঠে আমার মন বসে না কাঁঠালচাঁপার গন্ধে",
    **key("কাঁঠালচাঁপা ফুলের গন্ধে কবির পাঠে মন বসে না"))

add("S07", POEM, "'পাখির মতো' কবিতায় কবি কোথায় লুকিয়ে থেকে কার মতো ডাকতে চান?",
    "short_answer", "short", "Understand", "medium",
    "বকুল ডালে লুকিয়ে থেকে পাখির মতো ডাকতে",
    **key("বকুল ডালে লুকিয়ে থেকে পাখির মতো ডাকতে চান",
          note="দুটি আলাদা তথ্য — জায়গা (বকুল ডাল) ও তুলনা (পাখি); প্রতিটিতে ১ নম্বর "
               "(MarkLogic §৭ — নম্বর আলাদা কথার সংখ্যা গোনে)।"))

# =========================================================================================
# S08 — বিস্তৃত উত্তর · 5 marks/item · descriptive → rubric
# =========================================================================================
add("S08", POEM,
    "'পাখির মতো' কবিতায় কবির কী কী করতে ইচ্ছা করে — পাঠ থেকে একটি তালিকা করে লেখো।",
    "descriptive", "structured", "Analyze", "medium",
    "কবির কী কী করতে ইচ্ছা করে তার একটি তালিকা করি",
    **rubric("পাঠ থেকে কবির ইচ্ছাগুলো আলাদা করে চেনা ও সাজানো — নদীর কাছে থাকা, বকুল ডালে "
             "লুকিয়ে পাখির মতো ডাকা, উড়ে যাওয়া, শহর ছেড়ে সবুজ গাঁয়ে ঘোরা, পাখি হওয়া; "
             "আর ইচ্ছাগুলো এমনভাবে লেখা যাতে আম্মা-আব্বার পড়ার নির্দেশকে ছোট করা না হয়",
             "কবিতা থেকে অন্তত পাঁচটি আলাদা ইচ্ছা নিজের ভাষায় তালিকা করে লেখা হয়েছে, "
             "কোনোটি বানানো নয়, সবই পাঠের; ভাষা শালীন ও পিতামাতার প্রতি সম্মান বজায় রাখা।",
             "দু-তিনটি ইচ্ছা লেখা হয়েছে, বা তালিকায় পাঠে নেই এমন কথা ঢুকেছে; "
             "অথবা পড়াশোনা বা পিতামাতাকে হেয় করে এমন কথা এসেছে।"))

add("S08", POEM,
    "'পাখির মতো' কবিতায় কবি পাখির মতো বন্য হতে চান কেন? পাঠ থেকে বুঝিয়ে লেখো।",
    "descriptive", "structured", "Analyze", "medium",
    "কবি পাখির মতো বন্য হতে চান কেন",
    **rubric("কবির চাওয়ার কারণ পাঠের ভেতর থেকে ব্যাখ্যা করা — বইয়ের বাঁধা পড়ায় মন বসে না, "
             "প্রকৃতির টান বেশি, তাই মুক্তভাবে উড়তে চান; সেই সঙ্গে বোঝানো যে কবির এই চাওয়া "
             "একটি কল্পনা, পড়াশোনা ছেড়ে দেওয়ার পরামর্শ নয়",
             "কারণ পাঠের পঙক্তি ধরে ব্যাখ্যা করা হয়েছে, এবং শিক্ষার্থী স্পষ্ট করেছে যে এটি "
             "কবির কল্পনা — জ্ঞান অর্জনের দায়িত্ব অস্বীকার করা হয়নি।",
             "কারণ বলা হয়েছে কিন্তু পাঠের সঙ্গে যুক্ত করা হয়নি; অথবা পড়াশোনা ছেড়ে দেওয়াই "
             "ভালো — এমন ভাব এসেছে।"))

add("S08", POEM,
    "'পাখির মতো' কবিতায় আম্মা-আব্বা কবিকে পড়তে বলেন, কিন্তু কবির মন পড়ায় বসে না। "
    "একজন শিক্ষার্থীর জন্য বাবা-মায়ের কথা শোনা কেন জরুরি — নিজের মত পাঁচটি বাক্যে লেখো।",
    "descriptive", "structured", "Evaluate", "hard",
    "আম্মা বলেন পড়রে সোনা আব্বা বলেন মন দে",
    **rubric("পিতামাতার আনুগত্য ও জ্ঞান অর্জনের গুরুত্ব সম্পর্কে নিজের যুক্তিসহ মত, "
             "কবিতার প্রসঙ্গ ধরে",
             "পাঁচটি আলাদা যুক্তি লেখা হয়েছে, প্রতিটি কবিতার প্রসঙ্গের সঙ্গে যুক্ত; "
             "পিতামাতার প্রতি সম্মান ও জ্ঞান অর্জনের দায়িত্ব — দুটোই স্পষ্টভাবে এসেছে।",
             "দু-তিনটি যুক্তি, বা যুক্তি কবিতার সঙ্গে যুক্ত নয়; পিতামাতার প্রতি সম্মানের দিকটি "
             "অনুপস্থিত বা অসম্মানজনক ভাষা এসেছে।"))

add("S08", POEM,
    "'তোমরা যখন শিখছ পড়া / মানুষ হওয়ার জন্য' — 'পড়াশোনা করে মানুষ হওয়া' বলতে তুমি কী বোঝো? "
    "নিজের মত পাঁচটি বাক্যে লেখো।",
    "descriptive", "structured", "Evaluate", "hard",
    "তোমরা যখন শিখছ পড়া মানুষ হওয়ার জন্য",
    **rubric("পড়াশোনার উদ্দেশ্য নিয়ে নিজের মত — জ্ঞান, চরিত্র, আদব ও অন্যের উপকারে আসা; "
             "কেবল পরীক্ষা পাসের চেয়ে বড় লক্ষ্যের কথা",
             "পাঁচটি আলাদা কথা, প্রতিটিতে নিজের যুক্তি; ভালো চরিত্র ও আদবের কথা এসেছে, "
             "এবং জ্ঞানকে অন্যের উপকারে লাগানোর কথা বলা হয়েছে।",
             "দু-তিনটি কথা, যুক্তি দুর্বল; শুধু পরীক্ষা বা চাকরির কথা, চরিত্র ও আদবের দিক "
             "অনুপস্থিত।"))

# =========================================================================================
# S09 — মূলভাব · 5 marks/item · একটি প্রশ্ন (নেপ §৯ — ১টি)
# One item only: two মূলভাব items on one poem are the same question twice.
# =========================================================================================
add("S09", POEM, "'পাখির মতো' কবিতার মূলভাব নিজের ভাষায় লেখো।",
    "descriptive", "structured", "Analyze", "hard",
    "আমি না হয় পাখিই হব পাখির মতো বন্য",
    **rubric("পুরো কবিতা থেকে মূল ভাব বের করে আনা — শিশুমনের প্রকৃতির টান ও মুক্তির কল্পনা, "
             "পড়ার টেবিলের বাঁধনের বিপরীতে; আর সেই কল্পনাকে পড়াশোনা ও পিতামাতার নির্দেশের "
             "বিরোধী করে না দেখানো",
             "মূলভাব নিজের ভাষায়, কবিতার কোনো পঙক্তি হুবহু না তুলে; প্রকৃতির টান ও শিশুর "
             "কল্পনা — দুটোই এসেছে, এবং কল্পনাটি কল্পনা হিসেবেই উপস্থাপিত।",
             "কবিতার পঙক্তি তুলে দেওয়া হয়েছে, বা কেবল একটি দিক এসেছে; অথবা পড়াশোনা "
             "ছেড়ে দেওয়াই কবিতার শিক্ষা — এমন ভুল ভাব এসেছে।"))

# =========================================================================================
# S10 — ভাব নির্ণয় · 1 mark/item · অনুশীলনী ৫
# ⚠ SLOT NOTE, reported and NOT resolved here: MarkLogic_BAN_Spine.md's BAN-S10 C5 row reads
# পদ নির্ণয় (D0). This chapter's own "কোন প্রশ্নে কাজে লাগবে" line authorises ভাব নির্ণয় as its
# alternative — "এটি পদ নির্ণয়ের বিকল্প হিসেবে ব্যবহার করা যাবে" — and পাঠ ১৩ carries no পদ
# material at all, so a পদ নির্ণয় item would source grammar from outside the chapter, which §4
# forbids. The MARK is identical (1/item) either way, so nothing in the spine's mark authority
# moves. Raised as a batched question; not settled by this bank.
# =========================================================================================
add("S10", POEM, "'আম্মা বলেন, পড়রে সোনা' — বাক্যটি কোন ভাব প্রকাশ করে?",
    "short_answer", "short", "Understand", "easy",
    "আম্মা বলেন পড়রে সোনা",
    **key("আদেশ"))

add("S10", POEM, "'আমার কেবল ইচ্ছে জাগে নদীর কাছে থাকতে' — বাক্যটি কোন ভাব প্রকাশ করে?",
    "short_answer", "short", "Understand", "easy",
    "আমার কেবল ইচ্ছে জাগে নদীর কাছে থাকতে",
    **key("ইচ্ছা"))

add("S10", POEM, "'কেমন করে শহর ছেড়ে সবুজ গাঁয়ে ঘুরব!' — বাক্যটি কোন ভাব প্রকাশ করে?",
    "short_answer", "short", "Understand", "medium",
    "কেমন করে শহর ছেড়ে সবুজ গাঁয়ে ঘুরব",
    **key("বিস্ময়"))

# --- THE C-03 SUBSTITUTION -------------------------------------------------------------
add("S10", POEM, "'আর একটা গল্প বলো না!' — বাক্যটি কোন ভাব প্রকাশ করে?",
    "short_answer", "short", "Apply", "medium",
    "ভাব নির্ণয় আদেশ নিষেধ অনুরোধ",
    **key("অনুরোধ",
          note="অনুশীলনী ৫-এর অনুরোধ-বাক্যটি পাঠের সতর্কতা-নির্দেশ অনুযায়ী বদলানো হয়েছে "
               "(কোড C-03); কাজ, ভাব-শ্রেণি ও পড়ার কাঠিন্য অপরিবর্তিত।"))

add("S10", POEM,
    "অনুশীলনী ৫-এর তালিকা থেকে 'নিষেধ' ভাব বেছে নাও, আর 'পাখির মতো' কবিতার প্রসঙ্গে "
    "সেই ভাব প্রকাশ করে এমন একটি বাক্য নিজে লেখো।",
    "short_answer", "short", "Apply", "easy",
    "ভাব নির্ণয় আদেশ নিষেধ অনুরোধ",
    **key("পড়ার সময় জানালার বাইরে তাকিয়ো না।",
          note="শিক্ষার্থীর নিজের যেকোনো শুদ্ধ নিষেধবাচক বাক্য গ্রহণযোগ্য, যদি তা কবিতার "
               "প্রসঙ্গের সঙ্গে যুক্ত হয়। নমুনা উত্তর দেওয়া হলো।"))


# =========================================================================================
# POOL INDEX — LABELS, NOT PARTITIONS (QUESTION_POLICY §3 row 12: one Pool per chapter;
# HW · AS · CT are selection labels and an item may carry more than one).
# =========================================================================================
def q(*ns):
    return [f"QP-BAN-C5-U13-Q{n:02d}" for n in ns]


POOL_INDEX = {
    # HW — REF-08: the practice surface. Everything except the two Evaluate essays and the মূলভাব,
    # which need class discussion first.
    "HW": q(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 21, 22, 23, 24),
    # AS — QB-D-004: deliberately mixed, about half at HW level and half above.
    "AS": q(2, 3, 6, 8, 11, 13, 15, 16, 17, 18, 19, 21, 23),
    # CT — MarkLogic §৬ + CD-021: 4–6 items lifted at IDENTICAL marks, at least one উচ্চতর.
    # Here 5 items = ১+২+২+৫+৫ = ১৫ নম্বর; Q16 (Analyze) and Q19 (Analyze) satisfy the উচ্চতর rule.
    "CT": q(2, 10, 13, 16, 19),
}

BANK = {
    "schema_version": "1.0",
    "policy_shape": "qp6",
    "bank_id": "QB-BAN-C5-U13",
    "wave": 1,
    "subject": "BAN",
    "class": 5,
    "chapter": "পাঠ ১৩ — পাখির মতো",
    "extraction_path": SRC,
    "source_extraction": SRC,
    "curation": "FLEXIBLE · C-03 substitution applied at Q23 (অনুশীলনী ৫)",
    "header": {
        "target": 24,
        "reason": (
            "24 clears REF-09 §4.3's floor of 20, serves all seven slots this chapter's own "
            "'কোন প্রশ্নে কাজে লাগবে' line names (S01·S02·S03·S07·S08·S09·S10), and divides "
            "against REF-06 §3.6's C3–5 band without forcing any level outside it — a §4 "
            "production target, not a quota."),
        "topics": ["TOP-BAN-C5-05", "TOP-BAN-C5-01", "TOP-BAN-C5-02"],
        "spine_slots": ["S01", "S02", "S03", "S07", "S08", "S09", "S10"],
        "slot_counts": {"S01": 1, "S02": 3, "S03": 5, "S07": 5, "S08": 4, "S09": 1, "S10": 5},
        "remember_cap": (
            "শব্দার্থ IS CAPPED, DELIBERATELY, and the cap was planned before drafting. MarkLogic "
            "§৩ fixes শব্দার্থ as জ্ঞানমূলক, so every S02 item is `Remember` and REF-06 §3.6's "
            "20–30% band is the binding constraint. Two caps applied: (1) only FOUR words carry a "
            "meaning IN the extraction (কর্ণফুলী · কাঁঠালচাঁপা · 'দুধভরা ওই চাঁদের বাটি' · বন্য) — "
            "অনুশীলনী ১'s গন্ধ · কূল · গাঁ · ইচ্ছা are set as TASKS with no key in the chapter, so "
            "a শব্দার্থ item on them would take its answer from outside the chapter (§4, REF-09 "
            "§5); they are used at S03 instead, where the STUDENT supplies the sentence. (2) Of "
            "those four, 'দুধভরা ওই চাঁদের বাটি' is authored once, as the S07 অনুশীলনী ৪ঙ item, "
            "not twice. Net: S02 = 3, and Remember = 3 (S02) + 1 (S01) + 1 (S07 ৪ক, literal "
            "recall labelled honestly) = 5 = 20.8% — inside the floor, not 40% over the ceiling."),
        "gaps": [
            "S04 শূন্যস্থান · S05 বহুনির্বাচনি · S06 বিপরীত শব্দ · S11 বিরামচিহ্ন · S12 যুক্তবর্ণ · "
            "S13 এক কথায় প্রকাশ · S14 আবেদনপত্র · S15 রচনা — NOT served. পাঠ ১৩'s own "
            "'কোন প্রশ্নে কাজে লাগবে' line names seven slots and these are not among them; the "
            "chapter carries no material for them. Recorded as a gap, not filled (§4, §7).",
            "S02 শব্দার্থ is under-served relative to what a শব্দার্থ slot could take: 3 items "
            "against অনুশীলনী ১'s five words plus the four glossed ones. See remember_cap — the "
            "limit is the Bloom band and the absence of keys in the chapter, not the wave size.",
            "S10 is authored as ভাব নির্ণয়, NOT পদ নির্ণয়. MarkLogic_BAN_Spine.md's BAN-S10 C5 "
            "row reads পদ নির্ণয় (D0); this chapter's own line authorises ভাব নির্ণয় as its "
            "alternative and পাঠ ১৩ carries no পদ material. The per-item mark is 1 either way, so "
            "no mark is inferred. RAISED, not settled."
        ],
    },
    "flags": [],
    "pool_index": POOL_INDEX,
    "slot_index": SLOT,
    "source_index": ANCHOR,
    "questions": QUESTIONS,
}

# CD-055 / SOURCE_POLICY §7.9. `--wip` writes the bank still carrying the marker, which is the
# state it is in between Step 2 and Step 3. Removing the marker is part of FINISHING, so it is a
# flag on the build rather than a hand-edit of the artifact — the two states are re-derivable.
WIP_LINE = (
    "নির্মাণাধীন — all 24 items and their carriers are drafted; the gate suite has NOT yet been "
    "run against them and the Subject Lead has not read them. Resume at Step 3 of the wave-1 "
    "brief: build the envelopes, run gates.py and validate_import.py L1–L4, then rebuild without "
    "`--wip` to drop this line.")

if __name__ == "__main__":
    import sys
    assert len(QUESTIONS) == 24, f"target is 24; built {len(QUESTIONS)}"
    if "--wip" in sys.argv:
        BANK["header"]["অবস্থা"] = WIP_LINE
    OUT.write_text(json.dumps(BANK, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {len(QUESTIONS)} items to {OUT.relative_to(ROOT)}"
          + ("  [নির্মাণাধীন]" if "--wip" in sys.argv else "  [complete]"))
