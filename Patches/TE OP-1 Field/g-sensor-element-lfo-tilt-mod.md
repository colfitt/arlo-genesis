---
type: patch
title: "G-sensor — tilt modulation (Element LFO)"
device: TE OP-1 Field
date: 2026-06-15
description: "A hands-free, embodied modulation recipe — the Element LFO with a G-force source turns the OP-1's accelerometer into a performance controller: tilt the unit to sweep a filter for a tilt-wah, or scrub a long sample's playback position for a tilt-controlled granular freeze. Community recipe (ratbag98 / op1tips): depth ±100 is documented, the destination is to-taste."
tags: [g-sensor, modulated, element, granular, performance-setup]
dips:
  INTERNAL_MOD: "one connection per patch — Element-tilt uses it up"
controls:
  - { name: "LFO", type: switch, value: "element (G-sensor / tilt source)", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "Element source", type: switch, value: "G-force" }
  - { name: "Element depth", type: knob, value: "±100 (use -100 for sample-position scrub)" }
  - { name: "Element destination", type: switch, value: "filter cutoff (tilt wah) OR sample playback position (to-taste)" }
  - { name: "Sample playback", type: switch, value: "Play to End (for the position-scrub variant)" }
---

# G-sensor — tilt modulation (Element LFO)

## Concept

Use the accelerometer as a hands-free mod source. Set the **Element LFO** to a **G-force** source and the OP-1 listens to physical tilt instead of an internal clock. Point it at filter cutoff and you get a **tilt-wah** you sweep with your wrist; point it at a long sample's playback position (set to **Play to End**) and tilt becomes a **granular scrub / freeze** controller. Near-flat is the slow, granular sweet spot — this is performative, embodied modulation, and a genuinely unique OP-1 move where the motion sensor becomes a scrubbing controller.

## How to play it

1. Select the **Element LFO**; set source = **G-force**.
2. Set depth to **±100** (use **-100** for sample-position scrub).
3. Route the destination to **filter cutoff** (tilt wah) or, on a long sample set to **Play to End**, to **playback position**.
4. **Tilt the unit** to modulate live; hold it near level for the slow / granular sweet spot.
5. Record the gesture to tape for a one-take performance.

## Notes

- Documented community trick (ratbag98 / op1tips): **depth ±100 is the published value**; the **destination is to-taste** — the filter-cutoff "tilt-wah" framing is a dialable choice, not a sourced parameter, so treat the routing as a recipe rather than an exact preset.
- Only **one internal mod connection per patch** — using the Element LFO for tilt uses it up.
- A genuinely unique OP-1 move: the motion sensor becomes a scrubbing controller. Relates to the existing `wonky_bass` (element / tilt) patch but generalizes the technique to any destination.

## Sources

- Gear/TE OP-1 Field/research/links/github-ratbag98-op1tips-distilled.md (§G-sensor; §Stereo — G-sensor time-stretch)
- Gear/TE OP-1 Field/research/OP-1-Field-UsageGuide.md §1 (G-sensor modulation, Element LFO depth ±100)
- github.com/ratbag98/op1tips (Element LFO G-sensor source, depth -100, Play-to-End scrub)
