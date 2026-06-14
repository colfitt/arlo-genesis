---
type: patch
title: Stereo Pinging Phaser (Bounce Sweep)
device: Chase Bliss Lost & Found
date: 2026-06-14
description: Community patch (Mark Johnston "Secret Weapons") — a hands-free evolving stereo phaser where an armed BOUNCE sweeps the pole count min↔max for intermittent stereo pinging; a motion/"random"-leaning texture for the Microcosm that isn't another reverb.
tags: [phaser, motion, stereo, modulation, community]
dips:
  SPREAD: on
  TRAILS: on
hidden:
  "Control-bank ramp/bounce (BOUNCE)": "armed on L MODIFY — pole count oscillates min↔max continuously"
controls:
  - { name: "ROUTING", type: switch, value: "single channel", options: ["single", "L+R"] }
  - { name: "L slot mode", type: switch, value: "3A Pinging Phaser" }
  - { name: "TIME (LFO speed)", type: knob, value: "11:00" }
  - { name: "MODIFY (pole count)", type: knob, value: "the swept param (2–64 poles)" }
  - { name: "ALT (feedback)", type: knob, value: "1:00 (needs some feedback to speak)" }
  - { name: "MIX (RAMP) = ramp/bounce SPEED", type: knob, value: "slow = intermittent stereo pinging, fast = aggressive" }
  - { name: "FREEZE (HOLD)", type: button, value: "PAUSE — freezes the LFO so you can set poles (2–64) by hand" }
  - { name: "Slot/Bank", type: knob, value: "Preset bank 2 (BANK dip)" }
---

# Stereo Pinging Phaser (Bounce Sweep)

## Concept
A hands-free evolving stereo phaser from Mark Johnston's "Secret Weapons" walkthrough. Mode 3A (Pinging Phaser) runs with an armed BOUNCE on the L MODIFY knob so the pole count sweeps min↔max continuously, throwing "intermittent stereo pinging." It's a motion/random-leaning texture for the Microcosm that isn't yet another reverb. With BOUNCE armed, the MIX (RAMP) knob sets the ramp/bounce speed.

## How to play it
1. Set ROUTING to single channel, load 3A Pinging Phaser on the L slot.
2. SPREAD on (essential for the stereo effect).
3. Set TIME (LFO speed) ~11:00, ALT (feedback) ~1:00 (it needs some feedback to speak).
4. **Arm BOUNCE** on the L MODIFY knob (Control-bank ramp/bounce dip) so the pole count oscillates min↔max.
5. The **MIX (RAMP)** knob now sets the bounce **SPEED** — slow = intermittent stereo pinging, fast = aggressive.
6. **HOLD = PAUSE** freezes the LFO so you can dial poles (2–64) by hand.

## Notes
- Demoed on **beta firmware**, but the phaser/ramp engines are **not** the ones that changed (only synth/resonator did).
- Changing poles while playing throws "not-intentional but very cool" artifacts — on-aesthetic.
- MIDI clock-syncing the LFO is **not** useful (fastest sync = once/beat); use the free LFO or bounce instead.

## Sources
- Mark Johnston "Secret Weapons" — "3A SPREAD on, arm BOUNCE on the left MODIFY so the pole count sweeps min↔max; slow ramp = intermittent stereo pinging, fast = aggressive" — `research/transcripts/secret-weapons-mark-johnston-walkthrough.md`
- Phaser map (TIME = LFO speed, MODIFY = poles 2–64, ALT = feedback, HOLD = PAUSE freezes LFO; changing poles while playing = happy-accident artifacts) from BachelorMachinesTV Pt1 — `research/transcripts/bachelormachinestv-science-part1.md`
- Ref: Mark Johnston "Secret Weapons" — stereo pinging phaser via ramp
- Transformed from Pedalxly Lost-and-Found-Patches.md (community)
