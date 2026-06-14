---
type: patch
title: Reliable LFO Start-Phase Lock + P-lock-All-Active-Trigs
device: Elektron Digitakt 2
date: 2026-06-14
description: A free-running drone LFO that still re-phases cleanly at bar 1, plus dialing a param across a whole pattern in one move.
tags: [workflow, lfo, p-lock, drone, community]
controls:
  - { name: "Start-phase lock (method 1)", type: switch, value: "LFO MODE = FREE; trigless/yellow trig at step 1, condition 1ST, LFO.T enabled; p-lock MODE = TRG + SPH (start phase) on that step" }
  - { name: "Start-phase lock (method 3)", type: switch, value: "All trigs FREE; p-lock LFO MODE = SYNC on the first real trig" }
  - { name: "Re-phase limitation", type: switch, value: "Can fail on a LIVE pattern switch → use a pattern CHAIN so the change lands on a bar boundary" }
  - { name: "P-lock-all (OS 1.10+)", type: switch, value: "Hold a trig + press TRACK → adds/removes a param lock across ALL active trigs at once (push encoder to remove); per-page with hold + PAGE" }
---

# Reliable LFO Start-Phase Lock + P-lock-All-Active-Trigs

## Concept
Two workflow moves. First, make a free-running drone LFO re-phase cleanly at bar 1: either drop a 1ST-condition trig at step 1 with `LFO.T` and a `MODE = TRG` + `SPH` p-lock, or keep all trigs FREE and p-lock `MODE = SYNC` on the first real trig. Second, p-lock-all (OS 1.10+) dials a parameter across every active trig in one move — a major time-saver for a whole drone pattern.

## How to play it
1. Start-phase lock (method 1): default LFO `MODE = FREE`; drop a trigless/yellow trig at step 1, trig condition `1ST`, `LFO.T` enabled on it; p-lock `MODE = TRG` + `SPH` (start phase) on that step.
2. (method 3): all trigs FREE, p-lock LFO `MODE = SYNC` on the first real trig.
3. Limitation: re-phase can fail on a live pattern switch → use a pattern chain so the change lands on a bar boundary.
4. P-lock-all (OS 1.10+): hold a trig + press `TRACK` → adds/removes a param lock across all active trigs at once (push the encoder to remove); per-page with hold + `PAGE`.

## Notes
- `SPH` = LFO Start Phase; `LFO.T` = LFO-trig flag on the TRIG page. Start-phase technique is OG-era, transfers.
- P-lock-all is a major time-saver for dialing a whole drone pattern. Applies to any pattern.

## Sources
- `research/links/elektronauts-reliably-lock-lfo-start-point.md` (t/162628 — Lauli, Humanprogram)
- `research/transcripts/davemech-dt2-os110-deep-dive.md`
- Transformed from Pedalxly Digitakt-2-Patches.md (community)
