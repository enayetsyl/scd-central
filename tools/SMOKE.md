# SMOKE.md - tools/

Evidence that these tools have been run, not merely placed (AGENTS.md 5, CD-009).

## tools/run_all.py

Run 2026-08-19 on Windows, Python 3.13.9, at d9afff0.

    python tools\run_all.py --repo
    RUN_ALL VERDICT: CLEAN   (6 gate run(s), 0 FAIL, 0 REFUSED)

    python tools\run_all.py --bank workstreams\question-banks\banks\C5_BAN_U19_QuestionBank_v1.json --quiet
    RUN_ALL VERDICT: CLEAN   (1 gate run(s), 0 FAIL, 0 REFUSED)

Seeded defect - U19 copied outside banks/ with marks 1 rewritten to 99:

    python tools\run_all.py --bank seedtest\SEED.json --quiet
    RUN_ALL VERDICT: FAIL   (1 gate run(s), 1 FAIL, 0 REFUSED)
    FAILED:  BANK-GATES
    EXIT=1

Exit code read from ERRORLEVEL, not inferred from the printed verdict - the exit code is what
the pre-push hook acts on. Fixture deleted after the run. Exit 2 (REFUSED) not yet exercised.
