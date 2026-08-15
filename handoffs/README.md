# handoffs/ — the session-continuity chain (initiative-wide)

**Created 2026-08-15 by Principal ruling.** Initiative-wide, beside `SESSION_LOG.md` — **not a
workstream lane**, because the chain spans every lane and no single workstream owns it.

## Why this folder exists

Until 2026-08-15 the handoff chain lived **only in Claude project knowledge**, outside the repo.
That is how `HANDOFF_2026-08-15_question-policy-unification.md` came to state repo tip `4bc66d7`
and `CD-132` while the repo stood at `dda7956` and `CD-136` — **two commits and four CD rows
past it** — with no gate, sweep or census able to notice, because the stale file was not in the
repo to be read.

**It is `CD-133`'s shape one level up.** There, a register `QUESTION_POLICY` §10 asserted was
*"filed alongside"* had never been filed. Here, the document that carries repo state across
sessions was itself outside the repo. **`QB-D-013` is the same shape one level down** — a ruling
that lived only inside the artifact it governed. Three instances in one week of *a record kept
somewhere nothing reads it.*

## What is in here, and how it may be used

**The current handoff is the live one. Every other file is a READ-ONLY IMPORT: cited, never
continued** — the `CD-034` / `CD-043(b)` pattern. They are the chain's history, not its state.

**A superseded handoff's facts are stale by construction and must never be carried forward.**
Read them for *why* a decision was taken; read the repo for *what is true now*. This is the
lesson §11 of the live handoff has recorded eleven times.

| File | Date | Role |
|---|---|---|
| `HANDOFF_2026-08-09_unification.md` | 2026-08-09 | chain head — read-only import |
| `HANDOFF_2026-08-10_scd-central-migration.md` | 2026-08-10 | read-only import |
| `HANDOFF_2026-08-10_ocr-pipeline.md` | 2026-08-10 | read-only import |
| `HANDOFF_2026-08-11_math-ch6-onward.md` | 2026-08-11 | read-only import |
| `HANDOFF_2026-08-15_question-policy-unification.md` | 2026-08-15 | read-only import — **superseded entirely** by the file below; states `4bc66d7` / `CD-132`, both wrong |
| **`HANDOFF_2026-08-15_wave3-and-floors.md`** | **2026-08-15** | **LIVE — cite this one** |
| `SCD_UNIFICATION_SURVEY.md` | — | chain-adjacent working document, read-only import |
| `STATUS_2026-08-08_starter-kit.md` | 2026-08-08 | predates the chain head; chain-adjacent, read-only import |

## Recovery completeness — stated, not assumed

**All five chain handoffs were recovered.** Every file named in a `**Chain:**` line resolves to a
file in this folder: `unification` · `scd-central-migration` · `ocr-pipeline` · `math-ch6-onward` ·
`question-policy-unification`. **Nothing is recorded `NOT-IN-REPO`** (CD-133's term), because
nothing is missing.

*Recorded because the first sweep for these files appeared to show `scd-central-migration` absent
and it was not — an unparenthesised `-o` in a `find` predicate had silently dropped it from the
result set. **A search that returns fewer results than exist reads exactly like an absence**, which
is the failure CD-133 exists to guard against in the other direction. The census was re-run against
a plain directory listing before this line was written.*

## Convention

- One file per session-chain link: `HANDOFF_<YYYY-MM-DD>_<slug>.md`.
- Each names the file it supersedes and carries a `**Chain:**` line naming its predecessors.
- **Every fact is derived at source in the session that writes it** — from `git log`, the ledgers,
  the policy files and a fresh gate run. Numbers are never carried from a chat or from the previous
  handoff.
- Superseded files stay on disk unedited. **A handoff is superseded by a new file citing it, never
  by an edit** — the same append-only rule the decision ledgers run on.
