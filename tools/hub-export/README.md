# tools/hub-export — index

✅ VENDORED 2026-08-09. Source: `scd-hub`, import contract **LOCKED v1.0** (2026-06-09).

The only integration path to SCD Hub (CD-003). Artifacts are validated here at **authoring
time**, so they are born conformant rather than discovering it at import.

Flow: build the envelope → `validate_import.py` → Hub import as `draft` → in-app teacher
review → Principal promotes `reviewed → gold`. Nothing else is an integration path.

```
python3 validate_import.py <envelope.json> \
  --envelope-schema import-contract.schema.json \
  --stimulus-schema LOCKED_StimulusPayload_Schema_v1.json   # or --plan-schema / --question-schema
```

`--envelope-schema` is not optional in practice — see `VENDOR.md` V-1. Requires
`jsonschema >= 4.18`.

- `VENDOR.md` — upstream source, contract version, file roles, known deviations. Supersede-only.
- `SMOKE.md` — proof the harness has been run: pass path, fail path, exit codes (CD-009).

⚠️ **The harness has no script guard** (`VENDOR.md` V-2). Anything that assumes export-time
charset enforcement is assuming something this contract does not do — see **PENDING-P-002**.
