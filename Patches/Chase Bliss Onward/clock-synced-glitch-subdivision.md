---
type: patch
title: Clock-Synced Glitch Subdivision
device: Chase Bliss Onward
date: 2026-06-14
description: Lock the Glitch stutter to song tempo so banjo/baritone stutters sit with the kit.
tags: [glitch, clock-sync, midi, tempo, rhythmic, factory]
controls:
  - { name: "SIZE", type: knob, value: "= the subdivision (with MIDI clock present, Glitch repeats lock to tempo)" }
  - { name: "Tap tempo (no MIDI)", type: button, value: "double-tap BOTH footswitches (left taps tempo, right exits)" }
  - { name: "Glitch retrigger", type: button, value: "CC108 (clock-quantized)" }
  - { name: "Freeze retrigger", type: button, value: "CC109 (clock-quantized)" }
  - { name: "SIZE (MIDI)", type: knob, value: "CC14 (ch.2)" }
  - { name: "Slot/Bank", type: knob, value: "ch.2 (default); recall via PC in the one-PC whole-stack scene" }
---

# Clock-Synced Glitch Subdivision

## Concept
Lock the Glitch stutter to song tempo so banjo/baritone stutters sit with the kit. With MIDI clock present, SIZE = the subdivision (Glitch repeats lock to tempo). Without MIDI, double-tap both footswitches to enter tap-tempo.

## How to play it
1. With **MIDI clock present, SIZE = the subdivision** (Glitch repeats lock to tempo).
2. Without MIDI: **double-tap BOTH footswitches** to enter tap-tempo (left footswitch taps tempo, right exits).
3. For the rig: send clock from the Digitakt via the CB MIDIbox/TRS.
4. Fire **CC108 / CC109** to retrigger Glitch / Freeze clock-quantized (SIZE = **CC14**, ch.2). MIDI requires a Chase Bliss MIDIbox.

## Notes
- SIZE=subdivision and the tap-tempo gesture are manual / Doug Hanson verified.
- The specific CCs (CC14/CC108/CC109/CC51/CC53/CC56) live in the **shared cb-stack files**, not Onward's folder.
- The WAYWARD ZOIA clone CCs (70–77) are a clone's own choices and are **not** the real Onward map.

## Sources
- `research/transcripts/doug-hanson-onward-demo-feature-rundown.md`; manual pp.8–9, 45; CC map: `Gear/Chase Bliss Blooper/research/links/cb-stack-clock-sync-per-pedal.md`
- Ref: Doug Hanson + CB manual
- Transformed from Pedalxly Onward-Patches.md (factory)
