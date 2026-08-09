# lesson-plans/_wip/STATE.md — Step 4 (P03 fold-in)

## Phase

# ✅ STEP 4 IMPORTED · PROOF CHAIN RUN · WORKSTREAM LIVE — 2026-08-09

Three of four artifacts cleared the full chain. One stopped at the re-render gate. Three of the
five VENDORED-UNPROVEN rows flipped; two could not be, for want of a question artifact.

## Schema diff (item 2) — no escalation

`_inbox/LOCKED_C5_PlanSchema_v1.json` vs `tools/hub-export/LOCKED_C5_PlanSchema_v1.json`:
**byte-identical**, sha256 `6a15d89d7d621d7035404e3d32e2be4e88fcbc25edc71d963c3a4b08c8831b9c`.

`audits/` now holds **symlinks** to the vendored schema and `render_plan.py`, not copies —
`validate_plan.py` resolves both from its own directory, and a symlink makes divergence of a
LOCKED contract impossible rather than merely unlikely.

## Proof chain (item 3)

| Artifact | validate_plan | re-render | build_envelope | validate_import |
|---|---|---|---|---|
| C4 MATH U05 S01 SessionPlan v1 | PASS (1 warn) | **byte-identical** | EXIT=0 | **PASS** 0/0 |
| C4 MATH U05 S06 SessionPlan v1 | PASS (1 warn) | **byte-identical** | EXIT=0 | **PASS** 0/0 |
| C5 BAN U17 S01 SessionPlan v1 | PASS (1 warn) | **byte-identical** | EXIT=0 | **PASS** 0/0 |
| C5 BAN U20 ChapterPlan v3 | PASS (0 warn) | **RED — 1 byte** | stopped | stopped |

The `[XP]` warn is "multi-period session validated without its Chapter Plan"; the U20 Chapter
Plan is present but is a different unit, so it is not the matching parent.

Evidence: `reports/PROOF_CHAIN_2026-08-09.txt`, re-renders in `reports/rerender_2026-08-09/`.

### The one red, stated precisely

`LOCKED_C5_BAN_U20_ChapterPlan_v3.md` — locked 20926 B, re-render 20927 B, and
`re-render == locked + b"\n"`. Content is identical; the locked file is the **only one of the
four missing its terminal newline**. So this is **artifact-side, not renderer-side** — the
renderer is self-consistent and three of four round-trip exactly. **Not normalised away**: the
gate is byte-identical, and a gate that quietly tolerates a byte is not that gate.

## VENDORED-UNPROVEN rows — three flipped, two not

**Flipped to REQUIRED:** `render_plan.py` · `build_envelope.py` · `LOCKED_C5_PlanSchema_v1.json`
(exercised as the L2 plan payload schema — all three envelopes are `doc_type=session_plan`).

**NOT flipped — no evidence exists:** `build_question_envelopes.py` and
`LOCKED_QuestionPayload_Schema_v1.json`. **Step 4 supplied no question artifact of any kind.**
They close at Step 4b / question-banks, not here.

## Questions — batched per §6

**[Principal] Q-1 — the decision register cannot safely be continued.** The body ends at
**D-PROJ03-042**. **043 and 044 are cited as applied** in README v1.47, TODO v1.46 and MANIFEST
v1.33 but **were never written into DECISIONS** — the file's own v1.27 changelog says so, and
says "045 is not safely the next free number until both are written". Additionally **six**
handoffs independently claimed 045, four claimed 043, one claimed 044, and a proposed
serialization 045→052 exists but is explicitly not applied. **Write 043 and 044 from their
cited content, then allocate?** *Default:* nothing minted; no number assigned this session.

**[Principal] Q-2 — `D-PROJ03-OVERRIDE-2026-07-26`.** The C2 MATH U05 Chapter Plan was corrected
in place with **no version bump**, so that v2 byte-set is non-unique and is disambiguated only by
a `footer.version_log` row. Does it get a real number and a v3, or stand as an override?
*Default:* left as recorded.

**[Principal] Q-3 — B-LP.1c contradiction.** One handoff records it RESOLVED project-wide
(bismillah canonical, with a `PROJECT00_DECISIONS.md` patch drafted); every other handoff in the
batch treats it as open. The P00 patch is **not** applied. Which is it?
*Default:* treated as open, patch unapplied.

**[Principal] Q-4 — the U20 Chapter Plan's missing newline.** Re-lock a v4 whose `.md` matches
the renderer byte-for-byte, or record the 1-byte delta as an accepted artifact quirk and exempt
it? *Default:* red, artifact stopped, nothing re-locked.

**[Principal] Q-5 — D-038's re-render sweep cannot start here.** It is owed on
`LOCKED_C1_BAN_U21_SessionPlan_v1` and `LOCKED_C1_BAN_U28_SessionPlan_v1`, and **neither artifact
is in this repo**. Supply them and the sweep runs in one pass. *Default:* debt recorded in
LOCAL.md, nothing attempted.

**[Principal] Q-6 — companion-JSON provenance.** The three C3 Production Packs and the three
handoffs arrived as **Markdown with no companion JSON**, so they cannot enter the proof chain at
all. Is that expected (they are prose specs, not renderable plans), or is JSON owed?
*Default:* treated as prose, filed under `plans/packs/` and `handoffs/`.

## Blockers

None. Q-1 blocks *minting* a decision number, not the workstream.

## Next step

Step 4b / question-banks (P04) — it closes the last two hub-export rows. Or the D-038 sweep, if
the two C1 BAN standalones are supplied.
