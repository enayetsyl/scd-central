# UPSTREAM_ISSUES.md — tools/hub-export

Issues found in the vendored `scd-hub` harness. **This repo does not fix them.** The harness is
vendored under the LOCKED contract v1.0 and is supersede-only (CD-003, AGENTS.md §7) — a local
patch would silently diverge from the contract the Hub actually enforces. Each issue is carried
here until `scd-hub` resolves it in **its own D-series** and ships a superseding version.

---

## UP-004 — the envelope-schema default globs `*ImportEnvelope*`, which matches no file the contract ships

**Status:** OPEN · raised 2026-08-20 (TOOLS-CR-023 named it and deliberately left it) · owner: `scd-hub` repo, its D-series
**Component:** `validate_import.py` — `_resolve()` at the `--envelope-schema` default, `main()` line 301
**Blocks:** nothing. The script must simply be run WITH `--envelope-schema` passed explicitly.

**What.** Run with no `--envelope-schema`, the harness resolves its own default by globbing, next to
`validate_import.py`, for:

```
*ImportEnvelope*Schema*.json
*ImportEnvelope*.json
```

**Nothing in this repo matches either pattern.** Measured 2026-08-20 by walking the whole tree with
`.git` excluded: **zero files match `*ImportEnvelope*`**, and the only schema that exists is
`tools/hub-export/import-contract.schema.json`. So the default can never resolve, and the flag is in
practice mandatory rather than optional.

**What it does NOT do, stated because the opposite was assumed before the code was read.** It does
**not** validate against nothing and it does **not** pass silently. `_resolve()` exits by name:

```
ERROR: envelope schema not found (looked for [...]); pass it explicitly.
```

That is a refusal, and it is correct — `SOURCE_POLICY` §7.17's line, honoured. **This issue is a
usability defect, not a correctness defect**, and it is filed at that weight. TOOLS-CR-023's
description of the glob was accurate; the inference that it produced a silent pass was not, and the
distinction is recorded here so no later reader re-raises this as a false-green.

**Why it is not fixed here.** `validate_import.py` is **vendored and LOCKED** (SMOKE.md records
*v1.0 LOCKED 2026-06-09*; CD-003 · CD-013 · AGENTS.md §7 make it supersede-only). A one-line change to
the glob would be a local patch to the contract the Hub actually enforces — the precise divergence
CD-013 exists to prevent, and the same reasoning that routed UP-001 and UP-003 upstream instead of
patching. **The Principal ruled 2026-08-20 to fix it; this is the only route the ruling can take.**

**What would close it.** A superseding `validate_import.py` whose envelope-schema default names the
file the contract actually ships — e.g. `*import-contract*.schema.json` alongside the existing
patterns, so both the historical and current names resolve. On arrival: re-vendor, update `VENDOR.md`
and `SMOKE.md`, run the harness **with no `--envelope-schema`** and confirm it finds the schema, and
log the supersede as a CD row.

---

## UP-003 — `ref19_topic_id`'s pattern forbids a hyphen after the subject prefix, so two real REF-19 slugs are unrepresentable

**Status:** OPEN · raised 2026-08-14 (CD-125 / TOOLS-CR-002 / PENDING-P-029) · owner: `scd-hub` repo, its D-series
**Component:** `LOCKED_QuestionPayload_Schema_v1.json` — `ref19_topic_id`
**Blocks:** every C5 **Math** bank. **Does NOT block wave 1 (Bangla)** — no BAN slug is affected.

**What.** The pattern is

```
^(BAN|ENG|MATH|SCI|BGS)-[A-Z0-9]+$
```

`[A-Z0-9]+` excludes `-`, so **exactly one hyphen is permitted**: the one after the subject prefix.
`canon/topics/LOCKED_REF-19_Vertical_Topic_Progression_Map_v1_10.md` carries **121 backticked
slugs**, and **two of them have three segments**:

> `MATH-ADDSUB-REL` · `MATH-MULDIV-REL`

Neither can ever validate. **Two slugs that canon defines cannot be written into a payload.**

**And the harness's derived copy already "solved" it by truncation, which is the part that makes
this a ruling.** `validate_import.py`'s auto-extracted `REF19_SLUGS_DEFAULT` also holds 121 — but
holds `MATH-ADDSUB` and `MATH-MULDIV`. Measured both directions:

```
artifact − harness = {MATH-ADDSUB-REL, MATH-MULDIV-REL}
harness − artifact = {MATH-ADDSUB,     MATH-MULDIV}
```

The extractor's regex stopped at the second hyphen. **The truncated forms exist nowhere in REF-19**
— so the only two values that would validate are two ids canon does not contain, and two canon-layer
artifacts disagree about what a REF-19 id *is*.

**This is CD-088's PATTERN at a fifth instance** — *normalising an ID discards the thing that makes
it an ID* — and the discarded thing is a hyphenated segment, the same class of loss as CD-088(b)'s
scheme prefix.

**Nothing was patched.** The schema is LOCKED and supersede-only (CD-013), and the derived constant
is inside a vendored file under the same contract. The gate suite's `REF19-SLUG` reads the **LOCKED
artifact**, never the derived copy (CD-011: a registry is written from the artifact, never from a
summary — the ground QB-CR-007 refused to build canon on this exact constant), so it accepts the
two real slugs and would reject the truncations.

**What would close it.** A superseding `LOCKED_QuestionPayload_Schema_v1.json` whose
`ref19_topic_id` pattern admits further hyphenated segments — e.g.
`^(BAN|ENG|MATH|SCI|BGS)(-[A-Z0-9]+)+$` — **and** a re-extraction of `REF19_SLUGS_DEFAULT` that
does not truncate. On arrival: re-vendor, update `VENDOR.md` and `SMOKE.md`, re-run the slug census
both directions, and log the supersede as a CD row. **Until then no Math bank may be authored**,
because either value it could carry is wrong somewhere.

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
