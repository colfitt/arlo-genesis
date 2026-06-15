---
type: patch
title: "Phone — granular broken-line / scratch FX"
device: TE OP-1 Field
date: 2026-06-15
description: "Phone chops the signal into tiny re-pitched grains — the closest the Field gets to a granular effect; push it for a degraded broken-telephone morph or rake it with a tremolo LFO for a moving lo-fi scratch. Community recipe — the Phonic/Baud/Telematic ~99/00/99 'doubling' combo is documented (op1tips/ratbag98); the tremolo rake is to-taste."
tags: [effect, phone, granular, glitch, lo-fi, degraded]
controls:
  - { name: "FX", type: switch, value: "Phone" }
  - { name: "Phonic (green encoder)", type: knob, value: "~99 (pull toward center for subtle grain detune)" }
  - { name: "Baud (white encoder)", type: knob, value: "~00" }
  - { name: "Telematic (red encoder)", type: knob, value: "~99 (pull toward center for subtle grain detune)" }
  - { name: "Tune", type: knob, value: "[Shift]+Blue to set pitch" }
  - { name: "LFO (for scratch/rake)", type: switch, value: "Tremolo (Value-type)", options: ["value","tremolo","random","element","t_scale"] }
  - { name: "Portamento (for scratch/rake)", type: knob, value: "add + play legato between notes" }
---

# Phone — granular broken-line / scratch FX

## Concept

Phone chops the signal into tiny grains and re-pitches them with varying repetition — the closest the Field gets to a granular effect (there is no dedicated granular engine). Push it for a degraded broken-telephone morph, or rake the frequencies with a tremolo LFO for a moving lo-fi scratch. Great on a chopped vocal or synth lead for a degraded-radio bed.

## How to play it

1. Open the master FX slot and select **Phone**.
2. For a broken-phone morph: **Phonic ~99, Baud ~00, Telematic ~99**; tune pitch via **[Shift]+Blue**.
3. For subtle granular detune, pull the extremes back toward center.
4. For a scratch/rake, add a **Tremolo (Value-type) LFO + portamento** and play legato between notes so grains shift as you move pitch.
5. Run a chopped vocal or synth lead through it for a degraded-radio bed.

## Notes

- Phone is the Field's de-facto granular effect — there is no dedicated granular engine.
- HONESTY: the **Phonic-99 / Baud-00 / Telematic-99 "doubling" combo is community-documented** (op1tips/ratbag98), not officially published — treat it as a dialable starting recipe, not exact factory values. The **tremolo rake is to-taste** (rate/depth not published).
- The encoder color labels (green/white/red) follow the OP-1 Field's blue/green/white/red knob convention; verify on-screen names as TE firmware can rename FX params.
- Pairs well on a chopped vocal for a degraded-radio texture (cf. Tombola + Phone bed).

## Sources

- Gear/TE OP-1 Field/research/links/github-ratbag98-op1tips-distilled.md (§FX recipes — Phone-FX scratch)
- Gear/TE OP-1 Field/research/OP-1-Field-UsageGuide.md §1 (Phone-FX scratch)
- github.com/ratbag98/op1tips (Phonic-99/Baud-00/Telematic-99, scratch/rake technique)
- magazinmehatronika.com/en/op-1-field-review/ (Phone = granular grain-chopping pitch effect)
