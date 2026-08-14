# REF-02 — Three-Layer Lesson Plan Template (Canonical)

**Status:** v1.6 — **approved & LOCKED 2026-05-31** (master **D-051** / D-PROJ00-064: the §2.8 Homework Question Pool field is **retired** — questions live in Project 04, linked to the plan by topic tag; Spine is now seven numbered fields + Session Map; supersedes **v1.5** → /archive/). *Earlier: v1.5 — **approved & LOCKED 2026-05-31*** (back-pointer footer added recording the Production-Core source dependency — D-PROJ00-062; **payload-neutral, no rule change**; supersedes **v1.4** → `/archive/`). *Earlier: v1.4 LOCKED 2026-05-31* (classroom-materials standard wider-scrub — D-PROJ00-057, Decision Review under Principal direction; the চক/স্লেট naming is removed and the standard restated positively; superseded **v1.3** → `/archive/`); canonical locked template `LOCKED_REF-02_Three_Layer_Lesson_Plan_Template_v1_5.md` per `PROJECT00_README.md` §5.3. *Earlier:* **v1.3 LOCKED 2026-05-28** (master **D-050** / D-PROJ00-040; materials fold master **D-049** / D-PROJ00-039; v1.2 → `/archive/`). *v1.3 re-homes the three-layer model across **two plan types** (adopts master **D-050**): **Layer 1 Spine = chapter scope (Chapter Plan)**; **Layers 2–3 Lesson Flow + Flex Zone = period scope (Session Plan)**. Adds **§2.9 Session Map** and a new **§2A** (Chapter↔Session mechanics: reference rule, single-period collapse, session-count rule, IDs). Folds the **classroom-materials standard (D-049, restated positively per D-PROJ00-057)** — the only permitted teaching surface is a whiteboard with a marker; the only permitted pupil tools are খাতা/পেনসিল/কলম; any other surface or tool fails the materials gate. Terminology locked 2026-05-28: **Chapter** (Bangla: the book's division word, e.g. পাঠ/অধ্যায়) and **Session** (Bangla: পিরিয়ড); "lesson plan" is retained only as the informal family term. Full v1.0/v1.1/v1.2 history in §9.*
**Project:** 00 — Curriculum Foundations
**Date created:** 2026-05-20 (v1.0); 2026-05-20 (v1.1 same day)
**Owner:** Principal
**Author:** Claude (drafted); Principal (approval pending)
**Source decisions:** D-004 (Three-Layer model), D-005 (build dependency order), D-020 (Salafi framing), **D-050 (multi-period Chapter Plan + Session Plans; session-count rule)**, **D-049 (classroom-materials standard)**, plus Project 03 architecture decisions Q-A through Q-H (handoff §7 of `PROJECT00_handoff_2026-05-20_project02_to_ref02.md`), plus REF-02-chat additions Q1–Q4 (Principal direction 2026-05-20: time-based homework with guideline count; 2–4 hour Daily Homework Budget for Class 1; 20-question minimum Pool; inline Pool placement).
**Companion documents:**
- `PROJECT00_GLOSSARY.md` — canonical definitions of Spine / Lesson Flow / Flex Zone / Three-Layer Lesson Plan / Revision Anchor / Example Bank / Discovery Pattern / Homework Question Pool / **Classroom-Materials Standard** (Chapter Plan / Session Plan terms enter the GLOSSARY with this lock).
- `Bloom_Taxonomy_Comprehensive_Primer_Teachers_V1A.docx` (REF-06) — canonical Bloom's reference; §3.6 supplies class-band distribution; §6 supplies per-subject expression; Chapter 2 supplies verb lists.
- `PROJECT02_README.md` — Curation Policy categories C-01 through C-19 (current count; **REF-01 is authoritative — read C-{N} from REF-01 §4.1, never assume a fixed count here**), and cross-Project propagation flags F-01 / F-02 / F-03 / F-04.
- **REF-12 (School Mission and Islamic Values Reference, LOCKED v1.0)** — `LOCKED_REF-12_School_Mission_and_Islamic_Values_Reference_v1_0.md`. The upstream values charter §2.5 invokes via the positive replacement test (REF-12 §11) and as the background constraint for every lesson. REF-12 = *why / values*; REF-01 = *what to replace and how*; REF-21 = *how to find triggers*.
- `PROJECT00_README.md` — initiative architecture; §5.3 governs Draft vs Locked.
- REF-07 (Revision Architecture, to be produced Day 5) — operational specifics for how §2.6 Revision Anchors aggregate into a school-wide revision spiral.
- REF-08 (Homework Architecture, to be produced Day 6) — authoritative figures for §2.7 time budgets and guideline counts per class per subject; Daily Homework Budget governance.

---

## Quick-Navigation Checklist (staff-facing)

> **v1.3 in one line:** the three-layer model now spans **two plan types** — a chapter-scope **Chapter Plan** (Layer 1 Spine + the §2.9 Session Map) and one period-scope **Session Plan** per teaching period (Layers 2–3). A single-period chapter collapses to one standalone Session Plan. See §1 and §2A.

- [§1 — The model in one minute: three layers across two plan types](#1-the-three-layer-model--summary)
- [§2 — Chapter Plan: Layer 1 Spine at chapter scope (seven fields + Session Map)](#2-layer-1--spine-non-negotiable)
  - §2.1 Learning Objective · §2.2 Must-Cover Content · §2.3 Bloom's-Level Distribution · §2.4 Exit-Check · §2.5 Islamic-Alignment Note · §2.6 Revision Anchor · §2.7 Homework Specification · **§2.9 Session Map** *(former §2.8 Homework Question Pool retired — D-051)*
- [§2A — How a Chapter Plan and its Session Plans fit together](#2a-how-a-chapter-plan-and-its-session-plans-fit-together)
  - §2A.1 Reference rule · §2A.2 Single-period collapse · §2A.3 Session-count rule · §2A.4 IDs & filenames
- [§3 — Session Plan: Layer 2 Lesson Flow, the 35-minute reference (MANDATORY / FLEXIBLE)](#3-layer-2--lesson-flow-reference)
- [§4 — Session Plan: Layer 3 Flex Zone — what teachers may and may not change](#4-layer-3--flex-zone-teachers-choice)
  - §4.1 May decide · §4.2 May not decide · §4.3 Pedagogical posture · §4.4 Example Bank · §4.5 Discovery Pattern Suggestions
- [§5 — Embedded Replacement Content convention](#5-embedded-replacement-content-convention)
- [§6 — Review-and-Grading Criteria (Chapter Plan + Session Plan)](#6-review-and-grading-criteria)
- [§7 — Before-Publishing Checklist (Chapter-Plan + Session-Plan)](#7-before-publishing-checklist)
- [§8 — Worked Example: single-period case + multi-period case](#8-worked-example)
- [§9 — Version Log, Ownership, Cross-Project Consumers](#9-version-log--ownership)

---

## Purpose & Scope

This template defines the canonical form of every lesson plan produced under this initiative, regardless of class, subject, or unit. It is the structural authority that Project 03 (Lesson Plan Production) lesson plan files must conform to.

**Two plan types (v1.3, master D-050).** Most chapters past Class 1 run over several periods, so the three-layer model is split along its natural seam: **Layer 1 (Spine) is planned once at *chapter* scope (the Chapter Plan)**, and **Layers 2–3 (Lesson Flow + Flex Zone) are authored per *period* (one Session Plan each)**. A multi-period chapter = one Chapter Plan + N Session Plans; a **single-period chapter collapses** to one standalone Session Plan that inlines the Spine (the v1.2 single-file form, structurally unchanged). The Session Plan **references** the Chapter Plan and never re-derives Spine facts — see §2A. "Lesson plan" is kept only as the informal family name for the pair; precise references say *Chapter Plan* or *Session Plan*.

It does **not** contain subject-specific content. Subject-specific specialization — what vocabulary to mandate for Bangla, what procedures for Math, what ayat/hadith for Islamic Studies, etc. — lives in **Subject Spine Playbooks** (REF-03 onward), one per subject, also in Project 00.

This template solves the failure mode D-004 was designed for: fully-scripted plans remove teacher dynamism; loose plans erode standards. The Three-Layer model fixes both ends by separating *what must happen* (Spine, non-negotiable; Lesson Flow MANDATORY rituals) from *one way it could happen* (Lesson Flow FLEXIBLE segments) from *how the teacher actually runs the room* (Flex Zone, teacher's choice within the Example Bank and Discovery Pattern Suggestions).

v1.1 extends v1.0 in three structural directions: **systematic revision** (every lesson chains backward and forward via §2.6 Revision Anchor, integrating with REF-07); **bounded homework** (every lesson declares its homework spec via §2.7 and provides a pre-prepared Bloom's-tagged Pool via §2.8, integrating with REF-08); and **teacher scaffolding** (§4.4 Example Bank and §4.5 Discovery Pattern Suggestions give new teachers a pre-prepared inventory to pick from instead of having to invent on the fly).

---

## 1. The Three-Layer Model — Summary

The three layers are unchanged in substance; v1.3 only changes **where each is authored**. Layer 1 is a property of the whole chapter; Layers 2–3 are properties of a single period. So the three layers are homed across two plan types:

| Layer | Name | Authored in | Reviewable? | What it contains |
|---|---|---|---|---|
| 1 | **Spine** | **Chapter Plan** (chapter scope) | Yes — every field must be present and well-formed | Seven non-negotiable fields (§2.1–§2.7) **+ the §2.9 Session Map** (§2.8 retired — D-051); the core of what the chapter is |
| 2 | **Lesson Flow** | **Session Plan** (period scope) | Mandatory rituals are checked; flexible segments are not graded | A 35-minute scaffold per period, each segment annotated **MANDATORY presence** or **FLEXIBLE form/timing** |
| 3 | **Flex Zone** | **Session Plan** (period scope) | No — evaluated indirectly via whether Spine outcomes landed | Teacher's choice of examples (§4.4 Example Bank), discovery patterns (§4.5), sequencing, pacing |

**The two plan types.**

- **Chapter Plan** — one per chapter (the book's numbered division, `U{nn}`). Holds Layer 1 (the seven Spine fields planned at chapter scope) plus the **§2.9 Session Map** that breaks the chapter into its sessions. Built **first**, at the chapter-planning gate, where the session count is also set (§2A.3).
- **Session Plan** — one per teaching period (`_L{mm}`). Holds Layers 2–3 plus a thin header that **references** the Chapter Plan and carries that period's objective and must-cover slice (§3.0). Built **after** the Chapter Plan.
- **Single-period chapter** → one standalone Session Plan that inlines the Spine; no separate Chapter Plan (§2A.2).

**Reading rule.** A **Chapter Plan** is complete and compliant iff:

1. Every Spine field (§2.1–§2.7) is present and well-formed at chapter scope.
2. The §2.9 Session Map is present, with one row per session (session # · focus · objective · must-cover slice · exit-check · homework slice).
3. The session count was set at the chapter-planning gate and is within the §2A.3 band (or carries a logged reason / Subject-Lead approval).

A **Session Plan** is complete and compliant iff:

4. It carries the §3.0 reference line (Chapter Plan ID + session number) and re-derives **no** Spine fact.
5. Every MANDATORY Lesson Flow segment (Opening, Hook, Exit-Check, Closing) is present.
6. The §4.4 Example Bank provides minimum 3 examples per teaching point, and §4.5 provides minimum 3 discovery patterns.
7. Alignment holds with REF-01 (Islamic Curation Policy), the relevant Subject Spine Playbook (REF-03 onward), REF-06 (Bloom's V1A), REF-08 homework conventions, and the **D-049 classroom-materials standard** (whiteboard + marker only; খাতা/পেনসিল/কলম only — any other surface/tool fails the materials gate).

(A standalone single-period Session Plan is checked against both lists — it carries the Spine inline instead of a reference line.)

Lesson Flow timing (minute-by-minute) and Flex Zone choices (which specific example, which discovery pattern) are not graded for compliance. They exist to support the teacher, not to be audited.

---

## 2. Layer 1 — Spine (Non-Negotiable) — *the Chapter Plan*

The Spine is the seven-numbered, six-conceptual-field core of every chapter, **planned once at chapter scope in the Chapter Plan** and never re-derived in the Session Plans. (The former eighth field, §2.8 Homework Question Pool, is retired — D-051 — its questions live in Project 04, linked to the plan by topic tag.) v1.3 adds **§2.9 Session Map**, the Chapter-Plan field that breaks the chapter into its sessions.

> **Scope-reading convention (v1.3).** Each §2.x field below is authored **at chapter scope**. Where the field text written for v1.2 says "the lesson" or "this 35-minute lesson," read it as **"the chapter"** — the field describes the whole chapter, and each session draws its **slice** via the §2.9 Session Map. The only field that is genuinely period-level is the Bloom's progression note in §2.3 (it climbs across sessions rather than being one fixed per-period mix). In a **single-period chapter**, chapter scope and session scope coincide: "the lesson" = the one session, and these fields are filled inline in the standalone Session Plan (§2A.2).

Together these fields answer: *what will the student be able to do by the end of this chapter that they could not at the start; how will the teacher know; how does this chapter connect to what came before and after; what homework anchors it; how is it split into periods; and how does it respect Islamic values?*

### 2.1 Learning Objective

**Definition.** One sentence, observable, beginning with an action verb drawn from the Bloom's level chosen in §2.3.

**Format.** `Students will [verb from Bloom's level] [content] [under what conditions if relevant].`

**Good example.** "Students will identify and pronounce the Bangla vowels অ, আ, ই, ঈ when shown each letter card."

**Bad example.** "Students will learn about vowels." (Verb "learn" is not observable; "about vowels" is unbounded.)

**Rules.**

1. Exactly one verb. No "and-also" objectives stacked together — if you need two verbs, the lesson should be split.
2. The verb must match the Bloom's level in §2.3. ("Identify" is Remember/Understand; "explain why" is Understand/Analyze; "design" is Create.) The verb lists in V1A Chapter 2 (Remember §2.1, Understand §2.2, Apply §2.3, Analyze §2.4, Evaluate §2.5, Create §2.6) are the authoritative source.
3. **The verb must be observable.** A child shows it by doing, saying, writing, drawing, pointing, demonstrating with materials, or otherwise producing a verifiable artifact or behavior the teacher can directly confirm in the room.

**Observable verb modes — examples:**

| Mode | Sample verbs | What the teacher confirms |
|---|---|---|
| Oral | Say, recite, name, pronounce, explain, describe, summarize | Hearing the response |
| Written | Write, list, label, fill in, describe in writing | Reading the notebook (খাতা) |
| Graphic | Draw, point to, circle, mark, underline, match by line | Seeing the artifact |
| Physical/manipulative | Show, demonstrate, classify objects, sort, arrange, build | Watching the action |
| Produced artifact | Construct, design, create, compose | Examining the finished product |

### 2.2 Must-Cover Content

**Definition.** The specific content elements the lesson must cover before it can be marked complete. This field is generic at the universal-template level; its concrete form is specialized per Subject Spine Playbook (REF-03 onward).

**Form by subject** (indicative; authoritative form lives in each subject's REF-03+ playbook):

| Subject | What "Must-Cover Content" looks like |
|---|---|
| Bangla (BAN), English (ENG), Arabic (ARB) | Vocabulary words, grammar elements, reading passage elements, pronunciation items |
| Mathematics (MATH) | Concepts, procedures, formulas, fact families |
| Science (SCI) | Concepts, processes, key observable facts, simple investigations |
| Islamic Studies (ISL) | Ayat (with sura and ayah reference), hadith (with grading and source), concepts, adab items |
| Bangladesh & Global Studies (BGS) | Facts, places, dates, civic concepts, local-context terms |
| ICT | Tools, procedures, safety rules, terms |

**Rules.**

1. The list must be finite and bounded — not "everything about X."
2. Each item must be derivable from the Universal Core of the relevant stability analysis (REF-05) when one exists, or from current NCTB content when one does not. Items added explicitly for Islamic alignment under REF-01 are tagged `[Islamic-add]`.
3. Items listed here are the **minimum** for lesson completion. The Flex Zone may add elaboration but cannot subtract from this list.
4. F-01 systematic exclusions apply: no Western personal names, no Western foods, no Western clothing in any item or example (per `PROJECT02_DECISIONS.md` D-PROJ02-005 / F-01).
5. **Minimum may be raised over time.** When student capability grows — signaled by Class Test Tracker results, Master Tracker aggregates, or principal observation showing consistent over-performance — the Principal updates the relevant Subject Spine Playbook (REF-03+) with a higher minimum. Affected lesson plans are then re-generated to a new version against the updated playbook (not edited in place; LOCKED file discipline). Lowering the minimum requires explicit Principal approval and a documented reason in the relevant Project 03 DECISIONS file. The Spine field §2.2 is a **list**, not a number — capability growth manifests as a longer list (more items mandatory), not a higher threshold.

### 2.3 Bloom's-Level Distribution

**Definition.** The mix of cognitive levels (Remember, Understand, Apply, Analyze, Evaluate, Create) the lesson targets, expressed as the dominant level(s) and a rough share of lesson time at each.

**Reference — indicative class-band Bloom distributions (REF-06 §3.6, active scope):**

| Level | Class 1–2 | Class 3–5 |
|---|---|---|
| Remember | 35–45% | 20–30% |
| Understand | 30–40% | 25–35% |
| Apply | 15–25% | 25–35% |
| Analyze | 0–10% | 10–20% |
| Evaluate | 0–5% | 0–10% |
| Create | 0–5% | 0–10% |

The Class 3–5 column reflects the natural climb: Remember declines as Apply / Analyze / Evaluate / Create rise. (The table is a **convenience copy** of REF-06 §3.6 for the initiative's active class range. REF-06 §3.6 remains the authoritative source — if the two ever diverge, REF-06 wins; the Bangla and English Subject Spine Playbooks deliberately point to REF-06 rather than re-print, so this column is the only second copy.)

*(Indicative bands for Class 6–8 and 9–10 also live in REF-06 §3.6 and will be inlined when those classes enter the initiative's scope. Exact mark distributions remain to be set in Tier 1 and Tier 2 question-setting guidelines.)*

A single 35-minute lesson does not need to touch every level. It must declare which levels it targets and roughly how much time at each.

- Plans targeting only Remember are permitted at Class 1 only with explicit justification (e.g., first-introduction letter recognition).
- Plans targeting only Evaluate at Class 1 are **not** permitted (out of band).
- Plans for older classes follow the band for that class group.

**Format.** A single line or small table:
`Dominant: Remember (60%), Understand (30%). Exposure: Apply (10%).`

**Rules.**

1. The verb in §2.1 must come from one of the declared levels.
2. The exit-check in §2.4 must be at one of the declared levels.
3. Verb choice and example calibration follow V1A Chapter 2 verb lists and V1A §6 per-subject expression guidance.

### 2.4 Exit-Check

**Definition.** One observable check, taking 2–5 minutes, that determines whether the lesson's Learning Objective was met for each student.

**Format.** A specific question, task, or observation the teacher runs at the close of the 35-minute lesson.

**Examples by subject:**

- *Bangla letter recognition* — "Show the letter card for আ. Each student points to it on their desk chart."
- *Math addition* — "Solve 2 + 3 in your খাতা (notebook). Show me."
- *Islamic Studies adab* — "Tell your partner one adab when entering home, then both partners say it to the teacher."
- *Science observation* — "Look at the two plants on my desk. Say which one has been in sunlight and how you know."

**Rules.**

1. The exit-check must be at the same Bloom's level as the Learning Objective.
2. The exit-check is the **scope of formative questions** the lesson plan may include (per Project 03 architecture Q-F). A lesson plan may include 3–5 formative questions leading up to and including the exit-check. **Summative questions live in Project 04 (Question Banks), not here.**
3. The exit-check must produce a **per-student readout** — the teacher must be able to tell, for each individual student, whether the objective landed. Whole-class chorus checks do not satisfy this; circulate, observe individuals, or take individual responses. **Per-student readout ≠ one question per student:** a 12-pupil class gets **12 readouts of the *same* check** (the teacher confirms each child), not 12 different questions — a shared check keeps readouts comparable across pupils and classes. A small set of **2–4 variants** is used only to deter copying in a *written* check.
4. If the exit-check would not show whether the objective landed, the plan is incomplete.
5. **Exit-check failure handling.** Two cases:
   - **Partial failure (< 30% of students fail).** The lesson is marked complete. Failing student(s) are recorded in the Lesson Completion Tracker (Project 06). Standard follow-up sequence: **(a)** failing students appear in the next lesson's §2.6 Revision Anchor as a targeted revisit; **(b)** the next homework or weekly assignment includes a targeted item on the missed objective; **(c)** if the same student fails the same type of objective across **3 or more lessons**, flag for individual attention (catch-up session, parent inform, etc., per Project 06 follow-up rules).
   - **Systemic failure (30% or more of students fail).** The lesson itself is suspected misdesigned. The teacher does **not** re-teach to the whole class immediately; instead, the teacher escalates to the Subject Lead / Principal and the lesson plan is reviewed for revision before being run with another class. Re-teaching to the same class is decided after revision.
6. **Exit-Check Bank (parallel to the §4.4 Example Bank).** Every lesson plan provides a small ready inventory of exit-check forms — **minimum 2 per objective type** — so a teacher who cannot devise a check has a ready form to pick from and run as a per-student readout (rule 3). The Bank's *form adapts per subject*; the subject-specific exit-check forms live in the relevant Subject Spine Playbook (REF-03 onward — e.g. **REF-03 §3.6** for Bangla).

### 2.5 Islamic-Alignment Note

**Definition.** An explicit declaration of how this lesson aligns with the Islamic Curation Policy (REF-01) and the school's mission and values charter (**REF-12**). This is the field where the school's Salafi framing (D-020) lands operationally in the lesson plan. **The relationship is layered:** REF-12 names the values (the *why*); REF-01 turns them into the C-category replacement rules (the *what to replace and how*) — currently **C-01 through C-19**, but the count grows; **REF-01 §4.1 is authoritative**, never any in-template number; REF-21 is the trigger-detection layer (the *how to find*). §2.5 invokes all three: the C-category posture (below) comes from REF-01, and the **positive replacement test (REF-12 §11)** governs the substantive quality of any replacement.

**Required content.** One of the following annotations, with justification:

- **KEEP-AS-IS** — the lesson does not touch any current REF-01 C-category; standard NCTB content is acceptable as published. *Justification:* brief statement of why no category applies.
- **NEEDS-REPLACEMENT** — the lesson touches one or more REF-01 C-categories; replacement content is required. *Justification:* which category triggered the flag, which D-PROJ02 decision (if any) governs the replacement choice, and the `RC-{SUBJECT}-C{class}-U{unit}-L{lesson}` reference ID for the replacement content embedded per §5.
- **FLEXIBLE** — the lesson is acceptable as-is but may optionally be enhanced with Islamic framing. *Justification:* brief statement of the optional enhancement available.

**Cross-Project propagation flags (always apply, regardless of annotation):**

- **F-01.** Replace Western personal names, foods, and clothing in any student-facing element — *every time*. Names come from **REF-20 Approved Names Pool** (matching class pool); foods → local/halal substitutes; clothing → modest local dress. Applies systematically — even KEEP-AS-IS lessons must verify F-01 holds. (C-10 scope.)
- **F-02.** Bengali devotional poetry with tariqah lineages → scope under **C-15** (form preserved, content replaced). Tariqah orders, rituals, or hierarchies → scope under **C-17** (full content replaced).
- **F-03.** Nationalism-over-ummah content (C-18; high-frequency at Class 1, e.g. Liberation War / Language Movement). Remove flag salutes, flowers/wreaths at the Shaheed Minar or other monuments, ritual silence, and any nation-over-ummah framing. Teach the factual history plainly, reframed with ummah-priority. Borderline civic acts (e.g. standing for an anthem vs. saluting a flag) carry the REF-01 OPEN-02 caveat — escalate to the Principal rather than deciding alone.
- **F-04.** Role-play / dramatization / impersonation (C-19) — a **method-level** flag, easily missed on a theme-scan. Bar any task asking a pupil to *pretend to be* a fictional or other character; **never** enact prophets or sahaba. **Allow** genuine real-exchange practice between pupils as themselves (a real salaam, a real Q&A), pairing same-gender per C-02. Don't skip an "act it out as X" instruction just because the surrounding theme is wholesome.

**Curation Policy categories — reference list.** The REF-01 C-categories (currently C-01 through C-19; the count grows over time). **REF-01 §4.1 is the authoritative source** for each category's definition and stance; if the count or any definition changes, REF-01 wins. Project 03 Instructions §10 duplicates the current list at-hand for the lesson-plan author (Q-H / D-PROJ03-007) — that duplication is a convenience copy of REF-01, regenerated when REF-01 updates, not the source of truth. REF-21 (Curation Trigger Lexicon) supplies the how-to-find layer once locked.

**Rules.**

1. This field cannot be empty. Every lesson plan declares its alignment posture explicitly.
2. If NEEDS-REPLACEMENT, the inline replacement content per §5 is mandatory; a lesson plan with a NEEDS-REPLACEMENT note but no inline RC block is incomplete.
3. If the lesson plan author is uncertain whether a category applies, tag the lesson `[CURATION-REVIEW-PENDING]`; the lesson is not approved until the Principal or designated reviewer resolves it. Scholarly-disagreement cases route through the Curation Policy disagreement register (`PROJECT02_README.md` §11.2).
4. Salafi framing (D-020): when an NCTB element reflects general Bangladeshi Sunni-Hanafi-Sufi cultural Islam (mawlid/milad celebrations, urs and saint veneration, grave-related practices beyond authentic ziyarah, music in Islamic context, tawassul through deceased, bid'ah presented as Islamic norm), the lesson is flagged under the applicable C-category and NEEDS-REPLACEMENT applies.
5. **Positive replacement test (REF-12 §11).** When the posture is **NEEDS-REPLACEMENT**, the inline replacement (per §5) must do more than avoid the prohibited — it must **positively reflect** at least one Islamic value drawn from REF-12 §5–§7: Islamic family life, an authenticated prophetic narration, adab/akhlaq, the *signs of Allah* in nature (āyāt), or halal occupations. *Replacing the prohibited with a neutral filler does not satisfy this rule;* the replacement is the school's chance to teach a positive Islamic value in the same slot. The plan author confirms this in the §7 checklist; the reviewer confirms it in §6. A KEEP-AS-IS or FLEXIBLE lesson is not required to *positively* reflect a value (since nothing is being inserted), but it must still not contradict one — the global REF-12 §11 values-alignment items (tawhid frame, Islamic register, modesty, character-over-marks, adab) are background constraints for any lesson.

### 2.6 Revision Anchor

**Definition.** Every lesson chains backward (what does it build on, what gets revisited inside it) and forward (what items from this lesson get scheduled for future revision). The Revision Anchor field encodes those chains.

The Revision Anchor is the integration point between the lesson plan and the school-wide Revision Architecture (REF-07, to be produced Day 5). Operational specifics — how revision tracker entries aggregate, how weekly assignments select revision items, how monthly cumulative revision is scheduled — live in REF-07. The Revision Anchor lives here so every lesson plan provides the raw input that REF-07's machinery consumes.

**Three components:**

#### 2.6.a Builds-On (prior lessons)

Explicit list of prior lesson references this lesson depends on.

**Format.** Bulleted list of `C{class}_{SUBJECT}_U{unit}_L{lesson}` references, with one line per reference indicating what the dependency is.

**Example.**
- `C1_BAN_U1_L1` — letter introduction concept (this lesson assumes students have encountered the idea of a Bangla letter)
- `C1_BAN_U1_L2` — letter-sound correspondence (this lesson assumes students can match a letter shape to its name aurally)

**Rules.**

1. First lesson of a unit may have empty Builds-On if no prior lesson is in scope.
2. Builds-On references must be lessons within the same subject (within-subject dependency). Cross-subject dependencies (e.g., a Bangla lesson that builds on an Islamic Studies concept) are documented in the Lesson Plan but live structurally in §2.5 Islamic-Alignment Note, not here.
3. If a prior lesson has been re-versioned since this lesson was drafted, the reference is updated to the current version when this lesson is regenerated.

#### 2.6.b Revisited-In-This-Lesson

What specific content from prior lessons gets revisited inside this lesson (typically during the Hook segment, but could be elsewhere).

**Format.** Bulleted list. Each item names the content revisited and the source lesson reference.

**Example.**
- Letter আ recognition (from `C1_BAN_U1_L2`) — revisited via Hook flashcard warm-up
- Letter অ sound (from `C1_BAN_U1_L2`) — revisited via roll-call response

**Rules.**

1. Every Builds-On reference should produce at least one Revisited-In-This-Lesson entry (otherwise the dependency is invisible to the student).
2. Revisited items should each have at least one matching question in the topic's Project 04 Pool (selected at homework time).
3. Revisited items appear in the §3 Lesson Flow at the segment specified (typically the Hook).

#### 2.6.c Future-Revisit-Candidates

Items from this lesson's must-cover content (§2.2) that should appear in future revision, with suggested cadence.

**Format.** Table or bulleted list. Each item lists: the content item, the suggested next-revisit cadence, and the suggested revisit medium.

| Item | Suggested next revisit | Medium |
|---|---|---|
| (each must-cover item) | next lesson / this week's homework / this week's weekly assignment / next month / pre-exam revision | in-class hook / homework / class test / cumulative revision day |

**Rules.**

1. Every must-cover content item from §2.2 should appear in at least one Future-Revisit-Candidate slot.
2. The cadence suggestions are inputs to REF-07's machinery; REF-07 may override (e.g., if a student-cohort tracker shows mastery already, REF-07 may skip the next-lesson revisit).
3. "Pre-exam revision" cadence is appropriate only for items the school explicitly expects on the term exam.

### 2.7 Homework Specification

**Definition.** What homework, if any, this lesson assigns. Bounded by per-lesson time budget; questions selected from the topic's Project 04 Pool (register/master) — the former inline §2.8 Pool is retired (D-051).

This field integrates with REF-08 (Homework Architecture, Day 6). The figures below are the **pilot defaults for Class 1 pending REF-08 lock**; REF-08 will set authoritative per-class-per-subject figures.

**Fields:**

| Field | Class 1 pilot default | Notes |
|---|---|---|
| **Time budget per session** | 20 minutes for a single homework session covering this lesson | Firm cap. Source of truth: REF-08 once locked. |
| **Guideline question count** | 5–10 questions to assign from the topic's Project 04 Pool | Operational lever — adjust based on question type and student capability. |
| **Bloom's distribution of homework** | Aligned with §2.3 but Remember/Understand-heavy (homework lacks teacher scaffolding) | For Class 1 specifically: Remember ~50–60%, Understand ~30–40%, Apply ~5–15%, higher levels 0%. |
| **Traceability rule** | Each homework item traces to (a) current lesson's must-cover content (§2.2), OR (b) a §2.6 Revision Anchor item | The mechanism that makes revision homework explicit. |

**Rules.**

1. The time budget is the firm cap. Question count is the operational lever for the teacher.
2. Daily total homework time across all subjects is bounded by the school-level **Daily Homework Budget** (lives authoritatively in REF-08; currently set at **2–4 hours total daily for Class 1** per Principal direction 2026-05-20).
3. If the per-lesson time budget would push a student's daily total over the Daily Homework Budget, the teacher reduces the question count for this homework, or skips homework for this lesson. The reduction is logged in the Homework Tracker (Project 06).
4. **Zero homework is permitted.** Some lessons may not warrant homework (e.g., assessment-day lessons, lessons immediately before a holiday, lessons that already include extensive Independent Practice).
5. If §2.7 declares zero homework, the topic's Project 04 Pool is still available as a source for revision homework on later days.
6. Homework questions must satisfy F-01 and the Curation Policy, same as any other student-facing material.

### 2.8 Homework Question Pool — RETIRED (master D-051, 2026-05-31; supersedes D-029)

The Homework Question Pool is **no longer a lesson-plan field.** Questions live in **Project 04** — canonical production file → per-(class × subject) master → register (in Drive); ID `QP-{SUBJECT}-C{class}-U{nn}` (chapter scope; ≥20, default 30/topic per Project 04 conventions 4-A). **The plan carries no Pool — no inline copy, no reference block.** A plan and its questions are linked only by the **topic tag** (`TOP-…`) the Spine declares (§2.2 / the §2.9 Session Map). The teacher reads the topic tag → filters the Project 04 register/master → selects `Y` (the §2.7 time band and D-030 count-is-the-lever rule are unchanged). The §2.9 "homework slice" names the **topic + count**, not inline questions.

### 2.9 Session Map *(Chapter Plan only)*

**Definition.** The backbone of the Chapter Plan: the table that breaks the chapter into its teaching periods (**sessions**) and, for each, names what that session does. It is the bridge between the chapter-scope Spine above and the period-scope Session Plans that follow. **A single-period chapter has no Session Map** (chapter and session coincide — see §2A.2).

**Form.** One row per session, set at the chapter-planning gate (§2A.3):

| Session | Focus | Session objective | Must-cover slice (from §2.2) | Exit-check (from §2.4 Bank) | Homework slice (topic + count; from the Project 04 register) |
|---|---|---|---|---|---|
| `_L01` | (one-line focus) | (one objective drawn from the §2.1 chapter objective set) | (the §2.2 items this session covers) | (which §2.4 Bank form this session runs) | (topic + how many, selected from the Project 04 register) |
| `_L02` | … | … | … | … | … |
| … | | | | | |

**Rules.**

1. **Coverage.** Every §2.2 must-cover item appears in exactly one session's must-cover slice (no item unassigned, no item duplicated as "new" — re-teaching for revision is a §2.6 within-chapter revisit, not a second coverage).
2. **One objective per session.** Each session draws one objective from the §2.1 chapter objective set; a session needing two objectives is a sign the chapter is under-sessioned (revisit the session count, §2A.3).
3. **Bloom climb.** Read top-to-bottom, the session objectives should trace the §2.3 chapter Bloom progression (early sessions Remember/Understand, later sessions Apply/Analyze as the class-band allows) — not every session at the chapter's peak level.
4. **Within-chapter revision.** Where a session revisits an earlier session in the same chapter, that is recorded in §2.6 (within-chapter strand), and the revisit shows in the later Session Plan's Hook.
5. **The Session Map is the authority for what each Session Plan carries.** A Session Plan copies its objective and must-cover slice *from* its Session Map row by reference (§2A.1); it does not invent them.
6. **Session count is fixed here.** The number of rows = the session count set at the chapter-planning gate (§2A.3). Adding or removing a session after Session Plans exist is a Chapter-Plan revision (new version), not an in-place edit.

---

## 2A. How a Chapter Plan and its Session Plans fit together

*(New in v1.3, master D-050. This section is the operational contract between the two plan types.)*

### 2A.1 Reference rule — *reference, never restate*

A Session Plan **references** the Chapter Plan and re-derives nothing from the Spine. Its header (§3.0) names the Chapter Plan ID and the session number; its objective and must-cover slice are **copied from the §2.9 Session Map row**, not re-authored. If a Spine fact changes, it changes in the **Chapter Plan only**, and the Session Plans inherit it on regeneration. This is what makes a 14-session chapter maintainable: one source of truth, N thin period files. ("A teacher with one chapter source beats a teacher reconciling fourteen.")

### 2A.2 Single-period collapse

A chapter that the session-count rule (§2A.3) resolves to **one** period produces **one standalone Session Plan that inlines the Spine** — the v1.2 single-file form, structurally unchanged. No separate Chapter Plan is built, and there is no §2.9 Session Map. The standalone Session Plan therefore carries the seven Spine fields (filled inline) **and** Layers 2–3. It is checked against both reading-rule lists in §1.

### 2A.3 Session-count rule *(the chapter-planning gate)*

Set the session count **once, at chapter-planning, before any Session Plan is built:**

1. **Baseline = the TG Reconciliation period count** for that chapter (`completed_C{n}_{SUBJ}_TGReconciliation_v{ver}.md`, the D-042 gate output).
2. **Production band = ±40%, or ±1 session, whichever is larger** (rounded to whole sessions). *Worked: TG says 5 → 40% = 2 → band 3–7. TG says 2 → 40% = 0.8 → ±1 wins → band 1–3.*
3. **Within band:** the chapter author may adjust freely, recording **a one-line reason** in the Chapter Plan.
4. **Beyond band:** requires a **Subject-Lead decision**, recorded as a Chapter-Plan revision (with reason).
5. **Deferred to a later REF-02 revision:** *structural* school-vs-TG pacing divergence (whether the school should hold a slower honest pace vs honor the TG count) — out of scope for v1.3; the band above governs ordinary variance only.

The resulting count = the number of §2.9 Session Map rows.

### 2A.4 IDs & filenames *(D-037 ripple)*

The `U{nn}` division-anchor token is unchanged (= the chapter). The `_L{mm}` token is **kept but redefined** as the **session index** (period within the chapter) — the letter `L` is retained for filename continuity, exactly as `U` was kept though it no longer means "unit."

| Artifact | Filename pattern |
|---|---|
| Chapter Plan | `C{class}_{SUBJ}_U{nn}_ChapterPlan_v{n}.md` |
| Session Plan (multi-period chapter) | `C{class}_{SUBJ}_U{nn}_L{mm}_SessionPlan_v{n}.md` |
| Standalone Session Plan (single-period chapter) | `C{class}_{SUBJ}_U{nn}_SessionPlan_v{n}.md` *(no `_L` when there is one session)* |

(Pool and replacement-content IDs — `QP-…`, `RC-…` — keep the `U{unit}-L{lesson}` shape, now read as `U{chapter}-L{session}`.)

---

## 3. Layer 2 — Lesson Flow (Reference) — *the Session Plan*

### 3.0 The Session Plan header *(what sits above Layers 2–3)*

Every Session Plan opens with a **thin header** and then carries Layers 2–3. The header **references** the Chapter Plan (§2A.1) and re-derives no Spine fact:

- **Reference line** — `Chapter Plan: C{class}_{SUBJ}_U{nn}_ChapterPlan_v{n} · Session _L{mm} of {N}`.
- **This-session objective** — copied verbatim from the §2.9 Session Map row.
- **This-session must-cover slice** — copied from the same row.
- **This-session exit-check** — the §2.4 Bank form named in the row.
- **This-session homework slice** — the topic + count named in the row (questions from the Project 04 register).
- **Materials (D-049):** teacher = whiteboard + marker (the only permitted teaching surface); students = খাতা/পেনসিল/কলম only — any other surface or tool fails the materials gate.

Then: **§3 Lesson Flow** (below) and **§4 Flex Zone**. A **standalone single-period Session Plan** (§2A.2) replaces the reference line with the full inline Spine (§2.1–§2.7) and has no Session Map.

### 3.1–3.4 Lesson Flow

The Lesson Flow is a 35-minute scaffold. **It is renamed from "Suggested Flow" in v1.1** because v1.0's "Suggested" understated the mandatory rituals embedded in some segments. Each segment now carries one of two annotations:

- **MANDATORY presence** — the segment must appear in the lesson plan and in classroom delivery. Its specific content (the named rituals below) is fixed.
- **FLEXIBLE form/timing** — the segment must be planned for (presence assumed), but the lesson plan author and the classroom teacher have wide latitude over its form, length, and exact methods.

Reviewers check MANDATORY segments for presence (per §6). They do not audit FLEXIBLE segment timing or method.

### Structural template

| Minutes | Segment | Annotation | Purpose | Content |
|---|---|---|---|---|
| 0–3 | **Opening (সূচনা)** | **MANDATORY** | Settle the room; signal start; invoke Allah's name and blessing on learning | See §3.1 below |
| 3–8 | **Hook (আকর্ষণ)** | **MANDATORY presence** (form flexible) | Connect to prior lesson or to lived experience; engage attention | See §3.2 below |
| 8–18 | **Direct Instruction (পাঠ প্রদান)** | FLEXIBLE form/timing | Introduce the must-cover content from §2.2 | Teacher exposition, visual aid, modeling, demonstration |
| 18–25 | **Guided Practice (পরিচালিত অনুশীলন)** | FLEXIBLE form/timing | Students try the new content with teacher support | Whole-class then pair work; teacher circulates |
| 25–30 | **Independent Practice (স্বাধীন অনুশীলন)** | FLEXIBLE form/timing | Each student attempts alone | খাতা (notebook) work, oral round, short writing task |
| 30–33 | **Exit-Check (নির্গমন পরীক্ষা)** | **MANDATORY** | Run the check from §2.4; identify struggling students | The §2.4 check, executed |
| 33–35 | **Closing (সমাপ্তি)** | **MANDATORY** | Close the lesson properly; secure materials; invoke gratitude | See §3.3 below |

### 3.1 Opening — MANDATORY content

The Opening segment includes the following specific elements, in this order:

1. **Teacher enters and says Assalamu alaikum wa rahmatullah.** Teacher waits for and ensures all students reply (wa alaikum assalam wa rahmatullah). Reply by every student is part of the ritual; the teacher does not proceed until reply is received.
2. **Class discipline check.** Teacher reminds (briefly, not lecturing): hand-raise rule before speaking; permission rule before leaving seat; materials handling rule — students keep only what the teacher has directed open (**খাতা notebook, পেনসিল pencil, কলম pen** — the only permitted pupil tools per the D-049 materials standard; any other tool fails the gate); everything else goes in the bag.
3. **Bismillah ar-Rahman ar-Raheem.** Said collectively.
4. **Rabbi zidni 'ilma** (رَبِّ زِدْنِي عِلْمًا). Said collectively.
5. *(Other school-standard du'a — deliberately left open for future v1.x. The school may codify additional opening du'a in a later revision of this template per Principal direction 2026-05-20.)*

**Notes.**

- Attendance is **not** part of the Opening. Attendance is handled separately (Homework/Lesson Completion Tracker captures presence; the formal attendance taking happens at the school-administrative level, not in the lesson Opening).
- A teacher running an emergency catch-up session may compress steps 3–5 but cannot skip steps 1–2.
- Subject-specific Opening enhancements (e.g., recitation of a short Surah before an Islamic Studies lesson) live in the relevant Subject Spine Playbook (REF-03+), not here.

### 3.2 Hook — MANDATORY presence, FLEXIBLE form

The Hook is mandatory because it is the lesson's attention-grab and the natural place to perform the §2.6 Revisited-In-This-Lesson content. A lesson without a Hook starts cold and loses the revision integration point.

**Form options (teacher's choice from §4.5 Discovery Pattern Suggestions or own invention):**

- Question-led — teacher asks an open question.
- Object-led — teacher brings a real object related to the lesson.
- Story-led — teacher tells a brief story (Islamic-aligned per Curation Policy).
- Flashcard-led — quick recall of prior letters / words / facts (natural fit for §2.6 revisit).
- Picture-led — teacher shows a picture and asks students what they see.

**Rules.**

1. Hook presence is mandatory; Hook form is the teacher's choice from §4.5 or own invention.
2. The Hook segment is the **default location for §2.6 Revisited-In-This-Lesson content**. If the lesson plan places revisit elsewhere, the lesson plan must say so explicitly.
3. New teachers and probationary teachers default to the lesson plan's specified Hook form; experienced teachers may substitute per §4.2 sequencing rule.

### 3.3 Closing — MANDATORY content

The Closing segment includes the following specific elements, in this order:

1. **One-line takeaway.** Teacher states the lesson's takeaway in one sentence: *"আজ আমরা … শিখলাম।"* / "Today we learned …"
2. **Homework page note** (if §2.7 declares non-zero homework). Teacher tells students which questions (selected from the topic's Project 04 Pool) the homework comprises and which page/notebook to do them in. *(Students still have their notebook and pen in hand at this point — that is by design; see Notes.)*
3. **Materials-to-bag check.** Teacher directs students to put materials in their bag (খাতা notebooks, পেনসিল pencils, কলম pens, books — only the permitted pupil tools per the D-049 standard). Teacher visually confirms each student's desk is clear.
4. **Alhamdulillah.** Said collectively.
5. **Teacher says Assalamu alaikum wa rahmatullah** before leaving the room. Teacher waits for and ensures all students reply.

**Notes.**

- **Order rationale (v1.3, 2026-05-28).** Materials-to-bag is intentionally **step 3**, not step 1: the takeaway (step 1) and the homework note (step 2) both require students to *write* — the homework note specifically tells them which page/notebook to record. If notebooks and pens went into the bag at step 1, students could not record the homework. Bagging happens once writing is complete.
- A teacher running an emergency catch-up session may compress step 2 (homework note) but cannot skip steps 1, 3, 4, 5.
- The Closing Salam (step 5) is symmetrically paired with the Opening Salam (step 1). Both are MANDATORY.
- Subject-specific Closing enhancements (e.g., a brief reminder about Quran homework before Islamic Studies lesson ends) live in the relevant Subject Spine Playbook (REF-03+), not here.

### 3.4 Rules across the Lesson Flow

1. The Lesson Flow's **timing** (minute-by-minute) is FLEXIBLE except where MANDATORY segments are concerned. Reviewers do not check that the teacher used these exact minutes in these exact ways.
2. The Lesson Flow exists to remind authors and teachers that 35 minutes is the operational window. If the must-cover content cannot fit, the lesson should be **split**, not stretched.
3. Subject-specific adaptations of the FLEXIBLE segments live in REF-03 onward. For example, Bangla letter-recognition lessons typically need more time at Hook; Math procedural lessons typically extend Independent Practice; Science observation lessons typically extend Direct Instruction with a demonstration.
4. MANDATORY rituals (§3.1 Opening, §3.3 Closing, Hook presence, Exit-Check) are the same across all subjects. Subject-specific *enhancements* to MANDATORY rituals (e.g., specific Du'a before Quran lesson) belong in the Subject Spine Playbook.

---

## 4. Layer 3 — Flex Zone (Teacher's Choice) — *the Session Plan*

The Flex Zone is where the teacher's professional judgment lives, supported by the §4.4 Example Bank and §4.5 Discovery Pattern Suggestions. Like Layer 2, it is authored **per session**; the Example Bank and Discovery patterns are scoped to *this session's* must-cover slice (from the §2.9 Session Map row), not the whole chapter.

### 4.1 What the teacher MAY decide

- **Examples used.** Which concrete examples illustrate the must-cover content. **See §4.4 Example Bank for the lesson plan's pre-prepared example inventory** — new teachers default to picking from the bank; experienced teachers may invent (provided F-01 and the Curation Policy hold).
- **Sequencing within segments.** Whether to split Independent Practice into two short bursts; whether to interleave Direct Instruction and Guided Practice for a back-and-forth feel. (Hook ↔ Direct Instruction order is constrained — see §4.2 rule.)
- **Pacing within the 35 minutes.** Whether to spend 12 minutes on Direct Instruction and 5 on Guided, or the inverse — as long as MANDATORY segments fit and the Exit-Check still happens within the 35-minute window.
- **Elaboration depth.** How much to say about a single must-cover item; whether to dwell on a misconception that surfaced in the room.
- **Discovery patterns.** Which discovery-oriented teaching pattern fits the lesson. **See §4.5 Discovery Pattern Suggestions for the lesson plan's pre-prepared pattern inventory** — same default-versus-substitute rule as Example Bank.

### 4.2 What the teacher MAY NOT decide

- **Whether to cover the must-cover content from §2.2.** Every item on that list is mandatory.
- **The Learning Objective (§2.1).** The objective is fixed by the lesson plan author.
- **The exit-check method (§2.4).** Same for all teachers running this lesson, so per-student readouts remain comparable.
- **The Islamic-alignment posture (§2.5).** A lesson marked NEEDS-REPLACEMENT cannot be taught as KEEP-AS-IS in the room.
- **The MANDATORY Lesson Flow segments (§3.1, §3.2, §3.3).** Opening rituals, Hook presence, Exit-Check, Closing rituals are all non-skippable.
- **Hook-then-Direct-Instruction default sequence.** Reversal (Direct Instruction first, Hook later or omitted in form) is permitted only for teachers with demonstrated reliable student engagement. **New teachers and teachers in their probationary period follow the default sequence without exception.** "Demonstrated engagement" is determined through classroom observation (Project 07 scope).
- **The §2.7 Homework time budget cap.** Teacher may reduce homework but cannot exceed the cap.
- **The Project 04 Pool's Bloom's tagging.** Teacher cannot reclassify a question's Bloom's level (the tagging is canonical for tracker analysis; the Pool is a Project 04 artifact — D-051).

### 4.3 Pedagogical posture for the Flex Zone

(This subsection operationalizes the Principal's standing style preference — free thinking, self-discovery, independent problem-solving — within an Islamic framework.)

- **Spines stay outcome-neutral.** They specify the *what*, not the *how*. The Spine never says "use the discovery method"; it says "the student will identify and pronounce the Bangla vowels."
- **Lesson Flow MANDATORY segments are procedural, not pedagogical.** They specify rituals (Salam, Bismillah, materials-to-bag) and structural pivots (Hook, Exit-Check), not teaching methods.
- **Lesson Flow FLEXIBLE segments can be neutral or discovery-oriented.** It depends on what fits the 35-minute window for the specific lesson.
- **Flex Zones lean discovery-oriented.** The teacher's elaboration, examples, and pacing should default to inviting student thinking ("এই অক্ষরটি কোন শব্দে আছে?" / "Where else have you heard this word?") rather than telling. §4.5 Discovery Pattern Suggestions provide the patterns.
- **All discovery happens within Islamic framing.** When a student's hypothesis or example diverges from Islamic values (e.g., a student volunteers a musical jingle as a memory aid, or names a Western pop figure as an example), the teacher redirects to an Islamic-compatible alternative without shaming the student. Redirection patterns are developed in REF-03 and in teacher training (Project 07).

### 4.4 Example Bank

**Definition.** A pre-prepared example inventory for each teaching point in §2.2 Must-Cover Content. The teacher's fallback when they cannot or do not wish to invent their own example.

**Rules.**

1. Per teaching point in §2.2, **minimum 3 acceptable examples**.
2. All examples comply with F-01 (no Western names, foods, clothing) and the Curation Policy.
3. Examples are concrete, age-appropriate, and tied to the teaching point.
4. Teacher may substitute with their own example provided F-01 and Curation Policy hold; substitutions are logged in the relevant tracker for Subject Lead visibility.
5. The Example Bank format adapts per subject (per Subject Spine Playbook REF-03+):
   - Bangla/English/Arabic — words or phrases.
   - Math — concrete numerical examples, real-life problem situations.
   - Science — observable phenomena, demonstrable processes.
   - Islamic Studies — ayat, hadith, prophetic narrations, adab scenarios.
   - BGS — local places, Bangladeshi facts, civic scenarios.
   - ICT — tools, procedures, screen-shot-able examples.

### 4.5 Discovery Pattern Suggestions

**Definition.** A pre-prepared inventory of discovery-oriented teaching patterns for the lesson. The teacher's fallback when they want a discovery approach but don't have one in mind.

**Rules.**

1. **Minimum 3 patterns per lesson.** Symmetric with §4.4 Example Bank minimum.
2. Patterns are described concretely enough that a new teacher can run them without further explanation.
3. Subject-specific canonical pattern libraries live in REF-03+ Subject Spine Playbooks.
4. Teacher may substitute or invent provided F-01 and Curation Policy hold.

**Pattern types** (lesson plans may draw from these or invent new ones):

| Pattern | Description | Typical fit |
|---|---|---|
| Question-led | Teacher asks open question; students hypothesize before content is introduced | Hook segment; any subject |
| Demonstration-then-question | Teacher shows; students hypothesize what they saw; teacher then explains | Science observations, Math examples |
| Paired-exploration | Students discuss in pairs before whole-class share | Comprehension, problem-solving |
| Object-led | Teacher brings real object; students examine and hypothesize | Hook for any subject; Science |
| Story-led | Teacher tells a brief story; students predict next or identify lesson | Bangla, English, Islamic Studies, BGS |
| Comparison-led | Teacher presents two examples; students find the difference | Any subject; pattern recognition |
| Sorting-led | Teacher provides a mixed set; students classify | Bangla letter-sound, Science, Math, Islamic Studies adab |

---

## 5. Embedded Replacement Content Convention

*(Implements Project 03 architecture Q-G: replacement content inline, with reference ID for traceability. Unchanged from v1.0.)*

### Convention

When a lesson is marked **NEEDS-REPLACEMENT** in §2.5, the lesson plan file includes the **full replacement content inline** — story, poem, example, or other — at the point in the Lesson Flow where it is used. The replacement content is also cross-referenced to its canonical source in Project 05 by reference ID.

### Reference ID format

`RC-{SUBJECT}-C{class}-U{unit}-L{lesson}`

Example: `RC-BAN-C1-U2-L4` is the canonical replacement content used in Class 1 Bangla, Unit 2, Lesson 4.

If a single lesson uses more than one replacement content piece (rare; typical lesson uses zero or one), append a piece index: `RC-BAN-C1-U2-L4-a`, `RC-BAN-C1-U2-L4-b`.

### Inline block format

```
> **Replacement content — RC-BAN-C1-U2-L4**
> _Replaces NCTB content under C-05 (depictions of living beings) per REF-01 / D-PROJ02-002 (faceless figures rule)._
>
> [full story / poem / example text in Bangla — the actual content the teacher reads, shows, or distributes]
```

### Rules

1. The full replacement content lives in the lesson plan inline. A teacher with the lesson plan in hand should not need to open a second file to teach. ("A teacher with one document beats a teacher with two." — Project 03 Q-G.)
2. The canonical source remains the Project 05 file under the same ID. If Project 05 updates the canonical version, lesson plans referencing the ID are **re-generated**, not edited in place (per D-005 dependency order and LOCKED file discipline, `PROJECT00_README.md` §5.3).
3. The block declares which Curation Policy category triggered the replacement and which D-PROJ02 decision (if any) governed the replacement choice.
4. If the same replacement content is used across multiple lessons, each lesson references the same `RC-` ID; the canonical content is not duplicated.

---

## 6. Review-and-Grading Criteria

Both plan types are reviewed. A **Chapter Plan** is graded against the seven Spine fields and the §2.9 Session Map (and the session-count gate). A **Session Plan** is graded against its §3.0 reference integrity, the MANDATORY Lesson Flow segments, the Example Bank minimum, and the Discovery Pattern minimum. Everything else — FLEXIBLE segment timing, Flex Zone choices, embedded examples — is not graded for compliance. (A standalone single-period Session Plan is graded against both column-sets.)

### What reviewers check

| Element | Question reviewers ask |
|---|---|
| §2.1 Learning Objective | One sentence? Observable verb (oral/written/graphic/physical/artifact)? Verb matches §2.3 Bloom's level? |
| §2.2 Must-Cover Content | Finite list? Each item derivable from Universal Core or current NCTB? F-01 holds across all items? Items align with current Subject Spine Playbook minimum? |
| §2.3 Bloom's Distribution | Dominant level(s) declared? Within the class-band indicative range per REF-06 §3.6? |
| §2.4 Exit-Check | One observable check? 2–5 minutes? Same Bloom's level as §2.1? Produces a **per-student readout** (one shared check, *not* one question per child)? **≥2-form Exit-Check Bank provided** (rule 6)? Failure handling rules acknowledged? |
| §2.5 Islamic-Alignment Note | Posture declared (KEEP-AS-IS / NEEDS-REPLACEMENT / FLEXIBLE)? Justification present? F-01 verified? F-02 applied if relevant? Replacement content cross-referenced if NEEDS-REPLACEMENT? **If NEEDS-REPLACEMENT, positive replacement test (REF-12 §11) satisfied — replacement positively reflects a §5–§7 Islamic value (family life / authentic prophetic narration / adab–akhlaq / signs of Allah in nature / halal occupations), not merely avoids the prohibited?** |
| §2.6 Revision Anchor | Builds-On present (or empty with justification)? Revisited-In-This-Lesson present (or empty with justification)? Every must-cover item appears in at least one Future-Revisit slot? |
| §2.7 Homework Specification | Time budget within REF-08 caps (or pilot defaults)? Guideline count consistent with time budget? Bloom's distribution aligned with §2.3? Traceability rule satisfied (each homework item ties to §2.2 or §2.6)? |
| §2.8 Homework Pool | Minimum 20 questions? All Bloom's-tagged? Each question has answer key or rubric? F-01 and Curation Policy verified on every question? |
| §2.9 Session Map *(Chapter Plan)* | One row per session? Every §2.2 item assigned to exactly one session? One objective per session, tracing the §2.3 Bloom climb? Row count = the session count set at the §2A.3 gate? |
| §2A.3 Session count *(Chapter Plan)* | Set at chapter-planning against the TG-Reconciliation baseline? Within the ±40%/±1 band — or within-band reason logged / beyond-band Subject-Lead approval recorded? |
| §3.0 Reference integrity *(Session Plan)* | Reference line present (Chapter Plan ID + session # of N)? Objective and must-cover slice copied from the Session Map row, **not re-derived**? (Standalone single-period plan: full inline Spine instead.) |
| Materials (D-049) | Whiteboard + marker only (teacher) and খাতা/পেনসিল/কলম only (students) in all rituals, examples, and homework — no other surface or tool anywhere (any other fails the gate)? |
| §3 Lesson Flow | All MANDATORY segments present (Opening with all 4 rituals, Hook, Exit-Check, Closing with all 5 elements)? |
| §4.4 Example Bank | Minimum 3 examples per teaching point? All examples F-01 and Curation Policy compliant? |
| §4.5 Discovery Pattern Suggestions | Minimum 3 patterns? Each pattern concrete enough for new-teacher use? |
| §5 Embedded Replacement (if applicable) | Inline block present? RC- reference ID well-formed? Category and D-PROJ02 decision declared in the block? |

### What reviewers do NOT check

- Whether the Lesson Flow's minute-by-minute timing was followed in the classroom (only MANDATORY presence is checked).
- Whether the examples in the Flex Zone match those another teacher would pick.
- Whether the lesson "felt" engaging — except as observable in exit-check outcomes when classroom observations are run (Project 07 scope).
- Which specific question from the topic's Project 04 Pool the teacher assigned on a given day (the Homework Tracker captures rotation visibility separately).

### Grading outcomes

| Outcome | Meaning |
|---|---|
| **APPROVED** | All Spine fields present, well-formed; all MANDATORY Lesson Flow segments present; §4.4 and §4.5 minimums met; aligned with REF-01 / REF-03 / REF-06 / REF-07 / REF-08. Plan is ready for teacher distribution. |
| **REVISE** | One or more checked elements incomplete or misaligned. Reviewer notes which field(s); author revises and resubmits. |
| **CURATION-REVIEW** | §2.5 alignment is uncertain (scholarly disagreement, ambiguous category mapping). Plan held until the disagreement register resolves. |

---

## 7. Before-Publishing Checklist

*(For the plan author to run before submitting a draft for review. A multi-period chapter runs the **Chapter Plan** list, then the **Session Plan** list once per session. A single-period chapter runs both lists against the one standalone Session Plan.)*

### Chapter Plan — Spine (§2) + Session Map (§2.9)

- [ ] §2.1 Learning Objective: one sentence with an observable action verb.
- [ ] §2.1 verb matches the dominant Bloom's level declared in §2.3 (cross-checked against V1A Chapter 2 verb lists).
- [ ] §2.1 verb is observable across at least one mode (oral / written / graphic / physical / artifact).
- [ ] §2.2 Must-cover content is a finite, bounded list.
- [ ] §2.2 Each item derivable from the relevant stability analysis Universal Core, OR from current NCTB, OR tagged `[Islamic-add]`.
- [ ] §2.2 No Western personal names, foods, or clothing in any must-cover item or example (F-01).
- [ ] §2.2 Items align with the current Subject Spine Playbook minimum (in case the playbook has been updated since the last lesson plan version).
- [ ] §2.3 Bloom's-level distribution is declared and within the class-band indicative range per REF-06 §3.6.
- [ ] §2.4 Exit-check is specified, observable in 2–5 minutes, at the same Bloom's level as the objective, and produces a per-student readout (one shared check, not one question per child).
- [ ] §2.4 Exit-Check Bank: ≥2 ready forms for the objective type provided (rule 6); subject forms taken from the Subject Spine Playbook (REF-03 §3.6 for Bangla).
- [ ] §2.4 Failure handling rules acknowledged (30% threshold and 3-lesson individual-attention threshold are part of the lesson plan author's awareness, not their decision).
- [ ] §2.5 Islamic-alignment note declares one of KEEP-AS-IS / NEEDS-REPLACEMENT / FLEXIBLE, with justification.
- [ ] §2.5 If NEEDS-REPLACEMENT: replacement content is inline (per §5) AND cross-referenced to its `RC-{SUBJECT}-C{class}-U{unit}-L{lesson}` ID AND the block declares the C-category and D-PROJ02 decision (if any) that governed.
- [ ] §2.5 If NEEDS-REPLACEMENT: **positive replacement test (REF-12 §11) satisfied** — the replacement positively reflects an Islamic value from REF-12 §5–§7 (family life / authentic prophetic narration / adab–akhlaq / signs of Allah in nature / halal occupations), not merely avoids the prohibited.
- [ ] §2.6 Revision Anchor: Builds-On listed (or empty with justification).
- [ ] §2.6 Revisited-In-This-Lesson listed: every Builds-On item produces at least one revisit.
- [ ] §2.6 Future-Revisit-Candidates listed: every must-cover item appears in at least one slot with cadence and medium.
- [ ] §2.7 Homework time budget within Class 1 pilot default (20 min) or REF-08 spec once locked.
- [ ] §2.7 Each homework item traces to §2.2 or §2.6 (traceability rule).
- [ ] §2.7 If §2.7 declares zero homework, the topic's Project 04 Pool is still available for later revision homework.
- [ ] Homework draws on the topic's Project 04 Pool (≥20, default 30 — built/checked in Project 04, not the plan).
- [ ] §2.8 Each Pool question is Bloom's-tagged with answer key or rubric.
- [ ] §2.8 F-01 and Curation Policy hold for every Pool question.
- [ ] Plan declares the topic tag(s) (`TOP-…`) linking to the Project 04 Pool (ID `QP-{SUBJECT}-C{class}-U{nn}`, in Project 04).
- [ ] §2.9 Session Map present: one row per session; every §2.2 item assigned to exactly one session; one objective per session tracing the §2.3 Bloom climb.
- [ ] §2A.3 Session count set at chapter-planning against the TG-Reconciliation baseline; within the ±40%/±1 band, or within-band reason logged / beyond-band Subject-Lead approval recorded; row count matches.

### Session Plan — header (§3.0)

- [ ] §3.0 Reference line present: Chapter Plan ID + session `_L{mm}` of N.
- [ ] §3.0 This-session objective and must-cover slice **copied from the §2.9 Session Map row**, not re-derived.
- [ ] §3.0 This-session exit-check (from §2.4 Bank) and homework slice (topic + count, from the Project 04 register) named.
- [ ] Materials (D-049): whiteboard + marker only (teacher), খাতা/পেনসিল/কলম only (students) — any other surface or tool fails the materials gate.
- [ ] *(Single-period only)* standalone Session Plan inlines the full Spine (§2.1–§2.7) instead of a reference line; no Session Map.

### Session Plan — Lesson Flow (§3)

- [ ] §3.1 Opening present with all 4 rituals (Salam-with-reply, discipline check, Bismillah, Rabbi zidni 'ilma).
- [ ] §3.2 Hook present (form chosen from §4.5 or invented).
- [ ] §3.2 Hook performs §2.6 Revisited-In-This-Lesson content (or lesson plan declares alternate placement).
- [ ] §3.3 Closing present with all 5 elements **in order** (one-line takeaway, homework note if applicable, materials-to-bag, Alhamdulillah, Salam-with-reply).

### Session Plan — Flex Zone (§4)

- [ ] §4.4 Example Bank: minimum 3 examples per teaching point.
- [ ] §4.4 All examples F-01 and Curation Policy compliant.
- [ ] §4.5 Discovery Pattern Suggestions: minimum 3 patterns.
- [ ] §4.5 Each pattern concrete enough for new-teacher use.

### F-02 cases (if applicable)

- [ ] If the lesson involves Bengali devotional poetry with tariqah lineages: F-02 split applied — form preserved (C-15 scope), content replaced.
- [ ] If the lesson involves tariqah orders, rituals, or hierarchies: full replacement applied (C-17 scope under F-02).
- [ ] If uncertain about any category mapping: lesson tagged `[CURATION-REVIEW-PENDING]` and routed to disagreement register.

### Filename

- [ ] Filename follows D-017 / D-037 convention for the artifact type:
  - Chapter Plan → `C{class}_{SUBJECT}_U{unit}_ChapterPlan_v{version}.md`
  - Session Plan → `C{class}_{SUBJECT}_U{unit}_L{lesson}_SessionPlan_v{version}.md`
  - Standalone single-period Session Plan → `C{class}_{SUBJECT}_U{unit}_SessionPlan_v{version}.md` (no `_L`).

---

## 8. Worked Example

Two cases: **§8.1** a single-period chapter (the v1.2 example, now correctly framed as a standalone Session Plan), and **§8.2** a multi-period chapter (a Chapter Plan + one of its Session Plans).

### 8.1 Single-period case — standalone Session Plan

A complete skeleton drawn from Class 1 Bangla, পাঠ 3 — a chapter the session-count rule resolves to **one** period, so it collapses (§2A.2) to one standalone Session Plan that **inlines the Spine**. **All seven Spine fields are filled in**, then Layers 2–3. (No Homework Question Pool — D-051; the §2.7 Homework Specification names the topic tag + count, and the questions live in Project 04.)

This is illustrative — it shows what each Spine field looks like in practice. It is not a finished, locked plan.

---

**Filename (illustrative):** `C1_BAN_U1_SessionPlan_v1.md` *(single-period → no `_L`)*
**Class:** 1
**Subject:** Bangla (BAN)
**Chapter (`U`):** 1 · পাঠ 3
**Sessions:** 1 (single-period collapse)
**Duration:** 35 minutes (one পিরিয়ড)

### Spine *(inlined — single-period collapse)*

#### §2.1 Learning Objective

Students will identify and pronounce the Bangla vowels অ, আ, ই, ঈ when shown each letter card.

*Observable verb mode:* Oral (pronounce) + Physical/pointing (identify by pointing).

#### §2.2 Must-Cover Content

- Letters: অ, আ, ই, ঈ
- One sample word per letter (drawn from Universal Core where possible; full Example Bank in §4.4):
  - অ → অজগর (python)
  - আ → আম (mango)
  - ই → ইঁদুর (mouse)
  - ঈ → ঈগল (eagle)
- Pronunciation distinction: short ই vs long ঈ

#### §2.3 Bloom's-Level Distribution

Dominant: Remember (70%), Understand (25%). Exposure: Apply (5%).

*Note: Remember at 70% is on the high end of the Class 1–2 band 35–45%. Justified under §2.3 rule for first-introduction lessons (letter recognition is the foundational case).*

#### §2.4 Exit-Check

Teacher holds up each of the four letter cards in random order. Each student, going around the room one by one, says the letter name aloud as the card is shown. Teacher notes any student who hesitates more than 3 seconds on any letter for follow-up via §2.6 Revision Anchor in the next lesson.

Failure handling:
- If 0–4 students hesitate on 1+ letters (less than 30% in a typical 15-student class): partial failure. Recorded in Lesson Completion Tracker. These students appear in `C1_BAN_U1_L4`'s §2.6 Revisited-In-This-Lesson via flashcard warm-up. If the same students hesitate on the same letters across 3+ lessons, individual attention is triggered.
- If 5+ students hesitate (30%+): systemic failure. Teacher escalates to Subject Lead / Principal; this lesson plan is reviewed before being run with another class.

#### §2.5 Islamic-Alignment Note

**KEEP-AS-IS.** None of the current REF-01 C-categories triggered. The sample words (অজগর, আম, ইঁদুর, ঈগল) are concrete natural objects referenced by name only; no depictions of living beings shown to students in this lesson (no C-05 trigger). F-01 systematic exclusions verified: no Western names, foods, or clothing. F-02 not applicable (no devotional poetry, no tariqah content). F-03 not applicable (no nationalism content). F-04 not applicable (no role-play / impersonation tasks).

#### §2.6 Revision Anchor

**Builds-On:**
- `C1_BAN_U1_L1` — letter introduction concept (students have encountered the idea of a Bangla letter).
- `C1_BAN_U1_L2` — letter-sound correspondence (students can match a letter shape to its name aurally).

**Revisited-In-This-Lesson:**
- Letter shapes from `C1_BAN_U1_L2` — revisited via Hook flashcard warm-up.
- Concept of "letter" from `C1_BAN_U1_L1` — revisited implicitly through teacher's framing in Direct Instruction.

**Future-Revisit-Candidates:**

| Item | Suggested next revisit | Medium |
|---|---|---|
| Letter অ recognition | next lesson (`C1_BAN_U1_L4`) Hook | in-class flashcard |
| Letter আ recognition | this week's homework (`QP-BAN-C1-U1-L3` Q1, Q2) | written practice |
| Letter ই recognition | this week's homework | written practice |
| Letter ঈ recognition | this week's homework | written practice |
| Short ই vs long ঈ distinction | next month — first letter-distinction review | class test |

#### §2.7 Homework Specification

| Field | Value |
|---|---|
| Time budget | 20 minutes (Class 1 pilot default; REF-08 pending) |
| Guideline count | 6 questions from the topic's Project 04 Pool |
| Bloom's distribution | Remember 4 (~67%), Understand 2 (~33%) |
| Traceability | All 6 questions trace to §2.2 must-cover content; 1 of the 6 (a flashcard-style item) doubles as §2.6 revisit |

#### §2.8 Homework Question Pool — RETIRED (D-051)

> No inline Pool. Per master **D-051** the plan carries no questions — the §2.7 Homework Specification names the **topic tag** (`TOP-BAN-C1-U1-L3`) + count; the teacher filters the **Project 04** register/master by that tag and selects `Y` (D-030 count-is-the-lever). Questions are produced and stored in Project 04 (production file → master → register), never copied into the plan.

### Lesson Flow

#### Opening (0–3 min) — MANDATORY

1. Teacher enters, says "Assalamu alaikum wa rahmatullah." Waits for and confirms reply from all students.
2. Discipline check: hand-raise rule; permission rule before leaving seat; materials — Bangla খাতা (notebook), পেনসিল (pencil), কলম (pen) are the only permitted pupil tools on the desk (per D-049; any other tool fails the gate); everything else in the bag.
3. Bismillah ar-Rahman ar-Raheem (collective).
4. Rabbi zidni 'ilma (collective).

#### Hook (3–8 min) — MANDATORY presence, FLEXIBLE form

Form (from §4.5): **Flashcard-led** (performs §2.6 Revisited-In-This-Lesson).

- Teacher shows the letter cards from the previous lesson (`C1_BAN_U1_L2`) one at a time. Students name each letter chorally, then by rows.
- Teacher transitions: "আজ আমরা নতুন চারটি অক্ষর শিখব।"

#### Direct Instruction (8–18 min) — FLEXIBLE

Introduce each of the four letters with letter card + sample word + sound. Repeat each pair twice. Show the sample word visually (no depiction; just the written word).

#### Guided Practice (18–25 min) — FLEXIBLE

Teacher shows a card; whole class says the letter together; then rows; then individuals.

#### Independent Practice (25–30 min) — FLEXIBLE

Each student traces each letter once in their খাতা (notebook). Teacher circulates.

#### Exit-Check (30–33 min) — MANDATORY

Execute the §2.4 check.

#### Closing (33–35 min) — MANDATORY

1. One-line takeaway: "আজ আমরা চারটি স্বরবর্ণ শিখলাম — অ, আ, ই, ঈ।"
2. Homework note: "বাড়ির কাজ — পাঠ্যপুস্তকের অনুশীলনী পৃষ্ঠা [page] থেকে ৬টি প্রশ্ন। (From QP-BAN-C1-U1-L3, teacher selects 6.)"
3. Materials-to-bag check.
4. Alhamdulillah (collective).
5. Teacher says "Assalamu alaikum wa rahmatullah." Waits for and confirms reply from all students. Teacher leaves.

### Flex Zone

#### §4.1 — Teacher MAY decide

- Substitute any of the four sample words with another concrete word from §4.4 Example Bank.
- Reverse Direct Instruction and Guided Practice timing if the room is restless after Opening.
- Add a spoken clapping rhythm for the four letters — speech rhythm only, no melody, per D-PROJ02-003.
- Choose a different §4.5 Discovery Pattern (e.g., Object-led instead of Flashcard-led for Hook).

#### §4.2 — Teacher MAY NOT decide

- Skip any of the four letters from §2.2.
- Replace the exit-check with written-only (pronunciation must be oral).
- Skip Opening rituals, Hook, Closing rituals.
- (For new/probationary teachers) Reverse Hook ↔ Direct Instruction sequence.

#### §4.3 — Pedagogical posture

This lesson defaults to Direct Instruction in §3 because the content is new and unfamiliar. The Flex Zone discovery-orientation manifests via Hook (flashcard recall invites student initiation) and via the teacher's elaboration in Guided Practice ("এই অক্ষরটি আর কোন শব্দে শুনেছ?" / "Where else have you heard this letter?").

#### §4.4 Example Bank

| Letter | Acceptable example words (minimum 3) |
|---|---|
| অ | অজগর (python), অমল (pure / pristine), অসীম (limitless) |
| আ | আম (mango), আকাশ (sky), আল্লাহ (Allah) |
| ই | ইঁদুর (mouse), ইট (brick), ইমান (faith) |
| ঈ | ঈগল (eagle), ঈদ (Eid), ঈমানদার (faithful person) |

All examples verified F-01 (no Western names/foods/clothing) and Curation Policy (KEEP-AS-IS). Note that আল্লাহ, ইমান, ঈদ, and ঈমানদার carry Islamic resonance and are appropriate `[Islamic-add]` items.

#### §4.5 Discovery Pattern Suggestions

Minimum 3 patterns:

1. **Flashcard-led (default for Hook this lesson).** Show prior-lesson letters; students name. Transitions to new letters.
2. **Object-led.** Bring a real mango (আম) to class; ask "এটা কী?" Lead to letter আ. Bring or show a picture of a brick (ইট) for ই. (No animal depictions per C-05 / D-PROJ02-002; for living-being words, use the word only, not picture.)
3. **Sorting-led.** Mix the four new letter cards with two letters from `C1_BAN_U1_L2`. Students sort into "new" and "already-known" piles, then name each.

---

### 8.2 Multi-period case — Chapter Plan + one Session Plan

A compact skeleton for a **3-session** chapter (illustrative; Spine fields abbreviated to show structure, not filled to production depth). TG Reconciliation baseline for this chapter = 3 periods → band 2–5 (±40% rounds to ±1.2 → ±1; the larger of ±40% and ±1 → band 2–4; here author keeps 3).

#### 8.2.a Chapter Plan

**Filename (illustrative):** `C1_BAN_U2_ChapterPlan_v1.md` · **Class** 1 · **Subject** BAN · **Chapter (`U`)** 2 · **Sessions** 3

| Spine field (chapter scope) | Content (abbreviated) |
|---|---|
| §2.1 Objective **set** | (i) recognise the chapter's three letters; (ii) match each to its sound; (iii) read a 2-letter blend using them |
| §2.2 Must-cover | letters L₁ L₂ L₃; sound of each; one sample word each (Example Bank in Session Plans); the blend pattern |
| §2.3 Bloom progression | S1 Remember-heavy → S2 Remember+Understand → S3 Understand+Apply (within Class 1–2 band) |
| §2.4 Exit-Check Bank | ≥2 forms per objective type (point-to-card; say-the-sound; read-the-blend) |
| §2.5 Curation note | KEEP-AS-IS; F-01 verified; sample words use natural objects, no living-being depiction (C-05) |
| §2.6 Revision | within-chapter: S2 revisits S1, S3 revisits S1–S2 (Hook); cross-chapter: feeds the REF-07 spiral |
| §2.7 Homework spec | per-session 20-min cap (REF-08); daily cap unchanged |
| §2.8 Pool — RETIRED (D-051) | none in plan; questions live in Project 04, linked by topic tag `TOP-BAN-C1-U2` |

**§2.9 Session Map**

| Session | Focus | Objective | Must-cover slice | Exit-check | Homework slice |
|---|---|---|---|---|---|
| `_L01` | introduce L₁, L₂ | recognise & say L₁, L₂ | L₁, L₂ + sounds | point-to-card (Bank form A) | Pool Q1–Q6 |
| `_L02` | introduce L₃ + revisit L₁L₂ | recognise & say L₃; recall L₁L₂ | L₃ + sound; review L₁L₂ | say-the-sound (Bank form B) | Pool Q7–Q12 |
| `_L03` | blend the three | read a 2-letter blend | blend pattern across L₁–L₃ | read-the-blend (Bank form C) | Pool Q13–Q18 |

Session count = 3 (within band; no special reason needed).

#### 8.2.b Session Plan — `_L02` of 3

**Filename (illustrative):** `C1_BAN_U2_L02_SessionPlan_v1.md`

> **§3.0 Header**
> **Reference:** `C1_BAN_U2_ChapterPlan_v1` · Session `_L02` of 3
> **This-session objective** (from Session Map): recognise & say L₃; recall L₁, L₂.
> **Must-cover slice:** L₃ + its sound; review L₁, L₂.
> **Exit-check:** Bank form B (say-the-sound), per-student readout.
> **Homework slice:** `QP-BAN-C1-U2` Q7–Q12 (teacher picks 6 per §2.7).
> **Materials (D-049):** teacher whiteboard + marker only; students খাতা/পেনসিল/কলম only — any other surface or tool fails the materials gate.

**Lesson Flow (Layer 2)** — Opening (4 rituals) → **Hook:** flashcard recall of L₁, L₂ from `_L01` (performs the §2.6 within-chapter revisit) → Direct Instruction: introduce L₃ → Guided then Independent Practice (trace L₃ in the খাতা) → Exit-Check (Bank form B) → Closing (5 elements).

**Flex Zone (Layer 3)** — §4.4 Example Bank: ≥3 words for L₃ (F-01/Curation clean); §4.5 ≥3 discovery patterns (flashcard-led default for the Hook).

*Note how the Session Plan re-derives nothing: objective, slice, exit-check, and homework all point back to the Chapter Plan's §2.9 row (§2A.1).*

---

## 9. Version Log & Ownership

| Version | Date | Change | By |
|---|---|---|---|
| v1.0 | 2026-05-20 | Initial creation. Synthesizes D-004, D-005, D-020, Project 03 architecture decisions Q-A through Q-H (handoff §7 of `PROJECT00_handoff_2026-05-20_project02_to_ref02.md`), and Bloom's V1A §3.2, §3.6, §6.1–6.8. Spine: 5 fields. Layer 2 named "Suggested Flow." | Claude (drafted); Principal (approval pending) |
| v1.1 | 2026-05-20 | (a) Spine extended from 5 to 6 conceptual fields (8 numbered: §2.6 Revision Anchor, §2.7 Homework Specification, §2.8 Homework Question Pool added). (b) §2.1 observable-verb rule broadened to oral / written / graphic / physical / artifact modes with examples. (c) §2.2 added rule 5 on minimum-may-be-raised over time (via Subject Spine Playbook updates). (d) §2.4 added failure-handling rules: 30% systemic-failure threshold and 3-lesson individual-attention threshold (Principal-confirmed thresholds 2026-05-20). (e) Layer 2 renamed "Suggested Flow" → "Lesson Flow" with each segment annotated MANDATORY presence or FLEXIBLE form/timing. (f) Opening expanded with 4 mandatory rituals (Salam-with-reply, discipline check, Bismillah, Rabbi zidni 'ilma); attendance removed; "other school-standard du'a" deliberately open for future v1.x. (g) Hook elevated to MANDATORY presence. (h) Closing expanded with 5 mandatory elements (materials-to-bag, one-line takeaway, homework note, Alhamdulillah, Salam-with-reply). (i) §4.1 references new §4.4 Example Bank. (j) §4.2 sequencing rule tightened (Hook-then-Direct-Instruction default; reversal restricted to non-probationary teachers). (k) §4.4 Example Bank added (minimum 3 examples per teaching point). (l) §4.5 Discovery Pattern Suggestions added (minimum 3 patterns per lesson). (m) §6 reviewer checks expanded for new fields. (n) §7 Before-Publishing Checklist expanded. (o) §8 Worked Example fully rewritten to demonstrate all new fields. (p) §9 cross-Project consumers updated for REF-07 and REF-08 as future dependencies. | Claude (drafted); Principal (approval pending) |
| v1.2 | 2026-05-25 | **Exit-Check Bank added to §2.4** (adopts master **D-043**; D-PROJ00-021), surfaced during REF-03 review. (a) §2.4 rule 3 clarified — per-student readout is *one shared check observed per pupil*, not one question per child (2–4 variants only to deter written-copying). (b) §2.4 new **rule 6** — every lesson plan carries a ready Exit-Check Bank (≥2 forms per objective type), parallel to the §4.4 Example Bank; subject forms live in the Subject Spine Playbooks (REF-03 §3.6 Bangla). (c) §6 reviewer row + §7 checklist line added. (d) §9 Open-dependencies: REF-03 marked LOCKED v1.0. Supersedes v1.1 (→ `/archive/`). | Claude (drafted); Principal (approved 2026-05-25) |
| v1.3 | 2026-05-28 | **Two-tier Chapter/Session architecture (adopts master D-050) + classroom-materials fold (adopts master D-049).** The three-layer model is re-homed across two plan types: **Layer 1 Spine → Chapter Plan (chapter scope)**; **Layers 2–3 Lesson Flow + Flex Zone → Session Plan (period scope)**. (a) Front matter, Purpose, and **§1** rewritten for the two plan types + split reading rule. (b) **§2** reframed to Chapter scope with a scope-reading banner; **§2.9 Session Map** added (Chapter-Plan-only field). (c) New **§2A** — reference rule (reference, never restate), single-period collapse, session-count rule (TG baseline; ±40%/±1 band; chapter-planning gate), IDs/filenames (`U`=chapter, `_L` kept but redefined = session). (d) **§3** gains **§3.0 Session Plan header**; §3/§4 reframed to period scope. (e) **§6** review table gains Session Map, session-count, reference-integrity, and materials rows; intro covers both plan types. (f) **§7** split into Chapter-Plan + Session-Plan checklists; filename line updated for the three patterns. (g) **§8** relabelled — §8.1 single-period case (standalone Session Plan) + new §8.2 multi-period case (Chapter Plan + one Session Plan). (h) **D-049 materials fold:** স্লেট/চক references scrubbed throughout (§2.1 verb table, §2.4 example, §3.1/§3.3 rituals, §8.1 worked example); teacher = whiteboard + marker, students = খাতা/পেনসিল/কলম. (i) **Class 3–5 Bloom band inlined into §2.3** (REF-06 §3.6, active scope): Remember 20–30% · Understand 25–35% · Apply 25–35% · Analyze 10–20% · Evaluate 0–10% · Create 0–10%; the §2.3 table is marked a convenience copy with REF-06 §3.6 retained as the authoritative source; C6–8/C9–10 still pointer-only. (j) **REF-12 integrated into §2.5** — Definition extended to name the three-layer relationship (REF-12 *why* / REF-01 *what to replace* / REF-21 *how to find*); **new rule 5 — Positive Replacement Test (REF-12 §11)**: NEEDS-REPLACEMENT content must positively reflect an Islamic value from REF-12 §5–§7 (family life / authentic prophetic narration / adab–akhlaq / signs of Allah / halal occupations), not merely avoid the prohibited; §6 reviewer row and §7 checklist extended accordingly; REF-12 added to Companion documents. (k) **§3.3 Closing sequence reordered** (Principal field-check 2026-05-28): step 1 ↔ step 3 swap so the one-line takeaway (step 1) and homework note (step 2) — both writing tasks — precede materials-to-bag (step 3). Old order put materials away before students could record the homework. Salam (step 5) and Alhamdulillah (step 4) positions unchanged; the symmetry with the Opening Salam is preserved. §3.3 step list, the "may compress step N" note, the §7 checklist element list (now order-explicit), and the §8.1 worked-example Closing all updated to match. (l) **§2.5 stale-count refresh** (surfaced when the live Project 03 Instructions §10 were read): REF-02 v1.2 carried "C-01 through C-17" and F-01/F-02 only, but REF-01 has grown to **C-19** and the propagation flags now span **F-01 / F-02 / F-03 / F-04** (per Project 03 Instructions §10 / D-PROJ03-007). Six §2.5 sites updated — Companion documents, Definition, KEEP-AS-IS / NEEDS-REPLACEMENT posture text, the categories reference paragraph (now points to REF-01 §4.1 as authoritative and explicitly drift-protects: never assume a fixed count in-template), the F-flag block (expanded to F-01/F-02/F-03/F-04 with content lifted from REF-01 / Project 03 §10), and the §8.1 worked-example justification. §9 REF-01 open-dependency entry refreshed: REF-01 marked LOCKED (was "not yet locked, scheduled Day 4"). **Terminology locked** 2026-05-28: Chapter / Session (Bangla পিরিয়ড); "lesson plan" retained only as the informal family term. Supersedes v1.2 (→ `/archive/`). **Open ripple (workstream b, not yet applied):** REF-03 (per-subject period norms), REF-06 (Bloom across sessions), REF-07/REF-19 (within- vs cross-chapter revision), REF-08 (chapter-level pool, per-session daily cap), and the D-037 `_L{mm}` formalization. | Claude (drafted); Principal (approval pending) |
| v1.4 | 2026-05-31 | **Classroom-materials standard wider-scrub (D-PROJ00-057, Decision Review under Principal direction).** The চক/স্লেট naming is removed throughout and the D-049 materials standard restated **positively** as a closed permitted-list + catch-all: the only permitted teaching surface is whiteboard + marker; the only permitted pupil tools are খাতা/পেনসিল/কলম; **any other surface or tool fails the materials gate** (REF-11 G2). Rationale: চক/স্লেট are not available in the school, so naming them as "banned" is unnecessary; the "only … permitted" wording + the gate preserve enforceability against any backslide. Sites updated: §1 alignment line, §2.4 materials example, the §3.1/§3.3 discipline + materials-to-bag rituals, §6 review-table materials row, §7 checklist materials item, the §8 worked-example discipline step, and the §8 materials callout; the v1.3 §9 row is left intact as history. No structural, Bloom, session-count, or curation change — wording only. Supersedes v1.3 (→ `/archive/`). Companion edits this batch: D-049 master row restated positively in `PROJECT00_README.md` §3 (in-place amendment annotation, D-PROJ00-057), GLOSSARY Classroom-Materials Standard entry, REF-11 G2 (already positive). **Local-only — no master decision** (D-049 amended in place per mechanism (b); master range stays D-001 through D-050). | Claude (drafted); Principal (approval pending) |
| v1.6 | 2026-05-31 | **Master D-051 (supersedes D-029): §2.8 Homework Question Pool field retired** — questions move to Project 04, plan links by topic tag; Spine now seven numbered fields + Session Map; §2.7 / §2.9 / reviewer / reading-rule references repointed. Payload change. Supersedes v1.5 → /archive/. | Claude (drafted); Principal (apply on confirm) |

### Ownership

This file is canonical to Project 00. Edits go through the Draft → Locked discipline in `PROJECT00_README.md` §5.3 — this version is the locked `LOCKED_REF-02_Three_Layer_Lesson_Plan_Template_v1_3.md`, with v1.2 moved to `/archive/`. **Subject-specific specialization of any field (especially §2.2 Must-Cover Content, §4.4 Example Bank format per subject, §4.5 Discovery Pattern library per subject) lives in the Subject Spine Playbooks (REF-03 onward), not by editing this template.**

### Cross-Project consumers

- **Project 03 — Lesson Plan Production.** Primary consumer. Under v1.3 Project 03 produces **two artifact types** — a Chapter Plan per chapter and a Session Plan per period (single-period chapters → one standalone Session Plan). Both conform to this template structurally; filenames follow the §2A.4 patterns (`_ChapterPlan` / `_L{mm}_SessionPlan` / `_SessionPlan`). The current field-tested layout contract becomes the **Session-Plan layout**; a Chapter-Plan layout is the new artifact to build (Project 03, after the v5 layout contract).
- **Project 04 — Question Bank Production.** The plan carries no Pool (D-051); Project 04 owns the canonical Pool (`QP-{SUBJECT}-C{class}-U{nn}`), linked to the plan by the topic tag. Formative questions inside a lesson plan are scoped by the §2.4 exit-check (per Q-F).
- **Project 05 — Replacement Content Studio.** Replacement content referenced inline per §5 has its canonical source in Project 05 under the `RC-{SUBJECT}-C{class}-U{unit}-L{lesson}` ID system.
- **Project 06 — Tracker & Operations System.** Homework Tracker reads §2.7 caps and §2.8 question rotation; Lesson Completion Tracker reads §2.4 exit-check outcomes; Class Test Tracker informs §2.2 minimum-growth-over-time rule.
- **Project 07 — Teacher Training & Review.** V1B and V1C derivations of the Bloom's primer, the classroom observation rubric, and the peer-review checklists all use this template as the structural reference. §4.2 sequencing rule ("demonstrated engagement") is operationally defined here.

### Open dependencies acknowledged

- **REF-01 (Islamic Curation Policy).** **LOCKED.** §2.5 of this template defers to REF-01 §4.1 for the authoritative C-category list (currently C-01 through C-19) and to the F-01 / F-02 / F-03 / F-04 propagation flags. The lesson plan author and reviewer consult REF-01 directly; in-template numbers are convenience references only.
- **REF-03 (Bangla Subject Spine Playbook).** **LOCKED v1.0 (2026-05-25)** — `LOCKED_REF-03_Bangla_Subject_Spine_Playbook_v1_0.md`. §2.2, §4.4, §4.5 of this template defer concrete Bangla subject specialization to it, and §2.4's Exit-Check Bank takes its Bangla forms from REF-03 §3.6.
- **REF-06 (Bloom's V1A primer).** Produced and present in Project 00. §2.3 and §6 of this template reference V1A by section.
- **REF-07 (Revision Architecture).** **To be produced Day 5** per Principal direction 2026-05-20 (added to Phase 2 due to importance). §2.6 of this template provides the per-lesson inputs; REF-07 specifies the cross-lesson revision spiral, weekly assignment selection, monthly cumulative revision, and tracker integration.
- **REF-08 (Homework Architecture).** **To be produced Day 6** per Principal direction 2026-05-20. §2.7 and §2.8 of this template use Class 1 pilot defaults (20-minute per-lesson time budget; 5–10 guideline question count; 2–4 hour Daily Homework Budget) pending REF-08 lock. REF-08 will provide authoritative per-class-per-subject figures.
- **D-050 ripple (workstream b — open, not yet applied).** The two-tier model changes how several locked REFs read at chapter vs session scope; each needs a scoped patch in a follow-on pass: **REF-03** (per-subject period/session norms; how a subject's chapters typically session-ise), **REF-06** (Bloom progression is a chapter property climbing across sessions, not a per-period mix), **REF-07 / REF-19** (separate *within-chapter* revision — session N revisits N−1 — from the *cross-chapter* spiral), **REF-08** (homework Pool defined at chapter level; the daily time cap stays per session), and the **filename D-037** formalization of `_L{mm}` as the session slot + the `_ChapterPlan` form. Until applied, this template's §2A.4 is the interim authority for the filename forms.

---

## Downstream — built-asset dependents (back-pointer · D-PROJ00-062)

**This reference is a source of `LOCKED_ProductionCore_v1`** (Project 03 built asset): it supplies **Core §1–§3** — the Chapter-Plan Layer-1 Spine fields + §1.9 Session Map + §1.10 session-count rule; the Session-Plan Layer-2 Lesson-Flow segments + Opening/Closing rituals + the D-049 materials line; and the Layer-3 Flex Zone. A supersede of this file makes the Production Core **stale → rebuild required** before any new Chapter/Session Plan is built off it — see Core §7 and `LOCKED_ProductionAsset_Build_Policy_v1` §6 (Project 03), the change-time trigger in `PROJECT00_README.md` §5.3/§5.4, and the dependency record in `PROJECT00_CROSS_PROJECT_INDEX.md` (D-PROJ00-061).

*Payload scope:* the rebuild trigger fires on a change to the **extracted payload** (the Core §1–§3 content). A payload-neutral edit — such as this back-pointer footer (the v1.4 → v1.5 supersede that introduced it) — supersedes the file but does **not**, by itself, make the Core stale.

*Supersede record:* **v1.4 → v1.5**, 2026-05-31, footer added (D-PROJ00-062); v1.4 → `/archive/`. (Full version history in §9.)
