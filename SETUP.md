# SETUP.md — git init & push (mirrors the EnglishDrive procedure)

Do this on your machine (not in a chat sandbox), one step at a time.


## 0. Windows prerequisites (do these first)

```bash
git config --global core.symlinks true
git config --local  core.symlinks true
```

Both. **The local setting silently overrides the global one**, and git writes `false` into the local config at clone time on Windows without Developer Mode or an admin shell. With it false, git writes a symlink's *target path* as the file's *content*: two tracked files under `workstreams/lesson-plans/audits/` become 36-byte text stubs, `INT-ID-CHECK` goes red on Windows and green on Linux from the same commit, and `validate_plan.py` cannot run at all. Enable Developer Mode (Settings → Privacy & security → For developers) or run the clone from an admin shell.

Python must be on PATH. If `python` resolves to something unexpected, set `SCD_PYTHON` to a full interpreter path — the pre-push hook of §6 reads it.

## 1. Unzip and init

```bash
# unzip scd-central_starter.zip somewhere OUTSIDE any Google Drive-for-Desktop folder
cd scd-central
git init -b main
git add -A
git commit -m "scd-central v1.0 starter kit (AGENTS.md protocol, canon skeleton, 9 workstreams)"
```

## 2. Create the PRIVATE repo on GitHub

On github.com: New repository → `scd-central` → **Private** → no README/gitignore (we have them).
(Or: `gh repo create scd-central --private --source . --push` if GitHub CLI is logged in — then skip step 3/4.)

## 3. Create a fine-grained PAT (one per device, like EnglishDrive)

GitHub → Settings → Developer settings → Fine-grained tokens → Generate:
- Name: `scd-central-agent` (this device); later `scd-central-teacher` for the teacher laptop
- Repository access: **Only `scd-central`**
- Permissions: Contents **Read and write**
- Expiry: 1 year → **add it to the same Aug-2027 renewal reminder as the EnglishDrive tokens**

## 4. Remote with PAT-in-URL and push

```bash
git remote add origin https://<PAT>@github.com/enayetsyl/scd-central.git
git push -u origin main
```

> **SUPERSEDED 2026-08-19 — do not use PAT-in-URL.** `git remote -v` is the most commonly run
> diagnostic in this repo and it prints the remote in plain text, so a PAT in the URL is a live
> credential echoed into every transcript and screenshot. The PAT above was revoked for exactly
> that reason. **Use an SSH remote.** With two GitHub accounts on one machine a bare `github.com`
> host is ambiguous, so use a `~/.ssh/config` alias:
>
> ```bash
> git remote set-url origin git@github-personal:enayetsyl/scd-central.git
> ```
>
> If ssh ignores the key without explanation, its permissions are too open — a stale SID from a
> deleted Windows account is the usual cause. Fix with `icacls <keyfile> /inheritance:r` then
> `/grant:r "%USERNAME%:R"`, on both the key and `.ssh/config`.

## 5. Verify the gate runs

```bash
python tools/audits/canon_check.py
```

Expected right now: `RESULT: CLEAN` with ~12 WARN lines (canon files not yet slotted).
Each WARN disappears as you complete SLOTTING_CHECKLIST.md.


## 6. Install the pre-push hook (CD-176)

```bash
cp tools/hooks/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-push
```

**Required on every clone.** `.git/hooks/` is not tracked by git, so the committed file at
`tools/hooks/pre-push` is the source of truth and the installed file is a copy — re-install after
any change to it.

The hook runs `tools/run_all.py --repo` and blocks the push unless the last line of output is
`RUNALL_SENTINEL=CLEAN` **and** the exit code is 0. A crash, a pipe death, an interpreter that did
not resolve, or a mis-invocation all produce no sentinel and all block: absence of a verdict is a
refusal, not a pass. Verify it before trusting it — `SCD_ROOT=/tmp git push` must be refused.

This is the only verification layer a chat cannot forge, and it is not CI: it is local, it binds
only a machine where it has been installed, and `--no-verify` bypasses it.

## 7. First Cowork session

Open Cowork → attach the `scd-central` folder → "Run new tasks in the cloud" OFF → say:
"Read AGENTS.md and SLOTTING_CHECKLIST.md, then start Step 1 canon slotting; I will supply the files."
