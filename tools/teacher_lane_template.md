# teacher_lane_template.md — the brief a teacher-lane session is run from

**Authority:** CD-151 (2026-08-16), which vendored this file. **Before that row the template
existed only in chat briefs** — a files-over-memory breach (AGENTS §4) in the one artifact that
runs unattended under CD-141. **From now a teacher brief cites this path**, and the template gets
diff history like everything else.

**Provenance:** body vendored verbatim from `HANDOFF_2026-08-16_teacher-lane-live.md` §5, as
supplied by the Principal. **That handoff is not in this repo** — reported at filing, not
reconciled; the body below is the Principal's supplied text and he is its authority.

## How this file is operated — the two framing notes, verbatim from the handoff

> "Only the header line ever changes. S14/S15 line cites CD-147 superseding CD-139. Source path
> named explicitly. This is what the generation teacher runs; expert requests arrive via WhatsApp
> and are pasted as an added step 7 — the session validates the request against the chapter's
> declaration before authoring (inadmissible-slot request → STOP)."

> "Note for the thin-chapter chapters: once the CD row exists, step 3 gains one line — 'if a
> per-chapter thin-class ruling row exists for this পাঠ, PLAN runs in reduced mode per that row;
> absent the row, the standard applies.'"

**Status of the second note as of CD-151: NOT YET OWED.** Verified at source at filing time — no
thin-chapter ruling row exists anywhere in the repo, so step 3 carries no such line. **The note is
kept because it is the trigger**: the day that row is filed, step 3 gains the line and this note
is what says so. It is not a description of the template's current content.

**On the added step 7 in the first note:** an expert request pasted at the end is validated against
the chapter's declaration **before** authoring, and a request for an inadmissible slot is a STOP.
That renumbers nothing below — it is an addition the operator makes to a specific run, not a step
of the standing pipeline.

---

## TEMPLATE BODY — the brief. Only the header's `<N>` changes.

SCD প্রশ্নব্যাংক সেশন — বিষয়: বাংলা (BAN) · শ্রেণি: C5 · পাঠ: <N>
Teacher-lane session under CD-141 (as amended by CD-144). Bootstrap per tools/session_bootstrap.md:
clone from mount, repoint origin, fetch, hard-verify HEAD == origin/main before any work — stop on
mismatch, report both hashes.
Scope (hard boundary): bank-authoring classes only (declaration · plan · build · log); files under
workstreams/question-banks/ and banks/envelopes/, plus the log class's two named exceptions (root
SESSION_LOG.md, _wip/STATE.md). Any needed change outside that boundary, any gate FAIL not
resolvable inside it, any question needing a ruling → STOP and produce a report for the Principal.
Never ask the operator; never pad, patch policy, or improvise.
Pipeline:
1. Source: canon/marklogic/C5_Bangla_Source_13-23.md — the combined প্রশ্ন তৈরির উৎস file for
   পাঠ ১৩–২৩; the bank declares this path for SOURCE-TRACE. Verify the named পাঠ's section exists
   in it; stop-and-report if absent.
2. CD-138(e) admissibility declaration from the source at source — admissible slots, one-line
   content reason per exclusion. S14/S15 categorically excluded per CD-147 (superseding CD-139),
   no reason owed. Write the declaration to a file under workstreams/question-banks/_wip/ — AGENTS
   §3 puts all work-in-progress there, so a killed session is resumable from files alone.
3. Plan table per the register: per-slot content max, Bloom tags, pool size, every REF-06 floor
   with margin ≥2 (PLAN's standard). PLAN replaces the human countersign (CD-142). If PLAN cannot
   pass — including CD-141(g)'s 40-item minimum — STOP and report; grow-or-combine is the
   Principal's ruling. The plan table joins the declaration in the same _wip file (AGENTS §3).
4. Author to the plan. Teacher-keyed items short_answer/descriptive only (P-037). §4
   near-duplicate ban.
5. Full suite. CLEAN required — N/A counts as not-CLEAN except the ten qp6-shape gates CD-145
   names.
5b. Factual/curation review (CD-151). Run tools/bank_factual_review_prompt.md from that path,
   filling only its facts block from the declaration and the source's own ⚠ block. NEVER compose
   the prompt in-session — an agent that writes its own review prompt has left this template.
   Paste the reviewer's report verbatim. Fix every defect inside the lane and log each fix in
   SESSION_LOG.md with its qid and what changed; unlogged self-correction is barred. Re-run the
   prompt against the rebuilt bank — the verdict of record is the LAST run. Anything needing a
   ruling or a change outside the lane → STOP and report. 5b is pre-import screening, not the §6
   review; CD-142 is unaffected and a clean verdict is not approval.
5c. Sibling sweep (AGENTS §6). Any fix made at 5b must be checked across the sibling banks in the
   same session — run the suite over every bank in banks/, not only this chapter's, and report each
   verdict. A defect fixed in one bank and left standing in its siblings is the thing §6 names.
6. Regenerate all export artifacts: array, single/, batch wrapper — ENVELOPE-SYNC in sync, one
   digest. Then run the vendored harness over the regenerated output — every single/ envelope and
   the batch wrapper through tools/hub-export/validate_import.py, which AGENTS §11 requires at
   authoring time. ENVELOPE-SYNC proves the three artifacts agree with each other; the harness
   proves they satisfy the LOCKED import contract. Neither substitutes for the other.
7. REPO-WIDE GREEN + 5b clean + scope held → push per CD-141's standing authorization; paste the
   CD-083(b) range check per commit across origin/main..HEAD plus post-push server verification.
   Repo-wide green is CD-153: every gate in the repo, not only this workstream's suite, minus the
   exclusions CD-153 names — canon_check.py is IN, and a build commit that adds a canon citation
   is exactly what reddens it. A red the session did not cause is still a stop: a red repo is not
   pushed onto, whoever reddened it. Anything else → stop-and-report, nothing pushed.
Session log records everything. The bank awaits Hub import and subject-expert review; nothing here
is promotion.

## TEMPLATE BODY — ends here
