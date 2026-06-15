---
type: patch
title: "Sketch — super-saw stacked lines (fake unison)"
device: TE OP-1 Field
date: 2026-06-15
description: A forum-recipe trick (op1tips) that fakes a fat super-saw by drawing multiple horizontal pitch lines in the Sketch sequencer a click or two apart and stacking them with a tight division — turning the OP-1's mono engine into a thick detuned-oscillator wall, a clever workaround for its limited unison.
tags: [lead, pad, sketch-sequencer, supersaw, detune]
dips:
  HOLD: "[Shift]+Orange = Hold mode → instant evolving pad from the drawn stack"
controls:
  - { name: "Engine", type: switch, value: "Cluster (recommended)", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "Poly", type: switch, value: "on", options: ["on","off"] }
  - { name: "Sketch — draw lines (Blue)", type: knob, value: "draw 3 horizontal lines L→R" }
  - { name: "Sketch — pitch nudge (Green)", type: knob, value: "+1 to +2 encoder clicks between each line" }
  - { name: "Sketch — division", type: switch, value: "/4 ([Shift]+Green) so the lines stack", options: ["/1","/2","/4","/8","/16"] }
  - { name: "Undo/Redo drawing", type: switch, value: "[Shift]+Blue left/right" }
  - { name: "FX", type: switch, value: "nitro (saturation)" }
  - { name: "LFO", type: switch, value: "element (source = envelope, dest = cutoff)", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "Hold", type: switch, value: "[Shift]+Orange = Hold (sustain the stack as a pad)", options: ["on","off"] }
---

# Sketch — super-saw stacked lines (fake unison)

## Concept

Use the Sketch (drawing) sequencer to fake a fat super-saw: draw multiple horizontal pitch lines a click or two apart and set the division so they sound together, producing a thick detuned-oscillator wall from a single mono engine — a clever workaround for the OP-1's limited unison. The sequencer supplies the "extra oscillators" the engine's own unison can't.

## How to play it

1. Pick **Cluster**, enable **Poly**.
2. In **Sketch**, draw a horizontal line (Blue), nudge pitch +1 click (Green), draw another, nudge again — 3 lines total.
3. Set division to **/4** ([Shift]+Green) so the lines overlap into one fat tone.
4. Add **Nitro** + **Element LFO** (source = envelope, dest = cutoff) for movement.
5. **[Shift]+Orange** for **Hold** mode to turn it into a sustained pad.

## Notes

- Values published as **relative steps** (line count, +1/+2 pitch nudges, /4 division) — absolute pitches are to-taste, so treat the controls above as a dialable recipe rather than fixed numeric settings.
- The sequencer supplies the "extra oscillators" the engine's unison can't.
- Drawing in **Hold** mode makes an instant evolving pad from the drawn stack.
- **[Shift]+Blue** left/right = undo/redo the drawing as you experiment.

## Sources

- forum recipe — github.com/ratbag98/op1tips (Sketch super-saw: multi-line draw with pitch nudges, /4 division, Hold mode, Nitro+Element LFO); relative steps + division/Hold documented
