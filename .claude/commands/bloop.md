---
description: Run one research bloop — pick a target with me, dive in isolated sub-agents, gate the results, update state, offer the next.
argument-hint: [target name | "next" | "gaps"]
---

You are running ONE **bloop** — a single research pass in the blooping loop. The full
pattern and concepts are in `research/playbook.md`; this command is the steering wheel.
Follow these steps in order. **Keep your own (steering) context light** — never read a
full digest; route heavy reading to sub-agents and work from their compact summaries.

The argument (may be empty): **$ARGUMENTS**

## 0 · Orient  (cheap, always)
- Read `research/queue.md` and `research/log.md`. State lives on disk — this is how a
  fresh session resumes blooping with zero memory of past chats.
- Note **today's date** (from your context); you'll use it for the digest filename.
- If the working tree has **uncommitted corpus changes** from a previous bloop, commit
  them first (a clean git state stops sub-agents from misreading `git log`). Confirm with
  the user before committing if anything looks unexpected.

## 1 · Assemble the agenda
- If `$ARGUMENTS` names a specific target → use it; go to step 2 to confirm.
- If `$ARGUMENTS` is `gaps`, or the queue's bloop-worthy list is empty/stale → refresh it:
  run `bash research/build-inventory.sh`, then invoke the **`bloop-gapscan`** workflow with
  `args { date }`, and rewrite `research/queue.md` from its ranked output.
- Otherwise → build a short **on-deck list** (3–6 items) from: the top unchecked
  bloop-worthy entries in `queue.md`, any follow-up *seeds* on completed entries, and
  (optional) `last30days` fresh signal for owned gear.

## 2 · Ask the user — GATE 1
Present the on-deck list (each: target · why · suggested focus) via **AskUserQuestion**.
Ask them to pick one, combine, or name something else. **Do not proceed until they choose.**

## 3 · Run the bloop
Work out for the chosen target:
- `category` (gear / software / technique), `corpusPath` (`gear/<X>` or `software/<X>`, or
  null if net-new), `slug` (kebab-case; append `-l2`/`-l3` when re-blooping the SAME target
  so digests don't overwrite), `focus` (1–3 sentences of emphasis from the user).
- **`focus` says WHAT to research, never WHERE to write.** Do NOT tell the bloop to "capture
  X *into* `research/links/…`" — that names a *promotion target*, and the dive will read it as
  a place to write, breaking the staging boundary (it bit the MOOD MkII bloop). Say "capture
  the official CC chart (CC# → parameter)"; file placement happens at promotion (steps 5–6).
- **Lenses** — choose by intent:
  - *Spec / control gap* (e.g. capture a MIDI CC chart) → keep the default lenses
    (official / community / video / technical / comparison).
  - *Creative / patch / lineage* → custom lenses (identity, lineage, patches, combinations,
    comparison, …), tailored to the target and the user's focus — like the Big Time bloops.

Invoke the **`bloop-dive`** workflow with
`args { target, slug, date, category, corpusPath, focus, lenses, freshSignal? }`.
It runs in the background — tell the user to watch `/workflows`. Wait for the completion ping.

## 4 · Report + propose promotions — GATE 2
**First, a staging check:** run `git status --short`. The dive must have written ONLY under
`research/bloops/`. If anything was created or modified outside it (corpus files, downloaded
PDFs), flag it to the user — the bloop overstepped its boundary and that change needs explicit
review before it's trusted (the `bloop-dive` staging guard should prevent this, but verify).
The workflow returns a **compact summary + a digest path** (`research/bloops/<date>-<slug>.md`).
Do NOT read the whole digest. From the summary, show the user: what it learned, verified vs
flagged, the suggested corpus edits, candidate index chunks, and the follow-up questions.
Propose what to promote and ask the user (**AskUserQuestion**) what to apply.

## 5 · Apply promotions — verify first
For approved promotions, dispatch a small **parallel promotion workflow** whose agents touch
**disjoint files** and are told to **verify each correction against the on-disk manual or the
digest's verified findings BEFORE editing**, apply surgically, and report what they
changed/declined. Then show the user `git diff` — **the diff is the real gate.** (Sub-agents
sometimes act on a flawed instruction — a stale path, a wrong count, a `git log` false alarm;
the diff is how you catch it.)

## 6 · Update state + commit
- Mark the target done in `queue.md`; append its follow-up questions as new *seeds*; add a
  row to `research/log.md`.
- Stage candidate chunks under `research/_promotions/`.
- Commit the corpus changes + state as one atomic commit **on the worktree branch** — leave
  `main` untouched.

## 7 · Offer the next — GATE 3
Ask: *"Bloop the next one, or stop?"* If yes → back to step 1. If stop → give a one-paragraph
summary of what this bloop added.

---

### Principles (do not violate)
- **Steering context stays light** — never read full digests; only summaries + file paths return.
- **Every dive is isolated** — heavy research runs in sub-agent contexts, never in your seat.
- **The human gates every bloop** (steps 2, 4, 7). Never auto-chain or auto-promote.
- **Verify before promoting.** The `git diff` is the gate.
- **Commit between bloops** for a clean git state.
- **It's a blooper** — a single pass may be wrong; the loop, run again, reinforces the truth.
