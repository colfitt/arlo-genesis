---
type: patch
title: Humanized Percussion + Hi-Hat Breather (HOLD/sine LFOs)
device: Elektron Digitakt 2
date: 2026-06-14
description: Stop repeated percussion / hi-hats from sounding machine-gunned — a small RANDOM HOLD LFO on envelope plus a SINE LFO on attack.
tags: [percussion, hi-hat, humanize, lfo, groove, community]
controls:
  - { name: "Humanize — LFO DEST", type: switch, value: "AMP DEC (or ATK)" }
  - { name: "Humanize — LFO WAVE", type: switch, value: "Random" }
  - { name: "Humanize — LFO MODE", type: switch, value: "HOLD (each note-on latches a slightly different envelope)", options: ["FREE","TRIG","HOLD","ONE","HALF"] }
  - { name: "Humanize — LFO DEP", type: knob, value: "0.10–4 (SMALL — high depth kills the hits)" }
  - { name: "Hi-hat breather — LFO DEST", type: switch, value: "AMP attack" }
  - { name: "Hi-hat breather — LFO WAVE", type: switch, value: "SINE (attack breathes → repeated hits get dynamics)" }
---

# Humanized Percussion + Hi-Hat Breather (HOLD/sine LFOs)

## Concept
The essential "make-it-not-robotic" move for drum tracks. A small RANDOM LFO in HOLD mode on the AMP decay (or attack) latches a slightly different envelope on each note-on, so repeated percussion stops sounding machine-gunned. A SINE LFO on the attack makes hi-hats breathe so repeated hits get dynamics. The key is keeping the depth low.

## How to play it
1. Humanize: `LFO DEST = AMP DEC` (or `ATK`); `WAVE = Random`; `MODE = HOLD`; `DEP = 0.10–4` (small — high depth kills the hits) — each note-on latches a slightly different envelope.
2. Hi-hat breather: `LFO DEST = AMP attack`; `WAVE = SINE` — the attack breathes so repeated hits get dynamics.

## Notes
- `DEP 0.10–4` is a quoted concrete range; the low value is the key.
- Works on drum tracks in any kit.

## Sources
- `research/links/elektronauts-underrated-lfo-settings-destinations.md` (t/241235 — Humanprogram, mistcollector)
- Transformed from Pedalxly Digitakt-2-Patches.md (community)
