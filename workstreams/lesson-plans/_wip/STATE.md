# lesson-plans/_wip/STATE.md — Step 4 (P03 fold-in)

# ✅ STEP 4 CLOSED — 2026-08-09

**Proven artifacts (4/4).** All four plan artifacts clear the full chain:
`validate_plan` → byte-identical re-render → `build_envelope` → `validate_import`.

| Artifact | Status |
|---|---|
| C4 MATH U05 S01 SessionPlan v1 | proven |
| C4 MATH U05 S06 SessionPlan v1 | proven |
| C5 BAN U17 S01 SessionPlan v1 | proven |
| C5 BAN U20 ChapterPlan **v4** | proven (v3 archived — 1-byte newline supersede, D-046) |

**Register: reconstructed and continuous to D-PROJ03-049.** 043/044/045 reconstructed from
applied citations; 046 = U20 supersede; 047 = C2 MATH override (parked); 048 = B-LP.1c resolved;
049 = P00 reference import. **New work continues at 050.**

**Parked / carried:**

| Item | State |
|---|---|
| D-047 C2 MATH U05 | **PARKED** — surviving copy is pre-override, archived; post-override bytes **lost**; no v3 |
| D-038 re-render sweep | **owed** — neither C1 BAN standalone is in this repo; scope now also normalises openings (D-048) |
| B-LP.1c P00 patch | **pending-P00-fold-in** — approved in substance, applied at P00's migration |
| Master D-series | **unresolvable here** — D-001…D-053 live in `PROJECT00_README.md` §3, not supplied |
| Question-bank rows | 2 VENDORED-UNPROVEN rows await a question artifact |

## What Step 5 needs from the Principal

1. **`PROJECT00_README.md`** — the only file that resolves D-038/D-045/D-046/D-049/D-051 and
   every other master citation the quartet leans on.
2. **The two C1 BAN standalones** (`U21`, `U28`) — to run the D-038 sweep, now widened to openings.
3. **A question-bank artifact** — closes the last two VENDORED-UNPROVEN rows.
4. Step 5 proper: **english-programme** (recovered instructions), **islamic-studies** (greenfield),
   **accounting** (recovery package, open: Check-5 423,533; +28,592 residual).

---

## Detail — Step 4 record

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

## Rulings applied 2026-08-09 (CD-031)

| Item | Outcome |
|---|---|
| Register | **Reconstructed to D-046.** 043/044/045 written from applied citations; 045 held by the one applied claim of six, surfaced not folded. New work continues at **047** |
| U20 newline | **Superseded to v4**, v3 archived, v4 clears the full chain (D-PROJ03-046) |
| D-038 sweep | Deferred — stays a LOCAL.md debt row; neither standalone is in this repo |
| Packs/handoffs | **Reference imports.** JSON-source-of-record governs **Plans only**; scope line written into LOCAL.md |
| OVERRIDE | **Ruled → D-PROJ03-047 / CD-032. Execution OWED — neither byte-set is in this repo** |
| B-LP.1c | Brief given; awaiting ruling |

### ✅ D-PROJ03-047 EXECUTED 2026-08-09 — parked, post-override bytes lost

The surviving copy arrived and was **classified, not assumed**: `footer.version_log` **absent**,
dated 2026-06-21, zero occurrences of the override date → **pre-override bytes**. Archived to
`plans/chapter/archive/`.

**Reconstruction test failed.** Every mention of the override across the quartet and the three
handoffs states only *that* it happened in place with no version bump, and *how* the byte-sets are
distinguished — **none states what content changed.** No delta to apply, so the **post-override
bytes are recorded as LOST**. No v3 cut; nothing entered the proof chain.

Archive integrity verified: `validate_plan` PASS (0 warn); re-render differs on **exactly one line
of 168** — the renderer's own provenance stamp — a renderer-generation difference, not content
drift. Evidence: `reports/D047_CLASSIFICATION_2026-08-09.txt`.

⚑ **New batched question Q-7 (D-049 / master D-series)** — see below.

### Superseded — the earlier blocked note

The ruling is binding and recorded: re-issue the post-override bytes as **v3**, retire the name
**v2** as ambiguous, archive the pre-override bytes **if they survive** or record them **lost**
if they do not, and fold `D-PROJ03-OVERRIDE-2026-07-26` into the numbered sequence (done).

**But the C2 MATH U05 Chapter Plan is not in this repo — neither byte-set.** Step 4 imported no
C2 MATH artifact at all. So v3 could not be cut, the pre-override set could not be archived or
declared lost, and no chain run was possible. **Nothing was fabricated**, and no archive was
claimed that does not exist — which is the part of the ruling that would have been easiest to
quietly get wrong.

**On import:** cut v3 from the current bytes → archive-or-declare-lost the pre-override set →
run v3 through the full chain → add it to the proven set.

All four plan artifacts are now proven end-to-end.

## Questions — batched per §6

~~**Q-1 — register**~~ · ~~**Q-4 — U20 newline**~~ · ~~**Q-5 — D-038 sweep**~~ ·
~~**Q-6 — companion JSON**~~ → all ruled 2026-08-09, **CD-031**. Original text kept below.

**[Principal] Q-7 — D-049 is cited everywhere but its register is not in this repo.**
The C2 MATH U05 footer cites **D-049** (ব্ল্যাকবোর্ড p110 → whiteboard), and the quartet cites it
repeatedly — "never slate/chalk → positive D-049 §1.7", a "D-049 prep-item fix" at C1 BAN U25, a
"D-049-vs-geometry-instrument ruling owed". **It is NOT a D-PROJ03 row** (0 matches in the local
register) and correctly so: the quartet's own range statements — *"range unchanged (D-001–D-050)"*,
*"(D-001–D-051)"* — place D-049 in the **master D-series**. **But the master register is not in
`scd-central` at all**, so no citation to D-001…D-051 can be resolved here, and D-049's body cannot
be verified. This is not a P03 reconstruction candidate; it is a **missing-register provenance
gap** one level up. Import the master D-series, or rule that P03 may cite it unresolvable?
*Default:* cited as-is, unverifiable, flagged here.

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
