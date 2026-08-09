# _wip/STATE.md — scholarship (session-resumable state)

| Field | Value |
|---|---|
| Current build | — (nothing in build) |
| Phase | Policy adopted; production not started |
| Last completed step | `MODEL_PAPERS_POLICY.md` v1.0 adopted 2026-08-09 (CD-038): order C5 → C4 → C3 → C2 → C1; model CTs per subject only |
| Next step | First model paper — **C5 BAN model Annual (100)**, the only class × subject with a source extraction in canon today |
| Blockers / open PENDING-P tags | none |
| Files in `_wip` awaiting "done" | none |

## State of the gates

`audits/gates.py` is the unfilled `_template` copy and **FAILS by design** — a workstream with
zero gates cannot declare anything final. That is the correct state for a workstream that has
produced nothing. Its four gates (mark-total recompute · slot-by-slot spine match · domain-ratio ·
script guard) are written with the first C5 model paper, not before.

## Known constraint on the first build

Only `canon/marklogic/C5_Bangla_Source_13-23.md` exists, and it covers **পাঠ ১৩–২৩** only. A C5
Bangla model Annual drawing real questions will cover those chapters and must carry **typed
placeholders** — naming the slot, its marks and its domain — for anything outside them, per
MODEL_PAPERS_POLICY §4. Never invented content presented as real. C5 Bangla পাঠ ১–১২ and ২৪+ are
the first extractions owed under `canon/sources/SOURCE_POLICY.md` §4.
