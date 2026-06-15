---
type: patch
title: Mix-Bus Glue / Mastering Compression
device: Chase Bliss Clean
date: 2026-06-15
description: "Clean as a stereo mix-bus / mastering compressor at the very end of the chain — full-stereo I/O, line level, very low noise, riding the noon-to-3:00 feedback-to-feedforward limiting blend (smooth/natural to snappy/aggressive) on the Dynamics knob. Chase Bliss's recommended two-preset 'glue' workflow, and Tape Op's / Devin Belanger's preferred end-of-chain use. Exact knob positions are not published — dial by ear and by the LED."
tags: [compression, limiting, bus, mastering, stereo, glue, artist]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: "off (optional ON for stereo animation across the mix)"
  MISO: off
controls:
  - { name: "Dynamics", type: knob, value: "gentle comp range below the limiting/sag zones for glue; push toward noon-3:00 to ride the feedback->feedforward blend (smooth -> snappy)" }
  - { name: "Sensitivity", type: knob, value: "by the left LED so the comp only catches peaks (LED flickers on loud bits)" }
  - { name: "Wet", type: knob, value: "to unity (full wet for tone-fattening per Devin)" }
  - { name: "Dry", type: knob, value: "blended in for parallel cohesion" }
  - { name: "Attack", type: knob, value: "slowish (preserve transients)" }
  - { name: "EQ", type: knob, value: "noon (off)" }
  - { name: "Release", type: switch, value: "R (Slow 1.5s) or Mid (User) for whole-mix glue", options: ["L Fast 50ms", "Mid User 650ms", "R Slow 1.5s"] }
  - { name: "Mode", type: switch, value: "Mid (Manual)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "Physics", type: switch, value: "Mid (stable)", options: ["L subtle wobble", "Mid stable", "R twitchy"] }
---

# Mix-Bus Glue / Mastering Compression

## Concept
Clean placed across the stereo bus at the very end of the chain as a "glue" mix-bus / mastering compressor: full-stereo I/O, happy with line level, very low noise. The defining move is riding the feedback-to-feedforward limiting blend on a single knob — smooth/natural toward noon, snappy/aggressive toward 3:00. Set a gentle ratio with a slow release for whole-mix glue, or go full-wet to fatten and thicken the whole bus. This is Chase Bliss's recommended "glue" preset and Tape Op's / Devin Belanger's preferred end-of-chain use.

## How to play it
1. Place Clean end-of-chain across the stereo bus (or on a stem / master in the studio).
2. Set Sensitivity by the left LED so the comp acts only on peaks (LED flickers on the loud bits).
3. Set Dynamics in the gentle comp range, or push toward noon–3:00 to ride the feedback-to-feedforward limiting blend (smooth -> snappy).
4. Set Release SLOW (toggle R) or MIDDLE for whole-mix glue; slow the Attack to keep transients.
5. Blend Dry for parallel cohesion; bring Wet up for level / fattening (go full-wet for maximum thickening per Devin). Save to a preset slot per Chase Bliss's two-preset workflow.

## Notes
- Chase Bliss's documented two-preset workflow: an up-front enhancer in one slot, an end-of-chain glue setting in the other.
- Tape Op's preferred use is exactly this end-of-chain stereo mix-bus role — "wants to be played like an instrument," not set-and-forget.
- **HONEST — dialable recipe, no published values:** the slow-release/glue and feedback-to-feedforward concept are sourced, but exact knob positions are not published. Dial by ear and by the LED.
- **HONEST limitation:** Clean's variable release does not go as fast as a dedicated comp (Devin), so a super-slow-attack / super-fast-release mastering style is harder here.
- **Requires redeploying Clean to a stereo end slot in this rig** (it lives mono at the front).

## Sources
- `research/transcripts/devin-belanger-clean-most-useful-pedal.md` (mix-bus compression, full-wet fattening; honest release-speed limit vs Polyend Press)
- `research/links/daily-clean-stereo-spread-miso-and-chain-placement.md` (Tape Op: end-of-chain stereo mix-bus comp; feedback->feedforward blend as stereo glue)
- `research/transcripts/rhett-shull-clean-who-its-for-dusty-boost.md` (outboard-rack use: glue -> hard limiting on a whole mix)
- Chase Bliss Clean official manual (Overview p.3, two-preset "glue" workflow)
- tapeop.com/reviews/gear/165/clean-stereo-compressor-pedal
- Ref: Devin Belanger (stereo mix-bus glue) — provenance: manual workflow + review (Tape Op) + demo; dialable recipe, no published values
