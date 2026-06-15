---
type: patch
title: "Adaptive Envelope — Stay-Out-of-the-Way Comp"
device: Chase Bliss Clean
date: 2026-06-15
description: A Hidden Options responsiveness tweak — switch the envelope follower to Adaptive (or Combo) so attack/release dynamically adjust to your playing loudness, helping fast/dense passages keep their energy while staying out of the way. Layers under any comp recipe. Manufacturer feature per the Clean manual's Envelope Type section.
tags: [envelope, adaptive, combo, responsive, fast-playing, compression]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: off
  MISO: off
hidden:
  Envelope Type (Release toggle in Hidden Options): "ADAPTIVE (reactive follower) or COMBO (Analog attack + Adaptive release); Analog is the smoother, more static default"
controls:
  - { name: "Release", type: switch, value: "in Hidden Options = Envelope Type select: ADAPTIVE or COMBO (normally L Fast 50ms / Mid User 650ms / R Slow 1.5s)", options: ["Analog (default)", "Combo", "Adaptive"] }
  - { name: "Attack", type: knob, value: "sets the SLOWEST attack bound — the envelope adapts faster within it (dial to taste from your comp recipe)" }
  - { name: "Dynamics", type: knob, value: "to taste (dial from underlying comp recipe)" }
  - { name: "Sensitivity", type: knob, value: "by LED (dial from underlying comp recipe)" }
  - { name: "Wet", type: knob, value: "to taste (dial from underlying comp recipe)" }
  - { name: "Dry", type: knob, value: "to taste (dial from underlying comp recipe)" }
  - { name: "EQ", type: knob, value: "to taste (dial from underlying comp recipe)" }
  - { name: "Mode", type: switch, value: "to taste", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "to taste", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
---

# Adaptive Envelope — Stay-Out-of-the-Way Comp

## Concept
A behind-the-scenes responsiveness tweak that layers under any comp recipe. In Hidden Options, switch the envelope follower's ENVELOPE TYPE from the default Analog to **Adaptive** (or **Combo**). Adaptive makes attack/release dynamically adjust to your playing loudness — it helps fast playing keep its energy and stays out of the way, where Analog is smoother but more static. **Combo** pairs Analog attack with Adaptive release for the best of both: the responsiveness of Adaptive with the accuracy of Analog. With an adaptive type, ATTACK and RELEASE now set the *slowest possible* speeds, and the envelope adjusts faster within that range based on how hard you play.

## How to play it
1. Start from any comp recipe you like (e.g. Tight & Lively for funk/fast dense playing).
2. **Hold both footswitches** to open Hidden Options.
3. Set the **Release toggle (= Envelope Type in Hidden Options)** to **ADAPTIVE** for a reactive follower, or **COMBO** for Analog-attack + Adaptive-release.
4. Treat your ATTACK/RELEASE settings as the *slowest* bounds; the envelope will adapt faster within them based on your playing.
5. Use under fast/dense passages to keep energy without over-squishing; A/B against Analog to hear the smoother-but-static contrast.

## Notes
- Mode selection is a documented manufacturer feature; the **comp knob values here are a dialable recipe, not published settings** — borrow exact values from whatever comp patch you layer this under, then just flip the Envelope Type.
- Manual: "Adaptive is good at staying out of the way and helps faster playing maintain its energy, but it's not quite as smooth as Analog."
- Combo = "responsiveness of Adaptive with the accuracy of Analog."
- Layers under any other comp patch — pairs especially well with Tight & Lively for funk / fast dense playing.
- All CUSTOMIZE dips OFF; only the Hidden Options Envelope Type changes.

## Sources
- Chase Bliss Clean official manual — Hidden Options, Envelope Type / Combo (pp. 18–19): Analog / Combo / Adaptive follower behavior; Attack/Release become slowest-speed bounds under adaptive types
- `research/links/guitarpedalx-clean-hidden-options-map.md` (Release toggle = Envelope Type: Analog / Combo / Adaptive)
