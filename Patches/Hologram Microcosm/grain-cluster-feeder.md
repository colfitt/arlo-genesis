---
type: patch
title: Grain Cluster Feeder
device: Hologram Microcosm
date: 2026-06-15
description: "A dryish granular GENERATOR purpose-built to feed a downstream granular delay (Big Time misbias CLUSTER) rather than be its own finished wash — Granules engine (Strum B onset-chains or Haze B many randomized grains), Mix kept well under wet so the grain field stays forward and dynamic. DOUG-designed dialable recipe; created for the Microcosm → Big Time Misbias Cluster Swirl chain because every existing Microcosm patch is a wash/halo bed that would double-granulate the CLUSTER engine."
tags: [granular, grains, feeder, grain-source, strum, haze, dynamic, cluster, designed, swirl]
controls:
  - { name: "Engine", type: switch, value: "GRANULES — STRUM variation B (onset chains overlap into phasing/cascading runs) or HAZE variation B (many simultaneous randomized grains)", options: ["Strum B — onset chains", "Haze B — many randomized grains"] }
  - { name: "Activity", type: knob, value: "HIGH (Activity = grain density/spread; this density is the texture handed forward)" }
  - { name: "Time", type: knob, value: "moderate / mid (Time = rate; fast Time = choppier grains — keep mid so grains have length, not infinite)" }
  - { name: "Repeats", type: knob, value: "moderate (feedback-like duration; enough overlap for a field, not a runaway)" }
  - { name: "Shape", type: switch, value: "slower envelope so grains carry body" }
  - { name: "Filter", type: knob, value: "~noon (tame granular top before two stages of diffusion)" }
  - { name: "Space", type: knob, value: "LOW (this is a source, not a wash)" }
  - { name: "Mix", type: knob, value: "~10:00–11:00 (well under wet — grain field stays forward; this knob + pick attack are the live trigger for the downstream misbias)" }
  - { name: "Reverse (press selector in)", type: button, value: "optional — engaged (CC 47) for a smeared backward grain feed" }
  - { name: "Output", type: switch, value: "mono out → Big Time IN-L (auto-MISO) so Big Time owns the stereo image; or stereo out for a busier, less-defined field" }
---

# Grain Cluster Feeder

## Concept
A dryish granular GENERATOR purpose-built to feed a downstream granular delay (Big Time CLUSTER) rather than act as its own finished wash. A grain engine in the Granules family (Strum B onset-chains or Haze B many-randomized-grains) spits a dense field of discrete pitched grains; Mix is kept well under wet so the grain field stays forward and dynamic, letting the next stage do the diffusion. The whole rig depends on this pedal making grains, not reverb — stacking two wet diffusers turns to porridge, so this one stays a source. Dynamics-reactive by design: back Mix/attack down and soft playing rides clean; dig in to push grain density that triggers the downstream misbias sag.

## How to play it
1. Confirm Global Config baseline (input mono/stereo, Line, Buffered+Trails as desired).
2. Select a GRANULES engine: STRUM variation B (onset chains) or HAZE variation B (many randomized grains).
3. Set Activity HIGH for dense grains; Time/Repeats moderate (fast Time = choppier; avoid infinite).
4. Set Shape to a slower envelope so grains have body; Filter ~noon to tame the top.
5. Keep Space LOW and Mix ~10:00–11:00 — this pedal is a grain GENERATOR, not a wash.
6. Optionally arm Reverse (press selector in / CC 47) for a backward smeared grain feed.
7. Run mono out → Big Time IN-L (auto-MISO) and let Big Time's CLUSTER/DIFFUSE be the only true wash.
8. Use Mix + pick attack as the live trigger: soft = clean grains, dig in = denser field that pushes the downstream misbias into sag/crumble.

## Notes
- DESIGNED recipe — knob values are dialable starting points, not sourced numbers; Hologram publishes engine behavior, not knob marks.
- Purpose: avoid granular-into-granular mud. Keep Mix/Space low so this is a SOURCE; the downstream granular delay does the diffusion. Stacking two wet diffusers = porridge.
- Control semantics (documented): Activity = grain density/spread; Time = rate (fast = choppy); Repeats = feedback-like duration; Shape = envelope; Mix/Space = blend.
- Microcosm grain engines generate genuine stereo, but feeding a downstream stereo-delay mono (IN-L / MISO) keeps the image clean.
- No feedback knob; oldest material self-fades — fine here since this is a live grain source, not a sustained loop.

## Sources
- `gear/Hologram Microcosm/research/Microcosm-UsageGuide.md` (Activity = grain density/spread; Granules = Haze/Strum; Time = rate, fast = choppy; Mix/Space = blend)
- `gear/Hologram Microcosm/research/Microcosm-DeepResearch.md` (per-engine control map; engines generate genuine stereo)
- Adapted granular-into-granular "don't double-granulate" caution from `Patches/Hologram Microcosm/haze-a-diffuse-smeared-wash.md` and `ambient-smear-wash-clock-face-starting-point.md`
- Built for chain `Chains/microcosm-big-time-misbias-cluster-swirl.md` feeding `Patches/Chase Bliss Big Time/cluster.md` (Factory #6 misbias CLUSTER)
- 🟣 DOUG-designed (dialable recipe). Engine choice and control semantics are documented Microcosm behavior; specific knob positions are designed starting points (not published numbers). Created because no existing Microcosm patch fills the dry dynamic grain-FEEDER role — all existing ones are wash/halo/smear beds (Space up, mostly-wet) that would double-granulate into the Big Time CLUSTER engine.
