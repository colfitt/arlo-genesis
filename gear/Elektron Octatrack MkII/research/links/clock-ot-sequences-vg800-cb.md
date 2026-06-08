Manual: Octatrack MkII User Manual, §16.5 (p.102–103), §8.6.4 / CC DIRECT CONNECT (p.38), §15 MIDI tracks, Appendix C
Elektron manual

# OT MIDI tracks — sequence the VG-800 and the Chase Bliss pedals

The OT's **8 MIDI tracks** are a full external sequencer: note trigs, CC locks, LFOs on CCs, and the step-sequencer's conditional/probability/micro-timing — all aimed out the single DIN. Use them to play the **VG-800** (guitar-synth/COSM patches, patch changes) and to **automate CC-controllable params on the MIDI-equipped CB pedals** (Blooper, MOOD, Big Time, Generation Loss, Brothers, Clean) plus Microcosm / Chroma Console / H90.

## Per-MIDI-track channel
[MIDI] mode → select a MIDI track → double-tap [SRC] (NOTE SETUP) → **CHAN** = target's channel.
- e.g. MIDI track 1 → VG-800 channel; MIDI track 2 → Blooper; etc. Match each pedal's MIDI-in channel.
- **Keep these ≠ the OT audio-track TRIG CHANNELs** (clock-topology-ot-61sl-digitakt.md) to avoid cross-trigging.

## Sequencing the VG-800
- **Notes** on a MIDI track play the VG-800's synth/COSM voices (it responds to MIDI notes) — drone clusters, sustained pads, sequenced guitar-synth lines that you then resample.
- **Program Change** via the OT's PROG CH SEND (or a MIDI-track PC) flips VG-800 patches mid-song.
- **CC locks** ride VG-800 params (filter, model blend) per step.

## Sequencing/automating the CB pedals
- Each MIDI-equipped CB box takes MIDI CC for its params + tap/clock. Assign a MIDI track per pedal, then **p-lock or LFO its CCs**: e.g. ramp Blooper's layer/stability, sweep MOOD's wet length, modulate Big Time time/feedback, dirty Generation Loss wow/flutter — all locked to the sequencer step grid and synced to OT clock.
- Look up each pedal's CC map (in its own research folder) and set the **CTRL 1/CTRL 2 SETUP** CC numbers per MIDI track, or use **MIDI learn** ([FUNC]+knob C in CTRL SETUP) if the pedal can transmit the CC back.

## CC DIRECT CONNECT + AUTO CHANNEL (live-record knob moves)
PROJECT > CONTROL > MIDI SEQUENCER > **CC DIRECT CONNECT = On**, and set **AUTO CHANNEL**. Now if a peer controller (e.g. the **61SL MkIII** knobs, or the VG-800's own controls if they transmit) sends CCs on the auto channel, the active OT MIDI track passes them straight out AND can **live-record / p-lock** them. So you can ride a VG-800 or CB param by hand and capture the motion into the OT sequence.

## Avoid double-sequencing
If the OT MIDI-sequences the VG-800, don't ALSO have the 61SL sequencing the VG-800 on the same channel. Pick ONE sequencer per target. Typical division for this rig:
- **OT** = mangles audio (Thru/Flex) + MIDI-sequences the VG-800 + automates CB CCs.
- **61SL / Digitakt** = clock + drums/keys parts.
- Everyone shares ONE clock master (clock-topology-ot-61sl-digitakt.md).

## Cabling reality (single DIN OUT)
The OT's clock, transport, and all 8 MIDI tracks share the one MIDI OUT. Daisy-chain via each box's MIDI THRU, or split with a MIDI thru-box if the chain gets long / you need parallel branches (e.g. VG-800 on one branch, the CB stack on another). The 61SL's second DIN ("Out 2") can host a second independent chain if the 61SL is in the topology.
