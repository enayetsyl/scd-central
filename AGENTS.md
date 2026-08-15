# AGENTS.md — scd-central canonical protocol · v1.4

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

### 3.1 Sync approval — the base rule, and the ruling-only carve-out (Principal ruling 2026-08-12, CD-079)

**Base rule, in force throughout and recorded here for the first time: the agent syncs
only on the Principal's explicit approval.** §3's End clause above describes the *ritual*
— update STATE.md, append to SESSION_LOG.md, commit, push — and is left exactly as written.
**The push step of that ritual waits for the Principal.** Committing does not.

**Carve-out.** A commit **whose entire diff is text the Principal has already ruled in
session** is **pre-approved to push**, with no further named-commit approval. This covers
decision rows, `PENDING_PRINCIPAL.md` entries, and §-amendments that **execute** a CD row
already given.

**The agent verifies before invoking it, and states the verification in the push report:**
the diff touches **no code, no gate, no extraction content, and no governance text beyond
the ruling as given**. One added word the Principal did not rule makes it an ordinary commit.

**Everything else still waits:** extraction work, gate and tooling changes, and new
governance text not yet ruled sync **only on explicit Principal approval**.

**SECOND CARVE-OUT — THE TEACHER LANE (CD-141, 2026-08-15).** An agent working the bank-authoring
lane may push without per-commit approval, but only where **class AND path both fall inside the
boundary** (build · corrections · log · promotion, under `workstreams/question-banks/` and its
`banks/envelopes/`) **and the full suite is CLEAN including `PLAN` and `ENVELOPE-SYNC`, with `N/A`
excluded from CLEAN**. Anything else — any FAIL, any file outside scope, any question that needs a
ruling — **stops and reports, and is never put to the teacher**, who cannot rule (§2). The row
carries the rest, including the 40-item consequence and the dry run required before handover.
**Read CD-141 before relying on this sentence; this pointer is not the authority.**

**Why:** a ruling-only commit created *after* a named-commit approval was correctly held
under the base rule, costing a round-trip to release text the Principal had already given.
**The hold protected nothing.**

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

### 5.1 Gate-design rule — a gate that forbids naming the defect makes the defect unwriteable (CD-089)

**Every new gate is checked against this before it ships, and the check is recorded in its
`SMOKE.md` or selftest.** A gate that scans authored text for a forbidden token will also match the
places that exist **in order to say the token is forbidden** — the corrections ledger, the
disagreement log, the decision row that retires it, the README that explains the retirement. When
that happens the gate has not caught an error; it has made the error unrecordable, and the author
routes around it by not naming the thing. **A rule nobody can write down is not enforced, it is
forgotten.**

**The exemption, in three parts, identical at every site:**

- **A citation inside `backticks` is exempt.** Inline code is already markdown's way of saying
  "literal string, not prose", the escape is visible in the source rather than implicit, and every
  legitimate citation is one edit away from being correct markdown.
- **Bare prose is still counted.** The exemption is for naming the defect, not for committing it.
- **Fenced blocks are still checked.** A fence carries authored content, so contamination there is
  contamination.

**Scope the exemption to the check whose reason it is, never wider.** At REF-CITE the reason is
about naming the *retired* number, so the exemption covers the retired-number census and **not**
phantom resolution — a citation that resolves to nothing is broken whether or not it wears
backticks, and a wider reading would hollow out the resolver (CD-085(c), ruled not assumed).

**Three sites, one rule** — `SOURCE_POLICY` §7.16 (the Assamese script gate, source lane) ·
CD-085 (`canon_check.py` REF-CITE, retired-number census) · CD-089 (`PLACEHOLDER`, both repo-wide
gates). Each was discovered the same way: the gate went red on the file documenting the thing the
gate exists to catch. **The third one is why this is a design rule and not a third patch.**
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

**Human review — WHERE IT SITS (CD-142, 2026-08-15).** §6's review splits three ways.
**Item-level content review moves to the Hub's subject experts** — whether a question is good,
whether a teacher-supplied key is right. CD-136(g) named the Principal because the Hub lane did not
exist yet, **not because the judgement is his by nature**. **The plan-level countersign is replaced
by the `PLAN` gate**, which holds the arithmetic a human was counting by hand. **The Principal
retains** rulings, gate and tooling changes, canon and policy, debugging, promotion `reviewed →
gold` (a Hub act, CD-003), and revocation. **The venue moves; the standard does not.**

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
- **An aside goes to `.git/lock-debris/`, never to wherever it happened to be (CD-056).** git
  parses every entry under `refs/` as a ref, so a `main.lock.aside-…` left *inside*
  `refs/remotes/origin/` is read as a ref named that, and the next pull dies with
  **`fatal: bad object refs/remotes/origin/main.lock.aside-…`** followed by
  `did not send all necessary objects` — a failure that looks like a corrupt remote and is not
  one. Recorded because the aside practice itself created it. **Move aside files out of every
  git-parsed path in one step**; `.git/lock-debris/` exists for this and is the only destination.
- **Each git write re-creates the lock it cannot remove.** `git add` finishing successfully still
  leaves `index.lock` behind, so the *next* command fails. Move the lock aside immediately before
  each git write, not once at the start of the session.
- **`GIT_INDEX_FILE` IS NOT A SUBSTITUTE FOR MOVING THE LOCK ASIDE (TOOLS-CR-003).** Committing
  with `GIT_INDEX_FILE=<tmp>` works, but it **redirects the index without updating `.git/index`**,
  which is left describing the pre-commit tree. **The next ordinary `git add` then stages the exact
  inverse of the commit just made**, and **no gate catches it** — the pre-change rules are
  internally consistent, so the suite prints CLEAN on a repo that has silently un-ruled its own
  decisions. **If it is used at all, `git reset` MUST follow the commit before any further
  staging.** The aside practice above has no such cost and is the one to use.
- **`.git/lock-debris/` MUST BE CLEARED PERIODICALLY, AND IT IS THE PRINCIPAL'S JOB, NOT AN
  AGENT'S (TOOLS-CR-004).** The aside practice above has no cleanup step and never had one; the
  folder reached **145 entries across three sessions** before anyone looked. **The largest group
  is `maintenance.lock`, written by git's own background maintenance — so the folder grows even
  when no agent is working**, and an end-of-session trigger would miss the majority of it. The
  sandbox cannot perform any of this: it cannot unlink inside `.git/`.
  **Procedure, in this order — the order is the point:**
  **1. `del /s /q .git\*.lock`  ·  2. `git gc --prune=now`  ·  3. `rmdir /s /q .git\lock-debris`.**
  **`gc` itself fails on stale locks**, so a cleanup beginning with `gc` cannot begin at all. And
  a *failed* `gc` leaves **`gc.pid`** and **`packed-refs.lock`** behind, so blockers surface **one
  per attempt** — five had to be cleared serially on 2026-08-15. Expect to repeat step 1.
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

## 12. `_inbox/` — staging and classification (CD-086)

`_inbox/` is the repo's single staging area. It is **gitignored**, so anything in it exists on one
machine only; an agent on another device cannot see it and **stops rather than improvising**
(the failure recorded at CD-026).

### 12.1 What may be staged

Anything the Principal puts there. In practice the traffic falls into four classes, and **the class
decides the destination** — a staged file is not routed by where it looks like it belongs, but by
what kind of thing it is. Getting the class right is most of the work; the table is the whole rule.

| Class | Examples | Destination |
|---|---|---|
| **Source scans** | NCTB textbook PDFs, OCR drafts staged beside them | governed by `canon/sources/SOURCE_POLICY.md` §2.1 and §7.14 — **this section does not touch them** |
| **Canon references** | LOCKED REF files, policy documents several workstreams cite | `canon/` — the subtree that already holds that kind of authority; a REF file to `canon/refs/` with a `canon/refs/MANIFEST.md` row |
| **Workstream registers** | `PROJECT00_*`, `PROJECT04_*` decision logs, READMEs, TODOs | the owning `workstreams/<name>/`; read-only imports to its `references/` per CD-034 |
| **Assets** | fonts, images, spreadsheets consumed by a tool | `tools/` beside the tool that consumes them, with a `tools/MANIFEST.md` row |

**SOURCE_POLICY §2.1 governs scans and is not stretched to cover the other three.** It is written
about photographing a printed book; a policy import is not that, and reading it as though it were
is how a rule ends up governing something it never mentioned.

### 12.2 Who classifies

**The agent classifies; the Principal approves the destination for anything that is not obvious.**
Classification is a proposal like any other (§2 — the agent never self-approves).

### 12.3 A file that cannot be classified is reported, never moved

If a staged file matches no class, or matches two, or its identity cannot be verified at source —
**it stays in `_inbox/` and is reported.** A guess that lands in `canon/` is worse than a file left
staged, because the guess acquires the authority of its new location and the next session reads it
as settled.

**Report, do not move, in particular when:** the file's own header names a different ID than its
filename · the set is partial against the manifest it belongs to · two staged files claim the same
ID · the file is a register whose owning workstream does not exist yet.

### 12.4 Duplicates of existing canon are reported for deletion, never silently overwritten

Before moving anything into `canon/`, the agent checks whether canon already holds it, **by hash,
not by filename** — the unification import found five byte-identical duplicates whose names
matched and two whose names did not.

- **Byte-identical to a canon file** → the staged copy is **redundant**. The agent **reports it,
  with the md5 of both sides, and deletes only on approval** (§9's deletion rule applies unchanged:
  state the reason in chat first).
- **Same ID, different bytes** → **stop.** This is a version question and it is the Principal's.
  Never overwrite; never assume the staged copy is newer because it was staged later.
- **Already in canon under a different name** → the manifest row points at the **existing** path.
  **No second copy is made inside `canon/`** — that is precisely what §8 forbids, and a duplicate
  inside canon is invisible to `canon_check.py`'s NO-COPY check, which only looks *outside* canon.

*The second bullet was flagged at drafting as unenforceable — a gate can detect same-ID-different-
bytes but cannot rule on it. **The flag is rejected, and the reason is the section's purpose:** this
clause does not tell a gate what to do, it says **whose call it is**. That is protocol, not gate
logic, and a rule is not weaker for being addressed to a person.*

### 12.5 What leaves `_inbox/` leaves it completely

A classified file is **moved, not copied**. A copy left behind becomes a second source of truth
that no gate compares against the first.

### 12.6 The gate

`python tools/audits/canon_check.py` runs after any `_inbox/` classification that touched `canon/`,
and its verbatim output is pasted before the work is called done (§5).

### 12.7 Retention — nothing stays staged silently

**Anything still in `_inbox/` at session close is listed in that session's `SESSION_LOG.md` block,
with a one-line reason and a named owner.** Not a count, not "the usual" — one line per file or per
clearly-named set, saying why it is still there and who is expected to move it.

**Why this is a rule and not a habit.** `_inbox/` is gitignored (§12.1), so nothing that sits there
is visible in a diff, a commit, or a pull. At the time this section was adopted it held **8 OCR
drafts, 4 textbook PDFs and 2 font files with no review point at all** — some staged in April,
carried through every session since without once being named. **Staging that accumulates silently
is how a stale PDF gets picked up six weeks later as though it were current**, by a session that
has no way of knowing it is not: the file has no date in its name, no header, and no row anywhere
that says when it arrived or what supersedes it.

The retention list is the review point. **A file that appears on it three sessions running is
raised to the Principal** — either it has an owner and a date, or it does not belong in `_inbox/`.
