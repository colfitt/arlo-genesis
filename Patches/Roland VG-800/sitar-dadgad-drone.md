---
type: patch
title: "Sitar (DADGAD) — buzzing drone-string raga texture"
device: Roland VG-800
date: 2026-06-15
description: "The factory sitar preset Marcus Curtis tours in DADGAD / a sitar tuning — the VG-800's modeled SITAR voice with its buzzing sympathetic-string character, set up for droning raga textures (good enough for a \"Norwegian Wood\" cover, per Sound on Sound). Honest caveat: reviewers call the sitar the weak model, which is exactly the \"recorded-wrong\" texture this rig can exploit into a smear/fuzz."
tags: [sitar, drone, alt-tuning, factory, textural, world]
dips:
  CONTROL ASSIGN (GUITAR TO MIDI → ALT TUNE): "ON only if you MIDI out the retuned pitches"
controls:
  - { name: "INST TYPE", type: switch, value: "ACOUSTIC → SITAR model" }
  - { name: "ALT TUNE SW", type: switch, value: "ON", options: ["ON", "OFF"] }
  - { name: "ALT TUNE TYPE", type: switch, value: "D-MODAL (DADGAD; drops 1st/2nd/6th a whole step)" }
  - { name: "INST sub-params", type: knob, value: "dial from factory memory — no published values" }
  - { name: "REVERB", type: knob, value: "optional, add for sympathetic-string shimmer (recipe)" }
  - { name: "Slot/Bank", type: knob, value: "Factory sitar memory, or User Memory" }
---

# Sitar (DADGAD) — buzzing drone-string raga texture

## Concept

The factory sitar preset Marcus Curtis tours in DADGAD / a sitar tuning — the VG-800's modeled `SITAR` voice with its buzzing sympathetic-string character, set up for droning raga textures (good enough for a "Norwegian Wood" cover, per Sound on Sound). `ALT TUNE TYPE = D-MODAL` drops the 1st/2nd/6th a whole step for the DADGAD-type drone-string setup. Honest caveat: reviewers call the sitar the weak model — which is exactly the "recorded-wrong" texture this rig can exploit by smearing it into a reverb/fuzz wall.

## How to play it

1. Recall the factory sitar memory, or build: `INST = ACOUSTIC`, `TYPE = SITAR`.
2. `ALT TUNE SW = ON`, `ALT TUNE TYPE = D-MODAL` (drops 1st/2nd/6th a whole step — DADGAD-type drone) per the Parameter Guide.
3. Let open drone strings ring; play melodic lines with slides/bends over the drone for a raga feel.
4. Add reverb to suggest sympathetic strings; into a smear reverb (Dark Star V3 / Etherealizer) or the fuzz wall, the sitar's artifacts become texture, not a flaw.

## Notes

- Named factory behavior: Marcus Curtis demos "Sitar in DADGAD / a sitar tuning." D-MODAL definition is manual-verified.
- Honesty: the sitar model "wouldn't have fooled Ravi Shankar" but is fine for a "Norwegian Wood" cover (Sound on Sound) — use it as texture into time/space effects, not as a literal sitar.
- There may also be a separate Sitar Emulator effect in the broad FX list (web sources), but only the `SITAR` INST model is repo-verified. Exact INST sub-parameters and the precise factory tuning are not published — dial from the factory memory.
- 🟢 ALT TUNE recipe is manual-verified; 🟣 sitar INST values are dialed from a recipe (no published values).

## Sources

- 🟢 `research/transcripts/marcus-curtis-setup-and-demo.md` ("Sitar in DADGAD / a sitar tuning")
- 🟢 `research/links/parameter-guide-alt-tuning-values.md` (D-MODAL = DADGAD-type, manual-verified)
- `research/VG-800-DeepResearch.md` §3 (sitar = weak model, SoS)
- https://www.soundonsound.com/reviews/boss-vg-800 (sitar fine for a "Norwegian Wood" cover, not a concert sitar)
- https://guitar.com/news/gear-news/boss-vg-800-explore-mountains-of-electric-and-acoustic-guitar-sitar-and-banjo-sounds/ (sitar among the modeled stringed instruments)
- Provenance: factory preset (named) + manual-verified ALT TUNE recipe; merged with web reviewer notes; sitar INST values not published
