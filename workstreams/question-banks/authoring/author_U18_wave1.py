#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""author_U18_wave1.py — C5 Bangla, পাঠ ১৮ (ইচ্ছামতী) question bank, wave 1.

Run from the repo root:
    python3 workstreams/question-banks/authoring/author_U18_wave1.py

WHY THE SCRIPT IS THE ARTIFACT (LOCAL.md, "Artifacts & naming"). A bank nobody can re-derive is
not reviewable; this file is what makes it reproducible and reviewable AS CONTENT. It is promoted
with its bank.

WHAT BINDS THIS BANK — CD-171(c)'s complete list, each clause named where it bites.

 1. CD-138(e) DECLARATION, derived FROM THE SOURCE AT SOURCE. Written out in full at
    `workstreams/question-banks/_wip/U18_ADMISSIBILITY_2026-08-18.md`. **All thirteen
    non-paper-level slots are ADMITTED and `slot_exclusions` is EMPTY** — every one of them is
    supported by content printed in the section. The chapter's own *কোন প্রশ্নে কাজে লাগবে* line
    names only six slots and it caps nothing: CD-122(b) ruled it advisory and CD-134(c) forbids
    recording line-absence as an exclusion reason, so S02 · S04 · S05 · S06 · S08 · S11 · S12 ·
    S13 are admitted ON CONTENT and not on that sentence's silence.

 2. S01 AND S09 ARE ADMITTED ON THE SOURCE'S OWN SENTENCE, quoted rather than inferred:
    "কবিতা চারটি: পাঠ ১৩, ১৫, ১৮, ২০ — এগুলোই S01 (কবিতা মুখস্থ) ও S09 (মূলভাব) প্রশ্নের উৎস।"
    পাঠ ১৮ IS on that list. The same sentence took both slots from পাঠ ১৪ and পাঠ ১৬ and gave
    them to পাঠ ১৫ — one sentence deciding four chapters in both directions, so it is quoted and
    not reasoned around (CD-138(e) forbids inferring admissibility from content in EITHER
    direction).

 3. S14/S15 ARE NOT DECLARED AT ALL, AND THAT IS THE CORRECT SHAPE — NOT AN OMISSION.
    CD-147(a) makes আবেদনপত্র and রচনা paper-level for EVERY chapter, categorically; CD-147(c)
    says a bank silent about them is CORRECT, not INCOMPLETE, and a header ADMITTING one FAILs.
    **CD-147(g) is this chapter's own clause.** পাঠ ১৮'s অনুশীলনী ৫ carries a titled essay prompt
    ("আমি যা হতে চাই") and the extraction's কোন প্রশ্নে line names S15 for this পাঠ. A 2026-08-16
    probe read that as evidence পাঠ ১৮ admits S15. The Principal REFUSED that conclusion in terms:
    "পাঠ ১৮ does not admit S15 either. The anchor exists; the pipeline is still the paper's."
    The anchor is real and is not retracted; it is simply not what decides the question. NO S15
    ITEM IS AUTHORED AND S15 IS NOT ADMITTED.

 4. §4's NEAR-DUPLICATE BAN IS NOW THE ONLY BOUND (CD-171(a) retired every count). There is no
    minimum, no maximum, no Bloom floor and no per-slot demand. Each slot below stops where the
    section stops supporting it, and the stopping reason is written in that slot's own comment.
    NO ITEM IS AUTHORED TO REACH A NUMBER, BECAUSE THERE IS NO NUMBER.

 5. TAUGHT SET — CD-165 as amended by CD-166. C5's বিরামচিহ্ন are
    দাঁড়ি · কমা · প্রশ্নচিহ্ন · বিস্ময়চিহ্ন · উদ্ধরণ চিহ্ন. **ড্যাশ and সেমিকোলন are BARRED.**

CD-149 — BAN-S01's UNIT IS THE PRINTED LINE. প্রথম ৮ লাইন means eight lines as the book sets
them; the পঙ্‌ক্তি reading is REJECTED. CD-149(b) records that পাঠ ১৮'s own delimiter
("…নামবে অন্ধকার।") ALREADY falls exactly at printed line 8, and CD-149(e) says this chapter's
delimiter needs no adjustment when authored. Counted again here at source: the poem sets 48
printed lines and the first stanza is lines 1–8, ending at that endpoint. S01 is authored to that
span and the count is not restated in any student-facing string.

QB-CR-017 (OPEN) IS A DEFECT CLASS THIS BANK MUST NOT REPRODUCE — and the check is mechanical.
Thirteen S11 items across U13–U16 are each satisfied by placing ONE terminal mark; no gate sees it,
because every gate reads metadata and the defect lives in the prose. selfcheck() below DIFFS
each S11 stimulus against its key, counts the marks that must be inserted, FAILS the build on a
count of one, and FAILS on any mark outside C5's taught set. That is QB-CR-017's own proposed gate,
run here at authoring time on this bank only.

THE POEM'S PRINTED MARKS, counted line by line before any S11 stimulus was chosen:
  দাঁড়ি   — lines 4 8 12 16 20 24 26 28 32 34 36 38 44 48             (taught)
  কমা     — lines 6 11 17 18 22 23 27 42 45                            (taught)
  প্রশ্নচিহ্ন — line 40 only, "আমিই সে কি জানি"                              (taught)
  বিস্ময়চিহ্ন — line 46 only, "রাত্তিরে থম থম"                                (taught)
  ড্যাশ    — LINE 10 ONLY, "দুই পারেরই সাথে"                            ** BARRED AT C5 **
  সেমিকোলন — NOT PRINTED ANYWHERE IN THIS POEM
  উদ্ধরণ চিহ্ন — not printed (the poem carries no reported speech)        (taught, unused)
So printed line 10 is UNUSABLE as S11 stimulus and is not used. This is the measurement QB-CR-017
made at পাঠ ১৫ and found fatal there — that poem prints ড্যাশ and সেমিকোলন in FOUR lines, leaving
almost no admitted-only multi-mark span. পাঠ ১৮ prints ড্যাশ in one line and সেমিকোলন in none.

THE ⚠ BLOCK, clause by clause, and what each costs:
  · C-03 — "গান গেয়ে যাই" (printed line 15) and "পরীর নাচন" (printed line 27) may not be lifted
    into a question. NO stem, option, why_wrong, key, model_note, rubric row or S11 stimulus below
    touches either line. The poem is taught whole; these two lines are not asked about.
  · S01 — "প্রথম স্তবকই নিরাপদ"; the authored span is exactly the first stanza.
  · "কোণে কোণে আপন মনে করছে তারা কী কে" — printed lines 33–36 are left ENTIRELY unused; no anchor
    reaches them.
  · কবির নাম শুধু তথ্য হিসেবে — no honorific adjective anywhere. This is also the register's own
    E-AUTHOR-ENDORSE row constraint, scoped "C4 (এবং C5-এ কবিতার প্রশ্নে)". S01's model_note says
    so; no item writes any honorific.

NO INVENTED PERSONAL NAME APPEARS ANYWHERE. The only personal name in the bank is রবীন্দ্রনাথ
ঠাকুর, the poet the chapter itself records, carried as information (S01, S05). No REF-20 name is
needed because no item stages a character.

POST-REVIEW FIX PASS — 2026-08-18, after the step 5b factual/curation review
(`workstreams/question-banks/reports/BAN_U18_REVIEW_2026-08-18.txt`, VERDICT: 7 DEFECT(S)) and the
Principal's ruling on it. The bank is regenerated FROM THIS SCRIPT; the JSON is never hand-edited.

  R1 — THE TAUGHT-SET BAR IS ON MARKS THE STUDENT PLACES, not on marks that appear in a model
  answer. The review's finding 2 (";" and "—" inside `answer_key.accepted` at Q01 Q04 Q08 Q43 Q44
  Q45 Q47 Q48 Q49 Q50 Q71 Q72 Q73 Q74, including the S12 form "চ্ছ = চ + ছ; নতুন শব্দ — কচ্ছপ")
  IS THEREFORE NOT A DEFECT AND IS NOT FIXED. Those fourteen items are left exactly as authored,
  byte for byte, and are not tidied. CD-165/CD-166 still bar ড্যাশ and সেমিকোলন in what a STUDENT
  must write, which is why no S11 item requires either and printed line 10 is still unused.

  FIX 1 (finding 1) — Q30's three `why_wrong` strings attributed poets from the file's top-of-file
  table and from পাঠ ১৩/১৫/২০, all outside this bank's authority span. Each now says only that
  this section names রবীন্দ্রনাথ ঠাকুর as the কবি. The option TEXTS (bare poet names as
  distractors) are unchanged — they are not attributions.
  FIX 3 (finding 3) — Q36's distractor গ turned on ঢেউ, whose ONLY occurrence in the poem is
  printed line 27 ("ঢেউয়ে ঢেউয়ে পরীর নাচন,"), the C-03-barred line, and its `why_wrong` sent the
  reader back to it. The distractor is replaced with a wrong reading drawn from the unbarred
  lines 41–44 and the `why_wrong` rewritten. The `curation` paragraph's claim that no বিকল্প or
  why_wrong touches the two barred চরণ is true again.
  FIX 4 (finding 4) — S10: "নামপদ" out, "নাম-শব্দ" in, at Q57 · Q58 · Q61 · Q64. See the S10 block.
  FIX 5 (finding 5) — Q40: the "আপন" variant deleted. See the S06 block.
  FIX 6 (finding 6) — policy codes out of marker-facing model_notes. See the TEACHER_KEY block.
  FIX 7 (finding 7) — the open clause only where the answer is open. See the TEACHER_KEY block.

  TWO UNCOUNTED REVIEWER QUALITY NOTES ALSO FIXED, each marked at its site: Q34's honorific
  register shift inside one item, and Q76's definition, which admitted the chapter's own "পার"
  as well as ডাঙা. Q44 (folded justification, missing "ডান দিকে") and Q50 (একখনি→একখানি) are
  NOT touched: both are R1-dissolved carriers and the ruling freezes them.

LIMIT OF THE SOURCE, recorded rather than smoothed (CD-167(d)'s precedent). The extraction's
অনুশীলনী list runs ১ ৩ ৪ ৫ ৬ — **অনুশীলনী ২ IS ABSENT FROM THE EXTRACTION.** Nothing is authored
from it. For পাঠ ১৩–২৩ the extraction IS the whole of the repo-resident textbook, so this cannot
be checked at source at all.
"""
import json
import pathlib
import re
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[3]
EXTRACTION = "canon/marklogic/C5_Bangla_Source_13-23.md"
OUT = ROOT / "workstreams/question-banks/banks/C5_BAN_U18_QuestionBank_v1.json"
CHAPTER = "পাঠ ১৮ — ইচ্ছামতী"

# topic_tag / ref19_topic_id pairs. Every number verified at `canon/topics/TOPIC_NUMBERS.md` this
# session; a number with no row there is not used (CD-044). পাঠ ১৮ is কবিতা and its primary number
# is -05 / BAN-POEM. The rest are CROSS-CUTTING STRANDS and are per-QUESTION, not per-chapter.
POEM = ("TOP-BAN-C5-05", "BAN-POEM")
VOCAB = ("TOP-BAN-C5-01", "BAN-VOCAB")
WORDREL = ("TOP-BAN-C5-01", "BAN-WORDREL")
JUKTO = ("TOP-BAN-C5-01", "BAN-JUKTOBARNA")
PARTSP = ("TOP-BAN-C5-01", "BAN-PARTSPEECH")
SENT = ("TOP-BAN-C5-02", "BAN-SENTENCE")
# S11 rides -13 (বিরামচিহ্ন, MINTED CD-044) with ref19_topic_id BAN-SENTENCE — REF-19 v1.10 carries
# NO Bangla punctuation slug at all (PENDING-P-008, FLAGGED/non-blocking) and minting one here
# would be QB-CR-008's error in another register. This is the established U13–U16 choice.
PUNCT = ("TOP-BAN-C5-13", "BAN-SENTENCE")

# CD-136(b) teacher-gloss provenance, declared in the item's OWN model_note so the provenance
# travels with the item and not only with the bank header. P-037 (OPEN) admits it on
# `short_answer` and `descriptive` only; every item carrying it below is `short_answer`.
#
# FIX 6 — POLICY LEAKAGE OUT OF MARKER-FACING TEXT (2026-08-18 review, finding 6; Principal
# applied). A model_note is read by the MARKER and may carry the marking instruction and nothing
# else. The internal codes that used to ride these constants are recorded HERE and in the bank
# header instead, which is where an auditor looks for them:
#   · CD-138(b) — BAN-S10's admitted_set holds পদ নির্ণয় · ক্রিয়ার কাল · ভাষারীতি পরিবর্তন, and
#     C5 has SELECTED পদ নির্ণয়. The other two are off-choice at this class and NO item does
#     either. That is an AUTHORING constraint; it told the marker nothing and is gone from the
#     note. See header["s10_selection_ruling"].
#   · SLOT_REGISTER BAN-S12 composite — the slot's two halves (যুক্তবর্ণ ভাঙা + শব্দ গঠন) are both
#     required. The REQUIREMENT is a marking instruction and STAYS in the note, in plain Bangla;
#     the register citation is gone. See header["s12_composite_ruling"].
#   · CD-149 · SLOT_REGISTER BAN-S01 · E-AUTHOR-ENDORSE (Q01) — same treatment at S01 below;
#     the marks split and the no-honorific rule stay as instructions, the codes go to
#     header["s01_span_ruling"].
#   · CD-136 STAYS, bare and unchanged, in the exact plain form the four pushed banks already use.
#     It is the item's own provenance token, it is what gates.py's P-037 check keys on, and the
#     proposed `[[CD-136]]` delimited form has NO stripping step in this repo — so no `[[` is
#     introduced anywhere. Removing the OTHER codes is what resolves the CD-136(b) collision.
#
# FIX 7 — THE OPEN CLAUSE ONLY WHERE THE ANSWER IS OPEN (review finding 7). The old single
# TEACHER_KEY carried "কাছাকাছি অর্থের যেকোনো শুদ্ধ উত্তর গ্রহণযোগ্য" onto S10 and S12, whose
# answers are CLOSED — a word either is a বিশেষ্য or is not, and a যুক্তবর্ণ decomposition is
# fixed — where the clause instructed the marker to accept answers the slot must refuse, and at
# S12 contradicted the same note's own insistence that both halves are required. The constant is
# split three ways and each slot takes the one that is true of it:
#   S06 (বিপরীত শব্দ) → OPEN. A near-synonym antonym really is acceptable.
#   S10 (পদ নির্ণয়)  → CLOSED. There is no "কাছাকাছি অর্থ" of a পদ.
#   S12 (যুক্তবর্ণ)    → HALF-OPEN, stated as such: the decomposition is fixed, the new word is free.
TEACHER_KEY_BASE = ("এই উত্তরকুঞ্জি শিক্ষকের দেওয়া — বাংলা ভাষার সাধারণ তথ্য, পাঠে এর উত্তর দেওয়া "
                    "নেই (CD-136)। উদ্দীপক পাঠ ১৮ থেকেই নেওয়া।")

TEACHER_KEY_OPEN = TEACHER_KEY_BASE + " কাছাকাছি অর্থের যেকোনো শুদ্ধ উত্তর গ্রহণযোগ্য।"

TEACHER_KEY_CLOSED = (TEACHER_KEY_BASE + " এই প্রশ্নের উত্তর নির্দিষ্ট — উত্তরকুঞ্জিতে দেওয়া "
                      "রূপগুলোই গ্রহণযোগ্য, কাছাকাছি অর্থের অন্য উত্তর নয়।")

PADA_KEY = TEACHER_KEY_CLOSED

JUKTO_KEY = (TEACHER_KEY_BASE + " যুক্তবর্ণ ভাঙার অংশটি নির্দিষ্ট, এতে ছাড় নেই। নতুন শব্দ "
             "শিক্ষার্থীর নিজের যেকোনোটি গ্রহণযোগ্য, যদি তাতে ওই যুক্তবর্ণ থাকে। দুটি কাজই করতে "
             "হবে — শুধু ভাঙলে বা শুধু শব্দ গঠন করলে অর্ধেক কাজ।")

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


# ── ANCHORS ───────────────────────────────────────────────────────────────────────────────
# Every anchor is a span of the পাঠ ১৮ section, verified by selfcheck() against the chapter
# slice (not merely against the file) before the bank is written. Printed-line numbers are given
# so a reader can check the ⚠ bars: nothing anchors at lines 15, 27 or 33–36, and nothing but the
# barred-line census reads line 10.
A_L1_4 = "যখন যেমন মনে করি\n> তাই হতে পাই যদি\n> আমি তবে একখনি হই\n> ইচ্ছামতী নদী।"
A_L5_8 = "রইবে আমার দখিন ধারে\n> সূর্য ওঠার পার,\n> বাঁয়ের ধারে সন্ধেবেলায়\n> নামবে অন্ধকার।"
A_L9_12 = "আমি কইব মনের কথা"
A_L11_12 = "আধেক কথা দিনের বেলায়,\n> আধেক কথা রাতে।"
A_L13_14 = "যখন ঘুরে ঘুরে বেড়াই\n> আপন গাঁয়ের ঘাটে"
A_L17_20 = "গাঁয়ের মানুষ চিনি, যারা\n> নাইতে আসে জলে,\n> গোরু মহিষ নিয়ে যারা\n> সাঁতরে ওপার চলে।"
A_L21_24 = "দূরের মানুষ যারা তাদের\n> নতুনতরো বেশ,\n> নাম জানি নে, গ্রাম জানি নে\n> অদ্ভুতের একশেষ।"
A_L25_26 = "জলের উপর ঝলোমলো\n> টুকরো আলোর রাশি।"
A_L37_40 = "গাঁয়ের লোকে চিনবে আমার\n> কেবল একটুখানি।\n> বাকি কোথায় হারিয়ে যাবে\n> আমিই সে কি জানি?"
A_L41_44 = "একধারেতে মাঠে ঘাটে\n> সবুজ বরন শুধু,\n> আর একধারে বালুর চরে\n> রৌদ্র করে ধু ধু।"
A_L45_48 = "দিনের বেলায় যাওয়া আসা,\n> রাত্তিরে থম থম!\n> ডাঙার পানে চেয়ে চেয়ে\n> করবে গা ছম ছম।"

A_TITLE = "রবীন্দ্রনাথ ঠাকুর · কবিতা"
A_S01 = "প্রথম ৮ পঙ্‌ক্তি (S01-এর জন্য)"
A_GLOSS = ("আধেক — অর্ধেক · ঘাটের ধাপ — ঘাটের সিঁড়ি · ডাঙা — তীর; শুকনো জায়গা · দখিন ধারে — "
           "ডান দিকে · নতুনতরো — অন্যরকম · নাইতে — গোসল করতে · বরন — বর্ণ; রং · রাত্তির — রাতের বেলা")
A_EX1 = "জোড়া শব্দ দিয়ে বাক্য — চুপচাপ · মাঠে ঘাটে · ধু ধু · চেয়ে চেয়ে · থম থম · ছম ছম · ঝলমল"
A_EX3A = "ক. কবি কী হতে চান? কেন হতে চান?"
A_EX3B = "খ. ইচ্ছামতী নদীর কোন দিকে সূর্য ওঠে?"
A_EX3C = "গ. ইচ্ছামতী নদী কোন পারের মানুষের সাথে কথা বলবে?"
A_EX3D = "ঘ. ইচ্ছামতী নদীর দুই ধারের পার্থক্য কী?"
A_EX3E = "ঙ. ইচ্ছামতী নদীতীরের দিন ও রাতের বর্ণনা দাও।"


# =====================================================================================
# S01 · কবিতা মুখস্থ · COMPOSITE (কবির নাম · কবিতার নাম · প্রথম ৮ লাইন) · marks 10 · Remember
# ONE ITEM. A second memorisation stem for the same কবিতা would be the same question; §4's
# near-duplicate ban is the whole bound now (CD-171(a)) and this slot exhausts at one.
# THE SPAN IS EIGHT PRINTED LINES (CD-149(a)) — lines 1–8, the first stanza, ending at the
# extraction's own endpoint "নামবে অন্ধকার", which CD-149(b) records as already agreeing with
# the printed-line reading at this chapter. The count is NOT restated in the student-facing stem;
# the endpoints are what the student is given.
# E-AUTHOR-ENDORSE (SLOT_REGISTER BAN-S01, scope "C4 এবং C5-এ কবিতার প্রশ্নে") and the ⚠ block's
# fourth clause: the poet's name is asked as INFORMATION and no honorific adjective is accepted.
# =====================================================================================
add("S01", ["কবির নাম", "কবিতার নাম", "প্রথম ৮ লাইন"], POEM,
    "কবি ও কবিতার নাম লিখে 'ইচ্ছামতী' কবিতার 'যখন যেমন মনে করি' থেকে "
    "'নামবে অন্ধকার।' পর্যন্ত অংশটুকু মুখস্থ লেখো।",
    "short_answer", "structured", "Remember", "medium", 10, A_S01,
    **sa(["কবিতা: ইচ্ছামতী; কবি: রবীন্দ্রনাথ ঠাকুর। যখন যেমন মনে করি তাই হতে পাই যদি "
          "আমি তবে একখনি হই ইচ্ছামতী নদী। রইবে আমার দখিন ধারে সূর্য ওঠার পার, "
          "বাঁয়ের ধারে সন্ধেবেলায় নামবে অন্ধকার।"],
         "নম্বর ভাগ: কবির নাম ১ + কবিতার নাম ১ + প্রথম ৮ লাইন ৮ = ১০। অংশটি বইয়ের ছাপা আট "
         "লাইন, অর্থাৎ প্রথম স্তবক। চরণ হুবহু পাঠের মতো হতে হবে; বানান ও যতিচিহ্নে ছাড় দেওয়া "
         "যাবে। কবির নাম কেবল তথ্য হিসেবে — কোনো সম্মানসূচক বিশেষণ লেখা যাবে না বা চাওয়া "
         "যাবে না।"))


# =====================================================================================
# S02 · শব্দার্থ · simple · marks 1 · all Remember, easy
# EIGHT ITEMS AND THE SLOT IS EXHAUSTED: the chapter's অর্থ জেনে নিই list holds exactly eight
# glosses and no ninth word in the section is glossed anywhere. The keys are IN the chapter, so no
# CD-136 teacher-key note is carried — CD-136 is not in play for these.
# =====================================================================================
S02 = [
    ("আধেক", ["অর্ধেক"]),
    ("ঘাটের ধাপ", ["ঘাটের সিঁড়ি"]),
    ("ডাঙা", ["তীর", "শুকনো জায়গা", "তীর; শুকনো জায়গা"]),
    ("দখিন ধারে", ["ডান দিকে"]),
    ("নতুনতরো", ["অন্যরকম"]),
    ("নাইতে", ["গোসল করতে"]),
    ("বরন", ["বর্ণ", "রং", "বর্ণ; রং"]),
    ("রাত্তির", ["রাতের বেলা"]),
]
for w, acc in S02:
    add("S02", "মূল কাঠামো", VOCAB,
        f"পাঠে ব্যবহৃত '{w}' শব্দের অর্থ লেখো।",
        "short_answer", "short", "Remember", "easy", 1, A_GLOSS, **sa(acc))


# =====================================================================================
# S03 · বাক্য গঠন · simple · marks 1 · all Apply, medium
# TEN ITEMS. Seven are অনুশীলনী ১'s own জোড়া শব্দ, which IS this slot's task at this chapter and
# is the whole of that exercise; three more are glossed words from অর্থ জেনে নিই. It stops there:
# every further candidate word in the section is either inside a ⚠-barred line or already carried,
# and a further stem would be a near-duplicate of one below.
# BAN-S03-NOJOIN is honoured — not one of these is joined to a যুক্তবর্ণ or কারচিহ্ন task.
# NO MODEL SENTENCE CARRIES A PERSONAL NAME.
# =====================================================================================
S03 = [
    ("চুপচাপ", "ক্লাসে সবাই চুপচাপ বসে বইয়ের পাতা উল্টাচ্ছিল।", A_EX1),
    ("মাঠে ঘাটে", "ছুটির দিনে ছেলেমেয়েরা মাঠে ঘাটে ঘুরে বেড়ায়।", A_EX1),
    ("ধু ধু", "বৈশাখ মাসে নদীর চর ধু ধু করে।", A_EX1),
    ("চেয়ে চেয়ে", "খোকা জানালা দিয়ে চেয়ে চেয়ে বৃষ্টি দেখছিল।", A_EX1),
    ("থম থম", "ঝড়ের আগে চারদিক থম থম করছিল।", A_EX1),
    ("ছম ছম", "অন্ধকার পথে হাঁটতে গিয়ে গা ছম ছম করে উঠল।", A_EX1),
    ("ঝলমল", "উৎসবের রাতে সারা শহর আলোয় ঝলমল করছিল।", A_EX1),
    ("ডাঙা", "নৌকা থেকে নেমে আমরা ডাঙায় উঠে দাঁড়ালাম।", A_GLOSS),
    ("আধেক", "আধেক পথ হেঁটে এসে সে খানিক জিরিয়ে নিল।", A_GLOSS),
    ("নতুনতরো", "মেলায় গিয়ে সে নতুনতরো অনেক জিনিস দেখল।", A_GLOSS),
]
for w, model, anc in S03:
    add("S03", "মূল কাঠামো", SENT,
        f"'{w}' শব্দটি দিয়ে একটি অর্থপূর্ণ বাক্য লেখো।",
        "short_answer", "short", "Apply", "medium", 1, anc,
        **sa([model], "শিক্ষার্থীর নিজের যেকোনো শুদ্ধ বাক্য গ্রহণযোগ্য, যদি শব্দটি সঠিক অর্থে "
             "ব্যবহৃত হয় এবং বাক্যটি বিরামচিহ্নসহ সম্পূর্ণ হয়। নমুনা উত্তর দেওয়া হলো।"))


# =====================================================================================
# S04 · শূন্যস্থান পূরণ · simple · marks 1 · all Remember, easy
# TEN ITEMS, each frame a printed line of the poem with one word cut. The frames are drawn from
# the usable line-groups; the ones left out are the ⚠-barred lines (15, 27, 33–36) and line 10,
# whose ড্যাশ is barred at C5. Past ten, a further frame would cut a second word out of a line
# already used and the two stems would be near-duplicates.
# =====================================================================================
S04 = [
    ("'আমি তবে একখনি হই ______ নদী।' — শূন্যস্থান পূরণ করো।", ["ইচ্ছামতী"], A_L1_4),
    ("'রইবে আমার ______ ধারে সূর্য ওঠার পার,' — শূন্যস্থান পূরণ করো।", ["দখিন"], A_L5_8),
    ("'বাঁয়ের ধারে সন্ধেবেলায় নামবে ______।' — শূন্যস্থান পূরণ করো।", ["অন্ধকার"], A_L5_8),
    ("'আধেক কথা দিনের বেলায়, আধেক কথা ______।' — শূন্যস্থান পূরণ করো।", ["রাতে"], A_L11_12),
    ("'গাঁয়ের মানুষ চিনি, যারা ______ আসে জলে,' — শূন্যস্থান পূরণ করো।", ["নাইতে"], A_L17_20),
    ("'গোরু মহিষ নিয়ে যারা ______ ওপার চলে।' — শূন্যস্থান পূরণ করো।", ["সাঁতরে"], A_L17_20),
    ("'জলের উপর ঝলোমলো টুকরো ______ রাশি।' — শূন্যস্থান পূরণ করো।", ["আলোর"], A_L25_26),
    ("'একধারেতে মাঠে ঘাটে ______ বরন শুধু,' — শূন্যস্থান পূরণ করো।", ["সবুজ"], A_L41_44),
    ("'আর একধারে ______ চরে রৌদ্র করে ধু ধু।' — শূন্যস্থান পূরণ করো।", ["বালুর"], A_L41_44),
    ("'ডাঙার পানে চেয়ে চেয়ে করবে গা ______।' — শূন্যস্থান পূরণ করো।", ["ছম ছম"], A_L45_48),
]
for text, acc, anc in S04:
    add("S04", "মূল কাঠামো", POEM, text, "fill_blank", "short", "Remember", "easy", 1, anc,
        blanks=[{"blank_no": 1, "accepted": acc}])


# =====================================================================================
# S05 · বহুনির্বাচনি · simple · marks 1 · 3 Remember (easy) + 5 Understand (medium)
# BLOOM IS TAGGED FROM DEMAND, NOT FROM THE SLOT (QB-CR-011/QB-CR-012). বহুনির্বাচনি is a method
# of ANSWERING and fixes no level: the three Remember items ask back a fact the poem prints, the
# five Understand ones require reading a line and saying what it means.
# Exactly one correct option each; every distractor carries a why_wrong drawn from the section.
# NO OPTION, KEY OR why_wrong TOUCHES printed line 15 or 27 (C-03) or lines 33–36.
# EIGHT ITEMS: the usable stanzas support eight distinct readings and a ninth would re-ask one of
# these from the other side.
# =====================================================================================
add("S05", "মূল কাঠামো", POEM, "'ইচ্ছামতী' কবিতাটির কবি কে?",
    "mcq", "mcq", "Remember", "easy", 1, A_TITLE,
    options=[
        {"option_id": "ক", "text": "রবীন্দ্রনাথ ঠাকুর", "is_correct": True},
        {"option_id": "খ", "text": "কাজী নজরুল ইসলাম", "is_correct": False,
         "why_wrong": "এই পাঠের শুরুতেই 'ইচ্ছামতী' কবিতার কবির নাম লেখা আছে — রবীন্দ্রনাথ ঠাকুর।"},
        {"option_id": "গ", "text": "আল মাহমুদ", "is_correct": False,
         "why_wrong": "পাঠ অনুযায়ী 'ইচ্ছামতী' কবিতার কবি রবীন্দ্রনাথ ঠাকুর।"},
        {"option_id": "ঘ", "text": "কাজী কাদের নেওয়াজ", "is_correct": False,
         "why_wrong": "পাঠে এই কবিতার কবি হিসেবে কেবল রবীন্দ্রনাথ ঠাকুরের নামই দেওয়া আছে।"}])

add("S05", "মূল কাঠামো", POEM, "কবি নিজে কী হতে চান বলে কবিতায় বলেছেন?",
    "mcq", "mcq", "Remember", "easy", 1, A_L1_4,
    options=[
        {"option_id": "ক", "text": "ইচ্ছামতী নদী", "is_correct": True},
        {"option_id": "খ", "text": "গাঁয়ের ঘাট", "is_correct": False,
         "why_wrong": "ঘাট কবিতায় আছে, কিন্তু কবি ঘাট হতে চাননি — তিনি ঘাটে ঘুরে বেড়ানোর কথা বলেছেন।"},
        {"option_id": "গ", "text": "বালুর চর", "is_correct": False,
         "why_wrong": "বালুর চর নদীর এক ধারের বর্ণনা, কবির ইচ্ছা নয়।"},
        {"option_id": "ঘ", "text": "দূরের মাঠ", "is_correct": False,
         "why_wrong": "দূরের মাঠ কবিতায় নদীর যাওয়ার জায়গা, কবির রূপ নয়।"}])

add("S05", "মূল কাঠামো", POEM, "ইচ্ছামতী নদীর কোন ধারে সূর্য ওঠে?",
    "mcq", "mcq", "Remember", "easy", 1, A_L5_8,
    options=[
        {"option_id": "ক", "text": "দখিন ধারে", "is_correct": True},
        {"option_id": "খ", "text": "বাঁয়ের ধারে", "is_correct": False,
         "why_wrong": "বাঁয়ের ধারে সন্ধেবেলায় অন্ধকার নামে বলে কবিতায় আছে।"},
        {"option_id": "গ", "text": "বালুর চরে", "is_correct": False,
         "why_wrong": "বালুর চরের কথা এসেছে রৌদ্রের প্রসঙ্গে, সূর্য ওঠার প্রসঙ্গে নয়।"},
        {"option_id": "ঘ", "text": "ঘাটের ধাপে", "is_correct": False,
         "why_wrong": "ঘাটের ধাপ জলের নিচে তলিয়ে যাওয়ার প্রসঙ্গে এসেছে।"}])

add("S05", "মূল কাঠামো", POEM,
    "'আধেক কথা দিনের বেলায়, আধেক কথা রাতে।' — এই দুই চরণে কবি কী বোঝাতে চেয়েছেন?",
    "mcq", "mcq", "Understand", "medium", 1, A_L11_12,
    options=[
        {"option_id": "ক", "text": "নদী তার মনের কথা দুই পারের সঙ্গে ভাগ করে বলবে — কিছু দিনে, কিছু রাতে",
         "is_correct": True},
        {"option_id": "খ", "text": "নদী দিনে কথা বলবে, রাতে চুপ করে থাকবে", "is_correct": False,
         "why_wrong": "চরণ দুটিতে রাতেও কথা বলার কথা স্পষ্ট করে আছে।"},
        {"option_id": "গ", "text": "নদীর কথা কেউ শোনে না", "is_correct": False,
         "why_wrong": "কবিতায় নদী দুই পারের সাথেই কথা বলছে।"},
        {"option_id": "ঘ", "text": "নদী কেবল দূরের মানুষের সঙ্গে কথা বলবে", "is_correct": False,
         "why_wrong": "দূরের মানুষদের নাম ও গ্রাম নদী জানে না বলে কবিতায় আছে।"}])

add("S05", "মূল কাঠামো", POEM,
    "'নাম জানি নে, গ্রাম জানি নে' — কাদের সম্পর্কে কবি এ কথা বলেছেন?",
    "mcq", "mcq", "Understand", "medium", 1, A_L21_24,
    options=[
        {"option_id": "ক", "text": "দূরের মানুষ, যাদের বেশ অন্যরকম", "is_correct": True},
        {"option_id": "খ", "text": "গাঁয়ের মানুষ, যারা জলে নাইতে আসে", "is_correct": False,
         "why_wrong": "গাঁয়ের ওই মানুষদের নদী চেনে বলে কবিতায় আছে।"},
        {"option_id": "গ", "text": "যারা গোরু মহিষ নিয়ে ওপার যায়", "is_correct": False,
         # Reviewer quality note (uncounted): this why_wrong shifted to honorifics (তাঁরা · যাঁদের)
         # for the same villagers option খ calls "যারা" — two registers for one group inside one
         # item. Levelled to the item's own register; the chapter writes "যারা".
         "why_wrong": "তারাও গাঁয়েরই মানুষ, যাদের নদী চেনে।"},
        {"option_id": "ঘ", "text": "যারা ঘাটের ধাপে বসে থাকে", "is_correct": False,
         "why_wrong": "ঘাটের ধাপের প্রসঙ্গটি আলাদা; সেখানে চেনা-অচেনার কথা নেই।"}])

add("S05", "মূল কাঠামো", POEM,
    "কবিতা অনুসারে নদীর দুই ধারের চেহারা কেমন?",
    "mcq", "mcq", "Understand", "medium", 1, A_L41_44,
    options=[
        {"option_id": "ক", "text": "একধারে সবুজ মাঠ ঘাট, অন্যধারে বালুর চরে ধু ধু রোদ",
         "is_correct": True},
        {"option_id": "খ", "text": "দুই ধারেই সবুজ মাঠ", "is_correct": False,
         "why_wrong": "কবিতা দুই ধারকে আলাদা করে দেখিয়েছে — এক ধারে সবুজ, আর এক ধারে বালুর চর।"},
        {"option_id": "গ", "text": "দুই ধারেই বালুর চর", "is_correct": False,
         "why_wrong": "সবুজ বরনের ধারটির কথা কবিতায় স্পষ্ট আছে।"},
        {"option_id": "ঘ", "text": "একধারে ঘর, অন্যধারে হাট", "is_correct": False,
         "why_wrong": "ঘর বা হাটের কোনো কথা এই স্তবকে নেই।"}])

add("S05", "মূল কাঠামো", POEM,
    "'রাত্তিরে থম থম!' — চরণটি নদীতীরের রাত সম্পর্কে কী বোঝায়?",
    "mcq", "mcq", "Understand", "medium", 1, A_L45_48,
    options=[
        {"option_id": "ক", "text": "রাতে চারদিক নিস্তব্ধ ও গম্ভীর হয়ে যায়", "is_correct": True},
        {"option_id": "খ", "text": "রাতে অনেক মানুষের ভিড় হয়", "is_correct": False,
         "why_wrong": "দিনের বেলায় যাওয়া-আসার কথা আছে; রাত্তিরের বর্ণনা তার উল্টো।"},
        {"option_id": "গ", "text": "রাতে দুই ধারের সবুজ বরন আরও গাঢ় হয়", "is_correct": False,
         "why_wrong": "সবুজ বরনের কথা মাঠে ঘাটের বর্ণনায় আছে, রাতের প্রসঙ্গে নয়।"},
        {"option_id": "ঘ", "text": "রাতে বৃষ্টি নামে", "is_correct": False,
         "why_wrong": "বৃষ্টির কোনো কথা কবিতায় নেই।"}])

add("S05", "মূল কাঠামো", POEM,
    "'গাঁয়ের লোকে চিনবে আমার কেবল একটুখানি।' — কবি এখানে নদীর কোন দিকটি বোঝাচ্ছেন?",
    "mcq", "mcq", "Understand", "medium", 1, A_L37_40,
    options=[
        {"option_id": "ক", "text": "নদীর বেশির ভাগটাই মানুষের চেনার বাইরে থেকে যায়",
         "is_correct": True},
        {"option_id": "খ", "text": "গাঁয়ের লোক নদীকে একদমই চেনে না", "is_correct": False,
         "why_wrong": "'কেবল একটুখানি' কথাটি বলছে চেনে, তবে সামান্য।"},
        {"option_id": "গ", "text": "নদী গাঁয়ের লোকের কাছ থেকে দূরে সরে যায়", "is_correct": False,
         "why_wrong": "সরে যাওয়ার কথা নয়, চেনা-না-চেনার কথা।"},
        {"option_id": "ঘ", "text": "নদী কেবল দূরের মানুষকেই চেনে", "is_correct": False,
         "why_wrong": "দূরের মানুষদের নাম-গ্রাম নদী জানে না বলে কবিতায় আছে।"}])


# =====================================================================================
# S06 · বিপরীত শব্দ · alternative, C5 SELECTED = বিপরীত শব্দ · marks 1 · Remember, easy
# FIVE ITEMS, AND THE CHOICE IS DISCIPLINED: for each pair the poem prints BOTH members, so the
# antonym is supportable in the sense THIS chapter uses the word — the review prompt's own S06
# test. Words used adverbially or idiomatically (ধু ধু, থম থম, ছম ছম, চুপচাপ) are deliberately
# left out: they have no antonym in the sense the poem uses them.
# Teacher-supplied key (CD-136(b)), declared per item; the answers are general Bengali.
# =====================================================================================
S06 = [
    ("অন্ধকার", ["আলো"], A_L5_8),
    ("দিনের", ["রাতের"], A_L11_12),
    # FIX 5 (review finding 5) — "আপন" WAS ACCEPTED HERE AND IS NOT AN ANTONYM OF দূর in any
    # sense; its antonym is পর. The draft had reached for the poem's "আপন গাঁয়ের ঘাটে", which is a
    # different opposition (one's own vs another's, not far vs near), and a student writing it
    # scored full marks for a wrong answer. Only "কাছের" is kept.
    ("দূরের", ["কাছের"], A_L21_24),
    ("ডাঙা", ["জল"], A_L45_48),
    ("উপর", ["নিচ"], A_L25_26),
]
for w, acc, anc in S06:
    add("S06", "বিপরীত শব্দ", WORDREL,
        f"পাঠে ব্যবহৃত '{w}' শব্দের বিপরীত শব্দ লেখো।",
        "short_answer", "short", "Remember", "easy", 1, anc, **sa(acc, TEACHER_KEY_OPEN))


# =====================================================================================
# S07 · সংক্ষিপ্ত উত্তর · simple · marks 2
# EIGHT ITEMS · 5 Understand + 3 Analyze. The first four are অনুশীলনী ৩'s own ক · খ · গ · ঘ,
# asked in the book's words. অনুশীলনী ৩(ঙ) is a বর্ণনা দাও prompt and goes to S08, where its
# marks and its answer length belong — asking it twice at two lengths would be the near-duplicate
# §4 bars. The remaining four read parts of the poem the exercise does not reach.
# =====================================================================================
S07 = [
    ("কবি কী হতে চান? কেন হতে চান?",
     ["কবি ইচ্ছামতী নদী হতে চান। কারণ তিনি চান যখন যেমন মনে করেন তেমন হতে — নদী হলে তিনি "
      "দুই পারের সঙ্গে মনের কথা বলতে পারবেন এবং ঘুরে ঘুরে দূরের মাঠে মাঠে যেতে পারবেন।"],
     "Understand", "easy", A_EX3A),
    ("ইচ্ছামতী নদীর কোন দিকে সূর্য ওঠে?",
     ["দখিন ধারে — কবিতায় আছে 'রইবে আমার দখিন ধারে সূর্য ওঠার পার'।"],
     "Understand", "easy", A_EX3B),
    ("ইচ্ছামতী নদী কোন পারের মানুষের সাথে কথা বলবে?",
     ["দুই পারের মানুষের সঙ্গেই — আধেক কথা দিনের বেলায় আর আধেক কথা রাতে।"],
     "Understand", "easy", A_EX3C),
    ("ইচ্ছামতী নদীর দুই ধারের পার্থক্য কী?",
     ["এক ধারে মাঠে ঘাটে কেবল সবুজ বরন, আর এক ধারে বালুর চরে রৌদ্র ধু ধু করে। "
      "আবার দখিন ধারে সূর্য ওঠে আর বাঁয়ের ধারে সন্ধেবেলায় অন্ধকার নামে।"],
     "Understand", "medium", A_EX3D),
    ("গাঁয়ের কোন মানুষদের নদী চেনে বলে কবি লিখেছেন?",
     ["যারা জলে নাইতে আসে, আর যারা গোরু মহিষ নিয়ে সাঁতরে ওপার যায় — এই মানুষদের নদী চেনে।"],
     "Understand", "medium", A_L17_20),
    ("দূরের মানুষ সম্পর্কে নদী কী জানে না?",
     ["তাদের নাম জানে না, গ্রামও জানে না; কেবল দেখে তাদের বেশ নতুনতরো।"],
     "Analyze", "medium", A_L21_24),
    ("'গাঁয়ের লোকে চিনবে আমার কেবল একটুখানি।' — কবি এ কথায় নদী সম্পর্কে কী বোঝাতে চেয়েছেন?",
     ["নদীকে মানুষ যতটুকু দেখে ততটুকুই চেনে; বাকিটা কোথায় হারিয়ে যায় তা নদী নিজেও জানে না। "
      "অর্থাৎ নদীর বেশির ভাগটাই মানুষের চেনার বাইরে।"],
     "Analyze", "hard", A_L37_40),
    ("কবিতার নাম 'ইচ্ছামতী' রাখা হয়েছে কেন — কবিতার প্রথম স্তবক থেকে বুঝিয়ে লেখো।",
     ["প্রথম স্তবকে কবি বলছেন, যখন যেমন মনে করেন তাই হতে পেলে তিনি একখানি নদী হতেন। "
      "সেই ইচ্ছা থেকেই নদীর নাম 'ইচ্ছামতী' — যে নদী মনের ইচ্ছামতো বয়ে যায়।"],
     "Analyze", "hard", A_L1_4),
]
for text, acc, bl, df, anc in S07:
    add("S07", "মূল কাঠামো", POEM, text, "short_answer", "short", bl, df, 2, anc, **sa(acc))


# =====================================================================================
# S08 · বিস্তৃত উত্তর · simple · marks 5 · descriptive, rubric
# FIVE ITEMS, each with a DISTINCT content rubric — no two share one. Five is where the section
# stops: the poem has six stanzas, two of which are ⚠-barred in part (lines 15, 27) and one
# entirely (33–36), and each item below takes a different span. A sixth would re-describe a span
# already taken.
# BAN-S08-STRAND (the C2→C5 ইসলামি ধারা, whose C5 leg is পাঠ ২১ বিদায় হজ) is a PAPER-level
# obligation on one বিস্তৃত question and is not a bar on this chapter serving S08.
# =====================================================================================
add("S08", "মূল কাঠামো", POEM, "ইচ্ছামতী নদীতীরের দিন ও রাতের বর্ণনা দাও।",
    "descriptive", "structured", "Analyze", "hard", 5, A_EX3E,
    **rubric("দিন ও রাত — দুটোই কবিতার নিজের চরণ থেকে আলাদা করে এসেছে কি না, এবং বর্ণনায় "
             "কোনো ভয়-জাগানো বা অলৌকিক ব্যাখ্যা যোগ করা হয়নি কি না",
             "দিনের বেলায় যাওয়া-আসা, দুই ধারের সবুজ ও বালুর চরের রোদ, আর রাত্তিরে থম থম "
             "নিস্তব্ধতা ও ডাঙার পানে চেয়ে গা ছম ছম করা — দুই সময়ের বর্ণনা নিজের ভাষায় "
             "গুছিয়ে লেখা হয়েছে।",
             "কেবল দিন বা কেবল রাতের কথা এসেছে; অথবা কবিতার চরণ হুবহু তুলে দেওয়া হয়েছে।"))

add("S08", "মূল কাঠামো", POEM,
    "নদী হয়ে কবি কী কী করতে চান — কবিতা অনুসরণ করে লেখো।",
    "descriptive", "structured", "Understand", "medium", 5, A_L9_12,
    **rubric("কবির চাওয়াগুলো কবিতার নিজের চরণ থেকে নেওয়া হয়েছে কি না, এবং ঘরবাড়ি বা "
             "পড়াশোনা ছেড়ে যাওয়াকে কবিতার শিক্ষা বলে দেখানো হয়নি কি না",
             "দুই পারের সঙ্গে মনের কথা বলা, আপন গাঁয়ের ঘাটে ঘুরে বেড়ানো, দূরের মাঠে মাঠে "
             "যাওয়া, গাঁয়ের মানুষকে চেনা — অন্তত তিনটি চাওয়া কবিতা থেকে এসেছে এবং "
             "ইতিবাচক ভাষায় লেখা হয়েছে।",
             "একটি বা দুটি চাওয়া এসেছে; অথবা কবিতায় নেই এমন ইচ্ছা যোগ করা হয়েছে।"))

add("S08", "মূল কাঠামো", POEM,
    "ইচ্ছামতী নদীর দুই ধারের পার্থক্য বিস্তারিতভাবে লেখো।",
    "descriptive", "structured", "Analyze", "hard", 5, A_L41_44,
    **rubric("দুই ধারের তুলনা কবিতার দেওয়া তথ্য দিয়েই করা হয়েছে কি না — কোনো ধারকে ভালো "
             "বা মন্দ বলে বিচার করা হয়নি কি না",
             "সূর্য ওঠার দখিন ধার ও সন্ধের অন্ধকার নামা বাঁয়ের ধার, আর সবুজ বরনের মাঠ-ঘাট "
             "ও রৌদ্রে ধু ধু বালুর চর — দুই জোড়া বৈসাদৃশ্যই এসেছে এবং তুলনা হিসেবে সাজানো "
             "হয়েছে।",
             "কেবল এক জোড়া পার্থক্য এসেছে, অথবা দুই ধার আলাদা করে চিহ্নিত হয়নি।"))

add("S08", "মূল কাঠামো", POEM,
    "কবিতায় গাঁয়ের মানুষ ও দূরের মানুষের যে বর্ণনা এসেছে, তা নিজের ভাষায় লেখো।",
    "descriptive", "structured", "Understand", "medium", 5, A_L17_20,
    **rubric("দুই দলের মানুষকে কবিতার তথ্য দিয়েই আলাদা করা হয়েছে কি না, এবং অচেনা "
             "মানুষদের নিয়ে কোনো নেতিবাচক বা বিদ্রুপের কথা লেখা হয়নি কি না",
             "গাঁয়ের চেনা মানুষ — যারা জলে নাইতে আসে, যারা গোরু মহিষ নিয়ে ওপার যায় — আর "
             "দূরের অচেনা মানুষ, যাদের বেশ নতুনতরো এবং যাদের নাম-গ্রাম নদী জানে না; দুই "
             "দলই আলাদা করে এসেছে, শ্রদ্ধার ভাষায়।",
             "কেবল এক দলের কথা এসেছে; অথবা অচেনা মানুষদের নিয়ে বিদ্রুপ বা মনগড়া কথা "
             "যোগ করা হয়েছে।"))

add("S08", "মূল কাঠামো", POEM,
    "তুমি যদি একটি নদী হতে, কী কী করতে চাইতে? কবিতার ভাব অনুসরণ করে নিজের ভাষায় লেখো।",
    "descriptive", "structured", "Create", "hard", 5, A_L13_14,
    **rubric("লেখাটি কবিতার ভাব ধরে রেখেছে কি না — উপকার ও মিলনের ইচ্ছা, ঘর বা দায়িত্ব "
             "ছেড়ে পালানোর ইচ্ছা নয়; এবং কোনো অলৌকিক শক্তির দাবি করা হয়নি কি না",
             "নিজের অন্তত তিনটি ইচ্ছা লেখা হয়েছে, প্রতিটির সঙ্গে কবিতার কোনো ভাবের যোগ "
             "আছে — মানুষের কাছে থাকা, দূরে যাওয়া, দুই পারকে যুক্ত করা — এবং ভাষা "
             "শ্রেণির উপযোগী ও ইতিবাচক।",
             "ইচ্ছাগুলো লেখা হয়েছে কিন্তু কবিতার ভাবের সঙ্গে যোগ নেই, অথবা লেখাটি "
             "কবিতার চরণ তুলে দেওয়া হয়েছে।"))


# =====================================================================================
# S09 · মূলভাব · simple · marks 5 · descriptive · Analyze
# ONE ITEM. The slot's task is the whole poem's ভাব and a second stem for the same কবিতা would sit
# far above PLAN's near-duplicate bar. Admitted on the extraction's own sentence naming পাঠ ১৮ as
# an S09 source.
# THE ভাব IS READ OFF THE POEM'S OWN CHARAN AND NOTHING ELSE. This chapter carries NO
# "ভাব (অধ্যক্ষের অনুমোদিত পাঠ)" block — পাঠ ১৩ has one and this পাঠ does not (CD-167(c) added it
# at পাঠ ১৩ only) — so the rubric claims nothing the section does not print.
# =====================================================================================
add("S09", "মূল কাঠামো", POEM, "'ইচ্ছামতী' কবিতার মূলভাব নিজের ভাষায় লেখো।",
    "descriptive", "structured", "Analyze", "hard", 5, A_S01,
    **rubric("পুরো কবিতা থেকে মূল ভাব বের করে আনা — মনের ইচ্ছামতো নদী হয়ে দুই পারের মানুষের "
             "কাছে থাকা ও তাদের সঙ্গে কথা বলার আকাঙ্ক্ষা; এবং সেই ইচ্ছাকে ঘর, পড়াশোনা বা "
             "বড়োদের কথার বিরোধী করে না দেখানো",
             "মূলভাব নিজের ভাষায় লেখা হয়েছে, কবিতার চরণ হুবহু না তুলে; নদী হওয়ার ইচ্ছা, "
             "দুই পারের সঙ্গে কথা বলা এবং চেনা-অচেনা মানুষের মধ্য দিয়ে বয়ে চলা — এই দিকগুলো "
             "এসেছে এবং ভাষা ইতিবাচক।",
             "কবিতার চরণ তুলে দেওয়া হয়েছে, বা কেবল একটি দিক এসেছে; অথবা ঘর ছেড়ে চলে "
             "যাওয়াই কবিতার শিক্ষা — এমন ভুল ভাব এসেছে।"))


# =====================================================================================
# S10 · পদ নির্ণয় · alternative, C5 SELECTED = পদ নির্ণয় · marks 1 · Understand, easy
# EIGHT ITEMS. অনুশীলনী ৪ ("পাঠ থেকে নাম-শব্দ খুঁজে লেখা") is this slot's anchor at this chapter;
# the slot's task is পদ নির্ণয় generally, so ক্রিয়া, বিশেষণ and সর্বনাম are covered too, each
# asked INSIDE the line it appears in — the review prompt's own S10 test is whether the answer is
# right for the word AS USED. Eight distinct lines carry eight distinct target words; a ninth
# would take a second word out of a line already used.
# ক্রিয়ার কাল and ভাষারীতি পরিবর্তন are the other two members of this slot's admitted_set and C5
# has NOT selected them — an item doing either is off-choice (CD-138(b)) and none is authored.
# That ruling lives HERE and in header["s10_selection_ruling"] and NOT in any model_note (FIX 6).
# Teacher-supplied key (CD-136(b)), declared per item, in the CLOSED form (FIX 7).
#
# FIX 4 (review finding 4) — "নামপদ" WAS ACCEPTED on the four বিশেষ্য items and is now REJECTED.
# নামপদ is the SUPER-CLASS over বিশেষ্য · বিশেষণ · সর্বনাম, not the পদ itself: a student who
# writes it has not identified the পদ, and the same word would also cover Q59's keyed সর্বনাম, so
# accepting it makes two different items share one answer. In its place goes "নাম-শব্দ" — THE
# CHAPTER'S OWN TERM, the one this পাঠ's অনুশীলনী ৪ uses ("পাঠ থেকে নাম-শব্দ খুঁজে লেখা") and the
# one the source's advisory line ties to S10. It returned ZERO across the whole bank before this
# fix. This now matches exactly what the ক্রিয়া items (নামবে · চলে) already do with কাজ-শব্দ.
# =====================================================================================
S10 = [
    ("নদী", "'আমি তবে একখনি হই ইচ্ছামতী নদী।'", ["বিশেষ্য", "বিশেষ্য পদ", "নাম-শব্দ"], A_L1_4),
    ("সূর্য", "'রইবে আমার দখিন ধারে সূর্য ওঠার পার,'", ["বিশেষ্য", "বিশেষ্য পদ", "নাম-শব্দ"], A_L5_8),
    ("আমি", "'আমি কইব মনের কথা'", ["সর্বনাম", "সর্বনাম পদ"], A_L9_12),
    # NOT a second word out of "'আমি কইব মনের কথা'": two S10 stems quoting the SAME printed
    # line carry IDENTICAL token sets once punctuation is stripped, which is a 100% near-duplicate
    # at PLAN. The ক্রিয়া example is taken from a different printed line instead.
    ("নামবে", "'বাঁয়ের ধারে সন্ধেবেলায় নামবে অন্ধকার।'", ["ক্রিয়া", "ক্রিয়া পদ", "কাজ-শব্দ"],
     A_L5_8),
    ("মানুষ", "'গাঁয়ের মানুষ চিনি, যারা'", ["বিশেষ্য", "বিশেষ্য পদ", "নাম-শব্দ"], A_L17_20),
    ("চলে", "'সাঁতরে ওপার চলে।'", ["ক্রিয়া", "ক্রিয়া পদ", "কাজ-শব্দ"], A_L17_20),
    ("সবুজ", "'সবুজ বরন শুধু,'", ["বিশেষণ", "বিশেষণ পদ"], A_L41_44),
    ("ঘাট", "'আপন গাঁয়ের ঘাটে'", ["বিশেষ্য", "বিশেষ্য পদ", "নাম-শব্দ"], A_L13_14),
]
for w, line, acc, anc in S10:
    add("S10", "পদ নির্ণয়", PARTSP,
        f"{line} — এখানে '{w}' শব্দটি কোন পদ? নির্ণয় করো।",
        "short_answer", "short", "Understand", "easy", 1, anc, **sa(acc, PADA_KEY))


# =====================================================================================
# S11 · বিরামচিহ্ন বসানো · alternative, C5 SELECTED = বিরামচিহ্ন বসানো · marks 1 · Apply, medium
#
# ***THIS IS THE QB-CR-017 SLOT AND EVERY ITEM IN IT IS BUILT AGAINST THAT ROW'S UNFIXED DEFECT.***
# Thirteen S11 items across U13–U16 are each satisfied by placing ONE terminal mark. No gate saw
# one of them: every gate reads metadata and the defect lives in the prose. So:
#   (1) EVERY item below requires AT LEAST TWO marks, and none is a single terminal mark;
#   (2) EVERY mark required is inside C5's taught set (CD-165 as amended by CD-166) —
#       দাঁড়ি · কমা · প্রশ্নচিহ্ন · বিস্ময়চিহ্ন · উদ্ধরণ চিহ্ন;
#   (3) selfcheck() DIFFS each stimulus against its key, counts the inserted marks, and FAILS
#       the build on a count of one or on any mark outside the taught set. That is QB-CR-017's own
#       proposed gate, run here at authoring time.
#
# THE STIMULUS CHOICE WAS MADE FROM A CENSUS OF THE POEM'S PRINTED MARKS, BEFORE AUTHORING —
# QB-CR-017's own recorded lesson from পাঠ ১৫, whose poem prints ড্যাশ and সেমিকোলন in four lines
# and whose five S11 items are therefore unfixable. পাঠ ১৮ prints ড্যাশ in ONE line and সেমিকোলন
# in NONE. REJECTED as stimulus, with the reason:
#   lines 1–4    — one দাঁড়ি only (QB-CR-017's exact defect shape)
#   lines 9–12   — line 10 "দুই পারেরই সাথে" REQUIRES ড্যাশ, BARRED AT C5
#   lines 13–16  — line 15 is C-03-barred
#   lines 25–28  — line 27 is C-03-barred; and the span carries one mark
#   lines 29–32  — one দাঁড়ি only
#   lines 33–36  — the ⚠ block's third clause bars the span
# SIX SPANS SURVIVE and all six are used. The slot is exhausted at six, not stopped at a number.
# =====================================================================================
S11 = [
    # 2 marks — কমা (after পার) + দাঁড়ি (after অন্ধকার)
    ("রইবে আমার দখিন ধারে সূর্য ওঠার পার বাঁয়ের ধারে সন্ধেবেলায় নামবে অন্ধকার",
     "রইবে আমার দখিন ধারে সূর্য ওঠার পার, বাঁয়ের ধারে সন্ধেবেলায় নামবে অন্ধকার।",
     "দুটি চিহ্ন বসাতে হবে: 'পার'-এর পরে কমা, কারণ কথাটি এখানে শেষ হয়নি; আর 'অন্ধকার'-এর "
     "পরে দাঁড়ি, কারণ স্তবকের এই অংশ সেখানেই শেষ।", A_L5_8),
    # 3 marks — কমা + কমা + দাঁড়ি
    ("গাঁয়ের মানুষ চিনি যারা নাইতে আসে জলে গোরু মহিষ নিয়ে যারা সাঁতরে ওপার চলে",
     "গাঁয়ের মানুষ চিনি, যারা নাইতে আসে জলে, গোরু মহিষ নিয়ে যারা সাঁতরে ওপার চলে।",
     "তিনটি চিহ্ন: 'চিনি'-র পরে কমা, কারণ পরের অংশটি বলে দিচ্ছে কাদের কথা; 'জলে'-র পরে "
     "কমা, কারণ আরও একটি দল যোগ হচ্ছে; আর 'চলে'-র পরে দাঁড়ি, কারণ বাক্য শেষ।", A_L17_20),
    # 3 marks — কমা + কমা + দাঁড়ি
    ("দূরের মানুষ যারা তাদের নতুনতরো বেশ নাম জানি নে গ্রাম জানি নে অদ্ভুতের একশেষ",
     "দূরের মানুষ যারা তাদের নতুনতরো বেশ, নাম জানি নে, গ্রাম জানি নে অদ্ভুতের একশেষ।",
     "তিনটি চিহ্ন: 'বেশ'-এর পরে কমা, কারণ কথাটি চলতে থাকে; প্রথম 'নে'-র পরে কমা, কারণ "
     "পাশাপাশি দুটি কথা বলা হচ্ছে; আর শেষে দাঁড়ি।", A_L21_24),
    # 2 marks — দাঁড়ি (mid-span) + প্রশ্নচিহ্ন (at the end); two DIFFERENT marks
    ("গাঁয়ের লোকে চিনবে আমার কেবল একটুখানি বাকি কোথায় হারিয়ে যাবে আমিই সে কি জানি",
     "গাঁয়ের লোকে চিনবে আমার কেবল একটুখানি। বাকি কোথায় হারিয়ে যাবে আমিই সে কি জানি?",
     "দুটি চিহ্ন, দুই রকমের: 'একটুখানি'-র পরে দাঁড়ি, কারণ প্রথম বাক্যটি সেখানেই শেষ; আর "
     "শেষে প্রশ্নচিহ্ন, কারণ দ্বিতীয় অংশটি একটি প্রশ্ন।", A_L37_40),
    # 2 marks — কমা + দাঁড়ি
    ("একধারেতে মাঠে ঘাটে সবুজ বরন শুধু আর একধারে বালুর চরে রৌদ্র করে ধু ধু",
     "একধারেতে মাঠে ঘাটে সবুজ বরন শুধু, আর একধারে বালুর চরে রৌদ্র করে ধু ধু।",
     "দুটি চিহ্ন: 'শুধু'-র পরে কমা, কারণ এরপর দ্বিতীয় ধারের কথা আসছে; আর শেষে দাঁড়ি।",
     A_L41_44),
    # 3 marks — কমা + বিস্ময়চিহ্ন + দাঁড়ি; all three different
    ("দিনের বেলায় যাওয়া আসা রাত্তিরে থম থম ডাঙার পানে চেয়ে চেয়ে করবে গা ছম ছম",
     "দিনের বেলায় যাওয়া আসা, রাত্তিরে থম থম! ডাঙার পানে চেয়ে চেয়ে করবে গা ছম ছম।",
     "তিনটি চিহ্ন, তিন রকমের: 'আসা'-র পরে কমা; 'থম থম'-এর পরে বিস্ময়চিহ্ন, কারণ এখানে "
     "বিস্ময়ের ভাব; আর শেষে দাঁড়ি।", A_L45_48),
]
for bare, done, note, anc in S11:
    add("S11", "বিরামচিহ্ন বসানো", PUNCT,
        f"'{bare}' — অংশটিতে প্রয়োজনীয় বিরামচিহ্নগুলো বসিয়ে আবার লেখো।",
        "short_answer", "short", "Apply", "medium", 1, anc, **sa([done], note))


# =====================================================================================
# S12 · যুক্তবর্ণ ভেঙে শব্দ · COMPOSITE (যুক্তবর্ণ ভাঙা + শব্দ গঠন) · marks 1 · Apply, medium
# FOUR ITEMS ARE AUTHORED. The chapter carries NO যুক্তবর্ণ exercise at all (and অনুশীলনী ২ is
# absent from the extraction), so the stimulus words are the poem's own. RE-COUNTED AT SOURCE
# 2026-08-18: the poem's 48 printed lines print SEVEN distinct যুক্তবর্ণ —
#   চ্ছ (line 4, ইচ্ছামতী) · ন্ধ (lines 7 8, সন্ধেবেলায় অন্ধকার) · দ্ভ (24, অদ্ভুতের) ·
#   ত্ত (46, রাত্তিরে) · র্য (6, সূর্য) · গ্র (23, গ্রাম) · দ্র (44, রৌদ্র).
# The first four are authored. THE OTHER THREE ARE AN UNAUTHORED REMAINDER, NOT A CLOSED SET:
# whether র-ফলা / রেফ forms belong in a C5 S12 item is a curation question NOBODY HAS RULED,
# so they are left open for a later wave rather than declared out of scope here.
# সন্ধেবেলায় is not authored: it repeats ন্ধ and its stem would be a near-duplicate.
# Every stem NAMES the conjunct it means, so no item leaves a multi-conjunct word ambiguous (the
# review prompt's own S12 test). Every item does BOTH parts — half the task fails COVERAGE.
# Teacher-supplied key (CD-136(b)), declared per item.
# =====================================================================================
S12 = [
    ("ইচ্ছামতী", "চ্ছ", ["চ্ছ = চ + ছ; নতুন শব্দ — কচ্ছপ", "চ্ছ = চ + ছ; গচ্ছিত",
                         "চ্ছ — চ ও ছ; উচ্ছল"], A_L1_4),
    ("অন্ধকার", "ন্ধ", ["ন্ধ = ন + ধ; নতুন শব্দ — বন্ধু", "ন্ধ = ন + ধ; গন্ধ",
                        "ন্ধ — ন ও ধ; অন্ধ"], A_L5_8),
    ("অদ্ভুতের", "দ্ভ", ["দ্ভ = দ + ভ; নতুন শব্দ — উদ্ভিদ", "দ্ভ = দ + ভ; উদ্ভট",
                         "দ্ভ — দ ও ভ; উদ্ভব"], A_L21_24),
    ("রাত্তিরে", "ত্ত", ["ত্ত = ত + ত; নতুন শব্দ — উত্তর", "ত্ত = ত + ত; উত্তম",
                         "ত্ত — ত ও ত; পত্তন"], A_L45_48),
]
for w, jk, acc, anc in S12:
    add("S12", ["যুক্তবর্ণ ভাঙা", "শব্দ গঠন"], JUKTO,
        f"পাঠের '{w}' শব্দে থাকা '{jk}' যুক্তবর্ণটি ভেঙে দেখাও এবং ওই যুক্তবর্ণ দিয়ে একটি "
        f"নতুন শব্দ গঠন করো।",
        "short_answer", "short", "Apply", "medium", 1, anc, **sa(acc, JUKTO_KEY))


# =====================================================================================
# S13 · এক কথায় প্রকাশ · simple · marks 1 · Remember, easy
# FIVE ITEMS, all read off অর্থ জেনে নিই THE OTHER WAY — the phrase is the chapter's own gloss and
# the answer is the chapter's own word, so the key is IN the chapter and NO CD-136 teacher-key
# note is owed (contrast S06, S10 and S12, whose answers are general Bengali).
# Three of the eight glosses are left out and the reason is the review prompt's own S13 test:
# 'ঘাটের সিঁড়ি' → ঘাটের ধাপ is not ONE word; 'ডান দিকে' → দখিন ধারে is not one word; 'গোসল করতে'
# → নাইতে is a verb form, not the এক কথায় প্রকাশ শব্দ this slot asks for.
# =====================================================================================
S13 = [
    ("অর্ধেক অংশ", ["আধেক"]),
    # Reviewer quality note (uncounted), FIXED: the phrase used to read "নদীর পাশের তীর বা শুকনো
    # জায়গা", and "বা" made either half sufficient — so the chapter's own "পার" (সূর্য ওঠার পার ·
    # সাঁতরে ওপার চলে) satisfied "নদীর পাশের তীর" and was marked wrong. The তীর half is dropped;
    # the remaining half is the chapter's own gloss and only ডাঙা answers it.
    ("নদীর পাশের শুকনো জায়গা", ["ডাঙা"]),
    ("রাতের বেলা", ["রাত্তির"]),
    ("দেখতে অন্যরকম যা", ["নতুনতরো"]),
    ("বর্ণ বা রং", ["বরন"]),
]
for phrase, acc in S13:
    add("S13", "মূল কাঠামো", VOCAB,
        f"'{phrase}' — পাঠের শব্দ দিয়ে এক কথায় প্রকাশ করো।",
        "short_answer", "short", "Remember", "easy", 1, A_GLOSS, **sa(acc))


# =====================================================================================
def build():
    questions, slot_index, task_index, source_index = [], {}, {}, {}
    for i, it in enumerate(ITEMS, start=1):
        qid = f"QP-BAN-C5-U18-Q{i:02d}"
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

    # Pools — QB-D-001: every item in exactly one, no overlap. CT takes the short recall a 25-mark
    # class test can actually carry; AS takes the mixed band QB-D-004 wants (roughly half at or
    # above Apply); HW takes the rest.
    # CT first: the short recall a 25-mark class test can actually carry — S02's eight শব্দার্থ
    # and four শূন্যস্থান, all Remember/easy.
    ct = [q for q in qids if slot_index[q] == "S02"]
    ct += [q for q in qids if slot_index[q] == "S04"][:4]
    rest = [q for q in qids if q not in set(ct)]
    # AS is built to QB-D-004's SHAPE — roughly half at or above HW level — rather than by slot
    # membership. The first draft assigned AS by slot and landed at 93% above-level, which is the
    # mix QB-D-004 exists to prevent; measured by selfcheck() and corrected here.
    above = [q for q in rest
             if by_qid[q]["bloom_level"] in ("Apply", "Analyze", "Evaluate", "Create")
             or by_qid[q]["difficulty"] == "hard"]
    base = [q for q in rest if q not in set(above)]
    half = min(len(above), len(base)) // 2
    as_ = above[:half] + base[:half]
    hw = above[half:] + base[half:]

    return {
        "schema_version": "1.0",
        "policy_shape": "qp6",
        "bank_id": "QB-BAN-C5-U18",
        "wave": 1,
        "subject": "BAN",
        "class": 5,
        "chapter": CHAPTER,
        "extraction_path": EXTRACTION,
        "source_extraction": EXTRACTION,
        "curation": (
            "FLEXIBLE · এই পাঠের ⚠ ব্লকের প্রতিটি ধারা মানা হয়েছে। (১) C-03 — কবিতার ছাপা "
            "১৫ ও ২৭ নং লাইন দুটি থেকে কোনো প্রশ্ন করা হয়নি; কোনো stem, বিকল্প, why_wrong, "
            "উত্তরকুঞ্জি, model_note, rubric সারি বা S11 উদ্দীপক এই দুই চরণ ছোঁয়নি। কবিতার "
            "পূর্ণ পাঠ পড়ানো হবে, প্রশ্নে চরণ দুটি তোলা হয়নি। (২) S01-এর জন্য প্রথম "
            "স্তবকই নেওয়া হয়েছে — সেখানে গান বা নাচের কোনো উল্লেখ নেই (CD-149 অনুযায়ী ছাপা "
            "আট লাইন)। (৩) ছাপা ৩৩–৩৬ নং লাইন সম্পূর্ণ অব্যবহৃত — উৎসের ⚠ ব্লকের তৃতীয় "
            "ধারা; কোনো anchor সেখানে পৌঁছায়নি। (৪) কবির নাম কেবল তথ্য হিসেবে — কোথাও কোনো "
            "সম্মানের বিশেষণ নেই (E-AUTHOR-ENDORSE)। C-05 — কোনো ব্যক্তির ছবি নেই ও চাওয়া "
            "হয়নি। C-18 — কোনো জাতীয়তাবাদী আচার বা শ্রদ্ধা নিবেদনের প্রসঙ্গ নেই। কোনো "
            "কাল্পনিক ব্যক্তিনাম ব্যবহৃত হয়নি; একমাত্র ব্যক্তিনাম রবীন্দ্রনাথ ঠাকুর, যা "
            "পাঠের নিজের তথ্য।"),
        "header": {
            "target": len(questions),
            "reason": (
                "এই সংখ্যাটি কোনো লক্ষ্য নয় — CD-171(a) অনুযায়ী পুল-স্তরে কোনো ন্যূনতম, "
                "সর্বোচ্চ, Bloom-মেঝে বা প্রতি-স্লট দাবি আর নেই। প্রতিটি স্বীকৃত স্লটে "
                "ততগুলো আইটেম লেখা হয়েছে যতগুলো এই পাঠের বিষয়বস্তু বহন করে, তারপর থামা "
                "হয়েছে; থামার কারণ প্রতিটি স্লটের নিজের মন্তব্যে লেখা আছে "
                "(author_U18_wave1.py)। সীমা §4-এর near-duplicate নিষেধ: S02 আটটিতে থেমেছে "
                "কারণ অর্থ জেনে নিই-তে ঠিক আটটি শব্দ; S11 ছয়টিতে থেমেছে কারণ কবিতার ৪৮টি "
                "ছাপা লাইনে ঠিক ছয়টি স্প্যান আছে যেগুলো একাধিক চিহ্ন দাবি করে এবং যার "
                "কোনোটিই ড্যাশ চায় না; S12-তে চারটি আইটেম লেখা হয়েছে, আর কবিতার ৪৮টি ছাপা "
                "লাইনে আলাদা যুক্তবর্ণ ছাপা হয়েছে সাতটি — চ্ছ (ছাপা লাইন ৪) · ন্ধ (৭, ৮) · "
                "দ্ভ (২৪) · ত্ত (৪৬) · র্য (৬) · গ্র (২৩) · দ্র (৪৪)। এর প্রথম চারটি নিয়ে "
                "আইটেম লেখা হয়েছে; বাকি তিনটি — র-ফলা ও রেফ যুক্ত রূপ — নিয়ে কোনো আইটেম লেখা "
                "হয়নি, আর এই তিনটি C5-এর S12-তে চলে কি না তা এখনো কেউ নির্ধারণ করেনি। "
                "সেগুলো তাই অলিখিত অবশিষ্ট হিসেবে খোলা রইল, পরিসরের বাইরে বলে বাদ দেওয়া "
                "হয়নি; S01 ও S09 একটি করে, কারণ একই কবিতার দ্বিতীয় মুখস্থ "
                "বা দ্বিতীয় মূলভাব প্রশ্ন একই প্রশ্ন। কোনো আইটেম সংখ্যা ছোঁয়ার জন্য লেখা "
                "হয়নি, কারণ কোনো সংখ্যা নেই (CD-171(a), CD-151(b))।"),
            "topics": ["TOP-BAN-C5-05", "TOP-BAN-C5-01", "TOP-BAN-C5-02", "TOP-BAN-C5-13"],
            "spine_slots": [f"S{i:02d}" for i in range(1, 16)],
            "admissible_slots": sorted(by_slot),
            "slot_exclusions": {},
            "admissibility_declaration": (
                "CD-138(e), পাঠ ১৮-এর নিজস্ব ঘোষণা, canon/marklogic/C5_Bangla_Source_13-23.md-এর "
                "পাঠ ১৮ অংশ (লাইন ৩২২–৪১১) থেকে উৎসেই লেখা — পাঠ ১২ পড়া হয়নি (CD-127(b) "
                "consumption exclusion)। পূর্ণ ঘোষণা: workstreams/question-banks/_wip/"
                "U18_ADMISSIBILITY_2026-08-18.md। রেজিস্টারে BAN C5-এর পনেরোটি স্লট। এর মধ্যে "
                "দুটি — S14 আবেদনপত্র ও S15 রচনা — CD-147 অনুযায়ী প্রতিটি পাঠের জন্যই "
                "কাগজ-স্তরের, শ্রেণিগতভাবে; এই ঘোষণা তাদের নিয়ে কিছুই বলে না এবং বলার দায়ও "
                "নেই, যা CD-147(c) অনুযায়ী সঠিক, অসম্পূর্ণ নয়। CD-147(g) এই পাঠের নিজের ধারা "
                "এবং তা মানা হয়েছে: অনুশীলনী ৫-এ শিরোনামসহ রচনার নির্দেশ আছে ('আমি যা হতে "
                "চাই') এবং উৎসের 'কোন প্রশ্নে কাজে লাগবে' লাইনটিও এই পাঠের জন্য S15 নাম ধরে "
                "লেখে; ২০২৬-০৮-১৬-এর একটি probe এটিকে S15 স্বীকৃতির প্রমাণ হিসেবে পড়েছিল এবং "
                "অধ্যক্ষ সেই সিদ্ধান্ত সরাসরি প্রত্যাখ্যান করেছেন — 'পাঠ ১৮ does not admit S15 "
                "either. The anchor exists; the pipeline is still the paper's.' anchor-টি সত্য ও "
                "প্রত্যাহৃত নয়, কিন্তু সেটি প্রশ্নটির নিষ্পত্তি করে না। কোনো S15 আইটেম লেখা "
                "হয়নি এবং S15 স্বীকৃত নয়। বাকি তেরোটি স্লটের প্রতিটিই স্বীকৃত, বিষয়বস্তুর "
                "ভিত্তিতে, তাই slot_exclusions ফাঁকা। S01 ও S09 স্বীকৃত উৎসের নিজের বাক্যে: "
                "'কবিতা চারটি: পাঠ ১৩, ১৫, ১৮, ২০ — এগুলোই S01 (কবিতা মুখস্থ) ও S09 (মূলভাব) "
                "প্রশ্নের উৎস।' পাঠ ১৮ সেই চারটির একটি; একই বাক্য পাঠ ১৪ ও পাঠ ১৬ থেকে দুটি "
                "স্লট কেড়ে নিয়েছিল, তাই এটি উদ্ধৃত হয়েছে, অনুমান করা হয়নি। এই পাঠের নিজস্ব "
                "'কোন প্রশ্নে কাজে লাগবে' লাইন ছয়টি স্লটের নাম লেখে (S01 · S09 · S03 · S10 · "
                "S07 · S15); সেটি উপদেশমূলক, কোনো সীমা নয় (CD-122(b), CD-134(b)), আর 'লাইনটি "
                "নাম লেখেনি' — এই কারণে কোনো স্লট বাদ দেওয়া CD-134(c) নিষিদ্ধ করে। তাই S02 · "
                "S04 · S05 · S06 · S08 · S11 · S12 · S13 স্বীকৃত হয়েছে বিষয়বস্তুর ভিত্তিতে। "
                "CD-142(b) অনুযায়ী পরিকল্পনার কাউন্টারসাইন এখন PLAN গেট, মানুষের সই নয়।"),
            "slot_counts": slot_counts,
            "s01_span_ruling": (
                "CD-149(a) — BAN-S01-এর একক ছাপা লাইন; 'প্রথম ৮ লাইন' মানে বই যেভাবে সাজিয়েছে "
                "সেই আটটি লাইন, আর পঙ্‌ক্তি-পাঠ প্রত্যাখ্যাত। CD-149(b) নিজেই লিখে রেখেছে যে "
                "পাঠ ১৮-এর delimiter — 'নামবে অন্ধকার।' — ছাপা লাইনের হিসেবে ঠিক ৮ নম্বরে "
                "পড়ে, আর CD-149(e) বলছে এই পাঠের delimiter authoring-এর সময় কোনো সংশোধন চায় "
                "না। এই সেশনে উৎসে আবার গোনা হয়েছে: কবিতাটি ৪৮টি ছাপা লাইনে ছয় স্তবক, প্রথম "
                "স্তবক = ছাপা লাইন ১–৮, যা শেষ হয়েছে ওই endpoint-এ। Q01 ঠিক সেই স্প্যানে লেখা "
                "এবং কোনো গণনা student-facing কোনো স্ট্রিং-এ পুনরুক্ত হয়নি। Q01-এর নম্বর ভাগ "
                "SLOT_REGISTER BAN-S01-এর ঘোষিত অংশ অনুযায়ী: কবির নাম ১ + কবিতার নাম ১ + প্রথম ৮ "
                "লাইন ৮ = ১০। কবির নাম কেবল তথ্য হিসেবে চাওয়া হয়েছে, কোনো সম্মানসূচক বিশেষণ "
                "নয় — E-AUTHOR-ENDORSE (SLOT_REGISTER BAN-S01, scope 'C4 এবং C5-এ কবিতার "
                "প্রশ্নে')। নম্বর ভাগ ও সম্মানসূচক বিশেষণের নিষেধ — দুটোই marker-এর কাজের "
                "নির্দেশ, তাই Q01-এর model_note-এ আছে; কিন্তু CD-149, SLOT_REGISTER ও "
                "E-AUTHOR-ENDORSE কোডগুলো সেখান থেকে সরিয়ে এখানে আনা হয়েছে (২০২৬-০৮-১৮ "
                "পর্যালোচনার ৬ নং পর্যবেক্ষণ)।"),
            "s10_selection_ruling": (
                "BAN-S10-এর admitted_set-এ তিনটি কাজ: পদ নির্ণয় · ক্রিয়ার কাল · ভাষারীতি "
                "পরিবর্তন। পঞ্চম শ্রেণি নির্বাচন করেছে পদ নির্ণয়; বাকি দুটি এই শ্রেণিতে "
                "off-choice এবং সেগুলো নিয়ে কোনো আইটেম লেখা হয়নি (CD-138(b))। এটি authoring "
                "লেনের সিদ্ধান্ত — marker-এর জন্য এর কোনো কাজ নেই, তাই ২০২৬-০৮-১৮ পর্যালোচনার "
                "৬ নং পর্যবেক্ষণ অনুযায়ী Q57–Q64-এর model_note থেকে পুরো ধারাটি সরিয়ে এখানে "
                "রাখা হলো। একই সঙ্গে ওই আটটি আইটেমের উত্তরকুঞ্জি-নোট এখন CLOSED রূপে — পদের "
                "কোনো 'কাছাকাছি অর্থ' নেই (৭ নং পর্যবেক্ষণ)। গৃহীত উত্তর থেকে 'নামপদ' বাদ "
                "দেওয়া হয়েছে (এটি বিশেষ্য · বিশেষণ · সর্বনাম-এর উপরের শ্রেণি, তাই Q59-এর "
                "সর্বনামকেও ঢেকে ফেলত) এবং পাঠের নিজের শব্দ 'নাম-শব্দ' যোগ করা হয়েছে — "
                "অনুশীলনী ৪-এর ভাষা, যেভাবে ক্রিয়ার আইটেমে 'কাজ-শব্দ' আগেই ছিল (৪ নং "
                "পর্যবেক্ষণ)।"),
            "s12_composite_ruling": (
                "BAN-S12 composite — যুক্তবর্ণ ভাঙা ও শব্দ গঠন, দুটি অংশই আবশ্যক; একটিমাত্র অংশ "
                "করলে অর্ধেক কাজ। দাবিটি marking instruction, তাই সেটি Q71–Q74-এর model_note-এ "
                "সাদা বাংলায় আছে; কেবল SLOT_REGISTER উদ্ধৃতিটি সেখান থেকে সরিয়ে এখানে আনা "
                "হয়েছে (৬ নং পর্যবেক্ষণ)। ওই নোট এখন half-open — ভাঙার অংশ নির্দিষ্ট, নতুন "
                "শব্দটি শিক্ষার্থীর নিজের; আগের একক 'কাছাকাছি অর্থের যেকোনো শুদ্ধ উত্তর "
                "গ্রহণযোগ্য' ধারাটি নোটের নিজের 'দুটি কাজই করতে হবে' দাবির বিরোধী ছিল (৭ নং "
                "পর্যবেক্ষণ)।"),
            "model_note_policy": (
                "২০২৬-০৮-১৮-এর factual/curation পর্যালোচনার ৬ ও ৭ নং পর্যবেক্ষণ প্রয়োগ করা "
                "হয়েছে। model_note marker-এর পড়ার জিনিস, তাই তাতে কেবল marking instruction "
                "থাকবে: CD-138(b), CD-149, SLOT_REGISTER ও E-AUTHOR-ENDORSE — এই কোডগুলো "
                "marker-facing কোনো স্ট্রিং-এ আর নেই, সেগুলো authoring script-এর মন্তব্যে ও এই "
                "header-এ আছে। CD-136 provenance টোকেনটি অপরিবর্তিত ও অবিকৃত রাখা হয়েছে, ঠিক "
                "যে সাদা রূপে চারটি pushed ব্যাংক এটি বহন করে — এটিই আইটেমের নিজস্ব "
                "উৎস-ঘোষণা (CD-136(b)) এবং gates.py-র P-037 পরীক্ষা এই টোকেনই পড়ে। প্রস্তাবিত "
                "'[[…]]' রূপটি ব্যবহার করা হয়নি, কারণ এই রিপোতে তা ছাঁটার কোনো ধাপ নেই। "
                "TEACHER_KEY এখন তিন রূপে: OPEN (S06 বিপরীত শব্দ — কাছাকাছি অর্থের শুদ্ধ উত্তর "
                "সত্যিই চলে), CLOSED (S10 পদ নির্ণয় — উত্তর নির্দিষ্ট), এবং S12-র half-open রূপ। "
                "S02, S03, S04, S07, S11, S13-তে এই ধারা আগেও ছিল না, এখনো নেই।"),
            "taught_set_and_QB_CR_017": (
                "CD-165, CD-166 অনুযায়ী C5-এর বিরামচিহ্নের taught set: দাঁড়ি · কমা · প্রশ্নচিহ্ন "
                "· বিস্ময়চিহ্ন · উদ্ধরণ চিহ্ন। ড্যাশ ও সেমিকোলন পঞ্চম শ্রেণিতে নিষিদ্ধ। S11-এর "
                "উদ্দীপক বাছার আগে কবিতার ছাপা চিহ্নগুলো লাইন ধরে গোনা হয়েছে: দাঁড়ি ১৪টি "
                "লাইনে (ছাপা ৪ ৮ ১২ ১৬ ২০ ২৪ ২৬ ২৮ ৩২ ৩৪ ৩৬ ৩৮ ৪৪ ৪৮), কমা ৯টি লাইনে (ছাপা "
                "৬ ১১ ১৭ ১৮ ২২ ২৩ ২৭ ৪২ ৪৫), প্রশ্নচিহ্ন একটিতে (ছাপা ৪০), বিস্ময়চিহ্ন একটিতে "
                "(ছাপা ৪৬), ড্যাশ কেবল ছাপা ১০ নং লাইনে, এবং সেমিকোলন কোথাও নেই। তাই ১০ নং লাইন "
                "S11-এর উদ্দীপক হিসেবে অব্যবহৃত। QB-CR-017 (OPEN) — U13–U16-এর তেরোটি S11 "
                "আইটেম এমনভাবে লেখা হয়েছিল যে প্রতিটি একটিমাত্র শেষ-চিহ্ন বসালেই মিটে যায়, আর "
                "কোনো গেট সেটি দেখেনি কারণ গেট metadata পড়ে আর ত্রুটিটি prose-এ থাকে। এখানকার "
                "ছয়টি S11 আইটেমের প্রতিটি অন্তত দুটি চিহ্ন দাবি করে (২ · ৩ · ৩ · ২ · ২ · ৩), "
                "কোনোটিই একটিমাত্র শেষ-চিহ্ন নয়, এবং প্রতিটি দাবি করা চিহ্ন taught set-এর "
                "ভেতরে। authoring script-এর selfcheck() উদ্দীপক ও উত্তরকুঞ্জি diff করে চিহ্ন "
                "গুনে build ব্যর্থ করে — QB-CR-017-এর নিজের প্রস্তাবিত গেট, এই ব্যাংকে "
                "authoring-সময়ে চালানো।"),
            "topic_tag_ruling": (
                "পাঠ ১৮ কবিতা, তাই পাঠ-বিষয়ক আইটেমগুলো TOP-BAN-C5-05 (কবিতা/মূলভাব, BAN-POEM) "
                "বহন করে — canon/topics/TOPIC_NUMBERS.md-এর পাঠ-ধরন ছক পাঠ ১৩ · ১৫ · ১৮ · ২০-কে "
                "নাম ধরে -05 দিয়েছে। topic_tag প্রতি-প্রশ্নের ক্ষেত্র, প্রতি-অধ্যায়ের নয়: "
                "শব্দার্থ, বিপরীত শব্দ, যুক্তবর্ণ, পদ নির্ণয় ও এক কথায় প্রকাশের আইটেম -01, "
                "বাক্য গঠন -02, বিরামচিহ্ন -13। ছয়টি বিরামচিহ্ন আইটেম প্রথম থেকেই -13 বহন "
                "করছে, -02 নয় — QB-CR-014-এর শিক্ষা। ref19_topic_id বিরামচিহ্নে BAN-SENTENCE-ই "
                "থাকছে: REF-19 v1.10-এ যতিচিহ্নের কোনো slug নেই (PENDING-P-008, FLAGGED), আর "
                "এখানে একটি বানিয়ে নেওয়া হতো QB-CR-008-এর ভুলটাই অন্য রেজিস্টারে করা। প্রতিটি "
                "সংখ্যা এই সেশনে TOPIC_NUMBERS.md-এ যাচাই করা হয়েছে; সেখানে সারি নেই এমন কোনো "
                "সংখ্যা ব্যবহার করা হয়নি (CD-044)।"),
            "content_facts": (
                "বিষয়বস্তুর তথ্য হিসেবে লেখা হলো: Evaluate এই পুলে ০ এবং Create ১। পাঠটি "
                "কবিতা, আর এর অনুশীলনীর কাজগুলো — জোড়া শব্দে বাক্য, প্রশ্নোত্তর, নাম-শব্দ "
                "খোঁজা, ছড়া শেষ করা — কোনোটিই মূল্যায়নমূলক বিচার চায় না, তাই Evaluate-এর কোনো "
                "বিষয়বস্তু-ভিত্তি এই পাঠে নেই। Create-এর একটিমাত্র আইটেম (S08) কবিতার ভাব "
                "অনুসরণ করে নিজের ইচ্ছা লেখার কাজ। CD-171(b) অনুযায়ী Bloom নথিভুক্ত, "
                "রেশনভুক্ত নয়।"),
            "gaps": [
                "S14 · S15 — CD-147 অনুযায়ী কাগজ-স্তরের, শ্রেণিগতভাবে; এই পাঠ এদের নিয়ে কিছু "
                "ঘোষণা করে না এবং করার দায়ও নেই (CD-147(c))। অনুশীলনী ৫-এর শিরোনামসহ রচনার "
                "নির্দেশ থাকা সত্ত্বেও নয় — CD-147(g) এই পাঠের নাম ধরে সেই সিদ্ধান্ত "
                "প্রত্যাখ্যান করেছে।",
                "অনুশীলনী ২ ছাপা বইয়ে যা-ই থাকুক, এই extraction-এ নেই (তালিকা: ১ ৩ ৪ ৫ ৬)। "
                "সেখান থেকে কিছুই লেখা হয়নি এবং লেখা যেত না — তিন-টোকেনের কোনো anchor নেই। "
                "পাঠ ১৩–২৩-এর জন্য canon/sources/c5/bangla/evidence/-এ কোনো পৃষ্ঠা-চিত্র নেই "
                "(CD-167(d)), তাই এটি উৎসেও যাচাই করা যায় না। পরের পাঠকের এটি জানা দরকার।",
                "অনুশীলনী ৬ (ছড়া শেষ করা) ব্যবহার করা হয়নি, এবং কারণটি নীতিগত নয়, প্রমাণগত: "
                "উৎস অনুশীলনীটির নাম ও প্রথম কয়েকটি শব্দ ছাপে কিন্তু ছড়াটির একটি চরণও ছাপে "
                "না, তাই কোনো আইটেমের উত্তর উৎসে যাচাই করা যেত না। বই খোলা এখানে অনুমোদিত পথ "
                "নয় (উৎসের নিজের ভূমিকা: 'এই ফাইল থেকেই উপাদান নিতে হবে')।",
                "কবিতার ছাপা ১৫ ও ২৭ নং লাইন (C-03) এবং ৩৩–৩৬ নং লাইন (⚠ তৃতীয় ধারা) সম্পূর্ণ "
                "অব্যবহৃত। এগুলো এই ঢেউয়ে বাদ পড়েনি — এগুলো কোনো ঢেউয়েই ব্যবহার করা যাবে না।",
                "ছাপা ১০ নং লাইন S11-এর উদ্দীপক হতে পারেনি, কারণ ওই লাইনটি ড্যাশ দাবি করে আর "
                "ড্যাশ C5-এ নিষিদ্ধ (CD-165/CD-166)। লাইনটি S04 বা অন্য কোনো স্লটেও ব্যবহার "
                "করা হয়নি, কারণ চিহ্নটি চরণের অর্থের অংশ।",
                "S10-এ ক্রিয়ার কাল ও ভাষারীতি পরিবর্তন লেখা হয়নি — দুটিই BAN-S10-এর "
                "admitted_set-এর সদস্য, কিন্তু C5 নির্বাচন করেছে পদ নির্ণয়; নির্বাচনের বাইরের "
                "কাজ লিখলে COVERAGE ও PLAN দুটোই off-choice হিসেবে ধরে (CD-138(b))।",
                "S13-এ অর্থ জেনে নিই-এর আটটি অর্থের মধ্যে তিনটি ব্যবহার করা যায়নি: 'ঘাটের "
                "সিঁড়ি' → ঘাটের ধাপ এবং 'ডান দিকে' → দখিন ধারে এক শব্দ নয়, আর 'গোসল করতে' → "
                "নাইতে ক্রিয়ার রূপ, এক কথায় প্রকাশের শব্দ নয়।",
                "S07/S08-এর বাইরে বিস্তৃত উত্তরের আরও উপাদান এই কবিতায় নেই: ছয়টি স্তবকের দুটি "
                "আংশিক ও একটি সম্পূর্ণ ⚠-নিষিদ্ধ, আর বাকিগুলোর প্রতিটি ইতিমধ্যেই একটি করে "
                "S08 আইটেমে ধরা হয়েছে। ষষ্ঠ একটি আইটেম একই স্প্যানের পুনরাবৃত্তি হতো।",
            ],
        },
        "flags": [],
        "pool_index": {"HW": hw, "AS": as_, "CT": ct},
        "slot_index": slot_index,
        "task_index": task_index,
        "source_index": source_index,
        "questions": questions,
        "waves": {"1": (f"Q01–Q{len(questions):02d} · 2026-08-18 · author_U18_wave1.py · "
                        f"পাঠ ১৮-এর প্রথম ব্যাংক, CD-141 teacher-lane-এ authored under CD-171 "
                        f"(no pool-level counts), PLAN কাউন্টারসাইন সহ (CD-142(b))")},
    }


# =====================================================================================
# SELFCHECK — cheap pre-gate arithmetic, so a failing run says WHY before the suite does.
# It also runs THREE checks NO GATE IN THE SUITE PERFORMS on a qp6 bank:
#   · the QB-CR-017 S11 mark-count diff (that row's own proposed gate, not built repo-wide);
#   · the ⚠-barred-line scan, over every authored string, student- AND teacher-facing;
#   · the E-AUTHOR-ENDORSE honorific scan.
# =====================================================================================
TAUGHT_SET = {"দাঁড়ি", "কমা", "প্রশ্নচিহ্ন", "বিস্ময়চিহ্ন", "উদ্ধরণ চিহ্ন"}
MARK_CHARS = {"দাঁড়ি": "।", "কমা": ",", "প্রশ্নচিহ্ন": "?", "বিস্ময়চিহ্ন": "!",
              "সেমিকোলন": ";", "কোলন": ":", "ড্যাশ": "—"}
BARRED_LINES = [
    ("গান গেয়ে যাই", "C-03 · printed line 15"),
    ("পরীর নাচন", "C-03 · printed line 27"),
    ("কোণে কোণে আপন মনে", "warn-block clause 3 · printed line 33"),
    ("করছে তারা কী কে", "warn-block clause 3 · printed line 34"),
    ("আমারি ভয় করবে কেমন", "warn-block clause 3 · printed line 35"),
    ("তাকাতে সেই দিকে", "warn-block clause 3 · printed line 36"),
    ("দুই পারেরই সাথে", "printed line 10 · requires DASH, barred at C5 by CD-165/CD-166"),
]
HONORIFICS = ["মহান কবি", "বিশ্বকবি", "কবিগুরু", "জাতীয় কবি", "বিদ্রোহী কবি"]


def norm(s):
    s = unicodedata.normalize("NFC", s or "")
    s = re.sub(r"[‘’“”'\"()\[\]।,;:?!—–\-….*_#>|/·]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def all_strings(q):
    """Every authored string on an item — student-facing AND teacher-facing."""
    out = [q.get("question_text", "")]
    for o in q.get("options") or []:
        out += [o.get("text", ""), o.get("why_wrong", "")]
    for b in q.get("blanks") or []:
        out += list(b.get("accepted") or [])
    k = q.get("answer_key")
    if isinstance(k, dict):
        out += list(k.get("accepted") or [])
        out.append(k.get("model_note") or "")
    r = q.get("rubric") or {}
    for c in r.get("criteria") or []:
        out.append(c.get("criterion", ""))
        out += list((c.get("band_descriptors") or {}).values())
    return [s for s in out if s]


def selfcheck(bank):
    import collections
    bad = 0
    qs = bank["questions"]
    n = len(qs)
    print(f"  items: {n}")
    c = collections.Counter(q["bloom_level"] for q in qs)
    print("  bloom: " + " · ".join(
        f"{k} {c[k]}" for k in ("Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create")))
    d = collections.Counter(q["difficulty"] for q in qs)
    print(f"  difficulty: easy {100*d['easy']/n:.1f}% (floor 30%) · medium "
          f"{100*d['medium']/n:.1f}% · hard {100*d['hard']/n:.1f}%")
    if 100 * d["easy"] / n < 30:
        print("  <-- EASY BELOW 30% — DIFFICULTY will FAIL")
        bad += 1
    sc = bank["header"]["slot_counts"]
    print("  slots: " + " · ".join(f"{s} {sc[s]}" for s in sorted(sc)))
    pools = bank["pool_index"]
    print("  pools: " + " · ".join(f"{k} {len(v)}" for k, v in pools.items())
          + f"  (sum {sum(len(v) for v in pools.values())} of {n})")

    as_ = [q for q in qs if q["qid"] in pools["AS"]]
    hi = [q for q in as_ if q["bloom_level"] in ("Apply", "Analyze", "Evaluate", "Create")
          or q["difficulty"] == "hard"]
    print(f"  AS above HW level: {100*len(hi)/len(as_):.0f}% (QB-D-004 wants ~35-65%)")

    for q in qs:
        for s in [q["question_text"]] + [o.get("text", "") for o in q.get("options") or []]:
            if re.search(r"[0-9]", s):
                print(f"  <-- ASCII DIGIT in {q['qid']}: {s[:40]}")
                bad += 1

    # Anchors — resolved against THE CHAPTER SECTION, not merely against the file.
    full = (ROOT / EXTRACTION).read_text(encoding="utf-8")
    sec = full.split("# পাঠ ১৮ — ইচ্ছামতী")[1].split("# পাঠ ১৯")[0]
    hay = norm(sec)
    for qid, a in bank["source_index"].items():
        na = norm(a)
        if len(na.split()) < 3:
            print(f"  <-- ANCHOR TOO SHORT {qid}: {a!r}")
            bad += 1
        elif na not in hay:
            print(f"  <-- ANCHOR NOT IN THE পাঠ ১৮ SECTION {qid}: {a!r}")
            bad += 1
    print(f"  anchors: {len(bank['source_index'])} checked against the পাঠ ১৮ section only")

    hits = 0
    total_strings = sum(len(all_strings(q)) for q in qs)
    for q in qs:
        for s in all_strings(q):
            ns = norm(s)
            for frag, why in BARRED_LINES:
                if norm(frag) in ns:
                    print(f"  <-- BARRED LINE in {q['qid']} ({why}): {s[:50]}")
                    hits += 1
    print(f"  barred-line scan: {len(BARRED_LINES)} strings searched over {total_strings} "
          f"authored strings, {hits} hit(s)")
    bad += hits

    hon = 0
    for q in qs:
        for s in all_strings(q):
            for h in HONORIFICS:
                if h in s:
                    print(f"  <-- HONORIFIC '{h}' in {q['qid']}")
                    hon += 1
    print(f"  honorific scan (E-AUTHOR-ENDORSE): {hon} hit(s)")
    bad += hon

    # QB-CR-017 — the S11 mark-count diff. THIS IS THE CHECK NO GATE IN THE SUITE PERFORMS.
    print("  QB-CR-017 S11 mark-count diff (stimulus vs key):")
    for q in qs:
        if bank["slot_index"][q["qid"]] != "S11":
            continue
        # THE STIMULUS, NOT THE STEM. The stem ends with an instruction sentence that carries its
        # own দাঁড়ি; diffing the whole stem cancels the দাঁড়ি the student must insert and reports
        # 1 where the item requires 2. Found by this check's own first run and corrected — the
        # measurement is the point of the check, so a measurement artefact here is a real defect
        # in the check (CD-145(f): an arithmetic claim is verified by running the thing it counts).
        m = re.match(r"^'(.*?)' — ", q["question_text"], re.S)
        assert m, f"{q['qid']}: S11 stem does not carry a quoted stimulus"
        stim = m.group(1)
        key = (q["answer_key"]["accepted"] or [""])[0]
        added = {name: key.count(ch) - stim.count(ch) for name, ch in MARK_CHARS.items()}
        req = {k: v for k, v in added.items() if v > 0}
        total = sum(req.values())
        off = [k for k in req if k not in TAUGHT_SET]
        flag = ""
        if total < 2:
            flag += "  <-- SINGLE MARK — QB-CR-017's DEFECT SHAPE"
            bad += 1
        if off:
            flag += f"  <-- OUTSIDE C5 TAUGHT SET: {off}"
            bad += 1
        print(f"    {q['qid']}: {total} mark(s) — "
              + " · ".join(f"{k} x{v}" for k, v in req.items()) + flag)

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
                    bad += 1
    print(f"  worst within-slot stem similarity: {worst:.0%} (PLAN fails at 95%)")
    print(f"  selfcheck problems: {bad}")
    return bad


if __name__ == "__main__":
    bank = build()
    selfcheck(bank)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(bank, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"  wrote {OUT.relative_to(ROOT)}  ({len(bank['questions'])} items)")
