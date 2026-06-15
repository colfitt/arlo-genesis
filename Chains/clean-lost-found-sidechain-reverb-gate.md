---
type: chain
title: "Lost & Found → Clean Sidechain Reverb Gate"
date: 2026-06-15
artists: [Slowdive, "m b v"]
instrument: "guitar / synth + MPC kick trigger"
gear:
  - Chase Bliss Lost & Found
  - Chase Bliss Clean
  - Akai MPC Sample
---

# Lost & Found → Clean Sidechain Reverb Gate

A huge shoegaze reverb wash that blooms and then gets *chopped in time* — the tail swells up and ducks rhythmically against an external kick. The trick is doing the gating with a **swell**, not a noise gate: Tape Op's sleeper Clean move keys the **Dynamic Swell** from an outside source so the swell engine opens and closes on the *trigger* instead of on your playing. Put a giant stereo Slow-verb wash in front of it and feed the kick from the MPC into Clean's 1/8" sidechain, and every kick hit re-opens the swell — the L&F wall pumps and re-blooms on the beat. This is a swelling reverb *gate*, softer and more musical than a hard gated reverb: the tail breathes back up between hits instead of slamming shut.

🟣 DOUG-designed integration; no artist played this exact chain. It chases the documented Tape Op "weird, swelling reverb gate" result and aims it at a shoegaze wash + an MPC kick. L&F-spotlight: the big stereo reverb is the star, Clean is the rhythmic chopper, the MPC is just the metronome that drives the gate.

## Signal path

guitar / synth → **CB Lost & Found — "Shoegaze Special"** (1A Slow-verb → 6A Ensemble Expander, SPREAD on, stereo wash) → **CB Clean — "Kick-Keyed Swell Reverb Gate"** (stereo in/out, Dynamic Swell, SIDECHAIN dip ON, MISO off, keyed by the MPC kick) → amp / interface (stereo).

Trigger send (parallel, audio only, not in the guitar path): **Akai MPC Sample — "Kick Sidechain Trigger Send"** kick one-shot → a dedicated MPC output → 1/8" TS cable → **Clean's sidechain input jack**. The MPC kick is never heard in the wet wash; it only *keys* Clean's swell. Run the MPC's main outs to the mixer separately if you want to hear the beat.

## Per-unit

- **CB Lost & Found — "Shoegaze Special" (REUSE):** the named CB combo, `L>R` series, **L = 1A Slow-verb** (the diffused reverberant bed — `MODIFY ~1:00` pre-diffusion feedback, `TIME ~1:00` medium-large size, `ALT diffusion ~2–3:00` smeared), **R = 6A Ensemble Expander** (~4 voices, slow Juno LFO) for the swirl, `BLEND ~1:00`, `MIX ~1:00–2:00`. **SPREAD ON · TRAILS ON.** This is the *wash* — keep it generous and stereo; the more sustained the bloom, the more there is for the gate to chop. Push `MODIFY(L)` up and `EQ` CCW (darken) for a heavier doom-leaning wall. This is the L&F-spotlight stage: it does all the reverb, Clean does none.
- **CB Clean — "Kick-Keyed Swell Reverb Gate" (NEW):** `SIDECHAIN dip ON`, `SWELL AUX off` (Dynamic Swell), `LATCH off`, `MISO off`, `SPREAD off` (the wash is already stereo from L&F — let Clean pass it stereo, don't re-collapse it). Engage the **AUX swell**: with SIDECHAIN on, the Dynamic Swell now triggers off the *keyed* MPC kick, not your guitar. `Sensitivity` is set by ear so each kick crosses the swell threshold (green LED flickers on the beat). On the **Hidden Options page** (hold both footswitches until LEDs go green): `Swell In time (Wet knob)` fairly fast so the tail re-blooms snappily on the hit; `Swell Out time (Dry knob)` set to taste for how the wash ducks back down between kicks — short Out = choppy gate, longer Out = gentle pulsing swell. `EQ / Dynamics` to taste underneath. *Unpublished:* exact knob positions are a dialable recipe — set them by ear (Tape Op documents the move, not the numbers).
- **Akai MPC Sample — "Kick Sidechain Trigger Send" (NEW):** a tight, punchy kick one-shot (`Mono`, `Amp Attack 0`, short `Decay`, Transient Knob FX for snap) routed to its **own output** so it can key Clean without being heard in the wet path. Program the kick at whatever subdivision you want the gate to pulse — four-on-the-floor for a steady chop, or a syncopated pattern for a stuttering bloom. This is the metronome that drives the whole gate.

## Routing

Two separate cables doing two separate jobs, and that split is the whole design:

1. **The audio chain is mono-or-stereo series, two boxes:** instrument → L&F → Clean → out. L&F builds the stereo wash (SPREAD on); Clean passes it stereo (MISO off, SPREAD off) and rhythmically swells it. The reverb lives *before* Clean on purpose — Clean is gating an already-wet wall, so the gate acts on the tail itself, not on a dry note that later gets reverb'd. That's what makes it a reverb *gate* and not just a tremolo on a dry signal.
2. **The trigger is a parallel audio send, not in the guitar path:** MPC kick → dedicated MPC out → 1/8" TS → Clean's sidechain jack. The kick is audio-rate key only; it controls Clean's swell envelope and is never summed into the wet output. Keep the MPC's musical outs going to the mixer separately so you still hear the beat.

**Gain-staging / why it works:** the swell engine is the gate. With SIDECHAIN on, Clean's Dynamic Swell opens on the external key instead of your playing, so each kick hit re-opens the wash and the gaps between hits let it duck. Set `Sensitivity` by the green LED so *every* kick crosses the threshold cleanly — too low and the gate stutters/misses hits, too high and it never closes (no chop). The Swell In/Out times are the rhythmic shape: In governs how fast the tail snaps back up on the hit, Out governs how far it ducks before the next one. If the chop sounds too hard/clicky, lengthen Swell Out; if it sounds mushy and never gates, shorten Swell Out and raise Sensitivity. Keep Clean's own compression gentle underneath — the *swell* is doing the gating, not the limiter, so you don't need to slam Dynamics.

## Sound

A vast, stereo, slowly-blooming shoegaze reverb that pulses and re-blooms in time — the wall swells up on each kick and ducks in the gaps, so the wash itself becomes rhythmic. Softer and more organic than a hard gated reverb: the tail breathes rather than slams. At fast Swell Out it's a choppy, stuttering reverb gate; at slow Swell Out it's a gentle tidal pulse on the wall.

**Taste-ref:** Slowdive / *Souvlaki*-scale reverb wash crossed with the "weird, swelling reverb gate" Tape Op names for Clean's sidechained swell — a my-bloody-valentine-sized bed that ducks on the beat instead of sitting static.

## Play

1. Start the MPC kick pattern; confirm Clean's green LED flickers on every hit (re-set `Sensitivity` if it misses or never closes).
2. Build the wash: hold a sustained chord/pad into the L&F Slow-verb and let it bloom to full size before you listen for the gate.
3. Feel the pulse — the wall now swells up on each kick and ducks between. Ride **Swell Out** (Dry knob, hidden page) live: short = choppy gate, long = gentle tidal swell.
4. Change the MPC pattern to change the rhythm of the bloom — four-on-the-floor for a steady pump, syncopation for a stuttering, glitchy gate.
5. For a build, push L&F `MIX` / `MODIFY(L)` up to grow the wall while the gate keeps it rhythmic; pull L&F `EQ` CCW to darken into doom territory. Bypass Clean's AUX swell to drop back to a static, ungated wash for the chorus.

## Sources

- **Basis:** 🟣 designed integration; chains **CB Lost & Found — "Shoegaze Special"** (factory combo, reused) + **CB Clean — "Kick-Keyed Swell Reverb Gate"** (created) + **Akai MPC Sample — "Kick Sidechain Trigger Send"** (created). The core move — keying Clean's Dynamic Swell from an external source feeding a reverb to make a "weird, swelling reverb gate" — is documented in the Clean "Swelling Reverb Gate — Vocal Sidechain Swell" sheet and its sources (Tape Op review + gearnews); here it's re-aimed at an MPC kick (rhythmic) instead of a vocal, with the reverb placed *before* Clean so the swell gates the L&F wall.
- Real-jack sidechain mechanics (SIDECHAIN dip ON, external key into the 1/8" TS input keys comp/EQ/swells; key from a drum machine / MPC) from the Clean "Real Sidechain — Kick-Ducked Pump" sheet and the Clean manual (Customize SIDECHAIN pp.34–35).
- Slow-verb → Ensemble Expander stereo wash from the L&F "Shoegaze Special" sheet (CB Field Guide named Combo). MPC kick one-shot snap (Mono / Attack 0 / Transient FX) from the Akai MPC "Snappy One-Shot" sheet.
- **Note:** unpublished knob positions in the two created patches (Clean Swell In/Out, Sensitivity; MPC decay/transient values) are a dialable recipe (DOUG's interpretation), not factory-published numbers. The *concept and routing* are sourced; the *exact values* are by-ear.
- `Research/Taste-Profile/taste-profile.md` (shoegaze wash lens)
