# Celemony Melodyne — Usage Guide

> ⚠️ **Not installed on this machine** (wishlist/research). Profile says `installed: false`; no component found on disk. This guide is built from official Celemony docs + community/tutorial sources, tailored to the rig.

Melodyne is a **note-level pitch & time editor** — it "looks inside" a recording and shows it as **blobs** you can move in pitch, time, formant and volume, *non-destructively*, even on chords. In **Logic Pro** it runs as an **ARA2** processor (no record/transfer step). For a texture-focused, banjo-as-lead, drone/doom/shoegaze rig the value is two-sided: (1) quietly fix the **drift/intonation** the GK-5→VG-800 banjo/baritone chain throws off, and (2) **re-pitch, time-stretch, formant-mangle and re-voice** real recordings into pads, chords, harmonised drones and "wrong-analysis" glitch material. Lead with §2 (rig fixes) and §3 (creative) — that's where this earns its keep here.

---

## 1. What it is, which edition, and how it runs in Logic

**The model.** Audio → analysed into **notes/blobs**. The **thin red line** through a blob is its **pitch**; the **blob size** is **volume**. Pitch is split into **three independent dimensions** — pitch-center, pitch-modulation (vibrato), pitch-drift — so you can correct one without flattening the others. That separation is why Melodyne sounds the most *natural* of the tuners and is the whole point of using it over Logic's Flex Pitch. [transcripts/melodyne-celemony-basic-workflow.md, transcripts/melodyne-michael-wuerth-getting-started.md]

**Editions (the dividing line for this rig is Editor):** [links/melodyne-editions-comparison.md]
- **Essential** — Main tool only (pitch/time/duration), basic macros. Monophonic + whole-mix stretch. No formant/drift/vibrato sub-tools, no DNA. (Often free with hardware.)
- **Assistant** — the **full mono toolkit**: separate pitch-center/modulation/drift + **formant, sibilant, transient, amplitude, fade, timing** + **Audio-to-MIDI**. Still can't isolate a note from a chord. *Enough for a single-note banjo/baritone lead.*
- **Editor** — adds **DNA Direct Note Access** (edit **individual notes inside chords** on guitar/banjo/piano/samples), **tempo mapping**, **chord-track adaptation**, **scale editing**. *This is the tier you want for strummed banjo, re-voicing chords, and sampler-building.*
- **Studio** — adds **multi-track editing**, the **Sound Editor** (overtone-level resynthesis), track-transcending macros, quantize-to-reference.

**Running it in Logic (AU-only host):** insert **"Melodyne (ARA)"** in the **first** audio-FX slot, press **Play** to hand Logic the audio — no transfer step, and **edits travel with the region** when you move/copy it. Select several mixer strips, insert on one → a Melodyne window per track. Also available as **standalone app** and **plain plugin insert** (which needs the old Transfer/record step). [links/melodyne-ara2-in-logic.md]

**Get the algorithm right *before* editing** — switching it re-analyses and **wipes existing edits**: [links/melodyne-algorithms-guide.md]
- **Melodic** → banjo/baritone **single-note lead**, vocals, bass.
- **Polyphonic Decay** → **strummed/fingerpicked banjo & baritone chords** (DNA).
- **Polyphonic Sustain** → sustained string/organ/**drone** chords.
- **Universal** → transpose/stretch a **whole loop, mix or rhythm part** as one block.
- **Percussive** → drums/noise/atmospheres re-pitched or re-timed as one block.

---

## 2. Practical fixes for THIS rig (banjo / baritone)

**Fix drifting banjo/baritone intonation (GK-5 tracking drift):**
1. Logic: **Melodyne (ARA)** in slot 1 of the banjo/baritone track; Play to analyse. Set **Algorithm → Melodic** for a single-note line. [transcripts/melodyne-audio-edges-full-beginner-guide.md]
2. **Pitch tool → double-click** a note to snap it to the nearest lane centre — or select a phrase with the Main tool, switch to Pitch, **double-click to snap the whole group**.
3. Use the **Pitch Drift tool** (the most useful one) on any note that sags/rises over its length — it **keeps the vibrato and movement** and just re-centres the average. This is the GK-5/banjo workhorse. [transcripts/melodyne-michael-wuerth-getting-started.md]
4. Reach for **Pitch Modulation** only to gently tame an over-wide vibrato on a sustain — pushed far it flatlines into autotune.
5. **Watch the auto-snap**: Melodyne *averages*. A note that's in tune then drifts flat will average flat — **Note Separation** the in-tune part from the drift, then snap each piece.
6. **Don't snap to the wrong octave/lane** on very flat/sharp notes; **don't tune the GK-5's note-on glitches/breath-equivalents** (small blobs, no red line — leave them).

**Tighten a comped take / gentle timing:** **Time tool** (hold Opt, drag note start) nudges notes to the grid with **neighbours auto-adjusting** so it stays musical — far better than hard audio-quantize. Make sure **Logic's tempo matches the song** so the grid lines up. Keep it to tightening; drastic moves artifact. [transcripts/melodyne-audio-edges-full-beginner-guide.md, links/melodyne-tips-not-about-pitch-and-harmony.md]

**Chords (strummed banjo / baritone):** needs **Editor** + **Polyphonic Decay**. Then DNA lets you grab one note out of the strum to fix a sour string or re-voice the chord.

**Per-note balance:** the **Amplitude tool** rebalances individual notes inside a phrase (cleaner than clip-gain after the fact).

---

## 3. ★ Creative / sound-design use (the interesting part)

All from [links/melodyne-creative-sound-design.md] + [links/melodyne-tips-not-about-pitch-and-harmony.md]:

- **Formant mangle (timbre without pitch).** The **Formant tool** shifts vocal-tract resonances in cents while leaving pitch fixed. **Up** = lighter/smaller body (a banjo note reads ukulele-ish); **down** = darker, cavernous body — great for turning a plucked note into a drone bed. Automate a steady formant sweep across a passage for a slow morph. Best on **monophonic** sources.
- **Stretch a note into a pad.** Drag a blob's edges to time-stretch with **no pitch change** — one plucked banjo/guitar/synth note → a long sustained tone. Stack a few at different formants → an evolving bed. **Texture Mode**/Universal handles ambiguous-pitch material (pads, orchestral, atmospheres) for longer evolving stretches.
- **Make a chord/harmonised drone from one note/line.** **Copy the audio to a parallel track**, delete unwanted notes, **transpose** the kept ones to intervals (+3/+4 = diatonic third, +7 = fifth, +12 = octave), **snap to key**, and **nudge each copy's formant** so the voices have separate "throats." Stack copies → choir/wall from a single banjo or baritone take.
- **Re-pitch / re-tune a sample to a scale.** Set a **scale/key** (Pitch Grid + the tuning-fork **scale editor**) and snap a found sample, field recording, or pedal-swell to your drone's root + fifth (or a custom microtonal temperament — Studio).
- **"Wrong-analysis" glitch generator (very on-aesthetic).** Feed **non-musical/ambiguous audio** (speech, noise, a noisy Microcosm/Chroma Console swell) in, let Melodyne **mis-detect** it, and harvest the octave jumps / rhythmic displacements / ornaments. **Save as MIDI** → drive a mono synth or Kontakt for aleatoric, "recorded-wrong" material.
- **Sound Editor (Studio only):** true overtone-level resynthesis — re-sculpt a note's spectrum for a genuinely new timbre.

**Honest limits:** Melodyne is **offline, monophonic-ish, recording-based editing** — not a real-time generative/granular box. For automatable evolving drones it complements (doesn't replace) Reaktor/granular tools. Extreme stretch/pitch artifacts (often a feature here). Sound Editor is Studio-only; DNA polyphony is Editor+.

---

## 4. Rig-specific recipes (copyable)

**A. Fix banjo intonation (Logic ARA, Assistant+).** Melodyne(ARA) slot 1 → Play → **Algorithm: Melodic** → Pitch tool **double-click-snap** the phrase → **Pitch Drift** on saggy notes (keeps motion) → Note-Separate any "in-tune-then-flat" notes and snap halves → leave breaths/glitches. Bounce.

**B. Turn one recorded note into a chord/pad.** Record a single sustained banjo/baritone note → **Universal** (or Melodic) → **stretch the blob 4–8×** for length → **copy to 2–3 parallel tracks**, transpose to **root / +7 / +12** (snap to key) → **formant-shift each copy** differently → bus all into Big Sky/VintageVerb → instant drone chord/wall.

**C. Creative formant/pitch mangle.** Mono banjo/guitar take → **Formant tool down** for a cavernous body, **Pitch tool** for an unnatural interval leap, exaggerate the **Pitch Modulation** for a synthetic warble → reamp the result through the texture board (Microcosm/Chroma Console/QI).

**D. Retune a sample to your drone's scale.** Drop a found/field/pedal-swell sample in → set **scale = your drone root** via the tuning-fork editor → snap notes → it now sits in key. Optionally **Save as MIDI** and rebuild it in **Kontakt** as a playable instrument.

**E. Build a Kontakt instrument from a banjo sample.** Record/clean the banjo note(s) → stabilise drift → **Save as MIDI** to capture the pitch map, and/or just **bounce the cleaned, perfectly-tuned note** → map it across the keyboard in **Kontakt 8** (let Kontakt's own pitch-stretch handle the playable range; Melodyne's job is the clean, in-tune, formant-shaped source). See `Software/Native Instruments/research/…Kontakt…` for the sampler-build side.

---

## 5. Best learning resources

- **Celemony — "Melodyne 5: The basic workflow"** (YouTube, 3:49) — the official 4-minute orientation: blobs, the three independent pitch tools, Auto Stretch copy/paste. [transcripts/melodyne-celemony-basic-workflow.md]
- **Audio Edges — "FULL BEGINNER GUIDE"** (YouTube, 23 min) — best **tool-by-tool** walkthrough, all the modifier-key shortcuts (opt-cmd zoom, ctrl-click tool picker). [transcripts/melodyne-audio-edges-full-beginner-guide.md]
- **Michael Wuerth — "Everything You Need to Get Started"** (YouTube, 15 min) — clearest on **pitch-drift vs pitch-modulation** and splitting a note into transition/sustain/vibrato. [transcripts/melodyne-michael-wuerth-getting-started.md]
- **Celemony Help Center** — the authoritative reference for **editions**, **algorithms**, **ARA in Logic**, scales, tempo. [links/melodyne-editions-comparison.md, links/melodyne-algorithms-guide.md, links/melodyne-ara2-in-logic.md]
- **Breve Music Studios / Garnish / Sound On Sound** — the creative/sound-design angle (formant, stretch-to-pad, wrong-analysis glitch, retune-to-scale). [links/melodyne-creative-sound-design.md]
- **Sweetwater "5 tips that aren't pitch correction" / MusicRadar harmonies / Producer Society MIDI export** — non-vocal + harmony + audio-to-MIDI. [links/melodyne-tips-not-about-pitch-and-harmony.md]

---

## 6. Common pitfalls / gotchas

- **Choose the algorithm first.** Switching it later **deletes all edits/copies**. [links/melodyne-algorithms-guide.md]
- **Insert as "Melodyne (ARA)" in slot 1.** Not the plain insert, not later in the chain — or edits won't follow the region and you'll be stuck doing manual Transfers. Logic is **AU-only**. [links/melodyne-ara2-in-logic.md]
- **Put it before EQ/comp** — Melodyne tunes the *source*; processing before it (in plain-insert mode) is ignored, processing after it is fine. [transcripts/melodyne-michael-wuerth-getting-started.md]
- **Auto-snap averages** — it can pull an in-tune note flat. Separate then snap. [transcripts/melodyne-michael-wuerth-getting-started.md]
- **Over-modulation = autotune flatline**; over-stretch/over-pitch = artifacts. Use Drift, not Modulation, for natural results.
- **Editions matter for this rig:** strummed banjo/baritone chord editing and chord-track/scale tools need **Editor (DNA)**; overtone resynthesis (Sound Editor) needs **Studio**. Assistant covers single-note leads + formant + audio-to-MIDI.
- **vs Logic Flex Pitch:** Flex Pitch is free and fine for quick mono touch-ups; reach for Melodyne for DNA polyphony, better stretch/formant, scale tools, and audio-to-MIDI.
- **Match DAW tempo** before timing edits or the grid won't line up.
- **CPU/analysis:** each ARA instance analyses + holds audio; bounce/flatten when done to free it.

---

## 7. Captured sources

**Transcripts** (`research/transcripts/`):
- `melodyne-celemony-basic-workflow.md` — Celemony official overview.
- `melodyne-audio-edges-full-beginner-guide.md` — Audio Edges tool-by-tool.
- `melodyne-michael-wuerth-getting-started.md` — Wuerth, drift vs modulation.

**Links** (`research/links/`):
- `melodyne-editions-comparison.md` — Essential/Assistant/Editor/Studio + DNA.
- `melodyne-ara2-in-logic.md` — ARA2 vs plugin vs standalone in Logic.
- `melodyne-algorithms-guide.md` — Melodic/Polyphonic/Universal/Percussive map.
- `melodyne-creative-sound-design.md` — formant, stretch-to-pad, glitch, retune.
- `melodyne-tips-not-about-pitch-and-harmony.md` — non-pitch tips, harmonies, MIDI export.

## Sources
- Celemony: editions <https://www.celemony.com/en/melodyne/melodyne-5-editions> · algorithms <https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_AudioAlgorithms?env=standAlone> · ARA in Logic <https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_LogicARA_InsertVorbereitungen?env=logic> · Save as MIDI <https://helpcenter.celemony.com/M5/doc/melodyneAssistant5/en/M5tour_ExportMIDI_standalone?env=standAlone>
- Apple Support — ARA2 plug-ins in Logic Pro <https://support.apple.com/en-mz/guide/logicpro/lgcp58ce340b/10.7/mac/11.0>
- YouTube: Celemony basic workflow <https://www.youtube.com/watch?v=RkQ2l5TWqeY> · Audio Edges beginner guide <https://www.youtube.com/watch?v=ScHbHOfAQVk> · Michael Wuerth <https://www.youtube.com/watch?v=hck80UJgXKc>
- Creative: Breve Music Studios <https://brevemusicstudios.com/from-tuning-to-sound-design-making-the-most-of-melodyne/> · Garnish <https://la.garnishmusicproduction.com/production/creative-uses-for-melodyne/> · Sound On Sound creative pitch <https://www.soundonsound.com/techniques/creative-pitch-processing> · macProVideo ambient textures <https://www.macprovideo.com/article/audio-software/how-to-create-interesting-ambient-textures-melodyne>
- Tips/harmony/MIDI: Sweetwater <https://www.sweetwater.com/insync/5-things-probably-didnt-realize-melodyne/> · MusicRadar harmonies <https://www.musicradar.com/tuition/tech/how-to-create-vocal-harmonies-with-melodyne-423531> · Producer Society MIDI export <https://producersociety.com/export-midi-from-melodyne-tutorial/>
