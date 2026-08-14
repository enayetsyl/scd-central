# REF-07 — Revision Architecture (Canonical)

**Status:** v1.2 (**LOCKED** 2026-05-31 — back-pointer footer added recording the Production-Core source dependency, D-PROJ00-062; **payload-neutral, no rule change**; supersedes v1.1 → `/archive/`.) *Earlier: v1.1 (LOCKED 2026-05-29 — D-050 ripple, workstream-b item b.5; supersedes v1.0 → `/archive/`. Drafts v0.1–v0.5 retained as history.)* **v1.1 = scoped two-tier acknowledgement from master D-050 (REF-02 v1.3):** the triggered Hook-recall channel is renamed the **within-chapter revision strand** (session N revisits N−1, inside one Chapter Plan, governed by the §2.9 Session Map); the rest of REF-07's machinery (daily homework, weekly assignment, chapter-stop gate, maintenance track) is the **cross-chapter strand**, unchanged. No tracker, schedule, or operational change.
**Project:** 00 — Curriculum Foundations
**Date created:** 2026-05-21 (v0.1); 2026-05-21 (v0.2 same day, simplified per Principal feedback)
**Owner:** Principal
**Author:** Claude (drafted); Principal (approval pending)
**Source decisions:** D-022 (Revision Anchor field), D-026 (REF-07 exists — *operational expression refined by this version; recorded in D-PROJ00-007*), D-PROJ00-007 (REF-07 production + D-026 refinement + two-tier stop), D-025 (exit-check thresholds → failure-driven revision), D-033 (Hook MANDATORY), D-014 (tracker cadences — Assignment given Thu / collected Sun; Master Tracker review **monthly, confirmed 2026-05-21**), D-013 (8 trackers), D-024 (Daily Homework Budget), D-020 (Salafi framing).
**Companion documents:**
- `LOCKED_REF-02_Three_Layer_Lesson_Plan_Template_v1_1.md` — §2.6 Revision Anchor (now *read off* the topic chart, §3.4); §3.2 Hook.
- `PROJECT00_GLOSSARY.md` — Revision Anchor / Revision Architecture.
- REF-03 (Bangla Subject Spine Playbook, Day 5) — **holds the filled topic-wise revision chart per subject** (§3.3). *(Open dependency.)*
- REF-08 (Homework Architecture, Day 6) — sets the homework/assignment time caps this document obeys. *(Open dependency.)*
- Project 06 trackers — Assignment, Homework, Class Test, Lesson Completion, Master. The homework/assignment **lifecycle** lives there (TODO Day 6 step 6.1), not here.

---

## §0 — Summary (read this first)

**The one principle.** Revision matters, but **most revision happens *outside* class time** — in homework, in the weekly assignment, and in the per-chapter class test. Class time is for teaching. This keeps the system important *and* manageable.

**What REF-07 is.** A small, fixed set of revision channels plus one **topic-wise revision chart per subject** that says, for each topic, when it gets revisited and through which channel. The chart is the backbone; the channels are how it happens; the trackers report whether it happened.

**The revision channels:**

| Channel | When | Revision role | Logged in |
|---|---|---|---|
| **In-class, at the Hook** | Triggered only (not every class) — when the lesson *builds on* the last, or a student/cohort *failed* the last exit-check | Light recall warm-up | Lesson Completion Tracker |
| **Daily homework** | After most lessons | Reinforces today's lesson; may carry one revision item | Homework Tracker |
| **Weekly assignment** | Once a week — **given Thursday, collected Sunday** | The revision workhorse: this week's items **+** cumulative reach-back (incl. exam-horizon maintenance) | Assignment Tracker |
| **Per-chapter class test** | Per chapter | Assessment checkpoint **and the chapter-stop gate** — a topic that passes leaves the *dense* ladder and drops to a low-frequency maintenance track (§2.4) | Class Test Tracker |
| **Pre-exam in-class revision** | Before term exams | **Out of scope** — teacher's own classroom revision (distinct from exam-horizon maintenance, which rides the weekly assignment) | — |

**Two-tier stop (important).** "Retained" is **not** "done forever." Passing the chapter test ends the *dense early ladder* (R1→R2→R3) but the topic joins a **low-frequency maintenance track**: before the **half-yearly and annual exams** (those two horizons only), the weekly assignment's existing cumulative reach-back draws a light, rotating pass over maintenance topics so nothing on the exam goes cold (§2.4). No new channel, no revision day.

**Islamic grounding.** Scheduled revision is **muraja'ah** — the discipline by which the Qur'an is retained. The Prophet (ﷺ) likened forgetting memorised Qur'an to a hobbled camel that slips away once untied (agreed upon — al-Bukhari and Muslim). REF-07 extends that same return-and-retain discipline (already lived daily in the Quran Tracker) to every subject, *without* turning it into a heavy administrative load.

**Who acts on what:**
- **Teacher** → §2 (the channels) and §6 (worked example / quick-card).
- **Lesson-plan author (Project 03)** → §3.4 (read §2.6.c off the chart) and §7.1 checklist.
- **Subject Spine Playbook author (REF-03)** → §3 (build the subject's filled chart).
- **Tracker-designer (Project 06)** → §5 (the thin coverage view).

---

## Quick-Navigation Checklist (staff-facing)

- [§0 — Summary](#0--summary-read-this-first)
- [§1 — Purpose, scope, and the design principle](#1--purpose-scope-and-the-design-principle)
- [§2 — The revision channels](#2--the-revision-channels)
- [§3 — The topic-wise revision chart (the backbone)](#3--the-topic-wise-revision-chart-the-backbone)
- [§4 — Failure-driven revision (the D-025 link)](#4--failure-driven-revision-the-d-025-link)
- [§5 — Tracking & principal visibility (kept thin)](#5--tracking--principal-visibility-kept-thin)
- [§6 — Worked example + teacher quick-card](#6--worked-example--teacher-quick-card)
- [§7 — Checklists (author + tracker-designer)](#7--checklists-author--tracker-designer)
- [§8 — Design note: does in-class revision hurt the 35-minute lesson?](#8--design-note-does-in-class-revision-hurt-the-35-minute-lesson)
- [§9 — Roles & responsibilities](#9--roles--responsibilities)
- [§10 — Open dependencies, decisions for review, version log](#10--open-dependencies-decisions-for-review-version-log)

---

## §1 — Purpose, scope, and the design principle

### 1.1 Purpose
Stop content being taught once and never returned to. Give every topic a small, predictable schedule of return that a teacher can run without extra paperwork and that the Principal can see at a glance.

### 1.2 The design principle (governs every choice below)
**Keep it simple and operationally manageable. Push revision out of class time wherever possible.** A revision system that eats teaching minutes or buries teachers in tracking will not be used. So: in-class revision is *triggered, not blanket*; routine spaced revision lives in homework and the weekly assignment; tracking is a thin coverage signal, not a per-student state machine.

### 1.3 Scope (in)
The revision channels (§2); the two-tier stop and exam-horizon maintenance rule (§2.4); the topic-wise revision chart template with standard `TOP-…` IDs (§3); the failure-driven rule incl. bounded re-do + Pool top-up (§4); the requirement that homework/assignment be numbered and topic-tagged (§3.5); the thin principal coverage view (§5).

### 1.4 Scope (out — redirect)
- **Filled per-subject charts** → Subject Spine Playbooks (REF-03+). REF-07 gives the template only.
- **Tracker construction + the homework/assignment lifecycle** → Project 06 (TODO Day 6 step 6.1).
- **Question authoring** → Project 04 (REF-07 only says revision questions come from the §2.8 Pool).
- **Homework/assignment time caps** → REF-08.
- **Pre-exam in-class revision** → out of scope entirely; teacher's classroom call.
- **Per-chapter class test design** → Project 06 / Project 04; REF-07 only uses its *result* as the stop-rule.

### 1.5 What REF-07 is *not*
Not a new lesson layer, not a new field, not a separate "revision day." It adds **one** new artefact — the per-subject topic chart — and otherwise just routes existing channels.

---

## §2 — The revision channels

> **Two strands under REF-02 v1.3 (added v1.1, master D-050):**
> - **§2.1 = the *within-chapter* revision strand** — Hook-located, session N revisits session N−1, *inside one Chapter Plan*. Governed by the Chapter Plan's §2.9 Session Map (REF-02). REF-07 does not schedule it (the Chapter Plan does); REF-07 only names it here so the two strands are not confused.
> - **§§2.2–2.4 + §3 chart = the *cross-chapter* revision strand** — daily homework / weekly assignment / chapter-stop gate / maintenance track, all running *across* chapters. This is REF-07's primary domain, unchanged from v1.0.
> The fail-driven loop (§4) crosses both strands: an exit-check miss in session 3 of a multi-period chapter can be addressed in session 4's Hook (within-chapter) *and* picked up by the next weekly assignment (cross-chapter).

### 2.1 In-class, at the Hook — *triggered, not blanket* — **within-chapter strand**

**The Hook's real purpose** (correcting any earlier wording): the Hook exists to **capture students' attention at the very start of the lesson and get them engaged so they stay engaged throughout**. That is why it is MANDATORY (REF-02 §3.2, D-033). Revision is *one optional way* to spend Hook time — not the reason the Hook exists.

**When revision rides on the Hook** (only these two triggers):
1. **Build-on** — this lesson genuinely depends on the previous one. A quick recall warm-up of the prior content *helps the new lesson land*, so it is a runway, not a tax.
2. **Fail-driven** — a student or cohort failed the last exit-check (§4); the next Hook targets that specific gap.

If neither trigger applies, the Hook is pure engagement — no revision. **Revision is never a standing every-class requirement.**

**The three teacher habits at a revision Hook** (integrated from the prior draft):
- **Observe, don't grade.** Note who cannot recall a revisited item. This is a *signal*, not a test score.
- **Log one line.** In the Lesson Completion Tracker, mark the revisit done and record any non-recall student(s).
- **Tie to homework.** Ensure at least one §2.8 Pool question targets the revisited item, so the recall is reinforced that evening.

Keep it to ~1–2 minutes. A revision Hook is a warm-up, never a re-teach.

### 2.2 Daily homework — reinforcement

Most lessons set short homework (bounded by REF-08; Class 1 pilot default 20 min). Its first job is to reinforce **today's** lesson. Its second, optional job is to carry **one** revision item drawn from the topic chart (e.g. the prior topic due for its first return). Logged in the Homework Tracker; the full delivery→return lifecycle is Project 06's (TODO 6.1).

### 2.3 Weekly assignment — once a week (given Thursday, collected Sunday)

This is the **main revision workhorse**. One assignment cycle per week: **given Thursday, collected Sunday** (D-014, clarified). It carries:
- **This-week items** — topics introduced this week that the chart schedules for a weekly return; **plus**
- **Cumulative reach-back** — a small rotating set of older topics the chart marks for a later (≈monthly) return, **and** the exam-horizon maintenance pass for Retained topics before the half-yearly/annual exam (§2.4). *This is how both "monthly" revision and exam maintenance happen — folded into the weekly assignment, not a separate revision day.*

Selection is simple (teacher): take this week's chart-due items, add any overdue items the tracker flags, add any fail-driven items, then trim from the bottom if it exceeds the REF-08 time cap. Logged in the Assignment Tracker.

**One common assignment — not bespoke per student.** The weekly assignment (and the daily homework) is a **single sheet for the whole class**. A weak student does **not** receive a different assignment. Their extra practice on a topic they are failing is delivered through the fail-driven loop (§4) — targeted attention at the next Hook, plus the **resubmission** of the same common item if they get it wrong — never through a separate per-student worksheet. (Formal per-student remediation worksheets are deliberately out of scope; Phase-5 / Project 06 if ever needed.)

### 2.4 Per-chapter class test — the gate, and the two-tier stop

The school runs a **class test per chapter**. REF-07 uses it two ways:
- As the **assessment-linked revision checkpoint** for that chapter's topics.
- As the **chapter-stop gate** (see the two tiers below).

**Two-tier stop — "Retained" is not "done forever."** A topic mastered in Week 3 and never touched again will have decayed by the half-yearly in Month 3 or the annual in Month 9 — the camel slipping its rope (§0). So passing the chapter test ends only the *dense* early returns, not all contact:

- **Tier 1 — chapter-stop (at the chapter test).** Pass → the topic is **Retained** and leaves the **dense early ladder** (R1→R2→R3 stop). Fail → the topic **stays** on the dense ladder for those students via the fail-driven loop (§4).
- **Tier 2 — exam-horizon maintenance (after Retained).** A Retained topic drops into a **low-frequency maintenance pool**, not into nothing. Before the **half-yearly and annual exams** — those two horizons only — the weekly assignment's existing cumulative reach-back (§2.3) draws a **light, rotating, bounded** pass over the maintenance pool. Boundaries that keep this from bloating: only a *handful* of maintenance items per assignment; prioritised by (a) topics on the *upcoming* exam and (b) topics the tracker shows weakest; and only in the run-up to those two exams, not as a constant background hum. The exam itself is the topic's next real checkpoint.

**Sequencing rule — the chapter test is the gate, wherever it falls.** The chart's later returns (R3, R4…) are *candidates*, not guarantees:
- **Pass → chapter-stop**, and any *dense-ladder* returns the chart scheduled *after* the test are **cancelled** (the topic moves to maintenance instead — the "mastery stop, not column count" rule, §3.2 rule 3).
- **Fail → stays** on the dense ladder; affected students continue via §4.
- Returns scheduled *before* the chapter test happen normally (pre-test reinforcement).

In practice, for most unit topics the chapter test lands around or before the ≈1-month mark, so it **supersedes** a later dense cumulative reach-back rather than following it; the topic then reappears only as a maintenance touch before a big exam. Read the chart as "revisit densely *until the chapter test confirms retention*, then maintain lightly until the exam."

### 2.5 Pre-exam in-class revision — out of scope

Before a term exam a teacher may run their own classroom revision. REF-07 does **not** schedule, script, or track this. It is explicitly out of scope and left to teacher discretion. **Note the distinction:** this is *in-class* revision time (out of scope). The **exam-horizon maintenance** of §2.4 is different — it is not class time at all; it rides the *existing* weekly assignment's cumulative slot. Maintenance is in scope; a pre-exam revision *class* is not.

---

## §3 — The topic-wise revision chart (the backbone)

### 3.1 What it is
One table per subject (per class). Each row is a **topic**; the columns lay out *when* and *through which channel* that topic is revisited. It is the **single source of truth** for revision scheduling — the channels in §2 simply execute what the chart says. The chart is a **class-level floor**: it schedules common *exposure* for the whole class. Individual students who need more practice are handled separately and automatically (§3.6) — the chart itself stays one table, not one-per-student.

### 3.2 Template

| Topic | Topic ID | Introduced (lesson) | R1 — first return | R2 — second return | R3 — third return | … (expandable) | Chapter gate → then |
|---|---|---|---|---|---|---|---|
| *(topic name)* | `TOP-{SUBJECT}-C{class}-{nn}` | `C{class}_{SUBJECT}_U{unit}_L{lesson}` | gap **+ channel** | gap **+ channel** | gap **+ channel** | add columns as the topic warrants | pass → **chapter-stop → maintenance** (§2.4); fail → stays on ladder |

**Rules that keep it simple and honest:**
1. **Gaps are relative, never fixed dates.** Write "after +1 lesson," "this week," "≈1 month / cumulative" — not calendar dates. The teaching calendar shifts; the chart must not go stale. Actual dates are filled in by the trackers at delivery, not in the chart.
2. **Channel per return** is one of: *next Hook* (build-on only) · *daily homework* · *Thursday weekly assignment* · *cumulative slot in a later weekly assignment* · *per-chapter class test*.
3. **Expandable, not capped.** Default working width is **3 dense returns** (most primary topics need 1–3), but add R4, R5… for foundational/high-stakes topics. **The dense ladder stops at mastery, not a column count** — it ends when the chapter test confirms retention (§2.4), after which the topic moves to the low-frequency maintenance track, not to nothing.
4. **Default spacing ladder (Class 1; adjust per subject):** R1 ≈ +1 lesson (next Hook, *if* build-on) → R2 ≈ this week (Thursday assignment) → R3 ≈ within ~1 month (cumulative slot in a later Thursday assignment) → **chapter gate** at the per-chapter class test → **maintenance** (one light cumulative touch before each of the half-yearly and annual exams). Expanding intervals: each successful return lengthens the next gap. The chapter gate can fall at any point (§2.4); for many unit topics it arrives around R3 and supersedes it, so treat R3+ as candidates, not guarantees.

### 3.3 Where the chart lives
- **Template + rules:** here, in REF-07 (this section).
- **Filled chart per subject:** the **Subject Spine Playbook (REF-03+)** — Bangla first (Day 5, TODO step 5.2). Topics and their sensible spacing are subject-specific and draw on the stability analysis / Universal Core, so they belong with the subject, per D-008.

### 3.4 How the lesson plan reads from the chart (key simplification)
REF-02 §2.6.c (Future-Revisit-Candidates) is **no longer invented per lesson**. The lesson-plan author **reads the relevant topic's row off the subject chart and copies its revision schedule into §2.6.c.** This removes guesswork, keeps every lesson consistent with the school-wide plan, and is the main reason this design is lighter than v0.1. *(Usage change only — no structural edit to REF-02; flagged to Project 03, §10.2.)*

### 3.5 The Topic ID — standard, and the homework/assignment topic-tag

`TOP-{SUBJECT}-C{class}-{nn}` (subject + class + topic number) is the stable handle for every chart topic. **Standard, not optional** (resolved 2026-05-21): it is what lets the trackers count and trace revision, and it is the anchor the homework-numbering scheme hangs on. It stays deliberately at **topic** grain — there is no per-must-cover-item, per-student ID (that was the v0.1 over-reach).

**Topic-tag rule for homework and assignment.** Every homework and weekly assignment **carries the `TOP-…` code(s) of the topic(s) it covers.** This is what makes "how many times did topic আ get touched this term" and "repeat the homework for this topic" answerable. REF-07 owns *this requirement*; the actual unique homework/assignment ID **format** (`HW-…` / `AS-…`) and the tracker fields that hold the ID + topic tag are **Project 06's** (TODO Day 6 step 6.1), because that ID also serves homework counting and the delivery lifecycle, beyond revision.

### 3.6 Per-student variation — the chart is a floor, not a per-student schedule

**The problem this solves.** One student masters a topic after 2 practice rounds; another needs 4. A naïve system would try to *schedule* per-student round counts — and that is exactly what becomes unmaintainable (it was the v0.1 failure mode). REF-07 refuses to do this.

**The principle: the schedule is common; the exceptions are individual.** The chart schedules *exposure* for the whole class. Whether a particular child has actually *mastered* the topic is handled at three per-student points **that already exist in this design** — none of which is a schedule, and all of which are **driven by the student's own errors, not by anyone planning ahead:**

1. **Resubmission loop** (lifecycle stage 5, Project 06 / TODO 6.1). A student who gets a homework or assignment item *wrong* is sent to redo it. Extra rounds happen automatically, triggered by mistakes.
2. **Fail-driven targeting** (§4). A student who fails an exit-check gets that specific item targeted at the next Hook and in their next homework. Triggered by failure.
3. **Per-chapter class test** (§2.4) — the only per-student record that matters here. Pass → that student leaves the dense ladder for this topic (it moves to light maintenance); fail → they stay on the dense ladder and reach individual attention at the 3-lesson threshold (§4).

**Illustration — letter আ, two students:**
- **Student A** answers আ correctly in the Thursday assignment and passes the chapter test. They rode the common schedule (~2–3 exposures) and stopped. Nothing extra to manage.
- **Student B** gets আ wrong → resubmission (one extra round); also failed the L3 exit-check → targeted recall at the L4 Hook + an extra homework item; still shaky → individual attention. They received ~4–5 effective rounds — **all triggered by their own errors, none scheduled by anyone.**

**Why this stays maintainable.** The teacher **never tracks "rounds-to-mastery per student per topic."** That count is *emergent*, not *managed*. They track one common chart, plus the pass/fail and resubmission signals they are recording anyway. The chart adds **zero** per-student bookkeeping.

**Deliberately deferred.** Finer per-student adaptive scheduling (e.g. Anki-style individual intervals) is **out of scope** — it is the complexity this design exists to avoid. If field experience later shows a real need, it is a Phase-5 idea, not a pilot requirement.

---

## §4 — Failure-driven revision (the D-025 link)

The exit-check (REF-02 §2.4) feeds revision automatically — this is the one place revision *must* happen regardless of the chart:

- **Partial failure (< 30% of a class fail an objective):** the missed item is added to the **next lesson's Hook** as a targeted recall for those students (a build-on/fail-driven Hook, §2.1), and is reinforced in the next **common** homework/assignment — with those students re-checked and, if they get it wrong, sent through the **resubmission** loop. No separate per-student sheet is created (see §2.3). Recorded as a fail-driven revisit.
- **Systemic failure (≥ 30% fail):** this is a **lesson-design problem, not a revision event** — escalate to Subject Lead / Principal and review the lesson before re-running it (D-025). It does not enter the normal spiral until re-approved.
- **3-lesson individual rule (D-025) — what it means precisely:** the flag is about a **skill *type*, not a single topic.** It trips when a student fails the **same *type* of objective** (e.g. *vowel recognition* — of which আ, ই, উ are instances) in **3 or more separate lessons**. It is **cumulative, not necessarily consecutive** — three lessons across the unit/term, not three in a row. When tripped → individual attention (catch-up session, parent inform). *The exact counting mechanics — what resets the count, and whether only exit-check fails count or homework errors too — are D-025's "per Project 06 follow-up rules," finalized at Day-14 step 14.3, not fixed here (§10.2).* The Master Tracker surfaces the count (§5).

### 4.1 Targeted re-do with Pool top-up (the bounded catch-up move)

When a student fails a **numbered** homework or assignment on a topic, the teacher's catch-up move is:
1. **Repeat the same numbered sheet** (e.g. re-issue `HW-C1-BAN-0007`). This *is* the resubmission loop (lifecycle stage 5) — a known, already-prepared sheet, not improvised.
2. **Optionally attach a top-up** — a few **extra questions on the same topic, pulled from that topic's existing Project 04 Pool** (the ≥20-question Pool per topic, D-028). The teacher **selects** from the ready Pool; they do **not author** new questions. This gives a weak student more reps to catch up with the class.

**Boundaries that keep this from sliding back to v0.1:**
- The top-up is drawn **only** from the existing per-topic Pool (Project 04) — selection, never authoring.
- It is **reactive only** — triggered by a failure flag in the tracker. There is **no pre-planned per-student schedule** of who gets top-ups. (Pre-scheduling per-student practice is exactly the unmaintainable thing this design refuses, §3.6.)
- It is tracked **inside the existing resubmission stage** (re-do issued — with/without top-up → due → submitted → checked), not as a new stream. The unique homework/assignment ID makes the re-do traceable.

---

## §5 — Tracking & principal visibility (kept thin)

Deliberately minimal — per the design principle, no per-item state machine.

### 5.1 What is logged where — **no separate revision tracker**

**There is no 9th tracker.** The pack is fixed at 8 (D-013); a dedicated revision tracker would be exactly the complexity this design avoids. Every revision signal piggybacks on a tracker the teacher already fills, and the **Master Tracker only *reads* them** (it is the principal roll-up, not a logging tool).

| Channel | Where the teacher logs it | Revision signal captured |
|---|---|---|
| Hook revisit | **Lesson Completion Tracker** (already per-lesson) | revisit done? + who couldn't recall |
| Daily homework | Homework Tracker | the revision item assigned + done (full lifecycle per TODO 6.1) |
| Weekly assignment | Assignment Tracker | which topics revised + done (full lifecycle per TODO 6.1) |
| Per-chapter class test | Class Test Tracker | topic pass/fail → chapter-stop (→ maintenance) or stays on the dense ladder |

Each homework/assignment row carries its **unique ID** (`HW-…` / `AS-…`) and the **`TOP-…` topic tag(s)** it covers (ID format + fields are Project 06's, §3.5 / TODO 6.1). This is what lets the Master Tracker count touches per topic and trace a re-do.

**The only new logging the teacher does** is two small fields added to the Lesson Completion Tracker (Bangla label + English code, Instructions §5):
- `REV_HOOK_DONE` — *পুনরালোচনা হুক* — Y / N / NA (NA = no revision triggered this lesson).
- `REV_NONRECALL` — *মনে করতে পারেনি* — names of students who couldn't recall; this list feeds the fail-driven loop (§4).

That is the whole in-class logging burden: two fields, in a tracker the teacher is already in.

> The rich **Given → Absent/Re-deliver → Due → Submitted/Chase → Checked/Resubmit → Returned** lifecycle is **Project 06's** (TODO Day 6 step 6.1), shared by the Homework and Assignment trackers. REF-07 does **not** restate it.

### 5.2 The Master-Tracker revision view (principal level)
Three things only, sliceable by class / subject (and teacher where useful):
1. **Per-topic status** — *On-track* / *Overdue* / *Retained-maintaining* / *Failing*, by comparing the chart's planned returns against what the trackers show as delivered. ("Retained-maintaining" = passed the chapter gate, now on the light maintenance track.)
2. **Revision coverage %** = revisions delivered ÷ revisions due in the window. One number per class/subject. (Counted directly from the `TOP-…`-tagged homework/assignment IDs — §5.1.)
3. **Watch-list** — (a) **Overdue topics** (planned return missed), and (b) **repeat-failure students** (the D-025 3-lesson flag).

Review cadence: **monthly — confirmed 2026-05-21** (resolves the TODO Open decision "Master Tracker review cadence"). The monthly cumulative revision and the monthly Master-Tracker review sit in the same week.

### 5.3 What the Principal sees before the half-yearly / annual exam
No pre-exam revision *class* is built (that is out of scope, §2.5). Instead, in the run-up to each of the **two big exams**, the monthly coverage view flags any **Retained** topic that has had **no maintenance touch** this exam cycle, so the cumulative reach-back (§2.3) can pick it up. The signal the Principal acts on: "exam-scope topics with zero maintenance touches before the exam." Nothing extra to build — it reads off the same `TOP-…` touch counts.

---

## §6 — Worked example + teacher quick-card

### 6.1 Worked example — Class 1 Bangla, letter আ

Chart row (lives in REF-03):

| Topic | Topic ID | Introduced | R1 | R2 | R3 *(candidate)* | Chapter gate → then |
|---|---|---|---|---|---|---|
| স্বরবর্ণ **আ** recognition | `TOP-BAN-C1-03` | `C1_BAN_U1_L3` | +1 lesson → L4 Hook *(L4 builds on L3)* | this week → Thursday assignment | ≈1 month → cumulative slot *(only if not yet gated)* | pass → chapter-stop → **maintenance**; fail → stays |

How it plays out:
- **L3:** আ introduced (card + word আম).
- **L3 evening:** the **common** daily homework (e.g. `HW-C1-BAN-0012`, tagged `TOP-BAN-C1-03`) reinforces আ for everyone.
- **L4 Hook:** because L4 builds on L3, a 1-minute flashcard recall of আ (this *is* L4's §2.6.b). Teacher observes, logs one line; 2 students who can't recall it are noted (`REV_NONRECALL`).
- **Thursday assignment** (`AS-C1-BAN-0003`, tagged `TOP-BAN-C1-03`): আ is on the **one common assignment** for the whole class. The 2 weak students get **no separate sheet** — the teacher re-checks them; if they get আ wrong it goes through **resubmission** (repeat the same numbered sheet, optionally with a few extra আ questions pulled from the topic's Project 04 Pool — §4.1).
- **Unit 1 chapter test (the gate — ~3 weeks in, *before* the ≈1-month R3):** most of the cohort passes আ → **chapter-stop**; the dense R3 slot is **cancelled** and আ drops to the **maintenance track**. The 2 weak students fail আ → it **stays** on the dense ladder for them.
- **For the 2 who stayed:** আ rides the fail-driven loop — a later **common** Thursday assignment's cumulative slot includes it, those students re-checked + individual attention. If either keeps failing **vowel-recognition-type** objectives (আ, ই, উ…) across **3 separate lessons**, that trips the D-025 flag (§4) — about the *vowel-recognition skill*, not আ literally three times.
- **Before the half-yearly exam (Month ~3):** আ — long since Retained — gets **one light maintenance touch** in a Thursday assignment's cumulative slot (§2.4 Tier 2), so it isn't cold on the exam. No revision class, no new sheet type.

### 6.2 Teacher quick-card (the whole system on one card)
1. **Hook:** grab attention. *If* today builds on yesterday or someone failed yesterday → spend 1–2 min on recall; observe, log one line, tie to tonight's homework.
2. **Homework:** reinforce today; optionally carry one chart-due revision item. (Every homework/assignment is numbered and topic-tagged.)
3. **Thursday:** build the weekly assignment from the chart's due topics + overdue + fail-driven + (before a big exam) a light maintenance touch; collect Sunday.
4. **Failed a numbered sheet?** Re-issue the same sheet (+ optional Pool top-up); track it as a resubmission.
5. **Chapter test:** topics that pass leave the dense ladder and go to light maintenance; topics that fail stay in the dense cycle.
6. **Never** run a standalone revision block that eats teaching time.

---

## §7 — Checklists (author + tracker-designer)

### 7.1 Lesson-plan author (Project 03) — before publishing
- [ ] §2.6.c copied from the subject chart (not invented) for every topic in this lesson.
- [ ] Every must-cover item maps to a chart topic with at least one scheduled return.
- [ ] If the Hook carries revision, the trigger (build-on or fail-driven) is stated.
- [ ] Each Hook-revisited item has ≥1 matching §2.8 Pool question.

### 7.2 Tracker-designer (Project 06) — before wiring the revision view
- [ ] **No 9th tracker created** — signals piggyback on the existing 8 (§5.1).
- [ ] Two fields added to the Lesson Completion Tracker: `REV_HOOK_DONE` (পুনরালোচনা হুক) and `REV_NONRECALL` (মনে করতে পারেনি).
- [ ] Homework & Assignment trackers carry a **unique ID** (`HW-…` / `AS-…`) and a **`TOP-…` topic-tag** field.
- [ ] Per-topic status (On-track / Overdue / **Retained-maintaining** / Failing) computes from chart-planned vs tracker-delivered.
- [ ] Coverage % (counted from `TOP-…`-tagged IDs) and the two watch-lists (overdue topics; repeat-failure students) compute and slice by class/subject.
- [ ] Pre-big-exam flag: Retained topics with **no maintenance touch this exam cycle** are surfaced (§5.3).
- [ ] The 6-stage lifecycle (TODO 6.1) — including **resubmission with optional Pool top-up** (§4.1) — is built once and shared by both trackers.
- [ ] Review cadence matches the Principal's Day-6 decision (default monthly).

---

## §8 — Design note: does in-class revision hurt the 35-minute lesson?

A fair concern, and it shaped this design. The honest answer has two halves:
- **A separate, mandatory daily revision block *would* hurt completion** — 3–5 minutes lost every day across a 35-minute lesson is real erosion. So REF-07 **does not** require one.
- **Light recall *inside the Hook time that already exists*, only when the lesson builds on the last, does *not* hurt** — those minutes are already spent, and warming up the prior content actually *helps the new lesson land*. It is a runway, not a tax.

That is why in-class revision is **triggered, not blanket**, and why everything routine moves to homework, the weekly assignment, and the chapter test. **Teaching time is protected; the spacing happens outside class.**

---

## §9 — Roles & responsibilities

| Role | Owns |
|---|---|
| **Class teacher** | Triggered Hook recall; daily homework; building/collecting the weekly assignment; logging one-line revision signals |
| **Subject Spine Playbook author (REF-03)** | Building the subject's filled topic chart (§3) |
| **Lesson-plan author (Project 03)** | Reading §2.6.c off the chart (§3.4) |
| **Subject Lead** | Systemic-failure review (§4); chapter-gate (chapter-stop → maintenance) marking |
| **Tracker-designer (Project 06)** | The thin coverage view (§5) + the shared lifecycle (TODO 6.1) |
| **Principal** | Monthly coverage review; acting on the overdue + repeat-failure watch-lists |

---

## §10 — Open dependencies, decisions for review, version log

### 10.1 Open dependencies
- **REF-03 (Bangla chart, Day 5).** Holds the first filled chart. REF-07 ships the template; REF-03 fills it.
- **REF-08 (Homework Architecture, Day 6).** Sets the homework/assignment time caps §2.2/§2.3 obey.
- **Master-Tracker review cadence — RESOLVED 2026-05-21: monthly** (§5.2).

### 10.2 Decisions

**Adopted by the Principal in this chat (2026-05-21) — to be logged at lock:**
- **A. Two-tier stop + exam-horizon maintenance (§2.4).** "Retained" = chapter-stop (dense ladder ends), then a low-frequency maintenance track; one light cumulative touch before each of the **half-yearly and annual** exams (those two horizons only); bounded (a handful of items, prioritised by upcoming-exam + weakest).
- **B. Topic IDs are standard (§3.5).** `TOP-…` codes are mandatory, not optional — they anchor coverage counting and homework numbering. (Resolves the prior "optional Topic ID" question.)
- **C. Homework/assignment numbered + topic-tagged (§3.5).** Each carries a unique ID and its `TOP-…` tag. The ID *format* and tracker fields are Project 06's (TODO 6.1).
- **D. Bounded re-do + Pool top-up (§4.1).** Failed numbered sheet → repeat it + optional extra questions from the topic's existing Project 04 Pool (selected, not authored); reactive only; tracked in the resubmission stage. No pre-planned per-student scheduling.
- **E. Topic chart placement (§3.3)** — template here, filled chart in REF-03. **F. Default spacing ladder (§3.2 rule 4)** — confirmed direction.

**Confirmed by the Principal at lock (2026-05-21):**
1. **D-026 refinement — CONFIRMED.** REF-07 (a) folds monthly into the weekly assignment, (b) puts pre-exam in-class revision out of scope, and (c) uses the per-chapter class test as checkpoint **+ the two-tier maintenance track** (half-yearly/annual). Logged as **D-PROJ00-007**, which records that D-026's operational expression is refined accordingly. TODO step 5.3 + End-of-Phase-2 summary reconciled at lock.
2. **Project 04 as an *indirect* consumer — CONFIRMED** (supplies §2.8 Pool questions for revision + the §4.1 top-ups). GLOSSARY/CROSS_PROJECT_INDEX reconciled to match at lock.
3. **3-lesson-rule mechanics — DELEGATION CONFIRMED.** Working definition in §4 stands; exact reset/counting mechanics are finalized in Project 06 follow-up rules (Day-14 step 14.3).

### 10.3 Version log
| Version | Date | Change | By |
|---|---|---|---|
| v0.1 | 2026-05-21 | Initial draft — four-cadence spiral, per-item RV-IDs, state machine, four-formula Master-Tracker spec. | Claude (drafted); Principal (reviewed — flagged too complex) |
| v0.2 | 2026-05-21 | **Simplified per Principal feedback.** (a) Corrected the Hook's purpose (attention/engagement; revision optional). (b) In-class revision made *triggered* (build-on / fail-driven), not blanket; integrated the observe/log/tie-to-homework habits. (c) Added **daily homework** as a channel. (d) Weekly = **once, Thu give / Sun collect**; "monthly" folded into the weekly assignment's cumulative reach-back. (e) **Removed** the separate monthly revision day and term/pre-exam revision day; pre-exam in-class revision marked out of scope; per-chapter class test is the checkpoint + mastery stop-rule. (f) Introduced the **topic-wise revision chart** as the backbone (template here, filled chart in REF-03), expandable with a mastery stop. (g) §2.6.c now *read off* the chart, not invented per lesson. (h) Dropped per-item RV-IDs and the state machine; tracking reduced to a thin per-topic coverage view. (i) Added §8 design note on the 35-minute concern. | Claude (drafted); Principal (approval pending) |
| v0.3 | 2026-05-21 | **Per-student handling + logging clarified (Principal Q's).** (a) §3.1 marks the chart as a **class-level floor**. (b) New **§3.6** — per-student variation rides the existing resubmission + fail-driven + chapter-test mechanisms (error-driven, not scheduled); two-student illustration; finer per-student adaptive scheduling explicitly deferred to Phase 5. (c) §5.1 made explicit: **no 9th tracker**; signals piggyback on the existing 8; the only new in-class logging is two Lesson-Completion fields `REV_HOOK_DONE` / `REV_NONRECALL`. (d) §7.2 designer checklist updated with the no-9th-tracker note + the two fields. No change to the scrapped-v0.1 record (kept in this version log + at lock + archived v0.1). | Claude (drafted); Principal (approval pending) |
| v0.4 | 2026-05-21 | **Worked-example logic corrected (Principal Q's).** (a) §2.3 — assignments/homework are **one common sheet, never bespoke per student**; weak-student practice rides attention + resubmission, not separate worksheets. (b) §2.4 + §3.2 rule 4 — added the **chapter-test-as-gate sequencing rule**: the test can fall anywhere on the ladder; pass → Retained → later R columns cancelled; fail → stays; R3+ are candidates, not guarantees. (c) §4 — fail-driven remediation routed through common artefacts (Hook attention + resubmission); **3-lesson rule clarified** per D-025 exact wording (same skill *type* not one topic; cumulative not consecutive; precise mechanics → Project 06 / Day-14 14.3). (d) §6.1 worked example rewritten for sequence-coherence (chapter test gates before R3; corrected the "failing আ across 3 lessons" wording to a skill-type pattern). (e) §10.2 item 6 added (3-lesson mechanics confirmation). | Claude (drafted); Principal (approval pending) |
| v0.5 | 2026-05-21 | **Two-tier stop + homework numbering (Principal decisions, this chat).** (a) **Two-tier stop (§2.4):** "Retained" = chapter-stop → low-frequency **maintenance track**; one light cumulative touch before each of the **half-yearly and annual** exams (bounded, prioritised); fixes the decay gap for big exams without a revision class. §0 table, §2.3, §2.5, §3.2, §3.6, §5.2, §5.3, §6 all reconciled to the two tiers. (b) **Topic IDs now standard** (§3.5), not optional. (c) **Homework/assignment numbered + topic-tagged** (§3.5) — `TOP-…` tag required; `HW-…`/`AS-…` ID format → Project 06. (d) **Bounded re-do + Pool top-up (§4.1):** repeat the numbered sheet + optional extra questions from the topic's Project 04 Pool (selected not authored; reactive only; tracked in resubmission). (e) §1.3 scope, §5.1 (IDs/tags), §5.2 (Retained-maintaining status), §7.2 checklist updated. (f) §10.2 restructured into adopted-this-chat vs still-open. | Claude (drafted); Principal (approval pending) |
| **v1.0** | **2026-05-21** | **LOCKED.** All four open items confirmed by the Principal: Master-Tracker review cadence = **monthly** (§5.2); **D-026 refinement** confirmed → logged as **D-PROJ00-007**; **Project 04** confirmed as *indirect* consumer; **3-lesson mechanics** delegation to Project 06 confirmed. §10.2 flipped to "confirmed at lock"; §10.1 cadence dependency resolved; status set to LOCKED. No content changes to §1–§9 beyond these confirmations. | Claude (drafted); **Principal (approved + locked)** |
| v1.1 | 2026-05-29 | **D-050 ripple (workstream-b item b.5).** Scoped two-tier acknowledgement: §2 gains an intro callout naming the within-chapter (§2.1, Hook-located, governed by REF-02 §2.9) vs cross-chapter (§§2.2–2.4 + §3 chart, unchanged) strands; §2.1 header renamed to mark it as the within-chapter strand. The fail-driven loop (§4) crosses both. No tracker, schedule, or operational change. Supersedes v1.0 (→ `/archive/`). Cross-reference: `LOCKED_REF-02_Three_Layer_Lesson_Plan_Template_v1_3.md` §2A.1. | Claude (drafted); Principal (approval pending) |
| v1.2 | 2026-05-31 | **Back-pointer footer added (D-PROJ00-062).** New "Downstream — built-asset dependents" footer records that this reference is a source of `LOCKED_ProductionCore_v1` (Project 03 built asset; Core §4 revision author-rule) and that a supersede triggers a Core rebuild (Core §7 / Build Policy §6; change-time trigger README §5.3/§5.4, dependency record CROSS_PROJECT_INDEX, D-PROJ00-061). **Payload-neutral — no change to §1–§10 content;** the footer itself does not make the Core stale. Supersedes v1.1 (→ `/archive/`). | Claude (drafted); Principal (approval pending) |

### 10.4 Cross-Project consumers (confirmed at lock 2026-05-21)
- **Project 03 — Lesson Plans.** Primary. Reads §2.6.c off the subject chart (§3.4).
- **Project 06 — Tracker & Operations.** Builds the thin coverage view (§5) + shared lifecycle + `HW-…`/`AS-…` IDs (TODO 6.1).
- **REF-03 (Project 00).** Holds the filled per-subject chart.
- **Project 04 — Question Banks.** *Indirect* — supplies the §2.8 Pool questions revision draws from (incl. §4.1 top-ups). *(Confirmed; GLOSSARY/CROSS_PROJECT_INDEX reconciled at lock.)*
- **Project 07 — Teacher Training.** Indirect — teachers trained on the quick-card (§6.2).



---

## Downstream — built-asset dependents (back-pointer · D-PROJ00-062)

**This reference is a source of `LOCKED_ProductionCore_v1`** (Project 03 built asset): it supplies **Core §4** — the revision author-rule + checklist (within-chapter Hook recall at Spine §2.6, governed by the §2.9 Session Map; cross-chapter spiral via the per-subject topic chart). A supersede of this file makes the Production Core **stale → rebuild required** before any new Chapter/Session Plan is built off it — see Core §7 and `LOCKED_ProductionAsset_Build_Policy_v1` §6 (Project 03), the change-time trigger in `PROJECT00_README.md` §5.3/§5.4, and the dependency record in `PROJECT00_CROSS_PROJECT_INDEX.md` (D-PROJ00-061).

*Payload scope:* the rebuild trigger fires on a change to the **extracted payload** (the Core §4 content). A payload-neutral edit — such as this back-pointer footer (the v1.1 → v1.2 supersede that introduced it) — supersedes the file but does **not**, by itself, make the Core stale.
