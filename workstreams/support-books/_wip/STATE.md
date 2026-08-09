# support-books/_wip/STATE.md — Step 3 (support-books fold-in)

## Phase

**Step 3 import DONE. C1-BAN book NOT merged** — the L53 lesson object is prepared and its own
checks pass, but the gate is red on a **pre-existing, unrelated** L52 conjunct failure that only
the whitelist freeze resolves. Per governance README §3.2 step 8, a red does not merge.

## Done 2026-08-09

- Imported the 54-পাঠ book, 55 patches, 5 governance files, letter inventory, 2 whitelist
  candidates, skeleton + TG reconciliation + word map, the compliant image set, the validator
  report, and 3 validators.
- `audits/gates.py` written — runs the **seeded-error selftest first**, then the 10 checks.
  The selftest passes 16/16, so the instrument is proven before any book verdict is believed.
- L53 MOTOR fix prepared (steps 7–8 run; step 9 merge withheld).
- `LOCAL.md` filled, `REVIEW_QUEUE.md` and `CORRECTIONS.md` created, `REGISTRY.md` → **LIVE**.

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

## Questions — batched per AGENTS.md §6

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

**Q-1 blocks the L53 merge.** Nothing else in Step 3 is blocked.

## Next step

Principal answers Q-1 → freeze the approved whitelist entries into
`books/C1-BAN/letter_inventory_C1-BAN.json` as a recorded amendment (never a silent edit) →
re-run `audits/gates.py` → on green, complete step 9 and merge L53 → move the report into
`books/C1-BAN/reports/`.
