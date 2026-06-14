https://www.musicradar.com/how-to/logic-sample-alchemy · https://www.audeobox.com/learn/logic-pro/alchemy-synth-tutorial/
musicradar.com (OSC/Steve, 2024-01-15) + audeobox.com · Logic 10.8+ stock plugin

# Sample Alchemy — turning the rig's recordings into drones/textures (stock, free)

Sample Alchemy (Logic 10.8+) runs the **Alchemy engine** on ANY dropped sample —
granular/additive/spectral resynthesis. This is the killer stock tool for the
user's aesthetic: feed it a banjo/baritone recording, a frozen reverb wash, or a
sample of the pedalboard, and resynth it into an evolving drone bed. Free, AU,
no third-party plugin needed.

## Load
Drag audio straight from the Arrange window (or a recorded hardware take) into
Sample Alchemy. It auto-analyzes pitch so the sample plays back chromatically
from MIDI.

## Four synthesis modes
- **Granular** — layers tiny snippets (1-100 ms). Params: grain size, density,
  randomize timing/pan. THE drone/texture mode.
- **Additive** — sine-bank resynth (Harmonic / Partials / Formant sub-modes);
  smooth, pure pads.
- **Spectral** — splits pitched vs percussive, replaces pitched with sines /
  percussive with noise (Formant, Blur, Cloud, Metalize sub-modes). Great for
  smeared, "blurred" walls.
- **Sampler** — classic sample playback.

## Concrete ambient-drone recipe (granular)
- **Grain size 50-100 ms** = recognizable fragments of the source; **5-20 ms** =
  smooth evolving texture/wash.
- **Modulate Position with a slow LFO (0.1-0.5 Hz)** so the granular engine
  slowly scans through the audio — this is what makes it "evolve."
- Add reverb from Alchemy's built-in FX rack.
- "Very good at creating ethereal pads and drones... glitchy futuristic
  textures and drums too."

## Sources + playback modes
- **4 sources (A/B/C/D)** placed across the waveform; horizontal axis = playback
  start point, vertical = first synth parameter. Each source has independent
  synth settings.
- Playback modes: **Classic / Loop / Scrub / Bow (violin-like back-and-forth) /
  Arp**. "Bow" and "Scrub" are excellent for sustained drones.
- **Motion mode** records a custom playhead path for dynamic, performed scans.

## Transform Pad morph (from the full Alchemy)
The A/B/C/D corners are full parameter snapshots; moving the point crossfades
(interpolates filter cutoff, sources, FX, mod depths) — automate it for a slow
morph across an entire section.

## Rig recipe
Record the baritone/banjo or a pedalboard texture → drop into Sample Alchemy →
Granular, grain 10 ms, Position LFO 0.2 Hz → instant evolving drone bed under
the track. Then Freeze (Source Only) to save CPU. Pairs with ChromaVerb Freeze.
