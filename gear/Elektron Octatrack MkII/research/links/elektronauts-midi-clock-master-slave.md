https://www.elektronauts.com/t/midi-sync-octatrack-rytm/13290
elektronauts.com + Elektron OT MkII manual p.40 (SYNC) · (also "Midi basics - setup" /35880, OT-master-Digitakt-slave threads, "live performance setup OT+DT II+DN II" /243685)

# Clocking the rig — OT as MIDI master vs slave (concrete menu settings)

The OT has a single 5-pin MIDI OUT (plus IN/THRU). The sync settings live in **PROJECT > MIDI > SYNC** (and MIDI > CONTROL). Four independent toggles, activated with [YES]:
- **TRANSPORT SEND** — OT sends play/stop/continue + Song Position Pointer.
- **TRANSPORT RECEIVE** — OT responds to incoming play/stop/continue + SPP.
- **CLOCK SEND** — OT transmits MIDI clock (it becomes the tempo master).
- **CLOCK RECEIVE** — OT follows incoming MIDI clock (it becomes a slave).

## OT as MASTER (recommended for this rig)
- Enable **CLOCK SEND + TRANSPORT SEND** on the OT.
- On each slave (Digitakt 2, Digitone, VG-800, MIDI-equipped Chase Bliss/Microcosm/H90/Chroma), enable **CLOCK RECEIVE + TRANSPORT RECEIVE** and (for Elektron boxes) run that box's own sequencer locked to incoming clock.
- WHY master here: **pickup-machine OVERDUB and CUE-source Flex overdub are unreliable when the OT is slaved** — if you live-loop on the OT it MUST be the clock master. (See pickup/latency notes.)
- The classic pairing: **OT master, Digitakt slave**, and route the **Digitakt's audio into a Thru machine on the OT** so the drums get OT FX + can be resampled/scened with everything else.

## OT as SLAVE
- Enable CLOCK RECEIVE (+ TRANSPORT RECEIVE) and pick your external master (DAW, Digitakt). Works fine for plain playback/sequencing — just not for OT-side overdub looping.

## Daisy-chain / fan-out note
- The OT has only ONE MIDI OUT. To clock multiple slaves, daisy-chain via each box's MIDI THRU, or use a MIDI thru-box/splitter. Use the MIDI THRU port to pass clock onward.
- SWING: when OT is master and Digitakt slaves to its clock, swing must be set on the OT (or each box swings its own sequencer independently — the clock carries tempo, not groove).

## Stability / reliability context (from community + dossier)
- Build quality is excellent; no widespread failure pattern. The CompactFlash slot + the internal memory battery (~6-yr life, "BATTERY LOW" warning) are the only real consumables. Buy a known-good UDMA ≥133x CF card + a backup, and **never pull the card while the CARD STATUS LED blinks**. Widely trusted for live use once you're on 1.40B/C.
