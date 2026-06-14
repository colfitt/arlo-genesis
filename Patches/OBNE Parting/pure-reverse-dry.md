---
type: patch
title: Pure Reverse Dry (Modified Mix)
device: OBNE Parting
date: 2026-06-14
description: Uses Parting's unique Modified Mix mode to send the DRY signal through reverse too, so the entire tone plays backwards — a pure shoegaze/art-rock reverse swell with no clean signal poking through.
tags: [reverse, shoegaze, art-rock, modified-mix, signature, designed]
hidden:
  Mix Mode (Modified — dry AND wet pass through dissolve/mod/filter): "Modified (LED lit)"
controls:
  - { name: "Mix", type: switch, value: "Modified", options: ["Standard", "Modified"] }
  - { name: "Mix", type: knob, value: "1:00" }
  - { name: "Dissolve", type: knob, value: "2:00" }
  - { name: "Smear", type: knob, value: "1:00" }
  - { name: "Chance", type: knob, value: "12:00" }
  - { name: "Glitch", type: knob, value: "11:00" }
  - { name: "Time", type: knob, value: "1:00" }
  - { name: "Filter", type: knob, value: "12:00" }
  - { name: "Filter", type: switch, value: "LP", options: ["LP", "HP"] }
  - { name: "Shape", type: switch, value: "Sine", options: ["Sine", "Square", "Rev Saw", "Saw", "Random Sine", "Random Square", "Envelope"] }
  - { name: "Mod", type: switch, value: "Tremolo", options: ["Tremolo", "Vibrato"] }
  - { name: "Depth", type: knob, value: "8:00" }
  - { name: "Routing", type: switch, value: "Stereo", options: ["Mono", "Stereo-sum", "Stereo"] }
  - { name: "Trails", type: switch, value: "On", options: ["On", "Off"] }
  - { name: "Slot", type: knob, value: "live mode / MIDI slot" }
---

# Pure Reverse Dry (Modified Mix)

## Concept
Uses Parting's UNIQUE **Modified Mix** mode to send the DRY signal through reverse too — so the entire tone (not just a wet layer) plays backwards. A pure shoegaze/art-rock reverse swell with no clean signal poking through. This is the strongest use of the feature Emily Hopkins calls Parting's defining versatility move. In Modified mode the Filter touches the dry too, which is the intent here: it darkens the whole reversed wall.

## How to play it
1. Set global defaults: Routing Stereo, Trails ON.
2. Flip the Mix toggle to **Modified** (LED lit) so dry AND wet both pass through dissolve/mod/filter.
3. Set the Mix knob to 1:00 to favor the processed reverse.
4. Dissolve at 2:00 (reverse); Smear at 1:00 to bloom into reverb; Chance noon (constant), Glitch 11:00 (fixed).
5. Filter LP at noon darkens the whole reversed wall — accept that crush and filter now affect the dry too; that's deliberate.

## Notes
- 🟣 DESIGNED — never found. ⭐ Whole-signal reverse is a quintessential shoegaze/art-rock move.
- Accept that Filter + crush now affect the dry too — that is the point of Modified Mix here.
- Clocks are DOUG's tuning of a documented feature.
- Reference: making aesthetic (recorded-wrong / sustained walls); art-rock cluster 1 reverse signature; shoegaze lean.
- Save target: live mode / MIDI slot.

## Sources
- 🟣 designed from `research/transcripts/harp-lady-emily-hopkins-official-parting.md` (Modified Mix = mod/bit-crush/reverse applied to your DRY signal — "pure tremolo / pure bit-crush / pure reverse of your tone")
- `research/transcripts/harp-lady-pedals-that-inspired-parting.md` (two mix modes = unique to Parting)
- DeepResearch §2, §5.
- Transformed from Pedalxly Parting-Patches.md (designed)
