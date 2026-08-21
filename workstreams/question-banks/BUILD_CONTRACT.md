# BUILD_CONTRACT.md

**What a question bank must satisfy mechanically, so a BUILD lane does not learn it by failing the
gate.** Every fact below is derived from `workstreams/question-banks/audits/gates.py` at source, with
the line or constant named. Nothing here is remembered.

Repo path: `workstreams/question-banks/BUILD_CONTRACT.md`
Written 2026-08-21 against `gates.py` as at `origin/main` = `0f177dc`.

> **This file is a cross-check, not the authority.** `gates.py` is the authority. If this file and
> the gate disagree, the gate wins and this file is wrong — file a row and fix it. Re-derive any
> constant you are about to rely on; the whole point of the contract is that BUILD stops carrying
> numbers it has not read.

---

## 0. Fetch list — step 0 of every BUILD

Nothing is accepted pasted. `B=https://raw.githubusercontent.com/enayetsyl/scd-central/<COMMIT>`

| What | Path | Why |
|---|---|---|
| chapter extraction | `canon/sources/c5/bangla/C5_BAN_Source_<nn>.md` | the only source (CD-192(a)) |
| slot register | `canon/marklogic/SLOT_REGISTER.json` | slots, tasks, marks, constraints |
| spine | `canon/marklogic/MarkLogic_BAN_Spine.md` | cross-read only |
| **topic chart** | `canon/topics/TOPIC_NUMBERS.md` | `topic_tag` must resolve here |
| **REF-19 slugs** | `canon/topics/LOCKED_REF-19_Vertical_Topic_Progression_Map_v1_10.md` | `ref19_topic_id` must resolve here |
| **the gate itself** | `workstreams/question-banks/audits/gates.py` | so BUILD can read the contract, not guess it |
| **schema exemplar** | the newest bank in `workstreams/question-banks/banks/` | the JSON shape is not documented anywhere else |

Report byte counts for all seven. A fetch that fails stops the lane.

---

## 1. `source_index` — the anchor contract

**This is the one that cost পাঠ ২২ a full rebuild (QB-CR-022): 114 of 117 items failed.**

`g_source_trace`, `gates.py:1180-1208`. Two conditions, both required, per item:

1. **≥ 3 tokens** after `qp_norm` (`MIN_ANCHOR_TOKENS = 3`, line 1193)
2. **present verbatim** in the extraction — `qp_norm(anchor) in qp_norm(whole extraction file)`

`qp_norm` (line ~470) is NFC + strip `‘’“”'"()[]।,;:?!—–-….*_#>|/·` + collapse whitespace. So
pipes, dashes and dotted lines vanish: a markdown table row normalises to its words, and a dotted
blank normalises to nothing.

**An anchor is a span of the book, not a citation label.** `ছাপা ১২৪` is two tokens and fails.
`অনুশীলনী ৩ · ছাপা ১২৮` is three tokens but appears nowhere as a run of text, and fails. Use the
printed sentence, glossary row, or exercise line the item actually draws on.

Anchors need not be unique — items drawing on one printed sentence honestly share one.

**Watch for:** spans that cross a page break. The extraction puts `### ছাপা ১২৭` and image captions
between the halves, so a sentence split across pages will not match as one string. Stop the anchor at
the page edge.

**Untraceable by construction:** exercise rows that are only dotted lines. Anchor those items to the
table's header plus its one worked row instead.

---

## 2. Near-duplicate — two gates, two thresholds

| Gate | Threshold | Scope | On breach |
|---|---|---|---|
| `g_zero_overlap` | `NEAR_DUP_JACCARD = 0.80` (line 358) | **every pair in the bank** | FAIL |
| PLAN | `PLAN_DUP_FAIL = 0.95` (line 2027) | within one slot | FAIL |
| PLAN | `PLAN_DUP_REPORT = 0.85` (line 2028) | within one slot | reported, passes |

**0.80 bank-wide is the binding one**, and it is stricter than PLAN. A per-word drill on a bare
frame — `পাঠে ব্যবহৃত 'X' শব্দের অর্থ লেখো।` — puts items at exactly 0.80 and fails, even though
PLAN would tolerate them to 0.95.

**Remedy, which also makes better questions: embed each item's own printed sentence in the stem.**
`"<printed sentence>" — এখানে 'X' শব্দের অর্থ কী?` rather than the bare frame.

**`g_zero_overlap` also fails two items with the same `question_type` and an identical answer
signature** (`qb_answer_signature`, line 477):

- `mcq` → the correct option's text
- `fill_blank` → `blanks[*].accepted[0]` joined
- `short_answer` → `answer_key.accepted[0]`
- `descriptive` → the `criterion` of rubric rows whose `role` is `content`
- `true_false` → empty (not discriminating)

**Consequence for small answer spaces.** পদ নির্ণয় has ~5 possible answers, so 10 single-word items
collide. Vary the *item*, not the key: ask two words in one item, giving a distinct answer. Do not
reorder `accepted[]` to dodge the check — that is gaming a gate.

---

## 3. `task_index` — which register field

`_declared_tasks`, `gates.py:1533-1539`. The field read depends on `task_mode`:

| `task_mode` | gate reads | `task_index` value |
|---|---|---|
| `simple` | `admitted_task` | that string |
| `alternative` | `admitted_set` / `selected` | **`selected`**; if `selected` is null (UNSELECTED), any member of `admitted_set` |
| `composite` | `parts[].part` | **a LIST of every part** |

**`admitted_task` is never read on alternative or composite rows.** It is descriptive prose and it
drifts: in BAN C5 it equals `selected` in only one of four alternative rows. Taking it — the obvious
reading — fails three of four alternative slots and S12.

Composite: every part or the item fails twice (missing parts, plus the undeclared claim).

---

## 4. What is NOT a failure

Do not exclude a slot, pad a pool, or re-tag items to satisfy any of these:

- **Per-slot demand.** Supplying under `items_per_paper` is **PRINTED, NOT FAILED** — CD-171(a)(iv),
  `gates.py:1791`. The demand is the paper's and the paper composes across chapters. *A BUILD prompt
  saying "the floor is real" is wrong and has caused at least one unnecessary slot exclusion.*
- **Pool size.** No minimum, no ceiling (CD-171(a)).
- **Bloom distribution.** Report only (CD-171(d)). The **tag** is required and must be one of
  `Remember · Understand · Apply · Analyze · Evaluate · Create` (`REF06_C3_5`, line 374); an unknown
  level FAILs. The distribution does not.
- **Hard difficulty share.** Paper-level, not pool.

**What IS a pool-level failure:** `EASY_FLOOR = 30.0` (line 406) — under 30% easy and no compliant
paper can be drawn, so the pool fails. `difficulty` must be `easy` / `medium` / `hard`.

---

## 5. Per-item shape

`KEY_FIELD_BY_TYPE` (line 414) — each type carries exactly one key field and **must not carry any
other**:

| `question_type` | required field |
|---|---|
| `mcq` | `options` (each distractor needs `why_wrong`; exactly one `is_correct`) |
| `true_false` | `tf_answer` |
| `fill_blank` | `blanks` |
| `matching` | `pairs` |
| `short_answer` | `answer_key` |
| `descriptive` | `rubric` |

**Rubric** (`g_key_rubric`, line 1267): ≥2 bands · ≥1 criterion with `role: islamic_alignment` ·
**every criterion needs a `band_descriptors` entry for every declared band**. A second
`islamic_alignment` row is reported, not failed. A `content` role row is what gives a descriptive
item an answer signature — without one it is exempt from the collision check.

**P-037** (line 2181): an item declaring a teacher-supplied key — detected by the literal string
`CD-136` in `answer_key.model_note` — is admitted only on `short_answer` and `descriptive`.

**Header** must carry `reason` · `topics` (every one supplied by some item) · `admissible_slots` ·
`slot_exclusions` (content reason, never blank, never a pipeline reason). Every slot S01–S13 is in
exactly one of those two. **S14/S15 in neither** — CD-147, and admitting one FAILs even with no item
in it.

**Script guard:** no Arabic script, no arrows or emoji in rendered text. Bengali numerals in stems.
`ৰ` U+09F0 and `ৱ` U+09F1 never appear in NCTB content — find one and stop.

---

## 6. Export chain — the three artifacts, and where the gate looks

`load_envelope_index`, `gates.py:1837-1884`. The paths are not configurable.

```
envelopes/<BANKSTEM>.envelopes.json     the array
envelopes/single/<qid>.json             what validate_import.py reads
envelopes/<BANKSTEM>.batch.json         contract v1.1, what the Hub reads
```

Scripts live in **two different directories** — this is not obvious and cost four turns:

```
tools/hub-export/build_question_envelopes.py            --json --curation-tag --source-file --unit-title --out
workstreams/question-banks/authoring/split_envelopes.py <envelopes.json>     writes single/
workstreams/question-banks/authoring/build_batch.py     <envelopes.json>     writes .batch.json
```

`--curation-tag` is required: `KEEP_AS_IS` / `NEEDS_REPLACEMENT` / `FLEXIBLE`. Use PowerShell, not
`cmd.exe`, for `--unit-title` — Bengali mangles in cmd's codepage.

**Run all three before gating.** ENVELOPE-SYNC on a partial export reports what it did not read
(TOOLS-CR-028) but the comparison is only worth having when all three exist.

---

## 7. Repo edit recipe — Windows

Read the file's own bytes before editing. **Line endings differ per file in this repo:**
`tools/CORRECTIONS.md` is CRLF, `workstreams/question-banks/CORRECTIONS.md` is LF. Writing back with
the wrong one turns a one-line insert into a whole-file diff.

```powershell
$b = [System.IO.File]::ReadAllBytes($absolutePath)     # ABSOLUTE — .NET ignores PowerShell's cwd
$t = [System.Text.Encoding]::UTF8.GetString($b)
([regex]::Matches($t,"`r`n")).Count                     # 0 = LF, else CRLF
```

Write with `New-Object System.Text.UTF8Encoding($false)` — PowerShell 5.1's `Out-File -Encoding UTF8`
adds a BOM.

**`tools/CORRECTIONS.md` has TWO tables.** The main one is ascending and ends mid-file; a second
block sits near EOF. An append lands the row in the wrong table. Read the row-id-to-line-number map
first.

**Sweep with `Get-ChildItem`, never `git ls-files | Select-String '\.md$'`.** Git quotes and
octal-escapes the two Bengali-named sources under `canon/sources/c5/bgs/` and `.../c5/science/`, so
an extension-anchored match silently drops both — TOOLS-CR-024's family, and it produced a wrong
evidence number inside TOOLS-CR-028's own draft.

**Print the number before and after every edit, and refuse to proceed if it did not move.**

---

## 8. Order of operations

1. BUILD authors; the authoring script's own pre-flight must pass before the bank is emitted.
2. **REVIEW reads the bank — before it is pushed.** QB-CR-020: twelve findings in a bank that passed
   all 24 gates, three of them factually false statements to a student. A green suite proves
   well-formedness, not truth.
3. BUILD applies the fixes.
4. Gates: `--bank` first, then `--repo --receipt`.
5. Commit order: **rows first, then code, then artifacts.** A row commit carries its
   `STATE.json` high-water update in the same commit or STATE-CHECK fires `BEHIND the ledger`.
6. Push on repo-wide `RUNALL_SENTINEL=CLEAN`.

Scarce numbers (CD · QB-CR · TOOLS-CR · PENDING-P) are re-taken at a freshly fetched origin
immediately before filing, by **both** methods — ledger read and token sweep with the file count
printed.

---

## 9. Known-open, so BUILD does not rediscover them

- **BAN-S08-STRAND** names বিদায় হজ as the C5 leg of an Islamic ladder. Most chapters do not carry
  it. Report which; never manufacture one.
- **BAN-S10 C5 is UNSELECTED** (CD-181) — all three of `ভাষারীতি পরিবর্তন` · `পদ নির্ণয়` ·
  `ক্রিয়ার কাল` are admitted. The row's `admitted_task` says `পদ নির্ণয়`, which no gate reads, and
  `self_checks.UNSELECTED_alternatives.cells` omits the cell because the register predates CD-181.
  The row is the fact.
- **BAN-S11 taught_set** at C5: দাঁড়ি · কমা · প্রশ্নচিহ্ন · বিস্ময়চিহ্ন · উদ্ধরণ চিহ্ন. It is a
  ceiling on marks, **not a floor on item count**. Sentences carrying `;` or `⸺` cannot be stimuli.
- **S12 রেফ and র-ফলা conjuncts** — whether they run at C5's S12 is undetermined. Open since পাঠ ১৮.
- **Sources 12–23 BAN and 01–20 ENG are PENDING**, not GREEN, and the cause is a missing
  `যাচাই-চ্যানেল` declaration rather than an owed sign-off (TOOLS-CR-026 cannot distinguish the two
  in its summary — read the file's own gate lines).
