---
type: chain
title: "Microcosm → Big Time Misbias Cluster Swirl"
date: 2026-06-15
artists: []
instrument: guitar / synth
gear:
  - Hologram Microcosm
  - Chase Bliss Big Time
---

# Microcosm → Big Time Misbias Cluster Swirl ⭐

Two granular engines stacked into a single dynamics-played wash: Microcosm spits a dense field of pitched grains, Big Time catches that field on its misbias CLUSTER engine and smears it into a swirling, sagging cloud. Soft playing stays mostly clean and intact; dig in and the misbias drops out under the attack so the wall crackles, sags, and crumbles before re-forming. A broken, drifting, lively soundscape you steer with your right hand — William-Basinski decay you trigger by touch.

🟣 DOUG-designed integration. No artist used this exact pair — the per-unit patch refs carry their own provenance, and the Sound section names the taste-ref it chases. Big Time knob values below are a **designed/dialable recipe** (Chase Bliss publishes character, not numbers), as is the new Microcosm feeder patch.

## Signal path

guitar / synth → **Hologram Microcosm — "Grain Cluster Feeder"** (granular grains, dryish — Mix back so the grains feed forward, not a finished wash) → **CB Big Time — "Cluster$%&!"** (STATE `#!&%` misbias, high CLUSTER, DIFFUSE on/high; gentle = clean, dig in = crumble) → amp / interface (stereo).

The whole move is granular-INTO-granular done *on purpose*: keep Microcosm relatively dry so it acts as a grain source rather than a reverb, then let Big Time's CLUSTER + DIFFUSE be the only true wash. Stack two wet diffusers and you get porridge — so one of them stays a generator.

## Per-unit

- **Hologram Microcosm — "Grain Cluster Feeder"** (NEW patch): a grain engine in the Granules family (Strum B onset-chains, or Haze B many-randomized-grains) generating discrete pitched grains rather than a glassy bed. **Activity high** (grain density is the texture you hand to Big Time), **Time / Repeats moderate** (fast Time = choppier grains; not infinite), **Shape = a slower envelope so grains have body**, **Filter ~noon** (tame the granular top before two stages of diffusion), **Space LOW**, **Mix ~10:00–11:00** — well under wet so the grain field stays forward and dynamic. Optionally arm **Reverse** for a smeared, backward grain feed. Keep it dryish: this pedal makes the *grains*, Big Time makes the *swirl*.
- **CB Big Time — "Cluster$%&!"** (REUSE — Factory #6, recall PC 6): MODE **Long**, STATE **`#!&%` (misbias)** — the playing-reactive sag is the entire point; VOICING **Warm or Analog**, MOTION **Sine**, **CLUSTER high ~75%** (the swirl), **DIFFUSE high + DIFFUSE TYPE on**, **COLOR low ~35%** (low so digging in is what breaks it up — don't pre-cook it), FEEDBACK ~60%, TILT EQ ~noon, **WET careful ~45%**, SPREAD **widen → ping-pong** to scatter the grains across the stereo field. Per the patch's own note: start sparse and see where it takes you.

## Routing

Mono guitar/synth in. Microcosm's grain engines generate genuine stereo, but to keep the chain clean run **Microcosm mono out → Big Time IN-L**, which auto-engages **MISO** (mono-in / stereo-out) so Big Time owns the stereo image — its SPREAD ping-pong then throws the misbias clusters L/R rather than fighting Microcosm's own stereo. If you'd rather hear Microcosm's stereo grains too, take Microcosm stereo → Big Time IN-L/IN-R, but expect a busier, less-defined field.

**Gain-staging is the whole game.** Big Time's misbias STATE is level- and dynamics-reactive: a hot, dense grain field will trigger the sag/dropout constantly (always-crumbling), while a quieter feed lets soft passages stay clean and only big hits break it. So **set Microcosm Mix and your pick attack as the trigger control** — back Microcosm Mix down until soft playing rides clean through Big Time, then dig in to cross the misbias threshold on demand. Keep Big Time **COLOR low** so it's your *attack*, not a high COLOR setting, doing the crumbling. Don't stack a downstream reverb — DIFFUSE here is already the wash.

## Sound

A misbiased wash of swirling granular clusters that crackles and sags as you dig in, then re-forms when you ease off — a broken, drifting, lively soundscape that never sits still. Soft = a clean-ish granular shimmer; hard = a collapsing, recorded-wrong cloud.

**Taste-ref:** William Basinski *Disintegration Loops* decay — but triggered by touch rather than by tape rot; the "punch-in-clean-then-destroy" gesture made playable. Adjacent to the drone/doom granular-wall aesthetic at its most lively/unstable.

## Play

1. Recall Big Time **PC 6** (faders fly to the Cluster$%&! positions); set Microcosm to the Grain Cluster Feeder, **Mix backed off**.
2. Play **sparse and soft** — grains feed Big Time, the misbias holds together, you get a clean-ish swirling shimmer.
3. **Dig in / hit a big chord** to cross the misbias threshold: Big Time sags and drops out under the attack, the cluster wash crackles and crumbles, then re-forms as you back off — Basinski decay on command.
4. Ride **Microcosm Activity** for more/less grain density live, and **Big Time CLUSTER** (or expression on COLOR/FEEDBACK) to push the swirl deeper.
5. To reset if it runs away, **hold Big Time MODE** to panic back to a clean delay.

## Sources

- **Basis:** designed integration; chains **CB Big Time — "Cluster$%&!"** (Factory #6, `Patches/Chase Bliss Big Time/cluster.md`) with a new **Hologram Microcosm — "Grain Cluster Feeder"** patch. Misbias playing-reactivity (gentle = clean, dig in = texture; sag-return) from `gear/Chase Bliss Big Time/research/transcripts/sonicstate-superbooth-john-snyder-eae-interview.md`; factory #6 intent ("misbiased wash of swirling clusters – start with sparse playing") from `gear/Chase Bliss Big Time/research/links/cb-big-time-factory-presets-recipes.md`.
- Microcosm control semantics (Activity = grain density/spread; Granules = Haze/Strum; Mix/Space = blend; engines generate genuine stereo) from `gear/Hologram Microcosm/research/Microcosm-UsageGuide.md` and `gear/Hologram Microcosm/research/Microcosm-DeepResearch.md`. Granular-into-granular mud caution adapted from the Haze-smear patches' "don't double-granulate" note.
- Taste-ref: William Basinski *Disintegration Loops* (touch-triggered decay).
