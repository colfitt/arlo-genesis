---
type: patch
title: "Pitch-to-MIDI Poly → Soft-Synth (USB)"
device: Roland VG-800
date: 2026-06-15
description: "Drive a soft-synth (MainStage / any DAW instrument) from the banjo or baritone over a single USB-C cable in POLY mode — all strings on one MIDI channel for a single timbre, with the soft-synth audio returning through the VG-800's outs into the front of Board 1. The simpler, any-synth counterpart to the existing per-string MONO sequencer driver. Sourced workflow from VGuitarForums (arkieboy); trigger-taming params are sourced starting points, no published knob values."
tags: [pitch-to-midi, banjo, synth, designed, sequencer]
dips:
  "GUITAR TO MIDI": "ON, mode = POLY (all strings one channel)"
  "CONTROL ASSIGN → GUITAR TO MIDI → ALT TUNE": "ON to transmit retuned pitches"
  "USB driver": "Mac/Win = Boss driver for multichannel; iOS = USB GENERIC (reduced)"
controls:
  - { name: "GUITAR TO MIDI", type: switch, value: "ON (System)", options: ["ON", "OFF"] }
  - { name: "MIDI mode", type: switch, value: "POLY (all strings on one channel, one timbre; receiving synth = OMNI, no per-string bend)", options: ["MONO", "POLY"] }
  - { name: "PLAY FEEL", type: switch, value: "FEEL3–4 (or NO DYNA + NO-DYNA VELOCITY ~100) — sourced starting point, verify by ear" }
  - { name: "LOW VELO CUT", type: knob, value: "2–4 (sourced starting point, no published value)" }
  - { name: "BEND RANGE", type: knob, value: "12–24 (sourced starting point)" }
  - { name: "HOLD", type: switch, value: "HOLD1 (sustains fast-decaying banjo notes across re-picks)" }
  - { name: "CONTROL ASSIGN → GUITAR TO MIDI → ALT TUNE", type: switch, value: "ON (optional — transmits the retuned pitches)", options: ["ON", "OFF"] }
  - { name: "USB-C", type: switch, value: "MIDI out + multichannel audio return on one cable" }
---

# Pitch-to-MIDI Poly → Soft-Synth (USB)

## Concept

Drive a soft-synth (MainStage / any DAW instrument) from the banjo or baritone over a single USB-C cable in POLY mode. `GUITAR TO MIDI = ON` with `mode = POLY` puts all strings on one MIDI channel for a single timbre — the any-synth-friendly counterpart to the existing per-string MONO Sequencer Driver patch. The soft-synth audio returns through the VG-800's outs into the front of Board 1, so the whole round trip happens on one cable. Per arkieboy (VGuitarForums): "Audio and MIDI can be routed through the USB cable… use guitar-to-MIDI to control MainStage, output the audio back to the VG."

## How to play it

1. Set `GUITAR TO MIDI = ON`, `mode = POLY`; connect one USB-C cable to the Mac.
2. In the DAW / MainStage, route the VG-800 MIDI to a soft-synth; route the soft-synth audio back to the VG-800 to come out the main outs (round-trip on one cable).
3. Tame the banjo's spiky triggering: `PLAY FEEL = FEEL3–4`, `LOW VELO CUT = 2–4`, `HOLD1` to sustain fast-decaying notes.
4. Set `ALT TUNE = ON` in `CONTROL ASSIGN` if you want the soft-synth to hear the retuned pitches; use the Boss driver README for the audio channel map.

## Notes

- Sourced workflow: "Audio and MIDI can be routed through the USB cable… use guitar-to-MIDI to control MainStage, output the audio back to the VG" (arkieboy, VGuitarForums). POLY = all strings on one channel, any-synth-friendly (set the receiving synth to OMNI); loses per-string bend.
- Distinct from the existing MONO-mode per-string Sequencer Driver patch (Digitakt/Octatrack). Trigger-taming param values (`PLAY FEEL`, `LOW VELO CUT`, `BEND RANGE`) are sourced starting points, not published knob values — dial from this recipe and verify by ear. Latency is sub-perceptible-but-nonzero (no published ms).
- Honesty: full "Re-Guitar" multichannel mode is not class-compliant — iOS needs USB GENERIC mode (reduced).

## Sources

- 🟢 `research/links/vguitarforums-usb-audio-software-instruments.md` (USB MIDI+audio round-trip to MainStage/soft-synth; class-compliant vs Re-Guitar)
- 🟢 `research/links/vguitarforums-guitar-to-midi.md` (MONO vs POLY; ALT-TUNE-to-MIDI; HOLD/velocity)
- `research/VG-800-DeepResearch.md` §8 (GUITAR-TO-MIDI poly/mono; USB-C multichannel)
- Provenance: sourced workflow (param starting points, no published values) — dialable recipe
