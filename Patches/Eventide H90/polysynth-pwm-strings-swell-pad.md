---
type: patch
title: "PolySynth — PWM Strings Swell Pad (freeze + solo)"
device: Eventide H90
date: 2026-06-15
description: "Turn the guitar/banjo into a polyphonic analog-style string-synth pad with a slow attack — chords become a lush, filtered PWM string section that swells in, and PolySynth's Freeze sustains the pad so you can solo on top. The starting point (load PolySynth, select 'PWM Strings', raise Attack, tweak the filter) is Eventide staff/announcement direction and the param set is from the H90 manual; exact knob values are not published, so this is a dialable recipe."
tags: [polysynth, synth, pad, strings, pwm, swell, freeze, sustained-wall]
dips:
  EXP: "assign Attack or Cutoff to expression for live swell/filter sweeps"
  LFO: "route LFO to pulse width to simulate chorusing"
  FREEZE: "Performance Parameter (momentary or latching); persists across HotSwitch toggles"
controls:
  - { name: "Preset A Algorithm", type: switch, value: "PolySynth (SIFT polyphonic guitar-to-synth)" }
  - { name: "Preset", type: switch, value: "PWM Strings (factory starting point)" }
  - { name: "Attack", type: knob, value: "raise for a slower, pad-like swell (recipe — no published value)" }
  - { name: "Cutoff", type: knob, value: "set filter brightness to taste (recipe — no published value)" }
  - { name: "Resonance", type: knob, value: "add for filter character (recipe — no published value)" }
  - { name: "Env Amount", type: knob, value: "sets filter-sweep depth (recipe — no published value)" }
  - { name: "Env Sense", type: knob, value: "sets how playing dynamics drive the filter (recipe — no published value)" }
  - { name: "LFO Rate", type: knob, value: "modulation speed (recipe — no published value)" }
  - { name: "LFO Shape", type: switch, value: "7 waveforms incl. Random + S&H (recipe — no published value)" }
  - { name: "LFO Amount", type: knob, value: "modulation depth (recipe — no published value)" }
  - { name: "Detune", type: knob, value: "raise for width/chorusing (recipe — no published value)" }
  - { name: "Spread", type: knob, value: "raise for stereo width (recipe — no published value)" }
  - { name: "Voice 1/2/3", type: knob, value: "Level / Shift / Shape per voice (recipe — no published value)" }
  - { name: "Freeze", type: switch, value: "map to a Perform footswitch — momentary or latching" }
---

# PolySynth — PWM Strings Swell Pad (freeze + solo)

## Concept
Turn the guitar or banjo into a polyphonic analog-style string-synth pad with a slow attack — chords become a lush, filtered PWM string section that swells in. PolySynth is the H90's SIFT polyphonic guitar-to-synth algorithm; starting from the factory "PWM Strings" preset and raising Attack gives that slow, pad-like bloom, while Cutoff/Resonance and the envelope (Env Amount/Sense) shape the filter and Detune/Spread open up the width. Because PolySynth has a Freeze, you can sustain the pad indefinitely and solo on top.

## How to play it
1. Load **PolySynth** on Preset A and select the **'PWM Strings'** preset.
2. Raise **Attack** for a slower, pad-like swell.
3. Tune **Cutoff/Resonance** for the filter character; dial **Env Amount/Sense** for a filter sweep that tracks your playing.
4. Add **Detune** and **Spread** for width; route the **LFO** to pulse width to simulate chorusing.
5. Map **Freeze** to a Perform footswitch — hold a chord, hit Freeze to lock the pad, and solo over it.
6. Optionally map **Attack** or **Cutoff** to expression for live swell/filter sweeps.

## Notes
- No published exact knob values for this recipe — treat the control values above as a dialable starting point, not sourced settings. What IS sourced: the start-at-'PWM Strings' + raise-Attack + tweak-filter direction is Eventide staff/forum + the PolySynth announcement, and the param set (Attack, Cutoff, Resonance, Env Amount/Sense, LFO Rate/Shape/Amount, Detune, Spread, three voices) is from the H90 manual.
- PolySynth is best for a "synthy" pad, vs Polyphony's more natural/organ-like tone.
- Freeze is a Performance Parameter (momentary or latching) and persists across HotSwitch toggles, so a frozen pad survives switching HotSwitch states.
- The LFO offers 7 waveforms including Random and Sample & Hold; pointing it at pulse width is the chorusing trick.

## Sources
- https://cdn.eventideaudio.com/manuals/h90/1.12.5/content/algorithms/synth.html (PolySynth params: Attack, Cutoff, Resonance, Env Amount/Sense, LFO, Detune, Spread)
- https://www.synthtopia.com/content/2023/12/03/eventide-intros-polysynth-for-h90-harmonizer-multi-effects-pedal/ (3 voices, LFO mod of cutoff/PWM/volume, envelope filter control, adjustable attack)
- research/links/eventide-forum-shimmer-swell-modechoverb-techniques.md (PolySynth swell — staff: start 'PWM Strings', Attack up, tweak filter)
- research/links/h90-ambient-pad-settings-recipes.md (Pads-to-solo-over: PolySynth Freeze)
- Provenance: manufacturer docs/announcement + Eventide staff direction — controls/preset published, values dialable
