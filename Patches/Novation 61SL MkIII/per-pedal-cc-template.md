---
type: patch
title: Per-Pedal CC Template — Blooper / MOOD / Onward (deep CC control)
device: Novation 61SL MkIII
date: 2026-06-14
description: Hands-on real-time control of one CB pedal's knobs, toggles, footswitches and dip switches from the 8 encoders / 16 buttons / aftertouch — the expressive complement to whole-board scene recall.
tags: [cb-stack, deep-cc, expressive, blooper, mood, onward, community, signature]
controls:
  - { name: "Encoder 1", type: knob, value: "CC14 (TIME / SIZE)" }
  - { name: "Encoder 2", type: knob, value: "CC15 (Blooper LAYERS / MOOD MIX)" }
  - { name: "Encoder 3", type: knob, value: "CC16 (LENGTH)" }
  - { name: "Encoder 4", type: knob, value: "CC17 / CC18 (MODIFY / CLOCK)" }
  - { name: "Encoder 5", type: knob, value: "CC20 (RAMP SPEED)" }
  - { name: "Buttons (bypass)", type: button, value: "CC102 right FS / CC103 left FS / CC104 ALT-hold-both (momentary)" }
  - { name: "Buttons (retrigger)", type: button, value: "CC108 retrigger Glitch / CC109 retrigger Freeze (Onward, any value)" }
  - { name: "Aftertouch", type: knob, value: "→ a modify-depth CC" }
  - { name: "Toggles", type: switch, value: "CC21–CC23", options: ["off", "on"] }
  - { name: "TAP", type: button, value: "CC93" }
  - { name: "EOM expression sweep", type: knob, value: "CC100 (0–127)" }
  - { name: "Part Channel", type: knob, value: "That pedal's channel" }
  - { name: "Part Destination", type: switch, value: "That pedal's DIN chain", options: ["USB", "DIN1", "DIN2", "CV"] }
  - { name: "Fader Pickup", type: switch, value: "ON (standalone)", options: ["On", "Off"] }
  - { name: "Template Slot", type: knob, value: "Template slot per pedal (clone & re-channel ×7 via libslmkiii)" }
dips:
  Left bank (CC61–68): "off=0 / on=1+ (flip DRY KILL / TRAILS / ramp polarity remotely)"
  Right bank (CC71–78): "off=0 / on=1+"
hidden:
  Big Time Loop Mode footswitch CCs: "CC102–107 reassigned in Loop Mode"
---

# Per-Pedal CC Template — Blooper / MOOD / Onward (deep CC control)

## Concept
Hands-on real-time control of one CB pedal's knobs, toggles, footswitches and dip switches from the 8 encoders / 16 buttons / aftertouch — ramping Blooper LAYERS live, retriggering Onward Glitch in time, flipping a dip switch remotely. The expressive complement to the whole-board scene-recall patch: this drives one pedal deeply rather than recalling the whole stack at once.

## How to play it
1. Reuse the verified CB CC map. KNOBS = CC14–CC20 (CC20 usually RAMP SPEED): Blooper LAYERS = CC15 / RAMP = CC20; MOOD TIME=14 / MIX=15 / LENGTH=16 / MODIFY=17 / CLOCK=18; Onward SIZE=14.
2. TOGGLES = CC21–CC23. FOOTSWITCHES = CC102 right FS / CC103 left FS / CC104 ALT-hold-both / CC105 left-hold / CC106 right-hold (Big Time reassigns 102–107 in Loop Mode).
3. Onward extras: CC108 = retrigger Glitch, CC109 = retrigger Freeze (any value — great clock-quantized re-triggers).
4. DIPS = CC61–68 (left bank) / CC71–78 (right bank), off=0/on=1+ (flip DRY KILL, TRAILS, ramp polarity remotely). TAP = CC93; EOM expression sweep = CC100 (0–127).
5. TEMPLATE LAYOUT (Components): enc1=CC14, enc2=CC15, enc3=CC16, enc4=CC17/18, enc5=CC20 RAMP; buttons = CC102/103 bypass toggles + CC104 ALT + CC108/109 retrigs (momentary); aftertouch → a modify-depth CC. Set Low/High to scale; toggle vs momentary per control.
6. PART Channel = that pedal's channel; Destination = its DIN chain.

## Notes
- Build-your-own (no factory CB template).
- Which footswitch CC maps to what is pedal-specific — check each pedal's own CC table before relying on a bypass mapping.
- CB CC layout is highly consistent → author one template, clone the rest (libslmkiii).

## Sources
- REUSED Gear/Chase Bliss Blooper/research/links/cb-stack-preset-scene-recall.md §4–5 (verified CC map) + int-recipe-cb-stack-pedals.md.
- Ref: Rig — CB stack.
- Transformed from Pedalxly 61SL-MkIII-Patches.md (community)
