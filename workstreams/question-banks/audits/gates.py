#!/usr/bin/env python3
"""gates.py — question-banks (P04) audit gates.

Run from repo root:
    python workstreams/question-banks/audits/gates.py <bank.json>

A SEEDED-ERROR SELFTEST runs FIRST (the support-books pattern, CD-025): the instrument is
proven before any bank verdict is believed. If the selftest fails, no verdict is printed.

Gates (QUESTION_BANK_POLICY.md v1.0 §5, LOCAL.md):
  SELFTEST        every check fires on a deliberately broken bank
  POOL-MEMBERSHIP every question in exactly one pool; no orphan qid            (QB-D-001)
  ZERO-OVERLAP    no duplicate/near-duplicate stem or answer across pools      (QB-D-001)
  DOMAIN-RATIO    mark-weighted domain mix: HW/AS enforced per pool, CT reported,
                  chapter total enforced, class band +/-5 points   (QuestionPolicy §৩, QB-D-006)
  MARK-VALUE      per-item marks match the MarkLogic spine slot value          (QuestionPolicy §৬)
  SOURCE-TRACE    every item traces to the chapter's source extraction         (SOURCE_POLICY)
  QUOTE-VERBATIM  every quoted span exists verbatim in the extraction          (KEEP-AS-IS/PROTECTED)
  HONORIFIC       the Prophet's name always carries (স)                        (extraction, বিশেষ নির্দেশ)
  AS-MIX          AS pool is roughly half HW-level, half above                 (QB-D-004)
  SCRIPT-GUARD    LANGUAGE_RULES §7 tiers over rendered strings                (CD-012/CD-018)
  NUMERALS        no ASCII digits in student-facing strings                    (LANGUAGE_RULES §2)
  ANSWER-SHAPE    exactly-one-correct MCQ, non-empty keys, rubric bands == marks
  RUBRIC-SPECIFICITY  no two S08 items share a content rubric
  TOPIC-NUMBER    every topic_tag is a row in canon/topics/TOPIC_NUMBERS.md  (CD-044)
  FLAG-TRACE      every ⚑ flag in the bank resolves in PENDING_PRINCIPAL.md and is not OPEN
  CEILING         balance owed against per-chapter ceilings — REPORT ONLY      (QB-D-002)

Exit 0 = CLEAN, 1 = FAIL. Paste output verbatim per AGENTS.md §5.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

# ---- canon-derived constants (cited, not copied: see the source file for each) ----

# MarkLogic_QuestionPolicy.md §৩ — domain mix by class band, +/-৫ points.
DOMAIN_BANDS = {
    1: {"জ্ঞান": 50, "অনুধাবন": 35, "প্রয়োগ": 15, "উচ্চতর": 0},
    2: {"জ্ঞান": 50, "অনুধাবন": 35, "প্রয়োগ": 15, "উচ্চতর": 0},
    3: {"জ্ঞান": 40, "অনুধাবন": 35, "প্রয়োগ": 20, "উচ্চতর": 5},
    4: {"জ্ঞান": 35, "অনুধাবন": 35, "প্রয়োগ": 20, "উচ্চতর": 10},
    5: {"জ্ঞান": 30, "অনুধাবন": 35, "প্রয়োগ": 25, "উচ্চতর": 10},
}
DOMAIN_TOLERANCE = 5.0

# MarkLogic_QuestionPolicy.md §৩ — Bloom to domain.
BLOOM_DOMAIN = {
    "Remember": "জ্ঞান",
    "Understand": "অনুধাবন",
    "Apply": "প্রয়োগ",
    "Analyze": "উচ্চতর",
    "Evaluate": "উচ্চতর",
    "Create": "উচ্চতর",
}

# MarkLogic_BAN_Spine.md — C5 per-ITEM marks by slot (not slot totals).
SPINE_ITEM_MARKS = {
    ("BAN", 5): {"S01": 10, "S02": 1, "S03": 1, "S04": 1, "S05": 1, "S06": 1,
                 "S07": 2, "S08": 5, "S09": 5, "S10": 1, "S11": 1, "S12": 1,
                 "S13": 1, "S14": 5, "S15": 12},
}

# QUESTION_BANK_POLICY.md §2 (QB-D-002) — per-chapter cumulative ceilings.
CEILINGS = {"HW": 100, "AS": 50, "CT": 30}

# LANGUAGE_RULES.md §7 — codepoint ranges taken from the validator, not restated from memory.
ARABIC = re.compile(r"[؀-ۿݐ-ݿﭐ-﷿ﹰ-﻿]")
ARROWS = re.compile(r"[←-⇿⟰-⟿⤀-⥿]")
EMOJI = re.compile(r"[\U0001F000-\U0001FAFF☀-➿⬀-⯿︀-️]")
WATCH = re.compile(r"[—…]")
ASCII_DIGIT = re.compile(r"[0-9]")

# The extraction's বিশেষ নির্দেশ for পাঠ ২১: the honorific is mandatory everywhere.
# Longest-first: alternation is leftmost-FIRST in Python, so "মহানবি" must precede "নবি"
# or the shorter branch would match inside it. Holes closed after the 2026-08-09 audit:
# bare নবি, হজরত, রসুল, মোহাম্মদ all walked through the original four-branch pattern.
PROPHET = re.compile(r"(মহানবি|মুহাম্মদ|মোহাম্মদ|নবিজি|রাসুল|রসুল|হজরত|নবি)")
HONORIFIC_WINDOW = 30

NEAR_DUP_JACCARD = 0.80
MIN_ANCHOR_TOKENS = 3
MIN_MCQ_OPTIONS = 3


# ---- helpers -------------------------------------------------------------------

def norm(s):
    """Normalise a Bengali string for comparison: NFC, collapse space, drop punctuation."""
    s = unicodedata.normalize("NFC", s or "")
    # Markdown emphasis is presentation, not content — strip it so a verbatim quote from the
    # extraction still matches when the source wraps part of it in ** ** (SOURCE-TRACE finding).
    s = re.sub(r"[‘’“”'\"()\[\]।,;:?!—–\-….*_#>|/·]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def tokens(s):
    return set(norm(s).split())


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def rendered_strings(q):
    """Every string a student or teacher actually reads (LANGUAGE_RULES §7 'rendered text')."""
    out = [q.get("question_text", "")]
    for o in q.get("options", []) or []:
        out += [o.get("text", ""), o.get("why_wrong", "") or ""]
    for b in q.get("blanks", []) or []:
        out += list(b.get("accepted", []) or [])
    for p in q.get("pairs", []) or []:
        out += [p.get("left", ""), p.get("right", "")]
    ak = q.get("answer_key") or {}
    out += list(ak.get("accepted", []) or [])
    if ak.get("model_note"):
        out.append(ak["model_note"])
    for st in ak.get("step_breakdown", []) or []:
        out.append(st.get("step", ""))
    rb = q.get("rubric") or {}
    for c in rb.get("criteria", []) or []:
        out.append(c.get("criterion", ""))
        out += list((c.get("band_descriptors") or {}).values())
    for g in q.get("glossary", []) or []:
        out += [g.get("term", ""), g.get("gloss", "")]
    return [s for s in out if s]


def answer_signature(q):
    """A comparable representation of what the item actually asks the student to produce."""
    qt = q.get("question_type")
    if qt == "mcq":
        return norm(next((o.get("text", "") for o in q.get("options", []) if o.get("is_correct")), ""))
    if qt == "true_false":
        return ""  # a boolean is not a discriminating answer; the stem check does this work
    if qt == "fill_blank":
        return " | ".join(norm((b.get("accepted") or [""])[0]) for b in q.get("blanks", []))
    if qt == "matching":
        return " | ".join(f"{norm(p.get('left'))}={norm(p.get('right'))}" for p in q.get("pairs", []))
    if qt == "short_answer":
        return norm(((q.get("answer_key") or {}).get("accepted") or [""])[0])
    if qt == "descriptive":
        # Descriptive items had NO signature, so all S08 items were exempt from the
        # answer-collision check (2026-08-09 audit). The rubric's content criterion is what
        # an S08 item actually asks for, so that is its signature.
        rb = q.get("rubric") or {}
        return " | ".join(norm(c.get("criterion")) for c in rb.get("criteria", [])
                          if c.get("role") == "content")
    return ""


def chapter_section(text, unit_bn):
    """Slice the extraction down to this chapter (headings are '# পাঠ <number>')."""
    m = re.search(rf"^#\s*পাঠ\s*{re.escape(unit_bn)}\b.*?$", text, re.M)
    if not m:
        return None
    rest = text[m.end():]
    nxt = re.search(r"^#\s*পাঠ\s", rest, re.M)
    return rest[: nxt.start()] if nxt else rest


# ---- gates ---------------------------------------------------------------------

def g_pool_membership(bank, ctx):
    errs = []
    pools = bank.get("pool_index") or {}
    qids = [q.get("qid") for q in bank.get("questions", [])]
    if sorted(pools.keys()) != sorted(CEILINGS.keys()):
        errs.append(f"pool_index keys {sorted(pools.keys())} != the three ruled pools "
                    f"{sorted(CEILINGS.keys())} (QB-D-001: HW/AS/CT, no CW)")
    seen = {}
    for pool, ids in pools.items():
        for qid in ids:
            seen.setdefault(qid, []).append(pool)
    for qid, ps in seen.items():
        if len(ps) > 1:
            errs.append(f"{qid} is in {len(ps)} pools {ps} — a question belongs to exactly one (QB-D-001)")
        if qid not in qids:
            errs.append(f"pool_index lists {qid} but no such question exists in the bank")
    for qid in qids:
        if qid not in seen:
            errs.append(f"{qid} is in no pool — every question must be assigned (QB-D-001)")
    if len(set(qids)) != len(qids):
        errs.append("duplicate qid in the bank — qids are permanent and never reused")
    return errs


def g_zero_overlap(bank, ctx):
    errs = []
    pool_of = ctx["pool_of"]
    qs = bank.get("questions", [])
    for i in range(len(qs)):
        for j in range(i + 1, len(qs)):
            a, b = qs[i], qs[j]
            pa, pb = pool_of.get(a.get("qid")), pool_of.get(b.get("qid"))
            if pa is None or pb is None:
                continue
            where = f"[{pa}] and {b['qid']} [{pb}]" if pa != pb else f"and {b['qid']}, both in [{pa}]"
            sim = jaccard(tokens(a.get("question_text")), tokens(b.get("question_text")))
            if sim >= NEAR_DUP_JACCARD:
                errs.append(f"{a['qid']} {where} have near-identical stems "
                            f"(token overlap {sim:.2f} >= {NEAR_DUP_JACCARD})")
            sa, sb = answer_signature(a), answer_signature(b)
            if sa and sa == sb and a.get("question_type") == b.get("question_type"):
                errs.append(f"{a['qid']} {where} have the identical answer "
                            f"'{sa[:40]}' for the same question_type")
    return errs


def _mix(items, band, errs):
    total = sum(i.get("marks", 0) for i in items)
    got = {d: 0.0 for d in band}
    for it in items:
        dom = BLOOM_DOMAIN.get(it.get("bloom_level"))
        if dom is None:
            errs.append(f"{it.get('qid')}: bloom_level '{it.get('bloom_level')}' maps to no domain")
            continue
        got[dom] += it.get("marks", 0)
    return total, got


def g_domain_ratio(bank, ctx):
    """QB-D-006 — HW and AS enforced per pool; CT REPORTED, not enforced; chapter total enforced.

    The CT carve-out is canon, not convenience: MarkLogic_QuestionPolicy.md §৬ rule ৩ rules that
    a class test's domain ratio is satisfied **across the year's tests combined**, not inside one
    test, because 25 marks cannot seat four domains at ratio. A single chapter's CT pool is that
    same situation, so enforcing the band inside it would contradict the canon rule it claims to
    implement. The chapter total is enforced instead, and that is where the mix has to hold.
    """
    errs = []
    cls = ctx["class_level"]
    band = DOMAIN_BANDS.get(cls)
    if not band:
        return [f"no domain band for class {cls}"]
    pools = bank.get("pool_index") or {}
    for pool in ("HW", "AS", "CT"):
        items = [ctx["by_qid"][q] for q in pools.get(pool, []) if q in ctx["by_qid"]]
        total, got = _mix(items, band, errs)
        if not total:
            continue
        for dom, want in band.items():
            pct = 100.0 * got[dom] / total
            off = abs(pct - want) > DOMAIN_TOLERANCE
            if pool == "CT":
                ctx["report"].append(("DOMAIN-RATIO", f"CT {dom} {pct:.1f}% vs band {want}%"
                                  + ("  <-- outside band, reported not enforced" if off else "")))
            elif off:
                errs.append(f"{pool}: {dom} {pct:.1f}% vs band {want}% "
                            f"(tolerance +/-{DOMAIN_TOLERANCE:.0f}) — QuestionPolicy §৩")
    allitems = [ctx["by_qid"][q] for ids in pools.values() for q in ids if q in ctx["by_qid"]]
    total, got = _mix(allitems, band, errs)
    if total:
        for dom, want in band.items():
            pct = 100.0 * got[dom] / total
            if abs(pct - want) > DOMAIN_TOLERANCE:
                errs.append(f"CHAPTER TOTAL: {dom} {pct:.1f}% vs band {want}% "
                            f"(tolerance +/-{DOMAIN_TOLERANCE:.0f}) — QuestionPolicy §৩")
    return errs


def g_mark_value(bank, ctx):
    errs = []
    key = (ctx["subject"], ctx["class_level"])
    table = SPINE_ITEM_MARKS.get(key)
    if not table:
        return [f"no spine per-item mark table vendored for {key} — add it from the spine before authoring"]
    slots = bank.get("slot_index") or {}
    for q in bank.get("questions", []):
        qid = q.get("qid")
        slot = slots.get(qid)
        if not slot:
            errs.append(f"{qid}: no slot_index entry — every item names its MarkLogic slot")
            continue
        if slot not in table:
            errs.append(f"{qid}: slot '{slot}' is not in the {key[0]} C{key[1]} spine")
            continue
        per_item = table[slot]
        if q.get("question_type") == "fill_blank":
            blanks = q.get("blanks", [])
            for b in blanks:
                if b.get("marks") != per_item:
                    errs.append(f"{qid}: blank {b.get('blank_no')} carries {b.get('marks')} "
                                f"but spine {slot} is {per_item} per item")
            if q.get("marks") != per_item * len(blanks):
                errs.append(f"{qid}: marks {q.get('marks')} != {len(blanks)} blanks x {per_item}")
        elif q.get("marks") != per_item:
            errs.append(f"{qid}: marks {q.get('marks')} != spine {slot} per-item value {per_item} "
                        f"(QuestionPolicy §৬ — CT lifts annual questions at unchanged marks)")
    return errs


def g_source_trace(bank, ctx):
    """SOURCE_POLICY §1 — content comes only from the extraction.

    Hardened after the 2026-08-09 audit, which showed the original check was vacuous: it only
    asked whether the anchor string appeared anywhere in the chapter, so a two-character word
    like "না" satisfied it and the anchor was never tied to the question it supposedly sourced.
    An anchor must now be a real span (3+ tokens), must appear in the chapter, and must SHARE
    vocabulary with the item — otherwise it is decoration, not provenance.
    """
    errs = []
    src = ctx["source_text"]
    idx = bank.get("source_index") or {}
    nsrc = norm(src) if src is not None else None
    for q in bank.get("questions", []):
        qid = q.get("qid")
        ref = idx.get(qid)
        if not ref:
            errs.append(f"{qid}: no source_index entry — content comes only from the extraction "
                        f"(SOURCE_POLICY §1); no extraction reference, no question")
            continue
        atoks = [t for t in norm(ref).split() if len(t) >= 3]
        if len(norm(ref).split()) < MIN_ANCHOR_TOKENS:
            errs.append(f"{qid}: source_index anchor '{ref}' is only "
                        f"{len(norm(ref).split())} token(s) — an anchor must be a real span of at "
                        f"least {MIN_ANCHOR_TOKENS}, or it proves nothing")
            continue
        if nsrc is not None and norm(ref) not in nsrc:
            errs.append(f"{qid}: source_index anchor '{ref[:50]}' does not appear in the extraction")
            continue
        itoks = {t for s_ in rendered_strings(q) for t in norm(s_).split() if len(t) >= 3}
        shared = set(atoks) & itoks
        if not (any(len(t) >= 4 for t in shared) or len(shared) >= 2):
            errs.append(f"{qid}: source_index anchor '{ref[:50]}' shares no substantive word with "
                        f"the item — the anchor is not tied to the question it claims to source")
    return errs


def g_answer_shape(bank, ctx):
    """Added after the 2026-08-09 audit: no gate looked at the answer carrier at all, so an MCQ
    with two correct options, or none, sailed through. The LOCKED schema expresses the
    exactly-one-correct rule, but the schema only runs at export — this catches it at authoring.
    """
    errs = []
    for q in bank.get("questions", []):
        qid, qt = q.get("qid"), q.get("question_type")
        if qt == "mcq":
            opts = q.get("options") or []
            n = sum(1 for o in opts if o.get("is_correct"))
            if n != 1:
                errs.append(f"{qid}: {n} correct option(s) — an MCQ has exactly one")
            if len(opts) < MIN_MCQ_OPTIONS:
                errs.append(f"{qid}: {len(opts)} options — at least {MIN_MCQ_OPTIONS} required")
            ids = [o.get("option_id") for o in opts]
            if len(set(ids)) != len(ids):
                errs.append(f"{qid}: duplicate option_id {ids}")
            for o in opts:
                if not o.get("is_correct") and not (o.get("why_wrong") or "").strip():
                    errs.append(f"{qid}: distractor '{o.get('option_id')}' has no why_wrong")
            if len({norm(o.get("text")) for o in opts}) != len(opts):
                errs.append(f"{qid}: two options carry the same text")
        elif qt == "short_answer":
            if not ((q.get("answer_key") or {}).get("accepted") or []):
                errs.append(f"{qid}: short_answer with an empty answer key")
        elif qt == "fill_blank":
            for b in q.get("blanks") or []:
                if not (b.get("accepted") or []):
                    errs.append(f"{qid}: blank {b.get('blank_no')} has no accepted answer")
        elif qt == "descriptive":
            rb = q.get("rubric") or {}
            bands = rb.get("bands") or []
            if len(bands) != q.get("marks"):
                errs.append(f"{qid}: rubric has {len(bands)} bands for a {q.get('marks')}-mark "
                            f"item — a marker cannot turn bands into a mark unless they "
                            f"correspond one-to-one")
    return errs


def g_rubric_specificity(bank, ctx):
    """Added after the 2026-08-09 audit, which found all eight S08 rubrics byte-identical and the
    recall descriptor ("পাঠ থেকে পাঁচটি আলাদা কথা") applied unchanged to opinion prompts."""
    errs = []
    seen = {}
    for q in bank.get("questions", []):
        if q.get("question_type") != "descriptive":
            continue
        rb = q.get("rubric") or {}
        content = [c for c in rb.get("criteria", []) if c.get("role") == "content"]
        if not content:
            errs.append(f"{q.get('qid')}: rubric has no content criterion")
            continue
        sig = norm(json.dumps([c.get("band_descriptors") for c in content],
                              ensure_ascii=False, sort_keys=True))
        if sig in seen:
            errs.append(f"{q.get('qid')}: content rubric is identical to {seen[sig]} — a rubric "
                        f"that fits every question grades none of them")
        else:
            seen[sig] = q.get("qid")
    return errs


def g_topic_number(bank, ctx):
    """canon/topics/TOPIC_NUMBERS.md — a number not in the chart is not used, it is queued.

    This gate exists because a wrong topic_tag survived a full gate chain AND a promotion: nothing
    checked the number against anything, because until CD-043 there was nothing to check it against
    (QB-CR-008, PENDING-P-007). The chart is now canon, so the check is now possible.
    """
    errs = []
    chart = ROOT / "canon" / "topics" / "TOPIC_NUMBERS.md"
    if not chart.exists():
        return ["canon/topics/TOPIC_NUMBERS.md is missing — no topic number can be validated"]
    text = chart.read_text(encoding="utf-8")
    # A tag counts as charted only where it heads a table row: "| `TOP-…` | meaning | slug | attestation |"
    charted = set(re.findall(r"^\|\s*\*{0,2}`(TOP-[A-Z]+-C[1-5]-\d{2})`", text, re.M))
    if not charted:
        return ["canon/topics/TOPIC_NUMBERS.md has no parseable rows"]
    for q in bank.get("questions", []):
        tag = q.get("topic_tag")
        if tag and tag not in charted:
            errs.append(f"{q.get('qid')}: topic_tag '{tag}' is not a row in "
                        f"canon/topics/TOPIC_NUMBERS.md — an unattested number is queued, not used")
    return errs


def g_flag_trace(bank, ctx):
    """QB-D-009 / CD-042 — a bank may be promoted carrying a FLAGGED tag, but only if the flag is
    real: it must name a tag that resolves in PENDING_PRINCIPAL.md, and that row must not be OPEN
    (an OPEN row blocks promotion outright, AGENTS.md §6). A flag pointing at nothing is worse
    than no flag, because it looks like the uncertainty has been handled.
    """
    errs = []
    flags = bank.get("flags") or []
    # The selftest injects a synthetic queue. Reading the live file in a seeded case made the
    # instrument depend on repo state that changes every session: the OPEN-path case named a real
    # OPEN row, the Principal ruled it, and the selftest went red on the next run — not because
    # the gate broke, but because the fixture was the live world. A test fixture must be a fixture.
    text = bank.get("_selftest_queue")
    if text is None:
        queue = ROOT / "PENDING_PRINCIPAL.md"
        text = queue.read_text(encoding="utf-8") if queue.exists() else ""
    for f in flags:
        tag = f.get("tag")
        if not tag:
            errs.append("a flag entry carries no tag")
            continue
        rows = [ln for ln in text.splitlines() if ln.startswith(f"| {tag} |")]
        if not rows:
            errs.append(f"flag {tag} does not resolve to a row in PENDING_PRINCIPAL.md")
            continue
        # Read the STATUS cell (last non-empty cell), not the whole row: a question or default
        # cell may legitimately contain the word. And match the word, not the literal "**OPEN**"
        # — the first version of this check looked for "**OPEN**" and so sailed straight past a
        # row reading "**OPEN — Principal-owed.**". It passed a bank it was written to stop.
        cells = [c.strip() for c in rows[0].strip().strip("|").split("|")]
        status = cells[-1] if cells else ""
        if re.search(r"\bOPEN\b", status):
            errs.append(f"flag {tag} is OPEN (Principal-owed) — an OPEN row blocks promotion "
                        f"(AGENTS.md §6, CD-042); it cannot ride along in a promoted bank")
        for key in ("status", "scope", "what", "closes_on"):
            if not (f.get(key) or "").strip():
                errs.append(f"flag {tag} has no '{key}' — a flag a reader cannot act on is decoration")
    return errs


def g_quote_verbatim(bank, ctx):
    """KEEP-AS-IS / PROTECTED: a quoted span must exist verbatim in the extraction."""
    errs = []
    src = ctx["source_text"]
    if src is None:
        return errs
    nsrc = norm(src)
    for q in bank.get("questions", []):
        for s in rendered_strings(q):
            for span in re.findall(r"[‘“]([^’”]{15,})[’”]", s):
                if norm(span) not in nsrc:
                    errs.append(f"{q.get('qid')}: quoted span '{span[:45]}…' is not verbatim in the "
                                f"extraction — this পাঠ is KEEP-AS-IS and PROTECTED")
    return errs


def g_honorific(bank, ctx):
    errs = []
    for q in bank.get("questions", []):
        for s in rendered_strings(q):
            for m in PROPHET.finditer(s):
                window = s[m.end(): m.end() + HONORIFIC_WINDOW]
                if "(স)" not in window:
                    errs.append(f"{q.get('qid')}: '{m.group(1)}' without (স) within "
                                f"{HONORIFIC_WINDOW} characters — the extraction's বিশেষ নির্দেশ "
                                f"makes the honorific mandatory everywhere")
    return errs


def g_as_mix(bank, ctx):
    """QB-D-004 — AS is roughly half HW-level, half above."""
    ids = (bank.get("pool_index") or {}).get("AS", [])
    items = [ctx["by_qid"][q] for q in ids if q in ctx["by_qid"]]
    if not items:
        return []
    higher = [i for i in items
              if BLOOM_DOMAIN.get(i.get("bloom_level")) in ("প্রয়োগ", "উচ্চতর")
              or i.get("difficulty") == "hard"]
    pct = 100.0 * len(higher) / len(items)
    if not 35.0 <= pct <= 65.0:
        return [f"AS pool is {pct:.0f}% above HW level ({len(higher)}/{len(items)}) — QB-D-004 wants "
                f"roughly half, i.e. 35–65%"]
    return []


def g_script_guard(bank, ctx):
    errs = []
    for q in bank.get("questions", []):
        for s in rendered_strings(q):
            if ARABIC.search(s):
                errs.append(f"{q.get('qid')}: Arabic script in rendered text — tier 1 RED anywhere "
                            f"(LANGUAGE_RULES §7 / CD-014). Use (স), never the Arabic glyph")
            if ARROWS.search(s) or EMOJI.search(s):
                errs.append(f"{q.get('qid')}: arrow/emoji/symbol glyph in rendered text — tier 2 RED "
                            f"(LANGUAGE_RULES §7)")
            ctx["watch"] += len(WATCH.findall(s))
    return errs


def g_numerals(bank, ctx):
    errs = []
    for q in bank.get("questions", []):
        for s in rendered_strings(q):
            if ASCII_DIGIT.search(s):
                errs.append(f"{q.get('qid')}: ASCII digit in a student-facing string "
                            f"('{s[:40]}…') — Bengali numerals only (LANGUAGE_RULES §2)")
    return errs


def g_ceiling(bank, ctx):
    """REPORT ONLY — being under ceiling is never a failure (QB-D-002)."""
    errs = []
    for pool, cap in CEILINGS.items():
        have = len((bank.get("pool_index") or {}).get(pool, []))
        ctx["report"].append(("CEILING", f"{pool}: {have}/{cap} authored, {max(0, cap - have)} owed to ceiling"))
        if have > cap:
            errs.append(f"{pool} holds {have} items, above the ceiling of {cap} (QB-D-002)")
    return errs


GATES = [
    ("POOL-MEMBERSHIP", g_pool_membership),
    ("ZERO-OVERLAP", g_zero_overlap),
    ("DOMAIN-RATIO", g_domain_ratio),
    ("MARK-VALUE", g_mark_value),
    ("SOURCE-TRACE", g_source_trace),
    ("ANSWER-SHAPE", g_answer_shape),
    ("RUBRIC-SPECIFICITY", g_rubric_specificity),
    ("TOPIC-NUMBER", g_topic_number),
    ("FLAG-TRACE", g_flag_trace),
    ("QUOTE-VERBATIM", g_quote_verbatim),
    ("HONORIFIC", g_honorific),
    ("AS-MIX", g_as_mix),
    ("SCRIPT-GUARD", g_script_guard),
    ("NUMERALS", g_numerals),
    ("CEILING", g_ceiling),
]


# ---- runner --------------------------------------------------------------------

def build_ctx(bank):
    by_qid = {q.get("qid"): q for q in bank.get("questions", [])}
    pool_of = {}
    for pool, ids in (bank.get("pool_index") or {}).items():
        for qid in ids:
            pool_of[qid] = pool
    subject, class_level, unit = "?", 0, "?"
    for qid in by_qid:
        m = re.match(r"^QP-([A-Z]+)-C([1-5])-U(\d+)", qid or "")
        if m:
            subject, class_level, unit = m.group(1), int(m.group(2)), m.group(3)
            break
    src_text = None
    ref = bank.get("source_extraction")
    if ref:
        path = ROOT / ref.split("#")[0]
        if path.exists():
            full = path.read_text(encoding="utf-8")
            unit_bn = str(int(unit)).translate(str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯"))
            src_text = chapter_section(full, unit_bn) or full
    return {"by_qid": by_qid, "pool_of": pool_of, "subject": subject,
            "class_level": class_level, "unit": unit, "source_text": src_text,
            "watch": 0, "report": []}


def run(bank, quiet=False):
    ctx = build_ctx(bank)
    fails = []
    for name, fn in GATES:
        errs = fn(bank, ctx)
        if not quiet:
            print(f"  {'FAIL' if errs else 'PASS'}  {name}"
                  + "".join(f"\n        - {e}" for e in errs))
        fails += [(name, e) for e in errs]
    return fails, ctx


# ---- seeded-error selftest (runs FIRST, CD-025) ---------------------------------

SELFTEST_ANCHOR = "আরাফাতের ময়দানে মহানবি (স) ভাষণ দিলেন"
BN_DIGITS = str.maketrans("0123456789", "০১২৩৪৫৬৭৮৯")


def bn(n):
    return str(n).translate(BN_DIGITS)

def _good_bank():
    """A synthetic bank that must be CLEAN: 3 pools x 20 one-mark items, each pool split
    6/7/5/2 = exactly the C5 band 30/35/25/10. Stems are unique so ZERO-OVERLAP stays quiet.
    It points at the REAL extraction so SOURCE-TRACE and QUOTE-VERBATIM are exercised."""
    blooms = ["Remember"] * 6 + ["Understand"] * 7 + ["Apply"] * 5 + ["Analyze"] * 2
    pools, qs, slots, srcs, n = {}, [], {}, {}, 0
    for pool in ("HW", "AS", "CT"):
        pools[pool] = []
        for k, bloom in enumerate(blooms):
            n += 1
            qid = f"QP-BAN-C5-U21-Q{n:02d}"
            # AS carries hard difficulty on three Understand items -> AS-MIX lands near half.
            diff = "hard" if (pool == "AS" and bloom == "Understand" and k < 9) else "easy"
            qs.append({"qid": qid, "topic_tag": "TOP-BAN-C5-07",
                       "ref19_topic_id": "BAN-INFOTEXT",
                       "question_text": f"সেলফটেস্ট নমুনা ভাষণ প্রশ্ন ক্রমিক {bn(n)} কোনটি",
                       "question_type": "mcq", "paper_role": "mcq", "bloom_level": bloom,
                       "difficulty": diff, "tier": "tier1", "marks": 1,
                       "options": [{"option_id": "ক", "text": f"সঠিক বিকল্প {bn(n)}", "is_correct": True},
                                   {"option_id": "খ", "text": f"ভুল বিকল্প {bn(n)}", "is_correct": False,
                                    "why_wrong": "পাঠে এই কথা নেই"},
                                   {"option_id": "গ", "text": f"অন্য ভুল বিকল্প {bn(n)}",
                                    "is_correct": False, "why_wrong": "পাঠে এই কথাও নেই"}]})
            pools[pool].append(qid)
            slots[qid] = "S05"
            srcs[qid] = SELFTEST_ANCHOR
    return {"schema_version": "1.0", "bank_id": "SELFTEST",
            "source_extraction": "canon/marklogic/C5_Bangla_Source_13-23.md",
            "pool_index": pools, "slot_index": slots, "source_index": srcs, "questions": qs}


def _twin_rubrics(b):
    """Two descriptive items carrying a byte-identical content rubric."""
    rb = {"bands": ["৫", "৪", "৩", "২", "১"],
          "criteria": [{"role": "content", "criterion": "সব প্রশ্নে খাটে এমন একটি মানদণ্ড",
                        "band_descriptors": {x: "একই বর্ণনা" for x in ["৫", "৪", "৩", "২", "১"]}},
                       {"role": "islamic_alignment", "criterion": "সংগতি",
                        "band_descriptors": {x: "একই বর্ণনা" for x in ["৫", "৪", "৩", "২", "১"]}}]}
    for k, pool in enumerate(("HW", "AS")):
        qid = f"QP-BAN-C5-U21-Q9{k}"
        b["questions"].append({"qid": qid, "topic_tag": "TOP-BAN-C5-07",
                               "ref19_topic_id": "BAN-INFOTEXT",
                               "question_text": f"সেলফটেস্ট ভাষণ বিস্তৃত প্রশ্ন {bn(k)}",
                               "question_type": "descriptive", "paper_role": "structured",
                               "bloom_level": "Evaluate", "difficulty": "hard", "tier": "tier1",
                               "marks": 5, "rubric": json.loads(json.dumps(rb))})
        b["pool_index"][pool].append(qid)
        b["slot_index"][qid] = "S08"
        b["source_index"][qid] = SELFTEST_ANCHOR


def _mutate(fn):
    b = json.loads(json.dumps(_good_bank()))
    fn(b)
    return b


def selftest():
    """Every gate must fire on a bank broken specifically for it."""
    import copy  # noqa: F401
    cases = []

    def add(gate, label, fn, expect=None):
        cases.append((gate, label, _mutate(fn), expect))

    add("POOL-MEMBERSHIP", "question in two pools",
        lambda b: b["pool_index"]["CT"].append("QP-BAN-C5-U21-Q01"))
    add("POOL-MEMBERSHIP", "a CW pool reappears",
        lambda b: b["pool_index"].update({"CW": []}))
    add("ZERO-OVERLAP", "same stem in HW and CT",
        lambda b: b["questions"][-1].update({"question_text": b["questions"][0]["question_text"]}))
    add("ZERO-OVERLAP", "exact duplicate INSIDE the HW pool",
        lambda b: b["questions"][2].update({"question_text": b["questions"][0]["question_text"]}))
    add("ANSWER-SHAPE", "an MCQ with two correct options",
        lambda b: b["questions"][0]["options"][1].update({"is_correct": True}))
    add("ANSWER-SHAPE", "an MCQ with no correct option",
        lambda b: b["questions"][0]["options"][0].update({"is_correct": False}))
    add("ANSWER-SHAPE", "a distractor with no why_wrong",
        lambda b: b["questions"][0]["options"][1].pop("why_wrong"))
    add("SOURCE-TRACE", "a one-word anchor that matches anything",
        lambda b: b["source_index"].update({"QP-BAN-C5-U21-Q01": "না"}))
    add("SOURCE-TRACE", "a real span that has nothing to do with the item",
        lambda b: b["source_index"].update({"QP-BAN-C5-U21-Q01": "জিলকদ মাসের শেষে"}))
    add("HONORIFIC", "bare নবি with no (স)",
        lambda b: b["questions"][0].update({"question_text": "নবি সাহেব কোথায় ভাষণ দেন"}))
    add("HONORIFIC", "হজরত with no (স)",
        lambda b: b["questions"][0].update({"question_text": "হজরত মুহাম্মদ কোথায় ভাষণ দেন"}))
    add("RUBRIC-SPECIFICITY", "two S08 items sharing one rubric", _twin_rubrics)
    add("TOPIC-NUMBER", "a topic_tag that is in no chart row",
        lambda b: b["questions"][0].update({"topic_tag": "TOP-BAN-C5-99"}))
    add("FLAG-TRACE", "a flag pointing at a tag that does not exist",
        lambda b: b.update({"flags": [{"tag": "PENDING-P-999", "status": "FLAGGED",
                                       "scope": "x", "what": "y", "closes_on": "z"}]}))
    add("FLAG-TRACE", "a flag naming a row that is OPEN (Principal-owed)",
        lambda b: b.update({
            "flags": [{"tag": "PENDING-P-XXX", "status": "OPEN",
                       "scope": "x", "what": "y", "closes_on": "z"}],
            "_selftest_queue": "| PENDING-P-XXX | d | w | q | def | by | **OPEN** — synthetic |"}))

    add("FLAG-TRACE", "a flag with no closes_on",
        lambda b: b.update({"flags": [{"tag": "PENDING-P-005", "status": "FLAGGED",
                                       "scope": "x", "what": "y", "closes_on": ""}]}))
    add("DOMAIN-RATIO", "every HW item becomes জ্ঞান",
        lambda b: [q.update({"bloom_level": "Remember"})
                   for q in b["questions"] if q["qid"] in b["pool_index"]["HW"]])
    add("DOMAIN-RATIO", "chapter total goes all-উচ্চতর",
        lambda b: [q.update({"bloom_level": "Create"}) for q in b["questions"]],
        expect="CHAPTER TOTAL")
    add("MARK-VALUE", "MCQ carries 5 marks",
        lambda b: b["questions"][0].update({"marks": 5}))
    add("SOURCE-TRACE", "an item with no extraction anchor",
        lambda b: b["source_index"].pop("QP-BAN-C5-U21-Q01"))
    add("QUOTE-VERBATIM", "an invented quotation",
        lambda b: b["questions"][0].update(
            {"question_text": "‘এই বাক্যটি পাঠে কোথাও নেই একেবারেই’ কে বলেছেন"}))
    add("HONORIFIC", "the Prophet's name without (স)",
        lambda b: b["questions"][0].update({"question_text": "মহানবি কোথায় ভাষণ দেন"}))
    add("AS-MIX", "AS is entirely recall",
        lambda b: [q.update({"bloom_level": "Remember", "difficulty": "easy"})
                   for q in b["questions"] if q["qid"] in b["pool_index"]["AS"]])
    add("SCRIPT-GUARD", "Arabic script in a stem",
        lambda b: b["questions"][0].update({"question_text": "بسم কী অর্থ"}))
    add("SCRIPT-GUARD", "an arrow in a stem",
        lambda b: b["questions"][0].update({"question_text": "মক্কা → মদিনা কোনটি"}))
    add("NUMERALS", "an ASCII digit in a stem",
        lambda b: b["questions"][0].update({"question_text": "10 হিজরিতে কী হয়েছিল"}))
    add("CEILING", "HW above its ceiling",
        lambda b: b["pool_index"].update({"HW": [f"QP-BAN-C5-U21-Q{n:02d}" for n in range(1, 102)]}))

    print("SELFTEST — the instrument is proven before any bank verdict (CD-025)")
    ok = True

    # Negative case: a FLAGGED row is promotable (CD-042) and must NOT trip FLAG-TRACE.
    # A gate that fires on everything is as useless as one that fires on nothing.
    neg = _mutate(lambda b: b.update({
        "flags": [{"tag": "PENDING-P-XXX", "status": "FLAGGED",
                   "scope": "x", "what": "y", "closes_on": "z"}],
        "_selftest_queue": "| PENDING-P-XXX | d | w | q | def | by | **FLAGGED** — synthetic |"}))
    if any(g == "FLAG-TRACE" for g, _ in run(neg, quiet=True)[0]):
        print("  FAIL  FLAG-TRACE fires on a FLAGGED row — it must not; FLAGGED is promotable")
        ok = False
    else:
        print("  PASS  FLAG-TRACE stays quiet on a FLAGGED row (CD-042: FLAGGED is promotable)")

    clean, _ = run(_good_bank(), quiet=True)
    if clean:
        print(f"  FAIL  baseline: the good bank is not clean -> {clean}")
        ok = False
    else:
        print("  PASS  baseline: an unbroken bank is CLEAN")

    for gate, label, broken, expect in cases:
        fails, _ = run(broken, quiet=True)
        fired = {g for g, _ in fails}
        hit = gate in fired and (expect is None
                                 or any(expect in m for g, m in fails if g == gate))
        if hit:
            print(f"  PASS  {gate:<16} fires on: {label}")
        else:
            print(f"  FAIL  {gate:<16} DID NOT FIRE on: {label}")
            ok = False

    print(f"SELFTEST RESULT: {'PASS' if ok else 'FAIL'} ({len(cases)} seeded errors + 1 baseline)")
    return ok


def main():
    if not selftest():
        print("\nRESULT: FAIL (selftest red — no bank verdict is believable, nothing was judged)")
        sys.exit(1)
    if len(sys.argv) < 2:
        print("\nusage: gates.py <bank.json>   (selftest above ran clean)")
        sys.exit(0)
    path = Path(sys.argv[1])
    bank = json.loads(path.read_text(encoding="utf-8"))
    print(f"\nBANK: {path}")
    fails, ctx = run(bank)
    for gate, line in ctx["report"]:
        print(f"  REPORT  {gate:<14} {line}")
    print(f"  REPORT  {'SCRIPT-GUARD':<14} tier-3 WATCH counter (em-dash/ellipsis): {ctx['watch']}")
    print(f"RESULT: {'FAIL' if fails else 'CLEAN'} ({len(fails)} failures)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
