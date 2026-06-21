---
type: patch
title: MOD Metallic Resonator
device: Chase Bliss Big Time
date: 2026-06-19
description: "A pitched, metallic Karplus-style resonator built from a very short MOD feedback delay line — MODE Mod at the short end, high FEEDBACK, SCALE Chromatic/Octave so the resonance lands on notes. This is a MANUAL-LISTED MOD use: 'resonators' is named once in the entire manual, under MOD (3–46 ms). Dialed by physics — a short feedback delay is a comb/Karplus resonator with peaks near 1/delay-time, so resonator pitch = TIME, ring = FEEDBACK, movement = MOTION. Honest residual: at 3–46 ms the resonance sits low/bass-heavy (~22–333 Hz) and self-oscillates easily (the analog limiter sustains runaway into a ring rather than a digital scream)."
tags: [mod, resonator, karplus, comb-filter, metallic, pitched, feedback, designed]
controls:
  - { name: "Slot/Bank", type: knob, value: "Save to a free internal slot (10 internal / 127 via MIDI); recall flies the faders to saved positions" }
  - { name: "MODE", type: switch, value: "Mod (3–46 ms — at the SHORT end the feedback delay line acts as a comb/Karplus resonator; this IS the patch)", options: ["Mod", "Short", "Long", "Loop"] }
  - { name: "STATE", type: switch, value: "Digital (clean, stable feedback — keeps the resonant pitch legible) or Saturated for a metallic, biting ring", options: ["Digital", "Compressed", "Saturated", "#!&% (misbias)"] }
  - { name: "VOICING", type: switch, value: "HiFi (flat — most defined resonance) or Focus for a band-passed metallic peak", options: ["HiFi", "Focus", "Warm", "Analog"] }
  - { name: "SCALE", type: switch, value: "Chromatic or Octave (quantize the resonance so it lands on usable notes — this is what makes it a pitched resonator rather than an arbitrary comb tone)", options: ["Off", "Chromatic", "Oct+4+5", "Octave"] }
  - { name: "MOTION", type: switch, value: "Off (static resonance) or slow Sine for a shimmering, detuned metallic ring", options: ["Off", "Sine", "Square", "Env"] }
  - { name: "COLOR", type: knob, value: "low–moderate ~30% (keep the resonance clean; high COLOR slams the limiter and clamps the ring)" }
  - { name: "TIME", type: knob, value: "VERY SHORT end of MOD (short delay = high resonant pitch; this knob is effectively the resonator pitch/comb-spacing control)" }
  - { name: "CLUSTER", type: knob, value: "low ~20% (thickener/widener in MOD — NOT a comb-tuning control; see Notes)" }
  - { name: "TILT EQ", type: knob, value: "above noon (lift the metallic upper peak so it reads; note TILT/lows govern feedback decay)" }
  - { name: "FEEDBACK", type: knob, value: "HIGH ~70–85% (long resonant ring/sustain; this is what turns the short delay into a pitched resonator)" }
  - { name: "WET", type: knob, value: "~45% (dry retained so plucks excite the resonator and read against it)" }
  - { name: "SPREAD", type: switch, value: "off or widen", options: ["off", "widen", "ping-pong"] }
  - { name: "MODE button (hold 2s)", type: button, value: "Panic reset → clean simple delay (use it — high FEEDBACK at short MOD can self-oscillate)" }
---

# MOD Metallic Resonator

## Concept
A short feedback delay line is, physically, a **comb / Karplus-Strong resonator**: it has spectral peaks near 1/delay-time, so at the **very short end of MOD** with **FEEDBACK high**, plucked input rings out as a pitched, metallic tone. **SCALE Chromatic/Octave** quantizes that resonance onto usable notes so it behaves like a tuned resonator rather than an arbitrary comb whistle. This is a **manual-listed MOD use** — "resonators" is named once in the entire manual, and it occurs under **MOD (3–46 ms)** ("useful for creating modulation, **resonators**, and doubling effects"). The recipe just dials that named use by physics: **resonator pitch = TIME** (delay length), **ring = FEEDBACK** (sustain), **movement = MOTION**. Closest existing neighbor is `mod-slap-comb-flange-double`, but that patch rides COLOR+FEEDBACK into a comb→flange *double* on a doubled source; this one is a pitched, SCALE-quantized resonator ring with FEEDBACK pushed for sustain.

## How to play it
1. Set **MODE Mod** and roll **TIME to the very short end** — this sets the resonant pitch / comb spacing.
2. Push **FEEDBACK high (~70–85%)** so the short delay rings out as a sustained, metallic resonance.
3. Turn **SCALE to Chromatic** (or **Octave**) so the resonance quantizes onto notes — now it tracks like a tuned resonator.
4. Keep **COLOR low–moderate (~30%)** so the analog limiter doesn't clamp the ring flat; **STATE Digital** keeps the pitch legible, or flip to **Saturated** for a more biting metallic ring.
5. Lift **TILT EQ above noon** so the metallic upper peak reads; remember TILT/lows govern feedback decay, so it doubles as a ring-length control.
6. Pluck staccato to excite the resonator; add a slow **MOTION Sine** for a shimmering, slightly-detuned ring.
7. **Watch for self-oscillation** — high FEEDBACK at short MOD can take off. Hold the **MODE button** (2 s) to panic-reset, or back FEEDBACK down.

## Notes
- ✅ MANUAL-LISTED MOD USE, dialed by physics. "Resonators" is named **once** in the entire manual, and it occurs under **MOD (3–46 ms)** ("useful for creating modulation, **resonators**, and doubling effects") — so MOD is the manual-named resonator mode and this is not an out-on-a-limb inference. The physics then dials it: a short feedback delay = comb/Karplus resonator with peaks near 1/delay-time, so **pitch = TIME, ring = FEEDBACK, movement = MOTION.** What is NOT a MOD recipe: the often-quoted "Turn up CLUSTER" and "Set TIME very low" are actually the adjacent **SHORT-mode** callouts, not MOD — do not cite them here. The manual's literal MOD-mode callouts are only "Turn on MOTION" and "Crank FEEDBACK." (The remaining honest residual is tonal, not evidentiary — see the low-tone/self-oscillation notes below.)
- **CLUSTER is NOT a comb-tuning / resonator-depth control in MOD.** The manual scopes CLUSTER in MOD to a **thickener, stereo-widener, and secondary modulation** — explicitly not a comb/metallic resonator. The earlier corpus framing of "raise CLUSTER to tune comb spacing as a Karplus depth control" was REFUTED; do not use CLUSTER that way here. The resonator pitch comes from **TIME (delay length)**; FEEDBACK sets the ring length.
- **STEP is non-functional in MOD mode** (verified): no footswitch sequence-stepping — TAP LEFT toggles MOTION on/off instead. (STEP is likewise dead in LOOP.)
- **Honest residual — the tone sits LOW.** At MOD's 3–46 ms the comb fundamentals run only ~22–333 Hz (at the 3 ms minimum the fundamental is ~333 Hz; longer delays drop lower), so the resonance is **low and bass-heavy**, not a clean high tunable comb — expect a thick, growling ring rather than a glassy bell. Lift TILT and use SCALE/VOICING to pull a usable metallic peak out of it.
- **Self-oscillation is real and per-channel** — the analog limiter lives in the feedback loop, so pushing FEEDBACK with Saturated turns runaway into a sustained musical ring rather than a digital scream; TILT steers its weight; hold MODE ~2 s to panic-reset. (SATURATED is the manual's **default** destruction STATE, so the biting-ring variant is reachable without going all the way to misbias.)
- ⚠️ HONEST: every clock-face position (TIME / FEEDBACK / COLOR / TILT / WET / CLUSTER) is a dialable DOUG recipe, not published Chase Bliss numerics. On recall the motorized faders fly to saved positions and override these starting points.

## Sources
- 🟣 DOUG-designed patch realizing a **manual-listed MOD use** ("resonators" named under MOD), dialed by physics (pitch = TIME, ring = FEEDBACK, movement = MOTION). Numeric fader positions remain a dialable recipe (designed starting points), flagged as such — the motorized faders override on recall.
- `research/bloops/2026-06-19-chase-bliss-big-time-l2.md` (L2 — Lens: MOD resonator; Suggested corpus edits): upgrade framing from "exploratory/provisional" to "manual-listed MOD use — 'resonators' named once in the entire manual, under MOD (3–46 ms), dialed by physics: pitch = TIME, ring = FEEDBACK, movement = MOTION." This was the finding the L2 verifier most tried to refute and could not (positional glyph-extraction against a byte-identical official re-download).
- `research/bloops/2026-06-19-chase-bliss-big-time-l2.md` (L2 — Lens: MOD resonator): manual's literal MOD callouts are only "Turn on MOTION" and "Crank FEEDBACK"; "Turn up CLUSTER" + "Set TIME very low" are the adjacent **SHORT-mode** callouts (x-position confirmed), NOT MOD. **CLUSTER in MOD is a thickener / stereo-widener / secondary-modulation, NOT a comb-tuner** (verbatim) — the "raise CLUSTER to tune comb spacing as a Karplus depth control" framing stays REFUTED. Honest residual: at 3–46 ms the fundamentals run ~22–333 Hz, so the resonance sits low/bass-heavy and is prone to self-oscillation (the analog limiter sustains it); SATURATED is the manual's default destruction STATE.
- STEP non-functional in MOD and LOOP; self-oscillation via limiter-in-feedback-loop; TILT-EQ-in-loop as feedback governor: `research/bloops/2026-06-19-chase-bliss-big-time.md` (candidate index chunks; Lens: combinations).
- Distinctness checked against `Patches/Chase Bliss Big Time/mod-slap-comb-flange-double.md` (MOD comb→flange double on a doubled source; this patch is a SCALE-quantized pitched resonator ring).
