---
type: patch
title: Swelling Reverb Gate — Vocal Sidechain Swell
device: Chase Bliss Clean
date: 2026-06-15
description: "Tape Op's sleeper sidechain trick — with SIDECHAIN on, key Clean's Dynamic Swell from an external source (a vocal) feeding into a reverb so the swell engine opens and closes on the keyed signal, producing a 'weird, swelling reverb gate.' A more radical, secondary-knob-controllable take on classic ducking / gated reverb that blooms with the trigger. Concept sourced from the Tape Op review + gearnews; exact knob values are not published — dial by ear."
tags: [sidechain, swell, reverb-gate, ambient, vocal, texture, studio]
dips:
  Dusty: off
  Swell Aux: "off (Dynamic Swell) — ON for the manual/tap swell variant"
  Motion: off
  Noise Gate: off
  Sidechain: on
  Latch: "off — ON to taste"
  Spread: off
  MISO: off
hidden:
  Swell In time (Wet knob): "sets the bloom/open shape — dial by ear (no published value)"
  Swell Out time (Dry knob): "sets the close/decay shape — dial by ear (no published value)"
controls:
  - { name: "AUX footswitch", type: button, value: "Swell engaged (Dynamic Swell now triggered by the keyed source, not your playing)" }
  - { name: "Sensitivity", type: knob, value: "sets the swell trigger threshold from the sidechain — dial so the keyed source crosses it (no published value)" }
  - { name: "EQ", type: knob, value: "to taste underneath (no published value)" }
  - { name: "Dynamics", type: knob, value: "to taste underneath (no published value)" }
  - { name: "Wet", type: knob, value: "main page to taste — repurposed as Swell In time on the hidden page" }
  - { name: "Dry", type: knob, value: "main page to taste — repurposed as Swell Out time on the hidden page" }
  - { name: "Sidechain input", type: switch, value: "external key (vocal) into the 1/8\" jack (SIDECHAIN dip ON)" }
---

# Swelling Reverb Gate — Vocal Sidechain Swell

## Concept
Tape Op's standout sidechain trick: with the SIDECHAIN dip ON, you key Clean's Dynamic Swell from an external source (a vocal) feeding into a reverb. The swell engine opens and closes on the *keyed* source instead of your playing, so the reverb blooms and ducks with the trigger — a "weird, swelling reverb gate." It's a more radical, secondary-knob-controllable take on classic ducking / gated reverb: the Swell In/Out times and Sensitivity let you shape exactly how the bloom attacks and decays around the keyed signal.

## How to play it
1. Flip the **SIDECHAIN dip ON** and patch the keying source (e.g. a vocal) into the 1/8" jack.
2. **Engage the AUX swell** — the Dynamic Swell now responds to the keyed source, not your playing.
3. **Hidden Options** (hold both footswitches until the LEDs go green): set Swell In (Wet) for the open shape and Swell Out (Dry) for the close shape; set **Sensitivity** so the keyed source crosses the trigger threshold.
4. Run Clean's output into a **reverb** and blend the swelling, reverb-tailed signal back with the dry source.

## Notes
- **Concept and use are sourced** (Tape Op / gearnews — vocal sidechain into reverb after Clean = swelling reverb gate); **exact knob positions are not published.** Treat the control values above as a dialable recipe and set them by ear.
- More radical than standard ducking: the secondary knobs (Swell In/Out, Sensitivity) let you shape the swell's attack/decay rather than just gating on/off.
- On-brand sleeper for the rig: key the swell from the **Digitakt** or another instrument instead of a vocal for rhythmic stereo motion into the texture / ambient boards.

## Sources
- `research/links/daily-clean-stereo-spread-miso-and-chain-placement.md` (Tape Op triggers the Dynamic Swell from a vocal sidechain into reverb for a "weird, swelling reverb gate"; sidechain could duck/swell from the Digitakt)
- `gearnews.com/chase-bliss-clean-revolutionary-compression` (vocal sidechain + reverb after Clean = swelling reverb gate blended back; more radical than standard ducking)
- [Tape Op review — Clean stereo compressor pedal](https://tapeop.com/reviews/gear/165/clean-stereo-compressor-pedal)
- Provenance: review (Tape Op + gearnews) — dialable recipe, no published values
