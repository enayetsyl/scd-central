# PENDING_PRINCIPAL.md — question queue for the Principal

Agents append rows (AGENTS.md §6); the Principal clears them from any device.

**Three statuses, because they gate different things (CD-042).**

| Status | Meaning | Blocks promotion/print? |
|---|---|---|
| **OPEN** | Principal-owed. A ruling is needed and only he can give it. | **YES** (AGENTS.md §6) |
| **FLAGGED** | File-owed. The ruling is made; it awaits verification against a named file that is not yet in the repo. The stated default stands and is tagged in the artifact. | **NO** |
| **RULED / CLOSED** | Settled. Row stays as history. | No |

A FLAGGED row is closed **only on verification at source** — never by elapsed time, never by a
second agent deciding the default looks right.

**Queue status as of 2026-08-10: 0 OPEN · 1 FLAGGED (PENDING-P-008) · the rest ruled.**
Ruled rows stay below as history; a reversal is a new row citing the old, never an edit.

| ID | Date | Workstream | Question (one line) | Default being used meanwhile | Needed by | Status |
|---|---|---|---|---|---|---|
| PENDING-P-041 | 2026-08-16 | canon/marklogic (ENG spine · ENG-S11) | **A POSSIBLE SPINE DEFECT, RAISED NOT REPAIRED: `ENG-S11`'s prose asserts a FORM question at C4 that no C4 row supports once C4 selects সংখ্যা.** The slot's C1 justification paragraph reads *ফরম পূরণ **প্রথম → চতুর্থ → পঞ্চম শ্রেণির** একটা সোজা সিঁড়ি (7.3) — এখানে নিজের নাম, শ্রেণি, বয়স লিখতে শিখলে **চতুর্থ ও পঞ্চম শ্রেণির ফরম** কঠিন লাগে না*. The C4 row's কারণ cell reads *cardinal ও ordinal সংখ্যা* against **Numeracy 7.2 (U06/U07)**, and the Principal ruled 2026-08-16 that **the কারণ column is the register's authoritative per-class task field**, so C4 selects **সংখ্যা**. Under that ruling **no C4 question carries a form at all**, and the ladder's middle rung is asserted by prose the class table does not support. Two readings: **(i)** the ladder is a **competency** claim — it cites 7.3, not 7.2, and it sits inside the C1 justification — so a teaching ladder is not a paper selection, nothing is wrong, and the sentence is merely easy to misread; or **(ii)** it is a **paper** claim, in which case either the C4 কারণ cell or the ladder sentence is wrong and the spine contradicts itself inside one slot. **A related observation, recorded so it is not rediscovered:** C5's ladder rung is unaffected either way — C5 is UNSELECTED, so a form at C5 is admitted, just not required. | **Reading (i) is applied and the spine is NOT amended.** C4 selects সংখ্যা per the ruling; C5 is UNSELECTED; the spine text is left exactly as written. Raised by the agent that hit the ambiguity while building the ENG register rows, per the standing rule that a source records and the consuming workstream curates — **an agent does not edit a MarkLogic spine to remove its own confusion.** The register rows carry the reading in `ENG-S11` C4's own `evidence_note`, which cites this row by number. | before the first C4 English model paper, and before any C1→C4→C5 form-ladder claim is relied on in teaching material | **OPEN — Principal's reading owed. Nothing is blocked:** the ENG C1–C5 register rows are written and CLEAN under reading (i). *(`PENDING-P-040` is unused: it was taken by a local commit that was discarded before any push and never reached origin. The number is left unfilled rather than reused, so nothing later resolves a citation to a row that was never filed.)* |
| PENDING-P-015 | 2026-08-10 | canon/sources (tooling) | **Two standing rules collide on a book too big for one session, and the collision reddened the whole repo's tool gate.** CD-051 widened `source_check.py --selftest`'s fixture pool to **every extraction on disk**, and its controls assert that an unmutated fixture is not red — which assumes every extraction on disk is finished. AGENTS.md §3 requires the opposite: work in progress lives in files under `_wip/` so a killed session is resumable. The first half-transcribed Math chapter therefore produced `[FALSE+ ] control · C5_MATH_Source_01.md` and `SELFTEST: FAIL`, from a file that was correctly reporting it was not done. | **Fixed in code the same session, not waived (AGENTS.md §5): a file may declare `**অবস্থা:** নির্মাণাধীন` and is then excluded from the pool as a control, and the selftest prints every file it skipped and why.** `run()` still checks such a file and still reports it red; the marker buys exclusion from being a control and nothing else. Removing the line is written into the resume instructions, so a finished file cannot stay outside the selftest by inertia. Recorded as CD-053(c). | before the next multi-session book (C5 SCI-BGS, or C4) | **CLOSED 2026-08-10 → CD-055. RULED: `নির্মাণাধীন` approved as convention.** An unfinished file declaring itself unfinished, excluded from selftest **controls** by name, is **AGENTS §3 and the fixture discipline reconciled rather than traded off** — both rules stay intact. The marker is not a waiver: the gate still runs on such a file and still reports it red, and removing the line is part of finishing the chapter. Recorded as **SOURCE_POLICY §7.9** (v1.4) so the next subject inherits it instead of rediscovering it. |
| PENDING-P-014 | 2026-08-10 | canon/sources (step ① · C5 গণিত) | **A math book cannot be transcribed at the resolution the math-critical rule demands inside one session, and the arithmetic should be ruled on rather than absorbed.** CR-001 sets a 400–700 dpi read before transcription, and the Principal extended it to **all** number-dense content in গণিত rather than on suspicion — which in a math textbook is effectively every page. Delivering a true 400 dpi page requires splitting it into **four** tiles (larger tiles are downscaled in transit, so the dpi rule is broken by the delivery, not by the render): **~4 reads × 181 printed pages ≈ 720+ reads**, against 190 pages of book. This session classified the book, re-derived the offset at 18 points, verified all ten chapter boundaries at both ends, fitted both gates for `অধ্যায়`, and transcribed printed page ১. **The book will take several sessions.** Is that accepted, or should the resolution rule be relaxed for math body text (e.g. ~300 dpi for prose and worked-example *prose*, with 400–700 dpi reserved for digits, operators, fractions and answer rows)? | **No relaxation. 400 dpi and full human check, book-wide** (SOURCE_POLICY §7.7 + CD-050(d)), with the session stopping at a stated resume point rather than lowering care — the Principal's own instruction, *"a partial book at full care beats the alternative"*. Relaxing later is cheap; a book read too coarsely has to be read again. | before অধ্যায় ২ is started | **CLOSED 2026-08-10 → CD-054. RULED: multi-session, no relaxation.** Resolution is not negotiable on this book — **every near-miss so far lived exactly where dpi was thinned** (the five Bangla cases, CR-001 among them), and in গণিত the exposure differs in kind: **a mis-read numeral becomes a wrong answer key, and this book has no second channel to catch it.** Cadence ruled: **one or more complete অধ্যায় per session at full care · checkpoint-commit per chapter · stated resume point in `STATE.md` · fresh session each sitting.** Ten chapters ≈ a week of sittings, accepted as the cost of a source with no second channel. Recorded as **SOURCE_POLICY §7.8** (v1.4). |
| PENDING-P-013 | 2026-08-09 | scholarship (step ②) | **Six content facts the C5 English extractions record that will bite a question author, none of them extraction-side.** (a) **Unit 20's only writing stimulus is six pictures of a deer** — C-05 bars living things, so the unit's composition prompt cannot go on a paper as printed. (b) **Units 14 and 17 lead with five-item MCQ exercises**, and `MarkLogic_ENG_Spine.md` states English carries no MCQ in any class. (c) **Unit 8 p43 prints "Quater past" / "Quater to"** twice, on a page that spells *quarter* correctly three times — and that page is exactly what `ENG-S11` draws on. (d) **Unit 15 is a poem with no prose passage**; may a poem serve as the `ENG-S03` passage? (e) **Unit 7's 2.1 is four-fifths lift-the-line**, against the spine's own-words requirement. (f) **Unit 17's only named character is Bidhan.** | None applied. SOURCE_POLICY §3 governs: the extraction **records**, the consuming workstream curates. Every item above is recorded in its unit file and nothing was altered. | before the first C5 English model paper | **CLOSED 2026-08-09 → CD-049. RULED, all six.** (a) deer stimulus: source as-is, step ② substitutes — **C-05 governs outputs, never the source record**; (b) MCQs **not mirrored** — MarkLogic retired MCQ from English; (c) source keeps **"Quater"**, output uses **"Quarter"** — a printed typo is never canon for output; (d) lift-the-line **not mirrored**, QuestionPolicy ratios govern; (e) **Bidhan** → CD-042 name rule, REF-2 C5 pool, structure kept; (f) **S03's passage IS the poem** for Units 10 and 15, recorded forward-only under `ENG-S03` in the spine. Written into `MODEL_PAPERS_POLICY.md` §8 (v1.1). No extraction edited. |
| PENDING-P-012 | 2026-08-09 | canon/sources (SOURCE_POLICY) | **Where does text that lives inside artwork go?** Unit 4's two maps carry ~75 place names as outlined artwork; Units 7, 11 and 18 repeat the pattern. The PDF text layer holds **not one character** of them, so `source_textcheck.py` can never corroborate them and putting them in the transcribed body fails the gate on ~60 words that are in fact correct. | **Artwork-borne labels go in the unit's names/labels section, explicitly flagged raster-only, outside the cross-checked body.** Applied in Units 4 and 11. | before C5 Bangla, whose maps and figures will repeat this | **CLOSED 2026-08-09 → CD-048. RULED: the default is confirmed.** Artwork-borne labels live in a names/labels section, **flagged raster-only, single-channel, Principal-verified, outside the cross-checked body**, and **any consumer citing them inherits the flag**. Recorded as **SOURCE_POLICY §7.5** (v1.2). Made executable the same day: `source_check.py` now FAILs an extraction that records artwork-borne text without a full-check sign-off row, with a seeded selftest for that path — the one kind of content no machine can corroborate is now the one kind a human is obliged to check in full. |
| PENDING-P-011 | 2026-08-09 | canon/sources (SOURCE_POLICY) | The staged book is **not the source class §2.1 describes.** §2.1/§2.3 assume a Principal scan with no text layer; `Class 5 English.pdf` is a **born-digital NCTB publisher PDF** (Adobe Illustrator, AcroForm) that *does* carry a text layer — and that text layer is wrong in two different ways (Bengali mojibake; English Caesar-shifted with commas dropped). Does SOURCE_POLICY record this second source class, and does raster-read remain mandatory for it? | **Raster-read, exactly as §2.3 requires.** The text layer was used only as a second channel to hunt for disagreements, never as authority. Evidence in this session's report. | before the remaining 19 units | **CLOSED 2026-08-09 → CD-046. RULED: yes — the born-digital publisher PDF is a named source class, recorded as SOURCE_POLICY §7.3.** Text layer never trusted; raster-read mandatory; the text layer admissible only as a disagreement-hunting channel that may never overrule the raster. This PDF is written into the policy as the proof, with its own byte-level evidence. The channel is now **executed**, not just permitted: `tools/audits/source_textcheck.py` (CD-047). |
| PENDING-P-010 | 2026-08-09 | canon/sources (SOURCE_POLICY) | Three extraction conventions the policy does not fix: **(a) granularity** — one file per unit (20 files) or chapter-range files like `C5_Bangla_Source_13-23.md`? **(b) subject token** — `C5_ENG_…` (matches the spine file names) or `C5_English_…` (matches the Bangla extraction's style)? **(c) scaffolding language** — Bengali headings around verbatim English, or English throughout? | **(a) one file per unit** — the Principal's own words this session were "per-chapter markdown files"; **(b) `ENG`** — matches `MarkLogic_ENG_Spine.md` and the `ENG-S03` slot ids; **(c) Bengali scaffolding, verbatim English body** — matches the sibling extraction and AGENTS §7. Unit 1 is built on all three. | before the remaining 19 units | **CLOSED 2026-08-09 → CD-046. RULED: the three defaults are confirmed as conventions v1.0** — one file per unit · `ENG` (spine) token · Bengali scaffolding around a verbatim body. Recorded in **SOURCE_POLICY §7.2** so the other nineteen files inherit them rather than each agent re-deciding. All 20 units are built on them. |
| PENDING-P-009 | 2026-08-09 | canon/sources (SOURCE_POLICY §4) | **The staged book is not the one §4 puts first.** §4 says *"`C5_Bangla_Source_13-23.md` already exists; **C5 Bangla 1–12 and 24+** complete that book first"* — the PDF staged in `_inbox/` is **C5 English**. Is English an intentional reordering, or was the Bangla book intended? | None. The agent did **not** silently re-order canon: Unit 1 was built as the Principal directed this session and is held in `canon/_wip/`, unpromoted. | before any unit is promoted to `canon/sources/` | **CLOSED 2026-08-09 → CD-046. RULED: intentional reorder.** C5 English completes first, then the C5 Bangla remainder, then the other C5 subjects, then C1–C4. Rationale on the row: English was the highest-risk extraction and is now proven, and step ② needs a non-Bangla subject. Recorded as **SOURCE_POLICY §7.1**, a forward-only supersede note — §4's own text is not edited. `Class 1 Bangla.pdf` stays in `_inbox/`, untouched, still last in the order. |
| PENDING-P-008 | 2026-08-09 | question-banks (+ lesson-plans, class-tests, scholarship) | The authoritative `TOP-<SUBJ>-C<n>-##` chart owed to **REF-07 §3.5** does not exist. **Sub-item:** REF-19 v1.10 carries **no Bangla punctuation slug**, so `TOP-BAN-C5-13` has a number and no slug of its own. | **`canon/topics/TOPIC_NUMBERS.md`** — seeded 2026-08-09 (CD-044) with the full attested C5 Bangla set plus the minted `-13`, every row citing its attestation. **A number not in that file is not used; it is queued** — enforced by the TOPIC-NUMBER gate. | before a second subject's banks are authored at scale | **FLAGGED — file-owed, non-blocking. C5 BANGLA CLOSED 2026-08-14.** **C5 Bangla is complete:** all eleven extracted পাঠ (১৩–২৩) resolve to a charted number. Two gaps found on audit were minted the same day under the CD-044 precedent — `TOP-BAN-C5-14` জীবনী (`BAN-BIOGRAPHY`, পাঠ ১৬) and `TOP-BAN-C5-15` ব্যবহারিক লিখন (`BAN-FUNCWRITE`, পাঠ ১৯ + ২৩) — and the contested U14 row was ruled **Drama `-09`** (QB-CR-009; REF-03 wins the authority chain and the source agrees, ধরন = নাটক). `-10` stays unassigned deliberately: its only description is a P03 usage note, not a P04 attestation, so fresh numbers were minted rather than adopting it. **The row stays FLAGGED because the close condition is all subjects, not one** — every other class × subject is still unwritten. **Original status:** **Close condition (revised, CD-044): the chart complete for all subjects**, and completion happens *in that file*, not by a ruling elsewhere. **Sub-item close condition:** a **REF-19 supersede authored at Project 00** adding a punctuation slug — REF-19 is LOCKED and read-only here (CD-043) and is **never edited**. Meanwhile a punctuation item keeps a valid existing `ref19_topic_id`, because the harness hard-validates that field against the REF-19 registry. |
| PENDING-P-007 | 2026-08-09 | question-banks | Which `TOP-` tag does a বিরামচিহ্ন item carry? `-11` is attested as মূল্যবোধ/মুক্ত-চিন্তা, and no number was attested for punctuation. | none applied — the wrong tag was not swapped for a guessed one | — | **CLOSED 2026-08-09 → CD-044. RULED: mint `TOP-BAN-C5-13` = বিরামচিহ্ন / যতিচিহ্ন.** Not folded into `-02`, because the C5 spine keeps `S03 বাক্য গঠন` and `S11 বিরামচিহ্ন` as separate mark slots and merging them would erase a distinction canon makes. Recorded in canon at **`canon/topics/TOPIC_NUMBERS.md`**, not only in the bank, and enforced by the new **TOPIC-NUMBER** gate. `QP-BAN-C5-U21-Q52` retagged; `ref19_topic_id` unchanged. QB-CR-008 closes with it. |
| PENDING-P-006 | 2026-08-09 | class-tests (+ question-banks) | The accepted Ch21 class test uses the name **আসিফ**, carried from the NCTB অনুশীলনী ৪, but আসিফ is not in REF-2's C5 pool and QuestionPolicy §৯ requires every student-facing name to come from it. Is the accepted CT superseded, or are names inside a quoted NCTB exercise carved out? | Bank items use **সাবিত** (REF-2 C5 male #3). The accepted CT is **not edited**. | before the next Ch21 CT is printed | **CLOSED 2026-08-09 → CD-042.** Principal ruling: the accepted Ch21 CT stays untouched and **আসিফ is grandfathered in that one historical paper only**. It is not a carve-out for quoted NCTB exercises: **every new item uses REF-2 C5-pool names**, and **সাবিত** in the bank is confirmed correct. Logged QB-CR-005 / class-tests CR-005. |
| PENDING-P-005 | 2026-08-09 | question-banks | Which `TOP-BAN-C5-##` tag do the S03 near-homophone sentence items for পাঠ ২১ carry? | `TOP-BAN-C5-02` | — | **CLOSED 2026-08-09 → CD-043. VERIFIED AT SOURCE, PASS on all four conditions.** REF-19 v1.10 imported and read: **zero `TOP-` strings, no topic id carries a numeric suffix**, 121 ids reconciling **exactly** with the vendored harness constant (0 diff either way). `D-PROJ04-011` attests verbatim *"`TOP-BAN-C5-02` বাক্য-রচনা (29)"*; `D-PROJ04-003` carries `-02` for U14 in *"30 × 5 topics `TOP-BAN-C5-06/01/02/11/12`"*. **`TOP-BAN-C5-02` on the 8 S03 items is CONFIRMED.** Evidence: `workstreams/question-banks/reports/P005_VERIFICATION_2026-08-09.txt`. QB-CR-004 and QB-CR-007 close with it. |
| PENDING-P-004 | 2026-08-09 | canon/language (all reader-facing output) | Does the CD-012 script guard apply to markdown canon and reader files, or only to strings bound for a renderer? Field-typed tiers have no meaning in a .md file, and canon already carries legend glyphs deliberately. | — | — | **RULED 2026-08-09 → CD-018** (guard governs strings entering a mechanical render path; extends to new paths on vendoring; human-read markdown out of scope; each path proves its glyph set in its own SMOKE.md). |
| PENDING-P-003 | 2026-08-09 | islamic-studies (+ any Arabic subject) | CD-012 makes Arabic script RED in any string, but islamic-studies and the Arabic subject will need ayat, hadith and du'a. Does tier 1 carve out Arabic-bearing subjects? | — | — | **RULED 2026-08-09 → CD-014** (tier 1 stands for all current workstreams; ground restated as renderer capability; lifts per render path on proven shaping + verbatim-sourced আলিম-reviewed text; `ARABIC-SLOT` placeholder meanwhile). |
| PENDING-P-002 | 2026-08-09 | canon/language + hub-export + support-books | Script-guard sources disagreed (CD-011 cross-check): Hub harness has none, SB validator check 8 has a narrower one than the old canon summary. Which is canon? | — | — | **RULED 2026-08-09 → CD-012** (SB validator's verified scope, 3 tiers; old summary corrected on 3 of 4 items). Harness gap logged upstream as UP-001 / CD-013. |
| PENDING-P-001 | 2026-08-09 | canon (all curation consumers) | REF-1 v1.2 declares Class 1 Bangla/English scope — how is C2–C5 / other-subject curation governed? | — | — | **RULED 2026-08-09 → CD-015** (whole-school scope, extends one class per year; class list read from SCHOOL_FACTS.md; overrides REF-1 §1.2, which is LOCKED and not edited). |

## ⚑ PENDING-P-016 — `math_arith_check.py` silently drops a long-division block that prints no minus signs

**Raised:** 2026-08-10 · **Workstream:** canon/_wip/c5-math · **Needed by:** before ছাপা ৩৯ is transcribed
**Status:** ✅ **CLOSED 2026-08-10 by CD-072** — both parts built and seeded; `SELFTEST: PASS`.
Evidence: `canon/_wip/c5-math/evidence/GATE_SWEEP_CD072_2026-08-10.txt`.
**Sibling check resolved CLEAN:** ছাপা ৮ **does** print `−` (400 dpi crop) — `C5_MATH_Source_01.md`
is faithful and owes no correction. The book uses **both** conventions in different chapters, which
is why the parser now reads both rather than picking one.

**What was found.** `parse_divisions` identifies a subtraction row by a leading `−`/`-`. **C5 গণিত
prints its long divisions with no minus signs at all** — just aligned digits under rules. When the
subtraction rows carry no sign, `subs` comes back empty, the block fails the guard
`if None not in (...) and subs:`, and **it is appended to nothing: neither verified nor reported**.

**Measured, not suspected.** The same ৬৯০৫ ÷ ৪ block, run through `parse_divisions`:

```
no minus  -> blocks found: 0
with minus-> blocks found: 1
```

**Why this is more serious than an uncovered shape.** CD-059 exists so unparsed shapes are *named* in
the census rather than vanishing. A `☐`-bearing block REFUSEs and is listed — visible. **This one is
absent.** The census cannot report what the parser never returned, so the file looks fully covered
while two complete divisions went unchecked. **Silence is the failure mode, not the gap.**

**Scope right now:** ছাপা ৩৮'s two blocks (৫৩৯৪০ ÷ ৪ and ৬৯০৫ ÷ ৪). Both were **verified by hand at
400 dpi** — ১৩৪৮৫ ভাগশেষ ০ and ১৭২৬ ভাগশেষ ১, every subtraction row matched — and the extraction says
so next to them. **অধ্যায় ৩ has more divisions ahead (ছাপা ৩৯–৪৮), and every one will be dropped the
same way until this is fixed.**

**Not fixed by the agent, and the reason is the transcription rule, not caution.** Adding `−` to make
the parser bite would be **printing something the book does not print** (SOURCE_POLICY §3). The
extraction must stay faithful; the parser must learn the book's layout.

**Proposed fix, one recommendation:** treat a rule-delimited numeric row inside a division block as a
subtraction row **whether or not it carries a sign**, and — separately and more importantly — **make an
unparseable division block REFUSE-and-report instead of disappearing**, so the census can never again
be silent about one. Seeds both ways: a signless block must verify; a signless block with a mutated
subtraction row must go RED; an undetectable block must appear as REFUSE, never absent.

**Note on the sibling file (AGENTS.md §6).** `C5_MATH_Source_01.md` writes its divisions **with** `−`.
Whether the book prints those signs on ছাপা ৮ was not re-checked this sitting — **if it does not, that
extraction has an unfaithful character in it** and the same crop check is owed there. Raised, not
assumed.

## ⚑ PENDING-P-017 — the ladder (মই-ভাগ) is a shape no gate models and no census names

**Raised:** 2026-08-10 · **Workstream:** canon/_wip/c5-math · **Needed by:** before অধ্যায় ৩ closes
**Status:** ✅ **CLOSED 2026-08-10 by CD-073** — census-visibility built and seeded (6 cases, PASS);
ladder *verification* deliberately deferred to its own ruling. Evidence:
`canon/_wip/c5-math/evidence/GATE_LADDER_CD073_2026-08-10.txt`.

**What.** ছাপা ৩৯ introduces the **ladder division** used for লসাগু — `২ ) ১২, ১৮` over a rule, then
`৩ ) ৬, ৯`, then `২, ৩`. It is not a long division: the divisor line carries **several** dividends
separated by commas, so `DIV_LINE` does not match and `parse_divisions` returns nothing.

**That part is correct** — a ladder is genuinely a different shape and must not be simulated as a
long division. **The problem is what happens next: nothing.** The block claims no shape, so
CD-072's REFUSE-never-vanish rule never engages, and the census line names `prose carrying numbers`
and `÷ long division` but **has no name for a ladder at all**. Measured: `parse_divisions` on the
ছাপা ৩৯ ladder returns **0 blocks**, and the census gains **0 entries**.

**Why it matters here specifically.** A ladder is dense with exactly the content this book gets
wrong — multi-column numerals in a fixed layout, the §7.14.2c hazard class. অধ্যায় ৩ has **two on
ছাপা ৩৯ alone** and near-certainly more on ৪০–৪৮, and চ্যানেল-অমিল row 5 already showed the OCR
reordering a multi-column row while reading every digit correctly.

**Both ছাপা ৩৯ ladders are hand-verified at 400 dpi and arithmetically sound:**
`২ ) ১২, ১৮ → ৬, ৯ → ২, ৩` with `২ × ৩ × ২ × ৩ = ৩৬` = লসাগু(১২, ১৮) ✓, and
`২ ) ১২, ১৪, ১৮ → ৬, ৭, ৯ → ২, ৭, ৩` with `২ × ৩ × ২ × ৭ × ৩` = ২৫২ = লসাগু(১২, ১৪, ১৮) ✓
(৭ is carried down undivided per the book's own printed step (২)).

**Proposed, one recommendation — smallest useful first: make the shape VISIBLE before making it
verified.** Teach the census to name a fenced block whose first line matches
`<prime> ) <n>, <n>[, <n>…]` as **`ladder (মই-ভাগ)`, REFUSE**, so it can never be silently absent.
That is §7.17(a) applied to a new shape and is a small change. **Verifying** a ladder — each row
divides by the stated prime, indivisible entries carry down unchanged, and the product of the left
column equals the লসাগু — is a **separate, larger ruling** and should not be bundled with it.

**Not built.** A second tooling detour inside a chapter the Principal asked to close would repeat
what already cost a sitting; and the arithmetic here is hand-verified, so nothing is unchecked —
only unnamed.

## ⚑ PENDING-P-018 — the coloured-grid figure is a shape whose *count* is the answer, and nothing checks it

> **✅ BUILT & CLOSED 2026-08-11 → CD-076.** Sitting 1, one commit, all four tasks together. Selftests PASS; evidence `canon/_wip/c5-math/evidence/GATE_SITTING1_2026-08-11.txt`.

**Raised:** 2026-08-11 · **Workstream:** canon/_wip/c5-math · **Needed by:** before অধ্যায় ৫ closes
**Status:** OPEN — propose-don't-build

**What.** অধ্যায় ৫ teaches decimals with **১০ × ১০ শতাংশ-ছক**: a 100-cell grid with some cells
coloured, and the pupil writes the shaded part as a fraction and a decimal. ছাপা ৬৩ alone carries
**three** of them (৪৮, ৬০, ৪৯ cells) and the chapter runs 28 pages.

**Why it is not just another figure.** In every previous chapter a figure was context — a photo, a
ribbon, a Venn. **Here the figure IS the number.** "৪৮ cells shaded" is the value ০.৪৮, and a
question authored from this page rests entirely on that count being right. It is CR-002's failure
class (counting, not reading) at 100 cells per figure, and `math_arith_check.py` has nothing to say
about it — there is no printed arithmetic to check.

**What was done on ছাপা ৬৩, so nothing is unverified today.** Two independent channels, agreeing:
**(a)** each grid enlarged at 400 dpi and counted by eye, row by row; **(b)** an **ad-hoc pixel
sampler** measuring colour saturation at the centre of each cell of a 10×10 lattice. Both returned
**৪৮ · ৬০ · ৪৯**.

**The sampler is NOT a gate and is not claimed as one (CD-020).** Run once, no seeds, not in
`tools/`, no SMOKE. **The crop is the authority; the sampler was a second pair of eyes.**

**Proposed, smallest useful first:** promote the lattice sampler to a real gate —
`tools/audits/grid_count_check.py` — that takes a page raster and a declared count, samples the
lattice, and goes **RED on disagreement**. Seeds both ways: a correct declared count CLEAN; a count
off by one RED; a grid whose lattice cannot be located REFUSE-and-report (never silent, §7.17(a)).

**Not built** — the অধ্যায় ৩ lesson: no gate construction mid-chapter. The counts stay
double-channel by hand until this has its own sitting.

## ⚑ PENDING-P-019 — `math_arith_check.py` cannot read a decimal, in the decimals chapter

> **✅ BUILT & CLOSED 2026-08-11 → CD-074.** Sitting 1, one commit, all four tasks together. Selftests PASS; evidence `canon/_wip/c5-math/evidence/GATE_SITTING1_2026-08-11.txt`.

**Raised:** 2026-08-11 · **Workstream:** canon/_wip/c5-math · **Needed by:** before অধ্যায় ৫ closes
**Status:** OPEN — propose-don't-build. **Run halted at ছাপা ৭০ to report this.**

**What.** The evaluator's `EXPR_OK` character class does not include the decimal point, so **any
line containing a decimal number yields no evaluable segment**. Measured, not surmised:

```
EXPR_OK accepts "০.৬"?  -> False
parse_chains("৬/১০ = ০.৬")        -> chains found: 0
parse_chains("০.৫ + ০.৫ = ১.০")   -> chains found: 0
parse_chains("০.৩ + ০.৪ = ০.৯")   -> chains found: 0     <-- a WRONG sum, unseen
```

**Why it matters here specifically.** In অধ্যায় ১–৪ the arith gate was the second channel that
caught *my* transcription errors — a mis-cropped digit broke an equality and went RED. It did
exactly that on অধ্যায় ৪'s ছাপা ৫৯. **In অধ্যায় ৫ that net is absent for the chapter's own
subject.** Every decimal sum, difference and equivalence the book prints is machine-unchecked;
the six chains verified so far are all *fraction* lines that happen to sit beside the decimals.
**The chapter is single-channel in the strongest sense: for decimals, the crop is the only check.**

**Not a false-RED risk — the current behaviour is safe.** Because `EXPR_OK` rejects the point, a
decimal line is *refused*, never mis-evaluated. Nothing is silently wrong today.

**But there is a landmine worth recording.** `_num("০.৬")` returns **6** — it strips the point.
No live path reaches it (chains are guarded by `EXPR_OK`; blocks and divisions use `cells()`,
which also rejects `.`), **but any future code path that passes a decimal to `_num` would read
০.৬ as 6 and could go RED on a correct transcription, or CLEAN on a wrong one.** Whoever builds
the decimal evaluator must fix `_num` in the same commit, not after.

**Proposed:** extend the evaluator to Bengali decimals using **`Fraction`, exactly as CD-064 did
for `÷`** — never float, so `০.১ + ০.২ = ০.৩` is exact and not 0.30000000000000004. Seeds both
ways: a correct decimal chain CLEAN; a mutated decimal digit RED; a **shifted decimal point** RED
(the chapter's signature failure); and `_num` on a decimal asserted to raise or return None rather
than silently drop the point.

**Not built** — the অধ্যায় ৩ lesson. **Pairs naturally with PENDING-P-018:** both want the same
dedicated gate sitting after অধ্যায় ৫'s pages are read, so both can be seeded against the whole
chapter's shapes rather than one page's.

**Nothing is unverified today.** Every decimal on ছাপা ৬৩–৬৯ was crop-read under the full
three-clause convention, and every printed computation was hand-checked and recorded next to it.

---

## ⚑ PENDING-P-020 — the book prints deliberately WRONG arithmetic, marked `✗`, and no gate models that shape

> **✅ BUILT & CLOSED 2026-08-11 → CD-075.** Sitting 1, one commit, all four tasks together. Selftests PASS; evidence `canon/_wip/c5-math/evidence/GATE_SITTING1_2026-08-11.txt`.

**Status: OPEN. Logged, hand-verified, not built** — the অধ্যায় ৩ lesson, and the standing
instruction that a new gate-shape found mid-chapter is logged and nothing more.

**The shape, measured.** ছাপা ৭৩ prints four worked items. Three of them show **two blocks
side by side**: a left block marked with a red `✗` whose arithmetic is *wrong on purpose*, and
a right block marked `✓` that is correct. The three ✗ blocks are:

| ছাপা (হুবহু) | সঠিক মান | কেন ছাপা হয়েছে |
|---|---|---|
| `৪ − ২.৩১ = ২.৩৩` | ১.৬৯ | উপরের রাশি ডান-প্রান্তে সাজানো, বিন্দু মেলানো হয়নি |
| `৩.৭৫ − ০.৫ = ৩.৭০` | ৩.২৫ | `০.৫`-এর `৫` শতাংশের স্তম্ভে বসেছে |
| `৭.৫৮ − ৬.৮৭ = ৭১` | ০.৭১ | ফলাফলে বিন্দু ও এককের `০` দুটোই বসানো হয়নি |

**Why this is a gate-shape and not just a page.** §7.11's table-hold exists for a line that is
*wrong in the book by accident* (অধ্যায় ৪, ছাপা ৫৯). This is different in kind: the book is
**correct to print these**, and the `✗` is load-bearing pedagogy. Two consequences:

1. **The mark is part of the datum.** A ✗ block quoted without its ✗ inverts the book's teaching.
   Chapter 2 already met this once, for comparisons, and answered it with the `সত্য`/`মিথ্যা`
   marking convention that `math_arith_check.py` reads. **The same idea now has to reach worked
   blocks**, not only comparisons.
2. **This directly constrains PENDING-P-019.** The moment a decimal evaluator exists, these three
   blocks become the first thing it reads, and it will go **RED on a correct transcription** unless
   it understands `✗`. So P-019 cannot ship a bare evaluator.

**Binding note for the build, to sit alongside the `_num` clause in P-019:** the decimal
evaluator and `✗`/`✓`-awareness must land **in the same commit**. Seeds both ways — a `✗`-marked
block whose arithmetic is wrong is **CLEAN** (the book said so); a `✗`-marked block whose
arithmetic is *right* is **RED** (a mis-transcription, the exact mirror of the `মিথ্যা` seed);
a `✓`-marked block that is wrong is **RED**. **A decimal evaluator that has never been shown to
stay quiet on a ✗ block is worse than no evaluator**, because its first three findings in this
chapter would all be false.

**Protection taken today, coverage deferred.** All three ✗ blocks are in **table-hold (§7.11)** in
`C5_MATH_Source_05.md`, so no future gate can reach them by accident; and they are recorded in
that file's `## ⛔ উৎস-সীমা` as ⛔-৪ with the never-quote-without-the-✗ condition. **Nothing was
built mid-chapter.**

**Hand-verified.** All seven marks counted twice (crop, and the OCR draft's four `\sqrt` +
three `\times`/`X` — the counts agree), and all four correct results checked by hand column by
column: ৭.০০ · ১.৬৯ · ৩.২৫ · ০.৭১.

### Amendment, 2026-08-11 — a **second sub-shape**, found on ছাপা ৮৬

**Scope widened by the agent; no new ruling sought.** This is the same doctrine and the same
gate sitting, so it is folded into P-020 rather than opened as P-021.

ছাপা ৮৬'s অনুশীলন ৬ prints **three more deliberately-wrong long divisions — with no `✗` at
all.** The only signal is the instruction: *নিচের হিসাবগুলোতে কী ভুল আছে ব্যাখ্যা করি এবং
তা ঠিক করি।*

| ছাপা (হুবহু) | সঠিক | ভুলের ধরন |
|---|---|---|
| `৪.৬৫ ÷ ১৫ = ৩১` | ০.৩১ | point absent |
| `২১.৩২ ÷ ৫.২ = ৪১` | ৪.১ | point absent |
| `৩ ÷ ০.১২৫ = ০.০২৪` | ২৪ | point three places wrong — **1000× too small** |

**Why this matters for the build.** P-020's original seed spec keyed on the `✗` mark. That spec
would leave these three **RED on a faithful transcription**, because there is no mark to key on.
So the evaluator needs **two** signals, not one:

1. **marked** — a `✓`/`✗` beside a worked block (ছাপা ৭৩);
2. **declared** — a block sitting under an instruction that says *find the error* (ছাপা ৮৬).

**Binding, alongside the `_num` clause and the `✗`-awareness clause — all in one commit:** the
evaluator must treat a block as *expected-wrong* when **either** signal is present, and seeds must
cover both. Add: a declared-wrong block that is **arithmetically right** is **RED** (a
mis-transcription — the mirror seed), exactly as for the `✗` case.

**Interim handling taken, same as before:** all three panels are in **table-hold (§7.11)** and
recorded as **⛔-৮** in `C5_MATH_Source_05.md` with a never-quote-without-the-instruction
condition. **Nothing built mid-chapter.** All three true values hand-checked with `Fraction`:
০.৩১ · ৪.১ · ২৪.


---

## ⚑ PENDING-P-021 — `source_check.py`'s SLOTS test checks that a slot is *mentioned*, not that it is *correctly identified* — and two closed chapters are wrong because of it

> **✅ BUILT & CLOSED 2026-08-11 → CD-077.** Sitting 2, three steps in order: gate hardened → অধ্যায় ৩ and ৪ corrected as dated append-only blocks → tri-sweep ৩·৪·৫ all SLOTS GREEN. Evidence `canon/_wip/c5-math/evidence/GATE_SITTING2_2026-08-11.txt`.

**Status: OPEN. Found at অধ্যায় ৫'s close, by writing the slot table against the spine
instead of copying the previous chapter's. Ch5 fixed before closing; ch3 and ch4 NOT
touched — they are closed and already reported, so correcting them is the Principal's call.**

**The measurement.** `canon/marklogic/MarkLogic_MATH_Spine.md` defines eleven slots, and they
are **exam question-types, not chapter topics**:

| slot | spine name |
|---|---|
| MATH-S01 | বহুনির্বাচনি প্রশ্ন |
| MATH-S02 | শূন্যস্থান পূরণ ও চিহ্ন বসানো |
| MATH-S03 | সংক্ষিপ্ত উত্তরের প্রশ্ন |
| MATH-S04 | চার প্রক্রিয়ার সমস্যা |
| MATH-S05 | লসাগু ও গসাগু |
| MATH-S06 | সাধারণ ও দশমিক ভগ্নাংশ |
| MATH-S07 | শতকরা |
| MATH-S08 | গড় |
| MATH-S09 | পরিমাপ |
| MATH-S10 | জ্যামিতি |
| MATH-S11 | উপাত্ত |

`C5_MATH_Source_03.md` and `C5_MATH_Source_04.md` both name them as **chapter topics**
(`S04 = সাধারণ ভগ্নাংশ`, `S05 = দশমিক`, `S09 = জ্যামিতি`…). From S05 onward the whole list is
**shifted by one**, and S01–S04's names are **invented**. Both chapters closed **SLOTS PASS**.

**Why the gate passed them.** The SLOTS check tests only that each of the eleven IDs appears
somewhere in the file. It does not compare the row's description against the spine. So a table
in which **every single row is mislabelled** is green.

**Why it matters, concretely.** The mapping is what step ④ reads to decide *which chapter
sources which exam slot*. Under the wrong table, অধ্যায় ৪ looks like the source for "সাধারণ
ভগ্নাংশ (S04)"; under the spine it is a source for **চার প্রক্রিয়ার সমস্যা (S04)** and for
**সাধারণ ও দশমিক ভগ্নাংশ (S06)** — different slots, different mark weights. And the corrected
অধ্যায় ৫ table shows something the wrong shape hid entirely: **the chapter is a direct source
for five slots at once** (S01 · S02 · S03 · S04 · S06), because the book itself prints MCQs,
fill-in-the-blanks, short answers and word problems inside the chapter.

**Two questions for the Principal.**

1. **Correct ch3 and ch4?** They are closed, gate-green, and reported. Re-opening them touches
   the CD-067 atomic-close record. The transcriptions themselves are untouched — the error is
   confined to the slot table at the end of each file. Recommend: correct both, as a single
   dated amendment block in each file rather than a silent edit, so the record shows what was
   believed at close and what replaced it.
2. **Tighten the gate?** Proposed smallest-useful scope: SLOTS additionally requires each row to
   carry the spine's own name for that slot, compared literally against
   `MarkLogic_MATH_Spine.md`'s `### \`MATH-Sxx\` — <name>` headings. Seeds both ways — a table
   with a renamed slot goes **RED**; a correct table stays CLEAN; a slot missing entirely stays
   RED as it does today. This is cheap and it is the check that would have caught this at
   অধ্যায় ৩'s close instead of অধ্যায় ৫'s.

**Not built.** Logged and handed over, per the standing rule for a new gate-shape.

### ✅ RULED — Principal, 2026-08-11. Status: **RULED, build scoped, not yet built.**

**Q1 — correct অধ্যায় ৩ and ৪: YES**, as **dated correction-blocks**. Both SLOTS tables are
re-derived from `MarkLogic_MATH_Spine.md`; each chapter gets a CR/supersede row stating the
error (**chapter-topic vs question-type, propagated by table-copying**), the corrected mapping,
and the date. **Append-only and visible — never a silent edit.** **Do NOT re-extract:** only
SLOTS was wrong; the transcriptions stand.

**Q2 — harden the SLOTS gate: YES.** The gate must verify each cited slot ID **against the
spine's own label**, not merely that an ID is present. The Principal's framing, recorded because
it names the class: *presence-not-correctness is the **CD-070 substring-luck failure at the
semantic level***. Seed both ways — correct mapping **PASS**, shifted/invented mapping **FAIL**.
**This gate would have caught ৩/৪ at close; it is the same class of fix as P-018/019/020.**

**Counter ruling — stays at 2.** অধ্যায় ৫'s close does **not** reach 3. The chapter is
mechanically GREEN, but **the same close proved অধ্যায় ৩/৪'s SLOTS-green was weaker than
claimed**, so "three consecutive GREEN" is not yet satisfied. **The counter reaches 3 only after
৩ and ৪ are corrected and the hardened SLOTS gate sweeps all three GREEN.** That sitting is what
*makes* the third GREEN real — it is not optional cleanup.

**Ordered tooling debt — two sittings** (see `canon/_wip/c5-math/STATE.md` for the executable
scope):

- **Sitting 1** — P-018 + P-019 + P-020, **one commit**.
- **Sitting 2** — P-021: harden SLOTS → correct ৩/৪ as dated CR blocks → re-sweep ৩/৪/৫.
  **Counter reaches 3 on that sweep.**

**Sync held** pending the Principal's go after both sittings are scoped.

---

## ⚑ PENDING-P-022 — `C5_MATH_Source_03.md` cites its OCR draft by the gitignored `_inbox/` filename, not the committed evidence path

**Status: OPEN.** Found at অধ্যায় ৬'s opening, while classifying and staging the ch6 draft
under §7.14.3a. **অধ্যায় ৩ was NOT touched** — it is closed, and correcting it mid-extraction is
the detour CD-067 forbids (Principal ruling, 2026-08-12).

**The measurement.** `canon/_wip/c5-math/C5_MATH_Source_03.md` records its draft as:

```
**খসড়া:** `C5_MATH_OCRDRAFT_ch3.md` · surya-ocr · ১৫০ dpi রাস্টার · PDF ৩৮–৫৫।
```

That is the **bare `_inbox/` filename**. `_inbox/` is gitignored (`.gitignore`, §2.1), so the
citation names a file **no other device can see** — which is precisely the unauditable
corroboration claim **§7.14.3a** exists to prevent.

**What is NOT wrong.** The evidence itself is intact: `canon/_wip/c5-math/evidence/OCRDRAFT_ch3_2026-08-10.md`
exists and is committed. **This is a citation string only**, not a missing artefact. অধ্যায় ৪ and ৫
cite correctly (`evidence/OCRDRAFT_ch4_2026-08-11.md`, `evidence/OCRDRAFT_ch5_2026-08-11.md`),
so the defect is confined to the first chapter run under the pipeline — the draft was staged before
§7.14.3a was written into the file's own citation line.

**Disposition (Principal, 2026-08-12): fix as a citation-string correction at the next gate
sitting, not mid-chapter.** Not a re-extraction, not a re-open of the chapter's content, and not
a CR row against the transcription — nothing about অধ্যায় ৩'s reading is in question.

**Worth a gate, at that sitting rather than now:** `source_check.py` could assert that any
`**খসড়া:**` citation resolves to a path under `evidence/`, since a gitignored citation is
machine-detectable and this one survived a chapter close. **Log-not-build applies — no tooling
detour during an active extraction (the অধ্যায় ৩ lesson, CD-078(c)).**

---

## ⚑ PENDING-P-023 — a source file can declare `যাচাই-চ্যানেল: দুই` and silently switch off CD-070's DEPTH enforcement

**Status: OPEN.** Found at অধ্যায় ৬'s opening, 2026-08-12, **by comparing the new file's gate
output against অধ্যায় ৩·৪·৫ as controls** — not by the gate, which said nothing.

**The measurement.** `source_check.py` reads the header's `**যাচাই-চ্যানেল:**` line to decide
whether a source is single- or dual-channel. `C5_MATH_Source_06.md` was scaffolded with
`দুই`, on the reasoning that the OCR draft *is* a second channel. The gate then reported:

```
channel : dual
[PASS   ] DEPTH    dual-channel source — §7.4 sampling depth governs, nothing to enforce here
```

**`OCR-corroborated` rows were therefore unenforced — CD-070's entire check was off, and the
file passed DEPTH while it was off.** The controls disagree unambiguously: অধ্যায় ৩, ৪ and ৫
all declare `একক` and all get `single-channel source; N row(s) 'পূর্ণ', M row(s)
'OCR-corroborated' with numeral-crop evidence…`.

**The canon is not ambiguous either.** §7.14.1: the draft has *"exactly the standing a text
layer has under §7.3"* — a disagreement-hunting input, never an authority. A §7.7 book with no
text layer stays **single-channel for §7.4's purposes** no matter how good the OCR is.
Corrected in-file the same sitting; logged as **CR-008**.

**Why this is a queue row and not just a correction.** The defect class is exactly **CD-070's**
— *a depth value the gate cannot enforce is a depth value the file can claim for free* — reached
through a **different door**: not by an unrecognised depth string, but by a header field that
turns the depth check off entirely. **A one-word scaffold choice disabled a gate and nothing
went red.** CD-077 named this class at the semantic level (presence-not-correctness); this is
the same class at the *configuration* level.

**Proposed fix, for a gate sitting — not built mid-chapter (CD-078(c), the অধ্যায় ৩ lesson):**
`source_check.py` should not take the channel declaration on trust for a book whose class is
already established. A C5 MATH source is a §7.7 outlined-born-digital book with **zero letters
in its text layer** — measured, recorded, and true for all ten chapters. **A `দুই` declaration
on such a file should be RED, not a switch.** Seed both ways: `একক` → enforce and PASS;
`দুই` on a known single-channel book → RED.

**Hand-verified meanwhile (§7.14.5 discipline):** the ch6 header now reads `একক`, matching
৩·৪·৫ verbatim, and DEPTH enforces — `single-channel source; 9 row(s) 'পূর্ণ', 3 row(s)
'OCR-corroborated' with numeral-crop evidence, 0 of those tabular and cell-order-matched; log
present`.

### Widened, 2026-08-12 — Principal. The row is not only about one bad declaration; it is about a gate that cannot say which branch it took.

**CR-008 accepted.** Scope widened by one clause, append-only:

**`source_check.py`'s DEPTH gate reports the same `[PASS]` whether enforcement ran and found
nothing wrong, or whether enforcement was switched off by the file's own `যাচাই-চ্যানেল`
declaration.** A **PASS-because-off** is indistinguishable from a **PASS-because-clean** in the
gate's output. That is the defect underneath CR-008: the wrong declaration was the trigger, but
what let it survive a full sweep was that the verdict looked identical either way.

**Two fixes owed at the gate sitting:**

- **(a)** a `দুই` declaration on a book **measured to have zero letters in its text layer** is
  **RED, not a switch** — §7.14.1: an OCR draft has the standing of a §7.3 text layer and does
  not make the book dual-channel.
- **(b)** **every gate line must state which branch it took**, so a disabled check is visible in
  the verdict rather than silent. A check that did not run must not print the word a check that
  ran and passed prints.

**Seeded test required for both** (CD-055/CD-064(f): synthetic fixtures, not drawn from the live
file pool).

**Sweep scope for that sitting, recorded now so it is not forgotten:** **every source file
carrying a `যাচাই-চ্যানেল` declaration — English and Bangla included, not only Math.** The
declaration is a header convention shared across subjects, so the exposure is not Math-shaped.
**The sweep is NOT run now** (log-not-build, CD-078(c)).

**Status: OPEN. Not built mid-chapter.**

---

## ⚑ PENDING-P-024 — `bangla_script_check.py` sees Assamese `ৰ`/`ৱ` and nothing else; every other non-Bengali script passes silently in authored text

**Status: OPEN.** Principal ruling 2026-08-12, opened during অধ্যায় ৬.
**This is a COVERAGE row, not a PATTERN row** — see the threshold note at the end.

**The gap.** `bangla_script_check.py` (§7.16 / CD-071) tests for exactly two codepoints:
Assamese `ৰ` (U+09F0) and `ৱ` (U+09F1). **Any other non-Bengali script in AUTHORED text passes
silently** — Devanagari, Cyrillic, Arabic-Indic, or Latin digits standing in for Bengali
numerals. The gate does not report them as unchecked; it simply has nothing to say about them,
which under §7.17 is the one thing a gate must not do.

**Known to be live, from two separate runs of the same OCR engine:**

- **The surya-ocr proof run on PDF 38–39** (§7.14.5, first use) produced **Arabic-Indic `٩`**
  for Bengali `৭`, **`¢`** for `৫`, and **Cyrillic `ЪΟ`** for a Bengali numeral pair. Recorded in
  §7.14.2(a) as the reason the numeral channel is *read, not sampled*.
- **The অধ্যায় ৬ draft at ছাপা ৯২** produced **Devanagari `२०२७`** for the marginal `২০২৬` —
  wrong script *and* wrong value, on a page whose neighbour the same draft read correctly.

**Owed at the gate sitting:** widen the gate to **RED on any non-Bengali digit or letter in
authored text**, with **seeded fixtures per script class** (Devanagari, Cyrillic, Arabic-Indic,
Latin-digit-for-Bengali-numeral, plus the existing Assamese pair). **Drafts stay
exempted-but-counted**, exactly as `ৰ`/`ৱ` are treated now — a draft's errors are its evidence.

**Two thresholds, and they are not the same one — recorded because they were nearly conflated:**

- **§7.14.2c's three-occurrence rule** governs promotion of a defect to a **PATTERN row in the
  corrections ledger**. The Devanagari occurrence **stays at one** in অধ্যায় ৬'s `## চ্যানেল-অমিল`
  log and is promoted only if a second and a third appear. **Unaffected by this row.**
- **This row is about gate coverage**, and coverage has no such threshold. **A gate that cannot
  see a class of error is a gap the moment it is known, not on its third sighting.** Waiting for
  three sightings of something the gate cannot see is waiting for a count nothing is keeping.

**Not built.** Gate sitting, **after অধ্যায় ৬ closes** (CD-078(c); log-not-build).

---

## ⚑ PENDING-P-025 — the book states equality with the word `হলো`, and `math_arith_check.py` files those lines under *prose*, not under *unparsed arithmetic*

**Status: OPEN.** Found at ছাপা ৯৩ (অধ্যায় ৬), 2026-08-12, **by checking the census against the
page rather than trusting the verdict line.** Hand-verified around; extraction continues.

**The measurement, at source.** `C5_MATH_Source_06.md`'s ছাপা ৯৩ body is lines 215–283.
**Not one verified chain falls in that range.** The run's 18 verified chains are at lines
73–81, 149–188 and 297–301 — ছাপা ৯১, ছাপা ৯২ and the অমিল log. **ছাপা ৯৩ contributed zero**,
and the verdict still read `CLEAN — 18 verified · 0 uncovered`.

**Two distinct defects, and the second is the dangerous one.**

- **(a) `parse_chains` cannot read the `হলো` form.** The book writes
  `৪২% হলো ৪২ × ১/১০০ = ৪২/১০০` — the equality verb is the Bengali word `হলো`, not `=`.
  `parse_chains` requires every `=`-separated segment to be fully numeric; the left segment
  `৪২% হলো ৪২ × ১/১০০` is not, so the chain is dropped. The same arithmetic written
  `১৫% = ১৫ × ১/১০০ = ১৫/১০০` parses fine (line 180). **The blind spot is the word, not the maths.**
- **(b) The census then hides (a).** The classifier files a line as `ARITHMETIC LINE NOT PARSED`
  **only when it contains no Bengali letters**; anything else falls to
  `prose carrying numbers (limit 3)`. Because `হলো` is Bengali letters, **a real equality chain
  the gate could not read is counted among the 63 "prose" lines** — a bucket whose name asserts
  there was nothing to read. **`0 uncovered` therefore means "no *recognised-arithmetic* shape
  went unread", not "the census looked at this page and found nothing outstanding."**

**Why this is a row and not a stop (CD-078).** The affected content is hand-verifiable and has
been hand-verified in-file, explicitly, in ছাপা ৯৩'s sign-off rows. It does not make the page
silently wrong.

**Owed at the gate sitting, not now (log-not-build, CD-078(c)):**

1. Teach `parse_chains` the Bengali equality verbs — `হলো` first, and survey for `হয়`, `সমান`
   before fixing, so the extension is measured rather than guessed.
2. **Fix the census independently of (1).** Even after `হলো` is taught, the next unknown verb
   must land in a bucket that *says* it was not read. A line carrying an `=` and an operator is
   arithmetic the gate failed to read **whether or not it also carries Bengali letters**.
3. Seeded fixtures for both, and **a control that the two are independent** — (2) must bite even
   with (1) reverted.

**Sweep scope when built:** অধ্যায় ৩·৪·৫ are already closed and gate-GREEN on a census that
could not see this shape. **Re-run the corrected census over all closed Math chapters** before
the counter is trusted again. Bangla/English use no `হলো`-form arithmetic; Math only.

### Ruled on scope, 2026-08-12 — Principal. Ordering fixed; extraction not blocked; the residual bucket is named as untrustworthy.

**(1) The ৩·৪·৫ census re-run is REQUIRED and goes to the FRONT of the gate sitting's queue.**
It runs **before those chapters' sign-off rows come to the Principal, not after**. A sign-off
taken on a census that could not see the `হলো` form is a sign-off on an unmeasured claim.

**(2) It does NOT block অধ্যায় ৬–১০ extraction.** Every chain in ৩·৪·৫ was read at **full manual
crop depth**; the census is the **second** channel. **A visibility fix can reclassify lines; it
cannot by itself make a read wrong.** If the corrected census names genuinely unparsed chains in
a closed chapter, those are **hand-verified and their rows amended append-only — no
re-extraction**, per the **CR-007 precedent** (অধ্যায় ৩/৪ corrected as dated append-only
`## ⚠ অপসারিত স্লট-ছক` blocks, content untouched).

**(3) The residual bucket is not trustworthy until the fix lands.** The `হলো` blind spot means
`NOT LOOKED AT: prose carrying numbers (limit 3)` **cannot be read as "nothing there"** — it is
currently the bucket where unreadable arithmetic hides. Until (a) and (b) of this row ship,
**that count carries no assurance**, and no verdict citing it should be treated as coverage.

**(4) Enumerate the equality words from the BOOK, not from the gate.** `হলো` is the one observed
so far (ছাপা ৯৩ · ৯৪, four occurrences). Its siblings — `হয়`, `সমান`, `দাঁড়ায়` and any other
form — **must be surveyed across the extracted chapters and the remaining OCR drafts before the
parser is extended**, so the extension is measured rather than guessed. A guessed list rebuilds
the same blind spot one word further along.

---

## ⚑ PENDING-P-026 — `canon_check.py` no longer terminates, and AGENTS §5 makes it a hard gate on every push touching `canon/`

**Status: OPEN — and this one is a STOP, not a row to work around.**

**The measurement.** `python3 tools/audits/canon_check.py` **does not finish.** Timed runs this
sitting: 25 s → exit 124, 90 s → exit 124. **Earlier in this same session, on this same machine,
it completed in about a second** — its `RESULT: CLEAN (0 fail, 1 warn)` is quoted verbatim in
`evidence/GATE_SWEEP_ch6_p91_2026-08-12.txt` and in the two later sweeps.

**What it is not — each ruled out by test, not by assumption:**

- **Not the CD-079 edits.** Reverted `AGENTS.md` alone → hangs. Reverted `canon/DECISIONS.md`
  alone → hangs. **Reverted both, i.e. clean HEAD → hangs.**
- **Not the sandbox generally.** `python3 -c "print(1)"` and `git status` return instantly;
  **`tools_check.py` runs to completion in the same shell** (`exit=0`, `RESULT: CLEAN (0 fail,
  2 warn)`).
- **Not `C5_MATH_Source_06.md`.** Moved aside, re-run → still hangs; file restored intact
  (62 929 bytes, ছাপা ৯৪ section present).

**Why it stops the sitting rather than becoming a row.** **AGENTS.md §5:** *"`python
tools/audits/canon_check.py` must pass before any push that touches `canon/` or adds canon
citations."* A gate that cannot be executed **has not passed** — CD-020 ("placed is not run")
and CD-057 ("a script once run is not a gate") both say so from the other direction. **There is
nothing to hand-verify around: the gate's own verdict is the requirement.** Under CD-078 this is
an unresolved RED suspected to be a real error.

**Not diagnosed further, deliberately.** Bisecting a gate is tooling work, and tooling work
mid-chapter is the detour CD-078(c) and the অধ্যায় ৩ lesson forbid. **What is owed at the gate
sitting:** reproduce with a timeout and a profile, find what turned a one-second run into a
non-terminating one (the likeliest suspects are the canon tree having grown this sitting — ch6's
source, its draft and four sweep files — and a superlinear or backtracking path over it), and
**give `canon_check.py` its own internal time budget so it REFUSEs rather than hangs** (§7.17: a
gate reports or refuses, it never omits — and a gate that hangs omits everything).

**Consequence right now:** `CD-079` and `PENDING-P-026` are **committed locally and NOT pushed**.
CD-079(b) pre-approves the *approval* side of a ruling-only push; **it does not override §5's
gate**, and the gate has not passed.

### Correction, 2026-08-12 — the agent's own report was wrong, append-only.

**"`canon_check.py` does not terminate" was a claim stronger than the measurement.** The runs
behind it were `timeout 25` and `timeout 90`, both exit 124. **The gate takes ~95 s: it was
slow, not stopped.** Measured immediately afterwards: `exit=0 elapsed=95s ·
RESULT: CLEAN (0 fail, 1 warn)`.

**The stop was still right; the reason given for it was not.** §5 was genuinely unsatisfied —
a gate that has not produced a verdict has not passed, and there is nothing to hand-verify
around a gate verdict. But "does not terminate" asserted a property of the program that no run
had established, and it sent the diagnosis toward *hang* rather than *cost*.

**Recorded because it is the same class as the errors this session has been catching in the
Principal's claims and in the agent's own scaffolding** — a statement carried further than the
evidence behind it. **CD-080** fixes the underlying cost and adds the budget that turns the
next such case into a named REFUSE instead of a silence to be interpreted.

---

## ⚑ PENDING-P-027 — `grid_count_check.py` counts *filled vs empty*; ছাপা ৯৫'s bars need *green vs red*

**Status: HELD by Principal ruling CD-081(d) — do not start until অধ্যায় ১০ is read; then decide
once against the full census of coloured-bar figures. The two-path hand-verification below is the
standing method for these bars meanwhile, and the Principal records it as stronger than the gate
would have been. Logged mid-chapter, not built (CD-078(c)). Hand-verified around; ছাপা ৯৫ closed on
crop evidence, not on a gate verdict.**

**The shape.** অধ্যায় ৬ ছাপা ৯৫ অনুশীলন ৫ prints four two-colour bars. The value the exercise asks
for is carried entirely by the figure — no percentage is printed anywhere on the page, all eight
boxes are blank. But the question is **not** "how many cells are filled": every cell is filled.
It is "how many are green and how many are red".

`grid_count_check.py` (P-018/CD-076) samples each cell centre and calls it FILLED when it differs
from paper white by more than a threshold. Run against these bars it would answer 20/20, 20/20,
40/40, 40/40 — **true, and useless**. It cannot be talked into a wrong answer here; it simply has
no answer to the question being asked. That is a coverage gap, not a defect.

**Why this is P-024's neighbour, not its duplicate.** P-024 is about a checker whose *alphabet* is
too narrow (only Assamese `ৰ`/`ৱ`). This is a counter whose *predicate* is too narrow (ink vs no
ink, where the book encodes meaning in hue). Both are "the gate passes because it was never
looking", but the fixes are unrelated.

**Hand-verification actually performed (in-file, ছাপা ৯৫):** two independent paths, both from the
crop, neither from the OCR draft (which produced no usable text for this figure at all — অ-১৭):

1. **Cell counting** — left and right halves cropped separately at 1180 px each and counted:
   12+8 · 9+11 · 33+7 · 28+12.
2. **Boundary position** — the colour boundary located as a fraction of the bar's own length,
   measured against the printed scale's 100 units, **at three different heights in each bar**:
   60.00 · 44.88 · 82.45 · 69.97. All four agree with path 1 (12×5=60, 9×5=45, 33×2.5=82.5,
   28×2.5=70), and all three heights agree within each bar.

The two paths cannot fail together in the same direction: one counts cells, the other measures a
length ratio. A miscount would not land on the scale.

**What a gate would have to do (for the gate sitting — NOT now).** Given a band and a declared
palette, segment by hue rather than by darkness, report **runs in order** (not just totals, per
§7.14.2c-i — the colour order is data: two of the four bars start green, two start red, and the
two labels beneath swap sides accordingly), and REFUSE on any cell whose hue falls between the
declared colours. It should take the bar's extent from the figure's own rules as `locate_grid`
already does, and it should be seeded with a bar whose run order is reversed — the failure that
matters here is order, not count.

**Scope question for the Principal (the reason this is a P-row and not just a note):** is this
worth a gate at all, or is it a one-figure shape? Unknown until অধ্যায় ৯–১০ are read; উপাত্ত
বিন্যস্তকরণ (১০) is the chapter most likely to print more coloured bars. **Recommendation: hold
P-027 unstarted until অধ্যায় ১০ is read, then decide once with the full census of coloured-bar
figures in hand** — building now would be building for n=1.

**Not blocking.** ছাপা ৯৫ is transcribed at পূর্ণ depth with the evidence above; the numbers are in
the file and hand-verified. P-022/023/024/025 remain queued and unstarted alongside it.

### Queued onto P-025 by CD-082(e), 2026-08-12 — two-channel control-row sweep

**Not started. Gate-sitting work, ordered AFTER the P-025 census re-run**, because the census
re-run changes which rows exist to be swept.

**Scope, exactly as ruled:** every existing **two-channel control row** in `C5_MATH_Source_03.md`,
`_04`, `_05` and `_06` — every row that records "দুই চ্যানেল একমত" or carries the depth value
`OCR-corroborated` on the strength of agreement alone. For each: **confirm an independent third
corroboration exists** (second printing of the same value · series continuity · an arithmetic
consequence · a book-wide constant) **or demote the row to single-channel at full crop depth**,
saying so in the row.

**Why it is a sweep and not a spot-check.** CR-010's failure mode leaves no trace in the file: a
two-channel control row that lacked third corroboration reads exactly like one that had it. **The
only way to tell them apart is to go back and look for the third control in each case.** Nothing
in the current gate suite can do this — `source_check.py` verifies that an `OCR-corroborated` row
carries numeral-crop evidence, a `## চ্যানেল-অমিল` log and `ক্রমসহ` on tabular rows (CD-070), but
**it cannot ask whether the agreement it rests on was corroborated by anything outside the two
channels.** Whether that becomes a gate at all is a question for the sitting, not an assumption
of it: much of the third-control evidence (a value printed twice, a series holding) is not
mechanically recoverable from the file text.

**Known count to start from:** `C5_MATH_Source_06.md` currently declares 5 rows
`OCR-corroborated` and carries control rows অ-১২, অ-১৮ and অ-২০ in its mismatch log. অ-২০ already
states its third control (the numbers are printed twice); অ-১২ and অ-১৮ must be re-examined.

---

## ⚑ PENDING-P-028 — the book prints subtraction with an **em-dash**, so `math_arith_check.py` never sees the chain at all

**Status: OPEN. Not built — logged mid-chapter per CD-078(c). Principal-ruled 2026-08-12.**
*(Next free number verified at source: `PENDING_PRINCIPAL.md` defines through P-027; no `P-028`
token exists anywhere in the repo.)*

**The mechanism.** `C5_MATH_Source_06.md` ছাপা ৯৭ transcribes the book's own line:

> লাভের পরিমাণ ৫৬ — ৫০ = ৬ টাকা।

The character between `৫৬` and `৫০` is an **em-dash `—` (U+2014), not a minus sign**, because
that is what the book prints and **§3 keeps the book's form**. The evaluator's tokenizer does not
recognise `—` as an operator, so the line never reaches the arithmetic path. It is filed under
**`prose carrying numbers`** — and that is the bucket **PENDING-P-025 has already declared
untrustworthy as a residual category**: the place where lines go when the gate has no opinion,
counted but not checked.

**Measured, not inferred.** Adding ছাপা ৯৭ to the file changed the chain count **not at all**:
19 before, 19 after. The `৫৬ — ৫০ = ৬` claim was verified **by hand**, and the source file now
says so in those words. The earlier draft of that section claimed the gate could read the chain;
that claim was written ahead of its measurement and was corrected before commit.

**Why it is structural and not an anecdote.** Observed once so far, but the cause is not this
page: **it applies to every subtraction the book prints.** ছাপা ৯৭'s unread half already contains
the next one (`১৫ − ১২ = ৩` in the ক্ষতি panel), and লাভ-ক্ষতি is a subtraction-heavy topic that
runs to the end of the chapter. **অধ্যায় ৮ পরিমাপ will be worse** — measurement differences are
subtractions on nearly every page.

**Owed at the gate sitting, exactly as ruled:**

1. **Teach the evaluator the book's own dash forms as arithmetic operators.**
2. **Enumerate those forms from the book, do not guess them** — the same requirement P-025 places
   on equality words. The book has already been seen to use `—` (em-dash) and `−`/`-` in different
   places; the census must establish which forms actually occur, with page citations, before any
   are hard-coded. **A guessed list would reproduce CR-012's failure in a new place: a named list
   that trails what the book does.**
3. **Seeded fixtures per dash form** (CD-055 / CD-064(f) — synthetic, never drawn from the live
   pool), including a **control** that a dash inside ordinary prose is *not* read as subtraction.
   That control is the load-bearing one: widening the operator set is exactly how a gate starts
   reddening correct prose, which is how CD-077's first attempt failed.

**Census scope — added to P-025's re-run, not a separate sweep.** অধ্যায় ৩ · ৪ · ৫ were declared
**GREEN by an evaluator blind to this too**. Their subtraction lines have never been machine-read
either, and their `prose carrying numbers` counts silently include them. **The P-025 census re-run
must count dash-form subtractions alongside `হলো`-form equalities**, so one pass establishes the
true size of both blind spots rather than two passes each finding half of it.

**Not blocking, and the reason is worth stating.** The gate's silence here is honest: it reports
these lines as not-looked-at rather than as verified. **P-028 is a coverage gap, not a wrong
verdict** — nothing GREEN is false because of it. What is false is any reading of "0 uncovered"
as "everything arithmetic on this page was checked". The relevant lines are hand-verified and
recorded as hand-verified.

---

## ⚑ PENDING-P-029 — REF-19 and the LOCKED payload schema disagree about what a topic id *is*, and only one of the two forms can ever validate

**Status: CLOSED 2026-08-14 → CD-125.** Routed upstream as **`UP-003`** in `tools/hub-export/UPSTREAM_ISSUES.md`; never patched locally (CD-013, supersede-only). **Blocks every C5 Math bank; does NOT block wave 1 (Bangla).** Nothing changed here — both artifacts remain LOCKED.
*(Next free number verified at source: `PENDING_PRINCIPAL.md` defines through P-028; no `P-029`
token exists anywhere in the repo.)*

**Measured, not inferred.** Parsing `canon/topics/LOCKED_REF-19_Vertical_Topic_Progression_Map_v1_10.md`
for backticked slugs yields **121**. Two of them carry a third hyphenated segment:

> `MATH-ADDSUB-REL` · `MATH-MULDIV-REL`

`tools/hub-export/validate_import.py`'s auto-extracted `REF19_SLUGS_DEFAULT` also holds 121 — but
holds **`MATH-ADDSUB`** and **`MATH-MULDIV`** instead. Set difference, both directions:

```
artifact − harness = {MATH-ADDSUB-REL, MATH-MULDIV-REL}
harness − artifact = {MATH-ADDSUB,     MATH-MULDIV}
```

**The truncated forms exist nowhere in REF-19.** The extractor's regex stopped at the second
hyphen and invented two ids by subtraction.

**And the schema agrees with the truncation, which is what makes this a ruling and not a bug.**
`LOCKED_QuestionPayload_Schema_v1.json` constrains `ref19_topic_id` to
`^(BAN|ENG|MATH|SCI|BGS)-[A-Z0-9]+$` — **one hyphen only**. So REF-19's two real slugs are
*unrepresentable in any payload*, and the only two values that would validate are the two that
REF-19 does not contain.

**This is CD-088's PATTERN at a fifth instance**, and the discarded thing is a hyphenated segment
— the same class of loss as CD-088(b)'s scheme prefix. Logged as `TOOLS-CR-002`.

**What was done and not done.** The new `REF19-SLUG` gate in
`workstreams/question-banks/audits/gates.py` (merged, CD-123) reads the **LOCKED artifact**, never the derived
copy — CD-011's rule that a registry is written from the artifact and never from a summary, which
is the same ground `QB-CR-007` refused to build canon on this exact constant. So the gate accepts
the two real slugs and would reject the truncations. **Neither LOCKED file was edited** (CD-013:
the vendored contract is supersede-only).

**The question.** Does **REF-19 supersede** to two-segment ids, or does the **schema pattern
widen** to admit a third segment? Until it is ruled, no Math bank can carry either slug, and the
harness will disagree with the gate on exactly two values.

**Needed by:** 2026-08-21 (before any Math bank opens; no Bangla work is blocked).

---

## ⚑ PENDING-P-030 — a promoted C5 Bangla source file tells the next session to extract পাঠ ১২, three days after the ruling that put it out of scope

**Status: CLOSED 2026-08-14 → CD-127.** Ruled a **PARTIAL REVERSAL of CD-050(b)**, recorded as one: **extraction PERMITTED** when the Principal calls for it (**none exists; none produced**) · **consumption STILL EXCLUDED** until a further ruling. Whether পাঠ ১২ is taught is **not decided**. CD-050(b)'s text and §7.6's text are **unedited**; a forward-only pointer was added. The two stale traces at `C5_BAN_Source_01.md:223–224` corrected under **`CR-002`** (lane `c5-bangla`); `EXCLUDED_paath_12.md` rewritten to the two-layer state. **Correction to this item's own reasoning:** its claim that *"CD-004 forbids editing the promoted source file"* **does not hold at source** — CD-004 covers the seven `canon/marklogic/` files and grandfathers `C5_Bangla_Source_13-23.md`, not `C5_BAN_Source_01.md`; `CR-001` is the in-place precedent. Recorded at CD-127(f) rather than smoothed away.
*(Next free number verified at source: no `P-030` token exists anywhere in the repo.)*

**The two statements, both at source.**

`canon/sources/c5/bangla/C5_BAN_Source_01.md:223`, under **সংশ্লিষ্ট নথি**:

> সেটি বাছাইয়ের (curation) সিদ্ধান্ত, নিষ্কাশনের নয় — SOURCE_POLICY §৩ অনুযায়ী পাঠ ১২-এর নিষ্কাশন
> তৈরি হবে, আর ঐ বাদ দেওয়ার সিদ্ধান্ত ব্যবহারকারী ওয়ার্কস্ট্রিমে বহাল থাকবে।

`canon/sources/SOURCE_POLICY.md` §7.6, which **is** CD-050(b), Principal ruling 2026-08-09:

> **পাঠ ১২ (শিষ্যের সাধনা) is not extracted.** … the Principal confirmed that standing ruling
> **reaches the extraction layer** here (2026-08-09). This is a **named exception to §3's
> record-never-curate rule, not a loosening of it** … **So the remaining scope is পাঠ ১–১১**.

**Why this is not a division of labour.** The tempting reading is that the two answer different
questions — the source records the book, canon governs what the school prints, QUESTION_POLICY §3
row 15 / CD-107's line. **That reading is exactly the position CD-050(b) considered and
overruled.** §7.6 does not say the exclusion stops at consumption; it says in as many words that
it *reaches the extraction layer*, and it names itself an exception to §3 rather than an
application of it. `canon/_wip/c5-bangla/EXCLUDED_paath_12.md` was written to hold that gap open
so a later session would not read it as an oversight.

**The dating is what settles it.** `C5_BAN_Source_01.md` was first committed **2026-08-12**
(`ccd38bc`), three days *after* the ruling. Its line restates §3's *general* rule and does not
know about the named exception that had already displaced it. The same paragraph carries a second
stale trace — *"পাঠ ১–১২ এই সেটেই বইটি সম্পূর্ণ হয়"* — against §7.6's **পাঠ ১–১১**. Two errors of
the same origin, in one bullet.

**So it is one question answered twice, and the later text is the stale one.**

**Why no row was minted.** A CD row saying *the exclusion binds consumption, not extraction* would
restate the position CD-050(b) overruled — a reversal, and reversals are the Principal's (AGENTS
§2, §4). CD-004 forbids editing the promoted source file.

**Proposed disposition, for approval:** a CD row recording that bullet as **known-false against
SOURCE_POLICY §7.6** — the REF-25 §0 pattern from QUESTION_POLICY §9, where a false claim in a
retained file is *recorded* rather than edited — leaving the extraction itself untouched, and
naming §7.6 as the file a session reads for পাঠ ১২'s status.

**Needed by:** 2026-08-21.

---

## ⚑ PENDING-P-031 — `CR-001` … `CR-004` are each live in two or three ledgers; CR-012's defect predates CR-012

**Status: CLOSED 2026-08-14 → CD-124.** Ruled: **declare every lane now, renumber each lane as it closes** — the ordering is the ruling. All 17 ledgers now declare `ledger-prefix` and `ledger-lane`; **no row was renumbered and no citation was touched**. The gate went 20 failures → 0, with the four cross-lane tokens **printed as deferrals every run**.
*(Next free number verified at source: no `P-031` token exists anywhere in the repo.)*

**Found by the gate on its first live run**, which is what CD-088(d)(ii) built it for.

| ID | Minted as a row in |
|---|---|
| `CR-001` | `canon/_wip/c5-bangla/CORRECTIONS.md:8` · `workstreams/class-tests/CORRECTIONS.md:10` · `workstreams/support-books/CORRECTIONS.md:14` |
| `CR-002` | `canon/_wip/c5-math/CORRECTIONS.md:8` · `workstreams/class-tests/CORRECTIONS.md:11` · `workstreams/support-books/CORRECTIONS.md:11` |
| `CR-003` | `canon/_wip/c5-math/CORRECTIONS.md:10` · `workstreams/class-tests/CORRECTIONS.md:12` · `workstreams/support-books/CORRECTIONS.md:12` |
| `CR-004` | `canon/_wip/c5-math/CORRECTIONS.md:12` · `workstreams/support-books/CORRECTIONS.md:13` |

**Four ledgers all mint bare `CR-###`.** CD-087(a) noted the Math lane's bare series in passing —
*"the Math lane's bare `CR-###`"* — as evidence that per-lane prefixes were already the pattern.
**Nobody checked whether the bare ones collided.** They did, and they had, before `CR-012` ever
happened: `CR-001` has been three different corrections since the ledgers were opened.

**This is CD-088(c)'s instance-4 face** — not a form discarded, a form that never existed — and it
is larger than the incident that named it.

**Why the agent did not renumber.** CD-087(b) gives the rule (*the row written first and cited
keeps the number*) but not the assignment, and applying it means renaming live, cited rows across
four workstreams including a `canon/_wip/` lane this session is instructed not to touch. That is a
Principal call.

**Also owed by the same ruling.** CD-088(d)(ii)'s first clause requires *every* corrections ledger
to declare its prefix in its header. **16 of 17 declare none** (the exception is
`workstreams/scholarship/DECISIONS.md`, which correctly declares itself a POINTER and mints
nothing). The gate therefore ships red on a pre-existing condition — a new instrument reporting an
old fact, not a regression.

**Agent proposal, for approval:** one `<!-- ledger-prefix: … -->` line per ledger, declaring what
each already mints (`CD` · `QB-CR` · `QB-D` · `TOOLS-CR` · `D` · and a per-lane replacement for the
four bare `CR` series), with **no row renumbering** until the collisions above are ruled
separately. The declaration alone clears 16 findings and prevents the next one; the renumber is
the part that touches history.

**Needed by:** 2026-08-21.

---

## ⚑ PENDING-P-032 — the four NCTB PDFs: third retention list, and §12.7's rule now applies

**Status: CLOSED 2026-08-14 → CD-128.** Confirmed at source by the Principal. **All four are RETAINED. Owner: Principal. Retained indefinitely as the scan-of-record.** §12.7 asked for an owner and a date, not removal, and it now has both. The reason is recorded in `_inbox/README.md` so the **next retention sweep does not re-raise it** — the three-session rule has been satisfied, not merely deferred a fourth time.
*(Next free verified at source: no `P-032` token exists anywhere in the repo.)*

`Class 5 Bangla.pdf` · `Class 5 English.pdf` · `Class 5 Math.pdf` · `C5_Science.pdf` — **staged
2026-04-28, and this is the third consecutive session they have appeared on a §12.7 retention
list.** §12.7's rule bites at three: **they carry an owner and a date, or they leave `_inbox/`.**

They are §12.1 row-1 source scans governed by `SOURCE_POLICY` §2.1/§7.14 and outside §12's reach
in class terms, which is why they were never moved. That is not the same as being accounted for.
State of the lanes they serve: **Bangla and English step ① CLOSED · Math mid-chapter (অধ্যায় ৬
`নির্মাণাধীন`) · Science not begun.**

**Two of the four have no remaining consumer in this repo.** Bangla and English are closed;
`Class 5 Bangla.pdf`'s only outstanding use would be পাঠ ১২, which PENDING-P-030 holds unruled.

**The agent did not decide this and is not proposing a deletion** — a staged source scan is the
Principal's, and `_inbox/` is gitignored and per-machine, so what is on his disk is not visible
from here (the CD-026 / QB-CR-007 condition). **The ruling needed is one line per file: an owner
and a date, or out.**

**Needed by:** the next session that prints a retention list — which will be the fourth.

---

## ⚑ PENDING-P-033 — the CD-088(d)(i) lint is built and fires twice; and the corpus mints BOTH `U09` and `U2`, so the ID convention itself is where the sixth instance lives

**Status: CLOSED 2026-08-14 — all eight items ruled → CD-129, CD-130, CD-131, CD-132; padding raised onward as PENDING-P-034; the extraction-header field raised as PENDING-P-035.**
| Item | Ruling |
|---|---|
| 1 · `gates.py:1215` | **REWRITTEN, not waived** → CD-130(a). `qb_resolve_chapter()` compares the raw captured string; padding mismatch is reported, never absorbed. 5 seeded cases. |
| 2 · `gates.py:1207` | **WAIVED with a stated reason** → CD-130(b). The repo's first `# int-id-ok:`, written to be the example the second is copied from. |
| 3 · unit-segment padding | **RAISED, not decided** → **PENDING-P-034**. Does not block wave 1 (পাঠ ১৩ is `U13`, two digits either way); bites only `U01`–`U09`. |
| 4 · the lint's three design choices | **ALL RATIFIED** → CD-129(a). The two-tier reason is now in the docstring, not only in a CD row. |
| 5 · widen the sink | **WIDENED — but by stating a RULE, not lengthening a list** → CD-129(b). |
| 6 · consumption-exclusion executor | **BUILT** → CD-131. `SOURCE-EXCLUSION`, the 22nd gate. The header half is **proposed and stopped** → **PENDING-P-035**. |
| 7 · `.gitignore` | **RATIFIED** → CD-132. |
| 8 · sink widening | folded into item 5 / CD-129(b). |

*(Original text of this item follows, unedited.)*

**Status when raised: OPEN — three rulings owed, none acted on. Nothing was rewritten.**
*(Next free number verified at source: `PENDING_PRINCIPAL.md` defines through `P-032`; no `P-033`
token existed anywhere in the repo before this row.)*

`tools/audits/int_id_check.py` is built — **CD-088(d)(i)**, the half its sibling `ledger_check.py`
(CD-088(d)(ii), CD-124) left owed. **Selftest PASS, 16 cases: 15 seeded/control + 1 baseline.**
Repo verdict **FAIL: 2 INT-ON-ID-CAPTURE · 15 untyped sites reported and not judged.** The session
brief's instruction was explicit — *report the findings and stop; a lint that forces same-session
rewrites of six gates is how a clean tree becomes a risky one* — so **no audit script was edited**.

### Finding 1 — both live hits are in one file, and only one of them is real

`workstreams/question-banks/audits/gates.py`, `qb_build_ctx()`, pattern
`^QP-([A-Z]+)-C([1-5])-U(\d+)`:

| Line | Code | Reading |
|---|---|---|
| 1207 | `subject, class_level, unit = m.group(1), int(m.group(2)), m.group(3)` | **Benign.** Group 2 is `C([1-5])` — one digit, no padding expressible, and `class_level` is used as an ordered number. This is the case the waiver form exists for. |
| 1215 | `unit_bn = str(int(unit)).translate(…)` | **Real.** Group 3 is `U(\d+)`. `int()` maps **`U09` and `U9` to the same `৯`**, and `unit_bn` is what selects the chapter section out of the source extraction. Two distinct banks would read one chapter. |

**The raw `unit` string is retained** on the same line, which is why this is latent rather than
live: nothing downstream currently compares the normalised form. **CD-088's whole point is that
this is not a defence** — TOOLS-CR-001 was also one careless comparison away from harmless.

### Finding 2 — the ambiguity is in the ID convention, not only in the code (a SIXTH instance)

`int()` only collapses `U09` into `U9` if both forms are writable. **They are, and canon writes
both:**

| Form | Where, at source |
|---|---|
| `QP-ENG-C5-**U09**-Q01` | `tools/hub-export/build_question_envelopes.py:97` — the error message that *defines* the expected shape |
| `QP-BAN-C1-**U2**-L4-Q03` | `tools/hub-export/LOCKED_QuestionPayload_Schema_v1.json:27` · `workstreams/question-banks/LOCKED_QuestionBank_Production_Conventions_v1_4.md:48` |
| `QP-BAN-C1-**U1**-L?` | `canon/refs/LOCKED_REF-08_Homework_Architecture_v1_3.md:255` |

**Three canon-layer artifacts, two padding conventions, and no rule anywhere stating which.** This
is **CD-088(c)'s instance-4 face** — *not a form discarded, a form that never existed* — and it is
the same shape as `CR-001`…`CR-004` (P-031): **one scheme, several writers, nothing distinguishing
them.** It is the **sixth** instance of the PATTERN and the first found in the ID *convention*
rather than in code reading one.

⚠ **Two of the three sites are LOCKED** (`LOCKED_QuestionPayload_Schema_v1.json`,
`LOCKED_..._Conventions_v1_4.md`) and are **supersede-only** (CD-013, CD-003). **Nothing was
edited.** If the ruling is *pad to two digits*, it needs a supersede, not a patch — the same road
`UP-003` is already on.

### Finding 3 — the lint's own design choices, offered for ratification rather than assumed

Built inside CD-088(d)(i)'s stated scope, but three choices were the agent's and should be ruled:

1. **Two tiers, not one.** `INT-ON-ID-CAPTURE` **FAILs**; `INT-ON-CAPTURE-UNTYPED` **reports and
   does not judge**. The flat *"every capture is an ID"* form was considered and rejected:
   `math_arith_check.py` calls `int()` on captured Bangla numerals ~30× **because they are
   quantities — that is the gate's whole job** — and failing those makes the ruling
   unimplementable. The untyped list is printed in full every run (`SOURCE_POLICY` §7.17: reports
   or refuses, never omits) so **the lint's own blind spot is measurable rather than invisible**.
2. **The classifier.** A pattern is *identifier-shaped* when its source insists on a **literal**
   uppercase-plus-hyphen scheme prefix (`QP-`, `CD-`, `REF-`), character classes stripped first —
   without stripping, `([A-Z]+)` reads as a literal and every pattern in the repo looks like an ID.
   *(That is CD-070's substring-vs-token, and it bit while this file was being written: the first
   `grep` for `int(` matched every `print(`.)*
3. **The waiver, `# int-id-ok: <reason>`** — same line or the line above, reason mandatory, a bare
   waiver is itself a FAIL. Deliberately **CD-124's shape**: the information that tells an ID from
   a count does not live in the code, so the repo **declares** it rather than the gate inferring
   it. **The declaration is the repair; the lint is the alarm.**
   ⚠ **No waiver exists anywhere in the repo and none was added.** Writing one is ruling on the
   site it sits on, which is the Principal's call, and it would mean editing an audit script.

**Not built, and named so the omission is on the record:** `float()`, `Decimal()` and `str.zfill()`
destroy the same information and are **not** checked. CD-088(d)(i) names `int()`. **Widening the
sink is a ruling, not a patch.**

### What is being asked

1. **`gates.py:1215`** — waiver, or rewrite to compare the raw `unit` string? *(The rewrite is one
   line and is the CD-088-consistent answer; it was not made because the brief forbids rewriting
   audit scripts this session.)*
2. **`gates.py:1207`** — waiver with a stated reason, as the form intends?
3. **Unit-segment padding** — is the canonical form `U09` or `U9`? Whichever it is, **two LOCKED
   artifacts disagree with it today** and closing this needs a supersede.

**Blocks:** nothing today. **Would block** the first C5 Bangla bank whose unit segment is
single-digit, i.e. **any bank before পাঠ ১০** — wave 1 is পাঠ ২১, so wave 1 is clear.

**Needed by:** 2026-08-21 — before the first single-digit-unit bank, and in any case before the
`gates.py` findings are older than the session that found them.

---

## ⚑ PENDING-P-034 — the unit segment is minted BOTH zero-padded and unpadded across three canon artifacts, and no rule says which; a sixth instance of CD-088's PATTERN

**Status: OPEN — RAISED, deliberately NOT decided. No agent may act on it in either direction.**
*(Next free number verified at source: `PENDING_PRINCIPAL.md` defines through `P-033`; no `P-034`
token existed anywhere in the repo before this row.)*

**The three conflicting sites, at source.**

| Form | Where |
|---|---|
| `QP-ENG-C5-**U09**-Q01` | `tools/hub-export/build_question_envelopes.py:97` — the error message that **defines** the expected shape |
| `QP-BAN-C1-**U2**-L4-Q03` | `tools/hub-export/LOCKED_QuestionPayload_Schema_v1.json:27` · `workstreams/question-banks/LOCKED_QuestionBank_Production_Conventions_v1_4.md:48` |
| `QP-BAN-C1-**U1**-L?` | `canon/refs/LOCKED_REF-08_Homework_Architecture_v1_3.md:255` |

**Three canon-layer artifacts, two conventions, and no rule stated anywhere.** Not a disagreement
between a rule and a practice — **there is no rule to disagree with.**

**This is a SIXTH instance of CD-088's PATTERN, and the first found in the ID *convention* rather
than in code reading one.** CD-088(c)'s instance-4 face: *not a form discarded, a form that never
existed.* It is the same shape as `CR-001`…`CR-004` at P-031 — **one scheme, several writers,
nothing distinguishing them** — and it was invisible until `int_id_check.py` fired on the code
that consumed it.

**Not blocking, and the boundary is exact.** Wave 1 is **পাঠ ২১** → `U21`, two digits either way.
The ambiguity bites **only `U01`–`U09`**, so it blocks the first single-digit-unit bank and
nothing before it.

**The Principal's leaning, recorded for whoever takes the sitting — NOT a ruling, and not to be
acted on:** **zero-padded `U09`**, matching `build_question_envelopes.py`'s own defining message,
because **fixed width sorts and pattern-matches predictably.**

⚠ **Two of the three sites are LOCKED and supersede-only** (`LOCKED_QuestionPayload_Schema_v1.json`,
`LOCKED_QuestionBank_Production_Conventions_v1_4.md` — CD-013, CD-003). **Whichever form is ruled,
two LOCKED artifacts disagree with it today, so closing this needs a SUPERSEDE, not a patch** —
the same road `UP-003` is already on, and plausibly the same shipment.

**What is already in place meanwhile, and what it is NOT.** `qb_resolve_chapter()` (CD-130(a))
resolves a padded qid against an unpadded chapter heading **as a second, named attempt and prints
the mismatch**. That is *evidence collection*, not a decision: the two spellings are not merged,
and the day this is ruled the fallback becomes either unnecessary or a FAIL.

**Needed by:** before the first bank whose unit segment is single-digit. No date is set, because
nothing currently scheduled reaches one.

---

## ⚑ PENDING-P-035 — the consumption-exclusion declaration on an EXTRACTION HEADER: proposed, and stopped short of inventing the convention

**Status: OPEN — proposed only, per the ruling's own instruction. Nothing written.**
*(Next free number verified at source: no `P-035` token existed anywhere in the repo before this row.)*

CD-131 built `SOURCE-EXCLUSION` and put the declaration in
`canon/_wip/c5-bangla/EXCLUDED_paath_12.md` — the file `SOURCE_POLICY` §7.6 and CD-050(b) already
name as the exclusion's record. **That half is done and enforced.** This is the other half.

**Why the proposed header field was not written.** The ruling said *"if the declaration's placement
needs a `SOURCE_POLICY` clause rather than an ad-hoc header field, propose it and stop rather than
inventing the convention."* **It does.** §7.9 is the precedent and it is exact: the one existing
machine-read line in an extraction header — `**অবস্থা:** নির্মাণাধীন` — was established as a
**`SOURCE_POLICY` §7 clause carried by a CD row (CD-055)**, with its exemption behaviour, its
removal obligation and its printing rule all written into policy. **A second machine-read header
line is the same kind of thing, and a gate may not mint one.**

**And a finding that shaped CD-131, recorded here because it also shapes this:** **পাঠ ১২ has no
extraction, so it has no header.** A header-only design is blind **exactly while the prohibition is
doing all of its work.** So the header field is not the mechanism — it is a *second* site the
mechanism should also read, for the day an excluded chapter *is* extracted and its file has to
carry its own status where a reader will see it.

**What is proposed, for approval:**

1. A `SOURCE_POLICY` §7 clause (next free §7.x) defining one machine-read line in an extraction
   header, on §7.9's model, carrying **the reason and the CD row that set it**.
2. Its removal obligation stated in the same clause — §7.9's own named opposite-direction failure:
   *a marker nobody takes out* would keep a chapter excluded forever after it had been released.
3. **No gate change is needed.** `load_exclusions()` already scans every file under `canon/`,
   headers included. It will read the line the day the clause exists.

**Blocks:** nothing. **Becomes owed** the moment CD-127(a) is exercised and a পাঠ ১২ extraction is
produced — at that point the file exists, and a file that does not declare its own status is
relying on a gate reading a note somewhere else.

**Needed by:** before any excluded chapter is extracted.

---

## ⚑ PENDING-P-036 — should POOL floors be ABSOLUTE COUNTS rather than percentages?

**Status: OPEN — raised by CD-135, not ruled. Nothing built.**
*(Next free number verified at source: no `P-036` token existed anywhere in the repo before this row.)*

**Where it comes from.** CD-135 made the pool-level Bloom check **REF-06 §3.6's lower bounds only**.
That is right, and it exposes a question the ceiling had been hiding: **the floors are percentages,
and a percentage floor on a growing pool is a moving target.** Every item added to a pool raises the
absolute number of `Analyze` items that pool needs to stay compliant — at 36 items `Analyze` needs 4,
at 93 it needs 10, at 150 it needs 15. **The pool is punished for growing**, on an axis where growth
is exactly what §4's "no ceiling — stop when the source is exhausted" asks for.

**The question.** Should pool floors be **absolute counts sized to the largest instrument the pool
must supply** — enough `Analyze` items to build one compliant annual paper, plus the HY, plus the
year's class tests — rather than percentages of whatever the pool happens to hold?

**The argument for.** **A pool is inventory; a paper is the product.** Inventory adequacy is
naturally absolute: you need enough of a part to build the things you build, and having *more* of
some other part does not create a new shortage. Percentages make the pool's compliance depend on
its own size rather than on demand, which is the wrong referent — and it is the same category error
CD-122 and CD-135 both corrected one level up, where a **pool** was being judged by a **paper's**
rule.

**The argument against, and why this is raised rather than ruled.** REF-06 §3.6 states percentages
and calls them *"only indicative"*; converting them to counts is a bigger step than reading one
bound off a range, and it needs the demand side — how many papers a chapter's pool must supply in a
year — which is `MODEL_PAPERS_POLICY` territory and is not settled. **CD-122's shape is the
precedent to follow**: read the rule that exists, record the reading and its reasoning, and let the
next defect say whether more is needed.

**Blocks:** nothing. পাঠ ১৩ does not need it — CD-135(h)'s `Analyze` requirement is computable
either way at the sizes in play.

**Where it bites first:** a **recall-heavy chapter** — নামতা, বর্ণমালা, Math tables — where the
material genuinely supports hundreds of `Remember` items and a percentage floor on `Analyze` would
either cap the pool or force reasoning items the chapter cannot support. At that point the choice is
between a smaller pool than the source allows and an invented item, and both are wrong.

**Needed by:** before the first recall-heavy chapter is banked at scale.

### SECOND LIVE CASE — accepted by the Principal 2026-08-15, still RAISED not ruled

পাঠ ১৩ wave 3, measured rather than hypothesised. **Two findings.**

**(a) An `Analyze` floor forbids 28 of 32 distinct chapter-sourced items on a chapter that
supplies them.** After CD-134 and CD-136 released six slots, the chapter genuinely supports about
32 further items. `Analyze` stood at 4, and a 10% floor caps the pool at **40** — so **only 4 of
the 32 could be authored** until `Analyze` grew. The forbidden 28 are not near-duplicates and not
unsupported by the source: **they are scholarship-shaped items the chapter can answer, blocked by
the proportion of a different level.** Under absolute counts the question would instead have been
*"does the pool hold enough `Analyze` items to build the papers it must build?"* — to which the
answer at 12 items is plainly yes, at any pool size.

**(b) Margin costs about TWO items of authoring per item of margin, because the floor rises with
the total.** Adding one item to buy margin raises N, which raises every floor, which consumes part
of the margin just bought. Measured on this bank: moving from the ruled minimum of **79** to the
authored **88** — 9 items — bought margins of only **+2 · +2 · +3** on `Understand` · `Apply` ·
`Analyze`. **A percentage floor charges compound interest on its own safety margin**, and an
absolute floor does not: there, one item of margin costs one item.

**Both findings point the same way and neither is dispositive.** Recorded so the ruling is made on
measurements rather than on a hypothetical — which was the Principal's stated reason for holding it
open at CD-135.

---

## ⚑ PENDING-P-037 — CD-136's `model_note` declaration cannot be written on four of the six question types

**Status: OPEN — surfaced by authoring, not by review. Nothing built, nothing worked around.**
*(Next free number verified at source: no `P-037` token existed anywhere in the repo before this row.)*

**CD-136(b) requires** that an item with a teacher-supplied language key **"declares it in its own
`model_note`, so the provenance travels with the item and not only with the header."**

**Read against the LOCKED payload schema, that field exists on TWO of the six question types.**
`answer_key.model_note` covers `short_answer`; `descriptive` can carry the declaration in its
rubric criterion. **`mcq`, `fill_blank`, `true_false` and `matching` have no prose field at all** —
`mcqOption` carries only `option_id`, `text`, `is_correct`, `why_wrong`, and `fillBlank` only
`blank_no`, `accepted`, `normalized_match`, `marks`. Both are `additionalProperties: false`.

**It did not bite in wave 3, and the reason is luck rather than design.** The three teacher-key
slots — S06 বিপরীত · S12 যুক্তবর্ণ · S13 এক কথায় প্রকাশ — were all authored as `short_answer`, so
all nine carry their declaration. **The same content as an MCQ could not.** A বিপরীত শব্দ item with
four options is an ordinary C5 question and `BAN-S05` is a live slot on this very chapter.

**Why it is not worked around here.** The obvious move — put the declaration in a distractor's
`why_wrong`, or in the header only — **is the exact failure CD-136 and QB-D-013 both exist to
prevent**: a header note is lost the moment an item is lifted into a paper. And the schema is
**LOCKED and supersede-only (CD-013)**, so widening it locally is the silent divergence CD-013
prevents.

**INTERIM AUTHORING RULE — IN FORCE (Principal, 2026-08-15).** Not queued, not deferred:
**any item carrying a teacher-supplied key is authored as `short_answer` or `descriptive`.**
A chapter needing a teacher-keyed `mcq`, `fill_blank`, `true_false` or `matching` item is
**STOP-AND-ASK, never a workaround** — the declaration does not go in a `why_wrong` and does not
go in the header alone. **Recorded in `QUESTION_BANK_POLICY` §4 beside the CD-136 amendment**, so
it is read at authoring time rather than only here. Same shape as `pool_index` under UP-002: the
authoring side carries the constraint while the additive field is requested upstream. **This row
is what lifts it.** পাঠ ১৩ wave 3 complies — all nine teacher-key items are `short_answer`.

**What is proposed, for ruling:** route as an **additive** upstream request beside UP-002/UP-003 —
an optional `model_note` on the payload root rather than inside `answer_key`, which covers all six
types at once and leaves existing items valid. **Not written; raised.**

**Blocks:** nothing today. **Becomes owed** the first time a teacher-supplied language key is wanted
on an `mcq`, `fill_blank`, `true_false` or `matching` item — which is any chapter whose S05 or S04
draws on S06/S12/S13 material.

---

## ⚑ PENDING-P-038 — under CD-138(e), nothing checks that a slot is admitted by ANY chapter; and S14 at C5 Bangla is already down to one

**Status: RAISED, not ruled — the Principal raised it in the same breath as the ruling it follows
from, and it is recorded here rather than built.**
*(Next free number verified at source: no `P-038` token existed anywhere in the repo before this row.)*

**The question, per (subject, class):** does the register owe a **completeness check** — that every
slot is admitted by **at least one** syllabus chapter — and **at what point in the year is it read?**
**Additionally: report any slot admitted by EXACTLY ONE chapter**, as a single point of failure.

**Why it exists.** CD-138(e) makes admissibility a per-chapter declaration and gives the gate exactly
one job: check floors over the declared set, and FAIL on an item in a slot declared inadmissible.
**Nothing in that mechanism looks across chapters.** So a slot every chapter declares inadmissible —
each with a perfectly good one-line content reason — **fails nothing, and the paper it belongs to is
silently unfillable.** The gate is right at every chapter and wrong about the year.

**AMENDED 2026-08-16 by CD-147 — the S14 instance dissolves, the general question does not.**
S14 and S15 are now **paper-level for every chapter, categorically**, so S14 at C5 Bangla is
**zero-admitted BY RULE**. That is not the defect this row describes and needs no single-point-of-
failure report: nothing was lost when পাঠ ৪'s admission was reversed, because no chapter was ever
supposed to carry it. **The row's general question stands unchanged and stays RAISED** — nothing in
the suite checks that a slot which SHOULD be admitted by some chapter actually is, and the worked
example below should now be read on any slot other than S14/S15.

**It is no longer hypothetical (CD-139(f)).** At C5 Bangla, **S14 is admitted by exactly one chapter
— পাঠ ৪** — on নমুনা আবেদনপত্র (ছাপা ২৪), the সাত-অংশের ছক (২৫) and অনুশীলনী ২ ও ৪, with evidence
crops on disk. **Retire or exclude that one chapter and the slot has no chapter at all**, and no gate
in the suite would say so. **S15 at C5 stands at ZERO admitting chapters today** — declared, revisable
on evidence, and precisely the state this check would report.

**Blocked on:** **MarkLogic §৪'s syllabus split**, unread for this purpose (chain handoff §6 records
it UNRESOLVED). The check needs to know **what the year's chapter set IS** before it can say a slot is
unserved by all of it — and **a query's silence is evidence only if the query is known to be complete**
(`TOOLS-CR-005`). A completeness check built over an incomplete chapter list would report false
single-points-of-failure and, worse, false all-clears.

**Not proposed as a gate today, and the reason is the same one:** the obvious implementation — sweep
the banks on disk and count admitting chapters per slot — **measures the banks that exist, not the
syllabus**. At C5 Bangla today that would read S14 as zero-admitted, because পাঠ ৪ has no bank yet.

**Blocks:** nothing today. **Becomes owed** when the first full-year C5 Bangla paper is assembled
from chapter banks — the first moment the year, rather than the chapter, is the unit being checked.

---

## ⚑ PENDING-P-039 — four pushed banks predate teacher-lane step 5b and owe a retro review run

**Raised:** 2026-08-16, by the governance session that filed **CD-151**. **Status: RAISED.
Blocks nothing.** No bank is withdrawn, no promotion is affected, and nothing on disk changes on
account of this row.

**What is owed.** পাঠ **১৩ · ১৪ · ১৫ · ১৬** were authored and pushed before CD-151 existed. Each
owes **one run of `tools/bank_factual_review_prompt.md`**, from that path, with its facts block
filled from that chapter's own declaration and the source's ⚠ block.

**Why ১৬ is on the list even though it had a review.** পাঠ ১৬ is the session that invented the
step, and it ran the review twice — `VERDICT: 15 DEFECT(S)`, then `VERDICT: 1 REMAINING` after the
fixes. **The last remaining defect was then fixed and the gate suite re-passed, and the reviewer
was never re-run.** So the correction that closed ১৬'s review stands **unverified in the repo
today**: the gates that re-passed check STRUCTURE, and the thing under review was FACT. **A gate
re-run is not a review re-run**, and treating it as one is precisely the gap CD-151(b) exists to
close. ১৬'s state of record is therefore *reviewed, one defect outstanding, fix unverified* — not
clean.

**Why none of the four is re-run before the others, and why none was re-run at filing.** A retro
run under the **agent-composed prompt CD-151 retires** produces a verdict of unknown standing — it
would be the same artifact grading itself, in a different session. **All four are re-run once
against the vendored prompt, or the retro is not uniform**, and a partial retro is worse than
none: it would leave four banks in three different states of verification with nothing recording
which was which.

**What closes this row.** Four verdicts, one per bank, each from the vendored prompt and each
logged in `SESSION_LOG.md` with its verdict line. Any defect found is fixed **inside the teacher
lane** under CD-151(b), with the qid and the change logged. A defect needing a ruling or a change
outside the lane is CD-151(c) — stop and report, and this row stays open until that is resolved.

**Owner:** the next teacher-lane session that is not authoring a new chapter, or a session the
Principal directs to it. **Needed by:** before the first full-year C5 Bangla paper is assembled
from these banks — the same trigger `PENDING-P-038` names, because that is the first moment the
four are read together as a set rather than one at a time.
