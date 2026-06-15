---
type: chain
title: "Hizumitas → Big Time → MOOD Doom Micro-Loop Mangle"
date: 2026-06-15
artists: [Boris, Chase Bliss]
instrument: "baritone / guitar"
gear:
  - EarthQuaker Devices Hizumitas
  - Chase Bliss Big Time
  - Chase Bliss MOOD MkII
---

# Hizumitas → Big Time → MOOD Doom Micro-Loop Mangle ⭐

Three anchors, one signature pipeline: a sustaining fuzz becomes an echo bed, the echo bed gets frozen, and a slice of that frozen bed is grabbed and time-warped into stuttering, pitch-bent glitch riding on top of the doom wall. The Hizumitas is the engine — its long sustain feeds **both** downstream boxes a continuous source, so the Big Time captures a real wall (not a choppy stab) and the MOOD micro-loop has unbroken material to chop. Big Time makes the echo and holds it; MOOD grabs a sliver and mangles it.

🟣 DOUG-designed integration. No artist played this exact chain — the per-unit patch refs carry their own provenance, the new MOOD patch is purpose-built for this chain (full spec saved alongside), and the Taste-ref names the sound it chases.

## Signal path

Baritone / guitar → **EQD Hizumitas — "Granular/Glitch Capture — sustained source for grains"** (long sustain, the unbroken doom source) → **CB Big Time — "Loop Diffuser"** (Long, infinite-feedback echo bed; hold **RIGHT = FREEZE** for the held HOLD bed) → **CB MOOD MkII — "Doom Slip Micro-Loop Mangle"** (new — Slip micro-loop grabs a slice of the frozen bed and time-warps/slips it into pitch-bent stutter; hold **LEFT = freeze the slice**) → amp / interface, stereo.

Mono fuzz → Big Time **IN-L** auto-engages **MISO** (mono-in / stereo-out); everything from Big Time onward is stereo, so the MOOD glitch can pan against the wide frozen wall.

**Shared clock:** Big Time is the clock master (**CC110**, 60–240 BPM) and MOOD follows (**CC51>0**, **CC54** sets the micro-loop division). One grid, three anchors — no Digitakt needed. This is what makes MOOD's stutter land *in rhythm with* the Big Time bed instead of fighting it.

## Per-unit

- **EQD Hizumitas — "Granular/Glitch Capture — sustained source for grains":** the load-bearing idea is the sustain — it makes the downstream capture (Big Time) and the MOOD micro-loop sound *intentional* rather than choppy. Hold a chord and the Hizumitas keeps the source alive long after the pick attack, so both engines get a continuous wall to work on. Run Sustain up for a long-sustaining drone voice, Volume and Tone to taste. *(⚠️ No published Hizumitas knob values for this patch — Sustain up / Tone to taste is a dialable recipe, not sourced positions. The Mood-against-sustained-Hizumitas pairing itself is the documented Wata-adjacent technique.)*
- **CB Big Time — "Loop Diffuser"** (factory #9): MODE **Long**, STATE **Saturated** (or **#!&%** misbias for sag-and-return), VOICING **Analog**, **COLOR ~30%** (LOW so the echoes climb), **FEEDBACK ~80%** (above COLOR → climbing wall), CLUSTER high **~70%**, TILT EQ noon → slightly down (lows feed the loop = longer tails), DIFFUSE high **~75%** + DIFFUSE TYPE **on** (ethereal), SPREAD **widen**, WET conservative (these get loud). Recall **PC 9** and the motorized faders fly to the saved positions. Play a few notes, let the infinite-feedback bed build, then **hold RIGHT to FREEZE** → a non-degrading held HOLD bed that MOOD can slice. *(Factory intent is sourced; the numeric fader positions are a designed interpretation — on PC recall the real preset's flying faders override these. The low-COLOR/high-FEEDBACK "most change over time" climb is documented in the manual.)*
- **CB MOOD MkII — "Doom Slip Micro-Loop Mangle"** (new, purpose-built): Wet MODE **Slip**, Looper MODE **Stretch**, ROUTING **IN+micro-loop**, MIX **~1:00** (featured glitch, not a second wall), CLOCK **~11:00** (a little grit). **SYNC = LEFT** (Micro-Looper synced to Wet) and feed Big Time's MIDI clock so the loop length locks to the grid (**CC51>0** follow, **CC54** sets the loop division). Tap the **RIGHT (Micro-Looper)** footswitch to grab a slice of the frozen Big Time bed; **hold LEFT to freeze** the Slip, then ride Slip **MODIFY** off neutral (semitone steps; CCW of noon = reverse) to pitch-bend the slice and rotate Looper **LENGTH** to resize it. The frozen slice stutters on the Big Time grid while you bend it. *(⚠️ A stray MIDI *Note* auto-engages Synth Mode, which ignores clock — keep Big Time sending clock + CC only, no notes, on MOOD's channel. No published numeric values; settings are a dialable recipe.)*

## Routing

Mono fuzz → Big Time **IN-L** auto-engages **MISO** (mono-in / stereo-out); stereo from Big Time onward, so the MOOD slice pans against the wide frozen cloud. Keep MOOD's **MIX moderate** — it's a featured glitch on top, not a second wall; the Big Time bed should still own the low-mids.

**Gain-staging / grid discipline is the whole game.** The Hizumitas is hot and sustaining, so keep Big Time **COLOR modest (~30%)** — too much COLOR plus a hot fuzz clamps the limiter "to porridge" before the bed can climb. The single shared clock (Big Time master via CC110 → MOOD follows via CC51/CC54) is what makes MOOD's micro-loop stutter *with* the bed on the same subdivision. If MOOD ever ignores the clock, you've tripped Synth Mode — re-check that only clock/CC (no Notes) are reaching it. If the Big Time bed runs away, **hold MODE on the Big Time** for an instant clean reset.

## Sound

A thick, sustaining fuzz echo holds forever on one chord, then a small chopped fragment of that same wall stutters and pitch-bends in rhythmic lockstep on top — you ride the doom bed while the slice slips and warps. The bed is saturated and oceanic; the glitch is granular, pitch-bent, and grid-tight.

**Taste-ref:** doom / experimental — Boris/Wata sustaining fuzz weight as the bed, with the Chase Bliss "freeze-and-mangle" aesthetic on top (frozen Big Time wall as ideal MOOD fodder); pitch-bent micro-loop glitch over a doom slab.

## Play

1. Hold one baritone/guitar chord and let the Hizumitas sustain feed the Big Time — let the infinite-feedback bed climb.
2. **Hold Big Time RIGHT to FREEZE** → the held HOLD bed locks, non-degrading.
3. Tap **MOOD RIGHT (Micro-Looper)** to grab a slice of the frozen bed; **hold MOOD LEFT to freeze** the Slip.
4. Ride MOOD Slip **MODIFY** (semitone steps; CCW of noon = reverse) to pitch-bend the held slice and rotate Looper **LENGTH** to resize it — it stutters on the Big Time grid.
5. Solo or drone over the whole thing. To collapse: tap MOOD's footswitches off, then **hold Big Time MODE to panic-reset** to a clean delay.

## Sources

- **Basis:** designed integration; chains **EQD Hizumitas — "Granular/Glitch Capture — sustained source for grains"**, **CB Big Time — "Loop Diffuser"** (factory #9), and **CB MOOD MkII — "Doom Slip Micro-Loop Mangle"** (new, purpose-built). Hizumitas-sustain-as-capture-source + the Mood-against-sustained-Hizumitas Wata-adjacent technique from the Hizumitas DeepResearch §10 / Usage Guide §6. Big Time Loop Diffuser FREEZE-then-solo, low-COLOR/high-FEEDBACK climb, and MISO auto-engage from the Big Time "Loop Diffuser" sheet (factory intent; manual pp.24–25). MOOD Slip micro-loop / freeze-the-slice + SYNC (LEFT = loop follows Wet) + MIDI-clock lock (CC51/CC54) and the Synth-Mode-ignores-clock caveat from the MOOD "SYNC", "Slip Pseudo-Sitar", and "Looper Remixer" sheets (manual pp.17, 26–27). Big Time as clock master via CC110 (60–240 BPM) from `gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md`.
- 🟣 designed (DOUG); fuzz knob values and MOOD/Big-Time fader positions are dialable starting points, not published presets — see each patch sheet.
- `Patches/EarthQuaker Devices Hizumitas/granular-glitch-capture-drone.md`
- `Patches/Chase Bliss Big Time/loop-diffuser.md`
- `Patches/Chase Bliss MOOD MkII/doom-slip-micro-loop-mangle.md`
