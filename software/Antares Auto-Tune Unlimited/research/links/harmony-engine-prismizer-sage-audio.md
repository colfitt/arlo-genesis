https://www.sageaudio.com/articles/how-to-actually-create-the-prismizer-vocal-effect
Sage Audio · How to (Actually) Create the Prismizer Vocal Effect · n.d.

The single best-documented *artist* technique for Harmony Engine: the **"Prismizer"** — the scattered, voluminous, choir-of-one vocal sound popularized by **Bon Iver (22, A Million), Frank Ocean, and Francis and the Lights** (and their engineer/the "Messina" rig). It IS Antares Harmony Engine driven by MIDI. Distilled:

**Core idea:** insert Harmony Engine as a **MIDI-controlled software instrument** (not a plain audio insert), feed it a clean dry vocal/source via side-chain, and **play the harmony notes from a MIDI keyboard** — the source's timbre is re-pitched to whatever you play, so one held note becomes a played, glassy chord.

**Setup (studio, 11 steps):**
1. Record a clean source — no reverb/comp/processing (anything that blurs pitch makes tracking worse). Minimize breaths/sibilance.
2. Create a **Software Instrument track**; insert Harmony Engine Evo as a **MIDI-controlled effect**.
3. Harmony Source = **MIDI Omni**.
4. Record/print the source sample, then **set the Side-Chain / Input Source to that vocal track** so Harmony Engine knows what audio to re-pitch.
5. Play the harmonies on a MIDI keyboard over playback (Logic: Cmd-K for the on-screen keyboard if no controller). Record the MIDI performance.

**The signature settings:**
- **Glide (transition rate) UP** — "longer glide = it takes longer for notes to change over." The slow portamento between played notes is the defining Prismizer move.
- **Throat Length:** shorter (slider down) = "more artificial/cartoonish," good for higher harmonies; longer (slider up) for lower harmonies. Use per-voice throat to keep the high voices glassy and the low voices bodied.

**Live-performance variant:** same steps 1–5, but **monitor** the input instead of recording it, set side-chain to the **input/live source**, drop the I/O buffer **below 128 samples** to cut latency, and max the processing threads.

**Helpers:** a **Randomizer MIDI FX** to randomize note velocity (1–127) for natural variation; a **Chord Trigger MIDI FX** to play full chords from a single key.

Rig takeaway: this is the documented "build a wall by playing it" method. For the rig: feed a **sustained banjo/baritone/synth drone** as the source, set MIDI Omni, **crank Glide**, and play slow chord changes from the 61SL MkIII — you get the Bon-Iver-style smeared choral wall on an instrument. Then into Valhalla for the tail. (Note: 4 voices = max 4 MIDI notes at once in Omni; use the built-in Choir multiplier to thicken beyond 4.)
