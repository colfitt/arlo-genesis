https://www.elektronauts.com/t/recording-digitakt-with-overbridge-in-logic/116879
elektronauts.com · users Kyriakos, zizlog, et al. · thread 2019-2021

# Recording a Digitakt's separate tracks into Logic Pro via Overbridge

The whole point: with the Overbridge AU you can pull each Digitakt track (kick,
snare, etc.) into Logic as its own audio track instead of just the stereo main
out. Critical wrinkle is that Logic **cannot record directly into a bus/aux** —
the Overbridge multi-outputs ARE buses, so you need a relay through audio tracks.

## Core principle (Kyriakos)
"In order to use OB in logic you have to use a **multi-output software
instrument** (the digitakt au in your case). These multi-outputs are **buss
tracks** instead of audio tracks. In logic you can NOT record straight into a
buss."

## Step-by-step
1. Add the **Digitakt Overbridge AU as a multi-output software instrument**
   track (NOT as an audio track).
2. Click the "+" on the instrument's mixer channel to expose the extra
   output/aux channels (one per Digitakt track you routed in Overbridge).
3. Create **audio tracks** — one per Digitakt output you want to record.
4. Set each **audio track's INPUT = the corresponding Bus** that the Digitakt
   AU outputs are feeding. (zizlog: "The audio of each individual track
   (Audio 1-8) is output to Bus 1. The stack's input is from Bus 1.")
5. Arm + record — now each Digitakt track lands on its own audio track.
6. (Optional) wrap the whole thing in a **Track Stack** for tidiness. zizlog
   shared a Logic template + screen recording for this.

## Gotchas
- **Digitakt must be the selected audio INPUT device** in Logic (Settings >
  Audio) for Overbridge to stream. You can still monitor/output through a
  different interface if you aggregate.
- The Overbridge buses are **audio-only** — they do NOT carry MIDI. To send
  MIDI/clock back to the Digitakt you must use the **Logic Environment** (a
  separate external-MIDI path), not the Overbridge plugin.
- Simpler fallback (not in this thread but implied): if you don't need stems,
  just record the Digitakt's stereo main out as a normal class-compliant USB or
  analog input and skip Overbridge entirely.

## Rig note
The Octatrack MkII has **no Overbridge** — for the OT you record its analog
outs (cue/main) or use it over USB as a plain class-compliant 2-in interface;
multitrack stems off the OT require its physical outputs into the Apollo x8 /
Babyface, one track per output, not a plugin. Same for the MPC Sample (record
its outs as audio).
