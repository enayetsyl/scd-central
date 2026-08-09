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

**Still unexercised at Step 4, and deliberately not flipped then:** the question-bank fan-out
script and the question payload schema. Step 4 supplied **no question artifact of any kind**, so
neither had been run; both stayed VENDORED-UNPROVEN until a question bank existed.
**That condition is now met — see the পাঠ ২১ proof below (CD-039).**

Also confirmed: the `_inbox` copy of the plan schema is **byte-identical** to the vendored copy
(sha256 `6a15d89d…31b9c`) — no divergence in the LOCKED contract, no escalation.

Full evidence: `workstreams/lesson-plans/reports/PROOF_CHAIN_2026-08-09.txt`.

## পাঠ ২১ pilot proof — `build_question_envelopes.py` + `LOCKED_QuestionPayload_Schema_v1.json` (CD-039)

Run 2026-08-09 against the first real question bank,
`workstreams/question-banks/_wip/C5_BAN_U21_QuestionBank_v1.json` (57 items: HW 30 · AS 15 · CT 12).

### Invocation note (finding V-2)

`build_question_envelopes.py`'s default envelope-schema path is
`../../docs/import-contract.schema.json`, which **does not exist in this repo** — the vendored
file lives beside the script at `tools/hub-export/import-contract.schema.json`. So
`--envelope-schema` must be passed explicitly here too, for the same reason as finding V-1.
The script is **not** edited: it is vendored under the LOCKED contract and is supersede-only
(CD-003, AGENTS.md §7).

```
python3 tools/hub-export/build_question_envelopes.py \
  --json workstreams/question-banks/_wip/C5_BAN_U21_QuestionBank_v1.json \
  --curation-tag KEEP_AS_IS \
  --envelope-schema tools/hub-export/import-contract.schema.json \
  --author "Principal" --unit-title "পাঠ ২১ — বিদায় হজের ভাষণ" \
  --out workstreams/question-banks/_wip/envelopes/C5_BAN_U21_QuestionBank_v1.envelopes.json

wrote 57 envelopes to workstreams/question-banks/_wip/envelopes/C5_BAN_U21_QuestionBank_v1.envelopes.json
EXIT=0
```

Then every envelope through the harness — `doc_type=question`, so **L2 dispatched to
`LOCKED_QuestionPayload_Schema_v1.json`** and **L3 reconciled `tags.{bloom_level, difficulty,
topic_tag, paper_role}` against the payload**, which is the first time either path has executed:

```
python3 tools/hub-export/validate_import.py <each of 57> \
  --envelope-schema tools/hub-export/import-contract.schema.json \
  --question-schema tools/hub-export/LOCKED_QuestionPayload_Schema_v1.json

=== QP-BAN-C5-U21-Q01.json ===
RESULT: PASS (0 warn, 0 advisory) — importable
EXIT=0
```

**All 57 results are recorded unelided** in
`workstreams/question-banks/reports/BAN_U21_GATES_2026-08-09.txt` — 57 `RESULT: PASS`, zero
`RESULT: FAIL`, zero non-zero exits. The first run of this file summarised 55 of them as
"identical"; an audit of this session flagged that as asserting rather than showing, and the
report was regenerated in full (AGENTS.md §5).

L4 question semantics exercised for real: the fill_blank item `QP-BAN-C5-U21-Q52` (the বিরামচিহ্ন
passage — the only fill_blank in the bank) carries five blanks at 1 mark each and passes the
per-blank sum check against its item marks of 5; every item's
`ref19_topic_id` (`BAN-INFOTEXT` / `BAN-VOCAB` / `BAN-SENTENCE`) cleared the HARD REF-19 registry
check.

**Both rows flip `VENDORED-UNPROVEN` to `REQUIRED`** in `tools/MANIFEST.md`:
`build_question_envelopes.py` and `LOCKED_QuestionPayload_Schema_v1.json`.

**`tools/images/pick_placements.py` is NOT flipped and is untouched by this pilot** — it is an
interactive tkinter GUI and cannot be proven headlessly (CD-022). The three UNPROVEN rows are now
two proven and one still open, not "the last two" as the v0.1 draft assumed.

Full evidence: `workstreams/question-banks/reports/BAN_U21_GATES_2026-08-09.txt`.
