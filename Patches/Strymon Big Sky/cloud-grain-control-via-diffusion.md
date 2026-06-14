---
type: patch
title: Cloud grain control via Diffusion (banjo-flattering)
device: Strymon Big Sky
date: 2026-06-14
description: Controlling Cloud's grain — low Diffusion flatters banjo transients, high Diffusion smooths to a pad; run zero-dry as an organic synth-pad substitute (community).
tags: [cloud, grain, diffusion, banjo-as-lead, zero-dry, pad, community, signature]
hidden:
  Diffusion: LOW = grainier (rides the banjo pluck attack) / HIGH = smooth pad
controls:
  - { name: "Machine", type: switch, value: "CLOUD", options: ["Cloud","Shimmer","Bloom","Chorale","Swell","Magneto","Nonlinear","Reflections","Room","Hall","Plate","Spring"] }
  - { name: "PARAM1", type: knob, value: "Low End" }
  - { name: "PARAM2", type: knob, value: "Diffusion (smoothness control)" }
  - { name: "DECAY", type: knob, value: "up to ~50 s" }
  - { name: "MIX", type: knob, value: "full wet (zero dry)" }
  - { name: "Slot/Bank", type: knob, value: "08A" }
---

# Cloud grain control via Diffusion (banjo-flattering)

## Concept
Diffusion is Cloud's smoothness control. Low Diffusion is grainier — the grain rides the banjo pluck attack instead of smearing it — while high Diffusion smooths the wash into a pad. Run zero-dry (Mix full wet) and Cloud becomes an organic synth-pad substitute. Directly supports banjo-as-lead-into-Cloud and the zero-dry-pad move.

## How to play it
1. Set Diffusion LOW to keep grain on the banjo transients, or HIGH for a smooth pad.
2. Push DECAY up to ~50 s for a sustained wash.
3. Run zero-dry to turn the source into a pad.

## Notes
- PARAM1 = Low End, PARAM2 = Diffusion.
- Recurring forum line: "cheap synth/keyboard → Big Sky on Shimmer + Cloud = godly" — the VG-800-into-Cloud path.
- Exposes more hands-on Cloud control than the later Cloudburst pedal.

## Sources
- research/links/community-magneto-cloud-drone-techniques.md
- Transformed from Pedalxly Big-Sky-Patches.md (community)
