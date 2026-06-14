---
type: patch
title: Clock-Synced Loop Layer + bass/baritone sub-drone (rig patch d)
device: Chase Bliss MOOD MkII
date: 2026-06-14
description: An in-time loop locked to the rig and committed to Blooper, plus a sub-drone from bass/baritone without thinning the fundamental. (DOUG-designed; SYNC/MIDI are factory features, knob feels inferred.)
tags: [sync, midi-clock, delay, tape, sub-drone, rig-integration, designed, signature]
hidden:
  SYNC (Wet MODE toggle): LEFT — Micro-Looper synced to Wet
controls:
  - { name: "Looper MODE", type: switch, value: "Tape (LENGTH set by CLOCK)", options: ["Env", "Tape", "Stretch"] }
  - { name: "Wet MODE", type: switch, value: "Delay", options: ["Reverb", "Delay", "Slip"] }
  - { name: "Wet TIME", type: knob, value: "a quarter-note feel" }
  - { name: "Wet MODIFY", type: knob, value: "1:00 (piling repeats)" }
  - { name: "CLOCK", type: knob, value: "sets loop length; keep HIGHER for the sub-drone variant to preserve low-end" }
  - { name: "Looper MODIFY (sub-drone variant)", type: knob, value: "octave-down" }
  - { name: "MIDI clock (CC51 follow / CC53 / CC54)", type: switch, value: "feed from the rig master to lock to Big Time / Blooper" }
---

# Clock-Synced Loop Layer + bass/baritone sub-drone (rig patch d)

## Concept
An in-time loop locked to the rig and committed to Blooper; plus a sub-drone from bass/baritone without thinning the fundamental. Tape loop length set by CLOCK with SYNC tying the Micro-Looper to the Wet Delay, fed by MIDI clock so the loop locks to the rig and can be captured in time then committed downstream.

## How to play it
1. Set Looper MODE = **Tape** (LENGTH set by CLOCK); engage **SYNC** (hidden — Wet MODE toggle LEFT) so the Micro-Looper syncs to Wet.
2. Set Wet MODE = **Delay**, TIME to a quarter-note feel, MODIFY 1:00 (piling repeats).
3. Feed **MIDI clock** from the rig master so the loop locks to Big Time / Blooper (send CC51>0 to follow; CC53/CC54 set divisions).
4. Capture in time, then commit to Blooper downstream.
5. **Sub-drone variant:** set Tape MODIFY octave-down, but keep **CLOCK higher** to preserve low-end (aggressive low-CLOCK downsampling thins bass fundamentals).

## Notes
- SYNC + MIDI-clock parts are factory features; the knob feels are inferred — dial by ear.
- Mike Gordon (Phish) documented running bass through MOOD MkII (Equipboard, user-maintained — not official).

## Sources
- designed from MOOD-MkII-DeepResearch.md §13(d) + §6 + manual SYNC; cf. Mike Gordon (Equipboard)
- Transformed from Pedalxly MOOD-MkII-Patches.md (designed)
