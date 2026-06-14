---
type: patch
title: Momentary-record a reverb sliver
device: Chase Bliss Blooper
date: 2026-06-14
description: Grab a split-second sliver of a sustained reverb pad and trigger it — hold LEFT for momentary record in SAMP; Andy Othling's Dark Star freeze move.
tags: [technique, sampler, samp-mode, reverb, artist, signature]
controls:
  - { name: "Mode", type: switch, value: "SAMP", options: ["NORM", "ADD", "SAMP"] }
  - { name: "LEFT footswitch", type: button, value: "HOLD = momentary record (records only while held; release to stop) — but tapping LEFT wipes the loop" }
  - { name: "RIGHT footswitch", type: button, value: "trigger; hold RIGHT toggles loop vs one-shot" }
  - { name: "Slot/Bank", type: knob, value: "SAMP-mode footswitches · park grabbed sliver in a free MIDI PC slot" }
---

# Momentary-record a reverb sliver

## Concept

Grab a split-second sliver of a sustained reverb pad and trigger it. In SAMP, holding the LEFT footswitch records only while held, so you can freeze a reverb pad (Andy uses an Old Blood Noise Dark Star) and momentary-record just a sliver to retrigger.

## How to play it

1. In SAMP mode, freeze a sustained reverb pad upstream.
2. HOLD the LEFT footswitch for momentary record — it records only while held; release to stop.
3. Trigger with the RIGHT footswitch; hold RIGHT to toggle loop vs one-shot.

## Notes

- WARNING: tapping LEFT in SAMP wipes the loop — only HOLD it.
- Capture stereo-dependent reverb tails before Blooper, since SAMP plays back mono — let the Chroma Console / H90 re-spread.

## Sources

- `research/transcripts/andy-othling-office-hours-blooper.md`
- `research/transcripts/knobs-better-bloops-sampler-mode.md`
- Ref: Andy Othling (Lowercase Noises)
- Transformed from Pedalxly Blooper-Patches.md (factory/artist)
