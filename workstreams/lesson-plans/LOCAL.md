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

**Register reconstructed and continuous to D-PROJ03-050** (CD-031…CD-035). The body had ended at 042
while 043/044 were cited as applied but never written, and 045 was claimed by six handoffs.
043, 044 and 045 are now written from their application citations, marked *reconstructed from
applied citations — Principal re-approved*; **only one of the six 045 claims had actually been
applied**, and it holds 045 on its own row rather than being folded into 044. The other five
minted nothing. New work continues at **051**.

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
| `references/` | **read-only reference imports** — cited, never continued from here |

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

## Openings — bismillah is canonical (D-PROJ03-048)

Lesson-plan openings carry **bismillah, then the objective cue**. The two compose; they are not
alternatives. **Forward-only:** new and re-locked plans carry it, existing locked plans stay valid
until the D-038 sweep — whose scope now also **normalises openings**.

## Registers — three of them, and bare `D-0NN` is ambiguous

| Register | File | Series |
|---|---|---|
| **Master** | `references/PROJECT00_README.md` §3 | `D-001…D-053` (52 rows) |
| P00 local | `references/PROJECT00_DECISIONS.md` | `D-PROJ00-###` (72 rows) |
| P03 local | `governance/PROJECT03_DECISIONS.md` | `D-PROJ03-###` (50 rows) |

Both references are **read-only**: cited, never continued from here.

**Sweep result (CD-035):** of 36 distinct bare citations, **35 resolve** — but **33 of those also
have a same-numbered `D-PROJ03` row**, so the bare form is ambiguous at each, including D-038,
D-045, D-046, D-049 and the heaviest users D-022 (103×), D-046 (81×), D-049 (80×). **Always check
both registers; never read the series off the bare string.**

⚠️ **`D-051` DANGLES** — cited **93 times**, present in **neither** register. §3 runs to D-053 but
holds only 52 rows, so D-051 has no body. Cited-but-unwritten master row; **not reconstructed**.

## Known debts

- **D-PROJ03-038 re-render sweep owed.** `LOCKED_C1_BAN_U21_SessionPlan_v1` and
  `LOCKED_C1_BAN_U28_SessionPlan_v1` — the only two standalone Session Plans built before the
  single-period branch was fixed to emit all 7 Spine fields — must be re-rendered from their
  companion JSON, surface-purity checked and re-locked v1 → v2. **Neither artifact is in this
  repo**, so the sweep cannot start here yet.
- ~~U20 Chapter Plan newline~~ — **CLOSED**: superseded to **v4** (D-PROJ03-046), v3 archived,
  v4 clears the full chain. Never normalised in place.
- **C2 MATH U05 v3 re-issue — RULED, EXECUTION OWED (D-PROJ03-047).** The 2026-07-26 in-place
  override is folded into the numbered register and the name "v2" is retired as ambiguous.
  ⚠️ **Neither byte-set is in this repo**, so v3 cannot be cut and the pre-override set cannot be
  archived or declared lost yet. On import of the C2 MATH U05 Chapter Plan: cut v3 from the
  current bytes, archive-or-declare-lost the pre-override set, run v3 through the full chain.
- **B-LP.1c contradiction** — one handoff records it resolved project-wide; every other treats
  it as open. Escalated on the TODO watch-list; the P00 patch is not applied.

## Scope line — what the JSON-source-of-record rule governs (CD-031)

**Plans only.** A Chapter Plan or Session Plan is JSON-first: the JSON is the source of record,
the Markdown is rendered from it, and the byte-identical re-render gate applies.

**Production Packs and handoffs are reference imports, not plan artifacts.** They arrive as
Markdown with no companion JSON and that is correct — they are prose specs and build records,
never rendered from JSON. **Do not over-apply the companion-JSON provenance rule to them**: a
missing `.json` beside a Pack or a handoff is not a gap.

## Operator workflow

Principal rules and locks; the agent builds, validates and renders. A plan is not "locked" until
it passes both the validator and the byte-identical re-render.

## Session-end sync

"save state and sync" = update `_wip/STATE.md` → append root `SESSION_LOG.md` → commit → push.
Gate output quoted as evidence goes to `reports/` (CD-024).
