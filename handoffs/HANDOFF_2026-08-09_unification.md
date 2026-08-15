# HANDOFF — SCD Unification & Agent-Repo Migration
**Date:** 2026-08-09 · **From:** the long migration/survey chat · **Owner:** SCD (Principal, School for Community Development, Sylhet; also full-stack dev at 365 AI Tech; builder of SCD Hub)

**Purpose of this file:** a new chat, given this file (plus `SCD_UNIFICATION_SURVEY.md`), must be able to continue the work without re-asking anything settled here.

---

## 1. What this whole effort is

SCD runs ~12 school workstreams (curriculum, question papers, support books, storybooks, accounting, app) that historically lived in separate Claude Projects with chat-resident knowledge — slow, error-prone (teacher had to re-check everything), and vulnerable (an earlier Claude account ban destroyed working memory; a recovery archive was built from the export).

**The decided direction:** move production to **Git repos + Claude Desktop agents (Cowork)** with governance-as-CLAUDE.md and **executed script gates** instead of model-asserted checks. This is field-proven (see §3). The end state is a **grand unification**: one central repo, shared canon, SCD Hub integration, easy project addition (plan agreed — see §5).

## 2. What is LIVE and running today

### EnglishDrive repo (the reference implementation)
- **Private repo:** `github.com/enayetsyl/EnglishDrive` (flipped private after exam papers were found exposed).
- Full corpus imported: governance (Charter v1.5, Run Book v1.17, Decision Log now **PD-001…PD-038**, 5 Drive Plans, specs), File 2 xlsx (pools + batch orders), exam papers, block masters C1–C5, extracts, assignments.
- **CLAUDE.md** governs agent sessions: pull-first (stop on conflict), WIP-to-file + `_wip/STATE.md`, phase gates, mandatory scripted audits with pasted verbatim output before any "final", auto-numbered PDs (agent assigns next free number, never asks), promotion out of `_wip/` only on explicit "done", forward-only naming (new stem `C#_ENG_Block##_Topic_v#.md`, no retroactive renames), lock-file rename-aside workaround, delete-outside-.git requires stated reason first, "save state and sync" command, SESSION_LOG.md appended per session.
- **audits/scripts/run_all.py**: 11+ gates incl. de-patterning, CW↔HW overlap, PT zero-overlap (with `"audit_scope": "pt_overlap_only"` flag per PD-032/034 for cross-half 6a sheets), held-word vs File 2 Batch Order (use BatchOrder file, not Pool), mark totals, sacred-word, values lexicon, **plus new promotions**: option-list completeness + HW-key-transcribable (PD-037), **cross-sheet zero-repeat gate (PD-036, `CROSS_SHEET_MAX_REPEATS = 0`; PD-038 rules it supersedes the old CW↔HW ≤2 allowance, which stays as backstop)**, and a **citation-check** (every "PD-###" in the repo must resolve; last sweep: 58 files, 550 citations, CLEAN).
- **Corrections ledger live:** `governance/CORRECTIONS.md`, 19 rows (CR-001…CR-019), 4 PROMOTED to executing gates, CR-010 naturalness marked "human gate by design", CR-005/012–016/018 OPEN. CLAUDE.md §5A: agent logs every teacher/Principal correction same-session, re-reads ledger before drafting, 3+ occurrences → PATTERN → propose promotion; a fix on one sheet must be checked across the block's other sheets same-session.
- **Auth model:** fine-grained GitHub PAT embedded in remote URL, one token per device (`EnglishDrive-agent`, `teacher-laptop`), 1-year expiry (Aug 2027 — renewal reminder needed). Cowork sandbox can't reach Windows Credential Manager; PAT-in-URL is the fix. GitHub CLI auth only helps the human terminal.
- **Environment quirks (Cowork):** "Run new tasks in the cloud" toggle must be OFF; sandbox cannot unlink inside `.git/` → agent renames lock files aside (approved standing practice, in CLAUDE.md); workspace-boot stalls → fully quit Claude Desktop and retry; delete permission prompt recurs per task — teacher's rule is Allow at start, agent must still state any non-.git deletion in chat first.
- **Teacher workflow:** open Cowork → attach folder → "start" → review → "done" per file → "save state and sync". `TEACHER_GUIDE.md` (EN+BN, bilingual line-by-line) exists in outputs of the old chat and should be committed to the repo root if not already; three exception rules: Principal questions get relayed verbatim, Deny+ask on unexpected deletes, exact-error-text to Principal on failures.
- **Teacher feedback received:** "more complex, too many questions, worksheets still need repeated fixing." Responses designed (question-routing + ledger, see §4-A) — ledger is DONE; **question-routing (PENDING_PRINCIPAL) is NOT yet implemented**.

### In-flight build: C2 Block 6b (have/has + match-to-make-a-sentence)
- Phase 1–3 done in Cowork. Key rulings: PD-025 governs — **one PT per week, own C2B06b-PT** (my earlier "combined 6a+6b PT / PD-028" citation was phantom — agent caught it by verifying at source; files-over-memory is the standing rule). Sacred words barred from match strips (PD-031). Cross-half grading allowed with widened PT audit scope (PD-032). Rulings 1–7 given (secular mirror of AN25 Q11 format incl. mis-paired-sentence form; oral-only I/we/you have; W5+W6 verb pool staged by day; held animals only, no giraffe; PT split A10·B5·C5·D6·E4=30; assignment via Generator Spec after Coverage Log reconciliation-from-artifacts).
- **Next step: Phase 4 — the hand-authored sentence bank comes to the Principal for word-by-word approval before any worksheet uses it.** This build is the first real test of whether teacher correction volume drops.
- Parallel session did a C4B06 v1.7 PT review; its corrections were cross-logged (CR-017/018/019). **Open item for the parallel session:** Part E cut 5→2 prompts (PT 36→33) — needs a PD with rationale or revert; also CR-018's rationale closes there.

### Scholarship / MarkLogic (Sylhet branch)
- Seven files now: `MarkLogic_Rules.md` + 4 spines (BAN/ENG/MATH/SCI-BGS) + **`MarkLogic_QuestionPolicy.md`** (domain ratios, answer-length by marks, repetition rules, consolidated content restrictions — an organic canon file) + `C5_Bangla_Source_13-23.md`. C5 = NAPE 2026 unchanged, C1–C4 derived with cause-codes D0/D1/D3–D6; **all papers 100 marks only (80-mark withdrawn)**; NAPE beats school rules (I-4 half-mark exception ENG S10). Three-tier assessment: HY 100 + Annual 100 + CT 20–30/chapter; skill-question vs chapter-question classification; yearly syllabus-split sheet is the only changing file. First production outputs exist (C5 Bangla annual paper, split sheet, two 25-mark CTs). Chapter 12 permanently excluded.
- **Known staleness:** Rules §6 still says ENG/MATH spines "not yet built" (they are). **Action owed:** upload all 7 files to the scholarship project's knowledge; fix §6.
- **Branch fact (memory-corrected):** system governs **Sylhet**; Mohammadpur papers were only the source/guide corpus (old iron rule: "Muhammadpur STRUCTURE + Sylhet CONTENT").

### Class Test Generator project
- **Transition declared but not yet written into its instructions:** CTs follow MarkLogic (QuestionPolicy + spines) going forward; Mohammadpur papers historical only. **Action owed:** one-line edit to that project's instructions naming `MarkLogic_QuestionPolicy.md`.

### SCD Hub (github.com/enayetsyl/scd-hub)
- Live MERN/GraphQL/Expo platform, real data in Atlas (91 students, 23 staff). **LOCKED import contract v1.0 + Python conformance harness (L1–L4)**; flow: envelope JSON → harness → import `draft` → in-app teacher review (feedback designed to round-trip to Claude) → Principal promotes `reviewed→gold`. Homework tracker + routine module complete; HR designed; de-identified question-usage feed back toward authoring. **⚑ Repo is PUBLIC — recommended private (docs carry LOCKED school policy); not yet done.**
- Atlas backups already go to the user's **100 GB Google Drive** via script.

## 3. Proven lessons (why this design)
Agent+repo caught, in real runs: a wrong answer-key entry ("The honest teacher") via 285-item programmatic diff; a phantom PD citation *supplied by me*; stale coverage logs; a silently-lost C1 Block 5 master; parallel-session corrections owed to the ledger. Governance shape (append-only decisions, supersede-only files, Principal gate, executed validators, disposable chats) was independently invented **six times** (EnglishDrive, P03, old Software, SB programme ×2, storybook venture, Hub) → unification = standardization, not invention.

## 4. Decisions taken but NOT yet implemented
- **A. Question-routing for the teacher:** batch one message/phase; classify [teacher] vs [Principal]; Principal items go to root `PENDING_PRINCIPAL.md` with needed-by dates; build continues on defaults for non-blocking items, tags `⚑ PENDING-P-###`; **no promotion/print with open tags**; blocking item at deadline → agent gives teacher one relay sentence only. Principal clears the queue in minutes from any device.
- **B. AGENTS.md as canonical protocol** (ChatGPT/Codex reads AGENTS.md; CLAUDE.md becomes a 3-line pointer) so ChatGPT can work the same repos; per-tool commit identities; never two agents on one workstream simultaneously; gates are scripts so tool-agnostic.
- **C. Storybook assets on Google Drive via rclone** (`tools/assets/sync.py`; `assets_manifest` filename+hash per book.json; migrate to R2 only when storefront launches). Repo never inside Drive-for-Desktop folder.
- **D. `.claudeignore`** for archive/, generated outputs, image dirs (context + prompt-cache protection). Graphify tool evaluated: legitimate, skip for launch, revisit for canon/ queries later.
- **E. Token renewal reminder** (Aug 2027) — user to set.

## 5. The Grand Unification Plan (agreed inline; starter kit NOT yet generated)
- **One private monorepo `scd-central`** for all school workstreams. Outside it: `scd-hub` (consumer app), storybook venture (own private repo, commercial IP, shares conventions + vendored tools only), `archive/old-account/` inside as read-only provenance.
- Layout: root AGENTS.md (+CLAUDE.md pointer), REGISTRY.md, SESSION_LOG.md, PENDING_PRINCIPAL.md; **`canon/`** (islamic-curation REF-1, image-rules, names REF-2, marklogic 7 files, language rules, school facts, canon DECISIONS.md) — **cited never copied**, with a `canon_check.py` audit; **`tools/`** (audits convention, render with vendored Nikosh/Noto + docx scripts, images/apply_strips.py, hub-export with vendored `validate_import.py`, assets/rclone sync); **`workstreams/`** (_template + english-drive, class-tests, scholarship, support-books, lesson-plans, question-banks, english-programme, islamic-studies, accounting); each workstream = thin LOCAL.md over the shared protocol.
- **Hub integration = the existing LOCKED contract**, nothing new: repos vendor the harness so artifacts are born conformant; Hub's usage feed is the return path.
- **New project = copy `_template/`, add REGISTRY row** — agent-executable from one sentence.
- Roles: Principal (rulings/gold) · teacher (start/done) · reviewer-আলিম lane (SB queue; mirrors Hub review) · agent (proposes, executes gates, never self-approves). Per-device PATs.
- **Migration order:** 1) create scd-central + extract canon (REF-1/REF-2, MarkLogic 7, image rules, script guard, school facts) → 2) fold in EnglishDrive + class-tests (kills per-session font rebuild) → 3) support-books (ends its three-way version split: production v2.0 / governance-project v1.0 uploads / approved v2.2 in chat-space; unblocks deferred Puppeteer print pipeline) → 4) lesson-plans (P03) + question-banks + hub-export gate → 5) accounting revival (open items: 423,533 Check-5 break; 28,592 residual; feeds Hub HR), english-programme rebuild (recovered EIA+phonics instructions), islamic-studies greenfield.

## 6. Key artifacts of this chat (carry forward)
- **`SCD_UNIFICATION_SURVEY.md`** — per-workstream survey, 7+ sections done (P03, EnglishDrive, Scholarship incl. post-survey growth, Recovery Archive incl. accounting + all-28-project map, Class Tests, Support Books governance+production, Storybook venture, SCD Hub). Re-upload it alongside this handoff; it is the evidence base for the plan.
- `TEACHER_GUIDE.md` (EN+BN) — commit to EnglishDrive root if not already.
- `EnglishDrive_starter.zip` — historical; the live repo supersedes it.

## 7. Immediate next actions (priority order)
1. **Generate the `scd-central` starter kit** (user has effectively approved the plan; kit = AGENTS.md + CLAUDE.md pointer, canon skeleton with existing files slotted, `_template/`, REGISTRY.md, canon_check.py, .claudeignore, .gitignore) — then git init/push like EnglishDrive.
2. Implement **§4-A question-routing** in EnglishDrive's CLAUDE.md (one Cowork prompt).
3. **C2B06b Phase 4** — sentence bank to Principal; watch teacher correction volume against the ledger.
4. Hygiene: upload 7 MarkLogic files to scholarship project + fix Rules §6; edit class-test project instructions (MarkLogic authority line); make scd-hub private; close the C4B06 Part-E PD in the parallel session; set token-renewal reminder.

## 8. Working style (binding)
Precise and concise; lead with the key point; ONE recommendation with 1–2 line justification; no option lists unless asked; plain accessible Bengali for teacher/reader-facing docs; Principal applies UI edits by hand → copy-paste-exact patches; files-over-memory always; flag-don't-improvise; step-by-step one-step-at-a-time when doing setup work with the user; verify at source before citing any decision.
