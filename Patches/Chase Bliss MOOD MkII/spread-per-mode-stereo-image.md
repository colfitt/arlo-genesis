---
type: patch
title: SPREAD — per-mode affected stereo image
device: Chase Bliss MOOD MkII
date: 2026-06-15
description: "Each MOOD mode has its own stereo behavior, unlocked by the SPREAD dip: Reverb scatters its taps, Delay ping-pongs L/R, Slip/Env/Stretch auto-pan, and Tape plays the right channel forward while the left runs in reverse. SPREAD does not enable stereo (MOOD is stereo by default) — it widens and animates the existing image, the fastest way to make any mode wide and moving. (Factory dip feature — official video manual pt.2 + manual pp.36-39; demo review guitar.com — no published clock-face values, so dial from the recipe.)"
tags: [dip, stereo, spread, ping-pong, panning, factory, technique]
dips:
  SPREAD: on (generate an affected stereo image — each mode has a unique take)
controls:
  - { name: "Wet MODE", type: switch, value: "any (Reverb = scattered taps, Delay = ping-pong, Slip = smooth pan)", options: ["Reverb", "Delay", "Slip"] }
  - { name: "Looper MODE", type: switch, value: "any (Env = pans over threshold, Tape = R-forward/L-reversed, Stretch = slow pan)", options: ["Env", "Tape", "Stretch"] }
  - { name: "CLOCK", type: knob, value: "sets pan/scatter speed together with the active mode's time control (dial to taste — no published values)" }
  - { name: "STEREO WIDTH (hidden — Wet TIME)", type: knob, value: "hold both footswitches + turn Wet TIME to set how wide the spread is (dial to taste)" }
  - { name: "SPREAD SOLO (hidden — ROUTING)", type: switch, value: "optional — spread only one channel instead of both" }
---

# SPREAD — per-mode affected stereo image

## Concept
SPREAD is the fastest way to make any mode wide and moving. It does **not** turn stereo on (MOOD is stereo by default — MISO handles a mono source); it **widens and animates the existing image**, and every mode has its own take on it. Reverb scatters its taps across the field, Delay ping-pongs L↔R (mirroring your input pan depth), Slip / Env / Stretch auto-pan, and Tape plays the right channel forward while the left channel runs in reverse. One dip, six distinct stereo behaviors.

## How to play it
1. Confirm you have a stereo image (stereo in, or MISO on for a mono source).
2. Flick the **SPREAD** dip on.
3. Pick a mode and play: Reverb taps scatter, Delay ping-pongs L↔R, Tape plays right-forward / left-reversed, Slip / Env / Stretch pan.
4. Hold both footswitches and turn **Wet TIME** to set **STEREO WIDTH**; use **SPREAD SOLO** (hidden, ROUTING) to spread only one channel.

## Notes
- No published clock-face values — controls above are a dialable recipe; the active mode's time control plus CLOCK set the pan/scatter speed, and Wet TIME (held) sets the width.
- SPREAD enhances/widens existing stereo — it does **not** turn stereo on (that's MISO).
- Tape's L-reversed / R-forward split is a distinctive, documented per-mode behavior worth exploiting for a wide degraded bed.
- Reviewers note the clean Delay ping-pong is "an absolute treat in a wide stereo rig."
- Rig flag: a mono downstream pedal collapses the spread — keep wide SPREAD for stereo-capable downstream stages.

## Sources
- gear/Chase Bliss MOOD MkII/research/transcripts/chasebliss-mood-mkii-video-manual-pt2.md (SPREAD — "generate an affected stereo image. Each of MOOD's modes has a unique take on this")
- gear/Chase Bliss MOOD MkII/research/MOOD-MkII-DeepResearch.md §4 (SPREAD per-mode: Reverb scatters, Delay ping-pongs, Slip/Env/Stretch pan, Tape right-forward/left-reversed, pp.38–39)
- gear/Chase Bliss MOOD MkII/research/transcripts/youtube-mood-mkii-hidden-options-dip-walkthrough.md (SPREAD "enhancing the stereo field… not turning stereo on or off")
- gear/Chase Bliss MOOD MkII/research/links/community-mood-mkii-guitar-com-hands-on-tips.md (delay "ping-pong stereo output")
- Chase Bliss MOOD MkII manual, "Spread" p.36-39 + "Customize" p.44 — chasebliss.com
- guitar.com "The Big Review: Chase Bliss Mood MkII" (clean delay in wide stereo rig) — guitar.com/reviews/effects-pedal/the-big-review-chase-bliss-mood-mkii/
