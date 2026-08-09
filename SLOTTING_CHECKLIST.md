# SLOTTING_CHECKLIST.md — files to copy into this kit (then delete this file)

Work top-down; after each slot, flip the file's row in `canon/MANIFEST.md` to REQUIRED and
re-run `python tools/audits/canon_check.py`.

## Step 1 — canon extract (before anything else) ✅ CLOSED 2026-08-09

- [x] `canon/marklogic/` ← the 7 MarkLogic files from the Scholarship project. **CD-004.**
      The §6 fix was unnecessary — the supplied v১ already lists all five spines.
- [x] `canon/islamic-curation/REF-1_Curation_Policy.md` ← **v1.2 LOCKED. CD-005.**
      The "v1.0 / 11 C-codes / S1–S4 / SB-016" description was stale: 19 categories C-01…C-19,
      three annotation tags, no severity scheme, flag ruling is C-18.
- [x] `canon/names/REF-2_Content_Register.md` ← **REF-20 Approved Names Pool v1.0. CD-006.**
      Recurring-cast reference-sheet claim withdrawn (storybook material).
- [x] `canon/image-rules/IMAGE_RULES.md` ← **REF-1-derived only. CD-007.** Stripe /
      largest-being / carve-out / photocopy-safe / silhouette ruled out of scope.
- [x] `canon/language/LANGUAGE_RULES.md` ← **CD-008.** সাধু/চলিত ruled; swarabritta out of
      scope; Hub renderer script guard deferred to Step 2 with its own CD row.
- [ ] `canon/school-facts/SCHOOL_FACTS.md` — stub in place and REQUIRED-passing.
      **Principal completes** (academic-calendar, staffing facts). Not agent-executable.

## Step 2 — tools

- [ ] `tools/render/` ← Nikosh + Noto Sans Bengali font files; Node docx scripts
      (class-test generator); `render_plan.py` (P03).
- [ ] `tools/images/` ← `apply_strips.py` + pdftoppm verification helpers (storybook pipeline;
      neutral tools only).
- [ ] `tools/hub-export/` ← `validate_import.py` + L1–L4 harness from `scd-hub`.
- [ ] `tools/assets/` ← rclone `sync.py` (or write fresh when first needed).

## Step 2b — english-drive + class-tests fold-in (handoff §5 order)

- [ ] `workstreams/english-drive/` ← full EnglishDrive repo content (preserve Git history if
      convenient: `git subtree add`; otherwise copy + keep old repo archived-private).
- [ ] `workstreams/class-tests/` ← project artifacts + write its POLICY section in LOCAL.md.

## Later steps (3–5)

Support-books (resolve the three-way version split by slotting ONLY the Principal-approved
set), lesson-plans (P03 quartet + validate/render toolchain), question-banks,
english-programme (recovered instructions from archive), islamic-studies (greenfield),
accounting (recovery package → `workstreams/accounting/`, open items into its STATE.md).

- [ ] `archive/old-account/` ← recovery packages (read-only provenance).
- [ ] Delete this file when done (its content is superseded by REGISTRY.md rows).
