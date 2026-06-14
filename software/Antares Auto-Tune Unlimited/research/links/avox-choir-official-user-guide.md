https://antares-web-frontend.sfo3.cdn.digitaloceanspaces.com/documentation/pdfs/Choir-User-Guide.pdf
antarestech.com (official) · Choir User Guide (current Auto-Tune-Central / Unlimited era) · n.d.

Authoritative spec for the standalone **Choir Vocal Multiplier** (the AVOX module). Distilled — the complete control set (it's deliberately tiny):

**What it is:** turns a single voice into a choir of **4 / 8 / 16 / 32** distinct unison voices. Each generated voice gets its own random pitch, timing, and vibrato variation relative to the original. Multiple instances on separate harmony parts = "an amazingly realistic, large vocal ensemble."

**The four controls — that's all of them:**
- **Choir Size:** menu, **4 / 8 / 16 / 32** voices generated from the original.
- **Vibrato Variation:** range of variation in **vibrato depth** applied across the generated voices.
- **Pitch Variation:** range of variation in **pitch** (detune) per generated voice.
- **Timing Variation:** range of variation in **timing** (entrance/onset) per generated voice.
  - All three: "each generated voice is individually assigned a vibrato/pitch/timing variation relative to the original; **higher settings = more variation among the voices.**" This is what moves it from tight-unison-thicken → loose, swimmy, detuned wall.
- **Stereo Spread:** **0 = all voices dead center (mono-stacked)**, increasing spreads them outward, **100 = spread across the entire stereo field.** **NOTE: Stereo Spread is only available on a stereo or mono-to-stereo track — disabled on a mono track.** (So in Logic you must run Choir on a stereo or mono→stereo channel to get width.)

**No** Number/Detune-by-percent knobs as separate from the above, **no** formant/throat control, **no** MIDI, **no** key/scale — it's pure unison-multiply + variation + spread. (Contrast Harmony Engine, which *generates intervals/chords*; Choir only **thickens whatever pitch is already there.**)

**DAW insert (Logic Pro):** Audio Units > Antares > **Choir**, on an audio/instrument track or bus. For Stereo Spread you need a **stereo or mono→stereo** track.

Rig takeaway: it's a one-knob-idea wall-maker. **Size 32 + push all three Variations + Spread ~70–100** = the shimmering detuned-choir-of-one. Because it doesn't change pitch, it's perfect on a **sustained drone / held banjo or baritone note / synth pad** — feed it one held pitch and it blooms into a 32-voice unison cloud around that pitch. Layer 2–3 instances on different held notes (or on the outputs of a Harmony Engine / Duo) for a stacked choral chord. Must be on a stereo channel in Logic for the width to engage.
