---
type: chain
title: Digitakt Crushed Loop → Console → Tape
date: 2026-06-14
artists: [Daft Punk, LCD Soundsystem]
instrument: synth (Digitakt loop)
gear:
  - Elektron Digitakt 2
  - Chase Bliss Clean
  - JHS Colour Box V2
  - Chase Bliss Generation Loss
  - MXNHLT PORTA424
  - JHS 424
  - UA Apollo x8
---

# Digitakt Crushed Loop → Console → Tape

A locked Digitakt loop whose timbre opens and closes over a long build, run through the Neve console front end and printed to cassette — the filter-house move wearing a recorded-wrong coat. A 🟣 DOUG-designed integration; the sidechain is an LFO/limiter approximation (no true sidechain key on the DT2; Clean fakes it on the bus), flagged.

## Signal path

Digitakt 2 (main out, stereo) → CB Clean (end-of-chain bus role) → JHS Colour Box V2 (XLR/line, PAD on) → CB Generation Loss → PORTA424 → JHS 424 → tape.

## Per-unit

- **Digitakt 2** — **#32 Filter-House Loop (open/close cutoff sweep)** as the timbre engine: 2–4-bar loop, LOOP ON, multimode FILTER low + RES high-not-screaming, **LFO → FILTER FREQUENCY** triangle very slow (one cycle over many bars) + a touch of **BIT REDUCTION** for SP-1200 grit; pair **#23 Ambient Send-FX** (ping-pong delay ~88 / dark reverb ~90) for depth. Clock-master template = **#29 DT2 MIDI / Clock-Master Rig Template**.
- **CB Clean** — **#13 Pseudo-Sidechain Bus Limiter** (Ricky Tinez) end-of-chain so a hot kick ducks the whole bus = the dance pump without a sidechain jack (Dry down, cut lows so bass doesn't over-trigger). Requires redeploying Clean to a stereo end slot.
- **JHS Colour Box V2** — **#10 Drum-Bus / Stereo-Loop Crush** (XLR input mandatory, PAD ON, HI for crush / LO for glue, HI-PASS ~9:00 so the low end doesn't pump) — the broken-console saturation on the loop bus.
- **CB Generation Loss** — **#10 Filtered Lo-Fi / "AM Radio" Small-Speaker Bed** (Model 7–9, band-limited, mid-forward) so the loop sits like a broken radio, OR **#1 Subtle Tape Age** for lighter patina.
- **PORTA424** — **#1 Always-On Cassette Print** (Trim 9:00, 18V) for clean cassette glue, or **#12 Bedroom 4-Track Demo Print** if you want the grit obvious.
- **JHS 424** — **#1 Subtle Always-On Tape Print** (Gain 1 9:00, Gain 2 10:00) — finish + mono-commit to Apollo; let PORTA424 carry tone.

## Routing / sync

**Digitakt = clock master** (CLOCK + TRANSPORT SEND on); its LFO-on-cutoff is the build, locked to the grid. The Colour Box is a **MONO device** — sum the DT2 stereo to mono into it (or process the bus mono). Clean redeployed to a **stereo end slot** for the pseudo-sidechain to pay off; the kick run a touch hot so it pushes the bus down each hit. Don't crank both tape boxes — PORTA424 = the tape here, 424 = level only.

## Sound

A four-on-the-floor (or motorik) loop that breathes open across minutes, ducking on the kick, saturated through a broken Neve and dulled to a small-speaker cassette bed — groove-first but recorded-wrong.

## Play

Start the loop, ride the DT2 filter cutoff open over the build (or let the slow LFO do it), bring layers in with **#25 Hands-Free LAST/NOT-LAST Auto-Fill** so the box plays its own transitions while both hands ride pedals. Foot the Colour Box from glue (LO) to crush (HI) at the drop.

**Taste-ref:** electronic-groove-first (Daft Punk filter-house / LCD pump) filtered through the lo-fi degrade arc. 🟣 — the sidechain is an LFO/limiter approximation (no true sidechain key on the DT2; Clean fakes it on the bus), flagged.

## Sources

- **Basis:** designed integration; chains DT2 #32 + #23 + #29 + Clean #13 + Colour Box #10 + Gen Loss #10 (or #1) + PORTA424 #1 (or #12) + 424 #1. The DT2-no-true-sidechain flag is from DT2 #33; Colour-Box-is-mono + line-level/PAD from Colour Box #10.
- `Research/Taste-Profile/lo-fi.md`
- `Research/Chains/lo-fi-grooves.md` (C2)
