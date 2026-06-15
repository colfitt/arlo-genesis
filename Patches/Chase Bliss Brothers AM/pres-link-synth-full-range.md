---
type: patch
title: "Pres Link Open — full-range/synth voicing"
device: Chase Bliss Brothers AM
date: 2026-06-15
description: "Chase Bliss's own recommendation for full-frequency sources (synths, modeled/divided signals): engage the PRES LINK dip so the TONE knob controls TONE and PRESENCE together, giving a more open, transparent, full-range response with a single more dramatic tone control. Ideal for the modeled VG-800 output and any synth or wide-bandwidth source. Dialable recipe — CB quotes the behavior and the use-case, not clock values."
tags: [boost, pres-link, synth, full-range, transparent, designed]
dips:
  PRES LINK: "on (for the channel in use — TONE then sweeps tone+presence together)"
  MASTER: "on (optional)"
controls:
  - { name: "CHANNEL MODE (channel in use)", type: switch, value: "BOOST (most open / most headroom) or OVERDRIVE for grit", options: ["BOOST", "OVERDRIVE", "DISTORTION"] }
  - { name: "GAIN", type: knob, value: "modest — keep the wide-band source clear, not squished (dial from recipe)" }
  - { name: "VOL", type: knob, value: "dial from recipe to taste" }
  - { name: "TONE", type: knob, value: "your single open/dark-to-bright control once PRES LINK is on — sweep to the most open, full-range response (dial from recipe)" }
  - { name: "PRESENCE", type: knob, value: "now slaved to TONE via PRES LINK (no longer set independently)" }
  - { name: "TREBLE BOOSTER", type: switch, value: "MIDDLE (off) to keep it neutral, or to taste", options: ["UP (bright)", "MIDDLE (off)", "DOWN (Rangemaster)"] }
---

# Pres Link Open — full-range/synth voicing

## Concept
Chase Bliss's own recommendation for full-frequency sources — synths, modeled and divided signals. Engage the PRES LINK dip on the channel you're running and the TONE knob now controls TONE and PRESENCE together, giving a more open, transparent, full-range response from a single, more dramatic tone control. This is the documented move for the modeled VG-800 output and any synth or wide-bandwidth source: BOOST keeps the most headroom and stays open, while OVERDRIVE adds grit if you want it.

## How to play it
1. Engage the PRES LINK dip for the channel you're running — now TONE controls TONE and PRESENCE simultaneously.
2. Set that channel to BOOST (most open) or OVERDRIVE for some grit.
3. Sweep the TONE knob to find the most open, full-range response — CB recommends this for full-frequency instruments like a synth.
4. Keep GAIN modest so the wide-band source stays clear, not squished.

## Notes
- CB-recommended: the PRES LINK behavior and the "use it for full-frequency/synth sources" recommendation are quoted; no exact knob numbers — dial from recipe.
- On the modeled VG-800 source, BOOST + PRES LINK is the documented move for the most open, full-range response.
- PRES LINK "makes for a more dramatic tone control" — a wider tonal sweep from one knob. Distinct from Pres-Link Tone Sweep (which chases the dramatic single-knob move as a performance tool).
- No published knob values — phrased as a dialable recipe by design.

## Sources
- research/links/cb-technical-demo-settings.md (PRES LINK: links TONE and PRESENCE, "more dramatic tone control")
- research/transcripts/cb-technical-demo.md (PRES LINK demoed)
- Brothers-AM-DeepResearch.md §6 (PRES LINK recommended for full-frequency/synth sources; BOOST + PRES LINK for modeled VG-800)
- Ref: Brothers AM manual, "Customize" (PRES LINK)
