https://www.elektron.se/explore/digitakt-ii
Elektron Digitakt II User Manual OS 1.15A §14.4.1 SYNC / §14.4.2 PORT CONFIG / §3.2 connectors (local PDF) · Elektron · 2025-07-08
Supplemented by: Elektronauts "Octatrack/Digitakt/Digitone best way to connect" (https://www.elektronauts.com/t/octatrack-digitakt-digitone-best-way-to-connect/84027) · MusicRadar all-Elektron guide

# DT2 clock master / slave — sending & receiving MIDI clock + transport

## The four SYNC switches (the whole game)
`[SETTINGS]` → MIDI CONFIG > **SYNC** (manual §14.4.1). Four independent toggles:
- **CLOCK RECEIVE** — DT2 follows external MIDI clock (DT2 = slave).
- **CLOCK SEND** — DT2 transmits MIDI clock (DT2 = master).
- **TRANSPORT RECEIVE** — DT2 responds to external start/stop/continue.
- **TRANSPORT SEND** — DT2 transmits start/stop/continue.
- (Also here: **PRG CH RECEIVE / PRG CH SEND** — respond to / send program-change for pattern selection. PC 0–127 selects pattern 1–128 / A01–H16. Channel set in CHANNELS menu.)

**DT2 as MASTER (the default for this rig):** CLOCK SEND = ON, TRANSPORT SEND = ON; CLOCK/TRANSPORT RECEIVE = OFF. Everything downstream sets its own clock-receive ON.

**DT2 as SLAVE (to DAW or Octatrack leading):** CLOCK RECEIVE = ON, TRANSPORT RECEIVE = ON; SEND = OFF.

> Only ONE master on a MIDI loop. Never leave two devices with CLOCK SEND on into each other.

## Port routing (where the clock physically goes)
`[SETTINGS]` → MIDI CONFIG > **PORT CONFIG**:
- **OUTPUT TO** = MIDI / USB / MIDI+USB / DISABLED — which physical port carries DT2's outgoing MIDI (incl. clock).
- **INPUT FROM** = MIDI / USB / MIDI+USB / DISABLED — where DT2 listens. *For Overbridge/DAW work, picking just MIDI or just USB (not MIDI+USB) reduces jitter/latency.*
- **OUT PORT FUNCTIONALITY / THRU PORT FUNCTIONALITY** = **MIDI**, **DIN 24**, or **DIN 48**. Setting a port to DIN 24/48 turns it into an analog DIN-sync pulse output (no MIDI data on that port) — for legacy/analog-clock gear. *(The DT2's physical jacks are labelled MIDI OUT/SYNC A and MIDI THRU/SYNC B precisely because they double as DIN-sync outs.)*
- **TURBO SPEED** — negotiates Turbo-MIDI speed if your interface supports it (tightens timing on long chains).
- **ENCODER DEST / TRIG KEY DEST / MUTE DEST** = INT / INT+EXT / EXT — whether knob moves, trig presses, and mutes also fire MIDI out (set INT+EXT to capture/echo performance gestures to external gear).

## MIDI DIN chaining note
- DT2 has MIDI **IN / OUT / THRU**. THRU forwards exactly what arrives at IN (clock included), so you can daisy-chain: DT2 OUT → device 1 IN; device 1 THRU → device 2 IN; etc. For many clock slaves a powered **MIDI thru-box** (star topology) beats a long thru-chain to avoid cumulative jitter.
- DT2 clock over **USB** works too (class-compliant) — good for clocking the DAW or USB-MIDI pedals.

## Who should be master in THIS rig
- **DT2 master is the natural default** for tempo-synced delays/loopers: it holds the groove and can carry **per-pattern tempo** (each DT2 pattern stores its own BPM), which a single master clock to all the pedals then distributes. The Octatrack thread consensus: "make the Digitakt the master… takt and tone can lock different tempi per pattern by nature," keep slaves on clock-receive.
- **Octatrack as master** when the OT's arranger is driving a performance (see the DT↔OT combo file). Then DT2 = CLOCK/TRANSPORT RECEIVE ON.
- **Novation 61SL MkIII** has its own deep sequencer + clock. Pick ONE brain: either let the SL master (DT2 slaves) when composing from the keyboard's sequencer, or let DT2 master and use the SL purely as a keyboard/controller on the auto channel. Don't run both as clock master.
- **DAW (Logic/Ableton)** as master when tracking to a grid — especially under Overbridge, where the DAW transport drives the DT2 (DT2 = receive). See Overbridge file.

## Tempo / BPM
- Set DT2 tempo: `[FUNC] + [PAGE/TEMPO]` (TEMPO menu); tempo is per-pattern. As slave, the incoming clock overrides this.
