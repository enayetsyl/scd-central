# SETUP.md — git init & push (mirrors the EnglishDrive procedure)

Do this on your machine (not in a chat sandbox), one step at a time.

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

(PAT-in-URL is the standing workaround: the Cowork sandbox can't reach Windows Credential Manager.)

## 5. Verify the gate runs

```bash
python tools/audits/canon_check.py
```

Expected right now: `RESULT: CLEAN` with ~12 WARN lines (canon files not yet slotted).
Each WARN disappears as you complete SLOTTING_CHECKLIST.md.

## 6. First Cowork session

Open Cowork → attach the `scd-central` folder → "Run new tasks in the cloud" OFF → say:
"Read AGENTS.md and SLOTTING_CHECKLIST.md, then start Step 1 canon slotting; I will supply the files."
