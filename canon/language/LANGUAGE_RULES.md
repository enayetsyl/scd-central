# LANGUAGE_RULES.md — canon

How the school writes. Every rule carries its source; cite this file or the source, and do not
copy either into a workstream file (AGENTS.md §8).

---

## 1. Register — who the document is for decides the language

| Audience | Rule | Source |
|---|---|---|
| Teachers, students, parents (reader-facing) | Plain, everyday Bengali. No jargon, no English where a common Bengali word exists. | AGENTS.md §7 |
| Reader-facing files | No version history inside the document; history lives in Git and decision logs. | AGENTS.md §7 |
| Agent- and audit-facing files | May carry codes, tables and reason-codes; still written so a teacher can follow them. | `canon/marklogic/MarkLogic_Rules.md` §1 |

## 2. Numerals — the split rule

- **Bengali numerals (০–৯)** in everything a teacher or student reads: question papers,
  teaching templates, worksheets, notices.
- **English numerals (0–9)** in the mark-authority files, so marks can be cross-checked at a
  glance across subjects.

Stated identically at the head of every spine — `canon/marklogic/MarkLogic_BAN_Spine.md`,
`MarkLogic_ENG_Spine.md`, `MarkLogic_MATH_Spine.md`, `MarkLogic_SCI_BGS_Spine.md`:
*"মিলিয়ে দেখার সুবিধার জন্য এই ফাইলে নম্বর ইংরেজি অঙ্কে লেখা। শিক্ষকদের টেমপ্লেটে বাংলা অঙ্কই থাকবে।"*

**Corollary:** a mark in English numerals in student-facing output is an error, and so is a
mark in Bengali numerals inside a spine file.

## 3. Personal names — spelling is canon, not a matter of taste

- The **বাংলা column of `canon/names/REF-2_Content_Register.md` is authoritative** for any name
  in student-facing text. Roman spellings are a teacher aid; the **উৎস (source) column is
  teacher-facing only and never appears in student material.**
- Principal-confirmed house-style anchors: **উমর · উসমান · আয়েশা · ফাতিমা · যুবায়ের · যায়েদ · মুয়াজ**.
- The **ز sound is rendered য** (যুবায়ের, যয়নব, রাযিয়া), following those anchors.
- Two-word names in exactly five approved cases: **আবু বকর, আব্দুর রহমান, আবু উবায়দা,
  আবু হুরায়রা, উম্মে কুলসুম**. Everywhere else, one usable token.

Source: `canon/names/REF-2_Content_Register.md` §0. Cite it — do not restate the pool.

## 4. সাধু and চলিত

- **School-authored text is always চলিত.** Every question paper, worksheet, lesson plan,
  notice and teaching template the school writes is in চলিত ভাষা.
- **সাধু source texts are quoted verbatim.** A সাধু passage from the textbook is reproduced
  exactly as printed — it is not modernised, paraphrased into চলিত, or silently smoothed.
- **Everything written *about* a সাধু text is in চলিত** — the question stem, the instruction,
  the mark scheme and the answer key, without exception. Only the quoted passage itself
  carries সাধু.

This is what lets a সাধু lesson be taught and examined without the paper drifting into সাধু.
Live case: `canon/marklogic/C5_Bangla_Source_13-23.md` lesson 20 (শিক্ষাগুরুর মর্যাদা), flagged
সাধু ভাষা. Basis: AGENTS.md §7 (plain accessible Bengali); Principal ruling CD-008.

## 5. Replacing language without breaking the lesson

When REF-1 requires a word or passage to be replaced, four things survive the edit unchanged:
the **learning outcome**, the **required vocabulary** (the word must appear somewhere, any
position), the **Bloom's cognitive level**, and the **reading-difficulty level**.

Source: `canon/islamic-curation/REF-1_Curation_Policy.md` §4.2–§4.4. In force **school-wide**
(CD-015) — all current classes, extending one class per year; the class list is read from
`canon/school-facts/SCHOOL_FACTS.md`.

## 6. Bengali-language machinery the papers assume

Papers test named Bengali-language items — যুক্তবর্ণ, কারচিহ্ন, ফলা ও রেফ, বিরামচিহ্ন,
ভাষারীতি/পদ, এক কথায় প্রকাশ, বিপরীত/সমার্থক শব্দ. These are skill items recurring across both
terms, not chapter-bound items.

Pointer only; the authority is `canon/marklogic/MarkLogic_QuestionPolicy.md`.

## 7. Script guard — what characters may appear in a string

Three tiers. **RED** = the artifact is rejected. **GREY** = reported, not rejected.
**WATCH** = counted and reported as a monitor only, never a failure.

| Tier | Characters | Rendered text fields (`text_bn`, `text_en`, titles) | Metadata fields |
|---|---|---|---|
| 1 | **Arabic script** | RED | RED |
| 2 | **Arrows, emoji, symbol glyphs** | RED | GREY |
| 3 | **Em-dash `—` and ellipsis `…`** | ALLOWED (WATCH counter) | ALLOWED |

### Tier 1 — a capability rule, not a doctrinal one

Arabic script is RED anywhere, in any string, for **every current workstream**.

The ground is **render capability**, not a judgement about Arabic. An unshaped Arabic string
tofus or breaks its joining in the Hub's PDF renderer, and that failure surfaces *after* gold
promotion — in a child's hand. The rule exists to stop that, and it lifts when the capability is
proven, not when someone argues it should.

A workstream may carry Arabic script in rendered fields only when **both** hold:

1. **Proven shaping.** Its full render path has passed an **executed** smoke test — real ayah
   text rendered and eyeball-verified: RTL correct, joining correct, no tofu — logged the way
   `tools/hub-export/SMOKE.md` is. Proven **per render path**, not once per repo: a new
   renderer, font or export route re-proves it.
2. **Verbatim quoted source only.** Every Arabic string is quoted source text carrying its
   provenance — mushaf or hadith reference in `source_note` — and is reviewed in the **আলিম
   lane**. Never model-composed. Never transliteration-round-tripped.

Until both hold, drafts use **Bangla + transliteration** with an **`ARABIC-SLOT`** placeholder
marking where the ayah will be inserted. This is the position for `islamic-studies` today.

Ruling: CD-014.

**Tier 2's split exists for a reason:** metadata fields (notes, compliance_note,
scene_description, style_profile, version_log) legitimately carry →, ⚠ and 🔒, so failing them
there would be a false positive. Rendered text is what a child sees; metadata is not.

**Tier 3 is a reversal of the earlier assumption.** Em-dash and ellipsis are permitted in
reader-facing text. The WATCH counter stays on **for one term** as a monitor, then the count is
reviewed and the counter either retired or promoted. (Term-end date comes from
`canon/school-facts/SCHOOL_FACTS.md` once the Principal completes it.)

### What the guard governs (CD-018)

**Strings that enter a mechanical render path.** Today that means Hub-bound JSON payloads and
support-book JSONs. It **extends automatically to any new path — a docx generator, a print
pipeline — the moment that path is vendored.**

**Human-read markdown is out of scope.** Canon files, teacher-facing tables and legend notation
(🔴 🟦 ★ ↑ ↓) are unaffected: editors and GitHub display them correctly, and there is no tofu
risk where no renderer runs.

**Each render path proves its own glyph set empirically.** A path's smoke test establishes what
actually survives it, and that result is recorded in that path's `SMOKE.md` — not assumed here.
If a glyph does not survive a path, the finding constrains the templates that feed that path;
it is **not** a change to this section.

Codepoint ranges, taken from the validator rather than restated from memory:

```
ARABIC  U+0600–06FF · U+0750–077F · U+FB50–FDFF · U+FE70–FEFF
ARROWS  U+2190–21FF · U+27F0–27FF · U+2900–297F
EMOJI   U+1F000–1FAFF · U+2600–27BF · U+2B00–2BFF · U+FE00–FE0F
```

⚠️ **Enforcement is authoring-side only.** The Hub import harness performs **no** charset check
— proven, not assumed (`tools/hub-export/SMOKE.md` test 3: an envelope carrying arrows, emoji,
em-dash and Arabic returns PASS). Nothing downstream will catch a violation, so the guard has to
hold where the content is written. Logged upstream at
`tools/hub-export/UPSTREAM_ISSUES.md` (UP-001).

Source: `validator_v2_rebuilt.py` check 8, verified scope; harness behaviour per
`tools/hub-export/SMOKE.md`. Ruling: CD-012.

## 8. Not covered here

- **Bengali swarabritta rhyme spec.** Out of scope — no workstream writes verse. If one does,
  it enters through a new CD row (CD-008).
