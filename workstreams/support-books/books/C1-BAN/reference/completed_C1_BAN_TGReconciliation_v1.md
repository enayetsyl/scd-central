# Class 1 Bangla — Teacher Guide ↔ Our-Analysis Reconciliation Report

**Doc type:** Source-validation / reconciliation — the TG↔skeleton verification artifact imported into Production per SETUP.md (D-019).
**Status:** Completed analysis. Imported and cleaned into Production; original archived in the source project. Pedagogical payload (§2 ledger codes/tags, §3 findings) is read-only per SETUP.md §1.2.
**Author:** Claude
**Output language:** English (staff-facing analysis); NCTB labels quoted in Bangla.

**Source validated against:** *NCTB "আমার বাংলা বই" Class 1 Teacher Guide, 2026 edition* (জাতীয় শিক্ষাক্রম ২০২১, পরিমার্জিত ২০২৫). 226 pp, image-only PDF; per-পাঠ যোগ্যতা/শিখনফল read by page rasterization + visual extraction (Bangla OCR unavailable; conservative reading).
**Our findings compared:** the C1-BAN curriculum skeleton (`completed_C1_BAN_Skeleton_v2.md`, the baseline).

---

## §0 — Executive summary & action checklist (read first)

**Headline verdict.** At the **lesson level, the analysis is complete and accurate** — all 54 পাঠ are in the skeleton, titles match the official সূচিপত্র exactly, and the decoding spine + teaching sequence verify against NCTB. The substance sits one level down, in the **per-lesson objectives (যোগ্যতা/শিখনফল)**, where the TG enriches what the skeleton held and corrects several genre tags.

**The three things that matter:**
1. **NCF Class 1 natively contains the free-thinking / self-discovery strand** (যোগ্যতা ৭.১, ৮.১, ১৬.২; method "একাকী চিন্তা"; পাঠ 53 = "সৃজনশীলতা বিকাশ"). The school mandate aligns with NCF intent here.
2. **Five C1 strands are present that a coarse reading would miss** — FREEWRITE, INFOTEXT, FUNCWRITE, POEM all have C1 rungs; and STORY is over-tagged (6 "থিমেটিক গল্প" lessons are really rhyme/poem/picture-composition/info). Real C1 stories are only পাঠ 9 and 46.
3. **The conjunct nuance is confirmed in the official codes** — *selected* যুক্তবর্ণ run through C1 যোগ্যতা ১.১/৫.১/৯.১/১৩.২ (hear/say/read/write) as whole units. This is consistent with this project's যুক্তবর্ণ rule B-1 (README §4.2 / D-009): a পাঠ may use only the whole-unit conjuncts its own NCTB পাঠ introduces, or none — systematic conjunct construction deferred to Class 2.

**The school additions are cleanly separated.** Every school addition (Islamic-transformation column, Muslim names, themes, avoid-list) is isolated in marked skeleton zones — none is mistaken for NCTB content.

### How this artifact is used now
This is a completed verification reference. Its payload is already merged into the C1-BAN skeleton (§3.1 codes + retagged genres), and the codes-count reconciliation against the skeleton passes (SETUP.md §1.4). The §2 ledger and §3 findings remain as the durable reference; §4 curation touchpoints feed live C-code decisions in the chapter loop (REF-1 taxonomy); §5 is retained as the analysis trail behind the genre retags. Nothing here is a pending cross-project action.

---

## §1 — Scope & method

The Teacher Guide is the authoritative per-lesson objective source NCTB issues alongside the textbook: its preface confirms every পাঠ carries **অর্জন-উপযোগী যোগ্যতা** (NCF competency codes), period-level **শিখনফল** (learning outcomes), **শিখন-শেখানো কার্যাবলি** (activities), **উপকরণ** (materials), and a per-lesson **মূল্যায়ন নির্দেশক** (assessment rubric). This reconciliation extracts the যোগ্যতা + শিখনফল + period count for all 54 পাঠ and sets them against the skeleton's lesson list.

**Confidence note.** Period counts come from the সূচিপত্র (TOC); per-পাঠ যোগ্যতা/শিখনফল from visual reading of rendered pages. The book uses an **inheritance structure** — vowel lessons (11–15) inherit পাঠ 10; consonant lessons inherit পাঠ 19; kar lessons follow পাঠ 21 — which the TG states explicitly, so inherited rows are marked rather than re-read. A 1-period discrepancy exists between the TOC total (**136**) and the per-পাঠ sum (**137**); immaterial, treated as a TOC transcription artifact.

### The NCF Class 1 Bangla যোগ্যতা framework (16 strands — the objective vocabulary)
`1.1` hear/identify letter + *selected-conjunct* sounds · `1.2` understand familiar words/sentences (listening) · `2.1` understand spoken questions/instructions · `3.1` comprehend picture/informational text + Q · `4.1` enjoy rhyme/poem/story (listening) · `5.1` pronounce letter/conjunct sounds · `5.2` speak words/sentences clearly · `6.1` Q&A / permission / request · `6.2` join simple conversation · `7.1` **describe in one's own way** + answer Q · `8.1` say words/sentences/lines + **express own feelings** · `9.1`/`9.2` read letters / conjunct-words / sentences · `10.1` read environmental/functional print · `11.1` read picture + number text · `12.1` read & comprehend & enjoy text · `13.1`/`13.2`/`13.3` write letters / words (letter-joining) / sentences (punctuation) · `14.3` fill a simple form (ছক) · `15.1` write short informational text · `16.2` **write in one's own way**.

---

## §2 — The 54-পাঠ reconciliation ledger

**Status key:** ✓ match (analysis correct) · ➕ TG-enrich (TG adds detail the skeleton lacked; no-শিখনফল noted) · ⚠ objective present that a coarse reading would miss · 🔁 retag (genre mis-classified). *"inh."* = inherits the cluster-leader's শিখনফল per the TG.

| পাঠ | Title (BN) | Per | যোগ্যতা | শিখনফল (period 1) | Skeleton type | Status |
|--:|---|:--:|---|---|---|:--:|
| 1 | আমার পরিচয় | 1 | 2.1, 6.1 | 2.1.2, 2.1.3, 6.1.2, 6.1.3 | পরিচয়/পরিচিতি | ✓ |
| 2 | এসো রং করি ও আঁকি | 2 | — | *none* — প্রাক-লিখন motor | অঙ্কন/রং | ➕ flag-colour (C-18) |
| 3 | আমি ও আমার বিদ্যালয় | 2 | 2.1, 6.1, 6.2 | 2.1.5, 2.1.3, 6.1.2, 6.1.3, 6.2.1 | পরিচয়/পরিচিতি | ✓ |
| 4 | আমি ও আমার সহপাঠীরা | 2 | 2.1, 6.1 | 2.1.2, 2.1.5, 6.1.2, 6.2.1 | পরিচয়/পরিচিতি | ✓ |
| 5 | আঁকাআঁকি | 1 | — | *none* — motor | অঙ্কন/রং | ➕ |
| 6 | আমরা কী কী করি | 2 | 2.1, 3.1, 5.2, 7.1 | 2.1.1, 3.1.1, 5.2.2, 7.1.1 | দৈনন্দিন কাজ | ⚠ 7.1 own-way; C-03/C-19 method |
| 7 | আঁকাআঁকি | 2 | — | *none* — motor → বর্ণ | অঙ্কন/রং | ➕ |
| 8 | ছড়া | 2 | 4.1, 8.1 | 4.1.1, 8.1.1, 8.1.4 | ছড়া | ✓ own-feelings |
| 9 | বাঘ ও রাখাল | 4 | 3.1, 4.1, 7.1, 8.1, 12.1 | 3.1.1, 7.1.2, 7.1.3, 12.1.4 | থিমেটিক গল্প | ✓ STORY |
| 10 | বর্ণ শিখি: অ আ | 2 | 1.1, 5.1, 9.1, 13.1 | 1.1.1, 5.1.1, 5.1.2, 5.1.4 | বর্ণ শিক্ষা | ✓ |
| 11 | বর্ণ শিখি: ই ঈ | 2 | inh. পাঠ 10 | inh. পাঠ 10 | বর্ণ শিক্ষা | ✓ |
| 12 | বর্ণ শিখি: উ ঊ | 2 | inh. পাঠ 10 | inh. পাঠ 10 | বর্ণ শিক্ষা | ✓ |
| 13 | বর্ণ শিখি: ঋ | 1 | inh. পাঠ 10 | inh. পাঠ 10 | বর্ণ শিক্ষা | ✓ |
| 14 | বর্ণ শিখি: এ ঐ | 2 | inh. পাঠ 10 | inh. পাঠ 10 | বর্ণ শিক্ষা | ✓ |
| 15 | বর্ণ শিখি: ও ঔ | 2 | inh. পাঠ 10 | inh. পাঠ 10 | বর্ণ শিক্ষা | ✓ |
| 16 | স্বরবর্ণ | 2 | 1.1, 5.1, 9.1, 13.1 | 1.1.1, 5.1.2, 9.1.1 | পুনরালোচনা | ✓ |
| 17 | ইতল বিতল | 2 | 4.1, 8.1 | 4.1.1, 8.1.1, 8.1.4 | ছড়া (ধ্বনিগত) | ✓ |
| 18 | কারচিহ্ন দেখি | 2 | — | *none* — matra concept-intro | কারচিহ্ন শিক্ষা | ➕ MATRA at C1 = concept-only |
| 19 | বর্ণ শিখি: ক খ গ ঘ ঙ | 5 | 1.1, 1.2, 5.1, 9.1, 13.1 | 1.1.2, 5.1.1, 5.1.4, 13.1.1 | বর্ণ শিক্ষা | ✓ |
| 20 | বর্ণ শিখি: চ ছ জ ঝ ঞ | 5 | inh. পাঠ 19 | inh. পাঠ 19 | বর্ণ শিক্ষা | ✓ |
| 21 | আ-কার শিখি | 1 | 1.1, 1.2, 5.1, 9.1, 13.1, 13.2 | 1.1.1, 1.2.2, 5.1.3, 9.1.3, 13.1.3, 13.2.1 | কারচিহ্ন শিক্ষা | ✓ (conjunct in 13.2) |
| 22 | ই-কার ঈ-কার শিখি | 2 | = পাঠ 21 | = পাঠ 21 | কারচিহ্ন শিক্ষা | ✓ |
| 23 | বর্ণ শিখি: ট ঠ ড ঢ ণ | 5 | inh. পাঠ 19 | inh. পাঠ 19 | বর্ণ শিক্ষা | ✓ |
| 24 | বর্ণ শিখি: ত থ দ ধ ন | 5 | inh. পাঠ 19 | inh. পাঠ 19 | বর্ণ শিক্ষা | ✓ |
| 25 | ট্রেন | 3 | 4.1, 8.1 | 4.1.1, 8.1.1, 8.1.4 | থিমেটিক গল্প | 🔁 STORY→RHYME (ছড়া) |
| 26 | বর্ণ শিখি: প ফ ব ভ ম | 5 | inh. পাঠ 19 | inh. পাঠ 19 | বর্ণ শিক্ষা | ✓ |
| 27 | উ-কার ঊ-কার শিখি | 2 | = পাঠ 21 | = পাঠ 21 | কারচিহ্ন শিক্ষা | ✓ |
| 28 | ঋ-কার শিখি | 1 | = পাঠ 21 | = পাঠ 21 | কারচিহ্ন শিক্ষা | ✓ |
| 29 | এ-কার ঐ-কার শিখি | 2 | = পাঠ 21 | = পাঠ 21 | কারচিহ্ন শিক্ষা | ✓ |
| 30 | বর্ণ শিখি: য র ল | 3 | inh. পাঠ 19 | inh. পাঠ 19 | বর্ণ শিক্ষা | ✓ |
| 31 | ও-কার ঔ-কার শিখি | 2 | = পাঠ 21 | = পাঠ 21 | কারচিহ্ন শিক্ষা | ✓ |
| 32 | বর্ণ শিখি: শ ষ স হ | 4 | inh. পাঠ 19 | inh. পাঠ 19 | বর্ণ শিক্ষা | ✓ |
| 33 | বর্ণ শিখি: ড় ঢ় য় ৎ | 4 | inh. পাঠ 19 | inh. পাঠ 19 | বর্ণ শিক্ষা | ✓ |
| 34 | বর্ণ শিখি: ং ঃ ঁ | 3 | inh. পাঠ 19 | inh. পাঠ 19 | বর্ণ শিক্ষা | ✓ |
| 35 | ছবি দেখি শব্দ বানাই | 1 | 1.2, 7.1, **16.2** | 1.2.1, 7.1.1, **16.2.1** | ছবি-ভিত্তিক রচনা | ⚠ FREEWRITE seed; method "একাকী চিন্তা" |
| 36 | এসো পড়ি ও লিখি | 2 | 1.2, 5.1, 9.1, **13.3** | 1.2.2, 5.2.2, 9.2.4, 13.3.1 | পঠন-লিখন | ✓ SENTENCE (small sentences) |
| 37 | এসো পড়ি ও লিখি | 2 | inh. পাঠ 36 | inh. পাঠ 36 | পঠন-লিখন | ✓ rubric rewards new-sentence attempt |
| 38 | এসো পড়ি ও লিখি | 2 | inh. পাঠ 36 | inh. পাঠ 36 | পঠন-লিখন | ✓ |
| 39 | ব্যঞ্জনবর্ণ | 1 | 1.1, 9.1, 13.1 | 1.1.2, 9.1.2, 13.1.2 | পুনরালোচনা | ✓ স্ব-মূল্যায়ন |
| 40 | মামার বাড়ি | 3 | 4.1, 8.1 | 4.1.1, 8.1.1, 8.1.4 | থিমেটিক গল্প | 🔁 STORY→RHYME (ছড়া) |
| 41 | তুলির ঘর | 3 | 1.2, 2.1, 5.2, **16.2** | 1.2.3, 2.1.1 (+ own-way write) | থিমেটিক গল্প | 🔁⚠ →picture-composition; 16.2 |
| 42 | ভোর হলো | 2 | 4.1, 8.1, 12.1, 13.3 | 4.1.2, 8.1.2, 8.1.5, 12.1.2, 13.3.2 | থিমেটিক গল্প | 🔁 STORY→POEM (কবিতা) |
| 43 | পড়ি ও লিখি | 3 | **11.1, 15.1** | 11.1.3, 15.1.3 | পঠন-লিখন | ⚠ INFOTEXT seed (read+write info) |
| 44 | যেতে যেতে পড়ি | 2 | **10.1** | 10.1.1, 10.1.2, 10.1.4, 10.1.5 | পঠন-লিখন | ⚠ FUNCWRITE (functional reading) |
| 45 | সাত দিনের কথা | 3 | 1.1, 1.2, 3.1, 5.1, 9.2, 12.1, 13.3, 16.2 | 1.1.4 (conjunct), 3.1.1 | থিমেটিক গল্প | 🔁⚠ →INFOTEXT; 16.2 |
| 46 | পিঁপড়া ও পায়রার গল্প | 4 | 8.1, 12.1, 16.2 | 8.1.5, 12.1.3, 12.1.5, 16.2.1 | থিমেটিক গল্প | ✓ STORY (real গল্প) |
| 47 | আজকের দিন | 2 | 1.2, 3.1, 5.2, 7.1, 9.2, 15.1 | 3.1.2, 7.1.3, 15.1.3 | থিমেটিক গল্প | 🔁⚠ →INFOTEXT (descriptive) |
| 48 | ছুটি | 4 | 4.1, 8.1, 12.1, 13.3 | 4.1.2, 8.1.2, 8.1.4, 8.1.5, 12.1.2 | থিমেটিক গল্প | 🔁 STORY→POEM (Tagore — curation) |
| 49 | আমাদের দেশ | 4 | 8.1, 12.1, 15.1 | 8.1.5, 12.1.3, 12.1.5, 15.1.3 | পরিচয়/পরিচিতি | ✓⚠ identity + INFOTEXT |
| 50 | মাছের রাজা | 2 | 3.1, 16.2 | 3.1.1, 3.1.2, 16.2 | থিমেটিক গল্প | 🔁⚠ →INFOTEXT (ইলিশ); C-05 image |
| 51 | সংখ্যা শিখি | 3 | 11.1, 16.2 | 11.1.1, 11.1.2, 16.2.1 | সংখ্যা শিক্ষা (আন্তঃবিষয়ক) | ✓ cross-curricular |
| 52 | আমাদের মুক্তিযুদ্ধ | 4 | 1.2, 2.1, 3.1, 5.2, 8.1, 12.1, 16.2 | 3.1.3, 8.1.5, 9.2.2 (conjunct), 12.1.3, 12.1.5 | মুক্তিযুদ্ধের ইতিহাস | ✓ **C-18 main instance** |
| 53 | শব্দ নিয়ে খেলা | 2 | — | *none* — "সৃজনশীলতা বিকাশ" (creativity) | শব্দ খেলা | ➕ free-thinking/creativity |
| 54 | আমার ঠিকানা | 1 | **14.3** | 14.3.1, 14.3.2 | পরিচয়/পরিচিতি | ⚠ FUNCWRITE (form-filling) |

**No-শিখনফল lessons (6):** 2, 5, 7 (pre-writing motor) · 18 (matra concept-bridge) · 53 (creativity). *All present in the skeleton (2/5/7/53 are easy to drop in a coarse merge — retained here).* **Period total:** 136 (TOC) / 137 (sum) — immaterial.

---

## §3 — Findings

**Lesson inventory — complete (✓).** All 54 পাঠ present in skeleton §3; titles match the TG সূচিপত্র one-for-one. The decoding spine, the inheritance structure, the review lessons, the real stories, the number and মুক্তিযুদ্ধ lessons all verify.

**TG enrichment we lack (➕).** Official per-পাঠ যোগ্যতা + শিখনফল codes (the skeleton has only aggregate outcomes); per-পাঠ period counts; per-পাঠ assessment rubrics (মূল্যায়ন নির্দেশক), one of which carries a *values/attitude* row.

**C1 strands present that a coarse reading would miss (⚠) — the substantive corrections.** Five strands the skeleton's aggregate outcomes obscured; the TG shows all five present at C1:
- **Free-writing / free-thinking** — যোগ্যতা ১৬.২ "নিজের মতো করে লিখি" (পাঠ 35, 41, 45, 46, 50, 51); oral ৭.১/৮.১ "নিজের মতো"/"নিজস্ব অনুভূতি" (পাঠ 6, 8, 9, 42, 47); method **"একাকী চিন্তা"**; and পাঠ 53 explicitly for **"সৃজনশীলতা বিকাশ."**
- **Informational text** — যোগ্যতা ৩.১ / ১১.১ / ১৫.১ (পাঠ 43, 45, 47, 49, 50, 52).
- **Functional writing** — ১০.১ functional reading (পাঠ 44) + ১৪.৩ form-filling (পাঠ 54).
- **Poem** (distinct from rhyme) — যোগ্যতা ১২.১ কবিতা (পাঠ 42, 48).
- **Conjuncts** — *selected* যুক্তবর্ণ in ১.১/৫.১/৯.১/১৩.২ and শিখনফল ১.১.৪/৯.২.২ — heard, said, read, **and written** at C1 as whole units.

**Type mis-classification (🔁).** Eight lessons the original skeleton filed as "থিমেটিক গল্প" are not prose stories: 25 & 40 are ছড়া (rhyme), 42 & 48 are কবিতা (poem), 41 is picture-composition, 45/47/50 are informational. Real C1 stories are only পাঠ 9 and 46. The retags are already applied in the skeleton (§3 / §3.1, marked "সংশোধিত v2").

**School additions — clean separation (no action).** The skeleton isolates all school-added material (the ইসলামি রূপান্তর column, §6.2 themes, §6.3 Muslim names, §6.4 avoid-list, §6.5 retain-list). Nothing school-added is conflated with NCTB-native content; the ledger's NCTB-native columns contain only TG-sourced data.

---

## §4 — Curation touchpoints surfaced (per-পাঠ, for the chapter loop)

These feed the per-পাঠ compliance map in the chapter loop; C-codes and their handling are governed by REF-1 (curation taxonomy), which is the final authority. Recorded here as advance notice, not as rulings:
- **C-18 (nationalist):** পাঠ 52 আমাদের মুক্তিযুদ্ধ is the one significant instance (4 periods, "১৯৭১..." narrative) — the C-18 factual-history carve-out (মুক্তিযুদ্ধ, civic facts) is retained per D-012; পাঠ 2 (flag-colouring) is minor; পাঠ 49/54 (country/address identity) benign.
- **C-03 / C-19:** পাঠ 6 recommends **গান গেয়ে শোনানো** (singing) and **অভিনয়** (role-play) as methods — candidates to convert to spoken / non-enacted; confirm against REF-1.
- **C-05:** পাঠ 50 uses an **ইলিশ মাছ** image — no-living-being / faceless image doctrine (D-010) applies.
- **Tagore:** পাঠ 48 ছুটি is a Tagore poem — a keep-or-replace curation call for the compliance map, not an auto-delete.
- **Anthem/flag:** under D-012, anthem front-matter and flag-focused content are omitted from support books entirely (students meet these in the NCTB book); mixed পাঠ keep their non-flag elements. This resolves the old "keep as constitutional" tension.

---

## §5 — Genre-map analysis trail (retained reasoning)

Retained as the reasoning behind the corrected genre tags now in the skeleton (§3 / §3.1). These are not pending actions; they record *why* each C1 type call was made, per-strand, so the retags can be audited against the TG.

**Free-writing / free-thinking (C1-present).** Own-way writing (যোগ্যতা ১৬.২; পাঠ 35/41/45/46/50/51) + oral own-way (৭.১/৮.১) + creativity (পাঠ 53). This is the strand the school mandate leans on; it originates at C1, not later.
**Informational text (C1-present).** যোগ্যতা ৩.১/১১.১/১৫.১; পাঠ 43/45/47/49/50/52.
**Functional writing (C1-present).** ১০.১ functional reading (পাঠ 44) + ১৪.৩ form-fill (পাঠ 54).
**Poem, distinct from rhyme (C1-present).** কবিতা যোগ্যতা ১২.১; পাঠ 42/48.
**Rhyme.** পাঠ 25 and 40 are ছড়া (were mis-filed as story).
**Story — narrowed.** Real prose stories are only পাঠ 9 and 46; the other "থিমেটিক গল্প" entries (25/40/42/45/47/48/50) are the retagged types above.
**Conjuncts.** *Selected* যুক্তবর্ণ present at C1 as whole units (যোগ্যতা ১.১/৫.১/৯.১/১৩.২; শিখনফল ১.১.৪/৯.২.২); systematic conjunct construction deferred to Class 2. Consistent with this project's rule B-1 (README §4.2 / D-009) — the validator's letter audit enforces it mechanically per book `letter_inventory`.
**Learner question-posing.** No explicit question-*posing* যোগ্যতা at C1 (own-way *answering* ≠ posing); oral own-way response seeds it from C1.

---

## §6 — Notes

- **Pilot scope:** this is a whole-book (54-পাঠ) reconciliation covering all of Class 1.
- **Conjunct policy alignment:** the "selected যুক্তবর্ণ as whole units" finding matches README §4.2 / D-009 (rule B-1); no conflict between this analysis and the project's taught-letter constraint.
- **Source file format:** the original skeleton was distributed as a mis-extensioned `.docx` that was actually markdown; the Production copy (`completed_C1_BAN_Skeleton_v2.md`) is true markdown.

---

## Version log
| Version | Date | Change | By |
|---|---|---|---|
| v1 | 2026-05-24 | Initial reconciliation. 54-পাঠ TG যোগ্যতা/শিখনফল/periods extracted (image-only TG, visual reading) and set against the skeleton. Lesson inventory = complete match; surfaced the five C1 strands (FREEWRITE/INFOTEXT/FUNCWRITE/POEM), STORY over-tagging, and the confirmed conjunct nuance. | Claude |
| — (cleaned) | 2026-07 | Imported into Production per SETUP.md (D-019): removed retired cross-project routing/staging/lock machinery (Project 00/01/02 flow, patch-list-for-review framing, supersede protocol) and foreign IDs with no D-series equivalent (REF-19 vertical map, REF-03 draft policy, source-project D-codes); re-pointed curation references to REF-1 / D-012 / D-010 and the conjunct finding to D-009 / README §4.2. Pedagogical payload (§2 ledger, §3 findings, genre tags) unchanged; codes-count reconciliation vs the skeleton passes. | Claude |
