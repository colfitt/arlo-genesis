---
type: patch
title: OT-as-Master-Sampler/Mixer (full desk-brain)
device: Elektron Octatrack MkII
date: 2026-06-14
description: The full desk-brain — OT mixes the pedalboard + a 2nd source, runs FX, samples on the fly, performs with the crossfader, prints to the interface, and clocks the rig.
tags: [live-fx, mixer, master, thru-machine, clock-master, designed, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank A / Part 1 · T1 Thru / T2-4 Neighbor / T5 Thru / T6-7 Neighbor / T8 Master" }
  - { name: "Input A/B", type: switch, value: "pedalboard stereo print" }
  - { name: "Input C/D", type: switch, value: "2nd source (VG-800 / OP-1 / Apollo send)" }
  - { name: "MIXER DIR AB", type: knob, value: "0 (reach mains only via Thru)" }
  - { name: "MIXER DIR CD", type: knob, value: "0 (reach mains only via Thru)" }
  - { name: "AB/CD GAIN", type: knob, value: "set so <REC> LEDs healthy" }
  - { name: "Track 1 machine", type: switch, value: "Thru INAB = A B (pedalboard) + FX1/FX2/LFOs", options: ["Static", "Flex", "Thru", "Neighbor", "Pickup", "Master"] }
  - { name: "Track 5 machine", type: switch, value: "Thru INCD = C D (2nd source, own FX)", options: ["Static", "Flex", "Thru", "Neighbor", "Pickup", "Master"] }
  - { name: "Tracks 2/3/4", type: switch, value: "Neighbor (extend Track 1)" }
  - { name: "Tracks 6/7", type: switch, value: "Neighbor (extend Track 5)" }
  - { name: "Track 8 machine", type: switch, value: "Master (PROJECT>CONTROL>AUDIO) = global EQ/Comp/Lo-Fi glue + final level" }
  - { name: "Crossfader XLV lock", type: knob, value: "Track 1 MAX@A/MIN@B, Track 5 MIN@A/MAX@B (equal-power A/B fade)" }
  - { name: "Clock", type: switch, value: "OT master (CLOCK + TRANSPORT SEND on)" }
---

# OT-as-Master-Sampler/Mixer (full desk-brain)

## Concept
The full desk-brain setup: the OT mixes the pedalboard plus a 2nd source (VG-800 / OP-1 / Apollo send), runs FX on each, samples on the fly, performs with the crossfader, prints to the interface, and clocks the whole rig. Synthesizes the manual's "super mixer" role onto the rig.

## How to play it
1. Route Input A/B = pedalboard stereo print; Input C/D = 2nd source. Main out L/R → Apollo x8 / Babyface; Cue out = independent stem.
2. MIXER: **DIR AB = 0, DIR CD = 0** (both reach mains only via Thru), set AB/CD GAIN so `<REC>` LEDs are healthy.
3. **Track 1 = Thru INAB = A B** (pedalboard) with FX1+FX2+LFOs. **Track 5 = Thru INCD = C D** (2nd source, own FX) — Track 5 is a chain head like Track 1.
4. Optional **Neighbor** racks: tracks 2/3/4 extend Track 1, tracks 6/7 extend Track 5.
5. **Track 8 = MASTER** (PROJECT>CONTROL>AUDIO) = global EQ/Comp/Lo-Fi glue + final level on the whole mix (incl. DIR inputs); no cue out, unaffected by mutes.
6. Place one trig on Track 1 + Track 5; [PLAY].
7. Mix: LEVEL/VOL per track = faders. Crossfader: XLV-lock Track 1 MAX@A/MIN@B and Track 5 MIN@A/MAX@B for an equal-power A/B fade. Mute = [FUNC]+[TRACK n].
8. Resample anytime: any recorder grabs A/B, C/D, or SRC3 = MAIN/CUE/T1–T8.
9. Clock: OT master (CLOCK + TRANSPORT SEND on) driving Digitakt / CB / VG-800 / Microcosm / H90 over DIN.

## Notes
- Neighbor cannot be on track 1 or 5 (the chain heads).
- All routing/level values are **designed** starting points — dial to taste.

## Sources
- designed from links/rig-recipe-ot-master-sampler-mixer.md (Manual §16.1 p96, §8.8 MIXER p42, §10.3.2 XLV/XDIR p54)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (DOUG-designed)
