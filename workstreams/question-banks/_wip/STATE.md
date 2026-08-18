# _wip/STATE.md — question-banks (session-resumable state)

| Field | Value |
|---|---|
| Current build | **পাঠ ১৯ (ভাষার খেলা) 46 items · পাঠ ১৮ (ইচ্ছামতী) 79 items · পাঠ ১৭ (মাটির নিচে পুরানো নগর) 78 items — built in PARALLEL 2026-08-18, three isolated `git worktree`s, one per chapter.** All three chapter suites CLEAN; all three exported and **hand-counted** (array · `single/` · `batch.item_count` each equal to the bank's item total) and passed through `validate_import.py`. Earlier: পাঠ ১৬ 96 · পাঠ ১৫ 96 · পাঠ ১৪ 84 · পাঠ ১৩ 110, all four CLOSED to in-repo fixing by **`CD-170`**. |
| Phase | **Post-`CD-171`. THERE ARE NO POOL-LEVEL COUNTS — no Bloom floor, no band, no per-slot demand, no minimum and no ceiling (`CD-171(a)`); every count binds the PAPER (`CD-171(b)`).** The margin and floor tables in the closed per-chapter sections below are **pre-CD-171 history and are not a live standard** — they are left unedited per AGENTS §7's forward-only rule and must not be read as targets. **What binds a bank is `CD-171(c)`'s five-item list and nothing else.** Step 5b runs and is **non-blocking** (`CD-171(g)`); its report is a committed artifact (`CD-157(d)`). |
| Last completed step | পাঠ ১৭ · ১৮ · ১৯ built, fixed, exported and pushed under a Principal-ruled parallel brief. Seven commits: `CD-173` · `CD-174` · `PENDING-P-042` (rows, filed serially, each number verified against a freshly fetched `origin` immediately before its own commit per `CD-154`), then one build commit per chapter, then this log. Bootstrap verified `HEAD == origin/main == 0574e877` before any work. |
| Next step | **Nothing is owed on পাঠ ১৭ · ১৮ · ১৯ in repo.** Their standing 5b defects travel to the Hub under `CD-142(a)`. Next chapters by content: **পাঠ ২০ (শিক্ষাগুরুর মর্যাদা)** — on the extraction's four-poem list, so S01 and S09 are admissible and `CD-149`'s printed-line span applies · **পাঠ ২২ (আমরা তোমাদের ভুলব না)**, the ছক's best source for **S06 বিপরীত শব্দ** and carrying **পাঠ ১৬'s শহিদ bar plus two more of its own** · **পাঠ ২৩**, which `CD-171(f)` names buildable alongside ১৯ and which shares `TOP-BAN-C5-15`. **Carry forward: the ছক's S10 ক্রিয়ার কাল line and its S11 প্রশ্ন তৈরি line both name tasks C5 does NOT select** — off-choice at `COVERAGE` (`CD-138(b)`), and পাঠ ১৭ hit both. |
| Blockers / open PENDING-P tags | **Nothing BLOCKS.** · **`PENDING-P-042` OPEN (raised this session, deliberately not built): `ENVELOPE-SYNC` declares a never-exported bank in sync** — the no-export branch at `gates.py:1822` needs BOTH the array and `single/` absent, and `single/` is shared, so for any new bank it is unreachable. **A green `ENVELOPE-SYNC` is not evidence that an export EXISTS. Hand-count every export until this is fixed.** · **`CD-174` is filed with EXECUTION OWED**: the `[[CD-136]]` machine-segment convention is **not adopted into any bank** because no render step in the bank path consumes `model_note`, so nothing would strip the delimiter; banks carry the plain `(CD-136)` form deliberately. · **`QB-CR-017` OPEN** — thirteen S11 single-mark items in U13–U16, unfixable in repo under `CD-170`; পাঠ ১৭/১৮ authored against it with a build-time check that refuses a count of one, পাঠ ১৯ has no S11. · **`PENDING-P-038` RAISED** · **`PENDING-P-008` FLAGGED** — REF-19 has no punctuation slug; S11 rides `TOP-BAN-C5-13` / `BAN-SENTENCE`. **`TOP-BAN-C5-15` is now in use for the first time**, at `U19 Q31`. · **`CD-173` records a live gap: `TAUGHT_SET_REQUIRED` is hardcoded to `(BAN,5,S11)` and the widening is SCOPED, not coded — the executor under-enforces until it is.** · **§4's near-duplicate ban has NO executing gate on a qp6 bank** — `ZERO-OVERLAP` is N/A and PLAN's scan is within-slot at 0.95. Measured: **U14 and U15 carry byte-identical cross-slot stems.** Principal ruled 2026-08-18: **keep as is, no gate, no row** — recorded so it is not re-derived. |
| Files in `_wip` awaiting "done" | this file · `U19_ADMISSIBILITY_2026-08-18.md` · `U18_ADMISSIBILITY_2026-08-18.md` · `U18_5B_PROMPT_FILLED_2026-08-18.txt` · `U17_ADMISSIBILITY_2026-08-18.md` · `U17_5b_FACTS_BLOCK_2026-08-18.txt` · `U16_ADMISSIBILITY_AND_PLAN_2026-08-16.md` · `U13_BLOOM_PROBE_2026-08-15.md` · `U13_ADMISSIBILITY_DRAFT_2026-08-15.md` · `BAN_C1-C4_REGISTER_BLOCKED_2026-08-15.md` · `U13_REVIEW_SHEET_2026-08-15.md` · `RULING_DRAFTS_teacher-lane_2026-08-15.md` |

## পাঠ ১৬ — the authored state, and the two things it hands forward

**96 items, digest `337e0461239e`** over the `questions` array alone, sorted by qid, header
excluded — the same quantity `ENVELOPE-SYNC` checks and the batch wrapper carries at
`item_count` 96.

| level | count | % | floor | margin |
|---|--:|--:|--:|--:|
| Remember | 26 | 27.1% | 20% (20) | **+6** |
| Understand | 27 | 28.1% | 25% (24) | **+3** |
| Apply | 28 | 29.2% | 25% (24) | **+4** |
| Analyze | 13 | 13.5% | 10% (10) | **+3** |
| Evaluate | 2 | 2.1% | 0% | +2 |
| Create | 0 | 0.0% | 0% | content fact, CD-135(d) |

Slots: S02 8 · S03 14 · S04 7 · S05 9 · S06 6 · S07 16 · S08 9 · S10 6 · S11 7 · S12 7 · S13 7.
Every one clears its CD-138(g) demand; **the eleven admitted slots owe 52 and the bank supplies
96.** Difficulty: easy 36.5% against a 30% floor · medium 47.9% · hard 15.6%.

**S01 AND S09 ARE EXCLUDED, AND IT IS THE THIRD CHAPTER THE SAME SENTENCE HAS DECIDED.** The
extraction reads *"কবিতা চারটি: পাঠ ১৩, ১৫, ১৮, ২০ — এগুলোই S01 (কবিতা মুখস্থ) ও S09 (মূলভাব)
প্রশ্নের উৎস।"* পাঠ ১৪ was not on the list and lost both; পাঠ ১৫ was and gained both; **পাঠ ১৬ is
গদ্য (ইতিহাস), is not on it, and loses both.** CD-138(e) forbids inferring admissibility from
content in both directions, and one sentence deciding three chapters two different ways is what
that rule looks like when it is working. **S14/S15 are not declared at all** — CD-147 makes them
paper-level categorically and CD-147(c) makes silence correct.

## What a later session must not re-derive from this chapter

- **THE ⚠ BLOCK ON পাঠ ১৬ IS THE HEAVIEST IN THE SOURCE AND ALL OF IT HELD ON THE FIRST READ.**
  **No item asks what শহিদ means, who counts as one, or invites a student to apply it** — the
  source requires questions about *ব্যক্তিদের ঘটনা ও অবদান* and bars the definitional form,
  because school policy restricts the word to one who gives their life in the path of Allah while
  the textbook uses it broadly. The word survives in the bank **only inside two proper names the
  book itself prints**: **শহিদ সাবের** (a person) and **'শহিদ বুদ্ধিজীবী দিবস'** (the day).
  Everywhere else the bank writes *প্রাণ দেন · প্রাণ হারান · হত্যা করা হয় · বুদ্ধিজীবী*.
  **C-03** (গান ও সুরকার) is unreachable — that paragraph is not in the extraction at all, so no
  anchor can land there. **C-18** (শহিদ মিনারে ফুল দেওয়া) appears in three rubrics only as a
  thing the marker must NOT reward. **C-05**: no picture of any person. **পাঠ ২২ carries the same
  শহিদ bar and two more of its own** — this chapter's handling is the precedent for it.
- **`যুক্তবর্ণটি` — THE DEFINITE SINGULAR — IS A CLAIM ABOUT THE WORD, AND TWO WORDS FALSIFIED
  IT.** Every S12 stem was first written *"পাঠের 'X' শব্দের যুক্তবর্ণটি ভেঙে দেখাও"*. Five of the
  seven stimulus words carry one conjunct. **`প্রতিষ্ঠাতা` carries প্র AND ষ্ঠ; `বিশ্ববিদ্যালয়`
  carries শ্ব AND দ্য** — so a student answering correctly on the other conjunct was unmarkable.
  **`COVERAGE` was quiet throughout and correctly so**: it checks that both declared halves of the
  composite task are claimed, and both were. **The gate reads the task declaration; nothing reads
  the word.** Every S12 stem now NAMES its conjunct. **This is `QB-CR-011`'s shape — a surface
  read instead of the thing underneath — in a place that pattern had not yet reached, and it is
  filed here rather than as a ledger row because it was caught before the artifact existed.**
- **A DRILL ITEM WHOSE STIMULUS DOES NOT SUPPORT ITS TASK PASSES EVERY GATE, AND IT HAPPENED IN
  TWO SLOTS.** One S11 item asked for nothing but a terminal দাঁড়ি; another required a
  **সেমিকোলন**, which is outside the C5 বিরামচিহ্ন set the slot drills. One S06 antonym item used
  **গভীর**, whose only use in this chapter is *গভীর রাতে* — অগভীর does not oppose that sense.
  **The first replacement was rejected on re-check for the identical fault**: **নতুন** occurs only
  as the adverbial *নতুন করে*. The stimulus is now **নিষ্ঠুর**, adjectival in the chapter's own
  gloss of পাষণ্ড. **A gate counts items; it cannot ask whether an item is worth asking.**
- **TWO ADMITTED-SET MEMBERS ARE UNAUTHORED, AND THE TWO REASONS ARE DIFFERENT IN KIND.**
  **অনুশীলনী ৫ (ক্রিয়ার রূপ) is unauthored by SELECTION** — ক্রিয়ার কাল is in BAN-S10's
  `admitted_set` and C5 selected পদ নির্ণয়, so COVERAGE would redden it as off-choice
  (CD-138(b)). **অনুশীলনী ৭ (ঘটনা সাজিয়ে অনুচ্ছেদ — বকের বাসার গল্প) is unauthored by
  EVIDENCE**: the source prints the exercise's NAME and not one sentence of the story, so **no
  three-token anchor exists and SOURCE-TRACE could bind nothing to it.** The second is not a
  content limit and must not be read as one — it is a limit on what the extraction carries, and
  opening the book is not an authorized path (the source's own preface: *"এই ফাইল থেকেই উপাদান
  নিতে হবে"*).
- **`-13` IS THE PUNCTUATION TAG AND পাঠ ১৬ CARRIED IT FROM THE FIRST ITEM.** Seven S11 items,
  `topic_tag` `TOP-BAN-C5-13`, `ref19_topic_id` `BAN-SENTENCE` (REF-19 has no punctuation slug —
  `PENDING-P-008`). Third chapter running where `QB-CR-014` costs nothing because it was known
  before authoring began.
- **`TOP-BAN-C5-14` / `BAN-BIOGRAPHY` IS THIS CHAPTER'S PRIMARY NUMBER**, minted 2026-08-14 for
  exactly this পাঠ. It is used here for the first time — **a number minted for a purpose is not in
  use until something carries it** (`QB-CR-014`(d)), and as of this bank, `-14` is.

## পাঠ ১৫ — the authored state, and the one thing it hands the Principal

**96 items, digest `d86c5e99bac3`** over the `questions` array alone, sorted by qid, header
excluded — the same quantity `ENVELOPE-SYNC` checks and the batch wrapper carries at
`item_count` 96.

| level | count | % | floor | margin |
|---|--:|--:|--:|--:|
| Remember | 26 | 27.1% | 20% (20) | **+6** |
| Understand | 28 | 29.2% | 25% (24) | **+4** |
| Apply | 27 | 28.1% | 25% (24) | **+3** |
| Analyze | 13 | 13.5% | 10% (10) | **+3** |
| Evaluate | 2 | 2.1% | 0% | +2 |
| Create | 0 | 0.0% | 0% | content fact, CD-135(d) |

Slots: S01 1 · S02 8 · S03 13 · S04 6 · S05 8 · S06 6 · S07 14 · S08 9 · S09 1 · S10 8 · S11 8 ·
S12 6 · S13 8. Every one clears its CD-138(g) demand; **the thirteen admitted slots owe 54 and the
bank supplies 96.**

**ONLY TWO SLOTS ARE INADMISSIBLE HERE — S14 AND S15 — AND THE REASON THE OTHER TWO CAME BACK IS
THE SAME SENTENCE THAT TOOK THEM AWAY AT পাঠ ১৪.** The extraction reads *"কবিতা চারটি: পাঠ ১৩, ১৫,
১৮, ২০ — এগুলোই S01 (কবিতা মুখস্থ) ও S09 (মূলভাব) প্রশ্নের উৎস।"* পাঠ ১৪ was not on the list and
lost both; **পাঠ ১৫ is on it and gains both.** CD-138(e) forbids inferring admissibility from
content **in both directions**, and this pair is the clean demonstration: one sentence, two
chapters, opposite verdicts, neither inferred.

## What a later session must not re-derive from this chapter

- **THE S01 SPAN IS AN OPEN QUESTION AND Q01 DOES NOT DEPEND ON THE ANSWER.** The extraction calls
  the span *"প্রথম ৮ পঙ্‌ক্তি"* and also delimits it by its endpoints. **Counted — not read — the
  delimited span runs to ten পঙ্‌ক্তি across six printed lines**, because the book prints two
  পঙ্‌ক্তি per line for four of the six. `SLOT_REGISTER` `BAN-S01` names the part *"প্রথম ৮ লাইন"*
  at 8 marks. **Q01 quotes the endpoints and states no number to any student**, so the item is
  correct on either reading and nothing needs re-authoring once the Principal rules. **The lesson
  is CD-145(e) applied one row over: a count inside a SOURCE is no more readable than a count
  inside a ruling.**
- **TWO ADMITTED-SET MEMBERS ARE UNAUTHORED BY SELECTION, NOT BY ABSENCE, AND THIS CHAPTER IS THE
  RICHEST SOURCE OF BOTH.** অনুশীলনী ৪ is **সমার্থক শব্দ** (`BAN-S06` set; C5 selected বিপরীত শব্দ)
  and অনুশীলনী ৮ is **ক্রিয়ার কাল** (`BAN-S10` set; C5 selected পদ নির্ণয়). Either would be an
  off-choice task and COVERAGE reddens it (CD-138(b)). **The extraction calls this chapter S10's
  *"সবচেয়ে নিরাপদ উৎস"* because two of the বৃত্তি forms sit here** — so if the C5 selection is ever
  revisited, this is the chapter that pays for it, and `header.gaps` says so.
- **`-13` IS THE PUNCTUATION TAG AND পাঠ ১৫ CARRIED IT FROM THE FIRST ITEM.** Eight S11 items,
  `topic_tag` `TOP-BAN-C5-13`, `ref19_topic_id` `BAN-SENTENCE` (REF-19 has no punctuation slug —
  `PENDING-P-008`). **This is `QB-CR-014` costing nothing because it was known before authoring
  began**, the same shape as `QB-CR-009` at পাঠ ১৪: a correction discharged by writing it right,
  not by editing live items.
- **E-AUTHOR-ENDORSE AND THE 'স্বর্গপানে' CAUTION ARE BOTH HELD, AND HOLDING THE SECOND ONE COST A
  DESIGN CHOICE.** The poet is named কাজী নজরুল ইসলাম with no epithet anywhere. **No item asks what
  'স্বর্গপানে' means** — the extraction warns its sense here is *"আকাশের দিকে", ধর্মীয় অর্থে নয়*,
  so the word appears once only, at S12, where the task is breaking স্ব into স + ব and the formed
  word is স্বাধীন. A শব্দার্থ item on it would have been admissible and was declined.

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
