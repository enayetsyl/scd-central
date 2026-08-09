# LOCAL.md — scholarship / MarkLogic

Read AFTER root `AGENTS.md`. May tighten the protocol, never loosen it.

## Identity

The Sylhet branch's mark-scheme workstream: **model papers** — one model HY (100) and one model
Annual (100) per class × subject, plus one model CT (25 marks · 35 minutes) — generated from the
MarkLogic spines and used as the reference implementation every real paper is compared against.
Classes per `canon/school-facts/SCHOOL_FACTS.md`; subjects BAN · ENG · MATH · SCI · BGS.

The operative specification is `MODEL_PAPERS_POLICY.md` in this folder.

## Status & provenance

**MIGRATING** · migration step 1 (canon extract, done) · source: the Scholarship Claude project.
The seven MarkLogic files were extracted to `canon/marklogic/` at CD-004 and are canon from there;
this folder holds the production side only. `MODEL_PAPERS_POLICY.md` adopted 2026-08-09 (CD-038).
**No model paper has been produced yet.**

## Decision series

**`CD-###` in `canon/DECISIONS.md`** — this workstream has **no local series**, per its REGISTRY
row: its reader-facing files stay history-free, and its rulings are canon-level because every
paper-producing workstream depends on them (CD-002). `DECISIONS.md` in this folder is a pointer,
not a log.

## Canon citations used

- `canon/marklogic/MarkLogic_Rules.md` · the four spines · `MarkLogic_QuestionPolicy.md`
- `canon/marklogic/C5_Bangla_Source_13-23.md` — the only extraction available today
- `canon/sources/SOURCE_POLICY.md` — where real questions come from
- `canon/school-facts/SCHOOL_FACTS.md` — the class list (load-bearing, CD-015/CD-017)
- `canon/names/REF-2_Content_Register.md` · `canon/language/LANGUAGE_RULES.md`
- `canon/islamic-curation/REF-1_Curation_Policy.md` — via QuestionPolicy §৯

Cite, never copy (AGENTS.md §8).

## Artifacts & naming

| Artifact | Path | Naming |
|---|---|---|
| Model paper (in build) | `_wip/` | `MODEL_C<n>_<SUBJ>_<HY\|ANNUAL\|CT>_v<v>.md` |
| Model paper (approved) | `models/` | same stem; supersede-only once marked MODEL |
| Gate reports | `reports/` | `MODEL_C<n>_<SUBJ>_GATES_<date>.txt` |

Forward-only naming; an approved model is never edited, only superseded (AGENTS.md §7).

## Gates

`audits/gates.py` is the unfilled template and **FAILS by design** — a workstream with zero gates
cannot declare anything final. Its gates (mark-total recompute · slot-by-slot spine match ·
domain-ratio · script guard) are written when the first C5 model paper is built.

Render path: `tools/render/ct_docx.py` (accepted CD-023). The reference CTs under
`tools/render/reference/` are **FORMAT reference only**; their ৪৫ মিনিট line is superseded by
CD-021 and must never be copied.

## Operator workflow

Principal- or agent-driven authoring, one class × subject per session. Each model paper is
**Principal-approved individually** before it is marked MODEL.

## Session-end sync

"save state and sync" = update `_wip/STATE.md` → append a root `SESSION_LOG.md` block → commit →
push.
