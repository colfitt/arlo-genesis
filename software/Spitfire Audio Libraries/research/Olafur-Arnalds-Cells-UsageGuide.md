# Ólafur Arnalds Cells — Usage Guide

The one Ólafur Arnalds library actually **installed** here (`Olafur Arnalds - Cells.component/.vst/.vst3` — Spitfire-app plugin, *not* Kontakt; 29.79 GB). It's a **generative harmonic engine**: hold a note or chord and it spins out evolving "cells" of string + synth that stay locked to your key. In this drone/post-classical rig it's an idea-sparker and a bed-maker — let it generate, **capture the surprise**, then bounce the wall to audio or re-voice the melodies under banjo/baritone into Valhalla/EchoBoy. Companion products (Evolutions, Chamber Evolutions, Composer Toolkit, Stratus) are covered here as **general technique** and to map Ólafur's aesthetic — *they are NOT in this install's CONTENTS.md (Cells only).*

---

## 1. Essential workflows

**The core loop — hold and harvest.** Don't write string lines note-by-note. Hold a note or chord and Cells generates micro-expression "cells" at different intervals that never stray from your harmony. ([cells-musictech](research/links/olafur-cells-musictech-blend-synths-strings.md), [cells-walkthrough](research/transcripts/olafur-cells-walkthrough-edna-soundbed.md))

**Pick a harmony mode (upper-right):**
- **Scale mode** — set a key center + tonality (minor, major-7, sharp-11, dom-7…). On = that note sounds; off = silent. You can deliberately turn *on* out-of-scale notes for tension. Best when you know your key. ([cells-walkthrough](research/transcripts/olafur-cells-walkthrough-edna-soundbed.md), [spitfire-product](research/links/olafur-cells-spitfire-product-page.md))
- **Played mode** — analyzes what you play in real time and adds a degree of randomness to introduce complementary harmonies. More surprising; good for breaking out of a stuck progression. ([cells-musictech](research/links/olafur-cells-musictech-blend-synths-strings.md))

**Velocity drives the intervals (the key mechanic).** How *hard* you hit determines how far the cell reaches up: ~0 = no change, then +2 (2nd), +3 (minor 3rd), +5 (4th), +7 (5th). Soft = unison/calm; harder = wider intervals. Spend a minute dialing velocity sensitivity to your controller. The result is **deterministic per note** — play the same MIDI back and you get the same result, so a recorded take is reproducible. ([cells-walkthrough](research/transcripts/olafur-cells-walkthrough-edna-soundbed.md))

**Capture the output (THE workflow Ólafur intends).** His own words: Cells "constantly surprises me with little melodies that get created within the random intervals, often inspiring new melodies that I then take over to other instruments." So: record the MIDI, lift the fragments you like, and **re-voice them on banjo/baritone/felt-piano**. To keep a generated wall: **bounce to audio** — Spitfire say to bounce saved Cells tracks before updates (Scale-mode intervals can shift across versions), and **Played mode works in offline/non-realtime bounce**, so you can freeze the evolving texture rather than only printing in real time. ([spitfire-product](research/links/olafur-cells-spitfire-product-page.md), [cells-bounce-faq](research/links/olafur-cells-midi-cc-and-bounce-faq.md))

**Articulations evolve live.** Hold notes, switch articulation (e.g. Motion → Cirrus), then add a new note — the old notes keep playing and the vibe shifts underneath. Great for slow morphs without re-triggering. ([cells-walkthrough](research/transcripts/olafur-cells-walkthrough-edna-soundbed.md))

---

## 2. Signature presets & settings

**Recording sources** — strings = **SinfoniaNord** (cello-forward ensemble) recorded at Hof, Akureyri, Iceland; synths = vintage **Korg & Juno**, signal paths curated by Ólafur. ([spitfire-product](research/links/olafur-cells-spitfire-product-page.md))

**Content families to reach for (200+ presets):** ([spitfire-product](research/links/olafur-cells-spitfire-product-page.md))
- **Strings / Full Band** — Cells Motion Clouds; Scatter Cirrus Intensity; Octaves Living Cells (Sparse/Medium); Shimmer (Sparse/Medium); Parallel Motion Shimmer; Full Band with interval options (unison→7ths); glissando/two-note variants.
- **Synth** — Cells 1/2/3 modules; Bass (Long Straight, Long Sparse/Medium); Synth Bass (Sub 60 II, Sub Stab, Short Stab, Short Sub 20); One Shots (Back Stab, Swell 60, Ratatattat, Single Hits).
- **Sound design** — Mallet Pads (Swarm Moving, Soft Organ, Organic/Inorganic Moves, Ps Waves); **Organic Warps** (Air Ensemble, **Granular Strings**, Scattered Bows, String Abstraction/Waves, **Submerged**); **Sonic Warps** (**Bass Drone/Dist**, Ps Pad Filtered, Detuned, **Old Tape** variations) — the warps are the most drone/lo-fi-aligned in the box.

**Mic positions** — Mix 1 / Mix 2 + **FX positions**. The **close condenser** is the special, slightly-sharp one; the **ribbon** rolls off the top (use to tame harshness); **Mix 1** sits you further back with more depth; **FX2** sounds like an old echo/delay machine filtering to the mids (a built-in lo-fi color). ([cells-walkthrough](research/transcripts/olafur-cells-walkthrough-edna-soundbed.md))

**MIDI CC controls** (shared Spitfire-app player): **CC1 = Dynamics** (the main one — moves through dynamic layers), **CC11 = Expression**, **CC21 = Vibrato**, **CC17 = Release** (extend tails for drones), **CC19 = Reverb**. Automate CC1 for swells. ([cells-cc-faq](research/links/olafur-cells-midi-cc-and-bounce-faq.md))

---

## 3. Power-user tips, tricks & hidden features

- **The eDNA engine is the deep rabbit hole.** Select **both** "standard synth" and "synth" or controls grey out. You get an **A and a B section**, each loaded from individual samples (= **two Sound Bays**). A **crossfader** mixes them; the **Oscillate Mixer** (set a multiplier, e.g. 16×) slowly morphs between A and B for hands-off evolution; vertical sliders set each source's feed; each bay has its own FX. There's also a **gate sequencer** for rhythmic patterns. ([cells-musictech](research/links/olafur-cells-musictech-blend-synths-strings.md), [cells-walkthrough](research/transcripts/olafur-cells-walkthrough-edna-soundbed.md))
- **Out-of-scale toggle = tension.** Add chromatic notes outside the key for the "queasy" edge — pairs well with playing harder (wider intervals). ([cells-musictech](research/links/olafur-cells-musictech-blend-synths-strings.md))
- **The basses are a hidden gem.** Bass / contrabass / synth bass — "haunting" on studio speakers (won't translate on phone). Solo player centered in the room. Good standalone drone source. ([cells-walkthrough](research/transcripts/olafur-cells-walkthrough-edna-soundbed.md))
- **Character is fixed-but-broad.** Everything is warm/calm/embracing — even "tension" is a warm fuzzy tension. It does happy/wonder/amazement, not aggression. Don't fight it; lean into it as a *bed*, push aggression elsewhere (pedals, RC-20, Decapitator).
- **Deterministic = editable.** Because output repeats per note, you can comp/edit the MIDI to "compose" the generative result, not just gamble on it.

---

## 4. Notable users & techniques (Ólafur's aesthetic, sourced)

**Sound-as-decision philosophy.** "Why play this piano instead of that piano? … why this mic and not that mic?" He treats "all sound design as much as melodies." ([characterful-interview](research/links/olafur-musictech-characterful-sound-interview.md))

**The felt piano.** A modified **1904 Bechstein grand** felted and sampled ultra-quiet (the room held its breath per note). Captured with **KM84** (tight/crisp), a **Coles ribbon** below the soundboard run through a **Roland Space Echo** for gritty low end, plus a processed blend (KM84 + C12 through Pultec EQ + an 1178 compressor). Productized as the felt grand in the **Composer Toolkit**. ([characterful-interview](research/links/olafur-musictech-characterful-sound-interview.md), [composer-toolkit-walkthrough](research/transcripts/olafur-composer-toolkit-walkthrough.md))

**String tone at the source, not in EQ.** **Sul tasto** (bow over the neck) for a hollow, harmonic tone; lower registers (violin G-string, viola C-string) so you carve less in the mix; **KM84** + original **AKG C12** mics. The Evolutions/Cells "sul tasto" articulations come straight from this. ([characterful-interview](research/links/olafur-musictech-characterful-sound-interview.md))

**Synths + outboard.** Primary synth = **Korg PS-3100**; secondary = **Roland Juno** (leads/sub). **Roland Space Echo** for vitality, **Studer** console for hands-on feedback routing, **tape** for effects and "a little instability" on solo piano. ([characterful-interview](research/links/olafur-musictech-characterful-sound-interview.md))

**Stratus — the generative engine behind it all.** Two self-playing "ghost" pianos: he plays one chord, software manipulates it via **Euclidean rhythms** + randomness and sends rhythmic textures to two pianos; a **randomness slider** pushes notes to upper/lower octaves. "It always plays something different. It's never the same twice." Built with programmer **Halldór Eldjárn** over ~2 years (first heard on 'Doria', 2016) to beat writer's block — "technology … needs to serve a purpose, spark ideas and have a function." He even routes Stratus's generative MIDI into the **Korg PS-3100** for unique textures. Cells is essentially this idea packaged as a plugin. ([stratus-npr](research/links/olafur-stratus-npr-one-key-many-notes.md), [stratus-meaning](research/links/olafur-stratus-meaning-spitfire-composer.md), [characterful-interview](research/links/olafur-musictech-characterful-sound-interview.md)) *(One origin story — nerve damage to his left hand from a car accident — appears in some outlets but NOT in the NPR/Spitfire sources captured here; flagged unconfirmed.)*

---

## 5. Rig-specific recipes

**Generative bed under banjo (the headline move).** Cells in **Played mode**, soft velocity for unison/2nd cells, a warm string preset (Octaves Living Cells or Motion Clouds) → record a held progression → bounce to audio (offline OK) → that becomes the evolving wall. Play **banjo/baritone as lead** over it into **EchoBoy/Valhalla**. Lift any "surprise melody" Cells throws and double it on the banjo. ([spitfire-product](research/links/olafur-cells-spitfire-product-page.md), [cells-bounce-faq](research/links/olafur-cells-midi-cc-and-bounce-faq.md))

**Degraded post-classical wall.** Start from the **Organic/Sonic Warps** (Granular Strings, Submerged, Old Tape, Bass Drone/Dist) or pick the **FX2** mic for the built-in echo-filtered color, then push it harder downstream: **SketchCassette II** for wow/flutter, **RC-20** for noise/wobble, **Decapitator** for grit → the "recorded-wrong" sustained wall. Cells supplies the *motion*; the FX supply the *damage*.

**eDNA self-morphing drone (hands-off).** Synth mode → load a string-ish A and a synth B into the two Sound Bays → **Oscillate Mixer** at a slow multiplier so it crossfades A↔B forever → hold a chord, automate **CC17 (Release)** up for long tails and **CC1 (Dynamics)** for slow swells → into Valhalla Room/VintageVerb on a long decay. ([cells-walkthrough](research/transcripts/olafur-cells-walkthrough-edna-soundbed.md))

**Re-voice to hardware.** Because the output is deterministic MIDI-in, you can print the generated cells and resample/route the audio out to the **pedalboard** (reamp) or into **Kontakt** to map as a new sampled instrument — same hardware-front, software-studio path used elsewhere in this rig.

**Logic (AU) note.** Cells loads as the **AU** in Logic. Heavy presets (Full Band, eDNA with FX) are CPU-hungry — **freeze/bounce** once the part is set (offline bounce supported). In **Ableton Live 12 Lite** use it for clip-launch beds but commit to audio early given Lite's limits.

---

## 6. Best learning resources

- **Spitfire's own Cells walkthrough** (Paul Thompson) — the canonical feature tour; referenced inside the Soundbed video as the place that "goes through everything."
- **Soundbed Videos — "Ólafur Arnalds Cells – Walkthrough, eDNA"** ([transcript](research/transcripts/olafur-cells-walkthrough-edna-soundbed.md)) — **best player's-feel deep dive**: velocity→interval mechanic, mic positions, eDNA. 29 min.
- **MusicTech — "How to blend synths and a string orchestra…"** ([link](research/links/olafur-cells-musictech-blend-synths-strings.md)) — clearest written explanation of modes + eDNA Sound Bays.
- **Spitfire walkthroughs for Evolutions** ([transcript](research/transcripts/olafur-evolutions-walkthrough.md)) **& Chamber Evolutions** ([transcript](research/transcripts/olafur-chamber-evolutions-walkthrough.md)) — the Evo Grid, feathering, waves (general technique).
- **Composer Toolkit walkthrough** ([transcript](research/transcripts/olafur-composer-toolkit-walkthrough.md)) — felt grand + warps; closest window into his outboard aesthetic.
- **MusicTech "characterful sound" interview** ([link](research/links/olafur-musictech-characterful-sound-interview.md)) — the gear/technique bible (felt piano, sul tasto, Korg PS-3100, Space Echo, tape).
- **NPR "One Key, Many Notes"** ([link](research/links/olafur-stratus-npr-one-key-many-notes.md)) — Stratus, plainly explained.

---

## 7. Common pitfalls / gotchas

- **It's Cells only here.** Evolutions / Chamber Evolutions / Composer Toolkit / Stratus are **not installed** (not in CONTENTS.md) — treat their sections as technique/aesthetic reference, not owned tools.
- **Not Kontakt.** Runs in the **Spitfire Audio app + dedicated plugin** (AU/VST2/VST3/AAX). Needs the Spitfire app; library lives on the external **PlaySomeGodDamnMusic** drive (mount it first).
- **Bounce before updating.** Saved **Scale-mode intervals can change across versions** — bounce Cells tracks to audio first. ([cells-bounce-faq](research/links/olafur-cells-midi-cc-and-bounce-faq.md))
- **Velocity curve matters.** Cheap/uneven controllers make the interval mechanic unpredictable — set velocity sensitivity deliberately.
- **One aesthetic.** Warm and gentle only; no aggression in the box — bring grit from FX/pedals.
- **CPU.** Full Band + eDNA + multiple mics is heavy in Logic/Ableton; freeze or bounce (offline supported).
- **29.79 GB** download; large sample streaming off the external drive — keep it mounted and ideally on fast storage.

---

## 8. Captured sources

**Transcripts** (`research/transcripts/`):
- `olafur-cells-walkthrough-edna-soundbed.md` — Soundbed Videos, Cells + eDNA deep dive (29:01).
- `olafur-evolutions-walkthrough.md` — Spitfire, original Evolutions Evo Grid (27:07).
- `olafur-chamber-evolutions-walkthrough.md` — Spitfire, Chamber Evolutions: feathering + waves (13:17).
- `olafur-composer-toolkit-walkthrough.md` — Spitfire, felt grand + organic/sonic warps (23:58).

**Links** (`research/links/`):
- `olafur-cells-musictech-blend-synths-strings.md` — MusicTech: modes + eDNA Sound Bays.
- `olafur-cells-spitfire-product-page.md` — official content list, sources, Ólafur's capture quote.
- `olafur-cells-midi-cc-and-bounce-faq.md` — Spitfire CC chart + bounce/offline-Played-mode guidance.
- `olafur-musictech-characterful-sound-interview.md` — felt piano, sul tasto, Korg PS-3100, Space Echo, tape.
- `olafur-stratus-npr-one-key-many-notes.md` — NPR: how Stratus works.
- `olafur-stratus-meaning-spitfire-composer.md` — Spitfire: Stratus development + philosophy.
- `olafur-chamber-evolutions-making-music-review.md` — independent Evo Grid breakdown.

## Sources
All claims trace to the captured files above (each begins with its original URL). Primary: Spitfire Cells product page/FAQ + walkthroughs; MusicTech Cells feature + "characterful sound" interview; NPR + Spitfire Composer on Stratus; Making Music on Chamber Evolutions; Soundbed Videos Cells walkthrough.
