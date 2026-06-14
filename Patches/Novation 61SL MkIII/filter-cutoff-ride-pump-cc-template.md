---
type: patch
title: Filter-Cutoff Ride + Pump-CC Template
device: Novation 61SL MkIII
date: 2026-06-14
description: DOUG-designed filter-house controller — ride the cutoff of whatever holds the loop (VG-800 SYNTH / soft synth / Elektron FX) and send a pump-CC; SL as clock master for the four-on-the-floor. (Daft Punk / LCD taste-profile.)
tags: [taste-profile, filter-house, cutoff-ride, pump, daft-punk, lcd-soundsystem, designed, signature]
controls:
  - { name: "World/Mode", type: switch, value: "Standalone template/session", options: ["Standalone", "InControl"] }
  - { name: "Encoder 1", type: knob, value: "Filter CUTOFF CC (slow open/close = filter-house build)" }
  - { name: "Encoder 2", type: knob, value: "RESONANCE" }
  - { name: "Fader 1", type: knob, value: "A pump-CC, or a CC automation lane that ramps down on each beat (the duck)" }
  - { name: "Per-control Low/High", type: knob, value: "Set to scale" }
  - { name: "Fader Pickup", type: switch, value: "ON", options: ["On", "Off"] }
  - { name: "Clock", type: switch, value: "SL = clock master (Tx On) — loop + synced delays follow one tempo (4-on-the-floor)", options: ["SL master Tx On", "Off"] }
  - { name: "VG routing", type: knob, value: "Route to its CONTROL ASSIGN CCs (CC#1–31 window)" }
  - { name: "Template/Session Slot", type: knob, value: "61SL-E1 — Save-Lock it" }
---

# Filter-Cutoff Ride + Pump-CC Template

## Concept
A hands-on filter-house controller: ride the cutoff of whatever holds the loop (VG-800 SYNTH / soft synth / Elektron FX) and send a pump-CC, with the SL as clock master for the four-on-the-floor. This box makes no sound — it's a template/session aimed at Daft Punk-style filter-house cutoff automation and LCD-style four-on-the-floor pump.

## How to play it
1. Standalone template/session.
2. enc1 → filter CUTOFF CC (slow open/close = the filter-house build).
3. fader1 → a pump-CC, or record a CC automation lane that ramps down on each beat (the duck).
4. enc2 → RESONANCE.
5. Set Low/High to scale; Fader Pickup ON.
6. SL = clock master (Tx On) so the loop and synced delays follow one tempo (4-on-the-floor).
7. VG side: route to its CONTROL ASSIGN CCs (CC#1–31 window).

## Notes
- 61SL-E1.
- This box makes no sound — it's a template/session.
- Templates built in Components; port is a per-Session setting.

## Sources
- Research/Taste-Profile/sources/splice-filter-house-techniques.md + daft-punk-homework-synths-reverbmachine.md + sidechain-pump-settings-house-techno.md
- Ref: Daft Punk filter-house cutoff automation; LCD four-on-the-floor pump.
- Transformed from Pedalxly 61SL-MkIII-Patches.md (designed)
