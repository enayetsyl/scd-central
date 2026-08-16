#!/usr/bin/env python3
"""CD-149 — correct `QP-BAN-C5-U15-Q01`'s S01 span to EIGHT PRINTED LINES.

WHY THE ITEM WAS WRONG, and it was not an authoring slip.
`author_U15_wave1.py` built Q01 from the extraction's own delimiters — *"থাকব না কো বদ্ধ ঘরে…"
থেকে "…বরণ মরণ-যন্ত্রণাকে।" পর্যন্ত* — which was the correct thing to do with the source in hand.
**The delimiter itself is defective**: counted at source it falls at printed line SIX, where the
same extraction's delimiters for পাঠ ১৩, ১৮ and ২০ all fall exactly at line EIGHT. CD-149 rules the
unit is the printed line and locates the defect. So this corrects the ITEM, and the source flag it
came from is recorded in CD-149(c) — the extraction is not edited here.

WHAT MOVES: `question_text` and `answer_key.accepted[0]` on Q01 only, plus `model_note`'s wording
of the span. NOTHING ELSE — not marks, not bloom_level, not difficulty, not topic_tag, not
ref19_topic_id, not the slot or task index, and no other item. Asserted per field before writing.

THE WAVE SCRIPT IS NOT EDITED (`QB-CR-014(g)`). `author_U15_wave1.py` keeps the delimiter-derived
span it authored, because editing it would make the record say wave 1 already knew the delimiter
was short. The bank is reproducible as wave 1 THEN this script.

UNLIKE `correct_S14_S15_declarations_CD147.py`, THIS ONE CHANGES THE `questions` ARRAY, so the
digest moves and all three export artifacts must be regenerated. That is the caller's next step and
`ENVELOPE-SYNC` will fail until it is done — correctly.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BANK = ROOT / "workstreams/question-banks/banks/C5_BAN_U15_QuestionBank_v1.json"
QID = "QP-BAN-C5-U15-Q01"

# The eight printed lines, transcribed from canon/marklogic/C5_Bangla_Source_13-23.md পাঠ ১৫
# পূর্ণ পাঠ, in the book's own line order. Lines 7 and 8 are what the old span was missing.
LINES = [
    "থাকব না কো বদ্ধ ঘরে, দেখব এবার জগৎটাকে—",
    "কেমন করে ঘুরছে মানুষ যুগান্তরের ঘূর্ণিপাকে।",
    "দেশ হতে দেশ দেশান্তরে",
    "ছুটছে তারা কেমন করে,",
    "কীসের নেশায় কেমন করে মরছে যে বীর লাখে লাখে,",
    "কীসের আশায় করছে তারা বরণ মরণ-যন্ত্রণাকে।",
    "কেমন করে বীর ডুবুরি সিন্ধু সেঁচে মুক্তা আনে,",
    "কেমন করে দুঃসাহসী চলছে উড়ে স্বর্গপানে।",
]

NEW_STEM = ("কবি ও কবিতার নাম লিখে 'সংকল্প' কবিতার 'থাকব না কো বদ্ধ ঘরে…' থেকে "
            "'…কেমন করে দুঃসাহসী চলছে উড়ে স্বর্গপানে।' পর্যন্ত প্রথম আট লাইন মুখস্থ লেখো।")
NEW_KEY = "কবিতা: সংকল্প; কবি: কাজী নজরুল ইসলাম। " + " ".join(LINES)
NEW_NOTE = ("নম্বর ভাগ SLOT_REGISTER BAN-S01-এর ঘোষিত অংশ অনুযায়ী: কবির নাম ১ + কবিতার নাম ১ + "
            "প্রথম ৮ লাইন ৮ = ১০। CD-149 অনুযায়ী একক হলো মুদ্রিত লাইন, পঙ্‌ক্তি নয় — বইয়ের বিন্যাসে "
            "আট লাইন, শেষ লাইন '…চলছে উড়ে স্বর্গপানে।'। লাইন হুবহু পাঠের মতো হতে হবে; বানান ও "
            "যতিচিহ্নে ছাড় দেওয়া যাবে। কবির নাম কেবল তথ্য হিসেবে — কোনো সম্মানসূচক বিশেষণ লেখা "
            "যাবে না বা চাওয়া যাবে না (E-AUTHOR-ENDORSE)।")


def main() -> int:
    bank = json.loads(BANK.read_text(encoding="utf-8"))
    items = bank["questions"]
    target = [q for q in items if q.get("qid") == QID]
    if len(target) != 1:
        print(f"REFUSING: expected exactly 1 item with qid {QID}, found {len(target)}")
        return 1
    q = target[0]

    if q["question_text"] == NEW_STEM:
        print(f"  OK    {QID} already at the CD-149 span — nothing to do")
        return 0

    others_before = json.dumps([x for x in items if x.get("qid") != QID],
                               ensure_ascii=False, sort_keys=True)
    frozen_before = {k: json.dumps(v, ensure_ascii=False, sort_keys=True)
                     for k, v in q.items()
                     if k not in ("question_text", "answer_key")}
    header_before = json.dumps(bank.get("header"), ensure_ascii=False, sort_keys=True)
    idx_before = (json.dumps(bank.get("slot_index"), ensure_ascii=False, sort_keys=True),
                  json.dumps(bank.get("task_index"), ensure_ascii=False, sort_keys=True),
                  json.dumps(bank.get("source_index"), ensure_ascii=False, sort_keys=True))

    q["question_text"] = NEW_STEM
    q["answer_key"]["accepted"] = [NEW_KEY]
    q["answer_key"]["model_note"] = NEW_NOTE

    # --- prove nothing else moved -------------------------------------------------------
    assert json.dumps([x for x in items if x.get("qid") != QID], ensure_ascii=False,
                      sort_keys=True) == others_before, "another item moved — refusing"
    for k, v in frozen_before.items():
        assert json.dumps(q[k], ensure_ascii=False, sort_keys=True) == v, \
            f"{QID}.{k} moved and must not have — refusing"
    assert json.dumps(bank.get("header"), ensure_ascii=False,
                      sort_keys=True) == header_before, "the header moved — refusing"
    assert (json.dumps(bank.get("slot_index"), ensure_ascii=False, sort_keys=True),
            json.dumps(bank.get("task_index"), ensure_ascii=False, sort_keys=True),
            json.dumps(bank.get("source_index"), ensure_ascii=False,
                       sort_keys=True)) == idx_before, "an index moved — refusing"
    assert set(q["answer_key"]) >= {"accepted", "model_note"}, "answer_key lost a key — refusing"

    BANK.write_text(json.dumps(bank, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"  FIXED {QID} — span now 8 printed lines, ending '…চলছে উড়ে স্বর্গপানে।'")
    print("        question_text, answer_key.accepted[0] and model_note moved; nothing else.")
    print("        THE DIGEST HAS MOVED — regenerate array, single/ and .batch.json before the suite.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
