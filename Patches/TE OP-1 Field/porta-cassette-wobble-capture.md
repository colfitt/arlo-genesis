---
type: patch
title: "Porta tape — cassette wobble capture"
device: TE OP-1 Field
date: 2026-06-15
description: "Commit a take to the Porta (Tascam-style cassette) tape style for baked-in hiss and tape WOBBLE — the money mode for a 'recorded-wrong' drone/doom aesthetic. Character applies only at record time, so you record TO the Porta tape, then lift the wobbled audio onto a Studio reel to keep working (demo technique, ADG/loopop — method-level, no published values)."
tags: [tape-trick, cassette, degraded, lo-fi, drone, signature]
dips:
  ALT_TAPE: "Disc Mini (minidisc-ish, subtle artifacts, near-instant tape-stop)"
controls:
  - { name: "Tape style", type: switch, value: "PORTA (chrome tag) — set via [Shift]+[Tape]", options: ["Studio","Porta","Disc Mini","Vintage"] }
  - { name: "Record to tape", type: switch, value: "record any source to the Porta tape — hiss + wobble bake in", options: ["record","stop"] }
  - { name: "Noise preview", type: switch, value: "[Shift]+[Record]+[Stop] to hear the noise floor without recording" }
  - { name: "Lift", type: switch, value: "lift the wobbled audio off the Porta tape" }
  - { name: "Drop", type: switch, value: "drop the lifted audio onto a Studio reel — wobble persists" }
---

# Porta tape — cassette wobble capture

## Concept

Commit a take to the Porta (Tascam-style cassette) tape style for baked-in hiss and tape WOBBLE — the money mode for a "recorded-wrong" drone/doom aesthetic. The Porta character applies only at record time, so you must record TO the Porta tape; you can then lift the wobbled audio onto a Studio reel to keep working cleanly. A project commits to one tape style. Method-level — no published numeric values.

## How to play it

1. [Shift]+[Tape] → select the PORTA tape style (chrome).
2. Record your source to the Porta tape — hiss and wobble bake in.
3. Preview the noise floor first via [Shift]+[Record]+[Stop] if you want.
4. [Lift] the wobbled audio and [Drop] it onto a Studio reel to keep editing cleanly.
5. Each overdub stacks more noise — commit deliberately.

## Notes

- Documented tape behavior (ADG, loopop). Method-level — no published numeric values; treat the controls above as a dialable recipe, not sourced settings.
- Character is baked AT record time only — recording onto Studio then dropping to Porta stays CLEAN.
- Disc Mini is the alternative tape style: minidisc-ish, subtle artifacts, near-instant tape-stop.

## Sources

- Gear/TE OP-1 Field/research/transcripts/adg-op1-field-full-walkthrough-for-owners.md (§Tape styles; §baked in at record time)
- Gear/TE OP-1 Field/research/OP-1-Field-DeepResearch.md §3 (tape styles), §13b
- Gear/TE OP-1 Field/research/OP-1-Field-UsageGuide.md §1 (character baked in at record time)
