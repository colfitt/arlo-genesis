---
type: patch
title: "MicroPitch — Stereo Thickener (always-on widener)"
device: Eventide H90
date: 2026-06-15
description: "The classic Eventide always-on widener — subtle dual detune (one voice slightly up, one slightly down) with short delays to fatten a clean tone and spread it wide in stereo. Sits great in front of the rig's reverb walls or as a doubling layer. Voice ranges and FLEX behavior are from the Eventide manual; the Mix-and-delay thickening rule is a Rig-Talk community rule of thumb (exact amount dialable)."
tags: [micropitch, pitch, detune, stereo, widener, chorus, always-on, community]
dips:
  FLEX: "assign to a footswitch/HotSwitch for an octave-ish dive on demand"
  DELAY: "each voice has up to 2 s of delay — also great for vocal doubling"
controls:
  - { name: "Preset A Algorithm", type: switch, value: "MicroPitch" }
  - { name: "Pitch Shift Up (A)", type: knob, value: "+7 to +9 cents (range: unison to +50 cents)" }
  - { name: "Pitch Shift Down (B)", type: knob, value: "-7 to -9 cents (range: unison to -50 cents)" }
  - { name: "Delay (per voice)", type: knob, value: "under ~100 ms for strong doubling (up to 2 s available)" }
  - { name: "Mix", type: knob, value: "~30-50% with short delays (drops to ~15-25% past ~200 ms, where detune weakens)" }
  - { name: "Tone", type: knob, value: "filters the voices — pull back if doubling sounds glassy" }
  - { name: "FLEX (Performance Parameter)", type: switch, value: "doubles both voices' pitch-shift for a dramatic dive" }
---

# MicroPitch — Stereo Thickener (always-on widener)

## Concept
The classic Eventide "always-on" widener. Two pitch voices — one a few cents up, one a few cents down — combined with short per-voice delays fatten a clean tone and spread it wide in stereo. Subtle detune (~+/-7 to +/-9 cents) thickens without sounding like an obvious chorus, so it lives well as a permanent layer in front of the rig's reverb walls, or as a doubling layer under leads/vocals. Each voice can run up to 2 s of delay, and the FLEX performance parameter can double both voices' shift for an octave-ish dive on demand.

## How to play it
1. Load MicroPitch on Preset A.
2. Set Pitch Shift Up (A) a few cents up and Pitch Shift Down (B) a few cents down — e.g. +/-7 to +/-9 cents for subtle thickening.
3. Keep delays short (under ~100 ms) and Mix around 30-50% for strong doubling.
4. Use Tone to tame brightness if the doubling sounds glassy.
5. Assign FLEX to a footswitch/HotSwitch for an octave-ish dive when you want it.

## Notes
- No published exact knob values for this recipe — treat the control values above as a dialable starting point, not sourced settings. What IS sourced: the +/-50 cent per-voice range, FLEX doubling both voices' pitch-shift, and the Tone control are from the Eventide manual. The "Mix 30-50% with short delay thickens; lower Mix / longer delay weakens the detune" guidance is a Rig-Talk community rule of thumb.
- Distinct from the existing shimmer and detuned-synth-pad seeds — this is the dry stereo widener, not a reverb tail or a synth bed.

## Sources
- https://cdn.eventideaudio.com/manuals/h90/1.1.2/content/algorithms/pitch.html (MicroPitch: +/-50 cent voices, FLEX doubles shift, Tone control)
- https://www.rig-talk.com/forum/threads/seasoned-micro-pitch-shift-users-advice-requested.329936/ (Mix 30-50 with short delay for thickening; lower mix weakens detune) *(community rule of thumb)*
- provenance: manufacturer manual + Rig-Talk MicroPitch user thread (ranges published, exact amount dialable)
