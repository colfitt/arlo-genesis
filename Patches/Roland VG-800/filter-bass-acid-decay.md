---
type: patch
title: "FILTER BASS Acid Decay — touch-responsive filter pluck"
device: Roland VG-800
date: 2026-06-15
description: FILTER BASS synth model voiced as a touch-responsive acid/funk bass pluck — the FILTER DECAY parameter drives the snappy filter-close that defines a plucky acid bass. Distinct from the FILTER BASS Doom Sub (sustained crush); this one is the bouncy, filter-enveloped pluck. Dialable recipe from manual-verified params.
tags: [bass, acid, filter-bass, electronic, synth, textural]
dips:
  OUTPUT SELECT: "LINE/PHONES"
  GK CALIBRATION: "low strings — lower SENS, higher DISTANCE for clean bass tracking"
controls:
  - { name: "Mode", type: switch, value: "BASS mode (separate 150-memory set)", options: ["GUITAR", "BASS"] }
  - { name: "INST TYPE", type: switch, value: "SYNTH" }
  - { name: "SYNTH TYPE", type: switch, value: "FILTER BASS" }
  - { name: "FILTER CUTOFF", type: knob, value: "dial for squelch (0–100; mid, ride open by ear)" }
  - { name: "FILTER RESO", type: knob, value: "raised for the acid squelch (0–100)" }
  - { name: "TOUCH SENS", type: knob, value: "up — filter opens on harder picking (0–100; keep up or DECAY won't respond)" }
  - { name: "FILTER DECAY", type: knob, value: "lower = faster filter close / plucky (0–100; needs TOUCH SENS not too low)" }
  - { name: "COLOR", type: knob, value: "set for low-range body/strength (0–100)" }
  - { name: "Slot/Bank", type: knob, value: "User Memory (BASS mode)" }
---

# FILTER BASS Acid Decay — touch-responsive filter pluck

## Concept

The FILTER BASS synth model voiced as a touch-responsive acid/funk bass pluck, using its `FILTER DECAY` parameter for the snappy filter-close that defines a plucky acid bass. Distinct from the existing doom-sub use — this is the bouncy, filter-enveloped pluck. `FILTER RESO` gives the acid squelch, `TOUCH SENS` makes the filter open with picking dynamics, and a low `FILTER DECAY` snaps the filter shut for the pluck. A dialable recipe — param names and ranges are manual-verified, exact factory values are not published.

## How to play it

1. Switch to BASS mode (a separate 150-memory set). Set `INST TYPE = SYNTH`, `SYNTH TYPE = FILTER BASS`.
2. Raise `FILTER RESO` for the acid squelch and `TOUCH SENS` so the filter opens on harder picking.
3. Lower `FILTER DECAY` for a fast, plucky filter close (keep `TOUCH SENS` up or `DECAY` won't respond).
4. Set `COLOR` for low-range body. Play staccato single notes for the bouncing acid pluck.

## Notes

- FILTER BASS params (`FILTER CUTOFF` / `FILTER RESO` / `TOUCH SENS` / `FILTER DECAY` / `COLOR`, all 0–100) are manual-verified; the manual notes `FILTER DECAY` needs `TOUCH SENS` not too low to be audible.
- Complements the existing FILTER BASS Doom Sub (sustained crush) and Around-the-World acid patches — this one focuses on the `FILTER DECAY` pluck mechanic.
- 🟡 Exact factory values are not published — dial from the ranges (recipe, not sourced numbers).

## Sources

- 🟢 FILTER BASS params (CUTOFF/RESO/TOUCH SENS/FILTER DECAY/COLOR ranges + behavior) from `research/links/parameter-guide-synth-engine-values.md`
- 🟡 dialable recipe from manual-verified params — no published values
