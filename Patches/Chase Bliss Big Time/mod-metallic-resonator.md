---
type: patch
title: MOD Metallic Resonator
device: Chase Bliss Big Time
date: 2026-06-19
description: "A pitched, metallic Karplus-style resonator built from a very short MOD feedback delay line — MODE Mod at the short end, high FEEDBACK, SCALE Chromatic/Octave so the resonance lands on notes. The physics is sound (a short feedback delay is a comb/Karplus resonator with peaks near 1/delay-time, and the manual does list 'resonators' as a MOD-mode use), but this is framed as a DIALABLE INFERENCE, not a quoted first-party recipe — the manual's literal MOD callouts are only 'Turn on MOTION' and 'Crank FEEDBACK'. Provisional/exploratory."
tags: [mod, resonator, karplus, comb-filter, metallic, pitched, feedback, designed, provisional]
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
A short feedback delay line is, physically, a **comb / Karplus-Strong resonator**: it has spectral peaks near 1/delay-time, so at the **very short end of MOD** with **FEEDBACK high**, plucked input rings out as a pitched, metallic tone. **SCALE Chromatic/Octave** quantizes that resonance onto usable notes so it behaves like a tuned resonator rather than an arbitrary comb whistle. The manual does list "resonators" among MOD-mode uses, and the MOD callouts include "Crank FEEDBACK" — so this recipe is *defensible physics*, but it is offered as a **dialable inference**, not a quoted first-party recipe (see the honesty flag below). Closest existing neighbor is `mod-slap-comb-flange-double`, but that patch rides COLOR+FEEDBACK into a comb→flange *double* on a doubled source; this one is a pitched, SCALE-quantized resonator ring with FEEDBACK pushed for sustain.

## How to play it
1. Set **MODE Mod** and roll **TIME to the very short end** — this sets the resonant pitch / comb spacing.
2. Push **FEEDBACK high (~70–85%)** so the short delay rings out as a sustained, metallic resonance.
3. Turn **SCALE to Chromatic** (or **Octave**) so the resonance quantizes onto notes — now it tracks like a tuned resonator.
4. Keep **COLOR low–moderate (~30%)** so the analog limiter doesn't clamp the ring flat; **STATE Digital** keeps the pitch legible, or flip to **Saturated** for a more biting metallic ring.
5. Lift **TILT EQ above noon** so the metallic upper peak reads; remember TILT/lows govern feedback decay, so it doubles as a ring-length control.
6. Pluck staccato to excite the resonator; add a slow **MOTION Sine** for a shimmering, slightly-detuned ring.
7. **Watch for self-oscillation** — high FEEDBACK at short MOD can take off. Hold the **MODE button** (2 s) to panic-reset, or back FEEDBACK down.

## Notes
- ⚠️ EXPLORATORY / PROVISIONAL — this is a **dialable inference, not a quoted first-party recipe.** The manual's literal MOD-mode callouts are only "Turn on MOTION" and "Crank FEEDBACK." The often-quoted "Turn up CLUSTER" and "Set TIME very low" are actually the adjacent **SHORT-mode** callouts, not MOD — do not cite them as a MOD recipe. The *physics* (short feedback delay = comb/Karplus resonator with peaks near 1/delay-time) is sound and the manual does list "resonators" as a MOD-mode use, which is why a pitched-resonator recipe is defensible **as an inference**.
- **CLUSTER is NOT a comb-tuning / resonator-depth control in MOD.** The manual scopes CLUSTER in MOD to a **thickener, stereo-widener, and secondary modulation** — explicitly not a comb/metallic resonator. The earlier corpus framing of "raise CLUSTER to tune comb spacing as a Karplus depth control" was REFUTED; do not use CLUSTER that way here. The resonator pitch comes from **TIME (delay length)**; FEEDBACK sets the ring length.
- **STEP is non-functional in MOD mode** (verified): no footswitch sequence-stepping — TAP LEFT toggles MOTION on/off instead. (STEP is likewise dead in LOOP.)
- **Self-oscillation is real and per-channel** — the analog limiter lives in the feedback loop, so pushing FEEDBACK with Saturated turns runaway into a sustained musical ring rather than a digital scream; TILT steers its weight; hold MODE ~2 s to panic-reset.
- ⚠️ HONEST: every clock-face position (TIME / FEEDBACK / COLOR / TILT / WET / CLUSTER) is a dialable DOUG recipe, not published Chase Bliss numerics. On recall the motorized faders fly to saved positions and override these starting points.

## Sources
- 🟣 DOUG-designed patch, offered as a DIALABLE INFERENCE (not a quoted first-party recipe), flagged as such throughout.
- `research/bloops/2026-06-19-chase-bliss-big-time.md` (Suggested corpus edits): "(c) optionally `mod-metallic-resonator` framed as a dialable inference, not a quoted manual recipe (MODE Mod short end, high FEEDBACK, SCALE Chromatic/Octave) — and note that STEP does not work in MOD or LOOP."
- `research/bloops/2026-06-19-chase-bliss-big-time.md` (Flagged / uncertain): manual's MOD callouts are only "Turn on MOTION" and "Crank FEEDBACK"; "Turn up CLUSTER" + "Set TIME very low" are SHORT-mode callouts; the physics (short feedback delay = comb/Karplus resonator, peaks near 1/delay-time) is sound and the manual lists "resonators" as a MOD-mode use → recipe defensible only as an inference. Also: the "CLUSTER in MOD = comb/metallic resonator / raise CLUSTER to tune comb spacing" framing was REFUTED — CLUSTER in MOD is a thickener/widener/secondary-modulation.
- STEP non-functional in MOD and LOOP; self-oscillation via limiter-in-feedback-loop; TILT-EQ-in-loop as feedback governor: `research/bloops/2026-06-19-chase-bliss-big-time.md` (candidate index chunks; Lens: combinations).
- Distinctness checked against `Patches/Chase Bliss Big Time/mod-slap-comb-flange-double.md` (MOD comb→flange double on a doubled source; this patch is a SCALE-quantized pitched resonator ring).
