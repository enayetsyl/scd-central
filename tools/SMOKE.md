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

## tools/subject_search.py

Proven 2026-08-20 (CD-188), Linux, Python 3.12.3. Three runs, in both directions.

Selftest — six synthetic cases, no live ledger read:

    python3 tools/subject_search.py --selftest
    SELFTEST: PASS (6 cases)
    EXIT=0

Live search, the case the tool was built for — one word returns the whole S14/S15 history
(CD-134, CD-136, CD-139, CD-147, CD-150, QB-CR-012), which is what CD-186(d) needed and
did not run:

    python3 tools/subject_search.py S15
    RESULT: 16 hit(s) across 3 file(s) for ['S15']

The zero case, exercised deliberately because a search that finds nothing is the answer a
drafter wants and is therefore the answer most likely to be believed unearned (TOOLS-CR-005):

    python3 tools/subject_search.py ZZZNOTATERM
    RESULT: 0 hit(s) across 0 file(s) for ['ZZZNOTATERM']
      NOTHING FOUND - which is a weaker statement than it looks. ...

The zero result prints its own caveat rather than a bare count. Not registered in run_all.py
and not a gate - CD-188(d): no script can observe whether a human searched before drafting.
