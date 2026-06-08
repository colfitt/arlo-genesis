# patchbay v4.0 — The Bridge

**Milestone brief for the `patchbay-plugin` repo.** Drop this into `.planning/` and run
`/gsd-new-milestone` (or `/gsd-ingest-docs`) to formalize it into phases + plans.

> **One-line goal:** Free patchbay from Claude (make every capability callable over MCP/CLI by
> a local model) and extend it across the **physical↔digital bridge** — presets, MIDI, Ableton —
> so it becomes the capability engine behind ARLO + an odysseus shell.

---

## Where patchbay is today (read before planning)

| Milestone | Status |
|---|---|
| v1.0 `dialed-in` | ✅ shipped 2026-05-07 |
| v2.0 gear-knowledge (`ingest`, `research`, citations) | ✅ shipped 2026-05-18 · 138 tests |
| **v3.0 `finish-a-damn-song` (ARLO)** | ▶ **90% — paused at the KNOW-04 seed-source gate** |
| v3.1 markdown-canonical | ⏸ paused (HTML renderer judged not load-bearing) |

**Prerequisite P-0 (not new work, but do it first):** finish v3.0. Populate
`arlo/sources/SEED-PLAN.md` with ~5 canonical sources and run the final ingest + verification.
Don't open a new milestone with ARLO sitting at 90%.

## What v4.0 is (and isn't)

v4.0 is the **model-agnostic + bridge** milestone. It does two strategic things:

1. **Liberates** patchbay's capabilities from the Claude Code runtime by exposing them over **MCP/CLI**,
   so a local/free model (via odysseus) can drive them. This realizes the *useful* half of the paused
   v3.1 (model-agnostic retrieval) without resurrecting the HTML renderer.
2. **Bridges physical↔digital** — pedal presets, MIDI hardware control, and Ableton — so patchbay can
   theorycraft chains, recreate rigs in the box, and set up sessions.

**Not in v4.0:** the combined patchbay+Ody shell (that's Track C, a separate later effort);
`add-gear` / `soundcheck` / `purge` (stay deferred unless pulled in); the v3.1 HTML renderer.

## Data wiring (decided)

Capabilities read canonical data **in place** via `patchbay.yml` — no migration into patchbay
(this supersedes the paused v3.1 sub-spec 3, which proposed the reverse):

```yaml
gear_root:     /Users/cfitt/Dev/Pedalxly/Gear
software_root: /Users/cfitt/Dev/Pedalxly/Software
arlo_root:     /Users/cfitt/Dev/arlo-genesis/arlo   # canonical ARLO corpus, as of 2026-06-04
```

---

## Phases

Each maps to the `roadmap.html` Track-B tags. Effort is rough; GSD will split into plans.

### Phase B0 — Liberate patchbay (MCP/CLI surface) · **keystone**
- **Goal:** patchbay's core verbs are callable by a non-Claude agent (odysseus on a local model),
  not only as Claude Code skills.
- **Delivers:** an MCP server (Python MCP SDK — matches patchbay *and* Ody) exposing:
  `list_gear(filter)`, `get_gear(name)`, `search_knowledge(query, scope)`, `research(gear)`,
  `ingest(gear, source)`, `tone_chase(...)`, `dial_in(...)`. Thin CLI wrappers for the same verbs.
  Reuses existing Python helpers; the research dispatcher already takes injected MCP tool callables.
- **Done when:** from a local-model Ody agent (no Claude, no pasting), calling `search_knowledge` /
  `get_gear` returns grounded, **cited** results from the per-gear `chunks.jsonl` + arlo corpus.
- **Depends on:** P-0; data wiring above.
- **Effort:** Med. **This phase unblocks everything else.**

### Phase B1 — Pedal preset save / recall
- **Goal:** capture and recall device presets as structured, cited markdown (and exportable files).
- **Delivers:** a `preset` capability — save a named preset for a device (knob state in the existing
  clock-position format, consistent with `dialed-in`), list/recall, export `.syx` where the device
  supports SysEx. Stored under `<gear_root>/<Brand Item>/presets/` (folder already exists).
- **Done when:** save → list → recall a preset for a MIDI-capable pedal; format matches `dialed-in`.
- **Depends on:** B0 (reachable over MCP). **Effort:** Low–Med.

### Phase B2 — MIDI control  *(folds in patchbay's deferred `patchbay:midi`)*
- **Goal:** produce MIDI artifacts and send real-time MIDI to hardware.
- **Delivers:** (a) `.mid` clip + `.syx` dump generation (pure file writes); (b) a small Rust/Node
  `midir` sidecar for real-time CC / Program-Change / SysEx; (c) the sidecar wrapped as `midi-mcp`
  (`midi.send`, `midi.program_change`, `midi.sysex`); (d) a MIDI-CC reference built from already-ingested manuals.
- **Done when:** a generated `.mid` opens in Ableton; a real CC sent to a connected pedal changes it;
  the CC cheat-sheet is generated from owned-gear manuals.
- **Depends on:** B0; B1 (presets feed SysEx). **Effort:** Med. *(Claude can't open CoreMIDI — hence the sidecar.)*

### Phase B3 — Ableton bridge (MCP)
- **Goal:** bridge physical signal chains ↔ Ableton; author Live artifacts, then (later) control Live.
- **Delivers:** **authoring first** — generate `.als` session scaffolds + `.adg` device/rack presets
  from a chosen chain or song setup (deterministic gzipped-XML writer); translate an owned-pedal chain
  ↔ an owned-plugin chain. **Runtime control second** — via a community Ableton MCP (spike to verify):
  create tracks, load devices, set tempo.
- **Done when:** "build an Ableton session for [chain/song]" emits an `.als` that opens with the
  intended tracks/devices; *(stretch)* a live command creates a track in a running set.
- **Depends on:** B0. **Open question:** authoring vs runtime first (see below). **Effort:** Med–High.
  **Spike required** (`.als` format + Ableton MCP feasibility).

### Phase B4 — Research goes local
- **Goal:** patchbay's deep-research runs on local/free models — close the cost loop.
- **Delivers:** the research synthesis + citation steps become model-agnostic via the B0 seam,
  runnable against a local model (Ollama) hosted by Ody or standalone. Ships with a **fixed eval set**
  (held-out gold gear answers) gating local-model output on the citation/grounding bar.
- **Done when:** a `research(gear)` pass completes on a local model with citations meeting the eval bar;
  Claude is opt-in for hard cases only.
- **Depends on:** B0. **Effort:** Med. **Honest risk:** local models are weaker at synthesis/citation
  discipline — the eval gate + Claude fallback exist precisely for that.

### Phase B5 — Ableton Extensions toolkit · **LAST**
- **Goal:** patchbay authors Ableton Extensions and suggests actions to build into them.
- **Delivers:** an extension-builder capability — scaffold a minimal Extension; AI suggests actions
  derived from the user's gear/workflows; connect patchbay's knowledge to the extension surface.
- **Done when:** generate a minimal working Ableton Extension exposing ≥1 patchbay-driven action.
- **Depends on:** B3; Ableton's Extensions API maturity. **Effort:** High. **Spike the API first** (brand-new surface).

---

## Sequencing

```
P-0 finish v3.0 ──▶ B0 (keystone) ──┬──▶ B1 ──▶ B2
                                    ├──▶ B3 ──▶ B5 (last)
                                    └──▶ B4
```
B0 gates all of v4.0. After B0, B1→B2 (presets→MIDI), B3 (Ableton), and B4 (research-local) can
proceed in parallel. B5 is last and depends on B3.

## Cross-cutting principles (apply to every phase)

- **MCP-first / model-agnostic** — every new capability is reachable over MCP/CLI, never Claude-only.
- **Markdown canonical** — artifacts stay source-cited markdown; chunks/indexes are derived caches.
- **Citation discipline preserved** — all research + recommendations remain cited (carry v2.0 rules).
- **Inventory-honest, GAS off by default** — recommend owned gear unless explicitly asked.
- **Local/free is the runtime target; Claude is an opt-in seeder.**

## Open questions (resolve at planning)

1. **MCP framework** — Python MCP SDK (matches patchbay + Ody)? Confirm.
2. **Ableton order** — author `.als`/`.adg` first, or runtime control first? (Recommend authoring first.)
3. **Local model bar** — which onboard/free model + runner clears the B4 research eval gate?
4. **v3.1 disposition** — does v4.0's model-agnostic work formally supersede paused v3.1 sub-spec 2,
   or does v3.1 stay parked separately?
5. **Songs** — where do song files live, and are they in scope for the Ableton/authoring phases?

---
*Authored 2026-06-04 from the arlo-genesis roadmap (Track B). Cross-ref: `arlo-genesis/roadmap.html`.*
