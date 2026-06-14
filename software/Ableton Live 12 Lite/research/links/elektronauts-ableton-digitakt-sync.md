https://www.elektronauts.com/t/ableton-digitakt-midi-clock/104394
elektronauts.com · Digitakt forum · accessed 2026-06-07

# Ableton ↔ Digitakt MIDI clock sync (community)

Directly relevant: the rig runs a Digitakt 2. Same principles apply to the
Octatrack MkII and MPC Sample.

## Recommended config (Live master, Digitakt slave)
- Ableton Live = **master clock**, Digitakt = slave (most common, most stable
  for clip-launch performance where Live drives the set).
- On Digitakt: enable **Clock Receive**, set MIDI input to **USB**, verify the
  sync button is on for the current USB mode.
- In Ableton: enable **Sync** on the Digitakt output port in Link/Tempo/MIDI
  prefs. Watch the **"Track" and "Sync"** toggles per port — getting the right
  pair on/off takes trial-and-error.

## Gotchas people actually hit
- **USB hub adds latency** → "I was using a USB hub and I think that gave some
  extra latency." Connect the Elektron **directly** to the computer, not through
  a hub.
- **Overbridge vs USB-MIDI mode** changes the device NAME in Ableton's prefs.
  When you flip the DT's USB mode, "watch ableton's prefs when you switch modes
  on the DT and you'll see the name change (takes a few seconds)" — then re-tick
  Sync for the newly-named port.
- Most failures here are **config/connection**, not drift — i.e. it's usually a
  wrong toggle or wrong port, not a fundamental timing problem.

## Practical takeaway for the rig
Plug the Digitakt 2 / Octatrack MkII straight into the Apollo/Babyface or the
Mac (no hub) for clock. Use a dedicated path for clock if note data is heavy.
