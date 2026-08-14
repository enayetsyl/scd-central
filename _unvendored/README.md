# `_unvendored/` — parked, not staged, not vendored

**This README is committed. Everything beside it is gitignored.**

That split is the whole point. `_inbox/` is gitignored in full (AGENTS.md §12.1), so a file parked
there is invisible in every diff, commit and pull — which is the failure §12.7 was written to end.
Moving a file to a second gitignored folder would change nothing. So the **file** stays out of Git
and the **row below** goes in: a session on another device cannot open the file, but it can read
that the file exists, whose it is, and why nothing consumes it.

**This folder is not an authority and is not a staging area.** Nothing here is classified under
§12.1, nothing here is on its way anywhere, and nothing may cite it. A file leaves this folder in
one of exactly two directions: a consumer appears and it is vendored properly under `tools/` with a
`tools/MANIFEST.md` row (§12.1 Assets), or the Principal says delete it.

## Why a font is not an Assets-class file

§12.1's Assets row reads **"fonts, images, spreadsheets *consumed by a tool*"**, destination
"`tools/` **beside the tool that consumes them**". The qualifier is doing the work. A font with no
consumer has no tool to sit beside, and `tools/MANIFEST.md`'s own header already refuses it:
*"Rows are executable tools only — fonts and data are not listed here"*, with font presence
asserted at runtime by `ct_docx.py` and `glyph_probe.py` instead.

So the class test fails on its own terms, and §12.3 applies: **a file that matches no class is
reported, never moved into a governed subtree.** This folder is the reporting surface — it is
deliberately outside `canon/`, outside `tools/` and outside `workstreams/`, so nothing parked here
can acquire authority from its location, which is the risk §12.3 names.

## Parked

| File | Arrived | Owner | Why it is here |
|---|---|---|---|
| `NotoNaskhArabic-Medium.ttf` | 2026-08-09 | Principal | **These are the Arabic lane's** (Principal, 2026-08-14, closing Q-7). Naskh is an Arabic-script face and `islamic-studies` is the lane that will need one. No tool references them **yet** — `tools/render/ct_docx.py` and `glyph_probe.py` name their own configured fonts and neither is this. |
| `NotoNaskhArabic-SemiBold.ttf` | 2026-08-09 | Principal | As above; the two were staged together. |

## For whoever opens the Arabic lane — read this before re-sourcing anything

**You are looking for these files. They are here.** They were parked rather than vendored because
nothing consumed them, and they are named here so the lane does not start by downloading fonts it
already has.

**`islamic-studies` is greenfield and its Arabic content is an `ARABIC-SLOT` placeholder today.**
That is not an oversight — **CD-014** gates Arabic script on *renderer capability, not doctrine*.
A workstream may carry Arabic in rendered fields only when **both** hold:

1. **Proven shaping** — the full render path has passed an **executed** smoke test with real ayah
   text rendered and eyeball-verified (RTL correct, joining correct, no tofu), logged the way
   `tools/hub-export/SMOKE.md` is, and proven **per render path** so a new renderer, font or export
   route re-proves it.
2. **Verbatim quoted source only** — every Arabic string is quoted source text with provenance
   (mushaf or hadith reference in `source_note`), reviewed in the **আলিম lane**, never
   model-composed and never transliteration-round-tripped.

**These fonts are candidates for (1), not a discharge of it.** Vendoring a font does not prove a
render path; an executed smoke test does. The order is: open the lane → build the render path →
smoke-test it with these faces → **then** vendor them under `tools/` beside the tool that consumes
them, with a `tools/MANIFEST.md` row. Until that smoke test exists, they stay here.

REL is out of scope by `canon/QUESTION_POLICY.md` §7 until `islamic-studies` opens, so there is no
present consumer and no deadline.

**Both are licensed OFL (Google Noto).** Re-downloading them is free and takes a minute, which is
the second reason not to vendor a binary nothing reads: the cost of being wrong about deleting them
is near zero, and the cost of a committed binary nobody can account for is not.
