---
type: patch
title: "EXP Morph: Bed → Reverse-Crush Bloom"
device: OBNE Parting
date: 2026-06-14
description: Designed for the rig — the single defining Parting performance gesture; one expression-pedal sweep reshapes the whole downstream texture chain from a clean wash (heel) to a reverse + bit-crush + Smear-to-reverb + filter-closing chaos bloom (toe).
tags: [exp, morph, performance, reverse, bit-crush, bloom, signature, designed]
hidden:
  EXP Assignment (hold On/Off, sweep knobs — heel when pressed, toe when released; unmoved knobs unaffected; saves per preset):
    Dissolve: "12:00 → 3:00 (clean → long reverse)"
    Smear: "1:00 → 3:00 (light → lush reverb)"
    Chance: "12:00 → 2:00 (constant → old-signal feedback)"
    Filter: "1:00 → 10:00 LP (open → half-closed, darkening as it builds)"
controls:
  - { name: "Chance", type: knob, value: "12:00 (heel base)" }
  - { name: "Smear", type: knob, value: "1:00 (heel base)" }
  - { name: "Dissolve", type: knob, value: "12:00 (heel base)" }
  - { name: "Glitch", type: knob, value: "10:00 (heel base)" }
  - { name: "Filter", type: knob, value: "1:00 (heel base)" }
  - { name: "Filter", type: switch, value: "LP", options: ["LP", "HP"] }
  - { name: "Mix", type: knob, value: "11:00 (heel base)" }
  - { name: "Mix", type: switch, value: "Standard", options: ["Standard", "Modified"] }
  - { name: "Shape", type: switch, value: "Sine", options: ["Sine", "Square", "Rev Saw", "Saw", "Random Sine", "Random Square", "Envelope"] }
  - { name: "Mod", type: switch, value: "Tremolo", options: ["Tremolo", "Vibrato"] }
  - { name: "Depth", type: knob, value: "9:00 (heel base)" }
  - { name: "EXP", type: button, value: "heel→toe morph (assign per preset: hold On/Off, sweep knobs); also accepts OBNE Scooch momentary as external tap" }
  - { name: "Routing", type: switch, value: "Stereo", options: ["Mono", "Stereo-sum", "Stereo"] }
  - { name: "Trails", type: switch, value: "On", options: ["On", "Off"] }
  - { name: "Slot", type: knob, value: "Dedicate one Preset slot (EXP map is per-preset)" }
---

# EXP Morph: Bed → Reverse-Crush Bloom

## Concept
DESIGNED for this rig: the single defining Parting performance gesture — one expression-pedal sweep reshapes the entire downstream texture chain from a clean wash (heel) to a reverse + bit-crush + Smear-to-reverb + filter-closing chaos bloom (toe). This is "the EXP" the rig art wants, realized as a real-time morph controller. The multi-knob EXP map (any combination of knobs at once, saved per-preset) is the documented defining feature; this specific heel/toe assignment is DOUG's.

## How to play it
1. Set the HEEL (base) to Constant Bed values: Chance 12:00, Smear 1:00, Dissolve 12:00, Glitch 10:00, Filter 1:00 LP, Mix 11:00 Standard, Shape Sine, Tremolo, Depth 9:00. Routing Stereo, Trails ON.
2. ASSIGN the EXP map: hold On/Off, then sweep the knobs you want — heel position when pressed, toe when released; unmoved knobs are unaffected; the map saves per preset. Assign:
   - Dissolve 12:00 → 3:00 (clean → long reverse)
   - Smear 1:00 → 3:00 (light → lush reverb)
   - Chance 12:00 → 2:00 (constant → old-signal feedback)
   - Filter 1:00 → 10:00 LP (open → half-closed, darkening as it builds)
3. Perform the morph with a single expression-pedal sweep; Microcosm/QI/Dark Star re-mangle the result downstream.
4. No expression pedal? The EXP jack also accepts an OBNE Scooch momentary as an external tap.
5. Dedicate one Preset slot to the morph (the EXP map is per-preset).

## Notes
- 🟣 DESIGNED — never found. ⭐ The headline rig move: one gesture morphs the whole Board-2 wall from clean to broken in real time.
- The multi-knob EXP map (any combination at once, per-preset) is the documented defining feature; this specific heel/toe assignment is DOUG's.
- Reference: rig recipe (DeepResearch §13b — the "EXP" the rig art wants); OBNE-ecosystem expression strategy (§9).
- Save target: dedicate one Preset slot (the EXP map saves per preset).

## Sources
- 🟣 designed from `research/transcripts/harp-lady-emily-hopkins-official-parting.md` (EXP controls anything / multiple things at once)
- `research/Parting-DeepResearch.md` §2 / §4 / §13(b) (EXP maps any combination of knobs, per-preset; heel=clean / toe=reverse+crush+smear+filter morph)
- `research/Parting-UsageGuide.md` §3.
- Transformed from Pedalxly Parting-Patches.md (designed)
