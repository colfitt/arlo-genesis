---
type: patch
title: "Pollia — VocalShiftMIDI + Shimmer (Vines artist preset)"
device: Eventide H90
date: 2026-06-15
description: "Vines (Cassie Wieland) artist preset pairing VocalShiftMIDI with Shimmer — ethereal soundscapes that stack the MIDI-driven vocal harmonies into octave-up celestial choirs, 'choir-like compositions that feel both massive and intimate.' One of the five Vines presets for VocalShiftMIDI, published via the Eventide blog; the algorithm pair is published but raw knob values are not, so the controls below are a dialable recipe."
tags: [vocalshiftmidi, shimmer, reverb, pitch, harmonizer-plus, vocal, choir, ambient, shimmer-wall, artist-preset, vines, midi]
dips:
  HARMONIES: "driven via MIDI"
  PITCH_FREEZE: "HotSwitch -> Shimmer Pitch Freeze to lock the climb for solo-over pads"
  PITCH_SHIFT: "A/B near 1200c (octave up) for the choir stack"
controls:
  - { name: "Preset A Algorithm", type: switch, value: "VocalShiftMIDI (MIDI-driven pitched vocal harmony voices)" }
  - { name: "Preset B Algorithm", type: switch, value: "Shimmer (twin pitch shifters in the reverb feedback path)" }
  - { name: "Routing", type: switch, value: "Series (VocalShiftMIDI -> Shimmer)", options: ["Series", "Parallel", "Insert"] }
  - { name: "Pitch Shift A (B)", type: knob, value: "near +1200c / octave up — recipe, no published value" }
  - { name: "Pitch Shift B (B)", type: knob, value: "just above/below the octave for a wider choir — recipe, no published value" }
  - { name: "Pitch Decay (B)", type: knob, value: "high — sustains the rising octave stack — recipe, no published value" }
  - { name: "Decay (B)", type: knob, value: "high / long tail — recipe, no published value" }
  - { name: "Delay (B)", type: knob, value: "low — recipe, no published value" }
  - { name: "Mix (B)", type: knob, value: "blend dry vs. the shimmer wash to taste — recipe, no published value" }
  - { name: "Freeze", type: switch, value: "Pitch Freeze (keeps the climb) or Pitch+verb Freeze (locks everything for soloing over)", options: ["Pitch Freeze", "Pitch+verb Freeze"] }
  - { name: "Pitch Freeze (HotSwitch / Perform)", type: button, value: "lock the rising shimmer for a held celestial pad" }
---

# Pollia — VocalShiftMIDI + Shimmer (Vines artist preset)

## Concept
Vines (Cassie Wieland) "Pollia" artist preset: VocalShiftMIDI supplies the MIDI-driven pitched vocal harmony voices, then Shimmer's twin pitch shifters fold those voices back through the reverb feedback path, climbing octave-up into "celestial vocal stacks" and "choir-like compositions that feel both massive and intimate." Where Biblically Accurate (Wormhole) smears the voices and Clinton Lake (Sticky Tape) dirties them, Pollia lifts them — the cathedral/heavenly end of the Vines set, a vocal shimmer wall rather than a clean harmonizer.

## How to play it
1. Load VocalShiftMIDI on Preset A and Shimmer on Preset B (Series, A -> B).
2. Drive the harmony voices via MIDI over a held source note so the chord stacks.
3. Set Shimmer's Pitch Shift A/B near the octave (~1200c) with high Pitch Decay and a long Decay for the rising choir.
4. Blend the Mix so the vocal voices feed the shimmer wash rather than sitting on top of it.
5. Use Pitch Freeze (or Pitch+verb Freeze) on a HotSwitch to lock the climb into a held celestial pad and play over it.

## Notes
- Described in the Eventide blog as "ethereal soundscapes" / "celestial vocal stacks" and "choir-like compositions that feel both massive and intimate."
- One of the five Vines presets for VocalShiftMIDI (alongside Vines Vox, Angel Gate, Clinton Lake, Biblically Accurate).
- Distinct from the existing shimmer patches (shimmer-heaven-octave-stack-manual, shimmer-pitch-wall, shimmer-drone-exp-pedal-pitch-decay-freeze): this is the MIDI-vocal-harmony-into-Shimmer pairing, not a guitar-fed shimmer wall.
- HONESTY: the VocalShiftMIDI + Shimmer pairing is published (Eventide blog), but raw knob values are NOT. Every control value above is a dialable recipe — the Pitch Shift / Pitch Decay / Decay starting points are drawn from the rig's general shimmer-wall recipe, not from Vines' actual settings. Dial by ear.

## Sources
- https://www.eventideaudio.com/blog/vines-brings-her-signature-vocal-sound-to-the-h90/ (Vines / Cassie Wieland; Pollia = VocalShiftMIDI + Shimmer; "celestial vocal stacks", "choir-like compositions that feel both massive and intimate")
- https://cdn.eventideaudio.com/manuals/h90/1.11.4/content/algorithms/reverb.html (Shimmer parameters — twin pitch shifters, Pitch A/B in cents, Pitch Decay, Pitch Freeze vs Pitch+verb Freeze)
- `gear/Eventide H90/research/H90-DeepResearch.md` — Shimmer algorithm summary + shimmer/pitch-wall recipe (Pitch A/B near 1200c, high Decay/Pitch Decay, Pitch Freeze)
- provenance: artist Vines (Cassie Wieland) via Eventide blog + manual/research (params) — pair published, no values
