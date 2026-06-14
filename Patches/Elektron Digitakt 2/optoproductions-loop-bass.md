---
type: patch
title: Optoproductions Loop-Bass (one-note loop + per-bar pitch p-lock)
device: Elektron Digitakt 2
date: 2026-06-14
description: A fast melodic bassline from a single sampled note (e.g. a baritone / VG-800 note) without locking every step — p-lock only the pitch per bar, per Optoproductions.
tags: [bass, groove, p-lock, baritone, factory, artist]
controls:
  - { name: "Source", type: switch, value: "A one-note loop (e.g. sampled baritone / VG-800 note)" }
  - { name: "Pattern LENGTH", type: knob, value: "64, with one trig" }
  - { name: "Track LENGTH", type: knob, value: "16 (so it repeats per bar)" }
  - { name: "P-lock", type: switch, value: "PITCH only, per bar (faster than locking every note)" }
  - { name: "SRC (machine)", type: switch, value: "Oneshot → WERP (set segment length, tweak)", options: ["ONESHOT","GRID","SLICE","REPITCH","WERP","STRETCH"] }
  - { name: "Variation (optional)", type: switch, value: "p-lock sample START with a RANDOM value per step; LFO → pitch saw/exponential, trig-mode = trigger, for click" }
---

# Optoproductions Loop-Bass (one-note loop + per-bar pitch p-lock)

## Concept
A fast melodic bassline from a single sampled note, without locking every step. Record a one-note loop, run one trig over a 64-step pattern with a 16-step track length so it repeats per bar, and p-lock only the PITCH of that single note per bar — much faster than locking every note. Switch the SRC machine from Oneshot to Werp to set segment length. Maps directly onto a sampled baritone/banjo note as a melodic bass.

## How to play it
1. Record a one-note loop.
2. Pattern `LENGTH 64` with one trig, track `LENGTH 16` (so it repeats per bar).
3. P-lock only the PITCH of that single note per bar (much faster than locking every note).
4. Switch SRC machine Oneshot → Werp, set segment length, tweak.
5. (Also: p-lock sample `START` with a RANDOM value per step for variation; add LFO → pitch saw/exponential, trig-mode = trigger, for click.)

## Notes
- Maps directly onto a sampled baritone/banjo note as a melodic bass.
- One bass track; the note lives in one sample slot.

## Sources
- Ref: Optoproductions (Melvin) — "Digitakt 2 Sampling Tutorial" (yt `wi-DCA-uyO8`).
- `research/transcripts/optoproductions-dt2-sampling-tutorial.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (factory/artist)
