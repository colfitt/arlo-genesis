(synthesized recipes — values derived from the official control ranges in room-controls-deep-dive.md + room-official-modes-taxonomy.md + the two transcripts; NOT one verbatim factory patch. Flagged synthesized per capture convention.)
Sources: Valhalla DSP blog control/mode posts · room-workhorse-parameter-walkthrough · room-late-section-crossover-decay · room-early-tricks-gated-space

# ValhallaRoom — copyable recipes for the drone/doom/shoegaze rig

All meant to run **100% wet on an aux/send** unless noted; EQ/saturate the return.
Dial order (workhorse method): **Mode → Early Size → Late Size → Decay → High Cut → Depth**, then fine-tune Mod + the 3-band decay mult.

## 1. Natural ambient space (the believable depth bed)
- Mode **Large Room** (stable pitch) · Depth **~70-80%** · Predelay **15-25 ms** · Decay **2-4 s** · Late Size ~25 · Early Size ~30 ms · Diffusion 1.0 · High Cut **5-7 kHz** · Lo Cut ~150 Hz · Mod low (0.3 Hz / low depth). The honest room you put everything in.

## 2. Lush "bloom" drone (slow swell, evolving)
- Mode **LV-426** (slow attack, dense, deep) or **Dark Space** · Depth **100%** · Predelay 0-20 ms · Decay **15-30 s** · Late Size **near max** · Early Size large + **Early Send ~1.0** (slow cathedral onset) · Diffusion 1.0 · **Late Mod Rate ~0.5 Hz / Depth high** (lush detuned tail) · High Cut **2.5-3.5 kHz** · Bass Mult **~0.6 @ Xover ~250 Hz** (keeps the low wall out of the mud). Static input → evolving wall.

## 3. Big realistic hall
- Mode **Large Chamber** or **Dense Room** · Depth ~85% · Predelay **30-60 ms** · Decay **6-12 s** · Late Size max · Early Size ~50-80 ms with some Early Send · Diffusion 1.0 · Mod ~0.5 Hz / med · High Cut 5-6 kHz. Big and clean, not muddy.

## 4. Tight room "glue"
- Mode **Medium Room** / **Large Room** · Depth ~60% · Predelay **5-10 ms** · Decay **0.3-0.8 s** · Late Size small (~10-15) · Early Size small (~20-30 ms) · Diffusion high · High Cut 6-8 kHz · **Mix ~10-15%** (insert, not send). Sits a dry banjo/baritone in a real place without an obvious tail.

## 5. The "depth bed under VintageVerb"
- Mode **Large Room** · **Depth 0%** (Early only) · Early Size **< 40 ms** · Diffusion to taste · Mod off · Mix low. Pure placement layer — gives the dry source a believable position; route its output (or run in parallel) into VintageVerb's colored wall so the color sits in a real space. *(Room = where it is; VintageVerb = what it sounds like.)*

## 6. Degraded / lo-fi tape drone
- Mode **Dark Room** (11 kHz ceiling, noisy interpolation, grainy flutter) · Depth 100% · Decay **10-20 s** · Late Size large · **Early + Late Mod Depth high** (kills metallic ring, adds wobble) · High Cut ~3 kHz · Bass Mult ~0.6. Then **saturate the return** (Decapitator / SketchCassette) for the doom/shoegaze wall. Closest Room equivalent to VintageVerb's 1970s color.

## 7. Shimmer-ish rising tail (no true Shimmer in Room)
- Any lush mode (**Bright Room** for max sheen) · Decay 8-15 s · **High Mult ~1.5-2.0 with High Xover ~4-6 kHz** → the highs ring LONGER than the body = a rising, airy sheen on the tail. + Late Mod Depth high for chorused movement. *Honest: this is bright-tail emphasis, not pitch-shifted shimmer — for real octave-up shimmer use ValhallaShimmer, H90/Big Sky, or feed Room into a pitch shifter.*

## 8. Self-feeding Space drone (Early engine alone, v2.0.0)
- Any mode · Depth **0%** (Early only) · **Space ~65-85%** (early reflections self-feed into their own reverb) · Early Size medium-large · Diffusion 1.0 · **Early Mod Depth high** · Predelay to taste. A modulated wash built entirely from the Early section — a different texture than the Late tail; nudge Space for a near-runaway evolving bed.

## Notes on extremes
- Room's Late decay maxes at **100 s** (vs VintageVerb's 70) → "near-frozen" walls are slightly easier here, but there is **NO real Freeze** — for truly held infinite drones use **Big Sky Freeze** or **Supermassive** max feedback.
- Always **Lo Cut / Bass Mult < 1** on long tails or the low end blooms into mud.
- High Diffusion stays smooth (won't go metallic) — leave it at 1.0 unless you specifically want distinct early slaps.
