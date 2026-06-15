---
type: chain
title: "Hizumitas → Big Time Synth-Filter Tone Suite"
date: 2026-06-15
artists: [Boris, Radiohead]
instrument: baritone / banjo drone (single sustained chord)
gear:
  - EarthQuaker Devices Hizumitas
  - Chase Bliss Big Time
  - Eventide H90
---

# Hizumitas → Big Time Synth-Filter Tone Suite ⭐

The headline Hizumitas technique turned into a *performance gesture*. Hold one baritone/banjo drone through the Hizumitas wall, then physically sweep the **Tone** knob through the note's decay so the fuzz behaves like a synth filter — the wall burns and changes shape as it rings, fat → dark → mid-forward — and Big Time + H90 multiply that morphing wall into stereo time and a mangled hall. The sweep is the song. Everything downstream exists to bloom what the right hand is doing on the Tone knob.

🟣 DOUG-designed integration. No artist played this exact chain — the per-unit patch refs carry their own provenance, and the Taste-ref names the sound it chases (Premier Guitar's documented "Tone-as-synth-filter on sustained notes" technique, Boris/Wata sustaining-wall weight, Radiohead-adjacent textural decay).

## Signal path

baritone / banjo (single sustained chord) → **EQD Hizumitas — "Synth-Filter Decay Sweep"** (mono; right hand rides the Tone knob through the decay) → **CB Big Time — "Cluster$%&!"** (IN-L, auto-MISO mono→stereo; MODE Long, CLUSTER high) → **Eventide H90 — "MangledVerb — Doom Reverb-into-Drive"** (reverb-into-drive hall, body only) → tape.

The only "real signal order" invoked is the general **fuzz-before-delay-before-reverb** standard (documented pedal-order best-practice), not an artist-specific path. The expressive event happens at the *front* of the chain — on the Hizumitas Tone knob — and everything after it is a multiplier.

## Per-unit

- **EQD Hizumitas — "Synth-Filter Decay Sweep"** — Volume 11:00, Sustain 12:00, **Tone START at 1:00 (fat), then physically SWEEP CW→CCW through the note's decay.** This is a live gesture, not a fixed value — the load-bearing move of the whole chain. As the note rings, sweeping the Tone toward CCW closes the voicing like a lowpass filter sweeping down through an envelope (the "inverted Tone through decay" gesture: bright/fat on attack, darker as it decays). Needs amp/monitor volume so the sustain bloom arrives and the chord never dies before you finish the sweep. *(Honesty: the START values are a designed recipe; the documented signature is the sweep itself — "use the tone knob as an almost synth-like filter control on sustained notes," Premier Guitar.)*
- **CB Big Time — "Cluster$%&!"** *(factory #6)* — MODE **Long**, STATE **#!&% (misbias)**, VOICING **Warm/Analog**, **COLOR ~35%** (low — the fuzz already supplies all the saturation, so keep COLOR modest or the misbias limiter clamps a hot fuzz to porridge), TIME long, **CLUSTER ~75%** (the swirl — this is what smears each Tone position into a moving cloud so the sweep reads as a continuous morph, not stepped echoes), TILT EQ noon, FEEDBACK ~60%, WET ~45%, **SPREAD widen → ping-pong** (scatters the cluster across the stereo field). MOTION Sine adds slow movement under the swirl. Recall **PC 6**; faders fly to saved positions, then trim COLOR/WET by ear against the fuzz level.
- **Eventide H90 — "MangledVerb — Doom Reverb-into-Drive"** — MangledVerb on Preset A (Pre-Delay → Reverb → EQ → Distortion). Big **Size** for a cavernous mangled space; push **Distortion** just into the soft-clip region so the dirt chews the tail without burying the swept body; add a touch of **Wobble** for seasick detune so the hall slides under the moving wall; cut the **Low band** pre-distortion to keep the baritone bottom from turning to mud. Keep the wet contribution as *body*, not a second wall — it's the doom space the morphing cluster lives inside. *(Honesty: signal flow, the soft-clip→overdrive split, Wobble, band EQ and Size~15-for-distortion are sourced from the Eventide manual + Algorithm Guide; Distortion amount, Output Level, Wobble rate and Decay are a dial-by-ear recipe — no published numerics.)*

## Routing

Mono Hizumitas wall → **Big Time IN-L auto-engages MISO** (mono-in / stereo-out) — the clean way to fan one mono fuzz into a stereo cluster field; stereo from Big Time onward into the H90. No clock needed (free-running drone, not rhythmic).

**Gain-staging is the whole game.** The Hizumitas supplies all the saturation, so Big Time's job is *smear-and-spread*, not more dirt: CLUSTER high turns each Tone-knob position into a moving cloud, while COLOR stays modest so the misbias STATE adds character without clamping the hot fuzz to mush. Because CLUSTER blurs the boundaries between repeats, the discrete Tone sweep reads downstream as one continuous filter morph — that's the trick. The H90 MangledVerb then catches the whole moving wet field; keep its wet contribution as body so the reverb-into-drive is doom *space*, not competition for the wall. Favor **DRY KILL ON** on the Big Time if you want a pure morphing wet bed to print — the swept fuzz then exists only as its stereo cluster reflection, no dry note alongside it.

## Sound

A held drone whose voicing visibly *changes shape as it decays* — fat and bright on the attack, closing dark and mid-forward as the right hand sweeps the Tone, multiplied into a swirling stereo cluster and wrapped in a mangled, detuned hall. The wall burns down like an embers fade, and Big Time + H90 make that burn enormous and three-dimensional. Synth-filter-on-a-fuzz as a single expressive gesture.

**Taste-ref:** Premier Guitar's documented Hizumitas move — *"letting embers of drop-D riffs slowly burn and change shape as they decayed"* — scaled to a drone, with Boris/Wata sustaining-wall weight and Radiohead-adjacent textural decay.

## Play

1. Set the Hizumitas (Vol 11:00 / Sustain 12:00 / **Tone 1:00**) and let one baritone or banjo chord bloom to full sustain at amp volume.
2. As the note rings, **physically sweep the Tone knob CW→CCW** through the decay — slow and deliberate. The voicing morphs fat/bright → dark/mid-forward like a lowpass filter closing under an envelope. *This is the performance.*
3. Let Big Time's CLUSTER smear each Tone position into a moving cloud, ping-ponging across stereo, so the sweep reads as one continuous filter morph.
4. The MangledVerb hall catches the moving field and adds detuned doom space underneath.
5. Re-trigger and re-sweep for each phrase; vary the *speed* of the Tone sweep to vary how fast the wall changes shape. Panic-reset Big Time (hold MODE) if the misbias runs away.

## Sources

- **Basis:** designed integration; chains **EQD Hizumitas "Synth-Filter Decay Sweep"** + **CB Big Time "Cluster$%&!"** (factory #6) + **H90 "MangledVerb — Doom Reverb-into-Drive"**. The headline technique — Tone-knob-as-synth-filter on sustained notes — is sourced verbatim from Premier Guitar (*"use the tone knob as an almost synth-like filter control on sustained notes, letting embers of drop-D riffs slowly burn and change shape as they decayed"*) via `Patches/EarthQuaker Devices Hizumitas/synth-filter-decay-sweep.md` and `seven-string-drop-a-synth-filter.md`. Big Time CLUSTER/Long/misbias factory intent and COLOR-modest-against-hot-fuzz gain-staging from the Cluster$%&! patch (`research/links/cb-big-time-factory-presets-recipes.md`, SuperBooth Snyder interview) + fuzz-before-delay / MISO auto-engage from `research/links/centerpiece-minimal-chains-and-sampler-integration.md` §A. MangledVerb signal flow + Wobble + band EQ from the H90 patch (Eventide manual + Algorithm Guide).
- `Research/Taste-Profile/taste-profile.md` (morphing-wall / textural-decay thesis)
