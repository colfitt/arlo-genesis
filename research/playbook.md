# Blooping — the ARLO Research Loop

> The Chase Bliss Blooper builds a loop one layer at a time, each pass stepping on the
> last. **Blooping** builds your research the same way: each pass is layered on what the
> corpus already knows, you decide what goes down next, and the heavy lifting happens
> somewhere that never muddies your hands.

This is the written-down pattern. It is also the spec for the tooling in
`.claude/workflows/bloop-dive.js`, `.claude/workflows/bloop-gapscan.js`, and
`.claude/commands/bloop.md`, and a primer on **workflows and sub-agents** so the
pattern is repeatable by you, not just by me.

---

## 1. Why this exists: context rot

A single Claude session that runs ten deep research dives in a row turns to mush. The
early findings bury the later reasoning; your steering judgment degrades; the model
starts repeating itself and losing the thread. That decay is **context rot**, and it is
the specific enemy blooping is built to defeat.

Two principles fall out of that, and everything else in this document serves them:

- **Principle 1 — Heavy work runs in a fresh context, never in your seat.** Each bloop's
  actual research happens in *isolated sub-agent contexts*. Your steering session never
  ingests the raw 40 KB of findings — it gets back a compact summary and a file path.
  The bulk lands on disk in `research/bloops/`, not in your conversation.

- **Principle 2 — All state lives on disk, so the session is disposable.** The queue, the
  log, and every bloop digest are files. Your steering thread holds almost nothing that
  isn't recoverable. When even *that* thread gets heavy, you open a fresh session, type
  `/bloop`, and it resumes perfectly by reading `queue.md` + `log.md`. The session rots;
  the state does not.

Add one human rule on top:

- **The human gate.** Blooping never auto-chains. Every bloop *stops* and asks you what's
  next before it does anything, and stops again after, before promoting results. You are
  the metronome. This is what keeps it from wandering into rabbit holes — and what lets
  you keep blooping all day to actually use your subscription.

---

## 2. The four primitives (so you know which lever you're pulling)

| Primitive | What it is | Its job in blooping |
|---|---|---|
| **Sub-agent** (`Agent` tool) | A fresh Claude with its *own clean context*, handed one briefed task, returns a result. It cannot see your chat — you brief it fully. | The unit of isolated research. One sub-agent = one research lens. |
| **Workflow** (`Workflow` tool) | A *script* that orchestrates many sub-agents deterministically — fan-out in parallel, pipeline through stages, verify, synthesize. Runs in the background; watch it in `/workflows`. | **One whole bloop.** `bloop-dive.js` is a Workflow. |
| **`/loop`** | Re-runs a prompt or command on an interval, or self-paced. | Optional hands-free driver once you trust a target list. Usually you'd rather gate by hand. |
| **`/schedule`** | A cron cloud agent that runs unattended. | Later: overnight drips of bloops into `research/bloops/` for morning triage. Note: headless runs may lose interactively-authed tools like `last30days`. |

**When do you fan out vs. just do it yourself?** Reach for a Workflow when the work is
**parallel** (five research lenses at once) or needs **independent verification** (a
skeptic checking a claim it didn't make). Do *not* fan out to author a single coherent
document or make one judgment call — that just fragments the work. We built this engine
by hand for exactly that reason; we run *bloops* as Workflows for exactly the opposite one.

---

## 3. Anatomy of one bloop

A bloop is a single run of the `bloop-dive` Workflow against one **target** (a pedal, a
plugin, a technique, a question). It runs four phases:

```
target ──▶ [1 · RECON]   1 sub-agent reads what the corpus ALREADY holds for this
                          target (DeepResearch, UsageGuide, GearProfile, links,
                          transcripts) → returns "known" + the specific GAPS to fill.
                          This is how a bloop LAYERS on prior passes instead of redoing them.
                                   │
                                   ▼
           [2 · FAN-OUT]  ~5 sub-agents in parallel, one research lens each:
              • Official / manual / firmware      • Community / forum gotchas
              • Video / tutorial settings          • Technical / MIDI + ARLO control surface
              • Comparison / role-in-your-rig
              Each returns SOURCED, structured findings. (Optional last30days lens for
              fresh signal — firmware, deals, new techniques in the last 30 days.)
                                   │
                                   ▼
           [3 · VERIFY]   skeptic sub-agents adversarially check the notable claims —
                          is it sourced? accurate? not hallucinated? — and flag the shaky ones.
                                   │
                                   ▼
           [4 · SYNTHESIZE]  1 sub-agent writes ONE digest to research/bloops/<date>-<slug>.md
                             in the house format, and returns a COMPACT summary:
                             verified findings · suggested corpus edits · candidate
                             index-chunks · NEW follow-up questions for the queue.
```

**The Workflow writes only to `research/bloops/`.** Nothing touches the per-item corpus,
the suggestion index, or the v2 app without you saying so. That separation is the whole
"raw → triage → promote" discipline.

---

## 4. The loop flow: what `/bloop` does

`/bloop` is the steering wheel. One invocation:

1. **Assemble the agenda** — read `research/queue.md`, run a quick gap-scan, optionally
   pull `last30days` signal, note any active music goal. Produce a short ranked "on deck"
   list.
2. **Ask you** — *"Here's what's on deck. Pick one, combine, or name something else."*
   ← your stop #1. Nothing runs until you choose.
3. **Run** the `bloop-dive` Workflow on the chosen target (background; watch in `/workflows`).
4. **Report + propose promotions** — show the digest summary; offer the corpus edits /
   index-chunks / v2 items for a yes/no. ← your stop #2.
5. **Update state** — mark the target done in `queue.md`, **append the follow-up questions
   the bloop surfaced** (this is the chaining — each pass seeds the next), and add a line
   to `research/log.md`.
6. **Offer to loop** — *"Next one?"* Back to step 1, or stop. ← your stop #3.

```
   you ─▶ /bloop ─▶ agenda ─▶ ❓"what next?" ─▶ bloop runs in isolated context
                                                         │
                                              compact summary returns
                                                         │
                                   ❓"promote? loop again? stop?" ─▶ ◀ HARD STOP ▶
```

---

## 5. The files

```
research/
  playbook.md         ← you are here. the pattern + primer (rarely changes)
  queue.md            ← the bloop queue: ranked targets + open questions from past bloops
  log.md              ← one line per bloop: date · target · where it wrote
  build-inventory.sh  ← regenerates the deterministic corpus inventory for the gap-scan
  bloops/             ← one dated digest per bloop, PRE-triage (your staging area)
    2026-06-19-<slug>.md
  _promotions/        ← findings staged for later append into v2's chunks.jsonl
.claude/
  workflows/bloop-dive.js     ← the Workflow that runs one bloop (read it to learn sub-agents)
  workflows/bloop-gapscan.js  ← the Workflow that sweeps the corpus + seeds the queue
  commands/bloop.md           ← the /bloop steering command (the loop driver)
```

Your existing `gear/<Device>/research/` and `software/<Plugin>/research/` folders stay the
**source of truth**. `research/bloops/` is a loading dock, not a warehouse.

---

## 6. The agenda: how a target gets chosen

Four sources feed the "on deck" list. You always have the final say.

- **The queue** (`queue.md`) — what you intentionally want, plus follow-up questions past
  bloops surfaced. The primary driver.
- **Gap-scan** — an automated sweep of `gear/` and `software/` for missing or thin
  artifacts: no UsageGuide, no DeepResearch, no MIDI CC map, stale or stub files. Keeps
  the loop self-feeding when the queue runs dry.
- **Fresh signal** (`last30days`) — what's *new* in the last 30 days about your gear and
  topics: firmware, techniques, deals, releases.
- **Music goal** — an active track or song (e.g. a Cold-wire piece). When set, the agenda
  biases toward research that serves the music in progress, not gear for its own sake.

v1 leans on the **queue + gap-scan** (always local, always available). `last30days` and
the music goal ride along as optional per-run enrichers.

---

## 7. The output: routing a finished bloop

Every bloop lands first in `research/bloops/`. From there, **you** trigger promotion —
nothing is automatic. Four destinations (sequenced, not all at once):

1. **Per-item corpus** (v1, primary) — fold verified findings into
   `gear|software/<Target>/research/<Target>-DeepResearch.md` and `-UsageGuide.md` in the
   house format.
2. **Research inbox** (v1) — the `research/bloops/` digest itself *is* the inbox. Triage it,
   then promote or discard.
3. **Suggestion index** (promote-on-review) — turn confirmed findings into chunks appended
   to v2's `chunks.jsonl`. Done from the main tree, since `v2/` is its own repo and is not
   present in this worktree.
4. **ARLO v2 docs/data** (promote-on-review) — findings that affect the app (MIDI maps,
   feature ideas, competitor patterns) flow into `v2/research` or `v2/docs`.

Keeping 3 and 4 as deliberate promotion steps is what keeps the suggestion index clean —
only verified, reviewed findings ever reach ARLO's brain.

---

## 8. How to run it

**Default — stay in your seat, gate by hand:**
```
/bloop          # assembles agenda, asks what's next, runs one bloop, asks before promoting
```
Repeat `/bloop` for each layer. Each run is isolated, so your steering thread stays light.

**When your steering thread itself gets heavy:** open a fresh Claude session and run
`/bloop`. It reloads everything from `queue.md` + `log.md`. The work doesn't miss a beat.

**Hands-free (optional):** drive `/bloop` with the `/loop` skill, self-paced, when you have
a trusted target list and don't want to gate every single pass.

**Away from the desk (later):** a `/schedule` routine drips bloops overnight into
`research/bloops/` for you to triage in the morning.

| Situation | What runs the bloop |
|---|---|
| Quick/medium target, stay in the thread | **Sub-agents via the Workflow** (default) |
| Steering thread getting long | **Fresh session** → `/bloop` reloads from disk |
| Research while you're away | **`/schedule`** (later add-on) |

All three read and write the same files. You are never locked in.

---

## 9. Glossary

- **Bloop** — one run of the `bloop-dive` Workflow against one target; produces one digest.
- **Blooping** — running the loop: bloop, gate, bloop, gate.
- **Target** — what a bloop researches (pedal, plugin, technique, question).
- **Lens** — one research angle inside a bloop (official, forum, video, technical, comparison).
- **Digest** — the dated file in `research/bloops/` a bloop writes.
- **Promotion** — your deliberate move of findings from a digest into the corpus / index / v2.
- **The gate** — the human stop before and after each bloop. Non-negotiable; it's the point.

---

## 10. Lessons from the first runs (Big Time + MOOD MkII)

The first production bloops taught the engine four things — the first three about
**sub-agents being confidently wrong**, the fourth about the staging boundary — all caught by
the human gate / `git diff`:

1. **Sub-agents reason from `git log`, not just file content — and an uncommitted worktree
   fools them.** A layer-2 agent declared a chain "never fixed" because `git log` showed no
   commit — but the fix was sitting uncommitted in the working tree. → **Commit between
   bloops** so later passes see a consistent history.
2. **Sub-agents will act on a flawed instruction if you let them.** One was told to fix a
   "broken path" that didn't exist in its file; it verified and declined instead of
   fabricating a change. → Brief agents to **verify before editing**, and always review the
   **`git diff`** — the diff is the gate, not the agent's report.
3. **Don't trust counts in the brief.** An agent told to stage "15 chunks" found the digest
   held 14, counted them, and staged 14. → Let agents re-derive facts; treat orchestrator
   numbers as hints.
4. **A `focus` that says WHERE to write breaks the staging boundary** (MOOD MkII, 2026-06-20).
   The focus said "capture the CC chart *into* `research/links/…`"; the lens agents have Write
   tools and obeyed — writing the chart + a downloaded PDF straight into the corpus, bypassing
   the gate. Worktree isolation caught it (uncommitted, reviewed via `git diff`). → `bloop-dive`
   now carries a **staging guard** (research passes write nothing; synthesis writes only the
   digest; the guard overrides any "capture into" wording), and `/bloop` composes `focus` as
   WHAT-not-WHERE plus a post-dive `git status` staging check.

And the payoff the philosophy promised: **the loop reinforced the truth.** Layer 2 corrected
and *upgraded* layer 1's own outputs (reworded an over-confident Env-polarity claim; promoted
a patch from "provisional" to "manual-confirmed"). A single pass can be wrong; the blooper,
run again, sharpens it.

---

*Pattern status: v1 — built, validated, hardened. Steps (1) `bloop-dive.js` + gap-scan-seeded
`queue.md` and (2) the `/bloop` command are DONE; proven on two Big Time bloops (loop
self-corrected) and a MOOD MkII production bloop (which surfaced + drove the staging guard).
Remaining: (3) optional `/schedule` overnight drips.*
