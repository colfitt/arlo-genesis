https://www.strymon.net/support/nixie-2/
strymon.net · Strymon (official) — Nixie 2 support + Deco V2 preset/MIDI docs
How Deco V2 presets actually live and load. Distilled from Nixie 2 support, the Deco support pages, and the V1→V2 changelist.

## Where presets live on the Deco V2
- **300 MIDI preset locations** on the pedal (V2 only — V1 had no preset memory). Recalled via **MIDI Program Change** over the 1/4" TRS EXP/MIDI jack or USB-C.
- **Favorite switch / "Favorite" mode** stores ONE preset to a footswitch (set the EXP/MIDI jack to Favorite, or use a Favorite-mode press). Live-Edit secondaries (High/Low Trim, Auto-Flange Time, Wide Stereo, Doubletracker Boost/Cut) ARE saved per preset.
- **Not saved per preset** (set once via power-up): MIDI channel, MIDI OUT mode, Input Mode (Normal/Studio), Bypass mode.

## How presets load via Nixie 2 (the editor/librarian)
- **Deco V2 is supported in Nixie 2** (listed among USB-connected pedals as of Nixie v2.2.0). Connect via **USB-C**.
- Presets are **.syx (sysex) files**. Import flow: **File → Presets → Import Preset → select the .syx**. Same panel exports/backs up. Nixie 2 is the backup/organize/create/share tool.
- You drag a downloaded .syx into Nixie and write it to a preset slot, then recall it on the pedal via Favorite or Program Change.

## "This Week's Preset" status for the Deco — HONEST FLAG
- Unlike the Big Sky (which has many Deco-aesthetic TWP entries with downloadable .syx), **there is no substantial official "This Week's Preset" library specifically for the Deco.** The TWP series skews to the delay/reverb pedals (TimeLine, BigSky, Volante, etc.). I found **no dedicated downloadable Deco preset pack** from Strymon, and **no confirmed community .syx pack** for the Deco in this pass. (Don't claim one exists.) The Deco's preset value is "roll your own scenes in the 300 slots + back them up / share .syx via Nixie 2," not a curated official library.

## Rig note (MIDI is the real win here)
Board 1 is otherwise stomp-and-go, but the Deco's 300 slots mean you can recall a full saturation+doubletracker SCENE per song via Program Change (Wide Stereo, Trims, Boost/Cut all travel with it). If the End Board's MIDI brain sends clock, set **MIDI Clock Sync on the TYPE knob** to lock echo repeats to tempo. Build scenes by ear, save to Nixie 2, recall live.
