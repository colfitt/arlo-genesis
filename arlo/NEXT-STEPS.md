# ARLO Next Steps

**Status:** paused for current research pass to complete (30 batches across aesthetic + albums streams). Resume planning after batches finish.

This doc captures **what's pending**, **what we've learned**, and **what to do differently in the next research pass** before continuing.

---

## Current state (snapshot)

- **Repo:** [github.com/colfitt/arlo](https://github.com/colfitt/arlo) (private). Commit `c4b4850`.
- **Content:** 38 seed files generated, 127 more planned across:
  - 12 aesthetic batches (A1–A10 + T1 + T2) → ~38 files
  - 18 album batches (AL1–AL18) → ~89 files
- **Dispatch surface:** `QUICK-DISPATCH.md` — 30 sessions × 2 prompts (kickoff + verify), all paste-able.
- **What's running:** whatever batches you fire from your own Claude Code sessions over the next ~few days.
- **What I'm not doing:** no more batches, no more anchors, no more PROMPTS / SESSIONS changes until you say go.

---

## Why pause before more dispatching

Three reasons to take a breath after the current pass:

1. **Tool quality.** The current research pass uses agents with WebSearch + WebFetch. That tooling reliably hits top-5 sources per topic but rarely goes deeper. The next pass should use **Claude Deep Research** (the proper feature, not agent-style web scanning), which produces longer, more cross-referenced reports.

2. **Source completeness.** Many of the canonical sources for this aesthetic are **YouTube-only** (interviews, rig rundowns, masterclasses, documentaries). Caption quality varies — auto-captions hallucinate proper nouns, miss technical terms, drift on accented speakers. **Whisper transcription** produces dramatically better source-of-truth for those.

3. **Integration design.** The patchbay-plugin integration path (`ARLO_KNOWLEDGE_PATH` config setting) needs to be sketched concretely before we generate too much more content. If the spiked chunk schema requires structural changes, we want to apply them to the master template *before* firing more batches, not after.

---

## Lessons learned (Phase 1 research pass)

### What worked well

- **Chunk-shaped markdown** — H2 sections at 100–250 words each produce naturally embed-sized chunks
- **Anti-hallucination guard** — agents honestly flag weak-verification spots instead of fabricating
- **Pre-cluster batching** — grouping albums/artists by production-era / genre lets the agent re-use cluster-shared techniques (WhoSampled cross-checks for hip-hop, pre-1975 engineer-credit warnings for art-rock, etc.)
- **Cited Retrieval Topics footer** — every file ends with 5–10 conversational query phrasings; these are gold for benchmark sets
- **Inline citations** (markdown links within sentences) — these directly become the source-map for the hover-to-source UX downstream
- **Per-batch hallucination instructions** — telling the agent "the Coodercaster pickup config is from Lindley + Valco; verify before citing" caught specific risks in advance
- **Reroutes** (e.g., Talking Heads *Remain in Light* as album not artist file) — avoided content duplication across streams

### What didn't work as well

- **Web-scanning agents plateau quickly.** Top 5 sources are hit; the same 5 keep appearing across batches. Doesn't reach deeper sources (academic papers, full-length interviews, podcasts).
- **YouTube caption quality is unreliable.** Andrew Bird's pedal-board breakdown, Pikelny's banjo lessons, Premier Guitar Rig Rundowns — all caption-only currently. Agents either skip them or grab clearly-wrong caption fragments.
- **Mythologized albums** (Joy Division *Unknown Pleasures*, Beasties *Paul's Boutique*, Bowie Berlin Trilogy) have rich apocryphal fan-forum lore — agents sometimes grab those instead of citable production-magazine sources. The anti-hallucination guard helps but isn't perfect.
- **Recent releases** (Clipse *Let God Sort Em Out*, Cameron Winter *Heavy Metal*) have light press coverage and high hallucination risk. Worth re-doing once more interviews emerge.
- **Outsider/cult albums** (Threebrain, The Unicorns) are X-tier — agents can produce short honest files but the corpus value is genuinely low. Acceptable as-is.
- **No structured chunk schema enforcement** — current files conform to a *convention* (the master template) but nothing validates schema-correctness. A linter / validator would catch drift.

---

## Improved tooling for the next research pass

### 1. Claude Deep Research

The big upgrade. Instead of dispatching general-purpose agents with WebSearch+WebFetch, use Claude's actual **Deep Research** feature (available in claude.ai chat, not Claude Code agents) for the higher-value files.

Why it's better here:
- **Multi-source cross-referencing.** Deep Research traces claim-to-source-to-corroboration chains across 20+ sources per query, not 5.
- **Real document fetching.** Reads full academic papers, longer-form interviews, archival material that WebSearch summaries miss.
- **Structured citations.** Produces clean inline citations with deep links that already match our hover-to-source UX target.
- **Longer focused output.** Single Deep Research run can replace 5–10 separate agent runs on the same topic.

Tradeoffs:
- One run at a time (not parallel like agents)
- Burns more compute per query
- Different output format — needs a post-processing step to match ARLO's master template

**When to use it:**
- High-priority files where current output is thin (mk.gee, Threebrain, recent releases)
- Files where agents flagged "weak verification" in their reports
- New anchors when ARLO expands further
- Any topic where you want a longer-than-2500-word treatment

**When NOT to use it:**
- Bulk fills where 1500-word standard files are fine
- Topics already well-covered by current agent output

### 2. Whisper YouTube transcription

The other tool gap. For YouTube-only sources (rig rundowns, masterclasses, long-form interviews, documentaries), Whisper produces:
- **Accurate proper nouns** (gear names, producer names, studio names) — where auto-captions fail
- **Punctuation and structure** — auto-captions are a wall of text
- **Speaker identification** (with `--diarize` mode) — useful for multi-person interviews
- **Timestamp-anchored** — every line has a millisecond timestamp = perfect for the hover-to-source UX (jump-to-moment)

**Workflow sketch:**
```
1. yt-dlp to grab audio-only (smallest file)
2. whisper (or whisper-cpp / whisperX for diarization) → SRT or JSON transcript
3. Save raw transcript to corpus/transcripts/{video-slug}.srt
4. Run a dedicated "transcript-to-chunks" prompt that produces an ARLO-shaped markdown file with timestamp citations
5. The hover-to-source can now jump to mm:ss in the original video
```

**High-leverage targets to transcribe:**
- Premier Guitar Billy Strings Rig Rundown (already cited via captions — should be Whisper'd)
- KNOBs pedal demos (text-on-screen, not spoken — Whisper less useful here)
- Switched On Pop episode on mk.gee (the deep-analysis podcast format with transcript already partly available, but Whisper would be more rigorous)
- Tape Notes podcast episodes (cherry-pick 8–15 — the John Kennedy interviews are exactly the right format for chunking)
- Any Sound on Sound video interviews
- A.G. Cook YouTube interviews on PC Music
- BCNR's "How They Made *Ants From Up There*" YouTube doc

### 3. (Optional) Structured-output prompts

Currently the master template produces markdown — flexible, but no schema enforcement. Tradeoff to consider:

| Approach | Pro | Con |
|---|---|---|
| Current: markdown convention | Human-readable, flexible | No validation; drift over time |
| Strict YAML front-matter + markdown body | Validatable + human-readable | Slightly more rigid |
| JSON chunks with markdown content fields | Fully machine-readable | Loses the "you can read a file" UX |

**Recommendation:** keep markdown body, but add a JSON schema validator that confirms every file has required front-matter fields. Run it as a pre-ingest step in patchbay. Doesn't change ARLO's content authoring; just catches drift.

---

## The patchbay integration path

### `ARLO_KNOWLEDGE_PATH` design

The integration is intentionally simple: patchbay-plugin gets a configurable path that points at an ARLO corpus directory.

```toml
# patchbay-plugin/config.toml (example)
[knowledge]
arlo_knowledge_path = "~/Dev/arlo/corpus"
# or
# arlo_knowledge_path = "/Users/cfitt/Library/arlo-corpus"
# or
# arlo_knowledge_path = ["~/Dev/arlo/corpus", "~/Library/private-notes"]
```

Patchbay's `:ingest` reads from this path (or these paths), walks the markdown tree, parses each file's chunks, embeds them, builds the index.

**Default value:** `~/Dev/arlo/corpus/`. Anyone cloning patchbay alongside ARLO gets working defaults. Anyone wanting to point at a different corpus (paid, private, friend's, generated-for-a-specific-album-project) sets a custom path.

**Multi-corpus support:** array of paths means patchbay can serve a primary public corpus + a private personal corpus simultaneously. The hover-to-source UX shows which corpus a chunk came from.

### Repo separation rationale (recap)

| Concern | Living where |
|---|---|
| Markdown content + citations + Cited Retrieval Topics | ARLO repo |
| Provenance metadata (Source: line, Tags) | ARLO repo |
| Ingest pipeline (markdown → chunks → embeddings) | patchbay-plugin |
| Vector index / SQLite store | patchbay-plugin's `data/` (generated, gitignored) |
| Retrieval logic / RAG prompting | patchbay-plugin |
| Chat surface / hover-to-source UI | patchbay-plugin |

ARLO is **data**. Patchbay is **runtime**. They communicate via the file-system path.

### File-system layout (target state)

```
~/Dev/
├── arlo/                                  ← github.com/colfitt/arlo (private)
│   ├── README.md
│   ├── PROMPTS.md / SESSIONS.md
│   ├── AESTHETIC-*.md / ALBUMS-*.md
│   ├── QUICK-DISPATCH.md
│   ├── NEXT-STEPS.md                      ← this file
│   └── corpus/                            ← target of ARLO_KNOWLEDGE_PATH
│       ├── albums/
│       ├── artists/
│       ├── techniques/
│       ├── recording/ … (etc.)
│       └── transcripts/                   ← NEW for next pass (Whisper output)
│
└── patchbay-plugin/                       ← your current repo
    ├── config.toml                        ← ARLO_KNOWLEDGE_PATH setting
    ├── src/
    │   ├── ingest/                        ← patchbay:ingest implementation
    │   ├── retrieval/
    │   └── chat/
    └── data/                              ← generated, gitignored
        ├── index.sqlite
        └── source-map.json
```

---

## Knowledge transfer plan: patchbay-plugin → ARLO

What to bring over from patchbay-plugin's spike work into ARLO before the next research pass:

### Verify the chunk schema matches

Patchbay's spike findings include a validated chunk schema (per CLAUDE.md auto-load). Before re-doing or extending corpus content, confirm ARLO's master-template output produces chunks that **already match** the spiked schema. If there's drift (e.g., a required front-matter field missing), update the master template in `PROMPTS.md` / `AESTHETIC-PROMPTS.md` / `ALBUMS-PROMPTS.md` *now* so future batches are schema-compliant.

**Action item for next session:** load the `spike-findings-patchbay-plugin` skill, compare the spiked chunk schema against ARLO's current front-matter shape, document any deltas, fix master templates if needed.

### Reuse the ingest pipeline architecture

When patchbay's `:ingest` is implemented (per spike), the implementation should:
- Read markdown from `ARLO_KNOWLEDGE_PATH`
- Parse H2 sections as chunks (this is already how ARLO content is shaped)
- Extract inline citations as source-map entries
- Use the "Cited Retrieval Topics" footer to seed a benchmark query set

ARLO's master template already produces chunk-shaped output. The ingest pipeline doesn't need to handle complex parsing.

### Cross-pollinate the prompt-engineering patterns

The batched-dispatch pattern + anti-hallucination guard + per-batch cluster-specific instructions developed for ARLO content generation are reusable patterns. They could inform:

- patchbay-plugin's own internal research workflows (when patchbay needs to fetch and chunk a new manual, for example)
- Future ARLO-content-extension workflows when expanding to new genres / eras / techniques

The pattern: PROMPTS file (templates) + SESSIONS file (kickoffs) + per-batch verification prompts. Could become a generalizable batched-research pattern in patchbay's `:research` command.

### What NOT to transfer

- patchbay-plugin runtime internals (vector store, retrieval logic, UI code) — stay in patchbay
- Plugin lifecycle / Claude Code integration layer — stays in patchbay
- Anything UI-related — stays in patchbay

---

## After-current-research-pass roadmap

Once all 30 batches have been fired and verified, here's the phased plan:

### Phase 1 — Audit + validate current corpus (1–2 sessions)

- Read 10–15 sample files at random across the corpus
- Spot-check 3–5 specific factual claims per file
- Categorize each file: **Keep** (good as-is) / **Supplement** (add Deep Research depth) / **Re-do** (current output too thin or risky)
- Pay special attention to flagged-weak files (mk.gee, Threebrain, Clipse 2025, recent releases)

### Phase 2 — Deep Research enhancements (selective, ~10–20 files)

- Pick the 10–20 files where Deep Research would meaningfully upgrade depth
- Run Deep Research in claude.ai, save outputs
- Convert outputs to ARLO master-template shape
- Replace or supplement existing corpus files

### Phase 3 — Whisper transcripts (Tape Notes + key YouTube)

- Set up the yt-dlp + Whisper pipeline
- Transcribe 15–25 high-value YouTube sources (Premier Guitar Rig Rundowns, Tape Notes episodes, Switched On Pop episodes, A.G. Cook interviews, etc.)
- Save raw transcripts to `corpus/transcripts/`
- Run a "transcript-to-chunks" prompt that produces timestamp-anchored chunks
- Add these to the corpus with `Source-type: youtube-transcript` tag

### Phase 4 — Schema alignment + validation

- Verify all corpus content matches the patchbay-spiked chunk schema
- Build a simple validator script (`scripts/validate-corpus.sh` or similar)
- Run validation on the full corpus; fix any drift
- Document the schema in `corpus/README.md`

### Phase 5 — Patchbay integration (`:ingest` implementation)

- Implement patchbay-plugin's `:ingest` reading from `ARLO_KNOWLEDGE_PATH`
- Generate embeddings + index
- Build retrieval surface
- Run the ~900 Cited Retrieval Topics through the retrieval pipeline as a benchmark set
- Iterate on chunking strategy / embedding model based on retrieval quality

### Phase 6 — Chat surface + hover-to-source UI

- Build the patchbay-plugin chat command that does RAG against the corpus
- Implement structured-output so each sentence is tagged with chunk references
- Build the hover-to-source rendering (jump to source URL, or jump to mm:ss in YouTube transcript)

---

## Open questions to revisit after the pause

1. **Audiobook/podcast tier.** Whisper makes podcast ingestion tractable. Should the seed corpus include Tape Op interviews, Tape Notes episodes, Switched On Pop, Broken Record by Rick Rubin? Each one is ~5–8 chunks. 20 episodes = ~150 chunks of high-quality production-interview content.

2. **Re-ingest cadence.** When ARLO content changes (new files, edits), does patchbay re-ingest the whole corpus, or incremental? Per-file hashing + smart re-indexing is probably the right design.

3. **Multi-corpus precedence.** If two corpora have chunks about the same topic (e.g., user's private notes + ARLO), which wins on retrieval? Probably weight by recency + source-tier, but worth a deliberate decision.

4. **Embedding model.** Anthropic embeddings API? OpenAI `text-embedding-3-large`? Local model (`bge-large` / `nomic-embed-text-v1.5`)? Tradeoffs: API cost vs. local-compute requirements vs. quality ceiling.

5. **Test-query coverage.** When `:ingest` is implemented, fire all ~900 Cited Retrieval Topics through the retrieval pipeline. What % retrieve the "right" chunk in top-3? This is the canonical benchmark for the system.

6. **Acquisition delta.** The acquisition list (Senior, Pattison, Pedler, Katz, Welsh, Berklee banjo book, Brian Coleman *Check the Technique*, Brian Eno diary, Mark Lewisohn *Recording Sessions*) — when do these get acquired? Acquisition unlocks direct-quote chunks replacing the synthesis paraphrases.

7. **Public-corpus question.** Once the corpus is mature, is there a version (synthesis-only paragraphs, no direct book quotes, all citations to publicly-accessible URLs) that could be made public? Or does it stay private indefinitely?

---

## What I'm NOT doing right now

- Not dispatching any more batches
- Not adding more anchors
- Not modifying PROMPTS / SESSIONS / planning files
- Not changing corpus content
- Not building the patchbay-plugin integration yet
- Not running Deep Research or Whisper passes yet

---

## Wait condition

Resume planning + execution when:

- [ ] All 12 aesthetic batches (A1–A10 + T1 + T2) have been fired and verified
- [ ] All 18 album batches (AL1–AL18) have been fired and verified
- [ ] Verify-prompt outputs reviewed; weak/risky files flagged

After that:
1. Walk through this roadmap
2. Decide which Phase to tackle first (probably Phase 1 audit, before Phase 2 Deep Research enhancements)
3. Make any chunk-schema adjustments before any further content generation

---

## Quick reference: where things live

| Thing | Location |
|---|---|
| This planning doc | `~/Dev/arlo/NEXT-STEPS.md` |
| Repo (private) | https://github.com/colfitt/arlo |
| Active dispatch reference | `~/Dev/arlo/QUICK-DISPATCH.md` |
| Master index | `~/Dev/arlo/README.md` |
| Existing corpus | `~/Dev/arlo/corpus/` (38 files; will grow to ~165) |
| patchbay-plugin (separate repo) | `~/Dev/patchbay-plugin/` |
| Target integration config | `~/Dev/patchbay-plugin/config.toml` → `ARLO_KNOWLEDGE_PATH` |

Tell me when the research pass is done and we'll pick up from Phase 1.
