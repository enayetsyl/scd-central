# _wip/STATE.md — question-banks (session-resumable state)

| Field | Value |
|---|---|
| Current build | **পাঠ ১৪ (কুপোকাত) 84 items, digest `831c54c1aa7d` · পাঠ ১৩ 110 items, digest `22ae7c4f299a` after `QB-CR-014`'s eight-tag correction.** Both suites CLEAN, both exports in sync across array · `single/` · `.batch.json`. পাঠ ২১ CLEAN, untouched. |
| Phase | **`CD-141` dry run COMPLETE and its one defect ruled (`CD-144`).** Handover to unattended use remains the Principal's call, not the agent's. |
| Last completed step | `677cc62` ruling (CD-144) · `775b5cd` log (পাঠ ১৪ block appended) · `21f3445` corrections (QB-CR-014, eight tags + export) · `c1a3ccc` build (signature re-pinned) · this file. Session run OUTSIDE the teacher lane on normal approval. |
| Next step | The Principal's call on `CD-141` handover. Then the next chapter, or পাঠ ১৪ wave 2 against the content named in that bank's `gaps`. |
| Blockers / open PENDING-P tags | **None outstanding from this session** — the CD-141 contradiction is ruled at `CD-144`. · **`PENDING-P-038` RAISED** (nothing checks a slot is admitted by ANY chapter) — FLAGGED-not-OPEN. · **`PENDING-P-008` FLAGGED** — REF-19 has no punctuation slug; পাঠ ১৪'s six S11 items ride `BAN-SENTENCE` under `TOP-BAN-C5-13`, the established choice. |
| Files in `_wip` awaiting "done" | this file · `U13_BLOOM_PROBE_2026-08-15.md` · `U13_ADMISSIBILITY_DRAFT_2026-08-15.md` · `BAN_C1-C4_REGISTER_BLOCKED_2026-08-15.md` · `U13_REVIEW_SHEET_2026-08-15.md` · `RULING_DRAFTS_teacher-lane_2026-08-15.md` |

## RESOLVED — `CD-144` amends `CD-141(b)`, and the dry run is what found the defect

**The blocker this file carried on 2026-08-16 is closed.** `CD-141(a)` pre-approved the `log`
class while `CD-141(b)` confined every authorized commit to `workstreams/question-banks/`, leaving
root `SESSION_LOG.md` — `log` class at a root path — unreachable, and with it **AGENTS §3's End
clause, from inside the lane it governs**.

**`CD-144` (2026-08-16) names two path exceptions, `log` class ONLY:** root `SESSION_LOG.md` and
this file. **No other root file, no other class** — a `build`, `corrections` or `promotion` commit
touching a root file is still unauthorized and CD-141(b)'s two tests both still have to hold.
`CD-141`'s text is unedited; the amendment is a new row with a forward-only pointer, and AGENTS
§3.1's carve-out paragraph is updated to match.

**The held পাঠ ১৪ block is appended** — handed over as a file, staged in `_inbox/` by the
Principal, read from the mount, and verified byte-identical to the handed-over text with only its
scaffolding comment stripped.

**What is worth carrying forward is not the fix but how it surfaced.** `CD-141(h)` required one
attended run before handover, and it was filed knowingly on a single ledger instance. That run
produced a CLEAN 84-item bank **and** this defect — and **the clause reads correctly right up
until a session tries to close under it**. Reading the row could not have found it.

## পাঠ ১৪ — the authored state

**84 items, digest `831c54c1aa7d`** over the `questions` array alone, sorted by qid, header
excluded — the same quantity `ENVELOPE-SYNC` checks and the batch wrapper carries.

| level | count | % | floor | margin |
|---|--:|--:|--:|--:|
| Remember | 22 | 26.2% | 20% (17) | **+5** |
| Understand | 24 | 28.6% | 25% (21) | **+3** |
| Apply | 24 | 28.6% | 25% (21) | **+3** |
| Analyze | 12 | 14.3% | 10% (9) | **+3** |
| Evaluate | 2 | 2.4% | 0% | +2 |
| Create | 0 | 0.0% | 0% | content fact, CD-135(d) |

Slots: S02 8 · S03 12 · S04 6 · S05 8 · S06 6 · S07 10 · S08 8 · S10 6 · S11 6 · S12 6 · S13 8.
Every one clears its CD-138(g) demand; the eleven admitted slots owe 52 and the bank supplies 84.

**FOUR SLOTS ARE DECLARED INADMISSIBLE, and two of them are new to this chapter.** S14/S15 as at
পাঠ ১৩. **S01 and S09 are excluded because পাঠ ১৪ IS A নাটক** — and the reason is the source's own
sentence, not an inference: *"কবিতা চারটি: পাঠ ১৩, ১৫, ১৮, ২০ — এগুলোই S01 (কবিতা মুখস্থ) ও S09
(মূলভাব) প্রশ্নের উৎস।"* পাঠ ১৪ is not one of the four. **CD-138(e) forbids inferring
admissibility from content, and quoting the source's own designation is not that inference** — the
file says which chapters feed those two slots, and this chapter is not on the list.

**`QB-CR-009` IS DISCHARGED HERE AND THE DISCHARGE COST NOTHING, WHICH IS THE POINT OF HAVING
CAUGHT IT EARLY.** The row was RULED 2026-08-14 (U14 is Drama `TOP-BAN-C5-09`, not Story `-06`)
with execution owed "when the U14 bank is next opened". **No U14 item existed on disk** — verified
by grep across `banks/`, not assumed — so the correction is discharged by authoring `-09` from the
start rather than by editing anything. **A re-tag of live items would have been the expensive
version of the same fix.**

## Three things a later session must not re-derive

- **`-13` IS THE PUNCTUATION TAG AND পাঠ ১৩ NOW CARRIES IT — corrected, `QB-CR-014`.**
  `TOPIC_NUMBERS.md`'s own *"Why `-13` was minted rather than folded into `-02`"* says the spine
  keeps `S03 বাক্য গঠন` and `S11 বিরামচিহ্ন` as separate mark slots at C5. পাঠ ১৩'s eight S11 items
  carried `-02`; they now carry `-13`, digest `e76631e34fa0` → `22ae7c4f299a`, signature re-pinned
  with the sign-off standing. **The lesson outlives the fix: `TOPIC-NUMBER` proves a tag EXISTS,
  never that it is the RIGHT one for its slot** — both numbers are charted, so both banks passed
  and would have gone on passing. **A number minted for a slot must be checked INTO USE, and
  nothing does that today.** `ref19_topic_id` stays `BAN-SENTENCE` everywhere: REF-19 has no
  punctuation slug at all (PENDING-P-008).
- **THE BANK IS AT ITS BLOOM LIMIT, NOT ITS CONTENT LIMIT, AND THE HEADER NAMES WHAT IS LEFT.**
  The অর্থ জেনে নিই list carries about thirty glossed words and S02 took eight; thirteen are named
  unextracted in `header.gaps`. **A content limit is a claim about how far the book was read**
  (the wave-3 lesson at পাঠ ১৩), so this wave claims no such limit.
- **C-19 IS A PROHIBITION ON THIS CHAPTER, NOT A PREFERENCE.** অনুশীলনী ৬ (শ্রেণিকক্ষে নাটকটি
  অভিনয় করি) is unusable, no item may ask a student to play a character, and C-05 bars animal
  pictures. অনুশীলনী ৩'s সংলাপ is left to a later wave for that reason and the reason is in `gaps`
  — writing it needs the "student writes as themselves" condition held in a rubric row.

## Carried forward, unchanged

- **Contract v1.1's four traps** — `envelope_version` stays `"1.0"`; the wrapper is EXACTLY FOUR
  KEYS; `digest` is an AUDIT field the Hub does not recompute; `items` is the loosest gate in the
  contract, deliberately. All four survived this bank's export unchanged.
- **`jsonschema` must be installed before the harness runs** —
  `pip install --break-system-packages 'jsonschema>=4.18'`. The vendored copy predates
  `Draft202012Validator` and the failure presents as N content failures and is nothing of the kind.
- **Work happens in a container clone** (`tools/session_bootstrap.md`). The mount is the
  Principal's pull-only working copy. **This session's bootstrap caught the mount five commits
  behind `origin` and stopped**, which is what step 4 exists for.
- **`_inbox/` still holds the three superseded v1.1 originals plus a redundant v1.0
  `import-contract.md`** — the mount is pull-only for agents, so removing them is the Principal's
  (AGENTS §12.4/§12.5).
- **UP-002** `pool` field · **UP-003** `ref19_topic_id` rejects `MATH-*-REL`, blocking every C5
  Math bank.
- **C4 S11's declaration is OPEN on the Principal's ruling** — the register keeps
  `selected: বিরামচিহ্ন বসানো` with its RAISED note.
- **No gate reads a spine file.** The spine parse lives at build time in
  `tools/audits/slot_register_check.py`. Both halves of CD-138(b) stay seeded.
