# AGENTS.md — scd-central canonical protocol · v1.1

Every agent session (Claude Cowork, Claude Code, Codex, or any other tool) in this repository
follows this file. `CLAUDE.md` is a pointer here. Per-workstream rules live in
`workstreams/<name>/LOCAL.md`, read AFTER this file; a LOCAL.md may tighten this protocol,
never loosen it. This protocol generalizes the field-proven EnglishDrive CLAUDE.md.

## 1. What this repo is

`scd-central` is the single private monorepo for all SCD school workstreams (see REGISTRY.md).
Outside it: `scd-hub` (the consumer app — integration only via its LOCKED import contract v1.0)
and the commercial storybook venture (own repo; shares conventions and neutral tools only;
absolute no-crossover). `archive/old-account/` is read-only provenance.

## 2. Roles

- **Principal** — sole ruling authority. Rulings, locks, `gold` promotion, canon changes.
- **Teacher** — zero-Git operator: "start" → corrections → "done" per file → "save state and sync".
- **Reviewer (আলিম lane)** — second-human review queue where a LOCAL.md defines one; mirrors the Hub's in-app review.
- **Agent** — proposes, executes gates, logs, never self-approves, never improvises policy.

**Never two agents on one workstream simultaneously.** Different workstreams in parallel are
fine. Each tool commits under its own identity (e.g. `scd-agent-cowork`, `scd-agent-codex`);
each device uses its own fine-grained PAT embedded in the remote URL.

## 3. Session protocol

**Start:** `git pull` first — on any conflict, STOP and report; never resolve silently.
Read order: AGENTS.md → the workstream's LOCAL.md → its `_wip/STATE.md` → its DECISIONS.md
tail → its corrections ledger (if present) → PENDING_PRINCIPAL.md (rows for this workstream).

**During:** all work-in-progress goes to files under the workstream's `_wip/`, with
`_wip/STATE.md` kept current (phase, blockers, next step) — a killed session must be resumable
from files alone. Phase-gated builds: no phase advances past its gate. Promotion out of
`_wip/` only on the Principal's or teacher's explicit "done" for that file.

**End — "save state and sync":** update `_wip/STATE.md`, append a session block to root
`SESSION_LOG.md`, commit, push. Verbatim commands live in each LOCAL.md if they differ.

## 4. Decisions

- Append-only decision logs; a reversal is a new row citing the old one. Never edit old rows.
- Each workstream keeps its native series (PD-### for english-drive, D-### for support-books,
  etc. — see REGISTRY.md). Cross-cutting/canon decisions are **CD-###** in `canon/DECISIONS.md`.
- The agent assigns the next free number itself (verify at source, never from memory) and never
  asks the Principal for a number.
- **Files-over-memory, always.** Before citing any decision, verify it exists at source.
  A citation that cannot be resolved is treated as phantom and flagged, even if the Principal
  supplied it.

## 5. Gates — executed, never reasoned

- Every workstream has `audits/gates.py` (or equivalent) runnable from the repo. "Final",
  "done", or promotion claims require the gate run's **verbatim output pasted in chat** first.
- A red gate returns the artifact to its build phase. No exceptions survive contact; a needed
  exception becomes a decision row + a gate-code change, not a waiver in chat.
- Repo-wide: `python tools/audits/canon_check.py` must pass before any push that touches
  canon/ or adds canon citations; `python tools/audits/tools_check.py` must pass before any
  push that touches tools/.
- A tool is done when it has been **run**, not when it has been placed: every REQUIRED row in
  `tools/MANIFEST.md` carries a `SMOKE.md` recording the command and its verbatim output.

## 6. Corrections ledger + question routing

**Corrections (ledger):** every teacher/Principal correction is logged same-session in the
workstream's CORRECTIONS.md (CR-### rows). The agent re-reads the ledger before drafting.
3+ occurrences of a pattern → mark PATTERN → propose promotion to an executing gate. A fix
applied to one artifact must be checked across the sibling artifacts same-session.

**Questions (routing):** batch questions one message per phase; classify each **[teacher]**
(operational, answer in-flow) vs **[Principal]** (policy/content ruling). Principal items go
to root `PENDING_PRINCIPAL.md` with a needed-by date and a tag `⚑ PENDING-P-###`; the build
continues on stated defaults for non-blocking items. **No promotion or print while the
workstream has an open tag.** A blocking item at its deadline → the agent gives the teacher
exactly one relay sentence for the Principal, verbatim, nothing more.

## 7. Files and naming

- Forward-only naming; no retroactive renames. Supersede-only for locked files: a LOCKED file
  is never edited — a successor version replaces it and the decision row records the supersede.
- Reader-facing files stay clean (no version history inside); history lives in Git commits
  and decision logs.
- Teacher- and reader-facing documents are written in plain, accessible Bengali.

## 8. Canon — cited, never copied

`canon/` holds the shared authority files (curation policy REF-1, names REF-2, MarkLogic ×7,
image rules, language rules, school facts). Workstreams **cite** canon paths/IDs; they never
copy canon content into their own files. `tools/audits/canon_check.py` enforces existence,
resolvable CD-### citations, and duplicate-copy detection. Canon changes are Principal-gated
and logged as CD-### rows. `archive/old-account/` is never cited as current authority.

## 9. Environment workarounds (Cowork)

- "Run new tasks in the cloud" toggle OFF.
- Sandbox cannot unlink inside `.git/` → rename lock files aside (approved standing practice).
- Workspace-boot stalls → fully quit Claude Desktop and retry.
- Any deletion outside `.git/` requires the agent to state the reason in chat FIRST. Teacher's
  standing rule: Allow at task start; Deny+ask on unexpected deletes.
- On any failure the teacher relays the exact error text to the Principal — no paraphrase.

## 10. Adding a workstream

Copy `workstreams/_template/` to `workstreams/<name>/`, fill LOCAL.md, add a REGISTRY.md row
(name, status, decision series, source). That is the whole procedure — agent-executable from
one sentence.

## 11. Hub integration

Artifacts destined for SCD Hub pass `tools/hub-export/validate_import.py` (the vendored LOCKED
contract v1.0 harness) at authoring time. Flow: envelope JSON → harness → Hub import `draft` →
in-app teacher review → Principal promotes `reviewed→gold`. Nothing else is an integration path.
