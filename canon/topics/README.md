# canon/topics/

The **vertical topic map** — which topic each subject teaches, and how it deepens across classes.

- `LOCKED_REF-19_Vertical_Topic_Progression_Map_v1_10.md` — canon by **CD-043**, imported
  2026-08-09, sha256 `43a4d837…d837a`. **READ-ONLY and supersede-only**: it is a LOCKED Project-00
  artifact and is never edited here. A newer version replaces it and the supersede is a CD row.
- Cited, never copied (AGENTS.md §8).

## What it does and does not settle

**Settles:** the canonical topic **slugs** — `BAN-POEM`, `ENG-SENTSTR`, `MATH-FRACTION` and so on.
121 of them across five subjects. These are the values `ref19_topic_id` takes in a Hub-bound
question payload, and the harness hard-validates against them.

**Does NOT settle:** the `TOP-<SUBJ>-C<n>-##` **numbers**. Verified at source on import — the file
contains **zero** `TOP-` strings and **no topic id carries a numeric suffix** (CD-043). The numbers
are a separate scheme owed to REF-07 §3.5, which is **not yet in this repo**; until it arrives the
numbering authority is the attested usage in
`workstreams/question-banks/references/PROJECT04_DECISIONS.md` (CD-043, residual row PENDING-P-008).

Do not read a `TOP-` number off this file. It has none.
