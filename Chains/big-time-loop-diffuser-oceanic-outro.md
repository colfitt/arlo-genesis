---
type: chain
title: Big Time Loop Diffuser → Oceanic Outro
date: 2026-06-15
artists: []
instrument: guitar / synth pad
gear:
  - Chase Bliss Big Time
  - Strymon Big Sky
---

# Big Time Loop Diffuser → Oceanic Outro ⭐

Two pedals, one outro that plays itself. Big Time runs its factory **LOOP DIFFUSER** logic — low COLOR under high FEEDBACK so the echoes climb, with DIFFUSE and CLUSTER cranked until the delay stops being a delay and becomes its own slowly-dissolving reverb. Big Sky catches that saturated, climbing echo in a huge concert/arena **Hall** so the doom blooms into a believable oceanic space. Play a few notes, sit back, and the atmosphere builds itself.

🟣 DOUG-designed integration. No artist used this exact two-pedal chain — the per-unit patch refs carry their own provenance, and the Taste-ref names the sound it chases. The Big Time recipe is the documented factory #9 intent; the Big Sky Hall patch is dialable (see its note).

## Signal path

Guitar / synth pad → **CB Big Time — "Loop Diffuser"** (MODE Long · STATE Saturated · VOICING Analog · slow Sine MOTION · DIFFUSE + CLUSTER high · FEEDBACK above COLOR) → **Strymon Big Sky — "Oceanic Outro Hall"** (Hall machine, Arena size, long decay) → amp / tape.

Mono in works fine: feed only Big Time **IN-L** and it auto-engages **MISO** (mono-in / stereo-out), fanning the climbing loop into a stereo field that the Big Sky's stereo Hall then deepens. If your source is already stereo (synth pad), run full stereo in and out.

## Per-unit

- **CB Big Time — "Loop Diffuser"** — factory #9, recall **PC 9** and the motorized faders fly to it. MODE **Long**, STATE **Saturated** (or **#!&%** misbias for a rawer, more broken bloom — both are in the patch), VOICING **Analog**, MOTION slow **Sine**, SCALE **Off**. The gain structure is the whole trick: **COLOR ~30%** (low) sitting *under* **FEEDBACK ~80%** is the manual's documented "most change over time" setting — the echoes climb until they hit the internal limiter and transform into a sustaining wall (manual pp.24–25). **DIFFUSE ~75%** + **CLUSTER ~70%** smear the taps into haze so it reads as reverb, not slap-back. **TILT EQ** at noon-to-slightly-down feeds lows back into the loop for longer tails. **WET conservative — these get loud** (the manual warns twice about runaway). SPREAD **widen**. Hold the **RIGHT footswitch to FREEZE** the bed for a non-degrading infinite pad to solo over.

- **Strymon Big Sky — "Oceanic Outro Hall"** — the huge space the saturated echo blooms into. **Hall** machine, **Size = Arena** (the bigger of Concert/Arena), long decay (~10–15 s of the Hall's 500 mS–20 S range), MIX held back so it's depth-not-mush behind the already-thick Big Time wall, **Low End pulled below noon** (Big Time's looped lows are already heavy; cranked Hall Low End turns to porridge — the documented baritone/low-source caution), TONE up to keep the bloom open, light MOD. HOLD = FREEZE if you want to lock the room and change parts over it. Values are a **dialable recipe**, not a captured factory slot — see the patch note.

## Routing

Big Time first, Big Sky second — saturate and diffuse *before* the room, never the reverse, or the Hall just reverberates a dry note instead of the climbing wall. Gain-staging is the game: keep Big Time **COLOR modest under high FEEDBACK** so the loop climbs cleanly into its limiter rather than clamping to porridge, then let the Big Sky Hall add *space*, not more *level* — pull the Hall MIX back so it deepens rather than competes. Two ambient stages stack their low end fast: pull **Big Time TILT** toward noon-or-just-up and **Big Sky Low End below noon** so the doom bloom stays defined. For a pure wet outro, enable **DRY KILL** in Big Time's Options menu so only the wet repeats feed the Hall and the dry stays clean upstream (prevents double-preamp coloration). No clock needed — this is a free-running drone, not a rhythmic delay.

## Sound

A slowly dissolving infinite-feedback chord that blooms forever — a few notes climb into a saturated, diffused echo that the Hall opens into a huge oceanic space, building an atmosphere that never quite resolves. FREEZE either pedal and it becomes an endless bed to play melody over.

**Taste-ref:** ambient / drone-doom outros — the "delay-becomes-reverb-becomes-ocean" move; Chase Bliss's own Loop Diffuser demo aesthetic blown out into a cathedral.

## Play

Strike a few notes (or one held chord) and **stop playing** — the Loop Diffuser does the work, climbing and dissolving on its own. Let the wall build, then **hold Big Time's RIGHT footswitch to FREEZE** the bed and solo a line over the held ocean, or **HOLD = FREEZE on the Big Sky** to lock the room instead and ride Big Time's evolving loop inside it. To collapse the outro, tap RIGHT to unfreeze, or **hold MODE on Big Time to panic-reset** back to a clean delay.

## Sources

- **Basis:** DOUG-designed integration; chains **CB Big Time — "Loop Diffuser"** (factory #9) → **Strymon Big Sky — "Oceanic Outro Hall"** (new, dialable).
- Big Time recipe: low-COLOR / high-FEEDBACK "most change over time" climb + DIFFUSE/CLUSTER long-form ambient haze + MISO auto-engage + DRY KILL routing from `gear/Chase Bliss Big Time/research/Big-Time-DeepResearch.md` (manual pp.24–25, p.36, §5) and the Loop Diffuser patch's own factory-intent sources.
- Big Sky Hall: machine params (Low End, Mid, Size Concert/Arena; 500 mS–20 S decay) and Low-End caution for low sources from `gear/Strymon Big Sky/research/Big-Sky-DeepResearch.md` (machine table §; starting-point Hall (Concert) §13a; baritone Low-End note).
