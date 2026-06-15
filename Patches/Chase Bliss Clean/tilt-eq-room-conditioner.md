---
type: patch
title: "Tilt EQ — Room Conditioner"
device: Chase Bliss Clean
date: 2026-06-15
description: "Use Clean's single EQ knob in Manual mode as a fixed tilt/tone conditioner — CCW darkens (removes highs), CW brightens/tightens (removes lows), noon = off — to 'room-condition' a source or drum bus without touching the compression. Bass Fox / BachelorMachines + manual + ReviewRevival; tilt direction and usable sweep are published, the exact amount is dialable."
tags: [eq, tilt, tone-shaping, utility, static, community]
dips:
  Dusty: off
  Swell Aux: off
  Motion: off
  Noise Gate: off
  Sidechain: off
  Latch: off
  Spread: "off (SPREAD turns Manual EQ into bursts of flickering panning)"
  MISO: off
controls:
  - { name: "Mode", type: switch, value: "Mid (Manual / fixed EQ — no creative modulation)", options: ["L Shifty", "Mid Manual", "R Modulated"] }
  - { name: "EQ", type: knob, value: "tilt: CCW removes highs (darker/spongier), CW removes lows (brighter/tighter), noon = off — keep within ~10:00-2:00 for musical results (amount dialable)" }
  - { name: "Dynamics", type: knob, value: "gentle or off (this is a tone move, not a comp move)" }
  - { name: "Dry", type: knob, value: "blend up to net-emphasize a band (EQ is wet-only)" }
  - { name: "Wet", type: knob, value: "output level" }
---

# Tilt EQ — Room Conditioner

## Concept
Run Clean's lone EQ knob in Manual mode as a fixed tilt/tone conditioner with no creative modulation. Turn it CCW to remove highs for a darker, spongier tone, or CW to remove lows for a brighter, tighter tone — noon is off, and the usable musical sweep is roughly 10:00–2:00. This is Bass Fox's "room conditioning" move: brighten or darken a source or a drum bus to fit the mix without touching the compression at all. Because the EQ is wet-only, you can even net-*emphasize* a band by blending Dry back in.

## How to play it
1. Set the **Mode** toggle to **MIDDLE (Manual / fixed EQ)**.
2. Turn **EQ CCW to darken** (remove highs) or **CW to brighten/tighten** (remove lows) — noon is off; keep within **~10:00–2:00** for musical results.
3. **Trust the manual's direction:** CCW removes highs, CW removes lows (one demo had this reversed — go by ear and by the manual, not the demo).
4. Because the EQ only touches the wet path, **blend Dry up to net-emphasize a band** — e.g. cut all the highs on the wet and mix it in so the mixer/limiter adds low end to a kick with no first-stage compression needed. Use the same trick to restore brightness lost to heavy compression upstream.

## Notes
- **Direction and sweep are published; the exact amount is a dialable recipe** — there are no published knob *positions* for a given source, so set the tilt by ear against the mix.
- Single-dial tilt EQ only (no separate low/mid/high) — a limitation vs. a multi-band comp.
- One demo (Bass Fox) shows the EQ direction reversed relative to the manual; the controls above follow the **manual** (CCW = remove highs, CW = remove lows).
- **In THIS rig, keep EQ at noon** for Clean's front-of-board role and let the Colour Box do the tone shaping — this patch is for when Clean is redeployed as a studio / bus tool.
- BachelorMachines' wet-only EQ trick: cut all highs on the wet, blend it in, and let the mixer + limiter supply the low end with no first-stage comp.

## Sources
- `research/transcripts/bassfox-quincas-moreira-studio-tool-sidechain.md` (drums played with the tilt EQ brighter/darker, "room conditioning"; note the presenter's CW/CCW is reversed vs. the manual)
- `research/transcripts/bachelormachines-compressor-science-deep-dive.md` (Manual EQ is wet-only; add low end to a kick by cutting highs on the wet and blending)
- `research/transcripts/chase-bliss-clean-official-video-manual.md` (CCW removes highs, CW removes lows, noon = no effect)
- reviewrevival.ca/reviews/chase-bliss-clean-definitive-review-2025 (usable sweep ~10:00–2:00; SPREAD = flickering panning)
- Chase Bliss Clean official manual (EQ p.28–29 — Manual mode)
- Provenance: demo (Bass Fox / BachelorMachines) + manual + ReviewRevival (Manual tilt EQ) — direction/sweep published, dialable for amounts
