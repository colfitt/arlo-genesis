# Taste-Driven Cluster Workflows Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce 5 taste-anchored songwriting cluster workflows (dual-output: corpus chunk + workflow template each) derived from the user's Spotify listening history, plus a taste-profile artifact and 3 scaffold files, then dispatch the research and verify.

**Architecture:** Mirror the proven S1–S8 parallel-agent batch pattern. Write the taste profile and scaffold files first (deterministic, no research), then dispatch 5 parallel dual-output research agents (one per cluster), then run a verification pass. The new cluster workflows are a bridge layer: songwriting decisions + artist→Ableton mapping, cross-linking the existing `daw/ableton/` corpus rather than duplicating mechanics.

**Tech Stack:** Markdown corpus files with YAML frontmatter; `jq` for data verification; the Agent tool (general-purpose, background) for parallel research; `git` for commits.

**Spec:** `docs/superpowers/specs/2026-05-28-cluster-workflows-design.md`

**Cluster reference (from spec):**

| # | Slug | Thesis | Anchors | Type |
|---|------|--------|---------|------|
| 1 | `art-rock-studio-as-instrument` | arrangement/studio IS the compositional act | Radiohead, Talking Heads, Bowie | production-first |
| 2 | `indie-folk-confessional` | lyric-and-intimacy-first; song before production | Bon Iver, Sufjan, Big Thief | lyrics-first |
| 3 | `electronic-groove-first` | groove-first, loop-and-arrangement-driven | LCD Soundsystem, Daft Punk, Postal Service | production-first |
| 4 | `lo-fi-prolific-volume` | volume/speed over polish; demo IS the song | Car Seat Headrest, Modest Mouse | production-first |
| 5 | `post-punk-texture-dynamics` | texture, repetition, dynamics, build | Black Country New Road, Swans, Joy Division | exploring |

---

### Task 1: Create directories and write the taste-profile artifact

**Files:**
- Create dir: `arlo/taste-profile/`
- Create dir: `corpus/songwriting/cluster-workflows/`
- Create: `arlo/taste-profile/spotify-taste-profile.md`

- [ ] **Step 1: Create target directories**

Run:
```bash
mkdir -p /Users/cfitt/Dev/arlo/arlo/taste-profile /Users/cfitt/Dev/arlo/corpus/songwriting/cluster-workflows
```
Expected: directories exist (verify with `ls -d`).

- [ ] **Step 2: Write the taste-profile artifact**

Write `arlo/taste-profile/spotify-taste-profile.md` with this exact content:

```markdown
---
title: Spotify Taste Profile
source: Spotify Extended Streaming History export (2015-06-11 → 2025-11-06)
scope: Personal listening-derived taste profile that ARLO uses to taste-match workflows to the user
records_analyzed: 31106
primary_metric: total ms_played (hours listened)
excluded: ["Tapir! (Spotify metadata error, per user)"]
generated: 2026-05-28
tags: [taste-profile, personal-context, cluster-workflows]
---

# Spotify Taste Profile

This profile is derived from 31,106 audio streams (2015–2025). It is **personal context**,
not general-corpus knowledge. ARLO reads it to surface workflows whose `taste_cluster` /
`anchor_artists` match the user's listening, and to anchor conversation in artists the user
actually loves.

## Top artists by total hours (all-time, excl. Tapir!)

| Hours | Plays | Artist |
|------:|------:|--------|
| 88 | 1871 | Radiohead |
| 38 | 536 | LCD Soundsystem |
| 33 | 503 | Car Seat Headrest |
| 28 | 480 | Talking Heads |
| 26 | 651 | Bon Iver |
| 25 | 386 | Sufjan Stevens |
| 20 | 342 | David Bowie |
| 20 | 369 | Modest Mouse |
| 17 | 272 | The Postal Service |
| 16 | 302 | Arcade Fire |
| 15 | 253 | Daft Punk |
| 15 | 300 | Death Cab for Cutie |
| 15 | 475 | The Mountain Goats |
| 14 | 220 | Leonard Cohen |
| 13 | 243 | Big Thief |
| 13 | 281 | Future Islands |
| 12 | 307 | Neutral Milk Hotel |
| 12 | 254 | The Decemberists |
| 12 | 275 | Tyler, The Creator |
| 11 | 148 | Black Country, New Road |

## Recent window (2023–2025) confirms the same core

Radiohead (60h), LCD Soundsystem (25h), Sufjan (22h), Bon Iver (21h), Talking Heads (19h),
Car Seat Headrest (18h), The Postal Service (17h). Notable recent risers: Sufjan and Bon Iver
(folk lean up), Swans and Adrianne Lenker appearing. Taste is stable across the decade.

## The 5 clusters

### 1. Art-rock / studio-as-instrument — `art-rock-studio-as-instrument`
Anchors: **Radiohead, Talking Heads, David Bowie.** The arrangement/studio is the
compositional act; songs emerge from sound-design and re-contextualization.

### 2. Indie-folk / confessional — `indie-folk-confessional`
Anchors: **Bon Iver, Sufjan Stevens, Big Thief / Adrianne Lenker.** Lyric-and-intimacy-first;
capture the performance, build outward sparingly.

### 3. Electronic / dance-leaning — `electronic-groove-first`
Anchors: **LCD Soundsystem, Daft Punk, The Postal Service.** Groove-first, loop-and-arrangement
driven; the rhythm section is the hook.

### 4. Lo-fi / prolific — `lo-fi-prolific-volume`
Anchors: **Car Seat Headrest, Modest Mouse.** Volume and speed over polish; the demo is the song.

### 5. Post-punk / experimental — `post-punk-texture-dynamics`
Anchors: **Black Country New Road, Swans, Joy Division.** Texture, repetition, dynamics, and
build over conventional verse-chorus.

## How ARLO uses this

1. Match the user's `taste_cluster` to surface fitting workflows from `arlo/workflows/`.
2. Anchor examples in the user's own artists when explaining a technique.
3. Over repeated songs, track which clusters produce *finishes* (noted in each song's `ARLO.md`).
```

- [ ] **Step 3: Verify the taste profile**

Run:
```bash
test -f /Users/cfitt/Dev/arlo/arlo/taste-profile/spotify-taste-profile.md && \
grep -c "art-rock-studio-as-instrument\|indie-folk-confessional\|electronic-groove-first\|lo-fi-prolific-volume\|post-punk-texture-dynamics" /Users/cfitt/Dev/arlo/arlo/taste-profile/spotify-taste-profile.md && \
grep -qi "Tapir" /Users/cfitt/Dev/arlo/arlo/taste-profile/spotify-taste-profile.md && echo "OK: 5 cluster slugs present, Tapir exclusion noted"
```
Expected: prints a count ≥ 5 then `OK: ...`.

- [ ] **Step 4: Commit**

```bash
git add arlo/taste-profile/spotify-taste-profile.md
git commit -m "Add Spotify taste-profile artifact for cluster workflows"
```

---

### Task 2: Write CLUSTER-WORKFLOWS-RESEARCH-PLAN.md

**Files:**
- Create: `CLUSTER-WORKFLOWS-RESEARCH-PLAN.md`

- [ ] **Step 1: Write the research plan**

Write `/Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-RESEARCH-PLAN.md` covering, in full prose (no placeholders):

1. **Mission fit** — every workflow must help a stuck musician finish a song; cut anything that doesn't.
2. **Sourcing tiers (named-practitioner-first):** Tier 1 = Sodajerker, Tape Notes, Song Exploder, Switched On Pop, Rick Beato, Pitchfork/The Believer interviews, and producer testimony (Nigel Godrich → Radiohead; Tony Visconti → Bowie; Brian Eno's published writing → Talking Heads; Thomas Bangalter/Guy-Manuel interviews → Daft Punk; James Murphy interviews → LCD; Will Toledo interviews → Car Seat Headrest). Tier 2 = reputable long-form music journalism. **REFUSE:** AI-tutorial sites, fan blogs, generic listicles.
3. **Anti-hallucination is absolute** — omit any quote/technique/attribution that can't be verified; fabricated process claims about real artists poison retrieval worst of all.
4. **School-naming honesty** — "Godrich's method is X" beats "the right way is X."
5. **Bridge-layer rule** — do NOT re-teach Ableton mechanics; translate the school into Ableton moves and cross-link the existing `daw/ableton/` files listed per cluster in the spec.
6. **Cross-stream boundaries** — reference (don't rebuild) the already-built individual workflows (bowie-burroughs-cut-up, sufjan-research-then-write, stems-first-production-first, etc.).
7. **The 5 clusters** — paste the cluster reference table from this plan's header (slug / thesis / anchors / Ableton-bridge targets / corpus cross-links / type), copying the per-cluster Ableton-bridge and cross-link lists verbatim from the spec's "The 5 clusters" section.

- [ ] **Step 2: Verify**

Run:
```bash
test -f /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-RESEARCH-PLAN.md && \
grep -qi "anti-hallucination" /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-RESEARCH-PLAN.md && \
grep -qi "Sodajerker" /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-RESEARCH-PLAN.md && echo "OK"
```
Expected: `OK`.

---

### Task 3: Write CLUSTER-WORKFLOWS-PROMPTS.md

**Files:**
- Create: `CLUSTER-WORKFLOWS-PROMPTS.md`

- [ ] **Step 1: Write the prompts/master-template rows**

Write `/Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-PROMPTS.md` containing:

1. **Stream addendum** — the clauses every cluster file must honor: mission-fit, source preference, honesty about subjectivity, dual-output (corpus chunk + workflow template), the new frontmatter fields (`taste_cluster`, `anchor_artists`), the mandatory "In Ableton" body section, and default tags `cluster-workflow`, `taste-anchored`, `finishing-songs` plus a per-cluster tag.
2. **Dual-output spec** — corpus chunk at `corpus/songwriting/cluster-workflows/<slug>.md` (1500–2500w, standard ARLO chunk shape) + workflow template at `arlo/workflows/<slug>.md` (600–1000w, frontmatter + body sections incl. "In Ableton").
3. **One topic row per cluster (CW1–CW5)** with variables filled from the cluster reference table: Title, Slug, Thesis, Anchor artists, Type, Ableton-bridge targets (exact `daw/ableton/` filenames), Corpus cross-links, Tags. Copy the per-cluster lists verbatim from the spec.

- [ ] **Step 2: Verify**

Run:
```bash
test -f /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-PROMPTS.md && \
grep -c "CW[1-5]" /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-PROMPTS.md && \
grep -qi "In Ableton" /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-PROMPTS.md && echo "OK: 5 topic rows"
```
Expected: count ≥ 5, then `OK`.

---

### Task 4: Write CLUSTER-WORKFLOWS-SESSIONS.md (the 5 agent kickoff messages)

**Files:**
- Create: `CLUSTER-WORKFLOWS-SESSIONS.md`

- [ ] **Step 1: Write the sessions file**

Write `/Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-SESSIONS.md` with: a How-to-run section, a batch-overview table (CW1–CW5), a tracking checklist, and the **5 kickoff messages below verbatim** (these are the exact prompts dispatched in Task 5, so they are self-contained). Each kickoff is one paste-able block.

The shared kickoff skeleton (used for all 5, with per-cluster blocks substituted):

> Run research batch {CW_ID} for ARLO Taste-Driven Cluster Workflows.
>
> You are a research-and-write agent producing seed knowledge-base entries for ARLO, a local-first AI songwriting/production assistant whose mission is to help musicians FINISH SONGS. This batch is DUAL OUTPUT.
>
> Read /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-PROMPTS.md, /Users/cfitt/Dev/arlo/PROMPTS.md (base master template), /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-RESEARCH-PLAN.md, and /Users/cfitt/Dev/arlo/arlo/taste-profile/spotify-taste-profile.md.
>
> Write TWO files:
> 1. Corpus chunk → /Users/cfitt/Dev/arlo/corpus/songwriting/cluster-workflows/{slug}.md (1500–2500 words, standard ARLO chunk shape: front-matter, 8–15 H2 sections, Cited Retrieval Topics, Sources, See-also footer).
> 2. Workflow template → /Users/cfitt/Dev/arlo/arlo/workflows/{slug}.md (600–1000 words). Frontmatter: name / origin / type / applicable_when / duration_estimate / taste_cluster / anchor_artists. Body sections: The premise / When ARLO should offer this / The steps / ARLO prompts for each step (verbatim) / **In Ableton** / When to abandon this workflow / Sources.
>
> CLUSTER: {thesis paragraph}
> ANCHOR ARTISTS: {anchors}
> TYPE: {type}
> taste_cluster: {slug}
> anchor_artists: {anchors as list}
>
> The "In Ableton" section MUST translate this school into concrete Ableton moves AND cross-link these existing corpus files (do NOT re-teach mechanics — link them): {Ableton-bridge targets}.
> Cross-link these existing songwriting-corpus files in the See-also footer: {corpus cross-links}.
>
> Mandatory rules: mission-fit; anti-hallucination absolute (omit any unverifiable quote/technique/attribution); school-naming honesty; named-practitioner-first sourcing ({named sources for this cluster}); REFUSE AI-tutorial sites, fan blogs, listicles.
> Default tags: cluster-workflow, taste-anchored, finishing-songs, {per-cluster tag}, plus anchor-artist tags.
>
> Efficiency guardrails: cap WebSearch at ~4 queries per file; if an attribution can't be verified in 2 queries, omit it; don't WebFetch the same URL twice; keep tone craft-focused and constructive.
>
> After both files complete, list both with `ls -lh` and report word counts. Return a concise summary (under 250 words): files written, blockers, word counts. Do NOT paste file contents. Begin.

Per-cluster substitution blocks:

- **CW1** slug `art-rock-studio-as-instrument`; thesis "the arrangement/studio IS the compositional act — songs emerge from sound-design, re-contextualizing parts, and productive constraint, not from a finished song played into a mic"; anchors Radiohead, Talking Heads, David Bowie; type production-first; Ableton-bridge `corpus/daw/ableton/timeless/resampling-discipline.md`, `corpus/daw/ableton/timeless/beat-repeat-stutter-and-glitch.md`, `corpus/daw/ableton/devices/spectral-resonator-spectral-time-pitch-time-machine.md`, `corpus/daw/ableton/timeless/reamping-through-pedal-amp-cabinet.md`, `corpus/daw/ableton/timeless/audio-to-midi-extraction.md`, `corpus/daw/ableton/timeless/bounce-in-place-commit-discipline.md`; cross-links `arlo/workflows/eno-oblique-strategies.md`, `arlo/workflows/bowie-burroughs-cut-up.md`, `arlo/workflows/waits-break-the-demo.md`; per-cluster tag `art-rock`; named sources Nigel Godrich/Radiohead interviews, Brian Eno on Talking Heads (Remain in Light), Tony Visconti on Bowie (Berlin era), Sodajerker, Song Exploder, Tape Notes.
- **CW2** slug `indie-folk-confessional`; thesis "lyric-and-intimacy-first; the song exists before the production; capture the performance, build outward sparingly"; anchors Bon Iver, Sufjan Stevens, Big Thief / Adrianne Lenker; type lyrics-first; Ableton-bridge `corpus/daw/ableton/editing/comping-in-live-11-plus.md`, `corpus/daw/ableton/editing/warping-discipline.md`, `corpus/daw/ableton/timeless/live-as-looper-and-performance-instrument.md`, `corpus/daw/ableton/patterns/vocal-chains-in-live.md`; cross-links `arlo/workflows/sufjan-research-then-write.md`, `arlo/workflows/stems-first-production-first.md`, `arlo/workflows/nick-cave-letter-method.md`, `corpus/songwriting/lyric/image-stacking-technique.md`, `corpus/songwriting/form/through-composed-song-construction.md`; per-cluster tag `indie-folk`; named sources Justin Vernon/Bon Iver interviews, Sufjan in The Believer/Pitchfork, Adrianne Lenker/Big Thief in Sodajerker/Pitchfork.
- **CW3** slug `electronic-groove-first`; thesis "groove-first, loop-and-arrangement-driven — build an 8-bar world, find the song in the arrangement, the rhythm section is the hook"; anchors LCD Soundsystem, Daft Punk, The Postal Service; type production-first; Ableton-bridge `corpus/daw/ableton/timeless/eight-bars-first-discipline.md`, `corpus/daw/ableton/workflows/clip-launching-and-follow-actions.md`, `corpus/daw/ableton/timeless/drum-rack-as-multizone-instrument.md`, `corpus/daw/ableton/patterns/sidechain-ducking-classic-vs-modulator.md`, `corpus/daw/ableton/timeless/groove-pool-and-extracted-grooves.md`, `corpus/daw/ableton/workflows/session-vs-arrangement-view.md`; cross-links `arlo/workflows/tom-cosm-8-bar-loop-cycle.md`, `arlo/workflows/beat-first-topline-workflow.md`, `arlo/workflows/stems-first-production-first.md`; per-cluster tag `electronic`; named sources James Murphy/LCD interviews, Daft Punk (Bangalter/de Homem-Christo) interviews, Jimmy Tamborello & Ben Gibbard on The Postal Service, Switched On Pop, Tape Notes.
- **CW4** slug `lo-fi-prolific-volume`; thesis "volume and speed over polish; the demo IS the song; finish-ugly; high output is the path to good songs"; anchors Car Seat Headrest, Modest Mouse; type production-first; Ableton-bridge `corpus/daw/ableton/timeless/bounce-in-place-commit-discipline.md`, `corpus/daw/ableton/timeless/eight-bars-first-discipline.md`, `corpus/daw/ableton/devices/saturator-vs-roar.md`, `corpus/daw/ableton/timeless/resampling-discipline.md`; cross-links `arlo/workflows/spoon-two-demos-a-week.md`, `arlo/workflows/waits-break-the-demo.md`, `corpus/songwriting/finishing/finish-ugly-school.md`, `corpus/songwriting/stalls/the-demo-trap.md`; per-cluster tag `lo-fi`; named sources Will Toledo/Car Seat Headrest interviews (the Bandcamp-era prolificacy), Isaac Brock/Modest Mouse interviews, Sodajerker.
- **CW5** slug `post-punk-texture-dynamics`; thesis "texture, repetition, dynamics and build over conventional verse-chorus; tension through restraint and accumulation"; anchors Black Country New Road, Swans, Joy Division; type exploring; Ableton-bridge `corpus/daw/ableton/timeless/live-as-looper-and-performance-instrument.md`, `corpus/daw/ableton/timeless/beat-repeat-stutter-and-glitch.md`, `corpus/daw/ableton/timeless/send-return-as-parallel-bus.md`, `corpus/daw/ableton/timeless/velocity-randomization-and-humanization.md`; cross-links `corpus/songwriting/form/through-composed-song-construction.md`, `arlo/workflows/eno-oblique-strategies.md`, `corpus/songwriting/melodic-harmonic/pedal-tones-drones-anchoring.md`; per-cluster tag `post-punk`; named sources Michael Gira/Swans interviews, Black Country New Road interviews, Joy Division (Martin Hannett production) documented history, Sodajerker.

- [ ] **Step 2: Verify**

Run:
```bash
test -f /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-SESSIONS.md && \
grep -c "Run research batch CW" /Users/cfitt/Dev/arlo/CLUSTER-WORKFLOWS-SESSIONS.md && echo "OK: kickoffs present"
```
Expected: count = 5, then `OK`.

- [ ] **Step 3: Commit scaffold files**

```bash
git add CLUSTER-WORKFLOWS-RESEARCH-PLAN.md CLUSTER-WORKFLOWS-PROMPTS.md CLUSTER-WORKFLOWS-SESSIONS.md
git commit -m "Add cluster-workflows scaffold files (research plan, prompts, sessions)"
```

---

### Task 5: Dispatch the 5 parallel research agents

**Files:** none created directly here; the agents write the 10 content files.

- [ ] **Step 1: Dispatch all 5 agents in parallel (background)**

Using the Agent tool (subagent_type `general-purpose`, `run_in_background: true`), dispatch one agent per cluster (CW1–CW5). Each agent's prompt is the corresponding **self-contained kickoff message from Task 4** (substituted block inlined — the agent does not depend on reading the scaffold files, though it may). Send all 5 in a single message so they run concurrently.

Expected: 5 "Async agent launched successfully" results with agentIds.

- [ ] **Step 2: Track each agent as a task**

Create a TaskCreate entry per cluster (CW1–CW5) set to in_progress; mark completed as each notification arrives.

- [ ] **Step 3: Handle failures by re-dispatch (lesson from S5)**

If an agent returns a stream-idle timeout or content-filter block, check which of its 2 files landed (`ls corpus/songwriting/cluster-workflows/ arlo/workflows/`) and re-dispatch only the missing file(s) with tightened guardrails. Do not re-run completed files.

---

### Task 6: Verification pass, checklist, and final commit

**Files:**
- Modify: `CLUSTER-WORKFLOWS-SESSIONS.md` (check off CW1–CW5)

- [ ] **Step 1: File-count + structure check**

Run:
```bash
cd /Users/cfitt/Dev/arlo
echo "corpus chunks (expect 5):"; ls corpus/songwriting/cluster-workflows/*.md | wc -l
echo "new workflow templates present (expect 5 new):"; ls arlo/workflows/{art-rock-studio-as-instrument,indie-folk-confessional,electronic-groove-first,lo-fi-prolific-volume,post-punk-texture-dynamics}.md 2>&1
```
Expected: corpus count = 5; all 5 template paths resolve (no "No such file").

- [ ] **Step 2: Frontmatter schema check (the 2 new fields)**

Run:
```bash
cd /Users/cfitt/Dev/arlo
for f in arlo/workflows/{art-rock-studio-as-instrument,indie-folk-confessional,electronic-groove-first,lo-fi-prolific-volume,post-punk-texture-dynamics}.md; do
  echo "--- $f ---"
  grep -E "^(name|type|taste_cluster|anchor_artists|applicable_when|duration_estimate|origin):" "$f"
done
```
Expected: each file shows all 6 frontmatter keys including `taste_cluster` and `anchor_artists`.

- [ ] **Step 3: "In Ableton" section + cross-link resolution**

Run:
```bash
cd /Users/cfitt/Dev/arlo
echo "=== In Ableton section present (expect 5) ==="
grep -rli "In Ableton" arlo/workflows/{art-rock-studio-as-instrument,indie-folk-confessional,electronic-groove-first,lo-fi-prolific-volume,post-punk-texture-dynamics}.md | wc -l
echo "=== Ableton cross-link targets resolve ==="
miss=0
for t in resampling-discipline beat-repeat-stutter-and-glitch eight-bars-first-discipline drum-rack-as-multizone-instrument live-as-looper-and-performance-instrument comping-in-live-11-plus; do
  find corpus/daw/ableton -name "$t.md" | grep -q . || { echo "MISSING TARGET: $t"; miss=1; }
done
[ $miss -eq 0 ] && echo "OK: sampled bridge targets exist"
```
Expected: count = 5; `OK: sampled bridge targets exist`.

- [ ] **Step 4: Citation + See-also discipline**

Run:
```bash
cd /Users/cfitt/Dev/arlo
echo "=== AI-tutorial citation check ==="
grep -rEil "chatgpt|claude\.ai|bard\.google|copilot\.microsoft|perplexity\.ai/articles" corpus/songwriting/cluster-workflows/ arlo/workflows/{art-rock-studio-as-instrument,indie-folk-confessional,electronic-groove-first,lo-fi-prolific-volume,post-punk-texture-dynamics}.md && echo "FAIL" || echo "OK: no AI-tutorial citations"
echo "=== See-also on corpus chunks ==="
grep -rLEi "see also" corpus/songwriting/cluster-workflows/ && echo "(missing above)" || echo "OK: all chunks have See-also"
```
Expected: `OK: no AI-tutorial citations` and `OK: all chunks have See-also`.

- [ ] **Step 5: Check off the SESSIONS tracking checklist**

In `CLUSTER-WORKFLOWS-SESSIONS.md`, change the CW1–CW5 checklist items from `- [ ]` to `- [x]`.

- [ ] **Step 6: Final commit**

```bash
cd /Users/cfitt/Dev/arlo
git add corpus/songwriting/cluster-workflows/ \
  arlo/workflows/art-rock-studio-as-instrument.md \
  arlo/workflows/indie-folk-confessional.md \
  arlo/workflows/electronic-groove-first.md \
  arlo/workflows/lo-fi-prolific-volume.md \
  arlo/workflows/post-punk-texture-dynamics.md \
  CLUSTER-WORKFLOWS-SESSIONS.md
git commit -m "Add 5 taste-driven cluster workflows (corpus chunks + templates)"
```

---

## Self-review notes

- **Spec coverage:** taste profile (Task 1), 3 scaffold files (Tasks 2–4), 5 dual-output clusters (Task 5), verification incl. new frontmatter fields + Ableton bridge + citations (Task 6). All spec deliverables mapped.
- **Anchor artists / Ableton targets / cross-links** are copied from the spec verbatim into the per-cluster kickoff blocks (Task 4), so the dispatched agents need no interpretation.
- **Failure handling** (Task 5 Step 3) encodes the S5 timeout/content-filter lesson: re-dispatch only missing files.
- **Verification** uses `jq`/shell/`find` checks instead of unit tests (content pipeline, not code).
