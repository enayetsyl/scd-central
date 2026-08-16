# VENDOR.md — tools/hub-export

Vendored 2026-08-09; **contract v1.1 superseded in whole 2026-08-15** (CD-143, upstream `D-#495`,
scd-hub commit `7ad4903`). **Supersede-only — never edited locally** (AGENTS.md §7, CD-003).
A change upstream arrives as a replacement file plus a decision row; it is never patched here.

| Field | Value |
|---|---|
| Upstream | `scd-hub` (github.com/enayetsyl/scd-hub) |
| Contract | Import contract **v1.1**, 2026-08-15, upstream `D-#495` — supersedes **LOCKED v1.0** (2026-06-09, D-PROJ04-005) |
| Harness | `validate_import.py` **v1.1** 2026-08-15 — adds **L1b**, the `question_batch` wrapper check |
| `envelope_version` | **still `"1.0"`** — the DOCUMENT is v1.1, the WIRE VALUE is not. `question_batch` is additive (new doc_type + branch), the same rule that kept question/stimulus at 1.0 |
| Runtime | Python 3, `jsonschema >= 4.18` (Draft 2020-12) |
| Proven | `SMOKE.md`, 2026-08-09 — pass path, fail path, exit codes |

## Files

| File | Role |
|---|---|
| `validate_import.py` | The conformance harness. **L1b `question_batch` wrapper — item_count vs items length, and the 500-item size guard; both are WHOLE-BATCH rejects.** L1 envelope schema · L2 payload schema by doc_type · L3 envelope↔payload consistency · L4 question semantics (marks sums, REF-19 registry, stimulus_ref form) · ADV REF-21 lexicon scan, plan surface only |
| `import-contract.schema.json` | The machine-readable outer contract — **the source of truth** |
| `import-contract.md` | Human-readable orientation to the same contract |
| `LOCKED_C5_PlanSchema_v1.json` | Payload schema, plan doc-types |
| `LOCKED_QuestionPayload_Schema_v1.json` | Payload schema, `doc_type=question` |
| `LOCKED_StimulusPayload_Schema_v1.json` | Payload schema, `doc_type=stimulus` |
| `build_envelope.py` | Wraps one Project-03 plan + its rendered Markdown into an envelope |
| `build_question_envelopes.py` | Fans a question-bank JSON out into N single-doc envelopes |

The two `build_*` scripts are authoring convenience — they derive envelope structure from the
live schemas and do **not** validate. Output still goes through `validate_import.py` unchanged.

## Known deviations from as-supplied

- **V-1 — schema filename vs discovery glob.** The harness looks for `*ImportEnvelope*.json`;
  the schema is supplied as `import-contract.schema.json`. `--envelope-schema` must be passed
  explicitly. Not renamed — supersede-only. See `SMOKE.md`.
- **V-2 — no script guard.** The harness performs no charset/script check. This contradicts the
  assumption behind the CD-008 deferral. Raised as **PENDING-P-002** under CD-011, unmerged.

## Not vendored here

The SB (support-book) validators that arrived in the same drop — `validator_v2_rebuilt.py`,
`validator_letter_audit.py`, `validate_admin_pass.py` — are **not** hub-export tools. They
belong to the support-books workstream (Step 3). One of them, `validator_v2_rebuilt.py`, was
read read-only for the CD-011 cross-check; none were moved.
