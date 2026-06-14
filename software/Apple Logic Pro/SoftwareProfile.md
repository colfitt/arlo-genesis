---
name: Logic Pro
brand: Apple
category: software
subcategory: daw
formats: [au, standalone]
host_in: []
host_for: [au]
installed: true
install_path: /Applications/Logic Pro.app
version: latest
status: owned
tags: []
related: []
---

# Apple Logic Pro

**Summary** — Apple's flagship DAW. **AU-only host** (no VST/VST3/AAX). The
studio/assembly end of a hardware-front rig.

## Why I have it
Primary DAW and studio hub: the place the hardware-front chain (pedalboards,
VG-800, Elektrons, OP-1, MPC) gets **recorded, reamped, and committed**, plus a
deep stock-plugin toolkit (ChromaVerb, Space Designer, Sample Alchemy, Tape
Delay) that already covers the drone/tape/lo-fi aesthetic before any third-party
plugin.

## Signature uses
- **Reamping the board** via the I/O plugin (Ping latency comp) or pre-fader
  send → Apollo x8 → Radial X-Amp → pedals/VG-800 → back in.
- **ChromaVerb Freeze** infinite clouds + **Space Designer custom IRs** (drag in
  pedalboard tails / field recordings) for walls of sound.
- **Sample Alchemy** granular drones + **track-header drag** to sample the
  banjo/pedalboard into a playable instrument.
- **Stock tape/lo-fi degrade**: Tape Delay (0 ms, 100% wet) + Bitcrusher as
  saturators.
- **MIDI clock / multitrack** out to Digitakt 2 (Overbridge stems) & Octatrack
  (DIN clock + analog-out audio).

## Notes
- **AUv2 detection is broken at the OS level** — new AUs often need a reboot;
  Reset & Rescan / clear the audiounits cache / "use anyway" if validation flakes.
- **Offline bounce of a hardware (I/O-plugin) track = silence** — use Real-Time
  bounce or bus-record.
- **Aggregate Device (Apollo + Babyface)** → clock-master conflict can crackle;
  pick one master. MIDI clock as master has tiny 24-ppqn drift.
- Deep usage research → `research/Logic-Pro-UsageGuide.md` (9 transcripts + 27
  links).
