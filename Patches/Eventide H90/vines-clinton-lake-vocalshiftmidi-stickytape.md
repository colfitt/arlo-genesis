---
type: patch
title: "Clinton Lake — VocalShiftMIDI + Sticky Tape (Vines artist preset)"
device: Eventide H90
date: 2026-06-15
description: "Gritty, distorted tape harmonies with a saturated 'TV static' character — VocalShiftMIDI drives MIDI harmony voices into Sticky Tape for dense, dirty atmospheric vocal textures. Vines (Cassie Wieland) artist preset 'Clinton Lake' via the Eventide blog; the algorithm pair is published but no knob values are."
tags: [pitch, harmonizer-plus, vocalshiftmidi, stickytape, tape, lofi, vocal, degraded, artist-preset, vines]
controls:
  - { name: "Preset A Algorithm", type: switch, value: "VocalShiftMIDI (MIDI-played harmony voices)" }
  - { name: "Preset B Algorithm", type: switch, value: "Sticky Tape (tape saturation + wow/flutter)" }
  - { name: "Routing", type: switch, value: "Series (VocalShiftMIDI -> Sticky Tape)", options: ["Series", "Parallel", "Insert"] }
  - { name: "Harmony Voices (A)", type: knob, value: "drive intervals via MIDI — recipe, no published value" }
  - { name: "Saturation (B)", type: knob, value: "push high for grit/density — recipe, no published value" }
  - { name: "Wow / Flutter (B)", type: knob, value: "lean in for the 'TV static' character — recipe, no published value" }
  - { name: "Mix (A/B)", type: knob, value: "to taste — recipe, no published value" }
---

# Clinton Lake — VocalShiftMIDI + Sticky Tape (Vines artist preset)

## Concept
Vines (Cassie Wieland) "Clinton Lake" artist preset: VocalShiftMIDI supplies MIDI-played harmony voices, then Sticky Tape glues them with tape saturation and wow/flutter, yielding "distorted tape harmonies" with a "saturated TV static" character. Denser and dirtier than the cleaner harmonizer patches — squarely on the rig's degraded "recorded-wrong" thesis.

## How to play it
1. Load VocalShiftMIDI on Preset A and Sticky Tape on Preset B (Series, A -> B).
2. Drive the harmony voices via MIDI over a held source note.
3. Push Sticky Tape saturation for grit and density.
4. Lean into wow/flutter for the saturated "TV static" character.

## Notes
- Creates "distorted tape harmonies" with a "saturated TV static" character — denser, dirtier atmospheric vocal textures.
- No published knob values — controls are a dialable recipe, dial by ear. Only the algorithm pair (VocalShiftMIDI + Sticky Tape) is published.

## Sources
- https://www.eventideaudio.com/blog/vines-brings-her-signature-vocal-sound-to-the-h90/ (Vines / Cassie Wieland; Clinton Lake = VocalShiftMIDI + Sticky Tape)
