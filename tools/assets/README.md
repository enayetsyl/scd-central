# tools/assets — DEFERRED

**Status: DEFERRED by design.** Not a slot waiting to be filled — a decision, recorded.
The row that governs this folder is in `tools/MANIFEST.md` under **DEFERRED rows**, and it carries
both the reason and the trigger condition. Read it there; it is not duplicated here.

**Intended contents, if and when the trigger fires:** `sync.py` (rclone wrapper) + an
`assets_manifest` convention (filename + hash per consuming JSON).

**Where the binaries actually live:** large binaries — book images, scans — are on Google Drive via
rclone, **not in this repo**. Migration to R2 is a storefront concern and belongs to the storybook
venture's own repo (AGENTS.md §1 — absolute no-crossover), not here.

**Trigger:** storybook asset sync becoming real work in a lane that lives here, **or** the first use
of rclone by anything in this repo. Until one of those, this folder is correctly empty.

*The `NOT YET SLOTTED` marker was removed 2026-08-14 (Principal ruling, session-2 ruling 7). It had
fired a PLACEHOLDER warn on every gate run in every session for a month; a warning that never stops
firing has stopped conveying information, and it was training the reader to skim past the line where
a real one would appear.*
