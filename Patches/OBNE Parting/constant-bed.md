---
type: patch
title: Constant Bed (Tame-It Baseline)
device: OBNE Parting
date: 2026-06-14
description: The reliable, surprise-free starting point — a characterful but predictable delay-into-reverb that sits under everything and feeds steady material downstream; the home base to return to when chance chaos gets unmusical.
tags: [ambient, bed, texture, baseline, low-drama, community]
controls:
  - { name: "Chance", type: knob, value: "12:00" }
  - { name: "Smear", type: knob, value: "1:00" }
  - { name: "Glitch", type: knob, value: "10:00" }
  - { name: "Time", type: knob, value: "12:00" }
  - { name: "Dissolve", type: knob, value: "12:00" }
  - { name: "Filter", type: knob, value: "1:00" }
  - { name: "Filter", type: switch, value: "LP", options: ["LP", "HP"] }
  - { name: "Mix", type: knob, value: "11:00" }
  - { name: "Mix", type: switch, value: "Standard", options: ["Standard", "Modified"] }
  - { name: "Shape", type: switch, value: "Sine", options: ["Sine", "Square", "Rev Saw", "Saw", "Random Sine", "Random Square", "Envelope"] }
  - { name: "Mod", type: switch, value: "Tremolo", options: ["Tremolo", "Vibrato"] }
  - { name: "Rate", type: knob, value: "11:00" }
  - { name: "Depth", type: knob, value: "9:00" }
  - { name: "Time-Subdivision", type: knob, value: "quarter (default, hold Aux + Time)" }
  - { name: "Routing", type: switch, value: "Stereo", options: ["Mono", "Stereo-sum", "Stereo"] }
  - { name: "Trails", type: switch, value: "On", options: ["On", "Off"] }
  - { name: "Slot", type: knob, value: "Preset 1 (safe home base)" }
---

# Constant Bed (Tame-It Baseline)

## Concept
The reliable, surprise-free starting point for Parting — a characterful but predictable delay-into-light-reverb that sits under everything and feeds steady material downstream (Lost & Found / Microcosm / Dark Star). With Chance at noon the trigger is constant (no random feedback) and Glitch below noon keeps the clock fixed, so the output stays musical and repeatable. This is the setting to return to when chance chaos gets unmusical.

## How to play it
1. Set the global rig defaults: Routing = full Stereo (hold On/Off + tap Preset to the 3rd LED), Trails ON, Aux = Tap Tempo.
2. Dial Chance to noon and Glitch below noon — this gives the constant, fixed-clock behavior that makes the bed predictable.
3. Smear at 1:00 diffuses the delay toward light reverb; keep Depth low (9:00) for subtle movement only.
4. Save to Preset 1 as your safe home base.

## Notes
- This is the "sit-in-a-mix" use Parting is least naturally suited to — deliberately low-drama.
- Clock values are INFERRED translations of documented directions; no source publishes exact numbers.
- Save target: Preset 1 (only 3 onboard slots; everything else lives in MIDI slots / live mode).

## Sources
- 🔵 `research/links/parting-named-sound-recipes.md` (recipe #6, per manual behavior)
- `research/transcripts/obne-dan-explains-it-all-parting.md` (Chance noon = constant; Glitch below noon = fixed clock)
- DeepResearch §13(a). Exact clocks INFERRED.
- Transformed from Pedalxly Parting-Patches.md (community — control-direction recipe, exact clocks inferred)
