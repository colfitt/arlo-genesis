---
type: patch
title: Falling-Apart Misbias Delay
device: Chase Bliss Big Time
date: 2026-06-15
description: "DOUG-designed (not factory) — a mournful, decaying #!&% misbias delay where each repeat crumbles and detunes as it loses level, dying out down the tail instead of climbing into a wall. Numeric values are a dialable recipe interpreting Chase Bliss's published character; flying faders override on recall."
tags: [degraded, misbias, delay, lo-fi, mournful, decay, falls-apart, signature]
controls:
  - { name: "MODE", type: switch, value: "Long", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "#!&% (misbias)", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Warm", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine (subtle tape-wow quiver)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "~35% (modest)" }
  - { name: "FEEDBACK", type: knob, value: "~45-55% (BELOW color → repeats fall apart instead of climbing)" }
  - { name: "TIME", type: knob, value: "to taste / tapped" }
  - { name: "CLUSTER", type: knob, value: "low-mid" }
  - { name: "TILT EQ", type: knob, value: "at/below noon (warm, mournful darkening)" }
  - { name: "WET", type: knob, value: "~40-50% (dry retained — not wet-only)" }
  - { name: "TEXTURE", type: knob, value: "mid (alt under COLOR = misbias sensitivity; lower = repeats coherent longer, higher = falls apart fast)" }
  - { name: "DIFFUSE", type: knob, value: "low-mid (alt under FEEDBACK)" }
  - { name: "SPREAD", type: switch, value: "off (mono two-pedal box) or widen", options: ["off", "widen", "ping-pong"] }
  - { name: "DRY KILL", type: switch, value: "OFF (series, dry retained) — flip ON only to run wet as parallel/aux", options: ["off", "on"] }
  - { name: "RIGHT footswitch (hold MODE)", type: button, value: "panic-reset back to a clean delay if the misbias runs away" }
---

# Falling-Apart Misbias Delay

## Concept
A mournful, decaying delay built on the #!&% (misbias) STATE: each repeat crumbles and detunes harder as it loses level over the tail, so the line dies out and falls apart rather than climbing into a wall. MODE Long + STATE #!&% + VOICING Warm with FEEDBACK kept below COLOR so echoes lose energy and disintegrate down the tail (the inverse of the doom-wall gain structure). Dry retained — this is a delay played UNDER collapsing notes, not a wet-only loop. Pairs with Clean's Sag/hold-bypass swell upstream, which the misbias dissolves into ghost repeats. Big Time publishes character, not numbers; the values here are a dialable recipe (flying faders override on recall) — flagged as such.

## How to play it
1. Set **MODE Long**, **STATE #!&% (misbias)**, **VOICING Warm**.
2. Dial **FEEDBACK below COLOR** (e.g. FEEDBACK ~50%, COLOR ~35%) so the repeats lose energy and fall apart down the tail instead of self-oscillating into a wall.
3. **TILT EQ at/below noon** for the warm, mournful darkening; **MOTION Sine** subtle for the tape-wow quiver.
4. Set **TEXTURE** (alt under COLOR) for misbias sensitivity — lower keeps repeats coherent longer before they collapse, higher makes them fall apart fast.
5. Play sparse held notes: quiet playing passes into mostly-coherent repeats, digging in triggers faster misbias dropout — each repeat crumbles and detunes more as it decays.
6. Keep dry retained (**DRY KILL OFF**) so it reads as a delay under the note, not a wet-only loop; flip DRY KILL ON only to run the wet as a parallel/aux.

## Notes
- Distinct from **Nostalgic Repeater** (DRY KILL wet-only Frippertronics loop), **Cluster$%&!** (high-CLUSTER chaotic swirling wash), and **Loop Diffuser** (infinite-feedback climbing doom wall) — this one is a DRY-retained mournful delay tuned to DECAY and fall apart, not climb or loop.
- #!&% misbias is playing-reactive: gentle = mostly clean, dig in = fast dropout/detune (Basinski "punch-in-clean-then-destroy" is native here).
- FEEDBACK kept BELOW COLOR is the deliberate inverse of the documented low-COLOR/high-FEEDBACK "most change over time" climbing-wall structure — here the line is meant to die out and disintegrate.
- 🟡 All numeric values are a **dialable recipe, NOT published settings** — Chase Bliss publishes character; on recall the saved preset's flying faders override anything written here.
- Pairs with Clean's hold-BYPASS max-Sag swell upstream: the swelled, level-shifted tone drops in and the misbias dissolves it into a ghost repeat.
- Hold MODE = panic-reset back to a clean delay if the misbias runs away.

## Sources
- 🟢 character (numerics interpreted) — `research/transcripts/sonicstate-superbooth-john-snyder-eae-interview.md` (#!&% misbias playing-reactivity: "play gently → stays clean; dig in → texture"; #!&% sag-and-return).
- 🟢 character — `research/links/cb-big-time-factory-presets-recipes.md` (factory intent quoted; misbias STATE character).
- 🟡 manual pp.24-25 (low-COLOR/high-FEEDBACK = "most change over time" climbing wall — inverted here to FEEDBACK-below-COLOR for falling-apart decay).
- Provenance: DOUG-designed patch from manufacturer-described character (#!&% misbias STATE + sag-and-return, Warm voicing, published COLOR/FEEDBACK gain rule inverted for decay). STATE/MODE/VOICING are named positions from the concept; all knob clock-face values are a dialable recipe, NOT published numbers — flagged in-patch.
