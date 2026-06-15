---
type: patch
title: "Synth Mode — play CLOCK with MIDI notes"
device: Chase Bliss MOOD MkII
date: 2026-06-15
description: "Play MOOD's CLOCK (and thereby pitch/character) from a MIDI keyboard — a stray MIDI Note auto-engages Synth Mode, turning CLOCK into pitch control so you can 'play' a frozen pad/drone as a monophonic granular synth with ADSR, portamento, velocity, and selectable output modes. Powerful for sequenced, pitched degradation — but it silently overrides MIDI clock sync. (Factory MIDI feature, new to MkII; no published note-map or ADSR numbers.)"
tags: [midi, synth-mode, clock, granular, adsr, technique, factory]
controls:
  - { name: "MIDI Note input (via Chase Bliss MIDIbox)", type: switch, value: "send a Note to auto-engage Synth Mode — Note transposes the wet output (no published note-to-pitch table; explore by ear)" }
  - { name: "CLOCK", type: knob, value: "becomes pitch control in Synth Mode; move the knob physically to exit back to normal/clock-synced behavior" }
  - { name: "Synth output mode", type: switch, value: "Open (constant drone), On/Off (gate sustain), or ADSR (enveloped) — set over MIDI", options: ["Open", "On/Off", "ADSR"] }
  - { name: "ADSR + portamento + velocity", type: knob, value: "Attack/Decay/Sustain/Release, portamento and velocity are user-set over MIDI (no factory numbers — dial from recipe)" }
  - { name: "Exit (CC59)", type: switch, value: "send CC59 to leave Synth Mode (or physically move CLOCK)" }
---

# Synth Mode — play CLOCK with MIDI notes

## Concept
Play MOOD's CLOCK — and thereby its pitch and character — straight from a MIDI keyboard or sequencer. Sending any MIDI **Note** auto-engages **Synth Mode**: CLOCK becomes pitch control and the note input transposes the wet output, so you can "play" a frozen pad or drone as a monophonic granular synth. Synth Mode adds Attack/Decay/Sustain/Release, portamento, velocity, and three output modes (Open / On-Off / ADSR). It's a strong move for sequenced, pitched degradation — but watch the gotcha: Synth Mode silently overrides MIDI clock sync. New to MkII, flagged in Doug Hanson's demo.

## How to play it
1. Connect a MIDI controller/sequencer through a Chase Bliss **MIDIbox** (converts MIDI to the 1/4" TRS MOOD expects).
2. Capture or freeze a sustained pad/drone as source material.
3. Send a **MIDI Note** — MOOD auto-engages **Synth Mode**, CLOCK becomes pitch control, and the note input transposes the wet output.
4. Choose an output: **Open** (constant drone), **On/Off** (gate sustain), or **ADSR** (enveloped); dial Attack/Decay/Sustain/Release plus portamento and velocity over MIDI.
5. Exit Synth Mode with **CC59** — or physically move the **CLOCK** knob — to restore normal / clock-synced behavior.

## Notes
- ⚠️ MIDI clock is **IGNORED** in Synth Mode — a stray Note from a sequencer (e.g. a Digitakt) silently knocks MOOD out of clock sync. Watch for this when sequencing a stack.
- No published note-to-pitch table and no factory ADSR numbers — the controls above are a dialable recipe; explore by ear / set everything over MIDI.
- Full setup details live in the separate MOOD MkII MIDI manual (not the main pedal manual).
- Doug Hanson's demo flags this as new-to-MkII: "play MOOD's CLOCK with a MIDI controller by sending MIDI notes."

## Sources
- gear/Chase Bliss MOOD MkII/research/transcripts/doug-hanson-mood-mkii-demo.md ("Synth Mode… lets you play MOOD's CLOCK with a MIDI controller by sending MIDI notes"); gear/Chase Bliss MOOD MkII/research/MOOD-MkII-UsageGuide.md §5/§7 (MIDI clock ignored in Synth Mode; stray Note auto-engages; exit via CC59; default channel 2; cb-stack-clock-sync-per-pedal)
- gear/Chase Bliss MOOD MkII/research/links/community-mood-mkii-pitfalls-and-gotchas.md (Synth Mode caveat); community-mood-mkii-vs-original-clock-noise-levels.md (Note Mode — MIDI keyboard transposes wet output)
- MusicRadar "Chase Bliss puts us in a good MOOD…" — musicradar.com/news/chase-bliss-mood-mkii; Effects Database, MOOD MkII (Synth Mode: ADSR/portamento/velocity, Open/On-Off/ADSR) — effectsdatabase.com/model/chasebliss/mood/mk2; Chase Bliss MOOD MkII MIDI manual — static1.squarespace.com/.../MOOD+MKII_MIDI+Manual_Pedal_Chase+Bliss.pdf
- Factory MIDI feature (Doug Hanson demo + cb-stack MIDI deep-dive + official MIDI manual + MusicRadar + Effects Database); no published note/ADSR values
