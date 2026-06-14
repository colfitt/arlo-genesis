https://alijamieson.co.uk/2016/07/21/reaktors-spacedrone/
alijamieson.co.uk · Ali Jamieson · Jul 2016 · "Reaktor's SpaceDrone"

Technical deep-dive on **SpaceDrone**, the flagship self-playing drone ensemble in the Reaktor **Factory Library** (the single most rig-relevant factory ensemble).

**Architecture:** 96 parallel voices spread across the frequency spectrum; each voice = noise generation → envelope → band-pass filter → stereo position. Signal path per voice follows subtractive principles: **noise oscillator → 2-pole band-pass filter → amplitude + stereo pan + reverb.**

**Key controls (verbatim mapping):**
- **Pitch** — *Fundamental* (sets filter frequency), *Offset* (adjusts harmonics), *Speed/Amt* (slow random LFO on pitch).
- **Envelope** — *Attack* and *Decay* shape amplitude; *Decay* governs both decay and release.
- **Dynamics** — *Density*, *Rnd* (randomness), *Dynamic* manage retrigger rate and volume range.
- **Resonance** — raises filter Q for tonal, resonator-like tones.
- **Damp** — frequency content (CCW opens highs; CW attenuates).
- **Panning** — Rate + randomness for stereo motion.

**The Geiger macro:** generates random trigger events "much like a Geiger Counter radiation particle detector" → drives the ADR envelope retriggering → this is what makes SpaceDrone evolve/self-generate.

**Technique:**
- **Evolving drones:** slow the LFO Speed, reduce Dynamic range, raise Resonance for harmonic definition.
- **Static pads:** Density high, Rnd low, Dynamic range maxed.
- **MIDI playability:** the article ships a modified version adding a **Gate MIDI input** with boolean (AND-gate) logic so you can "play" SpaceDrone from a keyboard while keeping its generative character — useful for triggering a drone from the Novation 61SL MkIII or S08.

Rig note: SpaceDrone is the go-to factory self-runner. Record its stereo output straight into Logic, then push it through Valhalla VintageVerb / EchoBoy for a wall under banjo.
