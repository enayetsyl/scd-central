# LOCAL.md — question-banks (P04)

Read AFTER root `AGENTS.md`. May tighten the protocol, never loosen it.

## Identity

Per-chapter tagged question pools for every class × subject, authored born-conformant to the
Hub's LOCKED import contract v1.0 and delivered to teachers through SCD Hub. Three pools per
chapter — **HW · AS · CT** — with zero overlap between them. Classes C1–C5 (extends per CD-015);
subjects BAN · ENG · MATH · SCI · BGS. **REL is out of scope** until `islamic-studies` opens.

The operative specification is `QUESTION_BANK_POLICY.md` in this folder.

## Status & provenance

**LIVE** (from 2026-08-09) · migration step 4 · source: Project 04 (P04), whose pool convention
arrives via master **D-051**, reconstructed at CD-036. No P04 corpus was imported — this
workstream starts from the policy and the pilot, not from a legacy file set.

## Decision series

**`QB-D-###`** · log: `DECISIONS.md` in this folder · current highest: **QB-D-009**.
The agent assigns the next free number itself, verified at source (AGENTS.md §4).

## Canon citations used

- `canon/sources/SOURCE_POLICY.md` — the only permitted content source for authoring.
- `canon/marklogic/MarkLogic_QuestionPolicy.md` — domain ratios (§৩), class-test rules (§৬),
  answer-length by marks (§৭), repetition rules (§৮), consolidated content restrictions (§৯).
- `canon/marklogic/MarkLogic_BAN_Spine.md` (and the other spines) — per-slot and per-item marks.
- `canon/marklogic/C5_Bangla_Source_13-23.md` — the C5 Bangla extraction (canon by CD-004).
- `canon/names/REF-2_Content_Register.md` — names, by class pool.
- `canon/language/LANGUAGE_RULES.md` — §2 numerals, §4 সাধু/চলিত, §7 script guard.
- `canon/islamic-curation/REF-1_Curation_Policy.md` — C-codes, via QuestionPolicy §৯.

Cite, never copy (AGENTS.md §8).

## Artifacts & naming

| Artifact | Path | Naming |
|---|---|---|
| Bank (source of record) | `_wip/` while building → **`banks/`** on "done" | `C<n>_<SUBJ>_U<unit>_QuestionBank_v<v>.json` |
| Authoring script | **`authoring/`** | `author_U<unit>_wave<n>.py` |
| Built envelopes | **`banks/envelopes/`** (+ `single/` per item) | `<bank stem>.envelopes.json` |
| Gate reports | `reports/` | `<subject>_U<unit>_GATES_<date>.txt` |

The bank JSON is the **source of record**. Envelopes are generated, never hand-edited. Forward-only
naming; a locked bank is supersede-only (AGENTS.md §7).

**The authoring script is promoted with its bank.** A 57-item JSON nobody can re-derive is not
reviewable; the script is what makes the bank reproducible and reviewable as content. It writes
directly to `banks/` once the bank is promoted.

**A wave is a valid promotable increment** (QB-D-002/QB-D-009): 100/50/30 are cumulative ceilings,
so a bank under ceiling is not an unfinished bank, and promotion does not wait for the ceiling.

### Flags carried in a promoted bank

A bank may be promoted carrying a **FLAGGED** queue tag (CD-042) but never an **OPEN** one. The
flag lives in the bank's own top-level `flags` block — tag, status, scope, what is unverified,
what closes it, and what no agent may change meanwhile — so a downstream reader sees the
uncertainty in the artifact rather than only in the ledger. The **FLAG-TRACE** gate enforces that
every flag resolves to a real, non-OPEN row in `PENDING_PRINCIPAL.md`.

### Bank file shape

```
{ "schema_version", "bank_id", "source_extraction", "wave",
  "pool_index": { "HW": [qid…], "AS": [qid…], "CT": [qid…] },
  "questions": [ <LOCKED QuestionPayload_v1 objects> ] }
```

`pool_index` is **authoring-side only** and sits outside the LOCKED payload — the payload schema
is `additionalProperties: false` and its `paper_role` enum means the REF-09 paper-section family,
not the pool (POLICY §3, UP-002). `build_question_envelopes.py` ignores `pool_index`.

## Gates

`audits/gates.py` — run from repo root: `python workstreams/question-banks/audits/gates.py <bank.json>`

1. **SELFTEST** — seeded-error selftest runs FIRST, before any bank verdict is believed
   (the `support-books` pattern, CD-025).
2. **POOL-MEMBERSHIP** — every question in exactly one pool; no unassigned, no orphan qid.
3. **ZERO-OVERLAP** — no near-duplicate stem or answer, across pools **and inside a pool**.
4. **DOMAIN-RATIO** — HW and AS enforced per pool, CT reported, chapter total enforced (QB-D-006).
5. **MARK-VALUE** — every item's marks match a MarkLogic per-item value for its slot.
6. **SOURCE-TRACE** — the item's anchor is a 3+ token span, present in the chapter, **and sharing
   vocabulary with the item** — an anchor not tied to its question proves nothing (QB-D-008).
7. **ANSWER-SHAPE** — exactly one correct MCQ option; no duplicate option ids or texts;
   `why_wrong` on every distractor; non-empty answer keys; rubric bands one-to-one with marks.
8. **RUBRIC-SPECIFICITY** — no two S08 items share a content rubric.
9. **QUOTE-VERBATIM** — every quoted span exists verbatim in the extraction (KEEP-AS-IS).
9a. **FLAG-TRACE** — every ⚑ flag in the bank resolves in `PENDING_PRINCIPAL.md` and is not OPEN.
10. **HONORIFIC** — the Prophet's name always carries (স), across eight name forms.
11. **AS-MIX** — the AS pool is roughly half HW-level, half above (QB-D-004).
12. **SCRIPT-GUARD** — LANGUAGE_RULES §7 tiers over rendered strings.
13. **NUMERALS** — no ASCII digits in student-facing strings (LANGUAGE_RULES §2).
14. **CEILING** — reports balance owed against the per-chapter ceilings; never fails on being
    under ceiling (QB-D-002).

**Human gates by design — and the limit is stated, not hidden.** No gate can judge whether an
answer is **true**, whether the Bengali reads naturally, or whether a সিরাত item's theological
register is right. An audit on 2026-08-09 proved this by passing a bank with a flipped answer key
(QB-D-008). The Principal's read of the bank is what closes those; the scripts close everything
structural.

## Operator workflow

Authoring runs are Principal- or agent-driven, not teacher-driven — the teacher's contact with
this workstream is through the Hub's in-app review, not through Git. Promotion `reviewed → gold`
is the Principal's, in the Hub (CD-003).

## Session-end sync

"save state and sync" = update `_wip/STATE.md` → append a root `SESSION_LOG.md` block → commit →
push. No workstream-specific additions.
