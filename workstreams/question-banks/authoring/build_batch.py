#!/usr/bin/env python3
"""build_batch.py — wrap a bank's envelope ARRAY into one contract-v1.1 `question_batch`.

Run from repo root:
    python workstreams/question-banks/authoring/build_batch.py <envelopes.json>

Writes `<bank stem>.batch.json` beside the array. Exit 0 on success.

WHY THIS IS A REPO SCRIPT AND NOT AN EDIT TO THE VENDORED BUILDER
-----------------------------------------------------------------
The session brief asked for `build_question_envelopes.py` to *additionally* emit the batch file.
**It cannot: that file is vendored.** `tools/hub-export/VENDOR.md` lists it, and its rule is
absolute — *supersede-only, never edited locally* (AGENTS.md §7, CD-003). A change to it arrives
from `scd-hub` as a replacement file plus a decision row; **a local patch would be un-superseded
the next time upstream ships, silently.**

`split_envelopes.py` already set this precedent, and for the same reason: the vendored builder
emits an array, the vendored harness validates one envelope per file, **neither is wrong and
neither may be edited**, so the join lives here. This is the second such join. The array and
`single/` outputs are untouched.

WHAT THE WRAPPER IS, READ FROM `import-contract.schema.json` AND NOT FROM PROSE
-------------------------------------------------------------------------------
**Exactly four keys**, because root `additionalProperties` is `false` and the batch branch sets
`subject`, `class_level`, `address`, `curation_tag`, `pinned_to`, `provenance`, `tags`,
`review_status`, `rendered_markdown` and `payload` to **false**. Anything helpfully added here is
a validation failure, not extra information.

  envelope_version  "1.0"  — **NOT "1.1"**. The DOCUMENT is v1.1; the wire value is a `const` and
                            stays 1.0 because `question_batch` is additive, the same rule that
                            kept question and stimulus at 1.0. This is the single easiest thing to
                            get wrong from a prose description of the change.
  doc_type          "question_batch"
  batch             {bank_id, bank_version, item_count, digest}
  items             the standard question envelopes, unchanged and in array order

`bank_id` and `bank_version` are split off the bank's FILE STEM (`C5_BAN_U13_QuestionBank_v1` →
`C5_BAN_U13_QuestionBank` + `v1`), which is the form the schema's own example gives. The bank's
internal `bank_id` (`QB-BAN-C5-U13`) is a different identifier and is deliberately not used.

THE DIGEST IS ENVELOPE-SYNC'S OWN NUMBER, and that is the point of computing it here: the
signature row, the export and the import audit trail then carry ONE quantity. **But the contract
says `digest` is optional and is "recorded on the batch audit row; not recomputed at import"** —
so it is an audit trail across the boundary, **not an integrity check the Hub enforces.** Do not
build anything on the assumption that a wrong digest would be caught over there.

WHAT THIS SCRIPT REFUSES
------------------------
It re-derives `item_count` from the array rather than trusting any input, and it refuses to write
a batch whose count would disagree with its items — the harness's L1b rejects that whole-batch,
so emitting one would only move the failure later. It also refuses at >500 items (the contract's
size guard) and on an empty array, for the same reason.
"""
import hashlib
import argparse
import json
import sys
from pathlib import Path

BATCH_MAX_ITEMS = 500          # contract v1.1 size guard, mirrored so this refuses early
ENVELOPE_VERSION = "1.0"       # const in the schema; the DOCUMENT is v1.1, the wire value is not
BATCH_DOC_TYPE = "question_batch"


def bank_content_digest(items):
    """sha256 over the bank's `questions`, sorted by qid — byte-identical to the function
    `ENVELOPE-SYNC` and `header.subject_lead_review` use. Kept in step deliberately: three places
    naming one number is the whole point, and three places computing it differently would be worse
    than not computing it at all."""
    return hashlib.sha256(json.dumps(sorted(items, key=lambda q: q.get("qid") or ""),
                                     ensure_ascii=False, sort_keys=True).encode()).hexdigest()


def main(argv=None):
    """TOOLS-CR-019 — argparse, so `--help` REFUSES by name instead of crashing.

    Before this, `sys.argv[1]` went straight into `Path(...).read_text()`, so an unrecognised
    argument was not rejected — it was read as a filename and died with
    `FileNotFoundError: '--help'`. **A traceback is not a refusal** (`SOURCE_POLICY` §7.17), and
    the file already carried a `usage:` string for the zero-argument case, which is what makes the
    omission legible as an oversight rather than a decision.

    **Exit codes are UNCHANGED**: 2 when no envelope path is given (argparse's own code for a usage
    error, which is what the hand-rolled branch returned), 1 on a content defect, 0 on success.
    """
    ap = argparse.ArgumentParser(
        prog="build_batch.py",
        description="Wrap an envelope array in the v1.1 batch wrapper the Hub imports.")
    ap.add_argument("envelopes", metavar="ENVELOPES_JSON",
                    help="path to a *.envelopes.json array produced by split/build_question_envelopes")
    args = ap.parse_args(argv)
    src = Path(args.envelopes)
    envelopes = json.loads(src.read_text(encoding="utf-8"))
    if not isinstance(envelopes, list):
        print(f"{src} is not an envelope array")
        return 1
    if not envelopes:
        print("empty envelope array — the contract requires minItems 1; nothing written")
        return 1
    if len(envelopes) > BATCH_MAX_ITEMS:
        print(f"{len(envelopes)} envelopes exceeds the contract's {BATCH_MAX_ITEMS}-item guard; "
              f"split the upload. Nothing written")
        return 1

    stem = src.name.replace(".envelopes.json", "")
    bank_id, _, bank_version = stem.rpartition("_")
    bank_file = src.parent.parent / f"{stem}.json"
    if not bank_file.exists():
        print(f"bank not found beside the export: {bank_file}")
        return 1
    bank = json.loads(bank_file.read_text(encoding="utf-8"))

    batch = {
        "envelope_version": ENVELOPE_VERSION,
        "doc_type": BATCH_DOC_TYPE,
        "batch": {
            "bank_id": bank_id,
            "bank_version": bank_version,
            "item_count": len(envelopes),
            "digest": bank_content_digest(bank["questions"]),
        },
        "items": envelopes,
    }
    assert batch["batch"]["item_count"] == len(batch["items"]), "count must equal items length"

    out = src.parent / f"{stem}.batch.json"
    out.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {len(envelopes)} items to {out}")
    print(f"  bank_id={bank_id} bank_version={bank_version} "
          f"digest={batch['batch']['digest'][:12]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
