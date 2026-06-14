---
type: patch
title: Cluster drone — hand-built wide detuned wall
device: TE OP-1 Field
date: 2026-06-14
description: A by-ear wide detuned Cluster drone wall dialed from scratch control-by-control, since op1.fun hides the numeric knobs.
tags: [drone, pad, lush, cluster, doom, designed, signature]
controls:
  - { name: "Engine", type: switch, value: "Cluster", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "T2 Blue (Attack)", type: knob, value: "high" }
  - { name: "T2 Orange (Release)", type: knob, value: "high" }
  - { name: "Blue (# of waves)", type: knob, value: "near max (thick)" }
  - { name: "Green (wave envelope)", type: knob, value: "toward CW (slow upward bloom)" }
  - { name: "White (spread)", type: knob, value: "high (wide drift)" }
  - { name: "Orange (unitor)", type: knob, value: "low-moderate (slow wobble)" }
  - { name: "Octave", type: knob, value: "-1/-2 (doom weight)" }
  - { name: "FX", type: switch, value: "nitro (saturation)" }
  - { name: "Slot/Bank", type: knob, value: "Cluster slot [2]" }
---

# Cluster drone — hand-built wide detuned wall

## Concept

A DOUG-designed, control-by-control build path for a wide detuned Cluster drone wall when you want to dial it from scratch — op1.fun hides the numeric knobs, so this is the build recipe. Thick supersaw (# of waves near max), slow upward bloom (wave envelope CW), wide drift (spread high), and a slow wobble (unitor low-moderate), dropped to −1/−2 for doom weight with Nitro saturation on top.

## How to play it

1. Select the Cluster engine.
2. **T2 envelope:** Blue (Attack) high, Orange (Release) high — long bloom and long tail.
3. **Engine page:** Blue "# of waves" near max (thick), Green "wave envelope" toward CW (slow upward bloom), White "spread" high (wide drift), Orange "unitor" low-moderate (slow wobble).
4. Set Octave −1 or −2 for doom weight.
5. Add **Nitro** FX for saturation.
6. Latch a held note/chord with the **Hold** sequencer and play a lead over it.

## Notes

- Cluster encoder labels (# of waves / wave envelope / spread / unitor) are community reverse-engineering (op-101 blog), not TE docs — directionally reliable, not gospel.
- This is the build path because op1.fun hides the numeric knobs; tune by ear.

## Sources

- designed from op-101 Cluster encoder map (http://op-101.blogspot.com/2011/09/cluster-description.html) + planks/tlorach patches
- Transformed from Pedalxly OP-1-Field-Patches.md (DOUG-designed)
