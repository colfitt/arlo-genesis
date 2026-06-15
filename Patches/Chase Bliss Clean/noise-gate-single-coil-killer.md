---
type: patch
title: "Noise Gate — Single-Coil Hum Killer"
device: Chase Bliss Clean
date: 2026-06-15
description: "Flip the NOISE GATE dip and Clean mutes the input between notes to kill the hum and hiss that compression amplifies — especially on single-coil or noisy vintage pickups. Factory mode plus a community gotcha (manual NOISE GATE p.35 / Hidden Options + Elektronauts Python): the threshold-low rule is published, the rest is a dialable recipe."
tags: [noise-gate, utility, single-coil, hum, gate, community]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: on
  Sidechain: off
  Latch: off
  Spread: off
  MISO: off
controls:
  - { name: "Sensitivity", type: knob, value: "GATE THRESHOLD in gate mode — keep LOW (an owner ran it 'all the way down' for quiet fingerstyle); dial from recipe, no published value" }
  - { name: "Dynamics", type: knob, value: "GATE RELEASE TIME in gate mode — set so the tail closes naturally, not abruptly; dial from recipe, no published value" }
  - { name: "Wet", type: knob, value: "your underlying comp's output — dial from recipe, no published value" }
  - { name: "Dry", type: knob, value: "to taste for parallel — dial from recipe, no published value" }
  - { name: "Attack", type: knob, value: "your underlying comp setting — dial from recipe, no published value" }
  - { name: "EQ", type: knob, value: "your underlying comp setting — dial from recipe, no published value" }
  - { name: "Release", type: switch, value: "to taste (runs your underlying comp)", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "Mid (stable)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
---

# Noise Gate — Single-Coil Hum Killer

## Concept
Flip the NOISE GATE dip and Clean mutes the input between notes to kill the hum and hiss that compression otherwise amplifies — especially on single-coil or noisy vintage pickups, where the comp's makeup gain drags up the noise floor between phrases. In gate mode the two main knobs are repurposed (confirmed in Hidden Options): SENSITIVITY becomes the gate threshold and DYNAMICS becomes the gate release. The owner gotcha is the whole reason this patch has a warning section: set the threshold LOW or it swallows lightly fingerpicked notes — critical for the quiet banjo control band.

## How to play it
1. Dial your normal compression tone first, then flip the NOISE GATE dip ON.
2. Enter Hidden Options and set the gate threshold (Sensitivity) LOW first — high enough to mute the hum, low enough to pass your softest intended notes.
3. Set the gate release (Dynamics) so the tail closes naturally, not abruptly.
4. Verify with your quietest fingerpicked note: if it gets swallowed, drop the threshold further.

## Notes
- Owner gotcha (Python / Elektronauts): "completely turn down the threshold or it will swallow up lightly finger-picked notes" — critical for the quiet banjo control band.
- Sensitivity/Dynamics are repurposed in gate mode, so you can't also use them for compression at the same time the way you would on the main page.
- No published knob values for the comp side of this patch — controls above are a dialable recipe, not sourced settings. Only the threshold-low rule is published; everything else is set to taste against your underlying compression tone.

## Sources
- `research/links/cb-manual-clean-compression-recipes.md` (NOISE GATE p.35 + Hidden Options p.17: Sensitivity = gate threshold, Dynamics = gate release)
- `research/links/elektronauts-clean-community-recipes.md` (Python: turn gate threshold fully down or it swallows lightly finger-picked notes)
- `research/links/compressorpedalreviews-clean-deep-dive.md` (noise-gate gotcha; threshold low or it eats soft notes)
- Chase Bliss Clean official manual (Customize NOISE GATE p.35, Hidden Options pp.16–17)
- elektronauts.com/t/chase-bliss-clean-the-creative-compressor-pedal/223147
