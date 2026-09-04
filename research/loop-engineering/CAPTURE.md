# Loop Engineering — idea capture

> Living scratch doc. We're collecting raw material toward a skill (working title: **Loop Engineering**).
> Source: idea dumps fed in by Col. Append freely; this is NOT a spec yet.

## Through-line so far
Stop engineering the *workflow*; engineer the *loop*. State a goal, let the agent write
dynamic code-mode orchestration to drive sub-agents through work→verify until the goal's
acceptance criteria are met, isolate context per concern, emit a readable artifact to gate on.
Simplicity + goal-first + self-verification + the right context boundary.

---

## The Claude Code primitives worth building on
(the "things I liked about Claude" — the raw building blocks)

### A. Context loaded *at skill-load time* (scripts in skills)
- A skill can run a script so the model **knows things the moment the skill loads** —
  e.g. repo-explorer lists "current cache contents" automatically — instead of
  load → act → act. Cuts the skill in half, more reliable/resilient.
- Pattern: open the skill body with the *result* of a listing, then branch on it.

### B. Composable context (CLAUDE.md `@import`, claude.local.md)
- `@path` imports, recursive up to 4 hops. Pull in README / package.json / `@AGENTS.md`.
- `claude.local.md` = personal overrides, gitignored, don't affect the team.
- AGENTS/CLAUDE.md as a **letter of intent** ("give it your psychosis") — not file paths.

### C. Code-mode dynamic workflows  ← the centerpiece
- Agent writes **throwaway JS** to orchestrate sub-agents. "You can never be more dynamic
  than code." Code is a *step between model runs*, not just an output.
- Shape: `meta` export (name + phases) → staged **audit → rule → verify**.
  - Schemas for structured returns (audit / ruling / verdict).
  - Prompt-generator **functions** (template string per item; inject `today`; ternary for priors).
  - `pipeline(clusters, stage1, stage2, …)` — dynamic, phases not strictly ordered.
  - **Adversarial verifiers** ("try to refute this using actual repo state; default to refuted").
  - Pull **priors from memory** (past tournament results, what's merged).
- "Output the code before you run it so we can read it together." ← gate the orchestration.
- ⚠️ Budget: burns tokens hard (~$100/10min on Fable). Orchestrate with cheaper models
  (Sonnet/Opus/Haiku) under a Fable conductor.

### D. Goal-bounded loops / run-until-clean
- Loop the agent until CI / Code Rabbit feedback comes back **empty**.
- **Self-verification**: give the agent the tools to prove its own work (CLI, test suite,
  computer-use, deploy-and-check) so when it pings you, it's actually done.

### E. Context isolation per concern
- One concern per thread; **fresh thread per concern** — stale context biases the model.
- Ephemeral **worktrees** for spin-up → PR → drop.
- Channel-level memory that **accumulates** (the Claude Tag insight): the right boundary
  for context+tools is the channel/task, not global-vs-project.

### F. Artifacts & ergonomics
- **HTML plan/digest** output — read it, gate it, hand to a fresh thread to build.
- `/bg` (by-the-way) side questions without derailing the main run.
- branch / rewind. Deep links (`claude://`) to launch sessions. Remote/async control.
- Scheduled self-tasking (cron → generates an HTML page in its own thread).

---

## Open questions for Col
- One skill (`/loop`) or a small family (loop + verify + isolate)?
- First *real* loop to ground it in (push OT-4b? PR audit? churn?) — avoid abstract.
- Does this absorb the earlier `/goal` idea, or sit beside it?

## The attack playbook (distilled)

**0. Frame** — fresh thread, one concern. Goal = outcome in 1-2 sentences. Name the done-condition.
**1. Align** — let it restate goal + acceptance criteria. Correct by reading, not detail-dumping. Trust it to find files.
**2. Size** — unsure? ask "how big?" Small → stay on main. Big/risky → ephemeral worktree.
**3. Plan (big only)** — model writes a short HTML/MD plan. Read → gate → hand to a fresh thread.
**4. Build** — simple prompt, let it write code. Don't name files.
**5. Verify** — agent proves its own work (tests / CLI / run the app). Loop until clean. No "looks done."
**6. Gate** — read the diff + artifact. PR only when it needs eyes (security / hosting / large).
**7. Done = criteria verified true.** Commit. New thread for the next concern.

**Escalate to a code-mode workflow when:** many similar items (audit/migrate/sweep) → fan out
sub-agents `find → rule → verify`, output the code before running, cheaper models under the conductor.
Otherwise: solo, conversational. ⚠️ Workflows burn tokens — budget first.

## Dumps ingested
1. "How I used to code 4 weeks ago" — simplicity, goal-first, steer-by-reading, thread-per-concern.
2. "Some things I like about Claude Code" — skills-with-scripts, @import, code-mode workflows, /bg, worktrees, rewind/branch, remote.
3. "The next coding paradigm" (Claude Tag) — channel-as-context-boundary, multiplayer/async, thread-per-task, accumulating memory, model-switching, agents-calling-agents.
