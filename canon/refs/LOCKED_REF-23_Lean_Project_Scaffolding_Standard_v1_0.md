# LOCKED — REF-23 · Lean Project Scaffolding Standard · v1.0

| Field | Value |
|---|---|
| Reference ID | REF-23 (confirm as next free number against `PROJECT00_CROSS_PROJECT_INDEX.md`) |
| Status | **LOCKED v1.0** |
| Date locked | 2026-05-28 |
| Scope | **All-future** — binds every Project scaffolded on or after this date |
| Decision | **D-PROJ00-035** (to be logged; resolves token-reduction item #12 + the #12 scope decision) |
| Type | Local-only canonical reference (Subject-Spine-style precedent — not a master-decision change) |
| Authority | Master `PROJECT00_README.md` §5 conventions; D-047 / D-048 |
| Output language | English (D-002 — governance/Claude-internal) |

---

## Summary (read this first)

This Standard defines the **minimum scaffolding** a Project must carry and the **stepwise procedure** for standing one up. Its purpose is token discipline: a new Project **inherits** the master conventions by pointer instead of restating them, so its local files stay lean.

- **What it binds:** every Project scaffolded from now on — Projects 04, 05, 06, 07, 08, and any future Project.
- **What it exempts:** Projects 00–03 (already scaffolded; they already carry the conventions). Retrofitting 01–03 is a **parked option**, applied only on Principal direction if bloat justifies it. Project 00 is the source hub — it holds the conventions, it does not inherit them.
- **The lean mechanism:** a bound Project's README carries **one inheritance line** (Part 4 below) pointing to master §5.5 / §5.12 / §5.13 / §5.14, rather than copying those conventions into local files.
- **The four mandatory files:** README, TODO, DECISIONS, and a `/handoffs/` folder. (GLOSSARY and CROSS_PROJECT_INDEX are Project-00-only and are **not** inherited.)

A scaffolding checklist sits at the end (Part 7).

---

## Part 1 — Purpose and binding scope

**1.1 Purpose.** Keep new-Project setup minimal and consistent. Every bound Project gets the same skeleton and inherits the same master disciplines, so no Project re-derives or re-pastes the §5 conventions (the token cost D-047/D-048 exist to remove).

**1.2 Binding clause (forward-looking).** Any Project scaffolded **on or after 2026-05-28** inherits this Standard at the moment its scaffolding files are created. The rule is forward-looking, not a fixed list — it captures Projects 04–08 today and any later Project automatically.

**1.3 Exemptions.**
- Projects 01, 02, 03 — exempt (already scaffolded; conventions already present).
- Project 00 — the source hub; holds the master conventions, does not inherit.
- **Parked:** retrofit of 01–03 onto this Standard — not active; revisit only on Principal direction (tracked with TR-01/TR-02 in `PROJECT00_TODO.md`).

**1.4 Relationship to master conventions.** This Standard does not replace or re-bind master §5 — master §5 already applies to every Project by being master. REF-23 governs only (a) the minimum file set, (b) the inherited-conventions pointer, and (c) the stand-up procedure. Where this Standard and master §5 ever disagree, **master §5 wins** and this Standard is superseded to match.

---

## Part 2 — The minimum scaffolding set (mandatory)

Every bound Project must carry exactly these, named per the `PROJECT{NN}_` prefix convention (D-017):

| File / folder | Required sections (minimum) |
|---|---|
| `PROJECT{NN}_README.md` | (1) one-line Context; (2) What lives here / What does **not** (redirect map); (3) Local conventions — a pointer to master §5 via the Part-4 inheritance line, **not** a re-statement; (4) the **§9-equivalent inherited-conventions line** (Part 4, verbatim); (5) Version log. |
| `PROJECT{NN}_TODO.md` | (1) Active tasks; (2) Standing tasks — **must include the consult-routine** (read this Project's README+TODO at chat start, per master §5.8) **and the cross-Project consult line** (master §5.14); (3) Parked items (if any); (4) Version log. |
| `PROJECT{NN}_DECISIONS.md` | (1) Local decision log (IDs `D-PROJ{NN}-NNN`); (2) Cross-Project propagation flags table; (3) "Relationship to master log" range line; (4) Version log. |
| `/handoffs/` | Empty at creation; populated per master §5.5 (Light/Full tiers). |

**Not inherited (Project-00-only):** `GLOSSARY.md`, `CROSS_PROJECT_INDEX.md`. A bound Project uses the canonical GLOSSARY/INDEX in Project 00; it does not keep its own.

**Created-when-triggered (not at scaffold time):** `PROJECT{NN}_MANIFEST_archived_files.md` — produced at the Project's **first archive cutover** per master §5.12, following the Project 01 manifest shape (summary/checklist on top → Kept table → upload-trigger legend → Archived tables → flags → version log). The scaffolding step only notes that this file is owed once an archive cutover occurs.

---

## Part 3 — Inherited disciplines (the lean part)

A bound Project **inherits, by pointer, and does not restate** the following master §5 conventions:

- **§5.5** — Light / Full handoff tiers (D-047).
- **§5.12** — Archived-files manifest discipline (D-047).
- **§5.13** — Tool-use discipline: patch over regeneration for files >100 lines; prefer `project_knowledge_search` over `view` for reference lookups; no re-pagination / no overlapping view ranges; combine bash diagnostics; don't re-upload files already in Project knowledge (D-047).
- **§5.14** — Cross-Project consult-routine: for cross-cutting work, read the relevant sections of each touched Project's README/TODO at task start; read-before-you-touch; no in-chat edits of other Projects' files (D-048).

The full text of each lives **only** in master `PROJECT00_README.md` §5. A bound Project references them through the Part-4 line — it must **not** copy their text into local files.

---

## Part 4 — The verbatim inheritance line (paste into each new README §9-equivalent)

> Inherits master §5.5 (Light/Full handoff tiers), §5.12 (archived-files manifest), §5.13 (tool-use discipline), and §5.14 (cross-Project consult-routine) per D-047/D-048 and REF-23 (Lean Project Scaffolding Standard).

Each bound Project's README carries this single line in its conventions section. No other reproduction of the §5 disciplines is permitted in local files.

---

## Part 5 — Stepwise scaffolding procedure (micro-management)

Run these steps in order when standing up a new bound Project. One file at a time; for any file deliverable, ask the Principal whether they want the prompt/spec or the file (style rule).

1. **Confirm the Project is in scope.** Verify it is scaffolded on/after 2026-05-28 and is not 00–03. If 01–03, stop — retrofit is parked (Part 1.3).
2. **Confirm the Project number + name** against `PROJECT00_README.md` §4 and the GLOSSARY Project-Names table (e.g., 05 = Replacement Content Studio).
3. **Confirm the next free local decision ID base** and the master-log range to cite, by reading `PROJECT00_DECISIONS.md` (per §5.14, this is cross-cutting — targeted read, not whole-file).
4. **Produce the Instructions text** for the Project (pasted into the Claude UI by the Principal). It must include a §4.8-equivalent consult-routine paragraph carrying the compact §5.14 mirror clause (F-1 snippet from the carry-forward brief).
5. **Produce `PROJECT{NN}_README.md`** with the five required sections (Part 2), including the Part-4 inheritance line.
6. **Produce `PROJECT{NN}_TODO.md`** with the consult-routine + cross-Project consult line in Standing tasks.
7. **Produce `PROJECT{NN}_DECISIONS.md`** with an empty local log seeded only with the scaffolding decision row, the propagation-flags table, and the "Relationship to master log" range.
8. **Create the `/handoffs/` folder** (empty).
9. **List the canonical REFs the Project consumes** (from `PROJECT00_CROSS_PROJECT_INDEX.md` reverse view) so the Principal knows what to load into substantive chats — do **not** duplicate those REFs into the Project unless the Project's own Instructions require duplication (e.g., the Project 03 §3.3 precedent).
10. **Run the §5.4 propagation back to Project 00:** log the new Project's creation + this REF-23 inheritance in `PROJECT00_DECISIONS.md`; add/confirm the Project's entry in `PROJECT00_CROSS_PROJECT_INDEX.md`; tick the corresponding `PROJECT00_TODO.md` scaffolding sub-item. Ask apply-now or add-to-TODO.

---

## Part 6 — Maintenance and supersede

- This is a **LOCKED** file — never edited in place. To change it, supersede with a new version (`LOCKED_REF-23_..._v1_1.md`) and move v1.0 to `/archive/` per master §5.3; ask the Principal before overwriting.
- **Triggers for a supersede:** a master §5 convention is added/amended (re-sync Parts 3–4); the scope ruling changes (e.g., retrofit of 01–03 is activated); the minimum file set changes.
- A supersede is logged as a new `D-PROJ00-NNN` row and propagated via §5.4. It does not change the master-log range unless a master convention itself changed.

---

## Part 7 — Scaffolding checklist (copy per new Project)

```
NEW-PROJECT SCAFFOLDING — PROJECT {NN} ({name})
[ ] In scope (scaffolded on/after 2026-05-28; not 00–03)
[ ] Project number + name confirmed (README §4 / GLOSSARY)
[ ] Next free D-PROJ{NN} base + master-log range confirmed (DECISIONS, targeted read)
[ ] Instructions text produced — includes §4.8 consult-routine + §5.14 mirror clause
[ ] PROJECT{NN}_README.md — 5 required sections + Part-4 inheritance line
[ ] PROJECT{NN}_TODO.md — consult-routine + cross-Project consult line in Standing tasks
[ ] PROJECT{NN}_DECISIONS.md — seed row + propagation-flags table + master-log range
[ ] /handoffs/ folder created (empty)
[ ] Consumed canonical REFs listed (INDEX reverse view) — duplicated only if Instructions require
[ ] §5.4 propagation to Project 00 done (DECISIONS + INDEX + TODO tick) — apply-now or TODO
[ ] MANIFEST owed-note recorded (created at first archive cutover, not now)
```

---

## Version log

| Version | Date | Change | By |
|---|---|---|---|
| v1.0 | 2026-05-28 | Initial lock. Resolves token-reduction item #12 (Lean Project Scaffolding Standard) and its scope decision = **all-future** (Projects 04–08 + any future Project; 00–03 exempt; retrofit parked). Local-only canonical reference per the new-reference-as-local precedent (D-PROJ00-019/-022/-027/-031); logged under **D-PROJ00-035** (to be recorded); master-log range unchanged. | Claude (drafted); Principal (approval pending) |
