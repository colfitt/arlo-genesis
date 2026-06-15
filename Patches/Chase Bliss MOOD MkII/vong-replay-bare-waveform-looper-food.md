---
type: patch
title: Bare-Waveform Looper Food (Vong Replay / OP-1)
device: Chase Bliss MOOD MkII
date: 2026-06-15
description: The Unperson chose a Vong Replay synth deliberately because it has only basic waveforms and no effects — the ideal Micro-Looper source that shows off MOOD's power. A continuous bare synth waveform (or an OP-1 controlling an Arturia clarinet preset) is captured cleanly, then granularized/pitch-warped by Stretch/Tape/Env. The most direct route to the "sustained wall" from a clean source. (The Unperson / Ali + rig dossier — technique sourced, no published knob values.)
tags: [synth, looper, stretch, tape, ambient, texture, technique]
controls:
  - { name: "Source", type: switch, value: "bare-waveform synth / OP-1 pad (continuous, no FX) — e.g. Arturia 'Augmented Woodwinds' clarinet" }
  - { name: "Looper MODE", type: switch, value: "Stretch (freeze a grain) or Tape (octave-shift)", options: ["Env", "Tape", "Stretch"] }
  - { name: "Looper MODIFY", type: knob, value: "Stretch: toward NOON to freeze a grain (dial to taste)" }
  - { name: "Wet MODE", type: switch, value: "Reverb (to smear the loop)", options: ["Reverb", "Delay", "Slip"] }
  - { name: "CLOCK", type: knob, value: "roll back for degradation (dial to taste)" }
  - { name: "ROUTING", type: switch, value: "IN+micro-loop, or micro-loop only", options: ["IN", "IN+micro-loop", "micro-loop only"] }
---

# Bare-Waveform Looper Food (Vong Replay / OP-1)

## Concept
The Unperson chose the Vong Replay synth deliberately — it has only basic waveforms and no effects, which makes it the ideal Micro-Looper source that shows off MOOD's power. Feed MOOD a continuous, effect-free synth waveform (or an OP-1 controlling an Arturia clarinet preset), capture it cleanly with the Micro-Looper, then let Stretch/Tape/Env granularize and pitch-warp it. This is the most direct route to the "sustained wall" from a clean source: the pedal provides all the texture, so the source should provide none.

## How to play it
1. Feed MOOD a sustained, effect-free synth waveform or an OP-1 pad (a clarinet/woodwind preset works well).
2. Engage the Micro-Looper to capture the sustained tone cleanly.
3. Granularize it: Looper MODE = **Stretch** (MODIFY toward NOON to freeze a grain) or **Tape** (octave-shift), under a **Reverb** smear on the Wet path.
4. Roll **CLOCK** back for degradation; build with overdub passes for an evolving wall.

## Notes
- A bare waveform is documented as ideal looper food — clean capture, then MOOD does the texture.
- Rig parallel: VG-800 pads / OP-1 Field route in exactly like this ("continuous synth/pad output is ideal looper food").
- **No published knob values** — the concept and source choice are the sourced parts; treat the control settings as a dialable recipe and tune by ear.

## Sources
- gear/Chase Bliss MOOD MkII/research/transcripts/unperson-mood-mkii-reverb-delay-looper.md (Vong Replay "chosen deliberately because it only has basic waveforms and no effects, so it shows off MOOD's power"; OP-1 controlling Arturia "Augmented Woodwinds" clarinet → MOOD)
- gear/Chase Bliss MOOD MkII/research/MOOD-MkII-DeepResearch.md §6 (Modeled VG-800 pads: "continuous synth/pad output is ideal looper food… Stretch/Env then granularize it")
- gear/Chase Bliss MOOD MkII/research/MOOD-MkII-UsageGuide.md §5 (synth/VG-800/OP-1 as looper food)
- Ref: The Unperson (Ali) — technique/source choice documented, no published knob values
