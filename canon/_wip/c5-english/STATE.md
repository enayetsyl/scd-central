# canon/_wip/c5-english/STATE.md — Production step ① · C5 English source extraction

A killed session must be resumable from this file alone (AGENTS.md §3).

## Phase

**Step ① of the production sequence (REGISTRY.md, CD-045): NCTB sources → per-chapter markdown.**
Book: **English for Today, Class Five (Experimental edition)**, NCTB, first print September 2025,
prescribed from academic year 2026. **20 units, printed pages 1–111.**

*(Corrected at source: printed 106 is where Unit 20 **starts**, not where the book ends. Printed
111 carries "The End"; PDF 118 is the back cover. An earlier version of this file said 1–106.)*

- **Unit 1 — DONE.** Spot-checked and signed by the Principal, promoted to
  `canon/sources/c5/english/`, gate **GREEN** (CD-046).
- **Units 2–20 — BUILT, sign-off owed.** Held here. `source_check.py` is RANGE/SLOTS/PAGES
  **PASS** and SIGNOFF **PENDING** on all nineteen. Promotion = move each file plus its
  evidence to `canon/sources/c5/english/` on the Principal's "done".

## Source PDF (provenance — not committed, SOURCE_POLICY §2.1)

`_inbox/Class 5 English.pdf` · 118 pages · md5 `09a9b96fdce532c3dd7a48dd4fcaa2e7`
**Offset: printed folio + 6 = PDF page**, verified per unit on its own first and last folio,
never assumed and never carried between sessions.

**Source class: born-digital publisher PDF (SOURCE_POLICY §7.3)** — not a scan. It carries a
text layer and that layer is wrong three ways: Bengali mojibake, a +29-shifted Latin subset,
and a −29 display subset. Everything transcribed was read off the raster.

## Unit boundaries — all read off the printed folio, not the contents page

| Unit | Printed | Unit | Printed | Unit | Printed | Unit | Printed |
|---|---|---|---|---|---|---|---|
| 1 | 1–6 | 6 | 30–34 | 11 | 54–60 | 16 | 82–90 |
| 2 | 7–11 | 7 | 35–38 | 12 | 61–68 | 17 | 91–96 |
| 3 | 12–15 | 8 | 39–46 | 13 | 69–73 | 18 | 97–99 |
| 4 | 16–23 | 9 | 47–51 | 14 | 74–78 | 19 | 100–105 |
| 5 | 24–29 | 10 | 52–53 | 15 | 79–81 | 20 | 106–111 |

Two candidate lists disagreed at Units 6 and 19; the contents page was right both times and the
raster settled it. Unit 6 opens on a picture-led page, which is why a text-density scan missed it.

## Gates

```
python3 tools/audits/source_check.py     canon/_wip/c5-english/C5_ENG_Source_NN.md
python3 tools/audits/source_textcheck.py canon/_wip/c5-english/C5_ENG_Source_NN.md \
        "_inbox/Class 5 English.pdf" --pages <printed+6 range>
```

Full sweep 2026-08-09 in `evidence/GATE_SWEEP_2026-08-09.txt`: **20/20 PASS** on RANGE, SLOTS
and PAGES. `source_textcheck` AGREE on 7 of 20; the 13 others amount to **24 single words**,
every one proved present in the raw text layer by `evidence/TEXTCHECK_RESIDUAL_2026-08-09.txt`
— a decoder limitation, not a transcription error. **Section B — the check that would catch a
dropped or invented passage — is clean on every unit.**

Both gates carry seeded-error selftests, and `source_textcheck` was additionally proven against
the *signed* Unit 1 by seeding three real faults into it (dropped dialogue line · one mis-read
word · dropped table row): all three caught.

## Teacher content-check — returned 2026-08-12

**Three findings, all Unit 14 §3.1** (the *want to be…* example sentences, ছাপা ৭৭).
**All three closed as no-change**: checked against the raster, `C5_ENG_Source_14.md:113–115`
already carries the printed underline spans exactly — `want to be` / `wants to be` / `wants to be`,
stopping before the article, not running on to the profession.
Evidence gap the check exposed has been filled: **`evidence/C5_ENG_U14_p077.png` added**.

This is an **input to** the Principal's spot-check, not a substitute for it. Sign-off status below
is unchanged. *(C5 Bangla's teacher check came back clean — see `canon/_wip/c5-bangla/STATE.md`.)*

## Open / next

1. Principal spot-checks Units 2–20 and signs, then "done" → promote. **Depth per CD-048:
   one sampled passage per unit — the longest, named in each file's header — because Section B
   is clean and every word-level disagreement is provenance-proven. Units 4 and 11 additionally
   carry a full-check row for their artwork-borne text, which no machine can corroborate; the
   gate FAILs either of them without it.**
2. Then **C5 Bangla** — started 2026-08-09, state at `canon/_wip/c5-bangla/STATE.md`.
   ⚠️ The scope written here (**"পাঠ ১–১২ and ২৪+"**) was wrong at both ends and is superseded by
   **SOURCE_POLICY §7.6 / CD-050**: the book has **23 পাঠ**, there is no পাঠ ২৪, and পাঠ ১২ is
   excluded by standing school ruling. Real remaining scope: **পাঠ ১–১১**.

**Queue is clear.** PENDING-P-009/010/011 closed at CD-046, PENDING-P-012 at CD-048,
PENDING-P-013 at CD-049. Nothing OPEN blocks this workstream.

## Housekeeping

- `canon/_wip/c5-eng-raster/` holds 115 regenerable page rasters, now correctly ignored by the
  widened `**/_wip/**/*.png` rule (CD-047). Kept, not deleted: they are the working set for the
  Bangla remainder and cost nothing in the repo.
- `_inbox/` now holds `Class 5 English.pdf`, `Class 5 Bangla.pdf` (corrected 2026-08-09: this
  line previously read `Class 1 Bangla.pdf`, which is not what is staged; C1 is last in the order) and
  the two Naskh weights, which are **new weights, not duplicates**, and are a tools change with
  its own SMOKE run rather than an inbox tidy-up.
- `canon/_wip/c5-eng-raster/pdf-118.png` was reported truncated by one agent, which re-rendered
  it for its own evidence rather than touching the shared file. Regenerable; not evidence.
