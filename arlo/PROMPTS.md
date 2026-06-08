# ARLO Seed-Document Prompts

This file contains a reusable prompt template plus 38 topic-specific variable sets for generating seed knowledge-base entries via deep research (Claude + web search).

**Output:** 38 markdown files dropped into `corpus/{scope}/{filename}.md`, each ~1500–2500 words, structured as 8–15 chunk-shaped sections.

**Provenance note:** These files will be tagged as `deep-research synthesis (2026-05)` — lower citation authority than direct-from-canonical-book chunks. The intent is to seed the corpus while waiting on book acquisition, then supplement with verified book chunks later.

---

## How to use this file

1. Pick a topic row from the table below.
2. Copy the **Master Template** block.
3. Substitute the 7 placeholders (`{{TOPIC}}`, `{{TITLE}}`, `{{SCOPE}}`, `{{FOLDER}}`, `{{FILENAME}}`, `{{SUBTOPICS}}`, `{{CANONICAL_REFS}}`, `{{SUGGESTED_TAGS}}`) with the values from that row.
4. Paste into a fresh Claude chat (Sonnet or Opus, web search enabled).
5. When the response comes back, save the markdown to the target path.
6. (Optional) Spot-check 2–3 specific claims for hallucination before adding to retrieval.

You can fire prompts in batches — the worked-example after the template shows what a fully substituted prompt looks like.

---

## Master Template

```
You are writing a seed knowledge-base entry for ARLO, a local-first AI songwriting/production assistant. The entry will be parsed into ~8–15 retrievable chunks and cited back to users during conversation.

TOPIC: {{TOPIC}}
SCOPE: {{SCOPE}}
TARGET PATH: corpus/{{FOLDER}}/{{FILENAME}}.md

## Your task

Produce a single markdown file titled "{{TITLE}}" focused on the following subtopics:

{{SUBTOPICS}}

Where relevant, ground the content in what is publicly discussed about these canonical sources (you do NOT need to have read them — reference what's known from reviews, interviews, excerpts, and citations available online):

{{CANONICAL_REFS}}

## Content requirements

- **Concrete over abstract.** Specific knob settings, specific exercises, specific recipes, specific numerical defaults, specific song examples — not philosophy or motivation.
- **Use reputable sources.** Sound on Sound, iZotope guides, manufacturer documentation, university music-theory resources (Berklee Online, Open Music Theory), songwriter/producer interviews from established outlets, technical blogs by working engineers. Avoid Reddit and forum posts unless quoting verifiable claims.
- **Cite inline.** Use markdown links — `[Source Title](URL)` — within sentences where claims originate. Do not save citations only for a bibliography.
- **Anti-hallucination guard.** If you cannot verify a specific number, setting, technique, or attribution with web research, OMIT it. Do not guess. Made-up specifics will poison ARLO's retrieval. When in doubt, prefer a qualitative claim ("compressors with fast attack capture transients more aggressively") over a fabricated specific ("set attack to 3.7ms for vocals").
- **Length:** 1500–2500 words.
- **Structure:** 8–15 H2/H3 sections, each one a self-contained idea (these will become individual retrieval chunks). Each section 100–250 words.
- **Audience:** intermediate musicians/producers. Assume basic vocabulary; don't re-explain what dB or LUFS mean.

## Required output format

Begin with this exact front-matter block (fill in your tag choices from the suggested set):

```
# {{TITLE}}

**Scope:** {{SCOPE}}
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Canonical references:** {{CANONICAL_REFS}}
**Tags:** {{SUGGESTED_TAGS}}

---
```

Then the 8–15 H2 sections.

End with these two required sections:

```
## Cited Retrieval Topics

List 5–10 specific user questions this document should be retrieved for. Phrase them as a musician would actually type them — lowercase, conversational, no question marks. Examples:
- "what's a good attack time for vocal compression"
- "how do i make a kick and bass not fight each other"

## Sources

Clean bibliography of every URL linked inline above, formatted as markdown links.
```

## What this is NOT

- Not a survey of every angle — go deep on the actionable specifics
- Not a beginner tutorial that re-explains fundamentals every time
- Not opinion or philosophy — concrete craft only
- Not exhaustive — 8 strong chunks beats 20 thin ones

Begin research and produce the markdown now.
```

---

## Worked example — what a fully-substituted prompt looks like

Taking row **#6 (eq-fundamentals)** below and substituting into the template:

> TOPIC: **EQ fundamentals for mixing**
> SCOPE: **mixing**
> TARGET PATH: **corpus/mixing/eq-fundamentals.md**
>
> ## Your task
> Produce a single markdown file titled **"EQ Fundamentals"** focused on the following subtopics:
> - the four EQ filter types (low-cut, high-cut, shelf, bell) and when each is appropriate
> - subtractive vs. additive EQ workflow philosophy
> - frequency bands by source (kick, snare, vocal, bass, guitar) with typical problem-and-fix frequencies
> - mid/side EQ basics and when to reach for it
> - common EQ mistakes (over-boosting, narrow-Q cuts, mismatched HPF settings across tracks)
>
> Where relevant, ground the content in what is publicly discussed about these canonical sources:
> - Mike Senior, *Mixing Secrets for the Small Studio*
> - Roey Izhaki, *Mixing Audio*
> - iZotope *Mixing Guide*
> - Bobby Owsinski, *The Mixing Engineer's Handbook*
>
> [...remaining template body...]
>
> Tags: `mixing`, `EQ`, `subtractive`, `low-end`, `principle`, `recipe`

---

## The 38 Prompts

Format per row: filename, title, scope folder, subtopics, canonical references to ground in, suggested tags.

### Recording (5)

---

#### 1. `mic-placement-by-source`

- **Title:** Mic Placement by Source
- **Scope:** recording
- **Folder:** recording
- **Subtopics:**
  - electric guitar amp miking (close + distant, single vs. dual)
  - acoustic guitar (12th fret, sound hole, body)
  - vocal mic distance and proximity effect
  - kick drum (inside, outside, sub mic)
  - snare top/bottom phase relationship
  - overheads (XY vs. spaced pair vs. Glyn Johns)
- **Canonical references:** Bobby Owsinski, *Recording Engineer's Handbook*; Mike Senior, *Recording Secrets for the Small Studio*; *Modern Recording Techniques* (Huber/Runstein)
- **Tags:** `recording`, `mic-placement`, `tracking`, `drums`, `vocal`, `guitar`, `recipe`

---

#### 2. `signal-flow-and-gain-staging`

- **Title:** Signal Flow and Gain Staging
- **Scope:** recording
- **Folder:** recording
- **Subtopics:**
  - signal-chain block diagram (source → mic → preamp → AD → DAW → DA → monitor)
  - dBFS vs. dBu vs. dBV — when each matters
  - tracking levels for 24-bit: why -18 dBFS RMS is the safe target
  - gain-staging plugin chains (avoiding clipping between plugins)
  - headroom budgeting across a mix
- **Canonical references:** Yamaha *Sound Reinforcement Handbook*; *Modern Recording Techniques*; Mike Senior, *Recording Secrets*
- **Tags:** `signal-flow`, `gain-staging`, `headroom`, `recording`, `mixing`, `principle`

---

#### 3. `room-treatment-budget`

- **Title:** Budget Room Treatment for Small Studios
- **Scope:** recording
- **Folder:** recording
- **Subtopics:**
  - the three problems (early reflections, modal buildup, flutter echo)
  - mirror-point treatment with rockwool/blankets
  - bass-trapping with corner absorbers (DIY 703/rockwool)
  - cloud panel above mix position
  - when (and when not) to add diffusion
  - measuring with Room EQ Wizard
- **Canonical references:** Mike Senior, *Recording Secrets*; F. Alton Everest, *Master Handbook of Acoustics*; *Modern Recording Techniques*
- **Tags:** `room-treatment`, `acoustics`, `monitoring`, `home-studio`, `recipe`

---

#### 4. `monitoring-and-headphones`

- **Title:** Monitoring and Headphones for Mix Translation
- **Scope:** recording
- **Folder:** recording
- **Subtopics:**
  - near-field monitor placement (equilateral triangle, tweeter at ear height)
  - reference-level calibration (~79 dB SPL @ -18 dBFS pink noise)
  - why NS10s persist as a midrange reference
  - headphone mixing limitations (no crossfeed → wide-pan inflation)
  - the consumer-system rotation (car, phone, AirPods) for translation checks
- **Canonical references:** Mike Senior, *Mixing Secrets for the Small Studio*; Bobby Owsinski, *The Mixing Engineer's Handbook*; Bob Katz, *Mastering Audio*
- **Tags:** `monitoring`, `translation`, `home-studio`, `mixing`, `principle`

---

#### 5. `tracking-vocals-in-the-small-studio`

- **Title:** Tracking Vocals in the Small Studio
- **Scope:** recording
- **Folder:** recording
- **Subtopics:**
  - mic choice for the voice in question (LDC, dynamic, ribbon)
  - distance, pop filter, and proximity effect management
  - foldback/headphone-mix design for performance comfort
  - dealing with untreated rooms (blankets, closet, mattress fortress)
  - punch-and-comp workflow vs. full take
  - tracking the de-esser at input vs. mixdown
- **Canonical references:** Mike Senior, *Recording Secrets*; Bobby Owsinski, *Recording Engineer's Handbook*; Howard Massey, *Behind the Glass*
- **Tags:** `recording`, `tracking`, `vocal`, `mic-placement`, `comping`, `recipe`

---

### Mixing (6)

---

#### 6. `eq-fundamentals`

- **Title:** EQ Fundamentals
- **Scope:** mixing
- **Folder:** mixing
- **Subtopics:**
  - four filter types (low-cut, high-cut, shelf, bell) and use cases
  - subtractive vs. additive philosophy
  - typical problem frequencies per source (mud at 200–400 Hz, harshness at 2–4 kHz, etc.)
  - mid/side EQ basics
  - common mistakes (over-boosting, narrow cuts, inconsistent HPF)
- **Canonical references:** Mike Senior, *Mixing Secrets for the Small Studio*; Roey Izhaki, *Mixing Audio*; iZotope *Mixing Guide*; Bobby Owsinski, *Mixing Engineer's Handbook*
- **Tags:** `mixing`, `EQ`, `subtractive`, `low-end`, `principle`, `recipe`

---

#### 7. `compression-fundamentals`

- **Title:** Compression Fundamentals
- **Scope:** mixing
- **Folder:** mixing
- **Subtopics:**
  - the five parameters (threshold, ratio, attack, release, knee) explained as moves
  - VCA vs. opto vs. FET vs. variable-mu character
  - typical settings per source (vocal, kick, snare, bass, mix bus)
  - parallel compression workflow
  - serial compression (gentle squash then peak control)
  - over-compression warning signs (pumping, lifelessness, lost transients)
- **Canonical references:** Mike Senior, *Mixing Secrets*; Roey Izhaki, *Mixing Audio*; iZotope *Mixing Guide*
- **Tags:** `mixing`, `compression`, `transient`, `parallel-processing`, `vocal-mixing`, `recipe`

---

#### 8. `reverb-and-delay-architecture`

- **Title:** Reverb and Delay Architecture
- **Scope:** mixing
- **Folder:** mixing
- **Subtopics:**
  - reverb types (room, plate, hall, chamber, spring) and where each fits
  - send-and-return architecture (one short room, one long plate, one slap)
  - pre-delay as separation tool (12–60 ms typical)
  - reverb EQ (HPF the return, sometimes shelve highs)
  - delay throws (1/4, dotted-8th, tape-style) and tempo synchronization
  - using delay instead of reverb for "dry but big"
- **Canonical references:** Mike Senior, *Mixing Secrets*; iZotope *Mixing Guide*; Bobby Owsinski, *Mixing Engineer's Handbook*
- **Tags:** `mixing`, `reverb`, `delay`, `depth`, `principle`, `recipe`

---

#### 9. `low-end-management`

- **Title:** Low-End Management
- **Scope:** mixing
- **Folder:** mixing
- **Subtopics:**
  - kick-and-bass frequency carving (one owns 60 Hz, other owns 80–100 Hz)
  - sidechain compression from kick to bass
  - mono-ing the low end below ~120 Hz
  - subs in headphones vs. monitors vs. consumer playback
  - the 30 Hz HPF question (when to filter sub-bass)
  - phase coherence between kick mics
- **Canonical references:** Mike Senior, *Mixing Secrets* (low-end chapter); SOS Inside Track articles; Bobby Owsinski, *Mixing Engineer's Handbook*
- **Tags:** `mixing`, `low-end`, `kick`, `bass`, `sidechain`, `mono`, `principle`

---

#### 10. `mix-translation-and-reference-tracks`

- **Title:** Mix Translation and Reference Tracks
- **Scope:** mixing
- **Folder:** mixing
- **Subtopics:**
  - the reference-track protocol (match loudness via LUFS first)
  - which references to pick (same genre, similar instrumentation, era-relevant)
  - the systems-rotation check (NS10, headphones, phone speaker, car)
  - common translation failures (too-bright on consumer, lost bass on phone)
  - tonal-balance plugins as a reference tool
  - the A/B technique without level-matching is useless
- **Canonical references:** Mike Senior, *Mixing Secrets* (heavily — this is his core thesis); Bob Katz, *Mastering Audio*; iZotope *Tonal Balance Control* docs
- **Tags:** `mixing`, `translation`, `reference-track`, `mastering`, `methodology`

---

#### 11. `vocal-mixing`

- **Title:** Vocal Mixing
- **Scope:** mixing
- **Folder:** mixing
- **Subtopics:**
  - vocal-chain order (HPF → de-ess → compression → EQ → saturation → automation)
  - the two-comp trick (slow then fast)
  - de-essing as static EQ vs. dynamic vs. clip-gain
  - vocal rider/automation vs. heavy compression
  - vocal-and-music balance vs. "vocal up" issue
  - lead vs. doubles vs. backing-vocal processing differences
  - reverb send count and pre-delay matching for vocals
- **Canonical references:** Mike Senior, *Mixing Secrets*; SOS Inside Track (Billie Eilish chain in corpus); Bobby Owsinski, *Mixing Engineer's Handbook*
- **Tags:** `mixing`, `vocal-mixing`, `de-esser`, `compression`, `automation`, `recipe`

---

### Mastering (3)

---

#### 12. `mastering-chain-and-process`

- **Title:** The Mastering Chain and Process
- **Scope:** mastering
- **Folder:** mastering
- **Subtopics:**
  - the canonical chain (EQ → multiband → glue compression → saturation → limiter)
  - when to deviate from that order
  - reference-track loudness matching before any moves
  - tonal balance check (frequency tilt, mono check)
  - one-pass vs. two-pass mastering
  - mastering for album consistency vs. single
- **Canonical references:** Bob Katz, *Mastering Audio*; iZotope *Mastering with Ozone* / Ozone Help (in corpus); Sound on Sound mastering features
- **Tags:** `mastering`, `mastering-chain`, `principle`, `methodology`

---

#### 13. `lufs-streaming-and-true-peak`

- **Title:** LUFS, Streaming Targets, and True Peak
- **Scope:** mastering
- **Folder:** mastering
- **Subtopics:**
  - integrated vs. short-term vs. momentary LUFS
  - per-platform integrated LUFS targets (Spotify -14, Apple -16, YouTube -14, Tidal -14, Amazon -14)
  - true-peak limit conventions (-1 dBTP universal, -2 dBTP for Spotify safety)
  - why "louder than the platform" hurts you (turn-down, distortion)
  - measuring with free meters (Youlean, Loudness Meter)
  - LRA (loudness range) and what's typical for genres
- **Canonical references:** Spotify Loudness Normalization docs (in corpus); Apple Mastered for iTunes; Bob Katz, *Mastering Audio* (older but principles intact); iZotope streaming-mastering guide
- **Tags:** `mastering`, `LUFS`, `streaming`, `true-peak`, `reference-fact`, `delivery`

---

#### 14. `limiting-dither-and-delivery`

- **Title:** Limiting, Dither, and Delivery
- **Scope:** mastering
- **Folder:** mastering
- **Subtopics:**
  - limiter parameters (ceiling, threshold, release, lookahead)
  - choosing a limiter character (transparent vs. colored)
  - dither when reducing bit depth (24 → 16 for CD)
  - file format conventions (WAV vs. AIFF vs. FLAC for delivery)
  - sample-rate decisions and SRC quality
  - DDP for album mastering vs. individual file submission
- **Canonical references:** Bob Katz, *Mastering Audio*; iZotope *Mastering with Ozone* guide / Ozone Help (in corpus)
- **Tags:** `mastering`, `limiting`, `dither`, `delivery`, `file-format`, `recipe`

---

### Structure (3)

---

#### 15. `pop-song-forms`

- **Title:** Pop Song Forms
- **Scope:** structure
- **Folder:** structure
- **Subtopics:**
  - the dominant pop forms (verse-chorus, verse-chorus-bridge, AABA)
  - section-length conventions (8-bar verse, 8-bar chorus, etc.) with exceptions
  - pre-chorus as a 20th-21st-century innovation
  - intro-outro length conventions in the streaming era
  - bridge as harmonic-or-lyrical pivot
  - hybrid forms (4-on-the-floor electronic build structures)
- **Canonical references:** Pat Pattison, *Songwriting: Essential Guide to Lyric Form and Structure*; Jack Perricone, *Great Songwriting Techniques*; Open Music Theory v2 Unit VII (in corpus index)
- **Tags:** `structure`, `arrangement`, `pop`, `verse`, `chorus`, `bridge`, `principle`

---

#### 16. `section-function-verse-prechorus-chorus-bridge`

- **Title:** Section Function: Verse, Pre-Chorus, Chorus, Bridge
- **Scope:** structure
- **Folder:** structure
- **Subtopics:**
  - what each section does emotionally and harmonically
  - the "stable vs. unstable" lens (verse stable, pre-chorus unstable, chorus stable, bridge unstable)
  - melodic register conventions per section (verse low, chorus high)
  - lyric-density conventions per section
  - the pre-chorus as harmonic-and-melodic launcher
  - bridges that contrast vs. bridges that summarize
- **Canonical references:** Pat Pattison, *Lyric Form and Structure*; Jack Perricone, *Great Songwriting Techniques*; Dominic Pedler, *Songwriting Secrets of the Beatles*
- **Tags:** `structure`, `arrangement`, `verse`, `chorus`, `pre-chorus`, `bridge`, `principle`

---

#### 17. `arrangement-arcs-and-transitions`

- **Title:** Arrangement Arcs and Transitions
- **Scope:** structure
- **Folder:** structure
- **Subtopics:**
  - dynamic arrangement across a song (sparse intro, dense chorus, bare bridge)
  - the "what enters in chorus 2" question (counter-melody, harmony stack, percussion layer)
  - transition tools (drum fills, risers, drops, silence, reverb throws)
  - the energy-budget concept (every section relative to its neighbors)
  - genre-specific arc conventions (pop, dance build/drop, indie folk dynamics)
- **Canonical references:** Rikky Rooksby, *Arranging Songs*; Dennis DeSantis, *Making Music* (in seed); Attack Magazine *Secrets of Dance Music Production*
- **Tags:** `arrangement`, `dynamics`, `transitions`, `structure`, `methodology`

---

### Harmony (4)

---

#### 18. `pop-chord-progressions-by-function`

- **Title:** Pop Chord Progressions by Function
- **Scope:** harmony
- **Folder:** harmony
- **Subtopics:**
  - the function model (tonic → predominant → dominant → tonic)
  - the most-used pop progressions (I-V-vi-IV, vi-IV-I-V, I-vi-IV-V, etc.) with frequency data
  - the four-chord axis and why it dominates pop
  - inversions and bass-line shape
  - cadence types (authentic, plagal, deceptive, half)
  - common substitutions in pop
- **Canonical references:** Hooktheory I/II + TheoryTab database; Open Music Theory v2 Unit VII; Dominic Pedler, *Songwriting Secrets of the Beatles*; Rick Beato, *The Beato Book*
- **Tags:** `harmony`, `chord-progression`, `pop`, `function`, `cadence`, `reference-fact`

---

#### 19. `modal-interchange-and-borrowed-chords`

- **Title:** Modal Interchange and Borrowed Chords
- **Scope:** harmony
- **Folder:** harmony
- **Subtopics:**
  - what modal interchange means (borrowing from parallel minor/major)
  - the most-common borrowings (♭VII, ♭VI, iv, ♭III) in pop
  - emotional effect of each (♭VII = uplifting-but-melancholy, etc.)
  - examples from specific songs
  - distinguishing modal interchange from modulation
  - chord-loop modal interchange in indie/alt-pop
- **Canonical references:** Hooktheory II; Open Music Theory v2 Chromaticism unit; Dominic Pedler, *Songwriting Secrets of the Beatles*; *The Beato Book*
- **Tags:** `harmony`, `modal-interchange`, `chord-progression`, `chromaticism`, `principle`, `example`

---

#### 20. `secondary-dominants-and-applied-chords`

- **Title:** Secondary Dominants and Applied Chords
- **Scope:** harmony
- **Folder:** harmony
- **Subtopics:**
  - the V-of-X concept
  - common secondary dominants in pop (V/V, V/vi, V/IV)
  - resolving and unexpected resolutions
  - applied diminished chords (vii°/X)
  - extended applied chains (V/V/V backcycling)
  - identifying them in songs you know
- **Canonical references:** Hooktheory II; Open Music Theory v2 Unit IV; *The Beato Book*; *Songwriting Secrets of the Beatles*
- **Tags:** `harmony`, `secondary-dominant`, `tonicization`, `chord-progression`, `principle`

---

#### 21. `voice-leading-for-songwriters`

- **Title:** Voice Leading for Songwriters (Not Choir Class)
- **Scope:** harmony
- **Folder:** harmony
- **Subtopics:**
  - common-tone connection (hold the shared note, move the others by step)
  - contrary motion between bass and top voice
  - avoiding parallel fifths/octaves between outer voices (the practical reason)
  - smoothing inversions to minimize voice jumps
  - voice leading in pad/synth arrangements (top-line stays smooth)
  - guitar-friendly voicings that imply voice leading
- **Canonical references:** Open Music Theory v2 Unit IV; Walter Piston, *Harmony*; *The Beato Book*
- **Tags:** `harmony`, `voice-leading`, `arrangement`, `principle`

---

### Melody (2)

---

#### 22. `melodic-contour-and-motif-development`

- **Title:** Melodic Contour and Motif Development
- **Scope:** melody
- **Folder:** melody
- **Subtopics:**
  - contour shapes (arch, descending, ascending, terraced)
  - chorus contour vs. verse contour conventions
  - motif and its transformations (inversion, augmentation, sequence)
  - the "answering phrase" structure
  - tension via leap, release via step
  - interval choices that signal genre (perfect fourth = anthem, tritone = unsettled)
- **Canonical references:** Jack Perricone, *Melody in Songwriting*; Pat Pattison; Open Music Theory v2
- **Tags:** `melody`, `contour`, `motif`, `topline`, `principle`

---

#### 23. `hook-construction`

- **Title:** Hook Construction
- **Scope:** melody
- **Folder:** melody
- **Subtopics:**
  - hook types (melodic, lyrical, rhythmic, production)
  - the four-bar hook archetype
  - why titles work as hooks
  - repetition with small variation (the second hook iteration trick)
  - the post-chorus hook in modern pop
  - examples of hooks that hit on contour vs. rhythm vs. lyric
- **Canonical references:** Jack Perricone, *Great Songwriting Techniques*; Dominic Pedler, *Songwriting Secrets of the Beatles*; Hooktheory database
- **Tags:** `melody`, `hook`, `topline`, `pop`, `chorus`, `example`

---

### Lyrics (4)

---

#### 24. `object-writing-and-sensory-imagery`

- **Title:** Object Writing and Sensory Imagery
- **Scope:** lyrics
- **Folder:** lyrics
- **Subtopics:**
  - the object-writing exercise (10 minutes, all senses, no editing)
  - the seven senses (sight, sound, taste, touch, smell, organic, kinesthetic)
  - using outputs in finished lyrics (specificity > generality)
  - "show don't tell" via concrete nouns
  - avoiding cliché through sense-bound detail
  - daily practice cadence
- **Canonical references:** Pat Pattison, *Writing Better Lyrics* (in seed); Pat Pattison, *Songwriting Without Boundaries*; Sound on Sound interview (in corpus)
- **Tags:** `lyrics`, `imagery`, `object-writing`, `methodology`, `recipe`

---

#### 25. `rhyme-types-and-cadence-function`

- **Title:** Rhyme Types and Cadence Function
- **Scope:** lyrics
- **Folder:** lyrics
- **Subtopics:**
  - the rhyme taxonomy (perfect, family, additive, subtractive, assonance, consonance)
  - cadential strength per rhyme type (perfect = closure, family = motion)
  - matching rhyme scheme to section function (chorus = stable, bridge = unstable)
  - internal rhyme and how it accelerates lines
  - mosaic and multisyllabic rhyme in hip-hop
- **Canonical references:** Pat Pattison, *The Essential Guide to Rhyming*; Pat Pattison, *Writing Better Lyrics*
- **Tags:** `lyrics`, `rhyme`, `prosody`, `cadence`, `principle`

---

#### 26. `point-of-view-tense-and-narrator`

- **Title:** Point of View, Tense, and Narrator
- **Scope:** lyrics
- **Folder:** lyrics
- **Subtopics:**
  - the four POV options (third-person, second-person, first-person, direct address)
  - tense decisions (past = reflective, present = immediate, future = anticipatory)
  - when to switch POV mid-song (and when not to)
  - narrator reliability and distance
  - direct address as default in pop and its risks
- **Canonical references:** Pat Pattison, *Writing Better Lyrics* (in seed); Sheila Davis, *The Craft of Lyric Writing*; Sound on Sound interview (in corpus)
- **Tags:** `lyrics`, `POV`, `tense`, `narrative`, `principle`

---

#### 27. `prosody-and-form-content-alignment`

- **Title:** Prosody: Form and Content Alignment
- **Scope:** lyrics
- **Folder:** lyrics
- **Subtopics:**
  - prosody as the central lyric concept
  - matching line length to emotional content
  - asymmetric structures for unstable feelings
  - melodic stress vs. linguistic stress and how to align
  - section-function reinforcement via prosodic tools
  - prosodic violations as intentional craft (when to break the rule)
- **Canonical references:** Pat Pattison, *Writing Better Lyrics*; Pat Pattison, *Lyric Form and Structure* (in seed)
- **Tags:** `lyrics`, `prosody`, `form`, `principle`, `methodology`

---

### Rhythm (3)

---

#### 28. `groove-construction-and-pocket`

- **Title:** Groove Construction and Pocket
- **Scope:** rhythm
- **Folder:** rhythm
- **Subtopics:**
  - the kick/snare/hihat backbone and where the genre lives
  - ghost notes and their placement
  - micro-timing (pushing/pulling specific elements)
  - swing percentages by genre (hip-hop ~58%, shuffle ~66%)
  - groove templates and quantize-to-groove workflows in DAWs
  - the "humanize" knob — what it does and when it helps
- **Canonical references:** Dennis DeSantis, *Making Music* (in seed); Attack Magazine *Secrets of Dance Music Production*; Ableton Live Reference Manual
- **Tags:** `rhythm`, `groove`, `pocket`, `swing`, `humanization`, `drums`, `recipe`

---

#### 29. `drum-programming-by-genre`

- **Title:** Drum Programming by Genre
- **Scope:** rhythm
- **Folder:** rhythm
- **Subtopics:**
  - house (4-on-floor, off-beat hats, clap on 2-4)
  - hip-hop (boom-bap vs. trap, kick-snare displacement)
  - rock/indie (driven 8ths, push/pull on hat)
  - dnb/breakbeat (chopped break vs. programmed)
  - pop (genre-blending modern beats)
  - velocity layering and natural-feel programming
- **Canonical references:** Attack Magazine *Secrets of Dance Music Production* and *Secrets of Techno Production*; Sound on Sound drum-programming articles; Ableton Live manual
- **Tags:** `rhythm`, `drum-programming`, `genre`, `electronic`, `pop`, `recipe`

---

#### 30. `kick-bass-relationship`

- **Title:** The Kick-and-Bass Relationship
- **Scope:** rhythm
- **Folder:** rhythm
- **Subtopics:**
  - frequency-domain separation (kick owns sub, bass owns body — or vice versa)
  - sidechain compression depth and timing per genre
  - rhythmic interlock patterns (bass-on-the-and, root-on-the-kick)
  - phase coherence between kick and bass
  - the dance-music duck (deep, fast release)
  - the rock approach (no sidechain, EQ-based separation)
- **Canonical references:** Mike Senior, *Mixing Secrets*; Attack Magazine; SOS Inside Track articles
- **Tags:** `rhythm`, `low-end`, `kick`, `bass`, `sidechain`, `mixing`, `principle`

---

### Synthesis (3)

---

#### 31. `subtractive-synthesis-fundamentals`

- **Title:** Subtractive Synthesis Fundamentals
- **Scope:** synthesis
- **Folder:** synthesis
- **Subtopics:**
  - oscillator-filter-amp signal path
  - waveform harmonic content (saw, square, triangle, sine)
  - filter types (LP, HP, BP, notch) and resonance
  - ADSR shape vocabulary
  - LFO modulation targets (pitch, filter, amp, pan)
  - the bass/lead/pad/pluck taxonomy as patch design starting points
- **Canonical references:** Gordon Reid, *Synth Secrets* (in seed); Fred Welsh, *Synthesizer Cookbook*; Ableton Learning Synths
- **Tags:** `synthesis`, `subtractive`, `oscillator`, `filter`, `envelope`, `LFO`, `principle`

---

#### 32. `fm-and-wavetable-synthesis`

- **Title:** FM and Wavetable Synthesis
- **Scope:** synthesis
- **Folder:** synthesis
- **Subtopics:**
  - FM core idea (modulator frequency × carrier = sidebands)
  - operator/algorithm vocabulary (DX7-style)
  - classic FM sounds (e-piano, bell, bass)
  - wavetable basics (a table of single-cycle waveforms, scan position as modulation target)
  - wavetable for evolving textures (slow position LFO + filter movement)
  - hybrid synthesis (wavetable + subtractive filter)
- **Canonical references:** Gordon Reid, *Synth Secrets* (in seed); Welsh's Synthesizer Cookbook; Native Instruments Massive/Massive X manuals
- **Tags:** `synthesis`, `FM`, `wavetable`, `principle`, `recipe`

---

#### 33. `patch-design-vocabulary`

- **Title:** Patch Design Vocabulary — Translating Adjectives to Moves
- **Scope:** synthesis
- **Folder:** synthesis
- **Subtopics:**
  - "warm" → low-pass filter close, detuned oscillators, slight saturation
  - "bright" → high filter cutoff, sawtooth or pulse content, slight chorus
  - "evolving" → slow LFO on filter and/or wavetable position
  - "glassy" → FM operator on a bell ratio, fast decay
  - "huge" → unison detune, octave stack, stereo widening
  - "plucked" → fast attack, fast decay, low sustain
  - the move-vocabulary as a teaching tool
- **Canonical references:** Welsh's *Synthesizer Cookbook* (102 universal patches); Gordon Reid, *Synth Secrets*; Ableton Learning Synths
- **Tags:** `synthesis`, `patch-design`, `recipe`, `vocabulary`, `methodology`

---

### Sampling (2)

---

#### 34. `chopping-resampling-and-warping`

- **Title:** Chopping, Resampling, and Warping
- **Scope:** sampling
- **Folder:** sampling
- **Subtopics:**
  - the chop workflow (slice to MIDI, slice to drum rack)
  - resampling as commitment (bouncing, then re-loading as audio)
  - warp modes (beats, complex, complex pro, re-pitch) and when each is right
  - time-stretching artifacts and how to hide them
  - pitch-shifting samples for tonal sound design
  - vinyl-style sampling chains
- **Canonical references:** Ableton Live Reference Manual; Attack Magazine; Dennis DeSantis, *Making Music* (in seed)
- **Tags:** `sampling`, `chopping`, `resampling`, `warping`, `electronic`, `recipe`

---

#### 35. `loop-based-arrangement`

- **Title:** Loop-Based Arrangement
- **Scope:** sampling
- **Folder:** sampling
- **Subtopics:**
  - the 8-bar/16-bar loop unit
  - building from a single loop (subtract, add, rearrange)
  - the "minus-one" arrangement technique
  - filter sweeps and risers as section markers
  - the breakdown-build-drop architecture in dance
  - using session view for arrangement exploration
- **Canonical references:** Dennis DeSantis, *Making Music* (in seed); Attack Magazine *Secrets of Dance Music Production*; Ableton Live Manual
- **Tags:** `sampling`, `arrangement`, `electronic`, `loop`, `dance`, `recipe`

---

### Workflow (3)

---

#### 36. `session-methodology`

- **Title:** Session Methodology
- **Scope:** workflow
- **Folder:** workflow
- **Subtopics:**
  - preproduction checklist (key, tempo, song length, references)
  - tracking-day flow (rough mix as you go, commit decisions)
  - the "decide once, move on" principle
  - separating composing, arranging, and mixing modes
  - session naming/versioning conventions
  - daily/weekly cadence (writing days vs. production days)
- **Canonical references:** Mixerman, *Zen and the Art of Producing*; Dennis DeSantis, *Making Music* (in seed); SOS Inside Track articles (TMS/Capaldi in corpus)
- **Tags:** `workflow`, `methodology`, `preproduction`, `tracking`, `principle`

---

#### 37. `finishing-work-and-completion`

- **Title:** Finishing Work and Completion
- **Scope:** workflow
- **Folder:** workflow
- **Subtopics:**
  - the "done is better than perfect" calibration
  - the 80/20 cutoff (last 20% of polish is 80% of the time)
  - bounce-and-listen-elsewhere as a fresh-ears tool
  - shipping vs. iterating decision criteria
  - finishing rituals (master bounce, archive session, log lessons)
  - the "throwaway song per week" practice
- **Canonical references:** Dennis DeSantis, *Making Music* (in seed); Mixerman, *Zen and the Art of Producing*
- **Tags:** `workflow`, `methodology`, `finishing`, `principle`

---

#### 38. `preproduction-and-demo-handoff`

- **Title:** Preproduction and Demo Handoff
- **Scope:** workflow
- **Folder:** workflow
- **Subtopics:**
  - what to lock before tracking (key, tempo, arrangement, structure)
  - demo-to-final transition (what survives, what gets retracked)
  - the "rough mix first" rule
  - stem hand-off conventions when working with a mixer
  - what a session-prep checklist contains
  - artist-vs-producer role separation
- **Canonical references:** Mixerman, *Zen and the Art of Producing*; SOS Inside Track features; Howard Massey, *Behind the Glass*
- **Tags:** `workflow`, `preproduction`, `methodology`, `demo`, `tracking`, `principle`

---

## Suggested Firing Order

If you don't want to fire all 38 at once, here's the order that builds the most useful retrieval surface first:

**Batch 1 — 10 highest-leverage:**
1, 6, 7, 12, 13, 18, 24, 28, 31, 36
*(mic placement, EQ, compression, mastering chain, LUFS, chord progressions, object writing, groove, subtractive synthesis, session methodology)*

**Batch 2 — next 10:**
2, 8, 11, 16, 25, 30, 33, 35, 14, 26
*(signal flow, reverb, vocal mixing, section function, rhyme types, kick-bass, patch design vocab, loop arrangement, limiting, POV)*

**Batch 3 — depth fill, the remaining 18:**
3, 4, 5, 9, 10, 15, 17, 19, 20, 21, 22, 23, 27, 29, 32, 34, 37, 38

---

## Post-Processing Checklist

After each prompt returns markdown, run through this before adding to retrieval:

- [ ] Verify the file is saved at the right path: `corpus/{scope}/{filename}.md`
- [ ] Check 2–3 specific numeric/factual claims against a known source
- [ ] Confirm "Sources" section has real URLs (no hallucinated citations)
- [ ] Confirm front-matter has the `Source: Deep-research synthesis (2026-05)` line
- [ ] Confirm tags align with the ARLO taxonomy
- [ ] If any section feels thin or generic, regenerate just that section with a more focused prompt
- [ ] (Optional) Add the file path to a `corpus/MANIFEST.md` you maintain by hand
