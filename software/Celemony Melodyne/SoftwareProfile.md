---
name: Melodyne (latest)
brand: Celemony
category: software
subcategory: effect
formats: [vst3, au, aax, ara2, standalone]
host_in: [logic, ableton]
installed: false
version: latest
status: not-installed
tags: []
related: []
---

# Celemony Melodyne (latest)

**Summary** — Pitch and time editor with note-level audio editing.

> ⚠️ **Not installed on this machine.** Listed as owned/wishlist for research.

## Why I have it
Note-level pitch & time editor — the surgical tool for two rig problems. **(1) Repair:** quietly fix the drifting intonation the GK-5 → VG-800 banjo/baritone chain produces, and tighten comped takes without robotic audio-quantize. **(2) Creative:** re-pitch / time-stretch / formant-mangle / re-voice real recordings into pads, harmonised drones, and "wrong-analysis" glitch material — the texture side, not pop-vocal tuning. In **Logic Pro** it runs as **ARA2** (no transfer step; edits follow the region). Pairs with Kontakt 8 for sampler-building from cleaned, in-tune source notes.

> Edition matters: **Assistant** = full mono toolkit (pitch/formant/drift/amplitude + audio-to-MIDI) — enough for single-note banjo leads. **Editor** = adds **DNA** (edit notes inside strummed banjo/baritone **chords**), tempo & scale tools — the meaningful tier for this rig. **Studio** = Sound Editor (overtone resynthesis) + multitrack.

## Signature uses
- **Fix banjo/baritone drift** — Melodic algo, Pitch-tool double-click snap, then the **Pitch Drift tool** (keeps vibrato/movement, just re-centres) — the GK-5 workhorse.
- **One note → pad/chord** — stretch a single note, copy to parallel tracks, transpose to root/+7/+12 (snap to key), formant-shift each copy, bus into Big Sky/VintageVerb.
- **Formant mangle** — drag formant down for a cavernous drone body without changing pitch.
- **Retune a sample/field-recording to the drone's scale** via the tuning-fork scale editor.
- **"Wrong-analysis" glitch** — feed noise/swells in, let it mis-detect, **Save as MIDI** → drive a mono synth/Kontakt.
- **Audio-to-MIDI** banjo/bass lines to rebuild as Kontakt instruments.

## Notes
- **Not installed** on this machine (wishlist). Guide built from Celemony docs + tutorials.
- **Choose the algorithm first** — switching it re-analyses and **wipes all edits** (Melodic / Polyphonic Decay / Polyphonic Sustain / Universal / Percussive).
- **Logic = AU-only**: insert **"Melodyne (ARA)" in the first FX slot** so edits travel with the region; ARA skips the Transfer/record step the plain plugin needs.
- Three independent pitch dimensions (center / modulation-vibrato / drift) → correct intonation without flattening vibrato (why it sounds natural). Use **Drift, not Modulation**, for natural results; Modulation→100% = vocoder/autotune.
- Auto-snap **averages** — an in-tune-then-flat note pulls flat; **Note-Separate** then snap halves.
- **DNA polyphony = Editor+**; **Sound Editor resynthesis = Studio**. vs Logic's free **Flex Pitch** — use Flex for quick mono touch-ups, Melodyne for DNA/formant/scale/stretch/audio-to-MIDI.
- Full guide: `research/Melodyne-UsageGuide.md`.
