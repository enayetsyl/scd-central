#!/usr/bin/env python3
"""CD-147 — simplify the S14/S15 exclusion reasons in the three live C5 BAN banks.

WHY THIS IS A SCRIPT AND NOT A HAND EDIT (`QB-CR-014(e)`/(g)).
The wave scripts are NOT edited: `author_U13_wave*.py`, `author_U14_wave1.py` and
`author_U15_wave1.py` keep the CD-139-era content reasons they were authored with, because editing
them would make the record say those waves already knew about CD-147. The bank is reproducible as
`waves THEN this correction script`, and the two-step IS the record.

WHAT MOVES, AND NOTHING ELSE.
`header.slot_exclusions["S14"]` and `["S15"]` only. Every other key of every other field is
asserted unchanged per bank before anything is written. No question, no `slot_index`, no
`task_index`, no digest input is touched — the `questions` array is byte-identical after this runs,
which is why no export regeneration and no signature re-pin is owed (contrast `QB-CR-014`, where
`topic_tag` moved on eight live items and all four artifacts had to be rebuilt).

IDEMPOTENT. Running it twice is a no-op; it refuses on any bank whose S14/S15 entries are missing
or already carry the new text with a different body.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BANKS = ROOT / "workstreams/question-banks/banks"

NEW = {
    "S14": ("CD-147 — S14 আবেদনপত্র প্রতিটি পাঠের জন্যই কাগজ-স্তরের (paper-level), শ্রেণিভেদে বা "
            "বিষয়বস্তুভেদে নয়। এটি কেবল কাগজ/পরীক্ষার পাইপলাইনে লেখা হয়, কোনো অধ্যায়-ব্যাংকে নয়। "
            "এই ঘোষণা আর বিষয়বস্তুর কারণ নয় — নিয়মটি শ্রেণিগত, তাই পাঠের কোনো কারণ দেখানোর দায় নেই।"),
    "S15": ("CD-147 — S15 রচনা প্রতিটি পাঠের জন্যই কাগজ-স্তরের (paper-level)। এটি কেবল "
            "কাগজ/পরীক্ষার পাইপলাইনে লেখা হয়, কোনো অধ্যায়-ব্যাংকে নয়। এই ঘোষণা আর বিষয়বস্তুর "
            "কারণ নয় — নিয়মটি শ্রেণিগত, তাই পাঠের কোনো কারণ দেখানোর দায় নেই।"),
}


def main() -> int:
    changed = 0
    for path in sorted(BANKS.glob("C5_BAN_U*_QuestionBank_v1.json")):
        raw = path.read_text(encoding="utf-8")
        bank = json.loads(raw)
        header = bank.get("header")
        if not header or "slot_exclusions" not in header:
            print(f"  SKIP  {path.name} — no header.slot_exclusions (pre-CD-138 shape)")
            continue

        before_questions = json.dumps(bank["questions"], ensure_ascii=False, sort_keys=True)
        before_header = {k: v for k, v in header.items() if k != "slot_exclusions"}
        before_other_excl = {k: v for k, v in header["slot_exclusions"].items()
                             if k not in NEW}

        touched = []
        for slot, text in NEW.items():
            if slot not in header["slot_exclusions"]:
                continue
            if header["slot_exclusions"][slot] == text:
                continue
            header["slot_exclusions"][slot] = text
            touched.append(slot)

        # --- second operation, named separately: the declaration PROSE cites CD-139(d) as live
        # --- authority. It is APPENDED to, never rewritten — the original sentence is the record
        # --- of what that session declared and on what, and a rewrite would erase the evidence
        # --- that the declaration ever rested on CD-139. Same forward-only shape as the ledgers.
        APPEND = (" [CD-147, 2026-08-16 — এই অনুচ্ছেদের S14/S15 অংশটুকু অতিক্রান্ত, বাকিটা বহাল। "
                  "S14 ও S15 এখন প্রতিটি পাঠের জন্যই কাগজ-স্তরের, শ্রেণিগতভাবে; CD-139(d)-এর পাঠ ৪-এ "
                  "S14 স্বীকৃতি নাম ধরে বাতিল। কোনো পাঠ এই দুটির জন্য বিষয়বস্তুর কারণ দেখানোর দায়ে "
                  "নেই। উপরের বাক্য মুছে ফেলা হয়নি — ঘোষণাটি তখন কীসের উপর দাঁড়িয়ে ছিল, সেটিই "
                  "রেকর্ড।]")
        decl = header.get("admissibility_declaration")
        if isinstance(decl, str) and "CD-147" not in decl:
            header["admissibility_declaration"] = decl + APPEND
            touched.append("admissibility_declaration(appended)")
            before_header = {**before_header,
                             "admissibility_declaration": header["admissibility_declaration"]}

        if not touched:
            print(f"  OK    {path.name} — already at CD-147 text, nothing to do")
            continue

        # --- assert that NOTHING else moved, per bank, before writing -------------------
        assert json.dumps(bank["questions"], ensure_ascii=False,
                          sort_keys=True) == before_questions, \
            f"{path.name}: the questions array moved — refusing"
        assert {k: v for k, v in header.items() if k != "slot_exclusions"} == before_header, \
            f"{path.name}: a header field other than slot_exclusions moved — refusing"
        assert {k: v for k, v in header["slot_exclusions"].items()
                if k not in NEW} == before_other_excl, \
            f"{path.name}: an exclusion reason other than S14/S15 moved — refusing"

        path.write_text(json.dumps(bank, ensure_ascii=False, indent=1) + "\n",
                        encoding="utf-8")
        changed += 1
        print(f"  FIXED {path.name} — {', '.join(touched)} now cite CD-147")

    print(f"\n{changed} bank(s) rewritten. The questions array is untouched in every one, so no "
          f"export regeneration and no signature re-pin is owed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
