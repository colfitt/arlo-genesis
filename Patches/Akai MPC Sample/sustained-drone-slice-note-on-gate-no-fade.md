---
type: patch
title: Sustained Drone Slice — Note On Gate, No Fade
device: Akai MPC Sample
date: 2026-06-14
description: Holding a fuzz-wall / banjo / baritone slice indefinitely while the pad is held — the Note On gate plus a killed decay, the rig's core drone-bed move.
tags: [drone, note-on, gate, sustain, community, signature]
controls:
  - { name: "Note On (Shift + blue Chop button)", type: switch, value: "ON (pad becomes a gate — sounds while held, stops on release)", options: ["off", "ON"] }
  - { name: "Amp Env Decay (B1 twice → Amp Env)", type: knob, value: "fully left to 0 (stops fade-out)" }
  - { name: "Decay From (Shift)", type: switch, value: "End (alt fade-fix)", options: ["Start", "End"] }
  - { name: "Loop", type: switch, value: "on (per-pad)", options: ["off", "on"] }
  - { name: "Loop Lock (Shift+B1, fw1.2.0)", type: button, value: "separate Loop-Start point to sustain forever" }
  - { name: "Slot/Bank", type: knob, value: "Per-pad (Sample)" }
---

# Sustained Drone Slice — Note On Gate, No Fade

## Concept
Holding a fuzz-wall / banjo / baritone slice indefinitely while the pad is held — on-aesthetic drone bed, the rig's core. Note On turns the pad into a gate (sounds while held, stops on release), the killed decay stops unwanted fade-out, and Loop + Loop Lock can sustain a slice forever. HIGH signature fit.

## How to play it
1. `Shift + blue Chop button` = NOTE ON (the under-label) → the pad becomes a gate (sounds while held, stops on release).
2. Stop unwanted fade-out: `B1` twice → AMP ENV → Decay → rotate fully left to 0 (or `Shift` = Decay From = end).
3. Also use per-pad Loop + a separate Loop-Start point (Loop Lock, `Shift+B1`, fw1.2.0) to sustain a slice forever.

## Notes
- HIGH signature fit — sustained drone walls are the rig's core.
- Loop Lock is fw1.2.0-confirmed.

## Sources
- 🔵 `research/links/mpcforums-ac50-amp-envelope-fade-and-note-on-sustain.md` (Note On manual p.32; Decay-fix p.26) + `research/links/mpcforums-ac50-firmware-13-knob-takeover.md`
- Transformed from Pedalxly MPC-Sample-Patches.md (community)
