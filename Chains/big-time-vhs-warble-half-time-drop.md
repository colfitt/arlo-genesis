---
type: chain
title: "Big Time VHS Warble → Half-Time Drop"
date: 2026-06-15
artists: [Boards of Canada, Tim Hecker]
instrument: guitar / synth
gear:
  - Chase Bliss Lost & Found
  - Chase Bliss Big Time
---

# Big Time VHS Warble → Half-Time Drop

A clean, modulated stereo delay that holds its composure — VHS tape warble lapping at the edges — until you stomp the floor switch and the **whole delay engine drops to half sample rate in real time**: bandwidth halves, delay time doubles, the repeats sag a full octave-ish down in pitch, and the warble that was decorative suddenly drags the whole thing into a lo-fi collapse. One footswitch, one gesture, live. The clean version and the crushed version are the *same patch* — the only thing that changes is the AUX switch.

This is a 🟣 DOUG-designed integration. No artist played this exact two-pedal chain — but the gesture is native to the box: Big Time's **AUX-in "Fun mode" (LEFT = 0.5X half-time drop)** is a documented hardware feature, and dropping to 0.5X mid-performance is exactly the "built-in 12-bit generation-loss" move the pedal was designed to perform. What's new is using it as a *live arrangement drop* with a tape pedal already warbling in front, so the collapse compounds instead of just crushing.

## Signal path

guitar / synth → **CB Lost & Found — "Gen Lite Tape Warble (Single-Slot, Full Wet)"** (6B Gen Lite, single channel, MIX FULL, slow wow) → **CB Big Time — "Half-Time Drop Delay (Clean Base + AUX 0.5X)"** (Digital/clean STATE, subtle Sine MOTION, AUX floor switch → LEFT = live 0.5X half-time drop) → amp / interface (stereo)

External AUX floor footswitch plugged into Big Time's AUX-in jack: **LEFT = 0.5X half-time drop, RIGHT = clear buffer.** That left switch *is* the performance.

## Per-unit

- **CB Lost & Found — "Gen Lite Tape Warble (Single-Slot, Full Wet)":** R slot = **6B Gen Lite** (a mini Generation Loss MkII) run as a *single channel* so it reads as believable tape, not per-side chorus. TIME pushed toward MAX = **slow wow** (the seasick VHS pitch-warp); MODIFY ~12:00–1:00 sets the warble depth; ALT (Gen Lite failure / crinkles) ~10:00–11:00 for tape crinkle; BLEND toward Gen Lite ~1:00–2:00 sets the degrade amount; **MIX FULL** — Gen Lite wants full wet to read as real tape. **SPREAD OFF**, TRAILS on. Crucially this is *not* the "Light Sleeper" combo — there's **no Orchestral Swell stage here**, because the concept wants the warble to age *what you actually play* (a played, clean, modulated source), not to remove the pick attack and turn it into a pad. This is the **tape voice** of the chain; it does the wow + crinkle so Big Time can stay clean until the drop.
- **CB Big Time — "Half-Time Drop Delay (Clean Base + AUX 0.5X)":** MODE **Long** (so the half-time drop has room to double the time without running into the ceiling — Long is 736 ms–12.2 s, and ~24 s with 0.5X), STATE **Digital** (limiter fully out of the way → clean, stable repeats; the lo-fi comes from the *drop*, not from baked-in saturation), VOICING **HiFi or Focus** (open and clean in the up-state so the collapse to lo-fi is dramatic; Focus if you want a touch of body), **MOTION Sine, subtle** (the gentle modulated-delay shimmer the concept calls "clean modulated"), **0.5X OFF in the saved state** — it lives on the AUX switch, *not* baked into the patch. COLOR low ~25–30% and FEEDBACK ~35–45% so the clean version is a tidy 2–4-repeat delay, not a wall. TILT EQ at noon. **AUX-in floor switch armed: LEFT = 0.5X half-time drop.** When you stomp it, the engine halves its sample rate live: bandwidth halves (instant lo-fi darkening), delay time doubles (the repeats stretch and sag long), and the running buffer pitches down. The created sheet flags every numeric position as a dialable recipe — Chase Bliss publishes character, not numbers, and on recall the motorized faders override anything written.

## Routing

Straight series, stereo-capable, mono-in is fine (IN-L auto-engages MISO → stereo out). **The whole game is keeping Big Time genuinely clean in the up-state so the drop has somewhere to fall:**

1. **Lost & Found ages the source, lightly and continuously.** Gen Lite at full wet supplies an ever-present wow + crinkle. Because Gen Lite *is* a mini Generation Loss, you do **not** also run a full Generation Loss in front — that's GenLoss-on-GenLoss mud. Keep BLEND modest enough that the up-state still reads as "clean modulated delay with tape character," not "already destroyed."
2. **Big Time stays clean until the stomp.** Digital STATE + HiFi/Focus + low COLOR means the repeats are tidy and full-bandwidth. This is deliberate restraint: if you bake in Saturated + 0.5X (the "Crushed Analog" approach), there's no *drop* left to perform — the contrast is the point.
3. **The AUX LEFT switch is the arrangement move.** Hitting 0.5X live takes the clean, warbled delay and collapses it: half the sample rate, double the time, pitch sag, 12-bit crush. The Gen Lite warble that was decorative now warbles a half-rate, lo-fi signal — the collapse compounds. Stomp again to come back up to the clean delay. **RIGHT on the AUX switch clears the buffer** if a long sagging tail won't get out of the way.

Gain-staging note: because Big Time runs Digital (no limiter) in the up-state, watch level into your interface when you drop to 0.5X — the doubled-time repeats can pile up. Pull FEEDBACK down before COLOR if it gets cluttered. If you want the wet kept out of the printed dry for a parallel/aux send, flip **DRY KILL ON** in Options — but in this two-pedal box the dry-retained series path is the intended sound. Hold Big Time's center **MODE button** for the panic-reset to a clean simple delay if a half-time tail runs away.

## Sound

In the up-state: a clean, gently modulated stereo delay with VHS tape warble breathing through the repeats — pretty, slightly seasick, composed. Then, on the footswitch: the floor drops out. Bandwidth halves into a dark lo-fi haze, the repeats stretch to double-length and sag down in pitch, and the tape wow drags across a 12-bit-crushed signal. It's the sound of someone yanking the tape speed to half mid-take. Taste-ref: Boards of Canada's wow-warped tape nostalgia for the up-state, collapsing into Tim Hecker-style degraded, pitch-dropped haze on the drop.

## Play

Play a sustained chord, an arpeggio, or a slow synth line and let the clean modulated delay repeat it with the Gen Lite warble lapping underneath. Find the moment — a section change, a held chord, the top of a build's release — and **stomp the AUX LEFT footswitch**: the whole thing drops to half-time. Time doubles, pitch dips, bandwidth collapses, and the warble that was decorative now drags the half-rate signal into lo-fi. Hold the dropped state through the section, then stomp again to snap back up to the clean delay. For a deeper sag, push Big Time to a longer TIME before you drop (the 0.5X doubling stretches it further); for more obvious tape character on the way down, nudge the Gen Lite BLEND up first. Use the AUX **RIGHT** switch to clear a tail that won't let go, and **hold MODE** as the panic-reset back to a clean delay.

## Sources

- **Basis:** 🟣 DOUG-designed integration; chains **CB Lost & Found — "Gen Lite Tape Warble (Single-Slot, Full Wet)"** (created) → **CB Big Time — "Half-Time Drop Delay (Clean Base + AUX 0.5X)"** (created). The headline gesture is real hardware: Big Time **AUX-in "Fun mode": LEFT = 0.5X half-time drop, RIGHT = clear buffer** — documented in `gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md` §3 (sourced to video / modwiggler).
- **0.5X mechanics** (halves sample rate, doubles max delay time → ~24 s in Long, adds 12-bit generation-loss reduction) from `Big-Time-UsageGuide.md` §1 (Modes/0.5X; superbooth-snyder, video). MODE/STATE/VOICING ranges (Long 736 ms–12.2 s; Digital = no limiter / clean; VOICING filter slopes) from the same guide.
- **Gen Lite full-wet, SPREAD-off-for-real-tape, slow-wow** recipe from the Lost & Found patch maps (BachelorMachinesTV Pt1/Pt2), via `Patches/Chase Bliss Lost & Found/light-sleeper-recorded-wrong-vhs-swell.md` — but stripped of the Orchestral Swell stage so the warble ages a played source, not a swell.
- **GenLoss-on-GenLoss-mud avoidance** and COLOR-modest-after-degrade gain-staging precedent: `Chains/lost-found-big-time-stacked-tape-degradation.md`.
- **Note:** all numeric knob/fader positions in both created patches are a **dialable recipe** (DOUG's interpretation) — Chase Bliss publishes character, not numbers, and on preset recall Big Time's motorized faders override anything written. The AUX Fun-mode behavior itself is sourced, not invented.
- `Research/Taste-Profile/taste-profile.md` (Boards of Canada / degraded lo-fi tape aesthetic).
