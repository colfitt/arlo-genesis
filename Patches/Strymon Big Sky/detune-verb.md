---
type: patch
title: "\"Detune Verb\" — ±10-cent detuned shimmer (the manual's trick)"
device: Strymon Big Sky
date: 2026-06-14
description: Beautifully detuned reverb — lush thickening and on-aesthetic warble; the manual's ±10-cent Shimmer detune trick baked into a factory slot (-10 CEN / +10 CEN in INPUT, Decay 4.96 S, INFINITE).
tags: [shimmer, detune, lush, warble, factory, signature]
hidden:
  Shift1: -10 CEN
  Shift2: +10 CEN
  Mode: INPUT
  HOLD: INFINITE
controls:
  - { name: "Machine", type: switch, value: "SHIMMER", options: ["Cloud","Shimmer","Bloom","Chorale","Swell","Magneto","Nonlinear","Reflections","Room","Hall","Plate","Spring"] }
  - { name: "DECAY", type: knob, value: "4.96 S" }
  - { name: "MOD", type: knob, value: "off (manual's pure-detune variant)" }
  - { name: "MIX", type: knob, value: "dial-art (not captured)" }
  - { name: "TONE", type: knob, value: "dial-art (not captured)" }
  - { name: "PRE-DELAY", type: knob, value: "dial-art (not captured)" }
  - { name: "Slot/Bank", type: knob, value: "26C-alt / 28C (factory + manual)" }
---

# "Detune Verb" — ±10-cent detuned shimmer (the manual's trick)

## Concept
The manual's detune trick as a factory slot: Shimmer with voice 1 at -10 cents and voice 2 at +10 cents, in INPUT mode. The tiny opposed detunes thicken the reverb into a lush, warbling wall instead of an obvious octave. Pairs with Hammock's "more warble" philosophy.

## How to play it
1. Hold a chord; the ±10-cent voices thicken the tail with warble.
2. The factory slot uses Decay 4.96 S with HOLD = INFINITE for a sustained detuned wall.
3. For the manual's pure-detune variant, keep the same Shifts in INPUT but turn MOD off for a clean detuned reverb.

## Notes
- Shift1/Shift2/Mode/Decay/HOLD are exact and cited. MIX/TONE/PRE-DELAY are dial-art (not captured).
- Two flavors: factory slot (INFINITE, default Mod) vs manual variant (MOD off for pure detune).

## Sources
- research/links/strymon-bigsky-factory-presets.md (factory 26C "Detune Verb")
- research/Big-Sky-DeepResearch.md §3 (BigSky_UserManual_RevD.pdf)
- Transformed from Pedalxly Big-Sky-Patches.md (factory)
