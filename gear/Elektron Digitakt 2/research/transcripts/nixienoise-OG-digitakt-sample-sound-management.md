https://www.youtube.com/watch?v=UwnXAs66B7k
Nixienoise · All about Digitakt sample and sound management: A deep dive! · 2024-06-18

> Source captions: YouTube auto-generated, cleaned to prose. ~13m.
> ⚠️ **OG DIGITAKT (Mark 1), NOT the DT2.** The presenter explicitly cites OG numbers: "64 megabytes of memory ≈ 14.5 min", "127 samples", "8 sample tracks + 8 MIDI tracks", "8 banks × 256 sound slots". Captured because the **sample/sound/kit hierarchy and the sound-browser/sound-pool concepts transfer to the DT2** — but the *numbers and some menu specifics differ*. DT2-correct figures are flagged inline.

## The storage hierarchy (concept transfers to DT2)
Project → Patterns (organized into **banks**, 8 banks × 16 patterns) → Tracks → (Sound = sample + all params) → Sample.
- OG: 8 sample + 8 MIDI tracks. **DT2: 16 tracks, each freely audio or MIDI.**
- Song mode (optional) organizes patterns into a song with per-track mutes.
- A track isn't *just* a sample — you can p-lock a different **sample** or a whole **sound** to an individual step (hold a step, turn the data knob).

## Saving / restoring
- Save the whole pattern to the project; or save **kit data** and **sequence data** independently (so you can restore one if you mess up).
- **Temporary pattern area**: FUNC + SAVE pattern / FUNC + RELOAD pattern — save/restore a safe state mid-performance. (Same on DT2.)

## Getting samples in
- Settings → **Samples**: shows loaded samples, or press left to view the **+Drive** (internal storage) file browser. Check samples (YES = checkmark), right-arrow for batch ops (select all / deselect / delete / move), then **Load to Project**.
- OG RAM: "64 MB ≈ 14.5 min over 127 samples". **DT2: 400 MB RAM, ~1016 usable sample slots, 8 banks of sample slots.**
- View RAM: Samples menu → left → **View RAM**. Free space: Settings → System → Storage.

## Sounds & the sound browser (concept transfers; OG slot counts differ)
- A **sound** = a track's full settings (sample + filter + LFO + FX) saved for reuse across patterns/projects.
- **Sound browser**: FUNC + push data knob (yellow "sound browser" label). On a fresh box it says "the +Drive has no sounds".
- **Export a sound**: Settings → Pattern → Import/Export → **Export Sound** → choose a slot ("8 banks × 256 = 2048 slots" on OG; DT2 = 2048 presets), name it, add **search tags** (e.g. synth, loop, atmospheric), save.
- FUNC + YES previews a sound in the browser.
- **Sounds live on the +Drive, not in the project pool.** To use one in a pattern: Settings → Import/Export → **Import Sound** (into a track), or **Manage Sounds** → select → **Copy To → Soundpool**. Then the sound shows up in **View Pool** in the sound browser.
- **Sound pool use**: on a track, hold a step + turn the data knob to pick a pool sound for that step (sound-lock), then further p-lock its other params. This is the same sound-lock/preset-lock idea the DT2 calls the **preset pool** (see cuckoo + xnb transcripts) — on DT2 you "add presets to the pool" then hold a trig + level encoder.
- Cross-project reuse: the sound browser lets you pull a saved sound into a brand-new project.
- The presenter notes **the Mark 2 (DT2) also lets you save the entire set of 16 tracks as a kit** to recall in another pattern/project — the OG (this video) does not.

Bottom line for DT2 users: trust the *workflow* (export sound → tag → manage → copy to pool → sound-lock per step; load samples to project; free RAM via select-unused), but use DT2's larger figures (400 MB RAM, 20 GB +Drive, 1016 sample slots, 2048 presets, 16 audio/MIDI tracks) and DT2's "preset pool" terminology.
