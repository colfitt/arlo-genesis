https://www.soundonsound.com/reviews/xln-addictive-drums-2
soundonsound.com (AD2 review) + AD2 manual (assets.xlnaudio.com/documents/addictive-drums-manual.pdf) + XLN "Interface overview - The Mixer section" support article · accessed 2026-06-11

# AD2's INTERNAL mixer FX — Delerb sends, the Bus channel, snapshots, master inserts

The most under-used part of AD2 for character work. All of this lives inside the
plugin and is recallable per-preset.

## Per-channel insert chain (every drum has its own)
Each mixer channel has: **EQ, Compressor, Distortion, Transient Shaper, Tape
Saturation** + **2 FX sends**. So a lot of "degrade" can happen WITHOUT leaving AD2 —
the Distortion + Tape Sat + Transient Shaper per drum are the built-in lo-fi tools.

## The two Delerb send units (FX1 / FX2)
- "Delerb" = a **delay feeding a reverb** in one unit. There are **two identical**
  ones (FX1, FX2).
- **Blend slider**: delay at one end → reverb at the other (or any mix between).
- Delay: **tempo-sync to 11 note values OR free ms**, + **Feedback** (100% =
  infinite repeats — useful for drones/post-rock washes), **Swing**, **Ping-Pong
  width**.
- Reverb: **Ambience / Room / Hall / Plate** algorithms, + **pre-delay, decay,
  damping, and "Swirl"** (a chorus that thickens the tail — great for shoegaze wash).
- Each channel has two **enable buttons** to toggle its sends fast.

## Delerb OUTPUT routing (the hidden power move)
The Delerb returns have their own output options in the Mixer:
- **Pre Master Inserts** — reverb/delay goes THROUGH the master inserts (so you can
  compress/filter the whole mix incl. the tail).
- **Post Master Inserts** — tail stays AFTER the master inserts: "compress the kit
  heavily on the master bus but keep the reverb uncompressed and natural." This is
  how you get a smashed dry kit under a clean wash.

## The Bus channel (parallel destination)
- One stereo **Bus** any channel can send a submix to. Classic use: **distort the
  Bus hard** and blend it back into the Master = parallel drum distortion entirely
  in-box. (For this rig you could instead route the Bus out and reamp/Decapitate it.)

## Snapshots (compare-without-committing)
- **5 snapshot slots** hold all sound/mix settings. Slot 1 = current state by default.
  Use them to A/B a clean kit vs. a degraded version, or build up a degrade in stages
  you can revert. Snapshots are session-level, not the same as saved presets.
