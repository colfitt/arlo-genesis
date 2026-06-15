---
type: chain
title: Big Time Nostalgic Repeater Frippertronics
date: 2026-06-15
artists: [Robert Fripp, Brian Eno]
instrument: guitar / synth
gear:
  - Chase Bliss Big Time
---

# Big Time Nostalgic Repeater Frippertronics ⭐

One pedal, no dry signal, no song-looper — just the Big Time set up as a *performative* sound-on-sound loop that crumbles as it grows. Hold a chord, let it commit to the loop, and every new pass carves an old one away while the analog grit and the Warm/Analog filter quietly destroy what's already in there. It's a cozy, quivering Frippertronics bed that's always degrading — the loop never sounds the same twice, and that's the point.

🟣 DOUG-designed integration. Robert Fripp / Brian Eno are the *taste-ref* (the original two-Revox "Frippertronics" sound-on-sound); this chain reproduces that decaying-loop aesthetic on one Big Time, not their literal rig. Per-unit patch refs carry their own provenance.

## Signal path

guitar / synth → **CB Big Time — "Nostalgic Repeater"** (foundation voice, DRY KILL ON, wet-only) → out (mono or stereo).

That's the whole chain. The Big Time IS the looper here. For the live performance — actually overdubbing and carving the loop in real time — switch the same pedal into Loop mode with **CB Big Time — "Frippertronics Carve Loop"** (the purpose-built Loop-mode recipe below). Both live on one pedal; pick the patch for what the moment needs:

- **"Nostalgic Repeater"** = sit-back, self-degrading repeats that crumble around held notes (factory #8, the on-aesthetic starting point).
- **"Frippertronics Carve Loop"** = you drive it — record a phrase, overdub passes, and let Warm/Analog sound-on-sound eat the old layers as new ones pile on.

## Per-unit

- **CB Big Time — "Nostalgic Repeater"** — Factory #8, recalled with **PC 8**. Comes pre-configured **DRY KILL ON** (pure wet, no dry print), VOICING **Warm**, STATE **#!&% (misbias) / Saturated**, MODE **Long (or Loop)**, FEEDBACK high (~70%), COLOR ~40%, CLUSTER ~30%, SPREAD widen. This is Chase Bliss's own "cozy looping delay that crumbles and quivers, with no dry signal" — the wet-only Frippertronics foundation, on-aesthetic out of the box. Use this when you want the crumble *without* hands on the footswitches.

- **CB Big Time — "Frippertronics Carve Loop"** — the performance patch. MODE **Loop**, VOICING **Warm** (or **Analog** for a darker ~4k destroy), STATE **Saturated**, TIME toward **max** for the long lo-fi loop window (3+ min lo-fi; ~45 s if you back TIME to noon for more fidelity), COLOR ~40% and FEEDBACK high so each pass stays loud enough to keep carving, DRY KILL **ON**, SPREAD widen. LEFT footswitch records / plays the loop; overdub passes layer on top. **Honesty note:** Loop mode runs *digital* feedback behind the scenes (manual p.29) — so the STATE limiter character doesn't bite the way it does in Long/Short. The "slow destroy" here comes from **VOICING Warm/Analog = sound-on-sound degrade** (UsageGuide §1: "Warm/Analog = sound-on-sound degrade"), not from the Saturated limiter. That's why VOICING is the destroy knob in this patch, and STATE is mostly cosmetic until you re-overdub.

## Routing

Single pedal, so gain-staging is internal. The whole pedal is loudness-driven — COLOR (preamp in) → FEEDBACK (loudness inside the loop) → WET (out) are interconnected (manual p.10). Set **WET carefully** — wet-only with DRY KILL means the loop *is* your entire output level, and high FEEDBACK climbs. Keep COLOR modest (~40%): you want the loop to degrade via the Warm/Analog filter and the sound-on-sound passes, not slam into clipping on every repeat.

**DRY KILL ON** (Options menu — double-tap both footswitches) is the keystone: it strips the dry so you get pure wet-only Frippertronics with no clean signal poking through, exactly the no-dry character the concept calls for. If you're feeding a downstream amp/board and want the loop to sit *under* a live dry, you'd flip DRY KILL off — but the wet-only print is the intended sound here.

No MIDI clock needed — this is a free-running, performative loop, not a tempo-synced delay. If you later want the carve to lock to a rig tempo, slave Big Time to the master clock (CB-stack MIDI), but for solo Frippertronics, free-run it.

## Sound

A cozy, crumbling, quivering sound-on-sound loop with no dry signal — degrading Frippertronics layers that carve old passes away as new ones pile on. The loop never resolves and never repeats cleanly; it slowly turns into a warm, lo-fi haze of its own past.

**Taste-ref:** Robert Fripp & Brian Eno — *(No Pussyfooting)* / *Evening Star* Frippertronics (the two-Revox sound-on-sound decaying loop), and Eno's *Discreet Music* tape-delay system. The aesthetic at its most minimal: one source, one loop, slow inevitable decay.

## Play

1. Recall **PC 8 ("Nostalgic Repeater")** to set the wet-only crumbling voice — or load **"Frippertronics Carve Loop"** and switch MODE to **Loop** to drive it by hand.
2. Hold a chord or sustained note and let it commit to the loop.
3. In Loop mode, **tap LEFT to record/play**; lay successive overdub passes on top.
4. Let it ride — Warm/Analog VOICING means each pass is darker and more degraded than the last, so the bed slowly eats itself even as you add to it.
5. Play melody/voicings *over* the decaying bed; the wet-only print keeps your live playing clean against the crumble.
6. To collapse, delete the loop (RIGHT footswitch behavior in Loop mode) or **hold MODE ~2 s to panic-reset** to a simple delay.

## Sources

- **Basis:** designed integration on one pedal; reuses **CB Big Time — "Nostalgic Repeater"** (factory #8) and a new purpose-built **CB Big Time — "Frippertronics Carve Loop"**.
- Factory #8 intent ("cozy looping delay that crumbles and quivers, with no dry signal... Frippertronics looping") quoted verbatim from `gear/Chase Bliss Big Time/research/links/cb-big-time-factory-presets-recipes.md` (🟢 factory intent).
- Loop-mode mechanics: `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` line 71 (looper as "performative phrase-freeze," variable-length up to 3.2 min), line 122 (Loop mode = digital feedback behind the scenes, manual p.29), §footswitches (per-mode record/play/delete).
- "Warm/Analog = sound-on-sound degrade" + looper fidelity vs. TIME: `gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md` §1 (line 58).
- DRY KILL in Options menu: `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` line 36, line 62.
- Taste-ref: Fripp/Eno Frippertronics is a making-aesthetic reference, not a sourced rig.
