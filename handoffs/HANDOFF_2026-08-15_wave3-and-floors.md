# HANDOFF — পাঠ ১৩ wave 3, the Bloom floor, and four rulings owed
**Date:** 2026-08-15 · **Owner:** SCD (Principal) · **Chain:** unification → scd-central-migration → ocr-pipeline → math-ch6-onward → question-policy-unification → **this file**

**SUPERSEDES `HANDOFF_2026-08-15_question-policy-unification.md` ENTIRELY.** That file states repo
tip **`4bc66d7`** and CD rows running to **CD-132**. Both are wrong as of this writing — the truth is
**`dda7956`** and **CD-136**. It went stale in exactly the way its own §4 warns about, and a fresh
session given it would carry wrong facts on turn one. Cite this file; cite that one only for the
history of the chain that produced it.

**Every fact below was derived at source in the session that wrote it** — from `git log`, the ledgers,
the policy files and a fresh `gates.py` run. No number is carried from a chat.

**NEW: the chain now lives IN THE REPO, at `handoffs/`** (Principal ruling 2026-08-15) —
initiative-wide, beside `SESSION_LOG.md`, not a workstream lane. All five prior chain handoffs were
recovered from project knowledge and filed alongside as **read-only imports, cited never continued**
(the CD-034 / CD-043(b) pattern); **none is `NOT-IN-REPO`, because none is missing.** `REGISTRY.md`
carries a row for the location. **The chain lived outside the repo until today, and that is exactly
how the predecessor came to state a tip two commits and four CD rows stale with nothing able to
notice — CD-133's shape one level up.** See `handoffs/README.md`.

---

## 1. Repo state, read at source

| | |
|---|---|
| **Tip** | **`dda7956`**, pushed, `origin/main..HEAD` empty, **working tree clean** |
| **`canon/DECISIONS.md`** | defines through **CD-136** |
| **`workstreams/question-banks/DECISIONS.md`** | through **QB-D-013** |
| **`workstreams/question-banks/CORRECTIONS.md`** | through **QB-CR-011** |
| **`tools/CORRECTIONS.md`** | through **TOOLS-CR-004** |
| **`PENDING_PRINCIPAL.md`** | through **P-037** (P-033 CLOSED; P-034 · P-035 · P-036 · P-037 OPEN) |
| **Gate suite** | **22 gates** — 11 carry a `QUESTION_POLICY` §6 row, 14 a `QUESTION_BANK_POLICY` §5 row, 4 both, 1 from a decision row with no § of its own (CD-131) |
| **Suite status** | **CLEAN, 0 failures.** Selftests: §5 family PASS (25 seeded + 10 CD-131 exclusion + 5 CD-130(a) resolver + 1 baseline); §6 family PASS (**18 seeded + 9 negatives** + 6 CD-055 declaration + 1 baseline, across 12 gates) |
| Other gates | `canon_check` CLEAN (1 standing warn — 237 retired SB citations at/below their frozen baseline, correct history under UD-60(b)) · `ledger_check` CLEAN (4 declared cross-lane deferrals, unchanged) · `int_id_check` CLEAN (15 untyped sites reported, not judged) |

### This chain's commits — `git log --oneline 4bc66d7..dda7956`

```
dda7956  Corrections: TOOLS-CR-004 — .git/lock-debris has no cleanup step, and it grows with no agent
d2dcfc3  Queue and record: PENDING-P-036 second live case; PENDING-P-037 + interim rule; session log
56c4c6e  Corrections: QB-CR-011 slot-as-property (PATTERN candidate 2 of 3); TOOLS-CR-003 + AGENTS §9
20e63b2  C5 BAN paath 13 wave 3 — 36 to 88, six slots released, sized against CD-135's floors
cb248be  Governance: QB-D-013 filed late; CD-133-136; QUESTION_POLICY v1.2; BLOOM-BAND is floors-only
6ecbe3b  C5 BAN পাঠ ১৩ wave 2 — 24 to 36, unlocked by the teacher-gloss ruling
cb9f2f6  C5 BAN পাঠ ১৩ wave 1 — the first bank authored under QUESTION_POLICY v1.1
```

**`cb9f2f6` and `6ecbe3b` had never been pushed** — the remote sat at `4bc66d7`. They were released by
Principal ruling 2026-08-15, on the ground that they are the same lane and same file as wave 3, which
supersedes their content: holding two superseded waves out of history while pushing the wave that
replaced them serves nothing.

---

## 2. What this chain ruled, and why

### `QB-D-013` — the teacher-gloss ruling, **filed late**

Ruled 2026-08-14: a **teacher-supplied gloss is an acceptable key for a শব্দার্থ item**. Applied that
day to four items — **Q25 গন্ধ · Q26 কূল · Q27 গাঁ · Q28 ইচ্ছা** — whose keys are not in the
extraction, because অনুশীলনী ১ sets those four as tasks and the chapter glosses none of them. Effect:
`Remember` 5 → 10, and the pool 24 → 36.

**The second point is the filing.** From 2026-08-14 until this chain, the ruling existed **only as the
string `header.teacher_gloss_ruling` inside the bank it governs**. A ruling recorded only in the thing
it rules **cannot be cited, cannot be superseded, and dies with the file**. Filed workstream-local per
CD-121(d) because it ruled four items in one bank; the general rule went to canon separately as
CD-136.

### `CD-133` — the Unification Decision Register was **never filed**

`QUESTION_POLICY` §10 closed: *"The Unification Decision Register (60 rows) is the provenance record
and **is filed alongside**."* It is not filed anywhere. Repo-wide census: **`UD-60` ×15 · `UD-23` ×11 ·
`UD-11` ×2 · `UD-09` ×2 — four numbers out of sixty**, no file defining any row, `UD-01` zero hits, and
`find` for `*UNIFICATION*` / `*REGISTER*` / `*UD_*` returning nothing.

Recorded **NOT-IN-REPO** — asserted as filed, absent from disk, may survive outside the repo —
**distinct from LOST**, meaning known to have existed here and now unrecoverable. **Both terms are
minted in CD-133.** **CD-090(b) is cited for its PRINCIPLE and explicitly not its labels**: it mints
`UNATTESTED-INSIDE-RANGE` / `RECONSTRUCTED-UNKNOWN` for *numbers in a sequence*, and neither fits a
whole file. **Not reconstructed** — 56 of 60 rows are cited nowhere, and CD-090(c) already rules that
cited-by is evidence a number was taken and never evidence of what it said. **§10's authority claim is
unaffected**; the CD rows are the authority and nothing in force depended on the register.

### `CD-134` — a chapter's own *কোন প্রশ্নে কাজে লাগবে* line is **advisory**

**This is CD-122(b) applied, not new ground, and the row says so.** CD-122(b) had already ruled the
line cannot be *inverted into an obligation*; CD-134 settles the other face — **it does not forbid a
slot either**. A Pool may serve **any** spine slot the extracted content supports.

**Executable half:** where a slot is not served, the recorded reason **must be that the CONTENT does
not support it**, never that the chapter's own line did not name it. The two look identical in a
header and are not — content-absence is a fact about the book no later wave can change; line-absence
is unfalsifiable, because nobody can tell from it whether the material was looked for.

Released six of পাঠ ১৩'s eight gap slots. **S04 · S05 · S11 by CD-134 alone; S06 · S12 · S13 needed
CD-136 as well**, because their keys are language facts the chapter does not gloss. **No §9 row** —
§4 applied, not superseded.

### `CD-135` — the pool Bloom check is a **FLOOR**, not a band

CD-122(a)'s argument, carried to the axis it had not been applied to: **a pool cannot fail a ceiling**,
because the author declines the surplus and a compliant paper stays constructible however skewed the
pool is. Nothing in that argument was about difficulty.

**Ruled:** at **POOL** level the check is **REF-06 §3.6's lower bounds only**. No upper bound fails a
pool. **The band — both bounds — continues to apply at PAPER level**, alongside the domain ratio.
Where a level's floor is 0 (`Evaluate`, `Create`), nothing is required, but **a level the chapter
cannot supply is stated in the bank header as a content fact**, because a 0% level passing a 0% floor
is otherwise indistinguishable from a level nobody looked for. **CD-121(a)'s axis assignment is
untouched** — only its readability *as a band* is superseded.

**Executable:** `gates.py`'s `REF06_C3_5` loop — the `share > hi` FAIL branch removed, `share < lo`
unchanged; **per-level counts against floors REPORTed every run** on both the single-bank and sweep
paths. Three seeds: above-ceiling **CLEAN** (the old failing case **kept and inverted**, CD-122(a)'s
device, so the symmetric form cannot creep back), below-floor **FAIL** unchanged, exactly-at-floor
**CLEAN**.

**Recorded consequence:** a percentage floor implicitly caps every other level — Understand 25 + Apply
25 + Analyze 10 = 60, so **`Remember` can never exceed 40%** of a pool however large. **Removing the
ceiling does not make the pool unbounded; it moves the binding constraint to the floors.**

### `CD-136` — teacher-supplied language keys, and **why there is no gate**

Generalises QB-D-013 per CD-121(d). Where the **stimulus** resolves to the chapter extraction and the
**key is a general Bangla language fact** — সমার্থক · বিপরীত · যুক্তবর্ণ বিভাজন · এক কথায় প্রকাশ ·
ভাষারীতি / পদ নির্ণয় / ক্রিয়ার কাল — **a teacher-supplied key is acceptable**, declared in the item's
own `model_note` so provenance travels with the item and not only with the header.

**Boundary, load-bearing:** this admits **language facts about chapter material**. Not new content, not
new facts, not prompts with no chapter anchor. **S14 আবেদনপত্র and S15 রচনা stay OUT of chapter
banks** — they anchor to nothing and carry no key at all, so neither half of the rule is in play.

**NO GATE CHANGE, and the reason must survive.** `SOURCE-TRACE` never read keys — **both**
implementations (`g_source_trace`, `g_qb_source_trace`) resolve only `source_index[qid]` — so *"the key
need not resolve"* was **already true** and needed no amendment. A FAIL branch for an undeclared
teacher key was **proposed and refused**, wrong twice over: it **builds key-resolution the gate does
not have in order to enforce a LOOSENING**, and it would fire on legitimate items whose keys are the
student's own work. An undeclared teacher key is not machine-detectable without that capability, and
the capability costs more than the defect. **Enforcement is §6's human review gate — the Principal as
Subject Lead (REF-09 §9).**

`QUESTION_POLICY` **v1.1 → v1.2**, one bump over four sites (§4 · §6 · §9 ×2 · §10), superseded wording
quoted in place at each. `QUESTION_BANK_POLICY` §4 first bullet → **stimulus scope**,
supersede-with-archive per master §5.3.

---

## 3. পাঠ ১৩'s state, and the four rulings the next session executes

**88 items · commit `20e63b2` · suite CLEAN · NOT PROMOTED.** The Principal reviews all 88 as Subject
Lead before promotion. Slots **7 → 13**: S01 1 · S02 7 · S03 11 · S04 5 · S05 6 · S06 3 · S07 20 ·
S08 13 · S09 1 · S10 10 · S11 5 · S12 3 · S13 3.

**Fresh `BLOOM-BAND` report, verbatim:**

```
Remember 26/88=29.5% vs floor 20% · Understand 24/88=27.3% vs floor 25% ·
Apply 24/88=27.3% vs floor 25% · Analyze 12/88=13.6% vs floor 10% ·
Evaluate 2/88=2.3% vs floor 0% · Create 0/88=0.0% vs floor 0%
```

### The four rulings owed

1. **Re-tags: Q11 · Q13 · Q14 · Q72 → `Remember`.**
2. **Duplicated-image items KEPT.**
3. **Target 72 — retire 16, none of them `Understand`.**
4. **P-036 stands as ruled, in `min()` form; its absolute half is INERT until the paper table
   exists, and §5 records why that is blocked rather than merely pending.**

### Re-derived arithmetic behind 72 — confirmed, and 76 was rejected for a reason worth keeping

Verified at source: **all four named items are currently `Understand`, all four in S07.** Q11 *কে শহর
ছেড়ে গাঁয়ে যেতে চায়* · Q13 *কবির পাঠে মন বসে না কেন* · Q14 *কোথায় লুকিয়ে থেকে কার মতো ডাকতে চান* ·
Q72 *কাঁঠালচাঁপার গন্ধ কবির কী করে*.

Post-re-tag the composition is **R30 · U20 · A24 · An12 · E2 · C0**.

**At the current N=88 this FAILS** — `Understand` 20 against a floor of 22. The re-tags are not
free; they force the pool down.

**Each level's ceiling on N after the re-tags:** `Remember` 30 → N ≤ 150 · **`Understand` 20 → N ≤
80** · `Apply` 24 → N ≤ 96 · `Analyze` 12 → N ≤ 120. **`Understand` binds at 80.**

**72 requires retiring 16, and `Understand` cannot supply any of them.** Best split preserving
`Evaluate` — **retire `Remember` 10 · `Apply` 4 · `Analyze` 2**:

| level | count | floor at 72 | margin |
|---|---|---|---|
| Remember | 20 | 15 | **+5** |
| Understand | 20 | 18 | **+2** |
| Apply | 20 | 18 | **+2** |
| Analyze | 10 | 8 | **+2** |
| Evaluate | 2 | 0 | — |
| Create | 0 | 0 | — (content fact, §CD-135(d)) |

**Why 76 was rejected, and this is the part to carry forward.** At 76 the best achievable split
gives margins of **+1 on `Understand`, `Apply` and `Analyze` alike** — it absorbs **one** further
`Understand` → `Remember` re-tag. **72 absorbs two.** The margin exists precisely because the
Subject Lead pass has not happened and that pass is **where `Understand` items get read down** —
**four moved in this chain alone**, on a tag-down rule minted mid-chain. A margin of +1 against a
review that has historically moved four items is not a margin. **No divergence from the ruled
number: 72 is confirmed.**

**Two constraints on the retirement set.** **(a) None of the 16 may be an `Understand` item** —
that level has zero slack in every compliant split. **(b) Do not empty `Evaluate`.** The
margin-maximising split *ignoring* `Evaluate` retires both of its items; it passes, because the
floor is 0%, but it would then oblige the header to declare `Evaluate` a content fact under
CD-135(d) — recording as *"the chapter cannot supply this"* a level the chapter demonstrably did
supply. **A level emptied to buy margin elsewhere is not a content fact, and writing it as one
would put a false sentence in the header** — the exact class of defect CD-133 was raised to correct.

**Re-derive from a fresh `BLOOM-BAND` run before cutting.** If the composition has moved, the split
above is wrong and the table must be rebuilt, not adjusted.

### 4. `header.gaps` and the re-tag list must agree — FLAG

The bank's `header.gaps` last entry already carries a **review item raised by the wave-3 tagging rule
and deliberately left unexecuted**: Q13 is tagged `Understand`, but the poem answers it verbatim in
the next line — *"পাঠে আমার মন বসে না / কাঁঠালচাঁপার গন্ধে"* — so under the tag-down rule it reads
`Remember`. **Ruling 1 executes exactly that, and for three more items.** When the re-tags land, **that
gaps entry must be rewritten or removed**, or the bank will carry a note saying a change is pending
that has already been made. The note also states margin arithmetic computed at N=88; that arithmetic
is superseded by the table above.

---

## 5. The paper table — P-036's activation is **BLOCKED**, not merely pending

**Highest-value next item.** It is what activates P-036's absolute half, and until it exists that half
is inert by ruling.

**The distinction matters and is itself the ruling: this is BLOCKED, not pending.** A pending item
needs someone to sit down and do it. **This one has a hole in the middle of the derivation** — the
mapping it needs does not exist and may not be constructible. **P-036 stands as ruled, in `min()`
form. What the absolute half MEASURES is ruled by the session that does the derivation, with the
data in hand — not now, and not by this file.**

**What is derivable now, from `MarkLogic_BAN_Spine.md` C5:** per-slot **items per paper**, from slot
marks ÷ per-item marks — S01 1 · S02 5 · S03 5 · S04 5 · S05 5 · S06 5 · S07 4 · S08 3 · S09 1 ·
S10 5 · S11 5 · S12 5 · S13 5 (plus S14 · S15, which are paper-level per CD-136). Marks reconcile to
100. `MODEL_PAPERS_POLICY` v1.1 §2 fixes **1 model HY (100) + 1 model Annual (100) + 1 model CT (25 ·
35 min)** per class × subject, and MarkLogic §১ sets **three exams a year**.

### THE THREE UNKNOWNS — all three must be closed before the absolute half can measure anything

**UNKNOWN 1 — the missing mapping, and it is the sharp edge.** Slot demand is derivable; **slot →
Bloom is not.** Getting from *five S05 items per paper* to *how many `Analyze` items the pool must
hold* requires mapping slots to Bloom levels — **which `QB-CR-011` has just ruled you must not
infer.** The spine's own `BAN-S05` line is the reason: বহুনির্বাচনি is *a way of answering, not a
skill*. **So the honest form of P-036's absolute half may be per-SLOT rather than per-Bloom-level.**
That sidesteps QB-CR-011 entirely — and it is **a different ruling from the one P-036 currently
frames**, which is written in Bloom terms throughout. **Settle what is being measured before building
anything to measure it.**

**UNKNOWN 2 — `MODEL_PAPERS_POLICY` was not written for this question.** v1.1 fixes paper *shape*
(§2: 1 model HY + 1 model Annual + 1 model CT per class × subject) and **defers the mix to MarkLogic
§৩, which is the PAPER's axis**. A search for Bloom vocabulary across the file returns essentially
nothing. **Its fitness as the input to this computation is UNVERIFIED** — it may be the right file,
it may need a section it does not have, or the demand side may belong somewhere else entirely.

**UNKNOWN 3 — a chapter's pool supplies only its SHARE of a paper, and the share is unread.**
Converting paper demand into per-chapter demand needs the syllabus split — MarkLogic §৪, *প্রতি
বছরের সিলেবাস ভাগের পাতা* — **which has not been read for this purpose by anyone.** Without it,
"enough items to build the papers" has a numerator and no denominator.

**This is a multi-file derivation with an unresolved design question at its centre, not a two-file
read.** Scope it as such.

---

## 6. The probe, and what it settled

**`bloom_level` is a property of the item's COGNITIVE DEMAND, never of its slot.** MarkLogic §৩ assigns
domains to a **paper**; `QUESTION_POLICY` §3 row 10 maps domain ↔ Bloom. **Neither fixes a slot's
level.** The spine says so in its own words, at `BAN-S05`:

> **বহুনির্বাচনি হলো *উত্তর দেওয়ার একটা পদ্ধতি*, কোনো দক্ষতা নয়।**

A slot the spine explicitly calls **not a skill** cannot carry a cognitive level.

A four-item probe — two S05, one S12, one S13, each tagged on demand with its reasoning — is committed
at **`workstreams/question-banks/_wip/U13_BLOOM_PROBE_2026-08-15.md`**. **Two of six slots moved:**
S05 carries **both** `Remember` and `Understand`; S12 read as `Apply`. Cost of the error, measured
before authoring: **+31 items / pool 99** under slot-derived tagging versus **+11 / pool 79** under
demand-derived — **nearly 3×**, and it would very likely have ended in *"the chapter cannot support
it."*

**`QB-CR-011` — PATTERN CANDIDATE, 2 of 3 instances.** *A spine slot read as carrying a property it
does not carry.* **Instance 1 is `CR-007`** (c5-math, 2026-08-11), where the MATH spine's slots are
**পরীক্ষার প্রশ্ন-ধরন** and were written as **অধ্যায়-বিষয়**, shifting the whole list one cell. Different
lane, different property, same shape. **A third instance promotes it to a PATTERN and a gate
proposal.** No gate is proposed now — a gate cannot read cognitive demand, which is why §6's human
review row is where this is caught.

**Why it was hard to see, and this is the transferable part: the slot-derived tagging was RIGHT FOUR
TIMES OUT OF SIX.** It fails only where the slot's name is a **format** (বহুনির্বাচনি) or a
**procedure** (যুক্তবর্ণ ভেঙে), and happens to be right where the name describes a recall task. **A
heuristic that is usually right for the wrong reason is harder to catch than one that is always
wrong.**

**Tagging rule minted with it (Principal, 2026-08-15), now standing:** **under floors, over-tagging
UPWARD is the dangerous direction** — it inflates the level that must clear a floor and hides the
breach. **Where a level is genuinely uncertain, TAG DOWN.** Applied to all three S12 items, authored
`Remember` though the probe read `Apply`; any `Apply` reading is **upside, confirmed in review**.

---

## 7. Drafting cost, and what it implies for sizing

**~73 minutes** of agent wall-clock for the whole session. **Authoring the 52 items was six of them.**
Roughly: verification and mounting **22 min** · four CD rows + QB-D-013 **20 min** · policy v1.2, gate
change, seeds, P-036 **12 min** · probe and projections **9 min** · authoring, the REPETITION fix and
gate runs **6 min** · ledgers, queue, interim rule **6 min**.

**~40 minutes of judgement + ~10 of authoring per chapter.** The authoring is the cheap part and does
not size the programme. **The judgement does — and it shrinks with the number of rulings already
settled, not with the number of chapters done.** This chain settled four. A chapter that raises no new
ruling should cost far less than 73 minutes; a chapter that raises one should be expected to cost
about this much again.

**What the policy made awkward**, recorded for whoever revises it: CD-136's `model_note` requirement
lands on a field that exists on **two of six** question types (that is P-037, and it only stayed
invisible because all nine teacher-key items happened to be `short_answer`); **the floors interact
multiplicatively and nothing computes them** — choosing a target means solving a small simultaneous
system by hand, and a throwaway script was written three times; and **`COVERAGE` reads the
header-stated target, so the bank grades itself** — sound today per CD-122(b) since there is no
slot-mapping to read instead, but it means the number deciding compliance is the number the author
chose, and only Subject Lead review stands between that and circularity.

---

## 8. Open / parked — refreshed at source, not copied forward

**Question-banks and tooling**

- **P-034** — unit segment minted **both** `U09` and `U9` across three canon artifacts, two conventions,
  no rule. **OPEN, RAISED, deliberately NOT decided — no agent may act in either direction.** Needed
  before the first bank whose unit segment is single-digit.
- **P-035** — consumption-exclusion declaration on an **extraction header**. **OPEN, proposed only,
  nothing written.** Blocks nothing; becomes owed the moment CD-127(a) is exercised.
- **P-036** — absolute pool floors vs percentages. **OPEN.** Now carries a **second live case** with two
  measured findings: **(a)** an `Analyze` floor forbade **28 of 32** distinct chapter-sourced items on a
  chapter that supplies them; **(b)** **margin costs ~2 items of authoring per item of margin**, because
  the floor rises with the total — 79 → 88, nine items, bought only +2/+2/+3. **RULED in `min()` form; absolute half
  INERT until §5's paper table exists, and §5 records that as BLOCKED rather than pending.**
- **P-037** — CD-136's `model_note` is **unwritable on four of six question types** (`mcq`,
  `fill_blank`, `true_false`, `matching`); the schema is LOCKED and supersede-only (CD-013). **Carries
  an INTERIM AUTHORING RULE already IN FORCE**, recorded in `QUESTION_BANK_POLICY` §4: a
  teacher-supplied key is authored as `short_answer` or `descriptive`, and any other type is
  **STOP-AND-ASK, never a workaround**. Proposed upstream as an additive payload-root field.
- **P-033 — CLOSED** 2026-08-14 → CD-129 · CD-130 · CD-131 · CD-132.
- **UP-002** — no `pool` field on the question payload. Blocks Hub usage-lock and AS rotation.
- **UP-003** — `ref19_topic_id`'s pattern forbids a second hyphen, so `MATH-ADDSUB-REL` and
  `MATH-MULDIV-REL` are unrepresentable. **Blocks every C5 Math bank**; Bangla unaffected.
- **QB-CR-009** — U14 Drama `-09`. **RULED, execution owed** — U14 items still carry `-06` on disk and
  must be corrected before any U14 bank is promoted.
- **QB-CR-011** — PATTERN candidate at **2 of 3**.
- **TOOLS-CR-003 / TOOLS-CR-004** — see §9.
- **CR-001 … CR-004** span multiple declared lanes; **DEFERRED by CD-124**, renumbered per lane at
  close, printed every `ledger_check` run. A fifth cross-lane token is a trigger to revisit.

**Unchanged cross-workstream rows** — EnglishDrive fold-in · P00 fold-in · english-programme ·
islamic-studies (ARABIC-SLOT; Naskh fonts parked in `_unvendored/` per CD-126) · accounting (Check-5
423,533; +28,592) · scd-hub privacy flip **UNCONFIRMED** · **PAT renewals Aug 2027** · `pick_placements`
workstation session.

**Math lane: paused by Principal.** অধ্যায় ৬ sits `নির্মাণাধীন`; ch7–ch10 OCR drafts exist only in
gitignored `_inbox/` on one machine. **The two-account control-set proof has never been run** and is
owed before that work becomes canon.

**Four empty workstreams FAIL by design** (`_template`, `curriculum-foundations`, `p01-nctb-stability`,
`scholarship`) — a workstream with zero gates cannot declare anything final.

**Sign-off queue remains the system's bottleneck**, unchanged by any of this.

---

## 9. Session mechanics — carried forward, with one addition

Inputs via `_inbox/` (AGENTS §12: four classes, agent classifies, report-never-move, duplicates by
hash, §12.7 retention list at close). Agent batches questions per AGENTS §6. **Verbatim gate output
before any "final". Sync only on explicit approval** — CD-083(b): one held commit anywhere in
`origin/main..HEAD` holds the push, and the range check is pasted **per commit**. **One commit, one
class** (CD-083(d)). Never two agents on one workstream. Bengali for teacher-facing, English for
protocol.

**NEW, and it nearly cost this chain its canon.** `AGENTS.md` §9 gained two clauses:

- **`GIT_INDEX_FILE` is not a substitute for moving the lock aside (`TOOLS-CR-003`).** It redirects the
  index without updating `.git/index`, which is left describing the pre-commit tree — so **the next
  ordinary `git add` stages the exact inverse of the commit just made**. It happened: commit `cb248be`
  landed correctly, and the stale index would have staged `−228/+19` across the same five files,
  removing CD-133–136, returning `QUESTION_POLICY` to v1.1 and `BLOOM-BAND` to a band. **No gate would
  have caught it, because the pre-change rules are internally consistent** — the suite prints CLEAN on
  a repo that has silently un-ruled itself. **A gate suite proves the state it is run against is
  coherent; it cannot prove that state is the one you meant.** If used at all, **`git reset` must
  follow**.
- **`.git/lock-debris/` must be cleared periodically, and it is the Principal's job (`TOOLS-CR-004`).**
  Order matters: **`del /s /q .git\*.lock` → `git gc --prune=now` → `rmdir /s /q .git\lock-debris`**.
  `gc` itself fails on stale locks, and a *failed* `gc` leaves `gc.pid` and `packed-refs.lock` behind,
  so blockers surface **one per attempt** — five were cleared serially. The folder had **145 entries
  across three sessions, never cleared**, and its **largest group is `maintenance.lock`, written by
  git's own background maintenance** — so **it grows with no agent working**, and a session-end trigger
  would miss the majority. The sandbox cannot perform any of it.

---

## 10. Working style (binding, unchanged)

Precise and concise; **ONE recommendation with 1–2 line justification**; copy-paste-exact rulings;
files-over-memory; flag-don't-improvise; **verify at source before citing any decision**. When the
Principal asks for options, give pros and cons on every row and recommend on each — **he rules, the
advisor does not**. Reply in Bengali when he writes in Bengali. **Do not re-remind him about the
sign-off ledger.**

---

## 11. THE ADVISOR'S ERRORS — read this before advising

The predecessor recorded **seven**. This chain added **four**, every one caught by the Principal
reading at source. **Eleven instances.**

1. **REF-19 topic IDs** — recommended demoting `TOPIC_NUMBERS.md` to a mirror. REF-19 has never carried
   numbers (CD-043 said so already).
2. **The `REF-2` divergence** — claimed the file then numbered `REF-2` held cast/reference-sheet canon
   REF-20 lacks. Byte-identical; the cast canon is the storybook venture's (CD-006). *(The retired
   number is backticked, not cited bare: UD-60(b) retired it to REF-20, and `SB_CITATION_BASELINE.md`
   applies SOURCE_POLICY §7.16 by analogy — a gate that forbids naming the retired number would make
   the retirement unwriteable.)*
3. **The C3 band "conflict"** — presented REF-17 vs MarkLogic as irreconcilable. The band is
   *indicative* by its own words and defers to Tier 1.
4. **The fixture citation** — wrote `(CD-055, CD-064(f))` into canon §6 for a rule neither states,
   lifted from a docstring. The real rule: **controls may be drawn from the live pool; seeds may not.**
5. **`gates.py` state** — briefed it as `_template` zero-gate. It was 795 lines, 16 gates; building as
   instructed would have deleted ten and un-promoted three rulings.
6. **পাঠ ১২** — instructed a "division of labour" row that was **the position CD-050(b) overruled**.
7. **Readiness list** — said two promoted sources; there were 31. Three handoffs stale.
8. **A label pair attributed to CD-090(b) that it does not carry.** Ruling D was drafted citing
   CD-090(b) for a `NOT-IN-REPO` / `LOST` distinction; at source CD-090(b) mints
   `UNATTESTED-INSIDE-RANGE` / `RECONSTRUCTED-UNKNOWN`, for numbers in a sequence. **The principle
   transfers; the labels do not.** Caught before it landed — **CD-121(c)'s pattern, a phrase acquiring
   authority by citation rather than by ruling.**
9. **Ruling A written as fresh ground when CD-122(b) had already ruled it.** The draft cited only
   §3 row 15 and read as new. CD-122(b) names the same *কোন প্রশ্নে কাজে লাগবে* line explicitly. A row
   that re-derives a settled ruling invites a later session to find two authorities for one rule.
10. **A `SOURCE-TRACE` gate branch proposed to enforce a LOOSENING.** The draft would have failed an
    item with a non-resolving key and no `model_note` — building key-resolution the gate does not have,
    in order to permit something, and firing on legitimate items whose keys are the student's own work.
11. **Duplicated-image items read as near-duplicates from stems alone**, which the Principal's own
    reading reversed. Stems were compared without reading what each item actually demands of the
    student. It moved the target materially — **the advisor's estimate was low, and the Principal's
    reading raised it.**

**The lesson, verbatim from the predecessor and now eleven instances deep: do not cite a §-number you
have not read in this conversation, and re-read repo state rather than carrying it from a handoff.**
Say *"I have not read X"* — the Principal accepts that; a wrong citation costs a session.

**And one this chain adds:** errors 9 and 11 were both **the advisor reading a surface — a §-number, a
question stem — instead of the thing underneath it.** Error 11 is the same shape as `QB-CR-011`'s
slot-as-property, one level out. **When you find yourself judging from a label, stop and read the
thing.**

---

## 12. Immediate next actions

1. **Execute the four rulings** — re-tags Q11 · Q13 · Q14 · Q72 → `Remember`; duplicated-image items
   KEPT; **target 72, retiring 16 of which none may be `Understand` and which must not empty
   `Evaluate`**; P-036 in `min()` form with its absolute half inert. **Re-derive §3's table from a
   fresh `BLOOM-BAND` run first** — do not carry the numbers from this file.
2. **Reconcile `header.gaps`' Q13 note with the re-tag list** (§4). They must not disagree.
3. **Principal's Subject Lead pass** on all 88 items. Nothing is promoted until it closes.
4. **Scope the paper table** (§5). It is **BLOCKED, not pending** — three unknowns, and the first is
   a design question: settle whether P-036's absolute half is **per-slot** or per-Bloom-level, because
   per-Bloom needs a mapping QB-CR-011 forbids inferring. **P-036 stands as ruled; what its absolute
   half measures is ruled by the session holding the data.**
5. **Size wave 2 of the programme** against §7's figures: ~40 min judgement + ~10 min authoring per
   chapter, judgement shrinking with rulings settled.
6. **`git gc` housekeeping** per §9 when convenient.
