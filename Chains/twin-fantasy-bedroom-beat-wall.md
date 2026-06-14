---
type: chain
title: Twin-Fantasy Bedroom Beat Wall
date: 2026-06-14
artists: [Car Seat Headrest]
instrument: banjo/VG-800 + MPC drums
gear:
  - Akai MPC Sample
  - Chase Bliss Clean
  - JHS Colour Box V2
  - Oxford Drive
  - Strymon Deco V2
  - Chase Bliss Generation Loss
  - Chase Bliss Big Time
  - MXNHLT PORTA424
  - JHS 424
  - UA Apollo x8
---

# Twin-Fantasy Bedroom Beat Wall

The "the demo IS the song" dense bedroom wall — an MPC-driven crunchy-dry beat under a banjo/VG-800 part, layered "as big as possible," every wart left audible, double-cassette-printed. A 🟣 DOUG-designed integration; Toledo used a laptop DAW + bundled mic, not pedals — this chases the *result*, not the signal path.

## Signal path

- **Drum/loop backbone:** MPC Sample → Apollo bus (its own degrade baked in) → summed into the End-board print.
- **Melodic part:** banjo/VG-800 → CB Clean (always-on) → JHS Colour Box V2 → Oxford Drive (relocated front) → Strymon Deco V2 → [End board] CB Generation Loss → CB Big Time → PORTA424 → JHS 424 → tape (PORTA424/424 print).

## Per-unit

- **MPC Sample** — runs **#14 Bake-the-Grit Resample (SP1200/MPC60 Authentic Crush)** on the breaks (pitch up +6 → Vintage Emulator SP1200 → Resample → tune back −6) + **#15 LoFi (Bitcrush + Decimate)** latched with **#16 Color (Cassette)** on a couple of hits (DIBIA$E's latch); finger-drummed with **#28 Dilla Feel (Quantize-Off micro-timing)** so it never machine-guns.
- **CB Clean** — **#1 Home Base (Safe Space)**, the always-on leveler; bump to **#5 Banjo Transient Tamer** when the banjo carries the part so plucks behave like guitar before the dirt.
- **JHS Colour Box V2** — **#15 Crunchy-Dry Direct-In (CBX-LF1)** — "boost a quiet source until it clips" = Toledo's recorded-quiet-then-boosted crunch. HI · STEP 3 · PRE-VOL 1:00 · MASTER set LAST. Keep it DRY downstream.
- **Oxford Drive** — **#OXF-LF1 Crunchy-Dry Demo Crunch (DS-2 character)** ('91 / Si / Gain 11–12:00 / Bass 8:00 / Contour 9:00 / Treble 1:00). **Relocate ahead of the fuzzes** (or guitar/banjo-only into the End board) so its fixed-mid filter isn't collapsed by the wall.
- **Strymon Deco V2** — **#16 Cassette Demo Fatten + Wobble (DEC-LF2)** — Voice cassette, bounce doubler, to layer the part "as big as possible" before the ruin.
- **CB Generation Loss** — **#29 Laptop-Bounce Cassette Demo (GL-LF1)** (Model 7 Dictatron-EX, Wow/Flutter 9:00, Saturate 11:00, Failure 9:00 with DROP BYP on, Dry Small). Keep hidden Hiss low + HUM BYP so it doesn't stack a 2nd noise floor into the print.
- **CB Big Time** — **#1 Crushed Analog (Factory #7)** — murky/saturated vintage echo right after Gen Loss; COLOR modest (the source is already degraded), 0.5X ON for the 12-bit crush.
- **PORTA424** — **#12 Bedroom 4-Track Demo Print (P424-LF1)** (Trim 12–1:00 the breakup gate, Treble 10:00, 9V trashier).
- **JHS 424** — **#13 Demo-Is-The-Song 4-Track Grit (424-LF1)** (Gain 1 12:00, Gain 2 12:00 — **well under the 3:00 gate**), XLR → Apollo, mono-commit.

## Routing / sync

**MPC = MIDI clock MASTER** (mandatory — MIDI-slave distortion on fw1.2.1; MPC master also keeps Big Time from distorting when slaved). Big Time follows via **CC111=0**; subdivision via **CC54**. Mono melodic path → Big Time IN-L auto-engages **MISO** (mono-in/stereo-out). H90 not in this chain; the stereo End bus mono-sums into PORTA424's mono input, then JHS 424 mono-commits to the Apollo. **Pick one tape box to destroy** — here PORTA424 carries the demo grit (9V), JHS 424 stays light (just level + XLR). Gain-staging: Colour Box MASTER set last (biggest jump); Deco is a gain device (level-match on engage).

## Sound

A dense, dry, mid-forward bedroom wall — crunchy direct-in part doubled and fattened, drums crushed to 12-bit SP1200 grit, the whole thing bounced through two cassette stages so chords smear and single notes bloom. Warts as identity.

## Play

Lay the MPC beat, hold the banjo/VG part and layer multiple passes (resample on the OT or MPC for the "as big as possible" stack). Footswitch the Oxford in for the dirty sections; ride Colour Box PRE-VOL by hand for the recorded-quiet-then-boosted swell into clipping. Leave everything DRY — no long verb.

**Taste-ref:** lo-fi-prolific-volume — Car Seat Headrest, *Twin Fantasy* / "Something Soon" bedroom-DAW degrade ("the demo is the song"). 🟣 chases the result; Toledo used a laptop, not pedals.

## Sources

- **Basis:** designed integration; chains MPC #14/#15/#16/#28 + Clean #1/#5 + Colour Box #15 (CBX-LF1) + Oxford OXF-LF1 + Deco #16 (DEC-LF2) + Gen Loss #29 (GL-LF1) + Big Time #1 + PORTA424 #12 (P424-LF1) + 424 #13 (424-LF1). Mirrors `Research/Taste-Profile/lo-fi.md` § "Something Soon / Twin Fantasy bedroom wall." MPC-master + Big-Time-slave-distortion facts cited from MPC sheet header + Big Time #2 note.
- `Research/Taste-Profile/lo-fi.md`
- `Research/Chains/lo-fi-grooves.md` (C1)
