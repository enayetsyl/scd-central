# canon/_wip/STATE.md — Step 1 canon extract (session state)

Canon slotting is repo-level, not a workstream, so its `_wip/` lives here (AGENTS.md §3 intent).
A killed session must be resumable from this file alone.

## Phase

**Step 1 — canon extract.** Phase 1b = slotting. MarkLogic (rows 1–7) DONE.
Rows 8–9 held at the gate on two identity/version questions to the Principal (below).
No promotion out of `_inbox/` until each file is slotted + its MANIFEST row flipped + gate re-run.
Files are **moved**, not copied, out of `_inbox/` — a copy left behind trips the gate's NO-COPY rule.

## Baseline gate (session start, 2026-08-09, before any change)

```
canon_check.py — root: /…/scd-central
  WARN  MANIFEST: canon/marklogic/MarkLogic_Rules.md [PENDING] missing (not yet slotted)
  WARN  MANIFEST: canon/marklogic/MarkLogic_BAN_Spine.md [PENDING] missing (not yet slotted)
  WARN  MANIFEST: canon/marklogic/MarkLogic_ENG_Spine.md [PENDING] missing (not yet slotted)
  WARN  MANIFEST: canon/marklogic/MarkLogic_MATH_Spine.md [PENDING] missing (not yet slotted)
  WARN  MANIFEST: canon/marklogic/MarkLogic_SCI_BGS_Spine.md [PENDING] missing (not yet slotted)
  WARN  MANIFEST: canon/marklogic/MarkLogic_QuestionPolicy.md [PENDING] missing (not yet slotted)
  WARN  MANIFEST: canon/marklogic/C5_Bangla_Source_13-23.md [PENDING] missing (not yet slotted)
  WARN  MANIFEST: canon/islamic-curation/REF-1_Curation_Policy.md [PENDING] missing (not yet slotted)
  WARN  MANIFEST: canon/names/REF-2_Content_Register.md [PENDING] missing (not yet slotted)
  WARN  MANIFEST: canon/image-rules/IMAGE_RULES.md [PENDING] missing (not yet slotted)
  WARN  MANIFEST: canon/language/LANGUAGE_RULES.md [PENDING] missing (not yet slotted)
  WARN  PLACEHOLDER: canon/image-rules/README.md still unslotted
  WARN  PLACEHOLDER: canon/islamic-curation/README.md still unslotted
  WARN  PLACEHOLDER: canon/language/README.md still unslotted
  WARN  PLACEHOLDER: canon/marklogic/README.md still unslotted
  WARN  PLACEHOLDER: canon/names/README.md still unslotted
  WARN  PLACEHOLDER: tools/assets/README.md still unslotted
  WARN  PLACEHOLDER: tools/hub-export/README.md still unslotted
  WARN  PLACEHOLDER: tools/images/README.md still unslotted
  WARN  PLACEHOLDER: tools/render/README.md still unslotted
RESULT: CLEAN (0 fail, 20 warn)
```

Target at end of Step 1: 11 MANIFEST warns and 5 canon PLACEHOLDER warns cleared;
the 4 `tools/` placeholder warns remain (Step 2, out of scope here).

## Session rulings (2026-08-09, Principal)

- Delivery: files are dropped into `_inbox/` (gitignored staging), then slotted.
- REF-1 version: not pre-decided — the agent reports the version the supplied file declares
  and asks before slotting.
- IMAGE_RULES.md / LANGUAGE_RULES.md: consolidation drafted only AFTER REF-1 + REF-2 are slotted.

## Slot ledger

| # | Canon path | Source expected | Status |
|---|---|---|---|
| 1 | canon/marklogic/MarkLogic_Rules.md | Scholarship project | ✅ slotted 2026-08-09 · v১ 08-08-2026 |
| 2 | canon/marklogic/MarkLogic_BAN_Spine.md | Scholarship project | ✅ slotted 2026-08-09 · v১ |
| 3 | canon/marklogic/MarkLogic_ENG_Spine.md | Scholarship project | ✅ slotted 2026-08-09 · v১ |
| 4 | canon/marklogic/MarkLogic_MATH_Spine.md | Scholarship project | ✅ slotted 2026-08-09 · v১ |
| 5 | canon/marklogic/MarkLogic_SCI_BGS_Spine.md | Scholarship project | ✅ slotted 2026-08-09 · v১ |
| 6 | canon/marklogic/MarkLogic_QuestionPolicy.md | Scholarship project | ✅ slotted 2026-08-09 · v১ |
| 7 | canon/marklogic/C5_Bangla_Source_13-23.md | Scholarship project | ✅ slotted 2026-08-09 · v১ |
| 8 | canon/islamic-curation/REF-1_Curation_Policy.md | was `LOCKED_CurationPolicy_v1_2.md` | ✅ slotted 2026-08-09 · v1.2 LOCKED · CD-005 |
| 9 | canon/names/REF-2_Content_Register.md | was `LOCKED_REF-20_Approved_Names_Pool_v1_0.md` | ✅ slotted 2026-08-09 · v1.0 · CD-006 |
| 10 | canon/image-rules/IMAGE_RULES.md | consolidate (agent drafts) | ✅ slotted 2026-08-09 · REF-1-derived only · CD-007 |
| 11 | canon/language/LANGUAGE_RULES.md | consolidate (agent drafts) | 🟡 DRAFT in `_wip/DRAFT_LANGUAGE_RULES.md` — 3 gaps, awaiting Principal |
| 12 | canon/school-facts/SCHOOL_FACTS.md | stub in repo | ⬜ Principal to complete (not blocking Step 1) |

## Per-file slot procedure (repeat for each row)

1. File lands in `_inbox/`.
2. Agent reads it, reports: declared version/date, obvious staleness, any canon-copy conflict.
3. Copy to the canon path (forward-only naming, AGENTS.md §7); no reader-facing version history inside.
4. Apply the checklist-authorised fix if the row calls for one (row 1: Rules §6 — ENG/MATH spines DO exist).
5. Flip that row in `canon/MANIFEST.md` PENDING → REQUIRED.
6. Replace the sub-folder `README.md` SLOT placeholder with a real index (clears PLACEHOLDER warn)
   — only once every file in that sub-folder is slotted.
7. Re-run `python tools/audits/canon_check.py`; paste verbatim.

## Gate after MarkLogic slot (2026-08-09)

`RESULT: CLEAN (0 fail, 12 warn)` — 8 MarkLogic warns cleared, 0 introduced.

## Findings raised at slotting — [Principal] items

**F-1 (resolved, no action).** The checklist expected `MarkLogic_Rules.md` §6 to be stale
(ENG/MATH spines said not to exist). The v১ file supplied already lists all five spine files
correctly. No edit applied; the checklist line is simply out of date.

**F-2 (open, non-blocking).** `MarkLogic_Rules.md` §6 lists six files. It does not list
`C5_Bangla_Source_13-23.md`, which is now canon. Adding a row is a canon content change →
Principal-gated. Default meanwhile: file is slotted and cited; §6 stays as supplied.

**Q-A (blocking row 8) — REF-1 identity + version.** `canon/README.md` and the SLOT README
expect *"REF-1 Curation Policy v1.0 LOCKED — 11 C-codes, S1–S4 severity, retain/avoid lists,
anthem/flag ruling SB-016."* The supplied file is **Islamic Curation Policy v1.2 LOCKED**
(locked 2026-05-26, Project 02, supersedes v1.1 and v1.0), and it differs on every count:
**19 categories C-01…C-19**, not 11 C-codes; **three annotation tags** (KEEP-AS-IS /
NEEDS-REPLACEMENT / FLEXIBLE), **no S1–S4 severity scheme**; no SB-016 anywhere (the flag /
monument ruling lives in **C-18**); it is called **REF-01** in its source project, not REF-1.
Its declared scope is **Class 1 Bangla + English only**; other subjects and classes expand at v2.0.

**Q-B (blocking row 9) — REF-2 identity.** MANIFEST expects
`REF-2_Content_Register.md` (*"Name Bank: 220 Principal-vetted names in 5 class pools,
recurring cast উমর/আনাস/খাদিজা/ফাতিমা with reference-sheet canon"*). The supplied file is
**REF-20 — Approved Names Pool (Bengali-Muslim) v1.0**. The Name Bank half matches exactly —
**220 name rows**, 5 class pools C1–C5, 22 male + 22 female each, উমর/আনাস/খাদিজা/ফাতিমা
present. But it carries **no recurring-cast reference sheet**; its §4 explicitly says what it
does not govern. So either "Content Register" = REF-20 under an older label, or the
reference-sheet canon is a second file still to be supplied.

**Q-A resolved 2026-08-09 (Principal):** v1.2 is authority, the README description was stale
→ CD-005, README corrected, slotted.
**Q-B resolved 2026-08-09 (Principal):** REF-20 IS REF-2; the recurring-cast reference-sheet
claim is withdrawn (storybook material, not school canon) → CD-006, README corrected, slotted.
**Scope ruling 2026-08-09 (Principal):** REF-1's C1-Bangla/English scope limit is raised as
**PENDING-P-001**, not written into canon as a standing rule.

## Row 10 ruling (2026-08-09, Principal)

**"IMAGE_RULES REF-1-derived only."** Draft promoted to `canon/image-rules/IMAGE_RULES.md`;
the four storybook-sourced gaps ruled out of scope and recorded as such in the file's §8 so
nobody re-applies them by assumption. `_wip/DRAFT_IMAGE_RULES.md` removed on promotion
(a second copy of a canon file is exactly what the NO-COPY rule exists to prevent). CD-007.

## Blockers

**Row 11 only.** `LANGUAGE_RULES` cannot be finished from repo sources. Draft is written and
traced at `_wip/DRAFT_LANGUAGE_RULES.md`; three gaps await a Principal ruling:

- **G-1 Hub renderer script guard** — blocked behind `tools/hub-export/`, a Step 2 slot.
  Cannot be resolved before Step 2 regardless of ruling.
- **G-2 swarabritta rhyme spec** — agent recommendation: drop until a workstream needs it.
- **G-3 সাধু-vs-চলিত** — no source anywhere; surfaced by C5 Bangla lesson 20.

The same ruling shape as row 10 would close G-2 and G-3 immediately; G-1 waits on Step 2.

## Next step

Principal rules on row 11's three gaps (or defers G-1 to Step 2 and closes G-2/G-3), then
row 11 promotes, MANIFEST flips, gate re-runs, and **Step 1 closes** — after which
`SLOTTING_CHECKLIST.md` Step 1 is ticked and Step 2 (tools) begins.

## Open PENDING-P rows

**PENDING-P-001** — REF-1 v1.2 scope is Class 1 Bangla/English only; how are C2–C5 and other
subjects governed meanwhile? Default in use: cite REF-1 only inside its declared scope,
flag out-of-scope citations. Blocks C2–C5 curation promotion/print, not the canon slot itself.
