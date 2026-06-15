---
type: chain
title: "Big Time Pitched FREEZE Solo Bed"
date: 2026-06-15
artists: [Chase Bliss]
instrument: guitar / synth
gear:
  - Chase Bliss Big Time
  - Walrus Audio QI Etherealizer
---

# Big Time Pitched FREEZE Solo Bed ⭐

Most freeze-bed moves capture whatever chord you happen to be holding. This one builds the chord *inside* the delay first: turn SCALE on so the Big Time's pitch movement quantizes to **octaves**, stack a CLUSTER of those octave-pitched repeats into a harmonized cloud, then **FREEZE** the whole thing into a non-degrading infinite chord-pad. A galaxy-wash halo from the QI Etherealizer haloes the held pitches while you solo the live harmony on top. The inventory has plenty of freeze beds and plenty of pitched cascades — this is the missing one that *freezes the pitched cluster itself*.

🟣 DOUG-designed integration; no artist played this exact chain. The Big Time patch is purpose-built for this pitched-freeze role (full spec saved alongside); the QI patch is an existing sheet. The Taste-ref names the sound it chases. Knob numerics are dialable starting points unless a published preset is cited — see each patch sheet.

## Signal path

guitar / synth → **CB Big Time — "Pitched Cluster Freeze Bed"** (MODE Long, **SCALE Octave**, MOTION Square, CLUSTER high → build a pitched cluster, hold **RIGHT = FREEZE**, IN-L auto-**MISO** mono→stereo) → **Walrus Audio QI Etherealizer — "Galaxy Wash / Oscillating Drone"** (Series, long-press **Freeze** ramps Space to 100%, hold **Tap/Osc** for the oscillating halo) → amp / interface, stereo.

The only "real signal-order" invoked is the standard **pitch/delay engine → ambient reverb-granular halo** placement: let the Big Time establish the harmonized held cluster, then drape the QI wash over the already-frozen pitches. No artist-specific path.

## Per-unit

- **CB Big Time — "Pitched Cluster Freeze Bed"** (new, purpose-built) — MODE **Long**, STATE **Compressed** (keeps the pitched repeats stable and stops the cluster running away before you freeze; go Saturated only if you want grit on the bed), VOICING **Focus** (clean enough to keep the octave pitches legible), **SCALE Octave** (TIME/MOTION quantize to octave jumps → the repeats stack as a real pitched cluster, not a detuned smear), MOTION **Square** (Thermae-style octave jumps that lay the cluster out), COLOR **~35–45%** (modest so the repeats build without slamming the limiter), TIME **mid–long** (sets how the octave steps space out), CLUSTER **high ~70–80%** (the multitap lines that *are* the chord — this is the arrangement fader), DIFFUSE **mid–high ~60%** with DIFFUSE TYPE **on** (smears the octave taps into a pad-like cloud), FEEDBACK **~60–70%** (long enough to populate the cluster before the freeze), TILT EQ **~noon to slightly below** (a touch of low boost for body), SPREAD **widen** (octave taps spread across the stereo field), WET **set carefully — LOUD**. Play a note/chord, let the octave cluster populate, then **hold RIGHT to FREEZE** → a harmonized, non-degrading infinite chord-pad. ⚠️ Knob values are a dialable recipe (designed, not a published preset); only the SCALE/CLUSTER/FREEZE *behaviors* are sourced. If it gets unruly, **hold MODE to panic-reset** to a clean delay.
- **Walrus Audio QI Etherealizer — "Galaxy Wash / Oscillating Drone"** — Flow **Series**, Grain mode **Phrase Sample**, Playback **x.5 (−1 oct)** for weight, Grain Mix ~2:00, Delay Mix ~noon, Feedback 2–3:00, Space **3:00 (big)**, Mix **full wet**, Tone by hand. **Long-press Freeze** to ramp Space to 100% over a frozen grain; **hold Tap/Osc** to oscillate the delay into a saturated snowball halo. This is the "let the Qi take over" pole — it haloes the held Big Time pitches rather than fronting them. No EXP jack, so ride **Tone by hand** (or MIDI CC) for the live sweep.

## Routing

Mono in → Big Time **IN-L auto-engages MISO** (mono-in / stereo-out); everything from the Big Time onward is stereo, so the QI sits in a stereo field and its galaxy wash spreads around the wide frozen cluster. Run the QI **Series** so the wash sits *on* the frozen bed (Parallel keeps a drier line if you'd rather the cluster stay forward).

**Gain-staging / order discipline is the whole game.** Keep Big Time COLOR modest (~35–45%) so the octave repeats *populate the cluster* instead of compressing into porridge before you freeze — you want the pitches distinct enough that the freeze captures a real chord, not mud. Freeze the Big Time **first**, then long-press the QI Freeze: layering the QI's maxed Space *after* the pitched cluster is locked keeps the harmony legible under the wash (stacking two big ambiences before the pitches settle just smears them). Watch levels: Big Time WET is loud and the QI is full-wet with Space at 3:00 — set the Big Time WET conservatively so the QI halo has headroom to bloom.

## Sound

A harmonized, infinite chord-pad — a frozen octave-stacked cluster that holds forever — with a galaxy-sized granular/oscillating wash shimmering around the held pitches while you solo the live harmony on top. The bed is pitched and glassy; the halo is vast and slowly oscillating.

**Taste-ref:** ambient / experimental — the Chase Bliss "freeze-and-mangle" aesthetic, but with a *pitched* bed (Thermae-octave cluster frozen, à la the Emily-Hopkins "Big Time as an instrument" octave-quantize move) under a Walrus galaxy wash. Adjacent to post-punk-texture-dynamics sustained walls, but harmonized rather than a single-chord drone. Approximation: SCALE Octave gives octave/Oct+4+5 stacking, not an arbitrary played voicing — it chases the harmonized-bed *result*, not a full chord harmonizer.

## Play

1. Set Big Time: MODE Long, **SCALE Octave**, MOTION Square, CLUSTER high, COLOR modest, FEEDBACK ~60–70%.
2. Play a note or chord and let the octave repeats **populate the cluster** (a few seconds — watch it stack into a pitched cloud).
3. **Hold Big Time RIGHT to FREEZE** → harmonized, non-degrading infinite chord-pad.
4. **Long-press the QI Freeze** to ramp Space to 100% over a frozen grain; **hold Tap/Osc** for the oscillating galaxy halo. Ride **Tone by hand**.
5. Solo the live harmony over the held cluster.
6. To collapse: short-press the QI Freeze to release the wash, then **hold Big Time MODE to panic-reset** to a clean delay.

## Sources

- **Basis:** designed integration; chains **CB Big Time — "Pitched Cluster Freeze Bed"** (new) + **Walrus Audio QI Etherealizer — "Galaxy Wash / Oscillating Drone"**. SCALE = Octave / Oct+4+5 / Chromatic pitch-quantize of TIME + MOTION, and MOTION Square = Thermae octave jumps, from `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` (SCALE, manual p.30) + `research/transcripts/mark-johnston-secret-weapons-big-time-deep-dive.md` (MOTION/SCALE) + `centerpiece-harp-lady-emily-hopkins-big-time-as-instrument.md` (octave/4th/5th quantize "as an instrument"). CLUSTER = added/multitap delay lines (the "arrangement fader") + DIFFUSE smears taps into a pad, same deep-dive sheet. FREEZE = hold RIGHT, "nothing new into the buffer, current sound revolves infinitely" → non-degrading infinite bed, same deep-dive sheet (manual p.16) + the **"Oceanic Drone Bed"** sheet's freeze-then-solo move. MISO mono→stereo auto-engage and panic-reset (hold MODE) from the same Big Time research. QI galaxy-wash / long-press-Freeze ramps Space to 100% / hold-Tap oscillation / no-EXP Tone-by-hand from the QI **"Galaxy Wash / Oscillating Drone"** sheet (DeepResearch §13(d) + UsageGuide §1).
- 🟣 designed (DOUG); Big Time knob numerics are a dialable recipe, not a published preset — only the cited control *behaviors* are sourced.
