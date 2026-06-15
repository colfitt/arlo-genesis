---
type: chain
title: "Clean → Big Time Harmonic-Trem Cloud"
date: 2026-06-15
artists: [Cocteau Twins, Mercury Rev]
instrument: guitar / keys
gear:
  - Boss CE-2W
  - Chase Bliss Clean
  - Chase Bliss Big Time
---

# Clean → Big Time Harmonic-Trem Cloud

A swirling pseudo-Leslie harmonic-tremolo voice smeared into rhythmic, modulated stereo echoes — a pulsing, evolving cloud of pitch-stable shimmer. The trick is that **Clean does the moving first**: its Modulated-EQ harmonic tremolo (plus MOTION and Physics) animates the raw note BEFORE it ever hits the delay, so Big Time captures *intentional* movement rather than smearing a static signal. The CE-2W out front pre-widens the source into a lush stereo field so the whole cloud is already three-dimensional before the echoes start fanning out. This is a 🟣 DOUG-designed integration — no artist played this exact chain; the artists/taste-ref name the sound it chases.

## Signal path

Guitar / keys → **Boss CE-2W — "Dreamy Ambient (Slow Oceanic Bed)"** (mono in → stereo out, lush slow wash) → **CB Clean — "Double Tremolo (Motion + Modulated EQ + Spread)"** (harmonic-trem EQ + MOTION + Physics, MISO/SPREAD stereo) → **CB Big Time — "Harmonic-Trem Cloud Catcher"** (Short, MOTION Sine, SPREAD widen — pitch-stable clean capture) → amp / interface (stereo).

## Per-unit

- **Boss CE-2W — "Dreamy Ambient (Slow Oceanic Bed)":** MODE **CE-1 Chorus**, RATE 7:30–8:00 (very slow), DEPTH ~3:00 (very deep), OUTPUT **A+B** for the stereo split. This is the lusher of the two widener patches on purpose — the concept wants a rich, oceanic field feeding the chain, not the subliminal "Subtle Stereo Widener." Mono-in/stereo-out establishes width at the very front. If lows get seasick on a dark guitar, back DEPTH toward 2:00.
- **CB Clean — "Double Tremolo (Motion + Modulated EQ + Spread)":** Mode toggle **RIGHT (Modulated)** so the EQ harmonic-tremolos at the **Attack** rate; **MISO + SPREAD + MOTION** dips ON; **Physics** engaged for the spring-glitch on the compression amount. This stacks both modulation engines (EQ moving + amplitude moving) and pans them across the stereo field = the pseudo-Leslie swirl. Set Sensitivity by the LED — motion only happens while you're playing above threshold and fades when you stop, which is exactly what makes the cloud "evolve" rather than buzz constantly. **No published clock-face values exist for this patch — all knob positions are a dialable recipe, set by ear/LED.** This is Clean redeployed in its end-of-chain stereo slot (MISO/SPREAD need stereo).
- **CB Big Time — "Harmonic-Trem Cloud Catcher":** MODE **Short**, STATE **Digital** (limiter off → pitch-stable, no smear of the trem), VOICING **HiFi** (keeps the shimmer intact), **MOTION Sine** for slow tape-style drift on the repeats, SCALE Off (pitch-stable is the whole point), **SPREAD widen** to fan the echoes wider than the Clean field, COLOR low ~25%, FEEDBACK ~45–55% (rhythmic cloud, not a runaway wall), TIME a short slap-to-eighth that lets the trem cycle land inside each repeat. **Numeric positions are a dialable recipe — Chase Bliss publishes character, not numbers.**

## Routing

Three boxes, all-stereo from the CE-2W onward. CE-2W goes **mono-in/stereo-out** (it owns the first width); Clean sits in its **end-of-chain stereo redeploy slot** (MISO converts the stereo-ish bed back to mono-in/stereo-out for its own SPREAD pan); Big Time runs stereo-in/stereo-out and widens once more. **Gain-staging / order reasoning is the headline:** Clean must come BEFORE Big Time so the harmonic tremolo is baked into the source — put the delay first and you'd just modulate a flat note and the repeats would be lifeless. Keep Big Time STATE on **Digital** (no limiter) and COLOR low so the delay stays pitch-stable and transparent — it's there to *multiply* the trem cloud in time and space, not to add its own grit. If the cloud gets muddy, thin the CE-2W DEPTH first (it's the deepest modulator in the chain), then drop Big Time FEEDBACK. The two SPREAD stages (Clean + Big Time) nest rather than fight because Clean's is amplitude/EQ pan and Big Time's is delay-tap placement.

## Sound

A pulsing, three-dimensional shimmer that never sits still: the note swirls Leslie-like in place (Clean), then that swirl is thrown into widening, sine-drifting echoes (Big Time), all riding on a lush slow chorus bed (CE-2W) — pitch-stable the whole way, so it shimmers without ever going sour. **Taste-ref:** Cocteau Twins' liquid chorused-guitar haze (Robin Guthrie) crossed with Mercury Rev's pseudo-Leslie organ-cloud washes — dream-pop width with a rotary heart.

## Play

Play sustained chords or slow arpeggios and let the Clean tremolo cycle bloom — the motion only lives while you hold above the Sensitivity threshold, so dynamics control how much the cloud "breathes." Ride **Clean's Attack** by hand to speed/slow the Leslie flutter mid-phrase, or roll the guitar/keys volume to fade the whole animated cloud in like a swell. On keys, hold a pad and let the three modulators (CE-2W chorus, Clean EQ/MOTION, Big Time Sine) beat against each other for a slowly-evolving organ wash. For a thicker climax, nudge Big Time FEEDBACK up toward 60% so the rhythmic echoes start to overlap into a continuous shimmer wall.

## Sources

- Basis: 🟣 designed integration; chains CE-2W "Dreamy Ambient (Slow Oceanic Bed)" + Clean "Double Tremolo (Motion + Modulated EQ + Spread)" + Big Time "Harmonic-Trem Cloud Catcher" (new). Clean-before-delay rationale (animate the source first) and the Modulated-EQ = harmonic tremolo / stereo-Leslie behavior are documented in the Clean patch sources (BachelorMachines, Bass Fox, Devin Belanger). Big Time Short + MOTION Sine + SPREAD-widen + Digital-no-limiter mechanics per the Big Time factory/transcript sources (Mark Johnston deep-dive). CE-2W slow/deep CE-1 wash per the CE-2W patch sources.
- Honesty flag: no published knob numbers exist for the Clean patch or the new Big Time patch — both are presented as dialable recipes, set by ear/LED.
