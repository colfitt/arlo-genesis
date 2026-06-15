---
type: chain
title: "Hizumitas → Big Time One-Stomp Detonation"
date: 2026-06-15
artists: [Swans, Boris]
instrument: baritone / guitar
gear:
  - EarthQuaker Devices Hizumitas
  - Chase Bliss Big Time
  - OBNE Dark Star V3
---

# Hizumitas → Big Time One-Stomp Detonation ⭐

A held fuzz chord swells into a self-oscillating, maximum-loudness wall on a single footswitch, then collapses into a frozen detuned shimmer on release. The OVERLOAD ramp turns a sustaining chord into a one-stomp *climax* — a fuzz wall, not a clean swell — and the Dark Star catches the fall as a cold, detuned pad.

🟣 DOUG-designed integration. No artist played this exact chain; the per-unit patch refs carry their own provenance, and the Taste-ref names the sound it chases. The OVERLOAD-in-Long behavior and the hold-MODE panic reset are manual-documented; the Dark Star freeze/pitch/crush capabilities are spec-documented.

## Signal path

Baritone / guitar → **EQD Hizumitas — "Doom Wall (max heavy)"** → **CB Big Time — "One-Stomp Climax"** (MODE Long, STATE Saturated, TILT down, FEEDBACK > COLOR, hold RIGHT = OVERLOAD) → **OBNE Dark Star V3 — "Frozen Detuned Collapse Pad"** (Aux = Hold catches the fall) → amp / tape.

Three pedals, dead simple: a maxed fuzz wall, a delay that detonates it, and a reverb that freezes the wreckage. Fuzz-before-delay is the standard order (documented EQD/JHS/Reverb signal-chain practice); freeze-reverb last so it catches everything upstream.

## Per-unit

- **EQD Hizumitas — "Doom Wall (max heavy)":** Volume max · Sustain max · Tone fully CW (max bass — mids scooped, highs tamed). The full-CW Tone is deliberate: the scooped/dark voicing keeps the wall *controllable* as Big Time ramps it. This is a held *chord* bloom, not a single oceanic note — hit the chord and let the long dense tail feed straight into Big Time. Needs real volume for the sustain/feedback bloom to arrive.
- **CB Big Time — "One-Stomp Climax":** MODE **Long** (OVERLOAD only works in Long), STATE **Saturated**, VOICING Analog, COLOR ~35% (headroom so the ramp has somewhere to go), TIME long, CLUSTER ~50%, **TILT EQ pushed DOWN** (boost lows → longer, louder tails feeding the climb), **FEEDBACK ~55% base** (the ramp drives it past COLOR toward max), SPREAD widen, **WET set conservatively** (the ramp is scary loud). Hold the **RIGHT footswitch** = OVERLOAD: COLOR + FEEDBACK ramp toward max into the wall; release to collapse.
- **OBNE Dark Star V3 — "Frozen Detuned Collapse Pad":** Mix mostly wet, Decay high, Filter dark (LPF side — cold, not glassy), Pitch 1 +1 oct (shimmer), Pitch 2 a hair off the center notch (Detune zone — cold chorus, not a clean interval), Crush ~11:00 (barely-there grit), Lag short, **Aux = Hold**, Stereo (trails on). You stomp Aux to freeze the instant the OVERLOAD releases, so the dying wall is caught as a static, detuned pad.

## Routing

Mono fuzz wall the whole way in; Dark Star runs Stereo (trails on) so the frozen pad blooms wide at the tail. **Gain-staging is the safety game:** the Hizumitas is already at maximum saturation, so keep Big Time's COLOR modest (~35%) — too much COLOR plus a hot fuzz makes the delay clamp the wall to porridge and leaves the ramp nowhere to climb. The headroom in COLOR/FEEDBACK is *intentional*: it's what OVERLOAD eats on the way up. **Safety:** the Big Time manual warns about volume twice — set WET low before you stomp this, and **hold the MODE button to panic-reset** to a clean delay if the self-oscillation runs away. The Dark Star's Hold passes new notes bone-dry, so once frozen you can play clean over the cold pad or just let it ring.

## Sound

A sustaining fuzz chord that detonates — on one footswitch — into a climbing, self-oscillating, maximum-loudness wall, then drops on release into a frozen, detuned, slightly-crushed cold pad that hangs in the air. Build and drop as a single gesture.

**Taste-ref:** post-punk / doom pulverising crescendo (Swans-adjacent feedback climb; Boris/Wata sustaining-wall density), with the collapse landing as a cold OBNE detuned shimmer rather than a clean shimmer swell.

## Play

1. Hold a chord on the maxed Hizumitas — let the overtone/feedback bloom at volume.
2. **Hold Big Time's RIGHT footswitch** → OVERLOAD ramps COLOR + FEEDBACK toward max; the held chord detonates into a self-oscillating fuzz wall.
3. At the peak, **release the RIGHT footswitch** to collapse — and on that release, **stomp the Dark Star Aux (Hold)** to freeze the dying wall into a frozen detuned pad.
4. Solo clean over the cold pad (Hold passes new notes dry), or let it ring out.
5. If the wall runs away, **hold Big Time's MODE button** to panic-reset to a clean delay.

## Sources

- **Basis:** designed integration; chains **Hizumitas — "Doom Wall (max heavy)"** + **Big Time — "One-Stomp Climax"** + **Dark Star V3 — "Frozen Detuned Collapse Pad"** (new, purpose-built). OVERLOAD-in-Long, COLOR/FEEDBACK ramp-to-max, and hold-MODE panic reset are manual-documented (Big Time manual p.16/26; `one-stomp-climax` patch). Maxed Doom-Wall fuzz voice quoted from EQD Noodlers / EQD product copy (`doom-wall-max-heavy` patch). Dark Star dual ±2-oct pitch shift, bipolar filter, Crush, and Aux = freeze/Hold are spec-documented (`gear/OBNE Dark Star V3/GearProfile.md`); the cold-detune + freeze-on-collapse recipe is a DOUG-designed dialable starting point, not a quoted/sourced setting.
- Fuzz-before-delay order: documented EQD / JHS / Reverb signal-chain best practice (not artist-specific).
- `Research/Taste-Profile/taste-profile.md` (post-punk/doom crescendo lens)
</content>
</invoke>
