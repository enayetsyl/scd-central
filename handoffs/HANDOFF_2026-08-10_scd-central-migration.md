# HANDOFF — scd-central Migration (continuation of HANDOFF_2026-08-09_unification)
**Date:** 2026-08-10 · **Owner:** SCD (Principal) · **Supersedes** the 2026-08-09 unification handoff's §5–§7 (plan → now executed)

**Purpose:** a new chat, given this file, continues as the Principal's advisor for the
scd-central migration without re-asking anything settled. The working pattern: Principal ↔
advisor chat (this role) ↔ Cowork agent sessions on the repo. The advisor gives ONE
recommendation with paste-ready ruling text; the agent executes gates and never self-approves;
files-over-memory and verify-at-source bind everyone including the advisor (it has been
corrected at source three times: candidate-inventory report claim, D-020 queue claim,
20–30 CT band vs canon's flat 25).

## 1. What is LIVE
**`scd-central`** (private, github.com/enayetsyl/scd-central) — the school monorepo, built
2026-08-09 from a starter kit, now through migration Steps 1–4. Latest state: ~ee511e1+
(policy import pending). AGENTS.md v1.1 = canonical protocol (question-routing §6,
corrections ledger, canon cite-never-copy §8, Cowork workarounds §9). Gates all executed:
`tools/audits/canon_check.py` + `tools_check.py` repo-wide; per-workstream `audits/gates.py`.
PENDING_PRINCIPAL queue: empty. CD-series ≈ CD-034+.

- **Step 1 canon — CLOSED.** 13/13 slotted: marklogic ×7 (Rules §6 fixed), REF-1, REF-2,
  IMAGE_RULES (REF-1-derived; storybook rules explicitly out of scope), LANGUAGE_RULES
  (script guard §7), SCHOOL_FACTS (load-bearing: class list per CD-015, term dates; CT line
  verified: 25 marks flat, no fixed day, subject teacher schedules).
- **Step 2 tools — CLOSED.** hub-export (8 files vendored, smoke-proven; symlinked not
  copied where LOCKED), render (fonts: NotoSerifBengali/NotoSerif/NotoNaskhArabic R+B;
  ct_docx.py generator ACCEPTED — coverage-driven font routing, --strict; glyph_probe.py;
  35-min/25-mark CT model output Principal-verified), images (apply_strips.py +
  verify_strip.py; pick_placements.py = tkinter, permanently UNPROVEN until a workstation
  click-session), assets (deferred by design).
- **Step 3 support-books — CLOSED, LIVE.** C1-BAN 54-পাঠ book merged **gate-GREEN** (L53
  MOTOR fix; sentinel covers পাঠ 2/5/7/53 — NOT 18). validator_v2_rebuilt.py is the gate
  (v2-original lost in chat space; rebuild spec-derived, 16/16 selftest). Conjunct
  whitelists FROZEN পাঠ ৪৫/৪৯/৫১/৫২ from NCTB pages (box-only derivation = canon CD-029;
  freeze overturned wrong `glyphs:[]` claims at ৪৯/৫১ = CR-005). D-020 (mixed-classroom
  fiqh, S4, OPEN → RQ-003 আলিম lane) and D-021 (weapon-line) reconstructed. Reviewer queue
  RQ-001–003+. The SB-P Claude project is RETIRED as production floor (status note filed).
- **Step 4 lesson-plans — CLOSED, LIVE.** 4/4 artifacts proven end-to-end
  (validate_plan → byte-identical re-render → build_envelope → validate_import): first
  born-conformant content. Register continuous to D-PROJ03-049 (043/044/045 reconstructed;
  046 U20 newline supersede; 047 C2-MATH-U05 override PARKED — surviving copy is
  pre-override, post-override bytes recorded LOST; 048 = **B-LP.1c: bismillah canonical**
  in openings, composed with objective cue, forward-only, P00 patch pending fold-in;
  049 reference import). Master D-series register (PROJECT00_README §3, D-001–D-053)
  imported READ-ONLY; **D-051 reconstructed** in its errata section from 78 convergent
  citations + D-PROJ00-064 corroboration (D-051 = HW-pool placement → Project 04,
  supersedes D-029). **CD-034: bare D-0NN is ambiguous — always check both registers**
  (33 of 36 bare citations collide with same-numbered D-PROJ03 rows).

## 2. Standing technical rulings (cite, don't re-derive)
- **Script guard follows render paths, not file formats** (CD-018): Hub-bound JSON +
  book JSONs red-tiered (Arabic red anywhere per D-011; arrows/emoji red in rendered
  text_bn/text_en/titles, grey in metadata; em-dash/ellipsis ALLOWED — WATCH counter
  review mid-Dec 2026). Markdown/legend glyphs out of scope. Hub harness has NO charset
  check (UP-001, proven empirically) — upstream scd-hub issue.
- **Arabic is capability-gated, not doctrine** (CD-014): docx→LibreOffice→raster path
  PROVEN for ayah (RTL/joining/harakat). Condition (2) still gates islamic-studies:
  verbatim sourced text + আলিম review; drafts stay on ARABIC-SLOT. Hub's pdfkit path
  cannot shape Arabic — upstream gap to raise before islamic-studies imports anything.
- **Evidence rules:** run-not-placed (CD-020: PENDING / VENDORED-UNPROVEN / REQUIRED-
  needs-SMOKE-run); raster-eyeball only (pdftotext proven to lie on tofu pages);
  seeded-error/negative-test every new gate; "declaring a loss is as much a claim as
  declaring an archive" — not-present ≠ lost until searched and stated where.
- **Deliverables stay committed** (teachers are zero-Git); evidence rasters committed,
  regenerable scratch gitignored. Reference CTs teach STRUCTURE not time (৪৫মিনিট in them
  is superseded; 35 std/30 permitted).

## 3. The question-project plan (Principal's new direction, in flight)
Three policy drafts v0.1 delivered to Principal (files exist; import pending his ⚑ answers):
1. **MODEL_PAPERS_POLICY** — model HY+Annual (100) per class×subject + model CT (25/35)
   generated from MarkLogic spines; C5 first; supersedes the 21 templates' 80-mark halves.
2. **SOURCE_POLICY** — every NCTB book scanned → per-chapter extraction files (the
   C5_Bangla_Source_13-23 pattern; raster-read, offset-verified); canon/sources/;
   extraction-only sourcing (no question from model memory).
3. **QUESTION_BANK_POLICY** — **three pools per chapter: HW · AS · CT (CW DISCARDED by
   Principal ruling); zero overlap between pools**; tags ride the LOCKED envelope fields
   (bloom_level, difficulty, topic_tag, paper_role — agent must VERIFY paper_role enum
   covers HW/AS/CT; if not it's an ADDITIVE upstream change, never improvised); born-
   conformant via vendored harness; **pilot = C5 Bangla পাঠ ২১** (seeds from accepted Ch21
   CT + annual material) which closes the LAST TWO VENDORED-UNPROVEN rows
   (build_question_envelopes.py + question payload schema).
⚑ owed from Principal: pool sizes (~30/15/10-12 defaults), AS difficulty skew, REL scope,
scan ownership, model-CT granularity, production order confirm.
**Hub software companions (later, scd-hub PRDs per its own D-series):** usage-lock (used
HW/AS question never auto-offered twice) + AS spaced-revision rotation (2/4/8-week style).
Authoring side only guarantees stable IDs + pool/topic tags.

## 4. Open/parked ledger
- D-047 parked (reopens only if post-override bytes surface in old exports).
- D-038 sweep parked + widened to openings; C1 BAN U21/U28 standalones NOT FOUND in P03
  project — Principal still to search the locking chats' outputs + local Lesson Plans folders.
- P00 fold-in future notes: errata D-051 must MOVE into §3 (never copy-over); planned
  register-consistency gate (range-claim vs actual rows — the disease hit twice).
- UP-001 (harness charset) · pdfkit-Arabic upstream row · WATCH review mid-Dec 2026 ·
  PAT renewals Aug 2027 · pick_placements workstation session.
- **Not yet migrated:** EnglishDrive + class-tests fold-in (original Step 2 — EnglishDrive
  still runs in its own repo with its own protocol; C2B06b Phase 4 sentence-bank and
  C4B06 Part-E PD status unknown to this chat), P00, question-banks (policies pending),
  english-programme (recovered instructions in archive), islamic-studies (greenfield,
  ARABIC-SLOT), accounting (Check-5 423,533 break; +28,592 residual).
- **Confirm scd-hub was flipped private** (advised after harness copy; unconfirmed).

## 5. Session mechanics (unchanged)
Inputs travel via `scd-central/_inbox/` (Principal stages, agent classifies before moving —
several wrong/partial drops were caught this way: wrong register, missing PDF, pre-override
bytes). Agent batches questions per AGENTS §6; Principal rules via paste-ready text from the
advisor; sync only on explicit approval; verbatim gate output before any "final". Cowork
quirks per AGENTS §9. Bengali for teacher-facing, English for protocol files.

## 6. Working style (binding, unchanged)
Precise & concise; ONE recommendation + 1–2 line justification; copy-paste-exact rulings;
files-over-memory; flag-don't-improvise; step-by-step for setup work; verify at source
before citing any decision — and expect the agent to verify the advisor's claims too.
