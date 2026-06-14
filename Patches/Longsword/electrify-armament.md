---
type: patch
title: Electrify Armament
device: Longsword
date: 2026-06-14
description: The disciplined "Wall" event — stacked AFTER the Hizumitas + Brothers AM fuzz wall with no-diode Center mode and Drive at minimum, so the Longsword is a tone-shaper, not added gain.
tags: [stacked, wall, eq, no-diode, intensifier, factory, signature]
controls:
  - { name: "Level", type: knob, value: "~1:00 (unity-plus, rebalance by ear)" }
  - { name: "Drive", type: knob, value: "MINIMUM (~7:00)" }
  - { name: "Low", type: knob, value: "to taste (cut ~10:00 to tame fuzz flub)" }
  - { name: "High", type: knob, value: "to taste" }
  - { name: "Mid", type: knob, value: "to taste (carve the cut; SHIFT-up)" }
  - { name: "Boost", type: knob, value: "set as the live intensifier" }
  - { name: "DIODE", type: switch, value: "center (no diodes)", options: ["up (MOSFET)", "center (no diodes)", "down (silicon)"] }
  - { name: "SHIFT", type: switch, value: "up (1 kHz)", options: ["up (1 kHz)", "down (300 Hz)"] }
  - { name: "Boost (footswitch)", type: button, value: "the live grit stomp / intensifier" }
---

# Electrify Armament

## Concept
EAE's OWN endorsement of the rig's stacked-intensifier approach: no-diode Center mode (minimal compression, max dynamics) + Drive at minimum + the Boost footswitch as the grit stomp. The canonical way to stack on the fuzz without piling compression on compression — the Longsword acts as a studio EQ with a footswitchable second distortion channel rather than added gain.

## How to play it
1. DIODE center (no diodes), Drive at minimum (~7:00) — the Hizumitas already has the gain.
2. Set Level for unity-plus (~1:00) and rebalance by ear (Center mode gets loud).
3. Use Low/High/Mid as a studio EQ; cut Low ~10:00 to tame fuzz flub; carve a cut with Mid + SHIFT-up.
4. Use the **Boost footswitch as the actual intensifier** at the climax.

## Notes
- Rebalance Level entering Center mode — it gets extremely loud at higher Drive and its dynamic range can run out.
- In Center mode at high gain the tone controls are more effective cutting than boosting — sculpt by subtraction.
- Use silicon (DIODE down) instead when you want the whole front end fused into one squared-off slab.

## Sources
- EAE V4.5 Technical Manual (Rev A), factory preset (e) — `Gear/Longsword/research/links/eae-manual-presets.md`
- Transformed from Pedalxly Longsword-Patches.md (factory)
