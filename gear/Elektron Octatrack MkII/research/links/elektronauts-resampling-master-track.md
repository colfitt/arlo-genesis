https://www.elektronauts.com/t/internal-resampling-help/14930
elektronauts.com · Octatrack subforum (+ "Resampling thread" /36129, "live resampling workflow" /198480, "resampling and rearranging the master track" /33802)

# Internal resampling + master track — the exact recipe

The OT's signature loop: capture → mangle → resample the mangle → mangle that. "Resample, resequence, rinse, repeat." Here's the concrete setup people actually use.

## Master track (track 8)
- Set **track 8 = MASTER** (a special routing where T8 sums the whole mix; can hold a master Compressor + reverb). It is THE thing you resample to capture "everything happening."

## Internal-resample REC setup (exact steps)
1. Open the RECORD menu: **FUNC + REC (A/B)**.
2. **Turn OFF INAB and INCD** (you're not recording the external inputs — you're resampling internal).
3. Set **SRC3 = MAIN** (the main mix) — or **better, SRC3 = T8** if track 8 is set as the master track (cleaner, captures the summed mix).
4. Assign the record trig to SRC3: **hold TRIG 1 + press [MIDI]** to make that trig a SRC3 (internal) record trig.
5. **Use a ONE-SHOT record trig (FUNC + TRIG), not a normal/continuous record trig** — this is the #1 mistake; a normal rec trig re-records every loop. One-shot fires once.
6. Set **RLEN = the pattern length** (usually 16 or 64 steps) so the capture is exactly one loop.
7. Workaround if it misbehaves: as soon as the track starts, remove the first trig and set **LOOP = OFF**.
- The capture lands in that track's **recorder buffer**, which appears at the top of the Flex slot list as a "Flex recording" (RECORDER1–8) — load it onto a Flex machine on another track to slice/play/mangle.

## Level / gain consistency (the recurring gotcha)
- Resampling through the **MASTER track re-applies the master Compressor**, so the resampled buffer can come back louder/squashed. Fixes: **resample via the CUE bus instead**, or **scene-lock master Compressor MIX = 0** while capturing. (See crossfader-scene-tricks note — same trap during transitions.)

## Timestretch matters for resampled loops
- Best creative results: **TIMESTRETCH = ON** on the resampled Flex sample (keeps it locked to BPM; the tiny fidelity cost is worth it).
- **TIMESTRETCH = OFF** has uses too: playing with RATE/pitch on a non-stretched buffer is interesting, AND **you can OVERDUB with a Flex machine using CUE as the source even in SLAVE mode when timestretch is off** — a way around the "pickups can't overdub when OT is slaved" bug.

## Workflow philosophy from the threads
- Chop/re-sequence the resampled loop rather than just looping it raw.
- Embrace imperfection — loops slightly off-grid or using **RTIM** (record timing offset) generate more interesting results.
- For live sets: record the master on loop to capture all your live tweaks, then beat-juggle / crossfade between the captured loop and live performance on top. Fast crossfader snaps (not slow fades) for beat-juggle feel; use conditional trigs / FILL for variation during transitions.
