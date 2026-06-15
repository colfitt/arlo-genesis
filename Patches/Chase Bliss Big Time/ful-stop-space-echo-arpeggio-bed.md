---
type: patch
title: "\"Ful Stop\" Space-Echo Arpeggio Bed"
device: Chase Bliss Big Time
date: 2026-06-14
description: Track-B emulation of Radiohead's "Ful Stop" (A Moon Shaped Pool) — Big Time covers the Boss RE-20 Space Echo role (short, dark, dotted tape echo) under the synth wash arpeggios.
tags: [taste-profile, radiohead, space-echo, tape, arpeggio, designed, signature]
hidden:
  CC54 subdivision: "dotted-8th or quarter, clock-locked"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot via CC27" }
  - { name: "MODE", type: switch, value: "Short", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Saturated (RE-20 tape-echo warmth) or Compressed", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Warm", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine (the Space Echo's tape wobble)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "0.5X", type: switch, value: "OFF", options: ["off", "on"] }
  - { name: "COLOR", type: knob, value: "~40% (tape-echo darkening on repeats)" }
  - { name: "TIME", type: knob, value: "dotted-8th or quarter, clock-locked" }
  - { name: "CLUSTER", type: knob, value: "~25% (a couple of taps, not a wall — the arp does the rhythm)" }
  - { name: "TILT EQ", type: knob, value: "slightly below noon (RE-20 darkens the top)" }
  - { name: "FEEDBACK", type: knob, value: "~45% (a few warm repeats)" }
  - { name: "WET", type: knob, value: "~35% (sits under the wash)" }
  - { name: "TEXTURE", type: knob, value: "~30% (alt)" }
  - { name: "DIFFUSE", type: knob, value: "low-mid (alt under FEEDBACK)" }
  - { name: "RATE", type: knob, value: "slow (alt under TIME — Space Echo flutter)" }
  - { name: "DEPTH", type: knob, value: "moderate (alt under CLUSTER — Space Echo flutter)" }
  - { name: "SPREAD", type: switch, value: "widen", options: ["off", "widen", "ping-pong"] }
---

# "Ful Stop" Space-Echo Arpeggio Bed

## Concept
Track-B emulation of the back half of Ful Stop — Jonny's "good phasing arpeggios" through a Boss RE-20 Space Echo riding under the synth wash. Big Time covers the RE-20 role: short, dark, dotted tape echo. Saturated/Warm/Sine gives the warm tape-slap character; modest CLUSTER keeps it to a couple of taps so the arpeggio does the rhythm. **Designed-to-emulate** — no Big Time artist setting is documented, and Radiohead never used a Big Time.

## How to play it
1. Set TIME to **dotted-8th or quarter**, clock-locked.
2. Keep WET low (~35%) — in Ful Stop the arpeggio delay is a *bed under* the Moog/Prophet wash, never the front.
3. Pair with a VG-800/OP-1 detuned-unison pad for the synth half.
4. The actual phaser swirl lives upstream (H90 phaser block / Caroline Somersault — there's no Big Time phaser).

## Notes
- Warm + Sine + modest CLUSTER = the warm tape-slap character of the RE-20.
- Keep WET low so the delay stays under the wash, not in front.
- Numeric fader positions are designed starting points; on recall the flying faders override these.

## Sources
- 🟣 designed from `Research/Taste-Profile/sources/ful-stop-synth-wash-phasing-arpeggios.md` (RE-20 Space Echo + Small Stone arpeggios under the wash) + manual control reference (Saturated/Warm/Sine = tape-echo voicing).
- Ref: Radiohead — "Ful Stop" (A Moon Shaped Pool, 2016): EHX Small Stone arpeggios → Boss RE-20 Space Echo under the Moog/Prophet/Juno unison wash.
- Transformed from Pedalxly Big-Time-Patches.md (designed)
