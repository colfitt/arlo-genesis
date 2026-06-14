https://splice.com/blog/mastering-ozone-elements-maximizer/
splice.com (Blog) · "Mastering basics with iZotope's Ozone: Maximizer" · Splice

The Maximizer is Ozone's brickwall limiter — the loudness stage. Key controls + safe
practice for NOT squashing.

## Core controls
- **Threshold**: lower = more limiting + loudness (and more squash).
- **Ceiling (output)**: set the true-peak max. Use -0.2 dB at the highest, or -1.0 to
  -2.0 dB to be safe against inter-sample/codec peaks (lossy encoding adds peaks).
- **Learn Threshold**: type your target LUFS and Maximizer auto-sets the threshold.

## Avoiding pumping / squash
- Keep gain reduction "no more than ~4.0 dB" at the loudest points to avoid audible
  pumping. (For drone, even less — every dB of limiting eats the slow swell.)
- **Sustain slider**: tunes how the limiter reacts to SUSTAINED material "like pads,
  guitars, drones, etc." — the single most relevant control for this rig. Raise it so the
  limiter rides the wall smoothly instead of grabbing the swell.
- **Character / Transient sliders**: match Character to tempo (toward "fast" for fast
  songs); raise Transient to preserve sharp hits (snares, banjo plucks) while still
  getting level.

## Streaming LUFS targets (normalization)
- Spotify -14, YouTube -13, Tidal -14, Apple Music -16 LUFS (integrated).
- Because of normalization, a -8 LUFS "loud" master gets turned DOWN to match a -14 one
  on playback — so crushing a drone for loudness buys nothing and loses dynamics.
  Master to ~-14 LUFS (or quieter) and keep the grit.
