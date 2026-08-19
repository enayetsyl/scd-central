# SETUP.md — git init & push (mirrors the EnglishDrive procedure)

One step at a time. **§1–§4 and §6 are machine-only** — they create a working tree, hold credentials, or install a hook that binds one machine. **§5 runs anywhere, including a chat sandbox** (demonstrated 2026-08-19: a sandbox cloned `origin/main` at `88a0a95` and ran the full repo suite to `RUNALL_SENTINEL=CLEAN`, matching this machine's verdict on the same commit).


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

> **HISTORICAL.** This is how the repo was created once, in Aug 2026. It is not the entry path
> for a new machine — the repo exists on GitHub and is public, so the entry path is a clone:
> `git clone git@github-personal:enayetsyl/scd-central.git` (or the https URL for read-only).
> Then §0, then §6.

## 2. Create the repo on GitHub

On github.com: New repository → `scd-central` → no README/gitignore (we have them).

> **SUPERSEDED 2026-08-19 — the repo is PUBLIC, not private.** The Principal ruled one repo,
> flipped in place (CD-180): production moved to ordinary chat sessions, and a chat can only fetch
> canon and gate scripts if the repo is public. There is no separate public mirror and none is to
> be created. **The consequence is permanent and must be understood before every commit: everything
> pushed here is world-readable, including exam papers and accounting.** Nothing secret goes in the
> repo — not a token, not a key, not a password, not a bank detail.

## 3. Create a fine-grained PAT (one per device, like EnglishDrive)

GitHub → Settings → Developer settings → Fine-grained tokens → Generate:
- Name: `scd-central-agent` (this device); later `scd-central-teacher` for the teacher laptop
- Repository access: **Only `scd-central`**
- Permissions: Contents **Read and write**
- Expiry: 1 year → add it to the same Aug-2027 renewal reminder as the EnglishDrive tokens

> **SUPERSEDED 2026-08-19 — do not mint a PAT for this repo.** The PAT described above was echoed
> unredacted into an agent transcript and **was revoked on 2026-08-19**. Authentication is SSH
> (see §4's note). **The Aug-2027 renewal reminder no longer applies to `scd-central`** — if it
> fires, it fires on a credential that does not exist; leave the EnglishDrive entries alone.
> A read-only clone of a public repo needs no credential at all.

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

For the whole suite rather than one gate, `python tools/run_all.py --repo`. **This section needs
no credential and no hook, so it runs anywhere the repo can be cloned** — a second machine, a
teacher laptop, or a chat sandbox. That is what makes an independent re-run possible.


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
refusal, not a pass.

**Verify it before trusting it.** Point `SCD_ROOT` at a directory that is not the repo; every gate
must REFUSE and the push must be blocked. In PowerShell:

```powershell
$env:SCD_ROOT = "C:\Users\HP"
git push
Remove-Item Env:\SCD_ROOT
```

**Clear the variable afterwards or every later run in that session is refused.** The bash form
(`SCD_ROOT=/tmp git push`) is not valid PowerShell — it fails as a command rather than as a gate,
which looks like a passing test and is not one.

This is the only verification layer a chat cannot forge, and it is not CI: it is local, it binds
only a machine where it has been installed, and `--no-verify` bypasses it.

## 7. Opening a BUILD session (CD-177)

Production runs in ordinary chat sessions, not Cowork. Cowork is retained for exceptions only.

A session opens with a fresh clone and a pasted HEAD hash:

```bash
git clone git@github-personal:enayetsyl/scd-central.git
cd scd-central
git log --oneline -1
```

**Paste that line verbatim; it is the first line of the session's receipt.** REVIEW verifies
same-commit against it, and a lane that cannot produce it stops at minute one rather than at the
push. **A chat without code execution can still describe a suite run it never performed** — the
hash is the tripwire, and §6's hook plus REVIEW are what actually enforce.

For gate scripts alone, a narrow clone is enough and takes seconds:

```bash
git clone --filter=blob:none --sparse --depth=1 https://github.com/enayetsyl/scd-central.git
```
