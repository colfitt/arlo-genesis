---
type: patch
title: "Volume-Knob Cleanup Dynamic Fuzz — Sustain under half"
device: EarthQuaker Devices Hizumitas
date: 2026-06-15
description: "Dynamic fuzz that cleans up off the guitar volume knob and picking attack while keeping its clipped edge (reviewer/community — Sweetwater + Premier Guitar + Guitar Player); behavior is sourced, exact clock values are not — dial from recipe."
tags: [dynamic, cleanup, low-gain, articulate, community]
controls:
  - { name: "Volume", type: knob, value: "near unity (~9:00) — dial from recipe, no published value" }
  - { name: "Sustain", type: knob, value: "under halfway (below noon) — load-bearing; dial from recipe, no published value" }
  - { name: "Tone", type: knob, value: "to taste — dial from recipe, no published value" }
---

# Volume-Knob Cleanup Dynamic Fuzz — Sustain under half

## Concept
With Sustain rolled back under halfway, the Hizumitas becomes an unusually dynamic fuzz that cleans up off the guitar volume knob and picking attack while keeping its clipped fuzz edge — it does NOT just collapse into a generic overdrive. Articulate even on the edge of chaos; complex chords retain note separation, so you can run clean-to-dirty passages without bypassing.

## How to play it
1. Set Sustain below noon (under halfway) and Volume near unity.
2. Play hard for full fuzz; lighten the attack or roll guitar volume down to clean up.
3. Even with a treble-bleed guitar it holds the clipped edge as you back off.
4. Exploit the note separation for clean-to-dirty passages without bypassing.

## Notes
- Reviewers: "cleans up nicely when rolling back the guitar's volume," and "with gain rolled back under halfway, very responsive to dynamics... keeps that clipped edge."
- Distinct from the existing `controlled-crunch-low-gain.md` (Sustain at minimum/CCW Tone, a factory clip); this is the mid-low Sustain dynamic-cleanup behavior with the clipped edge retained.
- **Honesty flag:** behavior is sourced, exact clock values are not — Sustain "under halfway" is the load-bearing direction. Treat all knob positions as a dialable recipe, not published numbers.
- Absorbs the in-repo guitar-volume-cleanup technique (a Sustain-UP variant); the core idea — clean up off the guitar volume — is documented across both.

## Sources
- Sweetwater user reviews — cleans up off the volume knob, dynamic under half gain (`https://www.sweetwater.com/store/detail/Hizumitas--earthquaker-devices-hizumitas-fuzz-sustainer-pedal/reviews`).
- Premier Guitar review — dynamic response, articulate on edge of chaos (`https://www.premierguitar.com/gear/reviews/earthquaker-devices-hizumitas`).
- Deep research — *"cleans up quite well when you lighten up on the attack and/or turn down the guitar volume... roll the volume back to 6–7"* (`gear/EarthQuaker Devices Hizumitas/research/Hizumitas-DeepResearch.md` §4).
- Usage guide — roll the instrument volume to 6–8 for controlled crunch, especially on treble-bleed guitars/baritone (`research/Hizumitas-UsageGuide.md` §1).
- Reviewer/community provenance (Sweetwater + Premier Guitar + Guitar Player) — dial from recipe, no published clock values.
