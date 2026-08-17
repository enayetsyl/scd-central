# bank_factual_review_prompt.md — the vendored factual/curation review (teacher-lane STEP 5b)

**Authority:** CD-151 (2026-08-16). **This file is the prompt. It is never composed in-session.**
A session runs step 5b by pasting the body below, filling ONLY the facts block, and handing it to
an independent reviewer. **An agent that writes its own review prompt has left the template** —
the prompt that grades a bank cannot be authored by the party whose bank is being graded, and a
review whose questions were chosen by the author is not independent review.

**Where the per-chapter input comes from.** The facts block is not research. Every field is
already produced by steps 2–3 of the same session — the CD-138(e) declaration yields the
admissible slots, the source's own ⚠ block yields the content bars, and the chapter section
yields the named people, events and dates. **If a field cannot be filled from work already done,
that is a signal the declaration is incomplete, not an invitation to go and find the answer.**

**WHAT THIS IS NOT.** Step 5b is **PRE-IMPORT SCREENING**. It is **not** the §6 human review and
it does not narrow **CD-142(a)** by one word: item-level content review — whether a question is
*good*, whether a teacher-supplied key is *right*, whether a stem suits the class — belongs to the
Hub's subject experts and still does. **A CLEAN 5b verdict is not approval, is not a sign-off, and
is not promotion.** It means the bank is fit to be offered for import, nothing further. Promotion
`reviewed → gold` remains the Principal's, in the Hub (CD-003).

---

## How to run it

1. Fill the facts block. Nothing else in the body is edited, ever.
2. Hand the filled body to a reviewer with read access to the repo and no write access.
3. Paste the reviewer's report into the session, verbatim.
3a. **WRITE THE REPORT TO `workstreams/question-banks/reports/` AND COMMIT IT** —
   `BAN_U<NN>_REVIEW_<YYYY-MM-DD>.txt`, verbatim, with the bank path and the run date at the top.
   **A 5b run without a committed report is NOT A RUN, and a verdict line is not a report**
   (CD-157). The verdict is a claim; the report is the evidence for it. Keeping the claim and
   discarding the evidence leaves a bank marked *reviewed, N defects* with **nothing in the repo
   saying which N** — no later session can act on it, audit it, or tell a fixed defect from an
   unfixed one. **This happened:** the 2026-08-17 retro logged four verdict lines and no bodies,
   and 61 per-qid findings against four PUSHED banks survived only in a transcript. **A report
   recovered from a transcript is admissible and must be marked as recovered, carrying the date of
   the ORIGINAL run.**
4. Fix every defect **inside the lane**, and log each fix in `SESSION_LOG.md` with its qid and
   what changed (CD-151(b) — unlogged self-correction after a self-run review is barred).
5. Re-run this prompt against the rebuilt bank. **The verdict of record is the LAST run**, and a
   fix that has never been re-reviewed leaves the bank without a clean verdict.
6. Anything not fixable inside the lane → **STOP and report** (CD-151(c)).

---

## FACTS BLOCK — the only part that changes

```
BANK FILE      : <repo-relative path to the bank JSON>
SOURCE FILE    : <repo-relative path to the extraction>
SOURCE SECTION : <the heading that opens this chapter's section, and the heading that ends it>
ADMITTED SLOTS : <the slot ids this chapter's header declares admissible>
NAMED CONTENT  : <the people, events, dates, places and titles the chapter section states as
                  fact — the things an answer key can be checked against>
CONTENT BARS   : <each ⚠ bar from the source's own block, one per line, as the EXACT STRINGS to
                  search — NEVER a bare token — plus one line on what the bar forbids>
PERMITTED NAMES: <for each barred STRING, the exact strings in which it is PERMITTED because the
                  book itself prints them as a proper name — declared here, never judged by the
                  reviewer in-session. If a barred string has no permitted form, write NONE.>
```

**STRINGS, NEVER TOKENS — CD-157(f), and it cost three false positives to learn.** A bare token
matches inside unrelated words. The 2026-08-17 retro declared `সাজা` and it matched inside
**সাজানো** (*to arrange* — a different lexeme) at পাঠ ১৪ `Q51`/`Q54`; it declared `ছবি` and it
matched figurative word-imagery at পাঠ ১৫. **The reviewer was right to report all three** — it is
told to report any occurrence that is not a declared string and forbidden from deciding for itself
which uses look harmless. **The fault was the declaration.** The fix is that declaring a bar now
costs the session real work: enumerate the forms the bar actually reaches, and enumerate every
permitted string beside them. **A token is one word to write; a string set makes the session do the
thinking the reviewer is barred from doing.**

**`PERMITTED NAMES` is declared, not judged, and that is the point.** A reviewer deciding
in-session which uses of a barred word are acceptable is making a curation ruling. The session
declares the permitted strings from the source; the reviewer's job is the mechanical one — find
every occurrence, and report any that is not one of the declared strings.

---

## PROMPT BODY — paste from here, verbatim

You are a verification reviewer for a Class-5 question bank. **Do NOT edit any file. Report only.**

The bank has already passed its full structural gate suite, so conformance is proven. Your job is
the part no gate can do: **factual and curation correctness**. Read the bank JSON and the named
section of the source file. The source section is the ONLY authority for fact — not your own
knowledge of the subject, and not the wider file.

Facts block for this run:

```
<paste the filled facts block here>
```

Check the following. Report each as **PASS**, or as a numbered list of defects **each naming the
exact qid**. Be terse; do not restate at length what is fine.

**1 · FACTUAL ACCURACY.** For every item, is the answer correct against the source section? Cover
`answer_key.accepted`, the `is_correct` MCQ option, every distractor's `why_wrong`, every
`blanks.accepted`, and every rubric `band_descriptors` string. Flag: any answer that contradicts
the source; any date, name, role or attribute that is wrong or swapped between people; any MCQ
where a distractor is arguably also correct; and **any model answer that asserts something the
source section does not state** — a key that reaches beyond the section is a defect even when the
claim is true in the world, because the student is being marked against the section.

**2 · THE CHAPTER'S CONTENT BARS.** For each token in `CONTENT BARS`, search **every
student-facing string**: `question_text`, MCQ option `text`, `why_wrong`, `answer_key.accepted`,
`answer_key.model_note`, rubric `criterion`, and rubric `band_descriptors`. List **every**
occurrence with its qid and field. For each, say whether it is one of the strings declared in
`PERMITTED NAMES` — permitted — or anything else, which is a **DEFECT**. Do not decide for
yourself whether an undeclared use seems harmless; report it.

**3 · STANDING CURATION BARS.** Verified at source in `canon/islamic-curation/`:
**C-03** music and dance including all percussion · **C-05** depictions of living beings ·
**C-18** nationalism over ummah and nationalist veneration rituals — flag salutes, wreaths or
flowers at monuments, ritual silence. C-18's own carve-out permits **factual history** — dates,
events, contributions — so report the ritual, not the history. Confirm no item draws on barred
material and no item requests a picture of a person. Note that a rubric row which *forbids* barred
content is correct and is not an occurrence.

**4 · INVENTED NAMES.** Every personal name in the bank must be either a figure the chapter itself
records, or a name from the approved pool. Flag any invented character.

**5 · NUMERALS.** Flag any ASCII digit `0-9` in a student-facing string; Bengali numerals only.
Internal codes inside a teacher-facing `model_note` are not student-facing and are not defects.

**6 · SLOT-SPECIFIC CORRECTNESS.** Apply only the checks whose slot appears in `ADMITTED SLOTS`.
- **S12 যুক্তবর্ণ** — is the conjunct decomposition orthographically right, and does the newly
  formed word actually contain that conjunct? Also flag any stimulus word carrying **more than
  one** conjunct where the stem does not say which one is meant.
- **S10 পদ নির্ণয়** — is the answer the right part of speech for the target word **as used in the
  given sentence**? Flag any accepted answer that is a super-class rather than the পদ itself, and
  any term that is not standard Bengali grammar.
- **S13 এক কথায় প্রকাশ** — does the answer actually match its definition phrase? Flag a definition
  the chapter also satisfies with a different word that is not accepted, and any accepted form
  whose grammatical class does not fit the definition.
- **S06 বিপরীত শব্দ** — does the stimulus word's use *in this chapter* support the antonym given?
  A word used adverbially or idiomatically may have no antonym in the sense the chapter uses it.
- **S11 বিরামচিহ্ন** — is every required mark inside the punctuation set taught at this class, and
  does each item require more than a single terminal mark?

**7 · LANGUAGE.** Are stems, keys and rubric rows natural, grammatical and appropriate for the
class? Flag anything clumsy, ambiguous, or above the class level. Flag any internal policy code
that has leaked into marker-facing or student-facing text.

Finish with one line and nothing after it:

`VERDICT: CLEAN` or `VERDICT: N DEFECT(S)`

## PROMPT BODY — ends here
