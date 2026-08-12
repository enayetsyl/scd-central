# SOURCE_POLICY — v1.13

*Canon. Adopted v1.0 by Principal ruling 2026-08-09 (CD-037), superseding the v0.1 draft staged in `_inbox/`.*
*v1.1 (CD-046) added **§7 Amendments**; v1.2 (CD-048) adds §7.4 spot-check depth and §7.5 raster-only content; v1.3 (CD-050) adds §7.6 the C5 Bangla book's real structure and §7.7 a third source class; v1.4 (CD-054, CD-055) adds §7.8 the extraction cadence for single-channel books and §7.9 the `নির্মাণাধীন` self-declaration; v1.5 (CD-057) adds §7.10 the depth rule's math extension; v1.6 (CD-065) adds §7.11 the rendering-choice rule; v1.7 (CD-066, CD-067) adds §7.12 the pure-exercise convention and §7.13 the multi-chapter cadence; v1.8 (CD-068) adds §7.14 the OCR-drafted source class and its verify-not-read inversion; v1.9 (CD-069) adds §7.15, which supersedes 7.14.2a's direction-blind trip-wire count; v1.10 (CD-070) adds §7.14.2c-i, the cell-order rule, and makes `OCR-corroborated` an enforced depth value; v1.11 (CD-071) adds §7.16, the Assamese-character gate; v1.12 (CD-072) adds §7.17 — a gate reports or refuses, never omits, and learns the page rather than the page learning the gate; v1.13 (CD-073) adds §7.18, the মই-ভাগ as a named census shape. §7 is forward-only: the sections it supersedes are left as written and are not edited.*
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

## 7.10 The depth rule's math extension — adds to §7.4 and §7.7 (Principal ruling 2026-08-10, CD-057)

§7.7 says a book with no text layer has no second channel and therefore cannot earn §7.4's
reduced spot-check depth. That is right about the **file**. It is not right about **math
content**, which carries its own redundancy: partial products must sum to the total, and each
partial must equal multiplicand × multiplier digit × place value. **A mis-read digit does not
balance** — which is precisely the failure the full-resolution ruling exists to catch.

`tools/audits/math_arith_check.py` executes it. As with §7.4, the reduction is **read off an
executed run, never assumed**, and the run's verbatim output is the evidence.

**Where the check reports the working CLEAN, that working earns §7.4-style reduced depth —
one sampled line per block rather than every digit.** Two clarifications that are part of the
ruling, not commentary on it:

- **Blanks pinned uniquely count as covered.** Where the book prints an exercise part-solved
  and the printed cells admit exactly one assignment of the hidden digits, the block is
  covered. It is often the *stronger* check: more constraints bear on fewer free digits.
- **`AMBIGUOUS` and `WIDTH` do not count.** A block admitting more than one assignment, and a
  pure scaffold whose cells are all empty, have had **no digit verified** — only, in the second
  case, their row widths. The gate reports these as their own statuses and returns REFUSE
  rather than CLEAN when a file contains nothing else, so a depth claim cannot rest on them.

**Everything the check cannot see stays at full manual depth**, and the list is exhaustive and
short: **words, names and instructions; problem-statement figures the book never computes; and
any working the gate reports as uncovered.** In practice most of a chapter is still full-depth —
the extension buys depth on the arithmetic and on nothing else.

**One thing the extension does not buy, recorded because it was learned the hard way.** The
first real run of this gate caught **CR-002**: an agent transcribing at 400 dpi mis-**counted**
the empty boxes in a scaffold — the digits were legible, the count was wrong, and resolution was
never going to help. **High resolution protects reading; only a second channel protects
counting.** §7.8's no-relaxation ruling is unaffected: the dpi floor and this check answer
different failures, and neither substitutes for the other.

## 7.11 Rendering choice — prefer the form the checker reads (Principal ruling 2026-08-10, CD-065)

A printed page can often be transcribed two ways that are **equally faithful to its content** and
differ only in markdown form — a bordered two-column box as a table, or as two labelled blocks; a
worked chain as blockquote lines, or as table rows. The forms are not equivalent to the gates:
**a `|` inside a cell stops `math_arith_check.py` reading anything on that line.**

**Where two renderings are equally faithful, take the one that is checked.** Faithfulness is the
constraint and is never traded; among renderings that satisfy it, the more-verified one wins. A
transcription that is correct and unchecked is weaker than the same transcription checked, and on
a single-channel source (§7.7) that difference is the whole margin.

**One exception, and it points the other way.** For a block the book itself marks **false** —
`✗`, or a verdict cell reading মিথ্যা — **protection comes first: it stays table-held.** CD-063's
inversion covers prose-form marked lines, but a marked block the layout already holds is left
held; making it machine-readable to gain coverage would trade a working guard for a check that
CD-064 only partly provides.

**And the boundary is a stop, not a judgement call.** A **false-worked block the book does NOT
print as a table** is **stop-and-ask** — a PENDING-P row, not an agent decision. Inventing a
layout to keep a gate quiet is the failure CD-061 rejected; inventing one to make a false block
checkable is the same failure wearing the opposite coat.

**Recorded because it was decided in a workstream and belongs above it.** The rule was written
into `canon/_wip/c5-math/STATE.md` when ছাপা ২২ forced the choice; a rule that lives only in a
workstream's state file dies with the workstream. Every subject that meets a bordered box will
meet this, and C5 গণিত will not be the last.

## 7.12 Pure-exercise sections — reduced page depth, undiminished numeral depth (Principal ruling 2026-08-10, CD-066)

§7.8 sets 400 dpi for the whole page because in a math book almost every page is number-dense.
**One kind of section is different in a way that can be stated exactly:** a section containing
**only bare exercises** — no printed working, no printed answers, no `✗`/`✓` marks — carries no
worked line to mis-read, no answer key to corrupt, and nothing for `math_arith_check.py` to read.
What it does carry is **problem-statement numerals**, and **a mis-read numeral there still reaches
a question paper.**

**So the page and the numerals are separated:**

- the section is transcribed at the **150 dpi working render**;
- **the numerals themselves are read at 400+ dpi via spot-crops** — the CR-001 rule is not
  relaxed, it is aimed;
- the sign-off row for such a section **states the convention**, so the Principal sees which
  depth each row was taken at rather than having to infer it.

**Everything else keeps full treatment, unchanged:** worked examples, any answer-bearing content,
tables, `✗`/`✓`-marked lines, word lists, and figures. **The test is the section's content, not
its heading** — an "অনুশীলন" that prints one worked example is not a pure-exercise section, and a
section that turns out to contain a printed answer stops being one the moment that is noticed.

**Why this is not the resolution relaxation §7.8 refused.** CD-054 rejected lowering dpi *for
number-dense content*. This lowers it only for **page furniture around numerals that are still
read at full resolution** — the instruction line, the item numbering, the layout. The numerals,
which are what CR-001 was written about, are read exactly as before.

## 7.13 Multi-chapter cadence — supersedes §7.8's one-chapter line (Principal ruling 2026-08-10, CD-067)

§7.8 set **one or more complete অধ্যায় per session**. In force now: **as many complete chapters
as full care allows, up to three per sitting.**

**Chapter close stays atomic and is not batched across chapters.** Per chapter, in order: full
read → SLOTS cross-reference → `নির্মাণাধীন` marker removed → gate sweep → checkpoint-commit.
A chapter is closed or it is not; three half-closed chapters are not two closed ones.

**The stop-rule is unchanged and outranks the ceiling.** The moment care would thin, the sitting
stops at a **stated resume point**, mid-chapter if that is where it lands. **Two chapters at full
care beat three at partial**, and the reason is on the record rather than asserted: every
near-miss this book and its sibling have produced — `ঝকঝাক` for `ঝকঝক`, `প্রচন্দ` for `প্রচণ্ড`,
`শীঁখ` for `শাঁখ`, and the eight-box count that should have been seven — happened where attention
or resolution had thinned. **Three is a ceiling, never a target.**

## 7.14 A fourth source class: OCR-drafted — the agent inverts from reader to verifier (Principal ruling 2026-08-10, CD-068)

§7.3 and §7.7 classify books by what the *publisher's file* carries. This section classifies by
what the *Principal supplies alongside it*: the Principal runs local OCR over the page rasters and
stages **per-chapter draft markdown in `_inbox/`** next to the PDF. The agent no longer reads the
book cover-to-cover by vision; it hunts the draft for disagreement.

**The motive is cost and is stated rather than hidden.** Vision-reading every page at 400 dpi in
four tiles was the budget driver. A machine that reads prose well enough to be argued with is
cheaper than one that reads nothing — which is what this book's text layer does (§7.7: 190 pages,
zero letters).

### 7.14.1 The draft is never trusted, and never discarded

It is a **machine channel of exactly the standing a text layer has under §7.3** — a
disagreement-hunting input, **never an authority**. §7.3's proof carries over without amendment: a
channel's fluency says nothing about its truth, and the C5 English text layer returned fluent
English with **every comma silently gone**. **A passage may not enter an extraction on the draft's
authority, and a draft reading may not overrule a crop.**

### 7.14.2 Verification depth — enumerated, not sampled at large

The agent spot-crops and vision-reads at **400 dpi**:

- **(a) every numeral.** Digits are where the marks live. The test run turned `৪` into `8`, `৭`
  into Arabic `٩`, `৫` into `¢`, and produced Cyrillic `ЪΟ` — a numeral channel this unreliable is
  not sampled, it is read.
- **(b) all known weak-glyph classes** — conjuncts, ণ/ন, শ/স/ষ, ড়/র, chandrabindu/hasant
  clusters, mixed-digit runs.
- **(c) every table cell, blank-box count, and `✗`/`✓` mark.** **CR-002 is why counting is named
  separately from reading:** those boxes were legible at 400 dpi and were still miscounted.
- **(d) headings, exercise labels, and poem lines in full.**
- **(e) a random 10% sample of plain prose lines.**

**Prose the OCR and the sample-check agree on is accepted at draft value**, recorded as
**`OCR-corroborated`** in the sign-off row's depth column — a new depth value following §7.12's
pattern, so the Principal **reads** which depth each row was taken at instead of inferring it.

**7.14.2a — the sample is a trip-wire, not a formality.** **One** substantive disagreement inside
the sample **widens it to 25%**; a **second voids OCR-corroboration for that chapter**, which drops
to **raster-full**. A sample that cannot fail is not a check.

> **SUPERSEDE NOTE (CD-069).** The counting rule in 7.14.2a is **direction-blind** as written — it
> counts any disagreement, including one where the OCR is *right* and our own transcription is
> wrong. **§7.15 supersedes it** and states which disagreements count. The text above stands as
> written; read **§7.15** for what is in force.

**7.14.2b — the sample is deterministic.** **Seed = chapter id**, and the **sampled indices are
logged**. A later reader can re-draw the same sample, and the agent cannot quietly re-roll until
the sample comes back clean.

**7.14.2c — provenance and patterns.** The draft header records **OCR engine, exact version, dpi,
and page range**. **Three occurrences of the same weak-glyph pattern become a `PATTERN` row in the
corrections ledger** (AGENTS.md §6), with promotion to an executing gate proposed.

**7.14.2c-i — cell ORDER is crop-matched, not only cell value (CD-070).** The cell-crop clause
above says every cell is read. **Reading every cell is not enough: the cells must be read in the
order the book prints them.** On ছাপা ৩৫ the OCR read all eleven numerals of a table **correctly**
and **reordered them** — ১২ and ৩৬ drifted to the end of the row. **A correct numeral in the wrong
cell is exactly as wrong as a misread one, and no spelling diff will ever catch it**, because
nothing is missing and nothing is misspelt. So the crop match is positional: **cell *n* of the
transcription against cell *n* of the page.** A sign-off row covering any table, row, cell or
column **states that the order was matched**, and `source_check.py` fails an `OCR-corroborated`
row that describes tabular content without it.

### 7.14.3 The disagreement log is what this source class buys

**Every OCR-vs-crop disagreement is logged in the file's `## চ্যানেল-অমিল` section, with the
resolution and the crop citation.** This log **replaces `source_textcheck.py`'s REFUSE** — which on
a §7.7 book is the honest verdict of a channel that has nothing to say, and therefore guards
nothing. For the first time on this book there is a real second channel, and its output is a
written record rather than an exit code.

**7.14.3a — the draft is committed as evidence, not merely staged.** `_inbox/` is gitignored
(§2.1). A draft left there would make the disagreement log cite a file **no other device can see**,
and the corroboration claim unauditable.

### 7.14.4 Nothing else moves

**All existing doctrine is unchanged:** arithmetic gates run identically; the **fence rule**
(CD-061), **`✗`/`✓` inversion** (CD-063/CD-064), **§7.11 rendering choice**, **§7.5 artwork
quarantine**, **Principal-only sign-off**, and **`নির্মাণাধীন`** (§7.9) all stand exactly as
written.

**7.14.4a — the pipeline buys no cadence.** **The §7.13 ceiling and its stop-rule lift only after
three consecutive gate-GREEN §7.14 chapters**, and not before. **A faster channel is a reason to
verify more, not to close chapters sooner.**

### 7.14.5 First use, and it starts by being tested

**First use is the C5 গণিত অধ্যায় ৩ resume.** Before any new page is touched, the draft is
**diffed against the already-verified pages of the same chapter** and the result reported. The
channel is **measured against known-good ground before it is trusted on unknown ground** — and if
it fails there, it fails cheaply.

## 7.17 A gate reports or refuses; it never omits — and it learns the page, the page never learns it (Principal ruling 2026-08-10, CD-072)

**Two rules, ruled together because one incident produced both.**

**(a) Silence is not a permitted gate outcome.** CD-059 requires unparsed shapes to be *named* in
the census; CD-060(b) makes a `☐`-bearing division REFUSE out loud. Both assume the shape reaches
the report. `math_arith_check.py` had a path where it did not: a division block whose numbers
would not parse was appended to nothing, so it was **neither verified nor reported**, and
**the census cannot name what the parser never returned**. The file then reads as fully covered.
**That is worse than an uncovered shape — an uncovered shape is visible.** In force: **every exit
from a shape parser appends something.** Unparseable is a **REFUSE with a line number**, never an
absence.

**(b) When the book's layout defeats a gate, the gate changes — not the transcription.** C5 গণিত
prints long division as **aligned digits under rules with no minus signs**; the reader identified
subtraction rows by a leading `−`, so those blocks yielded nothing. **Writing `−` into the
extraction to feed the parser would print something the book does not print, which §3 forbids.**
The parser was taught the layout instead: **the row immediately above a rule is the row being
subtracted**, which is true of the signed style as well, so one reader now handles both.

**The book uses both conventions, and that is the point.** ছাপা ৮ **does** print `− ৪ ০ ৫` and
`− ২ ২ ৫` — verified by 400 dpi crop during the sibling check — while ছাপা ৩৮ prints no signs at
all. **A gate keyed to one house style would have been silently wrong on half its own book.**

## 7.18 The মই-ভাগ (ladder) is a named shape — visible before it is verified (Principal ruling 2026-08-10, CD-073)

C5 গণিত finds লসাগু with a **ladder**, not a long division: the divisor line carries **several**
dividends at once, and each row is the row above **divided entry by entry**, with entries the
prime does not divide **carried down unchanged**.

**`math_arith_check.py` was right to refuse to parse it as a division — and wrong to then say
nothing.** Claiming no shape meant §7.17(a)'s never-vanish guarantee never engaged, so a block
dense with this book's own hazard — multi-column numerals in fixed layout, the §7.14.2c class —
was **invisible to the census**. In force: **a fenced block whose divisor line matches
`<prime> ) <n>, <n>[, …]` is reported as `ladder (মই-ভাগ)`, REFUSE**, with its line number and
rung count.

**Scope is visibility, and the limit is deliberate.** Verifying a ladder — every entry divisible
by the stated prime, indivisible entries carried down untouched, the left column's product equal
to the লসাগু — is a real evaluator and **a separate ruling**. Until it exists, ladder arithmetic
stays where it is: **read by hand at 400 dpi**. **REFUSE means "nothing here was machine-checked",
and saying so is the whole point** — an honest gap named in the census beats a silent one.

## 7.16 Assamese letters are not Bengali letters — an executed check, not a proofreading habit (Principal ruling 2026-08-10, CD-071)

**`ৰ` (U+09F0) and `ৱ` (U+09F1) have no valid use in a Bengali extraction.** They are the
Assamese letters of the shared Bengali-Assamese script; Bengali ra is `র` (U+09B0) and Bengali
ba is `ব` (U+09AC). A hit is therefore **never a house-style question and never a judgement
call** — which is exactly what makes it gate-able **with no false positives by construction**.

**`python tools/audits/bangla_script_check.py` fails on any occurrence in authored text**, in
any `canon/`, `_inbox/` or `workstreams/` markdown, printing every hit with file, line, column
and the word it sits in.

**Why it is code and not a habit.** The C5 গণিত অধ্যায় ৩ draft carried **27 occurrences across
8 words**, 18 of them `প্ৰাথমিক` — the running head of **every page of the book**. Against
`প্রাথমিক` that is one glyph's inner curve at reading size. **No human proofreader catches that
reliably; a machine catches it perfectly.** CR-003 was the mirror image — the machine channel
caught a dropped য-ফলা on a page already read at 400 dpi and signed off পূর্ণ. **One error a
machine misses and a human finds; one a human misses and a machine finds. Neither channel is
the reliable one — the reliability is in the disagreement**, which is §7.14's whole thesis,
now demonstrated in both directions on one chapter.

**Two exemptions, both narrow and both visible in the source:**

- **A file that declares itself `MACHINE OUTPUT`** in its header (§7.14 draft convention) is
  **counted and reported, never failed.** A committed OCR draft is *supposed* to contain these
  characters — it is evidence preserved byte-for-byte so the disagreement log can cite it, and
  "correcting" it would destroy the evidence.
- **A citation inside `backticks`.** The disagreement log and the corrections ledger must be
  able to quote `প্ৰাথমিক` in order to say it is wrong; **a gate that forbids naming the defect
  makes the defect unwriteable.** Inline code is already markdown's way of saying "literal
  string, not prose". **Bare prose stays clean, and fenced blocks are still checked** — in an
  extraction a fence carries authored transcription of the book, so contamination there is
  contamination.

## 7.15 The trip-wire counts only the disagreements it was built to catch — supersedes 7.14.2a's counting rule (Principal ruling 2026-08-10, CD-069)

**7.14.2a was written direction-blind, and the very first control set walked into the gap.** It
counts *any* substantive disagreement, so four disagreements would have voided C5 গণিত অধ্যায় ৩ —
including the one where the OCR was **right** and our own পূর্ণ-depth transcription was **wrong**
(CR-003, the dropped য-ফলা in `উপলক্ষ্যে`). Read literally, the rule retires the pipeline for
finding exactly what the pipeline exists to find.

**In force: the trip-wire counts only a substantive disagreement where the OCR LOSES on a plain-prose
line inside the 10% sample.** Explicitly **excluded from the count**:

- **the §7.14.2(b) weak-glyph classes** and **the §7.14.2(c) table, blank-box and `✗`/`✓` classes** —
  these are **crop-mandatory and are never accepted at draft value**, so an OCR failure there
  measures nothing about the sample. It was already going to be read at 400 dpi.
- **any disagreement where the OCR WINS.** That is not a trip-wire hit — **it is evidence the
  channel works**, and what it tightens is scrutiny of **our own prior reading**, not of the
  pipeline. It belongs in the corrections ledger as our error (AGENTS.md §6), not in the trip-wire
  count as the machine's.

**Everything else in 7.14.2a is unchanged:** one counted disagreement widens the sample to **25%**;
a second **voids OCR-corroboration for the chapter**, which drops to **raster-full**. **The
threshold did not move — only what is counted toward it.**

**Applied to the first control set (ছাপা ৩১–৩৪): zero trip-wire hits, one canon error caught.**
The three OCR failures (`পুরণ` for `পূরণ` · `গল্লটি` for `গল্পটি` · `সর্বনিয়` for `সর্বনিম্ন`) are
all weak-glyph-class and all crop-mandatory; the fourth was ours. **The pipeline proceeds, and the
reason it proceeds is written down rather than assumed.**
