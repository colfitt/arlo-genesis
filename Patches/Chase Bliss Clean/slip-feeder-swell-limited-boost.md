---
type: patch
title: Slip Feeder (Swell + Limited Boost)
device: Chase Bliss Clean
date: 2026-06-15
description: "DOUG-designed front-anchor for the Clean → MOOD Slip → QI chain — fuses Dynamic Swell, limiting, and Wet make-up boost so Slip's auto-sampler gets a swelled, dynamically-even, sustained, hot source whose semitone harmonies and reverse trails track cleanly. Mechanics sourced from the Clean manual + UsageGuide + BachelorMachines deep-dive; all clock-face values are a dialable recipe."
tags: [compression, swell, limiter, make-up-boost, sustain, slip-feeder, ambient, designed]
dips:
  Dusty: off
  Swell Aux: "ON (Dynamic Swell engaged on AUX)"
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: "off (momentary) — ON to make AUX a toggle"
  Spread: off
  MISO: off
hidden:
  Swell In time (Wet knob): "~noon (~100 ms-4 s) — slowish pad-like bloom"
  Swell Out time (Dry knob): "~noon (~100 ms-4 s) — graceful fall"
controls:
  - { name: "AUX footswitch", type: button, value: "Dynamic Swell (default momentary; flip LATCH for a toggle)" }
  - { name: "Sensitivity", type: knob, value: "set FIRST by ear to the LEFT red LED; re-set per instrument (recipe)" }
  - { name: "Dynamics", type: knob, value: "noon (limiting, ~4:1+, flat sustained ceiling under the swell) — recipe" }
  - { name: "Wet", type: knob, value: "past noon (make-up gain → drives MOOD hot) — recipe" }
  - { name: "Dry", type: knob, value: "OFF / low (so the swell reads cleanly) — recipe" }
  - { name: "Attack", type: knob, value: "10:00-11:00 (recipe)" }
  - { name: "EQ", type: knob, value: "noon (off — let MOOD color it)" }
  - { name: "Release", type: switch, value: "Mid (User 650 ms) — or R (Slow 1.5 s) for more sustain", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "Mid (stable)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
  - { name: "Slot/Bank", type: knob, value: "MIDI-recallable source-conditioner preset alongside the Slip scene" }
---

# Slip Feeder (Swell + Limited Boost)

## Concept
Purpose-built combination patch for the Clean → MOOD Slip → QI shimmer chain. Slip is a continuous auto-sampler that tracks best on a sustained, even-leveled source; a raw pluck (hard transient, fast decay) makes its semitone harmonies stutter and its reverse trails grab inconsistent chunks. This patch fixes that at the source: the AUX Dynamic Swell bows each note in from silence (removes the transient), the Dynamics knob pushed toward noon limits the swelled note to a flat sustained ceiling, and Wet make-up gain past noon drives MOOD hot. Together that is the "sustained consistent source so Slip's harmonies track." Deliberately distinct from the bare "Home Base" leveler (no swell) and the plain "Dynamic Volume Swell" (no limiting/boost emphasis) — it fuses all three jobs into one front-anchor voice.

## How to play it
1. **Set Sensitivity by ear to the LEFT red LED first**, at real playing volume; re-set it per instrument.
2. **Engage the AUX footswitch** (Dynamic Swell, default momentary; flip LATCH for a toggle) so notes bow in from silence.
3. **Push Dynamics toward noon (limiting)** so the swelled note hits a flat, sustained ceiling instead of a varying level — this is what lets Slip track.
4. **Bring Wet up past noon for make-up gain** so MOOD's input runs hot; keep Dry off/low so the swell reads cleanly.
5. **Hidden Options** (hold both footswitches until LEDs go green): Wet = Swell-In ~noon, Dry = Swell-Out ~noon for a pad-like swell.
6. Leave EQ at noon (off), Mode Mid (Manual), Physics Mid (stable); play held notes and confirm a soft pick bows in to a flat, sustained, hot level.

## Notes
- **Dialable recipe** — no published clock-face values; the swell + limiting + make-up-gain mechanics are sourced, the exact positions are set by ear (single-LED metering means no recallable detents).
- Deliberately **NOT** "Home Base" (leveler, no swell) and **NOT** "Dynamic Volume Swell" (swell only, no limiting/boost emphasis) — the whole point is fusing all three so Slip gets a single coherent sustained note.
- **HONEST:** the Wet/Dry boost is compressor make-up gain, not a pristine clean-boost circuit — plenty to drive MOOD hot, just not transparent.
- **Watch downstream level:** QI (last in chain) has no input-level switch and clips on hot sources, so size the Wet boost to drive MOOD, then trim if QI's grain input distorts.
- All CUSTOMIZE dips OFF except SWELL/LATCH as used (Dusty off, Motion off, Noise Gate off, Sidechain off, Spread off, MISO off).

## Sources
- Clean manual pp.30–31 Swell + Hidden Options pp.16–17 (Wet = Swell-In, Dry = Swell-Out, ~100 ms–4 s) — `research/links/cb-manual-clean-compression-recipes.md`
- `gear/Chase Bliss Clean/research/Clean-UsageGuide.md` (limiting + slow Release for a sustained wall; Wet/Dry boost = make-up gain; Sensitivity-by-LED; swell feeds downstream boards pre-swelled material)
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (limiting zone; Sag/swell on sustained sources makes swelling pads; ~noon swell = pad)
- Existing patches: `dynamic-volume-swell.md` (swell engine, feeds granular/loop boards), `home-base.md` (front-anchor leveler), `always-on-huge-fuzz-feeder.md` (hot limiting feeder) — this patch fuses their roles
- Ref/role: 🟣 DOUG-designed for the Clean → MOOD Slip → QI chain (source conditioner so Slip's semitone harmonies + reverse trails track)
