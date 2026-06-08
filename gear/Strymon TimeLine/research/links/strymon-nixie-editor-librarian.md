https://www.strymon.net/support/nixie-2/
strymon.net · Strymon (official) · Nixie 2 (current)

Nixie / Nixie 2 = Strymon's graphical preset editor + librarian + backup tool for **TimeLine, BigSky, Mobius** (the "Big Box" trio). This is the de-facto power-user workflow for the TimeLine because the pedal itself has a cramped 2-footswitch nav. Distilled setup + workflow.

## What it does
- **Backup / restore** all 200 presets to/from the computer. The single most-recommended first thing to do with a TimeLine.
- **Organize / reorder / drag-and-drop** single presets OR whole preset collections. Drag presets straight from a web page into Nixie.
- **Create / deep-edit** presets with every machine param exposed graphically (far easier than knob-pushing on the pedal).
- **Real-time bidirectional editing:** turn a knob on the pedal → the on-screen knob moves, and vice versa. All three Big-Box pedals can be connected at once, no re-patching between them.
- **Offline device feature:** build/explore presets for a pedal you don't physically have connected.
- Pushes **firmware updates** too (see strymon's "update firmware with Nixie" guide).

## Preset file format
- Presets are **.syx (sysex) files**. Import: `File → Presets → Import Preset →` pick the `.syx`. This is how community/commercial preset packs are shared (e.g. worship-scene packs).

## Connection — THE GOTCHA
TimeLine has **no USB**; Nixie talks to it over **5-pin MIDI**, so you need a MIDI interface. Strymon's warning is blunt: because of the very high data-transfer rate, **most "plug-and-play" MIDI interfaces FAIL** — every one they tested failed.
- **Recommended interfaces:** Roland **UM-ONE mkII**, Yamaha **UX-16**, or Strymon's own **MIDI Conduit**.
- Required pedal MIDI settings for Nixie to talk to it:
  - `MIDI PA` (program/param) = **ON**
  - `MIDI CT` (control) = **ON**
  - `MIDI TH` = **MERGE** (or `ON` on older firmware)
  - `MIDI ST` = **OFF**
- MIDI carries data only, not audio — you still monitor the pedal's audio output normally.

## Practical notes
- Note Nixie 1 vs Nixie 2: Nixie 1.0 compatibility was added to TimeLine firmware in v1.84; Nixie 2 is the current build. Either works for backup/edit; use 2.
- For THIS rig: Nixie is the clean way to maintain the TimeLine as a benched/failover unit — build a small bank of failover-ready presets (H90 delay subs, the Dual/Edge patch, the drone patches) offline, then sync them before a session. Backups mean a benched pedal's library survives the bench.
