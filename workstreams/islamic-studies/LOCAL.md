# LOCAL.md — <workstream name> (template — fill every ⬜)

Read AFTER root AGENTS.md. May tighten the protocol, never loosen it.

## Identity
⬜ One paragraph: what this workstream produces, for whom, classes/subjects covered.

## Status & provenance
⬜ LIVE / MIGRATING / PLANNED · source project(s)/repo · what was imported and when.
Keep the REGISTRY.md row in sync with this section.

## Decision series
⬜ Prefix (e.g. XX-D-###) · current highest number · where the log lives (`DECISIONS.md` here).

## Canon citations used
⬜ List the canon files/IDs this workstream depends on (e.g. canon/marklogic/…, REF-2 names).
Cite, never copy (AGENTS.md §8).

Already binding on this workstream before any authoring starts:

- `canon/language/LANGUAGE_RULES.md` §7 tier 1 — **Arabic script (CD-012, CD-014).**
- `canon/names/REF-2_Content_Register.md` — name pools and spelling house-style.
- `canon/image-rules/IMAGE_RULES.md` — living-being depiction (CD-007).

## POLICY — Arabic script (binding now, CD-014)

Arabic script is **RED in rendered fields** for this workstream today. This is a **renderer
capability** rule, not a doctrinal one: unshaped Arabic tofus or breaks joining in the Hub's PDF
renderer, and that surfaces after gold promotion, in a child's hand.

**Until it lifts, drafts use Bangla + transliteration with an `ARABIC-SLOT` placeholder** marking
where each ayah or hadith text will be inserted.

It lifts for this workstream only when **both** conditions in `LANGUAGE_RULES.md` §7 tier 1 hold —
proven shaping on this workstream's full render path (executed smoke test, real ayah, eyeball-
verified, logged), and verbatim quoted source with `source_note` provenance reviewed in the
**আলিম lane**, never model-composed. See the canon file for the authoritative wording; do not
restate it here.

## Artifacts & naming
⬜ File types, naming grammar, where finals live vs `_wip/`.

## Gates
⬜ What `audits/gates.py` checks, and any human gates (e.g. "naturalness = human gate by design").

## Operator workflow
⬜ Who runs sessions (teacher / Principal / reviewer lane) and the exact start/done phrases.

## Session-end sync
"save state and sync" = update `_wip/STATE.md` → append root SESSION_LOG.md block → commit → push.
⬜ Note any workstream-specific additions.
