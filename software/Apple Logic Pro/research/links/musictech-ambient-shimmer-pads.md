https://musictech.com/tutorials/logic-pro/how-to-create-ambient-shimmer-pads-in-logic-pro-x/
musictech.com · MusicTech tutorial team · (Logic Pro X tutorial)

Full copyable recipe for an ambient shimmer-pad send chain in stock Logic. The centerpiece move = a pre-fader send into a pitch-shift → reverb feedback loop that builds an "octave spiral."

## Source instruments
- **Vintage Electric Piano** patch (primary source for the pad).
- **Alchemy** "Antarctic Sun" soundscape preset, layered underneath for texture.

## The shimmer send chain (on an aux, fed by a PRE-FADER bus send)
All sends in **Pre-Fader** mode so the effect is independent of the instrument fader.

**Pitch Shifter (stock Logic)**
- Transposition: **+12 semitones** (one octave up)
- Mix: **100%**
- Delay: **60 ms**
- Crossfade: **62%**
- Output of the Pitch Shifter routes into the reverb; reverb output is fed back through the pitch shifter → each pass goes up another octave = the "shimmer spiral."

**ChromaVerb**
- Preset: **"Greek Wash"**
- Decay: **30 seconds**
- Width: **100%**
- Alt room types to try: **Synth Hall** (super-wide) or **Bloomy** (rich, dense)
- **Freeze** function is automatable → infinite frozen wash.

**Tape Delay #1 (aux 1)**
- Preset: **"1/4 Note Flutter"**
- Feedback: **0%**
- Dry/Wet: **0% dry / 100% wet**
- Flutter modulation on (pitch-drift)
- Pan: **hard left**

**Tape Delay #2 (aux 2)**
- Copy of #1 but **different Flutter Rate & Intensity**
- Pan: **hard right**
- A bus send feeds back to the original delay, kept **below 0 dB** to avoid self-oscillation.

## Workflow notes
- ~18 steps total: build the source patch → create the pre-fader sends → build pitch/reverb loop → Track Stack → automate the Freeze → bounce/print the printed audio.
- Lift the high end in the reverb's damping/EQ to make it shimmer more.
