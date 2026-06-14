---
type: patch
title: Dip-Stuck Recovery Ladder
device: Chase Bliss Onward
date: 2026-06-14
description: Recover a preset that feels "dead" / silent / won't trigger because a dip or a power-up gesture got silently saved into it.
tags: [troubleshooting, recovery, dips, factory-reset, community]
dips:
  ALL: off (step 2 of recovery)
hidden:
  SENSITIVITY (on SIZE): ~noon (so it actually triggers)
controls:
  - { name: "PRESETS toggle", type: switch, value: "middle (live knobs)", options: ["Left", "Middle/Live", "Right"] }
  - { name: "Factory reset", type: button, value: "CC56 via MIDI, or flip PRESETS left-and-back-to-center 3× until lights blink, then press both footswitches" }
  - { name: "Slot/Bank", type: knob, value: "n/a (recovery procedure)" }
---

# Dip-Stuck Recovery Ladder

## Concept
Recovering a preset that feels "dead" / silent / won't trigger because a dip (MANUAL / DUCK / SIDECHAIN / MISO / ½ SPEED) or a power-up gesture (Dry Kill) got silently saved into it. Because dips and hidden-option values save *into* the preset, a weird preset can silently carry a problem state into the next song.

## How to play it
1. Move the **PRESETS toggle to middle** (live knobs).
2. Turn **ALL dips OFF.**
3. Check hidden **SENSITIVITY (on SIZE) ~noon** so it actually triggers.
4. If still wrong, **factory reset** — **CC56** via MIDI, or the onboard gesture: flip PRESETS left-and-back-to-center 3× until the lights blink, then press both footswitches — and rebuild the preset.

## Notes
- Reset gesture is manual / Aaron-Rusch verified.
- The ML10X case (a stuck Dry-Kill-like state in a loop switcher) was fixed by factory reset.
- "Turn all dips off" is community folk-wisdom, not a single attributable quote.

## Sources
- `research/links/onward-troubleshooting-dips-off.md`; `morningstar-onward-ml10x-gotcha.md`; `research/transcripts/aaron-rusch-onward-hidden-options.md`; UsageGuide §7
- Ref: CB support folk-wisdom + Morningstar ML10X owner thread
- Transformed from Pedalxly Onward-Patches.md (community)
