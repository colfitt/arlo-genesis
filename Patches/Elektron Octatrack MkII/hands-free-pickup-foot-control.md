---
type: patch
title: Hands-Free Pickup Foot Control (MIDI note map)
device: Elektron Octatrack MkII
date: 2026-06-14
description: Driving the Pickup loopers from a MIDI foot controller while playing banjo/guitar standing — OT stays on the desk, both hands on the instrument.
tags: [looper, pickup, midi, foot-control, hands-free, community, signature]
controls:
  - { name: "Slot/Bank", type: knob, value: "Bank A / Part 4 · Pickups on tracks 1+2; AUTO CHANNEL = footswitch channel" }
  - { name: "Wiring", type: switch, value: "foot controller MIDI OUT → OT MIDI IN (5-pin DIN)" }
  - { name: "AUTO CHANNEL", type: switch, value: "controller sends on the OT AUTO CHANNEL (PROJECT>MIDI>CHANNELS>AUTO CHANNEL)" }
  - { name: "AUDIO NOTE IN", type: switch, value: "STANDARD" }
  - { name: "Note C (60)", type: button, value: "combo-record/overdub toggle (= [REC1])" }
  - { name: "Note E (64)", type: button, value: "play/stop toggle (= [REC2])" }
  - { name: "Note B (71)", type: button, value: "sync sequencer to active Pickup loop (start at next loop wrap)" }
  - { name: "Note A (69)", type: button, value: "move focus to PREVIOUS track" }
  - { name: "Note G# (68)", type: button, value: "move focus to NEXT track" }
  - { name: "CC 59 (CC-only controllers)", type: button, value: "sent to auto channel, interpreted as note-on (CC value = note number; CC59 val 60 = combo-record)" }
---

# Hands-Free Pickup Foot Control (MIDI note map)

## Concept
Driving the Pickup loopers from a MIDI foot controller while playing banjo/guitar standing — the OT stays on the desk with both hands on the instrument. The foot controller sends notes on the OT's AUTO CHANNEL, which drives the currently active track's Pickup.

## How to play it
1. Wire foot controller MIDI OUT → OT MIDI IN (5-pin DIN). Controller sends on the OT **AUTO CHANNEL** (PROJECT>MIDI>CHANNELS>AUTO CHANNEL); AUDIO NOTE IN = STANDARD.
2. Note map (auto channel, drives the ACTIVE track's Pickup):
   - **C(60)** = combo-record/overdub toggle (= [REC1])
   - **E(64)** = play/stop toggle (= [REC2])
   - **B(71)** = sync sequencer to active Pickup loop (start at next loop wrap)
   - **A(69)** = move focus to PREVIOUS track; **G#(68)** = move to NEXT track
3. CC-only controllers: send **CC 59** to the auto channel (interpreted as note-on, CC value = note number; CC59 val 60 = combo-record).
4. Use: Pickups on tracks 1+2; pedal 1 start / pedal 2 close a banjo phrase (OT BPM snaps); pedal → track 2 → counter-line (LEN = X2 for a longer bed); pedal → OT sequencer rides the loop.

## Notes
- Cuckoo's variant: note 60 = record, 64 = play/next, a switch = SYNC TO TEMPO, auto channel 9 via a USB-MIDI host.
- Note map is manual-grounded (designed wiring); the C60/E64 + channel-9 USB-host specifics are from the Cuckoo tutorial (community, verified).

## Sources
- Ref: Cuckoo "Loopbox" (community, verified)
- links/pickup-foot-control-rig.md + transcripts/cuckoo-ot-pickup-machine-loopbox.md (Manual §17.1.5 p106, §16.5 note p103, Appendix C p137; youtube JnbQ8ichm54)
- Transformed from Pedalxly Octatrack-MkII-Patches.md (DOUG-designed)
