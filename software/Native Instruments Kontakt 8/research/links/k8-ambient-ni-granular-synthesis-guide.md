https://blog.native-instruments.com/granular-synthesis/
blog.native-instruments.com · Native Instruments · "Granular synthesis: a beginner's guide" · 2023-04-04

NI's own granular primer with COPYABLE settings for evolving drones/pads. The
granular engine "shatters a sample into thousands of tiny grains" and lets you
reassemble them — the core of the "single sample → evolving wall" move. Featured
NI tools: **Straylight** (granular Kontakt instrument, owned) and **Form**.

## Copyable settings — diffuse sustained pad from any sample
- **Grain size ≈ 600 ms**, **grain interval ≈ 40 ms**. The large size + small
  interval = heavy grain OVERLAP → smooth diffuse sustain (not choppy/glitchy).
- **Sample range:** use min/max knobs to isolate the richest part of the source.
  Enable **"bounce edges"** so playback ping-pongs within that window = sustained-
  forever illusion (no obvious loop point).
- **Grain envelope:** medium fade-in / fade-out → keeps grains smooth, no clicky
  edges.
- **Jitter ≈ 50%** (moderate): randomizes playhead POSITION so the grain cloud
  obscures the source's original contour → organic, non-repeating motion.

## The evolving-LFO technique (the key to "alive" texture)
"Movement is the key — sounds that develop over time feel more alive." Assign
SLOW LFOs at DIFFERENT rates so nothing ever lines up:
- **LFO 1 → grain interval**, rate ~**0.05 Hz**.
- **LFO 2 → grain size**, rate ~**0.09 Hz** (deliberately different from LFO 1).
- Extra LFO → **jitter** for varying agitation.
- All rates **below 0.1 Hz** → minute-scale drift, never a perceptible cycle.

## Textural freeze
- A "textural freeze" smears/blurs the grain cloud to turn a **short percussive
  one-shot into an endless, complex evolving drone** (freeze the position, let the
  grain cloud sustain + the LFOs drift it).

### Takeaway for the rig
This is the exact recipe to turn a banjo pluck or a pedalboard tail into a forever
pad: load it into Straylight's grain layer (or any granular), grain size 600 /
interval 40 / jitter 50%, bounce-edges on, then two sub-0.1 Hz LFOs on size +
interval at different rates. Freeze on a rich moment = endless drone. Pairs with
the Clinton-Shorter and dark-ambient (protoU/Mebitek) field-recording-morph methods.
