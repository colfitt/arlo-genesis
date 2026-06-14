---
type: patch
title: Big Time Centerpiece Performance Template
device: Novation 61SL MkIII
date: 2026-06-14
description: DOUG-designed minimal-chain control of the CB Big Time as the rig's centerpiece — delay, loop, presets and clock from the SL, played live alongside OP-1/Digitakt/MPC.
tags: [cb-stack, big-time, centerpiece, performance, designed, signature]
controls:
  - { name: "Encoder 1", type: knob, value: "CC15 TIME" }
  - { name: "Encoder 2", type: knob, value: "CC19 WET" }
  - { name: "Encoder 3", type: knob, value: "CC14 COLOR" }
  - { name: "Buttons", type: button, value: "Scene PCs + a LIVE (PC0) + footswitch CCs (CC102–107)" }
  - { name: "Fader", type: knob, value: "A level" }
  - { name: "Aftertouch", type: knob, value: "→ a mod CC" }
  - { name: "Clock role", type: switch, value: "Decide per song — SL Tx master OR Big Time master", options: ["SL master (Big Time CC111=0 follows)", "Big Time master (CC110 OUT=1+)"] }
  - { name: "Subdivision", type: knob, value: "CC54 (0–12 = 1/16…whole)" }
  - { name: "Part Channel", type: knob, value: "Big Time's channel (default ch.2)" }
  - { name: "Fader Pickup", type: switch, value: "ON", options: ["On", "Off"] }
  - { name: "Session Slot", type: knob, value: "Session slot 11 (+ a dedicated Big Time template slot)" }
hidden:
  Big Time CC map (verified): "KNOBS CC14–CC19 (COLOR=14, TIME=15, … WET=19)"
  SAVE: "CC27 (to slot, value=slot#) / CC28 (current slot); 127 preset slots (10 factory)"
  Clock master: "CC110 OUT=1+ (range 60–240 bpm, auto half/double if out of range)"
  Clock follow: "CC111 FOLLOW=0"
  SCALE dependency: "OFF/CHROMATIC snaps delay to the quarter; OCT+4+5/OCTAVE = musical subdivisions"
---

# Big Time Centerpiece Performance Template

## Concept
Playing the CB Big Time live as the rig's centerpiece alongside OP-1/Digitakt/MPC — minimal-chain control of its delay, loop, presets and clock from the SL without diving into the pedal. Keeps the centerpiece hands-on while the SL clocks the room. Connects directly via 5-pin DIN (no MIDIBox needed).

## How to play it
1. PHYSICAL: SL DIN Out → Big Time MIDI IN directly (5-pin DIN, NO MIDIBox).
2. BIG TIME CC MAP (verified): KNOBS CC14–CC19 (COLOR=14, TIME=15, … WET=19); footswitches CC102–107 (reassigned in Loop Mode); SAVE = CC27 (to slot, value=slot#) / CC28 (current slot); 127 preset slots (10 factory).
3. CLOCK: Big Time can FOLLOW (CC111 FOLLOW=0) or BE MASTER — set MIDI OUT active with CC110 (OUT=1+, range 60–240 bpm, auto half/double if out of range) to let Big Time clock the rig; otherwise SL Tx master + Big Time CC111=0 to follow.
4. Subdivision = CC54 (0–12 = 1/16…whole); clock behavior depends on SCALE (OFF/CHROMATIC snaps delay to the quarter; OCT+4+5/OCTAVE = musical subdivisions).
5. TEMPLATE: enc1=CC15 TIME, enc2=CC19 WET, enc3=CC14 COLOR; buttons = scene PCs + a LIVE (PC0) + footswitch CCs; fader = a level; aftertouch → a mod CC.
6. PART Channel = Big Time's channel (default ch.2; change by holding both FS at power-up + send PC on target channel). Fader Pickup ON.

## Notes
- DESIGNED for the centerpiece.
- Big Time can be EITHER clock follower OR the stack's clock master (CC110) — decide per song; never Tx clock from the SL AND let Big Time output clock simultaneously.

## Sources
- designed from REUSED Gear/Chase Bliss Blooper/research/links/cb-stack-clock-sync-per-pedal.md (Big Time row: CC110/CC111/CC54) + cb-stack-preset-scene-recall.md (CC14–19, CC27/28) + cb-stack-midi-trs-and-midibox.md (Big Time = native DIN); taste-profile Big Time centerpiece.
- Ref: Rig — CB Big Time = centerpiece, played live with OP-1/Digitakt/MPC.
- Transformed from Pedalxly 61SL-MkIII-Patches.md (designed)
