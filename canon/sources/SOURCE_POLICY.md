# SOURCE_POLICY — v1.4

*Canon. Adopted v1.0 by Principal ruling 2026-08-09 (CD-037), superseding the v0.1 draft staged in `_inbox/`.*
*v1.1 (CD-046) added **§7 Amendments**; v1.2 (CD-048) adds §7.4 spot-check depth and §7.5 raster-only content; v1.3 (CD-050) adds §7.6 the C5 Bangla book's real structure and §7.7 a third source class; v1.4 (CD-054, CD-055) adds §7.8 the extraction cadence for single-channel books and §7.9 the `নির্মাণাধীন` self-declaration. §7 is forward-only: the sections it supersedes are left as written and are not edited.*
*Consumed by: question-banks · scholarship · class-tests · support-books.*
*Cited, never copied (AGENTS.md §8).*

## 1. Purpose

Every NCTB textbook the school teaches gets a machine-readable **source extraction** — the
pattern proven by `canon/marklogic/C5_Bangla_Source_13-23.md`. Extractions are the ONLY
permitted content source for question authoring: no question is written from model memory.

## 2. The pipeline (per book)

### 2.1 Scan — who does it, and where the file lands

The **Principal** photographs or scans the printed NCTB book into **one PDF per book** and
places it in **`_inbox/`** at the repo root. The agent reads it from there and produces the
extraction.

Two consequences of that choice, stated so nobody is surprised by them:

- **`_inbox/` is gitignored.** The PDF therefore exists only on the machine it was placed on.
  An agent session on any other device cannot see it, and a session that assumes it can will
  stop, not improvise — this is exactly the failure recorded in **CD-026**, where a ruling
  could not be executed because the expected `_inbox/` PDF was not present in the workspace.
- **The PDF is never committed.** Scans are large and are provenance, not authority. The
  **extraction markdown is the committed artifact**; the PDF is retained by the Principal
  (Drive or local) and re-supplied to `_inbox/` if an extraction ever has to be re-verified.

The **printed↔PDF page offset** is recorded in the extraction's header on first use, never
carried in memory between sessions.

### 2.2 Extract

Per chapter (or chapter-range) file: chapter title and printed pages; full text inventory
(poems and prose verbatim as printed); word-meaning lists (অর্থ জেনে নিই); exercises; and the
slot↔chapter cross-reference against the subject's MarkLogic spine.

### 2.3 Verify

The extraction is read from the **rasterised page** — school scans carry no text layer — and
the page offset is **verified against the printed folio, never assumed**. This is the method
established and proven at CD-029, where reading the printed page rather than trusting a
supplied list overturned two recorded `needs_review: false` entries.

**Spot-check:** the Principal or the teacher confirms 2–3 sampled passages per book verbatim,
and the sign-off is recorded in the file header.

> **SUPERSEDE NOTE (CD-048).** The sampling depth in the line above is superseded by **§7.4**,
> and artwork-borne text is governed by **§7.5**. The text stands as written; read §7.4/§7.5
> for what is in force.

## 3. Rules

- **An extraction records; it never curates.** NCTB text is transcribed as printed. Curation
  decisions (REF-1 codes, substitutions, KEEP-AS-IS / NEEDS-REPLACEMENT marks) happen
  downstream in the consuming workstream, never in the extraction.
- **Naming:** `<Class>_<Subject>_Source_<chapters>.md` — e.g. `C4_MATH_Source_01-14.md`.
- **Storage:** `canon/sources/<class>/<subject>/`. Canon, because several workstreams cite the
  same extraction. Supersede-only after Principal acceptance; a new NCTB print year is a new
  extraction and the old one is archived, never edited.
- **Script guard:** extractions are human-read markdown and are therefore **out of guard scope**
  per CD-018. Content that enters a JSON bank downstream falls under the guard *there*, in the
  consuming workstream, per `canon/language/LANGUAGE_RULES.md` §7.

## 4. Priority order

> **SUPERSEDE NOTE (CD-046).** The within-C5 order below is superseded by **§7.1**. The text
> that follows is left as written — read §7.1 for the order in force.

**C5 (all five subjects — scholarship year) → C4 → C3 → C2 → C1.** Within a class, the subject
with the nearest term-paper need comes first.

`C5_Bangla_Source_13-23.md` already exists; **C5 Bangla 1–12 and 24+** complete that book first.

**Religion (REL) is out of scope for now** (Principal ruling, this adoption). REL books enter
extraction when the `islamic-studies` workstream opens, not before — the curation questions REF-1
has not yet settled for REL are decided there, and an extraction produced ahead of them would be
recorded against rules that do not exist yet. The class-test generator's existing REL coverage is
unaffected; it simply has no extraction to cite until then.

## 5. Gates (executed)

Per extraction:

- every chapter in the stated range is present;
- every spine slot for that class-subject is cross-referenced, or explicitly marked absent;
- page numbers are monotonic against the recorded offset;
- the spot-check sign-off is present in the file header.

A gate run's verbatim output is pasted before an extraction is called done (AGENTS.md §5).

## 6. Open at adoption

> **CLOSED (CD-046).** The §5 gate now has an executing script:
> `python tools/audits/source_check.py <extraction.md>` — one check per §5 condition,
> proven by a five-seed negative selftest plus a clean control. The paragraph below is
> left as written; it describes the state at adoption, not the state today.

The gate in §5 has **no executing script yet** — no extraction has been produced under this
policy, so there is nothing to run it against. It is written when the first extraction under
this policy is built (C5 Bangla 1–12), and until then §5 is a specification, not a proven gate.
`C5_Bangla_Source_13-23.md` predates this policy and is grandfathered as canon by CD-004.

---

# 7. Amendments (forward-only)

Rulings made after v1.0 was adopted. Each names the section it supersedes; **the superseded
section is never edited**, per AGENTS.md §7. A later reversal is a new subsection here citing
the old one, not a rewrite of it.

## 7.1 Priority order within C5 — supersedes §4 (Principal ruling 2026-08-09, CD-046)

**C5 English (all 20 units) → C5 Bangla remainder (পাঠ ১–১২ and ২৪+) → the other C5 subjects
→ C4 → C3 → C2 → C1.**

§4 put the Bangla remainder first. It no longer does. Two reasons, both recorded so a later
session does not re-derive them: English was the **highest-risk** extraction of the set and is
now proven end to end (§7.3 is what made it risky), and **step ② — C5 model papers and CTs
(CD-045) — needs a non-Bangla subject** to work on; today Bangla is the only subject with any
extraction at all.

Everything else in §4 stands unchanged: **REL remains out of scope** until `islamic-studies`
opens, and within a class the subject with the nearest term-paper need still comes first.

## 7.2 Extraction conventions v1.0 — adds to §2.2 and §3 (Principal ruling 2026-08-09, CD-046)

Three conventions the policy left unfixed, ruled before the second file existed rather than
after the twentieth. Forward-only naming (AGENTS.md §7) means changing any of them later
produces a **new set of files, not a rename**, which is why they are ruled now.

| | Convention | Why this one |
|---|---|---|
| **(a) Granularity** | **One file per chapter/unit.** `C5_Bangla_Source_13-23.md`'s chapter-range form is grandfathered, not the pattern. | A question author works on one chapter; a range file makes them scroll past ten they did not ask for. Per-file gate output also names the failing chapter directly. |
| **(b) Subject token** | **The spine's subject code** — `ENG`, `BAN`, `MATH`, `SCI-BGS`. So `C5_ENG_Source_01.md`. | Matches `MarkLogic_ENG_Spine.md` and the `ENG-S03` slot ids the extraction cross-references, so one token runs through spine, slot and filename. |
| **(c) Language** | **Bengali scaffolding around a verbatim body in the book's own language.** Headings, notes and tables in plain Bengali; every transcribed line exactly as printed. | AGENTS.md §7 — reader-facing files are plain Bengali — without touching the transcription, which is not reader-facing prose but evidence. |

Naming grammar therefore: `<Class>_<SPINE-SUBJECT>_Source_<chapter>.md`, stored at
`canon/sources/<class>/<subject>/`, e.g. `canon/sources/c5/english/C5_ENG_Source_01.md`.

## 7.3 A second source class: born-digital publisher PDFs — adds to §2.1 and §2.3 (Principal ruling 2026-08-09, CD-046)

§2.1 describes one intake: the Principal photographs or scans a printed book, and §2.3 grounds
the raster-read rule on the fact that **school scans carry no text layer**. A book can also
arrive as a **born-digital publisher PDF** — NCTB's own typeset file — which *does* carry one.

**The rule does not relax for it. Raster-read stays mandatory, and the text layer is never
authority.** A text layer's *presence* says nothing about its *truth*, and the C5 English book
is the recorded proof:

- `Class 5 English.pdf` (Adobe Illustrator 24.1, AcroForm, 118 pp, md5 `09a9b96f…`) yields
  80,430 extractable characters, and they are wrong in two different ways at once.
- **Bengali comes out as mojibake** — the preface extracts as `ǇƷǍƵ ȟǀƷǆ ȟǀƷǆƘӂǂƾƲƤǍƾ`, with no
  recoverable text at all. This is the same failure CD-029 met on a scan, arriving by a
  different route.
- **English comes out Caesar-shifted by −3 for one font subset, with commas and spaces dropped
  entirely.** Printed page 1 reads `b) What do you do in the library?`; the text layer returns
  `E  :KDWGR\RXGRLQWKHOLEUDU\"`. Printed page 3's word list reads
  `neighbourhood, tomorrow, enjoy, famous,`; the text layer returns
  `QHLJKERXUKRRGWRPRUURZHQMR\IDPRXV`. A reader who un-shifts the letters and stops there gets
  fluent, plausible English with **every comma silently gone** — the most dangerous failure
  shape available, because it does not look like a failure.

**Permitted use of a text layer: as a disagreement-hunting second channel, never as a source.**
Transcribe from the raster; the text layer may be decoded alongside and diffed against the
transcription so that any disagreement is surfaced for human eyes. A passage may not enter an
extraction on the text layer's authority, and a text-layer reading may not overrule the raster.

The extraction header records which class the source was, so a later reader knows which
hazards applied.

## 7.4 Spot-check depth — amends §2.3 (Principal ruling 2026-08-09, CD-048)

§2.3 asks for 2–3 sampled passages per book. That was written when the human eye was the only
check on the transcription. It no longer is.

**Where `tools/audits/source_textcheck.py` reports Section B clean AND every word-level
disagreement is provenance-proven as a decoder limit, the spot-check is ONE sampled passage per
unit — the longest.** The machine diff stands as the second and third channel: Section B is
what would catch a dropped or invented passage, and a clean Section B means no stretch of the
book is unaccounted for in either direction.

The conditions are conjunctive and are read off an executed run, never assumed. A unit whose
Section B is dirty, or whose word-level disagreements have not been traced to the raw text
layer, returns to the older depth — the ruling buys depth with evidence, and without the
evidence there is nothing to buy it with.

**Sign-off rows stay Principal-only.** Nothing here lets an agent sign, and
`source_check.py`'s SIGNOFF check still reports PENDING rather than PASS until a human does.

## 7.5 Raster-only content — adds to §2.2 (Principal ruling 2026-08-09, CD-048, closing PENDING-P-012)

Some of a book's text is drawn, not typeset: map labels, diagram callouts, words inside artwork.
Unit 4's two maps carry about seventy-five place names of which the PDF text layer holds **not
one character**.

- Such text lives in the unit's **names/labels section, explicitly flagged raster-only**, and
  **outside the cross-checked body** — otherwise the cross-channel check reports dozens of
  correct words as missing and its output stops being read.
- It is **single-channel and Principal-verified**: the machine has nothing to say about it, so
  §7.4's one-sample depth does **not** apply. **The full set is checked by eye, not sampled.**
  `source_check.py` fails an extraction that records artwork-borne text without a full-check
  row in its sign-off table.
- **Any consumer citing those labels inherits the flag.** A question built on a map label rests
  on one human reading; that fact travels with the citation rather than being lost at the
  boundary between canon and the workstream that uses it.

## 7.6 The C5 Bangla book's real structure — supersedes the range in §4 and §7.1 (Principal ruling 2026-08-09, CD-050)

§4 and §7.1 both describe the remaining C5 Bangla work as **"পাঠ ১–১২ and ২৪+"**. Read against
the book, that range is wrong at both ends. Neither section is edited; this one is in force.

**আমার বাংলা বই, পঞ্চম শ্রেণি has 23 পাঠ and no more.** The সূচিপত্র runs ১–২৩ and stops;
পাঠ ২৩ (পোস্টার লিখি, প্ল্যাকার্ড লিখি) begins on printed ১৩০; printed **১৩২ carries সমাপ্ত**
and is the last page of the book. **There is no পাঠ ২৪ to extract, and no session should look
for one.** The "২৪+" was carried forward from a range nobody had checked against a book.

**পাঠ ১২ (শিষ্যের সাধনা) is not extracted.** `canon/marklogic/C5_Bangla_Source_13-23.md`
records it as deliberately excluded on Islamic-values grounds by school authority, and the
Principal confirmed that standing ruling reaches the extraction layer here (2026-08-09). This
is a **named exception to §3's record-never-curate rule, not a loosening of it**: §3 still
governs everything inside an extraction that exists, and the exception is recorded in
`canon/_wip/c5-bangla/EXCLUDED_paath_12.md` so the gap is visible rather than looking like an
oversight. A later session that finds পাঠ ১২ missing must read that note before acting.

**So the remaining scope is পাঠ ১–১১**, printed ১–৬২ = PDF 10–71. With পাঠ ১৩–২৩ already canon
and পাঠ ১২ excluded by ruling, that completes the book.

**Edition, flagged and not resolved.** This PDF's imprint reads *প্রথম মুদ্রণ সেপ্টেম্বর, ২০২৫*;
`C5_Bangla_Source_13-23.md` describes its source as *ডিসেম্বর ২০২৫ সংস্করণ* — plausibly from the
PDF's ModDate of 20 December 2025, but that is a guess and is recorded as one. **Both statements
are written side by side in each new file's header. The older file is not edited** (CD-004
grandfathers it), and no agent resolves this: it closes only if the Principal compares printings.

## 7.7 A third source class: outlined born-digital PDFs — adds to §2.1, §2.3 and §7.3 (Principal ruling 2026-08-09, CD-050)

§2.1 describes a scan with no text layer. §7.3 adds a born-digital publisher PDF that carries
one and lies. `Class 5 Bangla.pdf` is neither: it is **born-digital with every glyph converted
to outlines**, so it carries no text layer at all while looking, to any tool that asks only
whether fonts are embedded, like a file that does.

Measured, not assumed: `pdftotext` over 142 pages returns **421 characters** — 312 of them on
p142 (the back imprint), 4 on p28, none anywhere else. Pages 1, 20, 70, 100 and 141 register
**no fonts**. Page 70's content stream holds 9,790 curve operators and 183 fills and **not one
`BT` or `Tj`**: the text is drawn.

**Consequence — §7.4's reduced depth cannot be earned on such a book.** §7.4 buys one sampled
passage per unit against a clean Section B from `source_textcheck.py`, and **Section B is
trivially clean when the stream is empty.** An absent channel is not a passing one. So:

- **Depth is full human check, book-wide** — the depth §7.5 sets for artwork-borne text,
  applied to the whole book, because the whole book is single-channel.
- An extraction from such a source **declares itself** in its header (`**যাচাই-চ্যানেল:** একক`)
  and `source_check.py`'s **DEPTH** check fails it if any sign-off row claims sampled depth.
- `source_textcheck.py` **REFUSES** (exit 3) rather than reporting agreement when it has
  nothing to compare. A REFUSE on such a book is the expected result and is not a red gate;
  an AGREE would be a bug, and was one until CD-051.

The extraction header records which class the source was, so a later reader knows which
hazards applied — and, here, which one did not exist.

## 7.8 Extraction cadence for single-channel books — adds to §2.2, §7.4 and §7.7 (Principal ruling 2026-08-10, CD-054, closing PENDING-P-014)

§7.7 sets full human check, book-wide, for a source with no text layer. It did not say what that
costs, and the first Math book made the cost measurable: delivering a page at a true 400 dpi needs
it split into **four** tiles — a larger tile is downscaled in transit, so the resolution rule is
broken by the delivery rather than by the render — which is **roughly 720 reads for 181 printed
pages**. One session cannot hold that.

**The resolution is not negotiable, and the schedule is what gives way.**

- **No relaxation for math body text.** The 400–700 dpi rule (CR-001) applies to all number-dense
  content **before** transcription, not on suspicion. The reason is on the record: **five
  near-misses on the Bangla book all lived exactly where dpi had been thinned** — `ঝকঝক` read as
  `ঝকঝাক`, পাঠ ৪'s letter date, পাঠ ৬'s chandrabindu, `শাঁখ` read as `শীঁখ`, and `প্রচণ্ড`
  transcribed `প্রচন্ড`, which reached a commit. In গণিত the exposure is worse in kind, not only
  in degree: **a mis-read numeral becomes a wrong answer key, and a book with no second channel has
  nothing downstream that will catch it.**
- **Cadence: one or more complete অধ্যায় per session, at full care.** A chapter is the unit of
  work because it is the unit a question author uses and the unit the gate names.
- **Checkpoint-commit per chapter**, a **stated resume point in the workstream's `STATE.md`**, and
  a **fresh session each sitting**. A session that finds its care degrading stops at the resume
  point; it does not finish the chapter badly.
- **A ten-chapter book is about a week of sittings. That is the accepted cost of a source with no
  second channel**, and no agent trades it back for speed. An agent that thinks the trade is worth
  making raises a PENDING row; it does not make it.

## 7.9 An unfinished extraction declares itself — adds to §5 (Principal ruling 2026-08-10, CD-055, closing PENDING-P-015)

§7.8's cadence guarantees that a half-built extraction sits on disk between sittings, and AGENTS.md
§3 requires exactly that — work in progress lives in files so a killed session is resumable. But
`source_check.py --selftest` draws its controls from every extraction on disk and asserts that an
unmutated one is not red, which assumes each is finished. Both rules are right; together they turned
the whole repository's tool gate red the first time a chapter was interrupted mid-transcription.

**An extraction that is not finished says so, in one machine-read line in its header:**

```
**অবস্থা:** নির্মাণাধীন — <what is transcribed, what is not, where to resume>
```

- A file carrying that line is **excluded from the selftest's controls**, and the selftest
  **prints every file it skipped and why**. An extraction can be held out of the pool; it cannot be
  held out quietly, and it cannot be held out by accident.
- **The marker buys nothing else.** `source_check.py` still runs on such a file and still reports
  it red. It is not a waiver, and it does not touch SIGNOFF, DEPTH or any other check.
- **Removing the line is part of finishing the chapter** and belongs in the resume instructions.
  A marker nobody takes out would keep a finished extraction outside the selftest forever, which
  is the same silent-exclusion failure in the opposite direction.
