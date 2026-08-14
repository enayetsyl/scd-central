# LOCKED — Question Bank Production Conventions · v1.4 (Project 04)

**Status:** **LOCKED v1.4 — locked 2026-07-17** (`LOCKED_QuestionBank_Production_Conventions_v1_4.md`). Logged as **D-PROJ04-002/-006/-008/-014** (carried) + **D-PROJ04-015** (this supersede — exam-anchor alignment). **Supersedes LOCKED v1.3** (→ `/archive/`; `PROJECT04_MANIFEST_archived_files.md` **row 7** on lock). Never edit in place — supersede if revised (master §5.3).
**What changed v1.3 → v1.4 (D-PROJ04-015 — the exam-alignment pack):** (a) **§5.6 NEW — the examinable-substrate rule** (Principal ruling (a), 2026-07-16): for a **partially-flagged** পাঠ, bank content anchors on the **textbook minus its flagged elements**; replacement content is the substrate **only where the entire পাঠ was replaced**. (b) **§9 step 8a NEW — the mandatory exam-anchor coverage check** against **REF-26 (Exam Anchor Set, Project 00)**: every final-paper anchor on the built chapter must be answerable from the bank; the coverage table prints in the Review-Gate report; a ❌ is a named flag. (c) **§10 gains four hard checklist lines** (anchor coverage · PAT format-mix serviceability with the assembly-usable count stated · lane required-strands present-or-re-homed · substrate ruling cited). Everything else is unchanged from v1.3.
**Project:** 04 — Question Bank Production
**Owner:** Principal
**Author:** Claude (drafted); Principal (approved + locked 2026-05-31; superseded 2026-07-07; superseded 2026-07-16; superseded 2026-07-17)
**This is TODO 4-A** (= Project 00 TODO step 7.1).

**Governs:** how a Project 04 chat *produces, tags, stores, and delivers* question banks.
**Does NOT govern (defers to Project 00):** the question-setting *standard* — difficulty calibration, paper structures / mark splits, key & rubric bar, weak-student volume, the review gate → **REF-09** (Tier 1) and **REF-10** (Tier 2). Bloom mechanics → **REF-17 / REF-18**. **Paper assembly (structure, slots, format whitelists, ADMIN slots) → REF-25 (PAT)** — the school exam-scheme record. This document makes banks that *comply* with those; it never restates or overrides them.

---

## §0 — Summary (read first)

A Project 04 chat builds, for one **(class × subject)**, a tagged pool of questions organised **chapter → topic**, every question Bloom-tagged, difficulty-tagged, and carrying a key or rubric. The **topic is the atomic unit**; a chapter is the roll-up of its topics. Each build hands you two things: a **chapter production file** (rendered from the canonical JSON, versioned) and the **master-ready section** to splice into that subject's read-file. **No questions are ever copied into a lesson/session plan** — the plan and its questions are linked only by the shared topic tag. **Retrieval is served by the school software over MongoDB** (topic-tag filter), not by a local index (D-PROJ04-008).

**Locked rulings (D-PROJ04-002):**
1. **Topic is the atomic unit.** Ask by topic → that topic's Pool; ask by chapter → the union of its topics' Pools, each question keeping its `TOP-…` tag. (§2)
2. **Default 30 questions per topic; the ≥20 floor (D-028) is preserved.** Override up (no ceiling) or down, never below 20. (§4)
3. **Three selectable, tagged streams: homework (`HW-…`), weekly assignment (`AS-…`), per-chapter class test.** No classwork stream. (§8)
4. **Every question carries a stable QID.** (§3)
5. **The validated JSON payload is canonical (D-PROJ04-004 / D-PROJ04-006); the production file → master read-file are rendered views of it — local / in Google Drive, upload-on-trigger. Retrieval is served by the school software over MongoDB (D-PROJ04-008).** (§6/§7)
6. **Retrieval is app-side (D-PROJ04-008):** the school software imports the canonical JSON into MongoDB and filters by `topic_tag`. The build emits **no register TSV**. (§7)
7. **The lesson/session plan holds no Pool** — no inline copy, no reference. The link is the shared **topic tag** (`TOP-…`). **(Master D-051, supersedes D-029.)** (§6.1)

**Before-lock checklist** is at §10. **Build procedure** is §9.

---

## §1 — What a bank is (and is not)

A bank is a **tagged, keyed pool of questions** for one (class × subject), grouped by chapter and topic. It is **not** a finished exam paper. Papers, homework, and assignments are *assembled by selection* from the bank under REF-09 / REF-10, **with paper structure per REF-25 (PAT)** — the bank supplies the raw, already-compliant questions; it does not set mark totals or paper structure.

## §2 — The unit model: topic is atomic, chapter is the roll-up

- The **topic** (`TOP-{SUBJECT}-C{class}-{nn}`, the mandatory code from REF-07 §3.5 / REF-19) is the smallest addressable unit. Each topic owns one Pool.
- A **chapter** has no Pool of its own. A chapter request returns the **union of the Pools of every topic in that chapter**, each question still showing its `TOP-…` tag.
- The `TOP-…` tag is the single join key — it answers a topic request, a chapter request, **and** the plan↔questions link (§6.1) — so questions are never stored twice.

## §3 — IDs and tags

| Element | Format | Source |
|---|---|---|
| Topic tag | `TOP-{SUBJECT}-C{class}-{nn}` | REF-07 §3.5 / REF-19 |
| Pool (per topic; chapter-scope per D-050) | `QP-{SUBJECT}-C{class}-U{unit}[-L{lesson}]` | REF-08 §2.8 / REF-02 §2.8 |
| **Question (stable QID)** | `QP-…-Q{nn}` (e.g. `QP-BAN-C1-U2-L4-Q03`) | this doc |
| Homework item (selected, not authored) | `HW-{class}-{SUBJECT}-{nnnn}` | REF-08 §5.1 |
| Weekly assignment | `AS-…` | REF-07 |
| Chapter production file | `C{class}_{SUBJECT}_U{nn}_QuestionBank_v{ver}.md` | D-037 |
| Master read-file (per class × subject) | `C{class}_{SUBJECT}_QuestionBank_MASTER_v{ver}.md` | this doc |

The **QID is permanent** — once `…-Q03` exists it is never reused, even if retired; new questions take the next free number. A homework/assignment row, a master section, and the app's stored record all point back to the exact same question for life.

## §4 — Pool size

- **Default production target: 30 per topic.** Build to 30 unless a request says otherwise.
- **Hard floor: 20 (D-028, unchanged).** Never deliver below 20.
- **Per-request override:** more than 30 (no ceiling) or, narrowly, fewer — never below 20.

## §5 — Per-question requirements (the compliance bar)

1. A **Bloom tag**. Topic Bloom mix follows the **REF-17 §5.2 chapter-scope band** for the class, weighted toward the topic's REF-03 / REF-19 emphasis tier. Application / free-thinking is the default skew within the band.
2. A **difficulty tag** per **REF-09's** calibration (REF-09 owns the scale; the bank tags to it, never invents levels).
3. A **question type** from the schema's full `question_type` enum — **`mcq / short_answer / true_false / fill_blank / matching / descriptive`** (D-PROJ04-014) — with `paper_role` (MCQ / short / structured / creative) per REF-09's paper-structure vocabulary. The legacy paper formats are therefore **bankable items**: মিলকরণ = `matching`, সত্য-মিথ্যা = `true_false`, শূন্যস্থান = `fill_blank`; এলোমেলো-সাজানো / rhyming and similar are `short_answer` with the format stated in the stem. Administration items (শ্রুতলিপি, পঠন, হাতের লেখা, spelling tests) are **never bank items** — they belong to the paper template (REF-25 ADMIN slots).
4. A **mandatory answer key**, or a **rubric** for open-ended items (D-028 / REF-09).
5. **Curation clearance:** stem, every option, every name, every scenario passes **REF-01** + a **REF-21** self-scan; names from **REF-20** (matching class pool); English operative vocabulary = Core + Working + already-taught (**REF-22**), Receptive only inside a glossed passage.

**Language:** question content in Bangla (English subject excepted); IDs and tags in English.

**§5.6 — Examinable substrate (Principal ruling (a), 2026-07-16; D-PROJ04-015).** What a bank's content items test is fixed by curation status, never re-derived per chat:
- **পাঠ with KEEP or partial flags (elements excised/swapped):** the examinable substrate is **the textbook's own content minus the flagged elements**. Story facts, characters, plot, and prose stay bankable; only the specifically flagged lines/elements (e.g., a flagged rhyme, an image) are excluded or carried in their swapped wording. *Do not* re-anchor such a পাঠ onto replacement/theme content — that was the C2 BAN U20 v2 divergence this rule closes.
- **পাঠ fully replaced (RC supersedes the whole পাঠ):** the replacement content **is** what was taught, so it is the substrate (e.g., C5 BAN U14 উসামার বাহিনী).
- The build states which branch applies for every NEEDS-REPLACEMENT পাঠ in the chapter (checklist §10); doubt = ask the Principal, never guess.


## §6 — The storage model and how it reaches you (canonical = validated JSON; D-PROJ04-006 / D-PROJ04-008)

One question is **authored once as a validated JSON payload** (`LOCKED_QuestionPayload_Schema_v1.json`; a shared passage as `LOCKED_StimulusPayload_Schema_v1.json`) — the **single source of record** (D-PROJ04-004 / D-PROJ04-006). Everything teacher-facing is **rendered** from that JSON; editing only ever happens in the JSON source. The school software imports that JSON and stores it in **MongoDB**; retrieval is app-side (§7, D-PROJ04-008).

| Artifact | Granularity | Role | Where it lives |
|---|---|---|---|
| **Chapter production file** | per chapter | **Rendered teacher/author view** (the JSON payload is canonical — D-PROJ04-006). Rendered from the JSON; where the chat reviews and **versions** one chapter (carries the version log + review record). Superseded one chapter at a time (old → `/archive/`). | Local, MANIFEST-tracked, **upload-on-trigger** |
| **Master read-file** | per (class × subject) | **Teacher read copy** — "open one file, see the whole subject." A **concatenation of current chapter bodies.** **Never hand-edited.** | Google Drive |

*(The register — a per-(class × subject) Google Sheet — was retired by D-PROJ04-008; retrieval moved into the school software over MongoDB. See §7.)*

**Lineage:** author the **JSON payload** (canonical) → **render** the production file (with its `MASTER-BODY` block) and splice the master concatenation — both from the one JSON via the renderer/harness. The production file and master are **regenerated rendered views**, never hand-edited. The same canonical JSON is imported by the app into MongoDB for retrieval.

**Single-source generation (D-PROJ04-006 / D-PROJ04-008).** Because the production file/master **and the app's MongoDB records** are generated from the one validated JSON, there is **zero drift** between artifacts. The school software imports the JSON through the envelope (`LOCKED_SCHOOLSW_ImportEnvelope_Schema_v1.json`, `doc_type:"question"` / `"stimulus"`) and **renders its own display/PDF** from the payload — it does **not** consume the Markdown (unlike plan imports, which carry co-rendered Markdown). The closed contract + the import gate are `LOCKED_QuestionPayload_Schema_v1.json` / `LOCKED_StimulusPayload_Schema_v1.json` + `validate_import.py`.

**"Canonical" ≠ "kept in Project knowledge."** The canonical JSON payload is authoritative; it does not sit permanently in Project 04. Banks are plain text (small on disk), but to keep every chat lean (§5.13) they follow the **upload-on-trigger** pattern (REF-03 spines, REF-06 V1A, textbooks/TGs under D-006): upload a bank into a chat only while that (class × subject) is worked, remove after. Teachers read the **master in Drive** and **retrieve via the school software (MongoDB)**; Project 04 holds nothing between builds.

**Production file structure (so the master splices mechanically):** a thin **production header** (status, version log, review record) then the **question body** between markers:

```
<!-- MASTER-BODY:START  C3_BAN_U2 -->
## Chapter U2 — <title>
### TOP-BAN-C3-05 — <topic>
> Pool QP-BAN-C3-U2-L1 …
>   QP-BAN-C3-U2-L1-Q01  … (Bloom / difficulty / type) … Answer/Rubric: …
…
<!-- MASTER-BODY:END  C3_BAN_U2 -->
```

The master = the concatenation of every current chapter's `MASTER-BODY` block under a thin master header — a mechanical splice, never a re-author.

### §6.1 — The lesson/session plan carries no questions (master D-051)

The lesson/session plan holds **no Pool — neither an inline copy nor a reference block.** A plan and its questions are connected solely by the **topic tag** they share:

- the plan's **Spine** already declares the topic(s) it teaches as `TOP-…` codes;
- every stored question record carries the same `TOP-…` tag.

So at planning or teaching time the teacher reads the plan's topic tag → **filters the school software on that tag** (or opens the master) → selects questions. **A bank change never touches a plan.** This is **master D-051** (supersedes D-029, "Pool is inline"); it removed the inline-Pool field from the lesson-plan template (REF-02 v1.6), the homework rule (REF-08 v1.3), the Production Core (v3), and the Session/Chapter layout instructions (v9 / v3.2). D-030 is unchanged (the teacher still selects `Y`, now from the app/master).

## §7 — Retrieval (app-side, MongoDB) — D-PROJ04-008

The **retrieval engine is the school software.** On import through `LOCKED_SCHOOLSW_ImportEnvelope_Schema_v1.json`, each validated question/stimulus payload is stored in **MongoDB**; the app indexes on `topic_tag` (and chapter/unit, Bloom, difficulty, type, stream-suitability — the same fields the payload carries).

- Filter on `TOP-…` → every question on a topic across chapters; filter on Chapter/Unit → the chapter roll-up. This is also the plan↔questions lookup (§6.1).
- The app renders its own display/PDF from the canonical payload (no separate preview store).
- **No register TSV is emitted by the build** (retired, D-PROJ04-008). The `Source file + ver` drift-catcher is unnecessary: the app's records and the production file/master are single-source-generated from the one JSON (§6), so there is no artifact to drift against.

**Project 06 boundary:** the app is the **authoring + retrieval** index. The **live usage count** and the **delivery→return lifecycle** of any selected `HW-…`/`AS-…` belong to **Project 06's** trackers (REF-08 §5). The app may carry a last-used / rotation hint, but Project 06 owns the authoritative count.

## §8 — Retrieval and selection into streams

Selection is always *picking from the Pool via the school software (or the master)*, never authoring at point of use (D-030 — time is the cap, count is the lever):
- **Homework** → teacher reads the plan's `TOP-…` → filters the app → selects → items become `HW-…`, tagged `TOP-…`, logged in the Homework Tracker.
- **Weekly assignment** → `AS-…` (REF-07-scheduled), same path.
- **Per-chapter class test** → the chapter roll-up (filter on Chapter/Unit).
- **Exam papers (half-yearly / annual / mock)** → assembled from the bank **per REF-25 (PAT)**: template → fence → blueprint → selection → ADMIN slots → note block → review gate. The PAT owns structure, mark slots, format whitelists, and ADMIN slots; the bank owns the items. (D-PROJ04-014)
- **Classwork** → **not a bank stream**: lesson plan's Independent Practice / Flex Zone, untagged here.

## §9 — Build procedure (stepwise)

1. **Confirm the (class × subject)** and load inputs: REF-05 · REF-03 · REF-19 (topic list) · REF-09/REF-10 · REF-18/REF-17 · REF-01/REF-21/REF-20/REF-22.
2. **List the chapter's topics** from REF-19 → the `TOP-…` codes.
3. **For each topic, draft to 30** (≥20 floor): Bloom mix from REF-17 §5.2; difficulty per REF-09; skew to application/free-thinking. Include the lane's legacy-format types (`matching`, `true_false`, `fill_blank` etc.) in proportions that serve the lane's PAT slots (D-PROJ04-014).
4. **Stamp each question:** QID · Bloom · difficulty · type · key-or-rubric.
5. **Curation pass:** REF-01 + REF-21; names REF-20; English vocab REF-22.
6. **Assemble the chapter production file** (header + `MASTER-BODY` block) under the D-037 filename, rendered from the canonical JSON payload.
7. **Emit the master-ready section** (the `MASTER-BODY` block) for splicing.
8. **Run the §10 checklist + the REF-09 §9 Review Gate** (REF-10 §6 for stretch items).
9. **Deliver** the production file (+ the canonical JSON for app import); note any topic that fell back to the 20 floor and why.

*(v1.1 build-step 8 "Emit the register TSV block" is removed — D-PROJ04-008; retrieval is app-side, §7.)*

**Step 8a — Exam-anchor coverage check (mandatory; D-PROJ04-015).** Load the lane's section of **REF-26 — Exam Anchor Set** (Project 00). List every anchor whose পাঠ/topic falls in the chapter being built. For each: `F`/`W` anchors — at least one bank item must let a student answer that specific fact/word; `S` anchors — at least one item must exercise that skill; `ADMIN` anchors are skipped (never bank items). Print the coverage table — **anchor → covering QID(s), or ❌** — in the Review-Gate report. Every ❌ is a **named flag** for the Principal: cover it with a top-up item, or record the Principal's written reason to leave it. The check runs against the anchor set current at build time (REF-26 maintenance note).


## §10 — Before-lock checklist (per chapter build)

- [ ] Every topic has a Pool; each ≥ 20, default-targeted at 30.
- [ ] Every question has a QID, Bloom tag, difficulty tag, type (full enum, §5.3), key or rubric.
- [ ] Topic Bloom mix inside the REF-17 §5.2 band; skew to application/free-thinking.
- [ ] Difficulty tags map to REF-09's scale.
- [ ] The lane's PAT-required legacy formats are represented in the Pool (D-PROJ04-014).
- [ ] Curation clean: REF-01 + REF-21; names REF-20; English vocab REF-22.
- [ ] Language correct (Bangla content / English subject excepted; English IDs + codes).
- [ ] `MASTER-BODY` markers present and labelled.
- [ ] Canonical JSON payload validates against `LOCKED_QuestionPayload_Schema_v1.json` / `LOCKED_StimulusPayload_Schema_v1.json` (app-import ready).
- [ ] Review Gate passed (REF-09 §9; REF-10 §6 for stretch).
- [ ] Filename per D-037; production file marked rendered-view / JSON canonical; MANIFEST row noted.

*(v1.1 line "Register TSV emitted; rows 1:1 with the bank; `Source file + ver` correct" is removed — D-PROJ04-008.)*

**Added at v1.4 (D-PROJ04-015) — hard alignment lines (a build cannot pass these silently):**
- [ ] **Anchor coverage:** REF-26 lane section loaded; every chapter anchor ✅ covered or ❌-flagged with the Principal's ruling recorded; the coverage table is in the Review-Gate report.
- [ ] **PAT format-mix serviceability:** item counts by `question_type` stated against the lane's REF-25 template; the **assembly-usable pool** (items in formats the lane's annual paper actually uses) is stated as a number; formats outside the lane's whitelist (kept for class-test flex) are identified and capped by intent, not accident.
- [ ] **Required strands:** where the lane's paper draws per-পাঠ vocabulary strands (শব্দার্থ / বিপরীত / যুক্তবর্ণ etc.), the build either includes them or states in writing which other chapter/topic build homes them.
- [ ] **Substrate:** for every NEEDS-REPLACEMENT পাঠ in the chapter, the §5.6 branch (textbook-minus-flags / full-replacement) is named in the build header.


## §11 — Decisions, propagation, version log

Logged as **D-PROJ04-002** (§0 rulings 1–7). Notes:
- **README** — conventions are not folded into the README; it carries a pointer line; the rulings' canonical home is `PROJECT04_DECISIONS.md` (D-PROJ04-002).
- **Master D-051** (Pool placement) executes across REF-02 v1.6, REF-08 v1.3, Production Core v3, Session-Plan Layout v9, Chapter-Plan Layout v3.2 (Project 00 / Project 03).
- **Register retired (D-PROJ04-008):** retrieval moved into the school software over MongoDB; TODO 4-E (create the C5 × BAN register) is closed as superseded; no register artifact is produced going forward.
- **PAT adopted (D-PROJ04-014):** paper assembly is governed by **REF-25 (Project 00)**; this document points to it (§1, §8) and makes the lane's legacy formats bankable (§5.3). No payload-schema change was needed (the v1 `question_type` enum already carried `true_false / fill_blank / matching`).
- **Project 06** — QID + app record exist (usage/rotation hint reads off the QID); no tracker redesign owed.
- **MANIFEST** — `PROJECT04_MANIFEST_archived_files.md`: rows 1–2 = conventions v1.0 → v1.1 → v1.2; rows 3–5 = the 2026-07-08 bank-level cutovers (D-PROJ04-011/012/013); **row 6 = conventions v1.2 → v1.3 (this supersede)**.

| Version | Date | Change | By |
|---|---|---|---|
| DRAFT v1 | 2026-05-31 | First draft (topic-atomic / chapter-roll-up, default-30 / floor-20, three streams no-classwork, QID, register). | Claude |
| DRAFT v1.1 | 2026-05-31 | Three-artifact storage model; `MASTER-BODY` markers; paste-ready TSV register output; README-pointer. | Claude |
| DRAFT v1.2 | 2026-05-31 | Lesson-plan inline Pool removed — plan↔questions link is the topic tag (§6.1); the D-029 supersede; artifact set is exactly three. | Claude |
| **LOCKED v1.0** | 2026-05-31 | First lock (D-PROJ04-002, seven rulings). | Claude (drafted); Principal (approved + locked) |
| **LOCKED v1.1** | 2026-06-09 | Canonical source = validated JSON payload (D-PROJ04-004 / D-PROJ04-006). §0 ruling 5 + §6 amended; production file / master / register = rendered views. Supersedes LOCKED v1.0 (→ `/archive/`; first archive cutover → MANIFEST created). | Claude (drafted); Principal (approved + locked) |
| **LOCKED v1.2** | 2026-07-07 | **Register retired; retrieval moves into the school software over MongoDB (D-PROJ04-008).** §0 rulings 5–6, §6 (register artifact row dropped), §6.1, §7 (rewritten app-side), §8, §9 (build-step 8 removed), §10 (register checklist line removed). Everything else unchanged from v1.1. Supersedes LOCKED v1.1 (→ `/archive/`; MANIFEST row 2). | Claude (drafted); Principal (approved + locked) |
| **LOCKED v1.3** | 2026-07-16 | **Legacy formats bankable + PAT adopted (D-PROJ04-014).** §5.3 names the full schema `question_type` enum; ADMIN items excluded from the bank; §1/§8 point paper assembly to REF-25 (PAT, Project 00); §9 step 3 + §10 checklist line added. Everything else unchanged from v1.2. Supersedes LOCKED v1.2 (→ `/archive/`; MANIFEST row 6). | Claude (drafted); Principal (approved + locked) |
