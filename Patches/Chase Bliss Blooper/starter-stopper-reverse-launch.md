---
type: patch
title: "Starter — Stopper run in reverse to begin a loop"
device: Chase Bliss Blooper
date: 2026-06-15
description: "Disengaging Stopper makes the effect happen in reverse — a 'Starter.' Tape-stop the loop to a halt, adjust the knob while it's stopped to set a different speed/effect on the way back, then release to ramp it to life. Because Blooper keeps recording while stopped, the start can be printed into the loop in ADD. Factory cheat-sheet recipe (Stopper card, 'Starter')."
tags: [stopper, tape-stop, transition, reverse, factory]
dips:
  BANK B: "ON = engages the alt-bank Stopper on MOD B (or load Stopper via BLIP instead) — physical-only setup"
controls:
  - { name: "Mode", type: switch, value: "ADD (Blooper keeps recording while stopped — print the start)", options: ["NORM", "ADD", "SAMP"] }
  - { name: "MOD B", type: knob, value: "CCW of noon = melting tape-stop (further = longer to stop) · CW of noon = gradual volume fade-out · after stopping, adjust to change the start behavior" }
  - { name: "MOD B slot", type: switch, value: "B5 Stopper (ALT bank — requires BANK B dip; or load via BLIP)", options: ["B4", "B5", "B6"] }
  - { name: "MOD B engage", type: button, value: "arcade button (latch to stop; disengage = reverse 'start')" }
  - { name: "Slot/Bank", type: knob, value: "MOD B5 alt bank (BANK B dip or BLIP) · dial other knobs from recipe (no published values)" }
---

# Starter — Stopper run in reverse to begin a loop

## Concept

Disengaging Stopper causes the effect to happen in reverse — a "Starter." Use a tape-stop to halt the loop, then release Stopper to ramp it back to life. Adjust the knob once stopped to give a different speed/effect on the start. Blooper keeps recording while stopped, so the start can be printed.

## How to play it

1. Engage the BANK B dip, set MOD B to Stopper (slot B5), and place the knob counter-clockwise of noon (tape-stop side) or clockwise (volume fade).
2. Engage Stopper to halt the loop — the further CCW, the slower the melting stop.
3. While stopped, adjust the knob to set a different start speed/effect.
4. Disengage to "start" the loop in reverse — and since Blooper keeps recording while stopped, the start can be baked into the loop in ADD.

## Notes

- Stopper's tape-stop side (CCW) is time-based (desyncs the heads); the fade-out side (CW) is non-time-based.
- Can self-oscillate / run away in ADD mode — ride VOLUME.
- Rapidly toggling Stopper on/off makes a manual tremolo / melting vibrato (see Vibrodrops).
- Requires the BANK B dip (or a BLIP load) to put Stopper on MOD B — physical-only setup.
- Exact knob positions beyond CCW/CW of noon dial from recipe — no published values for the other knobs.

## Sources

- `research/links/chasebliss-blooper-modifier-cheat-sheet.md` (STOPPER · STARTER + TIP, verbatim)
- `research/transcripts/chase-bliss-blooper-firmware-3-tutorial.md` (Stopper CCW = tape-stop, CW = fade, records while stopped)
- official CB modifier cheat-sheet PDF + Blooper manual (Stopper description)
