# LOCAL.md — lesson-plans (Project 03)

Read AFTER root AGENTS.md. May tighten the protocol, never loosen it.

## Identity

Teacher-facing lesson plans for C1–C5: **Chapter Plans** (a whole NCTB unit) and **Session Plans**
(one period, or a multi-period slice of a chapter). The deliverable is Bangla **Markdown**; the
JSON is internal scaffolding (D-PROJ03-004). Also holds the C3 Production Packs and the
per-build handoff record.

## Status & provenance

**LIVE** (2026-08-09). Imported from the P03 project: governance quartet (README v1.47 ·
TODO v1.46 · DECISIONS v1.27 · MANIFEST v1.33), four plan artifacts, three C3 Production Packs,
three handoffs, `validate_plan.py`.

## Decision series

**D-PROJ03-###**, log at `governance/PROJECT03_DECISIONS.md`.

⚠️ **The next free number is NOT obvious — verify before minting.** The register body ends at
**D-PROJ03-042**. **043 and 044 are cited as applied** in README/TODO/MANIFEST but **were never
written into the register**, and 045 is contended by six independent handoff claims. The file
says so itself (v1.27 changelog). See `_wip/STATE.md` Q-1/Q-2 — **do not mint a number until the
Principal allocates.**

## Canon citations used

- `canon/islamic-curation/REF-1_Curation_Policy.md` — C-codes.
- `canon/names/REF-2_Content_Register.md` — cast and name pools.
- `canon/language/LANGUAGE_RULES.md` — §1–§2 register/numerals, §7 script guard.
- `canon/image-rules/IMAGE_RULES.md` — living-being doctrine.

Cite, never copy (AGENTS.md §8). The `governance/` quartet is P03's operating spec for
everything canon does not cover; **where it restates canon, canon wins** — each file carries a
canon-precedence banner (CD-027 pattern, applied CD-030).

## Artifacts & naming

`LOCKED_<CLASS>_<SUBJECT>_U<unit>[_S<session>]_<ChapterPlan|SessionPlan>_v<N>.{json,md}`

| Path | Holds |
|---|---|
| `plans/chapter/` · `plans/session/` | locked plans, JSON + rendered Markdown side by side |
| `plans/packs/` | C3 Production Packs |
| `governance/` | the quartet — §D of TODO is the authoritative lock register |
| `audits/` | `validate_plan.py`; **symlinks** to the vendored schema and `render_plan.py` |
| `handoffs/` · `reports/` · `_wip/` | build record · gate evidence · scratch |

## Gates

1. `python3 audits/validate_plan.py <plan.json> [--chapter <chapter.json>]` — L1 jsonschema +
   L2 semantic. Pass `--chapter` for a multi-period session or you get an `[XP]` warn and the
   Spine-match check is skipped.
2. **The byte-identical re-render rule — P03's own gate.** Re-render the locked JSON with
   `render_plan.py` and compare **byte-for-byte** with the locked `.md`. Any difference is red.
   This is what stops format/structure drift: the template produces section order, frozen
   headings and numerals, not the chat.
3. Hub path: `build_envelope.py` → `validate_import.py` (L1–L4), the only integration route (CD-003).

**Why symlinks in `audits/`:** `validate_plan.py` resolves its schema from its own directory and
imports `render_plan`. Symlinks mean there is exactly one copy of the LOCKED schema in the repo,
so the two can never silently diverge — the divergence that would otherwise be an escalation.

## Known debts

- **D-PROJ03-038 re-render sweep owed.** `LOCKED_C1_BAN_U21_SessionPlan_v1` and
  `LOCKED_C1_BAN_U28_SessionPlan_v1` — the only two standalone Session Plans built before the
  single-period branch was fixed to emit all 7 Spine fields — must be re-rendered from their
  companion JSON, surface-purity checked and re-locked v1 → v2. **Neither artifact is in this
  repo**, so the sweep cannot start here yet.
- **`LOCKED_C5_BAN_U20_ChapterPlan_v3.md` fails the re-render gate by one byte** (missing
  terminal newline). Content is identical. See `_wip/STATE.md`.
- **`D-PROJ03-OVERRIDE-2026-07-26`** — C2 MATH U05 Chapter Plan corrected in place with no
  version bump, so that v2 byte-set is non-unique, disambiguated only by a `footer.version_log`
  row.
- **B-LP.1c contradiction** — one handoff records it resolved project-wide; every other treats
  it as open. Escalated on the TODO watch-list; the P00 patch is not applied.

## Operator workflow

Principal rules and locks; the agent builds, validates and renders. A plan is not "locked" until
it passes both the validator and the byte-identical re-render.

## Session-end sync

"save state and sync" = update `_wip/STATE.md` → append root `SESSION_LOG.md` → commit → push.
Gate output quoted as evidence goes to `reports/` (CD-024).
