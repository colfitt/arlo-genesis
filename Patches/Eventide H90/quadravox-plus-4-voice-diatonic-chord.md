---
type: patch
title: "Quadravox+ — 4-Voice Diatonic Harmonizer (drone to chord)"
device: Eventide H90
date: 2026-06-15
description: "The Harmonizer+ Quadravox+ algorithm (firmware v1.10, ported from the H9000) — a 4-voice diatonic harmonizer with staggered delays and an arpeggio feel, scale-locked, to turn a mono baritone/banjo drone into a wide stereo chord. Feed it the string source, not just vocals. The full control list (Shift A-D, four staggered Delays, Spread, Detune, Formant Link, Glide) is published in the official Eventide manual; no factory knob values — dial the intervals to the song."
tags: [quadravox, pitch, harmony, diatonic, drone, sustained-wall]
dips:
  FIRMWARE: "Harmonizer+ requires firmware v1.10+ via H90 Control"
  PERFORMANCE: "Root learn / Glide performance controls map to footswitches"
controls:
  - { name: "Preset A Algorithm", type: switch, value: "Quadravox+" }
  - { name: "Key", type: knob, value: "song root (dial to song)" }
  - { name: "Scale", type: switch, value: "song scale (dial to song)" }
  - { name: "Quantization", type: switch, value: "lock harmonies to the scale (dial to song)" }
  - { name: "Shift A/B/C/D", type: knob, value: "diatonic interval per voice (dial to the chord you want)" }
  - { name: "Delay A/B/C/D", type: knob, value: "four staggered delays (A shortest) for the arpeggio feel (dial to song)" }
  - { name: "Division", type: knob, value: "sets the delay timing relationship (dial to song)" }
  - { name: "Spread", type: knob, value: "stereo width (A&C left / B&D right) — open for a wide chord" }
  - { name: "Detune", type: knob, value: "+/-50 cents to thicken (dial to taste)" }
  - { name: "Formant Link", type: switch, value: "ON for natural harmonies", options: ["On", "Off"] }
  - { name: "Auto EQ", type: switch, value: "On", options: ["On", "Off"] }
  - { name: "Glide A/B/C/D + Rise + Fall", type: knob, value: "performance pitch-rise/fall (map to footswitch)" }
---

# Quadravox+ — 4-Voice Diatonic Harmonizer (drone to chord)

## Concept
The Harmonizer+ Quadravox+ algorithm — a 4-voice diatonic harmonizer ported from the H9000 (firmware v1.10) — takes a single mono baritone/banjo drone and spreads it into a wide, scale-locked stereo chord. Four pitch voices (A & C panned left, B & D right) each get their own Shift and their own staggered Delay, so the voices arrive at slightly different times for an arpeggiated, blooming feel rather than a flat block chord. Quantization keeps every voice diatonic to the chosen Key/Scale; Detune (+/-50 c) and Formant Link keep the stack thick but natural. Feed it the string source, not just vocals — that is the rig translation.

## How to play it
1. Update firmware (v1.10+) via H90 Control, then load Quadravox+ on Preset A.
2. Set Key/Scale to the song, then dial Shift A-D to the diatonic intervals you want in the chord.
3. Open Spread for stereo width; add the four staggered Delays (A shortest) plus Division for the arpeggio feel.
4. Hold a drone and let the four voices build a scale-locked chord; add Detune to thicken and keep Formant Link ON.
5. Map Glide (Rise/Fall) to a footswitch for pitch-rise swells between sections.

## Notes
- The full control list (Shift A-D, four staggered Delays + Division, Spread, Detune +/-50 c, Formant Link, Auto EQ, Glide) is published in the official Eventide manual — **but no factory knob values are published, so treat every value above as a dialable recipe, not sourced settings.** Set the intervals and delays to the song.
- Harmonizer+ postdates the bundled v1.1.4 PDF — keep firmware current (v1.10+) or the algorithm will not appear.
- Distinct from VocalShift / VocalShiftMIDI (already on disk): Quadravox+ is the diatonic 4-voice with staggered delays / arpeggio feel, not the 3-voice VocalShift.

## Sources
- research/links/eventide-h90-harmonizer-plus-vocal-algorithms.md (Quadravox+ — cdn.eventideaudio.com H90 manual harmonizer-plus, firmware v1.10)
- https://cdn.eventideaudio.com/manuals/h90/1.1.2/content/algorithms/pitch.html (Quadravox: four voices, A & C left / B & D right)
- research/H90-UsageGuide.md §2 (Quadravox+)
- provenance: official manual control list (firmware v1.10) — controls published, no factory values
