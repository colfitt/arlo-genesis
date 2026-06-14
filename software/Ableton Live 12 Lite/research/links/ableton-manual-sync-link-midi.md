https://www.ableton.com/en/manual/synchronizing-with-link-tempo-follower-and-midi/
ableton.com · Ableton Reference Manual v12 · accessed 2026-06-07

# Live 12 sync — Link, Tempo Follower, MIDI clock (authoritative procedure)

All of this works identically in Lite — Link, MIDI clock in/out, and Tempo
Follower are NOT gated by edition. This is the canonical how-to for slaving the
Elektrons/MPC/OP-1 to Live or vice-versa.

## Live as MIDI clock MASTER (Live drives the hardware)
1. Settings → **Link/Tempo/MIDI** (Tempo & MIDI Settings).
2. Find your hardware's **MIDI output port**, toggle **Sync = On** for that
   output.
3. The Control Bar's lower indicator LED flashes when sync is transmitting.
- "Live can send MIDI Clock messages to an external MIDI sequencer or drum
  machine."

## Live as SLAVE (hardware drives Live's tempo)
1. Settings → Link/Tempo/MIDI, find the hardware's **MIDI input port**, set
   **Sync = On** for that input.
2. The **EXT button** appears in the Control Bar — click it to follow external
   clock. Upper LED flashes on valid incoming sync.

## MIDI Clock Sync Delay (the jitter/offset fix)
- Per-port control that delays Live's internal timebase vs the sync signal to
  compensate for transmission/buffer latency.
- Tune it: play a percussive pattern on BOTH Live and the device, listen, and
  "adjust the Sync Delay control until both sounds are in perfect sync." Allow a
  couple of measures for tempo to settle before judging.

## Ableton Link (the modern, jitter-free path)
- Syncs **beat, tempo, AND phase** across apps/devices over a wired or wireless
  network (or USB-ethernet). Enable: Control Bar **Link toggle** (Settings →
  Link tab).
- Any participant can change tempo and all followers track it.
- For this rig, only the OP-1 Field (newer firmware) and software speak Link
  natively — the Elektrons/MPC Sample do NOT, so they need MIDI clock.

## Tempo Follower (Live follows live-played audio)
- Settings → Link/Tempo/MIDI → set **Input Channel (Ext. In)** to an interface
  input, enable **Show Tempo Follower Toggle**, then click **Follow** in the
  Control Bar.
- Analyzes incoming audio in real time and bends Live's tempo to match a
  human/hardware performance. Useful if you want Live to chase the MPC/board
  instead of the other way around.

## Rig note
- Drum-machine/sequencer sync = MIDI clock (Sync-on on the out port).
- App-to-app and OP-1 Field = Link (tighter, phase-locked, no Sync Delay
  tuning).
