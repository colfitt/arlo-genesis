https://logic-users-group.com/threads/aggregate-device-to-combine-multiple-audio-devices.11914/ · https://support.apple.com/en-us/102171 · https://www.soundonsound.com/techniques/templates-logic-pro
logic-users-group + apple support + soundonsound · community

# Aggregate Devices (Apollo x8 + RME Babyface together) + template gotchas

The user owns BOTH a UA Apollo x8 and an RME Babyface Pro FS — combining them in
one Logic session means an **Aggregate Device** (macOS, Audio MIDI Setup). Real
benefits but real gotchas.

## Building it
- **Audio MIDI Setup > "+" > Create Aggregate Device**, tick both interfaces.
  In Logic: Settings > Audio > Device = the aggregate. Gives you all the
  Apollo + Babyface ins/outs at once (more inputs for multitracking the
  Elektron/MPC outs simultaneously).

## Gotchas (the important part)
- **Latency = the SLOWEST interface in the group**, plus the aggregate adds
  **~0.3 ms** on top. So pairing a fast and slow box drags everything to the
  slow one.
- **Clock master conflict**: exactly ONE device must be clock master. If both
  want to be master (or aren't word-clock locked), you get **intermittent
  crackle/pops** — the classic aggregate symptom. Designate one master and set
  the other to slave/external clock, or word-clock them together. The Apollo and
  Babyface both have clocking options; pick one master.
- **Mismatched software mixers** (UA Console vs RME TotalMix) makes monitoring/
  routing fiddly — "not much fun if you have very different interfaces."
- Recommendation for this rig: prefer running a **single interface** per session
  when you can (Apollo for tracking/reamping with its DSP + Console monitoring;
  Babyface for portable/simple sessions). Only aggregate when you genuinely need
  the combined I/O count, and lock the clock.

## Template best practices (bake the rig in)
- Pre-build a **drone/ambient template**: instrument groups in Track Stacks,
  go-to FX chains (ChromaVerb-freeze bus, SketchCassette/Tape degrade bus),
  External Instrument tracks for the VG-800/S08, audio tracks pre-armed to the
  Elektron/MPC interface inputs, MIDI clock destinations set in Project Settings.
- **Mix > I/O Labels**: name your interface inputs ("Apollo 1 = Pedalboard L",
  "Apollo 3 = OT Main", etc.) so the input menus read in plain English.
- "Anything redundant should be removed" — keep separate lean templates
  (tracking vs mixing vs performance) rather than one bloated one.
- Templates also store **Project Settings** (sync, sample rate, recording) — set
  those once so every drone session opens with MIDI clock + buffer ready.
