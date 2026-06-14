---
type: patch
title: Soft-Synth Master Keyboard (daily driver)
device: Novation 61SL MkIII
date: 2026-06-14
description: Standard-MIDI keybed Session for playing Kontakt 8 / Komplete 15 / Arturia V Collection 11 in Logic or Ableton — velocity + channel-pressure aftertouch the OP-1 lacks.
tags: [utility, master-keyboard, soft-synth, daily-driver, community]
controls:
  - { name: "World/Mode", type: switch, value: "Standalone (standard-MIDI, NOT InControl)", options: ["Standalone", "InControl"] }
  - { name: "Part 1 Destination", type: switch, value: "USB", options: ["USB", "DIN1", "DIN2", "CV"] }
  - { name: "Part 1 Channel", type: knob, value: "Ch1" }
  - { name: "Zones", type: switch, value: "Off", options: ["Off", "On"] }
  - { name: "Velocity Curve (Global)", type: switch, value: "Normal or Normal+", options: ["Soft", "Normal", "Normal+", "Hard"] }
  - { name: "Aftertouch (channel-pressure strip)", type: knob, value: "CC1 (mod) or a filter CC, set in Components" }
  - { name: "Mod/Pitch wheels", type: knob, value: "Active" }
  - { name: "Pads", type: button, value: "Finger-drumming (poly-AT), notes Ch1" }
  - { name: "Encoders/Faders", type: knob, value: "Left to plugin MIDI-learn (Automap gone)" }
  - { name: "Session Slot", type: knob, value: "Session slot 1 (Save-Lock)" }
---

# Soft-Synth Master Keyboard (daily driver)

## Concept
The "I just want to play in a part" patch. A simple standard-MIDI template/Session that turns the 61SL into the velocity-and-aftertouch keybed for soft synths in Logic Pro or Ableton — the expressive keybed the OP-1 lacks and the weighted S08 isn't built for. Keybed sends notes on Ch1; mod/pitch wheels active; encoders/faders are left to each plugin's own MIDI-learn since Automap is gone.

## How to play it
1. Set WORLD = standalone/standard-MIDI (NOT InControl).
2. Part 1: Destination = USB, Channel = Ch1, Zones = Off. Octave buttons to taste.
3. Velocity curve (Global) = Normal or Normal+.
4. In Components, route the channel-pressure aftertouch strip to CC1 (mod) or a filter CC — this is the one expression unlock for soft synths on this box.
5. Use the 16 PADS for finger-drumming (poly-AT).
6. For hands-on transport + mixer + device banking instead, flip to InControl (see "InControl DAW Surface + Clip Launch").

## Notes
- Foundation/utility patch.
- Aftertouch→CC is the one expression unlock for soft synths (no MPE on this box).
- Encoders/faders need per-plugin MIDI-learn — there is no auto per-plugin map since Automap was removed.

## Sources
- 61SL-MkIII-DeepResearch.md §13(a) + research/links/int-recipe-modular-softsynth.md §B + UsageGuide §5; factory standard-MIDI behavior.
- Transformed from Pedalxly 61SL-MkIII-Patches.md (community)
