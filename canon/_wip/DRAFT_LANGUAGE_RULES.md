# DRAFT — LANGUAGE_RULES.md (canon row 11) · NOT SLOTTED · awaiting Principal approval

Every rule below is traced to a slotted source. Rules I could **not** trace are listed as gaps
at the end rather than written in — an untraceable rule would be phantom canon (AGENTS.md §4).

---

## 1. Register — who the document is for decides the language

| Audience | Rule | Source |
|---|---|---|
| Teachers, students, parents (reader-facing) | Plain, everyday Bengali. No jargon, no English where a common Bengali word exists. | AGENTS.md §7 |
| Reader-facing files | No version history inside the document; history lives in Git and decision logs. | AGENTS.md §7 |
| Agent- and audit-facing files | May carry codes, tables and reason-codes; still written so a teacher can follow them. | canon/marklogic/MarkLogic_Rules.md §1 |

## 2. Numerals — the split rule

- **Bengali numerals (০–৯)** in everything a teacher or student reads: question papers,
  teaching templates, worksheets, notices.
- **English numerals (0–9)** in the mark-authority files, so marks can be cross-checked at a
  glance across subjects.

Source: stated identically at the head of every spine —
`canon/marklogic/MarkLogic_BAN_Spine.md`, `MarkLogic_ENG_Spine.md`, `MarkLogic_MATH_Spine.md`,
`MarkLogic_SCI_BGS_Spine.md`: *"মিলিয়ে দেখার সুবিধার জন্য এই ফাইলে নম্বর ইংরেজি অঙ্কে লেখা।
শিক্ষকদের টেমপ্লেটে বাংলা অঙ্কই থাকবে।"*

**Corollary:** a mark that appears in English numerals in student-facing output is an error,
and so is a mark in Bengali numerals inside a spine file.

## 3. Personal names — spelling is canon, not a matter of taste

- The **বাংলা column of `canon/names/REF-2_Content_Register.md` is authoritative** for any name
  in student-facing text. Roman spellings are a teacher aid; the **উৎস (source) column is
  teacher-facing only and never appears in student material.**
- Principal-confirmed house-style anchors: **উমর · উসমান · আয়েশা · ফাতিমা · যুবায়ের · যায়েদ · মুয়াজ**.
- The **ز sound is rendered য** (যুবায়ের, যয়নব, রাযিয়া), following those anchors.
- Two-word names are used in exactly five approved cases: **আবু বকর, আব্দুর রহমান, আবু উবায়দা,
  আবু হুরায়রা, উম্মে কুলসুম**. Everywhere else, one usable token.

Source: `canon/names/REF-2_Content_Register.md` §0. Cite it — do not restate the pool.

## 4. Replacing language without breaking the lesson

When REF-1 requires a word or passage to be replaced, four things survive the edit unchanged:
the **learning outcome**, the **required vocabulary** (the word must appear somewhere, any
position), the **Bloom's cognitive level**, and the **reading-difficulty level**.

Source: `canon/islamic-curation/REF-1_Curation_Policy.md` §4.2–§4.4. ⚠️ In force for **Class 1
Bangla and English only** until REF-1 v2.0 — see PENDING-P-001.

## 5. Bengali-language content the question papers assume

Papers test named Bengali-language machinery — যুক্তবর্ণ, কারচিহ্ন, ফলা ও রেফ, বিরামচিহ্ন,
ভাষারীতি/পদ, এক কথায় প্রকাশ, বিপরীত/সমার্থক শব্দ. These are skill items that recur across both
terms rather than chapter-bound items.

Source: `canon/marklogic/MarkLogic_QuestionPolicy.md` §skills-vs-chapters table.
This section is a pointer only; the authority stays in QuestionPolicy.

---

## Gaps — cannot be drafted from anything in this repo

**G-1 · Script guard for the Hub renderer.** The canon/language SLOT README names a rule —
"no Arabic script / emoji / em-dash / arrows in JSON strings — renderer constraint". Nothing in
the repo states it. `tools/hub-export/` is still an empty SLOT (Step 2), so the LOCKED import
contract v1.0 that would define the constraint is not here to check against.
**Needed:** the renderer/contract text, or the Principal's ruling stating the guard directly.

**G-2 · Bengali swarabritta rhyme spec.** The SLOT README says this is needed "if school-side
writing needs it". No source in repo, and no current workstream is writing verse.
**Recommendation:** drop it from canon for now; add it when a workstream actually needs it.

**G-3 · সাধু vs চলিত ruling.** `canon/marklogic/C5_Bangla_Source_13-23.md` flags lesson 20
(শিক্ষাগুরুর মর্যাদা) as সাধু ভাষা. Whether school-authored text may ever use সাধু, and how
সাধু source texts are handled in questions, is not ruled anywhere.
**Needed:** a Principal ruling, or confirmation that it is out of scope.
