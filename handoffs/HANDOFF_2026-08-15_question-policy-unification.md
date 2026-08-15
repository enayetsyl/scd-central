# HANDOFF — Question-policy unification complete; wave 1 authoring
**Date:** 2026-08-15 · **Owner:** SCD (Principal) · **Chain:** unification → scd-central-migration → ocr-pipeline → math-ch6-onward → **this file**

**Purpose:** a new advisor chat, given this file, continues without re-asking anything settled. Role unchanged: Principal ↔ advisor (ONE recommendation, paste-ready rulings, files-over-memory, verify-at-source). The loop: Principal ↔ advisor chat ↔ disposable Cowork agent sessions on the repo. The agent executes gates and never self-approves — **and it verifies the advisor, which in this chain it did repeatedly and correctly.**

---

## 1. What this chat did

Unified question preparation across five previously independent authorities into one governing file, then built the gates and opened wave 1.

**`canon/QUESTION_POLICY.md` v1.1 is LIVE** (adopted `109b232`, corrected `aba5f7c`). It resolves 18 conflicts between the P00 REF layer, P04's Conventions v1.4, the MarkLogic set, `QUESTION_BANK_POLICY` and `MODEL_PAPERS_POLICY`. The **60-row Unification Decision Register** is the provenance record — every row was ruled by the Principal, none by the advisor.

**Repo state: `4bc66d7`, pushed, clean.** CD rows now run to **CD-132**.

### Sessions in this chain
| Session | Commit | What |
|---|---|---|
| 1 | `74bcd8f` | P00/P04 import; `canon/refs/` (22 REFs + manifest); REF-CITE + SB-baseline gates |
| 2 | `075380d` | QUESTION_POLICY v1.0 adopted (CD-092…120); six supersedes; AGENTS §12 `_inbox` protocol |
| 3 | `cd03467` | Merged 21-gate suite; `ledger_check.py`; all 17 ledgers declare prefix+lane |
| 3b | `4bc66d7` | পাঠ ১২ reversal (CD-127); `int_id_check.py`; `SOURCE-EXCLUSION` gate → **22 gates** |
| 4 | *in flight* | **পাঠ ১৩ question bank — prompt issued, not yet reported** |

---

## 2. Where things stand

**Wave 1 = C5 Bangla পাঠ ১৩ পাখির মতো, alone.** Deliberate pilot with an exit condition: when it closes gate-GREEN you know the per-chapter cost and can size wave 2 against real numbers.

- Source: `canon/marklogic/C5_Bangla_Source_13-23.md` line 33 — a combined *প্রশ্ন তৈরির উৎস* file, **not** a per-chapter SOURCE_POLICY extraction. Different substrate; SOURCE-TRACE resolves against the path the bank declares.
- Target 24 items, `TOP-BAN-C5-05` / `BAN-POEM`, tier1 only.
- Agent drafts, **Principal reviews all items as Subject Lead** (REF-09 §9, UD-52).
- File: `workstreams/question-banks/banks/C5_BAN_U13_QuestionBank_v1.json` (master D-037).

**The bankable surface is much larger than wave 1** — 31 promoted C5 sources (Bangla পাঠ ১–১১, English U01–20) plus পাঠ ১৩–২৩. Narrow was chosen, not forced.

**Math lane: paused by Principal.** অধ্যায় ৬ sits `নির্মাণাধীন`; ch7–ch10 OCR drafts exist **only in gitignored `_inbox/` on one machine** — no committed evidence copy (§7.14.3a owed). Math and Science were extracted in the Principal's second Claude account and will be uploaded after teacher verification against the printed book. **The two-account control-set proof has never been run** and is owed before that work becomes canon.

**Sign-off queue: still the system's bottleneck**, unchanged by any of this.

---

## 3. Key rulings from this chain (cite, don't re-derive)

- **MarkLogic wins on structure; P04 wins on production.** REF-25's Annex A demoted to historical format reference, §2–§3 mechanism retained. Its §0 "no Math paper uses MCQ" is recorded **known-false** — the MATH spine's S01 is বহুনির্বাচনি at 10 marks C2–C5.
- **One Pool per chapter** (REF-08 §4 / D-050). HW·AS·CT are **selection labels, not partitions**. Floor 20/chapter (REF-09 §4.3 — REF-08 §4.1's own words say *lesson* Pool). **No ceiling**; the real bound is "stop when the source is exhausted."
- **Bloom governs the pool, domain governs the paper.** REF-06 §3.6 is the band's source and says *"only indicative"*; REF-17 §5.2 and REF-18 §4.2 restate it faithfully. Six Bloom levels stored, four NAPE domains **derived** — the payload has no domain field.
- **Repetition (§5):** `bloom_level: Remember` items may repeat verbatim across HW/AS/CT **and into HY/annual** — a listed, deliberate supersede of MarkLogic §৮'s শ্রেণি পরীক্ষা ও বড় পরীক্ষা row. Nothing above Remember may. Exposure capped by the domain ratio (৩০±৫% at C5).
- **Substrate:** the extraction records the book; canon governs what the school prints (CD-049, extended to banks).
- **Topic IDs are two registers:** `ref19_topic_id` = slug (REF-19, harness-validated); `topic_tag` = number (`TOPIC_NUMBERS.md`, CD-044). Neither derived from the other.
- **পাঠ ১২ (CD-127):** extraction **permitted later**, consumption **still excluded**. Enforced by the `SOURCE-EXCLUSION` gate, not just prose.
- **REF-01 → v1.3:** all classes and subjects, living/append-extensible (REF-21's mechanism).
- **UD-60(b):** SB-series `REF-1`/`REF-2` retired to P00 numbering by **rename + HISTORICAL alias**, historical citations untouched — rewriting an append-only log to say something it didn't is worse than an alias.
- **Rubric (interim):** minimum conforming — two bands, one `islamic_alignment` row. Marking is by the school's own scheme, outside the payload. The scholarship rubric is undocumented; when written it becomes additional rows, no migration.

---

## 4. The advisor's errors in this chain — read this before advising

The agent caught the advisor at source **seven times**. Every one was a §-citation or a state claim made from uploaded copies rather than the repo.

1. **REF-19 topic IDs** — recommended demoting `TOPIC_NUMBERS.md` to a mirror. REF-19 has never carried numbers (CD-043 said so already).
2. **REF-2 divergence** — claimed it held cast/reference-sheet canon REF-20 lacks. Byte-identical; the cast canon is the storybook venture's (CD-006).
3. **The C3 band "conflict"** — presented REF-17 vs MarkLogic as irreconcilable. The band is *indicative* by its own words and defers to Tier 1.
4. **The fixture citation** — wrote `(CD-055, CD-064(f))` into canon §6 for a rule neither states, lifted from a docstring. The real rule: **controls may be drawn from the live pool; seeds may not.**
5. **`gates.py` state** — briefed it as `_template` zero-gate. It was 795 lines, 16 gates; building as instructed would have deleted ten and un-promoted three rulings.
6. **পাঠ ১২** — instructed a "division of labour" row that was **the position CD-050(b) overruled**.
7. **Readiness list** — said two promoted sources; there were 31. Three handoffs stale.

**The lesson for the next advisor: do not cite a §-number you have not read in this conversation, and re-read repo state rather than carrying it from a handoff.** Say "I have not read X" — the Principal accepts that; a wrong citation costs a session.

---

## 5. Open / parked

- **P-033** — `int_id_check` findings: 15 untyped capture sites reported, not judged.
- **P-034** — unit-segment padding `U09` vs `U9`. Three canon sites, two conventions, **no rule**. Blocks only U01–U09. Principal's leaning (not a ruling): zero-padded. Needs a supersede — two of the three sites are LOCKED.
- **P-035** — extraction-header field for consumption exclusion. §7.9 says a machine-read header line needs a SOURCE_POLICY §7 clause, not an invented field.
- **UP-002** — Hub `pool` field. Blocks usage-lock and AS rotation.
- **UP-003** — `ref19_topic_id` pattern admits no hyphen after the subject prefix; `MATH-ADDSUB-REL` and `MATH-MULDIV-REL` fail it. **Blocks every C5 Math bank**; wave 1 unaffected.
- **QB-CR-009** — U14 Drama `-09` **RULED, execution owed**. পাঠ ১৪ is outside wave 1; rides whichever wave reaches it.
- **`CR-002` spans four lanes** (CR-001/003 three each, CR-004 two). Prefix declaration made them non-ambiguous; **renumbering waits for each lane to close** (P-031). A fifth cross-lane token is a trigger to revisit.
- **PATTERN, promoted (CD-088):** *normalising an ID discards the thing that makes it an ID* — four instances, sixth surfaced at P-034. Lint built; sink widened by **rule** (*any transform that can map two distinct ID strings to one*), not by list.
- **Possible second PATTERN, not raised:** *a gate that reads a form cannot distinguish minting it from describing it.* Four sites — §7.16, CD-085, `ledger_check`'s table-cell anchor, QB-CR-010's whole-line fix. Worth a row.
- **Unchanged from prior chains:** EnglishDrive fold-in · P00 fold-in · english-programme · islamic-studies (ARABIC-SLOT; Naskh fonts parked in `_unvendored/` per CD-126) · accounting (Check-5 423,533; +28,592) · scd-hub privacy flip UNCONFIRMED · PAT renewals Aug 2027 · `pick_placements` workstation session · **`.git/_cowork_trash/` to delete on the Principal's machine**.
- **Four empty workstreams FAIL by design** (`_template`, `curriculum-foundations`, `p01-nctb-stability`, `scholarship`) — a workstream with zero gates cannot declare anything final.

---

## 6. Session mechanics

Inputs via `_inbox/` (now governed by **AGENTS §12**: four classes, agent classifies, report-never-move, duplicates by hash, §12.7 retention list at close). Agent batches questions per AGENTS §6. Verbatim gate output before any "final". **Sync only on explicit approval** — CD-083(b): one held commit anywhere in `origin/main..HEAD` holds the push, and the range check is pasted per commit. **One commit, one class** (CD-083(d)). Never two agents on one workstream. Bengali for teacher-facing, English for protocol.

---

## 7. Working style (binding, unchanged)

Precise and concise; ONE recommendation with 1–2 line justification; copy-paste-exact rulings; files-over-memory; flag-don't-improvise; verify at source before citing any decision. **When the Principal asks for options, give pros and cons on every row and recommend on each — he rules, the advisor does not.** Reply in Bengali when he writes in Bengali. **Do not re-remind him about the sign-off ledger.**

---

## 8. Immediate next actions

1. **Session 4 reports back** — পাঠ ১৩ bank, 24 items, 22 gates. Prompt already issued.
2. **Principal reviews all items** as Subject Lead before promotion.
3. **Read the drafting cost** — how long, what was hard, what the policy made awkward. That number sizes wave 2.
4. **Size wave 2** against real numbers; the bankable surface is 31 promoted sources.
5. **Math lane** resumes on the Principal's call: evidence commit for ch7–ch10 first, then the two-account control-set proof, then অধ্যায় ৬ resume.
