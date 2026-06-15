---
type: patch
title: "Vibrodrops — Stopper as manual tremolo/vibrato"
device: Chase Bliss Blooper
date: 2026-06-15
description: "Rapidly toggling Stopper on/off turns the modifier into a manual tremolo or melting vibrato: the tape-stop side (CCW of noon) toggled fast gives vibrato, the fade-out side (CW of noon) gives tremolo. Print these performance gestures straight into the loop in ADD. Factory cheat-sheet recipe (Stopper card, 'Vibrodrops')."
tags: [stopper, tremolo, vibrato, performance, factory]
dips:
  BANK B: "ON = engages the alt-bank Stopper on MOD B (or load Stopper via BLIP instead) — physical-only setup"
controls:
  - { name: "Mode", type: switch, value: "ADD (Blooper records while Stopper is toggled, printing the gesture into the loop)", options: ["NORM", "ADD", "SAMP"] }
  - { name: "MOD B", type: knob, value: "CCW of noon (tape-stop side) = vibrato · CW of noon (fade-out side) = tremolo" }
  - { name: "MOD B slot", type: switch, value: "B5 Stopper (ALT bank — requires BANK B dip; or load via BLIP)", options: ["B4", "B5", "B6"] }
  - { name: "MOD B engage", type: button, value: "arcade button — rapidly toggle (momentary hold, or quick-press latch)" }
  - { name: "Slot/Bank", type: knob, value: "MOD B5 alt bank (BANK B dip or BLIP) · dial other knobs from recipe (no published values)" }
---

# Vibrodrops — Stopper as manual tremolo/vibrato

## Concept

Rapidly toggling Stopper on/off turns the modifier into a unique manual tremolo or melting vibrato. The tape-stop side of the knob, toggled fast, gives vibrato; the fade-out side, toggled fast, gives tremolo. Record these performance gestures into the loop in ADD so the manual modulation becomes part of the sound rather than a one-time pass.

## How to play it

1. Engage the BANK B dip and set MOD B to Stopper (slot B5), or load Stopper via BLIP.
2. For vibrato, park the knob on the tape-stop (CCW of noon) side; for tremolo, the fade-out (CW of noon) side.
3. Rapidly toggle Stopper on/off in time with the loop.
4. Record in ADD to print the manual tremolo/vibrato gesture into the loop.

## Notes

- Tape-stop side toggled fast = vibrato; fade-out side toggled fast = tremolo (firmware-3 tutorial).
- The modifier buttons can be momentary (hold) or latching (quick press) — manual; turn the modifier off any time to interrupt and reverse the gesture.
- Stopper can self-oscillate in ADD — watch your levels.
- Requires the BANK B dip (or a BLIP load) to put Stopper on MOD B — physical-only setup. The knob side is documented; exact depth dials from recipe — no published values for the other knobs.

## Sources

- `research/links/chasebliss-blooper-modifier-cheat-sheet.md` (STOPPER · VIBRODROPS + TIP, verbatim)
- `research/transcripts/chase-bliss-blooper-firmware-3-tutorial.md` (toggling tape-stop = vibrato, fade = tremolo)
- official CB modifier cheat-sheet PDF + Blooper manual (modifier button momentary/latch)
