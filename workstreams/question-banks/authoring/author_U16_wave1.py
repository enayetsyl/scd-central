#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""author_U16_wave1.py — C5 Bangla, পাঠ ১৬ (স্মরণীয় যাঁরা বরণীয় যাঁরা) question bank, wave 1.

Run from the repo root:
    python workstreams/question-banks/authoring/author_U16_wave1.py

WHY THE SCRIPT IS THE ARTIFACT (LOCAL.md, "Artifacts & naming"). A 96-item JSON nobody can
re-derive is not reviewable; this file is what makes the bank reproducible and reviewable AS
CONTENT. It is promoted with its bank.

THE CHAPTER IS গদ্য (ইতিহাস), AND THAT IS THE FACT TWO EXCLUSIONS TURN ON.
`canon/marklogic/C5_Bangla_Source_13-23.md`'s এক নজরে table gives পাঠ ১৬'s ধরন as গদ্য (ইতিহাস),
and the same file names which chapters source S01 and S09: "কবিতা চারটি: পাঠ ১৩, ১৫, ১৮, ২০ —
এগুলোই S01 (কবিতা মুখস্থ) ও S09 (মূলভাব) প্রশ্নের উৎস।" পাঠ ১৬ is NOT among them, so both slots
are EXCLUDED on the source's own words — the same sentence that took them from পাঠ ১৪ and gave
them to পাঠ ১৫. The verdict is read off the source, never inferred from content (CD-138(e)
forbids the inference in both directions).

S14/S15 ARE NOT DECLARED AT ALL, AND THAT IS THE CORRECT SHAPE. CD-147 makes আবেদনপত্র and রচনা
paper-level for EVERY chapter, categorically; a chapter owes no content reason for a slot no
chapter may serve, and a bank that says nothing about them is CORRECT, not INCOMPLETE (CD-147(c)).

THE ⚠ BLOCK ON THIS CHAPTER IS THE HEAVIEST IN THE SOURCE AND EVERY CLAUSE OF IT BINDS HERE.
  · "শহিদ" — the source requires questions about ব্যক্তিদের ঘটনা ও অবদান and forbids the
    definitional "শহিদ কারা" form. NO item below asks what the word means, who counts as one, or
    invites a student to apply it. It appears only inside two proper names the book itself prints:
    শহিদ সাবের (a person) and 'শহিদ বুদ্ধিজীবী দিবস' (the day). Everywhere else this bank writes
    প্রাণ দেন · প্রাণ হারান · হত্যা করা হয় · বুদ্ধিজীবী.
  · C-03 — the গান ও সুরকার paragraph is barred. It is not in the extraction at all, so no anchor
    can reach it and nothing is authored from it.
  · C-18 — no item touches শহিদ মিনারে ফুল দেওয়া or any ritual of homage. REF-01 §4.1 C-18's own
    carve-out is what this bank uses: the factual history — dates, events, contributions.
  · C-05 — no item carries or asks for a picture of any person.

NO INVENTED PERSONAL NAME APPEARS ANYWHERE. The only personal names are the historical figures the
chapter itself records; they are content facts, not characters, so QB-CR-005's REF-2 substitution
rule (which is about characters standing in an exercise) is not in play and no REF-2 name is
needed. Every S03 model sentence is written without a personal name for the same reason.
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[3]
EXTRACTION = "canon/marklogic/C5_Bangla_Source_13-23.md"
OUT = ROOT / "workstreams/question-banks/banks/C5_BAN_U16_QuestionBank_v1.json"
CHAPTER = "পাঠ ১৬ — স্মরণীয় যাঁরা বরণীয় যাঁরা"

# topic_tag / ref19_topic_id pairs. TOPIC_NUMBERS.md gives পাঠ ১৬ (গদ্য ইতিহাস/জীবনী) the primary
# number -14 / BAN-BIOGRAPHY, minted 2026-08-14. The cross-cutting strands are per-QUESTION and
# not per-chapter, which is why five other pairs appear below.
BIO = ("TOP-BAN-C5-14", "BAN-BIOGRAPHY")
VOCAB = ("TOP-BAN-C5-01", "BAN-VOCAB")
WORDREL = ("TOP-BAN-C5-01", "BAN-WORDREL")
JUKTO = ("TOP-BAN-C5-01", "BAN-JUKTOBARNA")
PARTSP = ("TOP-BAN-C5-01", "BAN-PARTSPEECH")
SENT = ("TOP-BAN-C5-02", "BAN-SENTENCE")
PUNCT = ("TOP-BAN-C5-13", "BAN-SENTENCE")

# The teacher-gloss provenance line (CD-136(b)). P-037 admits it on `short_answer` and
# `descriptive` only, and every item that carries it below is `short_answer`.
TEACHER_KEY = ("এই উত্তরকুঞ্জি শিক্ষকের দেওয়া — বাংলা ভাষার সাধারণ তথ্য, পাঠে এর উত্তর দেওয়া নেই "
               "(CD-136)। উদ্দীপক পাঠ ১৬ থেকেই নেওয়া। কাছাকাছি অর্থের যেকোনো শুদ্ধ উত্তর গ্রহণযোগ্য।")

PADA_KEY = (TEACHER_KEY + " পদ নির্ণয় C5-এর BAN-S10 স্লটে নির্বাচিত কাজ — ভাষারীতি পরিবর্তন ও "
            "ক্রিয়ার কাল এই স্লটে স্বীকৃত হলেও পঞ্চম শ্রেণিতে নির্বাচিত নয়, যদিও এই পাঠের "
            "অনুশীলনী ৫ ক্রিয়ার রূপের উৎস।")

JUKTO_KEY = (TEACHER_KEY + " দুটি কাজই করতে হবে — শুধু ভাঙলে বা শুধু শব্দ গঠন করলে অর্ধেক কাজ "
             "(SLOT_REGISTER BAN-S12 composite)।")

ITEMS = []


def add(slot, task, topic, text, qtype, role, bloom, diff, marks, anchor, **kw):
    ITEMS.append(dict(slot=slot, task=task, topic=topic[0], slug=topic[1], text=text,
                      qtype=qtype, role=role, bloom=bloom, diff=diff, marks=marks,
                      anchor=anchor, extra=kw))


def sa(accepted, note=None):
    k = {"accepted": accepted}
    if note:
        k["model_note"] = note
    return {"answer_key": k}


def rubric(criterion, full, partial):
    return {"rubric": {"bands": ["সম্পূর্ণ", "আংশিক"],
                       "criteria": [{"role": "islamic_alignment", "criterion": criterion,
                                     "band_descriptors": {"সম্পূর্ণ": full, "আংশিক": partial}}]}}


# Anchors — every one verified against the extraction by `selfcheck()` before the file is written.
A_ALL = "বাংলাদেশের স্বাধীনতার জন্য লক্ষ লক্ষ মানুষ প্রাণ দিয়েছেন"
A_ALL2 = "কৃষক, শ্রমিক, ছাত্র, শিক্ষক, রাজনীতিবিদ, পুলিশ, সৈনিক, নারী, শিশুসহ সর্বস্তরের মানুষ"
A_MARCH = "১৯৭১ সালের ২৫শে মার্চ গভীর রাতে পাকিস্তানি সেনারা ঢাকার নিরস্ত্র ও ঘুমন্ত মানুষের ওপর ঝাঁপিয়ে পড়ে"
A_ATTACK = "আক্রমণ চালায় ঢাকা বিশ্ববিদ্যালয়ের ছাত্রাবাসে, পুলিশ ব্যারাকে ও আবাসিক এলাকায়"
A_NINE = "নয় মাস ধরে হত্যাকাণ্ড চলে"
A_MID = "২৫শে মার্চের মধ্যরাতেই শহিদ হন"
A_MUNIR = "বিজ্ঞানের শিক্ষক; গোলাগুলির শব্দ শুনে পবিত্র কুরআন পড়া শুরু করেন"
A_PAPER = "সংবাদপত্র অফিসেও আক্রমণ"
A_DHIREN = "ধীরেন্দ্রনাথ দত্ত — বয়স ৮৫"
A_BHASHA = "১৯৪৮ সালে পাকিস্তান গণপরিষদে তিনিই প্রথম বাংলা ভাষাকে রাষ্ট্রভাষা করার দাবি তোলেন"
A_JOGESH = "যোগেশচন্দ্র ঘোষ — সাধনা ঔষধালয়ের প্রতিষ্ঠাতা, বয়স ৮৪"
A_RANADA = "রণদাপ্রসাদ সাহা — দানশীলতার জন্য লোকে ডাকত"
A_NUTAN = "নূতনচন্দ্র সিংহ — চট্টগ্রামের বিখ্যাত সমাজসেবক"
A_DEC = "১৯৭১ সালের ১৪ই ডিসেম্বর নতুন করে হত্যাযজ্ঞ শুরু"
A_DEC_PROF = "ধরে নিয়ে যাওয়া হয় অধ্যাপক"
A_DEC_JOUR = "সাংবাদিক সিরাজুদ্দীন হোসেন, লেখক শহীদুল্লা কায়সার"
A_BADHYA = "দেশ স্বাধীন হওয়ার পর অনেকের লাশ পাওয়া যায়"
A_DIBAS = "প্রতিবছর ১৪ই ডিসেম্বর পালিত হয়"

A_ABADHARITA = "অবধারিত — ঘটবেই এমন"
A_ABARUDDHA = "অবরুদ্ধ — বন্দি; আটক"
A_ATMA = "আত্মদানকারী — অন্যের উপকারের জন্য নিজের জীবন দান করেন যিনি"
A_KHYATA = "খ্যাতনামা — বিখ্যাত · নির্বিচারে — বাছবিচার না করে"
A_NIRBICHARE = "নির্বিচারে — বাছবিচার না করে"
A_PASHANDA = "পাষণ্ড — নিষ্ঠুর; নির্মম ব্যক্তি"
A_BARENYA = "বরেণ্য — বরণ করার যোগ্য"
A_MANASWI = "বরেণ্য — বরণ করার যোগ্য · মনস্বী — জ্ঞানী"

A_EX3 = "মিলকরণ — বরেণ্য · মেধাবী · নিরহংকার · নির্বিচার · অপূরণীয়"
A_EX6 = "দিয়ে বাক্য সম্পূর্ণ করা"


# =====================================================================================
# S02 · শব্দার্থ · simple · 5 owed · 8 authored · marks 1 · all Remember, easy
# The eight words are exactly the chapter's own অর্থ জেনে নিই list, so the key is IN the chapter
# and NO teacher-key note is carried — CD-136 is not in play for these.
# =====================================================================================
S02 = [
    ("অবধারিত", ["ঘটবেই এমন", "যা ঘটবেই"], A_ABADHARITA),
    ("অবরুদ্ধ", ["বন্দি", "আটক", "বন্দি; আটক"], A_ABARUDDHA),
    ("আত্মদানকারী", ["অন্যের উপকারের জন্য নিজের জীবন দান করেন যিনি"], A_ATMA),
    ("খ্যাতনামা", ["বিখ্যাত"], A_KHYATA),
    ("নির্বিচারে", ["বাছবিচার না করে"], A_NIRBICHARE),
    ("পাষণ্ড", ["নিষ্ঠুর", "নির্মম ব্যক্তি", "নিষ্ঠুর; নির্মম ব্যক্তি"], A_PASHANDA),
    ("বরেণ্য", ["বরণ করার যোগ্য"], A_BARENYA),
    ("মনস্বী", ["জ্ঞানী"], A_MANASWI),
]
for w, acc, anc in S02:
    add("S02", "মূল কাঠামো", VOCAB,
        f"পাঠে ব্যবহৃত '{w}' শব্দের অর্থ লেখো।",
        "short_answer", "short", "Remember", "easy", 1, anc, **sa(acc))


# =====================================================================================
# S03 · বাক্য গঠন · simple · 5 owed · 14 authored · marks 1 · all Apply, medium
# BAN-S03-NOJOIN is honoured: not one of these is joined to a যুক্তবর্ণ or কারচিহ্ন task.
# Fourteen is what carries the Apply floor with margin once S11 and S12 are counted.
# NO MODEL SENTENCE CARRIES A PERSONAL NAME — see the module docstring.
# =====================================================================================
S03 = [
    ("অবধারিত", "পরিশ্রম করলে সাফল্য অবধারিত।", A_ABADHARITA),
    ("অবরুদ্ধ", "ভারী বৃষ্টিতে পুরো এলাকা অবরুদ্ধ হয়ে পড়ল।", A_ABARUDDHA),
    ("খ্যাতনামা", "আমাদের দেশে অনেক খ্যাতনামা বিজ্ঞানী জন্মেছেন।", A_KHYATA),
    ("নির্বিচারে", "নির্বিচারে গাছ কাটলে পরিবেশের ক্ষতি হয়।", A_NIRBICHARE),
    ("বরেণ্য", "বরেণ্য মানুষদের জীবনী পড়লে অনেক কিছু শেখা যায়।", A_BARENYA),
    ("মনস্বী", "মনস্বী মানুষ অল্প কথায় গভীর কথা বলেন।", A_MANASWI),
    ("স্বাধীনতা", "স্বাধীনতার মূল্য অনেক বড়ো।", A_ALL),
    ("শিক্ষক", "শিক্ষক আমাদের সঠিক পথ চিনিয়ে দেন।", A_ALL2),
    ("বিশ্ববিদ্যালয়", "বড়ো ভাই বিশ্ববিদ্যালয়ে পড়াশোনা করেন।", A_ATTACK),
    ("সংবাদপত্র", "প্রতিদিন সকালে সংবাদপত্র পড়া ভালো অভ্যাস।", A_PAPER),
    ("প্রতিষ্ঠাতা", "এই বিদ্যালয়ের প্রতিষ্ঠাতা ছিলেন একজন শিক্ষানুরাগী।", A_JOGESH),
    ("সমাজসেবক", "একজন সমাজসেবক নিজের সুখের আগে অন্যের কথা ভাবেন।", A_NUTAN),
    ("দাবি", "ন্যায্য দাবি সবসময় ভদ্রভাবে জানাতে হয়।", A_BHASHA),
    ("তবু", "অনেক কষ্ট হয়েছিল, তবু সে হাল ছাড়েনি।", A_EX6),
]
for w, model, anc in S03:
    add("S03", "মূল কাঠামো", SENT,
        f"'{w}' শব্দটি দিয়ে একটি অর্থপূর্ণ বাক্য লেখো।",
        "short_answer", "short", "Apply", "medium", 1, anc,
        **sa([model], "শিক্ষার্থীর নিজের যেকোনো শুদ্ধ বাক্য গ্রহণযোগ্য, যদি শব্দটি সঠিক অর্থে "
             "ব্যবহৃত হয় এবং বাক্যটি বিরামচিহ্নসহ সম্পূর্ণ হয়। নমুনা উত্তর দেওয়া হলো।"))


# =====================================================================================
# S04 · শূন্যস্থান পূরণ · simple · 5 owed · 7 authored · marks 1 · all Remember, easy
# Five frames are the chapter's own sentences with one word cut. Two use অনুশীলনী ১'s words in
# authored frames — that exercise IS this slot's task and its six words are the chapter's own,
# but the textbook's frames are not in the extraction, so the frames are written here.
# =====================================================================================
S04 = [
    ("'১৯৭১ সালের ______ গভীর রাতে পাকিস্তানি সেনারা ঢাকার নিরস্ত্র ও ঘুমন্ত মানুষের ওপর "
     "ঝাঁপিয়ে পড়ে।' — শূন্যস্থান পূরণ করো।", ["২৫শে মার্চ"], A_MARCH),
    ("'নয় মাস ধরে ______ চলে।' — শূন্যস্থান পূরণ করো।", ["হত্যাকাণ্ড"], A_NINE),
    ("'১৯৪৮ সালে পাকিস্তান গণপরিষদে প্রথম বাংলা ভাষাকে ______ করার দাবি তোলা হয়।' — "
     "শূন্যস্থান পূরণ করো।", ["রাষ্ট্রভাষা"], A_BHASHA),
    ("'যোগেশচন্দ্র ঘোষ ছিলেন সাধনা ঔষধালয়ের ______।' — শূন্যস্থান পূরণ করো।",
     ["প্রতিষ্ঠাতা"], A_JOGESH),
    ("'নূতনচন্দ্র সিংহ ছিলেন চট্টগ্রামের বিখ্যাত ______।' — শূন্যস্থান পূরণ করো।",
     ["সমাজসেবক"], A_NUTAN),
    ("'সেদিন ______ মানুষ হত্যা করা হয়েছিল — কোনো বাছবিচার করা হয়নি।' — শূন্যস্থান পূরণ করো।",
     ["নির্বিচারে"], A_NIRBICHARE),
    ("'নয় মাস ধরে সারা দেশ ছিল ______ — মানুষ নিশ্চিন্তে ঘর থেকে বেরোতে পারত না।' — "
     "শূন্যস্থান পূরণ করো।", ["অবরুদ্ধ"], A_ABARUDDHA),
]
for text, acc, anc in S04:
    add("S04", "মূল কাঠামো", BIO, text, "fill_blank", "short", "Remember", "easy", 1, anc,
        blanks=[{"blank_no": 1, "accepted": acc}])


# =====================================================================================
# S05 · বহুনির্বাচনি · simple · 5 owed · 9 authored · marks 1 · 3 Remember + 6 Understand
# Exactly one correct option each; every distractor carries a why_wrong drawn from the chapter.
# BLOOM IS TAGGED FROM DEMAND, NOT FROM THE SLOT (QB-CR-011/QB-CR-012). The three `Remember`
# items ask back a fact printed in মূল তথ্য; the six `Understand` ones require reading a
# contribution, a phrase or a pattern and saying what it means. The spine itself says
# বহুনির্বাচনি is a method of answering and not a skill, so the slot fixes no level.
# NO ITEM ASKS WHAT 'শহিদ' MEANS OR WHO COUNTS AS ONE — the source's ⚠ forbids that form.
# =====================================================================================
add("S05", "মূল কাঠামো", BIO, "পাকিস্তানি সেনারা কোন রাতে ঢাকার ঘুমন্ত মানুষের ওপর ঝাঁপিয়ে পড়ে?",
    "mcq", "mcq", "Remember", "easy", 1, A_MARCH,
    options=[
        {"option_id": "ক", "text": "১৯৭১ সালের ২৫শে মার্চ", "is_correct": True},
        {"option_id": "খ", "text": "১৯৭১ সালের ১৪ই ডিসেম্বর", "is_correct": False,
         "why_wrong": "১৪ই ডিসেম্বর নতুন করে হত্যাযজ্ঞ শুরু হয়, ঘুমন্ত মানুষের ওপর প্রথম আক্রমণ নয়।"},
        {"option_id": "গ", "text": "১৯৪৮ সালের ২৫শে মার্চ", "is_correct": False,
         "why_wrong": "১৯৪৮ সাল পাঠে এসেছে ভাষার দাবির প্রসঙ্গে, আক্রমণের প্রসঙ্গে নয়।"},
        {"option_id": "ঘ", "text": "১৯৭১ সালের ১৬ই ডিসেম্বর", "is_correct": False,
         "why_wrong": "এই তারিখটি পাঠে নেই।"}])

add("S05", "মূল কাঠামো", BIO, "'শহিদ বুদ্ধিজীবী দিবস' প্রতিবছর কোন তারিখে পালিত হয়?",
    "mcq", "mcq", "Remember", "easy", 1, A_DIBAS,
    options=[
        {"option_id": "ক", "text": "১৪ই ডিসেম্বর", "is_correct": True},
        {"option_id": "খ", "text": "২৫শে মার্চ", "is_correct": False,
         "why_wrong": "২৫শে মার্চ রাতের আক্রমণের তারিখ; দিবসটির তারিখ আলাদা।"},
        {"option_id": "গ", "text": "একুশে ফেব্রুয়ারি", "is_correct": False,
         "why_wrong": "এই তারিখটি পাঠে নেই।"},
        {"option_id": "ঘ", "text": "ছাব্বিশে মার্চ", "is_correct": False,
         "why_wrong": "এই তারিখটি পাঠে নেই।"}])

add("S05", "মূল কাঠামো", BIO, "সাধনা ঔষধালয়ের প্রতিষ্ঠাতা কে ছিলেন?",
    "mcq", "mcq", "Remember", "easy", 1, A_JOGESH,
    options=[
        {"option_id": "ক", "text": "যোগেশচন্দ্র ঘোষ", "is_correct": True},
        {"option_id": "খ", "text": "রণদাপ্রসাদ সাহা", "is_correct": False,
         "why_wrong": "রণদাপ্রসাদ সাহাকে দানশীলতার জন্য 'দানবীর' বলা হতো।"},
        {"option_id": "গ", "text": "নূতনচন্দ্র সিংহ", "is_correct": False,
         "why_wrong": "নূতনচন্দ্র সিংহ ছিলেন চট্টগ্রামের বিখ্যাত সমাজসেবক।"},
        {"option_id": "ঘ", "text": "ধীরেন্দ্রনাথ দত্ত", "is_correct": False,
         "why_wrong": "ধীরেন্দ্রনাথ দত্তের পরিচয় পাঠে ভাষার দাবির সঙ্গে যুক্ত।"}])

add("S05", "মূল কাঠামো", BIO, "লোকে কাকে 'দানবীর' বলে ডাকত এবং কেন?",
    "mcq", "mcq", "Understand", "medium", 1, A_RANADA,
    options=[
        {"option_id": "ক", "text": "রণদাপ্রসাদ সাহাকে — তাঁর দানশীলতার জন্য", "is_correct": True},
        {"option_id": "খ", "text": "যোগেশচন্দ্র ঘোষকে — তাঁর ঔষধালয়ের জন্য", "is_correct": False,
         "why_wrong": "ঔষধালয় প্রতিষ্ঠার কথা ঠিক, কিন্তু 'দানবীর' নামটি তাঁর নয়।"},
        {"option_id": "গ", "text": "নূতনচন্দ্র সিংহকে — তাঁর সমাজসেবার জন্য", "is_correct": False,
         "why_wrong": "সমাজসেবার পরিচয় ঠিক, কিন্তু পাঠে 'দানবীর' নামটি তাঁকে দেওয়া হয়নি।"},
        {"option_id": "ঘ", "text": "ধীরেন্দ্রনাথ দত্তকে — তাঁর ভাষার দাবির জন্য", "is_correct": False,
         "why_wrong": "ভাষার দাবি তাঁর অবদান; 'দানবীর' নামের সঙ্গে তার সম্পর্ক নেই।"}])

add("S05", "মূল কাঠামো", BIO,
    "ধীরেন্দ্রনাথ দত্তকে বাংলা ভাষার ইতিহাসে বিশেষভাবে মনে রাখা হয় কেন?",
    "mcq", "mcq", "Understand", "medium", 1, A_BHASHA,
    options=[
        {"option_id": "ক", "text": "পাকিস্তান গণপরিষদে তিনিই প্রথম বাংলাকে রাষ্ট্রভাষা করার দাবি তোলেন",
         "is_correct": True},
        {"option_id": "খ", "text": "তিনি সাধনা ঔষধালয় প্রতিষ্ঠা করেন", "is_correct": False,
         "why_wrong": "ঔষধালয়টি প্রতিষ্ঠা করেন যোগেশচন্দ্র ঘোষ।"},
        {"option_id": "গ", "text": "তিনি চট্টগ্রামের সমাজসেবক ছিলেন", "is_correct": False,
         "why_wrong": "চট্টগ্রামের সমাজসেবক ছিলেন নূতনচন্দ্র সিংহ।"},
        {"option_id": "ঘ", "text": "তিনি একজন সাংবাদিক ছিলেন", "is_correct": False,
         "why_wrong": "পাঠে তাঁর পরিচয় সাংবাদিক হিসেবে দেওয়া হয়নি।"}])

add("S05", "মূল কাঠামো", VOCAB,
    "পাঠে ঢাকার মানুষকে 'নিরস্ত্র' বলা হয়েছে — এতে কী বোঝানো হয়েছে?",
    "mcq", "mcq", "Understand", "medium", 1, A_MARCH,
    options=[
        {"option_id": "ক", "text": "তাঁদের হাতে কোনো অস্ত্র ছিল না", "is_correct": True},
        {"option_id": "খ", "text": "তাঁরা সংখ্যায় কম ছিলেন", "is_correct": False,
         "why_wrong": "সংখ্যার কথা এখানে বলা হয়নি; কথাটি অস্ত্র নিয়ে।"},
        {"option_id": "গ", "text": "তাঁরা প্রশিক্ষিত ছিলেন না", "is_correct": False,
         "why_wrong": "প্রশিক্ষণের কথা পাঠে নেই।"},
        {"option_id": "ঘ", "text": "তাঁরা ঘুমিয়ে ছিলেন", "is_correct": False,
         "why_wrong": "ঘুমন্ত থাকার কথা আলাদা করে বলা আছে; 'নিরস্ত্র' তার অর্থ নয়।"}])

add("S05", "মূল কাঠামো", BIO,
    "পাঠে বলা হয়েছে প্রাণ দিয়েছেন 'সর্বস্তরের মানুষ' — এই কথায় কী বোঝানো হয়েছে?",
    "mcq", "mcq", "Understand", "medium", 1, A_ALL2,
    options=[
        {"option_id": "ক", "text": "কৃষক-শ্রমিক থেকে শিক্ষক-ছাত্র পর্যন্ত সব শ্রেণি-পেশার মানুষ",
         "is_correct": True},
        {"option_id": "খ", "text": "কেবল সৈনিক ও পুলিশ", "is_correct": False,
         "why_wrong": "সৈনিক ও পুলিশ তালিকার অংশ মাত্র, পুরো তালিকা নয়।"},
        {"option_id": "গ", "text": "কেবল ঢাকা শহরের মানুষ", "is_correct": False,
         "why_wrong": "কথাটি স্তরের, এলাকার নয়।"},
        {"option_id": "ঘ", "text": "কেবল শিক্ষক ও ছাত্র", "is_correct": False,
         "why_wrong": "তালিকায় কৃষক, শ্রমিক, নারী ও শিশুর কথাও আছে।"}])

add("S05", "মূল কাঠামো", BIO,
    "মিরপুর ও রায়ের বাজারের বধ্যভূমির কথা পাঠে কেন এসেছে?",
    "mcq", "mcq", "Understand", "medium", 1, A_BADHYA,
    options=[
        {"option_id": "ক", "text": "দেশ স্বাধীন হওয়ার পর সেখানে অনেকের লাশ পাওয়া যায়",
         "is_correct": True},
        {"option_id": "খ", "text": "সেখানে ২৫শে মার্চের আক্রমণ শুরু হয়", "is_correct": False,
         "why_wrong": "আক্রমণ শুরু হয় ছাত্রাবাস, পুলিশ ব্যারাক ও আবাসিক এলাকায়।"},
        {"option_id": "গ", "text": "সেখানে সাধনা ঔষধালয় ছিল", "is_correct": False,
         "why_wrong": "ঔষধালয়ের অবস্থান পাঠে বলা হয়নি।"},
        {"option_id": "ঘ", "text": "সেখানে ভাষার দাবি তোলা হয়", "is_correct": False,
         "why_wrong": "ভাষার দাবি তোলা হয় পাকিস্তান গণপরিষদে।"}])

add("S05", "মূল কাঠামো", BIO,
    "২৫শে মার্চ রাতে যেসব জায়গায় আক্রমণ চালানো হয়, সেগুলো সম্পর্কে কোন কথাটি ঠিক?",
    "mcq", "mcq", "Understand", "medium", 1, A_ATTACK,
    options=[
        {"option_id": "ক", "text": "তিনটিই ঢাকার ভেতরের জায়গা, কোনোটিই যুদ্ধক্ষেত্র নয়",
         "is_correct": True},
        {"option_id": "খ", "text": "সবই ছিল যুদ্ধক্ষেত্র", "is_correct": False,
         "why_wrong": "পাঠে নাম করা জায়গাগুলো যুদ্ধক্ষেত্র নয়, মানুষের বসবাস ও পড়ার জায়গা।"},
        {"option_id": "গ", "text": "সবই ছিল শহরের বাইরে", "is_correct": False,
         "why_wrong": "জায়গাগুলো ঢাকার ভেতরেই।"},
        {"option_id": "ঘ", "text": "কেবল বিশ্ববিদ্যালয়ে আক্রমণ হয়", "is_correct": False,
         "why_wrong": "পুলিশ ব্যারাক ও আবাসিক এলাকার কথাও পাঠে আছে।"}])


# =====================================================================================
# S06 · বিপরীত শব্দ · alternative, C5 SELECTED = বিপরীত শব্দ · 5 owed · 6 authored
# marks 1 · all Remember, easy · teacher-supplied key (CD-136(b)), declared per item.
# The stimulus words are the chapter's own; the answers are general Bengali and are not in it.
# =====================================================================================
S06 = [
    ("স্বাধীনতা", ["পরাধীনতা"], A_ALL),
    ("নিরস্ত্র", ["সশস্ত্র"], A_MARCH),
    ("অবরুদ্ধ", ["মুক্ত", "স্বাধীন"], A_ABARUDDHA),
    ("খ্যাতনামা", ["অখ্যাত", "অজ্ঞাত"], A_KHYATA),
    ("নিষ্ঠুর", ["দয়ালু", "সদয়"], A_PASHANDA),
    ("প্রথম", ["শেষ"], A_BHASHA),
]
for w, acc, anc in S06:
    add("S06", "বিপরীত শব্দ", WORDREL,
        f"পাঠে ব্যবহৃত '{w}' শব্দের বিপরীত শব্দ লেখো।",
        "short_answer", "short", "Remember", "easy", 1, anc, **sa(acc, TEACHER_KEY))


# =====================================================================================
# S07 · সংক্ষিপ্ত উত্তর · simple · 4 owed · 16 authored · marks 2
# 10 Understand (3 easy, 7 medium) + 6 Analyze (hard). The first seven follow অনুশীলনী ২'s own
# seven prompts — ২৫শে মার্চের ঘটনা · ভাষা দাবি · শহিদ সাবের · রণদাপ্রসাদ সাহা · দুজন সাংবাদিক ·
# কেন স্মরণ করব · ১৪ই ডিসেম্বর — recast so that every one asks about an EVENT or a CONTRIBUTION,
# which is the form the chapter's ⚠ block requires.
# =====================================================================================
S07 = [
    ("১৯৭১ সালের ২৫শে মার্চ রাতে ঢাকায় কী ঘটেছিল, সংক্ষেপে লেখো।",
     ["গভীর রাতে পাকিস্তানি সেনারা ঢাকার নিরস্ত্র ও ঘুমন্ত মানুষের ওপর ঝাঁপিয়ে পড়ে। "
      "ঢাকা বিশ্ববিদ্যালয়ের ছাত্রাবাস, পুলিশ ব্যারাক ও আবাসিক এলাকায় আক্রমণ চালানো হয়।"],
     "Understand", "easy", A_MARCH),
    ("বাংলা ভাষাকে রাষ্ট্রভাষা করার দাবি প্রথম কে, কোথায় ও কবে তুলেছিলেন?",
     ["ধীরেন্দ্রনাথ দত্ত, পাকিস্তান গণপরিষদে, ১৯৪৮ সালে।"],
     "Understand", "easy", A_BHASHA),
    ("সংবাদপত্র অফিসে আক্রমণের সময় কারা প্রাণ হারান?",
     ["শহিদ সাবের, সেলিনা পারভীন এবং কবি ও সাংবাদিক মেহেরুন্নেসা।"],
     "Understand", "easy", A_PAPER),
    ("রণদাপ্রসাদ সাহার পরিচয় সংক্ষেপে লেখো।",
     ["দানশীলতার জন্য লোকে তাঁকে 'দানবীর' বলে ডাকত। পাঠে তাঁকে সেই সব বরেণ্য মানুষের একজন হিসেবে স্মরণ করা হয়েছে, যাঁদের ১৯৭১ সালে হারাতে হয়।"],
     "Understand", "medium", A_RANADA),
    ("১৯৭১ সালে প্রাণ হারানো দুজন সাংবাদিকের নাম ও পরিচয় লেখো।",
     ["মেহেরুন্নেসা — কবি ও সাংবাদিক, মাত্র পঁচিশ বছর বয়সে প্রাণ হারান; সিরাজুদ্দীন হোসেন — "
      "সাংবাদিক, ১৪ই ডিসেম্বর যাঁদের ধরে নিয়ে যাওয়া হয় তাঁদের একজন।"],
     "Understand", "medium", A_DEC_JOUR),
    ("দেশের জন্য যাঁরা প্রাণ দিয়েছেন তাঁদের আমরা কেন স্মরণ করব?",
     ["তাঁদের আত্মদানেই দেশ স্বাধীন হয়েছে। তাঁদের কাজ ও অবদান জানলে আমরাও দায়িত্ববান হতে "
      "শিখি, আর তাঁদের রেখে যাওয়া কাজ এগিয়ে নিতে পারি।"],
     "Understand", "medium", A_ALL),
    ("১৯৭১ সালের ১৪ই ডিসেম্বর কী ঘটেছিল?",
     ["নতুন করে হত্যাযজ্ঞ শুরু হয় — অধ্যাপক, সাংবাদিক, লেখক ও চিকিৎসকদের বাড়ি থেকে ধরে "
      "নিয়ে যাওয়া হয়। এই দিনটি স্মরণে প্রতিবছর 'শহিদ বুদ্ধিজীবী দিবস' পালিত হয়।"],
     "Understand", "medium", A_DEC),
    ("এম. মুনিরুজ্জামান সম্পর্কে পাঠে কী বলা হয়েছে?",
     ["তিনি ছিলেন বিজ্ঞানের শিক্ষক। গোলাগুলির শব্দ শুনে তিনি পবিত্র কুরআন পড়া শুরু করেন, "
      "সেই অবস্থাতেই তাঁকে টেনেহিঁচড়ে নামানো হয়।"],
     "Understand", "medium", A_MUNIR),
    ("যোগেশচন্দ্র ঘোষ ও নূতনচন্দ্র সিংহের পরিচয় লেখো।",
     ["যোগেশচন্দ্র ঘোষ ছিলেন সাধনা ঔষধালয়ের প্রতিষ্ঠাতা, বয়স ছিল চুরাশি। নূতনচন্দ্র সিংহ "
      "ছিলেন চট্টগ্রামের বিখ্যাত সমাজসেবক।"],
     "Understand", "medium", A_JOGESH),
    ("দেশ স্বাধীন হওয়ার পর মিরপুর ও রায়ের বাজারে কী পাওয়া যায়?",
     ["ওই দুই জায়গার বধ্যভূমিতে অনেকের লাশ পাওয়া যায়।"],
     "Understand", "medium", A_BADHYA),
    ("পাঠে প্রাণ-দেওয়া মানুষের যে তালিকা আছে — কৃষক, শ্রমিক, ছাত্র, শিক্ষক, নারী, শিশু — "
     "এই তালিকা থেকে সেই সময় সম্পর্কে কী বোঝা যায়?",
     ["তালিকাটি দেখায় ক্ষতি কোনো একটি শ্রেণির ছিল না — কৃষক ও শ্রমিক থেকে ছাত্র, শিক্ষক ও "
      "রাজনীতিবিদ, পুলিশ ও সৈনিক, এমনকি নারী ও শিশু পর্যন্ত সবাই এর মধ্যে পড়েছিলেন। "
      "অর্থাৎ সব স্তরের মানুষকেই মূল্য দিতে হয়েছে।"],
     "Analyze", "hard", A_ALL2),
    ("২৫শে মার্চ রাতে বেছে নেওয়া জায়গাগুলো — ছাত্রাবাস, পুলিশ ব্যারাক, আবাসিক এলাকা — "
     "বিশ্লেষণ করে দেখাও আক্রমণটি কাদের ওপর ছিল।",
     ["তিনটিই ঢাকার ভেতরের জায়গা — পড়ার, কাজের ও বসবাসের — কোনোটিই যুদ্ধক্ষেত্র নয়। "
      "উৎস বলছে আক্রমণ চলেছে নিরস্ত্র ও ঘুমন্ত মানুষের ওপর, কোনো লড়াইয়ের ময়দানে নয়।"],
     "Analyze", "hard", A_ATTACK),
    ("১৪ই ডিসেম্বর যাঁদের ধরে নিয়ে যাওয়া হয়, তাঁদের পেশার তালিকা দেখে কী বোঝা যায়?",
     ["তালিকায় আছেন অধ্যাপক, সাংবাদিক, লেখক ও চিকিৎসক — অর্থাৎ দেশের জ্ঞান, চিকিৎসা ও "
      "লেখালেখির কাজ যাঁরা এগিয়ে নিতেন। বেছে বেছে তাঁদেরই ধরে নেওয়া হয়েছিল।"],
     "Analyze", "hard", A_DEC_PROF),
    ("ধীরেন্দ্রনাথ দত্তের ১৯৪৮ সালের দাবির সঙ্গে ১৯৭১ সালের ঘটনার কোন যোগসূত্র দেখা যায়?",
     ["১৯৪৮ সালে তিনি বাংলাকে রাষ্ট্রভাষা করার দাবি তোলেন; ভাষার সেই দাবি থেকেই দীর্ঘ পথ "
      "পেরিয়ে স্বাধীনতার লড়াই এগোয়। তেইশ বছর পর সেই বৃদ্ধ মানুষটিকেও প্রাণ দিতে হয় — "
      "দাবি আর মূল্য দুটোই এক সূত্রে বাঁধা।"],
     "Analyze", "hard", A_DHIREN),
    ("যোগেশচন্দ্র ঘোষ, রণদাপ্রসাদ সাহা ও নূতনচন্দ্র সিংহ — তিনজনের অবদানের মধ্যে কোন মিল আছে?",
     ["তিনজনই নিজের কাজ দিয়ে সাধারণ মানুষের উপকার করেছেন — কেউ ঔষধালয় গড়ে, কেউ দান করে, "
      "কেউ সমাজসেবা করে। তিনজনের পরিচয়ই সেবার পরিচয়।"],
     "Analyze", "hard", A_NUTAN),
    ("পাঠের নাম 'স্মরণীয় যাঁরা বরণীয় যাঁরা' কতটা মানানসই হয়েছে, পাঠের তথ্য দিয়ে দেখাও।",
     ["পাঠজুড়ে এমন মানুষদের কথা আছে যাঁদের কাজ মনে রাখার মতো — ভাষার দাবি, ঔষধালয় প্রতিষ্ঠা, "
      "দান, সমাজসেবা, পড়ানো ও লেখা। 'বরেণ্য' মানে বরণ করার যোগ্য, আর তাঁদের অবদান সত্যিই "
      "সেই যোগ্যতা রাখে — তাই নামটি মানানসই।"],
     "Analyze", "hard", A_BARENYA),
]
for text, acc, bloom, diff, anc in S07:
    add("S07", "মূল কাঠামো", BIO, text, "short_answer", "short", bloom, diff, 2, anc,
        **sa(acc, "মূল তথ্য ও ভাবটি ধরা পড়লেই পূর্ণ নম্বর; শব্দে শব্দে মিল থাকা জরুরি নয়।"))


# =====================================================================================
# S08 · বিস্তৃত উত্তর · simple · 3 owed · 9 authored · marks 5 · descriptive
# 7 Analyze + 2 Evaluate, all hard. Every rubric carries exactly two bands and the single
# mandatory `islamic_alignment` criterion row (§4's minimum shape).
# THE ALIGNMENT THREAD ACROSS ALL NINE, and it is this chapter's ⚠ block turned into rubric rows:
# the history is taught as FACT — dates, events, contributions — while (a) the word শহিদ is never
# defined, applied or asked about, (b) no answer is steered toward any ritual of homage or
# monument observance (C-18), and (c) service and sacrifice are praised as work done for people,
# never as nation-over-ummah framing and never as veneration of a person.
# =====================================================================================
S08 = [
    ("১৯৭১ সালের ২৫শে মার্চ রাতের ঘটনা ধারাবাহিকভাবে লেখো।",
     "Analyze",
     "ঘটনার ক্রম ও স্থান পাঠ থেকে ঠিকভাবে তুলে আনা — তথ্য হিসেবে ইতিহাস লেখা, কোনো "
     "আচার-অনুষ্ঠান বা শ্রদ্ধা নিবেদনের বর্ণনায় না গিয়ে",
     "রাত, আক্রমণকারী, আক্রান্ত জায়গা (ছাত্রাবাস · পুলিশ ব্যারাক · আবাসিক এলাকা) ও নয় মাস "
     "ধরে চলা হত্যাকাণ্ড — সব কটি ধাপ ক্রম মেনে লেখা হয়েছে; ভাষা সংযত এবং কেবল পাঠের তথ্যই "
     "ব্যবহৃত হয়েছে।",
     "দু-একটি ধাপ বাদ পড়েছে বা ক্রম গুলিয়ে গেছে; অথবা পাঠে নেই এমন তথ্য যোগ হয়েছে।"),
    ("ধীরেন্দ্রনাথ দত্তের অবদান বিশ্লেষণ করে লেখো।",
     "Analyze",
     "১৯৪৮ সালের দাবিটিকে তার নিজের গুরুত্বে ব্যাখ্যা করা — ব্যক্তিকে বন্দনা না করে অবদানকে "
     "তথ্য হিসেবে দেখানো",
     "পাকিস্তান গণপরিষদে ১৯৪৮ সালে তিনিই প্রথম বাংলাকে রাষ্ট্রভাষা করার দাবি তোলেন — এই "
     "তথ্যটি এবং তার তাৎপর্য স্পষ্টভাবে লেখা হয়েছে; বয়সের কথাও এসেছে; ভাষা সংযত।",
     "কেবল নাম ও সাল লেখা হয়েছে, দাবির গুরুত্ব ব্যাখ্যা করা হয়নি; অথবা পাঠে নেই এমন কথা এসেছে।"),
    ("১৯৭১ সালের ১৪ই ডিসেম্বর যাঁদের ধরে নিয়ে যাওয়া হয়, তাঁদের পেশা ও অবদান বিশ্লেষণ করে লেখো।",
     "Analyze",
     "পেশাভিত্তিক তালিকাটি পড়ে ক্ষতির স্বরূপ ব্যাখ্যা করা — ঘটনার তথ্য দিয়ে, কোনো ক্ষোভ বা "
     "বিদ্বেষের ভাষা ছাড়া",
     "অধ্যাপক, সাংবাদিক, লেখক ও চিকিৎসক — অন্তত তিন ধরনের পেশা নাম করে লেখা হয়েছে এবং বলা "
     "হয়েছে এঁরা দেশের জ্ঞান, লেখা ও চিকিৎসার কাজ এগিয়ে নিতেন; ভাষা সংযত।",
     "কেবল নামের তালিকা লেখা হয়েছে, পেশা বা অবদানের ব্যাখ্যা নেই; অথবা ভাষায় বিদ্বেষ এসেছে।"),
    ("যোগেশচন্দ্র ঘোষ, রণদাপ্রসাদ সাহা ও নূতনচন্দ্র সিংহ — তিনজনের সমাজসেবার পরিচয় লেখো।",
     "Analyze",
     "তিনজনের অবদান আলাদা করে চেনা ও মিলটি দেখানো — সেবাকে মানুষের উপকার হিসেবে দেখানো, "
     "ব্যক্তিপূজার সুরে নয়",
     "ঔষধালয় প্রতিষ্ঠা, দানশীলতা ও সমাজসেবা — তিনটি অবদানই আলাদা করে লেখা হয়েছে এবং "
     "তিনজনের কাজের মিল দেখানো হয়েছে; ভাষা সংযত ও তথ্যনিষ্ঠ।",
     "একজন বা দুজনের কথা লেখা হয়েছে; অথবা অবদান না লিখে কেবল পরিচয় দেওয়া হয়েছে।"),
    ("'শহিদ বুদ্ধিজীবী দিবস' কবে পালিত হয় এবং এর পেছনের ইতিহাস কী — বিশ্লেষণ করে লেখো।",
     "Analyze",
     "দিনটির তারিখ ও তার পেছনের ঘটনার যোগসূত্র ব্যাখ্যা করা — কেবল ইতিহাসের তথ্য, কোনো "
     "আচার, অনুষ্ঠান বা স্মৃতিসৌধে শ্রদ্ধা নিবেদনের বর্ণনা নয়",
     "১৪ই ডিসেম্বর তারিখটি এবং ১৯৭১ সালের ওই দিনের হত্যাযজ্ঞের কথা — দুটির যোগসূত্র স্পষ্ট "
     "করে লেখা হয়েছে; উত্তরটি ইতিহাসের তথ্যেই সীমাবদ্ধ থেকেছে।",
     "কেবল তারিখ লেখা হয়েছে, ইতিহাস নেই; অথবা উত্তরটি অনুষ্ঠান বা আচারের বর্ণনায় চলে গেছে।"),
    ("সংবাদপত্র ও লেখালেখির জগতের যাঁরা ১৯৭১ সালে প্রাণ হারান, তাঁদের কথা লেখো।",
     "Analyze",
     "সাংবাদিক ও লেখকদের নাম ও পরিচয় পাঠ থেকে ঠিকভাবে তুলে আনা — তথ্য হিসেবে, আবেগের "
     "অতিরঞ্জন ছাড়া",
     "শহিদ সাবের, সেলিনা পারভীন, মেহেরুন্নেসা, সিরাজুদ্দীন হোসেন ও শহীদুল্লা কায়সার — "
     "অন্তত তিনজনের নাম ও পরিচয় লেখা হয়েছে, এবং কোন প্রসঙ্গে তাঁরা এসেছেন তা স্পষ্ট।",
     "কেবল দু-একটি নাম লেখা হয়েছে পরিচয় ছাড়া; অথবা পাঠে নেই এমন নাম যোগ হয়েছে।"),
    ("পাঠটিতে ১৯৪৮, ২৫শে মার্চ ও ১৪ই ডিসেম্বর — এই তিনটি সময় কেন বিশেষভাবে এসেছে, "
     "বিশ্লেষণ করে লেখো।",
     "Analyze",
     "তিনটি সময়ের ঘটনা আলাদা করে চেনা ও তাদের যোগসূত্র দেখানো — তারিখগুলোকে ইতিহাসের তথ্য "
     "হিসেবে ব্যবহার করা",
     "১৯৪৮ — ভাষার দাবি; ২৫শে মার্চ — নিরস্ত্র মানুষের ওপর আক্রমণ; ১৪ই ডিসেম্বর — নতুন করে "
     "হত্যাযজ্ঞ ও পরে দিবস পালন। তিনটিই ঠিকভাবে লেখা হয়েছে এবং একটির সঙ্গে অন্যটির যোগ "
     "দেখানো হয়েছে।",
     "একটি বা দুটি সময়ের কথা লেখা হয়েছে; অথবা ঘটনাগুলো তারিখের সঙ্গে মেলেনি।"),
    ("দেশের জন্য যাঁরা কাজ করেছেন, তাঁদের কথা জানা আমাদের কেন দরকার — নিজের যুক্তি দিয়ে লেখো।",
     "Evaluate",
     "নিজের যুক্তি দাঁড় করানো এবং তা পাঠের তথ্য দিয়ে সমর্থন করা — কৃতজ্ঞতা ও দায়িত্ববোধের "
     "কথা বলা, কোনো ব্যক্তিকে বন্দনার সুরে নয় এবং কোনো আচার-অনুষ্ঠানের সুপারিশ ছাড়া",
     "অন্তত দুটি যুক্তি দেওয়া হয়েছে (যেমন — তাঁদের কাজ থেকে শেখা যায়, দায়িত্ব বুঝতে "
     "শেখা যায়) এবং প্রতিটি যুক্তি পাঠের কোনো তথ্য দিয়ে সমর্থিত; ভাষা সংযত ও শালীন।",
     "যুক্তি একটিই, অথবা যুক্তির সমর্থনে পাঠের কোনো তথ্য নেই; অথবা উত্তরটি আচার-অনুষ্ঠানের "
     "সুপারিশে চলে গেছে।"),
    ("একটি দেশের মেধাবী ও জ্ঞানী মানুষদের হারানো কত বড়ো ক্ষতি — পাঠের তথ্য দিয়ে যুক্তিসহ "
     "নিজের মত লেখো।",
     "Evaluate",
     "'অপূরণীয় ক্ষতি' কথাটির অর্থ নিজের যুক্তিতে দাঁড় করানো — মানুষের কাজ ও অবদানের "
     "দিক থেকে, কোনো জাতি-শ্রেষ্ঠত্বের সুরে নয়",
     "মত স্পষ্টভাবে জানানো হয়েছে এবং অন্তত দুটি যুক্তি পাঠের তথ্য দিয়ে সমর্থিত (যেমন — "
     "অধ্যাপক, চিকিৎসক ও লেখকদের কাজ একদিনে গড়ে ওঠে না); ভাষা সংযত।",
     "মত আছে কিন্তু যুক্তি নেই, অথবা যুক্তি আছে কিন্তু পাঠের কোনো তথ্য নেই।"),
]
for text, bloom, crit, full, part in S08:
    add("S08", "মূল কাঠামো", BIO, text, "descriptive", "structured", bloom, "hard", 5,
        A_ALL if bloom == "Evaluate" else A_DEC, **rubric(crit, full, part))



# =====================================================================================
# S10 · পদ নির্ণয় · alternative, C5 SELECTED = পদ নির্ণয় · 5 owed · 6 authored
# marks 1 · all Understand, easy · teacher-supplied key (CD-136(b)).
# SIX DIFFERENT SENTENCES, ONE TARGET WORD EACH — and that is a constraint, not a preference.
# Two items cut from ONE sentence carry the SAME normalised token set, so `PLAN`'s within-slot
# near-duplicate scan reads them as 100% identical however different the two questions actually
# are. The drill has to vary its stimulus sentence, not only its target word.
# অনুশীলনী ৫ of this chapter is ক্রিয়ার রূপ — a member of BAN-S10's admitted_set that C5 did NOT
# select. It is left unauthored and named in `header.gaps` (COVERAGE would read it off-choice).
# =====================================================================================
S10 = [
    ("'বাংলাদেশের স্বাধীনতার জন্য লক্ষ লক্ষ মানুষ প্রাণ দিয়েছেন।' — এখানে 'স্বাধীনতার' "
     "শব্দটি কোন পদ? নির্ণয় করো।", ["বিশেষ্য", "বিশেষ্য পদ"], A_ALL),
    ("'পাকিস্তানি সেনারা ঘুমন্ত মানুষের ওপর ঝাঁপিয়ে পড়ে।' — এখানে 'ঘুমন্ত' শব্দটি কোন পদ? "
     "নির্ণয় করো।", ["বিশেষণ", "বিশেষণ পদ"], A_MARCH),
    ("'তিনিই প্রথম বাংলা ভাষাকে রাষ্ট্রভাষা করার দাবি তোলেন।' — এখানে 'তোলেন' শব্দটি কোন পদ? "
     "নির্ণয় করো।", ["ক্রিয়া", "ক্রিয়াপদ"], A_BHASHA),
    ("'নূতনচন্দ্র সিংহ ছিলেন চট্টগ্রামের বিখ্যাত সমাজসেবক।' — এখানে 'বিখ্যাত' শব্দটি কোন পদ? "
     "নির্ণয় করো।", ["বিশেষণ", "বিশেষণ পদ"], A_NUTAN),
    ("'নয় মাস ধরে হত্যাকাণ্ড চলে।' — এখানে 'চলে' শব্দটি কোন পদ? নির্ণয় করো।",
     ["ক্রিয়া", "ক্রিয়াপদ"], A_NINE),
    ("'দেশ স্বাধীন হওয়ার পর অনেকের লাশ পাওয়া যায়।' — এখানে 'দেশ' শব্দটি কোন পদ? নির্ণয় করো।",
     ["বিশেষ্য", "বিশেষ্য পদ"], A_BADHYA),
]
for text, acc, anc in S10:
    add("S10", "পদ নির্ণয়", PARTSP, text, "short_answer", "short", "Understand", "easy", 1,
        anc, **sa(acc, PADA_KEY))


# =====================================================================================
# S11 · বিরামচিহ্ন বসানো · alternative, C5 SELECTED = বিরামচিহ্ন বসানো · 5 owed · 7 authored
# marks 1 · all Apply, medium
# `topic_tag` is TOP-BAN-C5-13, NOT -02. QB-CR-014's standing lesson, discharged here by writing
# it right from the first item: TOPIC-NUMBER proves a tag EXISTS, never that it is the RIGHT one
# for its slot. `ref19_topic_id` stays BAN-SENTENCE — REF-19 carries no punctuation slug at all
# (PENDING-P-008, FLAGGED), and minting one here would be QB-CR-008's error in the other register.
# The keys are derivable from the rules, so no CD-136 teacher-key note is carried.
# =====================================================================================
S11 = [
    ("নয় মাস ধরে হত্যাকাণ্ড চলে কত মানুষ যে প্রাণ হারালেন",
     "নয় মাস ধরে হত্যাকাণ্ড চলে। কত মানুষ যে প্রাণ হারালেন!",
     "প্রথম বাক্যটি শেষ হয়েছে, তাই দাঁড়ি; পরেরটিতে বিস্ময় প্রকাশ পেয়েছে, তাই বিস্ময়চিহ্ন।",
     A_NINE),
    ("ধীরেন্দ্রনাথ দত্ত ১৯৪৮ সালে যে দাবি তুলেছিলেন সেটি ছিল বাংলাকে রাষ্ট্রভাষা করার দাবি",
     "ধীরেন্দ্রনাথ দত্ত ১৯৪৮ সালে যে দাবি তুলেছিলেন, সেটি ছিল বাংলাকে রাষ্ট্রভাষা করার দাবি।",
     "'যে … সেটি' গঠনে দুই অংশের মাঝে কমা, বাক্যের শেষে দাঁড়ি।", A_BHASHA),
    ("কৃষক শ্রমিক ছাত্র শিক্ষক সবাই প্রাণ দিয়েছেন",
     "কৃষক, শ্রমিক, ছাত্র, শিক্ষক — সবাই প্রাণ দিয়েছেন।",
     "একজাতীয় শব্দগুলোর মাঝে কমা, তালিকার পরে ড্যাশ, শেষে দাঁড়ি।", A_ALL2),
    ("তুমি কি জানো শহিদ বুদ্ধিজীবী দিবস কোন তারিখে পালিত হয়",
     "তুমি কি জানো, 'শহিদ বুদ্ধিজীবী দিবস' কোন তারিখে পালিত হয়?",
     "প্রশ্নবোধক বাক্যের শেষে প্রশ্নচিহ্ন; দিবসের নামটি উদ্ধৃতিচিহ্নে।", A_DIBAS),
    ("যোগেশচন্দ্র ঘোষ ছিলেন সাধনা ঔষধালয়ের প্রতিষ্ঠাতা তাঁর বয়স ছিল চুরাশি",
     "যোগেশচন্দ্র ঘোষ ছিলেন সাধনা ঔষধালয়ের প্রতিষ্ঠাতা। তাঁর বয়স ছিল চুরাশি।",
     "এখানে দুটি আলাদা পূর্ণ বাক্য, তাই দুটিরই শেষে দাঁড়ি।", A_JOGESH),
    ("কী ভয়ংকর রাত ছিল সেটি",
     "কী ভয়ংকর রাত ছিল সেটি!", "বিস্ময় প্রকাশ পেয়েছে, তাই শেষে বিস্ময়চিহ্ন।", A_MARCH),
    ("রণদাপ্রসাদ সাহাকে লোকে ডাকত দানবীর",
     "রণদাপ্রসাদ সাহাকে লোকে ডাকত 'দানবীর'।",
     "বিশেষ নামটি উদ্ধৃতিচিহ্নে, বাক্যের শেষে দাঁড়ি।", A_RANADA),
]
for raw, fixed, note, anc in S11:
    add("S11", "বিরামচিহ্ন বসানো", PUNCT,
        f"'{raw}' — বাক্যটিতে প্রয়োজনীয় বিরামচিহ্ন বসিয়ে আবার লেখো।",
        "short_answer", "short", "Apply", "medium", 1, anc, **sa([fixed], note))


# =====================================================================================
# S12 · যুক্তবর্ণ ও শব্দ গঠন · COMPOSITE (যুক্তবর্ণ ভাঙা + শব্দ গঠন) · 5 owed · 7 authored
# marks 1 · all Apply, medium · teacher-supplied key (CD-136(b))
# Both parts are declared on every item — an item that only breaks the conjunct does half the
# task and COVERAGE fails it (SLOT_REGISTER BAN-S12 `parts`).
# =====================================================================================
S12 = [
    ("বুদ্ধিজীবী", "দ্ধ", "দ + ধ", "যুদ্ধ", A_DIBAS),
    ("প্রতিষ্ঠাতা", "ষ্ঠ", "ষ + ঠ", "শ্রেষ্ঠ", A_JOGESH),
    ("ছাত্রাবাস", "ত্র", "ত + র", "পাত্র", A_ATTACK),
    ("মধ্যরাত", "ধ্য", "ধ + য", "অধ্যায়", A_MID),
    ("বিশ্ববিদ্যালয়", "শ্ব", "শ + ব", "বিশ্বাস", A_ATTACK),
    ("নিরস্ত্র", "স্ত্র", "স + ত + র", "অস্ত্র", A_MARCH),
    ("পাষণ্ড", "ণ্ড", "ণ + ড", "দণ্ড", A_PASHANDA),
]
for word, conj, split, newword, anc in S12:
    add("S12", ["যুক্তবর্ণ ভাঙা", "শব্দ গঠন"], JUKTO,
        f"পাঠের '{word}' শব্দে থাকা '{conj}' যুক্তবর্ণটি ভেঙে দেখাও, আর সেই যুক্তবর্ণ দিয়ে "
        f"নতুন একটি শব্দ গঠন করো।",
        "short_answer", "short", "Apply", "medium", 1, anc,
        **sa([f"{conj} = {split}; নতুন শব্দ — {newword}", f"{conj} — {split}; {newword}"],
             JUKTO_KEY))


# =====================================================================================
# S13 · এক কথায় প্রকাশ · simple · 5 owed · 7 authored · marks 1 · 2 Remember + 5 Understand
# THE SPLIT IS DEMAND, NOT SLOT (QB-CR-011). Two answers — আত্মদানকারী and বরেণ্য — are glossed
# VERBATIM in the chapter's অর্থ জেনে নিই list, so recalling them is `Remember` and no CD-136
# teacher-key note is owed. The other five come from অনুশীলনী ৩'s মিলকরণ list and from the
# chapter's own নাম, are NOT glossed anywhere in it, and require reading a definition and naming
# the word — `Understand`, with the teacher-key note each item declares for itself.
# =====================================================================================
add("S13", "মূল কাঠামো", VOCAB,
    "'অন্যের উপকারের জন্য নিজের জীবন দান করেন যিনি' — পাঠের শব্দ দিয়ে এক কথায় প্রকাশ করো।",
    "short_answer", "short", "Remember", "easy", 1, A_ATMA, **sa(["আত্মদানকারী"]))
add("S13", "মূল কাঠামো", VOCAB,
    "'বরণ করার যোগ্য যিনি' — পাঠের শব্দ দিয়ে এক কথায় প্রকাশ করো।",
    "short_answer", "short", "Remember", "easy", 1, A_BARENYA,
    **sa(["বরেণ্য", "বরণীয়"], "পাঠের নামেই আছে 'বরণীয়' — দুটিই গ্রহণযোগ্য।"))
S13 = [
    ("যাঁর মেধা অসাধারণ", ["মেধাবী"], A_EX3),
    ("যাঁর কোনো অহংকার নেই", ["নিরহংকার"], A_EX3),
    ("বাছবিচার না করে যা করা হয়", ["নির্বিচার"], A_EX3),
    ("যে ক্ষতি আর পূরণ করা যায় না", ["অপূরণীয়"], A_EX3),
    ("দানে যিনি বীরের মতো", ["দানবীর"], A_RANADA),
]
for phrase, acc, anc in S13:
    add("S13", "মূল কাঠামো", VOCAB,
        f"'{phrase}' — এক কথায় প্রকাশ করো।",
        "short_answer", "short", "Understand", "medium", 1, anc, **sa(acc, TEACHER_KEY))


# =====================================================================================
def build():
    questions, slot_index, task_index, source_index = [], {}, {}, {}
    for i, it in enumerate(ITEMS, start=1):
        qid = f"QP-BAN-C5-U16-Q{i:02d}"
        q = {"qid": qid, "topic_tag": it["topic"], "ref19_topic_id": it["slug"],
             "question_text": it["text"], "question_type": it["qtype"],
             "paper_role": it["role"], "bloom_level": it["bloom"],
             "difficulty": it["diff"], "tier": "tier1", "marks": it["marks"],
             "chapter_ref": CHAPTER}
        q.update(it["extra"])
        questions.append(q)
        slot_index[qid] = it["slot"]
        task_index[qid] = it["task"]
        source_index[qid] = it["anchor"]

    by_qid = {q["qid"]: q for q in questions}
    qids = [q["qid"] for q in questions]
    by_slot = {}
    for qid in qids:
        by_slot.setdefault(slot_index[qid], []).append(qid)
    slot_counts = {s: len(v) for s, v in sorted(by_slot.items())}

    # Pools — QB-D-001: every item in exactly one, no overlap. CT takes the short recall a
    # 25-mark class test can actually carry; AS takes the mixed band QB-D-004 wants (roughly half
    # at or above Apply); HW takes the rest.
    ct, as_, hw = [], [], []
    for qid in qids:
        s, q = slot_index[qid], by_qid[qid]
        if s in ("S02", "S04") and len(ct) < 14:
            ct.append(qid)
        elif s in ("S03", "S08", "S12") or q["bloom_level"] in ("Analyze", "Evaluate"):
            as_.append(qid)
        else:
            hw.append(qid)

    return {
        "schema_version": "1.0",
        "policy_shape": "qp6",
        "bank_id": "QB-BAN-C5-U16",
        "wave": 1,
        "subject": "BAN",
        "class": 5,
        "chapter": CHAPTER,
        "extraction_path": EXTRACTION,
        "source_extraction": EXTRACTION,
        "curation": (
            "FLEXIBLE · এই পাঠের ⚠ ব্লকই উৎসের সবচেয়ে ভারী এবং তার প্রতিটি ধারা এখানে "
            "মানা হয়েছে। (১) 'শহিদ' শব্দটি নিয়ে কোনো সংজ্ঞামূলক প্রশ্ন নেই — কোনো আইটেম "
            "জিজ্ঞাসা করে না শব্দটির অর্থ কী বা কারা এর আওতায় পড়েন; শব্দটি কেবল দুটি "
            "নামের ভেতরেই আছে, যে দুটি নাম বই নিজেই ছাপে: শহিদ সাবের (ব্যক্তির নাম) ও "
            "'শহিদ বুদ্ধিজীবী দিবস' (দিবসের নাম)। বাকি সর্বত্র লেখা হয়েছে প্রাণ দেন · "
            "প্রাণ হারান · হত্যা করা হয় · বুদ্ধিজীবী। (২) C-03 — গান ও সুরকারের অনুচ্ছেদ "
            "নিষিদ্ধ; সেটি extraction-এ নেই, তাই কোনো anchor সেখানে পৌঁছায় না। (৩) C-18 — "
            "শহিদ মিনারে ফুল দেওয়া বা কোনো শ্রদ্ধা নিবেদনের আচার কোনো প্রশ্নে, উত্তরে বা "
            "rubric-এ নেই; REF-01 §4.1 C-18-এর নিজস্ব ছাড় অনুযায়ী কেবল তথ্যগত ইতিহাস — "
            "তারিখ, ঘটনা, অবদান — পড়ানো হয়েছে। (৪) C-05 — কোনো ব্যক্তির ছবি নেই ও চাওয়া "
            "হয়নি। কোনো কাল্পনিক ব্যক্তিনাম কোথাও ব্যবহৃত হয়নি; যে নামগুলো আছে সেগুলো "
            "পাঠের নিজের ঐতিহাসিক ব্যক্তি — চরিত্র নয়, তথ্য।"),
        "header": {
            "target": len(questions),
            "reason": (
                "৯৬ এই পাঠের প্রথম ঢেউ, এবং সংখ্যাটি বিষয়বস্তুর সীমা নয় — বাঁধন হলো Bloom-এর "
                "মেঝেগুলো। CD-141(g) অনুযায়ী ৪০-এর নিচে কোনো ব্যাংক PLAN পাস করে না, আর প্রতিটি "
                "ধনাত্মক মেঝে ≥২ মার্জিনে পার হতে হয়। এগারোটি স্বীকৃত স্লটের কাগজ-স্তরের দাবি "
                "৫২ (CD-138(g)) — সেটি মেটানোর পরেও Apply-এর মার্জিন আসে S03 · S11 · S12 থেকে "
                "এবং Analyze-এর মার্জিন S07 · S08 থেকে, তাই ওই পাঁচটি স্লট দাবির উপরে টানা "
                "হয়েছে। এই পাঠ গদ্য ও তথ্যবহুল — উৎস নিজেই বলছে 'এখানে প্রশ্নের ভালো উৎস "
                "অনেক' — তাই সীমা এসেছে Bloom থেকে, বিষয়বস্তু থেকে নয়।"),
            "topics": ["TOP-BAN-C5-14", "TOP-BAN-C5-01", "TOP-BAN-C5-02", "TOP-BAN-C5-13"],
            "spine_slots": [f"S{i:02d}" for i in range(1, 16)],
            "admissible_slots": sorted(by_slot),
            "slot_exclusions": {
                "S01": ("পাঠ ১৬ গদ্য (ইতিহাস), এতে মুখস্থ করার মতো কোনো কবিতাংশ নেই — এবং "
                        "কারণটি অনুমান নয়, উৎসের নিজের বাক্য: 'কবিতা চারটি: পাঠ ১৩, ১৫, ১৮, "
                        "২০ — এগুলোই S01 (কবিতা মুখস্থ) ও S09 (মূলভাব) প্রশ্নের উৎস।' পাঠ ১৬ "
                        "সেই চারটির একটিও নয়।"),
                "S09": ("একই বাক্য S09-কেও ওই চার কবিতায় বেঁধেছে; মূলভাব এখানে কবিতার কাজ, "
                        "আর পাঠ ১৬-এ কোনো কবিতা নেই — তাই এই পাঠ স্লটটির উৎস নয়।"),
            },
            "admissibility_declaration": (
                "CD-138(e), পাঠ ১৬-এর নিজস্ব ঘোষণা, canon/marklogic/C5_Bangla_Source_13-23.md-এর "
                "পাঠ ১৬ অংশ থেকে লেখা — পাঠ ১২ পড়া হয়নি (CD-127(b) consumption exclusion)। "
                "রেজিস্টারে BAN C5-এর পনেরোটি স্লট। এর মধ্যে দুটি — S14 আবেদনপত্র ও S15 রচনা "
                "— CD-147 অনুযায়ী প্রতিটি পাঠের জন্যই কাগজ-স্তরের, শ্রেণিগতভাবে; কোনো পাঠ "
                "এদের জন্য বিষয়বস্তুর কারণ দেখানোর দায়ে নেই এবং এই ঘোষণা তাদের নিয়ে কিছুই "
                "বলে না, যা CD-147(c) অনুযায়ী সঠিক, অসম্পূর্ণ নয়। বাকি তেরোটির মধ্যে এগারোটি "
                "স্বীকৃত এবং দুটি — S01 ও S09 — বাদ, প্রতিটির এক লাইনের বিষয়বস্তু-কারণসহ "
                "slot_exclusions-এ। বাদ দুটির ভিত্তি উৎসের নিজের বাক্য, বিষয়বস্তু থেকে "
                "অনুমান নয় — CD-138(e) সেই অনুমান দুই দিকেই নিষিদ্ধ করে; ঠিক এই বাক্যটিই "
                "পাঠ ১৪-এ দুটি স্লট কেড়ে নিয়েছিল আর পাঠ ১৫-কে দুটি স্লট দিয়েছিল। এগারোটি "
                "স্বীকৃত স্লটের দাবি ৫২ আইটেম (কাগজের মোট ৫৬, বাদ S01-এর ১ · S09-এর ১ · "
                "S14-এর ১ · S15-এর ১); দাবি কাগজ-স্তরের ও অবিভাজ্য (CD-138(d), CD-138(g))। "
                "CD-142(b) অনুযায়ী পরিকল্পনার কাউন্টারসাইন এখন PLAN গেট, মানুষের সই নয়।"),
            "slot_counts": slot_counts,
            "topic_tag_ruling": (
                "পাঠ ১৬ গদ্য (ইতিহাস/জীবনী), তাই পাঠ-বিষয়ক আইটেমগুলো TOP-BAN-C5-14 "
                "(জীবনী, BAN-BIOGRAPHY) বহন করে — canon/topics/TOPIC_NUMBERS.md-এর পাঠ-ধরন ছক "
                "পাঠ ১৬-কে নাম ধরে -14 দিয়েছে (MINTED 2026-08-14)। topic_tag প্রতি-প্রশ্নের "
                "ক্ষেত্র, প্রতি-অধ্যায়ের নয়: শব্দার্থ, বিপরীত শব্দ, যুক্তবর্ণ, পদ নির্ণয় ও "
                "এক কথায় প্রকাশের আইটেম -01, বাক্য গঠন -02, বিরামচিহ্ন -13। বিরামচিহ্নের সাতটি "
                "আইটেম প্রথম থেকেই -13 বহন করছে, -02 নয় — QB-CR-014-এর শিক্ষা: TOPIC-NUMBER "
                "প্রমাণ করে একটি ট্যাগ আছে, কখনো প্রমাণ করে না সেটিই এই স্লটের সঠিক ট্যাগ। "
                "ref19_topic_id বিরামচিহ্নে BAN-SENTENCE-ই থাকছে — REF-19-এ যতিচিহ্নের কোনো "
                "slug নেই (PENDING-P-008, FLAGGED), আর এখানে একটি বানিয়ে নেওয়া হতো QB-CR-008-এর "
                "ভুলটাই অন্য রেজিস্টারে করা।"),
            "content_facts": (
                "CD-135(d) — শূন্য মেঝের বিপরীতে যে স্তরটি শূন্য, সেটি বিষয়বস্তুর তথ্য হিসেবে "
                "এখানে বলা হলো: Create এই পুলে ০। পাঠটি তথ্যমূলক ইতিহাস এবং এর অনুশীলনীর "
                "সাতটি কাজের একটিও নতুন রচনা তৈরির নয় — শূন্যস্থান, প্রশ্নোত্তর, মিলকরণ, "
                "বহুনির্বাচনি, ক্রিয়ার রূপ, বাক্য সম্পূর্ণ করা ও ঘটনা সাজানো; কোনোটিই মৌলিক "
                "নির্মাণ চায় না। Evaluate ২টি আছে, দুটিই যুক্তিনির্ভর মতামতের প্রশ্ন।"),
            "gaps": [
                "S14 · S15 — CD-147 অনুযায়ী কাগজ-স্তরের, শ্রেণিগতভাবে; এই পাঠ এদের নিয়ে কিছু "
                "ঘোষণা করে না এবং করার দায়ও নেই (CD-147(c))।",
                "অনুশীলনী ৫ (ক্রিয়ার রূপ — খাওয়া · ওঠা · যাওয়া) এই ঢেউয়ে ব্যবহার করা হয়নি, "
                "এবং কারণটি বিষয়বস্তুর অভাব নয়। ক্রিয়ার কাল/রূপ BAN-S10-এর admitted_set-এর "
                "সদস্য, কিন্তু C5 নির্বাচন করেছে পদ নির্ণয়; নির্বাচনের বাইরের কাজ লিখলে "
                "COVERAGE off-choice হিসেবে ধরে (CD-138(b))। উৎসের ছকও পাঠ ১৬-কে S10-এর "
                "বিকল্প উৎস বলছে, বাধ্যতামূলক নয়।",
                "অনুশীলনী ৭ (ঘটনা সাজিয়ে অনুচ্ছেদ — বকের বাসার গল্প) ব্যবহার করা যায়নি এবং "
                "কারণটি নীতিগত নয়, প্রমাণগত: উৎস অনুশীলনীটির নাম ছাপে কিন্তু গল্পটির একটি "
                "বাক্যও ছাপে না, তাই তিন-টোকেনের কোনো anchor নেই এবং SOURCE-TRACE কোনো "
                "আইটেমকে সেখানে বাঁধতে পারত না। বই খোলা এখানে অনুমোদিত পথ নয় (উৎসের নিজের "
                "ভূমিকা: 'এই ফাইল থেকেই উপাদান নিতে হবে')।",
                "গান ও সুরকারের অনুচ্ছেদ (C-03) এবং শহিদ মিনারে ফুল দেওয়ার অংশ (C-18) — উৎসের "
                "⚠ ব্লক দুটিকেই নিষিদ্ধ করেছে এবং extraction-এ দুটির কোনোটিই নেই। কোনো আইটেম "
                "সেখানে যায়নি; ভবিষ্যতের কোনো ঢেউয়েও যাবে না।",
                "S08-এর নয়টি আইটেমের বাইরে বিস্তৃত উত্তরের আরও উপাদান এই পাঠে আছে — বিশেষত "
                "পৃথক ব্যক্তিদের নিয়ে আলাদা আলাদা প্রশ্ন। বিষয়বস্তুর সীমা ছোঁয়া হয়নি এবং "
                "সেটি ইচ্ছাকৃত: এই ঢেউয়ের বাঁধন Bloom, বিষয়বস্তু নয়।",
            ],
        },
        "flags": [],
        "pool_index": {"HW": hw, "AS": as_, "CT": ct},
        "slot_index": slot_index,
        "task_index": task_index,
        "source_index": source_index,
        "questions": questions,
        "waves": {"1": (f"Q01–Q{len(questions):02d} · 2026-08-16 · author_U16_wave1.py · "
                        f"পাঠ ১৬-এর প্রথম ব্যাংক, CD-141 teacher-lane-এ authored, PLAN "
                        f"কাউন্টারসাইন সহ (CD-142(b))")},
    }


def selfcheck(bank):
    """Cheap pre-gate arithmetic, so a failing run says WHY before the suite does."""
    import collections
    qs = bank["questions"]
    n = len(qs)
    floors = {"Remember": 20, "Understand": 25, "Apply": 25, "Analyze": 10}
    c = collections.Counter(q["bloom_level"] for q in qs)
    print(f"  items: {n}")
    for lvl, p in floors.items():
        need = -(-p * n // 100)
        m = c[lvl] - need
        print(f"    {lvl:<11}{c[lvl]:>4}   need {need:>3}   margin +{m}"
              + ("   <-- BELOW +2" if m < 2 else ""))
    print(f"    Evaluate   {c['Evaluate']:>4}   Create {c['Create']}")
    d = collections.Counter(q["difficulty"] for q in qs)
    print(f"  easy {100*d['easy']/n:.1f}% (floor 30%) - medium {100*d['medium']/n:.1f}% - "
          f"hard {100*d['hard']/n:.1f}%")
    demand = {"S02": 5, "S03": 5, "S04": 5, "S05": 5, "S06": 5, "S07": 4,
              "S08": 3, "S10": 5, "S11": 5, "S12": 5, "S13": 5}
    sc = bank["header"]["slot_counts"]
    print("  slots: " + " - ".join(f"{s} {sc[s]}/{demand[s]}" for s in sorted(sc)))
    bad = [s for s in demand if sc.get(s, 0) < demand[s]]
    if bad:
        print(f"  <-- UNDER DEMAND: {bad}")
    extra = [s for s in sc if s not in demand]
    if extra:
        print(f"  <-- ITEM IN AN UNDECLARED SLOT: {extra}")
    pools = bank["pool_index"]
    print("  pools: " + " - ".join(f"{k} {len(v)}" for k, v in pools.items())
          + f"  (sum {sum(len(v) for v in pools.values())} of {n})")
    for q in qs:
        for s in [q["question_text"]] + [o["text"] for o in q.get("options", [])]:
            if re.search(r"[0-9]", s):
                print(f"  <-- ASCII DIGIT in {q['qid']}: {s[:40]}")
    # Anchors, checked here so a bad one is named before SOURCE-TRACE prints ninety-six lines.
    import unicodedata

    def norm(s):
        s = unicodedata.normalize("NFC", s or "")
        s = re.sub(r"[‘’“”'\"()\[\]।,;:?!—–\-….*_#>|/·]", " ", s)
        return re.sub(r"\s+", " ", s).strip()

    hay = norm((ROOT / EXTRACTION).read_text(encoding="utf-8"))
    bad_anchor = 0
    for qid, a in bank["source_index"].items():
        na = norm(a)
        if len(na.split()) < 3:
            print(f"  <-- ANCHOR TOO SHORT {qid}: {a!r}")
            bad_anchor += 1
        elif na not in hay:
            print(f"  <-- ANCHOR NOT IN EXTRACTION {qid}: {a!r}")
            bad_anchor += 1
    print(f"  anchors: {len(bank['source_index'])} checked, {bad_anchor} bad")
    # Within-slot stem duplication — PLAN fails at 95%, and two items cut from ONE sentence
    # carry the SAME token set however different they look. Caught here, by slot, before the gate.
    by_slot = {}
    for q in qs:
        by_slot.setdefault(bank["slot_index"][q["qid"]], []).append(
            (q["qid"], norm(q["question_text"])))
    worst = 0.0
    for s, grp in sorted(by_slot.items()):
        for i in range(len(grp)):
            for j in range(i + 1, len(grp)):
                ta, tb = set(grp[i][1].split()), set(grp[j][1].split())
                sim = len(ta & tb) / len(ta | tb) if (ta | tb) else 0.0
                worst = max(worst, sim)
                if sim >= 0.95:
                    print(f"  <-- NEAR-DUPLICATE {s}: {grp[i][0]} ~ {grp[j][0]} {sim:.0%}")
    print(f"  worst within-slot stem similarity: {worst:.0%} (PLAN fails at 95%)")


if __name__ == "__main__":
    bank = build()
    selfcheck(bank)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(bank, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"  wrote {OUT.relative_to(ROOT)}  ({len(bank['questions'])} items)")
