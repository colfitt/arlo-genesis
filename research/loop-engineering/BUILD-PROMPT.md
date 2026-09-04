# Commission: design & build the `/loop` skill ("Loop Engineering")

> **How to use this file:** paste everything below the line into a fresh Claude Code session
> on any machine/project. It is fully self-contained — it carries all the research and intent
> it needs. It does not depend on any local files, paths, or prior memory.

---

## YOUR TASK

You are going to **design, then build, a Claude Code skill called `/loop`** ("Loop Engineering").
Work with me **conversationally** — propose, let me read and steer, gate at the key points.
Produce a real, installable skill at the end (a `SKILL.md` with frontmatter + body, plus any
small helper script you justify).

**Meta-rule for this very task:** do not over-engineer the act of building this. Do **not**
spin up a large multi-agent workflow just to write a skill file. Design it like a craftsperson
talking through a problem. The irony of burning a fortune in orchestration to produce a skill
whose whole point is restraint would not be lost on me.

---

## WHO I AM / HOW I WORK (honor this — it's the whole point)

- I build with AI **conversationally and goal-bounded**. I moved away from heavy workflow
  ceremony (rigid plan-mode, "skill for everything," parallel-worktree juggling, multi-phase
  agent fleets for trivial work). The models are good enough now that scaffolding mostly gets
  in the way.
- I state a **goal as an outcome**, then steer by **reading what the model says** and correcting
  — not by front-loading every detail. I trust the model to find the right files; me naming
  them is more likely to send it down the wrong hole.
- **One concern per thread.** Fresh thread for a new concern — stale context biases the model.
- My `CLAUDE.md`/`AGENTS.md` is a **letter of intent** (how I think, what I'm building, why) —
  not a rulebook of file paths.
- I care about **budget**. I want power, but I don't want a $100-per-10-minutes money fire when
  a single sub-agent would do.
- I already run small custom skills (e.g. a research-loop skill that spawns isolated "dive"
  sub-agents and gates results with me). I like that shape. `/loop` is the *development*
  counterpart to it.
- **Verification is my stopping point.** "Done" means proven, not asserted.

When in doubt, bias toward **simple, conversational, and verifiable** over clever and elaborate.

---

## THE BIG IDEA: Loop Engineering

**Engineer the loop, not the workflow.** Drive a goal through
`align → build → verify` until the acceptance criteria are *proven* true. Spawn fresh context
(sub-agents / threads / worktrees) only when the work demands it. Steer by reading outputs at
gates. Use code-mode workflows **only** when fan-out genuinely earns it — never as the default.

The skill ships **two modes on one spine**, chosen per task — ceremony is opt-in, never forced.

---

## INSPIRATION & RESEARCH (distilled — treat as inspiration, not law)

This draws on a set of talks about how senior builders actually use agentic coding tools now.
The distilled lessons:

**On working style**
- Prompts should usually be short — two sentences that state the *what* and the *goal*, not the *how*.
- Read the model's prose, not just its code. Steer its tone/format so you'll actually read it.
- Give examples instead of over-explaining. The smallest example that contains the problem wins.
- When the agent pushes back with a good reason, listen.
- Let the agent **verify its own work** (run tests, run the CLI, drive the app, deploy-and-check)
  so that by the time it pings you, it's actually right.
- Run agents **in a loop until external feedback is clean** (e.g. a code-review CLI returning
  no findings) instead of hand-shuttling errors back and forth.

**On orchestration ("code mode")**
- The most powerful pattern is letting the agent **write throwaway code that orchestrates
  sub-agents** — staged phases (e.g. `find → rule → verify`), structured schemas for returns,
  per-item prompt-generator functions, adversarial verifiers that try to *refute* a finding.
  "You can never be more dynamic than code." Code is a *step between model runs*, not just output.
- But it **burns tokens hard.** Use it only when the work is genuinely many independent units.
  Orchestrate with cheaper models under a smart conductor. **Output the orchestration code
  before running it** so a human can read it first.

**On context boundaries**
- The right boundary for context + tools is the **task/channel**, not "global vs project."
  Different concerns deserve different context and isolation. Threads-per-task keep unrelated
  work (and scheduled jobs) from polluting each other.

---

## CLAUDE CODE FEATURES I LOVE — AND HOW I USE THEM (design around these)

Build the skill to exploit these where the harness supports them, and **degrade gracefully**
where it doesn't (some are Claude-Code-specific; the skill should still work on a plain harness).

1. **Skills that run scripts at load time.** A skill can execute a script *as it loads* so the
   model already knows the relevant state (branch, git status, the goal, existing phases) the
   moment it activates — instead of load → discover → act. *Use this:* `/loop` should preload
   cheap state on invoke and open shorter and more reliably. On harnesses without load-time
   injection, fall back to running the same check as the first step.
2. **`CLAUDE.md` `@import` / letter-of-intent.** Compose context by importing files (`@AGENTS.md`,
   acceptance-criteria docs). *Use this:* the skill assembles goal + criteria + intent at frame.
3. **Code-mode workflows.** Dynamic staged sub-agent orchestration written as throwaway code.
   *Use this:* only behind the workflow gate (below), and only with the code shown first.
4. **`/bg` (by-the-way) side questions.** Ask a clarifier mid-run without derailing the main work.
   *Use this:* the skill expects to be interrupted and resumes cleanly.
5. **"Threads make new threads."** A thread spawns sub-agents/threads for isolated work and gets
   back only the conclusion. *Use this* at three altitudes: in-thread sub-agents (scout/verify),
   cross-thread baton hand-off (an artifact a fresh thread picks up), and code-mode fleets.
6. **Ephemeral worktrees** for spin-up → do → PR → drop. *Use this:* the skill offers a worktree
   for big/risky branches; stays on the current branch for small ones.
7. **Rewind / branch.** Course-correction without losing work. *Use this:* steer-gates assume the
   human may rewind a step and re-rule.
8. **`claude://` deep links.** An HTML artifact can render buttons that *launch* a new session
   (working dir + repo preset). *Use this:* plan/digest artifacts can emit "start the next phase"
   links. (Optional / capability-gated.)
9. **Self-verification tools** (CLI, tests, run-the-app, computer-use). *Use this:* the verify
   step is mandatory and uses whatever proof the project affords.
10. **HTML plan / digest artifacts.** Readable, gateable, and a clean hand-off baton. *Use this:*
    `phased` mode can emit a `PLAN.html` to read and approve.

---

## WHAT THE SKILL MUST DO

### Shared spine (both modes)
`preload → align → size → build → verify-loop → gate → done`

- **Preload:** capture branch, `git status`, the goal, any named spec/acceptance criteria.
- **Align:** restate the goal + acceptance criteria back to me; confirm if ambiguous.
- **Size:** small/clear → stay on the current branch; big/risky → offer a worktree.
- **Verify-loop:** build → prove it → iterate until criteria hold (with a round cap).
- **Gate:** I read the diff/artifact and steer.
- **Done = criteria verified true.** Commit. Offer the next concern as a fresh run.

### Mode A — `auto` (autonomous development)
For well-specified, lower-risk work. Run end-to-end; surface only when you must.
- Align once (skip if unambiguous) → derive work **units** from the goal/spec.
- LOOP per unit: `build → self-verify (verifier sub-agent) → pass: commit + next · fail: iterate
  (cap ~3 rounds)`.
- STOP on: all criteria proven · budget ceiling hit · a **genuine blocker**.
- On a blocker, **surface it — do not guess.** On done, a final gate (default ON for risky work,
  OFF for green). Optional `checkpoint=every N units` knob.
- Sub-agents: scout (lookups), adversarial verifier (per unit). **No fan-out unless units are
  truly parallel.**

### Mode B — `phased` (human-in-the-loop)
For ambiguous / higher-stakes work. Structured, gated at every boundary.
1. **Ask every time:** scope, acceptance criteria, constraints, risk, what's out of scope.
2. Write `phases/<slug>/PLAN.md` (+ `PLAN.html` if useful). List the phases.
3. Per phase write `phases/<slug>/phase-N.md`: **goal · blocks · acceptance test · status**.
4. Execute one phase, then **STOP at the phase gate** for review + commit. Next phase only on approval.

**Option — sub-agent-driven development with blocks.** Decompose a phase into **blocks** =
smallest independently-verifiable units (own goal, own test, no shared mutable state).
- 1 linear block → solo. · 2 independent blocks → one sub-agent each. · ≥3 independent blocks
  worth parallelizing → code-mode workflow (behind the gate).
- Each block sub-agent: build (TDD if it fits) → self-verify → return diff. Main thread
  integrates → runs phase-level verify → phase gate.

### Sub-agent discipline (the default reach when executing tasks)
- **Scout** (read-only): find a fact / map code; return the conclusion only.
- **Verifier** (adversarial): "try to refute this"; return a verdict.
- **Block builder:** build + self-verify one block; return diff.
- **Dive:** research a thin or external area.

### Workflow gate (do NOT go overboard)
Use a code-mode workflow **only** when **≥3 genuinely independent units** benefit from
parallelism *and* warrant verification (audits, sweeps, migrations, multi-block phases).
- **Never** wrap a single linear feature in a workflow — that's the overboard trap.
- **Output the orchestration code before running it.**
- Cheaper models per sub-agent under a smart conductor. Confirm budget first.
- Default execution path is **solo or sub-agents**; workflow is the opt-in exception.

### Budget guardrails
- Hard token ceiling per run; check remaining before any fan-out.
- Cap verify-iterate (~3 rounds) so a stuck unit can't spin forever.
- Sub-agents default to cheaper models.

### Steering (mid-run)
- Natural steer-gates after **align**, after **plan**, after **verify**.
- Expect `/bg` side questions without derailing; assume rewind/branch is available.

---

## SCENARIOS IT MUST HANDLE GRACEFULLY (validate the design against these)

1. **Two-sentence feature** — one solo thread, no fan-out, verify by running the app. (~80% of work.)
2. **Mid-build lookup** — spawn a scout sub-agent, get the conclusion, keep main context clean.
3. **Audit across many items** (e.g. "audit all open PRs / all config maps / all data fixtures":
   which are stale, redundant, ready) — the canonical code-mode fan-out, behind the gate.
4. **Steer mid-run** — a workflow is running, I `/bg` a clarifier, then rewind a step at the gate;
   nothing breaks.
5. **Ambiguous, higher-stakes feature** — `phased` mode: questions → phases folder → block
   execution → gate per phase.
6. **Scheduled / thread-per-task** — a recurring job that produces an HTML digest in its own
   isolated context. (Design should not preclude this.)

The insight to preserve: **all six are the same loop.** Only *how many threads it spawns* and
*whether it fans out* changes.

---

## DELIVERABLES (what I want at the end)

1. **`SKILL.md`** — frontmatter (`name`, `description`) + a tight, operational body. The body must
   be imperative ("do X"), not descriptive. Scannable, not a wall.
2. **Recommended install path** (project-level vs user-level) and why.
3. **Optional helper script** for load-time context injection — only if you justify it; keep the
   skill working without it.
4. **A short test/acceptance plan** — how we'll prove the skill behaves, mapped to the six scenarios.
5. **Graceful-degradation notes** — which features are Claude-Code-specific and how the skill
   behaves on a plainer harness.

---

## HOW TO WORK WITH ME

- Design it **conversationally**: propose the structure, let me read and steer, then write.
- Ask me **only the decisions that are genuinely mine** (see forks below) — don't fork-quiz me on
  things with an obvious default; pick the default, tell me, move on.
- Keep prompts and the skill body **simple**. If something gets complex, fix the root cause.
- **Verification is the stopping point even here:** before you call the skill "done," dry-run it
  (in your head or for real) against at least scenarios 1, 3, and 5 and show me it holds.
- Do **not** fire a multi-agent workflow to produce the skill.

---

## ACCEPTANCE CRITERIA FOR THE SKILL (we're done when…)

- [ ] `/loop [auto|phased] <goal>` works; bare invoke asks mode once.
- [ ] Both modes share one spine; the difference is autonomy + structure, not a different engine.
- [ ] `auto` stops correctly on proven / budget / blocker, and **surfaces blockers instead of guessing**.
- [ ] `phased` asks every time, writes a `phases/<slug>/` folder, and gates at every phase.
- [ ] The **blocks** option exists and routes solo / sub-agent / workflow by the §gate rules.
- [ ] Sub-agents are the **default** execution reach; workflow only past the ≥3-independent-units gate.
- [ ] Budget guardrails are explicit (ceiling, round cap, cheaper sub-agent models).
- [ ] The body is operational and scannable, and degrades gracefully off Claude Code.

---

## OPEN FORKS (decide these with me; my leanings noted)

1. **One skill `/loop <mode>` vs two skills** (`/loop-auto`, `/loop-phased`). — *lean: one skill.*
2. **`auto` final gate:** default ON for risky, OFF for green? — *lean: yes.*
3. **`phases/` location:** top-level `phases/`, `.loop/`, or under a research/scratch dir;
   gitignored if scratch? — *lean: top-level `phases/`.*
4. **Bare-invoke default:** ask mode once and remember, or default to `phased`? — *lean: ask once.*

Start by reflecting the design back to me in your own words and naming anything you'd change.
Then let's build it.
