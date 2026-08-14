# PROPOSAL — AGENTS.md §12, `_inbox/` — staging and classification

**STATUS: DRAFT. NOT ADOPTED. NOT self-adoptable.**
Written under Principal ruling (1) of the unification session-1 paste-back, which directed a new
AGENTS.md section rather than a `SOURCE_POLICY` §8, and directed that it be drafted and held.

**On adoption:** it becomes AGENTS.md **§12**, takes the next free CD number — **the one after
CD-084**, verified at source at drafting and re-verified at adoption (AGENTS.md §4) — and this file
is deleted. Until then nothing in it is in force, and the classification performed in unification
session 1 was performed **under this draft held as draft**, which is recorded in that session's
report rather than claimed as compliance.

*The number is named by its predecessor rather than written out, because writing the successor
token here would make this file cite a decision row that does not exist yet — a phantom citation
`canon_check.py`'s CD-CITE check correctly FAILs. It did, on this file's first draft. Same trap as
CD-080(e).*

---

## 12. `_inbox/` — staging and classification

`_inbox/` is the repo's single staging area. It is **gitignored**, so anything in it exists on one
machine only; an agent on another device cannot see it and **stops rather than improvising**
(the failure recorded at CD-026).

### 12.1 What may be staged

Anything the Principal puts there. In practice four classes, and the class decides the destination:

| Class | Examples | Destination |
|---|---|---|
| **Source scans** | NCTB textbook PDFs, OCR drafts staged beside them | governed by `canon/sources/SOURCE_POLICY.md` §2.1 and §7.14 — **this section does not touch them** |
| **Canon references** | LOCKED REF files, policy documents several workstreams cite | `canon/` — the subtree that already holds that kind of authority; a REF file to `canon/refs/` with a `canon/refs/MANIFEST.md` row |
| **Workstream registers** | `PROJECT00_*`, `PROJECT04_*` decision logs, READMEs, TODOs | the owning `workstreams/<name>/`; read-only imports to its `references/` per CD-034 |
| **Assets** | fonts, images, spreadsheets consumed by a tool | `tools/` beside the tool that consumes them, with a `tools/MANIFEST.md` row |

**SOURCE_POLICY §2.1 governs scans and is not stretched to cover the other three.** It is written
about photographing a printed book; a policy import is not that, and reading it as though it were
is how a rule ends up governing something it never mentioned.

### 12.2 Who classifies

**The agent classifies; the Principal approves the destination for anything that is not obvious.**
Classification is a proposal like any other (AGENTS.md §2 — the agent never self-approves).

### 12.3 A file that cannot be classified is reported, never moved

If a staged file matches no class, or matches two, or its identity cannot be verified at source —
**it stays in `_inbox/` and is reported.** A guess that lands in `canon/` is worse than a file left
staged, because the guess acquires the authority of its new location and the next session reads it
as settled.

**Report, do not move, in particular when:** the file's own header names a different ID than its
filename · the set is partial against the manifest it belongs to · two staged files claim the same
ID · the file is a register whose owning workstream does not exist yet.

### 12.4 Duplicates of existing canon are reported for deletion, never silently overwritten

Before moving anything into `canon/`, the agent checks whether canon already holds it, **by hash,
not by filename** — the unification import found five byte-identical duplicates whose names
matched and two whose names did not.

- **Byte-identical to a canon file** → the staged copy is **redundant**. The agent **reports it,
  with the md5 of both sides, and deletes only on approval** (AGENTS.md §9's deletion rule applies
  unchanged: state the reason in chat first).
- **Same ID, different bytes** → **stop.** This is a version question and it is the Principal's.
  Never overwrite; never assume the staged copy is newer because it was staged later.
- **Already in canon under a different name** → the manifest row points at the **existing** path.
  **No second copy is made inside `canon/`** — that is precisely what §8 forbids, and a duplicate
  inside canon is invisible to `canon_check.py`'s NO-COPY check, which only looks *outside* canon.

### 12.5 What leaves `_inbox/` leaves it completely

A classified file is **moved, not copied**. A copy left behind becomes a second source of truth
that no gate compares against the first.

### 12.6 The gate

`python tools/audits/canon_check.py` runs after any `_inbox/` classification that touched `canon/`,
and its verbatim output is pasted before the work is called done (AGENTS.md §5).
