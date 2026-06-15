---
type: patch
title: "Whole-Stack Scene — one PC recalls the AM with the board"
device: Chase Bliss Brothers AM
date: 2026-06-15
description: 'Documented MIDI/preset integration: beyond the 4 onboard presets, the AM stores a large MIDI bank of drive settings and can save its preset to the SAME Program Change number as the rest of the Chase Bliss board — so a single PC from your sequencer recalls a whole-stack scene per song and the AM fires alongside every other CB pedal. All AM controls AND dip states (modes, HI GAIN, MASTER, BANK, PRES LINK, presence) save with the preset. Requires a powered Chase Bliss MIDIbox feeding the AM''s ring-active TRS jack (TRS-MIDI, not native DIN/USB); default MIDI channel 2.'
tags: [midi, preset, scene-recall, per-song, program-change, routing, utility, designed]
dips:
  HI GAIN: per the saved tone (state saves with preset)
  MASTER: optional — on so VOL 2 acts as a global master for the recalled scene
  BANK: per the saved tone (state saves with preset)
  PRES LINK: per the saved tone (state saves with preset)
controls:
  - { name: "CHANNEL 2 MODE", type: switch, value: "per the chosen song tone — dial from recipe (no published value)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 2", type: knob, value: "per the chosen tone — no published values" }
  - { name: "VOL 2", type: knob, value: "per the chosen tone (optionally the global master via MASTER dip) — no published values" }
  - { name: "TONE 2", type: knob, value: "per the chosen tone — no published values" }
  - { name: "CHANNEL 1 MODE", type: switch, value: "per the chosen song tone — dial from recipe (no published value)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 1", type: knob, value: "per the chosen tone — no published values" }
  - { name: "VOL 1", type: knob, value: "per the chosen tone — no published values" }
  - { name: "TONE 1", type: knob, value: "per the chosen tone — no published values" }
  - { name: "TREBLE BOOSTER", type: switch, value: "per the chosen tone — saves with the preset", options: ["UP (bright)", "MIDDLE (off)", "DOWN (Rangemaster)"] }
  - { name: "PRESENCE", type: knob, value: "per the chosen tone — presence saves with the preset", options: [] }
  - { name: "MIDI channel", type: switch, value: "shared CB-stack channel (default ch.2)", options: [] }
  - { name: "Save", type: switch, value: "hold a footswitch ~3 sec (or send a PC while holding both footswitches) to store the preset", options: [] }
  - { name: "Onboard recall", type: switch, value: "footswitch = left/right preset; both/middle = LIVE", options: [] }
---

# Whole-Stack Scene — one PC recalls the AM with the board

## Concept
A MIDI/preset integration patch rather than a single tone. Beyond the 4 onboard presets, the Brothers AM can store a large bank of drive settings over MIDI. The trick: save the AM's preset to the SAME Program Change number that the rest of the Chase Bliss board uses for a given song, on a shared MIDI channel. Now one Program Change from your sequencer recalls a whole-stack scene — the AM's drive setting fires alongside every other CB pedal, no per-pedal recall needed. Everything saves with the preset: all AM controls, every dip state (modes, HI GAIN, MASTER, BANK, PRES LINK), and presence. Optionally repurpose VOL 2 as a global master (MASTER dip) so the recalled scene has one output control. The tone you save is whatever the song needs — use any of the other AM patches as your starting voice.

## How to play it
1. Dial the AM to the drive tone a given song needs (use any of the other patches as the starting tone — this patch supplies the routing, not the knob values).
2. Put the AM on the shared CB-stack MIDI channel (default 2) and save its preset to the SAME Program Change number the rest of the CB pedals use for that song (hold a footswitch ~3 sec, or send a PC while holding both footswitches).
3. Now a single Program Change from your sequencer recalls the AM's preset alongside the whole board — a one-PC scene per song; the dip states AND presence recall too.
4. Optionally set the MASTER dip so VOL 2 acts as a global master, giving the recalled scene one output control.
5. Remember the AM gets MIDI over the ring-active 1/4" TRS jack via a powered Chase Bliss MIDIbox — power the MIDIbox.

## Notes
- Documented integration, dialable tone: the PC-recall behavior, the shared-number whole-stack scene, the uniform CB-stack CC map, dips-and-presence-save-with-preset, the master-volume MASTER dip, and the MIDIbox requirement are all documented. The actual tone you save is your choice — dial the knobs from recipe; no knob values are published here, so none are presented as sourced.
- Common gotcha: forgetting to power the MIDIbox. The AM takes TRS-MIDI, not native 5-pin DIN or USB.
- Sources differ on the exact MIDI preset count (commonly cited around ~122/128 beyond the 4 onboard) — treat it as "a large bank" rather than a hard number. The uniform CB-stack CC map applies for remote control of individual params within the scene.

## Sources
- research/links/midi-preset-integration-cb-stack.md (PC recall, shared-number whole-stack scene, MIDIbox, dips save with presets)
- https://www.chasebliss.com/brothers-am (4 onboard presets, MIDI preset recall, dips + presence saved with presets)
- https://www.scribd.com/document/917850869/Brothers-AM-MIDI-Manual-Pedal-Chase-Bliss (MIDI manual — Program Change recall, default channel 2)
- https://guitar.com/reviews/effects-pedal/the-big-review-chase-bliss-brothers-am/ (second volume as master-volume DIP)
- Brothers-AM-UsageGuide.md §4 (MIDI/preset integration)
- Ref: chasebliss.com/brothers-am; Brothers AM MIDI manual
</content>
</invoke>
