#!/usr/bin/env python3
"""split_envelopes.py — split a built envelope ARRAY into one file per item.

Run from repo root:
    python workstreams/question-banks/authoring/split_envelopes.py <envelopes.json>

Why this exists: `build_question_envelopes.py` emits a JSON **array** of envelopes (one bank
fans out to N), but `validate_import.py` validates **one envelope per file**. Neither is wrong
and neither is edited — both are vendored under the LOCKED contract and are supersede-only
(CD-003, AGENTS.md §7). This is the join between them, kept in the repo so the gate-chain step
is reproducible rather than an undocumented shell one-liner.

Writes `<envelopes-dir>/single/<qid>.json`. Exit 0 on success.
"""
import json
import sys
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print("usage: split_envelopes.py <envelopes.json>")
        sys.exit(2)
    src = Path(sys.argv[1])
    envs = json.loads(src.read_text(encoding="utf-8"))
    if not isinstance(envs, list):
        print("ERROR: expected a JSON array of envelopes")
        sys.exit(2)
    out = src.parent / "single"
    out.mkdir(parents=True, exist_ok=True)
    for e in envs:
        p = e.get("payload", {})
        ident = p.get("qid") or p.get("stimulus_id")
        if not ident:
            print("ERROR: an envelope payload carries neither qid nor stimulus_id")
            sys.exit(2)
        (out / f"{ident}.json").write_text(
            json.dumps(e, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"split {len(envs)} envelopes into {out}")
    sys.exit(0)


if __name__ == "__main__":
    main()
