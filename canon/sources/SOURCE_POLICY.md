# SOURCE_POLICY — v1.0

*Canon. Adopted by Principal ruling 2026-08-09 (CD-037), superseding the v0.1 draft staged in `_inbox/`.*
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

The gate in §5 has **no executing script yet** — no extraction has been produced under this
policy, so there is nothing to run it against. It is written when the first extraction under
this policy is built (C5 Bangla 1–12), and until then §5 is a specification, not a proven gate.
`C5_Bangla_Source_13-23.md` predates this policy and is grandfathered as canon by CD-004.
