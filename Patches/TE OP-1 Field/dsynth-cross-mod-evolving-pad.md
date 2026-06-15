---
type: patch
title: DSynth — cross-mod evolving pad
device: TE OP-1 Field
date: 2026-06-15
description: "A dialable recipe (no published values) for a complex, drifting pad on the DSynth engine — two enveloped oscillators cross-modulating each other in the FM/AM-flavored zone so the timbre evolves as the two amp envelopes interact. Synthesized from forum DSynth-architecture analysis + the magazinmehatronika review (DSynth: \"complex, evolving textures from cross-modulation\")."
tags: [pad, dsynth, cross-modulation, evolving, ambient]
dips:
  Diagnostic: "drop OSC2 pitch to LFO range + bottom sine setting to HEAR the modulation type, then restore pitch"
controls:
  - { name: "Engine", type: switch, value: "DSynth (select via [Shift]+T1)", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","DSynth","DBox","Synth Sampler","Sampler"] }
  - { name: "Blue (envelope-depth macro)", type: knob, value: "mid-range — sets depth/polarity of BOTH oscillator envelopes at once; park mid for slow evolution" }
  - { name: "Orange (cross-mod type/strength)", type: knob, value: "FM region (mid = FM-sweep feel; other regions give AM / ring-mod-like character)" }
  - { name: "White (OSC2 amp envelope)", type: knob, value: "toward CW for long-decay pad (CCW = 0-attack/short-decay)" }
  - { name: "Green (OSC2 waveshape)", type: knob, value: "by ear — on-screen graphic does NOT match audible behavior" }
  - { name: "OSC2 params", type: switch, value: "[Shift] on the encoders" }
  - { name: "Octave", type: knob, value: "0 (drop for weight if desired)" }
---

# DSynth — cross-mod evolving pad

## Concept

Two enveloped oscillators modulating each other on the DSynth engine, parked in the FM/AM-flavored cross-mod zone for a complex pad that drifts in timbre as the two amp envelopes interact. DSynth is the OP-1's deepest stock engine — effectively 8 parameters across two oscillators — used here as a slow evolver rather than a percussive FM voice. Blue acts as a macro over both envelopes (depth/polarity), Orange selects the cross-mod character (FM / AM / ring-mod-like regions), White stretches the OSC2 amp envelope into a long pad tail, and Green sets OSC2 waveshape — dialed by ear, since forum analysts warn the on-screen graphic doesn't match what you hear.

## How to play it

1. Select **DSynth** via [Shift]+T1.
2. Use **Blue** as a macro to set both envelope depths/polarities — park it mid-range for slow evolution.
3. Set **Orange** to the FM-like cross-mod region for harmonic motion.
4. Sweep **White** CW for a long-decay pad tail.
5. Set **Green** (OSC2 waveshape) by ear — ignore the on-screen graphic.
6. Optional diagnostic: temporarily drop OSC2 pitch to LFO range + bottom sine setting to audition the modulation type, then restore the pitch.

## Notes

- **No published numeric values** — this is a dialable recipe, not sourced knob positions. Knob roles are described qualitatively by forum engine analysts; tune by ear.
- DSynth has effectively 8 parameters across two oscillators (OSC2 params live under [Shift] on the encoders) — the OP-1's deepest stock engine.
- HONESTY FLAG: forum users warn the **Green** on-screen graphic does not match actual timbral behavior — dial by ear, not by the screen.
- Engine list shown is the OP-1 Field set (DSynth/DBox are Field-only additions over the original OP-1).

## Sources

- op-forums.com/t/demystifying-the-dsynth-and-dbox-engines/7094 (DSynth architecture analysis)
- magazinmehatronika.com/en/op-1-field-review/ (DSynth: "complex, evolving textures from cross-modulation; best for evolving pads, growling basses")
- dialable recipe (no published values) — synthesized from forum engine analysis + review
