https://www.strymon.net/support/nixie-2/
strymon.net · Strymon (official) · Nixie 2 support page (current editor/librarian)

How the Nixie / Nixie 2 preset ecosystem works for the TimeLine: connection, backup, the .syx sharing format, and import. Cross-referenced with the Nixie public-beta page (https://www.strymon.net/nixie-public-beta/), the legacy Preset Librarian support page (https://www.strymon.net/support/preset-librarian/), and the backup/restore gear guide (https://www.strymon.net/gear-guide-backing-restoring-presets-bigsky-mobius-timeline/).

## The software, and which to use
- **Nixie 2** is the CURRENT graphical preset editor + librarian for TimeLine, BigSky, and Mobius. Use this.
- **Nixie (original / public beta)** — superseded by Nixie 2.
- **Strymon Preset Librarian** — LEGACY, discontinued. Older "This Week's Preset" download links reference it, but the .syx files it produced are the same format Nixie 2 reads, so legacy downloads still load.

## How it connects to the TimeLine (no USB on the pedal)
The TimeLine has 5-pin MIDI only — no USB jack. You need a real MIDI interface from the pedal's MIDI IN **and** MIDI OUT to the computer. Strymon's tested/recommended interfaces:
- Roland UM-ONE MKII
- iConnectivity MIO XC
- Strymon Conduit
Strymon explicitly warns: "every 'plug-and-play' MIDI interface that we have tested has failed." Use one with dedicated OS drivers.

Required TimeLine GLOBALS before connecting:
- MIDI PA (Program Adjust) and MIDI CT (Control): **ON**
- MIDI TH (Thru): **MERGE**
- MIDI ST (Send tempo / clock send): **OFF**
- MIDI CH: unique per pedal (TimeLine commonly on Channel 1)

## Backup is automatic
On launch, Nixie auto-detects connected Strymon pedals over MIDI, fetches all presets, and shows them in the Device Details window. "All your presets will be automatically backed up as soon as Nixie has detected your device." Real-time bidirectional sync: turn a knob on the pedal and it moves in Nixie, and vice versa.

## The sharing format: .syx (SysEx)
- Presets are stored/shared as **.syx (MIDI System Exclusive) files**. One file can hold a single preset or a full backup set.
- This is the universal currency for TimeLine preset sharing — every Strymon "This Week's Preset" download, every paid pack, and any community trade is a .syx file.

## Importing a downloaded preset
- File → Presets → Import Preset → select the .syx file. (Nixie also supports **drag-and-drop**: drag a .syx straight from a browser/Finder into the Nixie window.)
- Then write it to the pedal slot you want.
- Offline mode lets you build/audition presets for a pedal you don't physically have connected.

## Honest notes on the "community"
- There is **no in-app social/preset-marketplace** in Nixie 2 — the docs describe no sharing community feature. Sharing happens by passing .syx files around (Strymon's own blog, forums, Discord, paid stores).
- Strymon's official free preset stream is **"This Week's Preset"** (https://www.strymon.net/category/this-weeks-preset/) — each post has a downloadable .syx plus a settings image. This is the best-curated free source (see separate captured files for specific on-aesthetic ones).
