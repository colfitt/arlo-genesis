---
type: chain
title: "Hizumitas → MOOD Doom Freeze → Dark Star"
date: 2026-06-15
artists: [Boris, Chase Bliss]
instrument: "baritone / down-tuned guitar"
gear:
  - EarthQuaker Devices Hizumitas
  - Chase Bliss MOOD MkII
  - OBNE Dark Star V3
---

# Hizumitas → MOOD Doom Freeze → Dark Star ⭐

A saturated fuzz captured and frozen into a granular pad, then drenched in cavernous detuned stereo space — a monolithic shoegaze/doom drone. The MOOD is the spotlight: its **Trail Catcher** resamples the live Hizumitas wall *permanently into the micro-loop*, then a low **CLOCK** sweep granulates that baked-in fuzz into a degraded, downsampled wall. The Dark Star turns the degraded wall into an enormous octave-down stereo room. Two anchors (Hizumitas, MOOD) plus the Dark Star as the plus-one space.

🟣 DOUG-designed integration. No artist played this exact chain — the Hizumitas and Dark Star patch refs carry their own provenance, the MOOD patch is purpose-built for this chain (full spec saved alongside), and the Taste-ref names the sound it chases.

## Signal path

Baritone / down-tuned guitar → **EQD Hizumitas — "Doom Wall (max heavy)"** (sustained oceanic single-chord fuzz, the source the freeze bakes in) → **CB MOOD MkII — "Doom Freeze Granulate (Trail Catcher bake + low-CLOCK wall)"** (new — Reverb-freeze the fuzz, **Trail Catcher** resamples it into the micro-loop, then roll **CLOCK** down to granulate the baked loop into a degraded wall; hold **LEFT = freeze**) → **OBNE Dark Star V3 — "Octave-down doom pad (rig recipe b)"** (cavernous detuned octave-down stereo verb, the enormous final space) → amp / interface, stereo.

Mono fuzz → MOOD **IN-L**; flick MOOD's **MISO** dip so the mono fuzz fans to a stereo wet field, and everything from MOOD onward is stereo so the Dark Star's detuned octave-pad spreads against the full image.

No clock needed — this is a drone/freeze chain, not a rhythmic one. The whole performance is gesture (freeze, bake, sweep CLOCK), so leave MOOD free-running and don't feed it MIDI.

## Per-unit

- **EQD Hizumitas — "Doom Wall (max heavy)":** **Volume max · Sustain max · Tone fully CW** (max bass — mids scooped, highs tamed, the *controllable* dark wall). The patch is built for exactly this job: the long, dense, sustaining tail is what makes the downstream capture sound *intentional* rather than choppy. Needs real amp/monitor volume for the feedback-and-sustain bloom to arrive. *(The doom-clip settings — full Volume, full Sustain, Tone cranked for low end — are sourced from EQD Noodlers / EQD product copy; see the patch sheet.)*
- **CB MOOD MkII — "Doom Freeze Granulate (Trail Catcher bake + low-CLOCK wall)"** (new, purpose-built): Wet MODE **Reverb**, ROUTING **IN+micro-loop** (the loop runs *through* the Reverb so the fuzz + its trails get baked), MIX **~1:00** (mostly wet wall), Wet TIME **up to sustain**, Wet MODIFY **~1:00** (heavy smear). Dips: **MISO on** (mono fuzz → stereo wet), **TRAILS on** (toggling mid-performance won't kill the wash), **LATCH on** (freeze holds hands-free), **SMOOTH on** (continuous CLOCK bend instead of stepped 4ths/5ths). The move: hold a baritone chord into the maxed Hizumitas, **HOLD LEFT (Wet) to freeze** the fuzz-soaked reverb into an infinite bed; while the loop is picking up the Wet trails, **briefly toggle the Micro-Looper (RIGHT) OFF and back ON to Trail-Catch** — that resamples the fuzz + reverb trails *permanently* into the micro-loop. Then **roll CLOCK down (CCW)** into the lower third (toward 6k → 4k → 3k → 2k) to granulate/downsample the baked loop into a degraded, aliased wall. *(⚠️ Trail Catcher is permanent — plan the moment; while overdubbing, Wet effects are NOT recorded, only the bypassed always-listening state bakes them in. ⚠️ No published numeric MOOD values for this exact patch — MIX/TIME/MODIFY/CLOCK positions are a dialable recipe; the Trail-Catcher resample technique, the low-CLOCK granulate scale, and the Freeze-Pad hold are each individually documented — see the patch sheet.)*
- **OBNE Dark Star V3 — "Octave-down doom pad (rig recipe b)":** Mix **1:00** (mostly wet), Decay **3:00**, Multiply **11:00**, Filter **10:00** (LPF, dark), Pitch 1 **-1 oct**, Pitch 2 **-1 oct** (or -2 oct on one side for more grumble), Crush **11:00** (light bit-crush), Lag **noon**, Routing **Stereo (trails on)**. This is the cavernous detuned space — both shifters octave-down under a dark LPF give the "interstellar grumbles" room that turns the degraded MOOD wall into something enormous. *(DOUG-inferred numeric values for this rig — not quoted from any external source; see the patch sheet. Watch Multiply: high Multiply + high Decay tips into self-oscillation.)*

## Routing

Mono fuzz into MOOD **IN-L** with **MISO on** → stereo wet field; stereo from MOOD onward so the Dark Star's octave-down detune spreads wide. Keep MOOD **MIX ~1:00** — the frozen/baked fuzz wall should own the low-mids before the Dark Star adds its room.

**Gain-staging / order is the whole game.** The Hizumitas is maxed and sustaining, which is *exactly* what the Trail Catcher wants — a continuous, dense source means the resample captures a real wall, not a choppy stab, and the low-CLOCK granulate has unbroken material to degrade. Run the **Reverb-freeze first, bake second, sweep CLOCK third**: freeze the fuzz reverb (hold LEFT), Trail-Catch it into the loop (toggle the Micro-Looper off/on while the Wet trails are alive), *then* roll CLOCK down so you're granulating the already-baked fuzz wall, not the live input. Going into the Dark Star, keep its **Filter on the LPF side (10:00)** so the octave-down pad doesn't pile mud onto the already-dark fuzz — the dark verb tames the build, the detune supplies the size. If the Dark Star starts self-oscillating, back **Multiply** off before **Decay**.

## Sound

A monolithic doom/shoegaze drone: a maxed fuzz chord gets frozen into an infinite reverb bed, that bed is permanently baked into a loop, and a CLOCK sweep degrades it into a granular, downsampled wall — all of it then drenched in a cavernous, octave-down, detuned stereo room. The core is saturated and oceanic; the texture is degraded and granular; the space is enormous and dark.

**Taste-ref:** doom / shoegaze — Boris/Wata sustaining-fuzz weight as the bed, with the Chase Bliss "freeze-and-mangle" aesthetic (Trail-Catch the fuzz, low-CLOCK granulate) feeding an OBNE-style subterranean octave-down verb cathedral. A monolithic wall you stand inside.

## Play

1. Hold one baritone / down-tuned chord into the maxed Hizumitas and let the sustain bloom at volume.
2. **HOLD MOOD LEFT (Wet)** to freeze the fuzz-soaked reverb into an infinite bed (LATCH holds it hands-free).
3. While the Wet trails are alive, **briefly toggle MOOD RIGHT (Micro-Looper) OFF then back ON** to **Trail-Catch** — the fuzz + reverb is now baked permanently into the loop. (Plan this moment — it's permanent.)
4. **Roll MOOD CLOCK down (CCW)** into the lower third (6k → 4k → 3k → 2k) to granulate the baked loop into a degraded, aliased wall — SMOOTH on makes it a continuous bend.
5. The Dark Star turns the whole degraded wall into a cavernous octave-down stereo room — drone or solo over it.
6. To collapse: tap MOOD's footswitches off (TRAILS keeps the wash decaying), then let the Dark Star tail ring out.

## Sources

- **Basis:** designed integration; chains **EQD Hizumitas — "Doom Wall (max heavy)"**, **CB MOOD MkII — "Doom Freeze Granulate (Trail Catcher bake + low-CLOCK wall)"** (new, purpose-built), and **OBNE Dark Star V3 — "Octave-down doom pad (rig recipe b)"**. The Hizumitas maxed-doom-wall + "long sustain makes downstream capture sound intentional" logic from the Hizumitas "Doom Wall (max heavy)" sheet (EQD Noodlers / EQD product copy). MOOD's **Trail Catcher** permanent reverb-trail resample (toggle Micro-Looper off/on; permanent; overdub doesn't record Wet) from the MOOD "Trail Catcher" sheet (manual pp.28–31, p.41). The **Freeze Pad** Wet-hold (HOLD LEFT, LATCH, TRAILS) from the MOOD "Freeze Pad" sheet (manual pp.22–23). The **low-CLOCK granulate/downsample** sweep and CLOCK scale (2k…12k noon…64k) + SMOOTH continuous bend from the MOOD "Clock-Decay Character Shift" sheet (manual pp.18–19). The detuned octave-down cavernous stereo verb from the Dark Star "Octave-down doom pad (rig recipe b)" sheet (DOUG-designed from Dark Star DeepResearch §13(b)).
- 🟣 designed (DOUG); the MOOD MIX/TIME/MODIFY/CLOCK positions are a dialable recipe (the resample + granulate *techniques* are documented, the numeric positions are not published); the Dark Star numbers are DOUG-inferred for this rig; the Hizumitas maxed-doom settings are sourced — see each patch sheet.
- `Patches/EarthQuaker Devices Hizumitas/doom-wall-max-heavy.md`
- `Patches/Chase Bliss MOOD MkII/doom-freeze-granulate-trail-catcher.md`
- `Patches/OBNE Dark Star V3/octave-down-doom-pad.md`
