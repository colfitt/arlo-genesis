https://native-instruments.com/ni-tech-manuals/crush-pack-manual/en/dirt
native-instruments.com · NI Tech Manual — Crush Pack: DIRT · current

# DIRT — full control reference (from the manual)

Two circuit-modeled diode-clipping stages with wavefolding. **NOT confirmed installed on disk (Crush Pack referenced in navigator; only Bite verified in CONTENTS.md).**

## Controls
- **Drive (per stage):** input gain — right = more distortion intensity.
- **Amount (per stage):** the defining control. **Saturation in the first half of its range, WAVEFOLDING in the second half.** Wavefolding folds the waveform back into itself instead of clipping → complex/dynamic timbres even from a sine; cleaner than clipping.
- **Mode (per stage — three types):**
  - **I** — most subtle, least coloring (presence/warmth).
  - **II** — default, well-balanced, **brightest** tone.
  - **III** — most extreme, crushed, **dark** tone.
- **Tilt:** tone/spectral tilt — right boosts highs (brighter), left boosts lows (darker tails).
- **Bias:** asymmetry → produces **even harmonics**; fixes thin/hollow distortion (warmth/body).
- **FX Trim:** wet output level, **−18 dB → +6 dB** (dry not affected).
- **Routing:** **A > B** serial, **A < B** (B>A) serial, **A + B** parallel.
- **Mix/Blend:** serial = dry↔wet; parallel = blend between the two stage outputs. (Single-stage = set the other stage's Amount to 0.)
- **Safety (warning icon, by Drive):** disables gain compensation → higher gain / more extreme drive between stages.

No numeric ranges given for Drive/Amount/Tilt/Bias; no preset names on the page. (Separate Komplete-Now demo says Dirt ships 74 presets.)
