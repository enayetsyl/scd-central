# ASSEMBLY — Support-Book PDF generation
*How a validated `support-book.json` + compliant images become print PDFs. Companion to the schema. v1.0-draft · July 2026*

> **Scope.** This spec covers the render tail only: `compliance-done → assembled → QA-passed`. Everything upstream (the nine-step chapter loop, the validator) is README §3/§6. Assembly consumes a merged, validator-passed book JSON and finished compliant images; it invents no content. If the output is wrong, fix the JSON and re-render — never patch the PDF.

---

## §1 The renderer is a shared neutral tool (D-017)
The Bengali-safe renderer is reused from the storybook project **as a build tool, not as shared product infrastructure** — the way two projects might share a compiler, Node, or a font. It holds no content, has no product identity, and writes to a separate output root. Product separation (D-007) is therefore honoured *in substance*: the **products** — NCTB-adapted content, images, finished books, folders — never touch; only the neutral build machinery is common.

Discipline (inherited from the storybook `CLAUDE.md`): **the frozen renderer core is never modified for support-book needs.** All support-book-specific code lives in a support-book workbench/adapter that *spawns* the renderer's scripts with the right args and feeds it a support-book content shape. If the renderer core ever must change, the change is validated against **both** products before it ships (the cost of a shared tool, accepted knowingly).

**Separate roots (absolute):** support-book content root, images, and `out/` are distinct from the storybook roots. Only the renderer executables/libraries are shared.

---

## §2 What transfers unchanged from the storybook renderer
These are the hard-won, correctness-critical parts. They are reused **as-is** — do not re-implement, do not fork:

- **Bengali font strategy** — exactly four embedded faces (NotoSerifBengali Regular/Bold, NotoSerif Regular/Bold) as base64 `@font-face`; missing TTF throws; no `file://` links, no OS fallback. The Bengali face sits inside the English stack too, so a stray Bengali glyph never falls back to an OS font.
- **Script guard** — scans every string for codepoints outside the allowlist (Basic Latin, Latin-1, common punctuation, Bengali U+0980–09FF, danda/double-danda U+0964–0965, ZWNJ/ZWJ). Arabic, Devanagari digits, CJK, arrows/symbols, emoji all FAIL. **Rule: fix the text, never widen the allowlist.** This is the *same invariant* as schema check #8 — the two guards share one allowlist; a string that passes one must pass the other.
- **Geometry asserts** — after `emulateMediaType('print')`, measure the laid-out page and refuse to render if width/position is off by >0.5 mm. Never reintroduce mixed units (the inches-inside-mm 0.75-scale bug).
- **Post-render font audit** — inflate the PDF, list every `/BaseFont`, require every face embedded and on the four-face allowlist; any stray face = OS substitution = build fails.
- **Render determinism** — Puppeteer `--font-render-hinting=none --disable-lcd-text`; wait for `document.fonts.ready`; decode every `<img>` before snapshot.
- **Text-fit guard** — every text box carries `[data-fit]`; the build fails on overflow (a silently clipped sentence is worse than a failed build). Bengali/English line counts differ, so panel heights are *measured* (fit-sweep), never arithmetic.
- **Image chain** — crop (edge-artifact shave) → upscale (to the DPI floor) → strips (`apply_strips.py`, white compliance partition from `placements.json`; supports arrays of strips per image for multi-figure scenes; `contains_living_being:false` slots pass through untouched) → compliant. Lineage SHAs detect stale files and re-run only those.

---

## §3 What is support-book-specific (built new, in the adapter — never in the frozen core)

### 3.1 Geometry (portrait, not the storybook 8×8 square)
Support books sit beside a portrait NCTB textbook. The support-book geometry is its own `geometry.js`-shaped profile: portrait trim (to be fixed against the NCTB physical book — likely crown-quarto/A4-family), bleed, safe margin, 300 DPI minimum. Everything derives from these numbers as in the storybook core; the image short-side floor recomputes from the new trim. **Decide the exact trim before the render-proof pass** — it sets the image DPI floor.

### 3.2 Render profiles — two, both first-class, both always rendered (D-016)
| profile | canvas | colour/background | image handling | notes |
|---|---|---|---|---|
| **print-colour** | trim + bleed + crop slug | full colour, **true white** background (not the storybook cream — a সহায়িকা sits next to a white NCTB book) | 300 DPI PNG | the colour master |
| **bw-photocopy** | trim (photocopy master; marks as needed) | **greyscale / pure black-line, true white** (no cream — cream photocopies as grey) | high-contrast, tuned so the copier doesn't muddy midtones | the bulk-distribution edition; **must survive the school's actual copier** |

Both editions render from the same JSON every build; a book is not `assembled` until both pass their audits. The cream flatten used for sellable storybooks is **wrong here** and is not used in either support-book profile.

### 3.3 Composition (lessons in NCTB order, heterogeneous blocks — not a fixed spine)
The storybook composer lays out a fixed spine (cover/title/20 story pages/anchor/guardian/back). A সহায়িকা has **variable পাঠ count** and **heterogeneous block types** per পাঠ. The support-book composer walks `lessons` in NCTB order and lays out each block by `type` + `layout_hint`: heading, instruction, oral_text, decodable_text, poem/rhyme, story, dialogue, word_list, exercise, fill_blank, matching, writing_line, **tracing_ref**, table. It places each image from its recorded compliant filename, and renders **letter-tracing pages from vector assets at assembly** (`tracing_asset`/`vector_asset` slots — never AI images; their `prompt` stays `""`).

### 3.4 The bw-photocopy colour-pedagogy resolution
Each lesson's `bw_treatment` (schema) drives the B/W edition:
- `native_safe` → renders in B/W as-is.
- `redesigned` → the B/W-safe scheme (pattern/outline/shading replacing colour-coding) renders.
- `print_only_omit` → the পাঠ is **omitted from the bw-photocopy edition** and carries a teacher note pointing to the colour master / NCTB original.
The assembly validator (schema check 11) **red-fails** a build whose B/W edition still contains colour-dependent pedagogy marked `native_safe`.

### 3.5 Assembly-time validation profile (support-book, not storybook)
The storybook `validate.js` hard-checks a storybook shape (20 story pages, 24-page interior, ≥30% no-living-being, word budgets). Those are **wrong** for support books. The support-book assembly validator checks its own shape: complete পাঠ inventory in NCTB order; every image ≥ the DPI floor at full bleed; tracing/vector pages present where declared; B/W-edition completeness (check 11); and it re-runs the **same script guard** as a final gate. It does **not** impose a fixed page count or a minimum image density — support books are text-first.

---

## §4 The assembly step (sequence)
Run by the support-book workbench adapter; the only sanctioned writes across the tool boundary:
1. **Sync** the merged `support-book.json` + `images-compliant/` → the renderer's support-book content root.
2. **Fit-sweep** — Chrome measures every page in both language layers (where the book carries an English layer) and writes measured panel minimums back per book.
3. **Validate (assembly profile)** — support-book structural checks + script guard (§3.5). Fail = stop; fix JSON, re-run.
4. **Build** — render **both** profiles (print-colour + bw-photocopy) via the frozen core; resize each image once (never upscale — the DPI gate already ruled); compose one HTML document per edition so the text-fit guard fires across all pages; then the post-render page-count/media-box/font audit. Exit non-zero on any failure.
5. **Write back** any fit-sweep-updated JSON to the book folder.

Output: `out/<BOOK_ID>/<BOOK_ID>-<lang>-<profile>.pdf` for the profiles above, in a **support-book output root** separate from storybook `out/`.

---

## §5 The render-proof gate (before assembly is trusted)
Mirrors the validator's seeded-error test. On the **first completed C1-BAN chapter**, render both editions and physically verify:
1. Every যুক্তবর্ণ and কারচিহ্ন renders correctly (the Bengali toolchain's silent failure point).
2. The **bw-photocopy edition survives an actual pass through the school's copier** — images legible, no story-critical detail lost, the white compliance stripe reads clean, colour-pedagogy pages resolved (redesigned or omitted, never broken).
3. Images land per `layout_hint`, nothing clipped by crop; tracing/vector pages render at correct size.
4. NCTB page cross-references appear on the page (the সহায়িকা posture, D-006).
Until this passes on a real chapter, the assembly step is unproven — the same way an untested validator is unproven.

---

## §6 Known gotchas inherited from the machine
- Assembly can fail **EBUSY** if a PDF viewer holds an `out\*.pdf` open — close it.
- Occasional transient Puppeteer "Connection closed" — retry.
- PowerShell 5.1 has no `&&`; spawn `python`/`node`/`npm.cmd` with `shell:false`.
- Large print PDFs: the renderer's `pdfinfo` scans stream chunks individually (V8 string-length limit) — inherited, do not undo.
- **Banned-char reintroduction:** support-book content is drafted in Claude chats where Arabic honorifics are a live temptation (D-011 requires transliteration or Bangla). Sanitize against the shared allowlist before assembly; the schema guard is the upstream catch so it rarely reaches here.

## Version log
| v | Date | Change | By |
|---|---|---|---|
| 1.0-draft | 2026-07 | Initial assembly spec: shared-renderer-as-tool (D-017), transfer list, support-book-specific geometry/profiles/composition/validation, two always-rendered editions, bw_treatment resolution, render-proof gate. | Claude (draft); Principal (approval pending) |
