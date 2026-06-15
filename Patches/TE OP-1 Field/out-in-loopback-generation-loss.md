---
type: patch
title: Out-in loopback — generation-loss resample
device: TE OP-1 Field
date: 2026-06-15
description: The canonical on-box degradation loop — record a source to tape, resample it back via OUT-IN loopback (or the EAR), re-record, repeat 2-3x to stack tape noise and generation loss for the "recorded-wrong" finish (demo technique, ADG + UsageGuide — method-level, no published values).
tags: [tape-trick, degraded, lo-fi, generation-loss, designed, signature]
controls:
  - { name: "Record source", type: switch, value: "Porta or Disc tape (Porta for baked-in warmth + wobble)", options: ["Tape (4-track)","Porta","Disc"] }
  - { name: "Sample source", type: switch, value: "OUT-IN loopback or EAR (NOT mic → avoids feedback)", options: ["mic","ear","line-in","OUT-IN loopback"] }
  - { name: "FADE", type: switch, value: "OFF (when sampling the row)" }
  - { name: "Re-record passes", type: knob, value: "2-3x (lift → drop into sampler → re-record)" }
  - { name: "UNDO", type: switch, value: "hold [Tape] + LEFT (7 levels — take risks while stacking)" }
  - { name: "Tape style", type: switch, value: "commits per project" }
---

# Out-in loopback — generation-loss resample

## Concept

The canonical on-box degradation loop. Record a source — banjo, baritone, synth pad — to a Porta or Disc tape, then resample it back into the box via OUT-IN loopback (or the EAR), re-record, and repeat 2-3x. Each pass stacks tape noise and generation loss for the "recorded-wrong" finish the studio's aesthetic is built on. New-tape UNDO (7 levels) lets you take risks while stacking. This is the active resample technique — distinct from the existing Cassette Ambient, which is a downloaded pre-degraded patch.

## How to play it

1. Record the source (banjo, baritone, synth pad) to a **Porta** tape — warmth + wobble baked in.
2. Set sample source to **OUT-IN loopback** or **EAR**; **FADE OFF**.
3. Lift the take, drop it into the synth/drum sampler, re-record to another track.
4. Repeat **2-3x** to stack generation loss.
5. Bounce to **Disc** tape; finish with the SP-303 master crush if desired.

## Notes

- Documented on-box resampling (ADG out-in loopback; UsageGuide generation-loss loop). Method-level — no published knob values; controls above are a dialable recipe, not sourced settings.
- Watch double-compression on each sample-in (master comp at record + comp on playback).
- Tape style commits per project, so decide before you start stacking.
- Distinct from the existing Cassette Ambient (a downloaded pre-degraded patch) — this is the active resample technique.

## Sources

- Gear/TE OP-1 Field/research/transcripts/adg-op1-field-full-walkthrough-for-owners.md (§Input menu — OUT-IN loopback)
- Gear/TE OP-1 Field/research/OP-1-Field-UsageGuide.md §5 (Generation-loss loop), §1 (UNDO)
- Gear/TE OP-1 Field/research/OP-1-Field-DeepResearch.md §6 (resampling on-box), §13b
