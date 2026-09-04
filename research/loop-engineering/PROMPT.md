---
name: loop
description: Goal-bounded development loop for implementing a feature or attacking a problem, with verification as the only stopping point. Two modes — `auto` (autonomous) and `phased` (human-in-the-loop with a phases/ folder and optional sub-agent-driven blocks). Reaches for sub-agents by default; uses code-mode workflows only when fan-out genuinely earns it.
---

# /loop — Loop Engineering

Invocation: `/loop [auto|phased] <goal>` — if mode is omitted, ask once.

You run development as a **goal-bounded loop**, not a fixed procedure. Engineer the loop;
do not over-engineer the workflow.

## Prime directives
- The goal is an **outcome**, in 1–2 sentences. Restate it and the **acceptance criteria**
  before touching anything; confirm with the user if ambiguous.
- **Verification is the only stopping point.** "Done" = criteria *proven* (tests pass /
  app does the thing / output observed) — never asserted.
- Steer by **reading outputs at gates**, not by front-loading detail. Trust yourself to
  find the right files — don't make the user name them.
- One concern per run. Keep main context clean — push isolated work to sub-agents.
- Keep it simple. If a step gets complex, fix the root cause; don't pile on detail.

## On invoke (preload)
1. Cheaply capture state: branch, `git status`, the goal, any named spec/acceptance criteria.
2. Resolve **mode** (`auto` | `phased`); ask once if not given.
3. Restate the goal + acceptance criteria back to the user before proceeding.

## The spine (both modes)
`preload → align → size → build → verify-loop → gate → done`

---

## Mode: `auto` — autonomous development
For well-specified, lower-risk work. Run end-to-end; surface only when you must.

1. Align once (skip if unambiguous). Derive work **units** from the goal/spec.
2. LOOP per unit:
   `build → self-verify (verifier sub-agent) → pass: commit + next · fail: iterate (cap = 3 rounds)`
3. STOP when: **all criteria proven** · **budget ceiling hit** · **a genuine blocker**.
4. On blocker → **surface it, do not guess.** On done → final gate (default ON for risky
   work, OFF for green). Optional knob: `checkpoint=every N units`.

Sub-agents: scout for lookups, adversarial verifier per unit. **No fan-out unless units are
truly parallel.**

---

## Mode: `phased` — human-in-the-loop
For ambiguous / higher-stakes work. Structured, gated at every boundary.

1. **Ask every time:** scope, acceptance criteria, constraints, risk, what's out of scope.
2. Write `phases/<slug>/PLAN.md` (+ `PLAN.html` if useful to read/gate). List the phases.
3. Per phase, write `phases/<slug>/phase-N.md`: **goal · blocks · acceptance test · status**.
4. Execute one phase, then **STOP at the phase gate** for human review + commit.
   Next phase only after approval.

### Option: sub-agent-driven development with blocks
Decompose a phase into **blocks** = smallest independently-verifiable units (own goal, own
acceptance test, no shared mutable state).
- 1 linear block → **solo**.
- 2 independent blocks → **one sub-agent each** (sequential or parallel).
- ≥3 independent blocks worth parallelizing → **code-mode Workflow** (see gate below).

Each block sub-agent: build (TDD if it fits) → self-verify → return diff. Main thread
integrates → runs phase-level verify → phase gate.

---

## Sub-agent discipline (the default reach when executing tasks)
- **Scout** (read-only) — find a fact / map code; return the conclusion only.
- **Verifier** (adversarial) — "try to refute this"; return a verdict.
- **Block builder** — build + self-verify one block; return diff.
- **Dive** — research a thin or external area.

## Workflow gate (do NOT go overboard)
Use a code-mode Workflow **only** when **≥3 genuinely independent units** benefit from
parallelism *and* warrant verification (audits, sweeps, migrations, multi-block phases).
- **Never** wrap a single linear feature in a Workflow — that's the overboard trap.
- **Output the orchestration code before running it.**
- Cheaper models per sub-agent under a smart conductor. Confirm budget first.
- Default execution path is **solo or sub-agents**; Workflow is the opt-in exception.

## Budget guardrails
- Hard token ceiling per run; check remaining before any fan-out.
- Cap verify-iterate at 3 rounds so a stuck unit can't spin forever.
- Sub-agents default to cheaper models.

## Steering (mid-run)
- Natural steer-gates after **align**, after **plan**, after **verify** — pause; the user
  reads and redirects.
- Expect `/bg` side questions without derailing; rewind/branch for course-correction.

## Done
Goal met = acceptance criteria verified true. Commit. Offer the next concern as a fresh run.
