#!/usr/bin/env python3
"""
validator_v2_rebuilt.py — Support-Book validator, verified REBUILD of the lost v2.
================================================================================
Provenance: v2-original was executed in the SB-P Production build chats (July 2026)
and never exported; this rebuild is written from the documented spec — README §6
(checks 1–10 + seeded-error requirement), SCHEMA_support-book_v1.md §6 (letter-audit
algorithm) and §7 (check↔field map, red/grey tiers), D-004/D-008/D-009/D-011 — and
carries the two v2 fixes known from production:
  (a) multi-codepoint বর্ণ ড়/ঢ়/য় are normalised to precomposed form (placeholder
      substitution) BEFORE character scanning, so decomposed ড+়  etc. do not
      false-positive as untaught nukta;
  (b) NCTB cloze/blank markers (underscore runs, slash) are allowed punctuation
      in text, so fill-in blocks do not false-positive on the script guard.
Empirical scope note (from the merged পাঠ 1–14 snapshot that PASSED v2 at merge):
metadata fields (notes, compliance_note, scene_description, style_profile,
version_log) legitimately contain →/⚠/🔒, so check 8 RED applies to RENDERED text
fields only (text_bn, text_en, titles); metadata gets GREY reporting. Arabic script
is RED anywhere (D-011 absolute). Em-dash/ellipsis occurrences are counted and
reported for the pending CD-008 cross-check ruling, not red-failed here.

Usage:
  python validator_v2_rebuilt.py <book.json> <letter_inventory.json>   # validate
  python validator_v2_rebuilt.py --selftest <letter_inventory.json>    # seeded errors

Exit 0 = no red. Exit 1 = red (or selftest failure). Paste output verbatim (§5).
"""
import json
import re
import sys
import unicodedata

# ---------------- shared character machinery ----------------
HASANTA = "্"
ZW = {"‌", "‍"}
KAR_SET = set("ািীুূৃেৈোৌ")
SPECIAL_MARKS = set("ংঃঁ")
NUKTA = "়"
# v2 fix (a): decomposed -> precomposed placeholder substitution
PRECOMP = [("ড়", "ড়"), ("ঢ়", "ঢ়"), ("য়", "য়")]
# v2 fix (b): cloze markers _ and / allowed; plus standard punctuation
ALLOWED_PUNCT = (set(" \n\t।,.?!-—…‘’“”()৷॥:;·_/") |
                 set("০১২৩৪৫৬৭৮৯0123456789"))

ARABIC_RANGES = [(0x0600, 0x06FF), (0x0750, 0x077F), (0xFB50, 0xFDFF), (0xFE70, 0xFEFF)]
ARROW_RANGES = [(0x2190, 0x21FF), (0x27F0, 0x27FF), (0x2900, 0x297F)]
EMOJI_RANGES = [(0x1F000, 0x1FAFF), (0x2600, 0x27BF), (0x2B00, 0x2BFF), (0xFE00, 0xFE0F)]
RENDERED_LESSON_TEXT_KEYS = {"text_bn", "text_en"}
RENDERED_TOP_KEYS = {"title_bn"}
WATCH_FOR_CD008 = {"—": "em-dash", "…": "ellipsis"}

def _in(cp, ranges):
    return any(a <= cp <= b for a, b in ranges)

def precompose(text):
    for seq, one in PRECOMP:
        text = text.replace(seq, one)
    return text

# ---------------- report plumbing ----------------
class Report:
    def __init__(self):
        self.red, self.grey, self.passed, self.lines = 0, 0, 0, []
    def r(self, msg):
        self.red += 1
        self.lines.append(f"  [RED]  {msg}")
    def g(self, msg):
        self.grey += 1
        self.lines.append(f"  [GREY] {msg}")
    def p(self, msg):
        self.passed += 1
        self.lines.append(f"  [PASS] {msg}")
    def i(self, msg):
        self.lines.append(f"  [INFO] {msg}")
    def section(self, title):
        self.lines.append("")
        self.lines.append(title)

# ---------------- letter audit (check 4) ----------------
def cumulative_allowed(inv, lesson_no):
    L = inv["lessons"][str(lesson_no)]
    borno = {precompose(b) for b in L["cumulative_borno"]}
    kar = set(L["cumulative_kar"])
    glyphs = (L.get("conjunct_whitelist") or {}).get("glyphs") or []  # null -> none (B-1)
    conj = {precompose(c) for c in glyphs}
    return borno, kar, conj

def audit_text(text, lesson_no, inv):
    borno, kar, conj = cumulative_allowed(inv, lesson_no)
    text = precompose(text)  # v2 fix (a)
    allowed = borno | kar | SPECIAL_MARKS | ZW | ALLOWED_PUNCT | {HASANTA}
    v = []
    for idx, ch in enumerate(text):
        if ch == HASANTA:
            left = precompose(text[idx - 1]) if idx > 0 else ""
            right = precompose(text[idx + 1]) if idx + 1 < len(text) else ""
            cluster = f"{left}{HASANTA}{right}"
            if cluster not in conj:
                v.append({"type": "conjunct_not_whitelisted", "unit": cluster,
                          "detail": f"যুক্তবর্ণ not on পাঠ {lesson_no} whitelist (B-1)"})
    for ch in text:
        if ch in ZW or ch == HASANTA or ch in allowed:
            continue
        if ch == NUKTA:
            v.append({"type": "stray_nukta", "unit": repr(ch),
                      "detail": "nukta on unexpected base (not ড়/ঢ়/য়)"})
        elif "ঀ" <= ch <= "৿":
            kind = "kar_not_taught" if ch in KAR_SET else "borno_not_taught"
            v.append({"type": kind, "unit": ch,
                      "detail": f"not taught up to পাঠ {lesson_no}"})
        else:
            v.append({"type": "out_of_script", "unit": repr(ch),
                      "detail": "outside Bengali+allowed set"})
    return v

def letter_audit_applies(block, lesson):
    if block.get("oral") is True:
        return False
    if block.get("source") == "nctb" and not block.get("edited"):
        return False  # NCTB-original protected
    # README §6.4: every field in a replace পাঠ; every edited:true field otherwise
    return bool(block.get("edited")) or lesson.get("action") == "replace"

# ---------------- script guard (check 8) ----------------
def guard_scan(text):
    """Return (red_hits, grey_hits, cd008_hits) for one string."""
    reds, greys, watch = {}, {}, {}
    for ch in text:
        cp = ord(ch)
        if ch in WATCH_FOR_CD008:
            watch[ch] = watch.get(ch, 0) + 1
            continue
        if _in(cp, ARABIC_RANGES):
            reds[ch] = reds.get(ch, 0) + 1
        elif _in(cp, ARROW_RANGES) or _in(cp, EMOJI_RANGES):
            greys[ch] = greys.get(ch, 0) + 1
    return reds, greys, watch

def iter_strings(obj, path=""):
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, val in obj.items():
            yield from iter_strings(val, f"{path}.{k}" if path else k)
    elif isinstance(obj, list):
        for j, val in enumerate(obj):
            yield from iter_strings(val, f"{path}[{j}]")

# v2 fix (production, 2026-07-18): instruction-phrases only — descriptive animal
# stripes ("striped tiger", "clear stripes") are NOT stripe language.
STRIPE_FORBIDDEN = ["white stripe", "compliance stripe", "stripe band", "add a stripe",
                    "apply a stripe", "white band", "white bar", "blank band",
                    "সাদা দাগ", "censor"]

VALID_ACTIONS = {"retain", "retain-curated", "replace"}
VALID_BW = {"native_safe", "redesigned", "print_only_omit"}

# ---------------- the ten checks ----------------
def validate(book, inv, rep):
    lessons = book.get("lessons", [])
    is_c12_ban = book.get("class") in (1, 2) and book.get("subject") == "BAN"

    rep.section("CHECK 1 — JSON valid · schema_version · book_id")
    rep.p("book parses as valid JSON")
    if book.get("schema_version") == "1.0":
        rep.p('schema_version == "1.0"')
    else:
        rep.r(f"schema_version {book.get('schema_version')!r} != '1.0'")
    if re.fullmatch(r"C\d{1,2}-[A-Z]{3}", book.get("book_id", "")):
        rep.p(f"book_id {book['book_id']!r} well-formed")
    else:
        rep.r(f"book_id {book.get('book_id')!r} malformed")

    rep.section("CHECK 2 — Lesson inventory & action flags")
    nos = [l.get("lesson_no") for l in lessons]
    expect = list(range(1, len(lessons) + 1))
    if nos == expect:
        rep.p(f"lesson_no 1..{len(lessons)} complete, ordered, no gaps")
    else:
        rep.r(f"lesson_no sequence broken: {nos[:10]}... expected 1..{len(lessons)}")
    for l in lessons:
        a = l.get("action")
        if a not in VALID_ACTIONS:
            rep.r(f"L{l.get('lesson_no')}: action {a!r} invalid")
        if book.get("mode") == "C" and a == "replace":
            rep.r(f"L{l.get('lesson_no')}: Mode-C book contains 'replace' (D-005)")
    if all(l.get("action") in VALID_ACTIONS for l in lessons):
        rep.p("every lesson carries exactly one valid action flag")

    rep.section("CHECK 3 — যোগ্যতা/শিখনফল codes present per lesson")
    bad = [l["lesson_no"] for l in lessons
           if not l.get("competency_codes") or not l.get("outcome_codes")]
    if bad:
        for n in bad:
            rep.r(f"L{n}: empty competency/outcome codes")
    else:
        rep.p("codes non-empty on all lessons (MOTOR sentinel counts)")

    rep.section("CHECK 4 — Letter audit (C1–2 BAN school decodable text; v2 fixes active)")
    if not is_c12_ban:
        rep.i("book is not C1–2 BAN — letter audit skipped by design (D-004)")
    else:
        hits = 0
        for l in lessons:
            for b in l.get("blocks", []):
                if not letter_audit_applies(b, l):
                    continue
                for v in audit_text(b.get("text_bn") or "", l["lesson_no"], inv):
                    hits += 1
                    rep.r(f"L{l['lesson_no']}/{b.get('id')}: {v['type']} {v['unit']} — {v['detail']}")
        if hits == 0:
            rep.p("letter audit clean on all school decodable text")

    rep.section("CHECK 5 — Genre tag on every replace lesson")
    bad = [l["lesson_no"] for l in lessons if l.get("action") == "replace" and not l.get("genre")]
    if bad:
        for n in bad:
            rep.r(f"L{n}: replace lesson missing genre")
    else:
        rep.p("genre present on all replace lessons")

    rep.section("CHECK 6 — Image-slot booleans")
    ok = True
    for l in lessons:
        for s in l.get("image_slots", []):
            for key in ("contains_living_being", "photocopy_safe"):
                if not isinstance(s.get(key), bool):
                    ok = False
                    rep.r(f"L{l['lesson_no']}/{s.get('id')}: {key} missing or non-boolean")
    if ok:
        rep.p("contains_living_being + photocopy_safe boolean on every slot")

    rep.section("CHECK 7 — source_note on Islamic-narrative blocks (grey; heuristic)")
    pat = re.compile("নবী|রাসূল|রাসুল|সাহাবি|সাহাবা|হাদিস|হাদীস")
    flagged = 0
    for l in lessons:
        for b in l.get("blocks", []):
            if b.get("source") == "school" and pat.search(b.get("text_bn") or "") \
               and not b.get("source_note"):
                flagged += 1
                rep.g(f"L{l['lesson_no']}/{b.get('id')}: narrative-marker text without source_note (reviewer resolves)")
    if flagged == 0:
        rep.p("no school block with Islamic-narrative markers lacks a source_note")

    rep.section("CHECK 8 — Script guard (RED on rendered text; Arabic RED anywhere; CD-008 watch)")
    cd008 = {}
    red8 = 0
    for l in lessons:
        for b in l.get("blocks", []):
            for key in RENDERED_LESSON_TEXT_KEYS:
                reds, greys, watch = guard_scan(b.get(key) or "")
                for ch, n in reds.items():
                    red8 += 1
                    rep.r(f"L{l['lesson_no']}/{b.get('id')}.{key}: Arabic-script glyph {ch!r} ×{n}")
                for ch, n in greys.items():
                    red8 += 1
                    rep.r(f"L{l['lesson_no']}/{b.get('id')}.{key}: symbol/arrow/emoji {ch!r} ×{n} in rendered text")
                for ch, n in watch.items():
                    cd008[ch] = cd008.get(ch, 0) + n
    for path, s in iter_strings(book):
        if any(part in path for part in (".text_bn", ".text_en")):
            continue  # already scanned as rendered
        reds, greys, _ = guard_scan(s)
        for ch, n in reds.items():
            red8 += 1
            rep.r(f"{path}: Arabic-script glyph {ch!r} ×{n} (D-011: red anywhere)")
        for ch, n in greys.items():
            rep.g(f"{path}: metadata symbol {ch!r} ×{n} (non-rendered; grey)")
    reds, greys, watch = guard_scan(book.get("title_bn") or "")
    for ch, n in {**reds, **greys}.items():
        red8 += 1
        rep.r(f"title_bn: disallowed glyph {ch!r} ×{n}")
    if red8 == 0:
        rep.p("no red script-guard hit in rendered text; no Arabic script anywhere")
    if cd008:
        rep.i("CD-008 WATCH — rendered-text occurrences pending the script-guard ruling: "
              + ", ".join(f"{WATCH_FOR_CD008[c]} ×{n}" for c, n in cd008.items()))
    else:
        rep.i("CD-008 WATCH — zero em-dash/ellipsis in rendered text")

    rep.section("CHECK 9 — No stripe language in image prompts")
    ok = True
    for l in lessons:
        for s in l.get("image_slots", []):
            p = (s.get("prompt") or "").lower()
            for f in STRIPE_FORBIDDEN:
                if f in p:
                    ok = False
                    rep.r(f"L{l['lesson_no']}/{s.get('id')}: forbidden stripe phrase {f!r} in prompt")
    if ok:
        rep.p("no stripe-instruction strings in any prompt")

    rep.section("CHECK 10 — Compliance map derivable")
    bad = [l["lesson_no"] for l in lessons
           if not l.get("nctb_pages") or not l.get("action")
           or not l.get("competency_codes")]
    if bad:
        for n in bad:
            rep.r(f"L{n}: missing codes/action/nctb_pages")
    else:
        rep.p("every lesson has codes + action + nctb_pages")

    rep.section("GREY-AT-MERGE — prompts · refs · bw_treatment")
    for l in lessons:
        if l.get("bw_treatment") not in VALID_BW:
            rep.g(f"L{l['lesson_no']}: bw_treatment {l.get('bw_treatment')!r} not in {sorted(VALID_BW)}")
        for s in l.get("image_slots", []):
            if s.get("action") != "vector_asset" and not s.get("prompt"):
                rep.g(f"L{l['lesson_no']}/{s.get('id')}: empty prompt (red before Images)")
            if s.get("image_class") == "narrative_figure" and not s.get("refs"):
                rep.g(f"L{l['lesson_no']}/{s.get('id')}: narrative_figure with no refs (red before Images)")

# ---------------- seeded-error selftest (README §6: executed proof) ----------------
def selftest(inv):
    ok = True
    log = []
    def expect(name, violations, should_fail):
        nonlocal ok
        got = len(violations) > 0
        s = "PASS" if got == should_fail else "FAIL"
        if s == "FAIL":
            ok = False
        log.append(f"  [{s}] {name}: expected_fail={should_fail} got_fail={got} "
                   f"({sorted({v['type'] for v in violations})})")

    # clean cases
    expect("clean_p10_vowels", audit_text("আ অ আ", 10, inv), False)
    expect("clean_p26_baba", audit_text("বাবা মা", 26, inv), False)
    expect("v2fix_precomposed_p33", audit_text("\u09aa\u09dc\u09bf", 33, inv), False)   # p+RRA(U+09DC)+i precomposed
    expect("v2fix_DECOMPOSED_p33", audit_text("\u09aa\u09a1\u09bc\u09bf", 33, inv), False)   # p+DDA+NUKTA+i decomposed
    expect("v2fix_cloze_underscores", audit_text("আমার নাম ____", 30, inv), False)  # blanks allowed; all letters taught @30
    expect("v2fix_cloze_slash", audit_text("আম/আতা", 26, inv), False)
    # seeded errors
    expect("seed_borno_early", audit_text("ক আ", 15, inv), True)
    expect("seed_kar_early", audit_text("কে", 24, inv), True)
    expect("seed_DECOMPOSED_borno_early", audit_text("\u099a\u09a1\u09bc", 20, inv), True)   # cha+DDA+NUKTA; RRA untaught @20
    expect("seed_conjunct_no_whitelist", audit_text("ভক্ত", 30, inv), True)
    expect("seed_conjunct_null_default_none", audit_text("ক্ত", 45, inv), True)
    expect("seed_arabic_in_text", [{"type": "guard"}] if guard_scan("সালাম م")[0] else [], True)
    expect("seed_stray_nukta", audit_text("ব়", 30, inv), True)

    # book-level seeded errors through the full validator
    book = {"schema_version": "1.0", "book_id": "C1-BAN", "class": 1, "subject": "BAN",
            "mode": "R", "title_bn": "টেস্ট",
            "lessons": [{"lesson_no": 1, "nctb_pages": [1], "genre": "x",
                         "competency_codes": ["১.১"], "outcome_codes": ["১.১.১"],
                         "action": "replace", "bw_treatment": "native_safe",
                         "blocks": [{"id": "b1", "source": "school", "edited": True,
                                     "oral": False, "text_bn": "ক আ"}],  # untaught @1
                         "image_slots": [{"id": "s1", "prompt": "add a white stripe over the boy",
                                          "contains_living_being": True}]}]}  # photocopy_safe missing
    rep = Report()
    validate(book, inv, rep)
    for name, cond in [("book_letter_red", any("borno_not_taught" in x for x in rep.lines)),
                       ("book_stripe_red", any("stripe phrase" in x for x in rep.lines)),
                       ("book_boolean_red", any("photocopy_safe" in x for x in rep.lines))]:
        s = "PASS" if cond else "FAIL"
        if s == "FAIL":
            ok = False
        log.append(f"  [{s}] {name}: caught={cond}")
    return ok, log

# ---------------- main ----------------
def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "--selftest":
        inv = json.load(open(sys.argv[2], encoding="utf-8"))
        ok, log = selftest(inv)
        print("SEEDED-ERROR SELFTEST — validator_v2_rebuilt")
        print("\n".join(log))
        print("\nRESULT:", "PASS — rebuilt validator is a working net"
              if ok else "FAIL — do not merge through it")
        sys.exit(0 if ok else 1)

    book_path, inv_path = sys.argv[1], sys.argv[2]
    book = json.load(open(book_path, encoding="utf-8"))
    inv = json.load(open(inv_path, encoding="utf-8"))
    rep = Report()
    rep.lines.append("=" * 72)
    rep.lines.append(f"VALIDATOR REPORT — validator_v2_rebuilt · book {book.get('book_id')} "
                     f"· {len(book.get('lessons', []))} lessons")
    rep.lines.append("=" * 72)
    validate(book, inv, rep)
    rep.lines.append("")
    rep.lines.append("=" * 72)
    rep.lines.append(f"RESULT:  RED={rep.red}   GREY={rep.grey}   PASS={rep.passed}")
    rep.lines.append("VERDICT: " + ("FAIL — red failures must resolve before merge (step 8 → step 3)"
                                    if rep.red else "PASS — no red failures; greys listed for reviewer"))
    rep.lines.append("=" * 72)
    print("\n".join(rep.lines))
    sys.exit(1 if rep.red else 0)

if __name__ == "__main__":
    main()
