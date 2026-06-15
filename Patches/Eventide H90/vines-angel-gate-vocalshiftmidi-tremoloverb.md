---
type: patch
title: "Angel Gate — VocalShiftMIDI + TremoloVerb (Vines artist preset)"
device: Eventide H90
date: 2026-06-15
description: "Vines (Cassie Wieland) artist preset via Eventide's blog — VocalShiftMIDI harmonies pulsed by TremoloVerb into rich rhythmic swells, with the tremolo rate playable live via a HotKnob. One of the five Vines presets for VocalShiftMIDI; the pair is published but raw values are not."
tags: [vocalshiftmidi, tremoloverb, tremolo, vocal, artist-preset, vines]
dips:
  HotKnob: "tremolo rate (perform with it)"
  Shape: "Sine/Triangle = smooth; Square = choppy"
controls:
  - { name: "Preset A Algorithm", type: switch, value: "VocalShiftMIDI" }
  - { name: "Preset B Algorithm", type: switch, value: "TremoloVerb" }
  - { name: "HotKnob", type: knob, value: "mapped to tremolo rate (perform live)" }
  - { name: "Tremolo Shape", type: switch, value: "Sine / Triangle (smooth) or Square (choppy)", options: ["Sine", "Triangle", "Peak", "Ramp", "Square", "Random", "Sample/Hold", "Envelope", "ADSR", "Manual"] }
---

# Angel Gate — VocalShiftMIDI + TremoloVerb (Vines artist preset)

## Concept
Vines' "Angel Gate" preset: MIDI-driven vocal harmonies from VocalShiftMIDI are fed into TremoloVerb, whose tremolo chops and reverb tail turn the held harmonies into rich, rhythmic swells. The defining move is mapping the tremolo rate to a HotKnob so you can ride the pulse speed live as you play. Smooth shapes (Sine/Triangle) keep the swells legato; Square makes them choppy and gated.

## How to play it
1. Load VocalShiftMIDI on A and TremoloVerb on B.
2. Assign the tremolo rate to a HotKnob so it's adjustable in real time.
3. Choose a tremolo shape — Sine/Triangle for smooth swells, Square for a choppy/gated pulse.
4. Drive the harmonies via MIDI and pulse them with the trem, performing the rate on the HotKnob.

## Notes
- Part of the five Vines presets for VocalShiftMIDI.
- Raw values not published by Eventide — phrased as a dialable recipe. Treat the controls above as a starting point, not cited settings.
- Tremolo shape list is from the H90 manual (TremoloVerb); the specific shape Vines used isn't documented, so Sine/Triangle vs Square is your call per the smooth/choppy guidance.

## Sources
- Ref: Vines (Cassie Wieland) — https://www.eventideaudio.com/blog/vines-brings-her-signature-vocal-sound-to-the-h90/ (Angel Gate = VocalShiftMIDI + TremoloVerb, HotKnob maps trem rate)
- TremoloVerb shapes: https://cdn.eventideaudio.com/manuals/h90/1.11.4/content/algorithms/reverb.html
- provenance: artist Vines (Cassie Wieland) via Eventide blog + manual (shapes) — pair published, no values
