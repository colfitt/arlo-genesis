# Cluster Workflows — Prompts

Per-cluster master-template rows and the stream addendum for the **Taste-Driven Cluster
Workflows** stream. Use with `PROMPTS.md` (base master template) and
`CLUSTER-WORKFLOWS-RESEARCH-PLAN.md` (sourcing). Each cluster is **dual output**.

---

## Stream addendum (applies to every cluster file)

1. **Mission-fit:** every section must help a stuck musician finish a song.
2. **Source preference:** named-practitioner-first per the research plan's Tier 1/2. REFUSE
   AI-tutorial sites, fan blogs, listicles.
3. **Honesty about subjectivity:** name the school ("Godrich's method is X"), surface disagreement.
4. **Anti-hallucination is absolute:** omit any unverifiable quote/technique/attribution.
5. **Dual output:** a corpus chunk AND a workflow template (see spec below).
6. **New frontmatter fields** on the workflow template: `taste_cluster` and `anchor_artists`
   (in addition to name / origin / type / applicable_when / duration_estimate).
7. **Mandatory body section "In Ableton"** on the workflow template — concrete moves + explicit
   cross-links into `corpus/daw/ableton/` (bridge layer; do not re-teach mechanics).
8. **Default tags:** `cluster-workflow`, `taste-anchored`, `finishing-songs`, a per-cluster tag,
   plus anchor-artist tags.

## Dual-output spec

For each cluster, write TWO files:

1. **Corpus chunk** → `corpus/songwriting/cluster-workflows/<slug>.md`
   - 1500–2500 words, standard ARLO chunk shape: front-matter (Scope / Source / Canonical
     references / Tags), 8–15 H2 sections, Cited Retrieval Topics, Sources, See-also footer.
2. **Workflow template** → `arlo/workflows/<slug>.md`
   - 600–1000 words. Frontmatter: `name` / `origin` / `type` / `applicable_when` /
     `duration_estimate` / `taste_cluster` / `anchor_artists`.
   - Body sections: The premise / When ARLO should offer this / The steps / ARLO prompts for
     each step (verbatim) / **In Ableton** / When to abandon this workflow / Sources.
   - The corpus chunk is written first; the template is the operational derivation (prescriptive,
     ready to execute — not a rewrite of the chunk).

---

## Topic rows

### CW1 — Art-rock / studio-as-instrument
- **Title:** Studio-as-Instrument (Art-Rock Method)
- **Slug:** `art-rock-studio-as-instrument`
- **Thesis:** the arrangement/studio IS the compositional act — songs emerge from sound-design,
  re-contextualizing parts, and productive constraint, not from a finished song played into a mic.
- **Anchor artists:** Radiohead, Talking Heads, David Bowie
- **Type:** production-first
- **Ableton-bridge targets:** `corpus/daw/ableton/timeless/resampling-discipline.md`,
  `corpus/daw/ableton/timeless/beat-repeat-stutter-and-glitch.md`,
  `corpus/daw/ableton/devices/spectral-resonator-spectral-time-pitch-time-machine.md`,
  `corpus/daw/ableton/timeless/reamping-through-pedal-amp-cabinet.md`,
  `corpus/daw/ableton/timeless/audio-to-midi-extraction.md`,
  `corpus/daw/ableton/timeless/bounce-in-place-commit-discipline.md`
- **Corpus cross-links:** `arlo/workflows/eno-oblique-strategies.md`,
  `arlo/workflows/bowie-burroughs-cut-up.md`, `arlo/workflows/waits-break-the-demo.md`
- **Named sources:** Nigel Godrich/Radiohead interviews, Brian Eno on Talking Heads
  (*Remain in Light*), Tony Visconti on Bowie (Berlin era), Sodajerker, Song Exploder, Tape Notes
- **Tags:** `cluster-workflow`, `taste-anchored`, `finishing-songs`, `art-rock`, plus anchor tags

### CW2 — Indie-folk / confessional
- **Title:** Confessional / Performance-First (Indie-Folk Method)
- **Slug:** `indie-folk-confessional`
- **Thesis:** lyric-and-intimacy-first; the song exists before the production; capture the
  performance, build outward sparingly.
- **Anchor artists:** Bon Iver, Sufjan Stevens, Big Thief / Adrianne Lenker
- **Type:** lyrics-first
- **Ableton-bridge targets:** `corpus/daw/ableton/editing/comping-in-live-11-plus.md`,
  `corpus/daw/ableton/editing/warping-discipline.md`,
  `corpus/daw/ableton/timeless/live-as-looper-and-performance-instrument.md`,
  `corpus/daw/ableton/patterns/vocal-chains-in-live.md`
- **Corpus cross-links:** `arlo/workflows/sufjan-research-then-write.md`,
  `arlo/workflows/stems-first-production-first.md`, `arlo/workflows/nick-cave-letter-method.md`,
  `corpus/songwriting/lyric/image-stacking-technique.md`,
  `corpus/songwriting/form/through-composed-song-construction.md`
- **Named sources:** Justin Vernon/Bon Iver interviews, Sufjan in The Believer/Pitchfork,
  Adrianne Lenker/Big Thief in Sodajerker/Pitchfork
- **Tags:** `cluster-workflow`, `taste-anchored`, `finishing-songs`, `indie-folk`, plus anchor tags

### CW3 — Electronic / dance-leaning (groove-first)
- **Title:** Groove-First / Arrangement-Driven (Electronic Method)
- **Slug:** `electronic-groove-first`
- **Thesis:** groove-first, loop-and-arrangement-driven — build an 8-bar world, find the song
  in the arrangement, the rhythm section is the hook.
- **Anchor artists:** LCD Soundsystem, Daft Punk, The Postal Service
- **Type:** production-first
- **Ableton-bridge targets:** `corpus/daw/ableton/timeless/eight-bars-first-discipline.md`,
  `corpus/daw/ableton/workflows/clip-launching-and-follow-actions.md`,
  `corpus/daw/ableton/timeless/drum-rack-as-multizone-instrument.md`,
  `corpus/daw/ableton/patterns/sidechain-ducking-classic-vs-modulator.md`,
  `corpus/daw/ableton/timeless/groove-pool-and-extracted-grooves.md`,
  `corpus/daw/ableton/workflows/session-vs-arrangement-view.md`
- **Corpus cross-links:** `arlo/workflows/tom-cosm-8-bar-loop-cycle.md`,
  `arlo/workflows/beat-first-topline-workflow.md`, `arlo/workflows/stems-first-production-first.md`
- **Named sources:** James Murphy/LCD interviews, Daft Punk (Bangalter/de Homem-Christo)
  interviews, Jimmy Tamborello & Ben Gibbard on The Postal Service, Switched On Pop, Tape Notes
- **Tags:** `cluster-workflow`, `taste-anchored`, `finishing-songs`, `electronic`, plus anchor tags

### CW4 — Lo-fi / prolific (volume over polish)
- **Title:** Volume-Over-Polish (Lo-Fi / Prolific Method)
- **Slug:** `lo-fi-prolific-volume`
- **Thesis:** volume and speed over polish; the demo IS the song; finish-ugly; high output is
  the path to good songs.
- **Anchor artists:** Car Seat Headrest, Modest Mouse
- **Type:** production-first
- **Ableton-bridge targets:** `corpus/daw/ableton/timeless/bounce-in-place-commit-discipline.md`,
  `corpus/daw/ableton/timeless/eight-bars-first-discipline.md`,
  `corpus/daw/ableton/devices/saturator-vs-roar.md`,
  `corpus/daw/ableton/timeless/resampling-discipline.md`
- **Corpus cross-links:** `arlo/workflows/spoon-two-demos-a-week.md`,
  `arlo/workflows/waits-break-the-demo.md`, `corpus/songwriting/finishing/finish-ugly-school.md`,
  `corpus/songwriting/stalls/the-demo-trap.md`
- **Named sources:** Will Toledo/Car Seat Headrest interviews (Bandcamp-era prolificacy),
  Isaac Brock/Modest Mouse interviews, Sodajerker
- **Tags:** `cluster-workflow`, `taste-anchored`, `finishing-songs`, `lo-fi`, plus anchor tags

### CW5 — Post-punk / experimental (texture & dynamics)
- **Title:** Texture & Dynamics (Post-Punk / Experimental Method)
- **Slug:** `post-punk-texture-dynamics`
- **Thesis:** texture, repetition, dynamics and build over conventional verse-chorus; tension
  through restraint and accumulation.
- **Anchor artists:** Black Country New Road, Swans, Joy Division
- **Type:** exploring
- **Ableton-bridge targets:** `corpus/daw/ableton/timeless/live-as-looper-and-performance-instrument.md`,
  `corpus/daw/ableton/timeless/beat-repeat-stutter-and-glitch.md`,
  `corpus/daw/ableton/timeless/send-return-as-parallel-bus.md`,
  `corpus/daw/ableton/timeless/velocity-randomization-and-humanization.md`
- **Corpus cross-links:** `corpus/songwriting/form/through-composed-song-construction.md`,
  `arlo/workflows/eno-oblique-strategies.md`,
  `corpus/songwriting/melodic-harmonic/pedal-tones-drones-anchoring.md`
- **Named sources:** Michael Gira/Swans interviews, Black Country New Road interviews,
  Joy Division (Martin Hannett production) documented history, Sodajerker
- **Tags:** `cluster-workflow`, `taste-anchored`, `finishing-songs`, `post-punk`, plus anchor tags
