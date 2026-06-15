---
type: patch
title: "Pickup Morphing — continuous neck↔bridge morph"
device: Roland VG-800
date: 2026-06-15
description: "The factory \"Pickup Morphing\" preset Juca Nery tours — a continuous morph between modeled pickup positions (neck↔bridge), as opposed to the discrete Pickup Selector toggle. Sweep warm neck to bright bridge live, footswitch- or expression-controlled."
tags: [performance, pickup, factory, morph]
dips:
  MORPH ASSIGN: "EXP pedal (EV-30/FV-500) on a CTL/EXP jack for continuous morph, or CTL-1 for a two-state morph"
controls:
  - { name: "INST TYPE", type: switch, value: "E.GUITAR" }
  - { name: "Modeled pickup position", type: knob, value: "morph assigned to CTL-1 (toggle) or an EXP pedal (continuous) — dial from the factory memory, no published values" }
  - { name: "CTL-1", type: button, value: "two-state neck↔bridge morph (discrete)" }
  - { name: "EXP pedal (EV-30/FV-500)", type: knob, value: "continuous neck (warm) → bridge (bright) sweep on a CTL/EXP jack" }
  - { name: "Slot/Bank", type: knob, value: "Factory bank" }
---

# Pickup Morphing — continuous neck↔bridge morph

## Concept

The factory "Pickup Morphing" preset Juca Nery tours — a continuous morph between modeled pickup positions (neck↔bridge), as opposed to the discrete Pickup Selector toggle. Sweep the tone from warm neck to bright bridge live, footswitch- or expression-controlled. Named factory memory, distinct from the existing Pickup Selector patch (that one is a discrete neck/bridge toggle on CTL-1).

## How to play it

1. Recall the factory "Pickup Morphing" memory.
2. Confirm the modeled pickup position is mapped to CTL-1 (toggle) or an EXP pedal (continuous morph).
3. Sweep from neck (warm) to bridge (bright) as you play.
4. Pair with the existing Pickup Selector patch if you want the discrete toggle instead.

## Notes

- Named factory preset (Juca Nery: "Pickup Morphing"). Distinct from the existing Pickup Selector patch (that's a discrete neck/bridge toggle on CTL-1).
- Exact control-assign values are not published — dial from the factory memory. The controls above are a dialable recipe, not captured values.
- No onboard treadle, so continuous morph needs an external EXP pedal (EV-30/FV-500) on a CTL/EXP jack.

## Sources

- 🟢 `research/transcripts/juca-nery-creative-tool-patch-tour.md` ("Pickup Morphing")
- `research/links/boss-article-vguitar-advanced-features.md` (CTL/EXP jack map)
- `research/VG-800-DeepResearch.md` §8 (no onboard treadle; add EV-30/FV-500)
