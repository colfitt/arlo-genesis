---
type: patch
title: "Andy's Expression Treble Lead — sweep Gain 1 under the Rangemaster"
device: Chase Bliss Brothers AM
date: 2026-06-15
description: AndyDemos' expression setup — assign the expression pedal (or CV) to GAIN 1 with the classic Rangemaster treble booster on Channel 1, over a Channel-2 OVERDRIVE foundation (amp clean by itself). Sweep the pedal heel→toe to roll Channel 1's gain up and down under the booster for a swelling, vocal lead you control with your foot. Every knob is EXP/CV controllable; MIDI goes deeper (dips + presence too).
tags: [expression, cv, treble-booster, rangemaster, overdrive, lead, community]
dips:
  CONTROL bank (right side): assign EXP (or 0–5V CV) → GAIN 1; set HEEL = low / TOE = high range; MASTER on optional so the sweep changes saturation without moving stage level
controls:
  - { name: "TREBLE BOOSTER", type: switch, value: "DOWN (classic Rangemaster, feeding Channel 1)", options: ["UP (bright)", "MIDDLE (off)", "DOWN (Rangemaster)"] }
  - { name: "CHANNEL 1 MODE", type: switch, value: "BOOST or OVERDRIVE (the swept channel)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 1", type: knob, value: "swept by the expression pedal (heel = low, toe = high); dial from recipe" }
  - { name: "VOL 1", type: knob, value: "dial from recipe" }
  - { name: "TONE 1", type: knob, value: "dial from recipe" }
  - { name: "CHANNEL 2 MODE", type: switch, value: "OVERDRIVE (the foundation, since the amp is clean)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 2", type: knob, value: "dial from recipe" }
  - { name: "VOL 2", type: knob, value: "dial from recipe" }
  - { name: "TONE 2", type: knob, value: "dial from recipe" }
  - { name: "PRESENCE", type: knob, value: "DOWN" }
  - { name: "EXP/CV", type: button, value: "assigned to GAIN 1 via the CONTROL (right-side) dips; sweep heel→toe to swell the lead gain" }
---

# Andy's Expression Treble Lead — sweep Gain 1 under the Rangemaster

## Concept
AndyDemos' expression setup: assign the expression pedal (or CV) to GAIN 1 with the classic Rangemaster treble booster engaged on Channel 1, over a Channel-2 OVERDRIVE foundation (amp clean by itself). Sweeping the expression pedal rolls Channel 1's gain up and down under the booster for a swelling, vocal lead you control with your foot. Every knob is expression/CV controllable; MIDI goes deeper (dips + presence too).

## How to play it
1. Set the treble booster DOWN (classic Rangemaster) feeding Channel 1.
2. Set Channel 2 to OVERDRIVE as the foundation (works with a clean amp).
3. On the right-side CONTROL dip bank, assign the expression pedal (or 0–5V CV) to GAIN 1 and set the heel/toe range.
4. Sweep the expression pedal to roll Channel 1's gain up and down under the booster for a vocal, swelling lead.
5. Turn MASTER on if you want the sweep to change saturation without moving stage level; for deeper control use MIDI (which also moves dips/presence).

## Notes
- AndyDemos-quoted: the assignment (EXP → GAIN 1, Rangemaster on Ch1, Ch2 OD foundation) is quoted; CB confirms CV/expression over every knob and MIDI over dips + presence. No exact knob numbers — dial from recipe.
- Distinct from Ramped Drone Swell (which sweeps the push into Channel 2 for a drone build): this is a foot-controlled lead-gain swell with the booster on the front channel.
- CONTROLLER GOTCHA — on a Morningstar/MIDI controller, set the expression rule at the BANK level, not the preset level (documented gotcha).

## Sources
- research/transcripts/andy-brothers-am-demo.md ("expression pedal control… on channel one with the treble booster… activation of the gain control on channel one… foundation sound channel two with overdrive")
- research/links/andy-demo-settings.md ("Expression setup")
- https://www.chasebliss.com/brothers-am (CV/expression over every knob; MIDI controls everything incl. dips and presence)
- https://forum.morningstar.io/t/expression-control-via-midi-for-chase-bliss-am-brothers/11209 (expression-over-MIDI for Brothers AM)
- research/links/morningstar-expression-bank-level.md (bank-level rule)
- Ref: AndyDemos — Chase Bliss Brothers AM (2025-04-15)
