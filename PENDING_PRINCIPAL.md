# PENDING_PRINCIPAL.md — question queue for the Principal

Agents append rows (AGENTS.md §6); the Principal clears them from any device.
No promotion/print in a workstream while it has an OPEN row here.

| ID | Date | Workstream | Question (one line) | Default being used meanwhile | Needed by | Status |
|---|---|---|---|---|---|---|
| PENDING-P-003 | 2026-08-09 | islamic-studies (+ any Arabic subject) | **CD-012 makes Arabic script RED in any string — but this is an Islamic school.** `workstreams/islamic-studies/` (C1–C5, greenfield) and the Arabic subject named in REF-1 §1.2 will need Qur'anic ayat, hadith and du'a in Arabic script. Per CD-013 the underlying cause is renderer glyph support, not doctrine — so the fix is likely font support in the Hub renderer, not banning Arabic from Islamic content. Does tier 1 carve out Arabic-bearing subjects, or do they wait for renderer support? | CD-012 applies as ruled — Arabic stays RED everywhere. Nothing is being authored in islamic-studies yet, so nothing is blocked today. | before islamic-studies or Arabic authoring begins | OPEN |
| PENDING-P-002 | 2026-08-09 | canon/language + hub-export + support-books | Script-guard sources disagreed (CD-011 cross-check): Hub harness has none, SB validator check 8 has a narrower one than the old canon summary. Which is canon? | — | — | **RULED 2026-08-09 → CD-012** (SB validator's verified scope, 3 tiers; old summary corrected on 3 of 4 items). Harness gap logged upstream as UP-001 / CD-013. |
| PENDING-P-001 | 2026-08-09 | canon (all curation consumers) | REF-1 v1.2 governs Class 1 Bangla/English only (§1.2; other subjects + C2–C5 await v2.0) — how is C2–C5 / other-subject curation governed meanwhile? | REF-1 cited only within its declared C1 Bangla/English scope; out-of-scope citations are flagged, not auto-applied | before any C2–C5 curation promotion or print | OPEN |
