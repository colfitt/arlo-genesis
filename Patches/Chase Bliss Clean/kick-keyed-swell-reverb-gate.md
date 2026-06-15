---
type: patch
title: Kick-Keyed Swell Reverb Gate
device: Chase Bliss Clean
date: 2026-06-15
description: "Tape Op's sleeper Clean move re-aimed at a drum trigger: with the SIDECHAIN dip ON, Clean's Dynamic Swell keys off an external MPC kick (via the 1/8\" sidechain jack) instead of your playing. Placed AFTER a big stereo reverb wash, every kick re-opens the swell so the wash pumps and re-blooms in time — a soft, musical 'swelling reverb gate' that breathes back up between hits rather than slamming shut. Concept + routing sourced from the Tape Op review + gearnews; exact knob values are not published — dial by ear."
tags: [sidechain, swell, reverb-gate, rhythmic, shoegaze, ambient, kick, texture]
dips:
  Dusty: off
  Swell Aux: "off (Dynamic Swell, not Manual)"
  Motion: off
  Noise Gate: off
  Sidechain: "on (external key — MPC kick into the 1/8\" TS jack)"
  Latch: off
  Spread: "off (pass the incoming stereo wash — don't re-spread)"
  MISO: "off (pass the incoming stereo wash — don't re-collapse)"
hidden:
  Swell In time (Wet knob): "fairly fast so the tail re-blooms snappily on the hit — dial by ear (no published value)"
  Swell Out time (Dry knob): "to taste — short Out = choppy gate, longer Out = gentle pulsing swell (no published value)"
controls:
  - { name: "AUX footswitch", type: button, value: "Swell engaged — Dynamic Swell now triggered by the keyed kick, not your playing" }
  - { name: "Sensitivity", type: knob, value: "set by ear / by the green LED so every kick crosses the swell threshold (LED flickers on the beat) — no published value" }
  - { name: "EQ", type: knob, value: "gentle, to taste underneath (no published value)" }
  - { name: "Dynamics", type: knob, value: "gentle — the swell does the gating, don't slam the limiter (no published value)" }
  - { name: "Wet", type: knob, value: "main page to taste — repurposed as Swell In time on the hidden page" }
  - { name: "Dry", type: knob, value: "main page to taste — repurposed as Swell Out time on the hidden page" }
  - { name: "Sidechain input", type: switch, value: "external key (MPC kick send) into the 1/8\" jack (SIDECHAIN dip ON)" }
---

# Kick-Keyed Swell Reverb Gate

## Concept
Tape Op's sleeper Clean move re-aimed at a drum trigger: with the SIDECHAIN dip ON, Clean's Dynamic Swell triggers off the keyed source (an MPC kick) instead of your playing. Placed AFTER a big stereo reverb wash, every kick hit re-opens the swell so the wash pumps and re-blooms in time — a "swelling reverb gate" that breathes back up between hits rather than slamming shut like a hard noise gate. Softer, more musical, and rhythmic. Distinct from the vocal-keyed "Swelling Reverb Gate" patch (different trigger source, and the reverb sits *before* Clean here) and from "Real Sidechain — Kick-Ducked Pump" (that one is a DRY-down limiting duck; this is a swell/gate that passes the wet wall in stereo).

## How to play it
1. Flip the **SIDECHAIN dip ON** and patch the MPC kick send into Clean's 1/8" sidechain jack.
2. **Engage the AUX swell** — the Dynamic Swell now responds to the keyed kick, not your playing.
3. Place Clean **AFTER** your reverb wash (e.g. an L&F slow-verb) so the swell gates an already-wet tail = a reverb gate, not a dry tremolo.
4. Set **Sensitivity** by the green LED so every kick crosses the threshold (LED flickers on the beat); too low = stutter / missed hits, too high = never closes.
5. **Hidden Options** (hold both footswitches until the LEDs go green): Swell In (Wet) fast for a snappy re-bloom, Swell Out (Dry) to taste — short = choppy gate, long = gentle tidal pulse.
6. Keep **MISO / SPREAD off** so the stereo wash passes through; keep **Dynamics gentle** (the swell is the gate, not the limiter).

## Notes
- **Concept and routing are sourced** (Tape Op / gearnews — external key into Clean's swell + reverb = a "weird, swelling reverb gate"); **exact knob values are not published.** Treat the control positions above as a dialable recipe and set them by ear.
- Re-aims the documented vocal-sidechain trick at a rhythmic drum trigger (MPC kick) and places the reverb **before** Clean so the swell chops the wash.
- If the chop is too hard / clicky, lengthen Swell Out; if it never gates, shorten Swell Out and raise Sensitivity.
- The sidechain input keys EQ and swells too (not just compression) — that's *why* a swell can be gated from an external source at all.
- Distinct from "Real Sidechain — Kick-Ducked Pump" (DRY-down limiting duck) and from "Swelling Reverb Gate — Vocal Sidechain Swell" (vocal key, reverb after Clean).

## Sources
- `research/links/daily-clean-stereo-spread-miso-and-chain-placement.md` (Tape Op triggers the Dynamic Swell from a sidechain into reverb for a "weird, swelling reverb gate"; sidechain could duck / swell from the Digitakt or another instrument for rhythmic motion)
- `gearnews.com/chase-bliss-clean-revolutionary-compression` (external sidechain + reverb = swelling reverb gate; more radical than standard ducking)
- Chase Bliss Clean official manual — Customize SIDECHAIN pp.34–35 (external signal controls comp / EQ / swells via the 1/8" input); Swell + Hidden Options pp.16–17, 30–31 (Wet = Swell In, Dry = Swell Out)
- [Tape Op review — Clean stereo compressor pedal](https://tapeop.com/reviews/gear/165/clean-stereo-compressor-pedal)
- Provenance: review-sourced concept (Tape Op + gearnews), re-aimed at an MPC kick trigger by DOUG — dialable recipe, no published knob values
