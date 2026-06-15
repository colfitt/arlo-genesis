---
type: chain
title: "Big Time Lo-Fi Rhythmic Groove Engine"
date: 2026-06-15
artists: [LCD Soundsystem, Boards of Canada]
instrument: "synth stabs / drum machine (Akai MPC Sample)"
gear:
  - Akai MPC Sample
  - Chase Bliss Big Time
---

# Big Time Lo-Fi Rhythmic Groove Engine ⭐

A bit-crushed, multitap, clock-locked stereo delay groove where the **CLUSTER taps ARE the rhythm** — not an ornament on a beat, but the beat itself. The MPC fires sparse synth stabs and the Big Time fans them into a 12-bit percussive pattern that breathes: Compressed ducking keeps the repeats punchy and articulate until you stop playing, then the cloud collapses. CLUSTER is a free arrangement fader — slide it to add or strip taps without touching the sequence — and MPC Program Changes recall verse/chorus voices hands-free.

🟣 DOUG-designed integration. No artist used this exact two-box chain — the per-unit patch refs carry their own provenance, and the Taste-ref names the sound it chases.

## Signal path

**Akai MPC Sample** (clock MASTER) → MIDI clock + Program Change → **CB Big Time** (follows). Audio: MPC stereo out → **CB Big Time — "Lo-Fi Rhythmic Groove"** (MISO/stereo) → tape / interface. Two boxes, one grid.

## Per-unit

- **Akai MPC Sample — "Stab Sequencer — Clock Master + PC Scene Recall"** *(new)* — sparse synth-stab / drum-machine voices sequenced on a half-bar grid, running as **MIDI clock master** so its MIDI-slave distortion bug never bites. Program Change messages recall **verse / chorus / breakdown** scenes (different stab voice + pattern) hands-free as the song moves. This is the *source* — deliberately sparse, because the Big Time is going to multiply it.
- **CB Big Time — "Lo-Fi Rhythmic Groove"** *(reused)* — MODE **Short**, STATE **Compressed** (the duck that keeps taps punchy and articulate until you stop), VOICING **Focus**, MOTION **Off**, **0.5X ON** (the 12-bit lo-fi crush), **CLUSTER ~½** (the multi-tap pattern = the rhythm), TIME **slaved to MIDI clock** with subdivision set by **CC54** (1/2-bar / dotted-8th to taste), FEEDBACK **~35%** (articulate, not washy), WET **~40%**, TILT EQ slightly up, SPREAD **ping-pong** so the added taps fan L/R. **CC111 = 0** so the pedal follows the MPC clock.

## Routing

**MPC = clock master, Big Time = follower.** This direction is mandatory, not stylistic: the MPC Sample distorts audio when it is *slaved* on fw 1.2.1 (verify the 1.3.x fix before trusting it the other way), and slaving the Big Time is the clean path anyway. Set Big Time **CC111 = 0** (clock-ignore off) so it locks to incoming clock; **CC54** sets the tap subdivision against the MPC grid — park it around a 1/2-bar / dotted-8th feel so the taps land *between* the stabs and read as the groove. Stereo throughout: the MPC's stereo out feeds the Big Time stereo ins (or a mono stab auto-engages MISO mono-in/stereo-out), and SPREAD ping-pong scatters the cluster across the field.

**Gain-staging / the "breathe":** the whole trick is the Compressed STATE. With CLUSTER high, a Digital or Saturated delay would smear the taps into mush — Compressed ducks each repeat so the pattern stays percussive and *stops sounding* once you stop playing, which is what makes CLUSTER usable as rhythm instead of wash. Keep WET around 40% so the dry stabs still define the downbeats; push WET past the stabs only when you want the delay pattern to *become* the part. Don't over-feed FEEDBACK — at this CLUSTER density ~35% is already a full bar of taps; more just turns the groove into a drone.

**Scene recall:** save the Big Time patch to a free internal slot via **CC27**, and let MPC Program Changes drive both its own scene *and* (optionally) a Big Time PC recall on the section change, so verse → chorus flips the stab voice and the delay character on the same downbeat, hands-free.

## Sound

A clock-locked, bit-crushed stereo groove built entirely out of delay taps — sparse stabs in, a punchy 12-bit percussive pattern out, ducking in time so it stays articulate and dies when you stop. CLUSTER is the live "more rhythm / less rhythm" fader; the MPC's Program Changes move the arrangement underneath it.

**Taste-ref:** electronic / groove-first lo-fi — LCD Soundsystem's machine-locked percussive delays meeting Boards of Canada's crushed, clock-tight tape-grid feel. The taps-as-rhythm move (CLUSTER as a free arrangement fader) is the centerpiece gesture here, not an effect on top of a finished beat.

## Play

Start the MPC (it's the master); play / trigger a sparse stab pattern and let the Big Time fan it into the groove. **Ride CLUSTER** as your live arrangement fader — back it off for the verse so you mostly hear the stabs, slide it up into the chorus so the taps swarm into a full percussive pattern. Send a **Program Change** at the section boundary to flip verse/chorus stab voices hands-free; if you've parked a Big Time PC on the same message, the delay character flips with it on the downbeat. Stop playing to let the Compressed duck collapse the cloud — that silence *is* the arrangement. Hold the Big Time's mode footswitch as the panic-reset back to a clean delay if the grid ever runs away from you.

## Sources

- **Basis:** designed integration; chains **Akai MPC Sample — "Stab Sequencer — Clock Master + PC Scene Recall"** (new) + **CB Big Time — "Lo-Fi Rhythmic Groove"** (reused). CLUSTER-as-arrangement-fader, Compressed-keeps-taps-punchy, 0.5X crush, and clock-lock via CC54 / CC111=0 from the Big Time patch and `centerpiece-minimal-chains-and-sampler-integration.md` §C. MPC-as-clock-master (fw 1.2.1 slave-distortion bug → MPC must be master) from the same source + Big Time "Lo-Fi Rhythmic Groove" warning. CC27 slot-save + PC scene recall from the centerpiece sampler-integration notes.
- ⚠️ **Honesty:** the Big Time numeric knob positions are a dialable recipe interpreting Chase Bliss's published character (CB publishes character, not numbers; recall flying-faders override). MPC stab-voice / scene specifics are designed craft on AC50-confirmed controls, not a documented artist patch.
- `Gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md`
- `Patches/Chase Bliss Big Time/lo-fi-rhythmic-groove.md`
- `Research/Taste-Profile/electronic.md`
