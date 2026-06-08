# ARLO Aesthetic Corpus — Prompt Set

A reusable prompt template plus **18 topic-specific variable sets** for generating seed knowledge-base entries focused on the aesthetic profile from `AESTHETIC-RESEARCH-PLAN.md`.

**Output:** 18 markdown files split across two new top-level folders — `corpus/artists/` and `corpus/techniques/`.

**Provenance note:** Same as PROMPTS.md — generated files are tagged `Deep-research synthesis (2026-05) — verify before treating as authoritative`. Treat as aesthetic-anchored chunks that will eventually be supplemented by direct quotes from book sources (Berklee *Beyond Bluegrass Banjo*, Attack Mag *Secrets of Dance Music Production*, etc.) once acquired.

---

## Folder additions

```
corpus/
├── artists/         ← new — artist-anchored chunks
└── techniques/      ← new — technique-anchored chunks
```

Create these before firing batches: `mkdir -p ~/Dev/arlo/corpus/{artists,techniques}`.

---

## How to use

Same workflow as PROMPTS.md: pick a row, substitute variables into the master template, paste into Claude Code or dispatch as an agent. See `AESTHETIC-SESSIONS.md` for batch-dispatch kickoff messages.

---

## Master Template (Aesthetic-Anchored Variant)

```
You are writing a seed knowledge-base entry for ARLO, a local-first AI songwriting/production assistant. ARLO retrieves these chunks during conversation about a specific hybrid aesthetic: emotionally direct but experimental music blending Bon Iver-style vocal layering, LCD Soundsystem-style dance-punk repetition, Charli XCX-style maximalist sound design, mk.gee-style DI/reamped guitar weirdness, and Billy Strings/Punch Brothers/Pikelny-style acoustic virtuosity.

TOPIC: {{TOPIC}}
SCOPE: {{SCOPE}}
TARGET PATH: corpus/{{FOLDER}}/{{FILENAME}}.md

## Your task

Produce a single markdown file titled "{{TITLE}}" focused on these subtopics:

{{SUBTOPICS}}

## Primary sources to ground in

Read or reference these specific URLs as your primary evidence. They are real, accessible articles/manuals — not book titles to paraphrase:

{{PRIMARY_SOURCES}}

You may augment with additional web research via WebSearch, but every concrete claim should trace back to either one of these primary sources or to a reputable secondary source you cite inline.

## Content requirements

- **Concrete over abstract.** Specific gear models, specific plugin settings, specific song examples, specific exercise instructions. NOT philosophy or motivation.
- **Aesthetic anchoring.** Where relevant, name the specific artists/producers/tracks from the aesthetic stack (Vernon, Burton, Messina, Murphy, Mahoney, Cook, SOPHIE, mk.gee, Strings, Thile, Pikelny, Fleck). A concrete claim paired with a verifiable artist example is stronger than an abstract principle.
- **Inline citations.** Use markdown links: `[Source Title](URL)` within sentences where claims originate. Don't save citations only for a bibliography.
- **Anti-hallucination guard.** If you cannot verify a specific number, setting, or attribution through web research, OMIT it. Do not guess. Made-up specifics will poison ARLO's retrieval. Prefer qualitative ("Vernon stacks falsetto layers to compensate for SM57 limitations") over fabricated specifics ("Vernon uses a 12-voice stack at -8 dB each").
- **Length:** 1500–2500 words.
- **Structure:** 8–15 H2 sections, each a self-contained idea (these become retrieval chunks). 100–250 words per section.
- **Audience:** intermediate musicians/producers. Don't re-explain basic vocabulary (DAW, EQ, compression).

## Required output format

Begin with this front-matter:

```
# {{TITLE}}

**Scope:** {{SCOPE}}
**Source:** Deep-research synthesis (2026-05) — verify before treating as authoritative
**Aesthetic-stack relevance:** {{AESTHETIC_TAGS}}
**Tags:** {{SUGGESTED_TAGS}}

---
```

Then 8–15 H2 sections covering the subtopics.

End with these two sections:

```
## Cited Retrieval Topics

List 5–10 specific user questions this document should be retrieved for. Phrase them as a musician would actually type — lowercase, conversational, no question marks.

## Sources

Clean bibliography of every URL linked inline above.
```

## What this is NOT

- Not a survey covering every angle — go deep on the actionable specifics
- Not a beginner tutorial that re-explains fundamentals
- Not opinion or philosophy — concrete craft only
- Not exhaustive — 8 strong chunks beats 20 thin ones

Begin research and produce the markdown now.
```

---

## The 18 Prompts

Organized into two clusters: **Artists (10)** and **Techniques (8)**.

---

### Cluster A — Artist-Anchored (10 prompts)

---

#### 1. `bon-iver-vocal-layering-messina`

- **Title:** Bon Iver Vocal Layering and the Messina Device
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - Justin Vernon's vocal-stacking philosophy (SM57 falsetto layers, Bon Iver's choral-like sound)
  - The Messina device — Chris Messina's hardwired real-time Prismizer alternative
  - Francis Starlite's Prismizer as the inspiration
  - Live vs. studio use of the Messina
  - The vocal chain on *22, A Million*
  - Use of formant manipulation (Little AlterBoy and others)
- **Primary sources:**
  - [Sound on Sound, "Inside Track: Bon Iver '22, A Million'"](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million)
  - [W Magazine engineer interview (BJ Burton)](https://www.wmagazine.com/story/the-engineer-behind-bon-ivers-22-a-million-clears-up-any-confusion-about-its-high-tech-sound)
  - [MusicRadar: "How Bon Iver made a Platinum-selling record with two guitars and a single SM57"](https://www.musicradar.com/news/bon-iver-platinum-record-microphone)
- **Aesthetic-stack relevance:** Bon Iver, processed-folk intimacy
- **Suggested tags:** `bon-iver`, `vernon`, `messina`, `prismizer`, `vocal-stacking`, `formant`, `recipe`

---

#### 2. `bon-iver-sample-driven-songwriting`

- **Title:** Bon Iver Sample-Driven Songwriting (OP-1 and 22, A Million)
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - The OP-1 as Vernon's primary sketchpad
  - The "two-two" origin story — how a vocal-sample manipulation seeded the album's number/code aesthetic
  - Sample-as-songwriting-material vs. sample-as-decoration
  - Specific samples used on *22, A Million* (Stevie Nicks, Mahalia Jackson, Steve Winwood)
  - Resampling workflow — bouncing, re-loading, re-pitching
  - How constraints from the OP-1 shaped the album's identity
- **Primary sources:**
  - [MusicRadar: OP-1 + Steve Winwood sampling story](https://www.musicradar.com/artists/we-were-sampling-steve-winwood-in-between-bong-rips-on-my-op-1-how-bon-iver-met-haim-backstage-at-a-music-festival-and-ended-up-collaborating-a-decade-later)
  - [WhoSampled: "Justin Vernon Discusses His Use of Samples on Latest Album '22, A Million'"](https://www.whosampled.com/news/2016/11/02/bon-ivers-justin-vernon-discusses-his-use-of-samples-on-latest-album-22-a-million/)
  - [The Current: "All of the songs sampled on Bon Iver's '22, A Million'"](https://www.thecurrent.org/feature/2016/09/03/all-of-the-songs-sampled-on-bon-ivers-22-a-million)
  - [Varnado academic paper on "33 'God'" sampling aesthetic](https://www.arpjournal.com/asarpwp/wp-content/uploads/2021/12/Elizabeth-Navarra-Varnado_ARP2019.pdf)
- **Aesthetic-stack relevance:** Bon Iver, sample-as-songwriting
- **Suggested tags:** `bon-iver`, `vernon`, `op-1`, `sampling`, `resampling`, `teenage-engineering`, `songwriting`

---

#### 3. `lcd-soundsystem-synth-sound-design`

- **Title:** LCD Soundsystem Synth Sound Design Vocabulary
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - The EMS VCS3 and the "Someone Great" joystick-chord technique
  - Yamaha CS-60 as kick/snare source (resampled drum hits from synth)
  - Roland Juno-60, SH-101, EML Electrocomp 100 — when each is used
  - The Powertran Polysynth — Murphy's recent favorite
  - Reasons Murphy favors quirky/cheap synths over Moog/Prophet defaults
  - How LCD's specific synth choices contribute to dense-yet-clear mixes
- **Primary sources:**
  - [SynthHistory: "Interview with James Murphy"](https://www.synthhistory.com/post/interview-with-james-murphy)
  - [Reverb Machine: "LCD Soundsystem Synth Sounds"](https://reverbmachine.com/blog/lcd-soundsystem-synth-sounds/)
  - [Mixdown Magazine: "Gear Rundown: LCD Soundsystem"](https://mixdownmag.com.au/features/rig-rundown-lcd-soundsystem/)
  - [Vice: "DFA Records Has More Gear Than You"](https://www.vice.com/en/article/kby4nz/dfa-records-has-more-gear-than-you)
- **Aesthetic-stack relevance:** LCD Soundsystem, dance-punk, analog synth character
- **Suggested tags:** `lcd`, `murphy`, `dfa`, `analog-synths`, `ems`, `juno`, `cs-60`, `sound-design`

---

#### 4. `lcd-soundsystem-live-electronic-rig`

- **Title:** LCD Soundsystem's Live Electronic-Rock Hybrid Rig
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - The "no click track" rule — drummer Pat Mahoney as live timekeeper
  - Synthetic-elements-only on the NPC playback (606 drum machine, no organic samples)
  - Moog Taurus II with Korg SQ10 modular sequencer
  - Roland System 100m role
  - Rob Sinclair's live-trigger system architecture
  - How hardware sync is solved without timecode
- **Primary sources:**
  - [Mixdown Magazine LCD rig rundown](https://mixdownmag.com.au/features/rig-rundown-lcd-soundsystem/)
  - [MOD WIGGLER thread: "How does LCD Soundsystem sync their gear?"](https://www.modwiggler.com/forum/viewtopic.php?t=256620)
  - [Triple Geek: LCD Soundsystem 2016 visual setup](https://triplegeek.com/visuals/lcd-soundsystem-2016.html)
  - [Equipboard: LCD Soundsystem](https://equipboard.com/band/lcd-soundsystem)
- **Aesthetic-stack relevance:** LCD Soundsystem, live electronic-hybrid
- **Suggested tags:** `lcd`, `live-rig`, `hardware-sync`, `mahoney`, `triggers`, `modular`

---

#### 5. `james-murphy-analog-synth-philosophy`

- **Title:** James Murphy's Analog-Synth-as-Character Philosophy
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - "Cheap guitars, expensive synths" — Murphy's gear-cost inversion
  - The Squier Telecaster + Epiphone bass philosophy
  - DBX 165 + LA-2A + UA preamp drum-bus chain
  - Beyerdynamic M160, Coles 4033, RCA BK5 — the LCD ribbon-mic palette
  - Plantain Studio (DFA HQ) layout and workflow
  - How Murphy distinguishes "production" from "engineering" on LCD records
- **Primary sources:**
  - [SynthHistory interview with James Murphy](https://www.synthhistory.com/post/interview-with-james-murphy)
  - [Equipboard: James Murphy](https://equipboard.com/pros/james-murphy)
  - [Vice DFA gear feature](https://www.vice.com/en/article/kby4nz/dfa-records-has-more-gear-than-you)
  - [XLR8R: "LCD Soundsystem In The Studio"](https://xlr8r.com/features/lcd-soundsystem-in-the-studio/)
- **Aesthetic-stack relevance:** LCD Soundsystem, analog character, dance-punk production
- **Suggested tags:** `lcd`, `murphy`, `dfa`, `analog`, `gear-philosophy`, `studio`

---

#### 6. `pat-mahoney-dance-punk-drumming`

- **Title:** Pat Mahoney's Dance-Punk Drumming
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - "Hypnotic, not dumb" — Mahoney's defense of repetitive drumming
  - The disco-influence pipeline through Beastie Boys vinyl obsession
  - Drummer-as-tempo-keeper vs. click-track approach
  - Stripped-down kit vocabulary that makes bodies move
  - How Mahoney's playing interacts with Murphy's sequenced synths
  - The Museum of Love side project as a window into the disco influence
- **Primary sources:**
  - [Kisses & Noise: Pat Mahoney interview](http://kissesandnoise.com/2010/10/lcd-soundsystem-w-sleigh-bells-tonight-interview-pat-mahoney-of-lcd-soundsystem/)
  - [Ransom Note: "Pat Mahoney Talks: Museum Of Love And Life After LCD"](https://www.theransomnote.com/music/interviews/pat-mahoney-talks-museum-of-love-and-life-after-lcd/)
  - [i-D: Pat Mahoney on Museum of Love](https://i-d.co/article/pat-mahoney-talks-about-his-new-band-museum-of-love-and-life-after-lcd-soundsystem/)
  - [Georgia Straight: "Former punk rocker Pat Mahoney"](https://www.straight.com/article-156539/former-punk-rocker-pat-mahoney-not-afraid-admit-he-loves-disco)
- **Aesthetic-stack relevance:** LCD Soundsystem, dance-punk groove
- **Suggested tags:** `lcd`, `mahoney`, `drumming`, `dance-punk`, `disco`, `repetition`

---

#### 7. `charli-xcx-brat-production`

- **Title:** Charli XCX *Brat* Production Approach
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - The "tight collection of sounds" — minimalism-as-maximalism
  - A.G. Cook as executive producer; Finn Keane and Cirkut roles
  - The London illegal-rave scene as sonic touchstone
  - Specific *Brat* production moves (verifiable from Apple Music interview and reviews)
  - How *Brat* differs from earlier Charli + Cook work (*how i'm feeling now*, *Pop 2*)
  - The transition from hyperpop-aligned to mainstream-rave aesthetics
- **Primary sources:**
  - [Wikipedia: Brat (album)](https://en.wikipedia.org/wiki/Brat_(album))
  - [Grammy.com: "Charli XCX's Road To 'Brat'"](https://www.grammy.com/news/charli-xcx-brat-songs-albums-myspace-hyperpop)
  - [MIDiA Research case study](https://www.midiaresearch.com/case-studies/how-charli-xcx-leveraged-the-hyperpop-scene-into-a-global-movement)
  - [The Needle Drop *Brat* review](https://theneedledrop.com/album-reviews/charli-xcx-brat-album-review/)
- **Aesthetic-stack relevance:** Charli XCX, hyperpop, rave
- **Suggested tags:** `charli-xcx`, `ag-cook`, `brat`, `hyperpop`, `rave`, `pop-production`

---

#### 8. `mk-gee-di-direct-philosophy`

- **Title:** mk.gee's DI-Direct Guitar Philosophy
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - "I kind of hate guitar" — the framing that explains the refusal of amp tone
  - Recording DI-direct into a preamp (no amp) as default
  - The Fender Jaguar as primary instrument
  - Effects-processing post-tracking as the character-shaping stage
  - The "dead, plucky" raw tone as starting material
  - Analog tape recorders in the live rig
  - The bedroom-pop-meets-experimental-studio aesthetic
- **Primary sources:**
  - [Dazed: "The miseducation of Mk.gee"](https://www.dazeddigital.com/music/article/64551/1/mk-gee-michael-gordon-interview-autumn-2024-issue-dazed)
  - [Switched On Pop Substack: "Breaking Through: Doechii, Mk.gee, ROSÉ"](https://switchedonpop.substack.com/p/breaking-through-doechii-mkgee-rose)
  - [Passion of the Weiss: "Soundcheck: Mk.gee"](https://www.passionweiss.com/2024/02/26/soundcheck-mk-gee-two-star-and-the-dream-police/)
  - [Rolling Stone review](https://www.rollingstone.com/music/music-album-reviews/mk-gee-two-star-and-the-dream-police-1234971328/)
- **Aesthetic-stack relevance:** mk.gee, DI/reamped guitar weirdness
- **Suggested tags:** `mk-gee`, `gordon`, `di-recording`, `fender-jaguar`, `effects-processing`, `bedroom-pop`

---

#### 9. `billy-strings-flatpicking-stompboxes`

- **Title:** Billy Strings — Flatpicking Meets Stompboxes
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - The "rapid-fire alternate picking in open position" technical core
  - Doc Watson lineage + the metal cross-pollination
  - The Bourgeois D-style dreadnought as primary instrument
  - Strings' pedalboard — modelers, stompboxes, and racks layered onto acoustic
  - "Practicing with eyes closed" — the listening-focused practice method
  - How the bluegrass + pedals hybrid sounds in live context (Premier Guitar Rig Rundown)
- **Primary sources:**
  - [Premier Guitar Rig Rundown: Billy Strings 2023](https://www.premierguitar.com/videos/rig-rundown/billy-strings-2023)
  - [Premier Guitar: "Billy Strings and Molly Tuttle in Conversation"](https://www.premierguitar.com/artists/guitarists/billy-strings-and-molly-tuttle)
  - [Acoustic Guitar: Billy Strings interview](https://acousticguitar.com/interview-billy-strings-electrifying-bluegrass/)
  - [Premier Guitar Wong Notes podcast: Billy Strings](https://www.premierguitar.com/podcast/wong-notes/billy-strings)
- **Aesthetic-stack relevance:** Billy Strings, acoustic virtuosity + pedalboard
- **Suggested tags:** `billy-strings`, `flatpicking`, `bluegrass`, `pedals`, `acoustic-electric`, `rig`

---

#### 10. `punch-brothers-progressive-composition`

- **Title:** Punch Brothers — Progressive Bluegrass Composition
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - Chris Thile's "bluegrass instrumentation, classical strictures" framing
  - How chamber-music structure meets bluegrass instrumentation
  - The role of mandolin, banjo, fiddle, guitar, bass in a non-traditional bluegrass band
  - Specific song examples ("Movement and Location," etc.) showing progressive structures
  - Genre-crossing — bluegrass + jazz + classical + pop hybrids
  - Why Punch Brothers refuse to be "museum curators" of bluegrass
- **Primary sources:**
  - [The Boot: Chris Thile interview](https://theboot.com/chris-thile-interview-punch-brothers-whos-feeling-young-now-album/)
  - [PopMatters: Punch Brothers interview](https://www.popmatters.com/157872-no-concern-of-yours-an-interview-with-punch-brothers-2495857684)
  - [Seventh Row: "How to Grow a Band" review](https://seventh-row.com/2014/02/19/punch-brothers-how-to-grow-a-band/)
  - [Asheville Stages: Chris Thile interview](https://ashevillestages.com/music/interview-chris-thile)
- **Aesthetic-stack relevance:** Punch Brothers, modal-progressive bluegrass
- **Suggested tags:** `punch-brothers`, `thile`, `progressive-bluegrass`, `chamber-bluegrass`, `composition`

---

### Cluster B — Technique-Anchored (8 prompts)

---

#### 11. `vocal-stacking-bon-iver-style`

- **Title:** Vocal Stacking — Bon Iver-Style Layered Choirs
- **Scope:** technique
- **Folder:** `techniques`
- **Subtopics:**
  - The constraint-driven origin (single SM57, multiple falsetto layers)
  - Recording approach — multiple takes of the same line, panned and pitched
  - Layering by interval (octave, 3rd, 5th) vs. unison-stack
  - Formant manipulation for choir-from-one-voice effect (Little AlterBoy, Antares Harmony Engine)
  - Mixing the stack — pan distribution, EQ separation, reverb glue
  - When to use a stack vs. when single-take is stronger
  - Worked example from a specific Bon Iver track
- **Primary sources:**
  - [MusicRadar: Bon Iver Platinum-record SM57 story](https://www.musicradar.com/news/bon-iver-platinum-record-microphone)
  - [Sound on Sound: Inside Track Bon Iver](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million)
  - [Bon Iver vocal-double YouTube tutorial](https://www.youtube.com/watch?v=YzEhLhXv5eA)
  - [WAVHeaven Medium: "How to Produce like Bon Iver"](https://medium.com/@wavheaven/how-to-produce-like-bon-iver-d37b543a74f6)
- **Aesthetic-stack relevance:** Bon Iver, vocal stacking
- **Suggested tags:** `vocal-stacking`, `bon-iver`, `formant`, `sm57`, `recipe`, `mixing`

---

#### 12. `auto-tune-as-creative-tool`

- **Title:** Auto-Tune as Creative Tool — Cher to Bon Iver to SOPHIE
- **Scope:** technique
- **Folder:** `techniques`
- **Subtopics:**
  - The Andy Hildebrand origin (seismic autocorrelation → vocal pitch correction)
  - Cher "Believe" (1998) — first creative-use famous example
  - T-Pain's hip-hop pioneer status — the retune-speed-to-zero discovery
  - Kanye West *808s & Heartbreak* (2008) — bringing Auto-Tune to rap as expressive tool
  - Bon Iver "Woods" — Auto-Tune as folk experimentalism
  - SOPHIE / hyperpop — hard-tune as alien-pop aesthetic
  - Specific Auto-Tune settings for different aesthetics (retune speed, humanize, formant)
- **Primary sources:**
  - [Berklee: "A Sonic History of Auto-Tune According to T-Pain"](https://www.berklee.edu/news/berklee-now/sonic-history-auto-tune-according-t-pain)
  - [Red Bull: "History of Auto-Tune in seven songs"](https://www.redbull.com/gb-en/history-of-auto-tune-in-seven-songs)
  - [Complex: "The T-Pain Effect"](https://www.complex.com/music/a/kyle-kramer/the-t-pain-efffect-how-auto-tune-ruined-music-and-saved-hip-hop)
  - [Wikipedia: Auto-Tune](https://en.wikipedia.org/wiki/Auto-Tune)
  - [MusicRadar SOPHIE-style tutorial — hard-tune specifics](https://www.musicradar.com/tutorials/music-production-tutorials/how-to-craft-extreme-hyperpop-textures-to-make-sophie-style-tunes)
- **Aesthetic-stack relevance:** Bon Iver, Charli XCX, SOPHIE
- **Suggested tags:** `auto-tune`, `vocal-processing`, `creative-effect`, `hard-tune`, `formant`, `t-pain`, `bon-iver`, `sophie`

---

#### 13. `hyperpop-sound-design`

- **Title:** Hyperpop Sound Design — Transitions, Drops, and Extreme Textures
- **Scope:** technique
- **Folder:** `techniques`
- **Subtopics:**
  - Saturated 808s with distortion-as-harmonic-content
  - Hard-tune vocal settings — retune speed 0.00 ms, humanize zero
  - Formant shifting for chipmunk/alien effects (+7.20 semitones extreme)
  - High-pitched octave/interval leads and edgy angular basses
  - Sudden transitions — Beat Repeat, stuttered drops, glitchy interruptions
  - Wide stereo synth design with extreme processing
  - FM8 and Massive X for squelchy morphing textures
  - Worked examples — SOPHIE, Charli XCX, A.G. Cook, 100 gecs
- **Primary sources:**
  - [MusicRadar: "How to craft extreme hyperpop textures to make SOPHIE-style tunes"](https://www.musicradar.com/tutorials/music-production-tutorials/how-to-craft-extreme-hyperpop-textures-to-make-sophie-style-tunes)
  - [Native Instruments blog: "Hyperpop production 101"](https://blog.native-instruments.com/hyperpop/)
  - [Waves: "How to Produce Hyperpop Songs"](https://www.waves.com/how-to-produce-hyperpop-songs-tips)
  - [Cedar Sound Studios hyperpop guide](https://www.cedarsoundstudios.com/blogs/news/how-to-make-hyperpop-a-comprehensive-guide)
  - [Surge Sounds: Complete Hyperpop production guide](https://surgesounds.com/post/how-to-make-hyperpop-complete-production-guide)
- **Aesthetic-stack relevance:** Charli XCX, SOPHIE, A.G. Cook
- **Suggested tags:** `hyperpop`, `sound-design`, `sophie`, `ag-cook`, `hard-tune`, `transitions`, `808`, `synth-design`

---

#### 14. `hardware-sampling-workflow`

- **Title:** Hardware Sampling Workflow — OP-1, Octatrack, Digitakt
- **Scope:** technique
- **Folder:** `techniques`
- **Subtopics:**
  - The OP-1 sketchpad workflow — record, manipulate, commit
  - When hardware constraints become creative drivers
  - Octatrack pattern-and-scene live performance vocabulary
  - Digitakt parameter-locks and conditional trigs (already in corpus — extend it)
  - Hybrid hardware-into-DAW workflows (resampling chains)
  - Specific use cases — Bon Iver OP-1, LCD-style live triggering
  - When to commit a hardware sample vs. keep options open
- **Primary sources:**
  - [Teenage Engineering OP-1 product page](https://teenage.engineering/products/op-1)
  - [MusicRadar OP-1 + Steve Winwood story](https://www.musicradar.com/artists/we-were-sampling-steve-winwood-in-between-bong-rips-on-my-op-1-how-bon-iver-met-haim-backstage-at-a-music-festival-and-ended-up-collaborating-a-decade-later)
  - [Elektron Octatrack product page](https://www.elektron.se/en/octatrack-mkii-explorer)
  - Already in corpus: `corpus/sampling/elektron-digitakt-ii-manual.pdf`
  - [Sound on Sound Octatrack reviews/articles](https://www.soundonsound.com) (search)
- **Aesthetic-stack relevance:** Bon Iver, LCD Soundsystem, electronic-hybrid production
- **Suggested tags:** `hardware-sampling`, `op-1`, `octatrack`, `digitakt`, `live-rig`, `resampling`, `workflow`

---

#### 15. `reamping-fundamentals`

- **Title:** Reamping Fundamentals — DI Then Transform
- **Scope:** technique
- **Folder:** `techniques`
- **Subtopics:**
  - The two-stage flow (DI track → reamp box → amp → re-record)
  - Why reamping (not commit-tone-at-tracking) opens creative options
  - Impedance matching — what a reamp box does electrically
  - Setting reamp output levels to avoid distortion of the reamp box itself
  - Reamping non-guitar sources (vocals, synths, drums) — the "send to a Fender amp" trick
  - The mk.gee workflow as an extreme case (DI everything, then transform with effects-as-instruments)
  - Specific reamp boxes (Radial Reamp, Little Labs, Reamp.com)
- **Primary sources:**
  - [Premier Guitar: "How to Reamp Your Electric Guitar Tone"](https://www.premierguitar.com/diy/recording-dojo/reamp)
  - [Premier Guitar: "Reamping Fun for the Whole Band"](https://www.premierguitar.com/articles/Reamping_Fun_for_the_Whole_Band)
  - [Audient: Easy Guide To Reamping](https://audient.com/tutorial/reamping/)
  - [Pro Audio Files: Reamping Guitars guide](https://theproaudiofiles.com/reamping-guitars/)
  - [Roger Montejano: 14 reamping ideas](https://rogermontejano.com/articles/what-s-reamping-how-to-set-it-up-and-14-ideas-on-how-to-use-it)
- **Aesthetic-stack relevance:** mk.gee, Bon Iver, LCD Soundsystem
- **Suggested tags:** `reamping`, `di`, `guitar`, `recording`, `creative-workflow`, `mk-gee`

---

#### 16. `pedal-as-instrument-workflow`

- **Title:** Pedalboard as Instrument — Effects-Driven Composition
- **Scope:** technique
- **Folder:** `techniques`
- **Subtopics:**
  - The mindset shift — pedals as compositional element vs. tone shaping
  - Building a pedalboard around an aesthetic (ambient/textural vs. dance/rhythmic vs. acoustic-augmenting)
  - Signal-chain order rationales (drive → modulation → time-based vs. alternatives)
  - The KNOBs aesthetic — pedal-demo-as-composition
  - Specific aesthetic-relevant pedal archetypes (granular reverb, pitch shifter, modulated delay, sample-and-hold filter)
  - Billy Strings' acoustic-into-pedalboard approach
  - mk.gee's deliberate non-amp signal chain
- **Primary sources:**
  - [KNOBs YouTube channel](https://www.youtube.com/c/Knobs) (note: text-on-screen captions, verify per video)
  - [KNOBs Creative site](https://www.knobscreative.com/)
  - [Guitar World: "Meet Knobs"](https://www.guitarworld.com/features/knobs)
  - [Premier Guitar Recording Dojo column](https://www.premierguitar.com/diy/recording-dojo)
  - [Reverb News: "10 Up-and-Coming Gear YouTube Channels"](https://reverb.com/news/10-up-and-coming-gear-youtube-channels-you-should-know)
  - [Delicious Audio: Best Ambient-Shoegaze Reverb Pedals](https://delicious-audio.com/best-ambient-shoegaze-reverb-pedals/)
- **Aesthetic-stack relevance:** mk.gee, Billy Strings, ambient/textural production
- **Suggested tags:** `pedals`, `pedal-as-instrument`, `ambient`, `texture`, `signal-chain`, `knobs`

---

#### 17. `modal-bluegrass-harmony`

- **Title:** Modal Bluegrass Harmony — Beyond I-IV-V
- **Scope:** technique
- **Folder:** `techniques`
- **Subtopics:**
  - Traditional bluegrass harmonic vocabulary (I, IV, V, sometimes vi)
  - How Béla Fleck, Noam Pikelny, Chris Thile pushed bluegrass into modal territory
  - Specific modal moves — Mixolydian (♭VII), Dorian (minor + ♮6), Aeolian + Phrygian flavors
  - Modal-vamp structures vs. functional-progression structures in bluegrass
  - Voice leading on bluegrass instruments (mandolin chops, banjo rolls, fiddle drones)
  - How the Punch Brothers extend this with classical-borrowed chromaticism
- **Primary sources:**
  - [Fretboard Journal: Noam Pikelny interview](https://www.fretboardjournal.com/features/interview-noam-pikelny-art-banjo-fiddle-duo/)
  - [Banjo Newsletter: Noam Pikelny interviews Béla Fleck](https://banjonews.com/2021-09/noam_pikelny_interviews_bela_fleck_my_bluegrass_heart.html)
  - [Reverb: "Three Bluegrass Banjo Styles Explained with Noam Pikelny"](https://reverb.com/uk/news/3-bluegrass-banjo-styles-explained-with-noam-pikelny)
  - [Banjo Newsletter: "Some Basic Music Theory"](https://banjonews.com/2009-12/some_basic_music_theory.html)
  - [Berklee Press: *Beyond Bluegrass Banjo* book page](https://berkleepress.com/strings/beyond-bluegrass-banjo-etudes-and-ideas-for-the-modern-banjo-player/) (book not in corpus — discuss what's known about its contents from reviews)
- **Aesthetic-stack relevance:** Punch Brothers, Pikelny, Strings, modal-progressive bluegrass
- **Suggested tags:** `bluegrass`, `modal-harmony`, `pikelny`, `fleck`, `banjo`, `mandolin`, `harmony`

---

#### 18. `dense-but-clear-mixing`

- **Title:** Dense-But-Clear Mixing — Many Layers, Few Mud Spots
- **Scope:** technique
- **Folder:** `techniques`
- **Subtopics:**
  - The arrangement-as-mixing principle (mixing starts at the arrangement stage)
  - Frequency-pocket carving for layered tracks
  - Mono-low / stereo-high architecture
  - Send-effects vs. insert-effects when stacking many elements
  - The Bon Iver *22, A Million* mix philosophy (emotional density, sonic restraint)
  - The Charli XCX *Brat* "tight collection of sounds" minimalism-as-maximalism
  - LCD's multi-synth layering without mud
  - Specific moves — sidechain compression, M/S EQ, careful reverb send routing
- **Primary sources:**
  - [SOS Inside Track: Bon Iver "22, A Million"](https://www.soundonsound.com/techniques/inside-track-bon-iver-22-a-million)
  - [SOS Inside Track: Billie Eilish "Bad Guy"](https://www.soundonsound.com/techniques/inside-track-billie-eilish-bad-guy) (already in corpus)
  - [Reverb Machine: LCD Soundsystem synth sounds](https://reverbmachine.com/blog/lcd-soundsystem-synth-sounds/)
  - [Grammy.com Charli XCX *Brat* feature](https://www.grammy.com/news/charli-xcx-brat-songs-albums-myspace-hyperpop)
  - Already in corpus: `corpus/mixing/low-end-management.md`, `corpus/mixing/mix-translation-and-reference-tracks.md`
- **Aesthetic-stack relevance:** Bon Iver, Charli XCX, LCD Soundsystem
- **Suggested tags:** `mixing`, `density`, `arrangement`, `low-end`, `bon-iver`, `lcd`, `charli-xcx`

---

---

### Cluster C — Listening-History Expansion (10 prompts: 19–28)

These prompts were added after analyzing Spotify listening history. They cover Talking Heads, Ry Cooder, Radiohead, Sufjan Stevens, and Dijon. Four of these (19, 24) are **deprecated** because the albums corpus (`ALBUMS-PROMPTS.md`) covers the same material as album-anchored deep-dives.

---

#### 19. ~~`talking-heads-remain-in-light-production`~~ — **DEPRECATED**

Album-anchored treatment in `ALBUMS-PROMPTS.md` row #3 (`talking-heads-remain-in-light`). Do not execute as an artist file. Cross-link from `corpus/artists/talking-heads-*.md` overview file when written.

---

#### 20. `david-byrne-songwriting-philosophy`

- **Title:** David Byrne Songwriting Philosophy
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - Byrne's lyrical economy (short declarative phrases, anti-cliché)
  - Structural risk-taking across Talking Heads catalog
  - The solo career arc (*Rei Momo*, *Look Into the Eyeball*, *American Utopia*)
  - Collaboration with Eno (Bush of Ghosts, *Everything That Happens*)
  - The "I am a singer who writes" frame vs. "songwriter who sings"
  - Live performance as compositional thinking (*American Utopia* staging)
- **Primary sources:**
  - [Classic Pop, "Making Talking Heads: Remain in Light"](https://www.classicpopmag.com/features/talking-heads-remain-in-light/)
  - [David Byrne's own site, "40 Years Ago: Eno meets Byrne"](https://www.davidbyrne.com/news/40-years-ago-brian-eno-meets-david-byrne-changing-the-talking-heads-career-)
  - [More Dark Than Shark, "Byrne interview Nov 1980"](https://moredarkthanshark.org/eno_int_riu-nov80.html)
  - [The World (PRX), "Talking Heads' Remain in Light"](https://theworld.org/stories/2018/11/07/talking-heads-remain-light)
  - [American Songwriter, "Behind the Album: Remain in Light"](https://americansongwriter.com/behind-the-album-remain-in-light-the-album-where-talking-heads-pushed-the-boundaries-and-left-their-peers-behind/)
- **Aesthetic-stack relevance:** Talking Heads, art-rock songwriting
- **Suggested tags:** `talking-heads`, `byrne`, `songwriting-philosophy`, `american-utopia`, `solo-career`, `bush-of-ghosts`

---

#### 21. `oblique-strategies-and-studio-as-instrument`

- **Title:** Oblique Strategies and Studio-as-Instrument Methodology
- **Scope:** technique
- **Folder:** `techniques`
- **Subtopics:**
  - Origin of the Oblique Strategies cards (Eno + Peter Schmidt, 1975)
  - Specific use during Talking Heads *Remain in Light* sessions
  - Use during Bowie's Berlin Trilogy
  - "Studio as compositional instrument" — recording before songs are written
  - How to apply Oblique Strategies in a modern DAW workflow
  - Adjacent practices: deliberate constraint, role-swapping, recording-as-discovery
- **Primary sources:**
  - [Wikipedia: Oblique Strategies](https://en.wikipedia.org/wiki/Oblique_Strategies)
  - [More Dark Than Shark archive on Eno methodology](https://www.moredarkthanshark.org)
  - [Brian Eno on Oblique Strategies (interview compilations)](https://en.wikipedia.org/wiki/Oblique_Strategies) (search variants)
  - Cross-reference Bowie Berlin Trilogy sources for documented in-session use
- **Aesthetic-stack relevance:** Talking Heads, David Bowie, methodology-as-craft
- **Suggested tags:** `oblique-strategies`, `eno`, `studio-as-instrument`, `methodology`, `constraint`, `compositional-discovery`

---

#### 22. `ry-cooder-slide-guitar-and-coodercaster`

- **Title:** Ry Cooder Slide Guitar and the Coodercaster
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - The Coodercaster: '60s Stratocaster body, wider C-shaped neck, Teisco neck pickup (from Lindley), Valco lap-steel pickup in bridge
  - Bottleneck slide weight philosophy ("thick enough to drag, not so much that it slows down")
  - Open tuning preferences (open G: D-G-D-G-B-D; open D; open E)
  - "Sound different from the record" live ethos
  - Flatwound strings on the '67 Strat for Curtis-Mayfield-like warmth
  - The instrument-as-personal-design parallel with mk.gee
- **Primary sources:**
  - [Premier Guitar: "Ry Cooder: American Reverence"](https://www.premierguitar.com/articles/27236-ry-cooder-american-reverence)
  - [Guitar Player: "It's Okay to Sound Different from the Record"](https://www.guitarplayer.com/players/its-okay-to-sound-different-from-the-record-ry-cooder-reveals-his-stage-and-studio-secrets)
  - [Jas Obrecht: "Slide Guitar Masters With Ry Cooder"](https://jasobrecht.substack.com/p/listening-to-slide-guitar-masters)
  - [qp-slide.com: "History and characteristics of Coodercaster guitar"](https://qp-slide.com/en/history-characteristics-guitar-coodercaster/)
  - [Fretboard Journal: "Ry Cooder Photo Outtakes"](https://www.fretboardjournal.com/features/behind-scenes-ry-cooder-photo-outtakes/)
  - [YouTube: "Ry Cooder — History of his Coodercasters Guitars"](https://www.youtube.com/watch?v=S_uM4ykZ2hg)
- **Aesthetic-stack relevance:** Ry Cooder, slide guitar lineage, instrument-design philosophy
- **Suggested tags:** `ry-cooder`, `coodercaster`, `slide-guitar`, `open-tunings`, `bottleneck`, `flatwounds`, `instrument-design`

---

#### 23. `open-tunings-and-slide-guitar`

- **Title:** Open Tunings and Slide-Guitar Technique
- **Scope:** technique
- **Folder:** `techniques`
- **Subtopics:**
  - The three workhorse open tunings (open G, open D, open E)
  - Why open G favors slide vs. open D for fingerstyle
  - Slide weight and string-gauge interaction
  - Vibrato as the difference between novice and intermediate slide
  - The Robert Johnson → Ry Cooder → Derek Trucks → Bonnie Raitt lineage
  - Bottleneck vs. metal slide tonal differences
  - Slide on electric vs. acoustic (resonator) vs. lap steel
- **Primary sources:**
  - Premier Guitar slide-guitar lesson archive (search "open tuning slide")
  - [Acoustic Guitar magazine archive](https://acousticguitar.com) (search slide technique)
  - [Ry Cooder source set (row #22) doubles here](https://qp-slide.com/en/history-characteristics-guitar-coodercaster/)
  - Search "Derek Trucks slide guitar interview" + "Bonnie Raitt slide technique"
- **Aesthetic-stack relevance:** Ry Cooder, Billy Strings (slide variants in bluegrass), blues lineage
- **Suggested tags:** `slide-guitar`, `open-tunings`, `bottleneck`, `vibrato`, `lineage`, `technique`

---

#### 24. ~~`radiohead-kid-a-production`~~ — **DEPRECATED**

Album-anchored treatment in `ALBUMS-PROMPTS.md` row #7 (`radiohead-kid-a`). Do not execute as an artist file.

---

#### 25. `radiohead-in-rainbows-production`

- **Title:** Radiohead *In Rainbows* Production
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - The Stent → Godrich production transition mid-album
  - The 24-channel Audiotronix Motown-era console
  - "Bodysnatchers" guitar direct into console for natural distortion
  - The back-to-band ethos after *Hail to the Thief*
  - The pay-what-you-want release context shaping production timeline
  - Specific track-level production decisions ("Reckoner," "House of Cards")
- **Primary sources:**
  - [Happy Mag: "Engineering the Sound: Radiohead's *In Rainbows*"](https://happymag.tv/engineering-the-sound-radioheads-in-rainbows/)
  - [Wikipedia: Nigel Godrich](https://en.wikipedia.org/wiki/Nigel_Godrich)
  - [Nigel Godrich Producer Tumblr archive](https://nigelgodrichproducer.tumblr.com)
  - Search SOS for "In Rainbows" or "Audiotronix console"
- **Aesthetic-stack relevance:** Radiohead, art-rock production
- **Suggested tags:** `radiohead`, `in-rainbows`, `godrich`, `audiotronix`, `console-distortion`, `2007`

---

#### 26. `nigel-godrich-engineering-method`

- **Title:** Nigel Godrich Engineering Method
- **Scope:** artist-anchored (producer-as-anchor)
- **Folder:** `artists`
- **Subtopics:**
  - Godrich's career arc (Radiohead → Beck → McCartney → U2 → Atoms for Peace)
  - "From the Basement" series production approach
  - Beck *Sea Change* and *Mutations* — orchestral-folk-as-engineering
  - The relationship with Yorke beyond Radiohead (The Smile, Atoms for Peace)
  - Studio choices (RAK, Ocean Way, his own setups)
  - Godrich's preference for analogue summing + ITB hybrid
- **Primary sources:**
  - [Wikipedia: Nigel Godrich](https://en.wikipedia.org/wiki/Nigel_Godrich)
  - [Nigel Godrich Producer Tumblr archive](https://nigelgodrichproducer.tumblr.com)
  - [Happy Mag In Rainbows feature](https://happymag.tv/engineering-the-sound-radioheads-in-rainbows/)
  - Search Tape Op + Sound on Sound for "Nigel Godrich"
- **Aesthetic-stack relevance:** Radiohead, Beck, producer-as-collaborator lineage
- **Suggested tags:** `godrich`, `producer`, `radiohead`, `beck`, `from-the-basement`, `analog-ITB-hybrid`

---

#### 27. `sufjan-stevens-age-of-adz-production`

- **Title:** Sufjan Stevens *The Age of Adz* Production
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - The shift from *Illinois* orchestral-folk to electronic experimentalism
  - "Mutating sounds through effects pedals" — Sufjan's quote on the method
  - "Impossible Soul" 25-minute structure
  - Auto-Tune as creative-tool use (linking to the corpus's Auto-Tune-as-creative-tool technique file)
  - The Royal Robertson outsider-art conceptual frame
  - How *Carrie & Lowell* later inverted this maximalism
- **Primary sources:**
  - [The Quietus: "Adz And It Shall Be Given Unto You"](https://thequietus.com/interviews/the-age-of-adz-sufjan-stevens-interview/)
  - [Tape Op: *The Age of Adz* review](https://tapeop.com/reviews/music/80/the-age-of-adz-by-sufjan-stevens)
  - [HuffPost: "Adz and Ends" interview](https://www.huffpost.com/entry/adz-and-ends-an-interview_b_906944)
  - [Paste Magazine review](https://www.pastemagazine.com/music/sufjan-stevens/sufjan-stevens-the-age-of-adz-review)
  - [Wikipedia: The Age of Adz](https://en.wikipedia.org/wiki/The_Age_of_Adz)
- **Aesthetic-stack relevance:** Sufjan Stevens, orchestral-electronic-folk hybrid
- **Suggested tags:** `sufjan-stevens`, `age-of-adz`, `electronic-folk`, `auto-tune-creative`, `royal-robertson`, `2010`

---

#### 28. `dijon-absolutely-production`

- **Title:** Dijon *Absolutely* Production
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - Home + upstate-NY recording (2020 sessions)
  - AKG C414 omni-pattern vocal mic, hot-input-no-clipping
  - Elektron Octatrack loaded with breakbeats; Eurorack skiff; Ableton workflow
  - Mike Gordon (mk.gee) as core collaborator
  - "Songwriting and recording happened simultaneously" methodology
  - The R&B/Americana/soul fusion as anti-pop-polish
- **Primary sources:**
  - [Reverb News: "Dijon Talks Absolutely and His Omnidirectional Process"](https://reverb.com/news/dijon-interview)
  - [The FADER: Dijon Absolutely interview podcast](https://www.thefader.com/2021/11/16/dijon-fader-interview-podcast-absolutely)
  - [Olivia Powell Substack: "Dijon and Mk.gee's Intuitive Groove"](https://oliviapowell.substack.com/p/dijon-and-mkgees-intuitive-groove)
  - [Toni Truale: "Dijon, Mk.gee, and the Third Party Called Pop"](https://www.tonitruale.com/post/dijon-mk-gee-and-the-third-party-called-pop)
  - [The FADER's 2025 Guide to Dijon](https://www.thefader.com/2025/08/18/guide-to-dijon-discography-abhi-dijon-collaborations)
- **Aesthetic-stack relevance:** Dijon, mk.gee axis, R&B-folk fusion
- **Suggested tags:** `dijon`, `absolutely`, `akg-c414`, `octatrack`, `mk-gee`, `r-and-b-folk-fusion`, `home-recording`

---

### Cluster D — Secondary-to-Anchor Promotion (16 prompts: 29–44)

These prompts cover the 14 anchors promoted from secondary-reference tier per user decision (with Big Thief/Lenker and Geese/Winter each splitting into 2 files). Two are **deprecated** (33 Postal Service, 43 NMH) because the albums corpus handles them.

---

#### 29. `big-thief-nomadic-recording`

- **Title:** Big Thief Nomadic Recording (*Dragon New Warm Mountain*)
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - Five-location sessions: upstate NY, Topanga, Telluride, Tucson
  - James Krivchenia as drummer-producer
  - Sam Owens engineering; four-track-on-car-battery "Certainty" tracking
  - 20-song double-album format
  - The Bon Iver–adjacent intimate-folk-band production lineage
- **Primary sources:**
  - [Wikipedia: Dragon New Warm Mountain I Believe in You](https://en.wikipedia.org/wiki/Dragon_New_Warm_Mountain_I_Believe_in_You)
  - [NPR: Big Thief talks new album](https://www.npr.org/2022/02/18/1081872142/big-thief-talks-new-20-song-album)
  - [UNCUT: "We need each other to survive"](https://www.uncut.co.uk/features/interviews/big-thief-interview-dragon-new-warm-mountain-i-believe-in-you-album-136196/)
  - [Brooklyn Vegan album feature](https://www.brooklynvegan.com/big-thiefs-dragon-new-warm-mountain-i-believe-in-you-is-their-most-sprawling-many-sided-lp-yet/)
- **Aesthetic-stack relevance:** Big Thief, intimate-folk-band, nomadic recording
- **Suggested tags:** `big-thief`, `krivchenia`, `sam-owens`, `nomadic-recording`, `four-track`, `2022`

---

#### 30. `adrianne-lenker-intimate-folk`

- **Title:** Adrianne Lenker Intimate-Folk Solo Recording
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - The home-recording lineage (*abysskiss*, *songs*, *instrumentals*, *Bright Future*)
  - Live-to-tape philosophy
  - Phil Weinrobe collaboration on *Bright Future*
  - The Bon Iver / Elliott Smith intimate-vocal lineage
  - Acoustic-guitar mic placement (close-condenser + room mic combos)
  - Vocal-and-guitar-in-one-take vs. overdubbed approaches
- **Primary sources:**
  - Search Pitchfork, Fader, NPR for "Adrianne Lenker home recording"
  - [Wikipedia: Adrianne Lenker discography](https://en.wikipedia.org/wiki/Adrianne_Lenker)
  - Search Tape Op for Phil Weinrobe interview
  - Cross-reference Big Thief sources where Lenker speaks on solo aesthetic
- **Aesthetic-stack relevance:** Lenker solo, intimate folk, home-recording
- **Suggested tags:** `adrianne-lenker`, `solo`, `home-recording`, `bright-future`, `weinrobe`, `intimate-folk`

---

#### 31. `car-seat-headrest-bedroom-to-band`

- **Title:** Car Seat Headrest — Bedroom-to-Band Evolution
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - Will Toledo's Bandcamp era (12 self-released albums before Matador signing)
  - The *Twin Fantasy* re-recording (2011 lo-fi → 2018 elaborate-band)
  - Tracking at Soundhouse Seattle + Adam Stilson at Decade Music Chicago for vocals
  - The "clean and accessible, dense and interesting" production goal
  - Multi-section song-as-suite structure ("Beach Life-In-Death," etc.)
  - Toledo's home-mixing-with-vintage-console workflow
- **Primary sources:**
  - [Tape Op: Will Toledo DIY journey](https://tapeop.com/interviews/bonus/will-toledo-car-seat-headrest)
  - [Rolling Stone: "Why He Needed to Remake Twin Fantasy"](https://www.rollingstone.com/music/music-features/inside-car-seat-headrests-new-old-fantasy-200496/)
  - [Wikipedia: Twin Fantasy (Face to Face)](https://en.wikipedia.org/wiki/Twin_Fantasy_(Face_to_Face))
  - [American Songwriter: Twin Fantasy feature](https://americansongwriter.com/car-seat-headrest/car-seat-headrest-twin-fantasy)
- **Aesthetic-stack relevance:** Car Seat Headrest, bedroom-to-band arc, lo-fi-to-elaborate
- **Suggested tags:** `car-seat-headrest`, `toledo`, `twin-fantasy`, `bedroom-pop`, `re-recording`, `bandcamp-era`

---

#### 32. `black-country-new-road-ants-from-up-there`

- **Title:** Black Country, New Road *Ants From Up There* Production
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - Sergio Maschetzko (live engineer, first time in studio) as producer
  - Three-week tracking at Chale Abbey Studios
  - "Capture our material in a live setting" methodology
  - 7-piece-band live-tracking with chamber-folk arrangement
  - The Isaac Wood vocal era and subsequent line-up shift
  - Cross-link to Punch Brothers anchor for chamber-folk parallels
- **Primary sources:**
  - [Wikipedia: Ants from Up There](https://en.wikipedia.org/wiki/Ants_from_Up_There)
  - [Northern Transmissions: BCNR on *Forever Howlong*](https://northerntransmissions.com/black-country-new-road-are-having-fun-with-new-sounds-on-forever-howlong/)
  - [YouTube: "How Black Country, New Road made *Ants from Up There*"](https://www.youtube.com/watch?v=d7Dz0PkscdY)
  - [Wonderland Magazine: BCNR feature](https://www.wonderlandmagazine.com/2025/04/22/wonderland-meets-black-country-new-road/)
- **Aesthetic-stack relevance:** BCNR, chamber-folk, live-tracking, Punch-Brothers-adjacent
- **Suggested tags:** `bcnr`, `maschetzko`, `ants-from-up-there`, `chamber-folk`, `live-tracking`, `chale-abbey`

---

#### 33. ~~`postal-service-give-up-mail-collaboration`~~ — **DEPRECATED**

Album-anchored treatment in `ALBUMS-PROMPTS.md` row #88 (`postal-service-give-up`). Do not execute as an artist file.

---

#### 34. `andrew-bird-loop-violin-arrangement`

- **Title:** Andrew Bird — Loop-Violin Live Arrangement
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - Pluck-violin loop → bow-over-pluck → whistle-into-Line-6 architecture
  - Line 6 looper pedal as the central instrument
  - Analog octave pedal for cello/bass sounds
  - Custom percussive-imbura-like filtered pedals
  - "Cultivated precariousness" stated philosophy
  - The classical-violinist-as-folk-songwriter cross-training
- **Primary sources:**
  - [TechCrunch: "Andrew Bird And The Concept Of Cultivated Precariousness"](https://techcrunch.com/2012/03/06/interview-andrew-bird-and-the-concept-of-cultivated-precariousness/)
  - [Relix: Andrew Bird interview](https://relix.com/articles/detail/interview-andrew-bird/)
  - [Newport Festivals: "Using the Violin as a Songwriting Tool"](https://newportfestivals.org/sessions/andrew-bird)
  - [WFMT: "How Classical Music Shaped His Sound"](https://www.wfmt.com/2019/07/10/fretless-and-linear-how-classical-violin-shaped-andrew-birds-sound/)
  - [Strings Magazine: *Inside Problems* feature](https://stringsmagazine.com/andrew-bird-surveys-the-nature-of-things-on-inside-problems/)
- **Aesthetic-stack relevance:** Andrew Bird, loop-violin, virtuosity
- **Suggested tags:** `andrew-bird`, `loop-violin`, `whistling`, `line-6`, `live-looping`, `virtuosity`

---

#### 35. `father-john-misty-jonathan-wilson-lush-folk`

- **Title:** Father John Misty + Jonathan Wilson Production Collaboration
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - Jonathan Wilson as producer across *Honeybear*, *Pure Comedy*, *God's Favorite Customer*
  - Phil Ek mix on *Honeybear*; mastered at Sterling Sound
  - "Let me do what I do and explore" workflow
  - Joshua Tree hallucination origin of *Honeybear*'s sound
  - Laurel Canyon revival aesthetics (cross-link to Warren Zevon anchor)
  - Tillman vocal recording approach
- **Primary sources:**
  - [Reverb News: "Jonathan Wilson on Producing Father John Misty"](https://reverb.com/news/interview-jonathan-wilson-on-producing-father-john-misty-conor-oberst-and-himself)
  - [Billboard: Wilson on Pure Comedy collaboration](https://www.billboard.com/music/rock/jonathan-wilson-father-john-misty-pure-comedy-7777039/)
  - [Wikipedia: I Love You, Honeybear](https://en.wikipedia.org/wiki/I_Love_You,_Honeybear)
  - [Clash Magazine review](https://www.clashmusic.com/reviews/father-john-misty-i-love-you-honeybear-2/)
  - [Aquarium Drunkard review](https://aquariumdrunkard.com/2015/02/11/father-john-misty-i-love-you-honeybear/)
- **Aesthetic-stack relevance:** Father John Misty, Jonathan Wilson, Laurel-Canyon-revival folk
- **Suggested tags:** `father-john-misty`, `tillman`, `jonathan-wilson`, `phil-ek`, `lush-folk`, `laurel-canyon-revival`

---

#### 36. `cameron-winter-heavy-metal-guitar-center-album`

- **Title:** Cameron Winter — *Heavy Metal* Solo Production
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - Loren Humphrey production (Arctic Monkeys, Willie J Healey, Tame Impala lineage)
  - Recording across Guitar Center stores in NY using in-store equipment
  - Deliberate avoidance of drums and electric guitar (anti-Geese choices)
  - "More impressionistic than Geese material" stated goal
  - The 18-month-long creative process
  - Pitchfork's #3 album of 2025 reception
- **Primary sources:**
  - [NME: Cameron Winter interview](https://www.nme.com/news/music/geese-cameron-winter-interview-solo-album-heavy-metal-tom-waits-bob-dylan-3807498)
  - [The Face: Cameron Winter interview](https://theface.com/music/cameron-winter-interview-geese-getting-killed-heavy-metal)
  - [The Line of Best Fit: "Not Kidding This Time"](https://www.thelineofbestfit.com/features/interviews/cameron-winter-not-kidding-this-time)
  - [Stereogum: Airport interview previewing "Warning"](https://stereogum.com/2488636/cameron-winter-previews-warning-talks-geese-and-the-indie-complex-in-impromptu-airport-interview/news)
  - [Wikipedia: Heavy Metal (album)](https://en.wikipedia.org/wiki/Heavy_Metal_(album))
- **Aesthetic-stack relevance:** Cameron Winter, anti-rock-band aesthetic, guitar-center-as-studio
- **Suggested tags:** `cameron-winter`, `heavy-metal`, `loren-humphrey`, `guitar-center-recording`, `solo-album`, `2024`

---

#### 37. `geese-band-context`

- **Title:** Geese — NYC Art-Rock Band Context (Companion to #36)
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - The Brooklyn high-school-band origin
  - *Projector* (2021) and *3D Country* (2023) production
  - Cameron Winter as frontman within the band context
  - The "indie complex" framing (per Stereogum interview)
  - Cross-link to #36 Cameron Winter solo file
- **Primary sources:**
  - [Wikipedia: Geese (band)](https://en.wikipedia.org/wiki/Geese_(band))
  - [Stereogum interview](https://stereogum.com/2488636/cameron-winter-previews-warning-talks-geese-and-the-indie-complex-in-impromptu-airport-interview/news)
  - Search Pitchfork + Stereogum for "Geese 3D Country" or "Geese Projector"
  - Cross-reference Cameron Winter sources from row #36
- **Aesthetic-stack relevance:** Geese, NYC art-rock, indie-rock-revival
- **Suggested tags:** `geese`, `cameron-winter`, `3d-country`, `projector`, `nyc-art-rock`, `band-context`

---

#### 38. `vulfpeck-jack-stratton-minimalist-funk`

- **Title:** Vulfpeck / Jack Stratton — Minimalist Funk Production
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - "Play tight, leave space, and make it feel alive" philosophy
  - The "hit session" methodology (show up, learn the tune, record same day)
  - Willie Mitchell + Geoff Emerick references as analog-emulation targets
  - Light-footprint plugin-and-DAW mixing
  - The self-released "Sleepify" Spotify-exploit business gambit
  - Vulfpeck → Vulf Records → Theo Katzman / Cory Wong / Joey Dosik lineage
- **Primary sources:**
  - [The Believer: "An Interview with Jack Stratton"](https://www.thebeliever.net/an-interview-with-jack-stratton/)
  - [Third Story Podcast: Jack Stratton interview](http://www.third-story.com/listen/jackstratton)
  - [Stanford Daily: Vulfpeck production interview](https://stanforddaily.com/2016/12/08/jack-stratton-vulfpeck-interview/)
  - [Medium: "How Jack Stratton Hacked the Music Industry"](https://medium.com/the-balanced-sheet/jack-stratton-and-the-vulfpeck-model-00813f3ac8bf)
  - [Medium (Jazzism translated): Interview with Jack Stratton](https://medium.com/@RobertJon/vulfpeck-from-jazzism-magazine-488ac32acfaf)
- **Aesthetic-stack relevance:** Vulfpeck, minimalist funk, pocket, groove
- **Suggested tags:** `vulfpeck`, `stratton`, `minimalist-funk`, `pocket`, `groove`, `hit-session`, `vulf-records`

---

#### 39. `animal-collective-merriweather-ben-allen`

- **Title:** Animal Collective — *Merriweather Post Pavilion* Production
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - Ben Allen (Gnarls Barkley) brought in for low-end expertise
  - Sweet Tea Studios, Oxford Mississippi — month-long isolated session
  - "No phones, no computers" environment
  - The vocal-burial-vs-vocal-push compromise
  - "My Girls" production
  - Why this album defined late-2000s indie-experimental pop
- **Primary sources:**
  - [Sound on Sound: "Animal Collective: Recording Merriweather Post Pavilion"](https://www.soundonsound.com/people/animal-collective-recording-merriweather-post-pavilion)
  - [Baltimore Sun (City Paper): Ben H. Allen interview](https://www.baltimoresun.com/citypaper/bcp-blog-913-20090115-story.html)
  - [Happy Mag: "Engineering the Sound"](https://happymag.tv/engineering-the-sound-animal-collectives-merriweather-post-pavilion/)
  - [LA Record: Animal Collective interview](https://larecord.com/interviews/2009/05/29/animal-collective-interview-be-prepared-to-be-told-you-suck)
  - [Wikipedia: Merriweather Post Pavilion (album)](https://en.wikipedia.org/wiki/Merriweather_Post_Pavilion_(album))
- **Aesthetic-stack relevance:** Animal Collective, experimental-pop, low-end production
- **Suggested tags:** `animal-collective`, `ben-allen`, `merriweather`, `sweet-tea-studios`, `experimental-pop`, `low-end`

---

#### 40. `mark-knopfler-fingerstyle-clean-tone`

- **Title:** Mark Knopfler / Dire Straits — Fingerstyle and Clean Tone
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - Pickless attack — anchored right pinky + ring finger
  - The Strat 5-way switch lineage from Knopfler's playing
  - Clean-tone-as-Knopfler-signature (anti-distortion ethos)
  - "Plugged it in and started fiddling with the knobs" anti-mythologizing
  - The Sultans of Swing → Brothers in Arms arc
  - Why mk.gee inherits from + reacts against this tone tradition
- **Primary sources:**
  - [Premier Guitar: "Mark Knopfler's Fingerstyle Finesse"](https://www.premierguitar.com/lessons/intermediate/mark-knopflers-fingerstyle-finesse)
  - [Guitar World: "Knopfler on Making Brothers In Arms"](https://www.guitarworld.com/artists/guitarists/mark-knopfler-brothers-in-arms-40th-anniversary)
  - [Guitar Player: "Why He Ditched the Pick"](https://www.guitarplayer.com/players/mark-knopfler-tells-why-he-ditched-his-pick)
  - [MusicRadar: "How do you get that sound?"](https://www.musicradar.com/news/mark-knopfler-dire-straits-guitars)
  - [ds.mk-guitar.com: Knopfler interview archive](http://ds.mk-guitar.com/knopfler-interviews.htm)
- **Aesthetic-stack relevance:** Knopfler, fingerstyle, clean tone, mk.gee context
- **Suggested tags:** `knopfler`, `dire-straits`, `fingerstyle`, `clean-tone`, `strat`, `pickless`, `mk-gee-context`

---

#### 41. `warren-zevon-jackson-browne-waddy-wachtel`

- **Title:** Warren Zevon — Jackson Browne + Waddy Wachtel Co-Production
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - *Excitable Boy* (1978) Browne + Wachtel co-production
  - "Werewolves of London" rhythm-section saga (seven bands tried before Fleetwood + McVie locked it)
  - The "Apocalypse Now" production analogy (Wachtel's framing)
  - LA-rock-meets-sardonic-lyric production aesthetic
  - The Wachtel-as-arranger role across multiple Zevon records
- **Primary sources:**
  - [Guitar Player: Waddy Wachtel on his Zevon '70s adventures](https://www.guitarplayer.com/guitarists/next-thing-i-know-ive-got-the-everly-brothers-sitting-in-my-hotel-room-waddy-wachtel-on-his-1970s-adventures-with-warren-zevon-from-robert-johnsons-licks-to-werewolves-of-london)
  - [Waddy Wachtel Info: Excitable Boy page](http://waddywachtelinfo.com/WarrenZevon2.html)
  - [Times Georgian: "Excitable Boy is Zevon's zenith"](https://www.times-georgian.com/times_georgian/excitable-boy-is-zevons-zenith/article_9a3beb34-5466-5374-b783-08751fc4dfec.html)
  - [Stereophile: Werewolf on Mobile Fidelity reissue](https://www.stereophile.com/content/warren-zevon-werewolf-mobile-fidelity)
  - [Wikipedia: Warren Zevon (album)](https://en.wikipedia.org/wiki/Warren_Zevon_(album))
- **Aesthetic-stack relevance:** Warren Zevon, LA-rock, commitment-discipline production
- **Suggested tags:** `warren-zevon`, `jackson-browne`, `waddy-wachtel`, `la-rock`, `excitable-boy`, `1978`

---

#### 42. `john-prine-dave-cobb-rca-studio-a`

- **Title:** John Prine — Dave Cobb Production at RCA Studio A
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - *The Tree of Forgiveness* (2018) — Prine's final studio album
  - Dave Cobb production at RCA Studio A, Nashville
  - Sparse acoustic arrangements emphasizing weathered baritone
  - "Caravan of Fools" co-write with Dan Auerbach + Pat McLaughlin
  - The Cobb-Nashville-revival production lineage (Sturgill, Stapleton, et al.)
  - American songcraft canonical reference
- **Primary sources:**
  - [Salvation South: Prine + Cobb interview](https://www.salvationsouth.com/under-the-tree-of-forgiveness-john-prine-dave-cobb-interview/)
  - [Uproxx: Tree of Forgiveness interview](https://uproxx.com/music/john-prine-tree-of-forgiveness-interview/)
  - [Rolling Stone: "Fresh Revelations" review](https://www.rollingstone.com/music/music-album-reviews/review-john-prine-keeps-finding-fresh-revelations-on-tree-of-forgiveness-628390/)
  - [JohnPrine.com: "John Prine Returns to Songwriting"](https://yougotgold.johnprine.com/press/john-prine-returns-to-songwriting-jaunty-and-dark-on-the-tree-of-forgiveness-)
- **Aesthetic-stack relevance:** John Prine, Dave Cobb, Nashville-revival, songwriting
- **Suggested tags:** `john-prine`, `dave-cobb`, `rca-studio-a`, `nashville`, `songwriting`, `sparse-acoustic`

---

#### 43. ~~`neutral-milk-hotel-aeroplane-lo-fi`~~ — **DEPRECATED**

Album-anchored treatment in `ALBUMS-PROMPTS.md` row #89 (`neutral-milk-hotel-aeroplane`). Do not execute as an artist file.

---

#### 44. `david-bowie-berlin-trilogy-visconti-eno`

- **Title:** David Bowie — Berlin Trilogy Production (Visconti + Eno)
- **Scope:** artist-anchored
- **Folder:** `artists`
- **Subtopics:**
  - The trilogy: *Low* (1977), *"Heroes"* (1977), *Lodger* (1979)
  - Bowie + Visconti co-production; Eno as collaborator, NOT producer
  - Eno's EMS Synthi A portable synth for spacey textures
  - Visconti's Eventide Harmonizer on drums
  - "There were no songs on the table" — studio-as-composition methodology
  - The lineage to Talking Heads *Remain in Light* (year after)
  - Cross-link to row #21 (Oblique Strategies) and row #20 (Byrne)
- **Primary sources:**
  - [Sound on Sound: "Classic Tracks: David Bowie 'Heroes'"](https://www.soundonsound.com/techniques/classic-tracks-david-bowie-heroes)
  - [Mix Online: "Producing David Bowie's Landmark Berlin Trilogy"](https://www.mixonline.com/recording/producing-david-bowies-landmark-berlin-trilogy)
  - [Performing Songwriter: Tony Visconti interview](https://performingsongwriter.com/tony-visconti/)
  - [Louder: "Poor Iggy became a guinea pig"](https://www.loudersound.com/features/bowie-berlin-trilogy-low-heroes)
  - [The Bowie Bible: Low](https://www.bowiebible.com/albums/low/)
  - [Ultimate Classic Rock: "How Bowie Fashioned the Berlin Trilogy"](https://ultimateclassicrock.com/david-bowie-berlin-trilogy/)
  - [More Dark Than Shark: Brian Eno MOJO Nov 2017 (Berlin context)](https://www.moredarkthanshark.org/eno_int_mojo-nov17b.html)
- **Aesthetic-stack relevance:** Bowie, Visconti, Eno, art-rock, studio-as-composition
- **Suggested tags:** `bowie`, `visconti`, `eno`, `berlin-trilogy`, `low`, `heroes`, `ems-synthi-a`, `eventide-harmonizer`

---

## Suggested batch organization

13 batches total. See `AESTHETIC-SESSIONS.md` for actual kickoff messages.

| Batch | Prompts | Files | Folder | Notes |
|---|---|---|---|---|
| A1 — Bon Iver + LCD | 1, 2, 3, 4 | 4 | `artists/` | Original batch |
| A2 — LCD adjacents + Charli | 5, 6, 7 | 3 | `artists/` | Original batch — note: prompt #7 (charli-xcx-brat-production) overlaps with albums batch AL11 row #51. See A2 kickoff for guidance. |
| A3 — mk.gee + Bluegrass | 8, 9, 10 | 3 | `artists/` | Original batch |
| A4 — Talking Heads cluster | 20, 21 | 2 | `artists/`, `techniques/` | Prompt #19 deprecated (handled by albums AL1) |
| A5 — Ry Cooder + Radiohead cluster | 22, 23, 25, 26 | 4 | `artists/`, `techniques/` | Prompt #24 deprecated (handled by albums AL2) |
| A6 — Sufjan + Dijon | 27, 28 | 2 | `artists/` | |
| A7 — Big Thief + CSH + BCNR | 29, 30, 31, 32 | 4 | `artists/` | Big Thief and Lenker split into 2 files |
| A8 — Andrew Bird + FJM | 34, 35 | 2 | `artists/` | Prompt #33 deprecated (handled by albums AL18) |
| A9 — Cameron Winter + Geese + Vulfpeck + AC | 36, 37, 38, 39 | 4 | `artists/` | Geese + Cameron Winter split into 2 files |
| A10 — Knopfler + Zevon + Prine + Bowie | 40, 41, 42, 44 | 4 | `artists/` | Prompt #43 deprecated (handled by albums AL18). A11 merged into A10. |
| T1 — Vocal + Electronic | 11, 12, 13, 14 | 4 | `techniques/` | Original batch |
| T2 — Guitar + Mix + Theory | 15, 16, 17, 18 | 4 | `techniques/` | Original batch |

**Total:** 12 batches, 38 prompts executed (4 deprecated = 26 new actually run + 18 originals + 4 skipped = 44 total numbered).

Phased pacing recommendation (mirrors `AESTHETIC-SESSIONS.md`):
- **Wave 1 (validation):** A1 + A2 + A3 + T1 + T2 (original 5 batches; 18 files, ~30 min wall in parallel)
- **Wave 2 (listening-history expansion):** A4 + A5 + A6 (8 files, ~15 min in parallel)
- **Wave 3 (secondary-promotion expansion):** A7 + A8 + A9 + A10 (14 files, ~20 min in parallel)

Or fire all 12 batches in parallel for ~30 min total wall time.

---

## Post-processing checklist

After each batch completes:

- [ ] Files written to `corpus/artists/` or `corpus/techniques/` per spec
- [ ] Front-matter includes the `Source: Deep-research synthesis (2026-05)` line AND the new `Aesthetic-stack relevance:` field
- [ ] At least 8 H2 body sections per file
- [ ] Inline citations are real URLs from the primary-source list (spot-check 2–3)
- [ ] No fabricated specific gear settings, plugin numbers, or song-attribution claims
- [ ] Tags include both the aesthetic-stack name (e.g., `bon-iver`, `lcd`) AND the technique scope (e.g., `vocal-stacking`, `analog-synths`)
- [ ] (Optional) Update `corpus/README.md` to reflect the new folder structure and file count
