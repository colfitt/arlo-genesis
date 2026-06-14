https://www.youtube.com/watch?v=CtlLBL5o9uI
Sweetwater (Bobby Dellarocco) · "How to Create a Kontakt Sample Instrument" · 11:06

Bobby Dellarocco (Sweetwater Studios) turns a finger piano (mbira/kalimba-type
instrument) into a playable Kontakt instrument — the full sample-to-instrument
pipeline. Directly applicable to sampling the banjo/baritone/pedalboard tails.

## Recording for sampling (capture the variations)
- Recorded all samples into one long audio file in the DAW (Pro Tools).
- **Two passes per key for velocity layers:** round 1 played with the FINGER
  (softer, mellower) → low-velocity layer; round 2 played with a PICK (more
  percussive attack) → high-velocity layer. The pick take is mapped to higher
  velocity on the keyboard. (Recording each note with a different articulation =
  built-in velocity dynamics.)

## Chopping / cleanup in the DAW
- Use **Tab to Transients** to snap the playhead to the start of each sound, then
  separate and delete everything before the transient.
- Each sample: start **right at the top of the transient**; add a **manual fade-
  out** that's "long enough you get the sound but doesn't drag on forever," and a
  tiny **~5 ms fade-in** so playback never starts mid-waveform (avoids clicks).
- Kept a snippet of **ambient room noise** specifically to use as a denoise
  profile.
- **Denoise** with iZotope RX Spectral De-noise: use the **Learn** feature on the
  captured noise snippet to profile it, then remove that exact noise from every
  sample. ("When you re-trigger a sample over and over, even tiny noise drives you
  insane" — denoising is essential for sampled instruments.)
- **Tune** every sample with Melodyne: load all samples, confirm Melodyne tracked
  them **monophonic/melodic** (not polyphonic — it can mis-read overtones as
  separate notes), double-click each blob to snap to note center, fix any that
  are sharp/flat, then commit/render.

## Building the instrument in Kontakt
- Drag the WAV folder onto a fresh Kontakt instance (double-click empty rack to
  create one). Open **edit mode via the wrench icon**, go to the **Mapping
  Editor** — "where you do a lot of the programming."
- Place each sample on its root key; **drag the region's left/right edges to span
  multiple keys** (he spans 2 notes per sample, e.g. C + C# — sampling lets you
  hit in-between notes the acoustic instrument couldn't, e.g. C#, F).
- **Velocity zones:** drag the TOP/BOTTOM edges of a region to set its velocity
  range. Low-vel (finger) sample → velocity 1–64; high-vel (pick) sample →
  velocity 65–127. Now soft playing triggers the finger take, hard playing the
  pick take.
- At the extreme low/high ends, **stretch zones wider** so a few extra notes are
  playable beyond the recorded range.

## FX chain (his "ambient" taste, in-Kontakt insert FX)
- He likes "a bit of ambience and a bit of delay." Order matters:
  **Reverb (Plate) and Delay come BEFORE the Saturator** — so the saturator
  pushes/brings out the reverb tail rather than just the dry sound.
- Adds **Stomps "Saturation"** for grit.
- Adds **NI Transient Master** to tame the attack "just a hair" (softens the pluck
  → more pad-like).
- Result: a fully custom, ambient-flavored Kontakt instrument from a finger piano
  and "pretty basic processing."

### Takeaway for the rig
The exact pipeline for banjo→Kontakt: two articulations per note (e.g.
fingerpicked vs. bowed/e-bowed) for velocity layers → Tab-to-Transient chop →
RX denoise via a learned noise profile → Melodyne tune → map + velocity-zone in
Kontakt → reverb/delay-BEFORE-saturation insert chain + Transient Master to
soften attacks into a pad.
