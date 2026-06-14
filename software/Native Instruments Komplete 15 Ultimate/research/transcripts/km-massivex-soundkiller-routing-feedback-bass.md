https://www.youtube.com/watch?v=EpS7oVB5MmQ
SoundKiller · Advanced MASSIVE X - Bass Sound Design [TUTORIAL] · 2022-07-10 · 10:42

The best captured walkthrough of Massive X's ROUTING and FEEDBACK — directly relevant to textural/distorted bass walls. Covers LFO loop-restart/sync, phase-modulation %-based ratios (vs octaves), the Monarch double-notch filter, the A/B/C aux-effect slots (3rd oscillator, frequency shifter+crush, distortion), splitting oscillators down separate routing paths (sub vs frequency-shifted high end), the X/Y/Z stereo FX (Dimension Expander, chorus, delay), and turning on FEEDBACK after the filter for piercing self-oscillating tones. Cleaned from auto-subs.

---

Massive X, init patch with some saw. You can select really cool wavetables — e.g. a Vowel table.

LFO basics: create an LFO. It's bipolar by default (goes left and right); you can switch it to unipolar (goes one way). You can set it to sync. Every time you press a key the LFO phase restarts — that's because of "Loop Restart"; turn that on/off as needed. You can select different full shapes. Add LFOs to e.g. the volume.

Phase modulation: enable PM (it can also be modulated). Add white noise. In the Voices, set Reset OFF so the bass always starts with the same sound (so it doesn't change due to phasing). You can change the wavetable of the phase modulation (e.g. Triangle). The PM ratio works as a PERCENTAGE rather than by octave (like Serum / FL): multiple of 1 = 2, multiple of 2 = 4, multiple of 4 = 8, etc. That sounds really cool — the Triangle PM source can sound better than the default.

Filter: there are several filters; each has its own controls. The Monarch has a double-notch filter, which you can also LFO.

Aux effects A/B/C (insert slots): add a THIRD oscillator on A; or frequency shifters with crush, etc. You can route where things go — e.g. send the first utility/oscillators into utility A then into the filter, or the other way around. So if you want frequency shifting before the filter, route it that way. Concrete routing example: put a high-pass utility on A; disable oscillator 1; route oscillator 2 directly in as a sine SUB; put the frequency shifter on B so that ONLY the high end (everything after the high-pass) gets frequency-shifted. Modulate further: add two filters (e.g. add a low-pass) to make a band-pass. On C, put a Distortion (nothing too aggressive).

X/Y/Z stereo effects: the basic effects — e.g. the classic Dimension Expander. You can route oscillator 2 / oscillator B directly to the OUT so none of these stereo effects process it (drag oscillator 2 to the out, set it ~100% serial or ~20%). Add chorus (sounds nice), some delay (note: the delay seemed stuck at 1/16 — possible bug).

FEEDBACK: enable feedback — it takes the sound and puts it back into the feedback loop. In the filter, the feedback goes AFTER the filter back INTO the filter, creating a loop that's awesome for repetitive, very piercing sounds. Boost the volume. Add an LFO. That's a quick in-depth guide — Massive X is very powerful and very different from other VSTs.
