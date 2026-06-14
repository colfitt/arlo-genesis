---
type: patch
title: Clock-synced blooping
device: Chase Bliss Blooper
date: 2026-06-14
description: Loops that arm and start on the next clock pulse and never drift off the Digitakt 2 clock — via CV CLOCK dip or MIDI clock through the CB MIDIBox.
tags: [setup, midi, clock-sync, digitakt, factory]
dips:
  CV CLOCK: on (CV jack as clock input)
controls:
  - { name: "RECORD (CC#1)", type: button, value: "arms Blooper — waits for next pulse to start; playback also synced (no phasing)" }
  - { name: "Sync note division (CC54)", type: knob, value: "set division via CC54" }
  - { name: "LAYERS (CC#15)", type: knob, value: "MIDI-controllable via CC#15" }
  - { name: "RAMP (CC#20)", type: knob, value: "MIDI-controllable via CC#20" }
  - { name: "MIDI channel", type: knob, value: "default channel 2" }
  - { name: "Slot/Bank", type: knob, value: "dip + MIDI/CV (dips physical-only) · applies across all loop slots" }
---

# Clock-synced blooping

## Concept

Loops that arm and start on the next clock pulse and never drift off the Digitakt 2 clock. When following clock, pressing RECORD arms Blooper — it waits for the next pulse to start, and playback is also synced so there's no phasing.

## How to play it

1. Set the CV CLOCK dip (CV jack as clock input) OR feed MIDI clock via the CB MIDIBox (ring-active TRS; the box needs its own 9V).
2. Press RECORD to arm — Blooper waits for the next pulse to start.
3. Set the sync note division with CC54.
4. Blooper CC map: CC#1 = RECORD, CC#15 = LAYERS, CC#20 = RAMP. Default MIDI channel = 2.

## Notes

- Lock Drone Pattern, Arpeggiloop, and Time Machine Sequencing to this so the grid feels intentional.
- Dips are physical-only, not MIDI-addressable.

## Sources

- `research/links/cb-stack-clock-sync-per-pedal.md`
- `research/links/cb-stack-midi-trs-and-midibox.md`
- `research/Blooper-DeepResearch.md` §4 (MIDI quick-start PDF)
- Transformed from Pedalxly Blooper-Patches.md (factory)
