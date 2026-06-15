---
type: patch
title: "Busy Bee — Stretcher relaxes a busy loop"
device: Chase Bliss Blooper
date: 2026-06-15
description: "Record a very busy loop, then use Stretcher (the alt-bank, pitch-independent stretch) to slow and relax it — redefining the relationships of the sounds within without dropping the pitch, opening up 'the whole universe of sound between the notes.' Factory cheat-sheet recipe (Stretcher card · 'Busy Bee')."
tags: [stretcher, ambient, texture, time-stretch, factory]
dips:
  BANK B: "on — engages the alt-bank Stretcher (or load Stretcher via BLIP instead)"
controls:
  - { name: "Mode", type: switch, value: "NORM to audition, ADD to commit", options: ["NORM", "ADD", "SAMP"] }
  - { name: "MOD B slot", type: switch, value: "B4 Stretcher (ALT bank — requires BANK B dip, or load via BLIP)", options: ["B4", "B5", "B6"] }
  - { name: "MOD B", type: knob, value: "CCW from noon to slow the loop (up to 4x slower, pitch unchanged) — no published clock positions" }
  - { name: "MOD B engage", type: button, value: "arcade button — engage Stretcher" }
  - { name: "Slot/Bank", type: knob, value: "MOD B4 ALT bank (BANK B dip or BLIP load) — dialable recipe, no published values" }
---

# Busy Bee — Stretcher relaxes a busy loop

## Concept

Record a deliberately busy, dense loop, then reach for Stretcher — the alt-bank, pitch-independent stretch added in v3.0. Turning the knob counterclockwise from noon slows the loop down (up to 4x slower) while the pitch stays put, so it relaxes rather than detunes. The slowed timing redefines the relationships between the sounds within the loop, opening up "the whole universe of sound between the notes."

## How to play it

1. Record a deliberately busy, dense loop.
2. Engage BANK B and set MOD B to Stretcher (B4), or load Stretcher via BLIP.
3. Turn the knob counterclockwise from noon to slow the loop down (up to 4x slower) — pitch stays put, so it relaxes rather than detunes.
4. Notice how the slowed timing redefines the relationships between the sounds; layer fresh playing over the relaxed bed.
5. Audition in NORM, then switch to ADD to commit the stretched bed.

## Notes

- Stretcher decouples time from pitch (v3.0 feature) — CCW slows up to 4x without dropping the pitch.
- DSP-heavy: mutually exclusive with Pitcher and the Speed modifiers (except reverse). Plan one per loop.
- Pair with Filter to tame the ring-mod artifacts Stretcher can introduce.
- Requires the BANK B dip (or a BLIP load) to reach Stretcher in the alt bank.
- Honesty flag: exact knob clock positions are not published — knob travel beyond "4x slower" dials from this recipe, set by ear.

## Sources

- `research/links/chasebliss-blooper-modifier-cheat-sheet.md` (STRETCHER · BUSY BEE + TIP, verbatim)
- `research/transcripts/chase-bliss-blooper-firmware-3-tutorial.md` (Stretcher CCW slows, pitch unchanged)
- Official CB modifier cheat-sheet PDF + Blooper manual (Stretcher description — 4x range)
- Transformed from Pedalxly Blooper-Patches.md (factory)
