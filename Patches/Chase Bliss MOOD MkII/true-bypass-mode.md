---
type: patch
title: True-Bypass mode (footswitch toggle)
device: Chase Bliss MOOD MkII
date: 2026-06-15
description: Switch MOOD from its default buffered-bypass-with-trails into hard true-bypass by tapping both footswitches three times — useful for getting the pedal fully out of the signal path, but the always-listening Micro-Looper does NOT run in true-bypass, so capture stops working. A factory bypass mode documented in the community hidden-options walkthrough and the manual (p.17).
tags: [bypass, io, footswitch, factory, technique]
dips:
  TRAILS: "on (keep on so toggling mid-performance doesn't kill the wash)"
controls:
  - { name: "LEFT + RIGHT footswitches (true-bypass toggle)", type: switch, value: "tap BOTH footswitches 3× to enter true-bypass; tap either footswitch to exit back to buffered bypass" }
  - { name: "All three LEDs", type: switch, value: "blink red to confirm true-bypass is active" }
---

# True-Bypass mode (footswitch toggle)

## Concept
By default MOOD sits in buffered bypass with trails. Tapping **both footswitches three times** in quick succession flips it into hard **true-bypass**, pulling the pedal entirely out of the signal path — all three LEDs blink red to confirm. The catch: the always-listening Micro-Looper does **not** run in true-bypass, so its continuous capture stops working. Tap either footswitch to exit back to buffered bypass with trails. There are no knob values here — this is a footswitch gesture, not a knob recipe.

## How to play it
1. Tap both footswitches three times in quick succession.
2. Confirm: all three LEDs blink red — you're now in true-bypass.
3. Use it when you want MOOD entirely out of the chain.
4. Tap either footswitch to exit and return to buffered bypass with trails.

## Notes
- This patch has **no published knob values** — it's a footswitch gesture/toggle, not a dialable knob recipe.
- ⚠️ The Micro-Looper does **NOT** run in true-bypass — if you rely on always-listening capture, stay in buffered bypass.
- Default is buffered bypass with trails (keep **TRAILS** on so toggling mid-performance doesn't kill the wash).
- Same gesture also lives in the hidden/reset family — don't trigger it by accident.

## Sources
- gear/Chase Bliss MOOD MkII/research/transcripts/youtube-mood-mkii-hidden-options-dip-walkthrough.md (True bypass: tap both footswitches 3×, LEDs blink red; looper doesn't run in true-bypass)
- gear/Chase Bliss MOOD MkII/research/MOOD-MkII-DeepResearch.md §8 (Buffered bypass with trails; true-bypass via 3× both footswitches; looper won't run in true-bypass, manual p.17)
- gear/Chase Bliss MOOD MkII/research/links/community-mood-mkii-pitfalls-and-gotchas.md (true-bypass = both FS 3×; looper does not run in true-bypass)
