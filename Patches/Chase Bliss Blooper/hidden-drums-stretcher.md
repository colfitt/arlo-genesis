---
type: patch
title: "Hidden Drums — Stretcher condenses a loop to percussion"
device: Chase Bliss Blooper
date: 2026-06-15
description: "Condensing a loop with Stretcher (clockwise from noon) emphasizes its percussive aspects, letting you audition any loop as a drum pattern — the 'hidden drums' inside a sustained source. Pitch stays unchanged; all the way clockwise heads into pseudo ring-mod territory. Factory cheat-sheet recipe (Stretcher card · 'Hidden Drums')."
tags: [stretcher, rhythm, percussion, sound-design, factory]
dips:
  BANK B: "ON = engages the alt-bank Stretcher on MOD B (or load Stretcher via BLIP instead) — physical-only setup"
controls:
  - { name: "Mode", type: switch, value: "NORM to audition the condensed loop, ADD to commit the drum-like figure", options: ["NORM", "ADD", "SAMP"] }
  - { name: "MOD B", type: knob, value: "CW from noon to condense (up to 4x faster, pitch unchanged) · full CW = ring-mod-ish · dial by ear, no published value" }
  - { name: "MOD B slot", type: switch, value: "B4 Stretcher (ALT bank — requires BANK B dip; or load via BLIP)", options: ["B4", "B5", "B6"] }
  - { name: "MOD B engage", type: button, value: "arcade button" }
  - { name: "Slot/Bank", type: knob, value: "MOD B4 alt bank (BANK B dip or BLIP) · DSP-heavy, exclusive with Pitcher/Speed mods · dial other knobs from recipe (no published values)" }
---

# Hidden Drums — Stretcher condenses a loop to percussion

## Concept

Condensing a loop with the Stretcher (rotating clockwise from noon) emphasizes its percussive aspects, so you can audition any loop as a drum pattern — the "hidden drums" inside a sustained source. The condense is pitch-independent (up to 4x faster with pitch unchanged), and all the way clockwise heads into pseudo ring-mod territory.

## How to play it

1. Engage the BANK B dip and set MOD B to Stretcher (slot B4), or load Stretcher via BLIP.
2. Turn the MOD B knob clockwise from noon to condense the loop (up to 4x faster) — percussive content jumps forward.
3. Audition the condensed loop as a drum pattern; ease back from full CW to avoid ring-mod artifacts (or lean in for them).
4. Commit in ADD if you want to keep the drum-like figure.

## Notes

- Favorite KNOBs combo (firmware-3 tutorial): speed up a loop and add Stutter.
- Full clockwise enters pseudo ring-mod territory — pair with Filter to chill it out; pitch stays unchanged throughout.
- DSP-heavy: exclusive with Pitcher and the Speed mods. Requires the BANK B dip (or a BLIP load) to put Stretcher on MOD B.
- The "condense / clockwise" direction and "up to 4x faster" range are sourced; knob travel beyond that dials from recipe — treat the remaining knobs as a dialable recipe to taste, no published values.

## Sources

- `research/links/chasebliss-blooper-modifier-cheat-sheet.md` (STRETCHER · HIDDEN DRUMS + TIP, verbatim)
- `research/transcripts/chase-bliss-blooper-firmware-3-tutorial.md` (Stretcher CW percussive, ring-mod)
- official CB modifier cheat-sheet PDF (Stretcher > 'HIDDEN DRUMS')
