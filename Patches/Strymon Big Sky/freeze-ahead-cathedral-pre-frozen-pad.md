---
type: patch
title: Freeze-Ahead Cathedral (pre-frozen pad)
device: Strymon Big Sky
date: 2026-06-15
description: "The inverted-build reverb move — swell one chord into Cloud and FREEZE it FIRST, locking an empty oceanic pad in the air, then bring a Hizumitas→Big Time fuzz wall up underneath it into a room that's already lit. DIALABLE RECIPE: the Hold=FREEZE behavior and the freeze-the-pad-first workflow are sourced (Antoine Michaud transcript + Big-Sky-DeepResearch); the clock-position knob values are DOUG-dialed starting points, not cited artist dials."
tags: [drone, doom, oceanic, wall, freeze, cloud, freeze-ahead, inverted-build, designed, signature]
hidden:
  Diffusion: high (smooths Cloud grain into a smooth pad)
  HOLD: FREEZE (not INFINITE)
controls:
  - { name: "Machine", type: switch, value: "CLOUD", options: ["Cloud","Shimmer","Bloom","Chorale","Swell","Magneto","Nonlinear","Reflections","Room","Hall","Plate","Spring"] }
  - { name: "DECAY", type: knob, value: "20s+ (long pad)" }
  - { name: "PRE-DELAY", type: knob, value: "12:00" }
  - { name: "MIX", type: knob, value: "1:00 (dominant voice at the top of the build)" }
  - { name: "TONE", type: knob, value: "11:00" }
  - { name: "MOD", type: knob, value: "1:00" }
  - { name: "VALUE", type: button, value: "click → scroll past Boost & Persist → Hold → FREEZE" }
  - { name: "HOLD footswitch", type: switch, value: "hold to FREEZE the patch in the background" }
---

# Freeze-Ahead Cathedral (pre-frozen pad)

## Concept
The inverted-build reverb move: instead of striking a chord and freezing the space that blooms out of it (freeze-after, as the existing Drone Wall / Trippy Frozen patches do), you swell ONE chord into the Cloud machine and FREEZE it FIRST — locking an empty-feeling oceanic pad in the air — then bring a saturated fuzz/delay wall up underneath it. The cathedral exists before the source arrives; the wall rises into a room that's already lit. Built on the documented Big Sky Hold behavior (hold the footswitch to freeze any patch in the background; in FREEZE, anything played on top is NOT re-fed into the held pad, so the rising wall stays legible rather than smearing into the wash the way INFINITE would).

## How to play it
1. Swell ONE chord into the Big Sky with the guitar volume knob (slow attack) so the pluck disappears into the Cloud.
2. Hold the Big Sky footswitch to FREEZE — an oceanic Cloud pad now hangs in the air with nothing under it. (Set HOLD = FREEZE first: click VALUE → scroll past Boost & Persist → Hold → FREEZE.)
3. Leave the pad held and THEN bring up the fuzz/delay wall underneath (e.g. Hizumitas → Big Time) — it rises into the existing space.
4. Because it's FREEZE not INFINITE, the rising wall stays legible against the static pad instead of being re-fed into the wash.
5. To collapse, let the wall fall away and the frozen cathedral hangs alone again — back to where it started.

## Notes
- This is freeze-AHEAD (pad frozen before the source arrives), distinct from the existing Drone Wall (Cloud, freeze) and Trippy Frozen Drone Wall patches, which are freeze-AFTER (strike then freeze).
- Use FREEZE, not INFINITE: INFINITE re-feeds every new note into the held pad and turns the inverted build to mud; FREEZE keeps the pad fixed and the rising wall distinct.
- High Diffusion smooths the Cloud grain into a smooth pad so the held space reads as a room, not a texture.
- Chain role: receives the Big Time's stereo MISO field; this is the End-board reverb holding the static room the doom build rises into — set it FIRST in the performance order even though it sits last in signal flow.
- 🟣 DOUG-designed integration; knob values are a dialable recipe (inferred starting points), not cited artist dials — the Hold behavior is the sourced part. Grab/save your own preset once dialed.

## Sources
- research/transcripts/antoine-michaud-bigsky-infinite-vs-freeze.md (youtube.com/watch?v=GYo2VkFiYYE) — Antoine Michaud, "Infinite vs Freeze": hold the footswitch to freeze any patch in the background; FREEZE leaves notes played on top unaffected, INFINITE re-feeds them and goes chaotic.
- research/Big-Sky-DeepResearch.md §13(b) — Cloud long-decay/high-diffusion frozen drone anchor.
- Cloud machine descriptions: research/links/strymon-bigsky-product-machine-descriptions.md.

<!-- provenance: 🟣 DOUG-designed integration patch. Hold/FREEZE behavior and the freeze-the-pad workflow are sourced (Antoine Michaud transcript + Big-Sky-DeepResearch); the specific clock-position knob values are an unpublished dialable recipe (DOUG-dialed starting points), flagged as such — not presented as cited artist settings. -->
