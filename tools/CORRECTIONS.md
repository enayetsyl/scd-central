# CORRECTIONS.md — tools lane ledger (append-only, AGENTS.md §6)

<!-- CD-124: the prefix is what rows in this file ALREADY mint; the lane identifies this ledger. Declared now, renumbered per lane at close — no row is renumbered by this line. -->
<!-- ledger-prefix: TOOLS-CR -->
<!-- ledger-lane: tools -->

Agent errors in repo-wide tooling: gates, harnesses, render and audit scripts. **Rows are never
edited or deleted** — a wrong row is corrected by a new row citing it.
3+ occurrences of one shape → mark **PATTERN** → propose promotion to an executing gate.

**Why this file exists and why it has its own prefix — `TOOLS-CR-###`, starting at 001 (Principal
ruling 2026-08-14, session-2 ruling 4).** Per-lane prefixes are already the pattern
(`QB-CR-###` in question-banks, bare `CR-###` in the Math lane), and **two ledgers sharing one
number space across disposable sessions is CD-034's disease in a new place**. A tooling defect
belongs to no extraction lane; this file is its home, and its rows are numbered from 001 in a
space nothing else writes into.

**The renumber corrected a live collision, which is why it is recorded and not just done.** This
file's first row was filed as **`CR-012`** on the stated ground that *"CR-012 was verified free at
source … no `CR-012` token existed anywhere in the repo."* **That was false at source.**
`canon/_wip/c5-math/CORRECTIONS.md` already carried its own **CR-012** (the pair-general band-crop
rule, 2026-08-12, commit `5634a5f`), and `canon/_wip/c5-math/C5_MATH_Source_06.md` cites it three
times. **Two different rows carried one number for two days, and three live citations pointed at
the Math one.** The Math lane's CR-012 keeps the number — it was written first and it is the one
cited — and **the Math lane is not touched by this correction**; only this file's row is renumbered.

| TOOLS-CR | Date | Where | What was wrong | What was done |
|---|---|---|---|---|
| TOOLS-CR-001 | 2026-08-14 | `tools/audits/canon_check.py` · `parse_ref_manifest()` / `check_ref_citations()` | **The REF-CITE resolver normalised REF ids with `int()`, and `int("01") == int("1")`.** P00's **REF-01** and the retired support-book **REF-1** therefore collapsed to the same key. Because the current-series set was built first, it swallowed the alias set, and the `raw in alias` branch became unreachable. **Effect: every retired support-book citation silently stopped being censused while the gate still printed `CLEAN`.** No FAIL, no WARN, no visible symptom — the check reported success for a population it was no longer looking at. **This is the REF-01/REF-2 collision reappearing inside the gate built to police that exact collision.** | Keys are now the **raw string the register writes**, never integer-normalised; the two series are told apart by the **width** they are written at (P00 zero-padded two-digit `REF-01…REF-26`; retired support-book bare single-digit `REF-1`, `REF-2`), which is the same property that makes them two series. Reason recorded in the function docstring so a later reader does not "tidy" the normaliser back in. **Caught by the seeded census test, which existed only because the census was built with a seed in both directions** — the clean-repo run was green throughout. |

| TOOLS-CR-002 | 2026-08-14 | `tools/hub-export/validate_import.py` · `REF19_SLUGS_DEFAULT` | **A FIFTH instance of the promoted PATTERN, found by building the gate that reads the same register — and this one is in a LOCKED-adjacent constant.** `canon/topics/LOCKED_REF-19_…v1_10.md` carries **121 backticked slugs**, two of which are three-segment: **`MATH-ADDSUB-REL`** and **`MATH-MULDIV-REL`**. The harness's auto-extracted copy also holds 121 — but holds **`MATH-ADDSUB`** and **`MATH-MULDIV`** instead. **The extractor's regex stopped at the second hyphen, and the truncated forms exist nowhere in REF-19.** Set difference, both directions, measured: `artifact − harness = {MATH-ADDSUB-REL, MATH-MULDIV-REL}`, `harness − artifact = {MATH-ADDSUB, MATH-MULDIV}`. **This is `normalising an ID discards the thing that makes it an ID` exactly** (CD-088) — the discarded form is a hyphenated segment, the same class of loss as CD-088(b)'s scheme prefix. **And it compounds:** `LOCKED_QuestionPayload_Schema_v1.json`'s `ref19_topic_id` pattern is `^(BAN\|ENG\|MATH\|SCI\|BGS)-[A-Z0-9]+$` — **single hyphen only** — so the two real slugs are *unrepresentable in a payload*, and the only values that validate are the two truncations that do not exist. Two canon-layer artifacts disagree about what a REF-19 id is. | **Nothing was changed.** The REF19-SLUG gate in the merged `gates.py` (CD-123) reads the **LOCKED artifact**, not the derived copy (CD-011: a registry is written from the artifact, never from a summary — the same ground QB-CR-007 refused to build canon on this constant), so it accepts the two real slugs and would reject the truncations. **The harness is vendored under a LOCKED contract and is supersede-only (CD-013); the schema pattern is LOCKED.** Neither is the agent's to edit and neither was edited. Raised as **⚑ PENDING-P-029** — this is a Principal ruling about which of two canon artifacts is right, and it is upstream of both. |
## PATTERN candidates

**⚑ PATTERN CANDIDATE — `normalising an ID discards the thing that makes it an ID`.**
Named by the Principal on this file's first row (2026-08-14, then numbered `CR-012`, now
**TOOLS-CR-001**). **PROMOTED TO PATTERN 2026-08-14 — four instances on the record.** The gate is
proposed, not built (session-2 instruction: gates are session 3).

| # | Instance | Shape |
|---|---|---|
| 1 | **QB-CR-008** — `TOP-BAN-C5-11` read off MarkLogic spine slot `S11`. The `S-` and `TOP-` schemes are unrelated and collide at 11 by coincidence. | Two ID spaces treated as one because a *rendering* of them matched |
| 2 | **TOOLS-CR-001** — `REF-01` and `REF-2` collapsed by `int()`. | Two ID spaces treated as one because a *normalisation* of them matched |
| 3 | **CD-034 ⚑** — bare `D-0NN` across two registers: `D-049` appears bare 65× as a master row, `D-038` bare 33× *and* as `D-PROJ03-038` 10×. **The same bare string denotes different rows in different places.** | Two ID spaces treated as one because a *truncation* of them matched — the scheme segment (`PROJ03`) is the distinguishing form, and writing the number bare discards it |
| 4 | **This file's own renumber** — `CR-012` filed here while `canon/_wip/c5-math/CORRECTIONS.md` already held a different `CR-012`, on a verification that said the token was free. | Two ID spaces treated as one because *no prefix distinguished them at all* — the shared bare `CR-###` space is the collapse, made permanent |

**Why instance 3 completes it rather than merely resembling it.** The family was stated as: *the
distinguishing information lived in the **form** of the identifier — its scheme prefix, its
zero-padding — and a step that looked like harmless tidying threw that form away.* `D-PROJ03-038`
written as `D-038` throws away a **scheme prefix**, which is the first item on that list. CD-034
recorded it as a flag on a corpus convention rather than as an agent error, which is exactly why
it was not counted the first time; **the shape does not care who performed the tidying.**

**Instance 4 is the same shape reaching the ledgers themselves**, and it is the one that did
measurable harm: two live rows under one number for two days. It is also the instance CD-034
predicted in as many words.

**Proposed gate on promotion (NOT built this session).** Two checks, because the pattern now has
two faces:
1. **Source lint** — forbid `int()` on any captured id group in `tools/audits/*.py` and
   `workstreams/*/audits/*.py`; require comparison against the raw captured string.
2. **Ledger-collision check** — every corrections ledger declares its prefix in its header, and no
   `<PREFIX>-###` token may resolve to rows in two files. This is the check that would have caught
   instance 4 at the moment it was written, and it is the one the repo does not have.

**The family resemblance, stated so the third instance is recognisable:** in both, the distinguishing
information lived in the **form** of the identifier — its scheme prefix, its zero-padding — and a
step that looked like harmless tidying threw that form away. It is the same shape CD-083 named as the
canon's recurring failure (`CD-070` substring-vs-token, `CD-077` presence-vs-correctness): **a rule
written in a coarser unit than the one it is enforced in passes on paper and leaks in practice.**

**Proposed gate on promotion:** a lint over the audit scripts forbidding `int()` on any captured id
group, requiring comparison against the raw captured string. Not built — a two-instance pattern is
proposed, not promoted (AGENTS.md §6).
