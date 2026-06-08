---
video_url: https://www.youtube.com/watch?v=26AH-aL4b6Q
channel: "chase bliss"
title: "Clean - Video Manual"
duration: 861
ingested_at: 2026-06-03
---

# Clean — Video Manual (Chase Bliss official, ~14 min)

The maker's own walkthrough — the single highest-signal "how it works" source. Distilled to prose; the concrete, load-bearing bits below.

## Core concept
"Clean rewards your instrument's dynamics, creating a lively shifting version of whatever you play." Started as the question: *can the character and interactivity of distortion pedals translate to a clean instrument?* Two-stage stereo analog compressor.

## I/O config (back of pedal)
- Mono in / mono out → TS both ends.
- Stereo in / stereo out → TRS both ends.
- Mono in → stereo out → **TS input, TRS output, activate MISO dip.**
- Flip **SPREAD** dip in any config to create a unique stereo image.

## Compression controls (the essentials)
- **Sensitivity = "what too loud is"** (the dynamic threshold). CW = more sensitive. Lower = subtle/only-loud-material; higher = more responsive.
- **Dynamics = how much quieter to make it.** Zones:
  - **7:00–noon** = traditional comp: **1:1 at 7:00, 4:1 at 10:00, ∞:1 at noon.**
  - **noon–3:00** = hard limiter; gradually transitions **feedback → feedforward** (feedback = smooth/natural, feedforward = aggressive/snappy). Here **Sensitivity sets the maximum possible loudness.**
  - **last bit (past 3:00)** = simulated overloaded tube — "signal falls out, falters, and sputters as you play harder."
- **Wet & Dry knobs:** **Unity gain ≈ noon; both can deliver a fairly healthy boost past that.**
- **Left LED = compression meter:** brighter red = more compression. **PRO TIP: if you get lost, return to the illustrated "Home Base" settings.**
- **Attack:** 0.5 ms (min) → 300 ms (max). Also sets speed of motion-related EQ modes.
- **Release toggle:** 50 ms (L) / adjustable (mid, set by holding both footswitches + turning Attack, 50 ms–1.5 s) / 1.5 s (R).
- **Physics toggle:** L = subtle wobbly movement, MID = stable, R = twitchy/unstable. "Lets us sabotage it and produce instability and fluctuations."

## EQ section (one knob + 3 modes)
- CCW removes highs, CW removes lows, **noon = no effect.**
- **Shifty (L):** when input passes the Sensitivity threshold, EQ moves away from the knob setting toward full frequency, shifts back when you stop. Sweep speed set by Attack and Release.
- **Manual (MID):** classic fixed EQ.
- **Modulated (R):** EQ modulates around the knob's center point while you play; Attack sets speed; fades away smoothly when you stop.

## Swell (AUX footswitch)
- **Dynamic (default):** swells in when you play above the Sensitivity threshold, swells back out when you dip below.
- **Manual (flip SWELL AUX dip):** swell only when AUX is pressed; **holding mutes, releasing swells back to full;** single tap = one swell.
- Swell-in time = Wet knob hidden option; swell-out = Dry knob hidden option (100 ms → 4 s). Momentary by default; **LATCH** dip makes it latch. **Green LED tracks the swell.**

## Hidden bonus / dips
- **DUSTY:** "sets the end-of-chain limiter loose, transforming clean into a tactile overdrive with soft edges and a crumbly decay." Because the limiter is last, **changes to compressor/EQ/mixer all change the Dusty sound. Dusty also affects the DRY signal.**
- **SIDECHAIN:** external signal controls comp/EQ/swells via the 1/8" sidechain input (sync to drums etc).
- **NOISE GATE:** mutes input when not playing (filters hum amplified by compression). Hidden option under Sensitivity = gate threshold; under Dynamics = gate release.
- **MOTION:** modulates the *amount of compression* → "unique dynamic tremolo." Dynamics = depth, Attack = rate.

## Hidden options (hold both footswitches until both LEDs go green)
- **Release toggle → Envelope Type:** L = Analog (exactly matches Attack/Release knobs), R = Adaptive (auto-adjusts attack/release to playing loudness), MID = combo (analog attack + adaptive release).
- **Physics toggle → Spread Routing:** assign SPREAD independently to EQ or to volume-based effects (e.g. identical comp both channels but stereo movement only from EQ).
- **EQ knob → Envelope Balance:** filters lows out of the *control signal* so Clean responds to the upper register / ignores bass. Affects both the internal envelope follower AND the sidechain input. **Only filters control signal — no filtering on the audio outputs.**
- **Reset all hidden options:** flip preset toggle left↔center 3×, then press both footswitches when lights blink.

> Sign-off: "happy smooshing."
