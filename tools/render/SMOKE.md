# SMOKE.md — tools/render

Evidence that this render path has been **run**, not merely placed (AGENTS.md §5, CD-009), and
the record of its **proven glyph set** (CD-018). Re-run and update whenever a font, the
generator, or the export route changes — CD-018 proves per render path, not once per repo.

Run 2026-08-09. Chain: `ct_docx.py` → .docx → LibreOffice 26.2.4.2 → PDF → pdftoppm → PNG,
verified **on the rasterised page**, never on the .docx XML or a `pdftotext` round-trip.

## ⚠ Reproduction prerequisite — fonts must be installed, not merely present

LibreOffice resolves fonts by **name via fontconfig**. Vendored files sitting in `fonts/` are
invisible to it. Before any run:

```
mkdir -p ~/.local/share/fonts && cp tools/render/fonts/*.ttf ~/.local/share/fonts/ && fc-cache -f
```

**This is not a formality.** The first probe run of this session was done without it: LibreOffice
silently substituted DejaVu for every Bengali run and reported no error. The substitution and
raster signals were meaningless and would have "passed" a careless reading.

## Proven glyph set — docx path, 2026-08-09

| Class | Result | Carried by |
|---|---|---|
| Bengali: numerals ০–৯, যুক্তবর্ণ, কারচিহ্ন, ংঃঁ | ✅ correct | Noto Serif Bengali |
| **Arabic incl. harakat — RTL + joining** | ✅ **correct, eyeball-verified** | Noto Naskh Arabic |
| Em-dash `—`, ellipsis `…` (tier-3 WATCH) | ✅ correct | Noto Serif Bengali |
| Latin + ASCII digits | ✅ correct | Noto Serif Bengali |
| `✓` U+2713, `→` U+2192, `★` `↑` `↓` | ✅ correct **only via an explicit symbol run** | DejaVu Sans |
| `🔴` U+1F534, `🟦` U+1F7E6 | ❌ **TOFU — empty boxes** | no font on this path |
| `✅` U+2705, `⚠` U+26A0 | ❌ TOFU — **substituted away** per R-1 | n/a |

**Finding for templates (CD-018):** CT templates must not carry 🔴 🟦 ✅ ⚠. They may carry
✓ → ★ ↑ ↓ **only** through `ct_docx.py`, which routes them to the symbol font automatically.
Pasting them into a hand-built .docx will tofu. This constrains templates, not canon.

## Test 1 — generator, both reference CTs, `--strict`

```
ct_docx: C5_Bangla_ClassTest_Ch19.md -> C5_Bangla_ClassTest_Ch19.docx
  fonts: body=Noto Serif Bengali · symbol=DejaVu Sans · arabic=Noto Naskh Arabic
  substitutions applied (R-1): ✅->✓
  routed to symbol font: U+2192(→) U+2713(✓)
  UNRESOLVED: none — every character has a covering font
EXIT=0

ct_docx: C5_Bangla_ClassTest_Ch20.md -> C5_Bangla_ClassTest_Ch20.docx
  fonts: body=Noto Serif Bengali · symbol=DejaVu Sans · arabic=Noto Naskh Arabic
  substitutions applied (R-1): ✅->✓ · ⚠️->দ্রষ্টব্য: · ⚠->দ্রষ্টব্য:
  routed to symbol font: U+2192(→) U+2713(✓)
  UNRESOLVED: none — every character has a covering font
EXIT=0
```

`--strict` exits 1 on any character with no covering font. Both exit 0.

## Test 2 — full chain, embedded fonts

```
$ pdffonts C5_Bangla_ClassTest_Ch19.pdf
BAAAAA+NotoSerifBengali-Regular      TrueType   WinAnsi   yes yes yes
CAAAAA+NotoSerifBengali-Bold         TrueType   WinAnsi   yes yes yes
DAAAAA+DejaVuSans-Bold               TrueType   WinAnsi   yes yes yes
EAAAAA+OpenSymbol                    TrueType   WinAnsi   yes yes yes
FAAAAA+DejaVuSans                    TrueType   WinAnsi   yes yes yes
```

Exactly the configured fonts, plus OpenSymbol for list bullets. No unexpected fallback.

## Test 3 — eyeball on the raster (the load-bearing check)

4 pages per CT at 150 dpi. Confirmed by eye:

- Student-facing `১। সঠিক উত্তরটিতে টিকচিহ্ন (✓) দাও। ১×৫=৫` — **✓ renders**, no box.
- Teacher section `ফুল ফুটেছে গাছে। → ভ্রমর বসে কাছে।` — **→ renders**.
- Checklist — `✅` correctly became `✓` and renders throughout.
- Bengali numerals, conjuncts, কারচিহ্ন and em-dash all correct at print size.

## Arabic proof — CD-014 condition (1): SATISFIED for this path

`بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ` rendered via Noto Naskh Arabic and verified by eye:
**RTL order correct, letters joined correctly, harakat positioned correctly, no tofu.**

⚠️ Condition (2) — verbatim quoted source with `source_note` provenance, reviewed in the
**আলিম lane** — is a human gate and is **NOT** satisfied by this test. `islamic-studies`
remains on `ARABIC-SLOT` until (2) is met (CD-014).

## Not proven here

**`render_plan.py` is vendored but UNPROVEN.** It renders P03 plan artifacts and no plan JSON
was supplied, so it has not been executed. Do not treat its presence as a pass. See
`tools/_wip/STATE.md`.

## Header config (CD-021)

CT number and duration are **configuration, not free text in the source markdown**.
`--duration-min` defaults to 35 and **exits 1 outside 30–35**:

```
$ ct_docx.py ... --duration-min 45
ERROR: --duration-min 45 is outside the canon range 30-35 minutes for a 25-mark class test (CD-021)
EXIT=1
```

**Reference CTs — RULED (CD-023).** The two papers in `reference/` read `৪৫ মিনিট` and are
**deliberately not edited**: they are the historical record of tests actually given, an imported
reference corpus rather than live templates. They are marked **FORMAT reference only**; their
time line is superseded by CD-021 and **must never be copied**. See `reference/README.md`.

## Commands

```
python3 tools/render/ct_docx.py <ct.md> -o out.docx --ct-number 3 --strict
python3 tools/render/glyph_probe.py --fonts-dir tools/render/fonts --set all --corpus <ct.md>
```
