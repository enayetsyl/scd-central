#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""correct_U13_S11_tags.py — QB-CR-014: পাঠ ১৩'s eight S11 items move `-02` → `-13`.

Run from the repo root:
    python workstreams/question-banks/authoring/correct_U13_S11_tags.py

WHY THIS IS A SEPARATE SCRIPT AND NOT AN EDIT TO `author_U13_wave3.py`
----------------------------------------------------------------------
The wave scripts are the record of what each wave authored. **Editing wave 3 to emit `-13` would
make the record say the wave got it right**, and the whole value of the corrections ledger is that
it preserves the evidence a bank was ever wrong (`QB-CR-009`'s own words: *a silent re-tag would
destroy the evidence*). So wave 3 keeps `SENT = "TOP-BAN-C5-02"` and this file carries the
correction on top of it. **The bank remains reproducible as: wave 1–4, then this.**

IDEMPOTENT AND NARROW BY CONSTRUCTION. It rewrites `topic_tag` on items whose `slot_index` entry is
exactly `S11` and whose current tag is exactly `TOP-BAN-C5-02`, refuses if the count is not 8, and
touches no other field. `ref19_topic_id` stays `BAN-SENTENCE` — REF-19 carries no punctuation slug
at all (PENDING-P-008, FLAGGED), so there is nothing to move it to, and inventing one would be the
QB-CR-008 error in the other register.
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
BANK = ROOT / "workstreams/question-banks/banks/C5_BAN_U13_QuestionBank_v1.json"
OLD, NEW = "TOP-BAN-C5-02", "TOP-BAN-C5-13"
EXPECTED = 8


def main():
    bank = json.loads(BANK.read_text(encoding="utf-8"))
    slot_index = bank["slot_index"]

    targets = [q for q in bank["questions"]
               if slot_index.get(q["qid"]) == "S11" and q.get("topic_tag") == OLD]
    already = [q for q in bank["questions"]
               if slot_index.get(q["qid"]) == "S11" and q.get("topic_tag") == NEW]

    if already and not targets:
        print(f"  already corrected: {len(already)} S11 item(s) carry {NEW} — nothing to do")
        return 0
    if len(targets) != EXPECTED:
        print(f"  REFUSED: found {len(targets)} S11 item(s) at {OLD}, expected {EXPECTED}. "
              f"The bank is not in the state this correction was written against.")
        return 2

    for q in targets:
        before = dict(q)
        q["topic_tag"] = NEW
        # metadata only — prove it rather than assert it
        moved = {k for k in set(before) | set(q) if before.get(k) != q.get(k)}
        assert moved == {"topic_tag"}, f"{q['qid']}: unexpected field change {moved}"
        print(f"  {q['qid']}  {OLD} -> {NEW}   (ref19 {q['ref19_topic_id']}, unchanged)")

    # The header's topic list is the topic authority COVERAGE reads (§4). `-02` stays: 17 S03
    # items still carry it. `-13` is now supplied and must be declared.
    topics = bank["header"]["topics"]
    if NEW not in topics:
        topics.append(NEW)
        print(f"  header.topics += {NEW}  -> {topics}")
    supplied = {q["topic_tag"] for q in bank["questions"]}
    for t in topics:
        assert t in supplied, f"header declares {t}; no item supplies it"
    print(f"  {OLD} still supplied by {sum(1 for q in bank['questions'] if q['topic_tag']==OLD)} item(s)")

    BANK.write_text(json.dumps(bank, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"  wrote {BANK.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
