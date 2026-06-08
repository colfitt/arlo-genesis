Manual: Octatrack MkII User Manual, §16.1 (p.96), §8.8 MIXER (p.42), §10.3.2 XLV/XDIR (p.54)
Elektron manual

# RECIPE — "OT as the rig's master sampler / mixer"

The full desk-brain patch: the OT mixes the live pedalboard + a second source, applies FX, samples on the fly, performs with the crossfader, and prints to the interface. This is the "super mixer" role from manual §16.1, mapped onto this rig.

## Routing
- **Input A/B** = pedalboard stereo print (Boards 1–3).
- **Input C/D** = a second live source — e.g. VG-800 synth/COSM out, OP-1 Field sketch, or an Apollo monitor send.
- **Main out L/R → Apollo x8 / Babyface** (print). **Cue out** = independent stem to a second interface input.

## Build (Thru method = full FX + performance)
1. MIXER: **DIR AB = 0, DIR CD = 0** (both inputs reach the mains only via Thru tracks). Set AB/CD GAIN so `<REC>` LEDs are healthy.
2. **Track 1 = Thru (INAB = A B)** — the pedalboard, with FX1/FX2 + LFOs.
3. **Track 5 = Thru (INCD = C D)** — the second source, its own FX. (Track 5 is a chain head, like track 1 — leaves room for Neighbor racks on 2–4 and 6–8.)
4. (Optional) **Neighbor racks** on 2/3/4 (extends track 1) and 6/7 (extends track 5) for deep serial FX (int-ot-effects-processor-neighbor-chain.md).
5. **Track 8 = master track** — global EQ/compressor/Lo-Fi glue + final level on the whole mix before the interface.
6. Place one trig on track 1 and track 5; [PLAY].

## Mix + perform
- **LEVEL / VOL** per track = the mixer faders for each source.
- **Crossfader scenes**: XLV-lock track 1 (MAX@A / MIN@B) and track 5 (MIN@A / MAX@B) for an equal-power A/B fade between the pedalboard and the second source. Or scene-morph FX across both (rig-crossfader-scenes-performance.md).
- **Mutes**: [FUNC]+[TRACK n] drops any source instantly.

## Sample anytime
- Any track recorder can grab input A/B, C/D, or **SRC3 = MAIN/CUE/T1–T8** (resample the OT's own output). Capture the live mix or a single Thru track into a Flex buffer, slice it, re-sequence it on a spare track — all without stopping (resample-the-rig-master-track.md).

## Clock
OT as **master** (CLOCK + TRANSPORT SEND on), driving Digitakt/CB/VG-800/Microcosm/H90 over DIN; tempo set on OT (clock-topology-ot-61sl-digitakt.md). FX delays/freeze on the Thru tracks then sit in the rig's tempo grid.

## One-line summary
Pedalboard + a second source → two Thru tracks (each with FX) → optional Neighbor racks → master track glue → interface; crossfader morphs it, track recorders capture-and-destroy it, the OT clocks the whole electronic rig. Nothing else on the desk does all of this at once.
