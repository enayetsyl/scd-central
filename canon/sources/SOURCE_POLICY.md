# SOURCE_POLICY — v1.1

*Canon. Adopted v1.0 by Principal ruling 2026-08-09 (CD-037), superseding the v0.1 draft staged in `_inbox/`.*
*v1.1 (CD-046) adds **§7 Amendments** — three Principal rulings made when the first extraction was built. §7 is forward-only: the sections it supersedes are left as written and are not edited.*
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
