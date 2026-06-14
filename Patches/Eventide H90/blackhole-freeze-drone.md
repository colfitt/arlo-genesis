---
type: patch
title: Blackhole Freeze Drone
device: Eventide H90
date: 2026-06-14
description: Lock a held fuzz chord into an infinite pad and play over it — THE core drone technique, straight from Eventide staff (Brock), using Feedback fully clockwise as Freeze.
tags: [drone, doom, freeze, sustained-wall, performance, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "6" }
  - { name: "Preset A Algorithm", type: switch, value: "Blackhole" }
  - { name: "Feedback", type: knob, value: "fully clockwise (= Freeze)" }
  - { name: "Freeze (Performance Parameter)", type: button, value: "footswitch — latching, or momentary via aux switch / MIDI CC (>=64 press, <=63 release)" }
  - { name: "HotSwitch 1", type: button, value: "Blackhole Feedback to Freeze (instant locked pad)" }
---

# Blackhole Freeze Drone

## Concept
The core drone technique, straight from Eventide staff (Brock): lock a held Hizumitas/baritone fuzz chord into an infinite pad and play over it. Freeze is Feedback turned fully clockwise. Note the nuance — there is a finicky transition zone between **Infinite** (an infinite tail that still accepts input) and full-CW **Freeze** (locked, accepts no input).

## How to play it
1. Engage Blackhole on Preset A.
2. Assign **Freeze as a Performance Parameter** on a footswitch (latching, or momentary via aux switch / MIDI CC >=64 press, <=63 release).
3. Hold a fuzz chord, stomp Freeze, and the wall locks.
4. Play over the locked pad. Optionally map **HotSwitch 1 -> Blackhole Feedback to Freeze** for an instant locked pad.

## Notes
- Freeze persists independently of HotSwitch toggles — put it on a Performance Param, not a HotSwitch.
- The transition between Infinite and full-CW Freeze is finicky; find the sweet spot by ear.
- This is the workflow behind patches "Cavernous Blackhole Drone" and "Blackhole — Infinite Ambient Pad."

## Sources
- research/links/eventide-forum-freeze-drone-holds.md (Eventide forum, staff "Brock")
- Transformed from Pedalxly H90-Patches.md (community)
