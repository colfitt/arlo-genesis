# Loop Engineering — Design

Compiled from this thread's research. Companion to [CAPTURE.md](./CAPTURE.md) (raw idea dumps).
This doc is the converging spec for a `/loop` skill.

---

## 1. Thesis

**Engineer the loop, not the workflow.** State a goal as an *outcome*. Drive it through
`align → build → verify` until the acceptance criteria are *proven* true. Spawn fresh
context (sub-agents / threads / worktrees) only when the work demands it. Steer by reading
outputs at gates. Use workflows **only** when fan-out genuinely earns it — never as default.

The skill ships **two modes on one spine**: `auto` (autonomous) and `phased` (human-in-the-loop).
Pick per task; ceremony is opt-in, never forced.

---

## 2. Compiled research

### Working-style shift (the ground rules)
- Conversational + goal-bounded. No mandatory planning ceremony, no skill-design reflex.
- Goal = outcome in 1–2 sentences. Trust the model to find files (don't name them).
- Steer by **reading what it says**, not by front-loading detail. Fix root causes, don't pile on detail.
- One concern per thread; fresh thread for a new concern.
- AGENTS/CLAUDE.md = letter of intent (how we think / what we build / why), not file paths.
- **Verification is the stopping point.** Goal met = criteria proven, not asserted.

### Claude Code primitives we're building on
| Primitive | Where it plugs in |
|---|---|
| **Skills-with-scripts** (load-time context) | `/loop` preloads goal + repo/git state on invoke → opens half as long, more reliable |
| **`@import`** / letter-of-intent | Compose goal + acceptance criteria + AGENTS.md at frame |
| **Code-mode workflows** | Fan-out stage only: `find → rule → verify`, output code before running |
| **Self-verify tools** (CLI / tests / run-app / computer-use) | The verify-loop; "actually done" before it pings you |
| **`/bg`** side questions | Steer mid-run without derailing |
| **rewind / branch** | Wrong-turn recovery; take history elsewhere |
| **Ephemeral worktrees** | Isolation for big/risky branches |
| **HTML plan / digest** | The handoff baton + the gate artifact |
| **`claude://` deep links** | Artifact that *launches* the next thread |
| **Channel-as-context-boundary** (Claude Tag) | The right scope for context+tools = the task, not global-vs-project |

### "Threads make new threads" — 3 altitudes
- **In-thread / auto** — sub-agent for isolated work (scout / verify / dive); returns *only the conclusion*.
- **Cross-thread / baton** — the plan artifact is the handoff; a fresh thread builds it with zero stale context.
- **Fleet / code-mode** — agent writes throwaway orchestration that spawns a staged sub-agent fleet.
- Rule: *different concern → new thread · isolated lookup → sub-agent · many of the same → fan-out.*

### Mid-stream steering (first-class)
- Explicit **steer-gates** after align, after plan, after verify.
- `/bg` for clarifying questions · rewind/branch for course-correction.

---

## 3. The shared spine (every mode runs this)

```
preload context  →  align on goal + acceptance criteria  →  size
   →  build  →  verify-loop (until criteria proven)  →  gate  →  done
```

Sub-agents are available at every step (see §8). The modes differ only in **autonomy**
and **structure**, not in the spine.

---

## 4. Modes

### A. `/loop auto` — autonomous development loop
For well-specified, lower-risk work. Runs end-to-end, surfaces only when it must.

```
1. Align once (skip if goal is unambiguous).
2. Derive work units from the goal/spec.
3. LOOP per unit:
     build  →  self-verify (verifier sub-agent)
            →  pass? commit + next  :  iterate (round cap)
4. STOP when:  all criteria proven  |  budget ceiling hit  |  genuine blocker.
5. On blocker: SURFACE it (don't guess). On done: final gate (default on for risky work).
```

- **Sub-agents:** scout for lookups, adversarial verifier per unit. No fan-out unless units are truly parallel.
- **Gates:** minimal. Knob: `checkpoint=every N units` if you want to peek.
- **Guardrails:** hard token ceiling; cheaper models for sub-agents; round cap on verify-iterate.

### B. `/loop phased` — human-in-the-loop, phases folder
For ambiguous / higher-stakes work. **Asks questions every time**, plans into a folder, executes phase-by-phase with a gate at every boundary.

```
1. ASK (every time): scope, acceptance criteria, constraints, risk, what's out of scope.
2. Write  phases/<slug>/PLAN.md  (+ optional PLAN.html to read/gate).
3. Write  phases/<slug>/phase-N.md  per phase: goal · blocks · acceptance test.
4. Per phase — execute, then STOP at the phase gate for human review + commit.
5. Next phase only after approval.
```

#### Option: sub-agent-driven development with **blocks**
Within a phase, decompose into **blocks** = smallest independently-verifiable units
(own goal, own acceptance test, no shared mutable state).

```
Phase
 ├─ block 1  → sub-agent: build (TDD optional) → verify → return diff
 ├─ block 2  → sub-agent: build → verify → return diff
 └─ block 3  → sub-agent: ...
        main thread: integrate → run phase-level verify → phase gate
```

- **2 blocks, sequential or independent →** dispatch sub-agents one or in parallel.
- **≥3 independent blocks worth parallelizing →** a code-mode **Workflow** (output code first).
- **1 linear block →** solo, no orchestration.

---

## 5. When to use what (the discipline)

| Situation | Tool | Why |
|---|---|---|
| 2-sentence change / single linear feature | **solo loop** | orchestration is pure overhead |
| need an isolated fact / codebase lookup | **scout sub-agent** | keeps main context clean |
| need to confirm a claim / finding | **verifier sub-agent** | adversarial, returns a verdict |
| phase with 2 independent blocks | **sub-agent per block** | parallel or sequential, no Workflow needed |
| ≥3 independent units + verify pass | **Workflow (code-mode)** | fan-out earns it; staged find→rule→verify |
| audit / sweep / migrate across many items | **Workflow (code-mode)** | the canonical fan-out shape |
| **single linear feature** | **NOT a Workflow** | this is the "overboard" trap — avoid |

**Workflow gate:** only past **≥3 genuinely independent units** that benefit from parallelism
*and* warrant verification. Always **output the orchestration code before running it**.
Cheaper models per sub-agent under a smart conductor. Budget ceiling first.

---

## 6. Budget & guardrails (DOUG's department)
- Hard token ceiling per run; loop guards on remaining budget.
- Sub-agents default to cheaper models (Haiku/Sonnet); conductor stays sharp.
- Round cap on verify-iterate so a stuck unit can't spin forever.
- Workflows: opt-in past the §5 gate, code shown first, never the default execution path.

## 7. `phases/` folder layout (mode B)
```
phases/<slug>/
  PLAN.md            # the spec, acceptance criteria, phase list
  PLAN.html          # optional readable/gateable artifact
  phase-1.md         # goal · blocks · acceptance test · status
  phase-2.md
  notes.md           # decisions, deviations, surprises
```

## 8. Sub-agent role catalog
- **Scout** (read-only) — find/answer, return conclusion only.
- **Verifier** (adversarial) — "try to refute this," return verdict.
- **Block builder** — build + self-verify one block, return diff.
- **Dive** — `/bloop`-style research into an external/thin area.

## 9. Open forks (to converge)
1. **One skill `/loop <mode>` vs two skills** (`/loop-auto`, `/loop-phased`). *Recommend: one skill, mode arg.*
2. **Auto mode final gate**: default-on for risky, default-off for green? *Recommend: on for risky.*
3. **`phases/` location**: top-level `phases/`, `.loop/`, or under `research/`? *Recommend: top-level `phases/`, gitignored if scratch.*
4. **Mode default** when invoked bare: ask which mode, or default to `phased`? *Recommend: ask once, remember.*
