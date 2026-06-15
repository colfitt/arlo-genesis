---
type: patch
title: Feedforward Snappy Limiter / Brickwall
device: Chase Bliss Clean
date: 2026-06-15
description: "Push DYNAMICS from noon toward 3:00 to blend a single knob from feedback limiting (natural, smooth, relaxed) into feedforward limiting (precise, snappy, aggressive) — a rare control Tape Op flags as a standout — for a snappy, peak-catching brickwall that slams the next stage or hard-catches modeled-source transients. Manual + review-sourced (DYNAMICS noon = hard-limit is published); exact positions are by ear/LED."
tags: [limiting, feedforward, brickwall, transient-control, fuzz-feeder, factory]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: off
  MISO: off
controls:
  - { name: "Dynamics", type: knob, value: "noon -> 3:00 (noon = hard-limit / feedback infinity:1; toward 3:00 = feedforward, snappy/aggressive)" }
  - { name: "Sensitivity", type: knob, value: "sets the absolute ceiling / maximum loudness in this zone (set by LED)" }
  - { name: "Attack", type: knob, value: "FAST (CCW) for the snappiest peak-catch" }
  - { name: "Wet", type: knob, value: "output level — boost to compensate for limiting" }
  - { name: "Dry", type: knob, value: "DOWN for the pure limiter" }
  - { name: "EQ", type: knob, value: "noon (off), or cut lows to taste so bass doesn't over-trigger" }
  - { name: "Release", type: switch, value: "L (Fast)", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "Mid (stable)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
---

# Feedforward Snappy Limiter / Brickwall

## Concept
Set DYNAMICS to noon to enter hard limiting, where SENSITIVITY becomes the ceiling, then push toward 3:00 to blend from feedback limiting (natural, smooth, relaxed) into feedforward limiting (precise, snappy, aggressive) on a single knob — a rare control Tape Op flags as a standout. The aggressive feedforward end is the snappy, peak-catching brickwall for slamming the next stage or catching modeled-source transients hard.

## How to play it
1. Set Dynamics to noon (hard limiting, infinity:1 feedback) and set Sensitivity as the maximum loudness ceiling.
2. Sweep toward 3:00 to blend into feedforward limiting — snappier, more aggressive, faster peak-catch.
3. Use a fast Attack and fast Release (toggle L) for the snappiest brickwall; boost Wet to compensate.
4. Dry down for the pure limiter sound; Wet for output level.
5. Use end-of-chain on a full mix, or front-end to hard-catch modeled VG-800 / banjo transients before the dirt.

## Notes
- **HONEST:** DYNAMICS noon = hard-limit is published, and the feedback->feedforward blend plus "Sensitivity = ceiling past noon" are sourced — but the exact knob positions toward 3:00 are dialed by ear/LED, not published values. Treat the sweep as a dialable recipe.
- Single-knob feedback->feedforward blend is rare and flagged by both CB and Tape Op as a standout.
- Stage Two is an automatic hard limiter behind Stage One that catches anything that slips by.
- Distinct from the Always-On Fuzz Feeder (which targets even quiet-note saturation) and the Pseudo-Sidechain (which targets bus ducking).
- No look-ahead, so the very first instant of a transient can escape even here — normal.

## Sources
- `research/links/cb-manual-clean-compression-recipes.md` (Dynamics noon->3:00 blends feedback->feedforward: "Feedback - Natural, smooth, relaxed; Feedforward - Precise, snappy, aggressive"; Sensitivity sets the absolute ceiling)
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (noon = feedback limiter; toward 3:00 = feedforward, keys off the uncompressed signal, faster/more aggressive)
- `research/links/daily-clean-stereo-spread-miso-and-chain-placement.md` (Tape Op flags the feedback->feedforward blend as a standout)
- Ref: Chase Bliss Clean official manual (Dynamics — Limiting p.24-27; Stage Two auto hard limiter)
- Ref: compressorpedalreviews.com/post/chase-bliss-clean-compressor-review
