---
type: patch
title: Chorus → Reverb Send (shimmery modulated bed) + the mono gotcha
device: Elektron Digitakt 2
date: 2026-06-14
description: Shimmery, modulated reverb tails (chorused reverb) on an ambient bed — with the mono-collapse gotcha and the parallel-not-serial workaround.
tags: [ambient, chorus, reverb, send-fx, community, signature]
controls:
  - { name: "Track send", type: switch, value: "Send the track to CHORUS (not the Reverb send)" }
  - { name: "Chorus REVERB SEND", type: knob, value: "turn up (within the chorus's settings) → just the chorused reverb tail" }
  - { name: "Chorus output", type: knob, value: "pull down if you don't want to hear the chorus itself" }
  - { name: "Stereo workaround", type: switch, value: "Run CHORUS + REVERB in PARALLEL (both sends up on the track), not chorus-into-reverb" }
---

# Chorus → Reverb Send (shimmery modulated bed) + the mono gotcha

## Concept
Shimmery, modulated reverb tails: instead of using the Reverb send, send the track to CHORUS and turn up the chorus's own REVERB SEND, so you hear just the chorused reverb tail. The gotcha is that the chorus is collapsed to mono before hitting reverb ("flange-y, phase-y," high-end rolloff). For a stereo ambient bed, run chorus and reverb in parallel instead.

## How to play it
1. Instead of using the Reverb send, send the track to CHORUS, and within the chorus's settings turn up its REVERB SEND (pull chorus output down if you don't want to hear the chorus itself) → just the chorused reverb tail.
2. Gotcha: the chorus is collapsed to MONO before hitting reverb ("flange-y, phase-y," high-end rolloff).
3. For a stereo ambient bed, run chorus + reverb in PARALLEL (both sends up on the track), not chorus-into-reverb — or resample the wet result.

## Notes
- No numeric knob values are posted for this one — the parallel-not-serial workaround is the practical takeaway.
- FX params can be global or per-pattern; the parallel version on a wide bed.

## Sources
- `research/links/elektronauts-dt2-send-fx-chorus-reverb.md` (t/217570)
- Transformed from Pedalxly Digitakt-2-Patches.md (community)
