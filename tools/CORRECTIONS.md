# CORRECTIONS.md — tools lane ledger (append-only, AGENTS.md §6)

Agent errors in repo-wide tooling: gates, harnesses, render and audit scripts. **Rows are never
edited or deleted** — a wrong row is corrected by a new row citing it.
3+ occurrences of one shape → mark **PATTERN** → propose promotion to an executing gate.

**Why this file exists and why it starts at CR-012.** The `CR-###` series is shared across lanes,
and until now its rows lived in the lane whose work produced them — most in
`canon/_wip/c5-math/CORRECTIONS.md`. **CR-012 was verified free at source** before this row was
written (that file records its own next-free as CR-012, and no `CR-012` token existed anywhere in
the repo). A tooling defect belongs to no extraction lane, and filing it in the Math lane's ledger
would have meant editing a lane this session was told not to touch. **The series continues; only its
home is new.**

| CR | Date | Where | What was wrong | What was done |
|---|---|---|---|---|
| CR-012 | 2026-08-14 | `tools/audits/canon_check.py` · `parse_ref_manifest()` / `check_ref_citations()` | **The REF-CITE resolver normalised REF ids with `int()`, and `int("01") == int("1")`.** P00's **REF-01** and the retired support-book **REF-1** therefore collapsed to the same key. Because the current-series set was built first, it swallowed the alias set, and the `raw in alias` branch became unreachable. **Effect: every retired support-book citation silently stopped being censused while the gate still printed `CLEAN`.** No FAIL, no WARN, no visible symptom — the check reported success for a population it was no longer looking at. **This is the REF-01/REF-2 collision reappearing inside the gate built to police that exact collision.** | Keys are now the **raw string the register writes**, never integer-normalised; the two series are told apart by the **width** they are written at (P00 zero-padded two-digit `REF-01…REF-26`; retired support-book bare single-digit `REF-1`, `REF-2`), which is the same property that makes them two series. Reason recorded in the function docstring so a later reader does not "tidy" the normaliser back in. **Caught by the seeded census test, which existed only because the census was built with a seed in both directions** — the clean-repo run was green throughout. |

## PATTERN candidates

**⚑ PATTERN CANDIDATE — `normalising an ID discards the thing that makes it an ID`.**
Named by the Principal on CR-012 (2026-08-14). **Two instances on the record, one more makes it a
PATTERN under AGENTS.md §6 and it goes to an executing gate.**

| # | Instance | Shape |
|---|---|---|
| 1 | **QB-CR-008** — `TOP-BAN-C5-11` read off MarkLogic spine slot `S11`. The `S-` and `TOP-` schemes are unrelated and collide at 11 by coincidence. | Two ID spaces treated as one because a *rendering* of them matched |
| 2 | **CR-012** — `REF-01` and `REF-2` collapsed by `int()`. | Two ID spaces treated as one because a *normalisation* of them matched |

**The family resemblance, stated so the third instance is recognisable:** in both, the distinguishing
information lived in the **form** of the identifier — its scheme prefix, its zero-padding — and a
step that looked like harmless tidying threw that form away. It is the same shape CD-083 named as the
canon's recurring failure (`CD-070` substring-vs-token, `CD-077` presence-vs-correctness): **a rule
written in a coarser unit than the one it is enforced in passes on paper and leaks in practice.**

**Proposed gate on promotion:** a lint over the audit scripts forbidding `int()` on any captured id
group, requiring comparison against the raw captured string. Not built — a two-instance pattern is
proposed, not promoted (AGENTS.md §6).
