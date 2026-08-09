# tools/render — index

✅ VENDORED + PROVEN 2026-08-09. The school's print path: class-test Markdown to .docx.

| File | Role |
|---|---|
| `ct_docx.py` | Class-test Markdown → .docx. Font family is configuration. Routes every character to a font that actually covers it; `--strict` exits 1 if any character has none |
| `glyph_probe.py` | Establishes a render path's proven glyph set (CD-018) — cmap coverage, LibreOffice substitution, and raster for eyeball verification |
| `render_plan.py` | P03 plan renderer. **Vendored but UNPROVEN** — no plan JSON supplied yet |
| `fonts/` | Noto Serif Bengali (R/B), Noto Serif (R/B), Noto Naskh Arabic (R/B) |
| `reference/` | The two class tests `ct_docx.py` was authored against. **FORMAT reference only** — historical record, never edited; `৪৫ মিনিট` superseded by the 35-minute rule (CD-021), never copy the time line (CD-023) |
| `SMOKE.md` | The proven glyph set, the runs that established it, and the font-install prerequisite |

```
python3 ct_docx.py <ct.md> -o out.docx --strict
```

## Two things that will bite you

**Fonts must be installed, not merely present.** LibreOffice resolves fonts by name through
fontconfig; files sitting in `fonts/` are invisible to it and it substitutes silently without
erroring. Run the `fc-cache` step in `SMOKE.md` first.

**Templates must not carry 🔴 🟦 ✅ ⚠** — they tofu on this path (CD-018 finding). `✓ → ★ ↑ ↓`
are fine *through `ct_docx.py`*, which routes them to a symbol font; pasted into a hand-built
.docx they will tofu. Per R-1 the generator substitutes `✅`→`✓` and `⚠`→`দ্রষ্টব্য:`.

Arabic: Noto Naskh Arabic renders correctly, RTL and joining verified (CD-014 condition 1).
Condition 2 — verbatim source, আলিম-reviewed — is a human gate; `islamic-studies` stays on
`ARABIC-SLOT` regardless of this path (CD-014).

Language rules for output: `canon/language/LANGUAGE_RULES.md` §2 (Bengali numerals in anything
a teacher or student reads) and §7 (script guard). Cite, never copy.
