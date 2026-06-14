https://support.spitfireaudio.com/en/collections/14448942-labs
Spitfire Audio Help Centre · LABS plugin + MusicRadar "Fantastic free plugins" + KVR/MusicTech overviews · captured 2026-06

# The LABS plugin — what the controls actually do

LABS runs in **Spitfire's own free player** (NOT Kontakt). It loads as AU/VST/VST3/AAX or standalone. Logic users: Software Instrument track → Spitfire Audio → LABS. The interface is deliberately minimal and identical across every instrument — the genius (and the limit) is that there are only a few controls.

## The three core controls
1. **Expression slider (left).** The "articulation"/expression fader — adds the human touch. Maps to CC11 by default. In long sustained notes, automating expression is how you do SWELLS (the slider is the swell, exactly like riding a fader on a string section).
2. **Dynamics slider (next to it).** Represents how hard each note is "played." It **crossfades between recorded velocity layers** — so it doesn't change WHAT the sound is, it blends softer/louder sampled takes, letting slightly different textures emerge. **Mapped to the mod wheel by default** — push the mod wheel up and the sound gets "bigger"/fuller (you're crossfading into the louder, brighter sample layers). This is the single most important control for evolving textures: ride the mod wheel for living, breathing dynamics on a held chord.
3. **The rotary knob (the "warp"/effects dial).** Defaults to **reverb** on most instruments, but its assignment **changes per instrument** — depending on the patch it may control a different parameter (or expose more than one variable). This is the closest thing to LABS' "warp"/effects page: per-instrument it might be a granular/tone/blend control rather than reverb. Always check what the knob does on the specific patch.

## Notes on architecture
- **Sample-based, not synthesis.** LABS sounds are real instruments sampled (often "recorded wrong" / processed on purpose), which is why they sound rich and have a quirky character. Even the "synth" packs are usually real synths recorded through pedals/outboard, not modeled.
- **Per-instrument extra pages/parameters.** Some instruments expose more than the basic 3 (e.g. extra ADSR-style controls — Release / Sustain / Decay / Attack / Variation appear on textural patches like Arctic Swells; see labs-drones-pads.md transcript). LABS+ era added a built-in in-plugin browser/store to audition & download packs (hover + play to preview) — see labs-walkthrough-plugin.md.
- **Effects beyond the knob = your own chain.** LABS gives you the source + one built-in dial; everything else (the "warp" you want for drone/lo-fi) comes from the DAW chain after it — exactly where this rig's Valhalla / EchoBoy / Decapitator / SketchCassette live.

## Default CC map (handy for the 61SL MkIII)
- Expression → CC11 (ride for swells)
- Dynamics → Mod wheel / CC1 (ride for fullness & brightness crossfade)
- Knob → reverb (or per-instrument param) — assignable/automatable

## Sources
- https://support.spitfireaudio.com/en/collections/14448942-labs
- https://www.musicradar.com/news/fantastic-free-plugins-spitfire-audio-labs
- https://www.kvraudio.com/product/labs-by-spitfire-audio
- https://musictech.com/products/spitfire-audio-labs-software-instrument-plugin/
