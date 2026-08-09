# tools/_wip/STATE.md — Step 2 tools (session state)

Step 1 (canon extract) is CLOSED — see `canon/_wip/STATE.md` and CD-004…CD-008.
This file is the live state for **Step 2 — tools**.

## Phase

**Step 2 — tools.** Phase 2a = gate first, then intake. The gate exists and is proven;
nothing is vendored yet. Waiting on Principal-supplied files into `_inbox/`.

## Done this session (2026-08-09)

- `tools/MANIFEST.md` created — machine-readable tool index, mirrors canon/MANIFEST.md.
- `tools/audits/tools_check.py` created and **negative-tested**: all five FAIL paths fire
  and exit 1. Logged as **CD-009**.
- `tools/audits/README.md` documents both repo-wide gates.

Baseline (2026-08-09, nothing vendered yet):

```
tools_check.py — root: /…/scd-central
  WARN  MANIFEST: tools/hub-export/validate_import.py [PENDING] missing (not yet vendored)
  WARN  MANIFEST: tools/render/render_plan.py [PENDING] missing (not yet vendored)
  WARN  MANIFEST: tools/images/apply_strips.py [PENDING] missing (not yet vendored)
  WARN  PLACEHOLDER: tools/assets/README.md still unslotted
  WARN  PLACEHOLDER: tools/hub-export/README.md still unslotted
  WARN  PLACEHOLDER: tools/images/README.md still unslotted
  WARN  PLACEHOLDER: tools/render/README.md still unslotted
RESULT: CLEAN (0 fail, 7 warn)
```

## The rule that governs Step 2 (CD-009)

**A tool is done when it has been run, not when it has been placed.** Every REQUIRED row needs
a `SMOKE.md` beside it recording the command and its verbatim output. The gate fails without one.

## Slot ledger

| # | Target | Source expected | Status |
|---|---|---|---|
| 1 | `tools/hub-export/` — `validate_import.py` + L1–L4 harness + `VENDOR.md` | `scd-hub` (LOCKED contract v1.0) | ⬜ awaiting files |
| 2 | `tools/render/` — Nikosh + Noto Sans Bengali fonts, Node docx class-test generator, `render_plan.py` | EnglishDrive / class-test project / P03 | ⬜ awaiting files |
| 3 | `tools/images/` — `apply_strips.py` + pdftoppm verification helpers | storybook pipeline (neutral tool only) | ⬜ awaiting files |
| 4 | `tools/assets/` — rclone `sync.py` + assets_manifest convention | none | ⏸ DEFERRED (CD-009) |

**Recommended order: 1 → 2 → 3.** hub-export first because it is the only item that unblocks
something already deferred — the Hub renderer script guard held open by CD-008 — and because
CD-003 makes it the sole integration path. It is also self-testing: feed it one conformant and
one deliberately malformed envelope.

## Per-tool slot procedure

1. Files land in `_inbox/`.
2. Agent reports what arrived and any version/identity mismatch **before** moving anything.
3. **Move** (never copy) into the tool folder — a copy left in `_inbox/` trips canon_check's
   NO-COPY rule if the basename collides with canon.
4. Run the tool against a real input. Record command + verbatim output in `SMOKE.md`.
5. For `hub-export/` only: write `VENDOR.md` (upstream repo, contract version, date, commit if known).
   Vendored under LOCKED contract v1.0 — **supersede-only, never edited locally** (AGENTS.md §7, CD-003).
6. Flip the `tools/MANIFEST.md` row PENDING → REQUIRED; replace the folder's SLOT README with a real index.
7. Run **both** gates; paste verbatim.

## Blockers

**Waiting on the Principal to drop tool files into `_inbox/`.** Nothing in Step 2 can proceed.

## Protocol status — RESOLVED 2026-08-09

`AGENTS.md` amended to **v1.1** (CD-010): §5 now requires `tools_check.py` before any push
touching `tools/`, and states the run-not-placed rule with its SMOKE.md evidence requirement.
The gate is protocol, not just practice.

## Carried forward from Step 1 (not blocking)

- **PENDING-P-001** — REF-1 v1.2 governs Class 1 Bangla/English only.
- **F-2** — MarkLogic Rules §6 does not list `C5_Bangla_Source_13-23.md`, now canon.
- **CD-008 deferral** — Hub renderer script guard enters canon as its own CD row when
  `tools/hub-export/` is vendored. Closing Step 2 item 1 closes this too.

## Next step — hub-export first (Principal instruction 2026-08-09)

Principal drops hub-export files into `_inbox/` → vendor, smoke-test against one conformant and
one deliberately malformed envelope, write `VENDOR.md`, flip the row, run both gates.

**Then the deferred CD-008 script-guard row, under the CD-011 rule — read this before writing it:**

1. Derive the guard **from the actual harness code**. Not from memory, not from the
   `canon/language/` SLOT README summary, not from this file.
2. **Cross-check it against the SB validator's list.** ⚠️ That list is **not in this repo** and
   must be supplied alongside the harness — flag it if it does not arrive.
3. **Any disagreement between the two sources goes to the Principal as a PENDING-P item.**
   It is never silently merged, reconciled, or averaged. Two sources that disagree about what
   the renderer accepts is a finding, not a formatting problem.

Only once that row is written does CD-008's deferral close.
