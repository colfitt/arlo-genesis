---
type: patch
title: "Elk-Faithful 330pF Mod — single-cap tone-stack swap"
device: EarthQuaker Devices Hizumitas
date: 2026-06-15
description: "The single documented circuit mod for the Hizumitas — swap the tone-stack high-pass-filter cap from the stock 3n3 to 330pF for a much more Elk-faithful build (the original Elk BM Sustainar used 330pF; the Hizumitas's 3n3 is ~10x larger, which is what gives the wide clockwise low-end swing). An intermediate ~1nF value is a middle ground if the CW/bass side is too dark for your source. This is a HARDWARE mod, not a knob setting, and is not officially supported by EQD. Sourced from DeepResearch §12 + a vero-p2p 3n3-vs-330pF analysis — the most concrete public circuit datum on this pedal."
tags: [mod, reference, fuzz, factory]
controls:
  - { name: "Tone-stack HPF cap", type: switch, value: "hardware mod: 3n3 (stock) → 330pF (Elk-faithful) or ~1nF (less low-end swing)", options: ["3n3 (stock)", "330pF (Elk-faithful)", "~1nF (less low-end swing)"] }
  - { name: "Volume", type: knob, value: "re-dial to taste after the mod (recipe, no published value)" }
  - { name: "Sustain", type: knob, value: "re-dial to taste after the mod (recipe, no published value)" }
  - { name: "Tone", type: knob, value: "re-dial to taste after the mod — the bass/treble pivot sits differently (recipe, no published value)" }
---

# Elk-Faithful 330pF Mod — single-cap tone-stack swap

## Concept
The Hizumitas is EQD's clone of the Elk BM Sustainar, but the documented circuit analysis shows one deliberate deviation: the tone-stack high-pass-filter cap is 3n3, roughly 10x larger than the 330pF the original Elk used. That larger cap is what produces the Hizumitas's signature wide low-end swing as you turn Tone clockwise. Swapping that single cap to 330pF gives you a much closer Elk-faithful build; swapping it to something in between (e.g. ~1nF) keeps more of the modern voice but tames the aggressive low-end swing on the clockwise side. This is the single biggest documented circuit difference from the Elk and the most concrete public circuit datum on the pedal.

## How to play it
1. Open the pedal and locate the tone-stack high-pass-filter cap (stock value 3n3) — the obvious mod target.
2. For an Elk-faithful voicing, swap it to 330pF (the Elk's original value).
3. For a middle ground with less low-end swing on the CW side, try ~1nF instead.
4. Reassemble. The Tone knob's bass/treble pivot will now sit differently, so re-dial Volume, Sustain, and Tone to taste.

## Notes
- Documented mod target: *"The 3n3 tone cap is the obvious mod target. Swap to 330pF and you have a much closer Elk-faithful build. Swap to something between (e.g. 1nF) for less aggressive low-end swing."*
- **Honesty flag:** this is a HARDWARE mod, not a knob setting — it is NOT officially supported by EQD, and there are no published knob values to pair with it. The knob positions above are a dialable recipe (re-dial to taste post-mod), not sourced settings. No new community mod chatter surfaced this pass.
- The 3n3-vs-330pF tone-stack cap is the single biggest documented circuit deviation from the Elk and the most concrete public circuit datum for this pedal.
- Useful in this rig if the bright banjo on Board 1 needs less aggressive low-end swing on the clockwise Tone side — the ~1nF middle ground is the safer first step there.

## Sources
- DeepResearch §12 — *"The 3n3 tone cap is the obvious mod target. Swap to 330pF... Elk-faithful build. Swap to something between (e.g. 1nF) for less aggressive low-end swing"*; §1 vero-p2p 3n3-vs-330pF analysis (`gear/EarthQuaker Devices Hizumitas/research/Hizumitas-DeepResearch.md` §12, §1).
- Usage guide — *"the 3n3 tone cap is the single-cap mod target (→330pF for Elk-faithful, ~1nF for less low-end swing)"* (`research/Hizumitas-UsageGuide.md` §8).
- Provenance: DeepResearch §12 + vero-p2p (hardware mod — circuit datum, not a knob setting).
</content>
</invoke>
