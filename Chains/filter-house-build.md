---
type: chain
title: Filter-House Build
date: 2026-06-14
artists: [Daft Punk, LCD Soundsystem]
instrument: synth/sampler + banjo/baritone (VG-800)
gear:
  - Novation 61SL MkIII
  - Elektron Octatrack MkII
  - Akai MPC Sample
  - Elektron Digitakt 2
  - Roland VG-800
  - Chase Bliss Clean
  - MXR M173 Classic 108 Fuzz
  - EarthQuaker Devices Hizumitas
  - Chase Bliss Big Time
  - MXNHLT PORTA424
  - JHS 424
  - UA Apollo x8
---

# Filter-House Build

Groove-first, additive, filter-house — a 2–4-bar loop locked and never changed while **filter cutoff automation opens it over a long build**, a bouncing acid bass underneath, the four-on-the-floor pump, SP-1200 grit, a glided Da-Funk banjo lead, into the centerpiece delay and tape. The LCD "lock one loop, add layers across minutes" build + the Daft Punk "vary the timbre, not the notes" filter sweep, with the cued **Dance Yrself Clean** explosion as a Part switch.

This is a **designed integration** — no artist ever used this exact chain. Real method = CS-60/SH-101/808/909 & Juno-106/MKS-80/TB-303/SP-1200 in Pro Tools/Logic — none of this rig. ⚠️ pump = emulation; vocoder/talkbox = not achievable. 🟣 designed.

## Signal path

*Sequence/clock plane* — **61SL MkIII** (clock master + filter-cutoff ride) → **Octatrack MkII** (the locked loop + crossfader filter sweep) + **MPC Sample** (909/808 backbone) + **Digitakt** (optional).

*Audio* — Octatrack/MPC stereo out → Apollo bus (the loop/drum body); **VG-800** banjo/baritone lead + acid bass → **CB Clean** → MXR 108 → **Hizumitas** (the overdriven-guitar read for the Da Funk lead) → Board 3 → **Big Time** (clock-locked tempo-synced delay, the centerpiece) → **PORTA424 → JHS 424** tape → Apollo print.

## Per-unit

- **61SL MkIII** — **#14 Filter-Cutoff Ride + Pump-CC Template** (enc1 → filter CUTOFF CC = the slow open/close build · fader1 → a pump-CC / a CC ramp that ducks on each beat · enc2 → RESONANCE · Fader Pickup ON · **SL = clock master, Tx On**). Drives the VG-800 SYNTH cutoff (CONTROL ASSIGN, CC#1–31 window) or the OT's FX cutoff CC. For the explosion, layer **#15 Dance-Yrself-Clean Cued-Explosion Session** (Part 1 sparse vamp held ~3 min → cued Part 2 slam on the downbeat).
- **Octatrack MkII** — **#28 Filter-House Crossfader Open/Close** (disco/funk loop or a resampled banjo/VG figure on a Flex track, LOOP ON · FX1 = multimode resonant filter, FX2 = delay · **Scene A = filter CLOSED, Scene B = filter OPEN** — throwing the crossfader A→B *is* the build · slow LFO → cutoff under it · **Lo-Fi bit reduction for SP-1200 grit**) + **#30 One-Loop Additive Long Build** (lock ONE loop, never change it; add tracks across minutes; stage the explosion as a cued Part switch). Pump via **#29 4-on-the-Floor Sidechain-Pump Loop** (input compressor or LFO-ramp → AMP volume, WAVE=RAMP, synced 1/4, retrigged on the kick step). ⚠️ no true sidechain key — the pump is faked.
- **MPC Sample** — **#29 4-on-the-Floor 909/808 Kit + Cowbell** (tuned to the song key so it locks to the baritone sub · Swing 54–58% for the dirty-909 shuffle · Transient FX on the kick) and/or **#30 Resample-the-Synth-for-Drums** (synthesize the kit from a VG-800/OP-1 voice and resample it in = the "Get Innocuous!" DFA method, AC50-mapped). ⚠️ Resample is silent the first try — do it twice. Run **MPC as clock master OR slave carefully** — fw1.2.1 MIDI-slave distorts; on fw1.3.x verify, else let the MPC follow.
- **VG-800** — **#34 Da Funk Band-Passed Portamento Lead** for the banjo lead (SYNTH/SOLO, portamento ON = the slide in 4ths, FILTER CUTOFF mid + TOUCH SENS up = the band-passed wah) + **#35 Around-the-World Acid Filter-Bass** in BASS mode for the bouncing baritone bass (FILTER CUTOFF ~50 low, RESO ~60 high, FILTER DECAY ~25 snappy pluck). Ride the bass cutoff open over the build (or let the 61SL/OT do it).
- **CB Clean** — **#13 Pseudo-Sidechain Bus Limiter** if you want the whole VG/loop bus to pump with the kick (Dry down, Dynamics into limiting, fast/fast, cut lows so bass doesn't over-trigger — Ricky Tinez's documented house move) — best when Clean is redeployed to a stereo end slot; or keep #1 *Home Base* at the front for the lead.
- **MXR 108 + Hizumitas** — **108 #5 Stacked Fuzz Booster** (low fuzz, high output) → **Hizumitas #5 Balanced Mid-Forward Lead** so the Da Funk banjo lead reads like an overdriven guitar (the MS-20 / Juno-into-Fat-Cat colour). Only on the lead — not the loop.
- **Big Time** — **#2 Lo-Fi Rhythmic Groove (clock-locked)** (MODE Short · STATE Compressed · 0.5X ON for SP-1200-ish crush · TIME = MIDI clock via CC54 dotted-8th/16th · CLUSTER multi-tap = the groove · FEEDBACK ~35% articulate · SPREAD ping-pong). The tempo-synced stereo delay (1/8 L, dotted-1/8 R) the filter-house sources call for. ⚠️ MPC distorts when slaved on fw1.2.1 — run MPC master or Big Time master, not both.
- **PORTA424 #1 + JHS 424 #1** — tape glue on the bus for the SP-1200-at-45rpm grit lineage.

## Routing / sync

**61SL = clock master (Tx On)**, 24 PPQN to the OT, MPC, Digitakt and (via CC54) Big Time — one tempo for the four-on-the-floor; everything follows. **Never Tx AND Rx clock at once; feed clock on USB or DIN, not both.** The OT crossfader is the live filter-house controller (Scene A↔B), the 61SL enc1 the alternate cutoff ride. The pump is the **emulation** (LFO-ramp on track volume / OT input comp — no DAW-style sidechain key). The build is **arrangement** (add layers / cued Part switch) for LCD, **filter sweep** for Daft Punk — do both. Saturate the drop arp (Hizumitas) for the Dance-Yrself-Clean explosion. ⚠️ **No vocoder/talkbox on the rig** — the robot-voice option (VG-800 #36, filter-modulated carrier) only fakes the *result*.

## Sound

A locked disco/banjo loop that opens from a filtered murmur to a full-spectrum four-on-the-floor groove over minutes, pumping on the kick, an acid baritone bass bouncing under it, a glided overdriven banjo lead on top, tempo-synced ping-pong delay, SP-1200 grit, printed to tape — then a cued explosion slams the full kit + a saturated saw arp in on the downbeat.

## Play

61SL starts the room. Lock the OT loop and *never touch the notes* — only the filter. Throw the crossfader (or ride enc1) to open the cutoff over the build; bring MPC layers in one at a time. At the boundary, fire the **cued Part switch (OT-E3 / 61SL-E2)** to slam the explosion in on the downbeat. Carry the Da Funk banjo lead on the VG-800 (melody in 4ths, portamento). Ride Big Time WET for dub throws.

## Taste-ref

Daft Punk — "Around the World" / "Da Funk" filter-house, acid-pluck bass, glided band-passed lead; LCD Soundsystem — "All My Friends" one-loop additive build, "Dance Yrself Clean" withhold-then-explosion; the DFA resample-the-synth-for-drums method.

## Sources

- **Basis:** designed integration; chains **61SL #14/#15** + **Octatrack #28/#29/#30** + **MPC #29/#30** + **VG-800 #34/#35/#36** + **Clean #13** + **108 #5** + **Hizumitas #5** + **Big Time #2** + **PORTA424 #1** + **JHS 424 #1**. Pulls the electronic index "filter-house build" + "LCD additive long build" + "Da Funk banjo lead" chains into one path. Real method = CS-60/SH-101/808/909 & Juno-106/MKS-80/TB-303/SP-1200 in Pro Tools/Logic — none of this rig.
- `Research/Taste-Profile/electronic.md`
