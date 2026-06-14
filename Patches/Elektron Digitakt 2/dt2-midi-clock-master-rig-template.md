---
type: patch
title: DT2 MIDI / Clock-Master Rig Template (PC/CC step-sequencing)
device: Elektron Digitakt 2
date: 2026-06-14
description: Driving the rig — clock-syncing the pedals, sequencing the VG-800, firing pedal/VG-800 preset changes and CC sweeps in time from the DT2.
tags: [midi, clock, rig-integration, routing, workflow, community]
controls:
  - { name: "Clock master", type: switch, value: "SETTINGS → MIDI CONFIG > SYNC → CLOCK SEND + TRANSPORT SEND ON; PORT CONFIG OUT PORT FUNC = MIDI, OUTPUT TO = MIDI/USB" }
  - { name: "MIDI track", type: switch, value: "FUNC+SRC → SRC category → MIDI → YES (any of the 16 tracks)" }
  - { name: "Per MIDI track", type: switch, value: "up-to-4-note chord, PB/AT/MW/BC, 16 assignable CCs (VAL1–8 FLTR pg1 / SEL1–8 FLTR pg2; VAL9–16 AMP pg1 / SEL9–16 AMP pg2)" }
  - { name: "Recall external presets in time", type: switch, value: "Drop a trigless trig and p-lock BANK/SBNK/PROG on it (SRC page)" }
  - { name: "MIDI Learn", type: switch, value: "On FLTR/AMP page 2 hold FUNC+DATA, send a CC from the device, the slot captures it" }
  - { name: "Auto Channel", type: switch, value: "Lets the Novation 61SL MkIII (or VG-800 pitch-to-MIDI) play the active track" }
  - { name: "Default CC map", type: switch, value: "VAL1→CC70, VAL10→61 … VAL16→67 (reassign via SELx)" }
---

# DT2 MIDI / Clock-Master Rig Template (PC/CC step-sequencing)

## Concept
The template that drives the whole rig from the DT2 as clock master: clock-sync the pedals, sequence the VG-800, and fire pedal/VG-800 preset changes and CC sweeps in time. Any of the 16 tracks can become a MIDI track (4-note chord, PB/AT/MW/BC and 16 assignable CCs), and trigless trigs can p-lock BANK/SBNK/PROG to recall external presets on a step.

## How to play it
1. Clock master: `SETTINGS → MIDI CONFIG > SYNC` → `CLOCK SEND` + `TRANSPORT SEND` ON; `PORT CONFIG` OUT PORT FUNC = MIDI, OUTPUT TO = MIDI/USB. (Chase Bliss pedals take MIDI over 1/4" TRS — adapter or CB MIDIBox.)
2. Assign a MIDI track: `FUNC`+`SRC` → SRC category → MIDI → `YES` (any of the 16 tracks). Each MIDI track = up-to-4-note chord, PB/AT/MW/BC, and 16 assignable CCs (VAL1–8 on FLTR pg1 / SEL1–8 on FLTR pg2; VAL9–16 on AMP pg1 / SEL9–16 on AMP pg2).
3. Recall external presets in time: drop a trigless trig and p-lock `BANK`/`SBNK`/`PROG` on it (SRC page) to fire VG-800 / pedal preset changes on a step.
4. MIDI Learn: on FLTR/AMP page 2 hold `FUNC`+DATA, send a CC from the device, the slot captures it.
5. Auto Channel: lets the Novation 61SL MkIII (or VG-800 pitch-to-MIDI from banjo/baritone) play the active track.
6. Default CC map: VAL1→CC70, VAL10→61 … VAL16→67 (reassign via `SELx`).

## Notes
- Manual-verified button combos.
- Syncs to DT2 clock: Blooper, MOOD MkII (NOT in Synth Mode), Big Time, Lost & Found, Onward, Clean, TimeLine (delays only, not the looper), Big Sky (Pre-Delay), H90, Microcosm, Chroma Console.
- Does NOT sync: Generation Loss MkII (PC/CC only, warble free-runs) + Brothers AM (no time param) — use PC/CC only.
- Verify the VG-800's exact CC/PC map before relying on specific CC numbers.
- Dedicate 1–2 tracks to MIDI; keep the rest audio.

## Sources
- `research/links/rig-dt2-midi-tracks-sequencing-external.md`
- `research/links/rig-dt2-clock-sync-pedals-verified.md`
- `research/links/rig-dt2-clock-master-slave-sync.md` (Manual OS1.15A §5.3.2/§14.4/§16.3)
- Transformed from Pedalxly Digitakt-2-Patches.md (community)
