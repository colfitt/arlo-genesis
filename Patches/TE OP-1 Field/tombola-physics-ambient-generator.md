---
type: patch
title: "Tombola — physics ambient generator"
device: TE OP-1 Field
date: 2026-06-15
description: "The Tombola is a physics hexagon sequencer where note-balls bounce inside a rotating shape. Open the walls so notes escape on hits and let the rotation speed generate ever-shifting ambient melodies — optionally over a chopped-vocal + Phone bed for a degraded, self-evolving texture. Tombola behavior (blue = rotation, grey = opens the walls) is documented (MusicRadar); the held-sequence overlay trick is from community recipes (op1tips, op-forums Heyes); pad/FX settings are to-taste."
tags: [generative, tombola, ambient, sequencer, wash, phone]
dips:
  HOLD_OVERLAY: "hold [Shift] while the sequencer plays to stop new notes dropping in, so you can play a melody live over the generative pattern"
controls:
  - { name: "Sequencer", type: switch, value: "Tombola", options: ["Pattern","Tombola","Endless","Finger","Sketch","Arpeggio","Hold"] }
  - { name: "Tombola BLUE (hexagon rotation speed)", type: knob, value: "slow rotation for a drifting ambient flow — to-taste" }
  - { name: "Tombola GREY/white (open the walls)", type: knob, value: "open so note-balls escape as they hit a gap (the key to taming randomness)" }
  - { name: "[Shift]+Blue (hand-crank)", type: button, value: "manual hexagon rotation" }
  - { name: "Engine", type: switch, value: "long-attack/long-release pad (Cluster/Dimension) — or a chopped vocal sample for the degraded version", options: ["Dr Wave","Cluster","Phase","Digital","Voltage","FM","String","Face","iter","Synth Sampler","Sampler"] }
  - { name: "FX", type: switch, value: "Mother reverb — or Phone + a soft Element LFO for the degraded vocal bed" }
---

# Tombola — physics ambient generator

## Concept

The Tombola is a physics hexagon sequencer where note-balls bounce inside a rotating shape. Open the walls so notes escape on hits and let the rotation speed generate ever-shifting ambient melodies — a self-evolving pattern you set in motion rather than program. Run it under a long-attack pad (Cluster/Dimension) into Mother reverb for a clean wash, or swap the pad for a chopped vocal sample through Phone, lightly modulated by a soft Element LFO, for a degraded, self-evolving texture. Opening the walls is what turns pure randomness into musical phrases.

## How to play it

1. Load a **long-attack pad** (Cluster/Dimension) — or a **chopped vocal sample** for the degraded version.
2. `[Shift]+[Sequencer]` → **Tombola**; drop in a few note-balls.
3. Set **BLUE** for a slow rotation.
4. **Open the walls** (GREY) so notes escape on hits for a more melodic flow.
5. Add **Mother reverb** (or **Phone + soft Element LFO** for the vocal bed); hold **[Shift]** to overlay live notes over the held pattern.

## Notes

- **Opening the walls is the key** to taming pure randomness into musical phrases — closed walls trap the balls and the output stays chaotic.
- **Values are a dialable recipe, not sourced settings** — the Tombola control behavior (blue = rotation, grey = opens the walls) and the held-sequence overlay are published, but the pad/FX knob positions are not; treat the engine/FX block as a starting recipe and dial to taste.
- Distinct from the Andreas Roman *Tombola-on-FM-bells* patch: this is the generative-ambient build (pad or chopped-vocal + Phone bed), not the bell performance.

## Sources

- musicradar.com/news/8-things-op-1-field (Tombola: blue = rotation, grey = opens the walls)
- github.com/ratbag98/op1tips (hold Shift to play over the held sequence)
- Gear/TE OP-1 Field/research/links/op-forums-op1-field-workflows-tips.md (§Tombola ambient texture — Heyes)
- Gear/TE OP-1 Field/research/transcripts/digiphex-op1-field-sequencers-tutorial.md (§TOMBOLA)
