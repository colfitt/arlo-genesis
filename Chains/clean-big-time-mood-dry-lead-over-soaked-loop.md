---
type: chain
title: "Clean → MOOD → Big Time: Dry Lead Over a Soaked Loop"
date: 2026-06-15
artists: [The Unperson, Brian Eno]
instrument: guitar / synth
gear:
  - Chase Bliss Clean
  - Chase Bliss MOOD MkII
  - Chase Bliss Big Time
---

# Clean → MOOD → Big Time: Dry Lead Over a Soaked Loop

A clean dry melody played live over a captured, fully-wet evolving micro-loop bed — and Big Time adds depth only to the dry lead, never to the soaked loop. The whole move hinges on **MOOD's ROUTING = micro-loop only**: the Wet (Reverb) engine hits *only* the captured loop while your live input passes through bone-dry. So the bed drenches and evolves on its own, your hands stay clean and present, and the short delay at the end deepens just the live line floating on top.

🟣 DOUG-designed integration. The Clean and MOOD patches carry their own provenance; the Big Time patch is purpose-built for this chain (full spec saved alongside). Knob faces on the Big Time patch are a dialable recipe — Chase Bliss publishes character, not numbers — flagged below. The artists/taste-ref name the sound it chases, not a chain anyone played verbatim.

## Signal path

Guitar / synth → **CB Clean — "Home Base (Safe Space)"** (always-on transparent leveler, EQ off, gentle comp) → **CB MOOD MkII — "The Unperson — dry input over a reverb-soaked loop"** (ROUTING = **micro-loop only**, Wet MODE = **Reverb** → loop gets drenched, live input stays dry) → **CB Big Time — "Dry-Lead Depth (Short, Low-Mix Slap)"** (MODE **Short**, low WET, low FEEDBACK — subtle depth on the dry lead only) → amp / interface.

The only "real signal-order" claim here is the deliberate **leveler → micro-looper → short delay** placement: condition the source first, capture/soak the bed in the middle, then add lead depth last so the delay sees a *clean dry lead* (the soaked loop has already exited MOOD as part of its own wet path and is not re-fed into Big Time as a fresh dry signal to echo — see Routing).

## Per-unit

- **CB Clean — "Home Base (Safe Space)":** Sensitivity set FIRST by ear to the left red LED (re-set per instrument — a passive guitar and a hot synth never share a value); Dynamics 10:00–11:00 (gentle, transparent comp); Wet ~1:00 unity-to-slight-boost, Dry off; EQ at noon (off — let the source's own tone through); Mode **Manual**, Release **Mid**, Physics **Mid (stable)**, all CUSTOMIZE dips off. This is Clean in its front-of-board anchor slot: it just gives MOOD a steady, even-leveled input so loop captures are consistent and the dry lead sits at a predictable level when it reaches Big Time. Dead quiet even with Wet gained up.
- **CB MOOD MkII — "The Unperson — dry input over a reverb-soaked loop":** **ROUTING = micro-loop only** (the headline — Wet hits *only* the captured loop; your live input passes dry), **Wet MODE = Reverb** (soaks the loop into an evolving wash), CLOCK to taste (lower = more grit/character on the loop, higher = cleaner/longer), MIX around 1:00 so the soaked loop sits as a bed under the dry line. Capture the loop, then ride the hidden **DIRECT MICRO-LOOP** (looper MODIFY) and **FADE** (looper LENGTH) to push the drenched loop into the background under your dry playing. Demoed by The Unperson with synth / OP-1 / Mutable Rings as loop food — synth is ideal here. ⚠️ A stray MIDI Note would auto-engage Synth Mode; keep notes off MOOD's channel if you ever clock it.
- **CB Big Time — "Dry-Lead Depth (Short, Low-Mix Slap)"** (new, purpose-built): MODE **Short**, STATE **Digital** (limiter off → clean, pitch-stable, won't smear or saturate the lead), VOICING **HiFi** (keep the lead present and articulate), SCALE **Off**, MOTION **Off** (or **Sine** very slow/shallow for the faintest tape drift), COLOR **low ~20%**, TIME a **short slap-to-eighth**, CLUSTER **0** (single clean repeats, not a multi-tap wall), TILT EQ **noon → slightly up** (keep the lead on top of the bed), FEEDBACK **low ~25%** (one or two repeats, no build), WET **low ~25–30%** — depth and dimension, *not* a second wash. SPREAD **widen** subtle if you're running stereo. The whole point: Big Time deepens the live lead by a hair and gets out of the way; it must never own the mix or it muddies the MOOD bed. **Numeric positions are a dialable recipe — Chase Bliss publishes character, not numbers.**

## Routing

Three Chase Bliss boxes in a row. **The gain-staging / routing reasoning is the whole game:**

1. **MOOD's "micro-loop only" routing is what keeps the live input dry while the loop is reverb-soaked.** The Wet (Reverb) engine is fenced to the captured micro-loop; your live playing bypasses the Wet path entirely. That's why the bed can drench and evolve while your hands stay clean.
2. **Big Time then deepens only the lead, not the bed.** Big Time sees MOOD's *output* — which is (dry live input) + (the soaked loop as MOOD's own wet print). Keep Big Time's WET and FEEDBACK low and its TIME short so it reads as *depth on the dry transients of the live line* rather than re-echoing the already-washed bed. A long, high-feedback Big Time here would smear the loop into mud and erase the dry-vs-soaked contrast — the exact thing the chain exists to preserve. Short + low-mix is non-negotiable.
3. **Stereo:** if you want width, create it inside MOOD (MISO dip: TS in / TRS out — MISO *creates* stereo, SPREAD only *widens* it) and let Big Time pass/widen it; Big Time's IN-L also auto-engages MISO from a mono feed. Keep Clean's MISO/SPREAD off in this front-anchor role.
4. If the bed ever swallows the lead, the fix order is: drop MOOD MIX first (it's the loudest wet stage), then trim Big Time WET — never push Big Time up to "win," that just muddies everything.

## Sound

A clean, present melodic line sings live and intimate while underneath it a captured fragment slowly drenches, blooms and evolves into an ambient reverb bed — and the lead carries a touch of short, dimensional delay that the bed does not, so the two layers never fuse. The bed is soaked and atmospheric; the lead stays dry, articulate, and a half-step in front of it.

**Taste-ref:** The Unperson's "beautiful ambient setup" — dry playing over a drenched loop (synth / OP-1 / Rings as loop food) — crossed with Eno-style evolving-ambient beds where a static-but-living wash holds while a clean voice moves on top.

## Play

1. Set **Clean** by the LED, then dial **MOOD** ROUTING = micro-loop only / Wet = Reverb.
2. Feed a phrase (synth pad, OP-1, or a held guitar figure) and **capture the micro-loop** — the Reverb soaks *only* the loop.
3. Use MOOD's hidden **DIRECT MICRO-LOOP / FADE** to push the drenched loop back into the bed under you.
4. Now play your **dry lead** live on top — it bypasses MOOD's wet path and stays clean.
5. **Big Time** adds just a short, low-mix slap of depth to that dry line. Keep WET/FEEDBACK low; if it starts washing, you've gone too far.
6. To collapse: clear the MOOD loop (tap to re-record / replace), and **hold Big Time's MODE button to panic-reset** to a clean simple delay.

## Sources

- **Basis:** 🟣 designed integration; chains **CB Clean — "Home Base (Safe Space)"** + **CB MOOD MkII — "The Unperson — dry input over a reverb-soaked loop"** + **CB Big Time — "Dry-Lead Depth (Short, Low-Mix Slap)"** (new, purpose-built). The dry-over-soaked-loop core (ROUTING = micro-loop only, Wet = Reverb, dry input bypasses the wet path) is documented in the MOOD "The Unperson" patch (`unperson-mood-mkii-reverb-delay-looper.md`; MOOD-MkII UsageGuide §5; ref: The Unperson / Ali — Vong Replay / Mutable Rings / OP-1 → MOOD). MISO-creates-stereo / SPREAD-only-widens from the MOOD "MISO" patch (manual p.44, video manual pt.1/pt.2). Clean front-anchor leveler + LED-first procedure from the Clean "Home Base" patch (Clean manual pp.8–9). Big Time Short / Digital-no-limiter / low-mix mechanics from the Big Time gear profile and the Big Time "Clean Stereo Delay" + factory patch sources (Mark Johnston deep-dive: hold-MODE panic reset, Digital STATE = limiter off).
- **Honesty flag:** no published knob numbers exist for the new Big Time patch — all of its clock-face positions are a dialable recipe, set by ear. MOOD ROUTING/Wet-MODE and Clean toggles are real switch positions; Clean's Sensitivity is by-ear/per-instrument (single-LED metering, no recallable detents).
