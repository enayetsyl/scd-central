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
| Question Banks (P04) | `workstreams/question-banks/` | **LIVE** | QB-D-### (at QB-D-013) | 4 ✅ | P04 conventions via master D-051 (CD-036); no corpus imported — starts from policy + pilot |
| English Programme (EIA + phonics) | `workstreams/english-programme/` | PLANNED | EP-D-### (new) | 5 | recovered old-account instructions |
| Islamic Studies C1–5 | `workstreams/islamic-studies/` | GREENFIELD | IS-D-### (new) | 5 | none (new) |
| Accounting | `workstreams/accounting/` | PLANNED | AC-D-### (new) | 5 | recovery package (open: Check-5 423,533; +28,592 residual) |
| Curriculum Foundations (P00) | `workstreams/curriculum-foundations/` | **LIVE** | `D-PROJ00-###` (imported at 072) · **canonical home of the master `D-###` series** (README §3, at D-053) | 4 ✅ | P00 project — README · DECISIONS · TODO · CROSS_PROJECT_INDEX · GLOSSARY |
| NCTB Stability (P01) | `workstreams/p01-nctb-stability/` | PLANNED | `D-PROJ01-###` (attested to 006 in REF-04; register not yet imported) | 5 | scaffold only — no content this session; method is REF-04 |

## Initiative-wide locations (NOT workstreams)

The table above is **one row per workstream**, by its own header rule. These are initiative-wide
and belong to no lane, so they are listed separately rather than smuggled into that table.

| Location | Folder | Status | Role |
|---|---|---|---|
| Session-continuity chain | `handoffs/` | **LIVE** (created 2026-08-15) | The handoff chain. **Current file is live; all others are read-only imports, cited never continued** (CD-034 / CD-043(b)). Lived outside the repo until 2026-08-15, which is how a handoff came to state a tip two commits and four CD rows stale — CD-133's shape one level up. See `handoffs/README.md`. |
| Session record | `SESSION_LOG.md` | **LIVE** | Append-only narrative record, one entry per session. |

## Production sequence (Principal directive, CD-045)

**① NCTB sources to per-chapter markdown** (`canon/sources/SOURCE_POLICY.md`) →
*In flight. **C5 English** 20/20 units extracted — Unit 1 signed and in `canon/sources/c5/english/`,
Units 2–20 built in `canon/_wip/c5-english/` awaiting the Principal's spot-check (CD-046, CD-047).
**C5 Bangla** পাঠ ১–১১ built in `canon/_wip/c5-bangla/`, extraction complete, 77 sign-off rows all
unsigned; পাঠ ১২ excluded by ruling, পাঠ ১৩–২৩ already canon (CD-050, CD-051).
**C5 গণিত** in `canon/_wip/c5-math/`: book classified §7.7, all ten অধ্যায় boundaries confirmed
at both ends, both source gates fitted for `অধ্যায়`, and a third gate built for it —
`math_arith_check.py`, the book's only machine second channel (CD-052/053/057–067).
**অধ্যায় ১ and ২ COMPLETE** (ছাপা ১–৩০), slot cross-references written, all mechanical checks
PASS, **68 sign-off rows owed to the Principal**. **অধ্যায় ৩–১০ (ছাপা ৩১–১৮১) not started.**
Cadence is up to three complete chapters per sitting, stop-rule outranking (SOURCE_POLICY §7.13).
Order within C5 is now English → Bangla remainder → other subjects (SOURCE_POLICY §7.1).* →
**② C5 model papers and CTs, remaining subjects** (`workstreams/scholarship/`) →
**③ C1–C4** → **④ question pools** (`workstreams/question-banks/`).

Each step depends on the one before it. **পাঠ ২১ wave 2 waits for step ④** — the pilot exists to
have proven the step-④ machinery before step ④ arrives, not to run ahead of it. A session that
finds wave-2 material sitting ready should still not start it.

**Outside this repo:** `scd-hub` (app; LOCKED import contract v1.0 is the only interface) ·
storybook venture (own private repo; shares conventions + vendored neutral tools only).
