https://www.elektronauts.com/t/logic-pro-sync-with-digitakt-just-clock-and-start-resolved/183578
elektronauts.com · user ellioup (resolved) · 2022-11

# Logic → Digitakt: just clock + start, then record the analog outs (resolved)

This is EXACTLY the user's workflow: Logic tells the Digitakt when to start +
keeps it on the grid, then you record the Digitakt's analog outs into the
interface (here Focusrite/compressors; for this rig = Apollo x8 / Babyface)
as normal audio — NOT Overbridge stems.

## Resolution (OP)
Solved via the Apple Support doc **"Sync multiple MIDI devices to Logic Pro"**:
"In Logic Pro 10.4.5 or later, independently configure MIDI clock settings for
up to **16 external MIDI devices**." (i.e. File > Project Settings >
Synchronization > MIDI, tick Clock for the Digitakt destination — see
apple-sync-midi-clock-external-hardware.md.)

The takeaway: you do NOT need Overbridge just to sync + record. Overbridge is
only for pulling per-track stems over USB. For "start it on the grid and record
the stereo/analog outs," plain MIDI clock + an armed audio track on the
interface input is all you need.

## Gotcha worth knowing (OP)
"The one interesting part is the clock from Logic is making my project jump from
**109 to 109.1 bpm** (they must have a slight difference in timing)."
- Logic's transmitted MIDI clock can introduce a tiny tempo rounding/jitter so
  the displayed/perceived tempo nudges a fraction of a BPM. Usually cosmetic and
  inaudible, but if you're syncing a delay/LFO tightly, be aware Logic-as-clock-
  master over MIDI is not sample-accurate (MIDI clock is 24 ppqn and jittery by
  nature). For rock-solid sync, the alternative is to clock everything from one
  master and let Logic free-run, or accept the tiny drift.
