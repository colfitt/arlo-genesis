---
type: patch
title: Carry-on Shimmer Wash (Doom)
device: UAFX Del-Verb
date: 2026-06-14
description: The signature travel patch — a doom-leaning wall of sound (dark 224 Hall wash + hi-cut ping-pong delay) for baritone Jazzmaster or guitar on a minimal fly board. Post-punk/Swans-style sustained crescendo wall.
tags: [ambient, drone, doom, wall-of-sound, baritone, travel, designed, signature, post-punk]
controls:
  - { name: "Reverb Model", type: switch, value: "Hall 224", options: ["Spring '65", "Plate 140", "Hall 224"] }
  - { name: "Reverb voicing (app-assigned)", type: switch, value: "Dark N Dusty Trail (224 Large Hall B, lots of pre-delay — dark, distant)" }
  - { name: "Reverb", type: knob, value: "1:00–2:00 (big)" }
  - { name: "Delay Model", type: switch, value: "Precision", options: ["Tape EP-III", "Analog DMM", "Precision"] }
  - { name: "Delay voicing (app-assigned)", type: switch, value: "Stereo Ping Pong Hi-Cut (3.5 kHz LPF + 130 Hz HPF in feedback loop)" }
  - { name: "Delay Time", type: knob, value: "dotted-1/8 (tap/clock to song)" }
  - { name: "Feedback", type: knob, value: "1:00–2:00" }
  - { name: "Mix", type: knob, value: "noon" }
  - { name: "Color", type: knob, value: "slightly left (Precision Color = tone; left cuts treble → darker)" }
  - { name: "Mod", type: knob, value: "noon (off — bipolar, noon = off)" }
  - { name: "Trails", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "Footswitch Mode", type: switch, value: "Delay | Tap (reverb always-on wash, left foot drops delay, right foot taps)" }
---

# Carry-on Shimmer Wash (Doom)

## Concept
The closest the Del-Verb gets to the home wall-of-sound, packed onto a carry-on board. A dark, distant 224 Large Hall ("Dark N Dusty Trail") is the always-on wash; a hi-cut stereo ping-pong delay fills the space underneath without mudding it (3.5 kHz LPF + 130 Hz HPF live in the feedback loop). On a baritone Jazzmaster it leans doom — sustained, heavy, post-punk crescendo territory.

## How to play it
1. Pre-assign the voicings in the UAFX Control app over Bluetooth: Reverb toggle "Dark N Dusty Trail" on Hall 224, Delay toggle "Stereo Ping Pong Hi-Cut" on Precision. These store in the pedal so it plays phone-free.
2. Set the reverb as the always-on wash (Reverb knob 1:00–2:00). Leave it running.
3. Use the left footswitch to drop the delay in/out; tap the right footswitch to set the dotted-eighth to the song tempo.
4. Swell into chords and let the dark hall build the crescendo.

*Optional MIDI recall:* CC14=2 (Precision) → CC15=Hall **first**, then CC25=1 (dotted-1/8), CC24≈75, CC22≈64, CC28≈95 — send ~50 ms apart.

## Notes
- On baritone, watch Feedback near self-oscillation: **runaway goes subsonic fast and survives bypass — only Feedback-to-min kills it.**
- Keep both Mix and Reverb below full clockwise on a series board: full CW = kill-dry (100% wet), which mutes your dry tone on a series chain.
- Color is "slightly left" by design (darker wash); nudge further left for more doom, toward noon for less.

## Sources
- designed from manual (Color-as-tone on Precision, Mod-noon-off, kill-dry, runaway) + UA Preset & Voicing Lists ("Dark N Dusty Trail," "Stereo Ping Pong Hi-Cut") — `research/links/voicing-list-official.md`, `research/links/tips-power-user-hidden-behaviors.md`, `research/links/midi-official-manual-cc-chart.md`, `research/links/settings-midi-and-controls.md`
- Ref: Post-punk / experimental cluster — Swans-style sustained crescendo wall; baritone weight
- Transformed from Pedalxly Del-Verb-Patches.md (DOUG-designed)
