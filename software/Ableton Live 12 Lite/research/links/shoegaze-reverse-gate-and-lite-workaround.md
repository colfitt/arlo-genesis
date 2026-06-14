https://www.izotope.com/en/learn/4-ways-to-get-a-shoegaze-sound.html
izotope.com · iZotope Learn (+ Akihiko Matsumoto Shoegazer Reverse Gate M4L, sellfy)

# Shoegaze "reverse swell" wall — and the Lite-only way to do it

Shoegaze = "gauzy walls of sound... reverb-laden swells, blistering distortion, and
lots of delay, often all at once." The signature move is the REVERSE-REVERB SWELL
(sound rises out of silence).

## The popular tool (NOT Lite-loadable)
- **Akihiko Matsumoto "Shoegazer Reverse Gate" Max4Live device** (emulates the
  Yamaha SPX90 reverse gate). Tweak Threshold so it triggers on chord peaks; stretch
  with Attack/Release; ~70% wet keeps the chords intelligible; automate Dry/Wet +
  Release for cascading swells at climaxes.
- **REQUIRES Max for Live → will NOT load in Live 12 Lite.** Flag.

## The Lite-safe equivalent (no M4L)
The reverse-reverb swell predates plugins — it's an editing trick, fully Lite-doable:
1. Record/print the guitar (or banjo) part to an audio clip.
2. Put **Reverb** (stock, in Lite) on the track, long Decay, high Dry/Wet, print
   (resample) the reverberated tail to a new audio clip.
3. **Reverse that clip** (clip Reverse in the Sample box — Lite supports it).
4. Lay the reversed-reverb clip UNDER the dry note so the tail swells INTO the
   attack. Repeat per chord.
5. Optional: Auto Filter LP sweep + Saturator for the "blistering" edge.
This nails the shoegaze swell using only Reverb + clip reverse + resampling.

## Other Lite-safe shoegaze ingredients
- Wall density: layer 2-3 reversed/forward guitar takes (track budget permitting),
  detune slightly via clip Transpose, drench in Reverb.
- Grit: **Saturator** (Drive + Soft Clip) and/or **Erosion** for that "recorded-
  wrong" degraded top end — both in Lite.
- Smear: **Chorus-Ensemble** wide + **Reverb** → MBV-style pitch-wobble haze.

## Certainty
HIGH that the M4L reverse-gate needs Max for Live (it IS a M4L device). HIGH that the
reverse-reverb-via-resampling trick works in Lite (uses only confirmed Lite features:
Reverb, clip reverse, resampling). The exact iZotope wording is sourced; the Lite
recipe is reconstructed standard practice.
