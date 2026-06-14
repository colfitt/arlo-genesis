---
type: chain
title: Octatrack Capture-and-Destroy Break
date: 2026-06-14
artists: []
instrument: drums/sampler (MPC or Digitakt into Octatrack)
gear:
  - Akai MPC Sample
  - Elektron Octatrack MkII
  - JHS Colour Box V2
  - Chase Bliss Generation Loss
  - MXNHLT PORTA424
  - JHS 424
  - UA Apollo x8
---

# Octatrack Capture-and-Destroy Break

Sample the live drum/loop bus into the Octatrack, slice it, re-sequence it into a break the source never played, then crossfade clean-loop ↔ filter-swept-crushed-and-frozen — a performable recorded-wrong groove with one hand on the fader. A 🟣 DOUG-designed integration.

## Signal path

MPC Sample (or Digitakt) → Octatrack MkII inputs A/B → OT main out → JHS Colour Box V2 (line/XLR) → CB Generation Loss → PORTA424 → JHS 424 → tape.

## Per-unit

- **Octatrack MkII** — **#24 Fast Resampling Capture-and-Destroy** to grab the bus into a buffer at **LEVEL 127** (the anti-generation-loss rule), then **#11 Cuckoo Slice-Kit-from-a-Recording** to slice + keyboard-play it, **#12 LFO → STRT Slice-Walk** (RMP / SPD 33 / ×2 / DEPTH 16 / SYNC TRIG → dest STRT) to auto-march the 8 slices. Perform with **#15 Scene-Crossfade Performance** (Scene A = dry loop / Scene B = filter swept + Lo-Fi crushed + freeze-delay feedback high) and **#18 Beat-Repeat / Stutter Freeze** (master Delay LOCK=1, FB=127) for glitch-collapse stabs.
- **JHS Colour Box V2** — **#10 Drum-Bus / Stereo-Loop Crush** on the OT main out (PAD ON; HI for crush). For obvious console-fuzz stabs, **#3 Broken Console Preamp Fuzz** as a moment.
- **CB Generation Loss** — **#11 Demo-Crunch Cassette** (Model 7/10, DROP BYP on for a *consistent* warble) or **#31 Drunk-Drivers Dropout Demo (GL-LF3)** (Failure ramp + Bounce) when you want the dropout left audible as the hook.
- **PORTA424** — **#4 Mid-Voltage Edge-of-Breakup Workhorse** (Trim 12–1:00) — obvious-but-controlled cassette grit on the break.
- **JHS 424** — **#1 Subtle Always-On Tape Print** — finish + mono-commit (keep it light; PORTA424 carries the grit).

## Routing / sync

**OT must be clock MASTER to live-loop / live-resample reliably** (Pickup overdub misbehaves when OT is a MIDI clock slave). MIXER **DIR AB = 0** when running the bus through a Thru/Flex so you don't comb-filter dry-against-processed; capture via **CUE or scene-lock master Comp MIX=0** to avoid re-compression on resample. The OT main out is stereo → mono-sum into the Colour Box. The crossfader **Scene 1 empty = clean fader home** (PRESET MKII convention) so far-left = the untouched loop.

## Sound

A sliced, re-pitched, conditionally-mutating break that you can throw from clean to a filter-swept, bit-crushed, beat-frozen smear in one fader move, then degrade and print to cassette. Generative on its own — never loops identically.

## Play

Capture 4 bars, slice 16/auto, let the STRT-LFO walk the slices; ride the crossfader A↔B for the build, punch **[P/T8]** for stutter-freeze fills, fire a Gen Loss **#8 Momentary FAIL Punch-In** as chaos punctuation that the downstream Big Time/tape catches.

**Taste-ref:** lo-fi-prolific-volume break-flip craft + electronic-groove-first slice-mangle; the recorded-wrong groove as a live instrument. 🟣 designed.

## Sources

- **Basis:** designed integration; chains OT #24 + #11 + #12 + #15 + #18 + Colour Box #10 (or #3) + Gen Loss #11 (or #31 GL-LF3) + PORTA424 #4 + 424 #1. OT-must-be-master + LEVEL-127 + DIR-AB-0 + Comp-MIX-0 facts cited from OT #9/#24/#1; Scene-1-empty from OT #27.
- `Research/Taste-Profile/lo-fi.md`
- `Research/Chains/lo-fi-grooves.md` (C3)
