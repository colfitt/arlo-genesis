---
type: chain
title: "Samplers → Big Time Line-Level Centerpiece Send"
date: 2026-06-15
artists: [LCD Soundsystem, Boards of Canada]
instrument: OP-1 Field / synth / sampler
gear:
  - TE OP-1 Field
  - EHX Effects Interface
  - Chase Bliss Big Time
---

# Samplers → Big Time Line-Level Centerpiece Send ⭐

The minimal, line-level version of the centerpiece move: a whole OP-1/synth part runs through one saturating stereo delay as a clean wet-only aux send. No fuzz, no front board — just the sampler, the line-matching bridge, and Big Time set up the way Chase Bliss built it ("the perfect centerpiece for a synth setup," balanced + unbalanced stereo I/O, meant to take line-level sources). DRY KILL turns the pedal into a pure wet return; Program Changes recall song-section presets hands-free so the delay re-voices itself through the arrangement while you play.

🟣 DOUG-designed integration. No artist played this exact chain — the per-unit patch refs carry their own provenance, and the Taste-ref names the sound it chases.

## Signal path

**OP-1 Field** (line-level OUT, stereo — running **OP-1 Field — "Dimension — virtual-analog clean pad bed"**) → **EHX Effects Interface** (Pedalboard/line→instrument mode, the rig's confirmed line-matching path) → **Big Time IN-L/IN-R** (running **CB Big Time — "Line-Level Centerpiece Send"**, COLOR low, **DRY KILL** for wet-only return, MIDI clock shared) ← **OP-1 (or sequencer) MIDI** drives clock + Program-Change scenes → Big Time stereo OUT into the board/aux return.

## Per-unit

- **OP-1 Field — "Dimension — virtual-analog clean pad bed"** — the Field-exclusive virtual-analog engine, kept deliberately clean (slow attack, long release, built-in stereo chorus width up) so all the character is applied downstream by the delay. Recorded/played clean; the OP-1's OUT is line level and goes "farty/muddy/quiet" straight into instrument-level gear, so it must hit the EHX bridge first. The same engine doubles as the lead or bass when the song needs it — one part, one send.
- **EHX Effects Interface** — passive-feeling line↔instrument bridge (no patch; it's a USB/level utility). Here it does the one job the OP-1 → Big Time path documents: reconcile the OP-1's line output down to instrument level so Big Time's preamp sees a clean, properly-staged source. Keep it stereo (2-in/2-out). Buffered bypass.
- **CB Big Time — "Line-Level Centerpiece Send"** — the unifying delay, configured for a line source feeding a wet-only aux: STATE **Saturated** (the "one saturating character" the whole part inherits), **COLOR low** (line sources are already hot — too much COLOR slams the analog limiter to porridge), **DRY KILL ON** (Options) so the pedal returns 100% wet, slaved to shared MIDI clock (CC111 = 0), and song sections recalled by **Program Change** (PC# = slot, PC 0 = LIVE).

## Routing

The whole point is gain-staging a **line-level** source into a pedal that was designed for exactly that. Big Time takes line-level/balanced input on a 1 MΩ stereo front end, but the OP-1's specific output behaves badly into instrument-level gear, so the **EHX Effects Interface sits between them** as the documented level fix (OP-1 guide §5/§7). Once levels are right: keep **COLOR low** because the source is already hot ([R] in the centerpiece source), and switch on **DRY KILL** so Big Time returns **wet only** into a parallel/aux path — the cleanest possible centerpiece send (the dry stays in the desk, the delay character lives on its own fader). Clock is shared: feed MIDI from the OP-1 or the rig sequencer into Big Time's **native 5-pin DIN** (no MIDIBox needed), set **CC111 = 0** so Big Time follows, and **pick exactly one clock master — never loop clock.** Song-section recall: save a preset per section (CC27 = slot), then fire **Program Changes** (from a sequencer MIDI track or the OP-1) on section changes — the delay re-voices verse→chorus→outro hands-free. Put Big Time on the shared CB channel (default ch.2) if you later want one PC to jump a whole CB stack at once.

## Sound

A whole synth/sampler part unified through one saturating stereo delay character — sketch-to-finish glue. Because the dry is killed, the delay isn't an effect *on* the part, it *is* the part's printed voice on the aux: a saturated, COLOR-warmed stereo bloom that stays coherent from a quiet sketch to a finished mix because everything passes through the same character.

**Taste-ref:** electronic / synth-centerpiece — the LCD-style "one rig, one delay voice" backbone, with a Boards-of-Canada saturated-tape warmth on the wet return. The wet-only aux structure is mix-engineer territory (delay-throw on a send), built for sketch-to-finish reuse.

## Play

Play the part clean on the OP-1; the saturated wet return does the gluing. Ride **WET** (or the aux fader) to swell the delay in for choruses. Tap a **Program Change** on each section to jump the delay's voice (verse → chorus → outro) without touching the pedal. For an outro, recall a longer/higher-feedback section preset and let it bloom — or hold the **RIGHT footswitch to FREEZE** the last phrase into a held bed and play the next idea over it. Hold **MODE** to panic-reset to a clean delay if a section preset runs hot.

## Sources

- **Basis:** designed integration; chains **OP-1 Field "Dimension — virtual-analog clean pad bed"** + **EHX Effects Interface** (line→instrument bridge) + **Big Time "Line-Level Centerpiece Send"**. Line-level OP-1 → EHX → Big Time path, COLOR-low for hot line sources, DRY KILL = wet-only aux, native-DIN clock (CC111/CC54), and section-recall via Program Change all from the centerpiece source file §C [V/R].
- `gear/Chase Bliss Big Time/research/links/centerpiece-minimal-chains-and-sampler-integration.md` §C (OP-1 → EHX → Big Time levels; DRY KILL wet-only; CC111/CC27/PC recall)
- `gear/EHX Effects Interface/GearProfile.md` (line↔instrument bridge, modes, 2-in/2-out)
- `Research/Taste-Profile/electronic.md`
