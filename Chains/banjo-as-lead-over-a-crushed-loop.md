---
type: chain
title: Banjo-as-Lead over a Crushed Loop
date: 2026-06-14
artists: [Modest Mouse]
instrument: banjo (GK-5 → VG-800) + Digitakt loop
amp: ampless (direct/print)
gear:
  - Elektron Digitakt 2
  - Chase Bliss Clean
  - JHS Colour Box V2
  - Strymon Deco V2
  - Chase Bliss Generation Loss
  - Chase Bliss Big Time
  - MXNHLT PORTA424
  - JHS 424
  - Novation 61SL MkIII
  - UA Apollo x8
---

# Banjo-as-Lead over a Crushed Loop

A banjo lead line cascading over a degraded groovebox loop, with the **CB Big Time as the minimal-chain centerpiece** — the melodic counterpart to the wall chains. A 🟣 DOUG-designed integration.

## Signal path

- **Loop bed:** Digitakt 2 (crushed loop) → into the End bus.
- **Lead:** banjo (GK-5 → VG-800) → CB Clean → JHS Colour Box V2 → Strymon Deco V2 → **CB Generation Loss → CB Big Time** (centerpiece) → PORTA424 → JHS 424 → tape.

## Per-unit

- **Digitakt 2** — **#30 Sampled-Banjo Groove** or **#4 EZBOT Generative Sample-Chain Slicer** as the crushed loop bed (sampled banjo/baritone plucks, Lowpass 4, light Master Overdrive), clock-master template **#29**.
- **CB Clean** — **#5 Banjo Transient Tamer** (slow attack lets the pluck spike through THEN clamps; Envelope Balance high so it tracks the bright register) so the banjo behaves like a lead voice; re-LED the Sensitivity for the GK-5.
- **JHS Colour Box V2** — **#5 Banjo-Into-Fuzz Fixer** (fakes body, tames the 2–4 kHz ice-pick, light HI-PASS) so the banjo lead survives the chain, OR **#17 Brittle Jangle Front-End (CBX-LF3)** for a bright Modest-Mouse jangle reading.
- **Strymon Deco V2** — **#11 Banjo Lead Doubler (tame + thicken)** (sum doubler, low Wobble, dark Tone) so the lead swells inside the bed without ice-picking, OR **#15 Double-Track Jangle Chorus (DEC-LF1)** for the Brock double-track.
- **CB Generation Loss** — **#4 Half-Speed Drone Banjo (source-tuned)** (Model 4–5, light Wow/Flutter, Dry Small keeps the pluck) — degrades the lead "recorded-wrong" without losing intelligibility.
- **CB Big Time** — **#8 Banjo Thermae Cascade Lead** (SCALE Octave / Oct+4+5, MOTION Square, SCALE IGNORE ON for musical pitch ramps) — single plucks arpeggiate into octave ladders, clock-locked to the loop. Keep COLOR modest (source already degraded).
- **PORTA424** — **#7 Worn-Cassette Banjo Bed (banjo-as-lead)** (bass shelf up, treble down, 18V) so the bright percussive attack rounds into a lead inside the print.
- **JHS 424** — **#10 Banjo-as-Lead Drone Glue** (Gain 1/2 modest so transients don't gate, Treble 1:30 to claw articulation back) → Apollo.

## Routing / sync

Digitakt = clock master; Big Time follows (**CC111=0**, subdivision **CC54**) so the Thermae cascade locks to the loop. Banjo arrives summed line-level stereo (GK-5 → VG-800); Big Time IN-L mono → **MISO**. Keep Big Time COLOR modest after Gen Loss (over-saturating a pre-degraded source "sounds awful"). Optional: drive the lead from the **61SL MkIII #5 Big Time Centerpiece Performance Template** (ride COLOR/TIME/WET from the encoders) and **#2 VG-800 Audition & Control** for model/FX rides. One tape box destroys — PORTA424 (banjo bed) carries it, 424 stays glue.

## Sound

A bright, plucky banjo line that the Big Time fans into octave cascades over a crushed, ducking loop — the melodic hook riding a recorded-wrong groove, then cassette-printed so the lead sits *in* the tape, not on top of it.

## Play

Lock the DT2 loop, play single banjo plucks and let Big Time's Thermae do the melodic work (STEP MODE on the LEFT footswitch to step pitch by hand). Use CB Clean's **#12 Dynamic Volume Swell** on the AUX footswitch to bow the plucks in for an Ondes-like attack. Freeze the loop bed and solo over it for an intro/outro.

**Taste-ref:** lo-fi-prolific-volume banjo-as-lead reading (Modest Mouse brittle jangle) over the groove engine; the rig's banjo-as-lead tie-breaker. 🟣 designed.

## Sources

- **Basis:** designed integration; chains DT2 #30 (or #4) + #29 + Clean #5/#12 + Colour Box #5 (or #17 CBX-LF3) + Deco #11 (or #15 DEC-LF1) + Gen Loss #4 + Big Time #8 + PORTA424 #7 + 424 #10, optionally driven by 61SL #5/#2. "Over-saturating a pre-degraded source sounds awful" + MISO + CC111/CC54 cited from Big Time sheet placement notes + #2.
- `Research/Taste-Profile/lo-fi.md`
- `Research/Chains/lo-fi-grooves.md` (C6)
