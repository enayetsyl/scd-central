# SCHEMA — support-book.json v1

> ## ⚖️ Canon precedence (CD-027)
>
> This file is the workstream's **operating spec for everything canon does not cover** — the
> nine-step loop, roles, the annual cycle, the validator profile's mechanics.
>
> **Where it restates canon, canon wins.** Those sections are **superseded-by-citation**: they
> are left in place as the historical spec, not edited out, and the citation below is the
> authority to read instead.
>
> | Section here | Superseded by |
> |---|---|
> | §6 Letter-audit algorithm — script-guard portion | `canon/language/LANGUAGE_RULES.md` §7 (CD-012, CD-018) |
> | §7 check↔field map — image fields | `canon/image-rules/IMAGE_RULES.md` (CD-007) |
> | Any C-code semantics | `canon/islamic-curation/REF-1_Curation_Policy.md` v1.2 (CD-005) |
> | Name/cast fields | `canon/names/REF-2_Content_Register.md` (CD-006) |
>
> If this file and a canon file disagree, the canon file is right and this one is stale.


**Support-Book Programme · The single source of truth per book, and the contract for patches, the validator, and assembly**
*Version 1.0-draft (freezes with Principal approval together with Master Guide v1.0) · July 2026*

## §0 Design rules
1. **One JSON per book** (`support-book_C1-BAN.json`). It is the only artifact that travels; chats are disposable. Unlike the storybook pipeline, prompts live **inside** the image slots of this same file (one-file model — fewer moving parts for MERGE chats); a slot's `prompt` stays `""` until its PROMPTS task fills it.
2. **Per-পাঠ, not per-page.** Textbooks vary in length; the লesson (পাঠ) is the unit of work, review, and merge.
3. **Blocks carry provenance.** Every text block declares whether it is NCTB's (`source: "nctb"`) or school-written/edited (`source: "school"`), and whether it is oral or decodable. The letter audit keys off exactly this.
4. **Script guard everywhere:** every string field in the file — Bengali (U+0980–09FF incl. ০–৯, ৳) + danda ।॥ + ZWNJ/ZWJ, Basic Latin + Latin-1, dashes/curly quotes/ellipsis. No Arabic script, no emoji, no symbol glyphs. (Rendering-pipeline constraint; honorifics transliterated or in Bangla.)

## §1 Top level
```json
{
  "schema_version": "1.0",
  "book_id": "C1-BAN",
  "class": 1,
  "subject": "BAN",
  "mode": "R",
  "title_bn": "আমার বাংলা সহায়িকা — প্রথম শ্রেণি",
  "base_nctb_print_year": 2026,
  "has_text_en": false,
  "status": "ledger-approved",
  "front_matter": {
    "included": ["সূচিপত্র"],
    "omitted": [
      { "item": "জাতীয় সংগীত pages", "reason": "SB-016" },
      { "item": "জাতীয় পতাকা spec page", "reason": "SB-016" }
    ]
  },
  "lessons": [ /* §2 — one object per পাঠ, in NCTB order */ ],
  "version_log": [
    { "v": "0.1", "date": "2026-07-XX", "change": "Ledger import", "by": "MERGE chat / Principal gate" }
  ]
}
```
Field notes: `mode` ∈ {"R","C"} (Mode-C books never contain `action: "replace"` — validator enforces). `status` ∈ the Master Guide §8 flow. `has_text_en: true` for English books (then `text_en` is the primary layer and `text_bn` optional).

## §2 Lesson object (one per পাঠ)
```json
{
  "lesson_no": 40,
  "nctb_title_bn": "মামার বাড়ি",
  "nctb_pages": [57, 58],
  "genre": "কবিতা",
  "competency_codes": ["১.১", "১৬.২"],
  "outcome_codes": ["১.১.১", "১৬.২.১"],
  "action": "replace",
  "c_codes": ["C-05"],
  "severity": "S3",
  "status": "content-draft",
  "blocks": [ /* §3 */ ],
  "image_slots": [ /* §4 */ ],
  "nctb_omitted": [],
  "bw_treatment": "native_safe",
  "reviewer_signoff": { "by": null, "date": null, "checklist_passed": false },
  "notes": ""
}
```
Field notes: `genre` comes from the **TG-Reconciliation corrected tag set** (never the raw skeleton). `action` ∈ {retain, retain-curated, replace} (README §3.2 / D-008). `severity` present when action ≠ retain: retain-curated → S1|S2 (Mode-C: S1 only), replace → S3. `nctb_omitted` lists any NCTB element dropped inside a kept পাঠ (e.g., L2's flag drawing → `{ "item": "flag drawing", "reason": "D-012" }` while the শাপলা tracing stays). Every lesson from the NCTB book appears — a fully skipped পাঠ is still a lesson object with `action: "retain-curated"` and its omission recorded, so the compliance map stays complete. **`reviewer_signoff`** carries the single content sign-off (D-003, replacing the discarded ledger): `by` (reviewer), `date`, `checklist_passed` (boolean) — set true only when the teacher-reviewer's per-পাঠ checklist (README §7) passes. **`bw_treatment`** resolves how the পাঠ renders in the always-on bw-photocopy edition (D-016): ∈ {`native_safe`, `redesigned`, `print_only_omit`}. `native_safe` = the পাঠ has no colour-dependent pedagogy and renders in B/W as-is (the default). `redesigned` = colour-coded NCTB pedagogy has been replaced with a B/W-safe scheme (pattern/outline/shading) that the B/W edition renders. `print_only_omit` = the colour pedagogy is irreducible; the পাঠ is **omitted from the bw-photocopy edition** and carries a teacher note pointing to the colour master / NCTB original. The assembly validator red-fails a book whose bw-photocopy edition contains an unresolved colour-pedagogy page (i.e., colour-dependent content still marked `native_safe`). The old `brief_ref` field is removed (briefs are retired); the compliance map is derived from these lesson fields, not from a separate ledger.

## §3 Text block
```json
{
  "id": "L040-b02",
  "type": "poem",
  "source": "school",
  "edited": true,
  "oral": false,
  "text_bn": "…",
  "text_en": null,
  "source_note": null,
  "style_profile": "chhora-swarabritta",
  "layout_hint": "verse-center"
}
```
- `type` ∈ {heading, instruction, oral_text, decodable_text, poem, rhyme, story, dialogue, word_list, exercise, fill_blank, matching, writing_line, tracing_ref, table}.
- `source` ∈ {"nctb","school"}; `edited: true` on any school-written or school-modified text. **Letter-audit rule:** audit runs where `edited == true` AND `oral == false` AND book is C1–C2 BAN (MG §4.3/§6.4). NCTB-original text (`source:"nctb", edited:false`) is exempt.
- `oral: true` marks শুনি-ও-বলি / teacher-read content (exempt from letter audit, still curated).
- `source_note`: required (grey warning if absent) on any block whose content is an Islamic narrative — brief, e.g., `"সহিহ বুখারি-র প্রসিদ্ধ ঘটনা (রিভিউয়ার যাচাই করুন)"`. Reviewer resolves at checklist (SB-018).
- `style_profile`: optional pointer into `writing_style.md` for replacement verse/story blocks.

## §4 Image slot
```json
{
  "id": "L040-img-01",
  "scene_description": "গ্রামের পথে আম কুড়ানো — objects-first: ঝড়ে পড়া আম, ঝুড়ি",
  "image_class": "object",
  "action": "substitute_objects",
  "contains_living_being": false,
  "compliance_note": "object-only slot",
  "photocopy_safe": true,
  "refs": [],
  "prompt": "",
  "aspect": "4:3",
  "status": "draft"
}
```
- `image_class` ∈ {object, narrative_figure, animal_story, diagram, photo_replace, tracing_asset} — mirrors the MG §5 doctrine rows.
- `action` ∈ {substitute_objects, generate_stripe, redraw_schematic, keep_nctb, omit, vector_asset}.
- `contains_living_being` mandatory boolean; `generate_stripe` requires `true` + a real `compliance_note` (where the programmatic stripe lands / what stays clear). **No stripe language ever in `prompt`.**
- `refs`: filenames in `refs/school/` (cast reference sheets); required non-empty when the recurring cast appears; empty for object-only slots. Cast scenes obey the same-gender rule (SB-022) — enforced at PROMPTS review, not by the validator.
- `tracing_asset` + `vector_asset` = letter-tracing pages: rendered from vector assets at assembly, never AI-generated; `prompt` stays `""` permanently.

## §5 Patch file (what CONTENT/LEDGER/PROMPTS/MANIFEST chats emit)
```json
{
  "schema_version": "1.0",
  "book_id": "C1-BAN",
  "patch_id": "patch_C1-BAN_L040_CONTENT_v1",
  "task": "CONTENT",
  "lessons": [ /* complete lesson objects, replacing by lesson_no */ ]
}
```
**Merge rule (MERGE chat):** a patch replaces each listed lesson object wholesale by `lesson_no` (no field-level merging — the patch carries the complete lesson). MERGE chat then runs the validator on the merged book file and emits the report + updated `support-book_<ID>.json`. Top-level fields change only via a `task: "ADMIN"` patch gated by the Principal.

## §6 Companion data file — letter inventory (C1–C2 BAN)
`letter_inventory_C1-BAN.json` — machine form of Master Guide Appendix A:
```json
{
  "book_id": "C1-BAN",
  "cumulative_after_lesson": { "10": ["অ","আ"], "19": ["অ","আ","ই","ঈ","উ","ঊ","ঋ","এ","ঐ","ও","ঔ","ক","খ","গ","ঘ","ঙ"], "…": ["…"] },
  "kar_after_lesson": { "21": ["া"], "22": ["া","ি","ী"], "…": ["…"] },
  "conjunct_whitelist_by_lesson": { "45": ["প্ত","ট্র","ঙ্গ","স্প","ক্র"], "49": ["ন্দ"], "51": ["দ্দ"], "52": ["স্ত","ক্ত","দ্ধ","ম্ব","ষ্ট"] }
}
```
Audit algorithm: normalize the block's `text_bn` → strip whitespace/punctuation/danda → decompose into letters + কারচিহ্ন + conjunct clusters → every unit must be ∈ cumulative sets for that `lesson_no` (conjuncts ∈ whitelist entries with key ≤ lesson_no). Any miss = **red**, reported as {lesson, block id, offending unit, first-taught-at}.

## §7 Validator checks mapped to fields (README §6 ↔ schema)
| README §6 check | Keys inspected | Level |
|---|---|---|
| 1 JSON/version/id | `schema_version`, `book_id` (book + every patch) | red |
| 2 Lesson inventory & flags | `lessons[*].lesson_no` complete/ordered; one valid `action` each; Mode-C ⇒ no `replace`, severity ≤ S1 | red |
| 3 Codes present | `competency_codes`, `outcome_codes` non-empty per lesson | red |
| 4 Letter audit | blocks where `edited && !oral`, class 1–2 BAN, vs companion file (loaded only for C1–2 BAN, skipped elsewhere) | red |
| 5 Genre tag | `genre` ∈ corrected tag set on every `replace` lesson | red |
| 6 Slot booleans | `contains_living_being`, `photocopy_safe` on every slot | red |
| 7 Source note | `source_note` on narrative blocks | **grey** |
| 8 Script guard | every string in file | red |
| 9 No stripe language | `image_slots[*].prompt` ∩ forbidden strings = ∅ | red |
| 10 Compliance map derivable | every lesson has codes + action + `nctb_pages` | red |
| 11 B/W edition complete | no lesson with colour-dependent pedagogy left `bw_treatment:"native_safe"`; `print_only_omit` lessons carry a teacher note | red (at assembly) |
| — refs exist | `refs[*]` present in `refs/school/<class>/` | grey at merge, red before Images |
| — prompts filled | `prompt` non-empty on non-vector slots | grey at merge, red before Images |
| — signoff (informational) | `reviewer_signoff.checklist_passed` — not a validator red-check; the reviewer/Principal gate reads it before assembly release | info |

## Version log
| v | Date | Change | By |
|---|---|---|---|
| 1.0-draft | 2026-07 | Initial schema: one-file model (prompts in slots), per-পাঠ lessons, provenance-carrying blocks (`source`/`edited`/`oral`/`source_note`), doctrine-mapped image slots, patch format + wholesale-by-lesson merge rule, letter-inventory companion file + audit algorithm, validator↔field map. | Claude (draft); Principal (freeze pending) |
| 1.1-draft | 2026-07 | Ledger discarded (D-003): added `reviewer_signoff` {by, date, checklist_passed} to the lesson object as the single content sign-off; removed vestigial `brief_ref`; ref paths namespaced by class (`refs/school/<class>/`); letter audit noted as C1–2 BAN only (data-file-driven, D-004); MG references re-pointed to README/D-series. | Claude (draft); Principal (freeze pending) |
| 1.2-draft | 2026-07 | Added `bw_treatment` {native_safe, redesigned, print_only_omit} to the lesson object for the always-rendered bw-photocopy edition (D-016); added assembly check 11 (B/W edition completeness). | Claude (draft); Principal (freeze pending) |
