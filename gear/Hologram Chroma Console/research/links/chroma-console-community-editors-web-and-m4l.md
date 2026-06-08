Multiple sources — community MIDI editors for the Chroma Console
accessed 2026-06-03

# Community editors / controllers for the Chroma Console (no official app exists)

Hologram ships NO official editor app, so the community built three. All rely on the pedal's MIDI CC/PC implementation.

## 1. Chroma Controller — web editor
https://chromacontroller.co.uk/
Browser-based MIDI editor (Web MIDI). Exposes: knob positions, module selections, bypass states, GESTURE and CAPTURE transport (play / record / stop-erase / stop-clear), and an **auto tap-tempo with BPM entry + start/stop**. Save/load **shareable preset files** that export "all current knob positions, module selections, bypass state, etc." — preset files are portable between units (community preset sharing).
- **KEY GOTCHA (developer's own note):** "if you make a great preset on the web and then modify a control on the real pedal, the online interface will not correctly reflect the sound." → Editing is effectively **one-way (web → pedal)**; the pedal does NOT report its state back, so the editor and the hardware can silently desync. Treat the web editor as a sender, not a mirror.

## 2. Chroma Console Controller — Max for Live (vincer)
https://maxforlive.com/library/device/11170/chroma-console-controller
M4L MIDI-effect device; runs on Ableton Live 12 / Max 8.6 (released Oct 2024). Controls common parameters via MIDI CC (delay time, modulation depth, feedback, mix, etc.) and program-change patch switching. Lets you automate Chroma parameters from Ableton timeline/clips and sync to Live's clock — directly relevant if the Digitakt-clocked rig ever runs through a DAW.

## 3. chapelierfou M4L editor (posted on Elektronauts)
A second Max-for-Live editor shared in the Elektronauts mega-thread (Oct 4, 2024) featuring **randomizers, parameter visualization, and program recall**; another user called it "beautiful" for managing presets visually.

## Why this matters for the rig
- With the Digitakt 2 as clock master + a MIDI brain, the pedal is fully scene-recallable via Program Change, and per-module bypass via the v1.04 CCs.
- For preset BUILDING (vs live recall), the web/M4L editors are far less clunky than the pedal's scroll-through browser — build/organize presets at the desk, then recall live by PC.
- Watch the one-way-sync gotcha: don't trust the editor's display after you've touched the hardware knobs.
