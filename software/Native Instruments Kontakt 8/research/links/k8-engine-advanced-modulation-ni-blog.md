https://blog.native-instruments.com/advanced-modulation-tricks-kontakt/
blog.native-instruments.com · Advanced modulation and automation tricks in Kontakt

The single most load-bearing gotcha for the Kontakt mod system.

## Which modules CAN and CANNOT be modulated
- CANNOT be modulated: **Instrument Insert Effects, Send Effects, and Main
  (instrument) Effects.**
- CAN be modulated: **Source, Amplifier, and Group Insert Effects** parameters.
- WORKAROUND: if you want an LFO/envelope to wobble a reverb/delay/filter param,
  put that effect as a **Group Insert FX** (not an Instrument Insert / Send), or
  drive the param via **host automation** instead. This is the #1 thing people
  trip on when trying to make an effect "breathe."

## The five modulation source families
1. **Envelopes** — adjustable curves shaping a parameter over time (per MIDI note).
2. **LFOs** — repeating low-freq waveforms (sine, square, etc.).
3. **Complex LFO** — blends multiple wave shapes (richer, less periodic motion).
4. **Other internal** — **Step Modulator, Envelope Follower, Glide**.
5. **External** — **MIDI CC** messages or **random** values.

## Advanced moves
- **Multi-stage envelopes** ("Flexible"/DAHDSR style) build evolving, multilayered
  shapes far beyond basic AHDSR — the key to long, morphing pad swells.
- **Modulation Shaper** gives precise control over how a source maps to a target
  via a drawn curve, with **Modulation Intensity, Invert, and Lag (Smoothing)**.
  Lag/Smoothing = how you tame a steppy source into a glide.
- **Layering**: assign **multiple modulators to one parameter** (stack motion),
  or **one source to many parameters** (cohesive global movement).
- You can **modulate a modulator** (e.g. LFO rate modulated by a second LFO/env)
  for accelerating/decelerating, non-static motion.
