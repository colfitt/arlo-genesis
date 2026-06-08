https://www.youtube.com/watch?v=qcfjc2w_L60
EZBOT · A Guide to the Best Resampling Method for the Octatrack · 2022-11-07

The fastest, no-setup resampling method on the OT — no dedicated Flex track, no one-shot trigs, just the always-available recording buffer + the `[REC3]` internal-resample shortcut. EZBOT is one of the best current OT performance educators (sells the Ultimate FX / Solo / Techno templates).

## Premise
- Fresh project, drums on tracks 1–4 (kick/snare/hat/cymbal), simple pattern (running into a bus compressor so levels shift as instruments drop). **Track 8 = MASTER** (he notes nearly everyone runs a master track — it costs you one track but everything sums into it).
- Every track has a **recording buffer available at all times**; `[REC3]` (the internal-source rec button) is the long-available shortcut into it. You do **not** need to be on any special track — you can resample from any track, even the master.

## Method 1: resample the whole mix (the master track)
1. Go to a spare track (he uses track 5, just to stay tidy).
2. `[FUNC]` + `[REC]` → **REC SETUP 1**: choose what to capture.
   - **SOURCE 3 = TRACK 8** (the master) — captures the summed mix at its real volume and panning, identical to what you hear.
   - **RECORDING LENGTH = 4 bars** (keep it simple).
   - **Deselect inputs A B C D** so you don't record incoming noise from connected machines.
   - TRIG = 1 2 (doesn't matter here; the fixed length governs).
3. **REC SETUP 2**: he keeps **fades in/out** (not needed here, but helpful for melodic resampling where sounds overlap). Set **QUANTIZE RECORD = PATTERN LENGTH** (recording won't start until the top of the pattern; pattern length sets when it starts). QPL (quantize playback) doesn't matter here.
4. Start the pattern, hit **`[REC3]`**. The audio indicator flashes (internal audio passing), the **plus (+)** confirms recording. It captures one pass.

## Auditioning + saving the capture
- The audio editor shows the *current* track's sample — on an empty static track you see nothing. Switch the editor to the record buffer: **`[FUNC]` + `[REC3]` → EDIT THIS RECORDING** → there's the new sample.
- **Set that track's LEVEL to 127** so it doesn't attenuate — then it plays back at the exact volume you sampled.
- Save: file settings, or **`[REC3]` → SAVE THIS RECORDING** (auto-named with a timestamp). Then double-tap the track → select the saved sample → it loads into the static track.
- Mangle it: **QUICK CREATE SLICE GRID → set to slices → keyboard layout = slices** → scatter trigs with random slice assignments. Now you can mute the original drum tracks and just play the layered bounce — repeat to build ever-deeper layered/chopped samples. ("What the Octatrack is so good at.")

## Method 2: resample only *some* tracks (the CUE bus)
- REC SETUP 1 → **DESTINATION/SOURCE = CUE**, then **cue up only the tracks you want** (he cues kick, snare, cymbal — leaving the hat out). Play, hit `[REC3]`, wait the length.
- `[FUNC]` + `[REC3]` → EDIT THIS RECORDING → the bounce contains only the cued tracks (a selective "mixdown"). Save → assign to a free static (lands on track 6).

## Method 3: resample on the master track itself (last buffer)
- REC SETUP 1 → SOURCE = TRACK 8, RECORDING LENGTH = 16 (pattern is 16 steps), QUANTIZE RECORD = PATTERN LENGTH. Play → `[REC3]`; it waits for the master to finish, then records 16 steps.
- Caveat: on a **master track you cannot preview/audition** the captured sample (no play functions enabled) — but it works. Useful when record buffers 1–7 are all used: **buffer 8 (master) is still available**.

## Rig relevance
This is the core "capture and destroy" loop for the OT-on-the-desk role: print the whole mangled pedalboard mix (or a selective stem via the CUE method) to a buffer with one `[REC3]`, save, slice-grid it, and re-sequence — no special tracks or workaround. Method 2's CUE-bus selective resample is exactly how you'd isolate "just the banjo" or "just the wall" out of a full performance to the interface. Always set the captured track LEVEL to 127 so re-sampled layers don't quietly lose level each generation.
