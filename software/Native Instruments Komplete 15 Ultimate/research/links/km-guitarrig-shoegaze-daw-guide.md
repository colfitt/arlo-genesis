https://alijamieson.co.uk/2021/12/12/gazed-and-confused-a-guide-to-shoegaze-in-your-daw/
Ali Jamieson · "'gazed and Confused: A Guide to Shoegaze in your DAW"

A deep, DAW-agnostic shoegaze production guide. Several techniques name Guitar Rig directly and the chain-order reasoning transfers straight into GR's rack.

## Effect ordering (the standard order)
Distortion typically PRECEDES reverb to shape the fuzz before spatial processing. For guitars: **distortion pedal → amp → mic/cab emulation** (his example: a crunch distortion ~10 o'clock, tone at noon → Small Brownface amp + Vintage British 4×12 + Ribbon 121). NOTE the contrast with the NI shoegaze blog's "distortion at the END" trick — both are valid; distortion-first = a driven amp wall, distortion-last = crushing the reverb tails together. GR can do either by reordering in the Signal Flow.

## Reverse / swell reverb
- "Reverse reverb" via a non-linear reverb with a long attack (~380 ms) — "found a lot throughout Loveless."
- **Valhalla Shimmer "Bloom" preset** (diffusion 0.618), Size matched to session tempo, to trigger reverse-style swells. (In GR: the **Reverse** function in Loop Machine Pro, or **Psych Delay** which can be reversed/pitched, are the in-box equivalents.)

## Wall of sound construction
Kevin Shields: "2 valve amps with tremolo facing each other, played a few times, sampled and played backwards." Digital equivalent = multiple guitar tracks at varying distortion intensities:
- **dark, bottom-heavy distortion** (primary rhythm)
- **bright, harsh fuzz** (upper-frequency buzz)
- **medium aggression** (glue layer)
Then box each with high/low-pass filters ("box the sound") so layers don't fight. Multiband saturation (Saturn) as the digital fuzz-stack.

## Pitch / modulation
- Whammy-bar flutter faked with **SketchCassette II** ("fluttered old tape-like sound").
- Chorus/detune via slightly offset oscillators between layered tracks (natural shimmer, no chorus plugin).
- **Lead-tone shaping: Guitar Rig's Auto Filter + Fast Compressor (very short attack to remove transients) BEFORE Big Fuzz + Marshall/Vox amp sim** — an explicit GR lead recipe.

## Mixing philosophy
One or two *effective* reverbs beats many poor ones. Start channels at −10 dB for headroom. Bus similar elements (drums/guitars/synths) for unified reverb/delay sends. Much of Loveless is mono/centered — pan hard only when the source is genuinely stereo. Parallel compression (1176-style) to get drums loud without taking over (Alan Moulder technique).
