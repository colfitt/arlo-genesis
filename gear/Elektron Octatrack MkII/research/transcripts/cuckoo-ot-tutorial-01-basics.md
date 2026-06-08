https://www.youtube.com/watch?v=NrhPOGzn7LI
True Cuckoo · Octatrack Tutorial #1 - CUCKOO · 2015-03-21

The canonical Octatrack on-ramp. Cuckoo's framing up front: it is not actually *complicated*, it is *deep* — "a lot of opportunities," not a lot of complexity. Everything below is done live, sampling the OP-1 (and a mic) into the box.

## Project setup
- New project: `[FUNC]` + `PROJECT` → CHANGE → CREATE EMPTY PROJECT → name it. Creating a project writes a directory to the CF card (the card-status LED blinks while writing, goes solid green when idle — do not pull the card while blinking).
- OP-1 patched into **Inputs A/B**.

## Choosing a machine: Flex vs Static
- Each track defaults to a **Static** machine. Double-tap the track's `PLAYBACK`/machine button to change the machine type.
- Change all tracks to **Flex** (use the arrow). Flex vs Static: Flex is "more flexible," the biggest difference being **timestretch** — Flex lives in RAM and is the malleable one. This tutorial uses Flex throughout.

## Recording slots (the key mental model)
- Each track gets assigned one of the **8 recording slots** (RecordBuffer 1–8). On the recording page, set track 1 → recording 1, track 2 → rec 2, etc. These buffers are silent until you record into them.
- Why pre-assign: it lets you record *additional* sounds into buffers that aren't currently in the music — plan-ahead recording, capture new material live without disturbing what's playing.

## Recording a sample live
- MIXER menu: turn up **DIR (direct monitor)** for the input channel so you can hear the source (layout of the encoders mirrors the on-screen layout). **127** is roughly the level that gets recorded; you can GAIN a quiet signal up.
- Handy: hold `[FUNC]` while turning an encoder to **snap to values** (full / zero / full-negative) — used constantly to try then reset.
- To record: arm with `[REC]` on the target track — the icon turns to a **plus (+)** while recording, back to a stop sign when done. Stop manually by pressing the track + stop.
- Audition the buffer: press the track + play.

## Editing / trimming a sample
- Enter edit: select the track, press `[BANK]`/EDIT to enter the **Audio Editor**.
- The three navigation encoders = **start point**, **end point**, **loop point**. A fourth scales the *visual* gain of the waveform (display only, no sound effect). Other encoders = scroll and zoom.
- `[FUNC]` + `YES` = preview playback from the current playhead position (hold).
- Cuckoo trims the silence off the front by moving the start point to a good zero-crossing, then sets loop/end.

## Sequencing + the out-of-sync problem
- `[GRID]` (the sequencer) → place a trig on the track, press play.
- Lengthen the pattern: `[FUNC]` + `PAGE`, SCALE SETUP, add pages → a 4× longer sequence.
- A free-recorded loop will be out of sync. Turn on the metronome: `[FUNC]` + `[CUE]` to toggle, or route it — by default the click is headphones-only; PROJECT → CONTROL → METRONOME lets you send it to CUE volume and **MAIN** too. Also has **pre-roll** (e.g. 1 bar) for studio recording.

## SLICING (the headline technique — used on every track)
- Edit mode → **SLICE** mode → zoom in → position the playhead with the LEVEL knob (LEVEL acts as the timeline scrubber in this view) → press `YES` to drop a slice. A little white square around a marker = the OT snapped to a **zero crossing**.
- Drop slices across the whole sample to chop it into playable hits.
- To *play* slices: turn the trig row into a slice keyboard — `[FUNC]` + up/down cycles keyboard modes (TRACKS / CHROMATIC / SLOTS / **SLICE** / QUICK MUTE / DELAY CONTROL). Choose SLICE.
- But first the track must be told to use slices: **PLAYBACK menu → turn SLICES on.** Then the trig keys play each slice.
- He repeats the whole chain on a recorded **kick drum** (slice the two kicks, slices on, loop off so they don't loop), a **mic/voice "beatbox" kit** (slice the vocal sample → instant drum kit), and a melody.

## Building a kick from a filter
- Pitch the kick sample down in the PLAYBACK menu.
- FX1 default = **filter**, FX2 default = **delay** (double-tap the FX slot to see/swap the effect; FX1 options: filter, EQ, DJ-EQ, phaser, flanger, chorus, spatializer, comb, compressor, lo-fi; FX2 adds delay, plate reverb, spring, duck).
- Crank the filter **resonance** and hunt the low-cut frequency for a sub thump — "remember these numbers" to recreate a kick fast (he lands near 31). Both the low-cut and high-cut sides have their own resonance.
- For grit: FX1 → **Lo-Fi** (distortion + bit reduction); FX2 → **Dark Reverb**, set to **send** rather than mix.

## SCENES + the crossfader (the performance soul)
- Two scene buttons: **SCENE A** and **SCENE B**. Press `[SCENE A]` then a trig to assign which scene A holds; same for B. The selected scene lights red.
- Convention: **Scene A = clean**, **Scene B = the changes**.
- Hold a scene + tweak a parameter to lock it into that scene. Examples he locks: max **pitch** on a melody; negative **RATE** (playback speed → reverse) on a scene; a whole-pattern pitch shift (pitch the melody up while everything else goes down); an **LFO depth** lock (LFO 1 routed to pitch → instant vibrato, dial speed faster).
- The crossfader morphs A→B live. **Leapfrog trick:** while sitting on scene B (slot 2), reassign scene A to a *new* scene, fade to it, then reassign B, and walk through many states by alternately reassigning the off-side. "Extremely powerful... you can do this really fast."

## Master track + the freeze-delay buffer trick
- PROJECT → AUDIO → set **Track 8 = MASTER** (vs NORMAL). Track 8 then carries no samples of its own; everything passes through it — put a master high-pass/low-pass here (e.g. a DJ kill on scenes 15/16) and master FX.
- **Delay buffer lock** (a staple live move): on the master delay, double-tap to open its settings; it has a **TAPE mode** (delay buffer pitches up/down with time changes — digital-sounding, not a real tape). Turn **LOCK on**: when LOCK is on and **SEND = 0**, the delay freezes its buffer and mutes the live input — it loops the captured buffer. Crank **FEEDBACK** to max so the frozen fragment sustains. Used for "rhythmical hiccups."
- **DELAY CONTROL** keyboard mode (`[FUNC]` + arrow) exposes per-track delay live: each track with a delay shows T1, T2... and you can change the delay **TIME** (e.g. 32) live for stutter/rhythm changes. In TAPE mode it pitches; otherwise it cuts the buffer cleanly.

## CRITICAL: saving (or you lose everything)
- Recording slots are **wiped on every project load** — they are scratch buffers, not storage. Before powering down you must save each buffer to a real file.
- In edit mode → FILE menu → **SAVE AND ASSIGN SAMPLE** → name it → **ASSIGN TO FREE FLEX** (assigns the saved file to a free Flex slot). "Assign to self" puts it back in the same recording-buffer place — usually not what you want if you'll record again. Repeat for every buffer you care about.

## Rig relevance
This is the foundation for the "capture the pedalboard print and re-sequence it" workflow: record the stereo wall into a buffer (A/B in, DIR monitor up, `[REC]`), slice it, turn SLICES on, scatter the slices with the trig keys, and crossfade between clean (Scene A) and pitched/reversed/Lo-Fi'd (Scene B). The master-track delay-buffer freeze is exactly the "capture a fragment and sustain it forever" move for drone beds.
