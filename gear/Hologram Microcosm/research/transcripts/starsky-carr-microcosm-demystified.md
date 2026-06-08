https://www.youtube.com/watch?v=42cVBk8tuJw
Starsky Carr · "Hologram Microcosm Demystified: Cinematic to Glitchfest // Walkthrough and Tutorial" · 2022-11-13 · 31:47 · ~31k views

A synth-focused "strip it down so you understand what it's doing" tutorial. Deliberately NOT a pretty demo — Starsky uses a single drum/vocal loop sample fed in via MIDI so each algorithm's mangling is clearly audible. Best framing of the Microcosm as a "probability-driven granular sequencer." Captions auto-generated; cleaned to prose below.

---

## Framing
The Microcosm is like a writing partner in the studio: you can guide it but it always answers in its own way — "predictably unpredictable." It took him a while to like it because he was treating it as a standard delay/reverb, which misses the point. Think of each algorithm as a **probability-driven granular sequencer**: it takes the input, chops it into steps, then plays variations back — pitched, delayed, time-stretched, with reverb and a filter — so it never does the same thing twice (or can be quite repeatable if you know what it's doing). 11 effects x 4 variations = 44 algorithms in four groups: Micro Loop, Granules, Glitch, Multi-Delay.

## The knobs (demonstrated before the algorithms, on a Seq mode)
- **Shape** = envelope on the repeats. Four shapes: a downward ramp (transient pulse), a triangle (builds in and out, smoother), a ramp-up (sounds slightly reversed), and a square (on/off). Big impact on how the repeats sound.
- **Activity** = does something different per algorithm; on the demo Seq it adds filter variation to the repeats (you hear it drifting in and out).
- **Time** = playback speed of the chopped samples — half speed, quarter speed, etc.
- **TIP #1 — feed it MIDI clock (or use tap tempo).** "If you are playing along to something with a loop or with MIDI in any way, do set it up so it accepts the MIDI signal, because these little sequences each algorithm plays have to be in time, otherwise it just goes completely wild." Fine for weird ambient stuff, but generally you want events on/around the beat.
- **Repeats** = number of repeats.
- **Filter** = filters the high end off the affected signal only.
- **Space** = reverb.
- **Secondary (hold Shift) functions:** Space's secondary = reverb time (set a really long one); Shape's secondary = modulation frequency; Repeats' secondary = modulation depth; Filter's secondary = resonance.

- **TIP #2 — set the input level correctly.** Hold **Shift + Phrase Looper** to enter config; the **Mix knob** selects the input level (instrument vs. line). He spent "an embarrassingly long time" thinking the pedal was broken when it was just set to instrument level for a line-level synth — it "just sounds rubbish" when wrong.

## Algorithms (he picks representative ones rather than all 44)
**SEQ (Sequence):** chops the loop and repeats it back various ways.
- A: Activity adds filter variations.
- B: plays some chopped samples back at half speed (an octave lower); bounces between playback speeds; fully clockwise adds a soft sustainer pad underneath.
- C: filter sweeps over the chopped samples; Activity adds layers of samples (empty/spacious at low settings).
- D: adds bit crushing ("gone a bit Aphex Twin / Window Licker"); Activity adds more elements.

**GLIDE:**
- A: glides between half and normal speed; Activity changes the glide time (slower = nicer).
- B/C: glide between normal and double speed; filter sweeps appear.
- D: glides in both directions at once (high→low and low→high) — "beautifully spacey."

**MOSAIC:** chops and replays at various speeds without the glide or sequence behavior; variation comes via filter etc. Activity = number of active loopers (how many things are happening).
- A: octave up. B: same but an octave lower (down) rather than up. C: all at double speed (octave higher). D: fills the whole spectrum — up to two octaves higher plus normal and lower. (He demonstrates by speaking "one two three..." into it so you can hear the octave-stacked repeats clearly.) On odd-length loops it goes pleasantly poly-rhythmic.

**GRANULES / HAZE → TUNNEL:** more grains diffused = more textural; some play double speed, some half. Tunnel B is a sub-octave drone. Tunnel A has an envelope that compresses and lengthens the drone sample length — you can hear it time-stretching/squishing the sample.

**GLITCH (Blocks / Interrupt / Arp):** Blocks rearranges and pitch-shifts; samples filter in and out. Interrupt has bit crushing and heavy manipulation ("it's nasty"); pitch shifting in Interrupt B; the variation/number of glitches is controllable. Arp makes arpeggios out of what you played (clearest on distinct notes / the vocal sample, chopped into sections); C adds random filters per step; D adds bit crushing.

## Notes
- He does NOT cover the Phrase Looper ("never really used it") — he uses the Microcosm purely for the effect textures, full wet, into post.
- Recurring point: different algorithms suit different source material; pick the engine to match the tone you're feeding in.
