---
type: chain
title: "Big Time OVERLOAD Drop → Clean Banjo Lead Emerges From the Collapse"
date: 2026-06-15
artists: [Swans, Sufjan Stevens]
instrument: banjo (GK-5 → VG-800)
gear:
  - Roland VG-800
  - Chase Bliss Clean
  - Chase Bliss Big Time
---

# Big Time OVERLOAD Drop → Clean Banjo Lead Emerges From the Collapse ⭐

A one-stomp self-oscillating climax that drops into a clean, swelled banjo lead riding the collapsing tail. You hold the RIGHT footswitch in Long and the **OVERLOAD** ramp detonates the bed into a maximum-loudness wall; on release it collapses, and *out of that collapse* a clean banjo lead bows in attack-less — Clean's Swell engine violining each pluck so the lead emerges from near-silence rather than striking over the wreckage. A build/drop arc from two boxes: Big Time supplies the climax, Clean supplies the attack-less entrance.

🟣 DOUG-designed integration. No artist played this exact chain; the per-unit patch refs carry their own provenance and the Taste-ref names the sound it chases. The OVERLOAD-in-Long behavior and hold-MODE panic reset are manual-documented; Clean's Dynamic Swell (cross-the-Sensitivity-threshold-to-swell-in) is manual-documented; the build/drop *arc* (detonate → release into a swelled lead) is the designed move.

## Signal path

EBM-5 banjo (GK-5) → **VG-800 — "Sufjan Fingerpicked Banjo Lead"** (recall **VG-800 — "GK SETTING — EBM5 BANJO"** first) → **CB Clean — "Dynamic Volume Swell"** (the swell engine; AUX engaged) → **CB Big Time — "One-Stomp Climax"** (MODE Long · STATE Saturated · hold RIGHT = OVERLOAD, release to collapse) → stereo out → board / tape.

Three roles, two pedals doing the work: the VG-800 makes a clean discrete banjo pluck; **Clean is the swell engine** that strips the attack so the lead bows in; the Big Time both *is* the climax (OVERLOAD ramp) and the bed the lead falls into. Clean sits **before** Big Time on purpose — the swelled, attack-less note has to be what feeds the delay so the lead reads as emerging from the tail, not slapped on top of it.

## Per-unit

- **VG-800 — "Sufjan Fingerpicked Banjo Lead":** banjo played as a clean 4-string guitar (`INST = E.GUITAR/ACOUSTIC`, 5th string excluded via `STRING MUTE 5`, `NORMAL MIX ~20–40%` keeps the real pluck/finger noise). Dirt OFF, onboard REV/DLY off — we want a *bright, discrete, clean pluck*, because Clean's Swell tracks cleanest off a clearly-articulated transient and the lead needs to sing once it bows in. Recall **"GK SETTING — EBM5 BANJO"** first; it is the enabler nothing else tracks without (per-string SENS to the on-screen bar ≈75%, 5th-string strategy, `GLOBAL GAIN 2`).
- **CB Clean — "Dynamic Volume Swell":** the load-bearing unit for the *entrance*. AUX footswitch engages Dynamic Swell (momentary; flip LATCH for a toggle). Each banjo pluck that crosses the **Sensitivity** threshold swells in and swells back out below it — violined attacks, no volume pedal. Hidden Options: Wet = **Swell In** ~noon, Dry = **Swell Out** ~noon for a graceful bowed bloom (re-LED Sensitivity for the GK banjo — it will not match guitar settings). This is exactly the "feed pre-swelled material to the downstream board" move the patch is built for: the Big Time receives attack-less notes, so the lead emerges from the collapsing tail with no pick spike to give it away.
- **CB Big Time — "One-Stomp Climax":** MODE **Long** (OVERLOAD only works in Long), STATE **Saturated**, VOICING Analog, COLOR ~35% (headroom so the ramp has somewhere to go), TIME long, CLUSTER ~50%, **TILT EQ pushed DOWN** (boost lows → longer/louder tails feeding the climb), **FEEDBACK ~55% base** (the ramp drives it past COLOR toward max), SPREAD widen, **WET set conservatively** (the manual warns about volume twice — the ramp is scary loud). Hold the **RIGHT footswitch** = OVERLOAD: COLOR + FEEDBACK ramp toward max into a self-oscillating wall; **release to collapse** — and that collapse is the bed your swelled banjo lead rides down. Big Time knob values are a **dialable recipe** (motorized flying faders override on recall; numerics are designed starting points, not published settings).

## Routing

Mono front (banjo → VG-800 → Clean, Board 1). Big Time auto-engages **MISO** (mono-in/stereo-out) off IN-L, so the wall and the trailing lead open up to stereo from the Big Time onward — no stereo source needed. **Gain-staging is the whole arc:** the VG-800 gives a clean discrete pluck → Clean *swells it in* (attack-less, pre-swelled) → the Big Time eats COLOR/FEEDBACK headroom on the OVERLOAD ramp, then drops it back to the base FEEDBACK on release. Keep COLOR modest (~35%) and FEEDBACK with room above it — that headroom is *what OVERLOAD climbs into*; max it at rest and the ramp has nowhere to go. Run free (the swell and the stomp are hand-timed), or slave Big Time via CC54 if you want the climax to land on a grid. **Safety net:** set WET low before performing, and **hold the MODE button to panic-reset** Big Time to a clean delay if the self-oscillation runs away.

## Sound

A maximum-loudness self-oscillating wall that detonates on one footswitch and, on release, collapses — and out of the collapse a clean banjo lead bows in with no attack, riding the dying tail down as it sings. The whole build/drop happens as a single gesture from two boxes: the wall is the climb, the swelled lead is the landing.

**Taste-ref:** post-punk / experimental near-silence → overwhelming crescendo → collapse (Swans-adjacent feedback climb and drop), with the lead voice landing as a clean, bowed-in **Sufjan** banjo-as-lead rather than another layer of noise — the singing line emerging *from* the wreckage instead of over it.

## Play

1. Set the bed: hold or sustain the banjo into Big Time so OVERLOAD has material to climb.
2. **Hold Big Time's RIGHT footswitch** → OVERLOAD ramps COLOR + FEEDBACK toward max into the self-oscillating wall.
3. At the peak, **release the RIGHT footswitch** to collapse the wall.
4. On the drop, **pluck the banjo lead with Clean's AUX (Dynamic Swell) engaged** — each note bows in attack-less and emerges from the collapsing tail. Play *sparse, singing* phrases; let the swell do the entrance.
5. If the wall runs away, **hold Big Time's MODE button** to panic-reset to a clean delay.

## Sources

- **Basis:** designed integration; chains **VG-800 — "Sufjan Fingerpicked Banjo Lead"** (+ **"GK SETTING — EBM5 BANJO"**) → **CB Clean — "Dynamic Volume Swell"** → **CB Big Time — "One-Stomp Climax"** (all reused, no new patches). OVERLOAD = hold-RIGHT-in-Long ramps COLOR+FEEDBACK toward max + hold-MODE panic reset from the Big Time sheet / manual p.16/26 (`one-stomp-climax` patch). Attack-less entrance = Clean Dynamic Swell crossing the Sensitivity threshold, feeding pre-swelled material downstream (Clean manual pp.30–31 Swell + Hidden pp.16–17; `dynamic-volume-swell` patch). Banjo-as-lead source + 5th-string strategy from the VG-800 banjo patches.
- Big Time knob values are a **dialable recipe** (unpublished; motorized flying faders override on recall), not sourced manufacturer settings.
- `research/links/centerpiece-minimal-chains-and-sampler-integration.md` (centerpiece build/drop on the Big Time alone)
- `Research/Chains/banjo-baritone-leads.md` (designed)
- `Research/Taste-Profile/taste-profile.md` (post-punk near-silence → crescendo lens)
