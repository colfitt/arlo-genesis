---
type: patch
title: Recorded-wrong static splat (degraded)
device: MXR M173 Classic 108 Fuzz
date: 2026-06-14
description: The intentionally broken, gated, static splat — buffer off behind the always-in-line buffers so the fuzz misbehaves on purpose; lo-fi "recorded-wrong" walls fed into the granular engines.
tags: [fuzz, lo-fi, degraded, gated, post-punk, designed, signature]
controls:
  - { name: "OUTPUT/VOLUME", type: knob, value: "11:00–12:00" }
  - { name: "FUZZ/INPUT", type: knob, value: "2:00–3:00 (high, into the gate)" }
  - { name: "BUFFER", type: switch, value: "OFF", options: ["ON", "OFF"] }
---

# Recorded-wrong static splat (degraded)

## Concept
The intentionally broken, gated, static splat. Run BUFFER OFF *behind* the always-in-line buffers so the fuzz misbehaves on purpose — the thin/gated/crackly misbehavior the buffer is meant to cure is exactly the point here (Lo-fi + Post-punk brittle-texture clusters). This is Premier Guitar's "strangled chaos" voice. Feed the result into the Microcosm / Dark Star / H90 for granular degradation.

## How to play it
1. OUTPUT/VOLUME 11–12 o'clock.
2. FUZZ/INPUT 2–3 o'clock (high, into the gate).
3. BUFFER OFF — and let the buffered-into-FF mismatch make it static and "wrong."
4. Source = the VG-800/Colour Box line (NOT a passive guitar); feed it the maxed modeled line and let it sputter.
5. Embrace the gating/sputter on note decay.

## Notes
- Leans **into** the rig's normally-undesirable buffer mismatch as an aesthetic.
- Gating intensifies at high FUZZ with bright sources — the brighter the modeled line, the more ice and sputter.

## Sources
- Designed from `108-Fuzz-DeepResearch.md` §6, §11, §13(a) + `research/links/settings-premierguitar-108-review.md` + `research/transcripts/pedal-picassos-108-fuzz.md`
- Transformed from Pedalxly 108-Fuzz-Patches.md (designed)
