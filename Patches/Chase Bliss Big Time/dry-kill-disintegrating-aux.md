---
type: patch
title: Dry-Kill Disintegrating Aux
device: Chase Bliss Big Time
date: 2026-06-15
description: "DOUG-designed (not factory) — a saturated/self-degrading wet-only delay built to live on a parallel DAW aux send (DRY KILL ON) in a wet-dry-wet routing, so the analog preamp (COLOR) and limiter (STATE) only ever touch the echoes flown around a pristine printed dry. STATE/VOICING/DRY-KILL behavior and the line-staged COLOR-modest rule are sourced; numeric fader values are a dialable recipe interpreting Chase Bliss's published character — flying faders override on recall."
tags: [wet-only, dry-kill, saturated, misbias, disintegrating, aux-send, wet-dry-wet, studio, parallel, designed]
controls:
  - { name: "DRY KILL", type: switch, value: "ON (Options — pure wet return; the whole point of the patch)", options: ["off", "on"] }
  - { name: "Chain / Input", type: switch, value: "Parallel DAW/console aux → X-Amp (line→instrument) → IN; return level set on the DAW aux fader", options: ["aux send (line via X-Amp)", "insert"] }
  - { name: "MODE", type: switch, value: "Long", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Saturated (slow disintegration into a big harmonic mass) — or #!&% (misbias) for raw, self-sabotaging breakup", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "Focus (shaves highs+lows over time → focused floating repeats that sit around the dry)", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Off", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Sine, slow/subtle (tape-wow drift)", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "LOW ~25–30% (source already line-staged; over-COLORing a clean source slams the limiter to porridge — let STATE do the coloring)" }
  - { name: "TIME", type: knob, value: "tapped / MIDI clock (CC111=0 to follow)" }
  - { name: "CLUSTER", type: knob, value: "low ~20% (clean repeats, not dense)" }
  - { name: "TILT EQ", type: knob, value: "at/above noon (keep the disintegrating tail from clouding the dry center)" }
  - { name: "FEEDBACK", type: knob, value: "~55–65% (bloom + decay zone — below a runaway wall so the wet supports the dry instead of swallowing it)" }
  - { name: "WET", type: knob, value: "high / max (return level is set on the DAW aux fader anyway)" }
  - { name: "TEXTURE", type: knob, value: "mid (alt under COLOR — Saturated = clipping symmetry, more ragged turned up; #!&% = misbias sensitivity)" }
  - { name: "DIFFUSE", type: knob, value: "low-mid (alt under FEEDBACK)" }
  - { name: "SPREAD", type: switch, value: "widen (stereo wet flown around the mono/center dry)", options: ["off", "widen", "ping-pong"] }
  - { name: "RIGHT footswitch (hold)", type: button, value: "FREEZE the last phrase into a held bed, or ramp COLOR+FEEDBACK for a momentary swell" }
  - { name: "MODE footswitch (hold)", type: button, value: "panic-reset back to a clean delay if the degradation runs away" }
---

# Dry-Kill Disintegrating Aux

## Concept
A saturated/self-degrading wet-only delay purpose-built to live on a parallel DAW aux send (DRY KILL ON) in a wet-dry-wet studio routing — the pedal returns 100% wet so its analog preamp (COLOR) and limiter (STATE) only ever touch the echoes, never the printed dry. STATE Saturated gives "echoes that slowly disintegrate and expand into a big harmonic mass"; flip to the #!&% misbias STATE for the rawer, self-sabotaging "broken, drifting delay lines." COLOR stays low because an X-Amp/aux already staged the level — let STATE/TEXTURE/VOICING do the disintegrating, not COLOR slamming the limiter. FEEDBACK sits in the bloom-and-decay zone (not a runaway wall) so the wet supports a clean dry center instead of swallowing it. Distinct from "Nostalgic Repeater" (a wet-only LOOPING/Frippertronics engine) and "Line-Level Centerpiece Send" (a clean unifying glue): this one is a self-degrading delay flown around a pristine dry.

## How to play it
1. Set **DRY KILL ON** in Options so the pedal returns 100% wet — this is what makes it a clean studio send and is the load-bearing setting of the whole patch.
2. Feed it from a parallel DAW/console aux via an **X-Amp** (line→instrument), keep **COLOR low (~25–30%)**, and let **STATE** do the coloring; return level is the DAW aux fader, so set **WET high/max**.
3. Pick the disintegration flavor with **STATE**: **Saturated** for slow harmonic-mass bloom, **#!&% (misbias)** for raw self-sabotaging breakup; **TEXTURE** (alt under COLOR) sets the amount/sensitivity.
4. Keep **FEEDBACK ~55–65%** so the wet blooms and decays around the dry instead of climbing into a wall; ride the **DAW wet-aux fader** to swell it for choruses.
5. Optionally clock to the session (native 5-pin DIN; **CC111 = 0** to follow) and recall section voices via **Program Change** (PC# = slot, PC 0 = LIVE).
6. Hold the **RIGHT footswitch** to FREEZE the last phrase into a held bed, or to ramp COLOR+FEEDBACK for a momentary swell; **hold MODE** to panic-reset to a clean delay.

## Notes
- **DRY KILL is the load-bearing setting** — without it the pedal prints its dry too and the wet-dry-wet structure collapses. Verify it's ON in Options before recall.
- **COLOR low is deliberate:** an aux/X-Amp source is already at a good level, and over-saturating a clean source "sounds awful" / clamps the limiter (same rule as Crushed Analog after Generation Loss — COLOR feeds both the feedback loop AND the output limiter).
- **STATE #!&% misbias is playing-reactive** (soft = mostly clean, dig in = faster dropout) — that reactivity reads as the "self-degrading" character on the wet return.
- 🟡 All numeric fader positions are a **designed dialable recipe**, NOT published settings — Chase Bliss publishes character, not knob positions, and the motorized flying faders override anything written here on recall.
- **Not a looper** (cf. "Nostalgic Repeater") and **not a clean glue send** (cf. "Line-Level Centerpiece Send") — this is a self-degrading delay built to sit AROUND a pristine dry, not in series with it.

## Sources
- 🟢/🟣 designed from documented behavior — DRY KILL = wet-only aux return + COLOR-low for non-fuzz/line-staged sources + native-DIN clock (CC111) + PC section recall: `gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md` §C ([V/R]: "DRY KILL (Options) so Big Time returns wet-only into a parallel/aux path"; native 5-pin DIN; CC111 = MIDI clock ignore/follow; PC# recalls a slot, PC 0 = LIVE; analog stereo preamp COLOR feeding analog limiter).
- 🟢 STATE character verbatim — Saturated "echoes that slowly disintegrate and expand into a big harmonic mass"; #!&% misbias "sabotages and misbiases the limiter… raw, electric character… broken and obliterated sounds" / "broken drifting delay lines"; TEXTURE = clipping symmetry (Saturated) / misbias sensitivity: `gear/Chase Bliss Big Time/research/links/cb-big-time-factory-presets-recipes.md` + `centerpiece-big-time-as-song-centerpiece-one-pedal.md`.
- 🟣 VOICING Focus "shaves highs+lows over time → focused floating repeats" + hold-RIGHT freeze/ramp swell + hold-MODE panic-reset from the same centerpiece / Secret Weapons sources (`centerpiece-big-time-as-song-centerpiece-one-pedal.md` §3 + VOICING notes).
- Provenance: 🟣 DOUG-designed patch built from verified Big Time STATE/VOICING/DRY-KILL behavior; numeric knob positions are an interpreted dialable recipe (Chase Bliss publishes character, not numbers; flying faders override on recall) — flagged honestly per this rig's Big Time patch convention.
