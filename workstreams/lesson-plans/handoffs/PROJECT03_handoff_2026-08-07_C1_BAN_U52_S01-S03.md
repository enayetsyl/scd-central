# PROJECT03 Handoff — 2026-08-07 — C1 BAN পাঠ 52 · S01–S03 SessionPlan LOCKED

**Chat:** P03 · C1 BAN · U52 · S01–S03 · SessionPlan (BUILD → STAGE 2 LOCK on REVIEW: PASS)
**Work-product:** Lesson plans — the full multi-period Session-Plan family for পাঠ 52 (আমাদের মুক্তিযুদ্ধ), N=3.

---

## 1. Accomplishments

Locked the complete C1 BAN পাঠ 52 Session-Plan family (all 3 periods) against the attached `LOCKED_C1_BAN_U52_ChapterPlan_v2` (session-count re-cut 4→3 already propagated in the Chapter Plan's own supersede; no stale-handoff debt found this pass).

| File | Tag | RC | Conformance |
|---|---|---|---|
| `LOCKED_C1_BAN_U52_S01_SessionPlan_v1.md` + `.json` | NEEDS-REPLACEMENT | `RC-BAN-C1-U52` fragment (i) — "দেশের জন্য যুদ্ধ করতে গিয়ে **অনেকে মারা যান।**" inline | PASS 0 warn (`--chapter`) + byte-identical re-render + surface clean |
| `LOCKED_C1_BAN_U52_S02_SessionPlan_v1.md` + `.json` | NEEDS-REPLACEMENT | `RC-BAN-C1-U52` fragment (ii) — শহিদ gloss corrected to "যাঁরা আল্লাহর পথে (দীনের জন্য) জীবন দেন" inline | PASS 0 warn (`--chapter`) + byte-identical re-render + surface clean |
| `LOCKED_C1_BAN_U52_S03_SessionPlan_v1.md` + `.json` | KEEP-AS-IS | — (no replacement section) | PASS 0 warn (`--chapter`) + byte-identical re-render + surface clean |

- **RC source:** `LOCKED_C1_BAN_ProductionPack_v2` §11 (`RC-BAN-C1-U52`, E-18b). Both fragments + the mandatory teaching note are authoring-complete in the Pack — **no P05 author-block owed** (traceability pointer only, like the U23/U24/U25 bucket).
- **Exit-Check rotation:** S01 = bank id ৩ (‘মুক্তি’ জুড়ে পড়ো) → S02 = id ২ (কোন দিন স্বাধীন) → S03 = id ৮ (খাতায় বাক্য লেখো). No consecutive repeat.
- **Opening ritual:** all three lock **0-warn on the objective-cue form** (4th ritual = রাব্বি যিদনি ইলমা, aim-cue folded into the discipline/materials line) — the U26/U27 pattern, **not** হাজিরা. Adds to the B-LP.1c evidence on the 0-warn side.
- **Curation:** C-18 / F-03 (nationalism-veneration; aqeedah-sensitive শহিদ). Books-closed image rule applied (no leader-portraits / Shaheed-Minar imagery). D-049 materials clean. C-02 same-gender pairing on S03's collaborative Flex activity.
- Built to Core v4 / CP v3.3 / SP v11 / `LOCKED_C1_BAN_ProductionPack_v2` (stamp current: REF-03-BAN v1.2 · TG C1 BAN v1 · AnnSkel C1 BAN v3). Renderer D-034 class-name → প্রথম শ্রেণি.

## 2. Decisions

None new. All three locks are production under **D-046 + D-PROJ03-021**; no new D-number. The 4→3 session-count re-cut is a Chapter-Plan-chat-local revision already carried on `ChapterPlan_v2` (Core v4 §1.10 / REF-02 §2A.3, WITHIN band).

## 3. Open items

- **P04 Homework Pool** `QP-BAN-C1-U52` (topic tag `TOP-BAN-C1-11`) owed before teaching — Project 04 artifact (D-051), not on these plans.
- **B-LP.1c** (4th-ritual standard হাজিরা vs রাব্বি যিদনি ইলমা) still owed at Project 00; this family sits on the 0-warn objective-cue side.
- **⚠ Local re-run:** these locks ran `validate_plan.py` + `--chapter` against the **uploaded genuine** `LOCKED_C1_BAN_U52_ChapterPlan_v2.json` (not reconstructed) and Layer-1 in-sandbox (jsonschema per-session install). SCD should re-run `validate_plan.py <session>.json --chapter LOCKED_C1_BAN_U52_ChapterPlan_v2.json` locally (Windows, `PYTHONIOENCODING=utf-8`) before treating the lock as canonical — the in-sandbox install is per-session; the local run is the authoritative gate.

## 4. Output locations

`/mnt/user-data/outputs/` — six files: the three `LOCKED_C1_BAN_U52_S0{1,2,3}_SessionPlan_v1.md` + their companion `.json`.

## 5. Starter prompt for the next chat

> P03 · C1 BAN · U17–U20 (or next unbuilt পাঠ) · build the Session-Plan families. Consult README + TODO first; check each Chapter Plan for an unpropagated session-count re-cut before building; load Core v4 + SP v11 + `LOCKED_C1_BAN_ProductionPack_v2` + the attached LOCKED Chapter Plan.

---

## 6. Copy-paste-exact governance patches (apply order: DECISIONS → MANIFEST → README → TODO)

> No new decision → **DECISIONS.md** needs only a version-log row (no D-body change).

### PATCH 1 — PROJECT03_DECISIONS.md (v1.27 → v1.28)

**Add** this row at the top of the version-log table (after the header row `| Version | Date | Change | By |` and its `| --- |` separator):

```
| v1.28 | 2026-08-07 | **C1 BAN পাঠ 52 Session-Plan family LOCKED (S01–S03) — production, no new decision.** Off the attached `LOCKED_C1_BAN_U52_ChapterPlan_v2` (4→3 re-cut already carried on CP v2). S01+S02 NEEDS-REPLACEMENT (`RC-BAN-C1-U52` fragments (i)/(ii) inline, no P05 debt); S03 KEEP-AS-IS. All 0-warn objective-cue form; conformance PASS + `--chapter` + byte-identical. Runs under D-046 + D-PROJ03-021 — no new D-number. Header …044 → …044 (unchanged; no D-body edit). Cross-reference: `PROJECT03_README.md` v1.47, `PROJECT03_TODO.md` v1.46, `PROJECT03_MANIFEST_archived_files.md` v1.33, this handoff. | Claude (drafted); Principal (apply on confirm) |
```

**Header bump:** change `**Document status:** v1.27` → `**Document status:** v1.28`.

### PATCH 2 — PROJECT03_MANIFEST_archived_files.md (v1.32 → v1.33)

**Find** (unique anchor — end of the §1 row 37 status/notes cell, the `**⚠ U21 + U28 standalones need re-render + re-lock v1→v2 (D-PROJ03-038 regression).**` string):

```
**⚠ U21 + U28 standalones need re-render + re-lock v1→v2 (D-PROJ03-038 regression).**
```

**Replace with:**

```
**⚠ U21 + U28 standalones need re-render + re-lock v1→v2 (D-PROJ03-038 regression).** **2026-08-07 — পাঠ 52 multi-period Session-Plan family LOCKED:** `LOCKED_C1_BAN_U52_S01/S02/S03_SessionPlan_v1.md` (+ `.json` each), off `LOCKED_C1_BAN_U52_ChapterPlan_v2` (4→3 re-cut carried on CP v2). S01+S02 NEEDS-REPLACEMENT (`RC-BAN-C1-U52` E-18b inline — শহিদ-equation fragments (i)/(ii); no P05 author-block); S03 KEEP-AS-IS. All 0-warn objective-cue form; conformance PASS + `--chapter` + byte-identical.
```

**Header bump:** `**Document status:** v1.32` → `**Document status:** v1.33`; `**Last updated:** 2026-07-22` → `**Last updated:** 2026-08-07`.

### PATCH 3 — PROJECT03_README.md (v1.46 → v1.47)

**Add** this row at the top of the §4-status version-log table (immediately after the `| --- |` separator that follows `| Version | Date | Change | By |`, i.e. above the `| v1.45 |` row):

```
| v1.47 | 2026-08-07 | **C1 BAN পাঠ 52 Session-Plan family LOCKED (S01–S03).** §4 C1 BAN lane row extended: the multi-period family for পাঠ 52 (আমাদের মুক্তিযুদ্ধ) locked off `LOCKED_C1_BAN_U52_ChapterPlan_v2` (4→3 re-cut carried on CP v2). **S01+S02 NEEDS-REPLACEMENT** — `RC-BAN-C1-U52` (C-18/F-03, E-18b) inline: S01 "অনেকে মারা যান" (drops the শহিদ-equation), S02 শহিদ gloss corrected to "যাঁরা আল্লাহর পথে (দীনের জন্য) জীবন দেন"; both fragments authoring-complete in Pack §11 — **no P05 author-block owed.** **S03 KEEP-AS-IS.** Exit-Check rotation ৩→২→৮; **all three lock 0-warn on the objective-cue form** (adds to the B-LP.1c 0-warn side). Conformance PASS + `--chapter` (against the genuine uploaded CP `.json`) + byte-identical. Runs under D-046 + D-PROJ03-021 — no new decision. §4 self-version cells refreshed (DECISIONS v1.27→**v1.28**; TODO v1.45→**v1.46**; MANIFEST v1.32→**v1.33**). Header v1.46 → v1.47. Cross-reference: `LOCKED_C1_BAN_U52_S01/S02/S03_SessionPlan_v1.md`+`.json`, `PROJECT03_DECISIONS.md` v1.28, `PROJECT03_TODO.md` v1.46, `PROJECT03_MANIFEST_archived_files.md` v1.33, this handoff. | Claude (drafted); Principal (apply on confirm) |
```

**Header bump:** `**Document status:** v1.46` → `**Document status:** v1.47`; `**Last updated:** 2026-07-831` → `**Last updated:** 2026-08-07`. *(Note: the existing "2026-07-831" date string looks like a pre-existing typo; correcting to 2026-08-07 on this pass.)*

### PATCH 4 — PROJECT03_TODO.md (v1.45 → v1.46)

**Find** (unique anchor — the end of the **B-LP.1a** headline task line, ending `**Multi-period Session Plans IN PRODUCTION — U22 S01–S02 (2026-06-24) + six families LOCKED 2026-07-02:**`):

```
**Multi-period Session Plans IN PRODUCTION — U22 S01–S02 (2026-06-24) + six families LOCKED 2026-07-02:**
```

**Replace with:**

```
**Multi-period Session Plans IN PRODUCTION — U22 S01–S02 (2026-06-24) + six families LOCKED 2026-07-02 + U52 S01–S03 LOCKED 2026-08-07:**
```

**Then add** this sub-bullet at the end of the B-LP.1a sub-list (after the `- **U32 (4p)** …` bullet):

```
  - **U52 (3p)** — **S01–S03 LOCKED** (`LOCKED_C1_BAN_U52_S01/S02/S03_SessionPlan_v1.md` + `.json`; off `LOCKED_C1_BAN_U52_ChapterPlan_v2`, 4→3 re-cut carried on CP v2). **S01+S02 NEEDS-REPLACEMENT** — `RC-BAN-C1-U52` (C-18/F-03 nationalism-veneration; aqeedah-sensitive শহিদ, E-18b) inline: S01 "অনেকে মারা যান", S02 শহিদ gloss → "যাঁরা আল্লাহর পথে (দীনের জন্য) জীবন দেন"; **no P05 author-block owed** (Pack §11 fragments authoring-complete). **S03 KEEP-AS-IS.** Exit-Check rotation ৩→২→৮; conformance PASS 0 warn `--chapter` + byte-identical; **all three 0-warn objective-cue form** (B-LP.1c 0-warn side). Owes `QP-BAN-C1-U52` / `TOP-BAN-C1-11` in P04.
```

**Header bump:** `**Document status:** v1.45` → `**Document status:** v1.46`.
