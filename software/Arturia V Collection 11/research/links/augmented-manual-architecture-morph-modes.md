https://dl.arturia.net/products/augmented-strings/manual/augmented-series_Manual_2_0_0_EN.pdf
Arturia (official) · Augmented SERIES User Manual v2.0.0 · n.d. (downloaded & text-extracted locally) — covers STRINGS, VOICES, and all Augmented v2 instruments (identical layout/engine)

THE authoritative architecture + the Morph-mode detail that makes the evolving walls work.

== Engine (shared across Strings & Voices) ==
- "Hybrid synthesizer featuring **four separate sound sources (Engines)**." Each **Layer (A/B) contains two Engines**; each Engine is either a **Sampler** or a **Synth**.
- Each Engine = one of **five types: Analog, Granular, Harmonic, Simpler, Wavetable** (Simpler = lighter sample manipulation; the four "synth" types + the multi-sample Sampler).
- Each Engine has its own VCA / envelope / filter.
- "Blend Layers and modify various parameters using the **Morph Macro**."
- Modulation sources: **2 LFOs, 2 Function generators, 2 Random signal** generators (+ per-engine envelopes + keyboard).
- 8 Macros total: **4 for Sound (Color/Time/Motion/Morph)** + **4 for FX (FX A / FX B / Delay / Reverb)**, all MIDI-mappable.
- Built-in arpeggiator (multiple modes, chords, random); Super Unison; easy MIDI-learn.

== The THREE Morph Modes (the key to controlled walls) ==
Selected by buttons under the Morph knob:
- **Crossover** — equal-power crossfade 100% Layer A → 100% Layer B over the knob travel.
- **Additive** — Layer A stays at level; Layer B is gradually *added* on top over the travel (→ thicker as you morph = good for swelling a wall).
- **Custom** — each of the **four Parts changes volume in its own way**: the **Part Volumes** panel sets each Part's **Min** (knob left) and **Max** (knob right) level + a **Curve** per travel. "Design a Morph where two Parts get louder at different rates, one gets softer, one varies only slightly" — all moving at once on one knob.

== Macro Settings detail ==
- Each macro destination has On/Off, Destination name, **Curve** (drag: logarithmic ↔ linear ↔ exponential), **bipolar Modulation Amount** slider, Clear. Up to 8 destinations (scrollable past 4).
- Morph adds the layer-blend + modulation on top of all of the above → "no other control can create so much fascinating sonic movement."

== Augmented VOICES content (specific) ==
- Samples grouped **Choir / Female Solo / Male Solo**. Intent: "**not to reproduce words/sentences, but to create percussive and sustained textures**" — exactly the ambient-wall use case.
- **Choir**: 22-singer mixed choir; simple syllables Ah/Eh/Oh/Oo, plus evolving multi-syllable samples (Ah-Eh-Ah, Mh-Ah-Mh, Bah-Nah-Dah, Glo-Roh-Doh) that morph over a sustained note. Articulations: loud/soft Sustain, Staccato, Swell, and "an eerie pitch **Drift**."
- **Female/Male Solo**: single syllables or evolving vowel sets (Aah, Dooh, Eeh, Ei, Ha, Iih, Lah, Mm, Ohh, Ooh, Uuh); A-E-I-O-U vowel sweep, Vibrato, Staccato.

== CPU / performance (manual) ==
- **Polyphony** is user-selectable from a pop-up (top toolbar) — drop it to limit voices and CPU.
- A **CPU Meter** sits bottom-left; hover it to turn it into a **PANIC** button (kills stuck notes). Higher sample rates load CPU more. Manual advises larger buffer on slower machines (with latency cost). Confirms these are heavy — see augmented-ambient-use-cpu-freeze.md.
