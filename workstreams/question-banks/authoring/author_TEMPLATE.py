# -*- coding: utf-8 -*-
"""author_TEMPLATE.py — authoring scaffold for a C5 BAN chapter question bank.

Generalised from author_U22_wave1.py, which was rebuilt after QB-CR-022 (114 of 117 anchors
failed SOURCE-TRACE because they were written as citation labels).

WHAT THIS DOES. Every mechanical contract in BUILD_CONTRACT.md is asserted HERE, at author
time, so a bank that would fail the gate is never written to disk. The checks are copies of
the gate's own functions, not reimplementations of their intent — where a constant appears
below it is quoted from gates.py with its line named, and MUST be re-derived when this
template is used, because a copied constant drifts and the gate is the authority.

HOW TO USE.
  1. Fetch the chapter extraction, SLOT_REGISTER.json, TOPIC_NUMBERS.md, REF-19 and gates.py
     at a pinned commit into the working directory.
  2. Fill in CHAPTER / BANK_ID / EXTRACTION_PATH / COMMIT below.
  3. Define the verbatim anchor constants (section A) by reading the extraction.
  4. Author items (section B).
  5. Run. It emits the bank ONLY if every pre-flight passes.

WHAT IT DOES NOT DO. It does not judge whether a question is true, well-aimed, honestly
tagged, or fit for Class 5. That is REVIEW's work and no script substitutes for it
(QB-CR-020: twelve findings in a bank that passed all 24 gates).
"""
import collections
import hashlib
import itertools
import json
import re
import sys
import unicodedata

# ══════════════════════════════════════════════════════════════════════════════
# CONFIG — fill in per chapter
# ══════════════════════════════════════════════════════════════════════════════
COMMIT = "PUT_PINNED_COMMIT_HERE"
CHAPTER = "পাঠ nn — TITLE"
BANK_ID = "QB-BAN-C5-Unn"
QID_PREFIX = "QP-BAN-C5-Unn"
EXTRACTION_PATH = "canon/sources/c5/bangla/C5_BAN_Source_nn.md"
EXTRACTION_LOCAL = "C5_BAN_Source_nn.md"
REGISTER_LOCAL = "SLOT_REGISTER.json"
OUT_PATH = "/mnt/user-data/outputs/C5_BAN_Unn_QuestionBank_v1.json"

# gates.py constants — RE-DERIVE THESE, do not trust the copy.
#   NEAR_DUP_JACCARD  gates.py:358   MIN_ANCHOR_TOKENS gates.py:1193
#   PLAN_DUP_FAIL     gates.py:2027  PLAN_DUP_REPORT   gates.py:2028
#   EASY_FLOOR        gates.py:406   REF06_C3_5        gates.py:374
NEAR_DUP_JACCARD = 0.80
MIN_ANCHOR_TOKENS = 3
PLAN_DUP_FAIL = 0.95
PLAN_DUP_REPORT = 0.85
EASY_FLOOR = 30.0
BLOOM_LEVELS = {"Remember", "Understand", "Apply", "Analyze", "Evaluate", "Create"}
DIFFICULTIES = {"easy", "medium", "hard"}
KEY_FIELD_BY_TYPE = {
    "mcq": "options", "true_false": "tf_answer", "fill_blank": "blanks",
    "matching": "pairs", "short_answer": "answer_key", "descriptive": "rubric",
}

# ══════════════════════════════════════════════════════════════════════════════
# GATE FUNCTIONS — copied verbatim from gates.py so the pre-flight is the gate's
# own arithmetic and not an approximation of it.
# ══════════════════════════════════════════════════════════════════════════════
def qp_norm(s):
    """gates.py — NFC, punctuation-stripped, whitespace-collapsed."""
    s = unicodedata.normalize("NFC", s or "")
    s = re.sub(r"[‘’“”'\"()\[\]।,;:?!—–\-….*_#>|/·]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def qb_norm(s):
    return qp_norm(s).lower()


def qb_tokens(s):
    return set(qb_norm(s).split())


def qb_jaccard(a, b):
    return len(a & b) / len(a | b) if (a | b) else 0.0


def _stem_sim(a, b):
    ta, tb = set(a.split()), set(b.split())
    return len(ta & tb) / len(ta | tb) if (ta | tb) else 0.0


def qb_answer_signature(q):
    """gates.py:477 — what the item actually asks the student to produce."""
    qt = q.get("question_type")
    if qt == "mcq":
        return qb_norm(next((o.get("text", "") for o in q.get("options", [])
                             if o.get("is_correct")), ""))
    if qt == "true_false":
        return ""
    if qt == "fill_blank":
        return " | ".join(qb_norm((b.get("accepted") or [""])[0]) for b in q.get("blanks", []))
    if qt == "matching":
        return " | ".join(f"{qb_norm(p.get('left'))}={qb_norm(p.get('right'))}"
                          for p in q.get("pairs", []))
    if qt == "short_answer":
        return qb_norm(((q.get("answer_key") or {}).get("accepted") or [""])[0])
    if qt == "descriptive":
        rb = q.get("rubric") or {}
        return " | ".join(qb_norm(c.get("criterion")) for c in rb.get("criteria", [])
                          if c.get("role") == "content")
    return ""


def declared_tasks(row):
    """gates.py:1533 — the ONLY strings an item may claim at this slot."""
    if row["task_mode"] == "alternative":
        return list(row.get("admitted_set") or [])
    if row["task_mode"] == "composite":
        return [p["part"] for p in row.get("parts") or []]
    return [row.get("admitted_task")]


# ══════════════════════════════════════════════════════════════════════════════
# STATE
# ══════════════════════════════════════════════════════════════════════════════
EXTRACTION = open(EXTRACTION_LOCAL, encoding="utf-8").read()
HAY = qp_norm(EXTRACTION)
REGISTER = {r["slot"].split("-")[-1]: r
            for r in json.load(open(REGISTER_LOCAL, encoding="utf-8"))["rows"]
            if r.get("subject") == "BAN" and r.get("class") == 5}

QS, SLOT, TASK, SRC = [], {}, {}, {}
_n = [0]


def die(msg):
    sys.exit("PRE-FLIGHT REFUSED — " + msg)


def check_anchor(qid, a):
    """SOURCE-TRACE at author time. gates.py:1180-1208. QB-CR-022 exists because this
    was not run: an anchor must be a verbatim SPAN of the book, not a citation label."""
    n = qp_norm(a)
    if len(n.split()) < MIN_ANCHOR_TOKENS:
        die("ANCHOR TOO SHORT %s: %r -> %d token(s), floor is %d"
            % (qid, a, len(n.split()), MIN_ANCHOR_TOKENS))
    if n not in HAY:
        die("ANCHOR NOT IN EXTRACTION %s: %r" % (qid, a))


def add(slot, task, tag, text, qtype, role, bloom, diff, marks, src, **kw):
    _n[0] += 1
    qid = "%s-Q%02d" % (QID_PREFIX, _n[0])
    q = {"qid": qid, "topic_tag": tag[0], "ref19_topic_id": tag[1],
         "question_text": text, "question_type": qtype, "paper_role": role,
         "bloom_level": bloom, "difficulty": diff, "tier": "tier1",
         "marks": marks, "chapter_ref": CHAPTER}
    q.update(kw)
    check_anchor(qid, src)
    QS.append(q); SLOT[qid] = slot; TASK[qid] = task; SRC[qid] = src
    return qid


def sa(*a, **k):
    acc = k.pop("accepted"); note = k.pop("note", None)
    key = {"accepted": acc}
    if note:
        key["model_note"] = note
    return add(*a, answer_key=key, **k)


def mcq(slot, task, tag, text, opts, bloom, diff, marks, src):
    """opts: [(text, is_correct, why_wrong_or_None), ...] — option_id assigned ক খ গ ঘ."""
    o = []
    for oid, (t, ok, why) in zip("কখগঘঙচ", opts):
        d = {"option_id": oid, "text": t, "is_correct": ok}
        if not ok:
            d["why_wrong"] = why
        o.append(d)
    return add(slot, task, tag, text, "mcq", "mcq", bloom, diff, marks, src, options=o)


def rub(content_crit, cbands, align_crit, abands, bands=("সম্পূর্ণ", "আংশিক")):
    """A `content` row gives descriptive items an answer signature; without one they are
    exempt from the collision check, which is how five identical S08 items once passed."""
    return {"bands": list(bands),
            "criteria": [{"role": "content", "criterion": content_crit,
                          "band_descriptors": cbands},
                         {"role": "islamic_alignment", "criterion": align_crit,
                          "band_descriptors": abands}]}


# ══════════════════════════════════════════════════════════════════════════════
# SECTION A — VERBATIM ANCHORS. Read them off the extraction. Each must survive
# qp_norm as >= 3 tokens and appear in the file. Stop a span at a page break:
# the extraction interposes `### ছাপা nn` and image captions.
# ══════════════════════════════════════════════════════════════════════════════
# A_EXAMPLE = "একটি সম্পূর্ণ ছাপা বাক্য পাঠ্য অংশ থেকে।"

# ══════════════════════════════════════════════════════════════════════════════
# SECTION B — ITEMS. Vary each stem with its own printed context; a bare per-word
# frame lands at exactly 0.80 and FAILS ZERO-OVERLAP.
# ══════════════════════════════════════════════════════════════════════════════
# sa("S02", "মূল কাঠামো", VOCB, '"%s" — এখানে \'X\' শব্দের অর্থ কী?' % A_EXAMPLE,
#    "short_answer", "short", "Remember", "easy", 1, A_EXAMPLE, accepted=["..."])

# ══════════════════════════════════════════════════════════════════════════════
# PRE-FLIGHT — every mechanical gate this script can run, before anything is written
# ══════════════════════════════════════════════════════════════════════════════
def preflight(admissible, exclusions):
    fails = []

    # 1. ZERO-OVERLAP: stems, every pair in the bank
    for a, c in itertools.combinations(QS, 2):
        s = qb_jaccard(qb_tokens(a["question_text"]), qb_tokens(c["question_text"]))
        if s >= NEAR_DUP_JACCARD:
            fails.append("ZERO-OVERLAP %s ~ %s = %.3f" % (a["qid"], c["qid"], s))

    # 2. ZERO-OVERLAP: identical answer signature on one question_type
    seen = {}
    for q in QS:
        sig = qb_answer_signature(q)
        if not sig:
            continue
        k = (sig, q["question_type"])
        if k in seen:
            fails.append("ANSWER-COLLISION %s ~ %s: %r" % (seen[k], q["qid"], sig[:50]))
        else:
            seen[k] = q["qid"]

    # 3. PLAN within-slot
    for a, c in itertools.combinations(QS, 2):
        if SLOT[a["qid"]] != SLOT[c["qid"]]:
            continue
        na, nb = qp_norm(a["question_text"]), qp_norm(c["question_text"])
        s = 1.0 if na == nb else _stem_sim(na, nb)
        if s >= PLAN_DUP_FAIL:
            fails.append("PLAN-DUP %s ~ %s = %.3f" % (a["qid"], c["qid"], s))
        elif s >= PLAN_DUP_REPORT:
            print("  REPORT borderline %s ~ %s = %.3f (passes)" % (a["qid"], c["qid"], s))

    # 4. task_index against the register's own resolver
    for qid, t in TASK.items():
        row = REGISTER.get(SLOT[qid])
        if row is None:
            fails.append("NO REGISTER ROW for %s at %s" % (qid, SLOT[qid]))
            continue
        d = declared_tasks(row)
        claimed = t if isinstance(t, list) else [t]
        if row["task_mode"] == "composite":
            if sorted(claimed) != sorted(d):
                fails.append("COMPOSITE-HALF %s: claims %s, parts are %s" % (qid, claimed, d))
        elif row["task_mode"] == "alternative":
            for c in claimed:
                if row.get("selected") is None:
                    if c not in d:
                        fails.append("OFF-SET %s: %r not in %s" % (qid, c, d))
                elif c != row["selected"]:
                    fails.append("OFF-CHOICE %s: %r, C5 selected %r" % (qid, c, row["selected"]))
        else:
            for c in claimed:
                if c != row.get("admitted_task"):
                    fails.append("WRONG-TASK %s: %r, row says %r" % (qid, c, row.get("admitted_task")))

    # 5. per-item shape
    for q in QS:
        qt = q["question_type"]
        want = KEY_FIELD_BY_TYPE.get(qt)
        if want is None:
            fails.append("BAD-TYPE %s: %r" % (q["qid"], qt)); continue
        if not q.get(want):
            fails.append("NO-KEY %s: %s carries no %r" % (q["qid"], qt, want))
        for other in set(KEY_FIELD_BY_TYPE.values()) - {want}:
            if q.get(other) is not None:
                fails.append("EXTRA-KEY %s carries %r" % (q["qid"], other))
        if q.get("bloom_level") not in BLOOM_LEVELS:
            fails.append("BLOOM %s: %r" % (q["qid"], q.get("bloom_level")))
        if q.get("difficulty") not in DIFFICULTIES:
            fails.append("DIFFICULTY %s: %r" % (q["qid"], q.get("difficulty")))
        if qt == "mcq":
            correct = [o for o in q["options"] if o.get("is_correct")]
            if len(correct) != 1:
                fails.append("MCQ %s has %d correct options" % (q["qid"], len(correct)))
            for o in q["options"]:
                if not o.get("is_correct") and not o.get("why_wrong"):
                    fails.append("MCQ %s: distractor %r has no why_wrong" % (q["qid"], o["option_id"]))
            if len({o["option_id"] for o in q["options"]}) != len(q["options"]):
                fails.append("MCQ %s: duplicate option_id" % q["qid"])
        if qt == "descriptive":
            r = q["rubric"]; bands = r.get("bands") or []
            if len(bands) < 2:
                fails.append("RUBRIC %s: %d band(s)" % (q["qid"], len(bands)))
            if not [c for c in r.get("criteria", []) if c.get("role") == "islamic_alignment"]:
                fails.append("RUBRIC %s: no islamic_alignment row" % q["qid"])
            for c in r.get("criteria", []):
                miss = [b for b in bands if b not in (c.get("band_descriptors") or {})]
                if miss:
                    fails.append("RUBRIC %s: %r missing descriptor for %s" % (q["qid"], c.get("role"), miss))
        # P-037
        k = q.get("answer_key")
        note = (k.get("model_note") or "") if isinstance(k, dict) else ""
        if "CD-136" in note and qt not in ("short_answer", "descriptive"):
            fails.append("P-037 %s: teacher key on %s" % (q["qid"], qt))

    # 6. declaration completeness
    for s in ["S%02d" % i for i in range(1, 14)]:
        if (s in admissible) == (s in exclusions):
            fails.append("DECLARATION %s: must be in exactly one of admissible/exclusions" % s)
    for s in ("S14", "S15"):
        if s in admissible or s in exclusions:
            fails.append("CD-147 %s must be in NEITHER list" % s)
    for s, reason in exclusions.items():
        if not (reason or "").strip():
            fails.append("EXCLUSION %s: blank reason (CD-134(c))" % s)
    used = {SLOT[q["qid"]] for q in QS}
    for s in used - set(admissible):
        fails.append("ITEM IN UNDECLARED SLOT %s" % s)

    # 7. easy floor — the one pool-level failure that remains
    total = len(QS)
    easy = sum(1 for q in QS if q.get("difficulty") == "easy")
    share = 100.0 * easy / total if total else 0.0
    if share < EASY_FLOOR:
        fails.append("EASY-FLOOR: %.1f%% easy, floor is %.1f%%" % (share, EASY_FLOOR))

    # 8. script guard
    blob = json.dumps(QS, ensure_ascii=False)
    for ch, name in (("\u09f0", "ৰ U+09F0"), ("\u09f1", "ৱ U+09F1")):
        if ch in blob:
            fails.append("SCRIPT: %s present — never appears in NCTB content" % name)
    if re.search(r"[\u0600-\u06FF]", blob):
        fails.append("SCRIPT: Arabic range present in rendered text")

    if fails:
        print("\n".join("  FAIL  " + f for f in fails))
        die("%d pre-flight failure(s) — nothing written" % len(fails))

    print("PRE-FLIGHT CLEAN — %d items, %d slot(s), easy %.1f%%"
          % (total, len(used), share))
    print("  bloom:  " + " · ".join("%s %d" % kv for kv in
                                    sorted(collections.Counter(q["bloom_level"] for q in QS).items())))
    print("  NOTE: this proves WELL-FORMEDNESS ONLY. Truth, aim, honest tagging and grade fit")
    print("        are REVIEW's, and REVIEW reads the bank BEFORE it is pushed (QB-CR-020).")


def emit(header):
    pools = {}
    for q in QS:
        s = SLOT[q["qid"]]
        pools[q["qid"]] = "CT" if s in ("S08", "S09") else ("AS" if s in ("S05", "S07") else "HW")
    pool_index = collections.defaultdict(list)
    for qid, p in pools.items():
        pool_index[p].append(qid)
    bank = {
        "schema_version": "1.0", "policy_shape": "qp6", "bank_id": BANK_ID, "wave": 1,
        "subject": "BAN", "class": 5, "chapter": CHAPTER,
        "extraction_path": EXTRACTION_PATH, "source_extraction": EXTRACTION_PATH,
        "verified_against_commit": COMMIT,
        "curation": header.pop("curation"),
        "header": header, "flags": [],
        "pool_index": {k: sorted(v) for k, v in sorted(pool_index.items())},
        "slot_index": SLOT, "task_index": TASK, "source_index": SRC,
        "questions": QS,
        "waves": {"1": "Q01-Q%d · author_TEMPLATE.py · pinned %s" % (len(QS), COMMIT)},
    }
    bank["header"]["target"] = len(QS)
    bank["header"]["slot_counts"] = dict(sorted(collections.Counter(SLOT.values()).items()))
    bank["header"]["topics"] = sorted({q["topic_tag"] for q in QS})
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(bank, f, ensure_ascii=False, indent=1)
    print("WROTE %s" % OUT_PATH)
    raw = open(OUT_PATH, "rb").read()
    print("  bytes  : %d" % len(raw))
    print("  sha256 : %s" % hashlib.sha256(raw).hexdigest())
    print("           ^ REVIEW needs both before it will read the file (LANE_PROMPTS v3).")
    export_reminder(len(QS))


def export_reminder(n):
    """The bank is NOT finished when this script exits. BUILD_CONTRACT.md section 6, and the
    reason paath 22 wave 2 was RETURNED by REVIEW: the three export artifacts are keyed by
    qid, not by version, so the PREVIOUS wave's export stays on disk and stays wrong until it
    is rebuilt. A wave that retires items also leaves orphans, because split_envelopes.py
    writes and never deletes. Printed at emit because 'outside the script' is exactly how a
    mandatory step gets skipped -- that contract section was written and skipped the same day."""
    stem = OUT_PATH.replace("\\", "/").rsplit("/", 1)[-1][:-5]
    print("")
    print("=" * 78)
    print("NOT FINISHED. The export is three tools outside this script and none has run.")
    print("Rebuild it before gating, or ENVELOPE-SYNC fails and the push condition is unmet.")
    print("")
    print("  1. DELETE this bank's stale singles FIRST -- split_envelopes.py never deletes,")
    print("     so any item this wave retired survives as an orphan. Delete BY PREFIX, never")
    print("     the whole directory: single/ holds EVERY bank's envelopes, not just this one.")
    print("       Remove-Item ...\\banks\\envelopes\\single\\%s-*.json" % QID_PREFIX)
    print("")
    print("  2. tools/hub-export/build_question_envelopes.py")
    print("       --json <bank> --curation-tag FLEXIBLE --source-file %s" % EXTRACTION_PATH)
    print("       --unit-title \"%s\" --out ...\\envelopes\\%s.envelopes.json" % (CHAPTER, stem))
    print("  3. workstreams/question-banks/authoring/split_envelopes.py  <that .envelopes.json>")
    print("  4. workstreams/question-banks/authoring/build_batch.py      <that .envelopes.json>")
    print("")
    print("  Each must report %d. Then gate. ENVELOPE-SYNC must name array AND single/ AND" % n)
    print("  the wrapper -- if it names fewer, an artifact was not rebuilt and the run is")
    print("  half blind. PowerShell, not cmd.exe: --unit-title is Bengali.")
    print("=" * 78)


# preflight(ADMISSIBLE, EXCLUSIONS)
# emit(HEADER)
