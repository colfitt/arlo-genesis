https://www.hologramelectronics.com/pages/microcosm
hologramelectronics.com (official feature page) + YouTube looper tutorials (Hologram channel) · accessed 2026-06

# Looper deep-dive — pre/post-FX, reverse, vari-speed, burst, "auto-feedback"

Distilled from Hologram's official looper feature copy + their two official looping tutorial videos. Captures the looper gotchas and creative uses the brief asked for.

## Pre-FX vs Post-FX routing (the central looper concept)
Hologram's own analogy (from the looping tutorial):
- **Pre-FX = "paintbrushes on a canvas."** The loop records DRY; effects sit *after* the loop, so the effect re-processes the loop live. "Each new addition to the loop can have a different tone" — you can change engine/settings across overdubs and paint different colors onto the same loop.
- **Post-FX (default) = "an Instagram filter / picture frame."** The effect is **printed into** the loop. With the granular engines (which change constantly), "you can create situations where the loop keeps playing but never sounds the same way twice."
- **Killer feature:** you can flip pre↔post **instantly with a button press** (or CC 24) — switch the relationship between loop and effects mid-performance.

## Reverse, vari-speed, "auto-feedback"
- **Reverse:** dedicated switch (CC 23). You can also **record a loop while Reverse is active so it begins playback reversed.**
- **Vari-speed:** continuous playback-speed control (CC 17) — pitch/time-bend the whole loop.
- **"Auto-feedback" (gotcha + feature):** there is **no direct feedback/decay control** for the looper. But as you keep overdubbing, **older layers naturally fade out** on their own — Hologram calls this the practical equivalent of feedback. "Just jumping back and forth a couple of minutes will reveal some dramatic changes in the relative levels of older layers." Plan for it: long overdub sessions self-erase the oldest material.

## Burst mode (CC 26)
- **Burst = fast one-layer loops:** in Burst mode the **left footswitch records only while held down** — release = stop. Great for stutter/glitch stabs rather than sustained loops.

## Looper gotchas for THIS rig
- **The looper clears the Hold Sampler buffer** — they're mutually exclusive captures; decide which you're in.
- **Quantize (CC 27)** trims to nearest beat for sync, but over external MIDI clock it can **drift** on minute-plus loops (see Elektronauts capture) — re-quantize/re-trigger rather than free-running.
- For *structured song loops* the rig already plans to use the **CB Blooper**; reserve the Microcosm looper for **granular-bed capture** (record the evolving granular output, post-FX) where the never-the-same-twice behavior is the point.
