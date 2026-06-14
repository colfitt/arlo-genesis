---
type: patch
title: B-Bender (pedal-steel glide)
device: Roland VG-800
date: 2026-06-14
description: Country/pedal-steel bends; lap-steel-adjacent smears into the End-Board reverbs — the one fully-parametrized factory preset.
tags: [pedal-steel, bend, performance, factory]
controls:
  - { name: "INST TYPE", type: switch, value: "E.GUITAR" }
  - { name: "STR BEND SW", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "BEND DEPTH (B string / string 2)", type: knob, value: "+2 semitones (one tone up)" }
  - { name: "BEND DEPTH (all other strings)", type: knob, value: "0" }
  - { name: "BEND CONTROL", type: knob, value: "0 (resting); assign 0→100 to CTL-1" }
  - { name: "CTL-1", type: button, value: "Hold = smooth +2 glide on the B string only; release = standard" }
  - { name: "Slot/Bank", type: knob, value: "Factory bank" }
---

# B-Bender (pedal-steel glide)

## Concept

Country/pedal-steel bends; lap-steel-adjacent smears into the End-Board reverbs — the one fully-parametrized factory preset (official BOSS). `STR BEND` raises only the B string +2 semitones; assigning `BEND CONTROL 0→100` to CTL-1 makes holding the switch produce a "super-smooth" (SoS) +2 glide on that string only.

## How to play it

1. Set `INST TYPE = E.GUITAR`, `STR BEND SW = ON`.
2. `BEND DEPTH` on the B string (string 2) = `+2` semitones (one tone up); all other strings `0`.
3. `BEND CONTROL = 0` (resting); assign `BEND CONTROL 0→100` to CTL-1.
4. Hold CTL-1 = smooth +2 glide on the B string only; release = standard.

## Notes

- The only fully-parametrized named factory preset (official BOSS).
- Off-rig-signature, but a clean template for the `STR BEND` mechanism — point it at the banjo for sliding partial-capo drones.

## Sources

- 🟢 official BOSS `research/links/boss-article-vguitar-advanced-features.md` (https://articles.boss.info/exploring-the-advanced-features-of-the-boss-v-guitar-system/); BEND ranges from parameter-guide-alt-tuning-values.md
- Transformed from Pedalxly VG-800-Patches.md (factory)
