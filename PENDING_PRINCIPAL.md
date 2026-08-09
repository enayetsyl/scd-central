# PENDING_PRINCIPAL.md — question queue for the Principal

Agents append rows (AGENTS.md §6); the Principal clears them from any device.
No promotion/print in a workstream while it has an OPEN row here.

**Queue status: 1 OPEN as of 2026-08-09.** Ruled rows stay below as history; a reversal
is a new row citing the old, never an edit.

| ID | Date | Workstream | Question (one line) | Default being used meanwhile | Needed by | Status |
|---|---|---|---|---|---|---|
| PENDING-P-004 | 2026-08-09 | canon/language (all reader-facing output) | **Does the CD-012 script guard apply to markdown canon and reader files, or only to Hub-bound JSON payload strings?** Its tiers are field-typed (`text_bn`/`text_en`/titles vs metadata), which are support-book **JSON** fields — that taxonomy has no meaning in a .md file. It matters: existing canon already carries tier-2 glyphs deliberately — `MarkLogic_Rules.md` uses 🔴 🟦 ★ ↑ ↓ as teacher-facing legend notation, and `C5_Bangla_Source_13-23.md` tags lessons 🟦★. Under the strict reading, canon violates canon. | Guard applies to **Hub-bound JSON payload strings only** (its source domain); markdown canon and reader files are unaffected, and the legend glyphs stand. | before the render smoke test asserts §7 conformance on .docx output | OPEN |
| PENDING-P-003 | 2026-08-09 | islamic-studies (+ any Arabic subject) | CD-012 makes Arabic script RED in any string, but islamic-studies and the Arabic subject will need ayat, hadith and du'a. Does tier 1 carve out Arabic-bearing subjects? | — | — | **RULED 2026-08-09 → CD-014** (tier 1 stands for all current workstreams; ground restated as renderer capability; lifts per render path on proven shaping + verbatim-sourced আলিম-reviewed text; `ARABIC-SLOT` placeholder meanwhile). |
| PENDING-P-002 | 2026-08-09 | canon/language + hub-export + support-books | Script-guard sources disagreed (CD-011 cross-check): Hub harness has none, SB validator check 8 has a narrower one than the old canon summary. Which is canon? | — | — | **RULED 2026-08-09 → CD-012** (SB validator's verified scope, 3 tiers; old summary corrected on 3 of 4 items). Harness gap logged upstream as UP-001 / CD-013. |
| PENDING-P-001 | 2026-08-09 | canon (all curation consumers) | REF-1 v1.2 declares Class 1 Bangla/English scope — how is C2–C5 / other-subject curation governed? | — | — | **RULED 2026-08-09 → CD-015** (whole-school scope, extends one class per year; class list read from SCHOOL_FACTS.md; overrides REF-1 §1.2, which is LOCKED and not edited). |
