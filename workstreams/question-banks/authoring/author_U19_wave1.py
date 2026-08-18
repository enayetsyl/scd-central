#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""author_U19_wave1.py — C5 Bangla, পাঠ ১৯ (ভাষার খেলা) question bank, wave 1.

Run from the repo root:
    python3 workstreams/question-banks/authoring/author_U19_wave1.py

WHY THE SCRIPT IS THE ARTIFACT (LOCAL.md, "Artifacts & naming"). A JSON nobody can re-derive is
not reviewable; this file is what makes the bank reproducible and reviewable AS CONTENT. It is
promoted with its bank.

THE ONE FACT THIS WHOLE BANK TURNS ON: পাঠ ১৯ PRINTS NO USABLE SENTENCE.
`canon/marklogic/C5_Bangla_Source_13-23.md` lines 412–443 carry FOUR headings — অনুশীলনীর বিষয় ·
কোন প্রশ্নে কাজে লাগবে · ✅ বিশেষ সুবিধা · ⚠️ সতর্কতা — and NO `## পূর্ণ পাঠ`, NO `## অর্থ জেনে নিই`.
The chapter's own second line says so: "ব্যাকরণ-অনুশীলন (কোনো মূল পাঠ নেই, শুধু অনুশীলনী)".
What it actually prints is ten exercise NAMES, five words (দিয়ে · উপর · কাছে · থেকে · পক্ষে),
twelve synonym pairs (24 words) — and exactly ONE full sentence, "আমরা সবাই মিলে মেলায় যাচ্ছি",
which C-04 BARS.

AND THE SOURCE ITSELF SUPPLIES THE REMEDY, which is what authorises every composed stimulus below:
    "অনুশীলনী ১-এ **'আমরা সবাই মিলে মেলায় যাচ্ছি'** — মেলা/উৎসবের প্রসঙ্গ (C-04)।
     **প্রশ্নে অন্য বাক্য বসাতে হবে।**"
The extraction INSTRUCTS the question-author to put a different sentence in. Every composed
stimulus here is built only from words the chapter itself prints, and none of them is a personal
name (so QB-CR-005's REF-20 substitution question never arises).

THIN IS NOT UNIFORM, AND THAT IS THE FINDING. This chapter is near-empty in the COMPREHENSION
slots — no story, no event, no character, no line of argument — and rich in the SKILL slots. The
source says so in its own words: "এই পাঠে কোনো কাহিনি নেই — শুধু ভাষার কাজ। তাই এটি দক্ষতার
প্রশ্নের সবচেয়ে বড় উৎস". So S01 · S08 · S09 · S11 are EXCLUDED on content and S02 · S03 · S04 ·
S05 · S06 · S07 · S10 · S12 · S13 are admitted. CD-171(f): a thin chapter is an ordinary chapter —
it authors what its source supports and stops. There is no reduced mode and no threshold.

WHERE IT STOPS, AND WHY. The chapter prints 29 words and 10 task names. Once each word has been
put to one task, a further question is a near-duplicate of an existing one, and §4's ban — now the
ONLY bound (CD-171(a)) — is what stops the bank at 46 items. **This is the CHAPTER's content
limit, not the EXTRACTION's**: পাঠ ১৯ has no পূর্ণ পাঠ in the book either (the এক নজরে table calls
it ব্যাকরণ-অনুশীলন, pages ১০৭–১১১), so the extraction is carrying the whole shape of the chapter,
not a subset of it. Opening the book is not an authorised path — "এই ফাইল থেকেই উপাদান নিতে হবে".

TWO SLOTS LOSE THEIR BEST CONTENT TO THE CLASS'S OWN SELECTION, AND IT IS RECORDED RATHER THAN
ROUTED AROUND (CD-138(b)):
  · `BAN-S06` admits {বিপরীত শব্দ, সমার্থক শব্দ} and **C5 selected বিপরীত শব্দ**. So the twelve
    synonym pairs — which the source calls "সবচেয়ে ভালো উৎস" — cannot be asked as সমার্থক items
    at C5 at all. They are used at S02 (অর্থ), S13 (এক কথায়) and S05 (বহুনির্বাচনি) instead.
  · `BAN-S10` admits {ভাষারীতি পরিবর্তন, পদ নির্ণয়, ক্রিয়ার কাল} and **C5 selected পদ নির্ণয়**.
    So অনুশীলনী ১ (ক্রিয়ার কাল), which the source's own ছক names পাঠ ১৯ for — "১৯ (কাল)" — is
    unusable. Every S10 item here is পদ নির্ণয়.
Neither is written around by re-labelling the task. An off-choice item is a real failure and is
reported as a different thing from a task admitted nowhere.

S14/S15 ARE NOT DECLARED AT ALL, AND THAT IS THE CORRECT SHAPE (CD-147(c)).

S11 CARRIES ZERO ITEMS, SO QB-CR-017's DEFECT CLASS HAS NO SURFACE HERE. The slot is excluded on
content — none of the chapter's ten exercises is about punctuation and it prints no punctuated
sentence to work on. The exclusion reason is the অনুশীলনীর বিষয় table (the chapter's actual
content), NOT the chapter's own "কোন প্রশ্নে কাজে লাগবে" line, which CD-134(c) forbids as a reason.
"""

import json
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[3]
SRC = "canon/marklogic/C5_Bangla_Source_13-23.md"
OUT = ROOT / "workstreams" / "question-banks" / "banks" / "C5_BAN_U19_QuestionBank_v1.json"
CHAP = "পাঠ ১৯ — ভাষার খেলা"

# ── ANCHORS — every one a verbatim span of the পাঠ ১৯ section, asserted below ────────────
A_EX1 = "ক্রিয়ার কাল — আগেকার / এখনকার / পরের"
A_EX2 = "গুণ ও বৈশিষ্ট্য বসানো (বিশেষণ)"
A_EX3 = "শব্দ দিয়ে বাক্য — দিয়ে · উপর · কাছে · থেকে · পক্ষে"
A_EX4 = "দুটি বাক্য জোড়া দিয়ে একটি"
A_EX5 = "একটি বাক্য ভেঙে দুটি"
A_EX6 = ("একই রকম শব্দ (সমার্থক) — ঘর/বাড়ি · প্রভাত/সকাল · রজনী/রাত · পুস্তক/বই · অরুণ/রবি · "
         "মেয়ে/কন্যা · ক্ষুদ্র/ছোটো · মাতা/জননী · ললাট/কপাল · সাগর/সমুদ্র · দিবস/দিন · ছেলে/পুত্র")
A_EX7 = "মিলিয়ে মিলিয়ে বাক্য (অন্ত্যমিল)"
A_EX8 = "দৈনিক পত্রিকা থেকে তিনটি খবরের শিরোনাম"
A_KIND = "ব্যাকরণ-অনুশীলন (কোনো মূল পাঠ নেই, শুধু অনুশীলনী)"
A_NOSTORY = "এই পাঠে কোনো কাহিনি নেই — শুধু ভাষার কাজ।"
A_BEST = "S13 সমার্থক শব্দ — সবচেয়ে ভালো উৎস"
A_ARUN = "অনুশীলনী ৬-এ অরুণ, রবি, রজনী — এগুলো সাধারণ বাংলা সমার্থক শব্দ, ব্যবহারে বাধা নেই।"

# ── model_note boilerplate ──────────────────────────────────────────────────────────────
# CD-136(b) / P-037: a TEACHER-SUPPLIED key is one the chapter does not print. It is DECLARED in
# the item's own model_note and rides `short_answer` and `descriptive` only — never inferred from
# the slot, which would be QB-CR-011's shape.
TEACHER = ("এই উত্তরকুঞ্জি শিক্ষকের দেওয়া (CD-136(b)) — এটি বাংলা ভাষার সাধারণ তথ্য, পাঠ ১৯ এর "
           "উত্তর ছাপে না। উদ্দীপকের শব্দ পাঠ ১৯ থেকেই নেওয়া। ")
OWN_SENT = ("শিক্ষার্থীর নিজের যেকোনো শুদ্ধ বাক্য গ্রহণযোগ্য, যদি শব্দটি সঠিক অর্থে ব্যবহৃত হয় এবং "
            "বাক্যটি বিরামচিহ্নসহ সম্পূর্ণ হয়। নমুনা উত্তর দেওয়া হলো।")
PAD_NOTE = ("গৃহীত উত্তরগুলো পাঠ ১৯-এর নিজের তালিকার শব্দ; জোড়ার যেকোনো একটি শব্দই পূর্ণ নম্বর পাবে।")
# S06's key is never printed by the chapter: the twelve pairs are synonym rows, not antonym
# rows, and the section states no antonym relation anywhere. So ALL FIVE carry the same
# teacher-supplied declaration.
ANTONYM_NOTE = TEACHER + "কাছাকাছি অর্থের যেকোনো শুদ্ধ বিপরীত শব্দ গ্রহণযোগ্য।"
POD_NOTE = (TEACHER + "নির্দিষ্ট উত্তরই লাগবে — এই কাজে কাছাকাছি অর্থের কোনো বিকল্প নেই, গৃহীত "
            "তালিকার বাইরে কিছু নেওয়া যাবে না। এই আইটেমের গৃহীত তালিকার প্রথম রূপটিই আদর্শ "
            "উত্তর; ওই তালিকার বাকি রূপগুলো একই পদেরই অন্য নাম, সেগুলোও পূর্ণ নম্বর পাবে — "
            "কিন্তু অন্য কোনো পদের নাম নয়।")
JUK_NOTE = (TEACHER + "যুক্তবর্ণ ভাঙার উত্তরটি নির্দিষ্ট — সেখানে বিকল্প নেই। নতুন শব্দ যেকোনো শুদ্ধ "
            "শব্দ হতে পারে, যদি তাতে সেই যুক্তবর্ণ থাকে; গৃহীত তালিকা কেবল নমুনা। দুটি কাজই করতে "
            "হবে — শুধু ভাঙলে বা শুধু শব্দ গঠন করলে অর্ধেক কাজ।")

ITEMS = []


def add(slot, task, anchor, q, **kw):
    ITEMS.append({"slot": slot, "task": task, "anchor": anchor, "q": q, **kw})


def sa(text, accepted, note=None):
    ak = {"accepted": accepted}
    if note:
        ak["model_note"] = note
    return {"question_text": text, "question_type": "short_answer", "paper_role": "short",
            "answer_key": ak}


# ══════════════════════════════════════════════════════════════════════════════════════
# S02 · শব্দার্থ — task "মূল কাঠামো" · 1 mark
# The twelve pairs gloss a tatsama/সাধু word with its everyday one. The MEANING IS PRINTED,
# so these keys are NOT teacher-supplied and carry no CD-136 note.
# ══════════════════════════════════════════════════════════════════════════════════════
for w, meaning, extra in [
        ("রজনী", "রাত", []),
        ("প্রভাত", "সকাল", []),
        ("পুস্তক", "বই", []),
        ("ললাট", "কপাল", []),
        ("দিবস", "দিন", []),
]:
    add("S02", "মূল কাঠামো", A_EX6,
        sa(f"'{w}' — পাঠ ১৯-এর তালিকায় থাকা এই শব্দটির অর্থ লেখো।", [meaning] + extra),
        topic="TOP-BAN-C5-01", ref19="BAN-VOCAB", bloom="Remember", diff="easy", marks=1)

# ══════════════════════════════════════════════════════════════════════════════════════
# S03 · বাক্য গঠন — task "মূল কাঠামো" · 1 mark
# The source names পাঠ ১৯ the BEST source for this slot, and four of its ten exercises (৩ · ৪ ·
# ৫ · ৭) are sentence work. BAN-S03-NOJOIN is honoured: not one of these is joined to a যুক্তবর্ণ
# or কারচিহ্ন task — S12 stands entirely on its own below.
# ══════════════════════════════════════════════════════════════════════════════════════
for w, sample in [
        ("দিয়ে", "কলম দিয়ে চিঠিটি লিখলাম।"),
        ("উপর", "টেবিলের উপর পুস্তকটি রাখা আছে।"),
        ("কাছে", "সাগরের কাছে গিয়ে আমরা ঢেউ দেখলাম।"),
        ("থেকে", "ঘর থেকে বেরিয়ে সে মাঠে গেল।"),
        ("পক্ষে", "এত ভারী বোঝা তোলা তার পক্ষে সম্ভব নয়।"),
]:
    add("S03", "মূল কাঠামো", A_EX3,
        sa(f"'{w}' শব্দটি ব্যবহার করে একটি অর্থপূর্ণ বাক্য লেখো।", [sample], OWN_SENT),
        topic="TOP-BAN-C5-02", ref19="BAN-SENTENCE", bloom="Apply", diff="medium", marks=1)

for pair, joined in [
        ("পুস্তকটি ছোটো। পুস্তকটি খুব দরকারি।", "পুস্তকটি ছোটো কিন্তু খুব দরকারি।"),
        ("সাগর অনেক বড়ো। সাগরের জল নোনতা।", "সাগর অনেক বড়ো এবং এর জল নোনতা।"),
]:
    add("S03", "মূল কাঠামো", A_EX4,
        sa(f"'{pair}' — বাক্য দুটি জোড়া দিয়ে একটি বাক্য লেখো।", [joined],
           "যোগ-শব্দ (এবং · ও · কিন্তু · আর) ঠিকভাবে বসিয়ে অর্থ অটুট রেখে একটি পূর্ণ বাক্য হলেই "
           "পূর্ণ নম্বর; শব্দে শব্দে মিল থাকা জরুরি নয়।"),
        topic="TOP-BAN-C5-02", ref19="BAN-SENTENCE", bloom="Apply", diff="medium", marks=1)

for one, split in [
        ("প্রভাত হলো আর পাখিরা ঘর থেকে বেরিয়ে পড়ল।", "প্রভাত হলো। পাখিরা ঘর থেকে বেরিয়ে পড়ল।"),
        ("জননী রান্না করছেন এবং কন্যা তাঁকে সাহায্য করছে।",
         "জননী রান্না করছেন। কন্যা তাঁকে সাহায্য করছে।"),
]:
    add("S03", "মূল কাঠামো", A_EX5,
        sa(f"'{one}' — বাক্যটি ভেঙে দুটি বাক্য লেখো।", [split],
           "দুটি ভাগই আলাদা পূর্ণ বাক্য হতে হবে এবং প্রতিটির শেষে দাঁড়ি বসবে; যোগ-শব্দটি বাদ যাবে।"),
        topic="TOP-BAN-C5-02", ref19="BAN-SENTENCE", bloom="Apply", diff="medium", marks=1)

add("S03", "মূল কাঠামো", A_EX7,
    sa("'ঘর' শব্দটির সঙ্গে অন্ত্যমিল আছে এমন একটি শব্দ বেছে নিয়ে সেই শব্দ দিয়ে একটি বাক্য লেখো।",
       ["নদীর চরে সাদা পাখি বসে আছে।"],
       "'ঘর'-এর সঙ্গে অন্ত্যমিল আছে এমন শব্দ — চর · বর। যেকোনো একটি শুদ্ধ মিল-শব্দ নিয়ে "
       "লেখা যেকোনো শুদ্ধ বাক্য গ্রহণযোগ্য; নমুনা উত্তর দেওয়া হলো।"),
    topic="TOP-BAN-C5-02", ref19="BAN-RHYME", bloom="Apply", diff="hard", marks=1)

# ══════════════════════════════════════════════════════════════════════════════════════
# S04 · শূন্যস্থান পূরণ — task "মূল কাঠামো" · 1 mark per blank
# অনুশীলনী ২ is "গুণ ও বৈশিষ্ট্য বসানো (বিশেষণ)" — a BSANO (placing) task, and the source's own
# ছক routes it to S04 by name. Three items is what the chapter carries: it prints exactly one
# adjective pair (ক্ষুদ্র/ছোটো), so the rest of S04 rests on the pair list and the chapter's own
# stated facts. This slot is THIN and the bank says so rather than filling it out.
# ══════════════════════════════════════════════════════════════════════════════════════
for text, acc, anchor, bloom, diff in [
        ("'পিঁপড়া খুব ______ প্রাণী।' — পাঠ ১৯-এর শব্দতালিকা থেকে আকার বোঝায় এমন একটি "
         "বিশেষণ বসিয়ে শূন্যস্থান পূরণ করো।",
         ["ক্ষুদ্র", "ছোটো"], A_EX2, "Understand", "easy"),
        ("'রজনী শেষ হলে ______ আসে।' — পাঠ ১৯-এর শব্দতালিকার একটি শব্দ বসিয়ে শূন্যস্থান "
         "পূরণ করো।",
         ["প্রভাত", "সকাল", "দিন", "দিবস"], A_EX6, "Remember", "easy"),
        ("'পাঠ ১৯-এর অনুশীলনীতে ______ জোড়া একই রকম শব্দ দেওয়া আছে।' — শূন্যস্থান পূরণ করো।",
         ["বারো", "১২"], A_BEST, "Remember", "easy"),
]:
    add("S04", "মূল কাঠামো", anchor,
        {"question_text": text, "question_type": "fill_blank", "paper_role": "short",
         "blanks": [{"blank_no": 1, "accepted": acc, "marks": 1}]},
        topic="TOP-BAN-C5-01", ref19="BAN-VOCAB", bloom=bloom, diff=diff, marks=1)

# ══════════════════════════════════════════════════════════════════════════════════════
# S05 · বহুনির্বাচনি — task "মূল কাঠামো" · 1 mark
# বহুনির্বাচনি is a FORM, not a content type; the pairs and the chapter's own facts supply it.
# ══════════════════════════════════════════════════════════════════════════════════════
MCQ = [
    ("পাঠ ১৯-এর তালিকা অনুযায়ী 'ঘর' শব্দটির একই রকম শব্দ কোনটি?",
     [("বাড়ি", True, None),
      ("মাঠ", False, "মাঠ খোলা জায়গা বোঝায়, ঘর নয়।"),
      ("পথ", False, "পথ চলার জায়গা; ঘরের সঙ্গে অর্থের মিল নেই।"),
      ("নদী", False, "নদী জলের ধারা; তালিকায় ঘরের জোড়া হিসেবে এটি নেই।")],
     A_EX6, "TOP-BAN-C5-01", "BAN-VOCAB", "Remember", "easy"),
    ("পাঠ ১৯ কোন ধরনের পাঠ?",
     [("ব্যাকরণ-অনুশীলন", True, None),
      ("কবিতা", False, "এই পাঠে কোনো কবিতা বা চরণ নেই।"),
      ("নাটক", False, "এই পাঠে কোনো সংলাপ বা অভিনয়ের অংশ নেই।"),
      ("গল্প", False, "পাঠটি নিজেই বলছে এখানে কোনো কাহিনি নেই।")],
     A_KIND, "TOP-BAN-C5-02", "BAN-SENTENCE", "Remember", "easy"),
    ("'দিয়ে · উপর · কাছে · থেকে · পক্ষে' — পাঠ ১৯-এ এই শব্দগুলো নিয়ে কী করতে বলা হয়েছে?",
     [("বাক্য তৈরি করতে", True, None),
      ("যুক্তবর্ণ ভাঙতে", False, "যুক্তবর্ণ ভাঙা এই পাঠের কোনো অনুশীলনী নয়।"),
      ("বিপরীত শব্দ লিখতে", False, "এই শব্দগুলো দিয়ে বিপরীত শব্দ লেখার কথা পাঠে নেই।"),
      ("ছবি দেখে নাম লিখতে", False, "এমন কোনো কাজ এই পাঠের অনুশীলনীতে নেই।")],
     A_EX3, "TOP-BAN-C5-02", "BAN-SENTENCE", "Understand", "easy"),
    ("'একটি বাক্য ভেঙে দুটি' — পাঠ ১৯-এর এই অনুশীলনীটি কোন ধরনের কাজ?",
     [("বাক্য গঠন", True, None),
      ("শব্দার্থ", False, "শব্দার্থে শব্দের মানে লিখতে হয়, বাক্য ভাঙতে হয় না।"),
      ("যুক্তবর্ণ", False, "যুক্তবর্ণে বর্ণ ভাঙা হয়, বাক্য নয়।"),
      ("মূলভাব", False, "মূলভাব লিখতে একটি মূল পাঠ লাগে, যা এই পাঠে নেই।")],
     A_EX5, "TOP-BAN-C5-02", "BAN-SENTENCE", "Understand", "medium"),
]
for text, opts, anchor, topic, ref19, bloom, diff in MCQ:
    options = []
    for oid, (t, ok, why) in zip("কখগঘ", opts):
        o = {"option_id": oid, "text": t, "is_correct": ok}
        if not ok:
            o["why_wrong"] = why
        options.append(o)
    add("S05", "মূল কাঠামো", anchor,
        {"question_text": text, "question_type": "mcq", "paper_role": "mcq", "options": options},
        topic=topic, ref19=ref19, bloom=bloom, diff=diff, marks=1)

# ══════════════════════════════════════════════════════════════════════════════════════
# S06 · বিপরীত শব্দ — task "বিপরীত শব্দ" (C5's SELECTED form) · 1 mark
# NOT সমার্থক. সমার্থক is in this slot's admitted_set and C5 did not select it, so a সমার্থক item
# here would be OFF-CHOICE (CD-138(b)) — which is exactly why the chapter's twelve pairs are used
# at S02/S13/S05 and never at S06 as pairs.
# ══════════════════════════════════════════════════════════════════════════════════════
for w, acc, anchor, bloom, diff in [
        ("ক্ষুদ্র", ["বৃহৎ", "বিশাল", "বড়ো"], A_EX6, "Understand", "medium"),
        ("দিন", ["রাত", "রজনী"], A_EX6, "Remember", "easy"),
        ("মাতা", ["পিতা"], A_EX6, "Understand", "easy"),
        ("ছেলে", ["মেয়ে"], A_EX6, "Remember", "easy"),
        ("উপর", ["নিচ", "নিচে"], A_EX3, "Understand", "easy"),
]:
    add("S06", "বিপরীত শব্দ", anchor,
        sa(f"'{w}' — পাঠ ১৯-এর শব্দতালিকায় থাকা এই শব্দটির বিপরীত শব্দ লেখো।", acc, ANTONYM_NOTE),
        topic="TOP-BAN-C5-01", ref19="BAN-WORDREL", bloom=bloom, diff=diff, marks=1)

# ══════════════════════════════════════════════════════════════════════════════════════
# S07 · সংক্ষিপ্ত উত্তর — task "মূল কাঠামো" · 2 marks
# The chapter IS an exercise set, so "what does this piece of language work ask for" is its own
# comprehension content. FOUR items is all of it: there is no narrative to ask about.
# The last one is where TOP-BAN-C5-15 (ব্যবহারিক লিখন) gets its FIRST live carry in this repo.
# ══════════════════════════════════════════════════════════════════════════════════════
for text, acc, note, anchor, topic, ref19, bloom, diff in [
        ("পাঠ ১৯-এ কোনো মূল পাঠ নেই — তাহলে এই পাঠে কী আছে? সংক্ষেপে লেখো।",
         ["এই পাঠে কোনো কাহিনি বা মূল পাঠ নেই; আছে কেবল ভাষার নানা কাজের অনুশীলনী — ক্রিয়ার কাল, "
          "বিশেষণ বসানো, শব্দ দিয়ে বাক্য তৈরি, বাক্য জোড়া দেওয়া ও ভাঙা, একই রকম শব্দ এবং অন্ত্যমিল।"],
         "মূল কথা দুটি ধরা পড়লেই পূর্ণ নম্বর — (১) কোনো কাহিনি বা মূল পাঠ নেই, (২) কেবল ভাষার কাজের "
         "অনুশীলনী আছে। তিন-চারটি অনুশীলনীর নাম লিখলেই যথেষ্ট।",
         A_KIND, "TOP-BAN-C5-02", "BAN-SENTENCE", "Understand", "easy"),
        ("'একই রকম শব্দ' বলতে কী বোঝায়? পাঠ ১৯-এর তালিকা থেকে দুই জোড়া উদাহরণ দাও।",
         ["যে শব্দগুলোর অর্থ এক বা প্রায় এক, সেগুলোকে একই রকম শব্দ বলে। যেমন — রজনী ও রাত, "
          "পুস্তক ও বই।"],
         "সংজ্ঞার জন্য এক নম্বর, তালিকা থেকে দুই জোড়া সঠিক উদাহরণের জন্য এক নম্বর। তালিকার যেকোনো "
         "দুই জোড়াই গ্রহণযোগ্য।",
         A_EX6, "TOP-BAN-C5-01", "BAN-VOCAB", "Understand", "easy"),
        ("'দুটি বাক্য জোড়া দিয়ে একটি' আর 'একটি বাক্য ভেঙে দুটি' — কাজ দুটির পার্থক্য সংক্ষেপে লেখো।",
         ["প্রথম কাজে দুটি আলাদা বাক্যকে যোগ-শব্দ দিয়ে জুড়ে একটি বাক্য বানাতে হয়; দ্বিতীয় কাজে "
          "একটি বাক্যকে ভেঙে দুটি আলাদা পূর্ণ বাক্য বানাতে হয়। একটিতে বাক্যের সংখ্যা কমে, "
          "অন্যটিতে বাড়ে।"],
         "দুই দিকের কাজ আলাদা করে বোঝাতে পারলেই পূর্ণ নম্বর; উদাহরণ দিলে ভালো, কিন্তু আবশ্যক নয়।",
         A_EX4, "TOP-BAN-C5-02", "BAN-SENTENCE", "Analyze", "hard"),
        ("পাঠ ১৯-এর অনুশীলনীতে দৈনিক পত্রিকা নিয়ে কোন কাজটি করতে বলা হয়েছে?",
         ["দৈনিক পত্রিকা থেকে তিনটি খবরের শিরোনাম বেছে নিয়ে লিখতে বলা হয়েছে।"],
         "'পত্রিকা থেকে খবরের শিরোনাম' এবং 'তিনটি' — এই দুটি তথ্য থাকলেই পূর্ণ নম্বর।",
         A_EX8, "TOP-BAN-C5-15", "BAN-FUNCWRITE", "Remember", "easy"),
]:
    add("S07", "মূল কাঠামো", anchor, sa(text, acc, note),
        topic=topic, ref19=ref19, bloom=bloom, diff=diff, marks=2)

# ══════════════════════════════════════════════════════════════════════════════════════
# S10 · পদ নির্ণয় — task "পদ নির্ণয়" (C5's SELECTED form) · 1 mark
# NOT ক্রিয়ার কাল. অনুশীলনী ১ is the tense exercise and the source's ছক names পাঠ ১৯ for it —
# "১৯ (কাল)" — but C5 selected পদ নির্ণয়, so the tense exercise goes unused rather than being
# re-labelled. অনুশীলনী ২ (বিশেষণ) is what carries this slot: a বিশেষণ IS a পদ.
# Every stimulus is built from words the chapter prints.
# ══════════════════════════════════════════════════════════════════════════════════════
NOUN = ["বিশেষ্য", "বিশেষ্য পদ", "নাম-শব্দ"]
ADJ = ["বিশেষণ", "বিশেষণ পদ"]
VERB = ["ক্রিয়া", "ক্রিয়া পদ", "কাজ-শব্দ"]
for sent, word, acc, anchor, diff in [
        ("ক্ষুদ্র পিঁপড়াও দল বেঁধে চলে।", "ক্ষুদ্র", ADJ, A_EX2, "easy"),
        ("জননী কন্যাকে ডাকলেন।", "জননী", NOUN, A_EX6, "easy"),
        ("ছেলেটি পুস্তক পড়ে।", "পড়ে", VERB, A_EX2, "medium"),
        ("সাগরের জল খুব নোনতা।", "নোনতা", ADJ, A_EX2, "medium"),
        ("প্রভাতে সাগর শান্ত থাকে।", "সাগর", NOUN, A_EX6, "easy"),
]:
    add("S10", "পদ নির্ণয়", anchor,
        sa(f"'{sent}' — এখানে '{word}' শব্দটি কোন পদ? নির্ণয় করো।", acc, POD_NOTE),
        topic="TOP-BAN-C5-01", ref19="BAN-PARTSPEECH", bloom="Understand", diff=diff, marks=1)

# ══════════════════════════════════════════════════════════════════════════════════════
# S12 · যুক্তবর্ণ ও শব্দ গঠন — COMPOSITE, task ["যুক্তবর্ণ ভাঙা", "শব্দ গঠন"] · 1 mark
# Both parts or the item does half the task (CD-138(b)). Every conjunct below is inside a word
# পাঠ ১৯ actually prints.
# ══════════════════════════════════════════════════════════════════════════════════════
for word, juk, parts, samples, anchor in [
        ("প্রভাত", "প্র", "প্ + র", ["প্রদীপ", "প্রজাপতি"], A_EX6),
        ("পুস্তক", "স্ত", "স্ + ত", ["বস্তু", "হস্ত"], A_EX6),
        ("ক্ষুদ্র", "ক্ষ", "ক্ + ষ", ["ক্ষমা", "পক্ষ"], A_EX6),
        ("সমুদ্র", "দ্র", "দ্ + র", ["দ্রুত", "ভদ্র"], A_EX6),
        ("পত্রিকা", "ত্র", "ত্ + র", ["ছাত্র", "পত্র"], A_EX8),
]:
    add("S12", ["যুক্তবর্ণ ভাঙা", "শব্দ গঠন"], anchor,
        sa(f"পাঠ ১৯-এর '{word}' শব্দে থাকা '{juk}' যুক্তবর্ণটি ভেঙে দেখাও, আর সেই যুক্তবর্ণ দিয়ে "
           f"নতুন একটি শব্দ গঠন করো।",
           [f"{juk} = {parts}; নতুন শব্দ — {samples[0]}", f"{juk} — {parts}; {samples[1]}"],
           JUK_NOTE),
        topic="TOP-BAN-C5-01", ref19="BAN-JUKTOBARNA", bloom="Apply", diff="medium", marks=1)

# ══════════════════════════════════════════════════════════════════════════════════════
# S13 · এক কথায় প্রকাশ — task "মূল কাঠামো" · 1 mark
# A descriptive phrase in, ONE printed word out. The pairs used here are disjoint from S02's, so
# no pair is asked twice in opposite directions — §4's near-duplicate ban applied by hand, since
# no count gate constrains this bank any more (CD-171(a)).
# ══════════════════════════════════════════════════════════════════════════════════════
for phrase, acc, anchor, bloom, diff in [
        ("মানুষ যেখানে বসবাস করে", ["ঘর", "বাড়ি"], A_EX6, "Understand", "easy"),
        ("যিনি জন্ম দিয়েছেন", ["জননী", "মাতা"], A_EX6, "Understand", "easy"),
        ("যে সন্তান বালিকা", ["কন্যা", "মেয়ে"], A_EX6, "Remember", "easy"),
        ("যে সন্তান বালক", ["পুত্র", "ছেলে"], A_EX6, "Remember", "easy"),
        ("নোনা জলের বিশাল জলরাশি", ["সাগর", "সমুদ্র"], A_EX6, "Understand", "medium"),
]:
    add("S13", "মূল কাঠামো", anchor,
        sa(f"'{phrase}' — পাঠ ১৯-এর শব্দতালিকার শব্দ দিয়ে এক কথায় প্রকাশ করো।", acc, PAD_NOTE),
        topic="TOP-BAN-C5-01", ref19="BAN-VOCAB", bloom=bloom, diff=diff, marks=1)


# ══════════════════════════════════════════════════════════════════════════════════════
# ASSEMBLE
# ══════════════════════════════════════════════════════════════════════════════════════
def norm(s):
    s = unicodedata.normalize("NFC", s or "")
    s = re.sub(r"[‘’“”'\"()\[\]।,;:?!—–\-….*_#>|/·]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


full = (ROOT / SRC).read_text(encoding="utf-8")
m = re.search(r"^#\s*পাঠ\s*১৯\b.*?$", full, re.M)
assert m, "পাঠ ১৯ section not found in the extraction"
rest = full[m.end():]
nxt = re.search(r"^#\s*পাঠ\s", rest, re.M)
section = rest[: nxt.start()] if nxt else rest
nsec = norm(section)
for name, a in [("A_EX1", A_EX1), ("A_EX2", A_EX2), ("A_EX3", A_EX3), ("A_EX4", A_EX4),
                ("A_EX5", A_EX5), ("A_EX6", A_EX6), ("A_EX7", A_EX7), ("A_EX8", A_EX8),
                ("A_KIND", A_KIND), ("A_NOSTORY", A_NOSTORY), ("A_BEST", A_BEST),
                ("A_ARUN", A_ARUN)]:
    assert norm(a) in nsec, f"{name} is NOT a verbatim span of the পাঠ ১৯ section"
    assert len(norm(a).split()) >= 3, f"{name} is under the 3-token anchor floor"

questions, slot_index, task_index, source_index = [], {}, {}, {}
pool_index = {"HW": [], "AS": [], "CT": []}
for i, it in enumerate(ITEMS, start=1):
    qid = f"QP-BAN-C5-U19-Q{i:02d}"
    q = {"qid": qid, "topic_tag": it["topic"], "ref19_topic_id": it["ref19"]}
    q.update({k: v for k, v in it["q"].items() if k != "answer_key"})
    q.update({"bloom_level": it["bloom"], "difficulty": it["diff"], "tier": "tier1",
              "marks": it["marks"], "chapter_ref": CHAP})
    if "answer_key" in it["q"]:
        q["answer_key"] = it["q"]["answer_key"]
    # key order: keep the payload readable, schema is order-independent
    questions.append(q)
    slot_index[qid] = it["slot"]
    task_index[qid] = it["task"]
    source_index[qid] = it["anchor"]
    j = i - 1
    pool_index["CT" if j % 7 == 0 else ("AS" if j % 7 in (1, 2) else "HW")].append(qid)

ADMISSIBLE = ["S02", "S03", "S04", "S05", "S06", "S07", "S10", "S12", "S13"]
EXCLUSIONS = {
    "S01": ("পাঠ ১৯-এ মুখস্থ করার মতো একটিও কবিতাংশ ছাপা নেই — পাঠের নিজের লাইন "
            "'ব্যাকরণ-অনুশীলন (কোনো মূল পাঠ নেই, শুধু অনুশীলনী)' — এবং কারণটি অনুমান নয়, উৎসের "
            "নিজের বাক্য: 'কবিতা চারটি: পাঠ ১৩, ১৫, ১৮, ২০ — এগুলোই S01 (কবিতা মুখস্থ) ও S09 "
            "(মূলভাব) প্রশ্নের উৎস।' পাঠ ১৯ সেই চারটির একটিও নয়।"),
    "S08": ("পাঁচ নম্বরের গোছানো বিস্তৃত উত্তরের জন্য যে ঘটনা, চরিত্র বা যুক্তির সূত্র দরকার তার "
            "একটিও এই পাঠ ছাপে না — যা আছে তা দশটি অনুশীলনী-শিরোনাম আর একটি শব্দতালিকা, আর "
            "তালিকা লেখা তালিকা মুখস্থই, বিস্তৃত উত্তর নয়; ব্যান্ডভিত্তিক rubric যে পার্থক্য মাপে, "
            "মাপার মতো সেই বিষয়বস্তুই এখানে নেই।"),
    "S09": ("মূলভাব লিখতে একটি মূল পাঠ লাগে এবং এই পাঠে কোনো মূল পাঠ নেই; উৎসের যে বাক্যটি "
            "S01-কে চার কবিতায় বেঁধেছে সেই একই বাক্য S09-কেও বেঁধেছে, আর পাঠ ১৯ সেই চারটির "
            "একটিও নয়।"),
    "S11": ("পাঠের অনুশীলনীর বিষয় ছকে দশটি কাজের একটিও বিরামচিহ্ন নিয়ে নয়, এবং পাঠটি বিরামচিহ্ন "
            "বসানোর মতো একটিও বাক্য ছাপে না — একমাত্র ছাপা বাক্যটি C-04-এ নিষিদ্ধ; উদ্দীপকটি "
            "পুরোপুরি রচনা করতে হতো, আর সেটি এমন একটি কাজ চালাত যা এই পাঠ ধরায়ই না। "
            "(তুলনা: S03-এ উদ্দীপক রচনা বৈধ, কারণ বাক্য জোড়া ও বাক্য ভাঙা পাঠের নিজের ছাপা কাজ।)"),
}

bank = {
    "schema_version": "1.0",
    "policy_shape": "qp6",
    "bank_id": "QB-BAN-C5-U19",
    "wave": 1,
    "subject": "BAN",
    "class": 5,
    "chapter": CHAP,
    "extraction_path": SRC,
    "source_extraction": SRC,
    "curation": (
        "FLEXIBLE · পাঠ ১৯-এর ⚠ ব্লকের তিনটি ধারার প্রতিটি এখানে মানা হয়েছে। (১) C-04 — "
        "'আমরা সবাই মিলে মেলায় যাচ্ছি' বাক্যটি এই ব্যাংকের কোথাও নেই, কোনো আইটেমে, কোনো "
        "উত্তরে, কোনো rubric-এ নয়; উৎস নিজেই বলেছে 'প্রশ্নে অন্য বাক্য বসাতে হবে', আর এই "
        "ব্যাংকের প্রতিটি রচিত উদ্দীপক পাঠেরই ছাপা শব্দ দিয়ে গড়া। (২) অনুশীলনী ১০-এর "
        "রাজা-তরমুজের গল্প — উৎস একে শ্রেণিকক্ষের কাজ বলেছে, প্রশ্নপত্রে নয়; এই ব্যাংকে "
        "অনুশীলনী ১০ থেকে একটিও আইটেম নেই এবং কোনো anchor সেখানে পৌঁছায় না। (৩) অনুশীলনী "
        "৬-এর অরুণ · রবি · রজনী — উৎস স্পষ্ট করেই বলেছে এগুলো সাধারণ বাংলা সমার্থক শব্দ, "
        "ব্যবহারে বাধা নেই; রজনী ব্যবহৃত হয়েছে, আর অরুণ ও রবি শেষ পর্যন্ত কোনো আইটেমে বসেনি — "
        "কারণটি এই ⚠ ধারা নয়, কারণ পাঠ জোড়াটির অর্থ কোথাও লেখে না। এর বাইরে: কোনো কাল্পনিক ব্যক্তিনাম নেই, "
        "কোনো ছবি নেই ও চাওয়া হয়নি, কোনো গান-উৎসব-আচারের প্রসঙ্গ নেই।"),
    "header": {
        "target": len(questions),
        "reason": (
            f"{len(questions)}টি — এবং সংখ্যাটি কোনো লক্ষ্য নয়, একটি ফলাফল। CD-171(a)-এর পরে "
            "কোনো মেঝে, কোনো ছাদ, কোনো Bloom ব্যান্ড ও কোনো প্রতি-স্লট দাবি পুলের উপর বসে না; "
            "একমাত্র বাঁধন §4-এর near-duplicate নিষেধ। পাঠ ১৯ ছাপে ২৯টি শব্দ (১২ জোড়া সমার্থকের "
            "২৪ + অনুশীলনী ৩-এর ৫) ও ১০টি কাজের নাম। প্রতিটি শব্দকে একবার একটি কাজে বসানোর পর "
            "নতুন প্রশ্ন মানেই পুরোনো প্রশ্নের পুনরাবৃত্তি — সেখানেই থামা হয়েছে। সীমাটি এই "
            "পাঠের বিষয়বস্তুর, extraction-এর নয়: পাঠ ১৯-এর কোনো 'পূর্ণ পাঠ' বইয়েও নেই "
            "(উৎসের এক নজরে ছক: ধরন ব্যাকরণ-অনুশীলন, পৃষ্ঠা ১০৭–১১১), তাই extraction পাঠের "
            "গোটা রূপই বহন করছে, তার অংশ নয়।"),
        "topics": ["TOP-BAN-C5-01", "TOP-BAN-C5-02", "TOP-BAN-C5-15"],
        "spine_slots": [f"S{n:02d}" for n in range(1, 16)],
        "admissible_slots": ADMISSIBLE,
        "slot_exclusions": EXCLUSIONS,
        "admissibility_declaration": (
            "CD-138(e), পাঠ ১৯-এর নিজস্ব ঘোষণা, canon/marklogic/C5_Bangla_Source_13-23.md-এর "
            "পাঠ ১৯ অংশ (লাইন ৪১২–৪৪৩) থেকে উৎসে লেখা — পাঠ ১২ পড়া হয়নি (CD-127(b))। "
            "রেজিস্টারে BAN C5-এর পনেরোটি স্লট। এর মধ্যে দুটি — S14 আবেদনপত্র ও S15 রচনা — "
            "CD-147 অনুযায়ী প্রতিটি পাঠের জন্যই কাগজ-স্তরের, শ্রেণিগতভাবে; কোনো পাঠ এদের জন্য "
            "বিষয়বস্তুর কারণ দেখানোর দায়ে নেই এবং এই ঘোষণা তাদের নিয়ে কিছুই বলে না, যা "
            "CD-147(c) অনুযায়ী সঠিক, অসম্পূর্ণ নয়। বাকি তেরোটির মধ্যে নয়টি স্বীকৃত এবং চারটি — "
            "S01 · S08 · S09 · S11 — বাদ, প্রতিটির এক লাইনের বিষয়বস্তু-কারণসহ slot_exclusions-এ। "
            "চারটি বাদের কারণই বিষয়বস্তুর, পাঠের নিজস্ব 'কোন প্রশ্নে কাজে লাগবে' লাইনের নয় — "
            "CD-134(c) সেই কারণ নাম ধরে নিষিদ্ধ করে, কারণ দুটি header-এ একরকম দেখায় অথচ এক নয়। "
            "বিশেষভাবে S11: কারণটি পাঠের 'অনুশীলনীর বিষয়' ছক, অর্থাৎ পাঠের প্রকৃত বিষয়বস্তু — "
            "দশটি কাজের একটিও যতিচিহ্ন নয় এবং যতিচিহ্নযুক্ত কোনো বাক্য ছাপা নেই। "
            "CD-142(b) অনুযায়ী পরিকল্পনার কাউন্টারসাইন এখন PLAN গেট, মানুষের সই নয়।"),
        "slot_counts": {s: sum(1 for v in slot_index.values() if v == s) for s in ADMISSIBLE},
        "topic_tag_ruling": (
            "canon/topics/TOPIC_NUMBERS.md-এর পাঠ-ধরন ছক পাঠ ১৯-কে নাম ধরে দুটি সংখ্যা দিয়েছে — "
            "'১৯ ভাষার খেলা | ব্যাকরণ-অনুশীলন | -02 এবং -15 (minted)'। topic_tag প্রতি-প্রশ্নের "
            "ক্ষেত্র, প্রতি-অধ্যায়ের নয়: শব্দার্থ · বিপরীত শব্দ · এক কথায় প্রকাশ · পদ নির্ণয় · "
            "যুক্তবর্ণ ও শূন্যস্থানের আইটেম TOP-BAN-C5-01 (শব্দার্থ, BAN-VOCAB পরিবার) বহন করে; "
            "বাক্য গঠন ও পাঠ-পরিচয়ের আইটেম TOP-BAN-C5-02 (বাক্য-রচনা, BAN-SENTENCE)। "
            "TOP-BAN-C5-15 (ব্যবহারিক লিখন, BAN-FUNCWRITE) বহন করে একটিমাত্র আইটেম — অনুশীলনী "
            "৮-এর দৈনিক পত্রিকার খবরের শিরোনাম নিয়ে S07 প্রশ্নটি, এই পাঠের একমাত্র প্রায়োগিক "
            "লিখনের উপাদান। সংখ্যাটি TOPIC_NUMBERS.md-এ উৎসে যাচাই করা: MINTED 2026-08-14, "
            "পাঠ ১৯ + ২৩-এর জন্য, PENDING-P-008-এর C5 বাংলা অর্ধ CLOSED। রেপোর চারটি জীবিত "
            "ব্যাংকে -15 বহনকারী আইটেমের সংখ্যা শূন্য, তাই এই আইটেমটিই সংখ্যাটির প্রথম জীবিত "
            "ব্যবহার (QB-CR-014(d): উদ্দেশ্যের জন্য মিন্ট করা সংখ্যা ব্যবহারে আসে না যতক্ষণ না "
            "কিছু একটা সেটি বহন করে)। অন্ত্যমিলের আইটেমটি ref19_topic_id হিসেবে BAN-RHYME বহন "
            "করে — REF-19-এর নিজস্ব slug, বানানো নয়।"),
        "content_facts": (
            "CD-135(d) — শূন্য স্তরগুলো বিষয়বস্তুর তথ্য হিসেবে এখানে বলা হলো: এই পুলে "
            "Evaluate ০ এবং Create ০। পাঠ ১৯-এ মতামত বা মূল্যায়নের কোনো সূত্র নেই — কোনো ঘটনা, "
            "চরিত্র বা যুক্তি নেই যার উপর ভালো-মন্দের বিচার চাওয়া যায় — আর দশটি অনুশীলনীর "
            "একটিও নতুন রচনা তৈরির নয়; যেটি সবচেয়ে কাছে যায় (অনুশীলনী ১০, ধারাবাহিক গল্প) "
            "উৎসের ⚠ ব্লকে নাম ধরে প্রশ্নপত্র থেকে নিষিদ্ধ। Analyze ১টি — জোড়া দেওয়া ও ভাঙার "
            "পার্থক্যের প্রশ্ন — এবং সেটিই এই পাঠের একমাত্র তুলনামূলক সূত্র।"),
        "gaps": [
            "S14 · S15 — CD-147 অনুযায়ী কাগজ-স্তরের, শ্রেণিগতভাবে; এই পাঠ এদের নিয়ে কিছু ঘোষণা "
            "করে না এবং করার দায়ও নেই (CD-147(c))।",
            "অনুশীলনী ১ (ক্রিয়ার কাল — আগেকার / এখনকার / পরের) ব্যবহার করা হয়নি, এবং কারণটি "
            "বিষয়বস্তুর অভাব নয়। ক্রিয়ার কাল BAN-S10-এর admitted_set-এর সদস্য, কিন্তু C5 "
            "নির্বাচন করেছে পদ নির্ণয়; নির্বাচনের বাইরের কাজ লিখলে COVERAGE ও PLAN দুটোই "
            "off-choice ধরে (CD-138(b))। এটি এই পাঠের সবচেয়ে বড় ক্ষতি — উৎসের ছক পাঠ ১৯-কে "
            "S10-এ ডাকে ঠিক '১৯ (কাল)' বলেই, অর্থাৎ যে রূপের জন্য একে সুপারিশ করা হয়েছে "
            "শ্রেণিটি সেই রূপটিই নির্বাচন করেনি।",
            "অনুশীলনী ৬-এর ১২ জোড়া সরাসরি 'সমার্থক শব্দ লেখো' আকারে ব্যবহার করা হয়নি, একই "
            "কারণে: সমার্থক শব্দ BAN-S06-এর admitted_set-এ আছে কিন্তু C5 বিপরীত শব্দ নির্বাচন "
            "করেছে। উৎস এই তালিকাকে 'সবচেয়ে ভালো উৎস' বলেছে, আর শ্রেণির নির্বাচন তার সবচেয়ে "
            "সরাসরি রূপটিই বন্ধ করে দেয়। জোড়াগুলো তাই S02 (অর্থ), S13 (এক কথায় প্রকাশ) ও "
            "S05 (বহুনির্বাচনি)-তে কাজে লেগেছে।",
            "অনুশীলনী ৯ (শব্দ-জব্দ / ক্রসওয়ার্ড) ও ১০ (ধারাবাহিক গল্প) ব্যবহার করা হয়নি। "
            "উৎসের ছকে দুটিরই উৎস-ঘর '—', অর্থাৎ কোনো S-স্লটের উৎস নয়; আর ১০ ⚠-এ নাম ধরে "
            "নিষিদ্ধ ('রাজা-তরমুজের গল্প — শ্রেণিকক্ষের কাজ, প্রশ্নপত্রে নয়')।",
            "S04 পাতলা এবং সেটি বলা হচ্ছে, ঢাকা হচ্ছে না: অনুশীলনী ২ শূন্যস্থানের কাজ ঠিকই, "
            "কিন্তু পাঠ একটিমাত্র বিশেষণ-জোড়া (ক্ষুদ্র/ছোটো) ছাপে এবং শূন্যস্থান বসানোর মতো "
            "কোনো বাক্য ছাপে না। তিনটি আইটেমই এই পাঠ যা বহন করে তার পূর্ণ পরিমাণ।",
        ],
    },
    "flags": [],
    "pool_index": pool_index,
    "slot_index": slot_index,
    "task_index": task_index,
    "source_index": source_index,
    "questions": questions,
    "waves": {"1": (f"Q01–Q{len(questions):02d} · 2026-08-18 · author_U19_wave1.py · পাঠ ১৯-এর "
                    "প্রথম ব্যাংক, CD-141 teacher-lane-এ authored, CD-171(a)-এর পরে — কোনো "
                    "কাউন্ট গেট এই সংখ্যাটি বাঁধেনি")},
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(bank, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"wrote {OUT.relative_to(ROOT)} — {len(questions)} items")
for s in ADMISSIBLE:
    print(f"  {s}: {bank['header']['slot_counts'][s]}")
print("  pools:", {k: len(v) for k, v in pool_index.items()})
