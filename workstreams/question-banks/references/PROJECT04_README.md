# Project 04 — Question Bank Production · README

**Owner:** Principal
**Project:** 04 — Question Bank Production
**Status:** v1.8
**Scaffolded:** 2026-05-31 under REF-23 (Lean Project Scaffolding Standard); local seed D-PROJ04-001; creation logged in Project 00 as D-PROJ00-063
**Companion files:** `PROJECT04_TODO.md`, `PROJECT04_DECISIONS.md`, `/handoffs/`
**Canonical hub:** Project 00 — Curriculum Foundations (holds GLOSSARY, CROSS_PROJECT_INDEX, and all REFs; this Project keeps none of its own)

---

## 1. Context

Production home for chapter/topic-wise question banks across all classes (C1–C5) and all subjects — Bloom's-tagged, difficulty-graded, with answer keys and rubrics. Sole user: the Principal. Canonical references live in Project 00 and are consumed by pointer (§9).

## 2. What lives here

Per-(class × subject) question banks, organised per-topic, not per-chapter (D-028).

The Homework Question Pool that lesson/session plans link to by topic tag — master D-051 moved the Pool out of the lesson plan into Project 04 (supersedes D-029); produced and stored here (production file → master), governed by `LOCKED_QuestionBank_Production_Conventions_v1_2.md` (D-PROJ04-002 rulings; v1.1 per D-PROJ04-006 — canonical source for a question = the validated JSON payload; register retired per D-PROJ04-008, v1.2).

Answer keys and marking rubrics for every item.

The question data contract for the school software — `LOCKED_QuestionPayload_Schema_v1.json` and `LOCKED_StimulusPayload_Schema_v1.json` (shared passages); canonical source for a question = the validated JSON (D-PROJ04-004/006). The app imports the JSON, stores it in MongoDB, and serves teacher retrieval by topic-tag filter (D-PROJ04-008).

Weak-student practice sets — the bounded Pool top-ups Project 06 revision draws on (REF-07 §2.8, D-028 ≥20 floor).

`README.md`, `TODO.md`, `DECISIONS.md`, `/handoffs/` for this Project.

## 3. What does NOT live here (redirect)

Question-setting standards/methodology → Project 00 (REF-09 Tier 1, REF-10 Tier 2). Banks here comply; they don't redefine the standard.

Bloom's primers → Project 00 (REF-17/18/06). Stability analyses → Project 01. Curation policy → Project 02 (locked copy = REF-01).

Lesson plans → Project 03. Replacement content (stories/passages/examples) → Project 05.

Trackers, follow-up, parent comms → Project 06. Teacher training and supervised question-writing → Project 07.

If a request fits another Project, say so and ask before producing.

## 4. Standing conventions (inherited — lean)

Inherits master §5.5 (Light/Full handoff tiers), §5.12 (archived-files manifest), §5.13 (tool-use discipline), and §5.14 (cross-Project consult-routine) per D-047/D-048 and REF-23 (Lean Project Scaffolding Standard).

Filenames: master D-037 — `C{class}_{SUBJECT}_U{nn}[_L{mm}][_S{period}]_{Type}_v{ver}.{ext}`.

Draft vs Locked, propagation, handoffs: per master §5 (inherited above) — never restated locally.

Consult-routine (§4.8 = master §5.8 + §5.14): at the start of every chat, read this Project's README + TODO before responding, and briefly summarise the outstanding TODO items relevant to the chat's topic. When work is cross-cutting (changes expected in more than one Project), also read the relevant sections of each touched Project's README/TODO at task start (targeted reads per §5.13) — read-before-you-touch; no in-chat edits of other Projects' files.

## 5. Output language (master D-002)

Conventions, decisions, internal notes: English.

Question stems, options, keys, rubrics seen by students/teachers: Bangla (English subject excepted).

Bank-index column codes: English codes, Bangla labels.

## 6. Style (from the Principal)

Micro-management with clear stepwise instructions in every spec or process.

Student-facing items favour free thinking, application, and reasoning within an Islamic frame — not rote recall as default; Bloom spread follows the bank blueprint, never bottom-heavy.

Any teacher/staff-facing document (build spec, review checklist) carries a summary or checklist at the start or end.

Multi-file deliverables: one file at a time; for each file, ask prompt/spec or file. Inline text presents directly.

## 7. Islamic alignment

All question content aligns with Islamic values (Salafi framing, D-020). Apply REF-01 curation to every stem, option, name, and scenario before a bank is locked; self-check against the REF-21 trigger lexicon; draw personal names from REF-20 (matching class pool); for English, operative vocabulary = Core + Working + already-taught (REF-22), Receptive only inside a pre-taught/glossed passage. Canonical authority = REF-01; values statement = REF-12.

## 8. Build dependency (D-005)

Question banks are the last link: Stability Analysis → Annotated Skeleton → Replacement Content → Lesson Plans → Question Banks. A (class × subject) bank is built only after its upstream items are ready. Standing up this Project does not lift that gate.

## 9. Canonical references consumed (load per chat; not duplicated here)

REF-09 Tier 1 (mandatory floor) · REF-10 Tier 2 (enrichment/stretch) · REF-03 Subject Spine (relevant subject) · REF-05 stability analysis (relevant class × subject) · REF-18 V1C + REF-17 V1B Bloom (loaded; REF-06 V1A on demand) · REF-07 Revision (indirect — Pool/top-ups) · REF-01 Curation · REF-21 Trigger Lexicon · REF-20 Names Pool · REF-22 English Word-Bank · REF-13 GLOSSARY · REF-14 README · REF-15 TODO.

## 10. When in doubt

Wrong Project → say so, ask to redirect.

A convention conflicts with a specific ask → flag before proceeding.

Multi-file deliverable → §6.

Insufficient context → one focused question, don't guess.

## 11. Version log

| Version | Date | Change | By |
|---|---|---|---|
| v1.0 | 2026-05-31 | Initial scaffold under REF-23 (minimum file set + Part-4 inheritance line; conventions inherited by pointer, not restated; consumed REFs by pointer per INDEX). Local seed D-PROJ04-001; logged in Project 00 as D-PROJ00-063. | Claude (drafted); Principal (apply on confirm) |
| v1.1 | 2026-05-31 | Question-bank production conventions LOCKED (D-PROJ04-002) + master D-051 adopted (Pool moved out of the plan into Project 04, linked by topic tag). | Claude (drafted); Principal (apply on confirm) |
| v1.2 | 2026-06-09 | Question data-contract for the school software ratified (D-PROJ04-004, R-IMP5); canonical = JSON. | Claude (drafted); Principal (apply on confirm) |
| v1.3 | 2026-06-09 | Data-contract set LOCKED (D-PROJ04-005). | Claude (drafted); Principal (apply on confirm) |
| v1.4 | 2026-06-09 | Conventions §6 supersede executed (D-PROJ04-006); v1.0 archived; MANIFEST created. | Claude (drafted); Principal (apply on confirm) |
| v1.5 | 2026-06-16 | Chat-naming convention added (D-PROJ04-007, P04-local). | Claude (drafted); Principal (apply on confirm) |
| v1.6 | 2026-07-07 | **Register (TSV/Google Sheet) retired; retrieval moves into the school software / MongoDB (D-PROJ04-008).** README restructured to the Principal's 10-section layout (adds §6 Style, §10 When in doubt); §2 storage chain "production file → master → register" → "production file → master"; §2 data-contract bullet notes app-side topic-tag retrieval; conventions pointer moved to `LOCKED_QuestionBank_Production_Conventions_v1_2.md`. Master range unchanged (D-001–D-051). Cross-reference: `LOCKED_QuestionBank_Production_Conventions_v1_2.md`, `PROJECT04_DECISIONS.md` (D-PROJ04-008), `PROJECT04_TODO.md`, `PROJECT04_MANIFEST_archived_files.md` (row 2). | Claude (drafted); Principal (apply on confirm) |
| v1.7 | 2026-07-08 | **Currency only — 20 further banks LOCKED (D-PROJ04-009).** No structural change: banks are produced per-slice under the existing §2, and the roll-up is carried by DECISIONS/TODO. Version-log row records that the production frontier now spans C1/C2/C3 × BAN/MATH/SCI (seven lanes opened beyond C5 × BAN) and that per-lane master read-files are owed (TODO 4-D). Master range unchanged (D-001–D-051). Cross-reference: `PROJECT04_DECISIONS.md` v1.8 (D-PROJ04-009), `PROJECT04_TODO.md` v1.7. | Claude (drafted); Principal (apply on confirm) |
| v1.8 | 2026-07-08 | **Currency only — 23 further first-locks (D-PROJ04-010) + 3 bank supersedes (D-PROJ04-011/012/013).** No structural change. Records that the frontier now spans all of C1–C5 across BAN/MATH/SCI/BGS (eight further lanes opened at 010), and that the first bank-level archive cutovers occurred (MANIFEST rows 3–5): C5 BAN U15 v2, C5 BAN U13 v3 (with a Principal-authorised Conventions §3 QID-reuse exception), C4 BAN U14 v2. Master range unchanged (D-001–D-051). Cross-reference: `PROJECT04_DECISIONS.md` v1.9, `PROJECT04_TODO.md` v1.8, `PROJECT04_MANIFEST_archived_files.md` v1.3. | Claude (drafted); Principal (apply on confirm) |
