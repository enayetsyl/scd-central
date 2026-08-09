# SETUP NOTE — C1-BAN support-book renderer geometry: trim value

*Working artifact for the Production wave (C1–C5 2026). Not a governance file. Feeds ASSEMBLY.md §3.1 (support-book geometry) and the support-book `geometry.js` profile. Status: **ASSUMPTION — awaiting Principal ruling + physical confirmation**. Date: 2026-07-17.*

---

## Recommended value (provisional)

**Trim: 190 × 250 mm (demy quarto), portrait.**

This is the single number the support-book geometry derives from: the image short-side DPI floor (300 DPI min), the print-colour and bw-photocopy profiles, and the geometry asserts (>0.5 mm tolerance) all recompute from it (ASSEMBLY.md §3.1–3.2, §2 image chain).

## Why — and why it is only an assumption

The value is **inferred**, not measured. It is not safe to bake into the geometry until confirmed.

- **The source file carries no physical dimensions.** The uploaded `Class_1_Bangla.pdf` is not a PDF but a ZIP bundle of 90 page-raster JPEGs + extracted text + `manifest.json`. There is **no PDF page dictionary**, therefore **no MediaBox / CropBox / TrimBox / BleedBox** to read in points, and thus no authoritative trim or bleed in the file.
- **No DPI metadata.** Every page raster is a uniform **952 × 1260 px** with JFIF density unit = 0 (aspect-ratio only, no physical resolution). Absolute size is unspecified; any geometry back-computed from the pixels alone would inherit the scan's arbitrary resolution, not a real trim.
- **The inference:** pixel aspect ratio 952 / 1260 = **0.7556**. Nearest portrait book standard is **demy quarto (190 × 250 mm → 0.7600)**, ~0.6% off. Crown quarto (189 × 246 → 0.7683) is ~1.7% off; A4 (210 × 297 → 0.7071) is further. NCTB primary textbooks are in practice printed on a demy-quarto-class trim, consistent with this ratio. ASSEMBLY.md §3.1 anticipated "crown-quarto/A4-family"; the measured aspect ratio points specifically at demy quarto, closer than crown and clearly not A4.

## Standard-trim comparison table

| Standard | mm (portrait) | ratio | Δ vs raster (0.7556) |
|---|---|---|---|
| A4 | 210 × 297 | 0.7071 | −6.4% |
| Royal octavo | 156 × 234 | 0.6667 | −11.8% |
| Crown quarto | 189 × 246 | 0.7683 | +1.7% |
| **Demy quarto** | **190 × 250** | **0.7600** | **+0.6%** |

## What must happen before this value is configured

1. **Principal ruling** on snapping to demy quarto vs another standard (per the flag-uncertainty rule; this is an assumption, not a measurement).
2. **Confirmation from an authoritative source.** A printed copy is **not available** (2026-07-17), so ruler measurement is ruled out. Remaining paths, in order of strength:
   - (a) a genuine **print-production PDF** of this book with a real TrimBox (NCTB distributes official textbook PDFs; a real PDF — not this raster bundle — would resolve the aspect ratio to an exact trim);
   - (b) the **NCTB print specification / tender** for primary textbooks, if it names the trim — documentable and citable.
   Either overrides the inference below.
3. If neither (a) nor (b) materialises, proceeding on the inference (demy quarto, ~0.6% off) is acceptable for a first render-proof pass **provided** this note travels with the config and the Principal signs off knowing it is an assumption. Caveat: the render-proof's geometry asserts (>0.5 mm) and text-fit guard will catch layout drift, but **not** a whole-book scale error that preserves aspect ratio.
4. Only then fix the trim in the support-book `geometry.js` profile and run the render-proof pass (ASSEMBLY.md §3.1: "Decide the exact trim before the render-proof pass").

## Reversibility
Because the entire geometry derives from the single trim number, correcting the trim later (e.g. to crown quarto) is a one-line change + re-derive, not a rework — **provided nothing downstream hardcodes pixel dimensions instead of deriving from the trim.** Low-cost to proceed on the assumption on that condition.

## Note on the file itself
This bundle is a **digital/scanned raster**, not a print-production PDF: single raster per page, no boxes, no DPI. All 90 pages are pixel-identical (952 × 1260), so it is internally consistent, but the absolute size is unspecified and must be treated as approximate.
