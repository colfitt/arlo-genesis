https://www.youtube.com/watch?v=Hu9QInXDTGU
Andrew (synth/sound-design channel) · Ableton Live 12 — Drone and Atmospheric Synth Instrument Rack · 2024

> **LITE NOTE (orchestrator-added):** The concept is gold for this rig — a self-evolving
> drone Instrument Rack built on Drift + a reverb whose **Freeze** is pulsed by an LFO.
> Device status: **Drift ✓ (Lite)**, **Reverb ✓ (Lite, has a Freeze button)**,
> **Chorus-Ensemble ✓ (Lite)**, **Instrument Rack + Macros ✓ (Lite)**. The blocking
> exception: the **LFO audio-effect device used to drive the reverb Freeze is a Max for
> Live device → ✗ NOT in Live 12 Lite** (no M4L in Lite at all). The macro-randomization
> trick also relies on heavy macro mapping which works in Lite, but **you cannot
> automate the reverb Freeze with an LFO device in Lite.** Lite workarounds for the
> auto-freeze: (a) **manually toggle / record automation of the Reverb Freeze button**
> while a clip loops, then resample the result; (b) ride Freeze by hand during a Session
> performance; (c) use the clip envelope to draw Freeze on/off. The Drift-rack + macro
> design and the "randomize for new atmospheres" idea are otherwise fully Lite-doable.

## Cleaned transcript

Let's look at how to use **Drift** in Ableton Live to produce an atmospheric/drone synth with simple controls, plus the ability to randomize presets to create unexpected new soundscapes that can be saved with the rack.

**What's playing.** Very slow tempo (~20 BPM-feel), a single **D2 note held for one bar**, looping round and round — that's the only MIDI going to the rack.

**Rack architecture.** A **Drift synth inside an Instrument Rack**, a series of **Macros** mapped to Drift parameters, a **Reverb at the back**, **one LFO**, and a little **chorus** mapped in. The real trick: the LFO controls the **Freeze function inside the Reverb**. When Freeze activates, then deactivates ~every 1.5 bars (set by the LFO rate), each grab captures a new atmosphere; meanwhile Drift's own modulation generates a new sound during playback of the frozen audio. When it releases, you have a new sound and then a new grab — building up evolving atmospheres/drones.

You can set the LFO to a long period (e.g. **32 bars**) so it grabs and holds one freeze for a long time (still altering the sound, but over a frozen reverb), or a shorter range (**2–3 bars**), or quite fast (constantly grabbing new reverb tails). The presenter likes around **2–3 bars**.

**Randomization control.** Some Macros are **excluded from randomization** (right-click → exclude). He doesn't randomize **pitch** too much, keeps the **Reverb** constant, and leaves the **Drone on/off** out so the reverb tail behaves predictably. This gives more certainty about the result when you hit randomize.

**Build (how it's assembled).**
1. **Instrument Rack** → add **Drift**.
2. In Audio Effects add an **LFO** and a **Reverb**; place Reverb between the LFO and Drift. *(LITE: the LFO device is M4L-only — see Lite note.)*
3. **LFO setup:** depth **100%**, **musical/quantized rate**, **Square** wave. You can't map the LFO directly to the reverb Freeze, so map it via a Macro: first map the **Reverb Freeze to a Macro**, then map the **LFO to that Macro**, and set the Macro to 0. Now Freeze flips on/off each square-wave flank (e.g. every 1 bar).
4. **Reverb setup:** **Size 150** (larger), **dry/wet 25**, long **Decay (~20)**, **low-cut ~1 kHz** to trim reverb off the bass. Map Decay and dry/wet to Macros.
5. **Drift mapping:** enable the **cycling envelope** first. Map: **Attack** (range 0–60 s), **filter frequency**, **filter resonance** (lowpass resonance lowered from 101 to ~80 so randomization doesn't create harsh sounds), **osc-1 wave**, **osc-1 shape**, **osc-1 mod amount → LFO**, **osc-2 wave**, **frequency modulation amount**, **osc-2 detune** (tiny, ~0.07 so randomization only adds a small detune). XYZ macro combos add variety (cycling-env rate + tilt on X; hold + LFO rate + noise gain + drift amount on Y; high-pass freq + LFO waveform + osc-2 detune on Z).
6. Settings called out: lowpass min frequency floored at **100 Hz**, **cycling-envelope rate ~6** (low, for a little flavor), **drift amount max 50%** (so it never gets too out of tune).
7. **Exclude from randomization:** Drone on/off, the LFO freeze rate-related macros where noted, Reverb, and Reverb dry/wet.

Result: a Drift drone rack you can re-randomize for endless new atmospheres, each frozen-and-evolving, saved with the rack.
