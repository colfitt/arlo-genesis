---
type: patch
title: Drunk-Drivers Dropout Demo (repeatable warble)
device: Chase Bliss Generation Loss
date: 2026-06-14
description: CSH continuously-morphing lo-fi warble/dropout left audible as the hook — Failure-bounce so the dropout/crinkle character morphs continuously but stays musical. Ref GL-LF3 — Car Seat Headrest, "Drunk Drivers/Killer Whales".
tags: [lofi, ramping, taste-profile, warble, designed, signature, car-seat-headrest]
dips:
  FAILURE (ramp-target): on
  BOUNCE: on
  DROP BYP: on
controls:
  - { name: "Model", type: knob, value: "Model 7 (Dictatron-EX) or 10 (MS-Walker), from GL-LF1" }
  - { name: "Volume", type: knob, value: "= ramp SPEED (slow)" }
  - { name: "Saturate", type: knob, value: "~11:00" }
  - { name: "Wow", type: knob, value: "~9:00" }
  - { name: "Flutter", type: knob, value: "~9:00" }
  - { name: "Dry", type: switch, value: "Small", options: ["None", "Small", "Unity"] }
  - { name: "Aux", type: switch, value: "Fail (tap left footswitch for a one-shot snag accent)", options: ["Stop", "Filter", "Fail"] }
---

# Drunk-Drivers Dropout Demo (repeatable warble)

## Concept
CSH continuously-morphing lo-fi warble/dropout left audible as the hook. Starting from the Laptop-Bounce Cassette Demo (GL-LF1), the Failure ramp-target + Bounce make the dropout/crinkle character morph continuously but stay musical → the lo-fi warble left audible as a feature. Uses the verified Maintenance-Phase/Failure-bounce behavior (no MIDI clock needed).

## How to play it
1. Start from **Laptop-Bounce Cassette Demo** (#29 / GL-LF1).
2. Enable the **FAILURE ramp-target dip + BOUNCE dip** (Volume = ramp SPEED, slow) so the dropout/crinkle morphs continuously but stays musical.
3. Keep Saturate ~11:00, Wow/Flutter ~9:00, Dry **Small**.
4. For a one-shot snag accent over a section, set **Aux = Fail** and tap the left footswitch.
5. **Save the moving patch to a preset.**

## Notes
- 🟣 designed-to-emulate — chases the warts-as-feature result, not an artist setting. Clock positions are approximate intent.
- Store as an onboard preset (saves the *moving* patch).

## Sources
- designed from Gen-Loss ramp/Bounce behavior (sheet #18 Maintenance Phase; manual pg.38–41) + Failure surgery; Research/Taste-Profile/sources/car-seat-headrest-toledo-diy-lofi-method.md.
- Ref: GL-LF3 — Car Seat Headrest, "Drunk Drivers/Killer Whales" lo-fi warble left audible.
- Transformed from Pedalxly Generation-Loss-Patches.md (designed).
