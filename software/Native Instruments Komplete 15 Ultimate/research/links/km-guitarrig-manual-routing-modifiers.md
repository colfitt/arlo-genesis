https://native-instruments.com/ni-tech-manuals/guitar-rig-manual/en/tools-components.html
+ https://www.native-instruments.com/ni-tech-manuals/guitar-rig-manual/en/modifiers
Guitar Rig 7 manual — Tools Components + Modifiers (authoritative reference)

The authoritative source on GR's modular routing — what makes it a true FX rack, not a fixed amp chain.

## Routing / splitter Tools
- **Container** — group multiple components into one reusable multi-effect, controlled by up to **16 Container Macros**. "Organize your Rack more clearly, or conveniently reuse your favorite combinations of effects." (This is the building block for parallel sub-chains and macro-controlled mega-effects.)
- **Split Mix** — the core **parallel splitter**: feeds input into **two independent chains (A and B)**; add components to each path independently; freely adjust **pan + mix/blend** of the two paths before output. Includes **L/R (stereo channel) split** mode and **phase inversion**. (= in-box parallel processing, no aux send needed — like Decapitator's Mix but for entire sub-chains.)
- **Crossover Mix** — **frequency-split** (multiband): divides the spectrum into **Low and High bands** at an adjustable crossover frequency, with independent effect chains per band, per-band pan, and crossfade blend. (= distort/saturate only the highs while keeping lows clean — a cleaner alternative to Color's Bass Saver for multiband work.)
- **Split M/S** — **mid/side** processor: separates mid (shared/correlated) from side (decorrelated/stereo-difference) info, with range control + solo. (= mid/side reverb/EQ/saturation, e.g. widen a pad without smearing the centre.)
- **Loop Machine Pro** — multi-layer looper: A/B, half/normal/double speed, reverse, export.

## Modifiers (modulation sources)
Modifiers don't make/process sound — they **automatically drive any control in the Rack over time**. Assign any Modifier to any parameter:
- **LFO** — subsonic periodic waveform for constantly-changing values (e.g. assign to **Split Mix blend = auto-panner**, or to a filter cutoff, reverb size, delay time, pan, etc.).
- Also: **Envelope** (input-level-following), **Step Sequencer**, **input signal** as a modifier, and more.
"You can use them to control any parameter you want in any effect or amp in your rig." (The Beyond-Guitar video's sequencer-driven Beat Slicers + Gator are this system in action.)

## Why this matters for a degraded/drone rig
GR is fully modular: you can build **parallel grit + clean** (Split Mix), **multiband degrade** (Crossover), **mid/side wash** (Split M/S), **macro-controlled super-effects** (Container), and **automate chaos** (LFO/Envelope/Sequencer on any knob) — all inside one plugin instance on a send or insert. This is the structural argument for reaching for GR as an all-in-one creative rack rather than chaining many single-purpose plugins.
