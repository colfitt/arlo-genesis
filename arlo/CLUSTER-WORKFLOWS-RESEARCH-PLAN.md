# Cluster Workflows — Research Plan

Sourcing philosophy and cross-stream boundaries for the **Taste-Driven Cluster Workflows**
stream. The cluster workflows are a *bridge layer*: they translate the songwriting method of
a school the user actually listens to into concrete Ableton moves, cross-linking the existing
`corpus/daw/ableton/` files rather than re-teaching mechanics.

Design source of truth: `docs/superpowers/specs/2026-05-28-cluster-workflows-design.md`.
Taste evidence: `arlo/taste-profile/spotify-taste-profile.md`.

---

## 1. Mission fit

Every workflow must help a stuck musician **finish a song**. Cut anything that doesn't.
A cluster workflow is good only if a writer in that taste-world can leave it with a concrete
move they can try in the next session.

## 2. Sourcing tiers (named-practitioner-first)

**Tier 1 — primary, preferred:**
- Long-form practitioner interviews & podcasts: **Sodajerker, Tape Notes, Song Exploder,
  Switched On Pop, Rick Beato, Pitchfork / The Believer interviews.**
- Producer testimony tied to the anchor artists:
  - **Nigel Godrich** → Radiohead studio process
  - **Brian Eno**'s published writing/interviews → Talking Heads (*Remain in Light* loops/layering)
  - **Tony Visconti** → Bowie (Berlin-era process)
  - **Thomas Bangalter / Guy-Manuel de Homem-Christo** interviews → Daft Punk
  - **James Murphy** interviews → LCD Soundsystem
  - **Jimmy Tamborello & Ben Gibbard** → The Postal Service
  - **Will Toledo** interviews → Car Seat Headrest (Bandcamp-era prolificacy)
  - **Isaac Brock** interviews → Modest Mouse
  - **Michael Gira** interviews → Swans
  - **Black Country, New Road** interviews → compositional builds
  - **Martin Hannett** production history → Joy Division

**Tier 2 — acceptable supporting:** reputable long-form music journalism (Pitchfork, The Quietus,
NPR Music, Rolling Stone feature interviews, Bandcamp Daily).

**REFUSE:** AI-tutorial sites, fan blogs, generic listicles, gear-marketing copy.

## 3. Anti-hallucination is absolute

If a quote, technique, or attribution can't be verified against a Tier 1/2 source, **OMIT it.**
Fabricated process claims about real, living artists poison ARLO's retrieval worst of all —
and these are the user's favorite artists, so errors are maximally costly. When unsure, describe
the *generalizable* move and attribute it honestly ("a common art-rock move" rather than a false
specific claim).

## 4. School-naming honesty

Name the school. "Godrich's method is to commit sounds early and resist the undo" beats "the
right way is to commit early." When schools disagree (e.g. finish-ugly vs. polish-until-shipping),
surface the disagreement.

## 5. Bridge-layer rule

Do **NOT** re-teach Ableton mechanics — the `corpus/daw/ableton/` corpus owns those. Each cluster
workflow has an **"In Ableton"** section that (a) gives concrete moves translating the school's
process and (b) cross-links the specific existing files listed per cluster below. The new content
is the *songwriting decision* + the *artist→Ableton mapping*.

## 6. Cross-stream boundaries

Reference, don't rebuild, the already-built individual workflows:
`bowie-burroughs-cut-up`, `sufjan-research-then-write`, `stems-first-production-first`,
`tom-cosm-8-bar-loop-cycle`, `beat-first-topline-workflow`, `spoon-two-demos-a-week`,
`waits-break-the-demo`, `eno-oblique-strategies`, `nick-cave-letter-method`. Link them via
See-also; do not duplicate their content.

## 7. The 5 clusters

| # | Slug | Thesis | Anchors | Type |
|---|------|--------|---------|------|
| CW1 | `art-rock-studio-as-instrument` | the arrangement/studio IS the compositional act — songs emerge from sound-design, re-contextualizing parts, and productive constraint | Radiohead, Talking Heads, David Bowie | production-first |
| CW2 | `indie-folk-confessional` | lyric-and-intimacy-first; the song exists before the production; capture the performance, build outward sparingly | Bon Iver, Sufjan Stevens, Big Thief / Adrianne Lenker | lyrics-first |
| CW3 | `electronic-groove-first` | groove-first, loop-and-arrangement-driven — build an 8-bar world, find the song in the arrangement, the rhythm section is the hook | LCD Soundsystem, Daft Punk, The Postal Service | production-first |
| CW4 | `lo-fi-prolific-volume` | volume and speed over polish; the demo IS the song; finish-ugly; high output is the path to good songs | Car Seat Headrest, Modest Mouse | production-first |
| CW5 | `post-punk-texture-dynamics` | texture, repetition, dynamics and build over conventional verse-chorus; tension through restraint and accumulation | Black Country New Road, Swans, Joy Division | exploring |

### Per-cluster Ableton-bridge targets and corpus cross-links

- **CW1 art-rock-studio-as-instrument**
  - Ableton bridge: `corpus/daw/ableton/timeless/resampling-discipline.md`, `corpus/daw/ableton/timeless/beat-repeat-stutter-and-glitch.md`, `corpus/daw/ableton/devices/spectral-resonator-spectral-time-pitch-time-machine.md`, `corpus/daw/ableton/timeless/reamping-through-pedal-amp-cabinet.md`, `corpus/daw/ableton/timeless/audio-to-midi-extraction.md`, `corpus/daw/ableton/timeless/bounce-in-place-commit-discipline.md`
  - Cross-links: `arlo/workflows/eno-oblique-strategies.md`, `arlo/workflows/bowie-burroughs-cut-up.md`, `arlo/workflows/waits-break-the-demo.md`
- **CW2 indie-folk-confessional**
  - Ableton bridge: `corpus/daw/ableton/editing/comping-in-live-11-plus.md`, `corpus/daw/ableton/editing/warping-discipline.md`, `corpus/daw/ableton/timeless/live-as-looper-and-performance-instrument.md`, `corpus/daw/ableton/patterns/vocal-chains-in-live.md`
  - Cross-links: `arlo/workflows/sufjan-research-then-write.md`, `arlo/workflows/stems-first-production-first.md`, `arlo/workflows/nick-cave-letter-method.md`, `corpus/songwriting/lyric/image-stacking-technique.md`, `corpus/songwriting/form/through-composed-song-construction.md`
- **CW3 electronic-groove-first**
  - Ableton bridge: `corpus/daw/ableton/timeless/eight-bars-first-discipline.md`, `corpus/daw/ableton/workflows/clip-launching-and-follow-actions.md`, `corpus/daw/ableton/timeless/drum-rack-as-multizone-instrument.md`, `corpus/daw/ableton/patterns/sidechain-ducking-classic-vs-modulator.md`, `corpus/daw/ableton/timeless/groove-pool-and-extracted-grooves.md`, `corpus/daw/ableton/workflows/session-vs-arrangement-view.md`
  - Cross-links: `arlo/workflows/tom-cosm-8-bar-loop-cycle.md`, `arlo/workflows/beat-first-topline-workflow.md`, `arlo/workflows/stems-first-production-first.md`
- **CW4 lo-fi-prolific-volume**
  - Ableton bridge: `corpus/daw/ableton/timeless/bounce-in-place-commit-discipline.md`, `corpus/daw/ableton/timeless/eight-bars-first-discipline.md`, `corpus/daw/ableton/devices/saturator-vs-roar.md`, `corpus/daw/ableton/timeless/resampling-discipline.md`
  - Cross-links: `arlo/workflows/spoon-two-demos-a-week.md`, `arlo/workflows/waits-break-the-demo.md`, `corpus/songwriting/finishing/finish-ugly-school.md`, `corpus/songwriting/stalls/the-demo-trap.md`
- **CW5 post-punk-texture-dynamics**
  - Ableton bridge: `corpus/daw/ableton/timeless/live-as-looper-and-performance-instrument.md`, `corpus/daw/ableton/timeless/beat-repeat-stutter-and-glitch.md`, `corpus/daw/ableton/timeless/send-return-as-parallel-bus.md`, `corpus/daw/ableton/timeless/velocity-randomization-and-humanization.md`
  - Cross-links: `corpus/songwriting/form/through-composed-song-construction.md`, `arlo/workflows/eno-oblique-strategies.md`, `corpus/songwriting/melodic-harmonic/pedal-tones-drones-anchoring.md`

## 8. Default tags

`cluster-workflow`, `taste-anchored`, `finishing-songs`, plus a per-cluster tag
(`art-rock` / `indie-folk` / `electronic` / `lo-fi` / `post-punk`) and anchor-artist tags.
