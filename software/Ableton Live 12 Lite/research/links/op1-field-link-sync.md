https://op-forums.com/t/ableton-link-and-op-1/3786
https://www.ableton.com/en/manual/synchronizing-with-link-tempo-follower-and-midi/
op-forums.com / ableton.com (via search) · accessed 2026-06-07

# OP-1 / OP-1 Field ↔ Ableton sync

## Ableton Link (the clean path)
- Link syncs beat/tempo/phase over wired or wireless network between apps/devices.
  Enable in Live via the Control Bar **Link toggle**. Any participant can change
  tempo and all followers track it — no Sync Delay tuning, phase-locked.

## OP-1 reality check (honest)
- The original **OP-1 does NOT speak Link natively** — it syncs to Live via
  **USB MIDI clock** (in Live's MIDI prefs, tick Sync on the OP-1's in/out port),
  OR via an iOS bridge ("Link to MIDI" app over Camera Connection Kit) to bridge
  Link↔MIDI.
- **OP-1 Field**: community reports are mixed on native Link; the safe, documented
  path is the same **USB MIDI clock** sync. Treat it like the Elektrons: USB MIDI
  clock, Live as master, Sync on the port.

## Rig takeaway
Don't assume Link "just works" with the OP-1 Field — plan for **USB MIDI clock**
(Live master). If a future firmware adds native Link, switch to Link for tighter
phase lock. For now: MIDI clock for OP-1 Field, Digitakt, Octatrack, MPC; Link is
mainly for app-to-app and Link-native gear.
