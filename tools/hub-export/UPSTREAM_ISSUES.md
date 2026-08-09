# UPSTREAM_ISSUES.md — tools/hub-export

Issues found in the vendored `scd-hub` harness. **This repo does not fix them.** The harness is
vendored under the LOCKED contract v1.0 and is supersede-only (CD-003, AGENTS.md §7) — a local
patch would silently diverge from the contract the Hub actually enforces. Each issue is carried
here until `scd-hub` resolves it in **its own D-series** and ships a superseding version.

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
