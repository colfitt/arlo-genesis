https://www.youtube.com/watch?v=3w181cfjAiw
Native Instruments (KONTAKT: FIRST STEPS, Ch.2 Ep.4) · Steve (composer/engineer/lecturer) · "How to Loop a Waveform to Sustain a Sample"

# Looping waveforms for infinite sustain — distilled

The core technique for making your own recorded samples (e.g. sampled hardware/pedalboard drones) hold indefinitely in Kontakt.

**The problem.** Recorded samples have a fixed length; held chords will "run out" — and because samples are stretched/compressed across the keyboard, different notes run out at *different* times. Solution: loop a section in the middle.

**Workflow in the Wave Editor:**
1. Select a sample/zone → open the **Wave Editor**. It shows the actual audio file recalled when you hit a key in that zone. You can also fix sample **start/end** here.
2. Dragging the start to a new point causes a **click** because it's not landing on a **zero crossing**. There's a **Snap → snap to zero crossing** toggle up top — but he explicitly says "**don't trust that, trust your ears**."
3. To sustain, use the **Sample Loop** section (turn on **one loop**). Do NOT loop the whole file (it'll die out then restart). Loop a section in the **middle**.
4. First pass loops but clicks/pops at the seam → fix with **crossfade**.

**Crossfade settings (key numbers):**
- The **X-Fade** value is measured in **samples** (so are start/end). To get roughly a 1-second crossfade you need a high number — he uses **~50,000**.
- Stretch the crossfade longer if it feels abrupt; compact it if the fade-in/out is too obvious. Trust ears.
- Make the looped section **longer** so it captures more variation before repeating (less "obviously looped").

**Pro tips:**
- There's **no batch way** to set loops across all files — it's per-sample and time-consuming, but that's actually *good* for variation. Trust your ears, not the zero-snap.
- In Ch.1 he cut samples with only **~6 ms of fade** at the start so you don't fight start/end times later — then you only have to loop the ones you want to sustain.
- Works for synthesized AND acoustic sounds: record SHORT, then loop to sustain indefinitely.

**Rig recipe:** sample a sustained pedalboard drone (Big Time / Clean wash) or a bowed banjo note → cut with a tiny 6 ms head fade → map across the keys → loop a stable mid-section with a ~50k-sample crossfade → now one held key = an endless evolving wall, playable from the Novation 61SL or any MIDI in Logic.
