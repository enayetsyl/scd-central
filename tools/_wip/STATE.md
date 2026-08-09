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

## Session 2026-08-09 (later) — render vendoring ATTEMPTED, BLOCKED on inputs

`_inbox/` contained **only the 5 support-books files held for Step 3**. No fonts, no reference
CTs, no `render_plan.py`; `uploads/` and `outputs/` were empty and no font file exists anywhere
in the workspace. Nothing was vendored and no MANIFEST row was flipped.

**Toolchain verified present** (this was the other unknown, and it is now closed):

| Tool | Version |
|---|---|
| node / npm | v22.22.3 / 10.9.8 |
| LibreOffice (`soffice`) | 26.2.4.2 |
| poppler (`pdftoppm`, `pdffonts`, `pdftotext`) | present |
| python-docx, fontTools | present (fontTools 4.63.0) |

⚠️ **The sandbox has no Bengali or Arabic fonts** — only Latin/CJK Noto and DejaVu. `apt-get` is
not permitted (no root). So the vendored fonts are not merely a convenience: **without them
nothing Bengali can render here at all.** This also means the smoke test cannot be dry-run
against a substitute.

### Built while blocked: `tools/_wip/glyph_probe.py`

The instrument CD-018 requires ("each render path proves its own glyph set empirically").
Not promoted to `tools/render/` — it is `_wip` until it runs against the real vendored fonts.
Three independent signals, because no single one is trustworthy:

1. **COVERAGE** (fontTools cmap) — definitive: a missing cmap entry *is* tofu.
2. **SUBSTITUTION** (pdffonts) — reveals LibreOffice fallback.
3. **RASTER** (pdftoppm PNG) — for the human eyeball CD-014 requires on Arabic.

**Self-validated on DejaVu Sans, and it earned its design.** Two findings:

- **The text-layer check is invalid, demonstrated not asserted.** `pdftotext` returned
  perfectly correct Bengali from a page that renders as solid tofu boxes — confirmed by eye on
  the raster. Anything that verified via .docx XML or text round-trip would have reported a
  clean pass on a completely broken page.
- **Signal 2 is weaker than expected.** With glyphs missing, `pdffonts` still listed only the
  requested font and flagged no substitution. So **coverage + raster are load-bearing;
  substitution is supplementary.** Do not rely on it alone.

**Early result on the legend glyphs, independent of the vendored fonts:** DejaVu covers
**★ ↑ ↓** and both tier-3 WATCH characters (**—** and **…**), but does **not** cover
**🔴 (U+1F534)** or **🟦 (U+1F7E6)** — those are colour-emoji codepoints. If Nikosh and Noto Sans
Bengali also lack them (very likely — text fonts rarely carry emoji), then under CD-018 the
finding is: **CT templates must not carry 🔴/🟦**, and the canon legend stays as it is. Not
concluded yet — it needs the real fonts.

## Probe results 2026-08-09 — fonts + reference CTs received, BOTH proofs run

Inputs received: 8 fonts (NotoSerifBengali ×2, NotoSerif ×2, NotoNaskhArabic ×4), two reference
CTs (`C5_Bangla_ClassTest_Ch19.md`, `Ch20.md`), `render_plan.py`. **Nothing vendored yet** — the
findings below need rulings first. Fonts installed to the sandbox font path (`~/.local/share/fonts`
+ `fc-cache`); without that step LibreOffice silently falls back and signals 2–3 are void.

### Proven glyph set — docx → LibreOffice → pdftoppm, eyeball-verified on raster

| | Result |
|---|---|
| Bengali: numerals, যুক্তবর্ণ, কারচিহ্ন, special marks | ✅ correct (Noto Serif Bengali) |
| **Arabic incl. harakat — RTL + joining** | ✅ **correct (Noto Naskh Arabic)** |
| Em-dash, ellipsis (tier-3 WATCH) | ✅ correct |
| Latin + digits | ✅ correct |
| 🔴 U+1F534 · 🟦 U+1F7E6 | ❌ **TOFU — empty boxes on the page** |
| ✓ U+2713 · ✅ U+2705 · → U+2192 · ⚠ U+26A0 | ❌ **TOFU** |
| ★ U+2605 · ↑ U+2191 · ↓ U+2193 | ⚠ render only via DejaVu fallback, visually collided |

### CD-014 condition (1): SATISFIED for the docx path

Arabic ayah rendered and eyeball-verified: RTL correct, letters joined, diacritics positioned.
Font: **Noto Naskh Arabic**. Condition (2) — verbatim source with `source_note`, আলিম-reviewed —
is a human gate and remains open. islamic-studies stays on `ARABIC-SLOT` until (2) is met.

### ⚑ Finding R-1 — the reference CTs use glyphs that tofu

`✓` appears in **student-facing** text: *"সঠিক উত্তরটিতে টিকচিহ্ন (✓) দাও"* (Ch19 Q1, Ch20).
`→` and `✅`/`⚠` appear in the teacher section. All tofu in this path.
Under **CD-018** this constrains the template, not canon. Needs a ruling — options: substitute a
covered character (e.g. `(টিক)` or a Bengali-covered mark), or add a symbol fallback font to the
render path. **The generator cannot be finalised until this is decided — `✓` is in the template.**

### ⚑ Finding R-2 — font supply differs from the checklist

Checklist and `tools/render/README.md` specify **Nikosh + Noto Sans Bengali**. Supplied:
**Noto *Serif* Bengali**, and **no Nikosh at all**. Noto Serif Bengali covers everything Bengali
and renders correctly, so this is not a defect — but Nikosh is the Bangladesh government/NCTB
standard face, so the printed CT will not match NCTB's look. Confirm the substitution is intended.

## R-1 / R-2 RULED 2026-08-09 → CD-019 · `tools/render/` VENDORED AND PROVEN

Fonts vendored (Regular + Bold only; Naskh Medium/SemiBold skipped, left in `_inbox/`).
`render_plan.py` vendored. `ct_docx.py` authored against both reference CTs, font family as
config. `glyph_probe.py` promoted out of `_wip` to `tools/render/`. Both smoke tests run
end-to-end; proven glyph set and the font-install prerequisite recorded in
`tools/render/SMOKE.md`. **CD-014 condition (1) satisfied for the docx path.**

## Open items from this session

1. **`render_plan.py` is vendored but UNPROVEN** — no P03 plan JSON was supplied, so it has
   never been executed. Its MANIFEST row stays PENDING. Needs a plan JSON to smoke-test.
2. **⚑ Gate blind spot found.** `tools_check.py` warns when a PENDING row's file is *missing*,
   but goes silent once the file is *present yet unproven* — exactly `render_plan.py`'s state.
   A vendored-but-unrun tool currently produces no signal at all. Proposed fix: a third status
   (e.g. `VENDORED`) that warns until the folder's `SMOKE.md` names the file. Not implemented —
   changing gate semantics is a decision row, not a quiet edit.
3. **Nikosh absent (R-2, accepted).** Printed CTs will not match the NCTB face. If that matters
   for parent- or board-facing print, Nikosh has to be sourced and the path re-proven —
   CD-018 proves per render path, and a font change is a new path.

## Blockers

None. Step 2 remaining: `tools/images/`; `tools/assets/` DEFERRED.

Earlier input list (now satisfied except as noted):

1. **Font files** — Nikosh + Noto Sans Bengali (`.ttf`/`.otf`). Nothing Bengali renders without them.
2. **Reference CTs** — the produced class tests the generator is to be authored against.
   Authoring it without them would be improvising a format (AGENTS.md §2: agents never improvise).
3. **`render_plan.py`** (P03) and the existing Node docx scripts, if they are to be vendored
   rather than written fresh.
4. **For the CD-014 Arabic proof:** confirmation of which font is intended to carry Arabic.
   Neither Nikosh nor Noto Sans Bengali covers Arabic script, so a third font (e.g. a Noto
   Naskh Arabic) is required — or the proof cannot pass and islamic-studies stays on
   `ARABIC-SLOT`.

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
  promoted (CD-012). **Date now fixed: mid-December 2026**, at annual-exam close
  (`SCHOOL_FACTS.md` v1.0, CD-017).
- ~~PENDING-P-004~~ — RULED 2026-08-09 → **CD-018**. Guard governs strings entering a mechanical
  render path; **extends to the docx path automatically once `tools/render/` is vendored**;
  human-read markdown is out of scope. **The PENDING-P queue is empty again.**

## Next step — `tools/render/` (item 2)

Principal drops into `_inbox/`: Nikosh + Noto Sans Bengali font files, the Node docx generation
scripts (class-test generator), and `render_plan.py` (P03). Then the standard per-tool procedure
above: report → move → run → `SMOKE.md` → flip MANIFEST → replace SLOT README → both gates.

Two things to get right for `render/`:

1. **Fonts are binary.** Keep them in Git (small, stable) but they are already excluded from
   agent auto-read by `.claudeignore` (`tools/render/fonts/`). Add MANIFEST rows once filenames
   are known.
2. **The smoke test is a real render**, not a `--help`, and under **CD-018** it is also how this
   path's proven glyph set is established. The smoke document must carry, in one render:

   - Bengali numerals (০–৯) per `LANGUAGE_RULES` §2
   - the legend glyphs **🔴 🟦 ★ ↑ ↓**
   - an **em-dash** (—) and an ellipsis (…), the tier-3 WATCH characters
   - Bengali conjuncts (যুক্তবর্ণ) and কারচিহ্ন, which are the real Nikosh/Noto shaping risk

   Record in `render/SMOKE.md` **what survives the full docx → LibreOffice → pdftoppm chain**,
   verified on the rasterised page, not in the .docx XML. A renderer that loads but produces
   tofu is exactly the failure UP-001 warns about.

   **If the legend glyphs tofu in that chain, CT templates must not carry them. That is a
   finding to report — not a canon change** (CD-018). `LANGUAGE_RULES` §7 stays as written; the
   constraint lands on the templates feeding this path.
3. **Optional but valuable while the fonts are in hand:** CD-014 lifts tier 1 per render path on
   an executed Arabic-shaping proof. If Noto/Nikosh shape Arabic correctly through this docx
   path, that test can be run now and logged in `render/SMOKE.md` — it is the only thing standing
   between islamic-studies and real ayat. Condition (2), আলিম-reviewed verbatim source, is a
   separate human gate and is not satisfied by any render test.

CD-008 is closed by CD-012 (2026-08-09). Remaining Step 2 order: render/ then images/; assets/ DEFERRED.
