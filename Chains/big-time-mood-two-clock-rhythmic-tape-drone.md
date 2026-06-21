---
type: chain
title: "Big Time → MOOD Tape-Bait Octave-Down Drone"
date: 2026-06-15
artists: [Chase Bliss]
instrument: guitar / banjo
gear:
  - Chase Bliss Generation Loss
  - Chase Bliss Big Time
  - Chase Bliss MOOD MkII
  - Elektron Digitakt 2
---

# Big Time → MOOD Tape-Bait Octave-Down Drone ⭐

A rhythmic, already-degraded delay pattern grabbed by MOOD and warped an octave down into a pulsing tape drone. Generation Loss pre-ages the source, Big Time spins it into clock-locked lo-fi multitap repeats, and MOOD's Tape micro-looper snaps a slice of those repeats and drops it half-speed — so the grid you played turns into a slow, sub-heavy pulse that holds underneath you. One shared clock keeps the Tape loop length an even subdivision of the Big Time pattern, so the octave-down drone pulses *with* the repeats instead of smearing across them.

🟣 DOUG-designed integration. The Generation Loss and Big Time patches carry their own provenance; the MOOD patch is purpose-built for this chain (full spec saved alongside). The Taste-ref names the sound it chases.

## Signal path

Guitar / banjo → **CB Generation Loss — "Subtle Tape Age"** (near-always-on patina, breaks the source before the delay) → **CB Big Time — "Lo-Fi Rhythmic Groove"** (run MODE **Long/Mod** here for longer pre-rhythmic repeats, STATE Compressed, 0.5X ON, CLUSTER ~½, TIME slaved · CC54 sets the subdivision) → **CB MOOD MkII — "Tape-Bait Octave-Down Drone"** (Looper MODE **Tape**, MODIFY **0.5×** octave-down, SYNC LEFT, loop length on the shared grid via CC54) → amp / interface, stereo.

Off to the side, **Elektron Digitakt 2 — "DT2 MIDI / Clock-Master Rig Template"** is the clock master: its MIDI clock feeds Big Time (sets the delay subdivision) *and* MOOD (sets the Tape micro-loop length) so both pedals lock to one grid — the "shared clock" the whole move depends on. No audio runs through the Digitakt; it is purely the tempo brain. Mono in → Big Time **IN-L auto-engages MISO** (mono-in / stereo-out); everything from Big Time onward is stereo.

The only "real signal-order" invoked is the standard **degrade → delay → glitch-looper** placement (pre-age the source, establish the rhythmic repeats, then capture and warp them), not an artist-specific path.

## Per-unit

- **CB Generation Loss — "Subtle Tape Age":** the patina that everything downstream inherits. Wow ~10:00, Flutter just-below-audible, Saturate ~9:00, Failure ~8:00, Model 4 (Portamax-RT), Dry = Small. Leave it on under everything — a little goes a long way. Because it sits *first*, the Big Time repeats are already lo-fi before they're even clocked, which is exactly what makes them good MOOD bait: MOOD is then sampling pre-degraded material, so the octave-down drop reads as "old tape" rather than a clean pitch shift. *(Knob positions are the manual's labeled "nice and wistful" starting points distilled to clock-face — a faithful reading of intent, not factory-recallable numbers. On recall the pedal restores its real saved state.)*
- **CB Big Time — "Lo-Fi Rhythmic Groove":** the rhythmic engine and the MOOD bait. The saved patch is voiced MODE Short, but **for this chain run MODE Long (or Mod for warble)** so the repeats are long enough to give MOOD a meaty slice to grab — the patch's MODE field already lists Long as a valid option. STATE **Compressed** (keeps the multitaps punchy and stops the pre-degraded source running away), VOICING **Focus**, **0.5X ON** (first-party **12-bit** crush = the lo-fi grit), CLUSTER **~½** (the multitap pattern *is* the rhythm MOOD will sample), **COLOR ~40%** kept modest because Generation Loss already supplies saturation, FEEDBACK **~35%** (articulate, not washy so the rhythm stays legible for the looper), WET **~40%**. **TIME is slaved** to the DT2 clock; **CC54** sets the subdivision. *(Numeric fader positions are a designed interpretation of this patch's recipe — Chase Bliss publishes character, not numbers; on PC recall the motorized faders fly to the real saved values. STATE / 0.5X / CC54 / CC111 mechanics are sourced.)*
- **CB MOOD MkII — "Tape-Bait Octave-Down Drone"** (new, purpose-built): the capture-and-warp box. Looper MODE **Tape**, Wet MODE **Reverb** (a thin wash to glue the pulses; flip to **Delay** if you want the slice to also re-echo on-grid). Tape **MODIFY = 0.5×** (octave-quantized half-speed — the octave-down drop). **CLOCK kept higher** rather than slammed CCW, because aggressive low-CLOCK downsampling thins the bass fundamental and you *want* the octave-down weight to land; the grit comes from the already-degraded source, not from starving the clock. **SYNC = LEFT** (Micro-Looper synced to Wet) and feed **MIDI clock** so the Tape loop length is an even subdivision of the Big Time grid (CC51>0 to follow, CC54 sets the loop division). MIX ~1:00. Tap the **RIGHT (Micro-Looper)** footswitch to grab a slice of the running Big Time repeats; **hold LEFT to freeze** the Tape loop into a sustained pulsing drone, then ride **LENGTH** to resize the slice and **MODIFY** between 0.5× and 1× to flip the octave on the fly. ⚠️ A stray MIDI *Note* auto-engages Synth Mode (which ignores clock) — keep the Digitakt sending clock + CC only, no notes, to MOOD's channel.
- **Elektron Digitakt 2 — "DT2 MIDI / Clock-Master Rig Template":** the tempo brain. `SETTINGS → MIDI CONFIG > SYNC` → `CLOCK SEND` + `TRANSPORT SEND` ON; `PORT CONFIG` OUT PORT FUNC = MIDI. Unlike most Chase Bliss pedals, **Big Time has full-size 5-pin DIN MIDI (IN + THRU, default channel 2)** — so run the Digitakt's DIN OUT **directly into Big Time's DIN IN** (no TRS adapter, no CB MIDIBox). **MOOD**, by contrast, takes MIDI over **1/4" TRS**, so daisy-chain the clock onward from **Big Time's DIN THRU → a 5-pin-DIN-to-TRS lead (or CB MIDIBox) → MOOD**. Set the project tempo so the delay subdivision (CC54 on Big Time) and the Tape loop length (CC54 on MOOD) feel musical against each other — a 2:1 or 4:1 relationship makes the octave-down drone pulse cleanly under the repeats.

## Routing

**DT2 = clock master; Big Time and MOOD both follow** (CC111 ignore off on Big Time, CC51 follow on MOOD). Pick ONE master and never loop clock. This is a *two-pedals-on-one-clock* rig, which is the entire point: if MOOD's Tape loop length and Big Time's delay subdivision aren't locked to the same grid, the octave-down slice drifts against the repeats and you get smear instead of pulse.

**Gain-staging / grid discipline is the whole game:** Generation Loss already saturates, so keep Big Time **COLOR modest (~40%)** — too much COLOR over a pre-degraded source clamps the limiter "to porridge" and kills the transients MOOD needs to chop a clean rhythmic slice. Keep Big Time FEEDBACK articulate (~35%) so the multitap rhythm stays legible going into the looper — a washy bed gives MOOD nothing rhythmic to grab. On MOOD, **don't starve the CLOCK**: half-speed Tape playback already drops an octave, and low-CLOCK downsampling on top thins the very low end you're trying to feature. Mono source → Big Time IN-L auto-MISO for stereo spread out, so the octave-down drone sits in a wide field. If anything runs away, **hold MODE on the Big Time** for an instant clean reset.

## Sound

A rhythmic, already-degraded delay pattern gets snatched out of the air and dropped an octave into a slow, pulsing tape drone — the grid you played turns into a sub-heavy throb that holds underneath you, crusty and half-speed, locked to the same clock as the repeats still ticking over the top. Lo-fi, weighty, and hypnotic: a played rhythm captured in time and slowed into a bed.

**Taste-ref:** ambient / experimental — the Chase Bliss "capture-and-mangle" aesthetic (rhythmic Big Time repeats as ideal MOOD Tape fodder), with the octave-down weight of a half-speed tape loop. Hauschka / late-Tim-Hecker rhythmic-decay drones; the "tape running too slow" sub-pulse. ⚠️ The octave-down is real (Tape MODIFY 0.5×); the rhythmic lock is real (one clock, CC54 on both pedals).

## Play

1. Set the DT2 tempo and start the clock. Leave Generation Loss on under everything.
2. Play a rhythmic figure into Big Time (MODE Long/Mod) and let the clock-locked multitap pattern establish — back the guitar/banjo volume so the repeats are clean and legible, not slammed.
3. With the repeats running, **tap MOOD RIGHT (Micro-Looper)** to grab a slice of the pattern.
4. **Hold MOOD LEFT to freeze** the Tape loop, with MODIFY at **0.5×** — the captured rhythm drops an octave into a pulsing drone.
5. Ride **LENGTH** to resize the slice (longer = more of the pattern; shorter = a tighter throb) and flip **MODIFY** 0.5× ↔ 1× to drop or restore the octave live.
6. Solo or comp over the drone while the Big Time repeats keep ticking on top. To collapse: tap MOOD off, then **hold Big Time MODE to panic-reset** to a clean delay.

## Sources

- **Basis:** designed integration; chains **CB Generation Loss — "Subtle Tape Age"** + **CB Big Time — "Lo-Fi Rhythmic Groove"** + **CB MOOD MkII — "Tape-Bait Octave-Down Drone"** (new) + **DT2 — "DT2 MIDI / Clock-Master Rig Template."** Gen Loss pre-degrade propagating through downstream repeats from the "Subtle Tape Age" sheet; Big Time clock-locked multitap (CLUSTER as rhythm, COLOR-modest gain-staging over a degraded source, 0.5X = 12-bit crush, CC54 subdivision / CC111 ignore, MISO auto-engage) from the "Lo-Fi Rhythmic Groove" sheet and `gear/Chase Bliss Big Time/research/Big-Time-UsageGuide.md`. MOOD Tape octave-quantized MODIFY (.5×/1×/2×/4×), keep-CLOCK-higher-to-preserve-low-end, SYNC LEFT + MIDI clock (CC51/CC54), and Synth-Mode-ignores-clock caveat from the MOOD "Gritty Tape Loop", "Clock-Synced Loop Layer", and "SYNC" sheets (manual pp.17, 32–33). One-clock-master rig wiring from the DT2 clock-master template — but note Big Time takes **5-pin DIN** MIDI (DIN OUT → Big Time DIN IN direct; DIN THRU → TRS → MOOD), only MOOD uses 1/4" TRS MIDI.
- 🟣 designed (DOUG); knob values are dialable starting points, not published presets — see each patch sheet.
- `Patches/Chase Bliss Generation Loss/subtle-tape-age.md`
- `Patches/Chase Bliss Big Time/lo-fi-rhythmic-groove.md`
- `Patches/Chase Bliss MOOD MkII/tape-bait-octave-down-drone.md`
- `Patches/Elektron Digitakt 2/dt2-midi-clock-master-rig-template.md`
