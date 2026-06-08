Manual: Octatrack MkII User Manual, §8.7.2 SYNC (p.40), §8.7.3 CHANNELS (p.41), §16.1 (p.96)
Elektron manual + Elektronauts (hybrid-clock #160429, live-looping/pickup #106375)

# CLOCK & MIDI TOPOLOGY — OT with the 61SL MkIII, Digitakt 2, MPC, CB stack, VG-800

The OT has **one 5-pin DIN trio (In / Out / Thru)** and **no USB MIDI / no Overbridge** — it's DIN-only. So the OT joins the rig's MIDI web over DIN, and the **single MIDI OUT carries clock + transport + its 8 MIDI tracks together**.

## The two SYNC switches (PROJECT > MIDI > SYNC)
- **CLOCK SEND** — OT transmits 24 PPQN MIDI clock out the DIN.
- **TRANSPORT SEND** — OT sends play/stop/continue/SPP.
- **CLOCK RECEIVE / TRANSPORT RECEIVE** — OT follows external clock/transport.
- **PROG CH SEND/RECEIVE** (+ channel) — pattern changes can drive/follow program changes.
- Rule: **never have SEND and RECEIVE on at once** for clock — pick a master.
- Note: if BOTH clock-receive and transport-receive are on, the OT waits up to 16 s for clock after a start (handles DAW preroll). Transport-only = starts immediately.

## OT as MIDI clock MASTER (recommended default for this rig)
The OT is the dawless brain on the desk. Set **CLOCK SEND + TRANSPORT SEND = On**, RECEIVE off.
- OT **MIDI OUT → Digitakt 2 IN → Digitakt THRU → next box IN …** daisy-chain the MIDI-clocked gear: Digitakt 2, the CB stack (Generation Loss / Big Time / MOOD / Blooper / Brothers / Clean), Microcosm, Chroma Console, H90, VG-800.
- On each slave: set **Clock Receive = On**, **Transport Receive = On**. OT [PLAY]/[STOP] runs the whole rig; tempo set on the OT.
- **Why master:** the OT's clock is rock-solid and doesn't change with what's plugged in (Elektronauts consensus). Critically, **OT Pickup-machine overdub MISBEHAVES when the OT is slaved** — so if you live-loop on the OT, the OT *must* be master.

## OT as SLAVE (when the 61SL is the rig's conductor)
The just-finished 61SL recipe (Gear/Novation 61SL MkIII/research/links/int-recipe-elektrons-mpc.md) has the **61SL as standalone clock master + 8-track poly sequencer** driving Digitakt + OT + MPC, each on its own Part/channel/destination. To make the OT follow it:
- 61SL: **Global > MIDI Clock Tx = On** (24 PPQN to USB + both DINs).
- OT: **CLOCK RECEIVE + TRANSPORT RECEIVE = On**, SEND off. Feed clock from ONE source only (61SL DIN → OT MIDI IN).
- The OT now follows 61SL play/stop/tempo. Use the OT for what it's best at (Thru-FX, resampling, Flex re-sequencing) and DON'T live-loop with Pickup machines in this mode (overdub-while-slaved bug).

## "Who sequences whom" — the double-sequencing trap
The OT, Digitakt, MPC, and 61SL all have their own sequencers. Decide per song:
- **One master sequencer plays the others** → set the played boxes' incoming-MIDI to trigger sounds, and DON'T also run their internal patterns on the same tracks (= double-trigger chaos).
- **Keep clocks shared, sequencers independent** → all boxes share clock from one master, but each runs its own pattern (the classic Elektron jam). The OT's MIDI tracks then sequence only *external* targets (VG-800, CB CCs) — see clock-ot-sequences-vg800-cb.md.

## OT MIDI-track vs audio-track channel hygiene (important)
- The 8 **audio tracks** have **TRIG CHANNELs** (PROJECT > MIDI > CHANNELS) — they both respond to and SEND MIDI. The 8 **MIDI tracks** have their own channels (NOTE SETUP).
- **Keep audio-track channels ≠ MIDI-track channels ≠ slaved-gear channels**, or you'll get unintentional trigging. The manual flags this explicitly for the multi-box setup.
- **AUTO CHANNEL** = the active track's channel; used for foot-controller Pickup control + CC Direct Connect live-record.

## Canonical pairing — Digitakt 2 + OT
Digitakt = disciplined drums/one-shots/timekeeper; OT = mangle/resample/perform. Either can be master. Common: **Digitakt master** for tight drums, OT slaved — but if you Pickup-loop on the OT, flip it (OT master, Digitakt slaved). For the simplest reliable rig: **OT master of everything.**

## DAW note (Apollo/Logic in the loop)
If recording to Logic/Ableton, Elektronauts strongly suggest either (a) DAW is master and everything slaves to it, or (b) **run sync-free** — DAW as a dumb multitrack tape recorder, no MIDI clock between hardware and computer (eliminates the round-trip-latency headaches). For pure live performance, keep the DAW out of the clock chain entirely.
