https://www.youtube.com/watch?v=WJT_JoWO2tU
True Cuckoo · OCTATRACK Tutorial #2 - sampling · 2015-12-14

A deliberately step-by-step "zero to Octatrack" sampling guide — the same record→crop→assign→play loop repeated on every track until it's muscle memory. The OT is not a synth; it makes no sound on its own (a couple of trickery exceptions), it is built for samples.

## Project + input setup
- `[FUNC]` (the red shift/command key — everything labelled red is reached with it held) + `PROJECT` → CHANGE → CREATE EMPTY PROJECT → `YES`. Default name = today's date; he bumps it to tomorrow's because he'd already made one. Creates the card directory, recording-buffer files, project file.
- Inputs: **A/B** and **C/D**, two stereo pairs (monitored in stereo, but accessible independently). Source here = OP-1 / Pocket Operator into A/B. Input LED blinks when signal is present.

## Setting record levels (do this with DIR at max)
- MIXER (press `[MIXER]`/ones): A/B and C/D channels. Turn **DIR** to **127** — that max is the level being recorded regardless of monitor state, so check headroom there: green OK, **orange = borderline (still risky)**, **red = too loud**. Set the **GAIN** until clean, then turn DIR back down if you don't want to monitor it.

## Recording into buffers (hard-coded routing)
- Hold the **track** + press `[REC]`: icon turns to **plus (+)** = recording, runs to max buffer length (~16 s default) then auto-stops to a stop sign; or stop manually. He records kick, snare, hi-hat, a glass "ding."
- Key model: **track N always records to RecordBuffer N** — hard-coded. You can record into a buffer without disturbing whatever's playing on that track. Open architecture, slightly confusing at first, very powerful.

## Getting buffers onto tracks (Flex + buffer select)
- Double-tap `PLAYBACK` on a track → machine menu: STATIC / **FLEX** / THRU / NEIGHBOR / PICKUP. Only **Flex** can play back the recording buffers / live-recorded audio. Set all tracks to Flex.
- Double-tap the track button again → sample-select list: top entries are the **8 recording buffers**, below them 128 free Flex slots. Assign track 1 → RecBuffer 1, track 2 → RecBuffer 2, etc.
- Trig keys 9–16 (the red strip) trigger the sample. They **loop by default** — fix in the PLAYBACK right-page: **turn LOOP OFF** (key layout mirrors note layout). Now they fire one-shots.

## Metronome + pre-roll for live recording
- `[CUE]` + `[TEMPO]` = metronome on/off shortcut. Click is headphones/CUE-only by default; to hear it in MAIN: `[FUNC]` + `PROJECT` → CONTROL → METRONOME → MAIN level (he leaves ~15).
- Same menu: **PRE-ROLL** → 1 BAR, so `[REC]` + play counts in a bar before recording.

## Cropping recordings (remove the silent head)
- Select track → `[BANK]`/EDIT → editor. The nav encoders: one zooms the waveform *level* (display only), one zooms the *timeline*. Set the **end point** tight to where the hit ends.
- To crop: in TRIM you set in/out; switch to **EDIT** page, press `YES` → menu → **CROP TO SELECTION** → `YES` (everything outside selection is deleted). Watch which page you're on.
- **Zero-crossing**: when a white square appears around the selection point, you're on a zero crossing (no click on playback start). Hold `[FUNC]` while making the selection to snap-find it.

## Playing pitched + chromatic keyboard
- Default keyboard just launches the sample. `[FUNC]` + down/up = keyboard modes; go one down to **CHROMATIC** — now the trig keys play the sample across the keyboard (lit LEDs = white keys, unlit = black keys). `[FUNC]` + left/right transposes the playable range down/up an octave.
- Record a pitched melodic line live; the **pitch is written into each trig** as a p-lock (visible per-step in trig edit).

## Longer patterns + copy/paste pages
- Toggle GRID/program mode (`[REC]` lit = programming, off = jamming).
- `[FUNC]` + SCALE SETUP, press repeatedly to **add pages** (16 steps each → up to 4 pages = 64 steps).
- Copy a page to the next: with the PAGE button, `[FUNC]` + COPY, move to next page, `[FUNC]` + PASTE (repeat to fill all pages).
- Mute a track: `[FUNC]` + the track key.

## Time-stretch behaviour (AUTO is smart)
- PLAYBACK page → TIMESTRETCH = AUTO / ON / OFF. In AUTO the OT inspects the sample and decides: **very short sounds → stretch off** (snare stays the same length at different pitches), **longer sounds → stretch on** (a bass loop stays the *same length* regardless of pitch). Turning stretch OFF on a long sample makes lower pitches longer and higher pitches shorter (vari-speed) — useful creatively.

## Syncing a free-recorded loop: CALCULATE BPM FROM SECTION
- Record a turntable/loop into a buffer (it'll be the wrong tempo). In the editor, set the **loop points** around exactly one bar (zoom in to find the downbeats), then EDIT page → `YES` → **CALCULATE BPM FROM SECTION** → it suggests a value (e.g. 106 BPM) and sets the sample's tempo. Now at project tempo 120 the loop time-stretches into sync. Place a trig on page 1 to start it on the downbeat.
- He fits it under a busy mix with FX1 = **DJ EQ** (kill the competing low end).

## CRITICAL: saving (two separate saves)
1. **Save each buffer to a file** — recording buffers are wiped on every project load. Track → EDIT → FILE → **SAVE AND ASSIGN SAMPLE** → name (auto name = track + buffer + date/time) → **ASSIGN TO FREE FLEX** (keeps the buffer free; "assign to self" puts it back in the buffer). The saved file appears in the Flex slot list — re-select it on the track. Repeat per track. (You can also browse the card from the slot list and `[FUNC]` + `YES` to preview any sample before loading.)
2. **Save the project** — `[FUNC]` + `PROJECT` → SAVE → "any previously saved state will be lost, continue?" → `YES`. This is the state you reload to after a live performance has trashed everything.

## Rig relevance
The crop-to-zero-crossing and CALCULATE-BPM-FROM-SECTION steps are exactly what you'd do to lock a captured pedalboard bar (or a banjo phrase from the VG-800) cleanly to project tempo before slicing. The TIMESTRETCH=AUTO note matters for the rig's two extremes: sustained fuzz walls get stretched/held; fast banjo transients should often be stretch-off so they keep their attack.
