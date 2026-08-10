# canon/_wip/c5-bangla/STATE.md — Production step ① · C5 Bangla source extraction

A killed session must be resumable from this file alone (AGENTS.md §3).

## Phase

**Step ① of the production sequence (REGISTRY.md, CD-045): NCTB sources → per-chapter markdown.**
Book: **আমার বাংলা বই, পঞ্চম শ্রেণি**, NCTB, প্রথম মুদ্রণ সেপ্টেম্বর ২০২৫, শিক্ষাবর্ষ ২০২৬.
**23 পাঠ, printed pages ১–১৩২.**

- **পাঠ ১–৬ — BUILT, sign-off owed.** All six: `source_check.py`
  RANGE/SLOTS/PAGES/DEPTH **PASS**, SIGNOFF **PENDING**; `source_textcheck.py` **REFUSE**
  (see below — the correct outcome on this book, not a failure).
  Gate sweep: `evidence/GATE_SWEEP_2026-08-09.txt`.
- **পাঠ ৭–১১ — NOT STARTED.** Five files owed. See *Open / next* for the exact resume point.
- **পাঠ ১২ — NOT EXTRACTED by ruling.** See `EXCLUDED_paath_12.md`.
- **পাঠ ১৩–২৩ — already canon**, `canon/marklogic/C5_Bangla_Source_13-23.md` (CD-004,
  grandfathered range-file form). **Do not re-extract.**

### Progress

| পাঠ | নাম | ছাপা | pdf | অবস্থা |
|---|---|---|---|---|
| ১ | বৈচিত্র্যময় বাংলাদেশ | ১–৫ | 10–14 | ✅ BUILT · sign-off owed |
| ২ | তিতুমীর | ৬–১৮ | 15–27 | ✅ BUILT · sign-off owed |
| ৩ | দূরের পাল্লা | ১৯–২৩ | 28–32 | ✅ BUILT · sign-off owed |
| ৪ | পত্র লিখি | ২৪–২৭ | 33–36 | ✅ BUILT · sign-off owed |
| ৫ | ঠিক আছে | ২৮–৩১ | 37–40 | ✅ BUILT · sign-off owed |
| ৬ | সুখু আর দুখু | ৩২–৩৭ | 41–46 | ✅ BUILT · sign-off owed |
| ৭ | সাইক্লোন | ৩৮–৪১ | 47–50 | ⬜ |
| ৮ | রয়েল বেঙ্গল টাইগার | ৪২–৪৬ | 51–55 | ⬜ |
| ৯ | টুকটুক ও চিকু | ৪৭–৫২ | 56–61 | ⬜ |
| ১০ | রাখাল ছেলে | ৫৩–৫৬ | 62–65 | ⬜ |
| ১১ | কুটির শিল্প | ৫৭–৬২ | 66–71 | ⬜ |
| ১২ | শিষ্যের সাধনা | ৬৩–৬৮ | 72–77 | ⛔ excluded by ruling |

### Two shape findings the next session should not re-derive

**পাঠ ২ is a চিত্রকাহিনি** — nearly all its narrative sits in speech balloons beside the
pictures. Balloon text is transcribed **inside** the body, because the story is the balloons;
only text **painted into the illustration** (“বুম! বুম!!”, ছাপা ১৪) is pulled out into a
`## ছবির ভেতরের লেখা` section under §7.5, which trips the gate's raster rule and requires its
own full-check sign-off row. §7.5's stated reason for moving such text outside the body — that
the cross-channel check would report correct words as missing — does not apply on this book,
because there is no cross-channel check. The §7.5 sign-off obligation still does.

**পাঠ ৩ is a poem carrying pronunciation hasants** (ছিপ্‌খান্‌ · তিনজন্‌ · জাগ্‌ছে · পান্‌কৌটি ·
বক্‌বক্‌ · উন্মন্‌). It is S01 material — students write the first eight lines from memory — so
those marks are where marks are lost, and its first sign-off row is scoped to them specifically.
**A 150-dpi read was not enough:** `ঝকঝক` was first transcribed `ঝকঝাক` and only a 450-dpi crop
settled it. **Poem pages get a high-resolution crop before transcription, not after.**

## Scope — ruled 2026-08-09 (Principal), SOURCE_POLICY §7.6 / CD-050

**Remaining scope is পাঠ ১–১১** — printed ১–৬২ = pdf 10–71.

**There is no পাঠ ২৪.** §4 and §7.1 both say "পাঠ ১–১২ and ২৪+"; the সূচিপত্র runs ১–২৩ and
stops, পাঠ ২৩ starts printed ১৩০, and printed ১৩২ closes with **সমাপ্ত**. Superseded
forward-only by §7.6; neither older section is edited.

**পাঠ ১২ (শিষ্যের সাধনা) is NOT extracted.** `C5_Bangla_Source_13-23.md` records it as
deliberately excluded on Islamic-values grounds by school authority, and the Principal
confirmed that ruling reaches the extraction layer. A named exception to §3, not a loosening
of it — recorded at `EXCLUDED_paath_12.md` in this folder so the gap is visible.

**Edition.** This PDF's imprint reads প্রথম মুদ্রণ সেপ্টেম্বর ২০২৫; the older 13–23 file says
ডিসেম্বর ২০২৫ সংস্করণ, plausibly from the PDF's 20 Dec ModDate — recorded as a guess. Both
statements sit side by side in each new file's header; the older file is not edited (CD-004);
no PENDING-P row (Principal, 2026-08-09). No agent resolves this.

## Source PDF (provenance — not committed, SOURCE_POLICY §2.1)

`_inbox/Class 5 Bangla.pdf` · 142 pages · md5 `a119d576b43dac57bfc385f9721ffc86`
Adobe Illustrator 26.0 (Windows) → iLovePDF · PDF 1.6 · no AcroForm.

**Offset: printed folio + ৯ = PDF page.** Verified at 20 points across the whole book before
anything was extracted — seven folios read off the raster (pdf 14→৫, 27→১৮, 55→৪৬, 77→৬৮,
100→৯১, 138→১২৯, 140→১৩১) and thirteen পাঠ openings landing where the সূচিপত্র puts them.
Constant throughout. Never carried between sessions — re-verify.

**Source class: a third one, not §7.3's.** Born-digital publisher PDF **with the text
converted to outlines**. `pdftotext` over 142 pages yields **421 characters** — 312 on p142
(back imprint), 4 on p28, nothing anywhere else. Pages 1, 20, 70, 100 and 141 register **no
fonts at all**. Page 70's content stream carries 9,790 curve operators and 183 fills and
**not one `BT`/`Tj`**: every glyph is a drawn path.

**Consequence — the second channel does not exist here.** §7.3's decode-and-diff has nothing
to decode, so §7.4's one-sample depth cannot be earned on this book: its conditions are
conjunctive and read off an executed run, and Section B is trivially clean on an empty
stream. **Principal ruling 2026-08-09: full-eye check depth for the whole book**, the depth
§7.5 sets for artwork text, applied book-wide. `source_check.py`'s new DEPTH check enforces it.

## পাঠ boundaries — সূচিপত্র, each start confirmed on the printed page

| পাঠ | নাম | ছাপা | পাঠ | নাম | ছাপা |
|---|---|---|---|---|---|
| ১ | বৈচিত্র্যময় বাংলাদেশ | ১–৫ | ৭ | সাইক্লোন | ৩৮–৪১ |
| ২ | তিতুমীর | ৬–১৮ | ৮ | রয়েল বেঙ্গল টাইগার | ৪২–৪৬ |
| ৩ | দূরের পাল্লা | ১৯–২৩ | ৯ | টুকটুক ও চিকু | ৪৭–৫২ |
| ৪ | পত্র লিখি | ২৪–২৭ | ১০ | রাখাল ছেলে | ৫৩–৫৬ |
| ৫ | ঠিক আছে | ২৮–৩১ | ১১ | কুটির শিল্প | ৫৭–৬২ |
| ৬ | সুখু আর দুখু | ৩২–৩৭ | ১২ | শিষ্যের সাধনা | ৬৩–৬৮ |

End pages are derived from the next পাঠ's start and must be confirmed on the raster as each
file is built — only the start folios have been read so far.

## Gates

```
python3 tools/audits/source_check.py     canon/_wip/c5-bangla/C5_BAN_Source_NN.md
python3 tools/audits/source_textcheck.py canon/_wip/c5-bangla/C5_BAN_Source_NN.md \
        "_inbox/Class 5 Bangla.pdf" --pages <printed+9 range>
```

Verbatim runs for পাঠ ১ in `evidence/SOURCE_CHECK_2026-08-09.txt` and
`evidence/SOURCE_TEXTCHECK_2026-08-09.txt`.

**`source_textcheck.py` REFUSE is the expected outcome on every পাঠ of this book** and is not
a red gate. It means the channel is absent. A run that says AGREE on this book is a bug —
it did exactly that before this session's fix, comparing zero words against zero letters.

## Tool changes this session (both gates, seeded selftests re-run)

`source_check.py`
- reads `পাঠ` as well as `Unit` in the scope line and the body heading (a correct Bangla
  extraction was failing RANGE and PAGES on grammar alone);
- new **DEPTH** check: a file declaring `**যাচাই-চ্যানেল:** একক` must mark every sign-off row
  পূর্ণ and none নমুনা — **read off the গভীরতা column, not the whole row.** The first version
  scanned the row and went red on পাঠ ৪, whose first entry is “আবেদনপত্রের **নমুনা** — পুরোটা”,
  where নমুনা is the book's word for its sample letter. A gate that reddens correct files is a
  gate that stops being read;
- PAGES monotonicity scoped to the transcribed body — commentary and the slot cross-reference
  legitimately cite pages out of order; the range check stays global;
- selftest now draws fixtures from every extraction on disk and picks per seed, so the
  Bangla-grammar and single-channel seeds have something to bite on. **8 seeds RED** (the
  eighth added with the column fix: a single-channel file that simply omits the depth column
  must not pass by default), **all controls CLEAN.**

`source_textcheck.py`
- **REFUSE (exit 3)** when there is nothing to compare: stream under 40 letters/page, no
  extraction words, or a majority-Bengali transcription against a stream with no Bengali;
- Bengali-aware `letters()`, body anchor and word shape — `str.isalnum()` is False for any
  Bengali matra or hasant, which had left **three** words standing out of a five-page chapter;
- scaffolding is now "not in the book's script" rather than a stop-list, per §7.2(c);
- `*(...)*` page notes stripped from the compared body.
- **Regression-proved against all 20 English units, old script vs new: 0 of 20 differ** in
  Section A count, Section B count, verdict or exit code.

**No Bijoy/SutonnyMJ decoder was written.** The only Bangla text layer in this book is on
p142 (the back imprint), so a decoder would have nothing in scope to be proven against, and
an unproven decoder in a REQUIRED tool is exactly what CD-020 exists to prevent. The refusal
message names it as the missing capability so the next book that needs it says so out loud.

## Open / next

1. **Principal spot-checks পাঠ ১, ২, ৩ and signs** — 24 full-check rows in total (6 + 10 + 8).
   Depth is full, not sampled: there is no second channel. **No agent writes into the সই
   column** (SOURCE_POLICY §7.4, AGENTS.md §2) — an agent signature here would make the
   extraction single-channel *and* self-approved, which is the one combination this book's
   whole depth ruling exists to prevent.
2. **Resume at পাঠ ৭ (সাইক্লোন), printed ৩৮–৪১ = pdf 47–50.** Then ৮ (৪২–৪৬), ৯ (৪৭–৫২),
   ১০ (৫৩–৫৬), ১১ (৫৭–৬২). Rasters for pdf 10–71 are already rendered in
   `canon/_wip/c5-ban-raster/`. Build one file per পাঠ on the `C5_BAN_Source_01.md` pattern.
   **পাঠ ১০ (রাখাল ছেলে) is a poem — render it at 400+ dpi before transcribing, not after.**
   `BAN-S14` is **bound only in পাঠ ৪**; every other পাঠ marks it absent.
3. Rulings and tool changes from this session are recorded: **CD-050** (classification, scope
   correction, book-wide depth, edition flag) and **CD-051** (both gate changes).
   `SOURCE_POLICY` is at **v1.3** with new §7.6 and §7.7.

## Not synced

Nothing in this session has been committed or pushed. `git status` at hand-off: modified
`tools/audits/source_check.py`, `tools/audits/source_textcheck.py`, `canon/DECISIONS.md`,
`canon/sources/SOURCE_POLICY.md`, `canon/_wip/c5-english/STATE.md`; new
`canon/_wip/c5-bangla/`. Sync is on the Principal's explicit approval only.

## Housekeeping

- `canon/_wip/c5-ban-raster/` holds regenerable page rasters, ignored by `**/_wip/**/*.png`
  (CD-047). Evidence PNGs under `evidence/` are exempted by that rule's negation and are kept.
- `canon/_wip/c5-english/STATE.md` §Housekeeping says `_inbox/` holds `Class 1 Bangla.pdf`.
  It holds **`Class 5 Bangla.pdf`**. Noted, not corrected — that file is another workstream's
  state and this session did not touch it.
