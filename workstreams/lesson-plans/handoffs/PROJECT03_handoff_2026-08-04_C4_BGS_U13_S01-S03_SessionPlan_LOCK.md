# PROJECT03 handoff — 2026-08-04 — C4 BGS অধ্যায় ১৩ · S01–S03 Session Plans LOCKED (STAGE 2)

**Chat:** `P03 · C4 BGS · U13 · S01–S03 · SessionPlan` (BUILD → STAGE 2 lock)
**Mode:** BUILD. Locked on the STAGE 2 trigger — `SessionPlanReview_v2` returned **REVIEW: FAIL** with **zero content FAILs**, both FLAGs CLOSED, and only two validator-owned defects outstanding; both are fixed in this pass.

---

## 1. What was accomplished

Three multi-period Session Plans for **C4 BGS অধ্যায় ১৩ (অর্থ ও সম্পদ)** — the full 3-period chapter — authored (Layers 2–3), taken through the full conformance set, and LOCKED.

| Period | File pair (LOCKED) | Curation | Notes |
|---|---|---|---|
| ১/৩ | `LOCKED_C4_BGS_U13_S01_SessionPlan_v1.md` + `.json` | KEEP-AS-IS | Merged-foundation period (বোঝা); composite Exit-Check যাচাই ৩. |
| ২/৩ | `LOCKED_C4_BGS_U13_S02_SessionPlan_v1.md` + `.json` | KEEP-AS-IS + inline **F-04** reframe | Buy-sell as oneself, same-gender; no RC/P05. Transaction props ruled allowed (Review v2 FLAG-2). |
| ৩/৩ | `LOCKED_C4_BGS_U13_S03_SessionPlan_v1.md` + `.json` | KEEP-AS-IS + **F-07/TN-5** halal-finance note | Saving halal, সুদ impermissible; riba refused even illustratively (Pack correction 5). |

### Review defects fixed this pass (both validator-owned)
1. **SURFACE (all three).** `TOP-BGS-C4-13` and the Chapter-Plan filename are no longer on the teacher surface. In the rebuilt JSON the surface homework field carries **topic + count as plain teacher text only**; the `TOP-…` tag and the `LOCKED_…ChapterPlan_v3` reference now live in the internal footer only. Rendered-surface scan: **no forbidden code on any of the three surfaces.**
2. **S03 period sum.** Rebalanced to **35** (3+4+7+7+7+4+3). S01 (3+4+7+7+8+4+2=35) and S02 (3+4+6+8+9+4+1=35) unchanged.

### Conformance (in-sandbox, real jsonschema)
`pip install jsonschema --break-system-packages` → then for each session:
`validate_plan.py <session>.json --chapter C4_BGS_U13_ChapterPlan_v3.json` → **RESULT: PASS (0 warn)** ×3
`render_plan.py` → `.md`; **byte-identical re-render confirmed** ×3.
Cross-plan Spine match (objective · must-cover · Exit-Check full text vs §2.9 rows) **clean** — Spine copied verbatim, not re-derived.

> **⚠ Local re-run owed (authoritative gate).** The in-sandbox jsonschema install is per-session. SCD must re-run `validate_plan.py` locally (Windows, `PYTHONIOENCODING=utf-8`) with `--chapter` before treating these locks as canonical.
>
> **⚠ CP provenance risk carried (upstream, not a session defect).** The `--chapter` cross-check here ran against a **chapter JSON reconstructed from `LOCKED_C4_BGS_U13_ChapterPlan_v3.md`** (no genuine CP `.json` was ever attached; the CP footer itself flags the v3 JSON was reconstructed from the v2 Markdown). Diff the CP JSON against the genuine v2 source + run offline jsonschema Layer-1 **in the U13 ChapterPlan chat** before the CP lock is treated as canonical. This does not affect the session locks (their surface + Spine-verbatim + sum + rituals all pass), but the cross-plan equality inherits the CP-reconstruction risk.

---

## 2. Output locations

All in `/mnt/user-data/outputs/`:
- `LOCKED_C4_BGS_U13_S01_SessionPlan_v1.md` + `LOCKED_C4_BGS_U13_S01_SessionPlan_v1.json`
- `LOCKED_C4_BGS_U13_S02_SessionPlan_v1.md` + `LOCKED_C4_BGS_U13_S02_SessionPlan_v1.json`
- `LOCKED_C4_BGS_U13_S03_SessionPlan_v1.md` + `LOCKED_C4_BGS_U13_S03_SessionPlan_v1.json`
- This handoff.

*(The three `DRAFT_…_S0n_SessionPlan_v1.md` from the STAGE 1 chat are superseded by these LOCKED renders — the deliverable is rendered-from-JSON. Remove the DRAFT-named copies on lock per the LOCKED_-prefix pairing rule.)*

---

## 3. Open items (carried, not blocking these locks)

1. **CP provenance-diff** for `LOCKED_C4_BGS_U13_ChapterPlan_v3` — owed in the U13 ChapterPlan chat (diff v3 JSON vs genuine v2 source + offline Layer-1). Also the v2→/archive/ file move + MANIFEST archive row belong to that chat.
2. **Governance-record lag** — the CP v2→v3 (4p→3p within-band) supersede was never propagated. Patches in §4 below (README §4, TODO §C.22, MANIFEST row 46). No Pack edit owed (§5 row shows the TG baseline, a source fact).
3. **Drift watch (Review v2 §5).** The `TOP-` on-surface leak appeared three-for-three in the STAGE 1 drafts — a §3.0 pattern leak, not a per-plan slip. Fixed here because the JSON renderer keeps the tag in the footer by construction; **verify other C4 BGS session batches** don't repeat the on-surface `প্রশ্ন নির্বাচন` pattern before more C4 BGS sessions are built.
4. **`TOP-BGS-C4-13` Pool** — ≥20 items owed in Project 04 before teaching (D-051; non-blocking).

---

## 4. Precise governance patches (§14) — apply after these locks are accepted

**Apply order:** DECISIONS → MANIFEST → README → TODO.
**DECISIONS:** *no change.* This is a Project-03-local supersede + lock that rides existing decisions (v2→v3 within-band under REF-02 §2A.3 + D-046; lock under D-PROJ03-021/-034) — no new D- number is minted, so `PROJECT03_DECISIONS.md` gets no content row and no version-log bump.

### Patch A — `PROJECT03_MANIFEST_archived_files.md` (§1 row 46) · current v1.32

**FIND (verbatim substring within row 46):**
```
remaining **Session Plans IN PRODUCTION — `LOCKED_C4_BGS_U09_S01..S04_SessionPlan_v1.md` (+ `.json`) LOCKED 2026-06-28; rest pending**
```
**REPLACE:**
```
remaining **Session Plans IN PRODUCTION — `LOCKED_C4_BGS_U09_S01..S04_SessionPlan_v1.md` (+ `.json`) LOCKED 2026-06-28; `LOCKED_C4_BGS_U13_S01..S03_SessionPlan_v1.md` (+ `.json`) LOCKED 2026-08-04 (full 3-period chapter off CP **v3**; all KEEP-AS-IS — S02 inline F-04 buy-sell-as-oneself, S03 F-07/TN-5 halal-finance; conformance PASS 0 warn `--chapter`, byte-identical re-render, surface-purity clean); rest pending** ⚠ U13 CP v3 `.json` reconstructed from the v2 Markdown — diff vs genuine v2 source + offline Layer-1 before canonical
```
**Also update the U13 clause in the same row's status prose —**
**FIND:** `U13 KEEP-AS-IS/emphasise (v2, A8 D-035; D-022 waiver after separate REVIEW);`
**REPLACE:** `U13 KEEP-AS-IS/emphasise (**v3 — CP v2→v3 4p→3p within-band supersede, REF-02 §2A.3**; A8 D-035 carried; D-022 waiver; **S01–S03 SP LOCKED 2026-08-04, REVIEW PASS `…SessionPlanReview_v2`**);`
**Version-log — add new top row:**
```
| v1.33 | 2026-08-04 | **§1 row 46 (C4 BGS family) — U13 S01–S03 Session Plans LOCKED (full 3-period chapter) + U13 clause CP v2→v3 4p→3p within-band.** All KEEP-AS-IS (S02 inline F-04, S03 F-07/TN-5). CP v3 `.json` reconstruction risk flagged. No new decision (rides D-046 + D-PROJ03-021). Header bump. Cross-ref: README §4, TODO §C.22, `LOCKED_C4_BGS_U13_ChapterPlan_v3`, `C4_BGS_U13_S01-S03_SessionPlanReview_v2`. | Claude (drafted); Principal (apply on confirm) |
```
Header: bump `PROJECT03_MANIFEST_archived_files.md` **v1.32 → v1.33**, date 2026-08-04.

### Patch B — `PROJECT03_README.md` (§4, "First Class 4 BGS deliverables" row) · current v1.46

**FIND (verbatim substring within the row):**
```
U13 অর্থ (4p; v2 A8 D-035; D-022 waiver),
```
**REPLACE:**
```
U13 অর্থ (**3p — CP v2→v3 4p→3p within-band supersede, REF-02 §2A.3**; A8 D-035 carried; D-022 waiver; **S01–S03 SP LOCKED 2026-08-04, REVIEW PASS**; ⚠ CP v3 `.json` provenance-diff owed),
```
**Version-log — add new top row:**
```
| v1.47 | 2026-08-04 | **§4 First Class 4 BGS deliverables — U13 CP v2→v3 (4p→3p within-band) + S01–S03 Session Plans LOCKED (all KEEP-AS-IS; S02 inline F-04, S03 F-07 halal-finance).** No master-decision change. Header bump. Cross-ref: `PROJECT03_TODO.md` §C.22, MANIFEST §1 row 46, `LOCKED_C4_BGS_U13_ChapterPlan_v3`, `C4_BGS_U13_S01-S03_SessionPlanReview_v2`. | Claude (drafted); Principal (apply on confirm) |
```
Header: bump `PROJECT03_README.md` **v1.46 → v1.47**, date 2026-08-04. *(Note: the current README header shows "Last updated: 2026-07-831" — a typo; set the date cleanly to 2026-08-04 on this bump.)*

### Patch C — `PROJECT03_TODO.md` (§C.22 line) · current v1.45

**FIND (verbatim substring within the §C.22 stub, line 106):**
```
C.22 Class 4 BGS (in production — U09/U10/U12/U13/U14 CPs + U11 SP LOCKED 2026-06-23).
```
**REPLACE:**
```
C.22 Class 4 BGS (in production — U09/U10/U12/U13/U14 CPs + U11 SP LOCKED 2026-06-23; **U09 S01–S04 SP LOCKED 2026-06-28; U13 CP v2→v3 4p→3p within-band + U13 S01–S03 SP LOCKED 2026-08-04, REVIEW PASS — all KEEP-AS-IS, S02 inline F-04, S03 F-07/TN-5; ⚠ U13 CP v3 `.json` provenance-diff owed**).
```
**Version-log — add new top row:**
```
| v1.46 | 2026-08-04 | **§C.22 — C4 BGS U13 CP v2→v3 (4p→3p within-band, REF-02 §2A.3) propagated + U13 S01–S03 Session Plans LOCKED** (full 3-period chapter; all KEEP-AS-IS; S02 inline F-04 buy-sell-as-oneself, S03 F-07/TN-5 halal-finance; conformance PASS 0 warn `--chapter` + byte-identical re-render). CP v3 `.json` reconstruction-risk flagged (diff + offline Layer-1 owed in the U13 CP chat). No new decision (rides D-046 + D-PROJ03-021). Header bump. Cross-ref: `LOCKED_C4_BGS_U13_ChapterPlan_v3`, `LOCKED_C4_BGS_U13_S01..S03_SessionPlan_v1`, `C4_BGS_U13_S01-S03_SessionPlanReview_v2`, README §4, MANIFEST §1 row 46. | Claude (drafted); Principal (apply on confirm) |
```
Header: bump `PROJECT03_TODO.md` **v1.45 → v1.46**, date 2026-08-04.

*(No Pack patch — `LOCKED_C4_BGS_ProductionPack_v1` §5 shows the TG baseline পাঠ ৬০–৬৩/4, a source fact that stays correct; the 4→3 is a CP-level revision, not a Pack revision. Any Pack annotation would be a v1→v2 supersede, out of scope here.)*

---

## 5. Starter prompt for the next chat

> `P03 · C4 BGS · U13 · ChapterPlan` (provenance chat) — **or** the next in-scope C4 BGS division.
>
> "Diff `LOCKED_C4_BGS_U13_ChapterPlan_v3.json` against the genuine v2 source and run offline jsonschema Layer-1 locally to confirm the CP lock is canonical; move v2 → `/archive/` and add the MANIFEST archive row. Then continue C4 BGS in-scope Session-Plan builds (U01 · U07বি১ · U10 · U11বি১ · U12 · U14 — all KEEP/KEEP-emphasise, batch ≤6 per chat). Apply the §4 governance patches from `PROJECT03_handoff_2026-08-04_C4_BGS_U13_S01-S03_SessionPlan_LOCK.md` if not yet applied."
