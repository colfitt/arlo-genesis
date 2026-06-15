---
type: chain
title: "Big Time → Lost & Found Punch-In Destroy Loop"
date: 2026-06-15
artists: [William Basinski]
instrument: "electric piano / guitar"
gear:
  - Chase Bliss Big Time
  - Chase Bliss Lost & Found
  - TE OP-1 Field
---

# Big Time → Lost & Found Punch-In Destroy Loop ⭐

A long looping delay that stays pristine when you play gently and crumbles in real time when you dig in — Basinski decay triggered by *your* dynamics, then captured and re-aged. The Big Time runs a long repeat whose misbias degradation is ridden by your picking envelope: feather it and the loop holds clean; hit harder and the repeats start to sag, drop out, and disintegrate. The Lost & Found re-grains the decayed loop and runs it back through Gen Lite so each pass arrives older. The OP-1 Field punches in and resamples the whole thing, stacking one more generation of loss.

🟣 DOUG-designed integration. No artist played *this* chain — the per-unit patches carry their own provenance, and the Taste-ref names the sound it chases (Basinski's *Disintegration Loops* — tape that destroys itself as it plays, here driven by dynamics instead of literal tape rot).

## Signal path

e-piano / guitar → **CB Big Time — "Dynamics-Crumble Long Echo"** (MODE Long, STATE #!&%, VOICING Warm; IN-L auto-**MISO** mono→stereo) → **CB Lost & Found — "Grain Tumbler → Gen Lite Re-Age"** (`L>R` series: Grain Tumbler 4B → Gen Lite 6B) → (resample) → **TE OP-1 Field — "Out-in loopback — generation-loss resample"** (punch-in record → re-age) → tape / DAW.

## Per-unit

- **CB Big Time — "Dynamics-Crumble Long Echo"** (new) — MODE **Long** (8–12 s repeats), STATE **#!&% (misbias)**, VOICING **Warm**, MOTION **Env** so your playing envelope drives the wobble depth. FEEDBACK high (~70%) for a sustaining loop; **COLOR LOW (~25–30%)** so gentle playing stays clean and only hard attacks push the misbias into audible sag/dropout; TEXTURE up (~60%, the misbias-sensitivity alt under COLOR) is what makes digging in *crumble*. TILT EQ a hair above noon to keep the decayed repeats from turning to mud. This is the dynamics-control-the-disintegration engine. *(Knob positions are a dialable recipe — CB publishes character, not numbers; flying faders override on recall.)*
- **CB Lost & Found — "Grain Tumbler → Gen Lite Re-Age"** (new) — ROUTING **`L>R` series**, L slot **4B Grain Tumbler**, R slot **6B Gen Lite**. Grain Tumbler re-chews the decayed Big Time loop into a longer, accumulating grain bed; Gen Lite (mini Generation Loss MkII) then re-ages it with wow/flutter and crinkle so the already-crumbling repeats arrive *older*. BLEND toward Gen Lite to set the re-age depth; **HOLD R FS = TAPE STOP** for a slowdown punctuation; LATCH + HOLD on the Grain Tumbler freezes a repeatable grain pattern to solo over. GLUE ~10–11:00 tames grain spikes. SPREAD off so Gen Lite reads as believable tape, not per-side chorus.
- **TE OP-1 Field — "Out-in loopback — generation-loss resample"** (reused) — punch-in record the L&F output to a **Porta** tape, then resample back via **OUT-IN loopback** (or the EAR — never mic, avoids feedback), re-record, repeat **2–3×**. Each pass stacks tape noise + generation loss for the final "recorded-wrong" generation. FADE OFF when sampling the row; new-tape UNDO (7 levels) lets you take risks while stacking.

## Routing

Mono e-piano/guitar → Big Time **IN-L auto-engages MISO** (mono-in/stereo-out); stereo from Big Time onward. Feed Big Time's wet into Lost & Found's L input for the `L>R` series re-grain → re-age. **Gain-staging is the whole game:** keep Big Time COLOR LOW so the misbias only bites on hard attacks — that's what preserves the pristine-when-gentle / crumbles-when-you-dig-in response. Don't double-degrade: Gen Lite (6B) *is* a mini Generation Loss, so it carries the tape-age — let the Grain Tumbler handle texture and Gen Lite handle the patina rather than maxing both. For the OP-1 pass, line out of L&F → OP-1 input; if the OP-1's line input sounds farty into instrument-level gear, knock the level down at the source. Watch double-compression on the OP-1 (master comp at record + comp on playback) when stacking passes.

## Sound

A clean, long looping delay that holds pristine under gentle e-piano/guitar and visibly disintegrates the harder you play — repeats sagging, dropping out, and crumbling in real time — then re-grained and re-aged so each generation sounds older than the last, finally captured to tape one more time. Decay you conduct with your hands.

**Taste-ref:** William Basinski, *The Disintegration Loops* — tape that destroys itself as it plays, but here the destruction is dynamics-triggered rather than literal oxide rot, then re-aged twice (L&F Gen Lite + OP-1 generation-loss loop).

## Play

Start gentle — sustain a chord on the e-piano and let the Big Time loop hold clean. Then **dig in**: hard attacks push the misbias into audible sag and dropout, and the loop starts to crumble under your hands. Lean back into soft playing and it partially recovers (Snyder's misbias sag-return). Once the loop has the decay you want, **LATCH + HOLD the Grain Tumbler** on the L&F to freeze a grain pattern, then **punch-in record on the OP-1** and resample. Re-record 2–3× to stack the final generations of loss. Use the L&F **R-footswitch TAPE STOP** as a slowdown gesture to end the loop.

## Sources

- Basis: designed integration; chains **Big Time "Dynamics-Crumble Long Echo"** (new) → **L&F "Grain Tumbler → Gen Lite Re-Age"** (new) → **OP-1 "Out-in loopback — generation-loss resample"**. Dynamics-control-the-disintegration via STATE #!&% (misbias) + MOTION Env + TEXTURE is from the Big Time misbias/Snyder sag-return notes (`gear/Chase Bliss Big Time` patch sheets + `sonicstate-superbooth-john-snyder-eae-interview.md`); low-COLOR-so-gentle-stays-clean gain-staging from `oceanic-drone-bed` / `crushed-analog`.
- Grain Tumbler map + Gen Lite re-age (6B = mini Generation Loss MkII, `L>R` series, SPREAD off for believable tape, LATCH+HOLD freeze, GLUE tames spikes) from `gear/Chase Bliss Lost & Found` patch sheets (`grain-doubler-clock-locked-grain-mill.md`, `light-sleeper-recorded-wrong-vhs-swell.md`) + BachelorMachinesTV Pt2.
- OP-1 OUT-IN loopback generation-loss method from `Patches/TE OP-1 Field/out-in-loopback-generation-loss.md` (ADG walkthrough + OP-1-Field-UsageGuide §5).
- Taste-ref: William Basinski, *The Disintegration Loops*.
