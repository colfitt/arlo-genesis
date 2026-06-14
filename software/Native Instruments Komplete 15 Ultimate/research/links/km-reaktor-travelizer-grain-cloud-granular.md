Multiple sources · Travelizer + Grain Cloud — granular-process your own samples
https://www.adsrsounds.com/reaktor-tutorials/granular-synthesis-in-reaktor/  (ADSR · "Granular Synthesis in Reaktor")
https://www.adsrsounds.com/reaktor-tutorials/simple-reaktor-granular-synthesis/  (ADSR · simple version)
(companion to the captured transcript km-reaktor-grain-cloud-build.md)

**Travelizer** = the factory **Sample Transformer** ensemble built around Reaktor's **Grain Cloud module** — the fastest way to granular-process your own audio without building a patch.

- **Loading your own samples:** **double-click the sample window** at the top of the Travelizer interface → opens the **Sample Map** editing tools → load your own audio (drag a batch in, or build a map). The left-hand window selects samples from your hard drive for granular processing.
- **How Grain Cloud works (the key idea, verbatim):** it does NOT play the sample left-to-right start-to-end — instead it "explodes it into a cloud of grains as an **index** that can be moved around however you want." You scrub/freeze the playhead anywhere.
- **Jitter inputs** add random "jumpiness" to: **Pitch, Position, Length, Distance, Pan.** Crank these for evolving, never-repeating clouds; leave them low for a frozen drone.

**Other granular paths in Reaktor:**
- **Grain Cloud module** (Sampler menu) — build it yourself; full control over speed/direction/pitch (see the captured Salamander Anagram transcript for the step-by-step from-scratch build: ramp oscillator → Position, ADSR → amplitude, reverse button, restart-on-note, speed knob).
- **System Flow** (free) and **GRIP** (free, User Library) — pre-built granular front-ends if you don't want to wire Grain Cloud.

Rig recipe (granular-cloud a banjo): load a banjo sample into Travelizer → set **Position Jitter** low + **Length** long for a sustained cloud (or high Jitter for shimmer) → hold a note/chord → high reverb → bounce → into Valhalla VintageVerb / EchoBoy. This is the granular bed under the banjo lead.
