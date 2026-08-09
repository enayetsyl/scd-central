# LOCAL.md — support-books (সহায়িকা)

Read AFTER root AGENTS.md. May tighten the protocol, never loosen it.

## Identity

Islamised NCTB support books (সহায়িকা) — one book per class-subject, lesson-by-lesson, adapting
NCTB content under the curation policy while keeping curriculum alignment. Build wave C1–C5
(2026); pilot C1 বাংলা → English → গণিত. Active book: **C1-BAN**, 54 পাঠ.

## Status & provenance

**LIVE** (2026-08-09). Imported from the SB-Governance and SB-P Production projects: the 54-পাঠ
book JSON, five governance files, the letter inventory, 55 lesson patches, the skeleton and
TG-reconciliation references, the word map, the compliant image set, and three validators.

## Decision series

**D-###**, log at `DECISIONS.md` here. **Imported at D-019** (highest row present).
⚠️ `REGISTRY.md` said "at D-021+" — the imported log stops at D-019. See STATE.md Q-3.

## Canon citations used

- `canon/islamic-curation/REF-1_Curation_Policy.md` — the 19 C-codes and the three tags.
- `canon/names/REF-2_Content_Register.md` — the C1 cast pool and spelling house-style.
- `canon/image-rules/IMAGE_RULES.md` — living-being doctrine (CD-007).
- `canon/language/LANGUAGE_RULES.md` — §2 numerals, §4 সাধু/চলিত, §7 script guard.

Cite, never copy (AGENTS.md §8). The local `governance/` files are the workstream's own process
rules; where they overlap canon, **canon wins**.

## Artifacts & naming

| Path | Holds |
|---|---|
| `books/<BOOK-ID>/support-book_<BOOK-ID>.json` | the book — merge target |
| `books/<BOOK-ID>/patches/` | `patch_<BOOK-ID>_L###_CONTENT_v#.json`, one per lesson |
| `books/<BOOK-ID>/whitelists/` | conjunct-whitelist candidates + approved amendments |
| `books/<BOOK-ID>/reference/` | skeleton, TG reconciliation, word map — read-only provenance |
| `books/<BOOK-ID>/reports/` | validator reports |
| `books/<BOOK-ID>/images-compliant/` | post-stripe image set |
| `governance/` | README, SETUP, ASSEMBLY, SCHEMA, setup notes |
| `_wip/` | merge candidates and session state; nothing here is authority |

## Gates

`python3 audits/gates.py` — wraps the vendored SB validator and runs two stages:

1. **Seeded-error selftest** first. A validator that cannot catch a planted error is not
   evidence, so the instrument is proven before the book result is believed.
2. **The 10 checks** over the book JSON.

Exit 0 = no red. **A red returns the lesson to step 3 and does not merge** (governance README
§3.2 step 8). Human gates that no script replaces: the Principal's step-2 ruling on action flags,
and the **আলিম-lane** reviewer sign-off (`REVIEW_QUEUE.md`).

## Operator workflow

The nine-step per-chapter loop is in `governance/README.md` §3.2 and is load-bearing — each step
gates the next. Steps 7–9 (JSON → validator → merge) are the agent's; steps 2 and 5 are the
Principal's; the reviewer lane signs off separately.

**Merge after every chapter.** Never bank several unmerged lessons — a lost session then costs
at most one chapter.

## Session-end sync

"save state and sync" = update `_wip/STATE.md` → append root `SESSION_LOG.md` → commit → push.
Additionally: any validator run quoted as evidence goes to `books/<BOOK-ID>/reports/` (CD-024).
