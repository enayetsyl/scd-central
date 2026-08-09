# SETUP — Per-book setup
*What happens once, before a book's chapter loop begins: importing and cleaning the TG + skeleton, and generating cast references. Companion to the README (§3.1) and to `ASSEMBLY.md` (the render tail). v1.0-draft · July 2026*

> **Symmetry.** SETUP.md is the front of a book's life (import + refs); the nine-step chapter loop (README §3.2) is the middle; `ASSEMBLY.md` is the end (render). This file specifies only the once-per-book setup.

---

## §1 Import and clean the TG + skeleton

### 1.1 What this step is (and isn't)
The TG Reconciliation and skeleton were produced in the earlier analysis project and currently live there. Setup **imports** them into Production and **cleans** them. The purpose is *not* cosmetic and *not* pedagogical:

- The TG's pedagogical payload — genre tags and শিখনফল/যোগ্যতা codes — arrives **final and corrected** (the raw-skeleton tags were already reconciled; README §4.1). Setup treats it as **read-only**. Setup never edits, re-tags, or re-codes.
- The real risk cleaning addresses is **chat contamination**: old-flow framing left in a reference file (references to a LEDGER chat, an আলিম sign-off column, a two-file schema, SB-series decisions, or another project's cross-references) can mislead a production chat into acting on retired instructions. Cleaning removes that.
- Cleaning is also the act that gives the file **Production citizenship**: the cleaned copy lives in Production; the original stays archived in the source project. After this step, no production chat reaches across the project boundary for it (the cross-project reference the architecture forbids ends here).

### 1.2 Never touch (the protected payload — copied verbatim)
- Every পাঠ's শিখনফল/যোগ্যতা codes.
- The corrected genre tags.
- The letter-sequence / কারচিহ্ন / conjunct data the letter inventory is built from (C1–2 বাংলা).
- Flexibility-tier and transformation notes that flag what a পাঠ allows.
These are the reason the TG exists. They are preserved exactly.

### 1.3 Remove or re-point (the framing)
- **Foreign decision-series references** (SB-xxx and any other project's IDs): re-point to the D-series equivalent where one exists, otherwise remove. Never leave a dangling foreign ID.
- **Old-flow instructional framing**: LEDGER chat, per-পাঠ brief, separate MERGE chat, আলিম sign-off column, verification gate, two-file/prompts-file schema language — remove or update to the current model.
- **Content scoped to other books**: anything not about the book being set up.
- **Commentary that assumed the retired flow**: reword to the current flow or drop.

### 1.4 Verify (cheap, mandatory)
Because the payload is read-only, verification is only *"did I preserve it"* — a **codes-count reconciliation** against the retained original:
- The cleaned file must contain the **same set of শিখনফল/যোগ্যতা codes, per পাঠ**, as the original — same count, same codes, same পাঠ order.
- Genre tag present and unchanged on every পাঠ that had one.
- Any mismatch = stop and fix; a dropped or altered code is the one error this step can silently introduce, so it is the one thing checked. This is the setup step's equivalent of the seeded-error test.

### 1.5 Output
- Cleaned `TGReconciliation` + `skeleton` saved to Production, named for the book (`<CLASS>-<SUBJ>`).
- Original left untouched in the source project (the diff reference).

---

## §2 Cast reference images

### 2.1 Generate only what is absent (per class, D-013)
The recurring cast is **per class**, generated **once at that class's first book** and reused across that class's subjects. At setup, generate only refs that do not already exist:
- The **class cast** (four children) if this is the class's first book.
- Any genuinely **book-local** recurring figure not covered by the class cast.
Never regenerate an existing class cast — that is the discipline that keeps a child meeting the same four faces across their year.

### 2.2 Rules the refs must satisfy
- Names come from that class's Name Bank pool (REF-2 §4); the four cast names are reserved within the class.
- **Same-gender scene rule** (C-01): cast interactions are same-gender.
- One cast child carries a **mobility aid** (mirroring NCTB's inclusive cast).
- Dress/modesty per the image doctrine (README §5): adult male full beard + hem above ankle; female full coverage, face + hands only.
- Reference images are **canon** and attached to every generation; they override text.
- Saved to `refs/school/<class>/`.

### 2.3 Approval
Cast refs are approved before the chapter loop uses them — a wrong-once cast propagates through every image in the book.

---

## §3 When setup is complete
A book is ready for its chapter loop when: cleaned TG + skeleton are in Production and pass the codes-count reconciliation; the class cast (and any book-local figures) exist in `refs/school/<class>/` and are approved; and, for C1–2 বাংলা, the `letter_inventory_<CLASS>-<SUBJ>.json` exists (built from the TG's letter-sequence data) and the validator has passed its seeded-error test against it.

## Version log
| v | Date | Change | By |
|---|---|---|---|
| 1.0-draft | 2026-07 | Initial setup spec: import-and-clean TG/skeleton (payload read-only, framing removed/re-pointed, codes-count verification, Production citizenship), cast-ref generate-if-absent rules, setup-complete gate. | Claude (draft); Principal (approval pending) |
