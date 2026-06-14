https://www.youtube.com/watch?v=1iW9gzNy6BM
VoltageCtrlRtv (Shiro Fujioka / audiblealchemy.org) · Reaktor 6 Blocks Polyrhythmic Patch Tutorial + free ensemble · 2016-08-20

Walkthrough of a generative **Reaktor 6 Blocks** patch by Shiro Fujioka (the author behind the "VoltageCntrl-We Rise" User Library ensemble). Frames the patch as "auditory paint-by-numbers" — looks complex, reads simply once you trace the signal. This is a clean reference for how to wire a self-running generative Blocks patch.

**The signal flow (the generative spine):**

- **Clock module** = the pulse/tempo of the patch. → patched into the **Clock Divider**, which yields divisions of the master clock.
- One clock-divider division **clocks the Random Gates module**.
- **Random Gates** → into the **CFG** (West Coast Complex Function Generator), used here as a **quad envelope generator** → into the **dual mixable Low-Pass Gate** and also into a **VCA**. (This is what gives the random, plucked/bloom dynamics.)
- A **Quad Modulation source** (four modulators, four outputs): one output → into the **Quantizer**, which "dials in the pitches/notes of the patch." Quantizer → into the **DWG (Dual Waveform Generator)**, the sound source. The DWG plays the notes and feeds the **dual Low-Pass Gate** and the **VCA**.
- DWG's **Timbre out** → into a **Ring Mod**; the DWG's **Modulator out** also → into the Ring Mod (cross-modulation for grit/metallic tones).
- An **LFO** is clocked by a division of the Clock Divider (kept in sync with the patch pulse); it modulates different divisions/multiplications of the Clock Divider — this is what creates the **polyrhythm**.
- The **Quad Modulation source** also feeds the **CVP (Control Voltage Processor)** → into the Quantizer, to modulate quantizer parameters (shifting the note set over time).
- A **Quad LFO** modulates the dual Low-Pass Gate mixer, the Ring Mod, and the Reverb.
- Everything sums into a **4-channel Mixer** → **Reverb** → out to speakers. (In the downloaded version the reverb goes straight to the output; in the video an extra mixer is inserted only so he can add mic/voice.)
- A **MIDI out** block is present to send pitch+gate to external gear (modular synth / analog keyboard) — covered in a later tutorial.

**Performance / variation:** he steps through **Snapshots** to show the patch's range — one snapshot uses an LFO to modulate reverb **diffusion, size, feedback, low-pass, and wet/dry**; another changes the **Clock** rate (e.g. from 64) to reshape the rhythm. Free ensemble downloadable from the Reaktor User Library.

**Takeaway recipe (generative Blocks):** Clock → Clock Divider → (Random Gates → CFG envelopes) for dynamics, plus (Quad Mod → Quantizer → DWG) for pitched notes, cross-feed via Ring Mod, sync an LFO off a clock division for polyrhythm, sum → Reverb. Slow the Clock and stretch the CFG envelopes and it becomes a generative drone/ambient bed rather than a sequence.
