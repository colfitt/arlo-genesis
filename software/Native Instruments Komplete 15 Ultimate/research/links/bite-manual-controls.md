https://native-instruments.com/ni-tech-manuals/crush-pack-manual/en/bite
native-instruments.com · NI Tech Manual — Crush Pack: BITE · current

# BITE — full control reference (from the manual)

Anti-aliased sample-rate + bit-depth reduction. Confirmed installed on this rig (Bite.component / .vst / .vst3). Also a free standalone NI plugin.

## Exact ranges
- **Freq (resampling frequency):** 0.1 kHz → 44.100 kHz. Drop = lo-fi/aliasing.
- **Depth (bit depth):** 2 bits → 16 bits. Fewer values = more quantization distortion.
- **Crunch:** continuous control over the bit-reduction effect — lowers signal level before quantization so you can dial resolution **smoothly with no stepping/zipper artifacts.**
- **Jitter:** adds fluctuations to the sampling rate (clock jitter) → noisier, more unstable. **Independent left/right** processing → adds stereo width. (The "broken tape" control.)
- **Dither:** noise added to the resampled signal to *reduce* quantization distortion — independent stereo channels; pushable creatively as grit.
- **Pre Filter:** input low-pass, **50 Hz → 22050 Hz**; removes aliasing-prone highs before resampling.
- **Post Filter:** output low-pass, **50 Hz → 22050 Hz**; removes aliasing/ringing after the crush.
- **HP (high-pass):** **5 Hz / 100 Hz / 200 Hz** — removes low-frequency + DC content.
- **DC Mode:** toggle — either sustains the sound with buzzing or allows it to fade to silence.
- **Saturation:** drives the quantized signal into a saturator with automatic loudness compensation.
- **Expand:** changes the quantization distribution — left = more low-level resolution; right = less (clean up vs. dirty up the quiet tail).
- **Mix:** equal-power crossfade dry↔wet.
- Auto in/out gain compensation throughout.

## Notes
No preset names listed in the manual page. Pre/Post filters track the resampling frequency at their middle position = the "authentic vintage sampler" tuning (per the official walkthrough).
