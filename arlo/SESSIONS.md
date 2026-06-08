# ARLO Research Sessions — Batch Execution Plan

This file defines **12 numbered batches** that together produce all 38 seed documents. Each batch is a single kickoff message you paste into a fresh Claude Code session — Claude reads `PROMPTS.md`, executes the prompts in that batch, and writes outputs to the right corpus folder.

---

## How to run

### Serial (one session at a time)

1. Open a fresh Claude Code chat.
2. Copy the kickoff message for the batch you want to run.
3. Paste and send.
4. Wait for completion (rough estimate: 5–8 minutes per prompt; multiply by prompt count).
5. Confirm the files landed in `corpus/{scope}/`.
6. Move to the next batch.

### Parallel (multiple sessions at once)

1. Open N Claude Code tabs/windows (one per batch you want to run in parallel).
2. Paste a different batch kickoff into each.
3. Let them run concurrently.
4. Reconvene when all are done.

**All 12 batches are independent.** There are no cross-batch dependencies — every batch reads `PROMPTS.md` and writes to a different set of files. You can run them in any order, in any combination of serial/parallel.

### Practical parallelism limit

Don't run more than ~4 batches simultaneously — each does multiple web searches, and Anthropic rate limits will kick in if you saturate too hard. 3–4 parallel is the sweet spot.

---

## Batch Overview

| # | Batch | Prompts | Files written | Est. time |
|---|-------|---------|---------------|-----------|
| 1 | Recording A | 1, 2, 4 | mic-placement-by-source, signal-flow-and-gain-staging, monitoring-and-headphones | ~25 min |
| 2 | Recording B | 3, 5 | room-treatment-budget, tracking-vocals-in-the-small-studio | ~15 min |
| 3 | Mixing A | 6, 7, 11 | eq-fundamentals, compression-fundamentals, vocal-mixing | ~25 min |
| 4 | Mixing B | 8, 9, 10 | reverb-and-delay-architecture, low-end-management, mix-translation-and-reference-tracks | ~25 min |
| 5 | Mastering | 12, 13, 14 | mastering-chain-and-process, lufs-streaming-and-true-peak, limiting-dither-and-delivery | ~25 min |
| 6 | Structure | 15, 16, 17 | pop-song-forms, section-function, arrangement-arcs-and-transitions | ~25 min |
| 7 | Harmony | 18, 19, 20, 21 | pop-chord-progressions, modal-interchange, secondary-dominants, voice-leading | ~30 min |
| 8 | Melody | 22, 23 | melodic-contour-and-motif-development, hook-construction | ~15 min |
| 9 | Lyrics | 24, 25, 26, 27 | object-writing, rhyme-types, point-of-view, prosody | ~30 min |
| 10 | Rhythm | 28, 29, 30 | groove-construction, drum-programming-by-genre, kick-bass-relationship | ~25 min |
| 11 | Synth + Sampling | 31, 32, 33, 34, 35 | subtractive, fm-wavetable, patch-design, chopping-resampling, loop-arrangement | ~35 min |
| 12 | Workflow | 36, 37, 38 | session-methodology, finishing-work, preproduction-and-demo-handoff | ~25 min |

**Totals:** 12 batches, 38 prompts, ~5 hours of total Claude time. If you run 3 in parallel, wall-clock time drops to ~1.5–2 hours.

---

## Suggested batch firing order (priority)

If you don't want to run everything at once, this order produces the highest-value retrieval surface first:

**Wave 1 (~90 min serial, ~30 min if parallel):** Batches 3, 5, 1
*(Mixing A, Mastering, Recording A — covers the most-asked questions: EQ, compression, vocal mixing, LUFS, mic placement, signal flow)*

**Wave 2 (~90 min serial):** Batches 9, 7, 4
*(Lyrics, Harmony, Mixing B — covers craft fundamentals + reverb/low-end/translation)*

**Wave 3 (~75 min serial):** Batches 6, 10, 11
*(Structure, Rhythm, Synth+Sampling — fills out songwriting and electronic-production gaps)*

**Wave 4 (~45 min serial):** Batches 2, 12, 8
*(Recording B, Workflow, Melody — depth fill)*

---

## Kickoff Messages

For each batch, copy the **entire** message in the code block below into a fresh Claude Code chat.

---

### Batch 1 — Recording A

```
Run research batch 1 for ARLO.

Read /Users/cfitt/Dev/arlo/PROMPTS.md to load the master template and the topic variable rows.

For each of these prompts in order — #1, #2, #4 — do the following:

1. Find the topic row in PROMPTS.md and substitute its variables (TOPIC, TITLE, SCOPE, FOLDER, FILENAME, SUBTOPICS, CANONICAL_REFS, SUGGESTED_TAGS) into the master template.
2. Execute the deep research using web search. Follow the content requirements in the template: concrete over abstract, inline citations, anti-hallucination guard (omit unverified specifics rather than guess).
3. Write the rendered output to /Users/cfitt/Dev/arlo/corpus/recording/{filename}.md following the exact output format from PROMPTS.md — front-matter block, 8–15 H2 sections, Cited Retrieval Topics footer, Sources bibliography.
4. Move to the next prompt.

After all 3 files are written, list them with sizes and give a one-sentence summary of what each covers.

Reminder: if a specific claim, number, or attribution can't be verified during research, OMIT it. Don't guess. Made-up specifics will poison ARLO's retrieval.
```

---

### Batch 2 — Recording B

```
Run research batch 2 for ARLO.

Read /Users/cfitt/Dev/arlo/PROMPTS.md to load the master template and topic variable rows.

For each of these prompts in order — #3, #5 — do the following:

1. Find the topic row in PROMPTS.md and substitute its variables into the master template.
2. Execute the deep research using web search. Follow the content requirements: concrete over abstract, inline citations, anti-hallucination guard.
3. Write the rendered output to /Users/cfitt/Dev/arlo/corpus/recording/{filename}.md following the exact output format from PROMPTS.md.
4. Move to the next prompt.

After both files are written, list them with sizes and give a one-sentence summary of each.

Reminder: omit unverified claims rather than guess.
```

---

### Batch 3 — Mixing A

```
Run research batch 3 for ARLO.

Read /Users/cfitt/Dev/arlo/PROMPTS.md to load the master template and topic variable rows.

For each of these prompts in order — #6, #7, #11 — do the following:

1. Find the topic row in PROMPTS.md and substitute its variables into the master template.
2. Execute the deep research using web search. Follow the content requirements: concrete over abstract, inline citations, anti-hallucination guard.
3. Write the rendered output to /Users/cfitt/Dev/arlo/corpus/mixing/{filename}.md following the exact output format from PROMPTS.md.
4. Move to the next prompt.

After all 3 files are written, list them with sizes and give a one-sentence summary of each.

Reminder: omit unverified claims rather than guess.
```

---

### Batch 4 — Mixing B

```
Run research batch 4 for ARLO.

Read /Users/cfitt/Dev/arlo/PROMPTS.md to load the master template and topic variable rows.

For each of these prompts in order — #8, #9, #10 — do the following:

1. Find the topic row in PROMPTS.md and substitute its variables into the master template.
2. Execute the deep research using web search. Follow the content requirements: concrete over abstract, inline citations, anti-hallucination guard.
3. Write the rendered output to /Users/cfitt/Dev/arlo/corpus/mixing/{filename}.md following the exact output format from PROMPTS.md.
4. Move to the next prompt.

After all 3 files are written, list them with sizes and give a one-sentence summary of each.

Reminder: omit unverified claims rather than guess.
```

---

### Batch 5 — Mastering

```
Run research batch 5 for ARLO.

Read /Users/cfitt/Dev/arlo/PROMPTS.md to load the master template and topic variable rows.

For each of these prompts in order — #12, #13, #14 — do the following:

1. Find the topic row in PROMPTS.md and substitute its variables into the master template.
2. Execute the deep research using web search. Follow the content requirements: concrete over abstract, inline citations, anti-hallucination guard.
3. Write the rendered output to /Users/cfitt/Dev/arlo/corpus/mastering/{filename}.md following the exact output format from PROMPTS.md.
4. Move to the next prompt.

After all 3 files are written, list them with sizes and give a one-sentence summary of each.

Reminder: omit unverified claims rather than guess. For platform-specific LUFS values (Spotify, Apple Music, etc.), prefer official platform documentation as the source.
```

---

### Batch 6 — Structure

```
Run research batch 6 for ARLO.

Read /Users/cfitt/Dev/arlo/PROMPTS.md to load the master template and topic variable rows.

For each of these prompts in order — #15, #16, #17 — do the following:

1. Find the topic row in PROMPTS.md and substitute its variables into the master template.
2. Execute the deep research using web search. Follow the content requirements: concrete over abstract, inline citations, anti-hallucination guard.
3. Write the rendered output to /Users/cfitt/Dev/arlo/corpus/structure/{filename}.md following the exact output format from PROMPTS.md.
4. Move to the next prompt.

After all 3 files are written, list them with sizes and give a one-sentence summary of each.

Reminder: omit unverified claims rather than guess.
```

---

### Batch 7 — Harmony

```
Run research batch 7 for ARLO.

Read /Users/cfitt/Dev/arlo/PROMPTS.md to load the master template and topic variable rows.

For each of these prompts in order — #18, #19, #20, #21 — do the following:

1. Find the topic row in PROMPTS.md and substitute its variables into the master template.
2. Execute the deep research using web search. Follow the content requirements: concrete over abstract, inline citations, anti-hallucination guard.
3. Write the rendered output to /Users/cfitt/Dev/arlo/corpus/harmony/{filename}.md following the exact output format from PROMPTS.md.
4. Move to the next prompt.

After all 4 files are written, list them with sizes and give a one-sentence summary of each.

Reminder: omit unverified claims rather than guess. For frequency-data claims about chord progressions, prefer Hooktheory's TheoryTab database and Open Music Theory.
```

---

### Batch 8 — Melody

```
Run research batch 8 for ARLO.

Read /Users/cfitt/Dev/arlo/PROMPTS.md to load the master template and topic variable rows.

For each of these prompts in order — #22, #23 — do the following:

1. Find the topic row in PROMPTS.md and substitute its variables into the master template.
2. Execute the deep research using web search. Follow the content requirements: concrete over abstract, inline citations, anti-hallucination guard.
3. Write the rendered output to /Users/cfitt/Dev/arlo/corpus/melody/{filename}.md following the exact output format from PROMPTS.md.
4. Move to the next prompt.

After both files are written, list them with sizes and give a one-sentence summary of each.

Reminder: omit unverified claims rather than guess.
```

---

### Batch 9 — Lyrics

```
Run research batch 9 for ARLO.

Read /Users/cfitt/Dev/arlo/PROMPTS.md to load the master template and topic variable rows.

For each of these prompts in order — #24, #25, #26, #27 — do the following:

1. Find the topic row in PROMPTS.md and substitute its variables into the master template.
2. Execute the deep research using web search. Follow the content requirements: concrete over abstract, inline citations, anti-hallucination guard.
3. Write the rendered output to /Users/cfitt/Dev/arlo/corpus/lyrics/{filename}.md following the exact output format from PROMPTS.md.
4. Move to the next prompt.

After all 4 files are written, list them with sizes and give a one-sentence summary of each.

Reminder: omit unverified claims rather than guess. For Pattison-specific concepts (object writing, rhyme taxonomy), reference his books and the Sound on Sound interview (already captured in corpus/lyrics/sos-pattison-writing-better-lyrics-interview.md) rather than inventing variants.
```

---

### Batch 10 — Rhythm

```
Run research batch 10 for ARLO.

Read /Users/cfitt/Dev/arlo/PROMPTS.md to load the master template and topic variable rows.

For each of these prompts in order — #28, #29, #30 — do the following:

1. Find the topic row in PROMPTS.md and substitute its variables into the master template.
2. Execute the deep research using web search. Follow the content requirements: concrete over abstract, inline citations, anti-hallucination guard.
3. Write the rendered output to /Users/cfitt/Dev/arlo/corpus/rhythm/{filename}.md following the exact output format from PROMPTS.md.
4. Move to the next prompt.

After all 3 files are written, list them with sizes and give a one-sentence summary of each.

Reminder: omit unverified claims rather than guess. For genre-specific drum-programming specifics, prefer Attack Magazine and Sound on Sound articles.
```

---

### Batch 11 — Synth + Sampling

```
Run research batch 11 for ARLO.

Read /Users/cfitt/Dev/arlo/PROMPTS.md to load the master template and topic variable rows.

For each of these prompts in order — #31, #32, #33, #34, #35 — do the following:

1. Find the topic row in PROMPTS.md and substitute its variables into the master template.
2. Execute the deep research using web search. Follow the content requirements: concrete over abstract, inline citations, anti-hallucination guard.
3. Write the rendered output to /Users/cfitt/Dev/arlo/corpus/{synthesis OR sampling — based on the row's folder}/{filename}.md following the exact output format from PROMPTS.md.
4. Move to the next prompt.

Prompts #31, #32, #33 save to corpus/synthesis/; #34, #35 save to corpus/sampling/.

After all 5 files are written, list them with sizes and give a one-sentence summary of each.

Reminder: omit unverified claims rather than guess. For synthesis-fundamentals topics, prefer Sound on Sound's Synth Secrets series (Gordon Reid) and Welsh's Synthesizer Cookbook.

This batch is larger than most (5 prompts). If you start running low on context, complete the in-flight prompt fully, then summarize remaining work for me to continue in a new session.
```

---

### Batch 12 — Workflow

```
Run research batch 12 for ARLO.

Read /Users/cfitt/Dev/arlo/PROMPTS.md to load the master template and topic variable rows.

For each of these prompts in order — #36, #37, #38 — do the following:

1. Find the topic row in PROMPTS.md and substitute its variables into the master template.
2. Execute the deep research using web search. Follow the content requirements: concrete over abstract, inline citations, anti-hallucination guard.
3. Write the rendered output to /Users/cfitt/Dev/arlo/corpus/workflow/{filename}.md following the exact output format from PROMPTS.md.
4. Move to the next prompt.

After all 3 files are written, list them with sizes and give a one-sentence summary of each.

Reminder: omit unverified claims rather than guess. For producer-workflow specifics, prefer Sound on Sound Inside Track features (one already in corpus/workflow/) and Mixerman's Zen and the Art of Producing where its content is discussed online.
```

---

## Post-batch verification

After each batch completes, run this quick check from any terminal:

```bash
# Confirm files landed in the right places
find ~/Dev/arlo/corpus -name "*.md" -newer ~/Dev/arlo/PROMPTS.md -type f | sort

# Sanity-check sizes (should be 4-15 KB each)
find ~/Dev/arlo/corpus -name "*.md" -newer ~/Dev/arlo/PROMPTS.md -type f -exec ls -lh {} \;

# Spot-check front-matter on a random new file
head -20 ~/Dev/arlo/corpus/<some-batch-scope>/<some-filename>.md
```

## Tracking what's done

To keep track of which batches have completed, append to this checklist as you go:

- [x] Batch 1 — Recording A *(7 min wall, 3 files, 6403 words total)*
- [x] Batch 2 — Recording B *(8 min wall, 2 files, 4981 words total)*
- [x] Batch 3 — Mixing A *(8 min wall, 3 files, 6471 words total)*
- [x] Batch 4 — Mixing B *(8 min wall, 3 files, 6162 words total)*
- [x] Batch 5 — Mastering *(7 min wall, 3 files, 5524 words total)*
- [x] Batch 6 — Structure *(8 min wall, 3 files, 6279 words total)*
- [x] Batch 7 — Harmony *(9 min wall, 4 files, 8216 words total)*
- [x] Batch 8 — Melody *(7 min wall, 2 files, 4902 words total)*
- [x] Batch 9 — Lyrics *(7 min wall, 4 files, 6622 words total)*
- [x] Batch 10 — Rhythm *(8 min wall, 3 files, 6365 words total)*
- [x] Batch 11 — Synth + Sampling *(12 min wall, 5 files, 11943 words total)*
- [x] Batch 12 — Workflow *(9 min wall, 3 files, 6919 words total)*

When all twelve are checked, the corpus has 38 new seed documents on top of the existing 9 files — roughly 47 total documents, ~400+ chunks ready for ARLO retrieval.

---

## After all batches complete

Three follow-up tasks worth doing once the seed corpus is full:

1. **Validation pass** — pick 5–10 files at random and spot-check 2–3 specific claims each. Look for hallucinated plugin settings, made-up song attributions, or fake URLs. Flag anything suspicious with a `⚠ unverified` inline note.

2. **Cross-reference cleanup** — many files will cite the same canonical sources (Senior, Pattison, Pedler, etc.). Once you acquire those books, you can replace the deep-research-synthesis chunks with direct book-extract chunks, and update the `Source:` front-matter line accordingly.

3. **Retrieval-topic harvest** — every file ends with 5–10 "Cited Retrieval Topics" phrasings. Collect those into a single file (`corpus/RETRIEVAL-INDEX.md`) and use it to test your ARLO ingest/retrieval pipeline end-to-end. If a question phrasing doesn't pull the right chunk, the chunking strategy or embedding model needs tuning.
