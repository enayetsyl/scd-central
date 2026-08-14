# NCTB Curriculum Stability Analysis — Universal Methodology Playbook

A reusable, subject-agnostic methodology for running 10-year stability analysis on any NCTB textbook line (Class 1-6, any subject). Carry this document into every new conversation to skip re-derivation.

> **Update 2026-05-25 (Class 3 Bangla edition-misclassification lesson).** Added **§16.1 — Edition Confirmation Against the Teacher Guide (D-042)** (folded into the existing §16 TG-Reconciliation section) and a matching **§12** sanity-check row: before finalising any era/framework conclusion, confirm the edition against the Teacher Guide, not the textbook alone.
>
> **Update 2026-05-27 (Math line complete, Classes 1–5).** **§15 Math** rewritten from predicted-only to **field-tested**: NCF-2021 timing is *not* uniform across Math classes (C1=2023, C2=2024, C3=2024, C4=2026, C5=2026 — the old "1–3→2023 / 4–5→2024" prediction is wrong both ends); editions are bimodal (no Stable/Variable tier); watch the C3 trial→settled and C4/C5 front-matter-only sub-revisions; ÷-glyph OCR unreliable; Math is the lowest-risk subject for Islamic alignment. (D-PROJ01-005.)
>
> **Update 2026-05-27 (Math TG-reconciliation retrofit complete, Classes 1–5).** All five Math TGRs done (`completed_C{1–5}_MATH_TGReconciliation_v1.md`; D-PROJ01-006). Recorded the **Math TGR method** in §15 and §16: image-only / **SutonnyMJ legacy-font** Math TGs make `pdftotext` useless → rasterize (`pdftoppm` ~110 DPI) + Tesseract `ben+eng` + **visually verify every chapter opener**; chapter openers carry `অর্জন-উপযোগী যোগ্যতা` + `পাঠ সংখ্যা`, then per-পাঠ `শিখনফল`; পাঠ are **continuously numbered** — use the chain as an inventory-integrity check. Two field lessons: **(1) strand number ≠ chapter number** — read each chapter's যোগ্যতা from its header, never infer "chapter N → strand N" (the C4 case: Ch6 গুণিতক/গুণনীয়ক is strand ২, not ৬); **(2)** watch ৪র্থ-শ্রেণি-পুনরালোচনা review পাঠ at chapter starts — they surface vertical-alignment rungs and explain "off-family" codes. Verdicts were mostly clean validation + enrichment; **C4 carried real corrections** (the proof that Math TGRs need full scrutiny, not enrichment-only assumption).
>
> **Update 2026-05-27 (Science line opened — Classes 3–5 + first Science TGRs; D-PROJ01-007 / D-PROJ01-008).** **§15 Science** rewritten from predicted-only to **field-tested (Classes 3–5)**: NCF timing is again *not* uniform (C3=2024, C4=2026, C5=2026 — matching Math per class); editions bimodal/multi-era; **C3 carries a 2023 Ebtedayi (A\*) Islamic-dress madrasah variant** + a legacy-Bijoy text-only 2024 (`bijoy2unicode`); NCF adds physics/force + astronomy-earth-science + adolescence (C5 বয়ঃসন্ধিকাল) + an explicit objective layer, and drops air/hygiene/soil/food/population; Science is low-risk for Islamic alignment (Sun/earth-motion framed as natural science — softens the universe-origins watch-item; বয়ঃসন্ধিকাল = priority image-level review). **§15/§16 Science TGR method:** Science TGs are **image-only / no-text-layer InDesign** (distinct from Math's SutonnyMJ font; `pdffonts` empty) → rasterize + vision for openers + Tesseract `ben+eng` for the per-পাঠ শিখনফল layer; **পাঠ-numbering convention VARIES by class** (C3 restarts per chapter / 69; C4 & C5 continuous); strand ≠ chapter (carries from Math); **watch chapter-opener পাঠ-count misprints** (C5 Ch13). All three TGRs = clean validation + enrichment. Even though Science is a "future subject" (TG used in-analysis), standalone TGR artifacts + a skeleton-v2 supersede still resulted — plan the TGR artifact + skeleton v2 as deliverables even when no retrofit chat is needed.
>
> **Update 2026-05-28 (BGS line opened — Class 3 + first BGS TGR; D-PROJ01-010).** **§15 BGS** rewritten from predicted-only to **field-tested (Class 3)**: NCF transition at 2024 (matches C3 Math + C3 Science); Era A = frozen পরিমার্জিত-আগস্ট-২০১৫ reprint (২০১৭–২০২৩, ৭ years, ~৮৬ pp); 2024 again arrives as a **legacy-Bijoy text-only file** (`bijoy2unicode`) — same trap as C3 Science 2024. **Unique BGS finding: a 3-step within-era political evolution at chapter slot #3** — 2024 "আমাদের জাতির পিতা" (Bangabandhu solo, carried from Era A Ch10) → 2025 "আমাদের চার নেতা" → **2026 (Sep 2025 reprint) dropped entirely** (Ch4–13 renumbered to Ch3–12). More dramatic than Math C4/C5's front-matter-only de-politicization or Bangla's 28→29 পাঠ insertion — for BGS the de-politicization touches **chapter content directly**. School-favorable outcome at 2026 (no leader chapter remains). NCF adds 10-strand framework (১.x–১০.x) with per-পাঠ 3-part শিখনফল, standalone family-role + child-rights + money-use + emergency-preparedness chapters; drops standalone pollution + social-development + population chapters. **§15/§16 BGS TGR method:** BGS TGs have a **partial text layer** (chapter headers selectable, body image-only — a third category distinct from Math's legacy-font and Science's no-text-layer InDesign); rasterize openers + vision-verify first 2–3 + Tesseract `ben+eng` for rest; **continuous পাঠ numbering** (matches Math, differs from Science); **50-min session** (matches Math + Science). **Unique pitfall: TG-vs-reference chapter-count mismatch** — TG aligned with 2025 (13 ch), but 2026 reference dropped Ch3, requiring **−1 chapter offset for Ch4 onward** when reading the TG alongside a 2026 textbook. Surface the offset table prominently in BGS skeletons (S-02 pattern). **Verdict = clean validation + objective-layer enrichment** (no inventory/tier reversals; mirrors C3 English/Math/Science; explicitly unlike C3 Bangla). **BGS is the highest content-density subject for Islamic-alignment curation** so far (more touchpoints than Math/Science): priority watch-item is যোগ্যতা ৩.৪ in Ch4/Ch5 আমাদের সংস্কৃতি (mandates music/dance/festivals at per-পাঠ level — TG পাঠ ২৪ + ২৫); plus religious-festival-listing in Ch1 body text, TG Ch2 উপকরণ instruction to bring religious-observance images, mixed-gender child illustrations pending image-level sweep. Positive: madrasa positively named in both eras; inquiry pedagogy aligns with school priorities; the 3-row মূল্যায়ন নির্দেশক's third row (দৃষ্টিভঙ্গি ও মূল্যবোধ) is a NCF-native docking point for Islamic-values overlay (Project 03 future).

---

## 0. What This Playbook Is For

You (the user) are an Islamic school principal in Sylhet running a multi-year, multi-subject NCTB textbook stability analysis. The scope:

| Subject (Bangla name) | Class 1 | Class 2 | Class 3 | Class 4 | Class 5 | Class 6 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Bangla (বাংলা) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| English (ইংরেজি) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Math (গণিত / প্রাথমিক গণিত) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Science (প্রাথমিক বিজ্ঞান / বিজ্ঞান) | — | — | ✅ | ✅ | ✅ | ✅ |
| BGS (বাংলাদেশ ও বিশ্ব পরিচয়) | — | — | ✅ | ✅ | ✅ | ✅ |

That's **26 analyses** total. NCF 2021 may have renamed/integrated some subjects in lower classes — when starting each analysis, ask the user how they want the matching NCF subject mapped (e.g., "আমার বাংলাদেশ" might be the Class 3 BGS replacement).

Each analysis produces three deliverables:
1. Comparison report (English, markdown or docx)
2. 7-sheet analysis spreadsheet (xlsx)
3. Curriculum skeleton in Bangla (referenced to the most recent year)

Prior completed analyses (use as references, don't redo):
- **Class 1 Bangla** (2017-2026)
- **Class 1 English** (2017-2026)

---

## 1. First Conversation in Each New Analysis — Locked Questions to Ask

Always ask these upfront before any code runs. Once answered, treat them as **locked** for the rest of the analysis.

### Q1 — Scope confirmation
"Confirm: Class **{N}** **{Subject}** for years **{start}-{end}**?"

### Q2 — Reference year
"Which year should be the reference / target year against which everything else is compared?"
Default: latest available year.

### Q3 — Preservation tiers (carry over from prior analyses)
"Same preservation preferences as prior analyses?
- **Must preserve**: [subject-specific list, see Section 5]
- **Preserve if possible**: vocabulary (cross-year stability tier ii)
- **Flexible**: lesson count, lesson themes"

### Q4 — Subject-specific additions
"For this subject, anything new to track beyond the standard dimensions?"
See Section 5 for default subject dimensions.

### Q5 — Vocabulary split (language subjects only)
"For Bangla/English, same 3-way split (sight / content / action words)? Or different scheme?"
For Math: number sequence + operation symbols + math vocabulary terms.
For Science: concept terms + experiment vocabulary + observable phenomena.
For BGS: place names + cultural terms + historical/civic terms.

### Q6 — Exercise approach
"Same as prior: catalog all types with magnitude across all years?"

### Q7 — Scope depth
"All 10 years deep-analyzed, or sampled (3 per era)?"
Prior analyses chose all 10 years.

### Q8 — Checkpoint preference
"Show intermediate output per chunk and wait for approval, or run end-to-end?"
Prior analyses chose per-chunk approval.

---

## 2. Era Boundary Detection (DO THIS EARLY)

The 2023 NCF 2021 rollout is the dominant boundary, but it didn't hit all classes simultaneously. Verify empirically with this 60-second test:

1. List page counts of all 10 books for the (class, subject) combo
2. Look for the largest year-over-year page-count jump
3. Visually inspect the ToC of the year before and after the jump

Typical pattern (from prior analyses):
- **Era 1**: singleton year (often 2017) — pre-curriculum transition reprint
- **Era 2**: 5-year stable reprint cycle (often 2018-2022) — consistent page count
- **Era 3**: NCF 2021 era (often 2023+) — bigger page count, restructured ToC

The actual boundary year may differ per subject:
- Class 1-3 subjects: NCF rolled out 2023
- Class 4-5 subjects: NCF rolled out 2024 (verify per book)
- Class 6 subjects: NCF rolled out 2023

Always verify visually — don't assume. If 2023 looks like 2022, the boundary is later.

> **Field-tested correction (English line, 2026-05-22).** The "Class 4-5 → 2024" prediction did NOT hold for **Class 4 English**: the old 42-unit edition persisted through **2025**, and the NCF redesign appeared only in **2026** (boundary 2025→2026). This is *later* than Class 2 and Class 3 English, which both broke at 2024. Lower English classes broke earlier than Class 4 English — do not assume Class 4/5 = 2024. Also note: the Class 4 English redesign showed **no page-count jump** (~97→98 pp); the era was marked by ToC *structure* (42 flat units → 18 thematic units), not size. Always confirm the boundary by ToC structure per book.

> **Field-tested note (Bangla line, 2026-05-22).** **Class 2 Bangla** broke at **2024** (90→74 pp), the *same* boundary as Class 2/3 English — confirming the lower-class 2024 pattern holds across subjects. Two extra Bangla-specific cautions emerged: **(1)** the *page count clearly jumped* here (unlike Class 4 English), but always still confirm via the সূচিপত্র — the Era-A book is a *reprint of the আগস্ট ২০১৪ revised edition* (পরিমার্জিত শিক্ষাক্রম ২০১১), the Era-B book a fresh *প্রথম মুদ্রণ ২০২৩* under PEDP4. **(2)** A genuine **within-era sub-revision** was found *inside* Era B: the 2024 first edition had **28 পাঠ**, but from **2025** the book carries **29 পাঠ** (a fable inserted at পাঠ ৮, plus two retitles). Do not assume all years inside an era are identical — spot-check the ToC of the first edition vs later years of the same era.

---

## 3. File Format & Upload Hygiene

NCTB books from your archive arrive as `.pdf` files but with two underlying formats:
- **ZIP-of-JPEGs** (most files): a ZIP archive of numbered page images. Despite the `.pdf` extension, use `unzip` to extract.
- **Real PDF** (occasionally): an actual PDF that needs `pdftoppm -jpeg -r 150` to convert to JPEGs.

Always check the format first:
```bash
file your_book.pdf   # reports "Zip archive" or "PDF document"
```

If a file arrives as ~200 bytes of whitespace, the upload failed — ask the user to re-upload via the chat (not the project).

**Uploads are ephemeral — keep a persistent working file.** Uploaded books and Teacher Guides live only in `/mnt/user-data/uploads/` and are **cleared when the session resets** (including after a “limit reached” continuation). For any long, multi-batch extraction, write your running results to a persistent working file on disk (e.g. `/home/claude/<subject>_ledger.md`) as you go, and re-request the upload if it disappears. A reset then costs only the current batch, never the data already extracted.

---

## 4. Environment Setup (Same for Every Analysis)

Tools available in Claude's sandbox:
- `tesseract` 5.x — **must verify language pack** before starting
- `pdftoppm` (poppler-utils)
- Python 3 with `PIL` (Pillow)
- `unzip`, `bash`

**Language pack check (CRITICAL for non-English subjects):**
```bash
tesseract --list-langs
# Should show: eng osd
# For Bangla subjects you NEED: ben
```

If `ben` is missing for a Bangla/Math/Science/BGS analysis, install:
```bash
apt-get install -y tesseract-ocr-ben
# or
sudo apt install tesseract-ocr-ben
```

If `ben` is missing **and cannot be installed** (the sandbox often has no network for `apt-get`), do **not** block — fall back to **visual reading**: rasterize the pages (`pdftoppm -png -r 130`), optionally crop to the region of interest, and read the Bangla directly with the `view` tool. Claude's vision is more reliable than `tesseract` for Bangla — especially conjunct-heavy (যুক্তবর্ণ) text and the per-lesson objective blocks of a Teacher Guide (§16) — so visual reading is the **preferred** path for image-only Bangla *objective* extraction even when OCR is present. Read in bounded batches and record to the persistent working file (§3) as you go.

OCR speed: ~1 sec/page with 4-way xargs parallelism on a single CPU. For 800 pages, budget 15 minutes.

---

## 5. Per-Subject Dimensions to Track

Each subject has a default set of preservation dimensions. Customize per user input.

### 5.1 Bangla (বাংলা)
- **Letter/vowel/consonant sequence**: order of introduction (স্বরবর্ণ → ব্যঞ্জনবর্ণ → যুক্তবর্ণ)
- **Conjunct (যুক্তবর্ণ) coverage** — class-dependent
- **Matra / kar / fola** introduction
- **Grammar concepts**: simple/complex, কারক, বিভক্তি (mostly Class 3+)
- **Sentence patterns**: declarative/interrogative/imperative templates
- **Vocabulary (3-way)**: function words / content words / verbs
- **Exercise types**: শোনো-বলো, লেখো, পড়ো, মিল করো, বানাও, etc.
- **Learning outcomes** (derived from activities + concepts)

### 5.2 English
- **Letter sequence**: A-Z order, case treatment (upper vs lower introduction)
- **Grammar concepts**: pronouns, be-verbs, articles, demonstratives, question words, contractions, prepositions, imperatives, greetings/politeness
- **Sentence patterns**: substitution templates ("This is a ___", "What's your name?", "I live in ___")
- **Vocabulary (3-way)**: sight / content / action
- **Exercise types**: look_listen, trace_write, read_match, etc.
- **Learning outcomes** (derived)

### 5.3 Math
- **Number sequence**: how high does counting go in each class; numeral introduction order
- **Operation introduction**: when do `+`, `-`, `×`, `÷` first appear?
- **Math vocabulary terms**: counting (গণনা), greater/less (বেশি/কম), shape names, fraction terms
- **Problem types**: oral counting, written sums, word problems, comparison, ordering, geometry, measurement, time, money
- **Symbol coverage**: `=`, `<`, `>`, `+`, `-`, `×`, `÷`
- **Exercise types**: গণনা করো, যোগ করো, বিয়োগ করো, মেলাও, লেখো, আঁকো, etc.
- **Learning outcomes** (derived)

### 5.4 Science (প্রাথমিক বিজ্ঞান)
- **Concept introduction sequence**: living/non-living, plants, animals, body, weather, water, environment, etc.
- **Observation/experiment activities**: count + types
- **Classification systems**: animal types, plant types, materials, etc.
- **Scientific vocabulary terms**
- **Cross-cutting themes**: environment, health, technology
- **Exercise types**: পর্যবেক্ষণ করো, পরীক্ষা করো, লেখো, ছবি আঁকো, শ্রেণিবিন্যাস করো
- **Learning outcomes** (derived)

### 5.5 BGS / Bangladesh & Global Studies
- **Topic sequence**: family → community → district → country → world (typical scaffolding)
- **Geographic coverage**: places mentioned per book (villages, rivers, districts, countries)
- **Historical/civic concepts**: independence, national heroes, government, rights/duties
- **Cultural content**: festivals, religions, customs
- **Vocabulary terms**: civic/geographic
- **Exercise types**: recall, match, explain, locate on map, project work
- **Learning outcomes** (derived)

---

## 6. Class-Level Adaptations

| Class | Cognitive expectations | What changes in dimensions |
|---|---|---|
| 1-2 | Recognition, pictographic, simple production | Letter/numeral focus dominant; exercises heavily multimodal (look/listen/trace/say); vocab small |
| 3-4 | Transition to text-heavy; explicit grammar/concept teaching begins | Grammar concepts taught explicitly (not just embedded); paragraph-length reading appears; new subjects begin (Science, BGS) |
| 5-6 | Abstract reasoning; explicit rules and definitions | Grammar rules formalized; complex problem-solving in Math; experimental method in Science; longer reading passages |

**Body page ranges** will differ from Class 1 (which typically has 7-97 page bodies). For higher classes, expect larger books (100-200 pages). Always verify per book.

**Era-3 hierarchical restructuring**: NCF 2021 books across all classes share the pattern of 4-6 thematic units instead of 20-30 flat chapters. Verify but expect this.

---

## 7. Universal OCR Gotchas (READ BEFORE WRITING CODE)

These tripped me in Class 1 English. Watch for them in any analysis.

1. **Two-column ToC layouts.** Whole-page OCR garbles columns into mixed lines. Fix: image-split at 50% with small overlap, OCR each column separately. Applies to MOST NCTB books with side-by-side unit listings.

2. **Multi-column vocab/glossary pages.** Same problem, sometimes 3 columns. Use tight column splits with 2x upscaling via `PIL.Image.LANCZOS`.

3. **A-PDF watermarks** appear on older books (2017-era reprints): `"A-PDF To Image DEMO: Purchase from www.A-PDF.com to remove the watermark"`. Filter before any text counting:
   ```python
   WATERMARK_RE = re.compile(r"A-?PDF|Image DEMO|remove the watermark", re.IGNORECASE)
   ```

4. **OCR misreads in bold text.** `I` → `L`, `s/S` confusion in dialogues. Common in Q&A and rhyme sections. Add OCR variant patterns to regex (e.g., `(?:I|L)` instead of just `I`).

5. **Bangla OCR is harder than English.** Tesseract `ben` is significantly less accurate. Plan for:
   - Lower confidence on conjuncts (যুক্তবর্ণ)
   - Common confusion: ব/র/স, কিছু matras dropped
   - Use `--psm 6` and consider 2x upscaling for body pages too
   - May need to visually verify more pages

6. **OCR garbles small numerals in italic-style ToC.** Era 1/2 books often use stylized small numbers that Tesseract reads as `{|`, `'6`, `\3`, etc. Build a prefix-to-number lookup map for parsing.

7. **Era-3 imperative case inconsistency.** Bold imperatives in NCF 2021 books sometimes lose case (`Listen` → `listen`). Activity-line regex must accept lowercase first word.

8. **No vocab section in NCF 2021 books.** Era 3 typically drops the explicit vocab list. Mine vocab from body text with min-2-occurrence filter.

9. **Page-numbering quirk in some books**: first numbered page is "iii" or actual page 1 may be book-page 2. Visually verify body page ranges before mining.

10. **Math notation OCR.** Tesseract may read `+` as `t`, `=` as `==` or `--`, `×` as `x`. For Math analyses, run a math-symbol detector before generic text analysis.

---

## 8. Standard Pipeline (Subject-Agnostic Chunks)

| # | Chunk | Output |
|---|---|---|
| 1 | Setup + ZIP/PDF extraction | `pages/<year>/N.jpeg` |
| 2 | OCR all pages | `ocr/<year>/N.txt` |
| 3 | ToC parsing → lesson catalog | `lesson_catalog.json` |
| 4 | Front/back matter inventory | (often skipped) |
| 5 | **Dimension 1**: subject-primary (letters / numbers / concepts / topics) | `<dim1>.json` |
| 6 | **Dimension 2**: vocabulary 3-way (or subject equivalent) | `vocabulary_analysis.json` |
| 7 | **Dimension 3**: exercise/activity catalog with magnitude | `exercise_catalog.json` |
| 8 | **Dimension 4**: grammar/concept/structural patterns | `grammar_concepts.json` or `concept_inventory.json` |
| 9 | **Dimension 5**: sentence patterns / problem patterns / observation templates | `sentence_patterns.json` |
| 10 | Learning outcomes (derived from chunks 5-9) | `learning_outcomes.json` |
| 11 | Deliverables (report + xlsx + skeleton) | 3 files |

Run with **per-chunk approval**: produce output, summarize findings, ask "Approve and proceed to Chunk N+1?" Wait for explicit approval.

---

## 9. Standard Workspace Layout

```
/home/claude/nctb_<subject_class>/
├── pages/<year>/<N>.jpeg          # extracted page JPEGs
├── ocr/<year>/<N>.txt             # whole-page OCR
├── ocr_toc/<year>_combined.txt    # column-split ToC OCR
├── ocr_vocab/<year>_p<P>_combined.txt   # if a vocab section exists
├── extracted/                     # final analysis JSONs
└── progress.json
```

Persist a copy of `extracted/` and `ocr/` to `/mnt/user-data/outputs/<subject_class>_analysis/` periodically so partial work survives session timeouts.

---

## 10. Reusable Code Patterns

### 10.1 File format detection
```python
import subprocess, re
result = subprocess.run(['file', filepath], capture_output=True, text=True)
if 'Zip archive' in result.stdout:
    # unzip into pages dir
    pass
elif 'PDF document' in result.stdout:
    # pdftoppm -jpeg -r 150
    pass
```

### 10.2 Parallel OCR with year-batching
```bash
# Build job list
for d in pages/*/; do
  year=$(basename "$d")
  mkdir -p "ocr/$year"
  for img in "$d"*.jpeg; do
    pg=$(basename "$img" .jpeg)
    echo "$img ocr/$year/$pg"
  done
done > ocr_jobs.txt

# 4-way parallel — change -l flag for Bangla subjects
cat ocr_jobs.txt | xargs -L1 -P 4 bash -c \
  'tesseract $0 $1 -l eng --psm 6 2>/dev/null'
# Bangla: -l ben
# Mixed (Math with Bangla instructions + numerals): -l ben+eng
```

### 10.3 ToC column-split
```python
from PIL import Image
img = Image.open(toc_path)
w, h = img.size
left  = img.crop((0,           0, int(w * 0.52), h))
right = img.crop((int(w*0.48), 0, w,             h))
# Save each, OCR with --psm 6, concatenate left + "\n--- RIGHT ---\n" + right
```

### 10.4 Vocab 3-column split (if subject has explicit vocab section)
```python
col1 = img.crop((0,            0, int(w*0.33), h))
col2 = img.crop((int(w*0.33),  0, int(w*0.66), h))
col3 = img.crop((int(w*0.66),  0, w,           h))
# Upscale narrow strips 2x with Image.LANCZOS before OCR
```

### 10.5 Watermark filtering
```python
WATERMARK_RE = re.compile(r"A-?PDF|Image DEMO|remove the watermark", re.IGNORECASE)
clean = "\n".join(L for L in raw.splitlines() if not WATERMARK_RE.search(L))
```

### 10.6 Tier-ii stability tiers (cross-year)
```python
# Global (all 10 years)
if n == 10:    tier = 1  # universal
elif n >= 6:   tier = 2  # stable
elif n >= 2:   tier = 3  # drift
else:          tier = 4  # singleton

# Within-era (ratio-based)
ratio = years_present / era_size
if ratio == 1.0:   tier = 1
elif ratio >= 0.6: tier = 2
elif ratio >= 0.2: tier = 3
else:              tier = 4
```

### 10.7 Exercise magnitude tiers (cross-year totals)
```python
if total >= 100: "tier_A_dominant"
elif total >= 30: "tier_B_frequent"
elif total >= 10: "tier_C_occasional"
elif total >= 3:  "tier_D_rare"
else:             "tier_E_marginal"
```

### 10.8 Trend classification (per concept across eras)
```python
e2_yr = era2_total / num_era2_years
e3_yr = era3_total / num_era3_years
prev_max = max(e1_total, e2_yr)

if prev_max == 0 and e3_yr > 0:      trend = "Era_3_NEW"
elif prev_max > 0 and e3_yr == 0:    trend = "Era_3_DROPPED"
elif e3_yr > 1.5 * prev_max:         trend = "Era_3_RISING"
elif e3_yr < 0.5 * prev_max and e3_yr > 0:  trend = "Era_3_DECLINING"
elif total_all == 0:                 trend = "NEVER_USED"
else:                                trend = "STABLE"
```

### 10.9 OCR number-prefix repair (ToC parsing — Era 1/2 small italic numerals)
```python
PREFIX_TO_NUM = {
    "{|":11, "{i":11, "{l":11,
    "\\2":12, "{2":12,
    "13.":13, "\\3":13, "{3":13,
    "!4":14, "\\4":14,
    "'5":15, "‘5":15,
    "‘6":16, "'6":16, "!6":16,
    "‘7":17, "'7":17, "!7":17,
    "‘8":18, "'8":18, "!8":18,
    "'9":19, "‘9":19, "!9":19,
    "2|":21, "2{":21, "2l":21,
}
```

---

## 11. Deliverables Templates

### 11.1 Comparison Report (English, Markdown/DOCX)
Structure:
1. **Executive summary** (1 page) — what's stable, what changed, top recommendations
2. **Era boundaries** — page counts table, structural changes, justification
3. **Lesson catalog** — side-by-side ToCs, within-era stability
4. **Per-dimension findings** — one section per Chunk 5-10, each ending with a "preservation verdict" for the user's school
5. **Recommendations** — concrete adoption guidance for the reference year
6. **Known limitations** — OCR caveats, dimensions that couldn't be reliably measured

### 11.2 7-Sheet Analysis Spreadsheet (XLSX)
| Sheet | Content |
|---|---|
| 1. Overview | Era boundaries, page counts per year, decisions locked |
| 2. Lesson catalog | All 10 years side-by-side (units/lessons), within-era diffs highlighted |
| 3. Primary dimension | Letters / Numbers / Concepts / Topics (subject-specific) |
| 4. Vocabulary | 3-way buckets, per-year counts, tier classification, universal core |
| 5. Exercise catalog | Types × Years matrix, magnitude tiers, era-specific types flagged |
| 6. Grammar/Concept patterns | Per-concept counts, trend classification |
| 7. Sentence/Problem patterns | Templates × Years, trend classification |

Add an 8th sheet for Learning Outcomes if it warrants standalone treatment.

### 11.3 Curriculum Skeleton (Bangla, DOCX/MD)
Format:
- Based on the reference year's structure (typically the latest year's unit/lesson hierarchy)
- Per unit/lesson, annotate every element with preservation status:
  - 🟢 **মূলে রাখতেই হবে** (must preserve) — universal across all eras
  - 🟡 **পারলে রাখুন** (preserve if possible) — stable in reference era
  - 🔴 **নতুন সংযোজন** (new addition) — Era 3 only
  - ⚪ **নমনীয়** (flexible) — varies; teacher's choice
- Cross-reference to chunk outputs for backup data

---

## 12. Sanity Checks Per Analysis

After running the pipeline for a new (class, subject) combination, verify against these patterns:

| Check | Expected behavior |
|---|---|
| Page count progression | Roughly stable in Era 1/2, jumps in Era 3 |
| Within-Era-2 lesson count stability | Should be near-identical across years 2018-2022 |
| Within-Era-3 lesson count stability | Should be near-identical across years 2023-2026 |
| Primary dimension universal core | Always has some non-empty universal set |
| Exercise types preserved | Some types appear in all 10 years (the "spine") |
| At least one Era_3_NEW concept | NCF 2021 always adds something |
| At least one Era_3_DROPPED concept | NCF 2021 also removes something |
| **Edition confirmed against the Teacher Guide?** | **The era/framework conclusion must be checked against the TG, not the textbook alone — see §16.1 (D-042). A textbook-only pass can misread the edition.** |

If a check fails dramatically, investigate before publishing.

---

## 13. Communication Style With User

The user prefers:
- Concise responses with tables, not walls of prose
- Direct findings, not method narration
- Per-chunk checkpoint with explicit "Approve and proceed to Chunk N" prompt
- Bullets and tables where structural, prose elsewhere
- Don't re-ask questions answered earlier in the same analysis
- Honest flagging of OCR/measurement limitations rather than papering over them
- When OCR fails, show the raw OCR snippet so the user can verify rather than re-running blindly

The user has **good technical instincts** — they'll catch hand-waving. Be specific about what was measured and how.

---

## 14. How to Start a New Analysis in a Fresh Conversation

Paste a starter prompt like this:

> I'm running a 10-year NCTB stability analysis for **Class {N} {Subject}** (years {start}-{end}). I have a universal methodology playbook from prior analyses (Class 1 Bangla, Class 1 English).
>
> [attach this playbook .md file + the 10 PDF files for this analysis]
>
> Please read the playbook, then:
> 1. Confirm scope and reference year
> 2. Check file integrity (any zero-byte / corrupted uploads?)
> 3. Ask any subject-specific questions from Section 1 that aren't already answered
> 4. Verify era boundaries empirically (Section 2)
> 5. Then run the pipeline with per-chunk approval
>
> Use Section 5's subject-specific dimensions for {Subject}. Use Section 10's reusable code patterns. Watch for Section 7's OCR gotchas.

The new Claude should be self-sufficient with just this playbook + uploads.

---

## 15. Subject-by-Subject Notes (Field-Tested + Predicted)

### Bangla (already done for Class 1)
- Requires Bangla Tesseract pack
- Letter sequence: স্বরবর্ণ first, then ব্যঞ্জনবর্ণ
- Vocabulary phrases often include matra-bearing words; encoding matters
- Class 3+ adds explicit grammar (পদ, বাক্য, লিঙ্গ, বচন)
- **Class 2 Bangla field notes (2026-05-22):**
  - **Boundary at 2024** (90→74 pp). Era A 2017–2023 = পরিমার্জিত শিক্ষাক্রম ২০১১ reprints (imprint: প্রথম মুদ্রণ আগস্ট ২০১২ / পরিমার্জিত আগস্ট ২০১৪ / পুনর্মুদ্রণ <year>); Era B 2024–2026 = NCF 2021 (প্রথম মুদ্রণ ২০২৩, PEDP4).
  - **Content turns over heavily — unlike English.** Where English kept most lessons across the boundary, Class 2 Bangla *dropped ~9 Era-A lessons and added ~14 Era-B lessons*. **Do not assume text continuity for Bangla.** What survives is the **mechanics ladder** (বর্ণ → কার → ফলা → রেফ → যুক্তবর্ণ — taught every year, embedded in Era A vs. named single-topic lessons in Era B), the **শুনি–বলি–পড়ি–লিখি** skill spine, and a handful of **heritage texts** (the same Tagore/Nazrul/Bhattacharya poems + the Prophet ﷺ trench story *সবাই মিলে কাজ করি*).
  - **Within-era sub-revision exists:** Era B 2024 = 28 পাঠ (first ed) → 2025–2026 = 29 পাঠ (added *সিংহ আর ইঁদুরের গল্প* at পাঠ ৮; retitled *পয়লা বৈশাখ*→*নববর্ষ*, *সোনার ছেলে*→*দুখু মিয়ার জীবন*). Always compare the first-edition ToC of an era against later years.
  - **ToC location & form:** Era A puts the **সূচিপত্র mid-front-matter** (≈ book-page 11) and lists lessons **by title only — no "পাঠ N" numbering**; Era B uses a **numbered পাঠ** সূচিপত্র (ক্রম / পাঠের নাম / পৃষ্ঠা). A header regex of `পাঠ\s*[০-৯]+` finds Era-B lessons but **misses Era A entirely** — read the সূচিপত্র image instead.
  - **All 10 books were image-only** (2017–2025 = ZIP-of-JPEG mislabeled `.pdf`; 2026 = real but image-only PDF). OCR conjuncts/chandrabindu/matra unreliable (ঋ in *ঋতু*, ঁ in *ইঁদুর*, *ছোট* vs *ছোটো* all caused false-negatives) — verify catalogs visually.
  - **Era B per-lesson *শব্দ শিখি* boxes replace** the Era-A single end-glossary *শব্দের অর্থ জেনে নিই*. Era B also drops the formal *অনুশীলন* block in favour of activity-embedded prompts and raises matching / word-building / free-expression (*নিজের মতো লিখি*, *বাক্য নিয়ে খেলা*).

### English (already done for Class 1)
- Latin alphabet; English Tesseract pack sufficient
- Class 1 = letters + sight words; Class 4+ = paragraphs + tense + parts of speech

### Math (field-tested Classes 1–5 + predicted Class 6)

**Field-tested — Classes 1–5 Math complete (2026-05-27, `completed_C{1–5}_MATH_*`):**

- **NCF-2021 transition timing is NOT uniform across Math classes** (the single most important field correction). Empirical first-NCF year by class: **C1 = 2023, C2 = 2024, C3 = 2024, C4 = 2026, C5 = 2026**. Lower classes (1–3) broke in 2023–2024; upper classes (4–5) broke at **2025→2026**. The earlier "Class 1–3 → 2023 / Class 4–5 → 2024" prediction is wrong on both ends — confirm the boundary from the ToC + imprint per class, never assume.
- **Editions are bimodal (clean replacement, not drift):** within an era the books are ToC-identical reprints; a concept is either Universal Core (all years) or confined to one edition, so **expect no Stable/Variable tier** (sharply bimodal). Two within-era sub-revisions to watch: C3's Era B has a 2024 *trial* printing (পরীক্ষামূলক, 150 pp) that settled to 162 pp by 2025=2026; C4/C5's 2025 is a **front-matter-only** de-politicized re-issue (পরিমার্জিত অক্টোবর ২০২৪) — for Math the body is unchanged (unlike Bangla, where de-politicization touched lesson content). **Always compare the first-edition ToC of an era against later years.**
- **Universal Core spine (stable across classes):** number & place value, the four operations (+ − × ÷) and their symbols, four-operation word problems, fractions, measurement (length/weight/volume/time), currency, geometry, and data handling (from the class it appears). **Tier can differ by class** — place value is Era-3-only in C1 Math but Universal Core by C3; all four operations are UC by C3.
- **What NCF moved, per class:** C2 dropped Division + Fractions, added Pattern/Data/place-value-strand + ×0/×1 tables; C3 raised the number range to lakh and added Data + two inverse-relationship chapters (যোগ↔বিয়োগ, গুণ↔ভাগ); C4 dropped formal ল.সা.গু/গ.সা.গু (LCM/GCD) + the standalone Time chapter, added prime factorization/divisibility + চতুর্ভুজ; C5 merged গুণ+ভাগ+চার প্রক্রিয়া, reframed গাণিতিক প্রতীক → গাণিতিক বাক্য, folded সময় into পরিমাপ, and dropped ক্যালকুলেটর ও কম্পিউটার (the one true C5 deletion).
- **OCR:** all books are image-only scans; install the Bangla pack (`-l ben+eng`). The **÷ glyph is unreliable** (× sometimes reads `x/X`); confirm division via instructions / long-division layout, not the glyph, and run a symbol detector before generic text analysis. **Trust tier/era classifications over absolute counts** (~92–95% on illustrated Bangla).
- **Islamic-alignment: Math is the lowest-risk subject so far** (values-neutral). C5 favorable — no riba/সুদ, no gambling, no alcohol, no idolatry; Islamic contexts (নামাজ/মসজিদ/ঈদ/রোজা/হজ) present and rising; the percentage chapter uses profit/loss (লাভ/ক্ষতি), not interest. Flags routed to curation: rising music/song word-problem contexts (C5); a C3 sports-day example with মোরগ লড়াই (cockfighting) + যেমন খুশি তেমন সাজো (fancy-dress); mixed-gender child illustrations + living-being imagery throughout (image-level, not OCR-assessable). **Positive:** the C4 TG opens lessons with সালাম (×48).
- **TG status: Math TGR retrofit COMPLETE, Classes 1–5 (2026-05-27, D-PROJ01-006).** All five `completed_C{1–5}_MATH_TGReconciliation_v1.md` produced and propagated. **Method (field-tested):** Math TGs render with **SutonnyMJ legacy (WinAnsi, non-Unicode) fonts** → `pdftotext` is useless; rasterize (`pdftoppm` ~110 DPI) → Tesseract `ben+eng` → **visually verify every chapter opener** (`অর্জন-উপযোগী যোগ্যতা` + `পাঠ সংখ্যা`, then per-পাঠ `শিখনফল`); পাঠ are **continuously numbered** (use the chain as an inventory check); offset printed + 7 = PDF page (seen across classes); each পাঠ ≈ a **50-min period** (5 / 40 / 5); every পাঠ carries a **মূল্যবোধ ও দৃষ্টিভঙ্গি / মূল্যায়ন** values row. **Watch two things:** (1) **strand number ≠ chapter number** — read each chapter's যোগ্যতা from its header, never infer "chapter N → strand N" (C4: Ch6 গুণিতক/গুণনীয়ক sits on strand ২, not ৬); (2) **৪র্থ-শ্রেণি-পুনরালোচনা review পাঠ** at chapter starts surface vertical-alignment rungs and explain "off-family" codes. **Verdicts:** C1/C2/C3/C5 = clean validation + enrichment; **C4 carried real corrections** (Ch6 → ২.৮; Ch2 → ২.৩ with ২.৬ reseated to Ch4 ভাগ; সময় retained as ৭.৪ inside পরিমাপ) — so do **not** assume Math TGRs are enrichment-only; verify each chapter's যোগ্যতা and re-check Time / LCM-GCD coverage. C2's true period count is **110 পাঠ** (not the stability report's "~90"). **Downstream folds still owed (staged):** five `completed_C{n}_MATH_Skeleton_v2.md` + the Math REF-19 vertical-map fill (third subject).

**Predicted (not yet field-tested):**
- Class 6: introduction of algebra.
- Exercise-type spine seen across Classes 1–5: গণনা, যোগ, বিয়োগ, গুণ, ভাগ, মেলাও, লেখো, আঁকো, পরিমাপ, সমাধান করো; NCF adds complete-the-pattern, collect-and-organise-data, and a self-check step (নিজে করি / "দেখি পারি কি না").

### Science (field-tested Classes 3–5 + predicted Classes 1–2/6)

**Field-tested — Classes 3, 4 & 5 Science complete (2026-05-27, `completed_C{3,4,5}_SCI_*`; D-PROJ01-007/008). Science is the 4th subject line done (after Bangla/English/Math).**

- **NCF-2021 transition timing is NOT uniform across Science classes either** — empirical first-NCF year: **C3 = 2024, C4 = 2026, C5 = 2026.** C3 broke earlier (2023→2024) than the upper classes (2025→2026); confirm the boundary from ToC + imprint per class. (C3 Science's 2024 break matches C3 Math; C4/C5's 2025→2026 matches C4/C5 Math — Science migrated on its own schedule but landed on the same per-class years as Math.)
- **Editions are bimodal/multi-era (clean replacement, not drift):** within an era the books are ToC-stable reprints; expect no Stable/Variable middle tier (a frozen-then-replaced history). **Watch a madrasah-track variant:** C3's **2023 is an Ebtedayi (A\*) edition** — the same old 12-ch structure with the guide-characters redrawn in Islamic dress (হিয়া in hijab, রেজা in টুপি) — a single madrasah year sitting inside an otherwise general-track series. Tag it distinctly (**A\***), don't blend. **The NCF redesign roughly doubles the page extent and resequences chapters** (opens with life science, inserts physics + earth/space science mid-book, closes on technology/ICT).
- **NCF additions seen across classes:** **physics/force** (C3 বস্তুর উপর বলের প্রভাব; C4 গতি ও বল + standalone শক্তি; C5 বলের ধারণা + পদার্থের গঠন + শক্তির রূপান্তর — a 1→3 physics split at C5), **astronomy/earth science** (C3 জীবনের জন্য সূর্য; C5 ভূমিরূপ landforms + পৃথিবীর গতি), an **adolescence** chapter (C5 বয়ঃসন্ধিকাল), an explicit **উদ্ভিদ/প্রাণী split** (C3), and **problem-solving ICT** (C4 B11). **NCF drops as standalone:** environment, air, hygiene (→food/health), soil, food, population.
- **Universal Core spine (survives both eras):** matter, energy, water, soil, food/nutrition, technology, information & communication, living things; the core science lexicon; and the **inquiry pedagogy** — lead question → কাজ (observe/experiment) → আলোচনা (discuss) → সারসংক্ষেপ/summary. Structural conventions persist: guide-characters (C3 হিয়া/রেজা; C4 কেয়া/কাব্য; C5 দিপু/ঝুঁই) and the কাজ/আলোচনা/সাবধান হও symbol system. NCF adds graphic organisers, the **"আরও কিছু জানি"** extension box (C5), and an explicit **যোগ্যতা → শিখনফল** objective layer.
- **OCR / confidence:** all books image-only scans; structure (ToC/imprint/chapter openers) reads HIGH-confidence by vision; flowing-text OCR ~92–95%. **Watch a legacy-encoding trap:** C3's 2024 arrived as a legacy **Bijoy/SutonnyMJ** `.pdf`-named *text* file → convert with `bijoy2unicode` (text-only, no page images = lowest-confidence year). **Trust tier/era classifications over absolute counts.**
- **Islamic-alignment: Science is low-risk overall, with a few standing watch-items** routed to curation (observational only): universe/earth-origins framing — check the Sun / মহাবিশ্ব / পৃথিবীর গতি chapters against the creation narrative (the TGRs found these framed as **observational/natural science, not reverence**, which *softens* the watch-item); the **C5 বয়ঃসন্ধিকাল (adolescence)** chapter → biological/health framing + chart/poster methods = **priority image-level review**; growth & reproduction content (C4); mixed-gender child characters + living-being illustrations throughout; isolated গান/নাচ page mentions (verify on the image edition — no music/dance pedagogy detected). **Positive:** strong hygiene/cleanliness (Islamic etiquette), environmental care, and a native free-thinking pedagogy (যুক্তি-পাল্টাযুক্তি, একাকী চিন্তা, POE Predict-Observe-Explain).
- **TG status: first Science TGRs COMPLETE, Classes 3–5 (2026-05-27, D-PROJ01-008).** All three `completed_C{3,4,5}_SCI_TGReconciliation_v1.md` produced. **Method (field-tested):** Science TGs are **born-digital InDesign but have NO text layer** (image-only; `pdffonts` empty, `pdftotext` returns nothing) → rasterize chapter openers (110–200 DPI) + **vision-verify** যোগ্যতা + পাঠ সংখ্যা + numbering (HIGH), then **Tesseract `ben+eng`** for the per-পাঠ শিখনফল layer (fetch `ben.traineddata` — not preinstalled). Science pages render **cleaner than the Math TGs' SutonnyMJ legacy font**, so per-পাঠ OCR is more reliable — but still expect occasional Bangla-digit sub-index flips → anchor to the chapter competency family and spot-verify. **পাঠ-numbering convention VARIES by class:** C3 **restarts per chapter** (sums to 69 book-wide); C4 & C5 **number continuously** (C4 73 পাঠ, C5 92 পাঠ) — use the chain as an inventory-integrity check, and **watch the chapter-opener পাঠ-count line, which can misprint** (C5 Ch13 printed "১২টি (৮৩-৯১)" but the true span is পাঠ ৮৩–৯২; cross-check against the contiguous পাঠ chain + the closing মূল্যায়ন নির্দেশক-N). Each পাঠ states its পাঠ্যপুস্তকের পৃষ্ঠা নম্বর (capture the পাঠ↔textbook-page link) and ≈ a **50-min period**; per-পাঠ carries শিখনফল + উপকরণ + পদ্ধতি + কার্যাবলি + a **মূল্যায়ন নির্দেশক (জ্ঞান / দক্ষতা / দৃষ্টিভঙ্গি ও মূল্যবোধ)** values triad. **Two field lessons (carry from Math):** (1) **strand number ≠ chapter number** — read each chapter's যোগ্যতা from its own header (C4 Energy Ch5 = ৩.৪ within the Matter strand; both C4 ICT chapters share ৭.১, no ৭.২); (2) printed codes can carry **typos** (C3 Ch9 printed শিখনফল ৪.১.১ but it belongs to যোগ্যতা ৬.১ → recorded ৬.১.১). **Verdicts: all three = clean validation + objective-layer enrichment** (no inventory/tier reversals — unlike the C4 Math TGR). **Note on rollout shape:** although Science is a "future subject" (TG used in-analysis, no separate retrofit chat), standalone TGR artifacts + a skeleton-v2 supersede still resulted — so even for future subjects, plan for the TGR artifact + skeleton v2 as deliverables. **Downstream folds still owed (staged):** `completed_C3_SCI_Skeleton_v2.md` + `completed_C4_SCI_Skeleton_v2.md` (C5's v2 built), a C4 `StabilityReport` patch (69→73 + soften universe-origins) + a C3 confirmatory note, and the **net-new Science REF-19 vertical-map + Science Subject-Spine seeds** (Science is the newest subject — no Science REF-19 rungs or Science spine exist yet; Classes 1–2 Science still pending will complete the rungs).

**Predicted (not yet field-tested — Classes 1–2 Science + Class 6):**
- Classes 1–2: Science is often lighter / integrated — confirm whether a standalone প্রাথমিক বিজ্ঞান exists at those classes or whether the content sits inside an integrated book; the Science REF-19 rungs complete only once C1–C2 are analysed.
- Class 6: expect the secondary-style subject split (Physics / Chemistry / Biology strands begin to formalise).
- The original predicted concept-sequence (self → body → plants/animals → environment → matter → energy → technology) **partly held**, but NCF resequences to lead with life science and insert physics/earth-science mid-book; cross-curricular integration with Math (measurement) and BGS (environment) confirmed.

### BGS (field-tested Class 3 + predicted Classes 4–6)

**Field-tested — Class 3 BGS complete (2026-05-28, `completed_C3_BGS_*`; D-PROJ01-010). BGS is the 5th subject line opened (after Bangla/English/Math/Science). The first BGS TGR also produced in the same chat — establishing the BGS-side reconciliation method.**

- **NCF-2021 transition timing for C3 BGS = 2024** — empirical first-NCF year matches C3 Math and C3 Science (all three C3 subjects broke at 2024). The boundary is established by **complete TOC restructuring** (12 ch পরিমার্জিত-২০১৫ → 12–13 ch NCF-২০২১), not page count alone. Era A (২০১৭–২০২৩, ৭ years) = **frozen** ~৮৬-pp reprint of the আগস্ট ২০১৫ পরিমার্জিত edition; Era B = NCF 2021. Confirm per Class 4–6 when those analyses begin; do not assume the C3 timing.
- **Era B carries an UNUSUAL 3-step within-era political evolution at chapter slot #3 — unique to BGS so far.** 2024 (Oct 2023 first edition) Ch3 = "আমাদের জাতির পিতা" (Bangabandhu solo, carried from Era A Ch10) → 2025 (Oct 2024 revised) Ch3 = "আমাদের চার নেতা" (Fazlul Huq + Bhasani + Suhrawardy + Mujib) → **2026 (Sep 2025 reprint) Ch3 dropped entirely** (Ch4–13 renumbered to Ch3–12). The 2026 textbook is the first in nine years of Class-3 BGS reprints to carry no political-figure chapter — school-favorable trajectory. This is more dramatic than the Math C4/C5 front-matter-only de-politicization and the Bangla 28→29 পাঠ insertion: for BGS the de-politicization touches **chapter content directly**. **Always check TOC of every Era-B year for BGS subjects; do not assume reprint = identical content.**
- **Universal Core spine (survives both eras):** environment · coexistence · continents & oceans (exact title preserved) · country (Bangladesh) · professions · ethical/humane qualities · history · culture (Era A combined; Era B split into two standalone chapters) · the inquiry pedagogy · end-glossary · positive madrasa mention. **9 topic clusters carry forward.** Track place-name coverage and the within-Era-B political variability as unique BGS dimensions.
- **What NCF adds at C3 BGS:** the explicit **10-strand যোগ্যতা framework** (১.x environment, ২.x coexistence, ৩.x history-culture, ৪.x geography, ৫.x family-and-child, ৬.x ethics, ৭.x country-resources, ৮.x professions, ৯.x economics, ১০.x disaster) with per-পাঠ 3-part শিখনফল codes; standalone *family role* + *child rights & road safety* + *money use* + *emergency preparedness* chapters (no Era-A precedent). **What NCF drops:** standalone *পরিবেশ দূষণ* + *সামাজিক উন্নয়ন* (folded into Ch1); *জনসংখ্যা* (population) dropped entirely; adult-framed *অধিকার ও দায়িত্ব* reframed to child-centred rights; *দক্ষতা ম্যাট্রিক্স* preface, *নমুনা প্রশ্ন*, and *two-page-per-বিষয়বস্তু* layout retired.
- **OCR / confidence:** Era A and 2025/2026 books are scanned images; 2024 arrives as a **legacy Bijoy-encoded text file** (`.pdf`-named, decode-able with `bijoy2unicode` — matches the C3 Science 2024 trap from the same year), text-only no images. Trust tier/era classifications over absolute counts. The chapter inventory decodes cleanly from the Bijoy text — but visual content (illustrations, festival imagery, mixed-gender children) is unverified for 2024.
- **Islamic-alignment — BGS is the highest content-density subject for curation review** so far (more touchpoints than Math or Science). Standing watch-items routed to curation (observational only): **⚠⚠ priority: Ch5/Ch4 আমাদের সংস্কৃতি (যোগ্যতা ৩.৪)** explicitly mandates *সংগীত, নৃত্য, উৎসব-অনুষ্ঠান* (music/dance/festivals) as cultural-heritage components, with the TG locating these at per-পাঠ level (TG পাঠ ২৪ সংগীত-ও-নৃত্য + TG পাঠ ২৫ উৎসব-অনুষ্ঠান). **⚠ Ch1 narrative** lists "ঈদ, পূজা, বুদ্ধপূর্ণিমা, বড়দিন" as religions' festivals (Era B text-level addition; Era A omitted). **⚠ TG Ch2 উপকরণ instruction** to bring "বিভিন্ন ধর্মীয় অনুষ্ঠান পালনের ছবি" as classroom material. **Resolved at 2026:** the leader chapter / person-cult framing dropped. **Positive:** madrasa positively named alongside school/college in both eras; inquiry pedagogy (পর্যবেক্ষণ → কাজ → আলোচনা → মূল্যায়ন) aligns directly with school's free-thinking/self-try priority; the 3-row মূল্যায়ন নির্দেশক (knowledge / skill / **attitude-and-values**) supplies a native NCF docking point for Islamic-values overlay (Project 03 future work) without disturbing NCTB compliance.
- **TG status: first BGS TGR COMPLETE, Class 3 (2026-05-28, D-PROJ01-010).** `completed_C3_BGS_TGReconciliation_v1.md` produced. **Method (field-tested):** BGS TG has selectable Bangla text in chapter headers (unlike Science TG which is fully image-only InDesign) but image-content (illustrations, table cells, hand-drawn diagrams) remains image-only — **partial text layer**, a new category for the Playbook. Procedure: rasterize chapter openers (`pdftoppm` ~110 DPI) → **visually verify** the first 2–3 openers (catches digit-flips in 3-part codes) → **Tesseract `ben+eng --psm 6`** for remaining openers' যোগ্যতা + শিখনফল strip. **পাঠ-numbering convention: continuous through chapters** (Ch1 = পাঠ ১–৬; Ch2 starts at পাঠ ৭; etc.) — MATCHES Math; DIFFERS from Science (which restarts per chapter). **Session length: 50 minutes** (5+40+5) — MATCHES Math + Science; DIFFERS from English (45 min). **Per-পাঠ structure:** title + (কাজ ক ও খ; পৃষ্ঠা: N) + শিখনফল + উপকরণ + শিখন-শেখানো কার্যাবলি (ভূমিকা/মূলপাঠ/মূল্যায়ন) + 3-row মূল্যায়ন নির্দেশক + পাঠসমাপ্তি. **Per-chapter structure:** opener carries one or two NCF strand codes (e.g., Ch6 = ৫.১ + ৫.২; Ch7 = ৫.৪ + ৫.৫; Ch4 = ৩.২ + ৩.৩). **Field lesson UNIQUE to BGS (carry forward):** the **TG-vs-2026 chapter-count mismatch** — TG was finalised against the **2025** textbook (13 ch); 2026 dropped TG-Ch3 in the Sep 2025 reprint, requiring a **−1 chapter offset for Ch4 onward** when reading the TG alongside a 2026 textbook. Surface this offset table prominently in BGS skeletons (S-02 pattern). Watch for analogous TG-vs-reference offsets at higher BGS classes. **Verdict: C3 BGS TGR = clean validation + objective-layer enrichment** (no inventory/tier reversals — mirrors C3 English/Math/Science; explicitly **unlike** C3 Bangla). **Downstream folds still owed (staged):** `completed_C3_BGS_Skeleton_v2.md` (built), `completed_C3_BGS_StabilityAnalysis_v2.xlsx` (built), `completed_C3_BGS_StabilityReport_v2.md` (built), and the **net-new BGS REF-19 vertical-map + BGS Subject-Spine seeds** (BGS is the newest subject — no BGS REF-19 rungs or Subject Spine exist yet; Classes 4–6 BGS still pending will complete the rungs).

**Predicted (not yet field-tested — Classes 4–6 BGS):**
- Classes 4–5 BGS: confirm whether the within-Era-B 3-step political evolution observed at C3 also occurs (or whether the leader chapter was always absent at higher classes). The NCF-timing question is per-class: don't assume C3's 2024 break holds for C4/C5 BGS.
- Class 6 BGS: expect formal government / civics introduction (cabinet, parliament structure), broader global geography, possibly the first systematic constitutional rights treatment.
- BGS will likely be **the highest content-density subject for curation review across all classes** — plan for more curation throughput than Math or Science required.

---

## 16. Teacher-Guide (TG) Reconciliation — Mandatory Per Subject (D-042)

After a class × subject's stability analysis produces its skeleton, a **mandatory** reconciliation step (master **D-042** / D-PROJ00-016) validates and enriches that skeleton against the NCTB **Teacher Guide (শিক্ষক সহায়িকা)** — the companion NCTB issues alongside the textbook, which carries the **per-lesson objectives the textbook does not print**.

**Why it is mandatory.** The 10-year stability analysis maps *content stability*; it never captures per-lesson objectives. Only the TG carries each lesson's অর্জন-উপযোগী যোগ্যতা (NCF competency codes), period-level শিখনফল (learning outcomes), শিখন-শেখানো কার্যাবলি (activities), উপকরণ (materials), and মূল্যায়ন নির্দেশক (assessment rubric). Skipping it risks building lesson plans on an incomplete objective map. (The Class 1 Bangla pilot proved this: the vertical map had marked free-writing, informational-text, functional-writing, and distinct-poem strands “absent” at Class 1 when the TG shows all present.)

**Where it sits.** A validation **gate on the skeleton** — run after the skeleton is complete and **before lesson-plan production (Project 03)** begins for that subject. It refines, it does not re-order, the D-005 build chain.

**Inputs.** (a) the completed skeleton (REF-05) for that class × subject; (b) the matching subject's section of the Vertical Topic Progression Map (REF-19); (c) the NCTB Teacher Guide PDF for the **same edition/year** as the skeleton's reference year — **uploaded per chat, never stored** (D-006).

**Procedure (repeatable):**
1. **Confirm edition.** Verify the TG is the same NCF edition/year as the skeleton's reference year (e.g. NCF 2021, পরিমার্জিত ২০২৫). A mismatched edition invalidates the objective mapping.
2. **Establish the page offset.** Render a couple of pages and find the PDF-page − printed-page offset (TGs have front matter). Build a পাঠ/lesson → PDF-page map from the সূচিপত্র (TOC), which also gives **period counts**.
3. **Extract per-lesson objectives.** For each lesson read the header block (যোগ্যতা + শিখনফল + উপকরণ + পদ্ধতি). Use the **cluster-inheritance shortcut**: language TGs typically state objectives once for a cluster-leader lesson, the rest “follow পাঠ N” (Bangla vowels inherit the first vowel lesson, consonants the first consonant lesson, kar the first kar lesson) — read leaders in full, mark inheritors. Flag lessons with **no formal শিখনফল** (readiness / concept-bridge / creativity) explicitly. For image-only Bangla, use the visual-reading fallback (§4) and the persistent working file (§3).
4. **Reconcile.** Build a per-lesson ledger — lesson · title · periods · যোগ্যতা · শিখনফল · skeleton type · status (✓ match / ➕ TG-enrich / ⚠ reconcile / 🔁 retag). Confirm the lesson inventory is complete; surface (a) enrichment the TG adds (objectives / periods / rubrics), (b) omissions or mis-classifications in the skeleton or REF-19, (c) curation touchpoints for REF-01.
5. **Separate school additions.** Tag every row NCTB-native vs [school-add] so explicit Islamic additions stay distinct from NCTB content.

**Output — the fourth REF-05 artifact.** `completed_C{n}_{SUBJ}_TGReconciliation_v{ver}.md`: executive summary + checklist, scope/method, the full per-lesson ledger, findings, curation touchpoints, and a **patch list** (proposed edits to REF-19 / REF-03 / the skeleton — staged, not auto-applied; locked-file edits follow the supersede protocol). It **consumes** the skeleton + REF-19 and **feeds** corrections back to them and to REF-03.

**Rollout.** Mandatory for all in-scope (D-019) subjects. **Future subjects:** fold the TG in as a standard input to the stability analysis from the start (skeleton TG-validated on first production — no retrofit). **Already-completed subjects:** run a retrofit reconciliation pass as each nears production, prioritized by the build queue. First instance: Class 1 Bangla (`completed_C1_BAN_TGReconciliation_v1.md`, 2026-05-24). **Retrofit rollout status (2026-05-28):** all four prior subjects + the newly opened BGS line are now TG-reconciled at the analysed classes — **Bangla C1–C5** (2026-05-24/25), **English C1–C5** (2026-05-26), **Math C1–C5** (2026-05-27, D-PROJ01-006), **Science C3–C5** (2026-05-27, D-PROJ01-008), **BGS C3** (2026-05-28, D-PROJ01-010 — the first BGS TGR; produced alongside the C3 BGS stability analysis in the same chat, following the Science "future subject" rollout shape). The Math retrofit field-tested the OCR route for **image-only / SutonnyMJ-font** Math TGs (rasterize + Tesseract `ben+eng` + visual opener verification; continuous পাঠ numbering as an inventory check) and surfaced the **strand-number ≠ chapter-number** gotcha (verify each chapter's যোগ্যতা from its header — see §15 Math). Math was *not* uniformly enrichment-only: **C4 carried two competency-strand corrections + a Time-coverage correction**, so run each subject's TGR with full scrutiny, not an enrichment-only assumption. **Science C3–C5 also TG-reconciled (2026-05-27, D-PROJ01-008) — the first Science TGRs**; these ran alongside the Science analyses (a "future subject," TG used in-analysis, no separate retrofit chat), yet standalone TGR artifacts + a skeleton-v2 supersede still resulted, so even future subjects should plan the TGR artifact as a deliverable. Science TGs are **image-only / no-text-layer InDesign** (distinct from Math's SutonnyMJ legacy font — `pdffonts` empty): rasterize + **vision** for chapter openers (যোগ্যতা + পাঠ সংখ্যা) + **Tesseract `ben+eng`** for the per-পাঠ শিখনফল layer (cleaner than the Math font, but expect Bangla-digit sub-index flips). **পাঠ-numbering convention varies by class** (C3 restarts per chapter / sums to 69; C4 & C5 continuous), and the **chapter-opener পাঠ-count line can misprint** (C5 Ch13). All three Science TGRs = clean validation + enrichment (no inventory/tier reversals). See §15 Science. **BGS C3 TGR (2026-05-28, D-PROJ01-010) field-tested the BGS-side method**: BGS TGs have a **partial text layer** (chapter headers selectable, body image-only — a third category distinct from Math's legacy-font and Science's no-text-layer InDesign); per-পাঠ structure shared with Math + Science (3-row জ্ঞান/দক্ষতা/মূল্যবোধ-ও-দৃষ্টিভঙ্গি rubric); 50-min session matches Math + Science; continuous পাঠ numbering matches Math. **Unique to BGS so far: a TG-vs-2026-reference chapter-count mismatch** — the TG was finalised against the Era-B2 (2025) textbook (13 ch) but the Era-B3 (2026) reprint dropped Ch3 "আমাদের চার নেতা" entirely, requiring a **−1 chapter offset for Ch4 onward** in the TG when read alongside the 2026 textbook. The BGS skeleton v2 surfaces the offset prominently (S-02 pattern). **BGS C3 TGR verdict = clean validation + objective-layer enrichment** (no inventory/tier reversals — mirrors C3 English/Math/Science; unlike C3 Bangla). See §15 BGS.

### 16.1 Edition Confirmation Against the Teacher Guide (D-042 checkpoint)

**The checkpoint:** before finalising any era boundary or framework conclusion (especially "this Era is / is not NCF 2021"), **confirm the edition against the Teacher Guide (শিক্ষক সহায়িকা), not the textbook alone.** A textbook-/skeleton-only stability pass can misread the edition; the TG is the authoritative edition source NCTB issues alongside the book. (This is the edition-confirmation arm of the §16 reconciliation — it is Procedure step 1 above, elevated to an explicit gate: never assert an era/framework conclusion without it.)

**Why this exists (field lesson, 2026-05-25 — Class 3 Bangla).** The C3 stability analysis concluded Era B (2025–2026) was a "revised 2010-policy edition, NOT NCF 2021," resting on three textbook-surface signals. The C3 Teacher-Guide reconciliation overturned that — Era B **is** NCF 2021 (পরিমার্জিত ২০২৫). Each signal had been misread:
- a **"জাতীয় শিক্ষানীতি ২০১০" preamble line** is the standard legal umbrella carried in *every* edition (including NCF books) — not an edition marker;
- a **consolidated end-glossary** (vs per-lesson boxes) is a presentation choice, not a framework marker;
- a **missing print year** is a data gap, not evidence of a different edition.

**The decisive test (Bangla NCF vs pre-NCF).** Open the TG and read the per-lesson objective vocabulary:
- **NCF 2021** book → every পাঠ carries **অর্জন-উপযোগী যোগ্যতা** (class-level competency codes, e.g. ২.১/৬.২/১০.১) **+ 3-part শিখনফল codes** (e.g. ২.২.৩).
- **2010-policy / pre-NCF** book → uses **প্রান্তিক যোগ্যতা / উদ্দেশ্য** instead.
This single check is unambiguous and outranks any textbook-surface signal. (For other subjects, use the analogous NCF competency vocabulary the TG carries.)

**Practical notes.**
- The TG is uploaded-not-stored (D-006); confirm edition + পাঠ-count match the skeleton's reference year *before* extracting (a wrong-year TG would mismatch — e.g. a 28-পাঠ first edition vs a 29-পাঠ later edition).
- TG সূচিপত্র formats vary: some carry period counts, some only page numbers (then read each পাঠ's "পিরিয়ড সংখ্যা" / continuous numbering instead).
- If the TG is unavailable, **flag the era/framework conclusion as TG-unconfirmed** rather than asserting it from the textbook alone.

*(Source: C3 Bangla TG reconciliation §5.D / `completed_C3_BAN_StabilityReport_v2.md`, 2026-05-25. This is the reconciled canonical Project-00 copy — it merges the edition-confirmation checkpoint into §16, where the C3 report v2 §7 cites it as "REF-04 §16 / D-042.")*

---

## 17. When You're Stuck

If OCR quality is too low and you can't get clean text:
- Try `--psm 4` (column) or `--psm 11` (sparse text) instead of `--psm 6`
- Upscale images 2x with `PIL.Image.LANCZOS` before OCR
- For Bangla, try `-l ben+eng` if pages have mixed scripts
- Visually inspect the worst pages with the `view` tool to understand the layout issue

If a finding seems implausible (e.g., a clearly common word counts as 0):
- Show the raw OCR for one or two sample pages to the user
- Don't paper over with hand-waving — flag it as a known limitation

If a chunk's output looks structurally fine but the user disagrees with a verdict:
- Walk back through the code logic (not the LLM "intuition")
- Look for off-by-one page ranges, missed file variants, missed regex anchors

---

*This playbook is meant to evolve. After each analysis, append any new gotchas, subject quirks, or code patterns you discover to the relevant section.*
