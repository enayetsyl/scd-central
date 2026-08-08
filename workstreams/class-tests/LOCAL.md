# LOCAL.md — <workstream name> (template — fill every ⬜)

Read AFTER root AGENTS.md. May tighten the protocol, never loosen it.

## Identity
⬜ One paragraph: what this workstream produces, for whom, classes/subjects covered.

## Status & provenance
⬜ LIVE / MIGRATING / PLANNED · source project(s)/repo · what was imported and when.
Keep the REGISTRY.md row in sync with this section.

## Decision series
⬜ Prefix (e.g. XX-D-###) · current highest number · where the log lives (`DECISIONS.md` here).

## Canon citations used
⬜ List the canon files/IDs this workstream depends on (e.g. canon/marklogic/…, REF-2 names).
Cite, never copy (AGENTS.md §8).

## Artifacts & naming
⬜ File types, naming grammar, where finals live vs `_wip/`.

## Gates
⬜ What `audits/gates.py` checks, and any human gates (e.g. "naturalness = human gate by design").

## Operator workflow
⬜ Who runs sessions (teacher / Principal / reviewer lane) and the exact start/done phrases.

## Session-end sync
"save state and sync" = update `_wip/STATE.md` → append root SESSION_LOG.md block → commit → push.
⬜ Note any workstream-specific additions.

---
**Migration note (step 2):** POLICY: format authority = canon/marklogic (QuestionPolicy + spines);
Mohammadpur reference papers historical only. Vendor docx scripts + fonts via tools/render
(kills per-session rebuild). Add: coverage log (chapters tested per class/term); gates =
mark-total recompute, single-chapter scope, answer-key completeness. CT-scale mark derivation
(time-ratio ≈ 35/180) still needs a CD row in canon/marklogic — currently only in the recovery archive.
