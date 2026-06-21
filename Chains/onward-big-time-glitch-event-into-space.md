---
type: chain
title: "Onward → Big Time — Glitch Event Into Space"
date: 2026-06-15
artists: [DOUG-designed]
instrument: guitar / loops
gear:
  - Chase Bliss Onward
  - Chase Bliss Big Time
  - Elektron Digitakt 2
---

# Onward → Big Time — Glitch Event Into Space ⭐

The two-box "one direction per song" centerpiece: **Onward is the glitch event, Big Time is the space.** Stuttered, granular glitch fragments get smeared into rhythmic and ambient tails — Onward's clocked stutters feed Big Time's multitaps for stutter-on-stutter rhythmic glitch-delay, with both boxes locked to one shared clock so nothing runs away.

🟣 DOUG-designed integration. No artist played this exact chain — the per-unit patch refs carry their own provenance, and the Taste-ref names the sound it chases.

## Signal path

guitar / loops → **CB Onward — "Clocked Banjo/Loop Stutter Event"** (GLITCH channel, clocked) → **CB Big Time — "Lo-Fi Rhythmic Groove"** (CLUSTER multitap, DIFFUSE up, clocked) ← shared MIDI clock from Digitakt 2 → tape.

One direction only: Onward sits **in front** of Big Time and feeds it. The stutter is the source event; the delay is the room it lands in. Do not feed Big Time back into Onward — that's the runaway loop this design deliberately avoids.

## Per-unit

- **CB Onward — "Clocked Banjo/Loop Stutter Event"** — GLITCH channel, **SIZE small** so it grabs only the front transient (the percussive pick/loop attack survives as a clean stutter grain), with the stutter repeats **locked to MIDI clock** (SIZE = subdivision when clock is present). This is the event generator: short, articulate, rhythmic glitch fragments tracking the live signal. **CC108** retriggers the Glitch clock-quantized for punch-ins. SENSITIVITY (hidden, on SIZE) toward LESS so hot transients don't over-trigger.
- **CB Big Time — "Lo-Fi Rhythmic Groove"** — MODE **Short**, STATE **Compressed** (keeps the stuttered taps punchy and articulate in a dense mix), VOICING **Focus**. **TIME slaved to MIDI clock**, subdivision via **CC54** (dotted-8th or 16th), **CC111 = 0** so the pedal follows clock. **CLUSTER ~⅓–½** is the multitap pattern echoing the glitches (this is the "more/less taps" live fader). For this chain push **DIFFUSE up** (alt knob under FEEDBACK) so the stutter taps smear from rhythmic into the granular/ambient tail the concept wants — *this is the one dialed dip on the reused patch.* FEEDBACK ~35–45% (articulate, not washy), 0.5X ON for the 12-bit lo-fi crush, COLOR ~40%, WET ~40%, SPREAD ping-pong so the added taps fan L/R. SCALE Off/Chromatic so clock snaps cleanly.

## Routing

**Clock them together.** Run the **Digitakt 2 as the single clock master** sending MIDI clock to both boxes — **Onward** takes MIDI over **1/4" TRS** (via the CB MIDIBox/TRS), but **Big Time has native 5-pin DIN MIDI (IN + THRU, default channel 2)** so run the Digitakt's DIN OUT **directly into Big Time's DIN IN** (no TRS adapter needed for that leg). Onward syncs its Glitch stutter timing to clock (SIZE = subdivision); Big Time locks TIME via CC54 subdivision. Because they share one grid, every glitch grain lands on a tap and every tap lands on the grid — that's the stutter-on-stutter lock. Pick **ONE** master and never loop clock back. Signal is mono-in/stereo-out friendly: a mono source into Onward, stereo out of Onward into Big Time's stereo ins, stereo to tape.

**Gain-staging / runaway control:** the "one direction per song" rule *is* the safety. Onward generates discrete events that decay; Big Time's Compressed STATE and modest FEEDBACK keep the taps from piling into a wall. If it starts to thicken, pull DIFFUSE back toward rhythmic and drop CLUSTER — let the taps separate again. Hold Big Time's footswitch (Hold-MODE) as the panic reset to a clean delay.

## Sound

Stuttered, granular glitch events smeared into rhythmic and ambient tails — angular glitch fragments fanned by the delay into a slightly-crushed, clock-locked rhythmic cloud that dissolves toward ambient as DIFFUSE comes up. Glitch is the event, delay is the space.

**Taste-ref:** art-rock / studio-as-instrument — glitch-rhythm hooks smeared into rhythmic delay (Radiohead "Ful Stop" / reverse-glitch-delay territory), edging toward granular ambient as DIFFUSE opens up.

## Play

Play guitar (or run a loop) so the live signal triggers Onward's clocked stutters; the small SIZE keeps the pick/loop attack as a clean grain. Fire **CC108** from the master to retrigger the Glitch in time for rhythmic punch-ins. Big Time's **CLUSTER fader is the live "more/less taps" control**, and **DIFFUSE is the rhythmic↔ambient morph** — ride it from articulate stutter-delay toward a granular smear across a phrase. Keep one direction: glitch in, space out.

## Sources

- **Basis:** designed integration; chains **CB Onward — "Clocked Banjo/Loop Stutter Event"** (new) + **CB Big Time — "Lo-Fi Rhythmic Groove"** (reused), driven by a single Digitakt 2 clock master. "Glitch supplies the event, Big Time the space" + "clock them together" (Onward syncs GLITCH to MIDI clock; Big Time locks TIME via CC54, follows via CC111) from the centerpiece source file §B.
- `gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md`
- `gear/Chase Bliss Onward/research/links/cb-stack-clock-sync-per-pedal.md`
