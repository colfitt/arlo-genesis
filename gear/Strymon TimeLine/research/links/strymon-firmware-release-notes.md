https://www.strymon.net/faq/timeline-firmware-revision-release-notes/
strymon.net · Strymon (official) · ongoing (last rev April 2020)

Official TimeLine firmware revision history. The single best reference for old-vs-new differences — what each firmware added, and which bugs were patched. **v1.88 (April 2020) is the final/frozen release.** Confirm the owned unit is on 1.88; a lot of community "bugs" are stale and were fixed years ago.

## Revision-by-revision (newest → oldest)

**Rev. 1.88 — April 2020 (FINAL)**
- Fixed a DSP-bandwidth issue with **dBucket at its longest delay time while using the looper** (the one glitch case still documented). Pre-1.88 units can glitch there.

**Rev. 1.87 — March 2019**
- Added support for **MultiSwitch Plus** (the 3-button external switch).

**Rev. 1.84 — November 2017 — MAJOR MIDI UPDATE**
- **Per-preset MIDI Clock:** moved MIDI-clock on/off from GLOBALS into the per-preset PARAMS menu, so each preset can sync-or-not independently. (Big one for people running a master clock who want some presets free-running.)
- **MIDI THRU vs MERGE:** added a true pass-through THRU mode; the old "ON" behavior was renamed **MERGE** to distinguish merging from passing data through. Relevant when chaining multiple MIDI pedals downstream.
- Added **Nixie 1.0 compatibility**.
- Fixed looper high-frequency audio fidelity (looper sounds noticeably better post-1.84).
- Fixed missing Vinyl effect in custom **Lo-Fi** presets.
- Fixed MultiSwitch EXP-mode conflicts when in LOOPER mode.
- Fixed UNDO glitches during looper playback (repeated UNDO presses with no overdubs).
- Fixed a GRIT bug that eliminated filtering in the **Filter** machine.
- Fixed a MIDI-clock counting error on the first cycle.
- Fixed a 100%-wet preset bug that wrongly let dry signal through.

**Rev. 1.58 — February 2015**
- MultiSwitch EXP controller support: TAP, Bank, Preset, Looper modes.
- **MIDICL** global param for how the pedal responds to incoming MIDI clock.
- Improved MIDI THRU + tap-averaging precision.
- Fixed MIDI-clock start/stop dropping the wet signal, and the looper half-speed "right-channel-only" bug.
- Fixed delay trails getting cut off when bypassed in FEEDBACK LOOP mode.

**Rev. 1.42 — March 2013 (public beta)**
- **MIDI Clock Sweep + Reset** global params for tempo management.
- Global Tap Tempo per-preset toggle.
- New absolute looper MIDI commands: **Reverse = CC 103, Half Speed = CC 104**.
- Improved Swell triggering + preset recall.

**Rev. 1.33 — February 2013**
- "SUCCESS" indicator for preset install; Preset Dump backup function. (Known minor issues — beta 1.42 was recommended over it.)

**Rev. 1.23 — February 2012 — LOOPER OVERHAUL (the "big" looper update people reference)**
- **Looper Undo/Redo** (revert to the initial loop, then redo overdubs).
- **5-second Spillover** for delay trails across patch changes — origin of the "must wait ~5s" rule.
- **Kill-dry** for parallel loops; record 100% wet.
- Tap averaging + preset naming; Global Tap Tempo across presets.
- Dedicated MIDI CCs for bypass + looper control.

**Rev. 1.14 — August 2011**
- Tap subdivisions always applied; TAP LED goes amber when a non-quarter-note division is selected. Dedicated looper MIDI CCs added alongside note messages.

## Takeaways for this rig
- The "must wait ~5s before spillover engages" rule is real and dates to v1.23 — never been removed.
- Per-preset MIDI clock (key for syncing to the Digitakt 2 master clock while letting drone presets free-run) requires **≥1.84**.
- The TimeLine **receives but does NOT send** MIDI clock — it's always a clock slave, never the master (confirmed across firmware). So the Digitakt stays master; the TimeLine follows.
