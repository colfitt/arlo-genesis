---
type: patch
title: Doom Freeze Granulate (Trail Catcher bake + low-CLOCK wall)
device: Chase Bliss MOOD MkII
date: 2026-06-15
description: "Spotlight MOOD voice for the Hizumitas → MOOD Doom Freeze → Dark Star chain: freeze a maxed Hizumitas fuzz chord into an infinite Reverb bed, Trail-Catch it (briefly toggle the Micro-Looper off/on while the Wet trails are alive) to bake the fuzz + reverb PERMANENTLY into the micro-loop, then roll CLOCK down (CCW) into the lower third to granulate/downsample the baked loop into a degraded aliased wall. (DOUG-designed; the three component techniques are individually manual-documented, but the MIX/TIME/MODIFY and exact CLOCK positions are a dialable recipe, not published preset values.)"
tags: [doom, freeze, granular, trail-catcher, resample, reverb, degrade, clock, wall-of-sound, designed, signature]
dips:
  MISO: on (mono fuzz in → stereo wet/looper out)
  TRAILS: on (toggling the Micro-Looper mid-performance won't kill the wash)
  LATCH: on (the Wet freeze holds hands-free)
  SMOOTH: on (continuous CLOCK bend instead of stepped 4ths/5ths)
controls:
  - { name: "Wet MODE", type: switch, value: "Reverb (the freeze + smear engine)", options: ["Reverb", "Delay", "Slip"] }
  - { name: "ROUTING", type: switch, value: "IN+micro-loop (loop runs THROUGH the Reverb so the fuzz + trails get baked in)", options: ["IN", "IN+micro-loop", "micro-loop only"] }
  - { name: "MIX", type: knob, value: "~1:00 (mostly wet — the baked fuzz wall owns the low-mids) — dial by ear, no published value" }
  - { name: "Wet TIME", type: knob, value: "up enough to sustain the freeze indefinitely — dial by ear, no published value" }
  - { name: "Wet MODIFY", type: knob, value: "~1:00 (heavy smear) — dial by ear, no published value" }
  - { name: "CLOCK", type: knob, value: "rolled down (CCW) into the lower third live to granulate/downsample the baked loop — scale: 2k…3k…4k…6k…(12k noon)…16k…24k…32k…48k…64k (target ~6k → 4k → 3k → 2k)" }
  - { name: "LEFT footswitch (Wet / freeze)", type: button, value: "HOLD to freeze the fuzz-soaked Reverb into an infinite bed; LATCH holds it hands-free" }
  - { name: "RIGHT footswitch (Micro-Looper)", type: button, value: "while the Wet trails are alive, briefly toggle OFF then back ON to Trail-Catch (resample the fuzz + reverb trails PERMANENTLY into the loop). ⚠️ Permanent." }
---

# Doom Freeze Granulate (Trail Catcher bake + low-CLOCK wall)

## Concept
A purpose-built doom move that fuses three documented MOOD techniques into one gesture. Hold a maxed Hizumitas chord into a Reverb-freeze, then Trail-Catch (briefly toggle the Micro-Looper off/on while the Wet trails are alive) to resample the fuzz + reverb PERMANENTLY into the micro-loop. Then roll CLOCK down (CCW) into the lower third to granulate/downsample the baked-in fuzz into a degraded, aliased wall. The Hizumitas's long dense sustain is what makes the resample capture a real wall instead of a choppy stab, and gives the low-CLOCK granulate unbroken material to degrade. Built to feed a cavernous octave-down stereo verb (Dark Star) as the final space. Distinct from the factory **Trail Catcher** sheet (bake only, no granulate or doom framing), **Clock-Decay Character Shift** (live tail degrade, no resample), and **Freeze Pad** (hold only) — this chains all three over a maxed-fuzz source as the chain's spotlight.

## How to play it
1. Set Wet MODE = **Reverb**, ROUTING = **IN+micro-loop**, MIX ~1:00, Wet TIME up to sustain, Wet MODIFY ~1:00 (heavy smear). Flick dips **MISO** on, **TRAILS** on, **LATCH** on, **SMOOTH** on.
2. Hold a **maxed-Hizumitas baritone chord** and let the fuzz sustain bloom.
3. **HOLD the LEFT** (Wet) footswitch to freeze the fuzz-soaked reverb into an infinite bed (LATCH holds it hands-free).
4. While the Wet trails are alive, **briefly toggle the RIGHT** (Micro-Looper) footswitch **OFF and back ON** — Trail Catcher resamples the fuzz + reverb trails PERMANENTLY into the micro-loop. (Plan this moment — it's permanent.)
5. **Roll CLOCK down (CCW)** into the lower third (6k → 4k → 3k → 2k) to granulate/downsample the baked loop into a degraded, aliased wall — **SMOOTH** on makes it a continuous bend.
6. Play/drone over the wall, or feed it straight into the **Dark Star** octave-down stereo verb for the enormous final space.

## Notes
- ⚠️ **Trail Catcher is PERMANENT — plan the moment.** While **overdubbing**, Wet effects are NOT recorded (clean input only); the bake only happens in the bypassed always-listening state when you toggle the Micro-Looper off/on.
- The maxed Hizumitas's **long dense sustain is load-bearing**: it makes the resample capture a continuous wall, not a choppy stab, and gives the low-CLOCK granulate unbroken material to degrade.
- Low CLOCK = heavy aliasing/downsampling ("computer noises"); high = hi-fi. **SMOOTH** on gives a continuous bend instead of stepped 4ths/5ths.
- ⚠️ **Honesty:** no published numeric values for this exact patch — MIX/TIME/MODIFY/CLOCK positions are a **dialable starting point, not sourced**. The component techniques (Trail Catcher resample, low-CLOCK granulate, Freeze-Pad hold) are each individually documented (see Sources).
- Purpose-built for the **Hizumitas → MOOD Doom Freeze → Dark Star** chain; the spotlight pedal in that chain. Keep MIX where the baked fuzz wall owns the low-mids before the Dark Star adds its room.

## Sources
- 🟣 designed (DOUG) — purpose-built for the Hizumitas → MOOD Doom Freeze → Dark Star chain. Fuses three individually-documented MOOD techniques (Trail Catcher resample, low-CLOCK granulate, Freeze-Pad hold); the numeric MIX/TIME/MODIFY/CLOCK positions are a dialable recipe, not published presets.
- MOOD "Trail Catcher" patch sheet — permanent reverb-trail resample via toggling the Micro-Looper off/on; overdub does not record Wet (manual pp.28–31, p.41; chasebliss-mood-mkii-video-manual-pt1.md; Patches/Chase Bliss MOOD MkII/trail-catcher.md).
- MOOD "Clock-Decay Character Shift" patch sheet — low-CLOCK granulate/downsample sweep, CLOCK scale (2k…12k noon…64k), SMOOTH continuous bend (manual pp.18–19; mood-mkii-official-manual-try-this-recipes.md Recipe 2; Patches/Chase Bliss MOOD MkII/clock-decay-character-shift.md).
- MOOD "Freeze Pad" patch sheet — HOLD LEFT (Wet) to freeze infinitely, LATCH/TRAILS dips (manual pp.22–23; Patches/Chase Bliss MOOD MkII/freeze-pad.md).
- Pairing basis: EQD Hizumitas "Doom Wall (max heavy)" as the sustained source whose long tail makes downstream capture sound intentional (Patches/EarthQuaker Devices Hizumitas/).
