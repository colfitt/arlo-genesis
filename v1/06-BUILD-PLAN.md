# 06 — Build Plan

Phased, local, engine-first. Each phase has a **"done when"** so progress is unambiguous. Do not start a phase before the prior one's gate passes.

## Phase 0 — Project home + data wiring  *(half a day)*

- Decide the **project home** (this kit lives in `/Users/cfitt/Dev/arlo-genesis`; the home can be the same or a sibling — decide here).
- Create the [04](04-USING-IT-WITH-CLAUDE.md) layout: `CLAUDE.md` stub, `.claude/skills/`, and `data/` symlinks to the three real folders.
- Add a small **config** (one file) holding the three paths so nothing is hardcoded across the project.

**Done when:** from the home, `claude` can read a `GearProfile.md`, a `SoftwareProfile.md`, and a corpus file via its file tools.

## Phase 1 — ARLO engine (the crux)  *(1–2 days)*

- Write **`CLAUDE.md`** = ARLO persona: voice, honesty rules, the data map + frontmatter schemas, the own-only inventory rule, the citation rule, "re-read `research/`."
- Build **3–4 skills**: `gear-lookup`, `chain-design`, `software-pick`, `song-skeleton`.
- Add the **persona toggle** convention (persona-on = run in the home; persona-off = plain claude) so you can shape it / play with raw data.

**Done when:** the [02](02-USE-CASES.md) acceptance test passes — ask use-case #1, get a chain built only from owned gear, with ≥1 real citation, **without pasting data**.

## Phase 2 — Retrieval (scale the grounding)  *(1–2 days)*

- Stand up an **embedding index** over `chunks.jsonl` + `research/` (ChromaDB or similar; rebuildable from markdown).
- Expose it via a **`corpus-mcp`** (`search_corpus`) and a **`gear-mcp`** (`list_gear`/`get_gear`, software too). Mirror odysseus's `rag_server.py` / `memory_server.py` patterns.
- Point ARLO's skills at the MCP for retrieval instead of raw grep where it helps.

**Done when:** corpus-cited answers (use-cases #8/#9) return relevant chunks via search, not full-file reads.

## Phase 3 — Seed/grow the data with claude  *(ongoing, parallelizable)*

This is "use claude to seed as much data as I can":

- **Fire the arlo corpus dispatchers** that are *ready to fire* — the **AESTHETIC** and **ALBUMS** streams (`*-PROMPTS.md` + `*-SESSIONS.md`); re-run `scripts/export_chunks.py` to refresh `chunks.jsonl`, then re-index (Phase 2).
- **Expand gear/software `research/`** via a subagent skill: pick a device with thin research, deep-research it, write back into its `research/` folder (keeps the "constantly compiling" loop going, now claude-driven).
- Keep everything **markdown-canonical**; the index is regenerated.

**Done when:** a measurable jump in corpus/research coverage, re-indexed, and ARLO answers improve on a fixed question set.

## Phase 4 — UI  *(spike first, then build)*

- **Spike the open question** from [05](05-UI-DIRECTION.md): does the UI need music-specific surfaces, or is chat + gear sidebar + documents enough?
- **Spike Option 3:** can odysseus host ARLO as its agent and show your folders in the sidebar? Timebox it.
- Based on the spikes, either adopt odysseus (Option 1/3) or build a thin custom UI (Option 2) reusing the Tauri design language.

**Done when:** you can run a use-case end-to-end in the chosen UI, against real data, locally.

## Sequencing notes

- Phases 0–1 deliver a **usable ARLO** (CLI). Ship/​use it before touching UI.
- Phase 3 can run in parallel with 2/4 once retrieval exists.
- Nothing here requires the prior Tauri app; it's reference only.
