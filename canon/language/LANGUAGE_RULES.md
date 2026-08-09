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

Source: `canon/islamic-curation/REF-1_Curation_Policy.md` §4.2–§4.4. ⚠️ In force for **Class 1
Bangla and English only** until REF-1 v2.0 — see PENDING-P-001.

## 6. Bengali-language machinery the papers assume

Papers test named Bengali-language items — যুক্তবর্ণ, কারচিহ্ন, ফলা ও রেফ, বিরামচিহ্ন,
ভাষারীতি/পদ, এক কথায় প্রকাশ, বিপরীত/সমার্থক শব্দ. These are skill items recurring across both
terms, not chapter-bound items.

Pointer only; the authority is `canon/marklogic/MarkLogic_QuestionPolicy.md`.

## 7. Not covered here

- **Hub renderer script guard** (constraints on JSON strings). This is a machine constraint on
  export, not a rule a teacher reads. It is **deferred to Step 2** and enters canon as its own
  CD row when the LOCKED import contract v1.0 is slotted at `tools/hub-export/`. Until then no
  script guard may be asserted as canon (CD-008).
- **Bengali swarabritta rhyme spec.** Out of scope — no workstream writes verse. If one does,
  it enters through a new CD row (CD-008).
