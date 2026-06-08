# 04 — Using It With Claude (the crux)

The whole project hinges on this: **make `claude` use the seed data correctly.** Below are the viable approaches, the recommendation, and a concrete starting layout.

## The core problem

- The data is **large** (`chunks.jsonl` alone is 5.6 MB; hundreds of profiles + research files). You cannot paste it all into a prompt.
- ARLO must **prefer your data** over generic model knowledge, and **cite** it.
- It must stay **current** as `research/` grows.

So "use it correctly" = **retrieval + persona + access**, not "stuff the context window."

## Approaches

### A. Claude Code, native (recommended starting point)

Treat ARLO as a **Claude Code project** whose working directory can reach the three folders.

- **`CLAUDE.md` = the ARLO persona.** Defines voice, the honesty principles, the rule "recommend only gear/software the user owns," and *where the data lives + how to use it*.
- **Folder access.** Either run ARLO from a home that contains (or symlinks) `Gear/`, `Software/`, `arlo/`, or list their absolute paths in `CLAUDE.md` so claude reads them on demand with its file tools.
- **Skills** (Claude Code skills) for the repeatable moves:
  - `gear-lookup` — find/own-filter devices by need; read the right `GearProfile.md` + `research/`.
  - `chain-design` — compose a signal chain from owned gear, with citations.
  - `software-pick` — recommend from `Software` by `host_in`/`subcategory`/`installed`.
  - `song-skeleton` — draft structure using a chosen `workflow/`.
  - `corpus-cite` — retrieve from the corpus and cite (pairs with retrieval below).
- **Subagents** for breadth-heavy tasks (e.g., "research this new pedal" → writes into that device's `research/`), which doubles as **data seeding** (see [06](06-BUILD-PLAN.md)).

**Why first:** lowest build cost, immediately "uses claude correctly," and it's literally the ARLO-persona idea. Proves the engine before any infra.

**Gap it leaves:** semantic search over `chunks.jsonl`. Claude can grep/read files, but true "find the most relevant corpus chunks" wants retrieval (below).

### B. MCP servers over the data

Expose the data to claude as tools (this is also how odysseus is built — it ships `rag_server.py`, `memory_server.py`):

- **`gear-mcp`** — `list_gear(filter)`, `get_gear(name)` (profile + research), same for software.
- **`corpus-mcp` / RAG** — `search_corpus(query)` over an index of `chunks.jsonl` + research.

Structured, scalable, engine-portable (works from Claude Code *or* an odysseus-style UI). Add once A proves the shape of the queries.

### C. RAG / embeddings index

Embed `chunks.jsonl` + `research/` into a vector store (e.g., ChromaDB — what odysseus uses) and retrieve top-k for grounding/citation. This is the durable fix for the "5.6 MB can't be inlined" problem. Rebuildable from markdown anytime.

## Recommendation

**Start with A; grow into B + C.**

1. Stand up the ARLO persona + folder access + 3–4 skills in Claude Code. Hit the [02](02-USE-CASES.md) acceptance test (use-case #1, cited, no pasting).
2. When grep/read stops scaling (it will, on the corpus), add a **retrieval MCP** (B) backed by an **embedding index** (C).
3. Keep markdown canonical; the index is a cache.

This sequence means ARLO is *useful on day one* and gets *smarter with retrieval* without a rewrite — and none of it locks you to a particular UI.

## Concrete starting layout (Approach A)

```
<arlo-home>/                      # the new project home (decided from this kit)
  CLAUDE.md                       # ARLO persona + data map + rules  ← the heart
  .claude/skills/
    gear-lookup/SKILL.md
    chain-design/SKILL.md
    software-pick/SKILL.md
    song-skeleton/SKILL.md
  data/                           # symlinks (or config) to the real folders
    gear      -> /Users/cfitt/Dev/Pedalxly/Gear
    software  -> /Users/cfitt/Dev/Pedalxly/Software
    arlo      -> /Users/cfitt/Dev/patchbay-ai/arlo
```

**`CLAUDE.md` must encode at minimum:** who ARLO is (voice + honesty rules), the data map (what's in `data/gear|software|arlo` and the frontmatter schemas), the inventory rule (own-only unless asked), the citation rule, and "re-read `research/`; it grows."

> This `CLAUDE.md` is the "persona" the user wants a **toggle** for ("turn off the persona to play with the data"). Implementation: persona-on = run claude in `<arlo-home>` (loads `CLAUDE.md`); persona-off = run plain claude elsewhere. The shaping of this file is the iterative "shaping project."
