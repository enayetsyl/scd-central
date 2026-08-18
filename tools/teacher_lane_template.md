# teacher_lane_template.md — the brief a teacher-lane session is run from

**Authority:** CD-151 (2026-08-16) vendored this file. **CD-171(h) (2026-08-18) rewrote it
subject-neutral and multi-chapter — Principal-ruled, not an agent diff.** Before CD-151 the
template existed only in chat briefs, a files-over-memory breach (AGENTS §4) in the one artifact
that runs unattended under CD-141. **A teacher brief cites this path**, and the template gets diff
history like everything else.

**Provenance:** the CD-151 body was vendored verbatim from `HANDOFF_2026-08-16_teacher-lane-live.md`
§5, as supplied by the Principal; **that handoff is not in this repo** — reported at filing, not
reconciled. **This version is not that text.** It generalises the pipeline to any (subject, class)
and to a LIST of chapters, and it removes the count gates CD-171(a) retired. **Every hard boundary
is carried across unchanged and is re-stated rather than assumed** — a rewrite is exactly where a
boundary goes missing by being obvious to the person doing the rewriting.

## What changed at CD-171, and what did not

**CHANGED.** The header takes a **subject**, a **class**, a **chapter LIST** and a **source path**,
instead of naming Bangla C5 and a single `<N>`. **Step 3 is no longer a plan table with floors and
margins** — there are no pool floors, no 40-item minimum, no per-slot demand asked of a chapter and
no ceiling (**CD-171(a)**). **Step 5b no longer gates the push** (**CD-171(g)**, superseding
CD-151(c)): it runs, its report is committed, and the report travels to the Hub as reviewer input.

**NOT CHANGED, and listed because a generalisation is where these get dropped.** Never ask the
operator (**CD-141(e)** — the teacher is a zero-Git operator and cannot rule; a question put to
someone who cannot answer it is a way of proceeding without one). **Never pad.** **Never patch
policy.** **Stop and report on anything outside the bank-authoring classes.** The scope boundary is
still drawn TWICE, by class AND by path (**CD-141(b)**), and a commit passing one test and failing
the other is not authorized. 5b is still never composed in session (**CD-151(a)**), every fix is
still logged with its qid (**CD-151(b)**), and the reviewer's report is still a committed artifact
(**CD-157(d)** — a 5b run without a committed report is not a run).

**ON PADDING, now that no gate counts.** CD-141(g)'s bar on authoring items to satisfy a gate is
retired with the gate. **The reason survives the rule** (CD-151(b)): an item authored to move a
number is not an item, and there is no longer even a number for it to move. **A chapter's pool is
finished when the source is exhausted, not when it reaches a size.**

## How this file is operated

**The header is the only part the operator fills.** Everything below it is fixed text.

**A chapter LIST, not a chapter.** The session runs the per-chapter loop once per listed chapter,
**in list order**, and **commits once per chapter** (CD-083(d)). A chapter that stops does not
abort the chapters before it — their commits stand — and the session reports which chapter stopped
and why. **It does not skip a stopped chapter and carry on to the next**: a list is an order, not a
set, and a later chapter may depend on a ruling the stopped one raised.

**Expert requests arrive out of band** (WhatsApp) and are pasted as an added step 7. **The session
validates the request against that chapter's declaration BEFORE authoring, and a request for an
inadmissible slot is a STOP.** That renumbers nothing — it is an addition the operator makes to a
specific run, not a step of the standing pipeline.

**The thin-chapter note that CD-151 carried is DELETED.** It read: *"once the CD row exists, step 3
gains one line — if a per-chapter thin-class ruling row exists for this পাঠ, PLAN runs in reduced
mode per that row."* **No such row will ever exist. CD-171(f) closes the thin-chapter question as
dissolved rather than ruled** — it lived in CD-141(g)'s grow-or-combine clause, which CD-171(a)
retires, and it was never a `PENDING_PRINCIPAL.md` row. **A thin chapter is now an ordinary
chapter**: it authors what its source supports and stops. পাঠ ১৯ and ২৩ are buildable with no
per-chapter ruling, and **no thin-chapter class is to be minted** — a category defined by a
threshold that no longer exists would have no members.

---

## TEMPLATE BODY — the brief. Only the header block changes.

SCD প্রশ্নব্যাংক সেশন
  বিষয় (subject): <SUBJECT — e.g. বাংলা (BAN) · ইংরেজি (ENG)>
  শ্রেণি (class):  <C1 | C2 | C3 | C4 | C5>
  পাঠ তালিকা (chapter list): <e.g. ১৯, ২৩  — one or more, run IN THIS ORDER>
  উৎস (source path): <repo-relative path to the extraction that carries every listed chapter>

Teacher-lane session under CD-141 (as amended by CD-144 and CD-153). Bootstrap per
tools/session_bootstrap.md: clone from the mount, repoint origin, fetch, and hard-verify
HEAD == origin/main before any work. Stop on mismatch and report both hashes; take CD-152's
benign-behind or CD-156's benign-ahead branch only by running the commands, never by judgement.

Scope (hard boundary, and BOTH tests must hold — CD-141(b)): bank-authoring classes only
(declaration · plan · build · log), on files under workstreams/question-banks/ and
workstreams/question-banks/banks/envelopes/, plus the log class's two named exceptions (root
SESSION_LOG.md and _wip/STATE.md). A commit whose CLASS is pre-approved but whose PATH is not, or
the reverse, is NOT authorized. Any needed change outside that boundary, any gate FAIL not
resolvable inside it, and any question needing a ruling → STOP and produce a report for the
Principal. NEVER ASK THE OPERATOR (CD-141(e)). Never pad, never patch policy, never improvise.

PER CHAPTER, in list order. Steps 1–7 run once for each listed chapter, and each chapter ends in
ONE commit before the next begins.

1. Source. Read the header's source path. Verify the named chapter's own section exists in it;
   stop-and-report if absent. The bank declares that path for SOURCE-TRACE. Do not substitute a
   different file and do not read a second one — one chapter, one declared source.

2. Declaration (CD-138(e)). Derive the chapter's admissible slots FROM THE SOURCE AT SOURCE, with a
   one-line CONTENT reason for each excluded slot. The reason must be that the content does not
   support the slot, never that the chapter's own "কোন প্রশ্নে কাজে লাগবে" line did not name it
   (CD-134) — the two look identical in a header and are not.
   Paper-level slots are outside what a declaration may say at all and owe NO reason: BAN-S14 and
   BAN-S15 at every class (CD-147); ENG-S05 at C3/C4/C5, ENG-S13 and ENG-S14 at C4/C5 (CD-150).
   A bank silent about them is CORRECT, not incomplete; a header ADMITTING one FAILs.
   Write the declaration to a file under workstreams/question-banks/_wip/ — AGENTS §3 puts all
   work-in-progress there, so a killed session resumes from files alone.

3. Author. EVERY ADMISSIBLE TYPE, AS MANY AS THE CHAPTER'S CONTENT SUPPORTS, AND THEN STOP.
   There is no minimum, no maximum, no Bloom floor, no Bloom band and no per-slot demand at pool
   level (CD-171(a)). The bound is source exhaustion under §4's near-duplicate ban: stop when the
   extraction is exhausted, because past that point new questions are near-duplicates of existing
   ones. A chapter that supports twelve items is finished at twelve.
   Every item still declares the task it does, in the register's own vocabulary, matching the
   spine's কারণ column for its (subject, class, slot) — a slot id is not a task, and marks are not
   a task (CD-138(b)).
   Bloom levels are tagged on every item — RECORDED, NOT RATIONED (CD-171(b)). An untagged item, or
   one outside the six LOCKED levels, still FAILs.
   Taught-set constraints bind: no item may require a term or a mark the class's source does not
   print (CD-165, amended by CD-166).
   Teacher-supplied keys ride short_answer and descriptive only (P-037), declared in the item's own
   model_note (CD-136(b)).
   DO NOT AUTHOR AN ITEM TO REACH A NUMBER. There is no number.

4. Full suite. CLEAN required. N/A counts as not-CLEAN except the qp6-shape gates CD-145 names —
   a gate that did not judge is not a gate that passed (CD-141(c)).

5. Factual/curation review — STEP 5b (CD-151, non-blocking per CD-171(g)).
   Run tools/bank_factual_review_prompt.md FROM THAT PATH, filling only its facts block from this
   chapter's declaration and the source's own ⚠ block. NEVER compose the prompt in session — an
   agent that writes its own review prompt has left this template, and the reason is not tidiness:
   the prompt chooses which questions get asked, so an author who writes it selects the grounds on
   which their own work is graded.
   The FACTS BLOCK takes STRINGS, not tokens (CD-157(f)): enumerate the permitted forms. A token is
   cheap to write and matches inside other words — সাজা matched inside সাজানো and produced three
   false positives the session had to own.
   WRITE THE REPORT to workstreams/question-banks/reports/ AND COMMIT IT (CD-157(d)). A 5b run
   without a committed report is NOT A RUN, and a verdict line is not a report.
   Fix every defect inside the lane and log each fix in SESSION_LOG.md with its qid and what
   changed — unlogged self-correction is barred (CD-151(b)). Re-run the prompt against the rebuilt
   bank; the verdict of record is the LAST run.
   5b DOES NOT GATE THE PUSH (CD-171(g), superseding CD-151(c)). A non-clean verdict does not hold
   the bank back; the report travels with it to the Hub as reviewer input. But a defect whose FIX
   needs a ruling, or a change outside the lane, is STILL a STOP — what 5b lost is its veto over a
   clean bank, not the session's obligation to stop when it cannot proceed honestly.
   5b is pre-import screening and narrows nothing: CD-142(a)'s item-level content review by the
   Hub's subject experts stands, a clean verdict is not approval, and promotion reviewed → gold
   remains the Principal's act in the Hub (CD-003).

6. Sibling sweep (AGENTS §6). Any fix made at 5b is checked ACROSS the sibling banks in the same
   session — run the suite over every bank in banks/, not only this chapter's, and report each
   verdict. A defect fixed in one bank and left standing in its siblings is the thing §6 names.
   Enumerate every occurrence of the claim, not only the flagged instance (TOOLS-CR-008), and
   record the scope of the search: a token sweep closes a phrasing, not a claim.

7. Exports. Regenerate all three artifacts — array, single/, and the v1.1 batch wrapper — so
   ENVELOPE-SYNC is in sync on one digest. Then run the vendored harness over the regenerated
   output: every single/ envelope and the batch wrapper through tools/hub-export/validate_import.py,
   which AGENTS §11 requires at authoring time. (If it reports N content failures, check
   jsonschema first: `pip install --break-system-packages 'jsonschema>=4.18'` — the vendored copy
   predates Draft202012Validator and the failure presents as content when it is an import.)
   ENVELOPE-SYNC proves the three artifacts agree with each other; the harness proves they satisfy
   the LOCKED import contract. NEITHER SUBSTITUTES FOR THE OTHER.

8. ONE COMMIT for this chapter, then move to the next listed chapter at step 1.
   Paste git status immediately before the commit (QB-CR-016 — the git-mv staging hazard).

AFTER THE LAST CHAPTER — push, once, for the whole run.
   Condition: REPO-WIDE GREEN (CD-153) and scope held. Repo-wide green means EVERY gate in the
   repo, not only this workstream's suite, minus the exclusions CD-153 names — canon_check.py is
   IN, and a build commit that adds a canon citation is exactly what reddens it. A red the session
   did not cause is still a stop: a red repo is not pushed onto, whoever reddened it.
   5b clean is NO LONGER part of this condition (CD-171(g)).
   Push per CD-141's standing authorization; paste the CD-083(b) range check PER COMMIT across
   origin/main..HEAD with each commit's class stated, then verify server-side with git ls-remote
   asked of the SERVER, not of a local remote-tracking ref (AGENTS §3.1).
   Anything else → stop and report, nothing pushed.

Session log records everything: every chapter, every verdict, every fix, every stop. The banks
await Hub import and subject-expert review; nothing here is promotion.

## TEMPLATE BODY — ends here
