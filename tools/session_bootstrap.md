# session_bootstrap.md — how an agent session starts, works and pushes

**Authority:** Principal ruling 2026-08-15 — agent work moves OFF the mounted drive and into a
container clone. **`C:\scd-central` is no longer the work surface.**

**Status of the numbers below: MEASURED IN THE SESSION THAT WROTE THIS FILE**, not estimated.
Every claim here is one a later agent can re-run and falsify.

---

## 0. Why this exists — the two facts that shape everything

**FACT 1 — the mounted drive cannot unlink inside `.git/`, and the container filesystem can.**
This is the whole reason for the move. On the mount every git write leaves `index.lock` behind and
the *next* command fails, which is why AGENTS §9 grew the lock-aside practice, `.git/lock-debris/`,
TOOLS-CR-003 and TOOLS-CR-004. **None of that is needed in a container clone.** Measured:

```
--- after commit 1: does index.lock linger? ---
  no *.lock in .git/ — lock released normally
--- can we unlink inside .git/ directly? ---
  rm inside .git/ SUCCEEDED
--- second write with NO aside (this is what fails on the mount) ---
  second add+commit SUCCEEDED with no lock-aside
--- reset --hard, the operation that failed on the mount ---
  reset --hard SUCCEEDED
```

`git reset --hard` is the sharpest case: **on the mount it fails outright** with
`fatal: Could not reset index file`, because reset must replace `.git/index` itself. In the
container it simply works.

**FACT 2 — cloning this repo FROM GITHUB is not practical, and the reason is size, not permission.**
`.git` is **347 MB**; the tracked worktree is **369 MB**. Measured container throughput to GitHub
was roughly **0.2 MB/s**, so a full clone needs ~30 minutes of continuous transfer. **A bash call
here is capped well below that, and a backgrounded `git clone` does NOT survive between calls** —
each call is an independent shell and the child is reaped. A `--filter=blob:none` clone was
attempted and died at 226 KB with nothing written to its log.

**So the clone is taken from the mount — a local copy, 11 seconds — and `origin` is repointed at
GitHub for fetch and push.** The history is byte-identical; only the transport differs. Small
pushes over the network are fine: `git fetch` against an up-to-date repo took **1 second**.

---

## 1. The sequence

```bash
# 1 — clone from the mount (local I/O; ~11s for this repo)
cd ~/work && rm -rf scd-central
git clone --no-hardlinks -q /sessions/<session>/mnt/scd-central scd-central
cd scd-central

# --no-hardlinks is deliberate. A hardlinked clone shares object files with the mount, which is
# the filesystem this move exists to get away from.

# 2 — identity, per AGENTS §2 (each tool commits under its own identity)
git config user.name  scd-agent-cowork
git config user.email almajhudbd@gmail.com

# 3 — repoint origin at GitHub, carrying the PAT from the mount's own remote.
#     NEVER echo the URL unredacted; pipe through the redactor when reporting.
URL=$(cd /sessions/<session>/mnt/scd-central && git remote get-url origin)
git remote set-url origin "$URL"
git remote get-url origin | sed -E 's#//[^@]*@#//***@#'

# 4 — VERIFY BEFORE ANY WORK. Stop on mismatch; never "fix" it by resetting.
git fetch origin
git rev-parse HEAD
git rev-parse origin/main
git status --porcelain          # must be empty
```

**THE CLONE SOURCE IS THE MOUNT, AND THE MOUNT CAN LAG ORIGIN. THIS IS THE FAILURE MODE STEP 4
EXISTS FOR.** The Principal pulls his working copy by hand (§4), so it is behind `origin` from the
moment any session pushes until he next runs `git pull`. **A clone taken from a lagging mount is a
correct clone of the wrong commit** — it is internally consistent, its tree is clean, its history
is valid, and every one of those facts is true of stale state. Nothing about the repo will look
wrong. **`git fetch` then `HEAD == origin/main` is the only thing that catches it, and it must be
run before any work, not before the push** — by push time a session has already built on the wrong
base, and the damage is a merge conflict or, worse, a silent rebuild of something already fixed.

### Step 4 branches, and the branch is DECIDED BY COMPUTATION, NEVER BY JUDGEMENT (CD-152)

If `HEAD` and `origin/main` are equal, proceed. If they differ, run **both** of these and **paste
both, verbatim, in the session report**:

```bash
git merge-base --is-ancestor HEAD origin/main    # → true
git rev-list --count origin/main..HEAD           # → 0
```

**(a) BENIGN — the mount is strictly behind. BOTH results must hold.** The clone then moves to
`origin/main` and proceeds. **This is not reconciliation**: the clone holds nothing origin lacks,
so nothing can be lost, and **`origin/main` is the authority every session already works from —
the mount clone is a speed cache, not an authority.** §0 FACT 2 is why it exists: a GitHub clone
takes thirty minutes. It was never the canonical copy.

**The report must state HOW FAR the mount lags and NAME the commits.** Losing the stop must not
lose the notification — this is the only signal the Principal gets that his working copy is stale,
because the mount is pull-only for agents (§4) and nothing else tells him.

**(b) DIVERGENT, OR ANYTHING ELSE — STOP AND REPORT, unconditionally.** Do not `git pull`, do not
reset, do not re-clone and carry on. This branch covers **any** case that is not (a): the two
commands cannot be run cleanly, or `origin/main..HEAD` is non-empty **by even one commit**. A
mismatch of that shape means the mount and `origin` disagree about the current state of the work,
and which one is right is the Principal's to say — he may have pushed from elsewhere, or the mount
may hold something not yet pushed. **An agent that silently reconciles them destroys the evidence
of which was which.**

**THE AGENT DOES NOT DIAGNOSE ITS WAY PAST (b).** The whole value of (a) is that it is a
computation with no room for a judgement call; an agent permitted to reason about (b) would import
exactly the discretion (a) was built to exclude. Two commands decide it, and nothing else does.

**Why the split exists (CD-152(d)).** CD-141's lane **pushes unattended** and the mount is
pull-only for agents, so **a lagging mount is now the NORMAL opening state after every lane push,
not an anomaly.** The undivided stop fired on the routine case — two consecutive sessions stopped
on it, both strictly behind, both benign. **A stop rule that fires on the routine case trains the
operator to wave stops through**, and a stop waved through by habit is not protecting the case it
was written for.

**Verification is a stop condition, not a formality, and the (a) branch does NOT soften this.**
The brief states an expected HEAD; if `HEAD`, `origin/main` and the expected hash do not all agree,
**report and stop** — an expected hash is a statement about which commit the Principal believes the
work starts from, and (a) says nothing about it. **This is not
theoretical:** on 2026-08-15 an expected-HEAD line in a brief was the only thing that caught a
signature recorded before it was given (`QB-CR-013`). **No gate caught it. The expected-HEAD line
did.**

## 2. Working

**BEFORE ANYTHING ELSE — THE SESSION HAS TWO FILE SURFACES AND ONLY ONE REACHES THE CLONE.**
This is the trap §4's rule does not defend against on its own, and it is written here because
everything below is in bash and a reader can finish §1 believing the mount is behind them
(TOOLS-CR-006).

| Surface | Reaches the CLONE | Reaches the MOUNT |
|---|---|---|
| `bash` | `~/work/scd-central` — **all work happens here** | `/sessions/<session>/mnt/scd-central` |
| Read / Write / Edit file tools | **NEVER — there is no path to it** | `C:\scd-central` — **yes, and it is writable** |

**Every repo write goes through bash.** `C:\scd-central` in a Write or Edit call is the
Principal's working copy, not the clone, and it will accept the write: the mount is `drwx`, and
FACT 1 blocks only unlink inside `.git/`, not ordinary tracked files. The editing tools are the
natural instrument for editing a file and they are the wrong one here.

**If a write does land on the mount:** revert it by writing the original bytes back, **not with
git** — `reset --hard` and `checkout --` do not work there (FACT 1), and `git status` leaves an
`index.lock` that then blocks the Principal's next pull. Verify from inside the container clone,
and report it.

Work normally. **No lock-asides. No `.git/lock-debris/`. No `GIT_INDEX_FILE` tricks.** All three
exist for the mount, and the third is worse than dead weight — TOOLS-CR-003 records that
`GIT_INDEX_FILE` leaves `.git/index` describing the pre-commit tree, so the next ordinary `git add`
stages the exact inverse of the commit just made, and no gate catches it.

Run the suite from the clone's root exactly as before. Every tool resolves paths from the repo root
and none of them cares which filesystem it is on.

## 3. Pushing

```bash
git push origin main
git fetch origin                                   # fresh, not the ref the push just wrote
git rev-parse HEAD; git rev-parse origin/main      # must be equal
git ls-remote origin refs/heads/main               # asked of the SERVER, not a local ref
git log --oneline origin/main..HEAD                # must be empty
git status --porcelain                             # must be empty
```

**`git ls-remote` is not belt-and-braces.** A push writes the local remote-tracking ref itself, so
confirming against `origin/main` alone is checking the push against its own bookkeeping. Ask the
server.

**Push still needs the Principal's explicit approval** (AGENTS §3.1, CD-083(b)) with a per-commit
range check, **until a standing authorization row says otherwise.** CD-079's ruling-only carve-out
is unchanged.

## 4. The mounted drive is PULL-ONLY, and it belongs to the Principal

**No agent writes to `C:\scd-central`.** It is the Principal's working copy and his window onto the
work. After a session pushes, he refreshes it himself:

```
cd C:\scd-central
git pull
```

**Why this is a rule and not a preference.** Two writers on one checkout is how a stale index ends
up describing the wrong tree, and the mount is exactly where that is hardest to repair — `reset
--hard` does not work there. Keeping the mount agent-read-only means the one filesystem that cannot
be repaired is also the one that never needs repairing.

**The agent still READS the mount**, for the clone source and for the PAT. Reading is safe; writing
is barred.

## 5. Environment notes, before they cost a session

- **`jsonschema` is too old for `validate_import.py`.** The vendored copy predates
  `Draft202012Validator` and the harness cannot import it — the failure presents as N content
  failures and is nothing of the kind. First:
  `pip install --break-system-packages 'jsonschema>=4.18'`.
- **Background processes do not survive between bash calls.** `nohup … &` then polling in a later
  call finds nothing running. Anything long must fit one call or be restructured.
- **Deleting files inside a mounted folder can return `Operation not permitted`** and needs a
  desktop-app grant. **In the container clone this does not arise** — one more reason to work here.
- **`.git/lock-debris/` on the mount is the Principal's to clear** (TOOLS-CR-004), in this order,
  because `gc` fails on stale locks and a failed `gc` leaves its own:
  `del /s /q .git\*.lock` → `git gc --prune=now` → `rmdir /s /q .git\lock-debris`

## 6. What this file does NOT change

AGENTS.md §9's lock-aside practice **stays in force for any session that does work on the mount**.
This file does not retire it and must not be read as retiring it: it says the container clone is
the normal path, and §9 is what applies when something must be done on the mount anyway. **A
workaround is retired by the Principal, not by a file that stopped needing it.**
