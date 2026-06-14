https://www.ableton.com/en/products/live-lite/features/
ableton.com · Ableton (official) · accessed 2026-06-07

# Live 12 Lite — exact included devices & limits (authoritative)

This is the load-bearing reference for the whole Lite research: it determines which
shared racks/presets will actually open vs throw missing-device errors.

## Hard limits
- **8 audio + MIDI tracks** max (total, combined).
- **16 scenes**.
- **2 return tracks** (+ master).
- 8 mono in / 8 mono out.
- Session View: YES (full clip-launch / scene performance — the Lite headline feature).
- Group tracks: YES.

## Instruments included (Lite)
- **Drift** (subtractive synth, MPE-capable) — the only "real" synth in Lite.
- **Simpler** (one-shot / sampler).
- **Impulse** (8-slot drum sampler).
- **Drum Rack** (+ 126 factory Drum Racks).
- **Instrument Rack** (container — YES, Lite has racks).

## Audio effects included (Lite) — the WHOLE list
Auto Filter · Beat Repeat · Channel EQ · Chorus-Ensemble · Compressor · Delay ·
EQ Three · Erosion · Limiter · Phaser-Flanger · Redux · Reverb · Saturator ·
Tuner · Utility.
**Audio Effect Rack** container: YES.

## MIDI effects included (Lite)
Arpeggiator · Chord · MIDI Effect Rack · MIDI Monitor · MPE Control · Note Length ·
Pitch · Random · Scale · Velocity.

## NOT in Lite (will cause missing-device errors when loading shared racks)
- **Max for Live** — EXCLUDED. So ANY .adg/.adv that contains an M4L device
  (e.g. "One Button Live Looper", Holder spectral freeze, most generative gen
  tools) will fail to load in Lite. This kills a large slice of the ambient/drone
  rack ecosystem.
- **Looper** — NOT listed in Lite's audio effects. (Looper is a Standard/Suite
  device.) → No native loop-pedal device in Lite; loop with audio-track
  resampling + Session record instead (see looping notes).
- **Wavetable**, **Operator**, **Sampler**, **Analog**, **Electric**, **Tension**,
  **Collision**, **Granulator** — Suite/Standard instruments. Racks built on these
  will not load.
- **Echo** (the dedicated Echo device), **Hybrid Reverb**, **Spectral Resonator**,
  **Spectral Time**, **Corpus**, **Resonators**, **Grain Delay**, **Frequency
  Shifter**, **Vocoder**, **EQ Eight**, **Gate**, **Drum Buss**, **Glue
  Compressor**, **Multiband Dynamics**, **Overdrive**, **Amp**, **Cabinet**,
  **Pedal**, **Dynamic Tube**, **Roar**, **Shifter**, **Delay** is in Lite but
  **Echo / Grain Delay are NOT**. → Any shimmer/ambient rack that relies on Echo,
  Frequency Shifter, EQ Eight, Grain Delay, Spectral devices, or Wavetable WILL
  NOT open in Lite.

## Core library content available
- 659 Instrument Racks (54 MPE), 126 Drum Racks, **140 Audio Effect Racks**,
  244 loops, 2,220 drum hits.
- NOTE: many of those 140 stock Audio Effect Racks are built only from core
  devices and DO load in Lite — they are the safest "shared rack" source.

## Practical takeaway for this rig
The Lite-safe ambient palette = Reverb, Delay, Auto Filter, Erosion, Redux,
Saturator, Chorus-Ensemble, Phaser-Flanger, EQ Three/Channel EQ, Utility, wrapped
in Audio Effect Racks, plus Drift/Simpler as sources. Everything else in the
"shimmer/granular/spectral" world is Suite. Honest ceiling.
