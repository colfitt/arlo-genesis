---
type: patch
title: Lo-Fi Rhythmic Groove
device: Chase Bliss Big Time
date: 2026-06-14
description: A multi-tap groove locked to DT2/MPC MIDI clock — the live workhorse rhythmic delay that becomes the body of a song.
tags: [lo-fi, rhythmic, clock-locked, multi-tap, designed, signature]
hidden:
  CC54 subdivision: "dotted-8th / 16th (or Options → hold SCALE → TIME)"
  CC111 clock ignore: "0 (follow / slave to MIDI clock)"
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot via CC27; recall by PC on DT2 pattern change" }
  - { name: "MODE", type: switch, value: "Short", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Compressed (punchy, articulate in a dense mix)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Focus (or Warm for darker)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Off (or Sine subtle)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "0.5X", type: switch, value: "ON (built-in lo-fi crush)", options: ["off", "on"] }
  - { name: "COLOR", type: knob, value: "~40%" }
  - { name: "TIME", type: knob, value: "MIDI clock (slave) — subdivision via CC54" }
  - { name: "CLUSTER", type: knob, value: "~⅓–½ (multi-tap pattern = the groove)" }
  - { name: "TILT EQ", type: knob, value: "slightly up" }
  - { name: "FEEDBACK", type: knob, value: "~35% (articulate, not washy)" }
  - { name: "WET", type: knob, value: "~40%" }
  - { name: "TEXTURE", type: knob, value: "~40% (alt — gentle comp)" }
  - { name: "DIFFUSE", type: knob, value: "low (alt under FEEDBACK)" }
  - { name: "SPREAD", type: switch, value: "widen (or ping-pong for the added taps)", options: ["off", "widen", "ping-pong"] }
---

# Lo-Fi Rhythmic Groove

## Concept
A clock-locked multi-tap groove — the body of a song carried on one delay. Slaved to DT2/MPC MIDI clock, with CLUSTER set as the "free arrangement" fader generating the multi-tap rhythmic pattern. Compressed STATE keeps the taps punchy and articulate in a dense mix; the 0.5X crush supplies the lo-fi color.

## How to play it
1. Slave to MIDI clock: set **CC111 = 0** (clock ignore off, so the pedal follows).
2. Set the subdivision via **CC54** (dotted-8th / 16th), or use Options → hold SCALE → TIME.
3. Dial CLUSTER to ⅓–½ to set the multi-tap pattern — this is the groove.
4. P-lock COLOR/TIME/etc. via **CC14–19** from the DT2 for grid-quantized moves on pattern changes.
5. Save to a free internal slot via CC27 and recall by PC when the DT2 pattern changes.

## Notes
- Compressed keeps the multi-taps punchy; CLUSTER is the "free arrangement" fader here.
- ⚠️ MPC Sample distorts when slaved on fw 1.2.1 — run MPC as master (Big Time follows) or verify the 1.3.x fix.

## Sources
- 🟣 designed from `research/links/centerpiece-big-time-as-song-centerpiece-one-pedal.md` §5 (rhythmic-centerpiece recipe, [R]) + `centerpiece-minimal-chains-and-sampler-integration.md` §C (clock sync CC54/CC111, p-lock CC14–19) + `research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (CLUSTER multi-tap zones).
- Transformed from Pedalxly Big-Time-Patches.md (designed)
