# tools/_wip/STATE.md — Step 2 tools (session state)

Step 1 (canon extract) is CLOSED — see `canon/_wip/STATE.md` and CD-004…CD-008.
This file is the live state for **Step 2 — tools**.

## Phase

**Step 2 — tools.** Phase 2a (gate) and item 1 (hub-export) are DONE. The gate is proven and
`tools/hub-export/` is vendored, smoke-tested and documented. Remaining: `render/`, then
`images/`; `assets/` is DEFERRED. Waiting on Principal-supplied files into `_inbox/`.

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
| 1 | `tools/hub-export/` — `validate_import.py` + L1–L4 harness + `VENDOR.md` | `scd-hub` (LOCKED contract v1.0) | ✅ vendored + smoke-tested 2026-08-09 · 8 files · V-1, V-2 recorded |
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

## CD-011 cross-check — DONE 2026-08-09, result: DISAGREEMENT → PENDING-P-002

Both sources arrived and were compared. They do not agree, so under CD-011 nothing was merged.

- **Hub harness — no script guard at all.** Not a gap in reading: L1–L4 contain no charset
  check, `import-contract.schema.json` has **zero** `pattern` constraints, and the 7 patterns
  across the payload schemas are all ID/slug formats. Proven empirically — an envelope carrying
  `→ 🔒 — بسم` in `title` and `content` returns `RESULT: PASS … importable`, exit 0.
- **SB validator check 8 — has a guard, narrower than the old canon summary.** Arrows/emoji are
  RED **only in rendered text fields** (`text_bn`/`text_en`/titles) and GREY in metadata, because
  metadata legitimately carries →/⚠/🔒. Em-dash and ellipsis are **counted and reported, not
  red-failed** — its docstring says explicitly that they await this very CD-008 ruling. Arabic
  script is RED anywhere (D-011, absolute).

The old `canon/language/` SLOT summary ("no Arabic script / emoji / em-dash / arrows in JSON
strings") is wrong in detail on three of its four items against **both** sources.

Ruled the same day — see the next section.

## PENDING-P-002 RULED 2026-08-09 → CD-012 · CD-008 deferral CLOSED

Script guard is canon at `canon/language/LANGUAGE_RULES.md` §7: Arabic RED anywhere · arrows /
emoji RED in rendered text, GREY in metadata · em-dash and ellipsis ALLOWED with a WATCH counter
for one term. Old SLOT summary corrected on three of its four items in the CD-012 row.
Harness gap logged as **UP-001** (`tools/hub-export/UPSTREAM_ISSUES.md`) for `scd-hub`'s own
D-series — **not patched locally**, the harness is supersede-only (CD-013).

## Blockers

None in Step 2.

New, non-blocking: **PENDING-P-003** — CD-012 makes Arabic script RED everywhere, but
islamic-studies and the Arabic subject will need it. Nothing is authored there yet.

## Held for Step 3 — 5 files stay in `_inbox/` (Principal ruling 2026-08-09)

Support-books material from the same drop. **Stays in `_inbox/` until Step 3**; do not slot,
do not delete. `validator_v2_rebuilt.py` was read read-only for the CD-011 cross-check and is
the source of the CD-012 script-guard ranges.

| File | What it is |
|---|---|
| `validator_v2_rebuilt.py` | SB validator, rebuild of the lost v2 (checks 1–10, letter audit, script guard check 8) — read read-only for the CD-011 cross-check |
| `validator_letter_audit.py` | The subject-specific letter-audit check, C1–C2 বাংলা |
| `validate_admin_pass.py` | C1-BAN admin/governance merge pass (2026-07-17) |
| `letter_inventory_C1BAN_CANDIDATE_conjunctwhitelist.json` | C1-BAN letter inventory + conjunct whitelist (data, not a tool) |
| `VALIDATION_REPORT_C1BAN_54path.txt` | A validation report (output artifact) |

## Protocol status — RESOLVED 2026-08-09

`AGENTS.md` amended to **v1.1** (CD-010): §5 now requires `tools_check.py` before any push
touching `tools/`, and states the run-not-placed rule with its SMOKE.md evidence requirement.
The gate is protocol, not just practice.

## Carried forward from Step 1 (not blocking)

- ~~PENDING-P-001~~ — RULED 2026-08-09 → **CD-015**. REF-1's scope is the **whole school**, all
  current classes, extending one class per year; the class list is read from `SCHOOL_FACTS.md`.
  Overrides REF-1 §1.2, which is LOCKED and not edited. **The PENDING-P queue is now empty.**
- ~~PENDING-P-003~~ — RULED 2026-08-09 → **CD-014**. Tier 1 stands; ground restated as renderer
  capability; lifts **per render path** on proven Arabic shaping + verbatim আলিম-reviewed source.
  `ARABIC-SLOT` placeholder meanwhile. Recorded in `workstreams/islamic-studies/LOCAL.md`.
- **F-2** — MarkLogic Rules §6 does not list `C5_Bangla_Source_13-23.md`, now canon.
- **UP-001** — the Hub harness has no charset check; upstream's to fix, not ours (CD-013).
- **WATCH counter review** — em-dash/ellipsis counter runs for one term, then is retired or
  promoted (CD-012). Term-end date comes from `SCHOOL_FACTS.md` once completed.

## Next step — `tools/render/` (item 2)

Principal drops into `_inbox/`: Nikosh + Noto Sans Bengali font files, the Node docx generation
scripts (class-test generator), and `render_plan.py` (P03). Then the standard per-tool procedure
above: report → move → run → `SMOKE.md` → flip MANIFEST → replace SLOT README → both gates.

Two things to get right for `render/`:

1. **Fonts are binary.** Keep them in Git (small, stable) but they are already excluded from
   agent auto-read by `.claudeignore` (`tools/render/fonts/`). Add MANIFEST rows once filenames
   are known.
2. **The smoke test is a real render**, not a `--help`. Render an actual class test to .docx and
   confirm Bengali numerals per `LANGUAGE_RULES` §2 and the script guard per §7. A renderer that
   loads but produces tofu is exactly the failure UP-001 warns about.
3. **Optional but valuable while the fonts are in hand:** CD-014 lifts tier 1 per render path on
   an executed Arabic-shaping proof. If Noto/Nikosh shape Arabic correctly through this docx
   path, that test can be run now and logged in `render/SMOKE.md` — it is the only thing standing
   between islamic-studies and real ayat. Condition (2), আলিম-reviewed verbatim source, is a
   separate human gate and is not satisfied by any render test.

CD-008 is closed by CD-012 (2026-08-09). Remaining Step 2 order: render/ then images/; assets/ DEFERRED.
