---
type: patch
title: Ondes-Martenot Bowed-Swell (banjo intensity key)
device: Chase Bliss Clean
date: 2026-06-14
description: Emulates Jonny Greenwood's Ondes-Martenot intensity-key swell (Kid A) on the banjo-as-lead voice — Clean's Dynamic Swell makes a hard banjo pluck "bow in" like a violin so the line sings.
tags: [swell, ambient, radiohead, art-rock, lead, designed, signature]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: "off (momentary) — ON for a toggle"
  Spread: off
  MISO: off
hidden:
  Swell In time (Wet knob): "~noon-1:00 (slowish bowed attack)"
  Swell Out time (Dry knob): "~noon (graceful decay)"
controls:
  - { name: "AUX footswitch", type: button, value: "Dynamic Swell (default momentary; flip LATCH dip for a toggle)" }
  - { name: "Sensitivity", type: knob, value: "by left LED — sets the trigger point so soft notes don't auto-trigger, only intended notes bow in" }
  - { name: "Dynamics", type: knob, value: "gentle (~10:00)" }
  - { name: "EQ", type: knob, value: "noon (let the time boards color it)" }
  - { name: "Wet", type: knob, value: "noon (main page) — repurposed as Swell In ~noon-1:00 on hidden page" }
  - { name: "Dry", type: knob, value: "noon (main page) — repurposed as Swell Out ~noon on hidden page" }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "Mid (stable)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
  - { name: "Slot/Bank", type: knob, value: "MIDDLE 'live' slot, or a banjo-lead-scene preset (MIDI-recallable)" }
---

# Ondes-Martenot Bowed-Swell (banjo intensity key)

## Concept
A designed-to-emulate Track-B patch for Jonny Greenwood's Ondes-Martenot lead feel ("How to Disappear Completely," "The National Anthem," Kid A). The Ondes' intensity key shapes attack and decay in real time like a violin bow; Clean's Dynamic Swell does precisely that to a plucked source, making a hard banjo pluck *bow in* instead of strike so the line "sings" the way Jonny describes the Ondes ("nothing closer to singing"). Clean is a dynamics unit, so this swell gesture is exactly its lane — the rest of the Radiohead palette lives downstream.

## How to play it
1. **Engage the AUX footswitch** (Dynamic Swell, default momentary; flip the LATCH dip for a toggle). Signal swells in when playing crosses the Sensitivity threshold, swells out below it.
2. **Hidden Options** (hold both footswitches): Wet = Swell In time ~noon–1:00 (slowish bowed attack), Dry = Swell Out time ~noon (graceful decay).
3. Set Sensitivity by the left LED — so soft notes don't auto-trigger, only intended notes bow in.
4. Dynamics gentle (~10:00); EQ noon (let the time boards color it); Mode MID; Physics MID.
5. Feed the bowed banjo into **Big Time TB3 (Ondes Lead Delay)** for the long singing tail; add VG-800 portamento for the ribbon-glide pitch.

## Notes
- The honest fit: the Ondes is defined by its *dynamic swell + glide* — the swell half is exactly what Clean does. The glide/vibrato come from the VG-800; the long tail from Big Time.
- Don't over-compress underneath — keep the attack able to bow in cleanly.
- Designed-to-emulate (no artist setting); approximate values, dial by feel against the LED.

## Sources
- 🟣 designed from `Research/Taste-Profile/sources/kingofgear-radiohead-synths-ondes.md` (intensity key = bowed real-time attack/decay, "like singing")
- Dynamic Volume Swell (Patch 12) — Wet = Swell In, Dry = Swell Out
- Ref: Radiohead / Jonny Greenwood — Ondes Martenot leads, "How to Disappear Completely" & "The National Anthem" (Kid A): intensity-key swell shapes attack like a violin bow
- Transformed from Pedalxly Clean-Patches.md (designed)
