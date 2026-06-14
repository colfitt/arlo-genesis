---
type: patch
title: Classic-Mode Filter Box (HP/LP band-pass)
device: Chase Bliss Generation Loss
date: 2026-06-14
description: A usable resonant HP/LP band-pass sweep over anything — a utility filter you can Aux-footswitch or modulate; also fixes Classic mode's "no sound / sounds broken" first-engage state.
tags: [utility, filter, classic-mode, band-pass, factory]
dips:
  CLASSIC: on
controls:
  - { name: "Saturate", type: knob, value: "= GEN (full CW = clean/full-rate)" }
  - { name: "Failure", type: knob, value: "= HP (full CCW = low end open ≈20Hz)" }
  - { name: "Model", type: knob, value: "= LP (full CW = highs open ≈20kHz)" }
  - { name: "Wow", type: knob, value: "= LP cutoff too" }
---

# Classic-Mode Filter Box (HP/LP band-pass)

## Concept
A usable resonant HP/LP band-pass sweep over anything — a utility filter you can Aux-footswitch or modulate. In Classic mode the knobs change function to the gray alt labels. It also fixes Classic mode's "no sound / sounds broken" state on first engage (the filters are closed until you open them).

## How to play it
1. Set **CLASSIC dip = on** — the knobs now read the gray alt labels.
2. **Saturate = GEN** (full CW = clean/full-rate), **Failure = HP** (full CCW = low end open ≈20Hz), **Model = LP** (full CW = highs open ≈20kHz), **Wow = LP cutoff** too.
3. Open both filters wide, then **sweep HP up / LP down** to taste for the band-pass.

## Notes
- Not signature-fit — it's a clean filter utility — but documented and genuinely useful for sculpting a drone.
- If it "sounds broken" on first engage, the filters are just closed — open HP/LP up.

## Sources
- 🟢 `research/transcripts/kevwyxin-read-the-manual-part1-basics.md` + UsageGuide §1 + `research/transcripts/chasebliss-official-video-manual.md`.
- Transformed from Pedalxly Generation-Loss-Patches.md (factory/artist provenance).
