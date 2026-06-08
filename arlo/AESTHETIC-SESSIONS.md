# ARLO Aesthetic Corpus — Batch Execution Plan

5 numbered batches that together produce all 18 aesthetic-specific seed documents. Same dispatch pattern as `SESSIONS.md` — each kickoff reads `AESTHETIC-PROMPTS.md` from disk.

---

## Prerequisite

Create the two new folders first:

```bash
mkdir -p ~/Dev/arlo/corpus/{artists,techniques}
```

---

## Batch Overview

| # | Batch | Prompts | Files written | Est. wall time |
|---|-------|---------|---------------|----------------|
| A1 | Bon Iver + LCD | 1, 2, 3, 4 | 4 in `artists/` | ~10 min |
| A2 | LCD adjacents + Charli | 5, 6, 7 | 3 in `artists/` | ~9 min |
| A3 | mk.gee + Bluegrass | 8, 9, 10 | 3 in `artists/` | ~9 min |
| T1 | Vocal + Electronic technique | 11, 12, 13, 14 | 4 in `techniques/` | ~10 min |
| T2 | Guitar + Mix + Theory | 15, 16, 17, 18 | 4 in `techniques/` | ~10 min |

**Total:** 18 files. If all 5 batches in parallel: ~10–12 min wall time. Serial: ~50 min.

---

## How to run

Same as the original SESSIONS.md workflow — paste each batch kickoff into a fresh Claude Code session, or dispatch as parallel sub-agents from the main session.

**Parallelism note:** With Claude Code Max 20x, all 5 batches in parallel is comfortable. The aesthetic prompts cite specific URLs (not just book titles), so the agents will do more focused WebFetch calls than the general corpus batches did — slightly heavier per-agent compute, but no rate-limit risk at 5 concurrent.

---

## Kickoff Messages

---

### Batch A1 — Bon Iver + LCD (4 prompts)

```
Run aesthetic research batch A1 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/AESTHETIC-PROMPTS.md — contains the master template AND the 18 topic variable rows.
- /Users/cfitt/Dev/arlo/AESTHETIC-RESEARCH-PLAN.md — overall strategic context for why these files are being created (skim only).
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.

YOUR TASK:
Produce 4 markdown files by executing prompts #1, #2, #3, and #4 from AESTHETIC-PROMPTS.md, in that order:

1. Prompt #1 (bon-iver-vocal-layering-messina) → /Users/cfitt/Dev/arlo/corpus/artists/bon-iver-vocal-layering-messina.md
2. Prompt #2 (bon-iver-sample-driven-songwriting) → /Users/cfitt/Dev/arlo/corpus/artists/bon-iver-sample-driven-songwriting.md
3. Prompt #3 (lcd-soundsystem-synth-sound-design) → /Users/cfitt/Dev/arlo/corpus/artists/lcd-soundsystem-synth-sound-design.md
4. Prompt #4 (lcd-soundsystem-live-electronic-rig) → /Users/cfitt/Dev/arlo/corpus/artists/lcd-soundsystem-live-electronic-rig.md

FOR EACH PROMPT:
1. Read the topic row from AESTHETIC-PROMPTS.md (title, scope, folder, filename, subtopics, primary sources, suggested tags).
2. Substitute its variables into the master template at the top of AESTHETIC-PROMPTS.md.
3. Execute deep research. Start by WebFetch-ing the primary-source URLs listed in the prompt row — those are the canonical evidence for each topic. Then augment with WebSearch as needed. Aim for 6–10 source touches per file.
4. Write the rendered output to the target path. The file MUST include:
   - Front-matter block: # Title, **Scope:**, **Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative, **Aesthetic-stack relevance:**, **Tags:**
   - 8–15 H2 body sections, each 100–250 words of dense, specific content
   - "## Cited Retrieval Topics" footer with 5–10 lowercase conversational query phrases
   - "## Sources" bibliography with markdown-link URLs

CRITICAL CONSTRAINTS:
- Concrete over abstract — specific gear models, specific session details, specific song examples. NOT philosophy.
- AESTHETIC ANCHORING — name the specific artists/producers (Vernon, Burton, Messina, Murphy, Mahoney) and tie claims to their actual work.
- ANTI-HALLUCINATION: if you cannot verify a specific number, setting, or attribution through the primary sources or web research, OMIT it. Prefer qualitative claims over fabricated specifics. Made-up specifics will poison ARLO's retrieval.
- Length: 1500–2500 words per file.
- Inline markdown link citations within sentences (not only in a bibliography).
- Audience: intermediate musicians/producers.

WHEN ALL 4 FILES ARE WRITTEN:
- Use Bash to list with sizes
- One-sentence summary per file + body H2 count + inline citation count
- Flag any topic where verification was weak

Begin.
```

---

### Batch A2 — LCD adjacents + Charli (3 prompts)

```
Run aesthetic research batch A2 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/AESTHETIC-PROMPTS.md — master template + 18 topic rows.
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.

YOUR TASK:
Produce 3 markdown files by executing prompts #5, #6, and #7 from AESTHETIC-PROMPTS.md, in that order:

1. Prompt #5 (james-murphy-analog-synth-philosophy) → /Users/cfitt/Dev/arlo/corpus/artists/james-murphy-analog-synth-philosophy.md
2. Prompt #6 (pat-mahoney-dance-punk-drumming) → /Users/cfitt/Dev/arlo/corpus/artists/pat-mahoney-dance-punk-drumming.md
3. Prompt #7 (charli-xcx-brat-production) → /Users/cfitt/Dev/arlo/corpus/artists/charli-xcx-brat-production.md

FOR EACH PROMPT:
1. Read the topic row from AESTHETIC-PROMPTS.md.
2. Substitute its variables into the master template.
3. Execute deep research. WebFetch the primary-source URLs first; augment with WebSearch.
4. Write the markdown file with required front-matter (including Aesthetic-stack relevance line), 8–15 H2 sections, Cited Retrieval Topics footer, Sources bibliography.

CRITICAL CONSTRAINTS:
- Concrete over abstract — specific gear, specific sessions, specific artist quotes.
- AESTHETIC ANCHORING — Murphy/Mahoney/Cook/Charli specifics.
- ANTI-HALLUCINATION: omit unverified specifics rather than guess. The Charli XCX "Brat" production has been less technically documented than Bon Iver/LCD — be especially careful not to fabricate specifics there. Lean on what the artist has said in the Apple Music interview, the Grammy.com piece, and reviews.
- Length: 1500–2500 words per file.
- Inline markdown link citations.

WHEN ALL 3 FILES ARE WRITTEN:
- Use Bash to list with sizes
- One-sentence summary per file + body H2 count + inline citation count
- Flag any topic where verification was weak

Begin.
```

---

### Batch A3 — mk.gee + Bluegrass artists (3 prompts)

```
Run aesthetic research batch A3 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/AESTHETIC-PROMPTS.md — master template + 18 topic rows.
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.

YOUR TASK:
Produce 3 markdown files by executing prompts #8, #9, and #10 from AESTHETIC-PROMPTS.md, in that order:

1. Prompt #8 (mk-gee-di-direct-philosophy) → /Users/cfitt/Dev/arlo/corpus/artists/mk-gee-di-direct-philosophy.md
2. Prompt #9 (billy-strings-flatpicking-stompboxes) → /Users/cfitt/Dev/arlo/corpus/artists/billy-strings-flatpicking-stompboxes.md
3. Prompt #10 (punch-brothers-progressive-composition) → /Users/cfitt/Dev/arlo/corpus/artists/punch-brothers-progressive-composition.md

FOR EACH PROMPT:
1. Read the topic row from AESTHETIC-PROMPTS.md.
2. Substitute its variables into the master template.
3. Execute deep research. WebFetch the primary-source URLs first.
4. Write the markdown file with required front-matter, 8–15 H2 sections, Cited Retrieval Topics footer, Sources bibliography.

CRITICAL CONSTRAINTS:
- Concrete over abstract — specific gear, specific technique descriptions, specific song examples.
- AESTHETIC ANCHORING — mk.gee/Gordon, Strings, Thile, Punch Brothers specifics.
- ANTI-HALLUCINATION: mk.gee in particular has very thin technical documentation. Do NOT invent gear settings or session details for him — stick to what the Dazed profile, Switched On Pop episode, NYT profile, and album reviews actually say. If you cannot verify something specific, prefer a qualitative claim. This is the highest-hallucination-risk file in the batch.
- For Billy Strings and Punch Brothers — Premier Guitar Rig Rundowns and Acoustic Guitar interviews are gold; use them as primary anchors.
- Length: 1500–2500 words per file.
- Inline markdown link citations.

WHEN ALL 3 FILES ARE WRITTEN:
- Use Bash to list with sizes
- One-sentence summary per file + body H2 count + inline citation count
- Flag any topic where verification was weak (especially mk.gee specifics)

Begin.
```

---

### Batch T1 — Vocal + Electronic technique (4 prompts)

```
Run aesthetic research batch T1 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/AESTHETIC-PROMPTS.md — master template + 18 topic rows.
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.
- /Users/cfitt/Dev/arlo/corpus/lyrics/sos-pattison-writing-better-lyrics-interview.md — already in corpus (lyric craft, not directly relevant but a quality-baseline example of how to structure technique chunks).
- /Users/cfitt/Dev/arlo/corpus/mixing/sos-inside-track-billie-eilish-bad-guy.md — already in corpus; example of dense-but-clear mixing chain with specific settings.
- /Users/cfitt/Dev/arlo/corpus/sampling/elektron-digitakt-ii-manual.pdf — already in corpus (sampling hardware reference).

YOUR TASK:
Produce 4 markdown files by executing prompts #11, #12, #13, and #14 from AESTHETIC-PROMPTS.md, in that order:

1. Prompt #11 (vocal-stacking-bon-iver-style) → /Users/cfitt/Dev/arlo/corpus/techniques/vocal-stacking-bon-iver-style.md
2. Prompt #12 (auto-tune-as-creative-tool) → /Users/cfitt/Dev/arlo/corpus/techniques/auto-tune-as-creative-tool.md
3. Prompt #13 (hyperpop-sound-design) → /Users/cfitt/Dev/arlo/corpus/techniques/hyperpop-sound-design.md
4. Prompt #14 (hardware-sampling-workflow) → /Users/cfitt/Dev/arlo/corpus/techniques/hardware-sampling-workflow.md

FOR EACH PROMPT:
1. Read the topic row from AESTHETIC-PROMPTS.md.
2. Substitute its variables into the master template.
3. Execute deep research. WebFetch the primary-source URLs first; augment with WebSearch.
4. Write the markdown file with required front-matter, 8–15 H2 sections, Cited Retrieval Topics footer, Sources bibliography.

CRITICAL CONSTRAINTS:
- Concrete over abstract — specific Auto-Tune settings (retune speed, humanize, formant shift values), specific plugin chains for hyperpop hard-tune, specific OP-1 / Octatrack workflow steps.
- AESTHETIC ANCHORING — tie techniques back to the canonical examples: Bon Iver / SM57 / Messina for vocal stacking; T-Pain / Kanye / Bon Iver / SOPHIE for Auto-Tune lineage; SOPHIE / Cook / Charli for hyperpop; Vernon / OP-1 and Murphy / hardware for sampling.
- ANTI-HALLUCINATION: the MusicRadar SOPHIE-style tutorial cites very specific Auto-Tune settings (retune 0.00 ms, formant +7.20 semitones). Cite these accurately; do not invent additional specifics.
- Length: 1500–2500 words per file.
- Inline markdown link citations.

WHEN ALL 4 FILES ARE WRITTEN:
- Use Bash to list with sizes
- One-sentence summary per file + body H2 count + inline citation count
- Flag any topic where verification was weak

Begin.
```

---

### Batch T2 — Guitar + Mix + Theory (4 prompts)

```
Run aesthetic research batch T2 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/AESTHETIC-PROMPTS.md — master template + 18 topic rows.
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.
- /Users/cfitt/Dev/arlo/corpus/mixing/low-end-management.md — already in corpus; dense-but-clear mixing prompt should reference and extend this.
- /Users/cfitt/Dev/arlo/corpus/mixing/mix-translation-and-reference-tracks.md — already in corpus; relevant for the dense-but-clear file.
- /Users/cfitt/Dev/arlo/corpus/harmony/modal-interchange-and-borrowed-chords.md — already in corpus; modal-bluegrass file should reference and extend the modal-interchange vocabulary into a bluegrass-specific context.

YOUR TASK:
Produce 4 markdown files by executing prompts #15, #16, #17, and #18 from AESTHETIC-PROMPTS.md, in that order:

1. Prompt #15 (reamping-fundamentals) → /Users/cfitt/Dev/arlo/corpus/techniques/reamping-fundamentals.md
2. Prompt #16 (pedal-as-instrument-workflow) → /Users/cfitt/Dev/arlo/corpus/techniques/pedal-as-instrument-workflow.md
3. Prompt #17 (modal-bluegrass-harmony) → /Users/cfitt/Dev/arlo/corpus/techniques/modal-bluegrass-harmony.md
4. Prompt #18 (dense-but-clear-mixing) → /Users/cfitt/Dev/arlo/corpus/techniques/dense-but-clear-mixing.md

FOR EACH PROMPT:
1. Read the topic row from AESTHETIC-PROMPTS.md.
2. Substitute its variables into the master template.
3. Execute deep research. WebFetch the primary-source URLs first; augment with WebSearch.
4. Write the markdown file with required front-matter, 8–15 H2 sections, Cited Retrieval Topics footer, Sources bibliography.

CRITICAL CONSTRAINTS:
- Concrete over abstract — specific reamp box impedances, specific pedal-chain orders, specific modal moves (Mixolydian ♭VII in bluegrass), specific arrangement-mixing decisions.
- AESTHETIC ANCHORING — mk.gee for reamping; Strings / KNOBs / pedal-aesthetic for pedal-as-instrument; Pikelny / Fleck / Thile / Strings for modal bluegrass; Bon Iver / Charli / LCD for dense-but-clear mixing.
- ANTI-HALLUCINATION: the Berklee Press *Beyond Bluegrass Banjo* book is NOT in corpus yet, so do not invent quotes from it — discuss what's publicly known from the book's product page, reviews, and Pikelny's separate interviews instead.
- Length: 1500–2500 words per file.
- Inline markdown link citations.

WHEN ALL 4 FILES ARE WRITTEN:
- Use Bash to list with sizes
- One-sentence summary per file + body H2 count + inline citation count
- Flag any topic where verification was weak

Begin.
```

---

---

### Batch A4 — Talking Heads cluster (2 files: David Byrne + Oblique Strategies)

> **Note:** Prompt #19 (`talking-heads-remain-in-light-production`) is **deprecated** — handled as the album-anchored file in `ALBUMS-PROMPTS.md` row #3 / batch AL1. This batch executes only prompts #20 and #21.

```
Run aesthetic research batch A4 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/AESTHETIC-PROMPTS.md — master template + 44 topic rows.
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.
- /Users/cfitt/Dev/arlo/ALBUMS-PROMPTS.md row #3 (`talking-heads-remain-in-light`) — already covered as an album file; you do NOT need to write a duplicate. Reference it via cross-link.

YOUR TASK:
Produce 2 markdown files by executing prompts #20 and #21 from AESTHETIC-PROMPTS.md, in that order:

1. Prompt #20 (david-byrne-songwriting-philosophy) → /Users/cfitt/Dev/arlo/corpus/artists/david-byrne-songwriting-philosophy.md
2. Prompt #21 (oblique-strategies-and-studio-as-instrument) → /Users/cfitt/Dev/arlo/corpus/techniques/oblique-strategies-and-studio-as-instrument.md

DO NOT execute prompt #19 — it's deprecated (handled by albums corpus). Skip it.

FOR EACH PROMPT:
1. Read the topic row from AESTHETIC-PROMPTS.md.
2. Substitute its variables into the master template.
3. Execute deep research. WebFetch the primary-source URLs first; augment with WebSearch.
4. Write the markdown file with required front-matter, 8–15 H2 sections, Cited Retrieval Topics footer, Sources bibliography.

CRITICAL CONSTRAINTS:
- Concrete over abstract — specific Byrne lyrics, specific Oblique Strategies cards in named sessions, specific examples of studio-as-composition.
- AESTHETIC ANCHORING — Byrne specifics, Eno specifics, Talking Heads / Bowie session references.
- ANTI-HALLUCINATION: omit unverified specifics rather than guess.
- Length: 1500–2500 words per file.
- Inline markdown link citations.

WHEN BOTH FILES ARE WRITTEN:
- Use Bash to list with sizes
- One-sentence summary per file + body H2 count + inline-citation count
- Flag any topic where verification was weak

Begin.
```

---

### Batch A5 — Ry Cooder + Radiohead cluster (4 files)

> **Note:** Prompt #24 (`radiohead-kid-a-production`) is **deprecated** — handled as the album-anchored file in `ALBUMS-PROMPTS.md` row #7 / batch AL2. This batch executes only prompts #22, #23, #25, #26.

```
Run aesthetic research batch A5 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/AESTHETIC-PROMPTS.md — master template + 44 topic rows.
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.

YOUR TASK:
Produce 4 markdown files by executing prompts #22, #23, #25, #26 (SKIP #24 — deprecated):

1. Prompt #22 (ry-cooder-slide-guitar-and-coodercaster) → /Users/cfitt/Dev/arlo/corpus/artists/ry-cooder-slide-guitar-and-coodercaster.md
2. Prompt #23 (open-tunings-and-slide-guitar) → /Users/cfitt/Dev/arlo/corpus/techniques/open-tunings-and-slide-guitar.md
3. Prompt #25 (radiohead-in-rainbows-production) → /Users/cfitt/Dev/arlo/corpus/artists/radiohead-in-rainbows-production.md
4. Prompt #26 (nigel-godrich-engineering-method) → /Users/cfitt/Dev/arlo/corpus/artists/nigel-godrich-engineering-method.md

DO NOT execute prompt #24 — it's deprecated (handled by albums corpus). Skip it.

FOR EACH PROMPT:
1. Read the topic row from AESTHETIC-PROMPTS.md.
2. Substitute its variables into the master template.
3. Execute deep research. WebFetch the primary-source URLs first; augment with WebSearch.
4. Write the markdown file with required front-matter, 8–15 H2 sections, Cited Retrieval Topics footer, Sources bibliography.

CRITICAL CONSTRAINTS:
- Concrete over abstract — specific Coodercaster pickup configuration, specific open-tuning intervals, specific *In Rainbows* console gear, specific Godrich-engineered records.
- AESTHETIC ANCHORING — Cooder lineage, Godrich's catalog.
- ANTI-HALLUCINATION: for the Coodercaster pickup configuration, verify the specific pickup brands (Teisco from Lindley + Valco bridge) before citing.
- Length: 1500–2500 words per file.

WHEN ALL 4 FILES ARE WRITTEN:
- Use Bash to list with sizes
- One-sentence summary per file + body H2 count + inline-citation count
- Flag any topic where verification was weak

Begin.
```

---

### Batch A6 — Sufjan + Dijon (2 files)

```
Run aesthetic research batch A6 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/AESTHETIC-PROMPTS.md — master template + 44 topic rows.
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.

YOUR TASK:
Produce 2 markdown files by executing prompts #27 and #28:

1. Prompt #27 (sufjan-stevens-age-of-adz-production) → /Users/cfitt/Dev/arlo/corpus/artists/sufjan-stevens-age-of-adz-production.md
2. Prompt #28 (dijon-absolutely-production) → /Users/cfitt/Dev/arlo/corpus/artists/dijon-absolutely-production.md

FOR EACH PROMPT:
1. Read the topic row from AESTHETIC-PROMPTS.md.
2. Substitute its variables into the master template.
3. Execute deep research. WebFetch the primary-source URLs first; augment with WebSearch.
4. Write the markdown file with required front-matter, 8–15 H2 sections, Cited Retrieval Topics footer, Sources bibliography.

CRITICAL CONSTRAINTS:
- Concrete over abstract — specific *Age of Adz* electronic gear, specific Dijon *Absolutely* gear (AKG C414, Octatrack, Eurorack).
- AESTHETIC ANCHORING — Sufjan's orchestral-folk-to-electronic transition; Dijon's mk.gee-collaborator context.
- ANTI-HALLUCINATION: omit unverified specifics rather than guess.
- Length: 1500–2500 words per file.

WHEN BOTH FILES ARE WRITTEN:
- Use Bash to list with sizes
- One-sentence summary per file + body H2 count + inline-citation count
- Flag any topic where verification was weak

Begin.
```

---

### Batch A7 — Big Thief + Car Seat Headrest + BCNR (4 files)

```
Run aesthetic research batch A7 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/AESTHETIC-PROMPTS.md — master template + 44 topic rows.
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.

YOUR TASK:
Produce 4 markdown files by executing prompts #29, #30, #31, #32:

1. Prompt #29 (big-thief-nomadic-recording) → /Users/cfitt/Dev/arlo/corpus/artists/big-thief-nomadic-recording.md
2. Prompt #30 (adrianne-lenker-intimate-folk) → /Users/cfitt/Dev/arlo/corpus/artists/adrianne-lenker-intimate-folk.md
3. Prompt #31 (car-seat-headrest-bedroom-to-band) → /Users/cfitt/Dev/arlo/corpus/artists/car-seat-headrest-bedroom-to-band.md
4. Prompt #32 (black-country-new-road-ants-from-up-there) → /Users/cfitt/Dev/arlo/corpus/artists/black-country-new-road-ants-from-up-there.md

FOR EACH PROMPT:
1. Read the topic row from AESTHETIC-PROMPTS.md.
2. Substitute its variables into the master template.
3. Execute deep research. WebFetch the primary-source URLs first; augment with WebSearch.
4. Write the markdown file with required front-matter, 8–15 H2 sections, Cited Retrieval Topics footer, Sources bibliography.

CRITICAL CONSTRAINTS:
- Concrete over abstract — specific session-location details (Big Thief's 5 sites), specific Toledo studio choices, specific BCNR live-tracking specs.
- AESTHETIC ANCHORING — band-context vs. solo (Big Thief vs. Lenker); the bedroom-to-elaborate-band arc (CSH); chamber-folk-band live capture (BCNR).
- ANTI-HALLUCINATION: BCNR's Maschetzko production has specific details to verify (Chale Abbey Studios, first-time-in-studio framing). Don't fabricate.
- Length: 1500–2500 words per file.

WHEN ALL 4 FILES ARE WRITTEN:
- Use Bash to list with sizes
- One-sentence summary per file + body H2 count + inline-citation count
- Flag any topic where verification was weak

Begin.
```

---

### Batch A8 — Andrew Bird + Father John Misty (2 files)

> **Note:** Prompt #33 (`postal-service-give-up-mail-collaboration`) is **deprecated** — handled as the album-anchored file in `ALBUMS-PROMPTS.md` row #88 / batch AL18. This batch executes only prompts #34 and #35.

```
Run aesthetic research batch A8 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/AESTHETIC-PROMPTS.md — master template + 44 topic rows.
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.

YOUR TASK:
Produce 2 markdown files by executing prompts #34 and #35 (SKIP #33 — deprecated):

1. Prompt #34 (andrew-bird-loop-violin-arrangement) → /Users/cfitt/Dev/arlo/corpus/artists/andrew-bird-loop-violin-arrangement.md
2. Prompt #35 (father-john-misty-jonathan-wilson-lush-folk) → /Users/cfitt/Dev/arlo/corpus/artists/father-john-misty-jonathan-wilson-lush-folk.md

DO NOT execute prompt #33 — it's deprecated (handled by albums corpus). Skip it.

FOR EACH PROMPT:
1. Read the topic row from AESTHETIC-PROMPTS.md.
2. Substitute its variables into the master template.
3. Execute deep research. WebFetch the primary-source URLs first; augment with WebSearch.
4. Write the markdown file with required front-matter, 8–15 H2 sections, Cited Retrieval Topics footer, Sources bibliography.

CRITICAL CONSTRAINTS:
- Concrete over abstract — Andrew Bird's specific Line 6 pedal model and signal-chain order; FJM's Jonathan Wilson production approach.
- ANTI-HALLUCINATION: omit unverified specifics rather than guess.
- Length: 1500–2500 words per file.

WHEN BOTH FILES ARE WRITTEN:
- Use Bash to list with sizes
- One-sentence summary per file + body H2 count + inline-citation count
- Flag any topic where verification was weak

Begin.
```

---

### Batch A9 — Cameron Winter + Geese + Vulfpeck + Animal Collective (4 files)

```
Run aesthetic research batch A9 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/AESTHETIC-PROMPTS.md — master template + 44 topic rows.
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.

YOUR TASK:
Produce 4 markdown files by executing prompts #36, #37, #38, #39:

1. Prompt #36 (cameron-winter-heavy-metal-guitar-center-album) → /Users/cfitt/Dev/arlo/corpus/artists/cameron-winter-heavy-metal-guitar-center-album.md
2. Prompt #37 (geese-band-context) → /Users/cfitt/Dev/arlo/corpus/artists/geese-band-context.md
3. Prompt #38 (vulfpeck-jack-stratton-minimalist-funk) → /Users/cfitt/Dev/arlo/corpus/artists/vulfpeck-jack-stratton-minimalist-funk.md
4. Prompt #39 (animal-collective-merriweather-ben-allen) → /Users/cfitt/Dev/arlo/corpus/artists/animal-collective-merriweather-ben-allen.md

FOR EACH PROMPT:
1. Read the topic row from AESTHETIC-PROMPTS.md.
2. Substitute its variables into the master template.
3. Execute deep research. WebFetch the primary-source URLs first; augment with WebSearch.
4. Write the markdown file with required front-matter, 8–15 H2 sections, Cited Retrieval Topics footer, Sources bibliography.

CRITICAL CONSTRAINTS:
- Concrete over abstract — Cameron Winter's specific Guitar Center recording sites + Loren Humphrey credits; Geese's specific *3D Country* / *Projector* production; Vulfpeck's specific "hit session" methodology; Animal Collective Sweet Tea Studios month.
- AESTHETIC ANCHORING — Winter solo (#36) vs Geese band context (#37) should not duplicate each other; cross-link via tags.
- ANTI-HALLUCINATION: omit unverified specifics rather than guess.
- Length: 1500–2500 words per file.

WHEN ALL 4 FILES ARE WRITTEN:
- Use Bash to list with sizes
- One-sentence summary per file + body H2 count + inline-citation count
- Flag any topic where verification was weak

Begin.
```

---

### Batch A10 — Knopfler + Zevon + Prine + Bowie (4 files)

> **Note:** Prompt #43 (`neutral-milk-hotel-aeroplane-lo-fi`) is **deprecated** — handled as the album-anchored file in `ALBUMS-PROMPTS.md` row #89 / batch AL18. This batch executes only prompts #40, #41, #42, #44. (Original plan had A11 as separate Bowie batch; merged into A10 since A11 would have been 1 file.)

```
Run aesthetic research batch A10 for ARLO.

CONTEXT FILES YOU MUST READ FIRST:
- /Users/cfitt/Dev/arlo/AESTHETIC-PROMPTS.md — master template + 44 topic rows.
- /Users/cfitt/Dev/arlo/corpus/README.md — corpus taxonomy.

YOUR TASK:
Produce 4 markdown files by executing prompts #40, #41, #42, #44 (SKIP #43 — deprecated):

1. Prompt #40 (mark-knopfler-fingerstyle-clean-tone) → /Users/cfitt/Dev/arlo/corpus/artists/mark-knopfler-fingerstyle-clean-tone.md
2. Prompt #41 (warren-zevon-jackson-browne-waddy-wachtel) → /Users/cfitt/Dev/arlo/corpus/artists/warren-zevon-jackson-browne-waddy-wachtel.md
3. Prompt #42 (john-prine-dave-cobb-rca-studio-a) → /Users/cfitt/Dev/arlo/corpus/artists/john-prine-dave-cobb-rca-studio-a.md
4. Prompt #44 (david-bowie-berlin-trilogy-visconti-eno) → /Users/cfitt/Dev/arlo/corpus/artists/david-bowie-berlin-trilogy-visconti-eno.md

DO NOT execute prompt #43 — it's deprecated (handled by albums corpus). Skip it.

FOR EACH PROMPT:
1. Read the topic row from AESTHETIC-PROMPTS.md.
2. Substitute its variables into the master template.
3. Execute deep research. WebFetch the primary-source URLs first; augment with WebSearch.
4. Write the markdown file with required front-matter, 8–15 H2 sections, Cited Retrieval Topics footer, Sources bibliography.

CRITICAL CONSTRAINTS:
- Concrete over abstract — Knopfler's specific fingerstyle anchoring positions; Zevon's "Werewolves" specific seven-rhythm-section attempts; Prine's specific Dave Cobb + RCA Studio A specs; Bowie Berlin trilogy specific Visconti + Eno gear.
- AESTHETIC ANCHORING — Knopfler vs mk.gee context; Zevon LA-rock; Bowie's bridge to Talking Heads (cross-link to prompt #20).
- ANTI-HALLUCINATION: for Bowie, Eno's role is "collaborator" NOT "producer." Verify against Wikipedia's Producer line specifically.
- Length: 1500–2500 words per file.

WHEN ALL 4 FILES ARE WRITTEN:
- Use Bash to list with sizes
- One-sentence summary per file + body H2 count + inline-citation count
- Flag any topic where verification was weak

Begin.
```

---

## Note on existing batch A2 — Charli BRAT overlap

Batch A2 (originally written) executes prompt #7 (`charli-xcx-brat-production`) as an artist-anchored file at `corpus/artists/charli-xcx-brat-production.md`. **This overlaps** with `ALBUMS-PROMPTS.md` row #51 (`charli-xcx-brat`) at `corpus/albums/charli-xcx-brat.md`.

Two options when firing both:
- **Option A (recommended):** Run both. The artist file covers Charli's overall *Brat*-era production philosophy and aesthetic; the album file covers the specific session story. They serve different retrieval angles.
- **Option B (deduplicate):** Skip prompt #7 in A2. Only execute prompts #5 and #6. Add `Optionally skip #7 (charli-xcx-brat-production); covered as album file` to the A2 kickoff before pasting.

If unsure, default to Option A — having both gives ARLO more retrieval surface and you can always remove the artist file later if it feels redundant.

---

## Tracking checklist

- [x] Batch A1 — Bon Iver + LCD (4 files)
- [x] Batch A2 — LCD adjacents + Charli (3 files; see Charli BRAT note above)
- [x] Batch A3 — mk.gee + Bluegrass artists (3 files)
- [x] Batch A4 — Talking Heads cluster (2 files; #19 deprecated)
- [x] Batch A5 — Ry Cooder + Radiohead cluster (4 files; #24 deprecated)
- [x] Batch A6 — Sufjan + Dijon (2 files)
- [x] Batch A7 — Big Thief + CSH + BCNR (4 files)
- [x] Batch A8 — Andrew Bird + FJM (2 files; #33 deprecated)
- [x] Batch A9 — Cameron Winter + Geese + Vulfpeck + AC (4 files)
- [x] Batch A10 — Knopfler + Zevon + Prine + Bowie (4 files; #43 deprecated)
- [x] Batch T1 — Vocal + Electronic technique (4 files)
- [x] Batch T2 — Guitar + Mix + Theory (4 files)

When all 12 batches are checked: 40 aesthetic files (artist + technique) across `corpus/artists/` and `corpus/techniques/`. Combined with the 89 albums files, the full ARLO aesthetic-and-albums corpus reaches ~130 production-deep-dive documents.

---

## After all batches complete

Four follow-up tasks worth doing:

1. **Spot-check the mk.gee file** (from A3) — highest-hallucination-risk file in the entire aesthetic corpus given thin technical documentation. Verify 3–5 specific claims against the Dazed/NYT/Switched On Pop sources, and add `⚠ unverified` inline tags to anything that's a stretch.

2. **Cross-link album files to artist files.** After both AESTHETIC and ALBUMS batches complete, add "See also: `corpus/albums/...`" footers to artist files that have related album files (Bowie, LCD, Charli, Radiohead, Postal Service, NMH, Talking Heads, etc.). Manual edit, ~10–15 files.

3. **Re-process specific claims once books arrive.** Once Berklee Press *Beyond Bluegrass Banjo* is acquired, the modal-bluegrass-harmony file should be re-run with direct book quotes replacing the public-source paraphrases. Same for Attack Magazine *Secrets of Dance Music Production* and the dance-punk groove material.

4. **Harvest the Cited Retrieval Topics** from each new file into a unified `RETRIEVAL-INDEX.md` test set. ~40 aesthetic files × 7 phrasings + 89 album files × 7 phrasings = ~900 test queries — your ARLO ingest+retrieval pipeline can be benchmarked against this.
