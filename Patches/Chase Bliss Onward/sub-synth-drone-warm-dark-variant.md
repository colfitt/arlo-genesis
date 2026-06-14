---
type: patch
title: Sub-Synth Drone (warm/dark variant)
device: Chase Bliss Onward
date: 2026-06-14
description: Infinite sub-octave drone with a warmer, darker character — banjo/baritone pushed into a pad it physically can't hold.
tags: [drone, sub, dark, warm, doom, banjo, baritone, designed, signature]
hidden:
  SENSITIVITY (on SIZE): toward LESS (so the hot GK-5 doesn't grab string clicks)
controls:
  - { name: "Channel", type: switch, value: "FREEZE", options: ["FREEZE", "GLITCH"] }
  - { name: "OCTAVE", type: knob, value: "hard left (down/half)" }
  - { name: "SUSTAIN", type: knob, value: "max" }
  - { name: "FADE", type: switch, value: "Slow", options: ["Slow", "Mid", "Fast", "User"] }
  - { name: "TEXTURE", type: knob, value: "right (soft-clip OD, warmer/darker pad)" }
  - { name: "FREEZE footswitch", type: button, value: "hold to lock = infinite sub" }
  - { name: "Slot/Bank", type: knob, value: "build into L as a variant of Sub Synth, or audition live" }
---

# Sub-Synth Drone (warm/dark variant)

## Concept
Infinite sub-octave drone with a warmer, darker character — banjo or baritone pushed into a pad it physically can't hold. Extends the manual's Sub Synth for this rig: OCTAVE hard-left for the down/half voice, SUSTAIN maxed and FADE slow for an infinite hold, plus TEXTURE-right (soft-clip OD) for a warmer, darker pad. Aaron Rusch singles out TEXTURE-right as his favorite "warmer/darker" setting.

## How to play it
1. Set the channel to **FREEZE**.
2. **OCTAVE hard left** (down/half) + **SUSTAIN max** + **FADE = Slow**.
3. **Hold FREEZE** to lock = infinite sub-drone.
4. Push **TEXTURE right** (soft-clip OD) for a warmer, darker pad.
5. In the hidden menu, dial **SENSITIVITY (on SIZE) toward LESS** for the hot GK-5 so it doesn't grab string clicks.

## Notes
- TEXTURE-right = "warmer/darker" is a verified Aaron Rusch observation (his favorite setting); the full chain extends the manual's Sub Synth for this rig.
- The OCTAVE/SUSTAIN/FADE/hold-to-lock mechanic is manual/Aaron-Rusch verified; the banjo/baritone framing is the rig inference.

## Sources
- designed from UsageGuide §2/§5 + `research/transcripts/aaron-rusch-onward-freeze-channel.md` + manual Sub Synth (p.24)
- Transformed from Pedalxly Onward-Patches.md (designed)
