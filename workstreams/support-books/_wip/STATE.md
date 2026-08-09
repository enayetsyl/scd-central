# support-books/_wip/STATE.md — Step 3 (support-books fold-in)

## Phase

**Five of six rulings applied. Q-1 (whitelist freeze) is BLOCKED on a missing file, so the
L53 merge is still withheld.** The book on disk remains unmerged and untouched.

## ⛔ Q-1 BLOCKED — `_inbox/Class 1 Bangla.pdf` does not exist

The ruling requires deriving conjuncts from NCTB pages 71–72 (পাঠ ৪৯), 74–76 (পাঠ ৫১) and
77–78 (পাঠ ৫২) of `_inbox/Class 1 Bangla.pdf`, with the page winning over SCHEMA §6 where they
disagree. **That PDF is not in `_inbox/`, and no PDF exists anywhere in the workspace.**

Nothing was derived. The whole point of the ruling is that the *page* is the authority — a
conjunct list produced from memory or by reasoning backwards from the candidate file would be
exactly the phantom content AGENTS.md §4 forbids, and it would silently defeat the check the
Principal asked for. **Drop the PDF into `_inbox/` and the derivation, freeze, re-validation and
L53 merge all complete in one pass.**

## Rulings applied 2026-08-09

| Q | Ruling | Outcome |
|---|---|---|
| Q-1 | derive from NCTB pages, then freeze | ⛔ **BLOCKED** — PDF absent |
| Q-2 | reconstruct D-020 + D-021 | ⚠️ **partial** — D-021 done; **D-020 has no source** |
| Q-3 | rule L017 by content | ✅ **v2 operative**, proven byte-identical |
| Q-4 | no action on L009/L024/L026 | ✅ provenance note logged (CR-003) |
| Q-5 | log MOTOR-note correction | ✅ logged (CR-002); note fixed at L002's next patch |
| Q-6 | annotate the validation report | ✅ annotated in place, body unedited |

### Q-2 — D-021 reconstructed, D-020 could not be

**D-021 is solid**: 9 in-book citations. পাঠ ২৩'s ঢ sentence *'ঢাল তলোয়ার ঝনঝনিয়ে বাজে।'*
(p.33) was flagged **S4, no C-code**, and resolved to the static *'ঢাল তলোয়ার দেয়ালে সাজানো।'*
It establishes the **weapon-as-object precedent**, applied at পাঠ ২৪ (ধনুক). Row written, marked
*reconstructed from in-book citations — Principal re-approved.*

**D-020 has zero citations** — searched the book JSON, its version log, all 55 patches, the
governance files and the references. Nothing. A row reconstructed from the one-line description
"mixed-classroom fiqh, open S4" would be invented, not reconstructed, so **the row records the
gap instead** and reserves the number so D-021 is not renumbered. ⚑ New question **Q-7**: is
there another export that carries D-020, or should it be re-ruled from scratch?

### Q-3 — L017 settled by content, not by date or version number

The book's `L017-b04` rhyme is **byte-identical to v2**:

```
ঝমঝমিয়ে বৃষ্টি পড়ে, / গাছের পাতা নড়েচড়ে। / গাছের তলায় ব্যাঙের ছাতা, / ব্যাঙ বসে তার ছায়ায় একা।
```

v3 carries a **different rhyme entirely** ("ছাতা মাথায় ঘরে ফিরি…"). So the book was built from
**v2**, which is also the newer file by date — the *version number* is what is wrong, not the
date. Only `source_note` differs between book and v2, added at merge. Forward-only from here.

## L53 — steps 7, 8, 9

**Step 7 (JSON):** `_wip/L053_step7_lesson_object.json`. The supplied patch v1 carried the same
empty codes as the book, so it would not have fixed anything. The **MOTOR sentinel** was applied,
verified at source: L002 carries `["MOTOR"]` and its note records the Principal ruling.

**Step 8 (validator, on the merged candidate `_wip/support-book_C1-BAN.CANDIDATE.json`):**

```
CHECK 3  — [PASS] codes non-empty on all lessons (MOTOR sentinel counts)
CHECK 10 — [PASS] every lesson has codes + action + nctb_pages
CHECK 4  — [RED]  L52/L052-b08: conjunct_not_whitelisted দ্ধ / ক্ত  (×5)
RESULT:  RED=5   GREY=4   PASS=12      VERDICT: FAIL
```

**L53's own two reds are fixed.** The five remaining reds are L52's and pre-date this work.

**Step 9 (merge): WITHHELD.** Red gates do not merge. The candidate is kept in `_wip/`;
the book on disk is untouched, with a pre-merge copy at `_wip/support-book_C1-BAN.PRE-L53.json`.

## ⚑ The whitelist finding — why the freeze ruling is load-bearing

The supplied `VALIDATION_REPORT_C1BAN_54path.txt` shows **CHECK 4 PASS**. That report cannot have
been produced against the master inventory: with `letter_inventory_C1-BAN.json`, পাঠ 52's
whitelist is `glyphs: null`, and null means *no conjunct is legal* (rule B-1), so L52 red-fails.

The candidate file enumerates conjuncts for **four** lessons:

| পাঠ | Enumerated glyphs | `needs_review` |
|---|---|---|
| 45 | প্ত ট্র ঙ্গ স্প ক্র | **false** — Principal-approved |
| 49 | ন্দ | true |
| 51 | দ্দ | true |
| 52 | স্ত ক্ত দ্ধ ম্ব ষ্ট | true |

Only **পাঠ 45** is approved, and it has a separate standalone amendment file marked
*"Principal-approved; apply-on-freeze (standalone, not a silent edit)"* with full NCTB derivation.
**পাঠ 49, 51 and 52 are candidate-only and still flagged for review** — and 52 is exactly the one
L53's merge is waiting behind. Freezing therefore is not mechanical: it approves three unreviewed
entries. **Not done without the ruling.**

## Questions — the original batch, with the Principal's numbering mapped

⚠️ **The Principal's reply renumbered the batch, and one item fell out.** Mapping:

| Principal's Q | My original Q | Status |
|---|---|---|
| Q-1 freeze | Q-1 | ruled — blocked on the missing PDF |
| Q-2 (D-019 vs D-021+) | **Q-3** | ruled |
| Q-3 (L017 v2/v3) | **Q-2** | ruled |
| Q-4 (L009/L024/L026) | Q-4 | ruled |
| Q-5 (MOTOR note) | Q-5 | ruled |
| Q-6 (validation report) | *(not in my batch)* | new item, ruled + applied |
| — | **Q-6 governance vs canon** | ⚠️ **STILL OPEN — not answered** |

**My Q-6 was displaced by the reply's own Q-6 and never ruled.** It is carried below, still on
its stated default. Original batch text follows unedited.


**[Principal] Q-1 — the whitelist freeze.** Approve enumerated conjuncts for পাঠ 49 (ন্দ),
51 (দ্দ) and 52 (স্ত ক্ত দ্ধ ম্ব ষ্ট), or freeze only the approved পাঠ 45 amendment? Only the
first unblocks the L53 merge. *Default meanwhile:* nothing frozen, book unmerged.

**[Principal] Q-2 — patch version conflict at L017.** `v2` is dated **2026-07-28**, `v3` is dated
**2026-07-18**. Version number and date disagree, so "newest wins" is ambiguous. Which is
operative? *Default:* neither applied. (All other multi-version patches are consistent —
highest version is also newest: L010, L012, L013, L023, L050, L051.)

**[Principal] Q-3 — decision-series gap.** `REGISTRY.md` said "at D-021+"; the imported
`DECISIONS.md` ends at **D-019**. Are D-020/D-021 missing from the export, or was the registry
figure approximate? *Default:* REGISTRY now reads "imported at D-019".

**[Principal] Q-4 — three lessons have no patch file.** L009, L024, L026 have no
`patch_C1-BAN_L0##` in the drop, though all three lessons exist in the book and have images.
Were they built before the patch convention, or are the patches missing? *Default:* treated as
already-merged; nothing reconstructed.

**[Principal] Q-5 — the MOTOR note overstates its reach.** The L002 note says the sentinel covers
2/5/7/18/53, but **L18 was built with real codes**, not the sentinel. Should the note stand as
historical record, or does L18 need review? *Default:* note stands, L18 untouched.

**[Principal] Q-6 — governance vs canon.** The imported `governance/` files restate rules that
are now canon (image doctrine, script guard, names). `LOCAL.md` records **canon wins on
overlap**. Confirm — or should the governance files be trimmed to process-only?

## Blockers

**Q-1 blocks the L53 merge, and Q-1 is blocked on a missing file** — `_inbox/Class 1 Bangla.pdf`.
Nothing else in Step 3 is blocked.

## New questions — batched per §6

**[Principal] Q-6 (carried, unanswered) — governance vs canon.** The imported `governance/`
files restate rules that are now canon (image doctrine, script guard, names). `LOCAL.md` records
**canon wins on overlap** as the working default. Confirm, or trim the governance files to
process-only? Displaced by the reply's renumbering; still open.

**[Principal] Q-7 — D-020 has no source.** Zero citations anywhere in the import. Is there
another export carrying it, or should it be re-ruled from scratch? *Default:* the D-020 row
records the gap and reserves the number; nothing invented.

## Next step

Principal drops `Class 1 Bangla.pdf` into `_inbox/` → freeze the approved whitelist entries into
`books/C1-BAN/letter_inventory_C1-BAN.json` as a recorded amendment (never a silent edit) →
re-run `audits/gates.py` → on green, complete step 9 and merge L53 → move the report into
`books/C1-BAN/reports/`.
