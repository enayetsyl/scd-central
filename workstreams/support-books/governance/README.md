# README — Support-Book Programme
*Orientation + operating rulebook. Read this first in any new chat that needs project context. v2.0 · July 2026*

> **v2.0 note.** This README replaces both the old README (v1.0) and the retired `school-support-book-master-guide.md`. The Master Guide's operative rules are absorbed here and into the founding decisions in `DECISIONS.md`. The programme's production flow was redesigned; the content and posture rules are unchanged and carried forward as founding decisions D-001…D-0xx. Curation taxonomy lives in `REF-1`; names and per-class cast in `REF-2`; the field-by-field JSON contract in `SCHEMA_support-book_v1.md`.

---

## §1 What we are doing (one paragraph)
This school produces internal, free **support books** (সহায়িকা) parallel to NCTB textbooks, preserving every NCTB শিখনফল while adapting content and imagery to the school's values. Classes 1–4 and 6–7 run **Mode-R** (selective genre-matched replacement, per-পাঠ action flags); classes 5, 8, 9–10 run **Mode-C** (exam-fidelity: image curation and light text touches only, no replacement writing). The school grows one class per year; books are built one year ahead. The support book is presented — and genuinely functions — as সহায়িকা: the NCTB book keeps a real scheduled role (homework, fluency reading), and our books cross-reference NCTB page numbers.

---

## §2 Structure — two projects, five governance files

| Project | Holds |
|---|---|
| **Governance** | This README, `DECISIONS.md`, `SCHEMA_support-book_v1.md`, `REF-1_Curation_Policy_v1.md`, `REF-2_Content_Register_v1.md`. Two spec companions: `SETUP.md` (per-book setup) and `ASSEMBLY.md` (render tail). |
| **Production (rolling)** | Working artifacts only: pruned TG reconciliations + skeletons for in-build books, cast reference images, book JSONs, patches, the validator script + per-book letter-inventory data files. Sources rotate — only in-build books' sources stay in knowledge. |

**The filesystem is the database.** The merged `support-book_<CLASS>-<SUBJ>.json` per book is the single source of truth. Chats are disposable; each chapter chat emits a patch that merges into the book JSON. No ledger file, no brief file, no separate MERGE chat — those are retired.

| Governance file | What it is |
|---|---|
| `README.md` | This file — orientation + operating rules (modes, flow, image doctrine, writing rules, validator profile) |
| `DECISIONS.md` | Append-only decision log (D-numbers). Founding entries carry the content/posture rulings |
| `SCHEMA_support-book_v1.md` | Field-by-field contract for the book JSON, patches, letter-inventory file, validator |
| `REF-1_Curation_Policy_v1.md` | Curation taxonomy: C-code table, severity scale, decision rules, retain/avoid lists |
| `REF-2_Content_Register_v1.md` | Name Bank (per-class pools), **per-class recurring cast**, story allocation map, word lists |

---

## §3 The production flow

### 3.1 Per-book setup (once per book)
Full spec: `SETUP.md`. In short:
1. Pick the book. Upload its TG Reconciliation + skeleton from the source analysis project.
2. **Import and clean** them into Production: the pedagogical payload (শিখনফল/যোগ্যতা codes, corrected genre tags, letter-sequence data, tier notes) is **read-only**; remove or re-point old-flow framing and foreign decision-series references (prevents a chat acting on retired instructions); verify by **codes-count reconciliation** against the retained original. The original stays archived in the source project.
3. **Cast reference images** — the recurring cast is **per class** (§3.4). Generate the class cast **once, at the first book of that class**, and reuse across that class's subjects. Generate only *absent* refs: the class cast if this is the class's first book, plus any book-local recurring figure. Never regenerate an existing class cast.

### 3.2 Per-chapter loop (the nine steps, in order)
One chapter per chat, or several chapters in one chat while context stays clean; a big chapter can take its own chat. The order is load-bearing — each step gates the next:

1. **Compliance map** — the chat produces the পাঠ's compliance row: শিখনফল/যোগ্যতা codes, proposed C-code(s), severity, proposed action flag, NCTB pages.
2. **Principal ruling** — the Principal approves the action flag and codes *before* any content is written.
3. **Content** — text generated only if the action requires it (`replace`/`retain-curated`); written inside all applicable rules (§4).
4. **Image prompt** — the chat writes image prompts only. **No stripe language ever in a prompt.**
5. **Image approval** — images are generated *outside this chat* (ChatGPT/Gemini) from the prompt, returned here, and checked against the image manifest (§5): dress rules, `contains_living_being`, and that no story-critical detail sits where the stripe will land. Unapproved images do not proceed.
6. **Image ref** — stripe/upscale/crop run *outside the chat* (software on local PC); the finished filename is recorded in the slot.
7. **JSON** — the chat emits the complete lesson object (all codes, action, pages, blocks, slots, `reviewer_signoff`), not just prose.
8. **Validator script (executed, not reasoned)** — the validator *script* runs on the merged-candidate JSON and returns a pass/fail report. A fail returns to step 3; it does **not** proceed to merge.
9. **Merge** — on pass, the lesson object merges wholesale-by-lesson into the book JSON. **Merge after every chapter** — never bank multiple chapters unmerged in one chat, so a lost chat costs at most one chapter.

Every পাঠ goes through all nine steps, including trivial `retain` পাঠ (they pass the map and validator trivially). Skipping the boring ones is how the compliance map develops holes.

### 3.3 The validator (one script, data-driven)
There is **one** validator script, not one per subject. Its checks are subject-agnostic (JSON valid, flags present, codes present, script guard, no stripe language, slot booleans, compliance map derivable). The **only** subject-specific check is the letter audit, which runs when the book is **Class 1–2 বাংলা** by loading that book's `letter_inventory` data file, and is skipped otherwise. Build the validator once, when the first letter-inventory file exists, and prove it with the **seeded-error test** (§6) before any chapter merges through it. The validator is production *tooling* (Claude Code / code execution), not a governance document.

### 3.4 The recurring cast (per class)
Each class has its own four recurring children, drawn from that class's Name Bank pool (REF-2 §4), generated once and reused across that class's subjects. A child meets the same four faces in বাংলা, math, and English of their year. Cast scenes are **same-gender** (no mixed-gender pairings); one cast child carries a mobility aid (mirroring NCTB's inclusive cast). Reference images are canon and attached to every generation. The **C1 cast** is উমর, আনাস, খাদিজা, ফাতিমা (ফাতিমা keeps the mobility aid); C2–C10 casts are named as each class is reached, from that class's pool.

---

## §4 Writing rules (Mode-R content only)

**4.1 Genre and meter.** Rhyme replaces rhyme, poem replaces poem, informational text replaces informational text. Genre tags come from the **TG Reconciliation**, never the raw skeleton. ছড়া replacements follow স্বরবৃত্ত (4-matra feet, stress foot-initial); read every refrain aloud before approval. Register matches the NCTB book's own rhythm — short, concrete, শিশুতোষ; QA reads replacement and original side-by-side. Word/line budget within ±20% of the NCTB original.

**4.2 Taught-letter constraint (Class 1–2 বাংলা decoding books only).** Applies to text the child must **decode** (পড়ি/লিখি); does **not** apply to শুনি-ও-বলি oral text (`oral: true`), which still stays simple. Replacement decodable text for পাঠ N may use only letters + কারচিহ্ন taught up to পাঠ N. **যুক্তবর্ণ rule B-1:** a পাঠ may use only the specific whole-unit conjuncts its own NCTB পাঠ introduces, or none — no systematic conjunct construction at Class 1. Enforcement is **mechanical**: the validator's executed letter audit red-fails any violation. Writers write inside the inventory; the validator is the net, not the method. (Inventory data: the book's `letter_inventory` file.)

**4.3 Islamic content.** Narratives (sirah, sahabi, hadith-anchored) stay within **famous, well-known narrations**; drafts carry a brief `source_note` and **flag uncertainty rather than filling gaps** — narration details are never invented. Review sits with the teacher-reviewer, who consults an আলিম where a source or creed question arises. No separate verification gate. No Arabic script in any JSON string (rendering constraint): honorifics transliterated or in Bangla; hadith as বাংলা অর্থ + citation.

**4.4 Names and settings.** Character names only from the Name Bank (REF-2). The per-class recurring cast uses approved reference sheets — canon images override text. Settings: home, মাদ্রাসা/school, bazaar, nature, village/river — Islamic household framing, consistent with the NCTB book's world.

**4.5 Protected content (never removed by curation).** The full NCTB decoding spine and শিখনফল-bearing exercise structures; factual national/civic history (মুক্তিযুদ্ধ, civic facts) per REF-1 C-18; the free-thinking strand (যোগ্যতা ১৬.২, একাকী চিন্তা, নিজের-মতো expression) — replacements must preserve the child's own-expression space; inclusive representation present in NCTB (the mobility-aid child).

---

## §5 Image doctrine (decision table)

> The white compliance stripe is applied **programmatically by software, post-generation, outside the chat**. It is **never** written into any prompt. Composition-for-the-stripe is steered only via the internal `compliance_note` field.

| Image class | Default action | Notes |
|---|---|---|
| Countable objects in exercises | **Substitute objects** — dates, books, boats, stars, lanterns | Objects-first is the programme default; cleaner than striping many small figures |
| Narrative/decorative illustration with human figures | Objects/scenery where the পাঠ allows; else generate with cast refs + programmatic stripe | `contains_living_being: true`; modest full-coverage dress (adult male full beard, hem above ankle; female full coverage, face+hands only) |
| Animals a story requires | Keep animal, stripe applied | Story-critical detail must not sit under the stripe — eyeball pass required at image approval |
| Pedagogically essential diagrams | Schematic/line redraw, no facial detail | Never stripe a diagram into illegibility — the শিখনফল wins |
| Photographs of people | Replace (scenery/objects/redraw) | Photos don't survive stripe or photocopy |
| **Prophets, angels, Sahaba** | **Never depicted** — scenery / objects / silhouette only | Absolute; applies to historical scenes too |
| National symbols (anthem/flag) | **Omitted from support books** | Students meet this in the NCTB book; factual মুক্তিযুদ্ধ/civic imagery retained per C-18 |

**Two print editions, both always rendered** from the same validated JSON (D-016): **print-colour** (colour, true white) and **bw-photocopy** (greyscale/line, true white, high-contrast, verified on the school's actual copier). Because the B/W edition must always work, image discipline stays live — all replacement art is high-contrast line-art-capable, and colour-dependent NCTB pedagogy gets a B/W-safe redesign. Each lesson's `bw_treatment` ∈ {native_safe, redesigned, print_only_omit} resolves how it renders in the B/W edition; an unresolved colour-pedagogy page fails the assembly validator. Full render process: `ASSEMBLY.md`.

The **image manifest** lives inside the `support-book.json` slots (no separate file): slot id · পাঠ · image class · action · `contains_living_being` · `compliance_note` · `photocopy_safe` · ref ids · status.

---

## §6 Validator profile (hard checks — red = blocked)

1. Valid JSON; `schema_version` exact; `book_id` consistent across files.
2. পাঠ inventory complete and in NCTB order; every পাঠ has exactly one action flag; Mode-C ⇒ no `replace`, severity ≤ S1.
3. Every পাঠ lists ≥1 যোগ্যতা and ≥1 শিখনফল code (from the TG Reconciliation).
4. **Letter audit** (C1–2 বাংলা only): all school-written decodable `text_bn` ⊆ taught inventory + B-1 whitelist — every field in a `replace` পাঠ and every `edited:true` field in a `retain-curated` পাঠ. NCTB-original and `oral:true` exempt.
5. Genre tag present on every `replace` পাঠ, from the corrected tag set.
6. Every image slot has `contains_living_being` and `photocopy_safe` (booleans).
7. Islamic-narrative blocks carry `source_note` — **grey warning** if missing (reviewer resolves; no lock).
8. Script guard: Bengali + Latin ranges only; no Arabic script, emoji, or symbol glyphs in any string.
9. No stripe-instruction strings in any image prompt.
10. Compliance map derivable: every পাঠ has codes + action + `nctb_pages`.

Grey (allowed at merge, required before images/assembly): missing prompts; missing image assets; `photocopy_safe` pending.

**Seeded-error test (per pilot book):** plant ≥3 deliberate violations (one letter-audit, one missing flag, one unverified anchor); the validator must catch all before the book counts as pipeline-proven.

---

## §7 Roles and gates

| Actor | Responsibility |
|---|---|
| Claude (production chats) | Drafts the compliance map, content, image prompts; runs the validator script; always flags uncertainty rather than resolving it silently. |
| Teacher-reviewer | Per-পাঠ checklist: genre ✓ · letter audit passed ✓ · শিখনফল coverage ✓ · source note checked ✓ · register vs NCTB (side-by-side) ✓ · images match manifest ✓ · photocopy check ✓. Consults an আলিম on source/creed questions. **Single content sign-off**, recorded in the lesson object's `reviewer_signoff` field. |
| Principal | Gates: per-chapter action-flag/code ruling → content approval → assembly release. Owns `DECISIONS.md` and the supersede protocol. |

**Folder tree per book:** `SCHOOL-BOOKS/<CLASS>-<SUBJ>/{json, images-raw, images-approved, images-compliant, pdf}` — separate root from the commercial product. **Product separation is absolute:** support books never enter the storybook sales catalog, storefront, or any commercial channel; separate folder roots; no exceptions.

**Status flow:** `content-draft → content-approved → images-approved → compliance-done → assembled → QA-passed`.

---

## §8 Annual cycle
- **January (NCTB new print):** Mode-R books — LO-level diff, patch only LO-changed topics. Mode-C books — full content-level diff (exam fidelity).
- **Year-round:** the 2026 wave builds C1–C5 (pilot first, then tier-batched); from 2027, build the next incoming class each year (C6 first — permanent one-year lead).
- **Each term:** risk-register review (posture verifiability · exam-class transition exposure 4→5, 7→8 · copyright status · NCTB churn exposure).

---

## §9 Current state (update each merge)
- Build wave: **C1–C5 (2026)** · pilot: C1 বাংলা → English → গণিত
- Active book: **C1-BAN**
- Books in flight: [list + status]
- Open items: build + seeded-error-test the validator (once the C1-BAN letter-inventory file exists) · generate + approve the C1 cast reference sheets · begin C1-BAN chapter loop

## Version log
| v | Date | Change | By |
|---|---|---|---|
| 1.0 | 2026-07 | Initial README. | Claude (draft); Principal |
| 2.0 | 2026-07 | Full rewrite. Absorbs the retired Master Guide. New nine-step per-chapter flow; ledger/brief/MERGE-chat retired; per-class cast; one data-driven validator; `reviewer_signoff` in JSON; lean five-file governance. | Claude (draft); Principal (approval pending) |
| 2.1 | 2026-07 | Two always-rendered print editions (print-colour + bw-photocopy, D-016); assembly spec `ASSEMBLY.md` added (shared-renderer-as-tool, D-017); `bw_treatment` per-lesson field. | Claude (draft); Principal (approval pending) |
| 2.2 | 2026-07 | Per-book setup spec `SETUP.md` added (import-and-clean TG/skeleton, codes-count verification, cast-ref rules; D-019); §3.1 expanded to point to it. | Claude (draft); Principal (approval pending) |
