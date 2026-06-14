https://www.sageaudio.com/articles/what-is-the-prismizer-effect-and-can-it-be-used-on-instruments
Sage Audio · What is the Prismizer Effect and Can it Be Used on Instruments? · n.d.

The most useful source for the rig's headline use: Harmony Engine (Prismizer) on **instruments**, not voice. Honest, hands-on findings:

**What works / how well**
- **Guitar:** produces "synth-like to unique tones." Works **better with chords than single notes** per this author (NB: contradicts the general "monophonic only" framing — but they're driving it via MIDI/Chord-Trigger and accepting artifacts as the aesthetic). Unexpected artifacts that "can be introduced **creatively** with some persistence." Watch **phase cancellation** when blending with the original signal.
- **Drums:** "surprisingly well" with percussive MIDI playing — **low keys = gated, '80s Phil-Collins-style** textures; **high keys = melodic, almost a synth triggered by drums.** Muting the original signal makes the effect more pronounced.
- **Strings/violin & piano:** poor — significant distortion, out-of-key/failed harmonies, "sounds like the instrument wasn't struck correctly." The engine can't read those ADSR envelopes/timbres.

**Why non-vocals struggle (the real gotcha):** Harmony Engine is built for vocal timbres; non-vocal **ADSR envelopes** and timbres it "cannot interpret without causing distortion." That distortion IS the texture for an experimental rig, but it's why clean prep matters.

**Signal prep (critical):**
- Input "as **clean as possible**" — **no prior reverb/distortion/delay/compression.**
- **Guitar = DI** (direct in), NOT an amp or amp-modeled signal.
- Don't drive/overdrive the input.
- Set Harmony Source = **MIDI Omni**, side-chain to the instrument track, use **Chord Trigger** for harmonic control.
- Apply effects (reverb/delay/EQ/distortion) **after** harmony generation, on the harmonies.

Rig takeaway: a **clean DI banjo or baritone** (single-note picking or a DI'd drone), Harmony Engine in MIDI Omni, played from the controller, is the sanctioned path. **Mute/lower the dry** to push the synthetic harmony forward, expect glitch/phase artifacts and lean into them, and **print effects only after**. For percussive sources (MPC/Digitakt hits) the low-key gated / high-key melodic trick is a free sound-design move.
