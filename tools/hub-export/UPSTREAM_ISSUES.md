# UPSTREAM_ISSUES.md — tools/hub-export

Issues found in the vendored `scd-hub` harness. **This repo does not fix them.** The harness is
vendored under the LOCKED contract v1.0 and is supersede-only (CD-003, AGENTS.md §7) — a local
patch would silently diverge from the contract the Hub actually enforces. Each issue is carried
here until `scd-hub` resolves it in **its own D-series** and ships a superseding version.

---

## UP-002 — the question payload has no field for the pool a question belongs to

**Status:** OPEN · raised 2026-08-09 (QB-D-003 / CD-039) · owner: `scd-hub` repo, its D-series
**Component:** `LOCKED_QuestionPayload_Schema_v1.json`; `import-contract.schema.json` (`tags`)

**What.** `QUESTION_BANK_POLICY.md` v1.0 (QB-D-001) rules that every chapter carries exactly three
pools — **HW · AS · CT** — with zero overlap. The LOCKED payload has nowhere to record which pool
an item belongs to.

**Verified at source, not assumed.** `paper_role` looks like the natural home and is not:

```
"paper_role": { "enum": ["mcq", "short", "structured", "creative"],
                "description": "The REF-09 §4/§5.3 paper-section family this item is
                                written for … App filter for set assembly" }
```

It is a closed enum already meaning the paper-section family, mirrored three ways
(payload / envelope `tags.paper_role` / `vocab.ts PAPER_ROLES`) and read by the app for set
assembly — a different axis from the pool. Overloading it would corrupt a field the Hub relies on.
Adding a `pool` key to the payload instead is also blocked: `QuestionPayload_v1.json` is
`additionalProperties: false`, so harness **L2 would reject every item**.

**What is asked for.** An **ADDITIVE** change, exactly like the additions that brought in the
`question` and `stimulus` doc-types: a `pool` property (`enum ["HW","AS","CT"]`) on the question
payload, plus its mirror in `tags` so the app can filter on it, with `envelope_version` staying
`"1.0"` under the outer-contract stability rule.

**Consequence accepted here meanwhile.** Pool membership lives **authoring-side** in the bank
file's `pool_index` block, outside the LOCKED payload; `workstreams/question-banks/audits/gates.py`
enforces one-pool-per-question and zero overlap there, and `build_question_envelopes.py` ignores it.
So **the Hub cannot filter by pool on import**, and the two Hub-side features that depend on it —
**usage-lock** and **AS rotation** (`QUESTION_BANK_POLICY.md` §6) — are blocked until this lands.
The vendored schema is **not patched here**: it is supersede-only (CD-003, AGENTS.md §7), and a
local edit would silently diverge from the contract the Hub actually enforces (the CD-013 precedent).

**What would close it.** A superseding `LOCKED_QuestionPayload_Schema_v1.json` (+ envelope `tags`)
carrying `pool`. On arrival: re-vendor, update `VENDOR.md` and `SMOKE.md`, move pool membership from
`pool_index` into the payload, and log the supersede as a CD row.

---

## UP-001 — the import harness performs no charset / script check

**Status:** OPEN · raised 2026-08-09 (CD-013) · owner: `scd-hub` repo, its D-series
**Component:** `validate_import.py` v1.0 LOCKED 2026-06-09; `import-contract.schema.json`

**What.** The harness has no script guard at any layer. L1 envelope schema, L2 payload schema,
L3 consistency and L4 question semantics contain no charset validation; the envelope schema
carries **zero** `pattern` constraints; and the seven patterns across the three payload schemas
are all ID/slug formats with no bearing on text content.

**Evidence — reproducible.** `SMOKE.md` test 3. An otherwise conformant stimulus envelope with

```
payload.title   = "পাখির মতো — arrows → emoji 🔒 arabic بسم"
payload.content = "line one → line two — 🔒 بسم الله"
```

returns:

```
=== scriptguard_probe.json ===
RESULT: PASS (0 warn, 0 advisory) — importable
EXIT=0
```

**Why it matters.** Content promoted to `gold` carrying Arabic script or emoji would **tofu**
(render as missing-glyph boxes) in the Hub's own PDF renderer. The failure surfaces at the point
of printing for children, which is the worst place to find it — after teacher review and after
Principal promotion, when the artifact is already trusted.

**Consequence accepted here meanwhile.** Enforcement is **authoring-side only**: the guard in
`canon/language/LANGUAGE_RULES.md` §7 (CD-012) has to hold where content is written, because
nothing downstream will catch a violation. Authoring repos cannot rely on the import gate for
this.

**What would close it.** A superseding `validate_import.py` implementing the tiered guard, or an
equivalent constraint in the contract schema. On arrival: re-vendor, update `VENDOR.md` and
`SMOKE.md` (re-run test 3, which should then FAIL), and log the supersede as a CD row.
