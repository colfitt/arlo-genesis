---
type: patch
title: Harmonic-Trem Cloud Catcher
device: Chase Bliss Big Time
date: 2026-06-15
description: "Designed delay slot for the 'Clean → Big Time Harmonic-Trem Cloud' chain — a clean, pitch-stable Short delay that captures the upstream harmonic-tremolo/Leslie swirl intact (limiter off, HiFi voicing) and multiplies it in time and space with MOTION Sine drift and SPREAD widen."
tags: [clean, stereo, modulated, pitch-stable, shimmer, designed]
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot; flying faders override on recall" }
  - { name: "MODE", type: switch, value: "Short", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Digital (limiter off — pitch-stable, no smear)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "HiFi (keeps the trem shimmer intact)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off (pitch-stable is the point)", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine (slow tape-style drift on the repeats)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "low ~25%" }
  - { name: "TIME", type: knob, value: "short slap-to-eighth (so a trem cycle lands inside each repeat) / tapped" }
  - { name: "CLUSTER", type: knob, value: "0–low" }
  - { name: "TILT EQ", type: knob, value: "noon" }
  - { name: "FEEDBACK", type: knob, value: "~45–55% (rhythmic cloud, not a runaway wall; nudge toward 60% for a continuous shimmer-wall climax)" }
  - { name: "WET", type: knob, value: "~40%" }
  - { name: "TEXTURE", type: knob, value: "0 (alt — no aliasing)" }
  - { name: "DIFFUSE", type: knob, value: "low (alt under FEEDBACK)" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
---

# Harmonic-Trem Cloud Catcher

## Concept
A clean, pitch-stable Short delay built to CAPTURE pre-modulated material rather than smear a flat note. Limiter off (Digital STATE) and HiFi voicing keep the upstream harmonic-tremolo/Leslie swirl from Clean intact, while MOTION Sine adds slow tape-style drift to the repeats and SPREAD widen fans the echoes wider than the source field. The result is a rhythmic, evolving cloud of shimmer that multiplies the trem in time and space without adding its own grit. Designed as the delay slot in the 'Clean → Big Time Harmonic-Trem Cloud' chain; the distinguishing trait vs. the rig's other Big Time patches is that it is deliberately CLEAN (no 0.5X crush, no Saturated/misbias) so a swirling pitch-stable source stays pitch-stable through the echoes.

## How to play it
1. Set MODE Short, STATE Digital (limiter off), VOICING HiFi, SCALE Off so the delay stays clean and pitch-stable.
2. Flip MOTION to Sine for slow drift on the repeats and SPREAD to widen to fan the echoes in stereo.
3. Tap TIME to a short slap/eighth so the upstream Clean tremolo cycle resolves inside each repeat.
4. Keep COLOR low (~25%) and FEEDBACK ~45–55% for a rhythmic, evolving cloud; push FEEDBACK toward 60% for a continuous shimmer wall.
5. Feed it a pre-modulated source (Clean harmonic-trem / Leslie) — this patch multiplies that movement, it does not create it.

## Notes
- Built as a CLEAN capture: no 0.5X crush, no Saturated/misbias — deliberately distinct from Crushed Analog and Nostalgic Repeater so a pitch-stable swirling source survives the echoes.
- Digital STATE = no limiter, which is what keeps the harmonic tremolo from being clamped/smeared.
- Numeric fader positions are a dialable recipe (designed interpretation); Chase Bliss publishes character not numbers, and flying faders override on recall.
- Pairs with Clean 'Double Tremolo (Motion + Modulated EQ + Spread)' upstream and CE-2W 'Dreamy Ambient (Slow Oceanic Bed)' at the front.

## Sources
- 🟣 designed for the 'Clean → Big Time Harmonic-Trem Cloud' chain (capture-pre-modulated-source rationale).
- Short / MOTION Sine / SPREAD-widen + Digital-no-limiter mechanics per `research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (hold-MODE clean delay, STATE limiter behavior) and the Big Time factory-preset / voicing references.
- Honesty flag: no published clock-face values — all knob settings are a dialable recipe set by ear.
