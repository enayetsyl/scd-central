# REF-08 — Homework Architecture (Canonical)

**Status:** v1.3 (**LOCKED** 2026-05-31 — master **D-051** / D-PROJ00-064: the Homework Question Pool moves to Project 04; the plan carries no Pool, linked by topic tag; §4 placement repointed; budget / floating-allocation / tracker mechanics unchanged; supersedes v1.2 → /archive/.) *Earlier: v1.2 (LOCKED 2026-05-31 — back-pointer footer added recording the Production-Core source dependency, D-PROJ00-062; **payload-neutral, no rule change**; supersedes v1.1 → `/archive/`.) *Earlier: v1.1 (LOCKED 2026-05-29 — D-050 ripple, workstream-b item b.6; supersedes v1.0 → `/archive/`. Drafts v0.1–v0.2 retained as history.)* **v1.1 = scoped two-tier acknowledgement from master D-050 (REF-02 v1.3):** the **Homework Question Pool** (§4) now lives at **chapter scope** (one Pool per chapter, on the Chapter Plan), not per session; the **daily time cap** (§2 Daily Homework Budget) stays **per session** (each Session Plan's homework slice is bounded by the daily ceiling). No figure, cap, or governance change.
**Project:** 00 — Curriculum Foundations
**Date created:** 2026-05-22
**Owner:** Principal
**Author:** Claude (drafted); **Principal (approved + locked 2026-05-22)**
**Source decisions:** D-024 (Class 1 Daily Homework Budget 2–4 hrs — *operationalised here*), D-027 (REF-08 exists), D-028 (Pool min 20 questions), D-029 (Pool placement — superseded by D-051: Pool in Project 04), D-030 (time-cap firm / count is the lever), D-013 (8 trackers — no 9th), D-014 (tracker cadences — Homework daily; Assignment given Thu / collected Sun), D-PROJ00-006 (REF-08 = Homework Architecture, canonical numbering), D-PROJ00-008 (REF-07 locked — the model this document obeys), D-020 (Salafi framing). Adopts new master decision **D-036** (the floating-allocation method + uniform Classes 1–5 ceiling, initiative-wide — see §10.2 / master README §3).
**Companion documents:**
- `LOCKED_REF-07_Revision_Architecture_v1_0.md` — **primary companion.** Daily homework is a load-bearing leg of REF-07's revision spiral; REF-07 §1.4 routes the homework/assignment **time caps** to this document. REF-08 sets those caps; REF-07 owns the assignment's scheduling and content.
- `LOCKED_REF-02_Three_Layer_Lesson_Plan_Template_v1_1.md` — §2.7 Homework Specification and §2.8 Homework Question Pool: the lesson-plan fields REF-08 governs.
- REF-03 (Bangla Subject Spine Playbook, Day 5) — holds the filled topic-wise revision chart whose `TOP-…` tags homework items carry. *(Open dependency.)*
- Project 06 trackers — the **Homework Tracker** (daily) and **Assignment Tracker** (weekly). The 6-stage delivery→return lifecycle and the `HW-…`/`AS-…` ID *format* live there (TODO Day 6 step 6.1), not here.
- `Bloom_Taxonomy_Comprehensive_Primer_Teachers_V1A.docx` (REF-06) — homework Bloom's distribution (Remember/Understand-heavy at primary).

---

## §0 — Summary (read this first)

**The one principle.** A young child learns by **small, consistent daily effort**, not by weekend cramming. So homework is **bounded by time, not by question count** (D-030); the daily total is **capped per class**; and the cap is a **design target for the average student**, never a stick to beat the slow child with. *"The most beloved deeds to Allah are the most constant, even if little"* (al-Bukhari & Muslim). Daily homework is that small, constant deed.

**What REF-08 is.** The governance layer for **daily homework** (`HW-…`). It answers four questions and nothing more: *how much* homework a child may carry in a day (the budget), *how the day's budget splits across subjects* (the floating-allocation method — **not** a fixed table), *where the questions come from* (the topic's Project 04 Pool), and *how it is tracked* (the existing Homework Tracker — no 9th tracker).

**What REF-08 is NOT.** It is **not** the weekly assignment. The weekly assignment (`AS-…`, given Thursday / collected Sunday) is REF-07's revision workhorse and the Assignment Tracker's record. REF-08 sets only the assignment's **time cap** so the two channels never double-count a child's load (§3).

**The budgets (average student):**

| Channel | When | Who owns it | Time cap (Classes 1–5) |
|---|---|---|---|
| **Daily homework** (`HW-…`) | School nights (Sun–Thu; lighter Thu) | **REF-08** | **2–4 hrs/day** total across subjects (D-024); per-subject **0–40 min**, default 20 |
| **Weekly assignment** (`AS-…`) | Weekend (Fri + Sat); given Thu, collected Sun | **REF-07** + Assignment Tracker | **4 hrs/day** × 2 = 8 hrs (cap set here; content set by REF-07) |
| **Daily Quran muraja'ah** | Every day, incl. weekends | Quran Tracker (D-014) | A protected slice; **on weekends additional & outside** the assignment cap (§2.4) |

**The floating-allocation move (the heart of this document).** The 2–4 hr daily budget is **not** carved into fixed per-subject minutes, because topic load varies day to day — a heavy Bangla day may earn 40 min while Math takes 20; the next day reverses. Instead: each subject's lesson sets *its own* homework time that day via §2.7 (0–40 min band), the class teacher **sums** the day's declared times, and if the sum exceeds the ceiling the teacher **trims by question count, not by time** (D-030). The split is decided fresh each day by real lesson load, then reconciled against one firm ceiling (§2.2–§2.3).

**Islamic grounding.** Two principles govern every figure below. First, **moderation** — *"Allah does not burden a soul beyond its capacity"* (al-Baqarah 2:286): the ceiling protects the child from being overloaded, and a lesson may set **zero** homework when it does not warrant any (D-030 / REF-02 §2.7). Second, **consistency** — small daily reinforcement (the daily `HW-…`) builds retention far better than a weekend pile, mirroring the daily Quran muraja'ah discipline REF-07 §0 already invokes (the hobbled camel that slips its rope once untied). Homework is *adab of effort*, not punishment.

**Who acts on what:**
- **Teacher** → §2.3 (the daily allocation procedure) and §6 (worked week / quick-card).
- **Class teacher (coordination role)** → §2.3 step 2–4 (tally and trim the day's total).
- **Lesson-plan author (Project 03)** → §4 (link the plan to the topic's Project 04 Pool) and §7.1 checklist.
- **Tracker-designer (Project 06)** → §5 (Homework Tracker integration) and §7.2 checklist.
- **Principal** → §2.5 (the weekly load roll-up) and §2.6 (the average-student framing).

---

## Quick-Navigation Checklist (staff-facing)

- [§0 — Summary](#0--summary-read-this-first)
- [§1 — Purpose, scope, and the design principle](#1--purpose-scope-and-the-design-principle)
- [§2 — The Daily Homework Budget (governance)](#2--the-daily-homework-budget-governance)
- [§3 — Daily homework vs weekly assignment — the boundary](#3--daily-homework-vs-weekly-assignment--the-boundary)
- [§4 — The Homework Question Pool](#4--the-homework-question-pool)
- [§5 — Plumbing: IDs, topic tags, Homework Tracker integration](#5--plumbing-ids-topic-tags-homework-tracker-integration)
- [§6 — Worked example (a Class 1 week) + teacher quick-card](#6--worked-example-a-class-1-week--teacher-quick-card)
- [§7 — Checklists (author + tracker-designer + teacher)](#7--checklists-author--tracker-designer--teacher)
- [§8 — Design note: why floating, not fixed](#8--design-note-why-floating-not-fixed)
- [§9 — Roles & responsibilities](#9--roles--responsibilities)
- [§10 — Open dependencies, decisions for review, version log](#10--open-dependencies-decisions-for-review-version-log)

---

## §1 — Purpose, scope, and the design principle

### 1.1 Purpose
Stop daily homework from either (a) drifting up until a six-year-old is buried, or (b) drifting down until it stops reinforcing the lesson. Give every subject a predictable way to set the right amount of homework on any given day, give the child one firm daily ceiling, and let the Principal see the whole weekly load at a glance — all without a fixed timetable that goes stale the first week.

### 1.2 The design principle (governs every choice below)
**Bound the time, float the split, protect the child.** The daily *ceiling* is firm; the *split* across subjects is decided fresh each day by actual lesson load; the *question count* is the teacher's lever to stay inside the time (D-030). The ceiling is sized for the **average** student — faster children finish early, slower children take longer and that is expected and acceptable (§2.6). A system that fixed minutes per subject would fight reality every day and be abandoned; a system with no ceiling would overload the child. REF-08 does neither.

### 1.3 Scope (in)
The Daily Homework Budget per class (§2.1); the floating-allocation method and the daily reconciliation procedure (§2.2–§2.3); the weekend rule and the weekly load roll-up (§2.4–§2.5); the average-student framing (§2.6); the daily-homework vs weekly-assignment boundary (§3); the Homework Question Pool's sizing, placement, and time-vs-count rule, and how it feeds both routine homework and the bounded weak-student top-ups (§4); the requirement that homework be numbered (`HW-…`) and topic-tagged (`TOP-…`) and the Homework-Tracker integration (§5).

### 1.4 Scope (out — redirect)
- **The weekly assignment's content and scheduling** → REF-07 (§2.3, §2.4). REF-08 sets only its time cap.
- **The 6-stage delivery→return lifecycle and the `HW-…`/`AS-…` ID format and tracker fields** → Project 06 (TODO Day 6 step 6.1). REF-08 states the *requirement*; Project 06 builds the plumbing.
- **Question authoring** → Project 04. REF-08 only says homework questions come from the topic's Project 04 Pool (selected via the register/master, never authored at the point of use).
- **The filled per-subject topic chart** → REF-03+. REF-08 references it by `TOP-…` tag only.
- **Per-chapter class-test design and the chapter-stop gate** → REF-07 §2.4 / Project 06. REF-08 only uses the *window before* the class test for the §4.3 top-up rule.
- **The Quran daily-revision discipline itself** → the Quran Tracker (D-014). REF-08 only reserves it a protected slice — counted within the weekday budget but **additional and outside** on the weekend (§2.4).

### 1.5 What REF-08 is *not*
Not a new lesson field (it governs the existing §2.7 / §2.8), not a new tracker (it wires into the existing Homework Tracker), and not a fixed per-subject timetable (it is a method, §2.2).

---

## §2 — The Daily Homework Budget (governance)

### 2.1 The ceiling, per class

The Daily Homework Budget is the **maximum total daily homework time across all subjects** for a class, for the **average** student. It is a ceiling on the **daily `HW-…` channel only** — the weekend assignment is budgeted separately (§3).

| Class | Daily ceiling (avg student) | Daily floor (typical) | Weekend cap | Status |
|---|---|---|---|---|
| **Classes 1–5 (uniform)** | **4 hrs (240 min)** | **2 hrs (120 min)** | **4 hrs/day × 2 = 8 hrs** | **Authoritative** — Class 1 per D-024; extended to Classes 2–5 as a uniform ceiling by Principal direction 2026-05-22 |

**Reading the band.** "2–4 hrs" is **not** "always 4." The **floor (2 hrs)** is the typical day — every subject at its 20-min default. The **ceiling (4 hrs)** is the heavy day — reached only when several subjects genuinely have heavy new content at once. Most days sit near the floor.

**Uniform ceiling, flexing band.** The 2–4 hr daily ceiling (and the 8-hr weekend cap) is **identical for Classes 1–5**. The per-subject band below (0–40 min, default 20) is the **Class-1 working value**; for classes whose daily roster has fewer homework-bearing subjects (Classes 3–5 on most days), an individual subject may run a little above 40 — the firm constraint is always the **daily sum ≤ ceiling** (§2.2–§2.3), never the per-subject figure.

### 2.2 The floating-allocation method (no fixed split)

The day's budget is **not** pre-divided into "Bangla 30, Math 30, …". It is assembled from each subject's own §2.7 declaration and then reconciled.

**Per-subject daily band (Class 1):** each subject's §2.7 sets its homework time for the day inside a band of **0–40 minutes**, default **20 minutes**.
- Toward **40** on a heavy new-content day.
- At **20** on a normal day.
- Toward **0** on a light/review day; **exactly 0** on assessment-day lessons, the eve of a holiday, or a lesson that already had extensive Independent Practice (D-030 rule 4 / REF-02 §2.7 rule 4).

**Why this band.** Class 1 (Sun–Wed) carries **six daily subjects** — Bangla, English, Math, Quran, Arabic, Islam. The band is anchored so the arithmetic lands on D-024 automatically:
- 6 subjects × **20 min default** = 120 min = the **2-hr floor**.
- 6 subjects × **40 min max** = 240 min = the **4-hr ceiling**.

Thursday's reduced roster (Class 1–2: Quran + Arabic + weekly tests) simply produces a smaller daily sum by the same method — see §2.3 step 6.

So the per-subject band and the daily ceiling are two views of the same budget — the teacher never has to compute a split, only to keep the **sum** under the ceiling (§2.3).

**Variable rosters (Classes 3–5).** Where not every subject meets every day (e.g. Class 3–5: Bangla/English/Math four days a week, BGS/Science/Islam twice, Quran/Arabic daily), the method is unchanged: on any given day, sum the §2.7 times of **the subjects that actually met that day**, plus the daily Quran/Arabic slice, and reconcile against the **uniform daily ceiling** (§2.1). Fewer subjects on a given day simply means each may run a little higher within the same total. The floating method absorbs a different daily roster with no extra rule.

### 2.3 The daily reconciliation procedure (teacher-facing, stepwise)

Because more than one teacher feeds a single child (the class teacher for most subjects, specialists for Quran / Arabic / Islam), one person must see the **whole day's** load before it goes home. That is the **class teacher**, acting as the daily homework coordinator. Each school day, in order:

1. **Collect declarations.** Each subject lesson's §2.7 has set that subject's homework time and the `HW-…` items for the day (one **common** sheet for the whole class — never bespoke per student; REF-07 §2.3).
2. **Tally.** The class teacher adds the day's declared times across all subjects that met today. Call this the **day total**.
3. **Compare to the ceiling** for this class (§2.1).
4. **If day total ≤ ceiling →** issue as planned. **If day total > ceiling →** trim, in this priority order, **by cutting question count, not by extending time** (D-030):
   - (a) cut **pure-revision** items first (the optional "one revision item" a homework may carry, REF-07 §2.2);
   - (b) then reduce counts on the **lightest-priority subject(s)** for today;
   - (c) then **zero-out** a subject's homework for the day (permitted — D-030 rule 4).
   Repeat until day total ≤ ceiling.
5. **Log.** Record each subject's homework as a `HW-…`-numbered item with its `TOP-…` tag(s) in the Homework Tracker, and log any trim made in step 4 (the Homework Tracker captures the reduction — REF-02 §2.7 rule 3).
6. **Thursday — light homework + weekend handoff.** Thursday's reduced schedule (Class 1–2: Quran + Arabic + weekly tests) **may still set some light daily homework** from the subjects that met; tally and reconcile it exactly like any school night (steps 2–5), just smaller. In addition, the **weekly assignment** (`AS-…`) goes home for the weekend (§3) — worked Fri+Sat, so it does not overlap Thursday night's light homework. The class teacher confirms both the (light) Thursday homework and the assignment are issued and logged.

> **One common sheet.** Every child gets the same `HW-…` items. A weak child does **not** receive a different or longer sheet here; their extra practice arrives reactively through the §4.3 top-up and REF-07's fail-driven loop, never through a pre-planned per-student worksheet.

### 2.4 The weekend rule

- **Friday and Saturday carry NO academic daily homework.** The only scheduled academic out-of-class work on the weekend is the **weekly assignment** (`AS-…`).
- The weekly assignment is **given Thursday, worked over Fri + Sat, collected Sunday** (D-014, as REF-07 §2.3 confirms).
- **Weekend time cap (set here): 4 hrs per day × 2 days = 8 hrs**, average student. REF-08 owns this cap; **REF-07 owns what fills the assignment** (this-week items + cumulative reach-back + pre-big-exam maintenance) and trims from the bottom if it would exceed the 8-hr cap.
- **Daily Quran muraja'ah continues on Fri + Sat — additional, and OUTSIDE the 8-hr cap** (Principal direction 2026-05-22). It is a protected daily discipline: a few minutes of tilawah / hifz revision, tracked in the Quran Tracker (D-014), not academic homework. So a weekend day = up to 4 hrs assignment **plus** the short Quran touch on top.
- **No double-counting (academic):** weeknights carry `HW-…` (worked that night); the weekend carries `AS-…` (worked Fri+Sat). The two academic caps **add** rather than overlap — a child never works both academic channels on the same night.

### 2.5 The weekly load roll-up (Principal transparency)

So the totals are visible and never blow up unseen, here is the full weekly out-of-class load for an **average** Class 1 student:

| Days | Channel | Typical (floor) | Heavy (ceiling) |
|---|---|---|---|
| Sun–Wed (4 nights) | Daily homework | 4 × 120 min = **8 hrs** | 4 × 240 min = **16 hrs** |
| Thursday | Light daily homework (reduced roster) + assignment issued | ~0.5 hr | ~1 hr |
| Fri + Sat | Weekly assignment | **8 hrs** | **8 hrs** |
| **Weekly total** (academic) | | **≈ 16–17 hrs** | **≈ 25 hrs** |

*Plus daily Quran muraja'ah — a few minutes every day including the weekend, **additional and outside** these academic figures (§2.4, §2.6).*

The **typical** week (~16–17 hrs) is the realistic norm; the ceiling week (~25 hrs) is only hit if nearly every subject runs heavy every weeknight, which the §2.3 trim is designed to prevent. *If, in pilot, 4 hrs on a heavy weeknight proves too much in practice, the ceiling is yours to lower at review — this roll-up exists precisely so that judgment is made on visible numbers, not by surprise.* (REF-08 does not re-open D-024; it surfaces the arithmetic D-024 implies.)

### 2.6 The average-student framing (important)

Every figure above is a **design target for the average student**, not a hard per-student limit:
- **Fast / meritorious students** finish the common sheet well under the time budget. That spare capacity is theirs — REF-08 does not manufacture filler to consume it.
- **Weak students** take longer than the budget on the same common sheet, and may receive **reactive top-ups** (§4.3) that push their personal time *over* the ceiling. **This is accepted and expected** — the extra time is the support the weak child needs, given moderately (al-Baqarah 2:286: the burden matches capacity, and a struggling child's capacity is met with help, not with a harder cap).
- The teacher sets the common **question count** so the *average* child lands inside the time budget. The count is therefore the lever (D-030); the time is the design target the count is tuned to.

---

## §3 — Daily homework vs weekly assignment — the boundary

The two channels look similar (both are out-of-class practice, both numbered, both topic-tagged) but are owned by different documents and must never double-count a child's load. This table is the contract.

| | **Daily homework** | **Weekly assignment** |
|---|---|---|
| **ID** | `HW-{class}-{SUBJECT}-{nnnn}` | `AS-{class}-{SUBJECT}-{nnnn}` |
| **Primary job** | Reinforce **today's** lesson (+ optionally one revision item) | **Revision workhorse** — this-week items + cumulative reach-back + pre-big-exam maintenance |
| **When** | School nights (Sun–Thu; lighter on Thu) | Given Thu / worked Fri+Sat / collected Sun |
| **Time cap** | 2–4 hrs/day, per-subject 0–40 min — **set by REF-08** (§2) | 8 hrs over the weekend — **cap set by REF-08**, **content set by REF-07** |
| **Owned by** | **REF-08** (this document) + Homework Tracker | **REF-07** + Assignment Tracker |
| **Questions drawn from** | the topic's Project 04 Pool for the day's lesson | the Project 04 Pools of the week's + reach-back topics (REF-07 §2.3) |
| **Tracked in** | Homework Tracker (daily) | Assignment Tracker (weekly) |

**The no-double-count rule (restated).** Weeknights (Sun–Thu) carry `HW-…`, worked that night; the weekend carries the `AS-…` assignment, worked Fri+Sat. Thursday may carry *light* daily homework **and** is the assignment handoff day — no overlap, because Thursday's homework is done Thursday night while the assignment is done over the weekend (§2.3 step 6). This is why the two caps (2–4 hr weekday, 8 hr weekend) **add** rather than overlap, and the §2.5 roll-up is honest. (Daily Quran muraja'ah sits outside both caps — §2.4.)

**Where REF-07 and REF-08 meet.** REF-07 §1.4 explicitly routes "homework/assignment time caps → REF-08." This document supplies them: the daily ceiling (§2.1) is the cap REF-07 §2.2 assumed for daily homework, and the 8-hr weekend cap (§2.4) is the cap REF-07 §2.3 trims the assignment against. With REF-08 locked, REF-07's lone open dependency on the time budget is closed (see §10 and the chat-close reconciliation).

---

## §4 — The Homework Question Pool

REF-08 governs **how the topic's Project 04 Pool is sized and used**; Project 04 authors and owns the canonical questions, linked to the plan by topic tag (REF-02 §2.8 retired — D-051).

> **Two-tier scope (added v1.1, master D-050).** Under REF-02 v1.3, the Pool now lives at **chapter scope** — one Pool per chapter, authored on the **Chapter Plan** (the Pool ID `QP-{SUBJECT}-C{class}-U{nn}` covers the whole chapter; in the v1.3 token scheme `U` = chapter). Each **Session Plan** carries a **homework slice** from this Pool (named in the §2.9 Session Map row), not its own separate Pool. The **20-question floor** (§4.1) is read at **chapter** level: a chapter ≥ 20, not each session ≥ 20 — which is the same constraint as v1.0 for single-period chapters (one session = one chapter) and a *looser* constraint for multi-period chapters (the Pool no longer multiplies by session count). The **daily time cap** in §2 (Daily Homework Budget) is unchanged and stays **per session** (a child's daily load is the sum of that day's session-slices, not the chapter Pool). The pre-class-test top-up (§4.3) still pulls from the chapter Pool. Single-period chapters look identical to v1.0; multi-period chapters reduce the authoring burden (one Pool, sliced per session) without changing any cap.

### 4.1 Sizing (D-028) — and *why* 20
**Minimum 20 questions per lesson Pool.** The 20-minimum is not arbitrary; it is sized to sustain **two** demands at once without running dry:
1. **Routine rotation** across the year — the same lesson's homework may be assigned several times for revision; the Pool must not repeat the same questions each time (REF-02 §2.8 rule 1 / rule 6).
2. **Reactive top-ups** (§4.3) — when a weak student needs extra reps, the teacher pulls additional questions from the *same topic's* Pool without authoring anything new.
A Pool of, say, 8 would be exhausted by routine use alone and leave nothing for top-ups. **The 20-question floor is held; the threshold review is parked to the post-pilot retrospective** (TODO Open decision, confirmed 2026-05-22). Each Pool question is Bloom's-tagged and carries an answer key (or a rubric, if open-ended) — D-028.

### 4.2 Placement (D-051, supersedes D-029) and the time-vs-count rule (D-030)
- **In Project 04.** The Pool lives in Project 04 (canonical bank → per-(class × subject) master → register, in Drive); ID `QP-{SUBJECT}-C{class}-U{nn}` (chapter scope). **The plan carries no Pool** — no inline copy, no reference; a plan links to its questions only by the topic tag (`TOP-…`) the Spine declares. D-051 supersedes D-029 (inline placement); D-030 time-vs-count is unchanged.
- **Time is the firm cap; count is the lever (D-030).** §2.7 sets the day's *time* for this subject; the teacher then selects `Y` questions from the Pool, where `Y` is the guideline count tuned so the **average** student finishes inside that time. On a heavy day the teacher may raise `Y` toward the count's top (still inside the 40-min subject band); on a light day, lower it; if the day's tally would breach the ceiling, the teacher **cuts `Y`, never extends the clock** (§2.3 step 4).

### 4.3 How the Pool feeds routine homework *and* the pre-class-test top-up
The same Pool serves both flows — this is the efficiency of sizing it at 20:
- **Routine (every assigning day).** The teacher selects `Y` questions for the day's `HW-…`, satisfying the §2.7 traceability rule (each item ties to today's §2.2 must-cover content *or* a §2.6 Revision Anchor item).
- **Pre-class-test weak-student top-up (the bounded catch-up).** In the window before a chapter's class test, a student flagged by the fail-driven loop (REF-07 §4) may receive a **top-up**: a few **extra questions on the failed topic, selected from that topic's existing Pool** (REF-07 §4.1). Boundaries — all inherited from REF-07 so the two documents agree:
  1. **Selected, never authored.** Pulled only from the ready ≥20-question Pool.
  2. **Reactive only.** Triggered by a failure flag in the tracker — never a pre-planned per-student schedule.
  3. **Time-bounded.** The top-up's minutes count toward the child's daily load; on a top-up day the teacher trims the child's other `HW-…` to make room (the average-student ceiling still governs; a weak child may run over per §2.6).
  4. **Tracked as a resubmission**, not a new stream — the existing resubmission stage of the Homework Tracker lifecycle (REF-07 §4.1 / TODO 6.1) carries the re-issued numbered sheet + the top-up flag + its own due/submitted/checked.

---

## §5 — Plumbing: IDs, topic tags, Homework Tracker integration

### 5.1 Every homework item is numbered and topic-tagged
Each daily homework carries:
- a **unique ID** — `HW-{class}-{SUBJECT}-{nnnn}` (running number per class+subject; term-resettable or continuous is the tracker-designer's call), so the term's homework **count** is just a count of IDs; and
- one or more **`TOP-…` topic tags** — `TOP-{SUBJECT}-C{class}-{nn}` — linking the item to the topic(s) it covers on the REF-07 topic-wise revision chart.

The **ID format and the tracker fields that hold ID + tag are Project 06's** (TODO Day 6 step 6.1 / REF-07 §3.5). REF-08 owns the *requirement* that daily homework be generated already carrying them, and specifies (above) *how §2.7/§2.8 produce the items* that receive them.

### 5.2 What the tags buy (feeding the revision chart)
Because every `HW-…` carries its `TOP-…` tag(s), REF-07's machinery reads off them directly with **no extra logging**:
- the topic-wise revision chart's "daily homework" channel is satisfied when a `TOP-…`-tagged `HW-…` is delivered;
- the Master Tracker counts **touches per topic** from the `TOP-…` tags (REF-07 §5.2);
- a re-issued sheet is traceable by its unchanged `HW-…` ID (§4.3 / REF-07 §4.1).

### 5.3 Homework Tracker integration — **no 9th tracker** (D-013)
Daily homework is logged in the **existing Homework Tracker** (daily cadence, D-014); the pack stays at 8 (D-013). REF-08 adds **no new tracker** and **no new in-class logging field** — the two `REV_…` fields REF-07 added live on the Lesson Completion Tracker, not here. The Homework Tracker must support, within the shared 6-stage lifecycle built once for Homework + Assignment (TODO 6.1):
- the per-item **`HW-…` ID** and **`TOP-…` tag(s)** (§5.1);
- the **daily per-student load roll-up** — the instrument that makes the §2.3 day-total visible and the trim auditable (this *is* the reconciliation tool, not a new artefact);
- the **trim log** (which item was reduced/zeroed and by how much — REF-02 §2.7 rule 3);
- the **resubmission stage with optional top-up flag** (§4.3);
- columns in **Bangla labels + English codes** (Instructions §5).

> The Homework Tracker is the only place the daily ceiling becomes real: §2 sets the number, but the tracker's daily roll-up is what lets the class teacher *see* the day total in step 2–3 and the Principal *see* the weekly load (§2.5). Wiring this roll-up is the Project-06 deliverable REF-08 depends on.

---

## §6 — Worked example (a Class 1 week) + teacher quick-card

### 6.1 Worked example — Class 1, one ordinary week

Six daily subjects Sun–Wed (Bangla, English, Math, Quran, Arabic, Islam); Thursday is Quran + Arabic + weekly tests; assignment goes home Thursday for the weekend.

- **Sunday (a heavy Bangla day).** Bangla introduced two new vowels → §2.7 sets **40 min** (`HW-C1-BAN-0021`, tagged `TOP-BAN-C1-04`, `TOP-BAN-C1-05`). Math normal **20** (`HW-C1-MATH-0019`), English **20**, Islam **20**, Arabic **20**, Quran **20** (tilawah of the day's ayah). **Day total = 140 min** — under the 240 ceiling → issue as planned. Class teacher logs all six in the Homework Tracker.
- **Monday (everything heavy at once — the rare overflow).** Bangla 40, English 40, Math 40, Arabic 40, Islam 40, Quran 20 → tally **220** … then Math's lesson also wants to carry a *revision* item (+20) → **240+**. The class teacher applies §2.3 step 4: cuts the optional Math revision item first (back to 240), and since it's still at the very top, drops English's count so English falls to 30. **Day total ← 230 min**, inside the ceiling. The two trims are logged.
- **Tuesday / Wednesday.** Mostly default 20s; day totals near the 120 floor. A light Wednesday (review-only lessons) sets two subjects to **0 homework** — permitted (D-030 rule 4); day total ~80 min.
- **Thursday (light day).** Quran + Arabic classes run and may set a *little* daily homework (e.g. a short Quran tilawah review + one Arabic item) — tallied and reconciled like any night, just small. The **weekly assignment** `AS-C1-BAN-0006` (+ the week's other subjects, REF-07-built, ≤ 8-hr cap) also goes home for the weekend, logged in the Assignment Tracker.
- **Fri + Sat.** Weekly assignment only; the average child spends ~4 hrs each day on it. No academic `HW-…`. Daily Quran muraja'ah still happens — a few minutes, additional and outside the 4-hr cap (§2.4).
- **Sunday (next week).** Assignment collected; the cycle resumes.
- **A weak child this week:** got two Bangla vowels wrong on Sunday's `HW-C1-BAN-0021` → resubmission of the same sheet, plus (because a chapter test is near) a **top-up** of 3 extra vowel questions selected from `QP-BAN-C1-U1-L?`'s Pool (§4.3). Logged as a resubmission with the top-up flag; their personal time ran ~25 min over the day's budget — accepted (§2.6).

### 6.2 Teacher quick-card (the whole budget on one card)
1. **Per lesson:** set today's homework time in the **0–40 min** band by how heavy the topic was (default 20; **0** is allowed). Pick `Y` questions from the topic's Project 04 Pool to fit that time for the *average* child.
2. **End of day (class teacher):** **add up** every subject's homework time. Over the **ceiling** (Class 1 = 240 min)? **Cut question counts** — revision items first, then lightest subject, then zero a subject — until it fits. Never extend the clock.
3. **Number + tag** every sheet (`HW-…` + `TOP-…`) and log it; log any trim.
4. **Thursday (light day):** a *little* daily homework may go home **and** the **weekly assignment** goes home for the weekend.
5. **Fri/Sat:** assignment only (no academic homework). Daily Quran muraja'ah still happens — on top, outside the cap.
6. **Weak child got it wrong?** Re-issue the same numbered sheet (+ optional Pool top-up before a class test); track it as a resubmission. Their extra time is fine.
7. **Never** let a single child's day quietly climb past the ceiling unseen — the Homework Tracker's daily roll-up is there so it can't.

---

## §7 — Checklists (author + tracker-designer + teacher)

### 7.1 Lesson-plan author (Project 03) — before publishing §2.7 / §2.8
- [ ] §2.7 time budget is inside the per-subject band (Class 1: 0–40 min) and consistent with the class's daily ceiling.
- [ ] §2.7 guideline count `Y` is tuned so the **average** student finishes inside the time budget.
- [ ] §2.7 Bloom's distribution is Remember/Understand-heavy for primary (REF-06 §3.6), aligned with §2.3.
- [ ] §2.7 traceability holds — every homework item ties to today's §2.2 must-cover content *or* a §2.6 Revision Anchor item.
- [ ] §2.7 honestly allows **zero** where the lesson warrants none.
- [ ] The topic's Project 04 Pool (≥20, default 30) is in place — Bloom's-tagged, keyed/rubric'd, F-01 + Curation-Policy clean (built in Project 04, not the plan).
- [ ] Every Pool/homework item is ready to be numbered (`HW-…`) and topic-tagged (`TOP-…`) on delivery.

### 7.2 Tracker-designer (Project 06) — before wiring the Homework Tracker
- [ ] **No 9th tracker** — daily homework rides the existing Homework Tracker (§5.3).
- [ ] Homework Tracker carries the **`HW-…` ID** and **`TOP-…` tag(s)** per row.
- [ ] The **daily per-student load roll-up** is built (the §2.3 reconciliation instrument).
- [ ] The **trim log** field is built (which item reduced/zeroed, by how much).
- [ ] The shared **6-stage lifecycle** (TODO 6.1) — including **resubmission + optional Pool top-up** (§4.3) — is built once and shared with the Assignment Tracker.
- [ ] Columns use **Bangla labels + English codes** (Instructions §5).

### 7.3 Class teacher (daily coordinator) — every school day
- [ ] Collected every subject's §2.7 declaration for today.
- [ ] Tallied the **day total** across subjects that met today.
- [ ] Day total ≤ this class's ceiling — or trimmed by count (§2.3 step 4) until it is.
- [ ] Every sheet numbered, tagged, logged; any trim logged.
- [ ] Thursday: weekly assignment issued and logged instead of weeknight homework.

---

## §8 — Design note: why floating, not fixed

A fixed per-subject split ("Bangla 30 / Math 30 / …") was considered and rejected. The honest reasoning:
- **Topic load is not flat.** The day Bangla introduces two vowels is not the day Math introduces nothing new. A fixed split would either starve the heavy subject or pad the light one — every single day.
- **A fixed split fights the §2.7 field we already have.** REF-02 §2.7 already lets each lesson declare its own homework time. A fixed table would override that field; the floating method *uses* it.
- **The ceiling is the real constraint, not the split.** What protects the child is the **total** staying under the daily cap — and that is enforced by one tally + one trim rule (§2.3), far simpler than policing six fixed sub-budgets.

So REF-08 fixes the **ceiling** (firm, per class) and the **band** (0–40 min, to keep any one subject sane), and lets the **split float** with real lesson load, reconciled daily. *Bound the time, float the split, protect the child.*

---

## §9 — Roles & responsibilities

| Role | Owns |
|---|---|
| **Subject teacher** | Setting today's §2.7 time + `HW-…` items within the band; picking `Y` from the topic's Project 04 Pool |
| **Class teacher (daily coordinator)** | The §2.3 tally + trim; numbering, tagging, logging; Thursday assignment handoff |
| **Lesson-plan author (Project 03)** | A well-formed §2.7 / §2.8 per §7.1 |
| **Subject Spine Playbook author (REF-03)** | The filled topic chart whose `TOP-…` tags homework carries |
| **Tracker-designer (Project 06)** | Homework Tracker integration §5.3 + the shared lifecycle |
| **Subject Lead** | Reviewing teacher question-substitutions and trim patterns (is one subject always being trimmed?) |
| **Principal** | The weekly load roll-up (§2.5); confirming/adjusting the ceiling at review |

---

## §10 — Open dependencies, decisions for review, version log

### 10.1 Open dependencies
- **REF-03 (Bangla topic chart, Day 5).** Supplies the `TOP-…` codes homework tags point at. REF-08 is not blocked by it (tags are referenced, not authored here).
- **Project 06 Homework Tracker (Day 6 step 6.1).** Must build the daily roll-up, trim log, IDs/tags, and shared lifecycle (§5.3). The daily ceiling is only *enforceable* once this exists.
- **Project 04 Pools (Day 7+ / production).** Supply the ≥20-question Pools the daily homework and §4.3 top-ups draw from.

### 10.2 Decisions for the Principal (this draft)
**Confirmed by your direction 2026-05-22 (folded into this draft):**
- **A. Floating allocation, not a fixed split** (§2.2) — per-lesson §2.7, daily-reconciled, ceiling-bounded.
- **B. Pool minimum stays 20 questions** (§4.1); threshold review parked to post-pilot.
- **C. Weekend = weekly assignment only** (academic), 4 hrs/day × Fri+Sat = 8-hr cap (§2.4); no weekend academic daily homework.
- **D. Ceilings are average-student design targets** (§2.6); fast students finish under, weak students may run over with top-ups.
- **E. Rosters** — Class 1–2: six daily subjects, Thursday = Quran + Arabic + weekly tests; Class 3–5: Quran/Arabic daily, Bangla/English/Math ×4, BGS/Science/Islam ×2 (§2.1–§2.2).
- **F. Weekend Quran muraja'ah** (§2.4) — done daily including Fri+Sat, **additional and outside** the 8-hr assignment cap (your direction 2026-05-22). *(Resolves the prior open question.)*
- **G. Thursday carries light daily homework** in addition to the assignment handoff (§2.3 step 6, §3) — not the zero-homework day the v0.1 draft assumed.

**Resolved at lock (Principal direction 2026-05-22):**
1. **Master-README D-036 — APPLY NOW.** The floating-allocation method is adopted as an initiative-wide locked master decision (text below); added to README §3 via the propagation flag (§10.3 step 2).
2. **Classes 1–5 ceilings — UNIFORM.** All classes 1–5 share one ceiling: 2–4 hrs daily / 8 hrs weekend (§2.1). The earlier "provisional for 2–5" posture is dropped.
3. **The 4-hr weekday ceiling — CONFIRMED.** The §2.5 roll-up (heavy week ~25 hrs academic) is accepted; the weekday ceiling stands.

**Adopted master-README decision (D-036), applied at this lock:**
> **D-036** | Daily homework uses a **floating per-subject allocation within a firm daily ceiling**, set per-lesson via REF-02 §2.7 and reconciled daily by the class teacher (tally; trim by question count, not time, if over the ceiling). The split across subjects is **not** fixed. Per-class daily ceilings live in REF-08; **Classes 1–5 share a uniform ceiling of 2–4 hrs daily / 8 hrs weekend** (Class 1 per D-024; extended to Classes 2–5 by Principal direction 2026-05-22). Initiative-wide. Source: REF-08 v1.0, Principal direction 2026-05-22. | 2026-05-22

### 10.3 Chat-close sequence (at this lock — 2026-05-22)
With REF-08 locked, the following propagation runs (Claude drafts each patch; Principal applies in the project UI):
1. Flip REF-08 ⏳ → ✅ in `PROJECT00_CROSS_PROJECT_INDEX.md`; bump it + its version log.
2. Log **D-PROJ00-010** (REF-08 production) in `PROJECT00_DECISIONS.md`; add **D-036** to master README §3 (per §10.2 item-1 "apply now") and record the propagation in the flags table.
3. Patch `PROJECT00_GLOSSARY.md` — *Daily Homework Budget*, *Homework Specification*, *Homework Question Pool* refreshed; add *Homework Architecture*.
4. Reconcile `PROJECT00_TODO.md` step 6.3 → done; resolve the "REF-08 per-class-per-subject allocations" Open decision.
5. **REF-07 reconciliation — Principal's call (Claude will not edit locked REF-07 without it).** REF-07 v1.0 lists REF-08 as an "open dependency — not yet locked." Now that REF-08 is locked, either **(a)** supersede REF-07 → v1.1 to mark the dependency resolved (archiving v1.0), or **(b)** log the resolution in DECISIONS and leave the locked REF-07 file untouched. *(Awaiting Principal choice.)*
6. Produce the handoff to Project 00 `/handoffs/`.

### 10.4 Version log
| Version | Date | Change | By |
|---|---|---|---|
| v0.1 | 2026-05-22 | Initial draft. Daily Homework Budget governance (§2): per-class ceiling (Class 1 authoritative per D-024; 2–5 provisional), the floating-allocation method + daily reconciliation procedure, weekend rule (assignment-only, 8-hr cap), weekly load roll-up, average-student framing. Boundary contract daily `HW-…` (REF-08) vs weekly `AS-…` (REF-07) (§3). Pool sizing/placement/time-vs-count + routine-and-top-up feed (§4). Plumbing: `HW-…` IDs, `TOP-…` tags, Homework Tracker integration, no 9th tracker (§5). Worked week + quick-card (§6), checklists (§7), design note (§8), roles (§9), open items incl. proposed master D-036 (§10). | Claude (drafted); Principal (review pending) |
| v0.2 | 2026-05-22 | **Two Principal refinements (2026-05-22).** (a) **Weekend Quran** (§0 table, §1.4, §2.4, §2.5, §6, §10.2-F): daily Quran muraja'ah is done on Fri+Sat too, **additional and outside** the 8-hr assignment cap — resolves the v0.1 open question. (b) **Thursday homework** (§0 table, §2.2, §2.3 step 6, §3, §2.5, §6, §10.2-G): school nights are Sun–Thu — Thursday may carry *light* daily homework (reduced roster) in addition to the assignment handoff, not the zero-homework day v0.1 assumed; §2.5 roll-up + totals adjusted (~25 hr heavy week). §10.2 "for decision" list trimmed to three (D-036; Class 2–5 ceilings; weekday-ceiling sanity-check). | Claude (drafted); Principal (review pending) |
| **v1.0** | **2026-05-22** | **LOCKED.** All three review decisions resolved by the Principal: **D-036 applied now** (floating-allocation method → master README §3); **Classes 1–5 ceiling made uniform** (2–4 hr daily / 8 hr weekend — §2.1, dropping the provisional 2–5 posture); **4-hr weekday ceiling confirmed** (§2.5). §0 table caps relabelled Classes 1–5; §2.1 collapsed to one uniform row + "uniform ceiling, flexing band" note; §2.2 variable-roster note pointed at the uniform ceiling; §10.2 flipped to "resolved at lock"; §10.3 reframed as the executing chat-close sequence (REF-07 reconciliation pending Principal a/b). No content changes to §1, §3–§9 beyond the uniform-ceiling edits. | Claude (drafted); **Principal (approved + locked)** |
| v1.1 | 2026-05-29 | **D-050 ripple (workstream-b item b.6).** Scoped two-tier acknowledgement: §4 gains a callout noting the Homework Question Pool now lives at **chapter scope** (one Pool per chapter on the Chapter Plan; each Session Plan carries a homework slice from the §2.9 Session Map row); the 20-question floor reads at chapter level (loosens for multi-period chapters; identical to v1.0 for single-period); the daily time cap (§2) stays per session, unchanged. No figure, cap, or governance change. Status banner records the supersede. Supersedes v1.0 (→ `/archive/`). Cross-reference: `LOCKED_REF-02_Three_Layer_Lesson_Plan_Template_v1_3.md` §2.8 + §2A; `PROJECT00_TODO.md` workstream-b item b.6. | Claude (drafted); Principal (approval pending) |
| v1.2 | 2026-05-31 | **Back-pointer footer added (D-PROJ00-062).** New "Downstream — built-asset dependents" footer records that this reference is a source of `LOCKED_ProductionCore_v1` (Project 03 built asset; Core §5 homework author-rule) and that a supersede triggers a Core rebuild (Core §7 / Build Policy §6; change-time trigger README §5.3/§5.4, dependency record CROSS_PROJECT_INDEX, D-PROJ00-061). **Payload-neutral — no change to §1–§10 content;** the footer itself does not make the Core stale. Supersedes v1.1 (→ `/archive/`). | Claude (drafted); Principal (approval pending) |
| v1.3 | 2026-05-31 | **Master D-051 (supersedes D-029): Homework Question Pool moves to Project 04.** §4.2 placement repointed (inline → Project 04, linked by topic tag); §0 / §1.4 / §7.1 / §9 Pool references updated; budget (§2), boundary (§3), and tracker plumbing (§5) unchanged. Payload change. Supersedes v1.2 → /archive/. | Claude (drafted); Principal (apply on confirm) |
---

## Downstream — built-asset dependents (back-pointer · D-PROJ00-062)

**This reference is a source of `LOCKED_ProductionCore_v1`** (Project 03 built asset): it supplies **Core §5** — the homework author-rule + checklist (chapter-scope Homework Question Pool at Spine §2.8; per-session homework slice + daily-cap budget at Spine §2.7). A supersede of this file makes the Production Core **stale → rebuild required** before any new Chapter/Session Plan is built off it — see Core §7 and `LOCKED_ProductionAsset_Build_Policy_v1` §6 (Project 03), the change-time trigger in `PROJECT00_README.md` §5.3/§5.4, and the dependency record in `PROJECT00_CROSS_PROJECT_INDEX.md` (D-PROJ00-061).

*Payload scope:* the rebuild trigger fires on a change to the **extracted payload** (the Core §5 content). A payload-neutral edit — such as this back-pointer footer (the v1.1 → v1.2 supersede that introduced it) — supersedes the file but does **not**, by itself, make the Core stale.
