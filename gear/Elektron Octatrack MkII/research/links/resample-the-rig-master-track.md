Manual: Octatrack MkII User Manual, §9.1–9.2 (p.44–48), §17.1 (p.104), §17.2 (p.107–108), §17.3 (p.109), §13 audio editor / slice
Elektron manual

# RESAMPLE the rig — capture the pedalboard print, slice it, re-sequence it (+ master track)

The OT's resampling loop: **capture → mangle → resample the mangle → mangle that.** This is where a sustained fuzz wall or banjo phrase becomes something the guitar never actually played.

## Track recorders (the resampling engine)
- 8 track recorders, always available (one per track), independent of what machine the track holds.
- Sources set in **RECORDING SETUP 1** ([FUNC]+[REC1]): **INAB** / **INCD** (external pairs) and **SRC3** (internal: MAIN mix, CUE mix, or any track T1–T8 — that's how you resample the OT's own output).
- **RLEN** = record length in steps (BPM-locked; MAX = full reserved RAM, ~16 s by default, expandable in MEMORY menu). **TRIG** = ONE / ONE2 / HOLD.
- Captured audio lands in **recorder buffers 1–8**, which live at the top of the **Flex sample slot list**. To play a capture, **assign its recorder buffer to a Flex machine** on a track. Convention: buffer 1 → track 1, etc.
- **Buffers are volatile** — overwritten on next sample, and lost on power-off / project change. **Save** keepers: [FUNC]+[REC3] → SAVE THIS / ALL RECORDINGS (or via the audio editor FILE menu).

## Capture methods
- **Manual:** [TRACK]+[REC1] = sample input A/B; [TRACK]+[REC2] = sample C/D; [TRACK]+[REC3] = sample internal (per SRC3). (RECORD QUICK MODE lets you skip the [TRACK] press.)
- **Recorder trigs (automated):** in GRID RECORDING, place a recorder trig ([TRIG] while in RECORDING SETUP) — each trig starts a capture in sync. **One-shot recorder trigs** ([FUNC]+[TRIG], yellow) fire sampling once — ideal live so the trig doesn't re-capture every loop.
- **QREC** (RECORDING SETUP 2) quantizes the start of a manual/Pickup capture (PLEN = at next pattern wrap; or N steps) → perfect bar-aligned loops of the synced rig.

## Slice + re-sequence (turn the wall into a new part)
1. Load the capture (recorder buffer) into a **Flex machine**. Set track length 16/16 ([FUNC]+[PAGE]).
2. Open the **audio editor** ([TRACK]+[BANK] for the recorder buffer): TRIM start/end, then **SLICE menu** ([AMP]) → CREATE SLICE GRID → e.g. 16 SLICES. (Or slice on transients — for banjo set a high TSNS so slices land on picks.)
3. **SRC SETUP: SLIC = ON** so the **STRT** parameter selects slices. Place a sample trig per step; each step's STRT picks a slice.
4. **CREATE RANDOM LOCKS** (in SLICE EDIT) scatters the slices across the trigs → instant glitch re-sequence; repeat until you like it. Or hand-p-lock STRT + PITCH per step.
5. Add conditional/probability trigs, retrig (RTRG/RTIM), reverse (negative RATE), and Lo-Fi/Spring FX for the degraded character.

## Keep captures in BPM sync (§17.3 "by the book")
- Recorder-trig captures inherit the current OT BPM automatically.
- For imported/manual loops: in the audio editor **ATTRIBUTES** ([FX1]) set **ORIGINAL TEMPO** to the loop's true BPM and **TIMESTRETCH = NORMAL or BEATS**; then **SRC SETUP TSTR = AUTO** so the loop stretches to any project BPM. Use **SAVE SAMPLE SETTINGS** (FILE menu) to bake start-point + tempo into the sample.

## The master track (track 8) — final FX & level on the whole mix
- Turn **track 8 into a master track** to apply **master FX and level to everything**, including the DIR-monitored inputs (which the per-track FX blocks otherwise can't touch).
- Use it as a global EQ/glue/Lo-Fi/limiter stage on the full OT mix before it hits the Apollo/Babyface. **Cue out is not available on the master track**, and master track isn't affected by mutes.
- Drop a Dynamix compressor or a final Lo-Fi/Dark-Reverb on track 8 to "tape-glue" the resampled rig.

## Rig fit
A sustained fuzz/baritone wall resamples cleanly (dense, no gaps → timestretches without clicks). Banjo is the opposite (fast decay) — slice on transients and re-trigger for glitch-lead. The VG-800's COSM pads/synth are continuous-waveform sources that stretch into long drones beautifully.
