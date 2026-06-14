https://blog.native-instruments.com/5-free-reaktor-tools-for-generative-sequencing/
blog.native-instruments.com · NI Blog · "5 free generative sequencers for REAKTOR"

Free generative-sequencing tools/ensembles (User Library; full Reaktor 6). These are the *engines of randomness* you bolt onto a drone/oscillator to make it self-run.

1. **Squirrel Fishing** — S Bateman. **Four dedicated clock dividers** coax unpredictable melodic patterns from four individual oscillators; built-in reverb + pitch modulation. The cleanest "polyrhythm-from-clock-division" example. → entry 11661.
2. **The Swamp** — Aaron Hemeon. Sci-fi soundscape generator; "load this one up and wait for it to do its thing, or… start twisting knobs." Chaotic autonomous texture. → entry 12005.
3. **Thriller** — hello programchild. "Generative spektral synthesizer" — algorithmic harmonic content with arpeggiator. → entry 3529.
4. **Sort of the Rings** — hello programchild. Physics toy: "triggers a synthesizer with a series of jumping white balls" (X-Y ball physics → pitch sequencing). → entry 2847.
5. **Flip Flop** — Michael Hetrick. Clock-divider-modulated sequencer using **flip-flop logic and sample-and-hold**: a clock divider drives a Flip Flop module — one output controls an on/off switch, the second acts like a **sample & hold** → ever-changing pattern from a static Bento Box sequence. The canonical S&H-randomizer trick. → entry 8951.

**Core generative recipe (verbatim concept):** generate random control data (sample-and-hold, clocked random generators), then tame the randomness back into something musical (note quantizers; coincidentally triggered percussion for accents). That two-step — *randomize then quantize* — is the spine of every generative Blocks patch.
