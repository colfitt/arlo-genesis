https://blog.native-instruments.com/creating-sci-fi-sounds-with-conflux/
blog.native-instruments.com · Creating sci-fi sounds with Conflux · 2024/2025

Conflux signal flow + a concrete evolving/textural sound-design workflow.
Directly useful for the drone/ambient/cinematic aesthetic.

## Source layer
- **Wavetable synth + sample layer** side by side. UI: **four wavetable menus
  (blue dots)** and **four sample menus (purple dots)**.
- Notable wavetable sources include PPG Wave tables ("Robotic," "Yonder");
  vocal samples like "SingSang."

## Synthesis / audio-rate mod
- **Audio Mod module**: applies **frequency, pulse, and ring modulation** to the
  wavetable oscillator → timbral complexity / metallic-inharmonic content.
- **Pitch modulation**: the mod envelope shapes pitch sweeps — e.g. "short
  attack, medium decay, no sustain" for punchy laser/zap profiles.

## Modulation sources
- **LFO**: assign to **Wavetable Position** and **Audio Mod tuning** (active
  routes show as solid orange lines). Slow LFO on wavetable position = the core
  "evolving pad" move.
- **Animator** (step sequencer): programmed modulation sequences; you can "draw"
  shapes like an up-down klaxon sweep.
- **Random input**: spits out a new random value **each note** — assign to pitch,
  wavetable position, asymmetry for per-note timbral variation (great for living,
  non-static drones).

## FX chain (on-board)
- Spectral: high-pass filter w/ resonance, EQ, phaser, **shimmer (with detune)**.
- Dynamics/dist: compression, **Phat** (distortion), **digitize** (bitcrush/lo-fi).
- Spatial: **Raum reverb (incl. "cosmic" mode)**, "space," **diffusion delay**,
  gated reverb.

## Evolving-pad takeaway (this rig)
Blend a soft sample layer under a wavetable source → slow **LFO → Wavetable
Position** (low rate, moderate depth) → **Random → asymmetry/pitch** for drift →
Shimmer + Raum at the end. That's a self-evolving wall with no automation drawn.
