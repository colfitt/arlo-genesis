---
type: patch
title: Banjo-Lead Wall
device: Longsword
date: 2026-06-14
description: Banjo (Gold Tone EBM-5 + GK-5 → VG-800) carrying a lead line on top of the fuzz wall — adds the low-mid body a banjo lacks while taming its 2-4 kHz pierce.
tags: [banjo, lead, body, mid-boost, designed, signature]
controls:
  - { name: "Level", type: knob, value: "~noon (rebalance for unity-plus)" }
  - { name: "Drive", type: knob, value: "~11-12:00" }
  - { name: "Low", type: knob, value: "noon" }
  - { name: "High", type: knob, value: "~11:00 (ease the pierce)" }
  - { name: "Mid", type: knob, value: "boosted ~2:00 (the body move)" }
  - { name: "Boost", type: knob, value: "set (footswitch OFF, or ON to ride a louder lead)" }
  - { name: "DIODE", type: switch, value: "center (no diodes) or up (MOSFET) for evened attack/decay", options: ["up (MOSFET)", "center (no diodes)", "down (silicon)"] }
  - { name: "SHIFT", type: switch, value: "down (300 Hz)", options: ["up (1 kHz)", "down (300 Hz)"] }
  - { name: "Boost (footswitch)", type: button, value: "OFF (or ON to ride a louder lead, accepting its 300 Hz tightening)" }
---

# Banjo-Lead Wall

## Concept
Banjo-as-lead tie-breaker + indie-folk banjo-bed body. The 300 Hz mid-boost is the single most flattering dirt move in the rig for the banjo's missing body; the High cut plus Drive's built-in high rolloff kill the ice-pick. Center keeps the pluck dynamic; MOSFET smooths it for sustained lines.

## How to play it
1. DIODE center (no diodes — pluck attack reads) or up (MOSFET) if you want attack/decay evened.
2. Drive ~11-12:00, Mid SHIFT-down (300 Hz) boosted ~2:00, High ~11:00 to ease the pierce, Low at noon.
3. Boost footswitch OFF (or ON to ride a louder lead, accepting its 300 Hz tightening).
4. Rebalance Level (~noon) for unity-plus.

## Notes
- If still too bright, pick a darker VG-800 amp/cab model.
- Drive's built-in high-end rolloff keeps it from getting ice-picky at gain.
- Designed patch — knob positions are starting points, dial by ear.

## Sources
- designed from `Longsword-UsageGuide.md` §5 (banjo-lead recipe) + factory *Great Weapon Fighting* (300 Hz mid-boost) + the manual's Drive-rolloff / SHIFT-down-clarify notes (`eae-manual-presets.md`)
- Transformed from Pedalxly Longsword-Patches.md (designed)
