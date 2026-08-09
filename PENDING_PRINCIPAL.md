# PENDING_PRINCIPAL.md — question queue for the Principal

Agents append rows (AGENTS.md §6); the Principal clears them from any device.

**Three statuses, because they gate different things (CD-042).**

| Status | Meaning | Blocks promotion/print? |
|---|---|---|
| **OPEN** | Principal-owed. A ruling is needed and only he can give it. | **YES** (AGENTS.md §6) |
| **FLAGGED** | File-owed. The ruling is made; it awaits verification against a named file that is not yet in the repo. The stated default stands and is tagged in the artifact. | **NO** |
| **RULED / CLOSED** | Settled. Row stays as history. | No |

A FLAGGED row is closed **only on verification at source** — never by elapsed time, never by a
second agent deciding the default looks right.

**Queue status as of 2026-08-09: 0 OPEN · 1 FLAGGED (PENDING-P-005) · the rest ruled.**
Ruled rows stay below as history; a reversal is a new row citing the old, never an edit.

| ID | Date | Workstream | Question (one line) | Default being used meanwhile | Needed by | Status |
|---|---|---|---|---|---|---|
| PENDING-P-006 | 2026-08-09 | class-tests (+ question-banks) | The accepted Ch21 class test uses the name **আসিফ**, carried from the NCTB অনুশীলনী ৪, but আসিফ is not in REF-2's C5 pool and QuestionPolicy §৯ requires every student-facing name to come from it. Is the accepted CT superseded, or are names inside a quoted NCTB exercise carved out? | Bank items use **সাবিত** (REF-2 C5 male #3). The accepted CT is **not edited**. | before the next Ch21 CT is printed | **CLOSED 2026-08-09 → CD-042.** Principal ruling: the accepted Ch21 CT stays untouched and **আসিফ is grandfathered in that one historical paper only**. It is not a carve-out for quoted NCTB exercises: **every new item uses REF-2 C5-pool names**, and **সাবিত** in the bank is confirmed correct. Logged QB-CR-005 / class-tests CR-005. |
| PENDING-P-005 | 2026-08-09 | question-banks | Which `TOP-BAN-C5-##` tag do the S03 near-homophone sentence items for পাঠ ২১ carry? পাঠ ২১'s attested tags are `-07`, `-01`, `-11`; `-02` is attested as *sentence/রচনা* from the U20 Chapter Plan but not for পাঠ ২১, and the per-subject revision chart that defines the numbers is not in this repo. | **`TOP-BAN-C5-02`**, FLAGGED not confirmed. 8 items affected (HW 5 · AS 2 · CT 1). **Do not change it** on any agent's judgement. | on arrival of the revision chart | **FLAGGED 2026-08-09 → CD-042** (was OPEN). Principal will stage the revision chart — the file defining the `TOP-BAN-C5` numbers — into `_inbox/` in a coming session. **Converted from Principal-owed to file-owed: non-blocking.** It does not block wave-1 promotion and does not block wave-2 authoring. **Close only on verification against that file.** |
| PENDING-P-004 | 2026-08-09 | canon/language (all reader-facing output) | Does the CD-012 script guard apply to markdown canon and reader files, or only to strings bound for a renderer? Field-typed tiers have no meaning in a .md file, and canon already carries legend glyphs deliberately. | — | — | **RULED 2026-08-09 → CD-018** (guard governs strings entering a mechanical render path; extends to new paths on vendoring; human-read markdown out of scope; each path proves its glyph set in its own SMOKE.md). |
| PENDING-P-003 | 2026-08-09 | islamic-studies (+ any Arabic subject) | CD-012 makes Arabic script RED in any string, but islamic-studies and the Arabic subject will need ayat, hadith and du'a. Does tier 1 carve out Arabic-bearing subjects? | — | — | **RULED 2026-08-09 → CD-014** (tier 1 stands for all current workstreams; ground restated as renderer capability; lifts per render path on proven shaping + verbatim-sourced আলিম-reviewed text; `ARABIC-SLOT` placeholder meanwhile). |
| PENDING-P-002 | 2026-08-09 | canon/language + hub-export + support-books | Script-guard sources disagreed (CD-011 cross-check): Hub harness has none, SB validator check 8 has a narrower one than the old canon summary. Which is canon? | — | — | **RULED 2026-08-09 → CD-012** (SB validator's verified scope, 3 tiers; old summary corrected on 3 of 4 items). Harness gap logged upstream as UP-001 / CD-013. |
| PENDING-P-001 | 2026-08-09 | canon (all curation consumers) | REF-1 v1.2 declares Class 1 Bangla/English scope — how is C2–C5 / other-subject curation governed? | — | — | **RULED 2026-08-09 → CD-015** (whole-school scope, extends one class per year; class list read from SCHOOL_FACTS.md; overrides REF-1 §1.2, which is LOCKED and not edited). |
