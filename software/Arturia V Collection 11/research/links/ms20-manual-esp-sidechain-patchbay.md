https://dl.arturia.net/products/korg-ms-20-v/manual/korg-ms-20-v_Manual_1_0_2_EN.pdf
Arturia (official) · KORG MS-20 V User Manual v1.0.2 · n.d. (downloaded & text-extracted locally; PDF too large for direct fetch)

THE authoritative source for how external audio actually reaches the MS-20 V and what the ESP does. Distilled from the manual text.

== How external audio gets INTO the plugin (the load-bearing mechanism) ==
Two entry points, both fed by the DAW's audio/sidechain input:

1. **Plugin Audio Settings → Input Channels** (standalone) / **DAW sidechain** (as plugin): "Input Channels let you select which of the available inputs … when you want to route an external audio signal into the MS-20 V. **The Ext Out patchpoint can then be used to route external audio inside the plugin** (e.g. an external signal processor). Only one input or pair of inputs can be selected." → In a DAW you define the source as the plugin's **sidechain input**; it then appears at the **Ext Out** patch point in the patch bay, from which you cable it anywhere (most usefully into the ESP SIGNAL IN).

2. **EXTERNAL IN** patch point (in the main audio path): "an external audio signal input (generally made available within your DAW) that can be mixed with the VCOs before entering the Filters. This jack can also be used to create audio feedbacks within the synth (e.g. Signal Out → External In)." → mixes external audio with the oscillators *pre-filter*.

== The ESP (External Signal Processor) chain — exact order ==
SIGNAL IN → Amplifier (**Signal Level** — set good volume) → Bandpass Filter (**Low Cut Freq** + **High Cut Freq** to strip extreme lows/highs) → tap OUT after Amp or after Bandpass.
Then two parallel analysis paths off the amplified signal:
- **Frequency-to-Voltage (F-V) Converter**: "analyzes the frequency of the incoming signal and creates a control voltage that tracks the pitch" → **F-V CV OUT** (trim with **CV Adjust**). "To control the synth pitch, you can plug F-V CV OUT to VCO 1+2 CV IN."
- **Envelope Follower → ENV OUT**: "creates a voltage based on the loudness it sees." Plus a **TRIG OUT** that fires when the input passes the **Threshold Level**.
Manual's own note: "the ESP requires a great deal of careful playing and pitch stability, but it can produce some truly fun results — and you don't even need an external instrument to use it! It's perfectly happy listening to signals from elsewhere in the synth and processing them. Experiment!"

== The two filters / self-oscillation ==
- "Two resonant VCFs in series: a Highpass (HPF) followed by a Lowpass (LPF). Each has Cutoff Frequency and Peak (resonance)." **LINK** ties the two cutoffs together.
- **MK1 / MK2** filter-circuit models: MK1 = KORG 35 chip ("less subs, more noise, rawer and grittier when distorting but also less screamy" — and CPU-heavier; can cause dropouts/glitches in Poly). MK2 = OTA chip ("more subs and a cleaner, screamier resonance," smoother at high Peak, lighter CPU).
- Peak driven up self-oscillates → pure tone you can play as an oscillator (drone source with no VCO).

== Envelopes (relevant to long evolving tones) ==
- EG1: Delay / Attack / Release; **Trig / Gate / Loop** switch — **Loop turns EG1 into a second LFO** with a custom waveshape (retriggers at end of Release). Times up to ~60–70 s.
- EG2: 5-stage (Hold/Attack/Decay/Sustain/Release), **Classic vs Modern** ranges (Modern is much wider), default-wired to VCA + both filter cutoffs. Modern Decay Curve control.

== Patch-bay extras ==
- **TOTAL** patch = modulate both VCO pitch + both filter cutoffs at once (amount via MG/T.EXT knobs).
- **EG2 SIDECHAIN** = modulate EG2's level with another CV ("that's what a sidechain is").
- S&H is really a track-and-hold; commonly fed by noise for random stepped CV.
- **Master In / Signal Out** patch points (not on original hardware) → internal feedback loops.
- Hidden **Dispersion Controls** (click the KORG logo): 6 trimpots for VCO pitch drift, PW uniformity, envelope, filter cutoff voice-to-voice, resonance alignment, mod stability — 0.00 (perfect) → 1.00 ("totally out-of-whack / as filthy as you want"); snaps back per-preset. → instant analog-drift/"recorded-wrong" character on a poly patch.

== New-vs-hardware (from overview + manual) ==
6-voice polyphony + unison; SQ-10-style 12-step ×3-channel sequencer (Hz or DAW-sync, 8 bars→1/32); 4 FX slots series/parallel (16 effects); ring mod + hard sync; FM module accepts MG / EGs / External Signal.
