# SLOTTING_CHECKLIST.md — files to copy into this kit (then delete this file)

Work top-down; after each slot, flip the file's row in `canon/MANIFEST.md` to REQUIRED and
re-run `python tools/audits/canon_check.py`.

## Step 1 — canon extract (before anything else)

- [ ] `canon/marklogic/` ← the 7 MarkLogic files from the Scholarship project
      (while slotting: fix `MarkLogic_Rules.md` §6 — ENG/MATH spines DO exist).
- [ ] `canon/islamic-curation/REF-1_Curation_Policy.md` ← SB-Governance (slot the
      Principal-approved version; note version in canon/DECISIONS.md).
- [ ] `canon/names/REF-2_Content_Register.md` ← SB-Governance.
- [ ] `canon/image-rules/IMAGE_RULES.md` ← consolidate from REF-1 image sections +
      school-applicable stripe/faceless rules (agent can draft; Principal approves).
- [ ] `canon/language/LANGUAGE_RULES.md` ← consolidate (agent can draft; Principal approves).
- [ ] `canon/school-facts/SCHOOL_FACTS.md` — stub included; Principal completes.

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
