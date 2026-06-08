Manual: Octatrack MkII User Manual, §16.2 (p.98), §16.3 (p.99), §8.8 MIXER cue/MIX (p.42), §9.1 SRC3 (p.46)
Elektron manual

# The reamp / print loop — OT with the Apollo x8 and Babyface Pro FS

The OT's **balanced main outs + separate balanced cue outs** make it a clean citizen on the desk. Two distinct jobs: (1) printing the OT to the interface, (2) using the interface (or an external pedal) as a reamp send the OT processes.

## I/O recap
- 4 × balanced TRS inputs (A/B + C/D), 2 × balanced main out, 2 × balanced **cue out**, headphones.
- **No USB audio** — all audio is on 1/4" cables to the Apollo/Babyface. (USB is disk-mode only; can inject computer noise into outputs — use balanced cables.)
- **12 V** own PSU — NOT on the 9 V pedalboard supply.

## Print the OT to the interface
- OT **main out L/R → Apollo x8 line ins** (or Babyface) → record the full performance.
- **Cue outs** carry an independent stem: cue a track ([CUE]+[TRACK]) to send *just that track* to the cue outs → **cue out → a second interface input pair** = print a stem (e.g. the resampled banjo loop alone) while the mains carry the full mix. The **MIX** param (MIXER) sets whether headphones mirror main or monitor cue.
- Master-track (track 8) FX/level is the final glue stage before the interface (note: cue out is NOT available on the master track).

## OT as a send-effect / reamp processor (interface aux → OT → back)
Mirror of manual §16.2 (OT-with-external-FX), inverted for the rig:
- Send a DAW/interface aux (a dry guitar/banjo stem from the Apollo/Babyface) → **OT input A/B**. DIR AB = 0; **Thru machine** on a track applies OT FX; OT main out → back to an interface input → record the wet. The OT becomes an outboard stereo FX/sampler send.
- **LATENCY WARNING:** a round-trip *through the DAW* (Ableton/Logic) into the OT and back adds the DAW's buffer latency on top of the OT's ~1.5 ms — Elektronauts flag this as the usual "OT latency" complaint. Mitigate with the interface's own **input delay compensation** on that channel, or avoid the DAW round-trip and reamp **hardware-direct** (interface analog out → OT → interface analog in), where only the OT's ~1.5 ms applies (inaudible for playing).

## OT inside the external-pedal loop (§16.2 method)
- OT **cue out → an external pedal/board input**; that pedal's **output → OT input A/B** (DIR AB acts as the aux-return level). **[CUE]+[TRACK]** sends a track out to the pedal, the wet returns and can be further OT-processed or resampled. Lets you fold a favorite outboard pedal into the OT's chain and capture the result.

## Live FOH variant (no phasing) — manual §16.3
For processing the live pedalboard and returning only the wet to FOH/monitors:
- Inputs from the board → OT; **DIR = 0**; **[CUE]+[REC1]/[REC2]** routes incoming audio to the **cue outs** (not the mains) so the raw input never hits the mains and phases against the processed return. Sample + process, and only the OT main outs (processed/resampled audio) go back to the desk/FOH.

## Resampling the interface return
Track recorders can sample **SRC3 = MAIN or CUE** (or any track) — so you can resample the OT's own processed-and-returned signal internally, closing the capture-and-destroy loop without leaving the box.
