# Taste-Driven Cluster Workflows — Design Spec

**Date:** 2026-05-28
**Status:** Approved (design phase)
**Stream:** Cluster Workflows (artist-derived, taste-anchored)

## Problem

ARLO's mission is to help musicians finish songs. The existing songwriting-craft corpus
(66 artifacts: 51 corpus chunks + 15 workflow templates) skews folk/lyric. The user's
actual 10-year Spotify listening history skews art-rock and electronic. The user's
dominant artists by listening time — Radiohead (#1, 88h, 3.5× the #2) and LCD Soundsystem
(#2) — and the whole art-rock/electronic spine (Talking Heads, Daft Punk) have **no
workflow** in the corpus.

Goal: import enough seed data, derived from the user's most-listened artists, that an ARLO
agent can walk the user through songwriting workflows tailored to their taste, find what
works, repeat it, and iterate — so they produce songs faster. This effort delivers the
**knowledge-import layer**; the iterate-loop reuses ARLO's existing workflow-template
structure.

## Data provenance

- Source: Spotify Extended Streaming History export (`Streaming_History_Audio_2015-2023_0.json`,
  `Streaming_History_Audio_2023-2025_1.json`).
- 31,106 audio streams, 2015-06-11 → 2025-11-06.
- Engagement metric: **total `ms_played`** (hours listened) as primary signal, play count as secondary.
- **Tapir!** is excluded per user instruction (Spotify metadata error, not a real listening signal).

### Top artists by total hours (all-time, excl. Tapir!)

Radiohead (88h), LCD Soundsystem (38h), Car Seat Headrest (33h), Talking Heads (28h),
Bon Iver (26h), Sufjan Stevens (25h), David Bowie (20h), Modest Mouse (20h),
The Postal Service (17h), Arcade Fire (16h), Daft Punk (15h), Death Cab for Cutie (15h),
The Mountain Goats (15h), Leonard Cohen (14h), Big Thief (13h), Future Islands (13h),
Neutral Milk Hotel (12h), The Decemberists (12h), Tyler, The Creator (12h),
Black Country New Road (11h), and the rest of a stable long tail. The recent 2023–2025
window confirms the same core (Radiohead 60h, LCD 25h, Sufjan 22h, Bon Iver 21h),
with Sufjan/Bon Iver rising and Swans + Adrianne Lenker appearing.

## Scope decisions (locked with user)

| Decision | Choice |
|---|---|
| Plan focus | **Knowledge import first**; iterate-loop reuses existing workflow-template structure |
| Granularity | **One workflow per cluster** (5 clusters), each citing 2–3 anchor artists |
| Ableton angle | **Bridge layer** — translate the school into Ableton moves + cross-link the existing `daw/ableton/` corpus; do NOT re-teach mechanics |
| Cluster roster | **All 5 clusters** (incl. an indie-folk synthesis that ties together existing folk workflows) |
| Output structure | **Approach 1 — dual output** (corpus chunk + workflow template per cluster) mirroring the proven Bucket A pattern |
| Execution depth | **Carry through to dispatch + verify** — same end-to-end run as S1–S8 |

## Deliverables

12 content files + 3 scaffold files.

### 1. Taste-profile artifact (1 file)

`arlo/taste-profile/spotify-taste-profile.md` — personal context (not general corpus
knowledge). Contains: the 5 clusters with anchor artists, all-time vs. recent rankings,
listening signals (hours, play count, completion/skip behavior), the Tapir! exclusion note,
and data provenance. **Written first** — it defines the `anchor_artists` the workflows reference.
ARLO reads this to taste-match workflows to the user.

### 2. Cluster corpus chunks (5 files)

`corpus/songwriting/cluster-workflows/<slug>.md` — 1500–2500 words each. Standard ARLO chunk
shape (front-matter, H2 sections, Cited Retrieval Topics, Sources, See-also footer). The
retrievable knowledge layer: how each school actually writes/produces, anchored to the user's
artists, with verified sourcing.

### 3. Cluster workflow templates (5 files)

`arlo/workflows/<slug>.md` — 600–1000 words each. Sits alongside the existing 15 templates.
Existing frontmatter schema (name / origin / type / applicable_when / duration_estimate)
**plus two new fields**:

```yaml
taste_cluster: art-rock-studio
anchor_artists: [Radiohead, Talking Heads, David Bowie]
```

Body sections (existing schema): The premise / When ARLO should offer this / The steps /
ARLO prompts for each step (verbatim) / When to abandon this workflow / Sources — **plus one
new section: "In Ableton"** (concrete moves + explicit cross-links into `daw/ableton/`).

### 4. Scaffold files (3 files)

Following the project's existing stream convention so execution reuses the parallel-agent
batch system:
- `CLUSTER-WORKFLOWS-RESEARCH-PLAN.md` — sourcing philosophy, cluster definitions, anchor
  artists, Ableton bridge targets, cross-stream boundaries.
- `CLUSTER-WORKFLOWS-PROMPTS.md` — per-cluster master-template rows + stream addendum.
- `CLUSTER-WORKFLOWS-SESSIONS.md` — 5 paste-able agent kickoff messages (one per cluster),
  dual-output spec, guardrails.

## The 5 clusters

### 1. Art-rock / studio-as-instrument — `art-rock-studio-as-instrument`
- **Thesis:** the arrangement/studio IS the compositional act — songs emerge from
  sound-design, re-contextualizing parts, and productive constraint, not from a finished
  song played into a mic.
- **Anchors:** Radiohead (#1), Talking Heads, David Bowie.
- **Ableton bridge:** resampling-discipline, beat-repeat-stutter-and-glitch,
  spectral-resonator-spectral-time-pitch-time-machine, reamping-through-pedal-amp-cabinet,
  audio-to-midi-extraction, bounce-in-place-commit-discipline.
- **Corpus cross-links:** eno-oblique-strategies, bowie-burroughs-cut-up, waits-break-the-demo.
- **Type:** production-first.

### 2. Indie-folk / confessional (synthesis) — `indie-folk-confessional`
- **Thesis:** lyric-and-intimacy-first; the song exists before the production; capture the
  performance, build outward sparingly. Ties the existing Sufjan/Bon Iver/Big Thief
  workflows into one decision-layer.
- **Anchors:** Bon Iver, Sufjan Stevens, Big Thief / Adrianne Lenker.
- **Ableton bridge:** comping-in-live-11-plus, warping-discipline, live-as-looper-and-performance-instrument,
  vocal-chains-in-live.
- **Corpus cross-links:** sufjan-research-then-write, stems-first-production-first,
  nick-cave-letter-method, lyric/image-stacking-technique (C6), form/through-composed (E5).
- **Type:** lyrics-first.

### 3. Electronic / dance-leaning (groove-first) — `electronic-groove-first`
- **Thesis:** groove-first, loop-and-arrangement-driven — build an 8-bar world, find the
  song in the arrangement, the rhythm section is the hook.
- **Anchors:** LCD Soundsystem (#2), Daft Punk, The Postal Service.
- **Ableton bridge:** eight-bars-first-discipline, clip-launching-and-follow-actions,
  drum-rack-as-multizone-instrument, sidechain-ducking-classic-vs-modulator, groove-pool-and-extracted-grooves,
  session-vs-arrangement-view.
- **Corpus cross-links:** tom-cosm-8-bar-loop-cycle, beat-first-topline-workflow, stems-first-production-first.
- **Type:** production-first / beat-first.

### 4. Lo-fi / prolific (volume over polish) — `lo-fi-prolific-volume`
- **Thesis:** volume and speed over polish; the demo IS the song; finish-ugly; high output
  is the path to good songs.
- **Anchors:** Car Seat Headrest, Modest Mouse.
- **Ableton bridge:** bounce-in-place-commit-discipline, eight-bars-first-discipline,
  saturator-vs-roar (grit), resampling-discipline (lo-fi character).
- **Corpus cross-links:** spoon-two-demos-a-week, waits-break-the-demo,
  finishing/finish-ugly-school (F3), stalls/the-demo-trap.
- **Type:** production-first.

### 5. Post-punk / experimental (texture & dynamics) — `post-punk-texture-dynamics`
- **Thesis:** texture, repetition, dynamics and build over conventional verse-chorus;
  tension through restraint and accumulation.
- **Anchors:** Black Country New Road, Swans, Joy Division.
- **Ableton bridge:** live-as-looper-and-performance-instrument, beat-repeat-stutter-and-glitch,
  send-return-as-parallel-bus, velocity-randomization-and-humanization.
- **Corpus cross-links:** form/through-composed (E5), eno-oblique-strategies,
  melodic-harmonic/pedal-tones-drones-anchoring (D6).
- **Type:** exploring / production-first.

## Sourcing discipline (identical to songwriting-craft stream)

- **Named-practitioner-first** with citable interviews/books. Gold-standard sources for
  these artists: Sodajerker, Tape Notes, Song Exploder, Switched On Pop, Rick Beato,
  Pitchfork / The Believer interviews, plus producer testimony (Nigel Godrich for Radiohead,
  Tony Visconti for Bowie, Brian Eno's published work for Talking Heads).
- **Anti-hallucination is absolute** — omit any quote/technique/attribution that can't be
  verified. Fabricated process claims about real artists poison retrieval worst of all.
- **School-naming honesty** — "Godrich's method is X" beats "the right way is X." Surface
  disagreement between schools.
- **Genre/era-bound claims named as such.**
- **REFUSE:** AI-tutorial sites, fan blogs, generic listicles.

## Execution model

Reuses the proven parallel-agent batch system (S1–S8).

1. **Write the taste-profile artifact directly** — it is analysis of the user's own data
   (no research needed) and must exist first so workflows can reference its anchor_artists.
2. **Write the 3 scaffold files** (RESEARCH-PLAN, PROMPTS, SESSIONS).
3. **Dispatch 5 parallel dual-output research agents** (one per cluster), each producing its
   corpus chunk + workflow template. Same pattern as Bucket A. **Efficiency guardrails baked
   in from the start** (learned from the S5 timeout/content-filter incidents):
   - Cap WebSearch at ~4 queries per file; omit unverifiable attributions after 2 queries.
   - Don't WebFetch the same URL twice.
   - Keep tone craft-focused and constructive.
4. **Verification pass:** file counts (5 corpus + 5 templates), frontmatter schema incl. the
   2 new fields, Ableton-bridge cross-links resolve to real `daw/ableton/` files, no
   AI-tutorial citations, See-also footers present.

## How it plugs into the iterate-loop (enablement only — no new system built)

ARLO reads `arlo/taste-profile/spotify-taste-profile.md` → matches `taste_cluster` /
`anchor_artists` to surface workflows that fit the user's taste → the user sets
`workflow: <slug>` in a song's `ARLO.md` → ARLO runs the template's verbatim step prompts →
the user notes the outcome in that song's `ARLO.md`. Over repeated songs, which clusters
actually produce *finishes* becomes visible. The taste profile + 2 new frontmatter fields
are the **only** additions; everything else is existing structure.

## Out of scope

- The iterate-loop *system* (automated tracking of what works, dynamic recommendation
  composition) — deferred; this effort only enables it via the taste profile + frontmatter.
- Re-covering already-built individual workflows (Bowie cut-up, Sufjan research-first,
  Bon Iver stems-first, Big Thief through-composed) — referenced via cross-links, not rebuilt.
- DAW mechanics — owned by the existing `daw/ableton/` corpus, cross-linked not duplicated.

## Success criteria

- 12 content files written, all passing the verification pass.
- Each workflow template carries `taste_cluster` + `anchor_artists` and an "In Ableton"
  section with cross-links that resolve to real files.
- Every claim about a real artist's process is traceable to a verifiable named source;
  zero fabricated attributions.
- The taste profile accurately reflects the analyzed data (clusters, rankings, Tapir! excluded).
