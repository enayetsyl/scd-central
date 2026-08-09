# REGISTRY.md — workstream index

One row per workstream. Adding a workstream = copy `workstreams/_template/` + add a row here
(AGENTS.md §10). Status: LIVE (producing in this repo) · MIGRATING · PLANNED · GREENFIELD.

| Workstream | Folder | Status | Decision series | Migration step (handoff §5) | Source |
|---|---|---|---|---|---|
| English Skill-Building Drive | `workstreams/english-drive/` | MIGRATING | PD-### (at PD-038) | 2 | live repo `EnglishDrive` |
| Class Test Generator | `workstreams/class-tests/` | MIGRATING | CT-D-### (new) | 2 | Claude project "class test question" |
| Scholarship / MarkLogic | `workstreams/scholarship/` | MIGRATING | CD-### via canon (reader files stay history-free; local `DECISIONS.md` is a pointer) | 1 (canon extract) ✅ · MODEL_PAPERS_POLICY v1.0 (CD-038) | Scholarship Claude project |
| Support Books (সহায়িকা) | `workstreams/support-books/` | **LIVE** | D-### (imported at D-019) | 3 ✅ | SB-Governance + SB-P Production projects |
| Lesson Plans (P03) | `workstreams/lesson-plans/` | **LIVE** | D-PROJ03-### (reconstructed; continuous to D-049) · references: reference import — P00 workstream pending | 4 ✅ | P03 project |
| Question Banks (P04) | `workstreams/question-banks/` | **LIVE** | QB-D-### (at QB-D-010) | 4 ✅ | P04 conventions via master D-051 (CD-036); no corpus imported — starts from policy + pilot |
| English Programme (EIA + phonics) | `workstreams/english-programme/` | PLANNED | EP-D-### (new) | 5 | recovered old-account instructions |
| Islamic Studies C1–5 | `workstreams/islamic-studies/` | GREENFIELD | IS-D-### (new) | 5 | none (new) |
| Accounting | `workstreams/accounting/` | PLANNED | AC-D-### (new) | 5 | recovery package (open: Check-5 423,533; +28,592 residual) |

**Outside this repo:** `scd-hub` (app; LOCKED import contract v1.0 is the only interface) ·
storybook venture (own private repo; shares conventions + vendored neutral tools only).
