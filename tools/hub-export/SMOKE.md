# SMOKE.md — tools/hub-export

Evidence that the vendored harness has been **run**, not merely placed (AGENTS.md §5, CD-009).
Re-run and update this file whenever the harness or its schemas are superseded.

Run 2026-08-09 · `validate_import.py` v1.0 LOCKED 2026-06-09.

## Environment

`jsonschema >= 4.18` is required — the harness imports `Draft202012Validator`. A default
Ubuntu `python3-jsonschema` (3.2.0) fails at import with
`ImportError: cannot import name 'Draft202012Validator'`. Install with
`pip install --break-system-packages "jsonschema>=4.18"`. Verified against 4.26.0.

## Invocation note (finding V-1)

The harness discovers its envelope schema by glob `*ImportEnvelope*Schema*.json` /
`*ImportEnvelope*.json`. The file as supplied is named `import-contract.schema.json`, which
matches neither, so **`--envelope-schema` must be passed explicitly**. The file was NOT renamed:
it is vendored under the LOCKED contract and is supersede-only (CD-003, AGENTS.md §7).

## Test 1 — conformant envelope (expect PASS, exit 0)

```
python3 validate_import.py good_stimulus.json \
  --envelope-schema import-contract.schema.json \
  --stimulus-schema LOCKED_StimulusPayload_Schema_v1.json

=== good_stimulus.json ===
RESULT: PASS (0 warn, 0 advisory) — importable
EXIT=0
```

## Test 2 — deliberately malformed envelope (expect FAIL, exit 1)

Four seeded errors: `envelope_version` "2.0" (violates const), `subject` "BANGLA" (not in enum),
`payload.stimulus_id` "STIM-bad-id" (violates pattern), `payload.stimulus_type` deleted (required).

```
python3 validate_import.py bad_stimulus.json \
  --envelope-schema import-contract.schema.json \
  --stimulus-schema LOCKED_StimulusPayload_Schema_v1.json

=== bad_stimulus.json ===
  FAIL     [ENVELOPE] ['envelope_version']: '1.0' was expected
  FAIL     [ENVELOPE] ['payload']: 'stimulus_type' is a required property
  FAIL     [ENVELOPE] ['subject']: 'BANGLA' is not one of ['BAN', 'ENG', 'MATH', 'SCI', 'BGS']
RESULT: FAIL (3 fail, 0 warn, 0 advisory) — import REJECTED
EXIT=1
```

The harness caught three of the four seeded errors and stopped at the L1 envelope layer, which
is correct: L2 payload dispatch is gated behind a clean L1 (`if not any(c == "ENVELOPE" …)`),
so the `stimulus_id` pattern violation was never reached. Fixing L1 and re-running would surface
it. Both the pass and the fail path are therefore proven, exit codes included.

## Test 3 — script-guard probe (the CD-011 cross-check)

Same conformant envelope, with arrows, emoji, em-dash and Arabic script injected into
`payload.title` and `payload.content`:

`"পাখির মতো — arrows → emoji 🔒 arabic بسم"`

```
=== scriptguard_probe.json ===
RESULT: PASS (0 warn, 0 advisory) — importable
EXIT=0
```

**The harness has no script guard.** Not a silent skip — L1–L4 contain no charset check, the
envelope schema carries zero `pattern` constraints, and the seven patterns across the three
payload schemas are all ID/slug formats. Recorded as **PENDING-P-002** under CD-011; it is not
merged with the SB validator's list.

## Step 4 proof — `build_envelope.py` + `LOCKED_C5_PlanSchema_v1.json` (CD-030)

Three real P03 Session Plans wrapped and validated end-to-end, 2026-08-09:

```
build_envelope.py  -> wrote envelope   EXIT=0   (x3)
validate_import.py -> RESULT: PASS (0 warn, 0 advisory) — importable   EXIT=0   (x3)
   LOCKED_C4_MATH_U05_S01_SessionPlan_v1 · U05_S06 · LOCKED_C5_BAN_U17_S01
```

`doc_type=session_plan` on all three, so L2 dispatched to the plan payload schema — that schema
is now exercised, not merely present.

**Still unexercised, and deliberately not flipped:** the question-bank fan-out script and the
question payload schema. Step 4 supplied **no question artifact of any kind**, so neither has
been run; both stay VENDORED-UNPROVEN until a question bank exists.

Also confirmed: the `_inbox` copy of the plan schema is **byte-identical** to the vendored copy
(sha256 `6a15d89d…31b9c`) — no divergence in the LOCKED contract, no escalation.

Full evidence: `workstreams/lesson-plans/reports/PROOF_CHAIN_2026-08-09.txt`.
