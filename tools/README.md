# tools/ — shared neutral tooling layer

One copy of every cross-workstream tool. Workstreams call these; they do not keep private copies.

- `audits/`     — audit-script convention + canon_check.py (repo-wide gate)
- `render/`     — vendored Bengali fonts (Nikosh, Noto Sans Bengali) + docx/render scripts
- `images/`     — apply_strips.py (programmatic compliance stripe; stripe never in prompts)
- `hub-export/` — vendored validate_import.py (SCD Hub LOCKED import contract v1.0 harness)
- `assets/`     — rclone sync for large assets on Google Drive (repo never inside Drive-for-Desktop)
