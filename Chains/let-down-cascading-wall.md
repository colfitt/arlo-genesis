---
type: chain
title: Let Down Cascading Wall
date: 2026-06-14
artists: [Radiohead]
instrument: banjo (GK-5 → VG-800)
gear:
  - Roland VG-800
  - Chase Bliss Clean
  - Chase Bliss Generation Loss
  - Chase Bliss Big Time
  - Chase Bliss Blooper
  - Eventide H90
  - MXNHLT PORTA424
  - JHS 424
  - UA Apollo x8
---

# Let Down Cascading Wall

The OK Computer marquee — Jonny's cascading arpeggio *doubled an octave up + a third Jazzmaster layer* into a Phil-Spector wall, the 5/4-against-4/4 Reich phasing, dying into the St Catherine's ballroom reverb. One banjo/guitar arpeggio line becomes a shimmering, tape-warped, octave-stacked multi-tap cascade in a long hall. The one chain that **resists the degrade tie-breaker** — the jangle is the hook, so it stays bright.

This is a **designed integration** — no artist ever used this exact chain. Radiohead's actual method = Telecaster + Jazzmaster layers tracked in the St Catherine's ballroom (no pedals of this rig). 🟣 designed — never an artist chain.

## Signal path

banjo (GK-5 → **VG-800** Ondes/clean lead voice) → **CB Clean** (light comp, always-on) → *[skip the fuzz wall]* → Board-2 thru → **Generation Loss** (light tape flutter) → **Big Time** (5-against-4 cascade, ping-pong) with **Blooper** running an octave-up overdub stack underneath → **H90** (St Catherine's ballroom hall) → **PORTA424 → JHS 424** tape print → Apollo.

## Per-unit

- **VG-800** — #3 *GR-300 Thick-Synth Lead* or a clean bright **E.GUITAR** model for the Telecaster-arpeggio attack; feed a single bright arpeggio line. (For the gliding "How to Disappear" colour instead, swap to **TB1 Ondes-Martenot lead voice**, portamento ON — but Let Down wants the bright Tele jangle, not the glide.)
- **CB Clean** — #2 *Transparent Enhancer* (the ~2:1 thicken-don't-squash base, slow Attack so the pick stays uncompressed). Keep it gentle — the jangle needs its attack.
- **Generation Loss** — #2 *Vintage But Not Broken* nudged toward #1 *Subtle Tape Age* (Wow ~10:00, Flutter just up, Saturate ~9:00, Failure off, Dry Small) = the Kid-A "breathes wrong" tape warp arrives *before* the cascade, gently, without dropouts. Keep hidden Hiss low + HUM BYP so it doesn't stack noise into the print.
- **Big Time** — **TB1 "Let Down" Cascading Jangle-Delay** (MODE Short · STATE Compressed · VOICING HiFi · 0.5X OFF · COLOR ~30–35% · **TIME = 5-against-4 tap** vs the 4/4 · CLUSTER ~45–55% · TILT above noon · FEEDBACK ~40% · WET ~40% · **SPREAD ping-pong**). The multi-tap + 5/4 tap is what builds the "two clocks that refuse to agree."
- **Blooper** — **TB2 "Let Down" Octave-Stack Arpeggio Builder** (Mode ADD · record the clean bright arp STABILITY off · MOD A **Pitcher ALT-A2 = +1 oct** · punch-in overdub → original + octave-up · optional 3rd pass at a 5th/octave for the "Ed Jazzmaster" layer · REPEATS max). This is the *real* doubled-octave layer; Big Time TB1's taps cascade over the stack.
- **H90** — #3 *Blackhole Dark Matter Reverse Bloom* is wrong here; use the cluster's **H90-TB3** role via patch #1 *Cavernous Blackhole Drone* pulled back, OR #2 *Blackhole Infinite Ambient Pad* with **long pre-delay ~80–120 ms, decay ~4–6 s, Mix ~25–30%** = the "supernatural natural reverb" of the 3am ballroom, sitting *under* the cascade.
- **PORTA424** — #1 *Always-On Cassette Print* (Input Trim 9:00, 18V for firm lows under the hall, mono-sum the H90 bus). **JHS 424** — #1 *Subtle Always-On Tape Print* (Gain 1 9:00 / Gain 2 10:00, Treble 1:00 de-haze, XLR → Apollo). Tape glue, not grit — keep the jangle intact.

## Routing / sync

Banjo arrives mono into Board 1; **Big Time IN-L auto-engages MISO** (mono-in / stereo-out) so the ping-pong spreads. Clock-lock Big Time to the **Digitakt/MPC MIDI clock via CC54** (set the 5-against-4 as the subdivision relationship by tapping it, or run the dotted-8th and let the arp imply the 5). Blooper is **mono in/out** — its octave stack sums into Big Time, and the **Chroma Console re-expands to stereo** before H90 if you route through it (here we go Big Time → Blooper → H90 directly, stereo from Big Time's MISO). NO dry kill — the dry jangle must stay present. Bright/HiFi voicing throughout; Gen Loss stays subtle so the cascade isn't muddied.

## Sound

A bright, chiming, octave-stacked arpeggio wall that phases against itself (5 vs 4), warped just enough by tape to "breathe wrong," ringing into a long ballroom hall and printed to cassette. Spector-wide, supernatural, recorded-in-1997.

## Play

Fingerpick ONE steady bright arpeggio. Punch-in the Blooper octave-up overdub (hold LEFT one-shot) before the section so the stack is printed and rings under your live line. Let Big Time's ping-pong taps do the doubling/tripling illusion. For the build, raise Blooper REPEATS to max so all layers ring; for the outro, ride the H90 mix up. Optional: feed OP-1 **OP1-TB2 ZX-Spectrum bleeps** into Blooper's Scrambler for the dying-modem outro.

## Taste-ref

Radiohead — "Let Down" (OK Computer, 1997): doubled/tripled cascading arpeggios, 5/4-vs-4/4 Steve Reich phasing, St Catherine's ballroom 3am reverb, EMT 140 plate.

## Sources

- **Basis:** designed integration; chains **Big Time TB1** + **Blooper TB2** + **Clean #2** + **Gen Loss #1/#2** + **H90 #1/#2** (≈ index H90-TB3 ballroom hall) + **PORTA424 #1** + **JHS 424 #1**. Pulls the art-rock index "'Let Down' wall (one player)" chain into a full owned-gear path. Radiohead's actual method = Telecaster + Jazzmaster layers tracked in the St Catherine's ballroom (no pedals of this rig).
- `Research/Taste-Profile/art-rock.md`
- `sources/granular-before-reverb-signal-order.md` (reverb last)
