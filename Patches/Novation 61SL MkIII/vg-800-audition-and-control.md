---
type: patch
title: VG-800 Audition & Control (banjo/baritone NOT picked up)
device: Novation 61SL MkIII
date: 2026-06-14
description: Build-your-own template to audition and ride the Boss/Roland VG-800's models (GR-300/organ/acoustic/banjo/sitar) from the keybed without the GK-5 in the path — the VG-800 is the rig's main string source, banjo-as-lead.
tags: [vg-800, banjo-as-lead, string-source, audition, community, signature]
controls:
  - { name: "Part Channel", type: knob, value: "Ch4 (MUST match VG RX CHANNEL)" }
  - { name: "Part Destination", type: switch, value: "DIN to VG-800 (via BMIDI-5-35 TRS↔DIN)", options: ["USB", "DIN1", "DIN2", "CV"] }
  - { name: "Encoder 1", type: knob, value: "CC#20 → VG amp gain" }
  - { name: "Fader 1", type: knob, value: "CC#21 → FX1 level" }
  - { name: "Aftertouch", type: knob, value: "CC#22 → a mod depth" }
  - { name: "Buttons", type: button, value: "PC (VG memory recall) or CC toggles for FX on/off" }
  - { name: "Per-control Low/High", type: knob, value: "Set to scale each CC range (MIN>MAX inverts on VG side)" }
  - { name: "Fader Pickup", type: switch, value: "ON (standalone)", options: ["On", "Off"] }
  - { name: "MIDI Clock Tx", type: switch, value: "On (VG synced delays/mod follow SL)", options: ["On", "Off"] }
  - { name: "Session Slot", type: knob, value: "Session slot 2" }
---

# VG-800 Audition & Control (banjo/baritone NOT picked up)

## Concept
Auditioning and tweaking the VG-800's GR-300 / organ / acoustic / banjo / sitar models from the keybed without the GK-5 banjo/baritone in the signal path. Ride model/FX levels and a mod-depth target live, and recall VG memories by Program Change. The VG-800 is the rig's main string source — banjo is a LEAD voice via GK-5 → VG-800 — and this template lets you drive the synth side directly from the SL's keybed.

## How to play it
1. PHYSICAL: SL DIN Out → VG-800 MIDI IN via a Boss BMIDI-5-35 TRS↔5-pin-DIN cable (the VG has TRS MIDI, not full DIN).
2. VG SIDE (Parameter Guide): RX CHANNEL = Ch4; RX PC MAP = FIX (PC recalls VG memories); SYNC CLOCK = MIDI or MIDI-AUTO (follow SL tempo).
3. VG CONTROL ASSIGN 1..n: SOURCE = the CC#s the template sends (must be in CC#1–31 or CC#64–95 windows), TARGET = chosen VG params, MIN/MAX to scale (MIN>MAX inverts).
4. SL SIDE: Part Channel = Ch4 (MUST match VG RX), Destination = the DIN to the VG.
5. TEMPLATE (Components): enc1 = CC#20 → VG amp gain, fader1 = CC#21 → FX1 level, aftertouch → CC#22 → a mod depth; buttons = PC (memory recall) or CC toggles for FX on/off; Low/High per control to scale.
6. Fader Pickup = ON (standalone). SL MIDI Clock Tx On → VG synced delays/mod follow the SL.

## Notes
- Build-your-own (no factory VG-800 template).
- DON'T conflate directions: VG GUITAR-TO-MIDI (VG→SL) is the opposite path.
- Keep VG RX CHANNEL = SL Part channel or nothing moves.

## Sources
- research/links/int-recipe-vg800.md (SL V2 + VG-800 Reference Manual p.21 + Parameter Guide pp.40–42, 51) + UsageGuide §9 + DeepResearch §6/§13(d).
- Ref: Rig — VG-800 = main string source, banjo-as-lead.
- Transformed from Pedalxly 61SL-MkIII-Patches.md (community)
