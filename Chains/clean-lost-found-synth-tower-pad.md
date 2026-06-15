---
type: chain
title: "Clean → Lost & Found Synth-Tower Pad"
date: 2026-06-15
artists: [Stars of the Lid, Hans Zimmer]
instrument: baritone / low-register block chords
gear:
  - Chase Bliss Clean
  - Chase Bliss Lost & Found
---

# Clean → Lost & Found Synth-Tower Pad

A cinematic polyphonic sub-octave synth-and-pipe pad built from struck low block chords — a glassy synth tower that resonates forever. Two boxes, and the whole move is L&F's named **SYNTH TOWER** combo: the Impulse Synthesizer tracks each chord with sub-octave weight while the Sympathetic Resonator rings glassy pipes over the top, both running in `L+R` parallel and fused by L&F's hidden end-of-chain **GLUE**. The catch is that pitch-tracking modes only lock cleanly onto an *even, sustained* source — a passive baritone's first attack is a boomy spike that decays fast, which is exactly what makes a tracker stutter or drop the chord. So **Clean goes first to even the dynamics**: it limits the boom, tames the low strings, and stretches each struck chord into a flat-topped held bed *before* L&F ever tries to read the pitch. This is a 🟣 DOUG-designed integration; no artist played this exact chain — the artists/taste-ref name the sound it chases. L&F-spotlight.

## Signal path

Baritone (passive Jazzmaster, low-register block chords) → **CB Clean — "Baritone Drone Sustainer"** (full-range envelope, limiting + slow release = evened, sustained low bed) → **CB Lost & Found — "Synth Tower (Dual Synth Tracker)"** (`L+R` parallel: 5A Impulse Synth + 5B Sympathetic Resonator, GLUE ~11:00, MIX FULL, SPREAD on) → amp / interface (stereo).

## Per-unit

- **CB Clean — "Baritone Drone Sustainer":** Sensitivity set by the left LED with a **full-range envelope** — do NOT high-pass the control signal here; you *want* it to catch the lows and tame the baritone boom (Envelope Balance LEFT/full on the hidden page). Dynamics ~noon = **limiting**, which puts a flat ceiling on the violent first-attack spike; Attack ~10:00 (slightly faster, to catch the heavier/slower baritone transients); Release toggle **RIGHT (Slow 1.5 s)** to extend the held chord into a sustained bed; Wet ~1:00, Dry ~10:00 (keep some real-string body so the tracker has a clean fundamental to follow); EQ ~1:00 only if the lows still overwhelm. All CUSTOMIZE dips OFF. This is Clean doing one job: hand L&F an even, sustaining low chord instead of a spiky decaying one. *Approximate/designed values — dial Sensitivity by feel against the LED (GK-5/passive output differs); CB publishes character, not clock-face numbers.*
- **CB Lost & Found — "Synth Tower (Dual Synth Tracker)":** L&F's named factory combo. ROUTING **`L+R` parallel**, MIX **FULL** (CB marks this combo `*`). L slot = **5A Impulse Synthesizer** (requires **L SWAP on** — both modes live on the right channel natively), MODIFY (brightness) ~11:00–12:00 to keep it dark for doom, TIME (portamento) ~10:00; pick a **slow ALT attack** so the synth voice blooms as a pad rather than plucking. R slot = **5B Sympathetic Resonator**, MODIFY (feedback) ~2:00 for a long glassy ring, ALT octave **−1** for sub weight (sweep it during the ring for expression). BLEND ~noon balances the two synth voices. Hidden **GLUE ~11:00** — the Impulse Synth is a *dynamic* voice and GLUE evens it so the two voices fuse into one tower instead of one stabbing past the other. **SPREAD on, TRAILS on.** **Play BLOCK CHORDS struck together** — rolled chords only voice the last note. *GLUE position and the synth-side knob values are L&F's documented combo recipe + shipping map; treat exact clock positions as a dialable recipe set by ear.*

## Routing

Two boxes, series in → stereo out. Clean is in its **front-of-chain dynamics slot** (mono is fine — its SPREAD/MISO stay OFF here; width is L&F's job); L&F runs **stereo-out** with SPREAD on, so the pad fans wide from a single box. **The order and gain-staging are the entire chain:**

1. **Clean MUST come first, and it must be limiting, not just compressing.** A pitch tracker needs a steady fundamental to lock onto. The passive baritone's raw signal is a loud transient that collapses into a fast decay — feed *that* to the Impulse Synth and it stutters, mis-tracks, or drops the chord as it dies. Clean's hard ceiling (Dynamics ~noon) flattens the attack spike and the slow release holds the note up, so L&F reads one continuous, even chord. This is the "even the dynamics so the synth/resonator modes lock" move, made literal.
2. **Keep some Dry on Clean.** A 100%-wet over-limited signal can sound pumped and lose the clean fundamental the tracker keys off. Dry ~10:00 leaves real string in the blend so the Impulse Synth has an honest pitch to follow.
3. **GLUE fuses the two voices into one tower.** Impulse Synth (dynamic, attacky) and Sympathetic Resonator (slow, ringing) have very different envelopes; without GLUE the synth stabs out in front of the pipes. GLUE ~11:00 is L&F's own internal compressor evening them at the *output* — so you get two glue stages doing two different jobs: Clean evens the *input* chord for tracking, GLUE evens the *two synth voices* for cohesion. Don't push GLUE hard or the dynamic life flattens into a static drone.
4. **If it muds up on a low Jazz-bass-register chord,** watch GLUE/MIX so the wet sub doesn't swallow the fundamental (Impulse Synth is register-sensitive — it tracks fuller an octave down, but the sub can boom). Pull MODIFY (brightness) up slightly or ease the Resonator's −1 octave before touching Clean.

## Sound

A glassy, polyphonic sub-octave synth tower: each struck low chord blooms into a dark synth pad weighted with a sub-octave, haloed by long ringing pipe-resonance that hangs on after your hands leave the strings — evened and fused into one cinematic body that resonates forever. **Taste-ref:** Stars of the Lid's slow, swelling glassy drone-orchestras crossed with a Hans Zimmer low-brass-and-synth-pad bed — pitched, sustained, and architectural rather than rhythmic.

## Play

Strike **block chords together** in the low register and let go — the limiting holds the chord up while the Impulse Synth fills in the sub and the Resonator rings the pipes over the top. Because Clean's release does the sustaining, you don't have to hold the chord physically: hit it cleanly, lift, and let the tower bloom. Move slowly — pitch modes track cleanest on slow, sustained chordal input; fast changes or rolled chords artifact (the tracker only voices the last note of a roll). For expression, **sweep the Resonator's ALT octave during the ring** to bend the sub under the held pad, or ease Clean's Dynamics back toward compression (off the hard ceiling) when you want the chords to breathe with more attack instead of sitting as a flat pad. For a deeper, darker tower, drop the Impulse Synth MODIFY brightness and lean the BLEND toward the Resonator; for more shimmer up top, BLEND back toward noon.

## Sources

- **Basis:** 🟣 designed integration; chains **CB Clean — "Baritone Drone Sustainer"** (reused) + **CB Lost & Found — "Synth Tower (Dual Synth Tracker)"** (reused). The "limit-first so the pitch tracker locks onto an even held chord" rationale follows directly from the L&F shipping map (pitch modes track cleanest on slow sustained chordal input; "play block chords struck together") and Clean's documented baritone limiting role (full-range envelope, Dynamics ~noon limiting, slow release to extend a held bed).
- L&F **SYNTH TOWER** combo (Impulse Synthesizer + Sympathetic Resonator, `L+R` parallel, L SWAP on, MIX FULL/`*`, GLUE ~11:00 to even the dynamic Impulse Synth) from the CB Field Guide named Combos + BachelorMachinesTV Pt2 shipping maps, as captured in the Synth Tower patch sheet. L&F's hidden end-of-chain Glue compressor/saturator is documented in `gear/Chase Bliss Lost & Found/GearProfile.md`.
- Clean baritone limiting recipe (full-range Envelope Balance, faster attack for heavier transients, slow release + limiting for a sustained bed) from the Baritone Drone Sustainer sheet (Clean-DeepResearch §6 / Ricky Tinez live-limiter).
- **Honesty flag:** Chase Bliss publishes character, not clock-face numbers, for both pedals — all knob positions here (Clean Sensitivity/Dynamics/Attack/Wet/Dry, L&F MODIFY/BLEND/GLUE/ALT) are a dialable recipe set by ear and by the Clean LED, not factory-published values. The combo *structure* (modes, routing, SWAP, MIX FULL, SPREAD/TRAILS, GLUE evens the Impulse Synth) is sourced; the exact positions are interpretation.
