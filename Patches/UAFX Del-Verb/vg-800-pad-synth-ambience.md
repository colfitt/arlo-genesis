---
type: patch
title: VG-800 Pad / Synth Ambience
device: UAFX Del-Verb
date: 2026-06-14
description: A line-level pad/synth ambience patch — long 224 Hall (optionally the modulated "Swimmy and Shakey" tail) with a vibrato ping-pong delay sitting under a static pad, for VG-800 modeled amp/synth or any line source. Art-rock "verb that moves" texture.
tags: [ambient, pad, synth, modulated, indie-folk, art-rock, designed, signature]
controls:
  - { name: "Reverb Model", type: switch, value: "Hall 224", options: ["Spring '65", "Plate 140", "Hall 224"] }
  - { name: "Reverb voicing (app-assigned)", type: switch, value: "Default 224 Hall (Room A, long ambient tails) OR Swimmy and Shakey (224 Small Hall A, mid decay, 150 ms pre-delay — modulated/wobbly tail)" }
  - { name: "Reverb", type: knob, value: "1:00" }
  - { name: "Delay Model", type: switch, value: "Precision", options: ["Tape EP-III", "Analog DMM", "Precision"] }
  - { name: "Delay voicing (app-assigned)", type: switch, value: "Stereo Ping Pong Vibrato (LFO vibrato on the repeats)" }
  - { name: "Delay Time", type: knob, value: "dotted-1/8" }
  - { name: "Feedback", type: knob, value: "noon" }
  - { name: "Mix", type: knob, value: "10:00–11:00 (delay sits UNDER the pad)" }
  - { name: "Color", type: knob, value: "noon (flat)" }
  - { name: "Mod", type: knob, value: "noon (off — vibrato lives in the voicing, not the knob)" }
  - { name: "Trails", type: switch, value: "ON", options: ["ON", "OFF"] }
---

# VG-800 Pad / Synth Ambience

## Concept
Del-Verb is post-cab, end-of-chain, so it treats the VG-800 like any line source — its analog dry-through preserves the synth's low end. A long 224 Hall provides the bed; a vibrato ping-pong delay ("Stereo Ping Pong Vibrato") adds movement under an otherwise static pad. Swap the Hall voicing to "Swimmy and Shakey" for a detuning/modulated tail — the art-rock "verb that moves" character.

## How to play it
1. Pre-assign in the app: Reverb toggle "Default 224 Hall" (or "Swimmy and Shakey") on Hall 224, Delay toggle "Stereo Ping Pong Vibrato" on Precision.
2. Feed a VG-800 pad / synth patch (or any line source) into the pedal.
3. Hold sustained pad chords; the vibrato repeats add subtle movement underneath.
4. Keep delay Mix low (10:00–11:00) so it supports rather than competes with the pad.

## Notes
- The Mod knob stays at noon (off) — the vibrato lives in the *voicing*, not the knob.
- "Swimmy and Shakey" adds a detuning/modulated tail for the art-rock modulated-reverb texture; "Default 224 Hall" is the cleaner, long-tail option.
- Source-agnostic: corroborated by the OB-6 synth demo, so it works for any line-level synth, not just the VG-800.

## Sources
- designed from UA Preset & Voicing Lists ("Stereo Ping Pong Vibrato," "Default 224 Hall," "Swimmy and Shakey") + OB-6 synth demo + DeepResearch §6 (line-level, analog dry-through) — `research/links/voicing-list-official.md`, `research/transcripts/bonedo-synth-notalking-ob6.md`, `Gear/UAFX Del-Verb/research/Del-Verb-DeepResearch.md`
- Ref: Electronic/groove-first × indie-folk (sustained pad/string bed); art-rock modulated-reverb texture
- Transformed from Pedalxly Del-Verb-Patches.md (DOUG-designed)
