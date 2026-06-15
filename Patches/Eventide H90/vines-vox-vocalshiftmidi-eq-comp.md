---
type: patch
title: "Vines Vox — VocalShiftMIDI + EQ Compressor (artist preset)"
device: Eventide H90
date: 2026-06-15
description: "Artist preset by Vines (Cassie Wieland) from her LP 'I'll be here' — lush MIDI-driven pitched vocal harmonies that feel both electronic and deeply human, shaped by an EQ Compressor stage. Drive the harmonies from a MIDI keyboard/footboard. Algorithm pair published by Eventide's blog; raw values were not."
tags: [vocalshiftmidi, vocal, harmony, artist-preset, vines, midi, experimental-pop]
controls:
  - { name: "Preset A Algorithm", type: switch, value: "VocalShiftMIDI (MIDI-controlled pitched harmony voices)" }
  - { name: "Preset B Algorithm", type: switch, value: "EQ Compressor (tonal + dynamic control stage)" }
  - { name: "Unison Mix", type: knob, value: "blend dry/unison to keep harmonies natural" }
  - { name: "Formant", type: knob, value: "set per voice to keep harmonies human, not chipmunk" }
  - { name: "Vibrato", type: knob, value: "to taste" }
  - { name: "Delay", type: knob, value: "in ms or synced, to taste" }
  - { name: "Gate", type: knob, value: "to taste" }
  - { name: "Velocity Sensitivity", type: knob, value: "to taste" }
  - { name: "Pitch-Bend Range", type: knob, value: "set to playing style" }
  - { name: "Hold", type: switch, value: "sustain held voices" }
  - { name: "Freeze (HotSwitch / Perform)", type: button, value: "sustain/freeze the harmony" }
---

# Vines Vox — VocalShiftMIDI + EQ Compressor (artist preset)

## Concept
An artist preset by Vines (Cassie Wieland), built from the sound of her LP "I'll be here": lush, pitch-shifted MIDI harmonies on a vocal that feel both electronic and deeply human. VocalShiftMIDI generates the MIDI-controlled pitched voices, and an EQ Compressor stage gives the tonal and dynamic control that keeps the stack sitting in a track. The harmonies are driven from a MIDI keyboard/footboard rather than from a fixed scale, so the chord moves with what you play.

## How to play it
1. Load VocalShiftMIDI into one slot (Preset A) and EQ Compressor into the other (Preset B).
2. Feed harmony notes via MIDI to set the pitch-shifted voices.
3. Use Formant and Unison Mix to keep the harmonies natural rather than artificial.
4. Shape the result with the EQ Compressor for tone and dynamics.
5. Use Hold / Freeze to sustain a harmony when you want it to bloom.

## Notes
- Provenance: artist preset by Vines (Cassie Wieland), one of five she created for the H90's VocalShiftMIDI algorithm, via the Eventide blog. The algorithm pair (VocalShiftMIDI + EQ Compressor) is published; raw parameter values are not.
- **No published values** — the Eventide blog did not publish raw values or a download link, so the controls above are a dialable recipe, not sourced settings. Dial by ear.
- Distinct from the existing `vocalshiftmidi-live-harmony-drone` patch: that one is a live-harmony drone with no EQ-Compressor pairing and no artist provenance.

## Sources
- https://www.eventideaudio.com/blog/vines-brings-her-signature-vocal-sound-to-the-h90/ (Vines / Cassie Wieland artist presets; "Vines Vox" = VocalShiftMIDI + EQ Compressor)
