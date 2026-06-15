---
type: patch
title: "Clean-Up Lever — Gain 1 down, Volume up via expression"
device: Chase Bliss Brothers AM
date: 2026-06-15
description: That Pedal Show's clever external-control move — assign one expression sweep to control Channel 1's GAIN and Channel 2's MASTER volume at once, so a single foot motion lets you clean up by rolling the gain DOWN while the output volume holds (or rises) to keep your level up. A foot-operated clean-up that drops saturation without losing level, exploiting the KOT-style strong cleanup behavior. TPS-quoted assignment; no exact knob numbers — dial from recipe.
tags: [expression, overdrive, cleanup, master, performance, designed]
dips:
  MASTER: on
hidden:
  CONTROL dip bank (right side): assign the expression pedal to control GAIN 1 and VOL 2 (master) together; sweep toward 'clean' = GAIN 1 down + level held/raised by VOL 2. On a Morningstar/MIDI controller, set the expression rule at the BANK level.
controls:
  - { name: "CHANNEL 1 MODE", type: switch, value: "OVERDRIVE (the gain being cleaned up)", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 1", type: knob, value: "swept by the expression pedal toward 'clean' (rolls DOWN); dial from recipe — no published value" }
  - { name: "VOL 1", type: knob, value: "dial from recipe — no published value" }
  - { name: "TONE 1", type: knob, value: "to taste" }
  - { name: "CHANNEL 2 MODE", type: switch, value: "BOOST or OVERDRIVE, with MASTER active", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN 2", type: knob, value: "dial from recipe — no published value" }
  - { name: "VOL 2", type: knob, value: "acts as the global MASTER (MASTER dip on); co-controlled by the expression sweep to hold/raise level as GAIN 1 drops" }
  - { name: "TONE 2", type: knob, value: "to taste" }
  - { name: "PRESENCE", type: knob, value: "to taste" }
  - { name: "EXP/CV", type: button, value: "assigned to BOTH GAIN 1 and VOL 2 (master) via the CONTROL dips / MIDI controller; sweep toward 'clean' to roll gain down while level holds up" }
---

# Clean-Up Lever — Gain 1 down, Volume up via expression

## Concept
That Pedal Show's clever external-control move: assign expression so it controls Channel 1's GAIN and Channel 2's MASTER volume at the same time, so a single sweep lets you clean up — turn the gain DOWN while the output volume keeps your level up. A foot-controlled clean-up that drops saturation without losing level, exploiting the KOT's strong cleanup behavior. Channel 1 (OVERDRIVE) is the gain being cleaned up; Channel 2 carries the MASTER (VOL 2) that the same sweep holds or raises.

## How to play it
1. Turn the MASTER dip ON so VOL 2 is the global master.
2. In the CONTROL dip bank, assign the expression pedal to control GAIN 1 and VOL 2 together (TPS's "two CCs from one expression input" idea on a MIDI controller).
3. Sweep the expression pedal toward 'clean' to roll GAIN 1 down while the master volume keeps your level up.
4. Use it like a foot-operated clean-up: less saturation, same or more level, on the fly.

## Notes
- TPS-quoted: the "gain of side one + master of side two so you can clean up" assignment is quoted; no exact knob numbers — dial from recipe.
- On a Morningstar/MIDI controller: set expression rules at the BANK level (not preset), use a Ring-Active TRS-to-TRS cable, and the 'Select Exp Message' trick to drive two CCs from one input.
- Distinct from the Ramped Drone Swell (which ramps saturation UP into Channel 2): this is a cleanup-DOWN lever that preserves level.

## Sources
- research/transcripts/tps-vs-prince-duke-of-tone.md ("have the gain control of side one and control the master of side two… so you can clean up — turn the gain down but adjust the volume of side two")
- research/links/tps-demo-settings.md (external control)
- research/links/morningstar-expression-bank-level.md (bank-level rule; two-CC-from-one-input trick)
- Ref: That Pedal Show — Brothers AM (2025-04-25)
