# Cluster Workflows — Batch Execution Plan

5 numbered batches (CW1–CW5), one per taste cluster. Each is a single paste-able kickoff you
fire into a fresh Claude Code session (or dispatch as a background agent). Each batch reads the
scaffold files, executes its cluster, and writes **two files** (dual output): a corpus chunk and
a workflow template.

## How to run

### Serial / parallel
All 5 batches are independent — different slugs, no cross-batch dependencies. Run serially (one
session at a time) or fire all 5 in parallel. 3–4 concurrent is the comfortable rate-limit sweet
spot; all 5 at once is fine on Max 20× (re-dispatch any that hit a transient error).

### Minimal-kickoff form
```
Run batch {CW_ID} for ARLO Cluster Workflows.
Read /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-SESSIONS.md, find the "Batch {CW_ID}" heading,
follow the kickoff message verbatim. Begin.
```

## Batch overview

| # | Batch | Slug | Files written | Est. time |
|---|-------|------|---------------|-----------|
| CW1 | Art-rock / studio-as-instrument | `art-rock-studio-as-instrument` | corpus chunk + workflow template | ~12 min |
| CW2 | Indie-folk / confessional | `indie-folk-confessional` | corpus chunk + workflow template | ~12 min |
| CW3 | Electronic / groove-first | `electronic-groove-first` | corpus chunk + workflow template | ~12 min |
| CW4 | Lo-fi / prolific | `lo-fi-prolific-volume` | corpus chunk + workflow template | ~12 min |
| CW5 | Post-punk / texture & dynamics | `post-punk-texture-dynamics` | corpus chunk + workflow template | ~12 min |

**Total:** 5 batches → 10 files (5 corpus chunks + 5 workflow templates).

---

## Kickoff messages

### Batch CW1 — Art-rock / studio-as-instrument

```
Run research batch CW1 for ARLO Taste-Driven Cluster Workflows.

You are a research-and-write agent producing seed knowledge-base entries for ARLO, a local-first AI songwriting/production assistant whose mission is to help musicians FINISH SONGS. This batch is DUAL OUTPUT.

Read /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-PROMPTS.md, /Users/cfitt/Dev/arlo/PROMPTS.md (base master template), /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-RESEARCH-PLAN.md, and /Users/cfitt/Dev/arlo/arlo/taste-profile/spotify-taste-profile.md.

Write TWO files:
1. Corpus chunk → /Users/cfitt/Dev/arlo/corpus/songwriting/cluster-workflows/art-rock-studio-as-instrument.md (1500–2500 words, standard ARLO chunk shape: front-matter, 8–15 H2 sections, Cited Retrieval Topics, Sources, See-also footer).
2. Workflow template → /Users/cfitt/Dev/arlo/arlo/workflows/art-rock-studio-as-instrument.md (600–1000 words). Frontmatter: name / origin / type / applicable_when / duration_estimate / taste_cluster / anchor_artists. Body sections: The premise / When ARLO should offer this / The steps / ARLO prompts for each step (verbatim) / In Ableton / When to abandon this workflow / Sources.

CLUSTER: the arrangement/studio IS the compositional act — songs emerge from sound-design, re-contextualizing parts, and productive constraint, not from a finished song played into a mic.
ANCHOR ARTISTS: Radiohead, Talking Heads, David Bowie.
TYPE: production-first
taste_cluster: art-rock-studio-as-instrument
anchor_artists: [Radiohead, Talking Heads, David Bowie]

The "In Ableton" section MUST translate this school into concrete Ableton moves AND cross-link these existing corpus files (do NOT re-teach mechanics — link them): corpus/daw/ableton/timeless/resampling-discipline.md, corpus/daw/ableton/timeless/beat-repeat-stutter-and-glitch.md, corpus/daw/ableton/devices/spectral-resonator-spectral-time-pitch-time-machine.md, corpus/daw/ableton/timeless/reamping-through-pedal-amp-cabinet.md, corpus/daw/ableton/timeless/audio-to-midi-extraction.md, corpus/daw/ableton/timeless/bounce-in-place-commit-discipline.md.
Cross-link these existing songwriting-corpus files in the See-also footer: arlo/workflows/eno-oblique-strategies.md, arlo/workflows/bowie-burroughs-cut-up.md, arlo/workflows/waits-break-the-demo.md.

Mandatory rules: mission-fit; anti-hallucination absolute (omit any unverifiable quote/technique/attribution); school-naming honesty; named-practitioner-first sourcing (Nigel Godrich/Radiohead interviews, Brian Eno on Talking Heads / Remain in Light, Tony Visconti on Bowie / Berlin era, Sodajerker, Song Exploder, Tape Notes); REFUSE AI-tutorial sites, fan blogs, listicles.
Default tags: cluster-workflow, taste-anchored, finishing-songs, art-rock, plus anchor-artist tags.

Efficiency guardrails: cap WebSearch at ~4 queries per file; if an attribution can't be verified in 2 queries, omit it; don't WebFetch the same URL twice; keep tone craft-focused and constructive.

After both files complete, list both with `ls -lh` and report word counts. Return a concise summary (under 250 words): files written, blockers, word counts. Do NOT paste file contents. Begin.
```

### Batch CW2 — Indie-folk / confessional

```
Run research batch CW2 for ARLO Taste-Driven Cluster Workflows.

You are a research-and-write agent producing seed knowledge-base entries for ARLO, a local-first AI songwriting/production assistant whose mission is to help musicians FINISH SONGS. This batch is DUAL OUTPUT.

Read /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-PROMPTS.md, /Users/cfitt/Dev/arlo/PROMPTS.md (base master template), /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-RESEARCH-PLAN.md, and /Users/cfitt/Dev/arlo/arlo/taste-profile/spotify-taste-profile.md.

Write TWO files:
1. Corpus chunk → /Users/cfitt/Dev/arlo/corpus/songwriting/cluster-workflows/indie-folk-confessional.md (1500–2500 words, standard ARLO chunk shape: front-matter, 8–15 H2 sections, Cited Retrieval Topics, Sources, See-also footer).
2. Workflow template → /Users/cfitt/Dev/arlo/arlo/workflows/indie-folk-confessional.md (600–1000 words). Frontmatter: name / origin / type / applicable_when / duration_estimate / taste_cluster / anchor_artists. Body sections: The premise / When ARLO should offer this / The steps / ARLO prompts for each step (verbatim) / In Ableton / When to abandon this workflow / Sources.

CLUSTER: lyric-and-intimacy-first; the song exists before the production; capture the performance, build outward sparingly.
ANCHOR ARTISTS: Bon Iver, Sufjan Stevens, Big Thief / Adrianne Lenker.
TYPE: lyrics-first
taste_cluster: indie-folk-confessional
anchor_artists: [Bon Iver, Sufjan Stevens, Big Thief]

The "In Ableton" section MUST translate this school into concrete Ableton moves AND cross-link these existing corpus files (do NOT re-teach mechanics — link them): corpus/daw/ableton/editing/comping-in-live-11-plus.md, corpus/daw/ableton/editing/warping-discipline.md, corpus/daw/ableton/timeless/live-as-looper-and-performance-instrument.md, corpus/daw/ableton/patterns/vocal-chains-in-live.md.
Cross-link these existing songwriting-corpus files in the See-also footer: arlo/workflows/sufjan-research-then-write.md, arlo/workflows/stems-first-production-first.md, arlo/workflows/nick-cave-letter-method.md, corpus/songwriting/lyric/image-stacking-technique.md, corpus/songwriting/form/through-composed-song-construction.md.

Mandatory rules: mission-fit; anti-hallucination absolute (omit any unverifiable quote/technique/attribution); school-naming honesty; named-practitioner-first sourcing (Justin Vernon/Bon Iver interviews, Sufjan in The Believer/Pitchfork, Adrianne Lenker/Big Thief in Sodajerker/Pitchfork); REFUSE AI-tutorial sites, fan blogs, listicles.
Default tags: cluster-workflow, taste-anchored, finishing-songs, indie-folk, plus anchor-artist tags.

Efficiency guardrails: cap WebSearch at ~4 queries per file; if an attribution can't be verified in 2 queries, omit it; don't WebFetch the same URL twice; keep tone craft-focused and constructive.

After both files complete, list both with `ls -lh` and report word counts. Return a concise summary (under 250 words): files written, blockers, word counts. Do NOT paste file contents. Begin.
```

### Batch CW3 — Electronic / groove-first

```
Run research batch CW3 for ARLO Taste-Driven Cluster Workflows.

You are a research-and-write agent producing seed knowledge-base entries for ARLO, a local-first AI songwriting/production assistant whose mission is to help musicians FINISH SONGS. This batch is DUAL OUTPUT.

Read /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-PROMPTS.md, /Users/cfitt/Dev/arlo/PROMPTS.md (base master template), /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-RESEARCH-PLAN.md, and /Users/cfitt/Dev/arlo/arlo/taste-profile/spotify-taste-profile.md.

Write TWO files:
1. Corpus chunk → /Users/cfitt/Dev/arlo/corpus/songwriting/cluster-workflows/electronic-groove-first.md (1500–2500 words, standard ARLO chunk shape: front-matter, 8–15 H2 sections, Cited Retrieval Topics, Sources, See-also footer).
2. Workflow template → /Users/cfitt/Dev/arlo/arlo/workflows/electronic-groove-first.md (600–1000 words). Frontmatter: name / origin / type / applicable_when / duration_estimate / taste_cluster / anchor_artists. Body sections: The premise / When ARLO should offer this / The steps / ARLO prompts for each step (verbatim) / In Ableton / When to abandon this workflow / Sources.

CLUSTER: groove-first, loop-and-arrangement-driven — build an 8-bar world, find the song in the arrangement, the rhythm section is the hook.
ANCHOR ARTISTS: LCD Soundsystem, Daft Punk, The Postal Service.
TYPE: production-first
taste_cluster: electronic-groove-first
anchor_artists: [LCD Soundsystem, Daft Punk, The Postal Service]

The "In Ableton" section MUST translate this school into concrete Ableton moves AND cross-link these existing corpus files (do NOT re-teach mechanics — link them): corpus/daw/ableton/timeless/eight-bars-first-discipline.md, corpus/daw/ableton/workflows/clip-launching-and-follow-actions.md, corpus/daw/ableton/timeless/drum-rack-as-multizone-instrument.md, corpus/daw/ableton/patterns/sidechain-ducking-classic-vs-modulator.md, corpus/daw/ableton/timeless/groove-pool-and-extracted-grooves.md, corpus/daw/ableton/workflows/session-vs-arrangement-view.md.
Cross-link these existing songwriting-corpus files in the See-also footer: arlo/workflows/tom-cosm-8-bar-loop-cycle.md, arlo/workflows/beat-first-topline-workflow.md, arlo/workflows/stems-first-production-first.md.

Mandatory rules: mission-fit; anti-hallucination absolute (omit any unverifiable quote/technique/attribution); school-naming honesty; named-practitioner-first sourcing (James Murphy/LCD interviews, Daft Punk / Bangalter & de Homem-Christo interviews, Jimmy Tamborello & Ben Gibbard on The Postal Service, Switched On Pop, Tape Notes); REFUSE AI-tutorial sites, fan blogs, listicles.
Default tags: cluster-workflow, taste-anchored, finishing-songs, electronic, plus anchor-artist tags.

Efficiency guardrails: cap WebSearch at ~4 queries per file; if an attribution can't be verified in 2 queries, omit it; don't WebFetch the same URL twice; keep tone craft-focused and constructive.

After both files complete, list both with `ls -lh` and report word counts. Return a concise summary (under 250 words): files written, blockers, word counts. Do NOT paste file contents. Begin.
```

### Batch CW4 — Lo-fi / prolific

```
Run research batch CW4 for ARLO Taste-Driven Cluster Workflows.

You are a research-and-write agent producing seed knowledge-base entries for ARLO, a local-first AI songwriting/production assistant whose mission is to help musicians FINISH SONGS. This batch is DUAL OUTPUT.

Read /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-PROMPTS.md, /Users/cfitt/Dev/arlo/PROMPTS.md (base master template), /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-RESEARCH-PLAN.md, and /Users/cfitt/Dev/arlo/arlo/taste-profile/spotify-taste-profile.md.

Write TWO files:
1. Corpus chunk → /Users/cfitt/Dev/arlo/corpus/songwriting/cluster-workflows/lo-fi-prolific-volume.md (1500–2500 words, standard ARLO chunk shape: front-matter, 8–15 H2 sections, Cited Retrieval Topics, Sources, See-also footer).
2. Workflow template → /Users/cfitt/Dev/arlo/arlo/workflows/lo-fi-prolific-volume.md (600–1000 words). Frontmatter: name / origin / type / applicable_when / duration_estimate / taste_cluster / anchor_artists. Body sections: The premise / When ARLO should offer this / The steps / ARLO prompts for each step (verbatim) / In Ableton / When to abandon this workflow / Sources.

CLUSTER: volume and speed over polish; the demo IS the song; finish-ugly; high output is the path to good songs.
ANCHOR ARTISTS: Car Seat Headrest, Modest Mouse.
TYPE: production-first
taste_cluster: lo-fi-prolific-volume
anchor_artists: [Car Seat Headrest, Modest Mouse]

The "In Ableton" section MUST translate this school into concrete Ableton moves AND cross-link these existing corpus files (do NOT re-teach mechanics — link them): corpus/daw/ableton/timeless/bounce-in-place-commit-discipline.md, corpus/daw/ableton/timeless/eight-bars-first-discipline.md, corpus/daw/ableton/devices/saturator-vs-roar.md, corpus/daw/ableton/timeless/resampling-discipline.md.
Cross-link these existing songwriting-corpus files in the See-also footer: arlo/workflows/spoon-two-demos-a-week.md, arlo/workflows/waits-break-the-demo.md, corpus/songwriting/finishing/finish-ugly-school.md, corpus/songwriting/stalls/the-demo-trap.md.

Mandatory rules: mission-fit; anti-hallucination absolute (omit any unverifiable quote/technique/attribution); school-naming honesty; named-practitioner-first sourcing (Will Toledo/Car Seat Headrest interviews on the Bandcamp-era prolificacy, Isaac Brock/Modest Mouse interviews, Sodajerker); REFUSE AI-tutorial sites, fan blogs, listicles.
Default tags: cluster-workflow, taste-anchored, finishing-songs, lo-fi, plus anchor-artist tags.

Efficiency guardrails: cap WebSearch at ~4 queries per file; if an attribution can't be verified in 2 queries, omit it; don't WebFetch the same URL twice; keep tone craft-focused and constructive.

After both files complete, list both with `ls -lh` and report word counts. Return a concise summary (under 250 words): files written, blockers, word counts. Do NOT paste file contents. Begin.
```

### Batch CW5 — Post-punk / texture & dynamics

```
Run research batch CW5 for ARLO Taste-Driven Cluster Workflows.

You are a research-and-write agent producing seed knowledge-base entries for ARLO, a local-first AI songwriting/production assistant whose mission is to help musicians FINISH SONGS. This batch is DUAL OUTPUT.

Read /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-PROMPTS.md, /Users/cfitt/Dev/arlo/PROMPTS.md (base master template), /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-RESEARCH-PLAN.md, and /Users/cfitt/Dev/arlo/arlo/taste-profile/spotify-taste-profile.md.

Write TWO files:
1. Corpus chunk → /Users/cfitt/Dev/arlo/corpus/songwriting/cluster-workflows/post-punk-texture-dynamics.md (1500–2500 words, standard ARLO chunk shape: front-matter, 8–15 H2 sections, Cited Retrieval Topics, Sources, See-also footer).
2. Workflow template → /Users/cfitt/Dev/arlo/arlo/workflows/post-punk-texture-dynamics.md (600–1000 words). Frontmatter: name / origin / type / applicable_when / duration_estimate / taste_cluster / anchor_artists. Body sections: The premise / When ARLO should offer this / The steps / ARLO prompts for each step (verbatim) / In Ableton / When to abandon this workflow / Sources.

CLUSTER: texture, repetition, dynamics and build over conventional verse-chorus; tension through restraint and accumulation.
ANCHOR ARTISTS: Black Country New Road, Swans, Joy Division.
TYPE: exploring
taste_cluster: post-punk-texture-dynamics
anchor_artists: [Black Country New Road, Swans, Joy Division]

The "In Ableton" section MUST translate this school into concrete Ableton moves AND cross-link these existing corpus files (do NOT re-teach mechanics — link them): corpus/daw/ableton/timeless/live-as-looper-and-performance-instrument.md, corpus/daw/ableton/timeless/beat-repeat-stutter-and-glitch.md, corpus/daw/ableton/timeless/send-return-as-parallel-bus.md, corpus/daw/ableton/timeless/velocity-randomization-and-humanization.md.
Cross-link these existing songwriting-corpus files in the See-also footer: corpus/songwriting/form/through-composed-song-construction.md, arlo/workflows/eno-oblique-strategies.md, corpus/songwriting/melodic-harmonic/pedal-tones-drones-anchoring.md.

Mandatory rules: mission-fit; anti-hallucination absolute (omit any unverifiable quote/technique/attribution); school-naming honesty; named-practitioner-first sourcing (Michael Gira/Swans interviews, Black Country New Road interviews, Joy Division / Martin Hannett production documented history, Sodajerker); REFUSE AI-tutorial sites, fan blogs, listicles.
Default tags: cluster-workflow, taste-anchored, finishing-songs, post-punk, plus anchor-artist tags.

Efficiency guardrails: cap WebSearch at ~4 queries per file; if an attribution can't be verified in 2 queries, omit it; don't WebFetch the same URL twice; keep tone craft-focused and constructive.

After both files complete, list both with `ls -lh` and report word counts. Return a concise summary (under 250 words): files written, blockers, word counts. Do NOT paste file contents. Begin.
```

---

## Tracking

- [x] Batch CW1 — Art-rock / studio-as-instrument *(corpus chunk + workflow template)*
- [x] Batch CW2 — Indie-folk / confessional *(corpus chunk + workflow template)*
- [x] Batch CW3 — Electronic / groove-first *(corpus chunk + workflow template)*
- [x] Batch CW4 — Lo-fi / prolific *(corpus chunk + workflow template)*
- [x] Batch CW5 — Post-punk / texture & dynamics *(corpus chunk + workflow template)*

When all 5 are checked, the corpus has **5 new cluster corpus chunks + 5 new workflow templates** = **10 artifacts**, plus the taste-profile artifact.
