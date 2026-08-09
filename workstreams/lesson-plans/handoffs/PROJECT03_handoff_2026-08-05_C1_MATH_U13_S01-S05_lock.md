# PROJECT03 handoff — 2026-08-05 — C1 MATH U13 S01–S05 SessionPlan LOCK

**Chat:** P03 · C1 MATH · U13 · S01–S05 · SessionPlan
**Mode:** BUILD → STAGE 2 LOCK (REVIEW: PASS supplied, B1-hw)
**Work-product:** multi-period Session Plans, C1 MATH অধ্যায় 13 (প্যাটার্ন), periods 1–5, all KEEP-AS-IS.

---

## ⚠ READ FIRST — VERSION-COLLISION BLOCKER (needs a Principal ruling before propagation)

The uploaded `LOCKED_C1_MATH_U13_ChapterPlan_v2` (`.md` + `.json`) that these five Session Plans were built and cross-plan-validated against is a **5-period re-cut (8p→5p)** with an **8-form Exit-Check bank** (types: চালিয়ে-যাওয়া / যুক্তি / ভুল-খোঁজা / নিজে-বানানো; Session-Map pointers 1·2·4·5·7).

**Governance already records a *different* U13 v2:** README §4 row / MANIFEST §1 row 38 / MANIFEST §3 archive row / DECISIONS **D-PROJ03-044** all describe U13 v2 as an **8-period** chapter with a **bank 8→9** fix (form ৮ re-authored, form ৯ added) and **S07–S08 LOCKED** — i.e. "U13 fully locked, 8 periods, 🟦 PROTECTED MATH-PATTERN."

So there are **two artifacts sharing the filename `LOCKED_C1_MATH_U13_ChapterPlan_v2`**: the recorded 8-period one, and the uploaded 5-period one. They are not reconcilable by a patch. **I did not overwrite the existing U13 governance record.** The five Session Plans are internally correct and pass the full conformance set against the *uploaded* 5-period Chapter Plan, but their governance status is **HELD** until you rule:

- **(a)** The 5-period re-cut is the intended current U13 (supersede the recorded 8-period v2 → it becomes v3, or the 8-period one goes to `/archive/`, and the previously-locked S07–S08 are **retired** — they don't exist in a 5-period chapter). Then apply the propagation patches in §B below.
- **(b)** The recorded 8-period U13 v2 stands; the uploaded 5-period file is a stray/superseded draft. Then these five S01–S05 locks are **void** (they were built against the wrong Chapter Plan) — do not propagate; discard.
- **(c)** Something else (e.g. the 8-period was itself an error). Tell me and I'll reconcile.

Everything below assumes **(a)**. If (b)/(c), stop and ignore §B.

---

## Accomplishments (conditional on ruling (a))

- B1-hw REVIEW FAIL fixed at STAGE 1 (the `TOP-MATH-C1-08` tag stripped from the teacher-facing `আজকের বাড়ির কাজ` line; plain §2.9 slice restored; footer binding kept).
- STAGE 2 lock, all five: authored conformance JSON → `validate_plan.py <session>.json --chapter LOCKED_C1_MATH_U13_ChapterPlan_v2.json` → **RESULT: PASS (0 warn)** each → `render_plan.py` → **byte-identical re-render** confirmed each.
- jsonschema installed in-sandbox from PyPI (real Layer-1, not the offline shim).
- Surface purity: **0** `TOP-`/RC-/§/D-/C-/F- codes above the internal footer on all five rendered surfaces; homework lines are the plain §2.9 slices; `TOP-MATH-C1-08` lives in the footer only.
- Cross-plan Spine-match (`--chapter`) PASS: each §3.0 header objective / must-cover / Exit-Check text is byte-verbatim from the Session-Map row it points to. Pointers 1·2·4·5·7, no consecutive repeat.

## Output locations (delivered this chat)

`LOCKED_C1_MATH_U13_S01_SessionPlan_v1.md` + `.json`
`LOCKED_C1_MATH_U13_S02_SessionPlan_v1.md` + `.json`
`LOCKED_C1_MATH_U13_S03_SessionPlan_v1.md` + `.json`
`LOCKED_C1_MATH_U13_S04_SessionPlan_v1.md` + `.json`
`LOCKED_C1_MATH_U13_S05_SessionPlan_v1.md` + `.json`

Note: `render_plan.py` produces the canonical surface, so the delivered `.md` differs slightly from the STAGE-1 DRAFT (renderer-emitted frozen strings — e.g. segment heading `সরাসরি পাঠদান / Direct Instruction`, the `**ইসলামি দিক থেকে এক কথা।**` one-liner in the §3.0 header, flow-card `মি`, segment mandatory label `আবশ্যিক`/`নমনীয়`). The DRAFT was a close hand-authored approximation; the rendered `.md` is the lock artifact.

**Local re-run owed (authoritative gate):** the in-sandbox jsonschema install is per-session. Re-run each locally (Windows, `PYTHONIOENCODING=utf-8`): `validate_plan.py <session>.json --chapter <chapter>.json` → `render_plan.py` → byte-identical, before treating the lock as canonical.

---

## §B — Propagation patches (APPLY ONLY under ruling (a))

Apply in order: DECISIONS → MANIFEST → README → TODO. Each is copy-paste-exact.
*If (a) also requires retiring the recorded 8-period U13 v2 + its S07–S08 locks, that is a separate supersede I'll draft on your word — it is NOT in the patches below, which only add the S01–S05 lock and flag the collision.*

### B.1 — PROJECT03_DECISIONS.md (v1.27 → v1.28)

**Add a new decision** (append in the D-PROJ03 body, after the D-044 entry):

```
D-PROJ03-045 | 2026-08-05 | C1 MATH U13 — 5-period Chapter Plan v2 confirmed + S01–S05 Session Plans LOCKED. The uploaded LOCKED_C1_MATH_U13_ChapterPlan_v2 is a 5-period re-cut (8p→5p, WITHIN band ±40%/±1=[5,11]; merge of the two shape sessions + the two number sessions + review folded into the create session; no taught objective/must-cover dropped; 8-form bank, pointers 1·2·4·5·7). This SUPERSEDES the 8-period artifact previously recorded under the same filename at D-044 (whose S07–S08 locks are retired — a 5-period chapter has no S07/S08). S01–S05 LOCKED through the conformance set (JSON → validate_plan.py PASS 0 warn --chapter → render_plan.py → byte-identical); all KEEP-AS-IS; 🟦 PROTECTED MATH-PATTERN; B1-hw REVIEW FAIL (TOP- tag on the homework surface line) fixed pre-lock. Tag-L supersede. Project-03-local; no master change.
```

**Version-log row** (append to the DECISIONS version log table):

```
| v1.28 | 2026-08-05 | D-PROJ03-045 appended — C1 MATH U13 5-period ChapterPlan v2 confirmed (supersedes the 8-period v2 recorded at D-044; S07–S08 retired) + S01–S05 Session Plans LOCKED. Header v1.27 → v1.28. Cross-reference: PROJECT03_README.md, PROJECT03_MANIFEST_archived_files.md, PROJECT03_handoff_2026-08-05_C1_MATH_U13_S01-S05_lock.md. | Claude (drafted); Principal (apply on confirm) |
```

**Header:** bump `v1.27` → `v1.28`, date `2026-08-05`.

### B.2 — PROJECT03_MANIFEST_archived_files.md

**FIND** (row 38, the U13 clause inside the C1 MATH roll-up — this exact substring):

```
**U13 ChapterPlan v1→v2 (D-PROJ03-044** — Exit-Check bank fix: form ৮ re-authored self-create → continue-partner's-pattern + verify, companion form ৯ added, bank 8→9; v1→`/archive/`**)** + `…_U13_S01..S08_…` LOCKED (S01–S06 + S07–S08; U13 fully locked, 8 periods, 🟦 PROTECTED MATH-PATTERN);
```

**REPLACE WITH:**

```
**U13 ChapterPlan re-cut to 5 periods (D-PROJ03-045, 2026-08-05 — supersedes the 8-period v2 recorded at D-044; 8p→5p WITHIN band, merge shape+number sessions, review folded into create; 8-form bank, pointers ১·২·৪·৫·৭)** + `…_U13_S01..S05_…` LOCKED (all five periods; KEEP-AS-IS; 🟦 PROTECTED MATH-PATTERN; **⚠ the 8-period v2's S07–S08 locks are RETIRED — a 5-period chapter has no S07/S08**);
```

**Add an archive row** (MANIFEST §3, append):

```
| `LOCKED_C1_MATH_U13_ChapterPlan_v2.md` (8-period, + `.json`) | 2026-08-05 | `LOCKED_C1_MATH_U13_ChapterPlan_v2.md` (5-period re-cut) (D-PROJ03-045) | Filename collision resolved under ruling (a): the 8-period v2 recorded at D-044 is superseded by the 5-period re-cut. Its S07–S08 Session-Plan locks are retired (no S07/S08 in a 5-period chapter). Tag-L supersede, §5.3. |
```

**Version-log row** (MANIFEST version log, append):

```
| <next> | 2026-08-05 | C1 MATH U13 row 38 updated — 5-period ChapterPlan v2 (D-PROJ03-045) supersedes the recorded 8-period v2; S01–S05 SessionPlans LOCKED, S07–S08 retired. §3 gains one archive row. | Claude (drafted); Principal (apply on confirm) |
```

### B.3 — PROJECT03_README.md (v1.46 → v1.47)

**FIND** (in the DECISIONS status cell, line 81, the D-044 sentence):

```
**D-044 (2026-07-02) = C1 MATH U13 ChapterPlan v1→v2 Exit-Check bank fix (form ৮ re-authored continue-partner's-pattern + verify, form ৯ added; bank 8→9) + S07–S08 LOCKED.**
```

**REPLACE WITH:**

```
**D-045 (2026-08-05) = C1 MATH U13 ChapterPlan re-cut to 5 periods (8p→5p, WITHIN band; supersedes the 8-period v2 recorded at D-044) + S01–S05 SessionPlans LOCKED; the 8-period v2's S07–S08 locks retired.** **D-044 (2026-07-02) = C1 MATH U13 ChapterPlan v1→v2 Exit-Check bank fix (form ৮ re-authored continue-partner's-pattern + verify, form ৯ added; bank 8→9) + S07–S08 LOCKED — SUPERSEDED by D-045 (5-period re-cut).**
```

**Header:** bump `v1.46` → `v1.47`, and update the DECISIONS-file pointer in that cell from `v1.27` to `v1.28`.

### B.4 — PROJECT03_TODO.md (v1.45 → v1.46)

**FIND** (§C.20, immediately after the U10 bullet at line 265 — insert a new U13 bullet; anchor is the end of the U10 line):

```
Links `TOP-MATH-C1-03` (place value Pool owed P04).
```

**INSERT IMMEDIATELY AFTER that line:**

```
  - **U13 (5p, 🟦 PROTECTED MATH-PATTERN, KEEP-AS-IS): `LOCKED_C1_MATH_U13_ChapterPlan_v2` re-cut 8p→5p (D-PROJ03-045; supersedes the 8-period v2 at D-044). Session Plans S01–S05 LOCKED 2026-08-05** (`LOCKED_C1_MATH_U13_S01..S05_SessionPlan_v1.md` + `.json`; conformance set PASS 0 warn + `--chapter` + byte-identical re-render; B1-hw fixed pre-lock; pointers ১·২·৪·৫·৭; objective-cue Opening 0 OPEN-RITUAL). **⚠ The 8-period v2's S07–S08 locks are RETIRED.** Links `TOP-MATH-C1-08` (pattern Pool owed P04).
```

**Also update Open item #16** (line 420) — the U13 8-period assumption is now void; append to that bullet:

```
 **UPDATE 2026-08-05 (D-045):** U13 is now a 5-period chapter (re-cut 8p→5p); its former S07–S08 are retired. Open #16 concerns U14, not U13 — U14 S01–S06 record still owed.
```

**Header:** bump `v1.45` → `v1.46`, date `2026-08-05`.

---

## Cross-Project propagation

- **Project 04:** `TOP-MATH-C1-08` (pattern) Pool owed before অধ্যায় 13 is taught; **non-blocking** (already tracked in TODO drift-register item 04 / 376).
- **Project 00:** none. No master-file change (D-045 is Project-03-local; the re-cut executes REF-02 §2A.3 within-band).
- The standing D-034 Opening-ritual open item (TODO #00) is **not** touched — these five use the objective-cue construction (0 OPEN-RITUAL warns).

## Starter prompt for the next chat

> mode: BUILD — C1 MATH U13, resolve the ChapterPlan version collision (ruling on handoff 2026-08-05 §A). If ruling (a): confirm the 5-period v2 is canonical and S01–S05 locks stand; apply the §B patches. If (b): void the S01–S05 locks. Upload the authoritative `LOCKED_C1_MATH_U13_ChapterPlan_v2` (.md + .json) you want treated as current.
