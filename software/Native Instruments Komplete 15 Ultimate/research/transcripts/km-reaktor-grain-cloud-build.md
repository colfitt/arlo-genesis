https://www.youtube.com/watch?v=KS5YN4PO9BQ
ADSR Music Production Tutorials (Salamander Anagram / reaktortutorials.com) · NI Reaktor - Setting up the Grain Cloud Module · 2015-03-25

First video of a granular-synthesis series built around Reaktor's **Grain Cloud module** (found in the **Sampler menu** in the Reaktor structure/Core build view). Goal of this patch: a simple Grain Cloud setup giving control over speed, direction, and pitch of sample playback. This is the from-scratch route — the same engine that powers the factory **Travelizer** ensemble, so if you don't want to wire it yourself, load Travelizer and drop your own samples in.

**Building from scratch:**

- Add a **Grain Cloud module** from the Sampler menu. It has a *ton* of inputs and is "one of the most complicated modules in Reaktor," but most inputs have sensible default values, so you only wire the ones you want to control.

- **Give it samples:** open the **Sample Map editor** (upper-right). You can drag-and-drop a batch of files at once from Finder to build a sample map, or load a pre-made map from the Sample Map menu (he loads the map that ships with Ultraloop).

- **Amplitude:** Grain Cloud's amplitude input defaults to **1**, meaning it constantly spits out noise. Control it with an **ADSR envelope module** instead — create knobs for the ADSR inputs and trigger it from the **MIDI Gate**, so the grain engine only sounds while a note is held. (Alternative: drive amplitude from the running MIDI clock to make a groovebox.)

- **G (grain trigger) input:** feed it a **Gate module** so each new MIDI note starts a fresh grain (a short snippet of sound).

- **Select input** (which sample plays): right-click the input → **Create Control** to auto-build a knob with the right range.

- **Position input** (where in the sample grains are grabbed from): drive it with a **Ramp oscillator**. Frequency formula: **(1 / sample-length-in-ms) × 1000**. Set the ramp's **amplitude = the sample length**, so the ramp sweeps 0 → sample-length-ms, feeding the Position input (which expects milliseconds). This makes the grain "playhead" travel through the sample.

- **Pitch from MIDI:** take incoming note pitch, **subtract 60**, add the result to the Select value — so the selected sample plays at original pitch when you play MIDI note 60, and transposes up/down with higher/lower notes. (Each sample's root note governs its original-pitch playback.)

**Enhancements added:**

- **Reverse button:** oscillators accept *negative* frequency and run backwards. Multiply the ramp frequency by a button that = **−1 when on, +1 when off** → the position playhead sweeps backwards while grains still play forward in time, "some pretty cool effects."

- **Restart-on-note:** wire the ramp's **Sync input** to a MIDI Gate so the position resets to the start on each new note; gate it through a **Router module** with a "restart" button so the user can toggle the behaviour.

- **Speed knob:** multiply the ramp frequency by a value 0–2. ×1 = original speed, ×2 = double speed/pitch-up scan, ×0.5 = half-speed scan. (Position scan speed is independent of grain pitch — that's the granular trick.)

Polyphonic by default; remove the voice combiners to go mono. Keeping it poly lets you stack the same sample at different pitches/speeds.

**Why this matters for the rig:** this is the exact mechanism for granular-clouding a banjo sample — load a banjo recording into the sample map, hold a note, and the Grain Cloud freezes/scans it into an evolving cloud. Set a long ADSR release + low scan speed for a sustained drone bed; crank reverb downstream into a wall to sit under banjo.
