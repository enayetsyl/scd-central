#!/usr/bin/env python3
"""
Letter audit — the one subject-specific validator check (README §3.3, D-004/D-009).
Runs for Class 1-2 বাংলা by loading the book's letter_inventory_<ID>.json.
Executed, never reasoned (D-004). Red-fails any decodable block using a বর্ণ/কারচিহ্ন
not taught up to পাঠ N, or a conjunct not on পাঠ N's whitelist (B-1).

Scope (README §4.2): applies ONLY to blocks the child must decode (পড়ি/লিখি).
Blocks with oral:true are exempt (still curated elsewhere, not here).
"""
import json, sys, unicodedata

# Bengali combining vowel signs (কারচিহ্ন) codepoints.
KAR_SET = set("ািীুূৃেৈোৌ")
# Marks that attach but are taught as বর্ণ-level special signs in this book (পাঠ 34).
SPECIAL_MARKS = set("ংঃঁ")
HASANTA = "\u09cd"  # ্ — conjunct former
ZW = {"\u200c", "\u200d"}  # ZWNJ/ZWJ
# Punctuation/whitespace/digits always allowed in decodable text.
ALLOWED_PUNCT = set(" \n\t।,.?!-—…‘’“”()৷॥/") | set("০১২৩৪৫৬৭৮৯0123456789")

# Multi-codepoint বর্ণ (base + nukta U+09BC). These are taught/stored as WHOLE UNITS
# in the letter inventory (cumulative_borno lists "ড়" "ঢ়" "য়"), but a naive per-codepoint
# scan sees a bare nukta and mis-fails. Map each to a single private-use sentinel BEFORE
# scanning so the unit is matched as one glyph; the reverse map lets us name it in errors.
MULTI_BORNO = {"\u09a1\u09bc": "\uE000", "\u09a2\u09bc": "\uE001", "\u09af\u09bc": "\uE002"}
SENTINEL_TO_BORNO = {v: k for k, v in MULTI_BORNO.items()}
def _normalize_multi(text):
    for real, sent in MULTI_BORNO.items():
        text = text.replace(real, sent)
    return text

def load_inventory(path):
    return json.load(open(path, encoding="utf-8"))

def cumulative_allowed(inv, lesson_no):
    L = inv["lessons"][str(lesson_no)]
    borno = set(L["cumulative_borno"])
    # Represent taught multi-codepoint বর্ণ (ড়/ঢ়/য়) by their single-char sentinel so the
    # per-codepoint scan can match them as whole units (mirrors _normalize_multi on text).
    for real, sent in MULTI_BORNO.items():
        if real in borno:
            borno.discard(real)
            borno.add(sent)
    kar = set(L["cumulative_kar"])
    cj = L.get("conjunct_whitelist", {})
    glyphs = cj.get("glyphs") or []          # None -> [] : B-1 default 'none'
    conj = set(glyphs)
    return borno, kar, conj

def audit_text(text, lesson_no, inv):
    """Return list of violations (empty = pass)."""
    borno, kar, conj = cumulative_allowed(inv, lesson_no)
    allowed_chars = borno | kar | SPECIAL_MARKS | ZW | ALLOWED_PUNCT | {HASANTA}
    # Fold taught multi-codepoint বর্ণ (ড়/ঢ়/য়) into single sentinels before scanning.
    text = _normalize_multi(text)
    violations = []

    # 1) conjunct check: any hasanta-joined cluster must be on this পাঠ's whitelist.
    i = 0
    clusters = []
    for idx, ch in enumerate(text):
        if ch == HASANTA:
            # grab base before + consonant after to name the cluster (best-effort)
            left = text[idx-1] if idx > 0 else ""
            right = text[idx+1] if idx+1 < len(text) else ""
            cluster = f"{left}{HASANTA}{right}"
            clusters.append(cluster)
    for c in clusters:
        # normalise the visible conjunct (strip nothing; compare raw)
        if c not in conj:
            violations.append({"type": "conjunct_not_whitelisted",
                               "cluster": c,
                               "detail": "যুক্তবর্ণ not on পাঠ %s whitelist (B-1)" % lesson_no})

    # 2) per-character check for বর্ণ/কারচিহ্ন not yet taught.
    for ch in text:
        if ch in ZW or ch == HASANTA:
            continue
        cat = unicodedata.category(ch)
        if ch in allowed_chars:
            continue
        # An untaught multi-codepoint বর্ণ appears here as a sentinel -> name it by its real glyph.
        if ch in SENTINEL_TO_BORNO:
            violations.append({"type": "borno_not_taught", "char": SENTINEL_TO_BORNO[ch],
                               "detail": "বর্ণ not taught up to পাঠ %s" % lesson_no})
            continue
        # Is it a Bengali letter/sign at all?
        if "\u0980" <= ch <= "\u09ff":
            if ch in KAR_SET and ch not in kar:
                violations.append({"type": "kar_not_taught", "char": ch,
                                   "detail": "কারচিহ্ন not taught up to পাঠ %s" % lesson_no})
            elif ch == "\u09bc":
                # A bare nukta that survived normalization = a nukta on a base that is NOT one
                # of the three taught multi-units -> genuinely disallowed.
                violations.append({"type": "borno_not_taught", "char": "\u09bc",
                                   "detail": "unrecognised nukta combination not taught up to পাঠ %s" % lesson_no})
            elif ch not in KAR_SET:
                violations.append({"type": "borno_not_taught", "char": ch,
                                   "detail": "বর্ণ not taught up to পাঠ %s" % lesson_no})
        else:
            # non-Bengali, non-allowed -> script guard territory; flag here too
            violations.append({"type": "out_of_script", "char": repr(ch),
                               "detail": "character outside Bengali+allowed set"})
    return violations

def audit_lesson_block(block, lesson_no, inv):
    if block.get("oral") is True:
        return []  # exempt
    if block.get("source") == "nctb":
        # NCTB-original decodable text is protected/retained; audit only school text.
        return []
    text = block.get("text_bn", "") or ""
    return audit_text(text, lesson_no, inv)

# ---------------- seeded-error test (README §6 / SETUP §3) ----------------
def seeded_error_test(inv):
    """Prove the audit catches what it must and passes clean text. Returns (ok, log)."""
    log = []; ok = True
    def expect(name, got_violations, should_fail):
        nonlocal ok
        failed = len(got_violations) > 0
        status = "PASS" if failed == should_fail else "FAIL"
        if status == "FAIL": ok = False
        log.append(f"  [{status}] {name}: expected_fail={should_fail} got_fail={failed} "
                   f"({[v['type'] for v in got_violations]})")

    # Clean cases (should PASS = no violations)
    # পাঠ 10 knows only অ আ -> 'আম' uses আ + ম? ম not taught till 26. Use only অ/আ:
    expect("clean_p10_vowels_only", audit_text("আ অ আ", 10, inv), should_fail=False)
    # পাঠ 26 knows all consonants+ আ-কার(21)+ই-কার(22)+উ-কার(27? no, 27>26)
    # 'মা' = ম + া(21) ok at 26. 'বাবা' ok.
    expect("clean_p26_baba", audit_text("বাবা মা", 26, inv), should_fail=False)
    # oral block exempt even with untaught letters
    expect("oral_exempt", audit_lesson_block(
        {"oral": True, "source": "school", "text_bn": "ক্ষমা করো"}, 10, inv), should_fail=False)
    # nctb source exempt
    expect("nctb_exempt", audit_lesson_block(
        {"source": "nctb", "text_bn": "যেকোনো কিছু"}, 5, inv), should_fail=False)

    # Seeded errors (should FAIL = catch a violation)
    # untaught বর্ণ: 'ক' (taught পাঠ 19) used at পাঠ 15
    expect("seed_borno_too_early", audit_text("ক আ", 15, inv), should_fail=True)
    # untaught কারচিহ্ন: 'ে' (এ-কার, পাঠ 29) used at পাঠ 22
    expect("seed_kar_too_early", audit_text("কে", 24, inv), should_fail=True)  # ক ok@19, ে@29 not yet@24
    # conjunct where whitelist empty: 'ক্ত' at পাঠ 30 (no whitelist there)
    expect("seed_conjunct_no_whitelist", audit_text("ভক্ত", 30, inv), should_fail=True)
    # conjunct at a needs_review পাঠ whose glyphs are null -> default none -> must FAIL
    expect("seed_conjunct_needsreview_default_none", audit_text("ক্ত", 45, inv), should_fail=True)

    # --- multi-codepoint বর্ণ (ড়/ঢ়/য়) normalization regression (added with the tooling fix) ---
    # ড়/য় are introduced পাঠ 33; words using them must PASS at পাঠ 43 (were false-failing on bare nukta).
    expect("clean_multi_borno_p43", audit_text("উড়ে যায় ঘড়ি গায় চায়", 43, inv), should_fail=False)
    # The same multi-borno must still FAIL before পাঠ 33 (e.g. পাঠ 30, not yet taught).
    expect("seed_multi_borno_too_early", audit_text("উড়ে", 30, inv), should_fail=True)
    # A nukta on a base that is NOT one of the three taught units must still FAIL (bare-nukta guard).
    expect("seed_unrecognised_nukta", audit_text("ক\u09bc", 43, inv), should_fail=True)
    # forward slash (NCTB cloze option markers) is now allowed punctuation -> PASS.
    expect("clean_slash_option_marker", audit_text("যায়/খায়", 43, inv), should_fail=False)

    return ok, log

if __name__ == "__main__":
    inv = load_inventory(sys.argv[1] if len(sys.argv) > 1 else "/tmp/letter_inventory_C1-BAN.json")
    ok, log = seeded_error_test(inv)
    print("SEEDED-ERROR TEST")
    print("\n".join(log))
    print("\nRESULT:", "PASS — validator letter audit is a working net" if ok else "FAIL — do not merge through it")
    sys.exit(0 if ok else 1)
