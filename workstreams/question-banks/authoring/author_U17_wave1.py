#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""author_U17_wave1.py — C5 Bangla, পাঠ ১৭ (মাটির নিচে পুরানো নগর) question bank, wave 1.

Run from the repo root:
    python3 workstreams/question-banks/authoring/author_U17_wave1.py

WHY THE SCRIPT IS THE ARTIFACT (LOCAL.md, "Artifacts & naming"). A 78-item JSON nobody can
re-derive is not reviewable; this file is what makes the bank reproducible and reviewable AS
CONTENT. It is promoted with its bank.

THE CHAPTER IS গদ্য (তথ্যমূলক), AND THAT IS THE FACT TWO EXCLUSIONS TURN ON.
`canon/marklogic/C5_Bangla_Source_13-23.md`'s এক নজরে table gives পাঠ ১৭'s ধরন as গদ্য (তথ্যমূলক),
and the same file names which chapters source S01 and S09: "কবিতা চারটি: পাঠ ১৩, ১৫, ১৮, ২০ —
এগুলোই S01 (কবিতা মুখস্থ) ও S09 (মূলভাব) প্রশ্নের উৎস।" পাঠ ১৭ is NOT among them, so both slots
are EXCLUDED on the source's own words. The verdict is READ OFF the source, never inferred from
content (CD-138(e) forbids that inference in both directions), and never read off this chapter's
own "কোন প্রশ্নে কাজে লাগবে" line (CD-134).

S14/S15 ARE NOT DECLARED AT ALL, AND THAT IS THE CORRECT SHAPE. CD-147 makes আবেদনপত্র and রচনা
paper-level for EVERY chapter, categorically; a chapter owes no content reason for a slot no
chapter may serve, and a bank silent about them is CORRECT, not INCOMPLETE (CD-147(c)).

TWO OFF-CHOICE TRAPS, AND THE SECOND IS NOT THE ONE THAT WAS FLAGGED.
  · S11. The chapter's ছক says "S11 প্রশ্ন তৈরিকরণ — এই পাঠই একমাত্র সরাসরি উৎস।" প্রশ্ন তৈরি is
    in BAN-S11's `admitted_set` and C5 SELECTED `বিরামচিহ্ন বসানো`. Every S11 item below does
    বিরামচিহ্ন and অনুশীলনী ৩ is unauthored.
  · S10. The same ছক says "S10 ক্রিয়ার কাল (অনুশীলনী ৪)". ক্রিয়ার কাল is in BAN-S10's
    `admitted_set` and C5 SELECTED `পদ নির্ণয়`. অনুশীলনী ৪ is unauthored — and it is NOT
    laundered into S03, where আজ / গতকাল / আগামীকাল would be a tense drill wearing a
    sentence-building label.
  Same shape both times: the ছক names a task the SLOT admits and the CLASS did not select. The
  ছক is authoring evidence, never a task declaration (CD-138(b)).

QB-CR-017 IS OPEN AND IS NOT REPRODUCED HERE. Thirteen S11 items across U13–U16 are each satisfied
by placing ONE terminal mark. Every S11 item below requires at least TWO mark insertions, counted
by diffing the stimulus against the accepted answer — see `s11_work_check()`, which runs before the
file is written and refuses a count of one.

TAUGHT SET — CD-165 as amended by CD-166: দাঁড়ি · কমা · প্রশ্নচিহ্ন · বিস্ময়চিহ্ন · উদ্ধরণ চিহ্ন.
ড্যাশ and সেমিকোলন are BARRED at C5. This chapter prints BOTH — an em-dash in three মূল তথ্য
bullets and three table rows, and a SEMICOLON in the ব্রহ্মপুত্র trade sentence — so no S11
stimulus is taken from a span whose repair would need one.

THE ⚠ BLOCK.
  · অনুশীলনী ৬ (সংগ্রহ করি — পুরানো কয়েন, অন্য দেশের টাকা, ডাকটিকিট) is শ্রেণিকক্ষের কাজ,
    প্রশ্নপত্রে নয়. No item asks a student to collect, bring or display anything, and nothing is
    authored from that exercise.
  · মন্দির ভিটা / বৌদ্ধ বিহার — the source steers questions to other নিদর্শন (মুদ্রা, দুর্গ,
    বন্দর, বাটখারা). Neither string is in the extraction at all, so no anchor can reach them, and
    every নিদর্শন item names the four the source itself prefers.
  · ✅ বিশেষ সুবিধা's standing requirement — "অন্তত একটি প্রশ্ন 'কীভাবে বোঝা যায়' ধরনের রাখতে
    হবে" — is met by TWO S07 items (Q45, Q46), both tagged Analyze.

NO INVENTED PERSONAL NAME APPEARS ANYWHERE. The only personal names are হানিফ পাঠান and
হাবিবুল্লাহ পাঠান, historical figures the chapter itself records — content facts, not substituted
characters, so QB-CR-005's REF-20 rule is not in play.
"""
import json
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[3]
EXTRACTION = "canon/marklogic/C5_Bangla_Source_13-23.md"
OUT = ROOT / "workstreams/question-banks/banks/C5_BAN_U17_QuestionBank_v1.json"
CHAPTER = "পাঠ ১৭ — মাটির নিচে পুরানো নগর"

# topic_tag / ref19_topic_id pairs. TOPIC_NUMBERS.md gives পাঠ ১৭ (গদ্য তথ্যমূলক) the primary
# number -07 / BAN-INFOTEXT, attested at D-PROJ04-010 and quoted in the chart. Cross-cutting
# strands are per-QUESTION and not per-chapter, which is why six pairs appear.
INFO = ("TOP-BAN-C5-07", "BAN-INFOTEXT")
VOCAB = ("TOP-BAN-C5-01", "BAN-VOCAB")
WORDREL = ("TOP-BAN-C5-01", "BAN-WORDREL")
JUKTO = ("TOP-BAN-C5-01", "BAN-JUKTOBARNA")
PARTSP = ("TOP-BAN-C5-01", "BAN-PARTSPEECH")
SENT = ("TOP-BAN-C5-02", "BAN-SENTENCE")
# -13, not -02, on বিরামচিহ্ন — QB-CR-014's standing lesson. ref19_topic_id stays BAN-SENTENCE
# because REF-19 carries no Bangla punctuation slug (PENDING-P-008, FLAGGED, non-blocking); minting
# one here would be QB-CR-008's mistake in another register.
PUNCT = ("TOP-BAN-C5-13", "BAN-SENTENCE")

# The teacher-gloss provenance line (CD-136(b)). P-037 admits it on `short_answer` and
# `descriptive` only; every item carrying it below is `short_answer`.
TEACHER_KEY = ("এই উত্তরকুঞ্জি শিক্ষকের দেওয়া — বাংলা ভাষার সাধারণ তথ্য, পাঠে এর উত্তর দেওয়া নেই "
               "(CD-136)। উদ্দীপক পাঠ ১৭ থেকেই নেওয়া। কাছাকাছি অর্থের যেকোনো শুদ্ধ উত্তর গ্রহণযোগ্য।")

PADA_KEY = ("এই উত্তরকুঞ্জি শিক্ষকের দেওয়া — বাংলা ব্যাকরণের সাধারণ তথ্য, পাঠে এর উত্তর দেওয়া নেই "
            "(CD-136)। উদ্দীপকটি পাঠেরই। নির্দিষ্ট উত্তরই লাগবে — গৃহীত তালিকার বাইরে কিছু "
            "নেওয়া যাবে না।")

JUKTO_KEY = ("এই উত্তরকুঞ্জি শিক্ষকের দেওয়া — বাংলা ভাষার সাধারণ তথ্য, পাঠে এর উত্তর দেওয়া নেই "
             "(CD-136)। শব্দটি পাঠেরই। দুটি কাজই করতে হবে — শুধু ভাঙলে বা শুধু নতুন শব্দ গঠন করলে "
             "অর্ধেক কাজ। প্রশ্নে যুক্তবর্ণটির নাম বলা আছে, তাই একাধিক যুক্তবর্ণওয়ালা শব্দেও "
             "কোনটি চাওয়া হচ্ছে তা স্পষ্ট।")

SENT_KEY = ("এই উত্তরকুঞ্জি শিক্ষকের দেওয়া — নমুনা বাক্য, পাঠে এই বাক্যটি নেই (CD-136)। "
            "শিক্ষার্থীর নিজের যেকোনো শুদ্ধ বাক্য গ্রহণযোগ্য, যদি শব্দটি সঠিক অর্থে ব্যবহৃত হয় "
            "এবং বাক্যটি বিরামচিহ্নসহ সম্পূর্ণ হয়।")

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


def mcq(opts):
    return {"options": [dict(option_id=oid, text=t, is_correct=True) if ok else
                        dict(option_id=oid, text=t, is_correct=False, why_wrong=w)
                        for oid, t, ok, w in opts]}


def blank(accepted):
    return {"blanks": [{"blank_no": 1, "accepted": accepted, "marks": 1}]}


def rubric(criterion, full, partial):
    return {"rubric": {"bands": ["সম্পূর্ণ", "আংশিক"],
                       "criteria": [{"role": "islamic_alignment", "criterion": criterion,
                                     "band_descriptors": {"সম্পূর্ণ": full, "আংশিক": partial}}]}}


# ── Anchors — every one is a verbatim span of the পাঠ ১৭ section, checked by `selfcheck()` ────
A_NAGAR = "বাংলাদেশ অঞ্চলে প্রাচীনকালে নগর গড়ে উঠেছিল"
A_MAYNA = "কুমিল্লার ময়নামতি (সাত-আট শতক), বগুড়ার মহাস্থানগড় (তৃতীয় শতকের পরে)"
A_UWARI = "উয়ারী ও বটেশ্বর, নরসিংদী জেলার দুটি গ্রাম"
A_KHRIS = "ধারণা করা হয় খ্রিষ্টপূর্ব ছয়-সাত শতকে সেখানে নগর গড়ে ওঠে"
A_2000 = "২০০০ সালে মাটি খনন করে প্রাচীন নগরের রাস্তার নমুনা পাওয়া যায়"
A_FIND = "রৌপ্যমুদ্রা, হাতিয়ার, পাথরের পুঁতি"
A_SHITAL = "শীতলক্ষ্যা নদী ব্রহ্মপুত্রের একটি শাখা"
A_TRADE = "প্রাচীনকালে ব্রহ্মপুত্র নদীপথে বাণিজ্য হতো"
A_ROMAN = "সেই নদী থেকে বঙ্গোপসাগর হয়ে সমুদ্রপথে রোমান সাম্রাজ্যের সাথে যোগাযোগ ছিল"
A_1933 = "উয়ারী গ্রামে একটি পাত্রে জমানো মুদ্রা পাওয়া যায়"
A_HANIF = "স্কুলশিক্ষক হানিফ পাঠান ২০–৩০টি মুদ্রা সংগ্রহ করেন"
A_OLDEST = "এগুলোই এ পর্যন্ত পাওয়া সবচেয়ে পুরানো রৌপ্যমুদ্রা"
A_1955 = "বটেশ্বর গ্রামে দুটি পুরানো লোহার টুকরা — ত্রিকোণাকৃতির, একদিকে সুচালো"
A_1956 = "উয়ারী গ্রামে রৌপ্যমুদ্রার ভান্ডার — প্রায় চার হাজার মুদ্রা"
A_HABIB = "হানিফ পাঠানের পুত্র হাবিবুল্লাহ পাঠান প্রচুর নিদর্শন সংগ্রহ করে জাদুঘরে জমা দেন"
A_KHONON = "প্রত্নতত্ত্ববিদরা খননকাজ শুরু করেন"
A_DURGA = "মাটির নিচে আড়াই হাজার বছরের প্রাচীন দুর্গ-নগর"
A_INVENT = ("পাওয়া যায় ইটের স্থাপত্য, বন্দর, রাস্তা, গলি, পোড়ামাটির ফলক, মূল্যবান পাথর, "
            "পাথরের বাটখারা, কাচের পুঁতি, মুদ্রাভান্ডার")
A_FIFTY = "আশেপাশে প্রায় পঞ্চাশটি পুরানো জায়গার সন্ধান"
A_SONA = "এই সভ্যতা প্রাচীনকালে সোনাগড়া নামে বিশ্বজুড়ে পরিচিত ছিল"

A_ITIHASBID = "ইতিহাসবিদ — ইতিহাস বিষয়ে অভিজ্ঞ যিনি"
A_DURG = "দুর্গ — শত্রুসৈন্য সহজে প্রবেশ করতে পারে না এমন স্থান"
A_NIDARSHAN = "নিদর্শন — প্রমাণ; উদাহরণ"
A_PRATNA = "প্রত্নতত্ত্ববিদ — প্রাচীন ইতিহাস ও উপকরণ নিয়ে কাজ করেন যিনি"
A_MRIT = "মৃত্তিকা — মাটি · রৌপ্যমুদ্রা — রুপার তৈরি মুদ্রা বা টাকা"
A_ROUPYA = "রৌপ্যমুদ্রা — রুপার তৈরি মুদ্রা বা টাকা"
A_SAMRAJYA = "সাম্রাজ্য — সম্রাটের শাসনাধীন রাজ্য"
A_EX1 = "শূন্যস্থান — প্রমাণ · মহাস্থানগড় · ঐতিহাসিক · সভ্যতা · প্রাচীর"


# =====================================================================================
# S02 · শব্দার্থ · simple · marks 1 · 7 items · all Remember, easy
# The seven words ARE the chapter's own অর্থ জেনে নিই list, so the key is IN the chapter and no
# CD-136 teacher-key note is owed. Seven is the list; there is no eighth word to ask about.
# =====================================================================================
S02 = [
    ("ইতিহাসবিদ", ["ইতিহাস বিষয়ে অভিজ্ঞ যিনি", "ইতিহাস বিষয়ে অভিজ্ঞ ব্যক্তি"], A_ITIHASBID),
    ("দুর্গ", ["শত্রুসৈন্য সহজে প্রবেশ করতে পারে না এমন স্থান"], A_DURG),
    ("নিদর্শন", ["প্রমাণ", "উদাহরণ", "প্রমাণ; উদাহরণ"], A_NIDARSHAN),
    ("প্রত্নতত্ত্ববিদ", ["প্রাচীন ইতিহাস ও উপকরণ নিয়ে কাজ করেন যিনি"], A_PRATNA),
    ("মৃত্তিকা", ["মাটি"], A_MRIT),
    ("রৌপ্যমুদ্রা", ["রুপার তৈরি মুদ্রা", "রুপার তৈরি মুদ্রা বা টাকা"], A_ROUPYA),
    ("সাম্রাজ্য", ["সম্রাটের শাসনাধীন রাজ্য"], A_SAMRAJYA),
]
for word, acc, anc in S02:
    add("S02", "মূল কাঠামো", VOCAB,
        f"পাঠে ব্যবহৃত '{word}' শব্দের অর্থ লেখো।",
        "short_answer", "short", "Remember", "easy", 1, anc, **sa(acc))


# =====================================================================================
# S03 · বাক্য গঠন · simple · marks 1 · 10 items · all Apply, medium
# Ten stimulus words the chapter itself prints: the seven glossed words plus সভ্যতা · প্রমাণ ·
# ঐতিহাসিক from অনুশীলনী ১'s own word list. মহাস্থানগড় and প্রাচীর are NOT used — the first is a
# place name and the second never appears in the chapter's prose, only in that word list.
# অনুশীলনী ৪'s আজ / গতকাল / আগামীকাল are NOT used here: they are a ক্রিয়ার কাল drill, and
# relabelling one as বাক্য গঠন would be authoring around C5's S10 selection.
# =====================================================================================
S03 = [
    ("ইতিহাসবিদ", "ইতিহাসবিদরা পুরানো দিনের কথা খুঁজে বের করেন।", A_ITIHASBID),
    ("দুর্গ", "শত্রুরা যাতে ঢুকতে না পারে, সেজন্য রাজারা দুর্গ বানাতেন।", A_DURG),
    ("নিদর্শন", "মাটির নিচে পাওয়া মুদ্রাগুলো প্রাচীন নগরের নিদর্শন।", A_NIDARSHAN),
    ("প্রত্নতত্ত্ববিদ", "প্রত্নতত্ত্ববিদরা মাটি খুঁড়ে পুরানো জিনিস বের করেন।", A_PRATNA),
    ("মৃত্তিকা", "মৃত্তিকার নিচে লুকিয়ে ছিল পুরানো নগর।", A_MRIT),
    ("রৌপ্যমুদ্রা", "জাদুঘরে অনেক পুরানো রৌপ্যমুদ্রা রাখা আছে।", A_ROUPYA),
    ("সাম্রাজ্য", "একজন সম্রাট রোমান সাম্রাজ্য শাসন করতেন।", A_SAMRAJYA),
    ("সভ্যতা", "নদীর ধারে গড়ে ওঠা সভ্যতা অনেক পুরানো।", A_EX1),
    ("প্রমাণ", "মুদ্রাগুলোই বাণিজ্যের সবচেয়ে বড়ো প্রমাণ।", A_EX1),
    ("ঐতিহাসিক", "মহাস্থানগড় একটি ঐতিহাসিক জায়গা।", A_EX1),
]
for word, sent, anc in S03:
    add("S03", "মূল কাঠামো", SENT,
        f"'{word}' শব্দটি দিয়ে একটি অর্থপূর্ণ বাক্য লেখো।",
        "short_answer", "short", "Apply", "medium", 1, anc, **sa([sent], SENT_KEY))


# =====================================================================================
# S04 · শূন্যস্থান পূরণ · simple · marks 1 · 11 items · all Remember, easy
# Eleven DISTINCT printed facts. অনুশীলনী ১ is itself a শূন্যস্থান exercise; the sentences below
# are the chapter's own মূল তথ্য and table rows with one fact removed from each.
# =====================================================================================
S04 = [
    ("প্রাচীনকালে কুমিল্লার ______ ও বগুড়ার মহাস্থানগড়ে নগর গড়ে উঠেছিল।",
     ["ময়নামতি"], A_MAYNA),
    ("বগুড়ার ______ তৃতীয় শতকের পরে গড়ে ওঠা একটি প্রাচীন নগর।",
     ["মহাস্থানগড়"], A_MAYNA),
    ("উয়ারী ও বটেশ্বর ______ জেলার দুটি গ্রাম।", ["নরসিংদী"], A_UWARI),
    ("ধারণা করা হয়, খ্রিষ্টপূর্ব ______ শতকে উয়ারী-বটেশ্বরে নগর গড়ে ওঠে।",
     ["ছয়-সাত", "ছয় সাত"], A_KHRIS),
    ("______ নদী ব্রহ্মপুত্রের একটি শাখা।", ["শীতলক্ষ্যা"], A_SHITAL),
    ("সমুদ্রপথে ______ সাম্রাজ্যের সাথে এই অঞ্চলের যোগাযোগ ছিল।", ["রোমান"], A_ROMAN),
    ("১৯৩৩ সালে উয়ারী গ্রামে মুদ্রা সংগ্রহ করেন স্কুলশিক্ষক ______।",
     ["হানিফ পাঠান"], A_HANIF),
    ("১৯৫৬ সালে উয়ারী গ্রামে প্রায় ______ মুদ্রার ভান্ডার পাওয়া যায়।",
     ["চার হাজার"], A_1956),
    ("মাটির নিচে পাওয়া দুর্গ-নগরটি ______ বছরের প্রাচীন।",
     ["আড়াই হাজার"], A_DURGA),
    ("এই সভ্যতা প্রাচীনকালে ______ নামে বিশ্বজুড়ে পরিচিত ছিল।", ["সোনাগড়া"], A_SONA),
    ("উয়ারী-বটেশ্বরের আশেপাশে প্রায় ______ পুরানো জায়গার সন্ধান পাওয়া গেছে।",
     ["পঞ্চাশটি", "পঞ্চাশ"], A_FIFTY),
]
for text, acc, anc in S04:
    add("S04", "মূল কাঠামো", INFO, f"'{text}' — শূন্যস্থান পূরণ করো।",
        "fill_blank", "short", "Remember", "easy", 1, anc, **blank(acc))


# =====================================================================================
# S05 · বহুনির্বাচনি · simple · marks 1 · 8 items · 5 Remember/easy + 3 Understand/medium
# THE SPLIT IS COGNITIVE DEMAND, NEVER SLOT IDENTITY (QB-CR-011/012). Five stems recall one fact
# printed in মূল তথ্য or the table. Three require holding two facts apart — which Pathan did
# which thing, which number counts what, which route the text actually names.
# =====================================================================================
add("S05", "মূল কাঠামো", INFO, "উয়ারী ও বটেশ্বর গ্রাম দুটি কোন জেলায়?",
    "mcq", "mcq", "Remember", "easy", 1, A_UWARI,
    **mcq([("ক", "নরসিংদী", True, None),
           ("খ", "কুমিল্লা", False, "কুমিল্লায় আছে ময়নামতি, উয়ারী-বটেশ্বর নয়।"),
           ("গ", "বগুড়া", False, "বগুড়ায় আছে মহাস্থানগড়।"),
           ("ঘ", "ঢাকা", False, "পাঠে ঢাকা জেলার কোনো নাম নেই।")]))
add("S05", "মূল কাঠামো", INFO, "ময়নামতি কোন জেলায় অবস্থিত?",
    "mcq", "mcq", "Remember", "easy", 1, A_MAYNA,
    **mcq([("ক", "কুমিল্লা", True, None),
           ("খ", "বগুড়া", False, "বগুড়ায় আছে মহাস্থানগড়।"),
           ("গ", "নরসিংদী", False, "নরসিংদীতে আছে উয়ারী ও বটেশ্বর।"),
           ("ঘ", "ঢাকা", False, "পাঠে ঢাকা জেলার কোনো নাম নেই।")]))
add("S05", "মূল কাঠামো", INFO, "প্রত্নতত্ত্ববিদরা কত সালে খননকাজ শুরু করেন?",
    "mcq", "mcq", "Remember", "easy", 1, A_KHONON,
    **mcq([("ক", "২০০০", True, None),
           ("খ", "১৯৩৩", False, "১৯৩৩ সালে উয়ারী গ্রামে পাত্রে জমানো মুদ্রা পাওয়া যায়, খননকাজ নয়।"),
           ("গ", "১৯৫৫", False, "১৯৫৫ সালে বটেশ্বরে পাওয়া যায় দুটি পুরানো লোহার টুকরা।"),
           ("ঘ", "১৯৫৬", False, "১৯৫৬ সালে উয়ারীতে পাওয়া যায় রৌপ্যমুদ্রার ভান্ডার।")]))
add("S05", "মূল কাঠামো", INFO, "শীতলক্ষ্যা কোন নদীর একটি শাখা?",
    "mcq", "mcq", "Remember", "easy", 1, A_SHITAL,
    **mcq([("ক", "ব্রহ্মপুত্র", True, None),
           ("খ", "পদ্মা", False, "পাঠে পদ্মা নদীর কোনো উল্লেখ নেই।"),
           ("গ", "মেঘনা", False, "পাঠে মেঘনা নদীর কোনো উল্লেখ নেই।"),
           ("ঘ", "বঙ্গোপসাগর", False,
            "বঙ্গোপসাগর নদী নয়, সাগর; পাঠে বলা হয়েছে নদী থেকে বঙ্গোপসাগর হয়ে সমুদ্রপথে যোগাযোগ হতো।")]))
add("S05", "মূল কাঠামো", INFO, "১৯৫৫ সালে বটেশ্বর গ্রামে কী পাওয়া যায়?",
    "mcq", "mcq", "Remember", "easy", 1, A_1955,
    **mcq([("ক", "দুটি পুরানো লোহার টুকরা", True, None),
           ("খ", "প্রায় চার হাজার রৌপ্যমুদ্রা", False,
            "রৌপ্যমুদ্রার ভান্ডার পাওয়া যায় ১৯৫৬ সালে, উয়ারী গ্রামে।"),
           ("গ", "পাথরের বাটখারা", False, "বাটখারা পাওয়া যায় ২০০০ সালের খননে।"),
           ("ঘ", "ইটের স্থাপত্য", False, "ইটের স্থাপত্যও পাওয়া যায় ২০০০ সালের খননে।")]))
add("S05", "মূল কাঠামো", INFO, "প্রচুর নিদর্শন সংগ্রহ করে জাদুঘরে জমা দেন কে?",
    "mcq", "mcq", "Understand", "medium", 1, A_HABIB,
    **mcq([("ক", "হাবিবুল্লাহ পাঠান", True, None),
           ("খ", "হানিফ পাঠান", False,
            "হানিফ পাঠান ১৯৩৩ সালে মুদ্রা সংগ্রহ করেন; জাদুঘরে নিদর্শন জমা দেন তাঁর পুত্র।"),
           ("গ", "প্রত্নতত্ত্ববিদরা", False, "প্রত্নতত্ত্ববিদরা ২০০০ সালে খননকাজ শুরু করেন।"),
           ("ঘ", "ইতিহাসবিদরা", False, "নিদর্শন জমা দেওয়ার কথা পাঠে ইতিহাসবিদদের নিয়ে বলা হয়নি।")]))
add("S05", "মূল কাঠামো", INFO,
    "প্রাচীনকালে সমুদ্রপথে কোন সাম্রাজ্যের সাথে এই অঞ্চলের যোগাযোগ ছিল?",
    "mcq", "mcq", "Understand", "medium", 1, A_ROMAN,
    **mcq([("ক", "রোমান সাম্রাজ্য", True, None),
           ("খ", "মোগল সাম্রাজ্য", False,
            "পাঠে যে যোগাযোগের কথা আছে তা নদীপথ ও সমুদ্রপথের বাণিজ্য নিয়ে, আর সেখানে কেবল "
            "রোমান সাম্রাজ্যের নাম আছে।"),
           ("গ", "গ্রিক সাম্রাজ্য", False, "পাঠে গ্রিক সাম্রাজ্যের কোনো উল্লেখ নেই।"),
           ("ঘ", "পারস্য সাম্রাজ্য", False, "পাঠে পারস্য সাম্রাজ্যের কোনো উল্লেখ নেই।")]))
add("S05", "মূল কাঠামো", INFO, "মাটির নিচে পাওয়া দুর্গ-নগরটি কত বছরের পুরানো?",
    "mcq", "mcq", "Understand", "medium", 1, A_DURGA,
    **mcq([("ক", "আড়াই হাজার বছরের", True, None),
           ("খ", "চার হাজার বছরের", False,
            "চার হাজার সংখ্যাটি মুদ্রার — ১৯৫৬ সালে প্রায় চার হাজার মুদ্রার ভান্ডার পাওয়া যায়।"),
           ("গ", "পঞ্চাশ বছরের", False, "পঞ্চাশ সংখ্যাটি আশেপাশের পুরানো জায়গার।"),
           ("ঘ", "সাত-আট শতকের", False, "সাত-আট শতক ময়নামতির সময়, উয়ারী-বটেশ্বরের নয়।")]))


# =====================================================================================
# S06 · বিপরীত শব্দ (C5 SELECTED; সমার্থক শব্দ is admitted at the slot and NOT selected)
# simple · marks 1 · 5 items · Remember, easy · teacher-supplied key (CD-136(b))
# EVERY STIMULUS IS USED ADJECTIVALLY OR ADVERBIALLY IN THIS CHAPTER'S OWN PROSE. That test is
# QB-CR-018's U16 finding #13: a word the chapter uses only adverbially or idiomatically has no
# antonym in the sense the chapter uses it, and an item built on one drills nothing.
#   পুরানো — "সবচেয়ে পুরানো রৌপ্যমুদ্রা" · প্রাচীন — "প্রাচীন নগরের রাস্তার নমুনা"
#   মূল্যবান — "মূল্যবান পাথর" · নিচে — "মাটির নিচে" · অভিজ্ঞ — "ইতিহাস বিষয়ে অভিজ্ঞ যিনি"
# =====================================================================================
S06 = [
    ("পুরানো", ["নতুন"], A_OLDEST),
    ("প্রাচীন", ["আধুনিক", "নবীন"], A_2000),
    ("মূল্যবান", ["মূল্যহীন"], A_INVENT),
    ("নিচে", ["উপরে"], A_DURGA),
    ("অভিজ্ঞ", ["অনভিজ্ঞ"], A_ITIHASBID),
]
for word, acc, anc in S06:
    add("S06", "বিপরীত শব্দ", WORDREL,
        f"পাঠে ব্যবহৃত '{word}' শব্দের বিপরীত শব্দ লেখো।",
        "short_answer", "short", "Remember", "easy", 1, anc, **sa(acc, TEACHER_KEY))


# =====================================================================================
# S07 · সংক্ষিপ্ত উত্তর · simple · marks 2 · 9 items · 6 Understand + 3 Analyze
# Q45 and Q46 are the ✅ block's REQUIRED "কীভাবে বোঝা যায়" form. The source names that
# requirement in its own words and it is met twice, not once.
# =====================================================================================
add("S07", "মূল কাঠামো", INFO,
    "উয়ারী ও বটেশ্বর কোথায় অবস্থিত এবং এই দুটি গ্রাম কেন গুরুত্বপূর্ণ, সংক্ষেপে লেখো।",
    "short_answer", "short", "Understand", "easy", 2, A_UWARI,
    **sa(["উয়ারী ও বটেশ্বর নরসিংদী জেলার দুটি গ্রাম। ধারণা করা হয় খ্রিষ্টপূর্ব ছয়-সাত শতকে "
          "সেখানে নগর গড়ে ওঠে, তাই এগুলো ময়নামতি ও মহাস্থানগড়ের চেয়েও পুরানো।"],
         "মূল তথ্য ও ভাবটি ধরা পড়লেই পূর্ণ নম্বর; শব্দে শব্দে মিল থাকা জরুরি নয়।"))
add("S07", "মূল কাঠামো", INFO, "১৯৩৩ সালে উয়ারী গ্রামে কী ঘটেছিল?",
    "short_answer", "short", "Understand", "easy", 2, A_1933,
    **sa(["উয়ারী গ্রামে একটি পাত্রে জমানো মুদ্রা পাওয়া যায়। স্কুলশিক্ষক হানিফ পাঠান সেখান থেকে "
          "কুড়ি-ত্রিশটি মুদ্রা সংগ্রহ করেন, আর এগুলোই এ পর্যন্ত পাওয়া সবচেয়ে পুরানো রৌপ্যমুদ্রা।"],
         "মূল তথ্য ও ভাবটি ধরা পড়লেই পূর্ণ নম্বর; শব্দে শব্দে মিল থাকা জরুরি নয়।"))
add("S07", "মূল কাঠামো", INFO, "১৯৫৫ ও ১৯৫৬ সালে কী কী পাওয়া গিয়েছিল?",
    "short_answer", "short", "Understand", "easy", 2, A_1955,
    **sa(["১৯৫৫ সালে বটেশ্বর গ্রামে দুটি পুরানো লোহার টুকরা পাওয়া যায় — ত্রিকোণাকৃতির, একদিকে "
          "সুচালো। ১৯৫৬ সালে উয়ারী গ্রামে পাওয়া যায় রৌপ্যমুদ্রার ভান্ডার, প্রায় চার হাজার মুদ্রা।"],
         "দুটি সালের দুটি তথ্যই লাগবে; শব্দে শব্দে মিল থাকা জরুরি নয়।"))
add("S07", "মূল কাঠামো", INFO, "২০০০ সালের খননে মাটির নিচে কী কী পাওয়া গিয়েছিল?",
    "short_answer", "short", "Understand", "medium", 2, A_INVENT,
    **sa(["আড়াই হাজার বছরের প্রাচীন একটি দুর্গ-নগর পাওয়া যায়। সেখানে ছিল ইটের স্থাপত্য, বন্দর, "
          "রাস্তা ও গলি, পোড়ামাটির ফলক, মূল্যবান পাথর, পাথরের বাটখারা, কাচের পুঁতি ও মুদ্রাভান্ডার।"],
         "কয়েকটি নিদর্শনের নাম ঠিকভাবে লিখলেই পূর্ণ নম্বর; সবগুলো নাম লেখা জরুরি নয়।"))
add("S07", "মূল কাঠামো", INFO, "শীতলক্ষ্যা নদীর সঙ্গে প্রাচীন বাণিজ্যের সম্পর্ক কী?",
    "short_answer", "short", "Understand", "medium", 2, A_TRADE,
    **sa(["শীতলক্ষ্যা ব্রহ্মপুত্রের একটি শাখা। প্রাচীনকালে ব্রহ্মপুত্র নদীপথে বাণিজ্য হতো, আর সেই "
          "নদী থেকে বঙ্গোপসাগর হয়ে সমুদ্রপথে রোমান সাম্রাজ্যের সাথে যোগাযোগ ছিল।"],
         "নদী থেকে সাগর, সাগর থেকে দূরের দেশ — এই পথের কথাটি ধরা পড়লেই পূর্ণ নম্বর।"))
add("S07", "মূল কাঠামো", INFO, "হানিফ পাঠান ও হাবিবুল্লাহ পাঠানের অবদান কী ছিল?",
    "short_answer", "short", "Understand", "medium", 2, A_HABIB,
    **sa(["হানিফ পাঠান ছিলেন একজন স্কুলশিক্ষক; ১৯৩৩ সালে তিনি উয়ারী গ্রামে পাওয়া পুরানো "
          "রৌপ্যমুদ্রা সংগ্রহ করেন। তাঁর পুত্র হাবিবুল্লাহ পাঠান প্রচুর নিদর্শন সংগ্রহ করে "
          "জাদুঘরে জমা দেন।"],
         "দুজনের কাজ আলাদা করে বোঝা গেলেই পূর্ণ নম্বর।"))
add("S07", "মূল কাঠামো", INFO,
    "উয়ারী-বটেশ্বর ময়নামতি ও মহাস্থানগড়ের চেয়েও পুরানো — এটি কীভাবে বোঝা যায়?",
    "short_answer", "short", "Analyze", "hard", 2, A_MAYNA,
    **sa(["সাল মিলিয়ে দেখলেই বোঝা যায়। ময়নামতিতে নগর গড়ে ওঠে সাত-আট শতকে আর মহাস্থানগড়ে তৃতীয় "
          "শতকের পরে, কিন্তু উয়ারী-বটেশ্বরে ধারণা করা হয় খ্রিষ্টপূর্ব ছয়-সাত শতকে — অর্থাৎ আরও "
          "অনেক আগে।"],
         "যুক্তিটি সালের তুলনা থেকেই আসতে হবে; কেবল 'পুরানো' বললে পূর্ণ নম্বর নয়।"))
add("S07", "মূল কাঠামো", INFO,
    "প্রাচীনকালে এখানে বাইরের দেশের সঙ্গে বাণিজ্য হতো — নিদর্শন দেখে তা কীভাবে বোঝা যায়?",
    "short_answer", "short", "Analyze", "hard", 2, A_INVENT,
    **sa(["মাটির নিচে পাওয়া গেছে বন্দর, মুদ্রাভান্ডার আর পাথরের বাটখারা। বন্দর দিয়ে নৌকা ভিড়ত, "
          "মুদ্রা দিয়ে দাম মেটানো হতো আর বাটখারা দিয়ে ওজন করা হতো — এগুলোই কেনাবেচার নিদর্শন।"],
         "নিদর্শনের নাম আর তার কাজ — দুটোই লাগবে।"))
add("S07", "মূল কাঠামো", INFO,
    "মাটির নিচে যে নগর পাওয়া গেছে, তার কোন কোন নিদর্শন দেখে বোঝা যায় সেখানে মানুষ বসতি গড়ে বাস করত?",
    "short_answer", "short", "Analyze", "hard", 2, A_DURGA,
    **sa(["ইটের স্থাপত্য, রাস্তা ও গলি, বন্দর এবং দুর্গ — এগুলো এমনি এমনি মাটির নিচে আসে না, "
          "এগুলো মানুষের গড়া বসতির নিদর্শন।"],
         "অন্তত দুটি নিদর্শন আর তার ব্যাখ্যা থাকলেই পূর্ণ নম্বর।"))


# =====================================================================================
# S08 · বিস্তৃত উত্তর · simple · marks 5 · 4 items · 3 Analyze + 1 Evaluate, all hard
# Each rubric's content is DIFFERENT — a rubric that fits every question grades none of them.
# BAN-S08-STRAND (the C2→C5 ইসলামি ladder ending at বিদায় হজ) binds the PAPER and is served by
# পাঠ ২১; it is not a demand on this chapter and nothing here is bent toward it.
# =====================================================================================
add("S08", "মূল কাঠামো", INFO,
    "উয়ারী-বটেশ্বরে প্রাচীন নগর আবিষ্কারের ধারাবাহিক ইতিহাস লেখো।",
    "descriptive", "structured", "Analyze", "hard", 5, A_1933,
    **rubric("১৯৩৩ থেকে ২০০০ পর্যন্ত ঘটনাগুলো সাল ধরে ক্রম মেনে লেখা, প্রতিটি সালের সঙ্গে কী "
             "পাওয়া গেল তা মিলিয়ে — কেবল পাঠের তথ্যই ব্যবহার করে",
             "চারটি ধাপই ক্রম মেনে এসেছে — ১৯৩৩ সালে হানিফ পাঠানের সংগ্রহ করা মুদ্রা, ১৯৫৫ সালে "
             "বটেশ্বরের লোহার টুকরা, ১৯৫৬ সালে উয়ারীর রৌপ্যমুদ্রার ভান্ডার এবং ২০০০ সালে "
             "প্রত্নতত্ত্ববিদদের খননকাজ; হাবিবুল্লাহ পাঠানের নিদর্শন সংগ্রহের কথাও আছে; ভাষা "
             "সংযত এবং পাঠে নেই এমন কোনো তথ্য যোগ করা হয়নি।",
             "দু-একটি ধাপ বাদ পড়েছে বা সালের ক্রম গুলিয়ে গেছে; অথবা পাঠে নেই এমন তথ্য যোগ হয়েছে।"))
add("S08", "মূল কাঠামো", INFO,
    "২০০০ সালের খননে মাটির নিচে যে নগর পাওয়া গেল, তার বর্ণনা দাও।",
    "descriptive", "structured", "Analyze", "hard", 5, A_INVENT,
    **rubric("নগরটির বয়স, ধরন ও সেখানে পাওয়া নিদর্শনগুলো পাঠ থেকে ঠিকভাবে তুলে আনা",
             "নগরটি আড়াই হাজার বছরের প্রাচীন একটি দুর্গ-নগর — এই পরিচয়টি আছে; ইটের স্থাপত্য, "
             "বন্দর, রাস্তা ও গলি, পোড়ামাটির ফলক, মূল্যবান পাথর, পাথরের বাটখারা, কাচের পুঁতি ও "
             "মুদ্রাভান্ডারের মধ্যে অন্তত পাঁচটি নিদর্শনের নাম আছে; কেবল পাঠের তথ্যই ব্যবহৃত।",
             "নগরটির পরিচয় বা বয়স বাদ পড়েছে, কিংবা দুই-তিনটির বেশি নিদর্শনের নাম আসেনি।"))
add("S08", "মূল কাঠামো", INFO,
    "প্রাচীনকালে এই অঞ্চলের নদীপথ ও সমুদ্রপথের বাণিজ্য সম্পর্কে যা জান লেখো।",
    "descriptive", "structured", "Analyze", "hard", 5, A_TRADE,
    **rubric("শীতলক্ষ্যা থেকে ব্রহ্মপুত্র, ব্রহ্মপুত্র থেকে বঙ্গোপসাগর, সেখান থেকে দূরের দেশ — "
             "পথটি ধাপে ধাপে দেখানো এবং বাণিজ্যের নিদর্শনগুলোর সঙ্গে মিলিয়ে লেখা",
             "শীতলক্ষ্যা যে ব্রহ্মপুত্রের শাখা তা বলা হয়েছে; নদীপথে বাণিজ্যের কথা আছে; "
             "বঙ্গোপসাগর হয়ে সমুদ্রপথে রোমান সাম্রাজ্যের সাথে যোগাযোগের কথা আছে; বন্দর, "
             "মুদ্রাভান্ডার বা বাটখারার মতো অন্তত একটি নিদর্শন যুক্তি হিসেবে এসেছে।",
             "পথের এক-দুটি ধাপ বাদ পড়েছে, অথবা রোমান সাম্রাজ্যের যোগাযোগের কথা আসেনি।"))
add("S08", "মূল কাঠামো", INFO,
    "প্রত্নতত্ত্ববিদদের কাজ কেন দরকারি — এই পাঠের নিদর্শনগুলোর কথা ভেবে যুক্তি দিয়ে লেখো।",
    "descriptive", "structured", "Evaluate", "hard", 5, A_PRATNA,
    **rubric("মতামতের সপক্ষে যুক্তি পাঠের নিদর্শন থেকেই তোলা — মত আর তার প্রমাণ দুটোই থাকা",
             "একটি স্পষ্ট মত আছে, এবং তার সপক্ষে অন্তত দুটি যুক্তি পাঠের নিদর্শন থেকে এসেছে — "
             "যেমন খনন না হলে আড়াই হাজার বছরের দুর্গ-নগর মাটির নিচেই থেকে যেত, কিংবা "
             "মুদ্রা-বাটখারা না পেলে প্রাচীন বাণিজ্যের কথা জানা যেত না; ভাষা সংযত।",
             "মত আছে কিন্তু যুক্তি পাঠের নিদর্শন থেকে আসেনি, অথবা একটির বেশি যুক্তি নেই।"))


# =====================================================================================
# S10 · পদ নির্ণয় (C5 SELECTED; ভাষারীতি পরিবর্তন and ক্রিয়ার কাল are admitted at the slot and
# NOT selected) · simple · marks 1 · 6 items · Understand, easy · teacher key (CD-136(b))
# EVERY STIMULUS IS REPRODUCED AS THE CHAPTER PRINTS IT, terminal punctuation included, and the
# target is asked AS USED THERE. Accepted answers are standard Bengali grammar terms only — no
# super-class (নামপদ identifies none of the four পদ under it) and no coined term.
# অনুশীলনী ৪ (আজ / গতকাল / আগামীকাল) is NOT authored: it is ক্রিয়ার কাল, off-choice at C5.
#
# NO STIMULUS CARRIES PUNCTUATION THE SOURCE DOES NOT PRINT. The ১৯৫৫ table row is quoted WHOLE —
# "বটেশ্বর গ্রামে দুটি পুরানো লোহার টুকরা — ত্রিকোণাকৃতির, একদিকে সুচালো" — because the source
# ends that row without a দাঁড়ি, and truncating it at টুকরা would mean supplying one.
#
# 'শব্দটি' IS ONLY USED OF A SINGLE WORD. পাওয়া যায় is a two-word unit forming ONE ক্রিয়াপদ, so
# that item asks "কোন পদ হিসেবে ব্যবহৃত হয়েছে" instead, and its key stays inside the C5 পদ set
# (বিশেষ্য · সর্বনাম · বিশেষণ · ক্রিয়া · অব্যয়) — যৌগিক ক্রিয়া is a sub-classification above
# class level and is NOT accepted.
# =====================================================================================
# (stimulus, target, accepted, anchor, stem-shape) — "word" for a single word, "unit" for a
# multi-word unit that is one পদ.
S10 = [
    ("শীতলক্ষ্যা নদী ব্রহ্মপুত্রের একটি শাখা।", "শাখা",
     ["বিশেষ্য", "বিশেষ্য পদ"], A_SHITAL, "word"),
    ("মাটির নিচে আড়াই হাজার বছরের প্রাচীন দুর্গ-নগর।", "প্রাচীন",
     ["বিশেষণ", "বিশেষণ পদ"], A_DURGA, "word"),
    ("প্রত্নতত্ত্ববিদরা খননকাজ শুরু করেন।", "করেন",
     ["ক্রিয়া", "ক্রিয়া পদ"], A_KHONON, "word"),
    ("এই সভ্যতা প্রাচীনকালে সোনাগড়া নামে বিশ্বজুড়ে পরিচিত ছিল।", "সভ্যতা",
     ["বিশেষ্য", "বিশেষ্য পদ"], A_SONA, "word"),
    ("বটেশ্বর গ্রামে দুটি পুরানো লোহার টুকরা — ত্রিকোণাকৃতির, একদিকে সুচালো", "পুরানো",
     ["বিশেষণ", "বিশেষণ পদ"], A_1955, "word"),
    ("উয়ারী গ্রামে একটি পাত্রে জমানো মুদ্রা পাওয়া যায়।", "পাওয়া যায়",
     ["ক্রিয়া", "ক্রিয়া পদ"], A_1933, "unit"),
]
for sent, word, acc, anc, shape in S10:
    ask = (f"এখানে '{word}' শব্দটি কোন পদ? নির্ণয় করো।" if shape == "word"
           else f"এখানে '{word}' কোন পদ হিসেবে ব্যবহৃত হয়েছে? নির্ণয় করো।")
    add("S10", "পদ নির্ণয়", PARTSP,
        f"'{sent}' — {ask}",
        "short_answer", "short", "Understand", "easy", 1, anc,
        **sa(acc, PADA_KEY))


# =====================================================================================
# S11 · বিরামচিহ্ন বসানো (C5 SELECTED; প্রশ্ন তৈরি is admitted at the slot and NOT selected, and
# this chapter's ছক calls itself প্রশ্ন তৈরি's only direct source — THE TRAP)
# simple · marks 1 · 6 items · Apply, medium
#
# QB-CR-017: EVERY ITEM BELOW REQUIRES AT LEAST TWO MARK INSERTIONS. The count is not asserted —
# `s11_work_check()` diffs each stimulus against its accepted answer and refuses a count of one,
# which is exactly the measurement QB-CR-017 proposes as a gate.
#
# TAUGHT SET (CD-165 amended by CD-166): দাঁড়ি · কমা · প্রশ্নচিহ্ন · বিস্ময়চিহ্ন · উদ্ধরণ চিহ্ন.
# No item requires ড্যাশ or সেমিকোলন. The chapter prints both, so the spans were chosen, not found:
# the ব্রহ্মপুত্র trade sentence carries a semicolon and is not used as a stimulus.
# =====================================================================================
S11 = [
    ("উয়ারী ও বটেশ্বর নরসিংদী জেলার দুটি গ্রাম",
     "উয়ারী ও বটেশ্বর, নরসিংদী জেলার দুটি গ্রাম।",
     "গ্রাম দুটির নামের পরে পরিচয় বসেছে, তাই সেখানে কমা; বাক্যটি শেষ হয়েছে, তাই শেষে দাঁড়ি।",
     A_UWARI),
    ("মাটি খনন করে কী কী পাওয়া গেল রৌপ্যমুদ্রা হাতিয়ার আর পাথরের পুঁতি",
     "মাটি খনন করে কী কী পাওয়া গেল? রৌপ্যমুদ্রা, হাতিয়ার আর পাথরের পুঁতি।",
     "প্রথমটি প্রশ্ন, তাই প্রশ্নচিহ্ন; পরের বাক্যে পাশাপাশি নাম আছে, তাই কমা, আর শেষে দাঁড়ি।",
     A_FIND),
    ("হানিফ পাঠান ছিলেন একজন স্কুলশিক্ষক তাঁর পুত্র হাবিবুল্লাহ পাঠান নিদর্শন জাদুঘরে জমা দেন",
     "হানিফ পাঠান ছিলেন একজন স্কুলশিক্ষক। তাঁর পুত্র হাবিবুল্লাহ পাঠান নিদর্শন জাদুঘরে জমা দেন।",
     "এখানে দুটি আলাদা পূর্ণ বাক্য, তাই দুটিরই শেষে দাঁড়ি।",
     A_HABIB),
    ("কত পুরানো এই নগর আড়াই হাজার বছরের",
     "কত পুরানো এই নগর? আড়াই হাজার বছরের।",
     "প্রথমটি প্রশ্ন, তাই প্রশ্নচিহ্ন; পরেরটি তার উত্তর ও একটি পূর্ণ বাক্য, তাই দাঁড়ি।",
     A_DURGA),
    ("এই সভ্যতা প্রাচীনকালে সোনাগড়া নামে পরিচিত ছিল কী সুন্দর নাম",
     ["এই সভ্যতা প্রাচীনকালে 'সোনাগড়া' নামে পরিচিত ছিল। কী সুন্দর নাম!",
      "এই সভ্যতা প্রাচীনকালে সোনাগড়া নামে পরিচিত ছিল। কী সুন্দর নাম!"],
     "এখানে দুটি আলাদা বাক্য — প্রথমটি শেষ হয়েছে, তাই দাঁড়ি; পরেরটিতে বিস্ময় প্রকাশ পেয়েছে, "
     "তাই বিস্ময়চিহ্ন। দাঁড়ি ও বিস্ময়চিহ্ন — এই দুটিই এখানে আবশ্যক। বিশেষ নামটিকে উদ্ধরণ "
     "চিহ্নের ভেতরে রাখলে তা শুদ্ধ, কিন্তু আবশ্যক নয়: পাঠে নামটি উদ্ধরণ চিহ্ন ছাড়াই ছাপা "
     "হয়েছে, তাই উদ্ধরণ চিহ্ন না বসালেও উত্তর সম্পূর্ণ ধরতে হবে।",
     A_SONA),
    ("প্রত্নতত্ত্ববিদরা খননকাজ শুরু করলেন মাটির নিচে বেরিয়ে এল আড়াই হাজার বছরের প্রাচীন দুর্গ-নগর",
     "প্রত্নতত্ত্ববিদরা খননকাজ শুরু করলেন। মাটির নিচে বেরিয়ে এল আড়াই হাজার বছরের প্রাচীন দুর্গ-নগর।",
     "এখানে দুটি আলাদা পূর্ণ বাক্য, তাই দুটিরই শেষে দাঁড়ি।",
     A_KHONON),
]
for raw, fixed, note, anc in S11:
    accepted = [fixed] if isinstance(fixed, str) else list(fixed)
    add("S11", "বিরামচিহ্ন বসানো", PUNCT,
        f"'{raw}' — বাক্যটিতে প্রয়োজনীয় বিরামচিহ্ন বসিয়ে আবার লেখো।",
        "short_answer", "short", "Apply", "medium", 1, anc, **sa(accepted, note))


# =====================================================================================
# S12 · যুক্তবর্ণ ও শব্দ গঠন · COMPOSITE (যুক্তবর্ণ ভাঙা + শব্দ গঠন) · marks 1 · 7 items
# Apply, medium · teacher-supplied key (CD-136(b))
# BOTH PARTS ARE DECLARED ON EVERY ITEM — an item that only breaks the conjunct does half the task
# and COVERAGE fails it (SLOT_REGISTER BAN-S12 `parts`).
# EVERY STEM NAMES ITS CONJUNCT. QB-CR-018's U16 finding #9: সাম্রাজ্য carries ম্র AND জ্য and
# স্থাপত্য carries স্থ AND ত্য, so a bare "যুক্তবর্ণটি" would have no single referent and a correct
# answer on the other conjunct would be unmarkable.
# =====================================================================================
S12 = [
    ("মৃত্তিকা", "ত্ত", "ত + ত", "উত্তর", A_MRIT),
    ("রৌপ্যমুদ্রা", "দ্র", "দ + র", "সমুদ্র", A_ROUPYA),
    ("সাম্রাজ্য", "ম্র", "ম + র", "নম্র", A_SAMRAJYA),
    ("স্থাপত্য", "স্থ", "স + থ", "স্থান", A_INVENT),
    ("পুত্র", "ত্র", "ত + র", "ছাত্র", A_HABIB),
    ("বাণিজ্য", "জ্য", "জ + য", "রাজ্য", A_TRADE),
    ("বিশ্বজুড়ে", "শ্ব", "শ + ব", "বিশ্বাস", A_SONA),
]
for word, conj, split, newword, anc in S12:
    add("S12", ["যুক্তবর্ণ ভাঙা", "শব্দ গঠন"], JUKTO,
        f"পাঠের '{word}' শব্দে থাকা '{conj}' যুক্তবর্ণটি ভেঙে দেখাও, আর সেই যুক্তবর্ণ দিয়ে "
        f"নতুন একটি শব্দ গঠন করো।",
        "short_answer", "short", "Apply", "medium", 1, anc,
        **sa([f"{conj} = {split}; নতুন শব্দ — {newword}", f"{conj} — {split}; {newword}"],
             JUKTO_KEY))


# =====================================================================================
# S13 · এক কথায় প্রকাশ · simple · marks 1 · 5 items · Remember, easy
# All five definition-phrases are printed VERBATIM in অর্থ জেনে নিই with their one-word answer
# beside them, so recalling the pairing is `Remember` and NO CD-136 teacher-key note is owed —
# the key is in the chapter. ONE ITEM CARRIES A MARKER NOTE ANYWAY: 'ইতিহাস বিষয়ে অভিজ্ঞ যিনি'
# is satisfied by ইতিহাসবিদ AND by ঐতিহাসিক, which অনুশীলনী ১'s word list prints, and the stem
# says "পাঠের শব্দ দিয়ে" — so both are accepted and the note tells the marker so. (Q01 runs
# word→meaning and has no such ambiguity; Q17 uses ঐতিহাসিক adjectivally, which is correct there.) মৃত্তিকা and নিদর্শন are not used here: their glosses are single
# words (মাটি · প্রমাণ), not definition-phrases, so they are শব্দার্থ and not এক কথায় প্রকাশ.
# =====================================================================================
S13 = [
    ("ইতিহাস বিষয়ে অভিজ্ঞ যিনি", ["ইতিহাসবিদ", "ঐতিহাসিক"], A_ITIHASBID,
     "স্টেমটি 'পাঠের শব্দ দিয়ে' বলছে, আর পাঠ দুটি শব্দই ছাপে — অর্থ জেনে নিই-তে ইতিহাসবিদ এবং "
     "অনুশীলনী ১-এর শব্দতালিকায় ঐতিহাসিক। দুটিই এই সংজ্ঞা মেটায়, তাই যেকোনোটি লিখলেই পূর্ণ "
     "নম্বর।"),
    ("শত্রুসৈন্য সহজে প্রবেশ করতে পারে না এমন স্থান", ["দুর্গ"], A_DURG, None),
    ("প্রাচীন ইতিহাস ও উপকরণ নিয়ে কাজ করেন যিনি", ["প্রত্নতত্ত্ববিদ"], A_PRATNA, None),
    ("রুপার তৈরি মুদ্রা বা টাকা", ["রৌপ্যমুদ্রা"], A_ROUPYA, None),
    ("সম্রাটের শাসনাধীন রাজ্য", ["সাম্রাজ্য"], A_SAMRAJYA, None),
]
for phrase, acc, anc, note in S13:
    add("S13", "মূল কাঠামো", VOCAB,
        f"'{phrase}' — পাঠের শব্দ দিয়ে এক কথায় প্রকাশ করো।",
        "short_answer", "short", "Remember", "easy", 1, anc, **sa(acc, note))


# =====================================================================================
def build():
    questions, slot_index, task_index, source_index = [], {}, {}, {}
    for i, it in enumerate(ITEMS, start=1):
        qid = f"QP-BAN-C5-U17-Q{i:02d}"
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

    qids = [q["qid"] for q in questions]
    by_slot = {}
    for qid in qids:
        by_slot.setdefault(slot_index[qid], []).append(qid)
    slot_counts = {s: len(v) for s, v in sorted(by_slot.items())}

    # Pools — QB-D-001: every item in exactly one, no overlap.
    # CT takes the short recall a 25-mark class test can actually carry (S02 · S04 · S06).
    # AS takes the mixed band QB-D-004 wants — roughly half at or above Apply (S03 · S07 · S08 ·
    # S13). HW takes the rest (S05 · S10 · S11 · S12).
    ct = [q for q in qids if slot_index[q] in ("S02", "S04", "S06")]
    as_ = [q for q in qids if slot_index[q] in ("S03", "S07", "S08", "S13")]
    hw = [q for q in qids if slot_index[q] in ("S05", "S10", "S11", "S12")]

    return {
        "schema_version": "1.0",
        "policy_shape": "qp6",
        "bank_id": "QB-BAN-C5-U17",
        "wave": 1,
        "subject": "BAN",
        "class": 5,
        "chapter": CHAPTER,
        "extraction_path": EXTRACTION,
        "source_extraction": EXTRACTION,
        "curation": (
            "FLEXIBLE · এই পাঠের ⚠ ব্লকের দুটি ধারাই এখানে মানা হয়েছে। (১) অনুশীলনী ৬ — "
            "পুরানো কয়েন, অন্য দেশের টাকা ও ডাকটিকিট সংগ্রহ — উৎস নিজেই বলছে এটি শ্রেণিকক্ষের "
            "কাজ, প্রশ্নপত্রে নয়; কোনো আইটেম শিক্ষার্থীকে কিছু সংগ্রহ করতে, আনতে বা দেখাতে "
            "বলে না এবং ওই অনুশীলনী থেকে কিছুই লেখা হয়নি। (২) মন্দির ভিটা ও বৌদ্ধ বিহার — উৎস "
            "প্রশ্নকে অন্য নিদর্শনের দিকে নিয়ে যেতে বলেছে (মুদ্রা, দুর্গ, বন্দর, বাটখারা); "
            "শব্দ দুটির কোনোটিই extraction-এ নেই, তাই কোনো anchor সেখানে পৌঁছায় না, আর প্রতিটি "
            "নিদর্শন-প্রশ্ন উৎসের পছন্দ করা চারটির নামই বলে। ✅ ব্লকের দাবিও মানা হয়েছে — "
            "'কীভাবে বোঝা যায়' ধরনের প্রশ্ন একটি নয়, দুটি (Q45, Q46), দুটিই Analyze। C-05 — "
            "কোনো ব্যক্তির ছবি নেই ও চাওয়া হয়নি; C-18 — কোনো শ্রদ্ধা নিবেদনের আচার নেই; C-03 — "
            "এই পাঠে গান-বাজনার কোনো উপাদানই নেই। কোনো কাল্পনিক ব্যক্তিনাম কোথাও ব্যবহৃত হয়নি; "
            "হানিফ পাঠান ও হাবিবুল্লাহ পাঠান পাঠের নিজের ঐতিহাসিক ব্যক্তি — চরিত্র নয়, তথ্য।"),
        "header": {
            "policy_shape": "qp6",
            "target": len(questions),
            "reason": (
                "৭৮ কোনো লক্ষ্য নয় এবং একটি আইটেমও সংখ্যায় পৌঁছাতে লেখা হয়নি — CD-171(a) "
                "অনুযায়ী কোনো ন্যূনতম, কোনো সর্বোচ্চ, কোনো Bloom মেঝে বা পুল-স্তরের স্লট-দাবি "
                "আর নেই। বাঁধন একটাই: §৪-এর near-duplicate নিষেধের নিচে উৎস নিঃশেষ হওয়া। "
                "প্রতিটি সংখ্যা বিষয়বস্তু থেকে এসেছে — S02 ৭টি কারণ অর্থ জেনে নিই-তে শব্দ সাতটিই; "
                "S13 ৫টি কারণ ওই সাতটির মধ্যে পাঁচটির অর্থ সংজ্ঞা-বাক্য, বাকি দুটির অর্থ একটি "
                "করে শব্দ; S06 ৫টি কারণ পাঠের গদ্যে বিশেষণ বা ক্রিয়াবিশেষণ হিসেবে ব্যবহৃত শব্দ "
                "পাঁচটিই; S04 ১১টি কারণ মূল তথ্য ও ছকে আলাদা করে তোলার মতো তথ্য এগারোটি; S12 ৭টি "
                "কারণ পাঠের শব্দে স্পষ্ট ও নাম-ধরে-বলা যায় এমন যুক্তবর্ণ সাতটি। যেখানে "
                "বিষয়বস্তু আছে কিন্তু আইটেম নেই, সেখানে কারণ header.gaps-এ লেখা আছে — "
                "অনুমান করতে বলা হয়নি।"),
            "topics": ["TOP-BAN-C5-07", "TOP-BAN-C5-01", "TOP-BAN-C5-02", "TOP-BAN-C5-13"],
            "spine_slots": [f"S{i:02d}" for i in range(1, 16)],
            "admissible_slots": sorted(by_slot),
            "slot_exclusions": {
                "S01": ("পাঠ ১৭ গদ্য (তথ্যমূলক), এতে মুখস্থ করার মতো কোনো কবিতাংশ নেই — এবং "
                        "কারণটি অনুমান নয়, উৎসের নিজের বাক্য: 'কবিতা চারটি: পাঠ ১৩, ১৫, ১৮, "
                        "২০ — এগুলোই S01 (কবিতা মুখস্থ) ও S09 (মূলভাব) প্রশ্নের উৎস।' পাঠ ১৭ "
                        "সেই চারটির একটিও নয়।"),
                "S09": ("একই বাক্য S09-কেও ওই চার কবিতায় বেঁধেছে; মূলভাব এখানে কবিতার কাজ, আর "
                        "পাঠ ১৭ তথ্যমূলক গদ্য — এর আছে সাল, সংখ্যা ও স্থানের তথ্য, বলার মতো "
                        "কোনো মূলভাব নয়। তাই এই পাঠ স্লটটির উৎস নয়।"),
            },
            "admissibility_declaration": (
                "CD-138(e), পাঠ ১৭-এর নিজস্ব ঘোষণা, canon/marklogic/C5_Bangla_Source_13-23.md-এর "
                "পাঠ ১৭ অংশ (লাইন ২৭০–৩২১) থেকে লেখা — পাঠ ১২ পড়া হয়নি (CD-127(b) consumption "
                "exclusion)। রেজিস্টারে BAN C5-এর পনেরোটি স্লট। এর মধ্যে দুটি — S14 আবেদনপত্র ও "
                "S15 রচনা — CD-147 অনুযায়ী প্রতিটি পাঠের জন্যই কাগজ-স্তরের, শ্রেণিগতভাবে; কোনো "
                "পাঠ এদের জন্য বিষয়বস্তুর কারণ দেখানোর দায়ে নেই, এই ঘোষণা তাদের নিয়ে কিছুই বলে "
                "না, এবং CD-147(c) অনুযায়ী সেটাই সঠিক — অসম্পূর্ণ নয়। বাকি তেরোটির মধ্যে "
                "এগারোটি স্বীকৃত এবং দুটি — S01 ও S09 — বাদ, প্রতিটির এক লাইনের বিষয়বস্তু-কারণসহ "
                "slot_exclusions-এ। বাদ দুটির ভিত্তি উৎসের নিজের বাক্য, বিষয়বস্তু থেকে অনুমান "
                "নয় (CD-138(e) সেই অনুমান দুই দিকেই নিষিদ্ধ করে), এবং এই পাঠের নিজের 'কোন "
                "প্রশ্নে কাজে লাগবে' লাইন নয় (CD-134 — দুটো হেডারে দেখতে এক, আসলে এক নয়)। "
                "ওই লাইনটি বরং এই ব্যাংকে দুবার প্রত্যাখ্যাত হয়েছে: সেটি S11-এ প্রশ্ন তৈরি ও "
                "S10-এ ক্রিয়ার কাল চায়, আর দুটিই স্লটে স্বীকৃত কিন্তু C5-এ নির্বাচিত নয় — "
                "header.gaps দেখুন।"),
            "slot_counts": slot_counts,
            "topic_tag_ruling": (
                "পাঠ ১৭ গদ্য (তথ্যমূলক), তাই পাঠ-বিষয়ক আইটেমগুলো TOP-BAN-C5-07 "
                "(তথ্যমূলক গদ্য, BAN-INFOTEXT) বহন করে — canon/topics/TOPIC_NUMBERS.md-এর "
                "পাঠ-ধরন ছক পাঠ ১৭-কে নাম ধরে -07 দিয়েছে, D-PROJ04-010-এর সাক্ষ্যে। topic_tag "
                "প্রতি-প্রশ্নের ক্ষেত্র, প্রতি-অধ্যায়ের নয়: শব্দার্থ ও এক কথায় প্রকাশ -01 "
                "(BAN-VOCAB), বিপরীত শব্দ -01 (BAN-WORDREL), যুক্তবর্ণ -01 (BAN-JUKTOBARNA), "
                "পদ নির্ণয় -01 (BAN-PARTSPEECH), বাক্য গঠন -02 (BAN-SENTENCE), বিরামচিহ্ন -13। "
                "বিরামচিহ্নের ছয়টি আইটেম প্রথম থেকেই -13 বহন করছে, -02 নয় — QB-CR-014-এর শিক্ষা। "
                "ref19_topic_id বিরামচিহ্নেও BAN-SENTENCE-ই থাকছে: REF-19-এ যতিচিহ্নের কোনো slug "
                "নেই (PENDING-P-008, FLAGGED, non-blocking), আর এখানে একটি বানিয়ে নেওয়া হতো "
                "QB-CR-008-এর ভুলটাই অন্য রেজিস্টারে করা।"),
            "content_facts": (
                "CD-135(d) — শূন্য মেঝের বিপরীতে যে স্তরটি শূন্য, সেটি বিষয়বস্তুর তথ্য হিসেবে "
                "এখানে বলা হলো: Create এই পুলে ০। পাঠটি তথ্যমূলক প্রত্নতত্ত্ব এবং এর ছয়টি "
                "অনুশীলনীর একটিও নতুন রচনা তৈরির নয় — শূন্যস্থান, প্রশ্নোত্তর, প্রশ্ন বানাই, "
                "কালভেদে বাক্য, তিনটি নাম লেখা ও সংগ্রহ করা; কোনোটিই মৌলিক নির্মাণ চায় না। "
                "Evaluate ১টি — প্রত্নতত্ত্ববিদদের কাজের প্রয়োজনীয়তা নিয়ে যুক্তিনির্ভর মতামতের "
                "প্রশ্ন। উৎসের ✅ ব্লক সতর্ক করেছে এই পাঠে সব প্রশ্ন জ্ঞানমূলক হয়ে যাওয়ার ঝুঁকি "
                "সবচেয়ে বেশি; Remember ৩৩/৭৮ এবং 'কীভাবে বোঝা যায়' ধরনের প্রশ্ন দুটি।"),
            "taught_set_note": (
                "CD-165, CD-166-এ সংশোধিত — C5-এর বিরামচিহ্নের সেট: দাঁড়ি · কমা · প্রশ্নচিহ্ন · "
                "বিস্ময়চিহ্ন · উদ্ধরণ চিহ্ন। ড্যাশ ও সেমিকোলন পঞ্চম শ্রেণিতে বারিত, এবং এই পাঠ "
                "দুটিই ছাপে — মূল তথ্যের তিনটি বুলেটে ও ছকের তিনটি সারিতে ড্যাশ, আর ব্রহ্মপুত্রের "
                "বাণিজ্যের বাক্যে সেমিকোলন। তাই S11-এর উদ্দীপকগুলো বেছে নেওয়া হয়েছে, খুঁজে পাওয়া "
                "হয়নি: যে বাক্য সারাতে বারিত চিহ্ন লাগত, সেটি উদ্দীপক করা হয়নি। QB-CR-017 "
                "(OPEN) — ছয়টি S11 আইটেমের প্রতিটিতে অন্তত দুটি চিহ্ন বসাতে হয়; গণনাটি দাবি নয়, "
                "author_U17_wave1.py-এর s11_work_check() উদ্দীপক ও উত্তর মিলিয়ে গুনে দেখে এবং "
                "এক-চিহ্নের আইটেম হলে ফাইলই লেখে না।"),
            "gaps": [
                "S14 · S15 — CD-147 অনুযায়ী কাগজ-স্তরের, শ্রেণিগতভাবে; এই পাঠ এদের নিয়ে কিছু "
                "ঘোষণা করে না এবং করার দায়ও নেই (CD-147(c))।",
                "অনুশীলনী ৩ (প্রশ্ন বানাই — কী, কেন, কোথায়, কীভাবে, কত, কেমন) ব্যবহার করা "
                "হয়নি, এবং কারণটি বিষয়বস্তুর অভাব নয় — উল্টোটা। উৎসের ছক বলছে 'S11 প্রশ্ন "
                "তৈরিকরণ — এই পাঠই একমাত্র সরাসরি উৎস'। কিন্তু প্রশ্ন তৈরি BAN-S11-এর "
                "admitted_set-এর সদস্য আর C5 নির্বাচন করেছে বিরামচিহ্ন বসানো; নির্বাচনের বাইরের "
                "কাজ লিখলে COVERAGE off-choice হিসেবে ধরে (CD-138(b))। ছক authoring evidence, "
                "task declaration নয়।",
                "অনুশীলনী ৪ (আজ / গতকাল / আগামীকাল দিয়ে বাক্য) ব্যবহার করা হয়নি, একই কারণে এবং "
                "একই আকারে — উৎসের ছক এটিকে 'S10 ক্রিয়ার কাল' বলছে, ক্রিয়ার কাল BAN-S10-এর "
                "admitted_set-এর সদস্য, আর C5 নির্বাচন করেছে পদ নির্ণয়। এই তিনটি শব্দকে S03 "
                "বাক্য গঠনে ঢুকিয়ে দেওয়াও হয়নি: সেটা হতো কালের অনুশীলনকে বাক্য গঠনের নাম "
                "পরিয়ে C5-এর নির্বাচনের চারপাশ দিয়ে যাওয়া।",
                "অনুশীলনী ৫ (এলাকার বিখ্যাত তিনটি জিনিসের নাম) ব্যবহার করা যায়নি এবং কারণটি "
                "নীতিগত নয়, প্রমাণগত: উত্তরটি শিক্ষার্থীর নিজের এলাকার, extraction-এ তার কিছুই "
                "নেই, তাই তিন-টোকেনের কোনো anchor নেই এবং SOURCE-TRACE কোনো আইটেমকে সেখানে "
                "বাঁধতে পারত না।",
                "অনুশীলনী ৬ (সংগ্রহ করি — পুরানো কয়েন, অন্য দেশের টাকা, ডাকটিকিট) — উৎসের ⚠ "
                "ব্লক এটিকে শ্রেণিকক্ষের কাজ বলেছে, প্রশ্নপত্রের নয়। কোনো আইটেম এখান থেকে "
                "লেখা হয়নি এবং ভবিষ্যতের কোনো ঢেউয়েও লেখা হবে না।",
                "পঞ্চাশটি পুরানো জায়গার বুলেটে ছয়টি নাম ছাপা আছে — রাঙ্গার টেক, সোনারু তলা, "
                "কেন্দুয়া, মরজাল, টঙ্গী রাজার বাড়ি, জানখীর টেক। এগুলো নিয়ে ছয়টি আলাদা স্মরণ-প্রশ্ন "
                "লেখা যেত এবং লেখা হয়নি — সেটাই §৪-এর near-duplicate নিষেধের কাজ: কেবল নামটুকু "
                "বদলে ছয়বার একই প্রশ্ন করা ছয়টি প্রশ্ন নয়।",
                "মন্দির ভিটা ও বৌদ্ধ বিহার — উৎসের ⚠ ব্লক প্রশ্নকে অন্য নিদর্শনের দিকে নিতে "
                "বলেছে। শব্দ দুটি extraction-এ নেই, তাই এখানে কোনো নিষেধ প্রয়োগ করতেই হয়নি; "
                "তবু কোনো আইটেম সেদিকে যায়নি এবং যাবেও না।",
            ],
        },
        "flags": [],
        "pool_index": {"HW": hw, "AS": as_, "CT": ct},
        "slot_index": slot_index,
        "task_index": task_index,
        "source_index": source_index,
        "questions": questions,
        "waves": {"1": (f"Q01–Q{len(questions):02d} · 2026-08-18 · author_U17_wave1.py · "
                        f"পাঠ ১৭-এর প্রথম ব্যাংক, CD-141 teacher-lane-এ authored under "
                        f"tools/teacher_lane_template.md as rewritten at CD-171(h)")},
    }


def _norm(s):
    s = unicodedata.normalize("NFC", s or "")
    s = re.sub(r"[‘’“”'\"()\[\]।,;:?!—–\-….*_#>|/·]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


MARK_CHARS = {
    "দাঁড়ি": ("।",), "কমা": (",",), "প্রশ্নচিহ্ন": ("?",), "বিস্ময়চিহ্ন": ("!",),
    "উদ্ধরণ চিহ্ন": ("'", "‘", "’", "“", "”", '"'),
    "সেমিকোলন": (";",), "কোলন": (":",), "ড্যাশ": ("—", "–"),
}
TAUGHT_C5 = {"দাঁড়ি", "কমা", "প্রশ্নচিহ্ন", "বিস্ময়চিহ্ন", "উদ্ধরণ চিহ্ন"}


def s11_work_check(bank):
    """QB-CR-017, executed rather than asserted.

    Diffs each S11 stimulus against its accepted answer and counts the POSITIONS where a mark has
    to be inserted. A count of one is the defect QB-CR-017 names — an item satisfied by placing a
    single terminal mark — and this refuses to write the file on one. It also refuses any mark
    outside C5's taught set (CD-165 · CD-166), on the answer strings, which is where the gate
    looks too.
    """
    ok = True
    print("  S11 — QB-CR-017 insertion count, per item:")
    for q in bank["questions"]:
        if bank["slot_index"][q["qid"]] != "S11":
            continue
        m = re.match(r"^'(.*?)' — ", q["question_text"], re.S)
        raw = m.group(1)
        fixed = q["answer_key"]["accepted"][0]
        # Positions: walk the answer, count characters that are marks and are NOT in the stimulus
        # at the same relative point. Simplest faithful measure — strip every mark from `fixed`
        # and confirm the remainder is the stimulus, then count the marks removed.
        marks_in_fixed = [c for c in fixed if any(c in chars for chars in MARK_CHARS.values())]
        stripped = "".join(c for c in fixed if c not in "।,?!'‘’“”\";:—–")
        if _norm(stripped) != _norm(raw):
            print(f"    <-- {q['qid']}: stripping the marks from the answer does NOT give the "
                  f"stimulus back — the item changes words, not only punctuation")
            ok = False
        n = len(marks_in_fixed)
        used = sorted({c for c, chars in MARK_CHARS.items()
                       if any(ch in fixed for ch in chars)})
        off = [c for c in used if c not in TAUGHT_C5]
        flag = ""
        if n < 2:
            flag, ok = "   <-- SINGLE MARK — QB-CR-017's defect, REFUSED", False
        if off:
            flag, ok = f"   <-- BARRED MARK {off} (CD-165/CD-166)", False
        print(f"    {q['qid']}: {n} mark(s) to insert — {' · '.join(used)}{flag}")
    return ok


def selfcheck(bank):
    """Cheap pre-gate arithmetic, so a failing run says WHY before the suite does."""
    import collections
    qs = bank["questions"]
    n = len(qs)
    c = collections.Counter(q["bloom_level"] for q in qs)
    print(f"  items: {n}")
    print("  bloom: " + " · ".join(f"{k} {c[k]}" for k in
                                   ["Remember", "Understand", "Apply", "Analyze",
                                    "Evaluate", "Create"]))
    d = collections.Counter(q["difficulty"] for q in qs)
    print(f"  difficulty: easy {100*d['easy']/n:.1f}% (floor 30%) · medium "
          f"{100*d['medium']/n:.1f}% · hard {100*d['hard']/n:.1f}%")
    sc = bank["header"]["slot_counts"]
    print("  slots: " + " · ".join(f"{s} {sc[s]}" for s in sorted(sc)))
    pools = bank["pool_index"]
    print("  pools: " + " · ".join(f"{k} {len(v)}" for k, v in pools.items())
          + f"  (sum {sum(len(v) for v in pools.values())} of {n})")
    for q in qs:
        for s in ([q["question_text"]] + [o["text"] for o in q.get("options", [])]
                  + [o.get("why_wrong", "") for o in q.get("options", [])]
                  + (q.get("answer_key", {}).get("accepted") or [])
                  + [b for bl in q.get("blanks", []) for b in bl.get("accepted", [])]):
            if re.search(r"[0-9]", s or ""):
                print(f"  <-- ASCII DIGIT in {q['qid']}: {s[:40]}")

    hay = _norm((ROOT / EXTRACTION).read_text(encoding="utf-8"))
    bad_anchor = 0
    for qid, a in bank["source_index"].items():
        na = _norm(a)
        if len(na.split()) < 3:
            print(f"  <-- ANCHOR TOO SHORT {qid}: {a!r}")
            bad_anchor += 1
        elif na not in hay:
            print(f"  <-- ANCHOR NOT IN EXTRACTION {qid}: {a!r}")
            bad_anchor += 1
    print(f"  anchors: {len(bank['source_index'])} checked, {bad_anchor} bad")

    by_slot = {}
    for q in qs:
        by_slot.setdefault(bank["slot_index"][q["qid"]], []).append(
            (q["qid"], _norm(q["question_text"])))
    worst = 0.0
    for s, grp in sorted(by_slot.items()):
        for i in range(len(grp)):
            for j in range(i + 1, len(grp)):
                ta, tb = set(grp[i][1].split()), set(grp[j][1].split())
                sim = len(ta & tb) / len(ta | tb) if (ta | tb) else 0.0
                worst = max(worst, sim)
                if sim >= 0.85:
                    print(f"  <-- BORDERLINE {s}: {grp[i][0]} ~ {grp[j][0]} {sim:.0%}")
    print(f"  worst within-slot stem similarity: {worst:.0%} (PLAN reports at 85%, fails at 95%)")
    return bad_anchor == 0


if __name__ == "__main__":
    bank = build()
    a = selfcheck(bank)
    b = s11_work_check(bank)
    if not (a and b):
        raise SystemExit("  REFUSED — the bank was not written; fix the lines marked <-- above")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(bank, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"  wrote {OUT.relative_to(ROOT)}  ({len(bank['questions'])} items)")
