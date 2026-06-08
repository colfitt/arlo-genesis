https://www.elektronauts.com/t/the-crossfader-transition-thread-tips-tricks-etc/4073
elektronauts.com · Octatrack subforum · long-running flagship thread (see also /t/your-favorite-x-fader-scene-tricks/961)

# THE crossfader + scene performance thread — concrete tricks

The crossfader is widely called "the greatest thing about the Octa." This thread is the performance bible for it.

## Scene-stacking layout (the workhorse system)
- Build **scenes 1–8 on the LEFT (Scene A) bank** and **scenes 9–16 on the RIGHT (Scene B) bank** mentally; as you progress a piece you copy a scene, modify it, and fade across — incremental morphs without ever switching pattern.
- Each scene is a snapshot of locked params across all tracks; copy a scene, tweak one or two params, and the fader becomes a smooth automation lane between "before" and "after."

## XVOL / XLEV — the equal-power / no-dip trick
- Lock **XVOL** (or **XLEV**) on the transition track(s) per scene. The Min/Max you set are tied directly to the track Volume settings.
- To crossfade between two sources without the level dip at center: set one source's level lock to MAX in Scene A / MIN in Scene B and the other inversely — the fader becomes an equal-power-ish A/B blend. This is how you avoid the classic "quieter in the middle" sag.

## The song/section TRANSITION trick (capture-and-fade)
- Use **record buffers + the crossfader to transition between songs/banks live.** Rather than continuous looping, fire a **one-shot record trig quantized to pattern length** (e.g. 64 steps / 4 bars) to grab a static snapshot of the outgoing section into a buffer. That captured snapshot won't drift or re-compress. Hold it on one side of the fader while you switch banks/patterns underneath, then fade to the new material. Seamless live set transitions with no gap.

## The master-compressor gotcha during transitions (IMPORTANT)
- If you resample through the **master track**, the **master compressor re-processes the sampled audio**, causing unwanted level/dynamics jumps when you then play that buffer back. Two fixes users cite:
  1. **Resample through CUE instead of the master track** (clean, un-recompressed capture), or
  2. **Scene-lock the master Compressor MIX down to 0** during the transition so it doesn't double-compress.

## Other fader tricks in the thread
- Scene-lock filter cutoff wide-open on A / swept-shut on B for a hand-played filter sweep.
- Scene-lock FX feedback (delay/freeze) high on one side for a build into a wash, then fade back.
- Be aware different machines/material react differently — loops may get quieter/louder across the fade depending on their gain; tune XVOL per material.
