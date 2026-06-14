---
name: Soundtoys (latest)
brand: Soundtoys
category: software
subcategory: bundle
formats: [vst3, au, aax]
host_in: [logic, ableton]
installed: true
version: latest
status: owned
tags: []
related: []
---

# Soundtoys (latest)

**Summary** — Effect bundle. **Installed: EchoBoy, EchoBoy Jr, Decapitator.**

## Why I have it
The character-effects toolkit: **EchoBoy** = the in-the-box tape echo (and secret
saturator/chorus/reverb) — the software counterpart to the hardware delays;
**Decapitator** = analog saturation/distortion (its own wave, pending). Both are
"make it sound better-wrong" boxes that suit the degraded/tape aesthetic.

## Signature uses
- **EchoBoy** as character delay, **self-oscillation drones** (automate Feedback
  to infinite), **saturation-only color** (Time 0 / FB 0 / 100% wet), and
  **EchoBoy → Valhalla** for ambient walls. → `research/EchoBoy-UsageGuide.md`
- **EchoBoy Jr** — the stripped single-echo EchoBoy: same core engine + 7 curated styles +
  **a 3-way Stereo Mode incl. Ping-Pong** (it's NOT mono), but no Style-Editor Decay /
  Diffusion / Wobble / Rhythm. **Reach for Jr to stamp a tape/Memory-Man color fast on a
  banjo/baritone insert; reach for full EchoBoy for drone/ambient walls** (Decay generation-loss,
  Diffusion-loop, feedback drones). → `research/EchoBoyJr-UsageGuide.md`
- **Decapitator** — analog **harmonic color** (5 styles A/E/N/T/P), shines as
  subtle warmth not full distortion; the **Mix knob** = in-box parallel
  saturation. Saturate-then-wash into Valhalla; complements RC-20/SketchCassette
  (motion) and the hardware Colour Box/Generation Loss (committed front-end). →
  `research/Decapitator-UsageGuide.md`

## Notes
- **EchoBoy:** High Cut is inverted (max = most cut); saturation-only at Time 0
  still phases unless Width/Diffusion/Wobble are zeroed; runaway feedback boosts
  level (use the **Limited** style); won't make a smooth reverb tail (feed
  Valhalla); CPU-heavy at scale → freeze.
- **Decapitator:** **no internal oversampling → aliases at 44.1/48k** (run 96k
  for clean, or embrace the crust for lo-fi); harshness = too much Drive into
  bright material; engage **Auto** for honest A/B; **T = triode/even, P = pentode/
  odd** harmonics. AU `.component` is the right format for Logic.
- Deep usage research: EchoBoy → `research/EchoBoy-UsageGuide.md` (5T+8L);
  Decapitator → `research/Decapitator-UsageGuide.md` (6T+13L); **EchoBoy Jr →
  `research/EchoBoyJr-UsageGuide.md` (Tier-C, 4 sources, 2026-06-13).** **All 3 Soundtoys
  units done.** (Fixed a stale claim in `links/echoboy-vs-echoboy-jr.md`: Jr is single-echo
  but keeps Ping-Pong / Wide stereo — not mono.)
